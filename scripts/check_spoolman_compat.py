"""Validate compiled data against Spoolman's current external DB contract."""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
import json
import sys
import time
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).parent.parent
DEFAULT_UPSTREAM_URL = (
    "https://raw.githubusercontent.com/Donkie/Spoolman/"
    "master/spoolman/externaldb.py"
)
ENUM_CLASS_NAMES = {
    "SpoolType",
    "Finish",
    "MultiColorDirection",
    "Pattern",
}
MODEL_CLASS_NAME = "ExternalFilament"
ROOT_MODEL_CLASS_NAME = "ExternalFilamentsFile"
PRIMITIVE_TYPES = {"str", "float", "int", "bool", "Any"}
MAX_UPSTREAM_BYTES = 1_000_000


@dataclass(frozen=True)
class FieldContract:
    annotation: ast.expr
    required: bool


@dataclass(frozen=True)
class SpoolmanContract:
    enum_values: dict[str, frozenset[str]]
    fields: dict[str, FieldContract]


def fetch_upstream_source(
    url: str,
    *,
    attempts: int = 3,
    timeout: int = 30,
) -> tuple[str, str | None]:
    """Fetch the authoritative upstream model with bounded retries."""
    last_error: Exception | None = None
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "SpoolmanDB-Community-compat-check"},
    )

    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                payload = response.read(MAX_UPSTREAM_BYTES + 1)
                if len(payload) > MAX_UPSTREAM_BYTES:
                    raise RuntimeError("Upstream contract source is unexpectedly large")
                source = payload.decode("utf-8")
                return source, response.headers.get("ETag")
        except Exception as exc:  # pragma: no cover - exact network errors vary
            last_error = exc
            if attempt < attempts:
                time.sleep(attempt)

    raise RuntimeError(
        f"Unable to fetch Spoolman contract after {attempts} attempts: {last_error}"
    )


def _extract_enum_values(node: ast.ClassDef) -> frozenset[str]:
    if node.decorator_list or not (
        len(node.bases) == 1
        and isinstance(node.bases[0], ast.Name)
        and node.bases[0].id == "Enum"
    ):
        raise RuntimeError(f"Upstream {node.name} enum structure changed")

    values: set[str] = set()
    for child in node.body:
        if (
            isinstance(child, ast.Expr)
            and isinstance(child.value, ast.Constant)
            and isinstance(child.value.value, str)
        ):
            continue
        if not isinstance(child, ast.Assign):
            raise RuntimeError(f"Unsupported statement in upstream {node.name}")
        if (
            len(child.targets) != 1
            or not isinstance(child.targets[0], ast.Name)
            or not isinstance(child.value, ast.Constant)
            or not isinstance(child.value.value, str)
        ):
            raise RuntimeError(
                f"Unsupported dynamic enum member in upstream {node.name}"
            )
        values.add(child.value.value)

    if not values:
        raise RuntimeError(f"No values found in upstream {node.name}")
    return frozenset(values)


def _is_field_call(value: ast.expr) -> bool:
    if not isinstance(value, ast.Call):
        return False
    if isinstance(value.func, ast.Name):
        return value.func.id == "Field"
    return isinstance(value.func, ast.Attribute) and value.func.attr == "Field"


def _is_ellipsis(value: ast.expr) -> bool:
    return isinstance(value, ast.Constant) and value.value is Ellipsis


def _is_reviewed_default(value: ast.expr) -> bool:
    if not isinstance(value, ast.Constant):
        return False
    return (
        value.value is None
        or value.value is Ellipsis
        or value.value is False
        or value.value is True
    )


def _validate_field_definition(value: ast.expr | None, field_name: str) -> None:
    if value is None or not _is_field_call(value):
        raise RuntimeError(
            f"Upstream field {field_name} no longer uses the reviewed Field contract"
        )

    assert isinstance(value, ast.Call)
    if len(value.args) > 1:
        raise RuntimeError(f"Upstream field {field_name} has unexpected Field arguments")
    if value.args and not _is_reviewed_default(value.args[0]):
        raise RuntimeError(f"Upstream field {field_name} has a dynamic default")
    allowed_keywords = {"default", "description", "examples"}
    unexpected = {
        keyword.arg for keyword in value.keywords if keyword.arg not in allowed_keywords
    }
    if unexpected:
        raise RuntimeError(
            f"Upstream field {field_name} added validation options: "
            + ", ".join(sorted(str(item) for item in unexpected))
        )
    for keyword in value.keywords:
        if keyword.arg == "default" and not _is_reviewed_default(keyword.value):
            raise RuntimeError(f"Upstream field {field_name} has a dynamic default")


def _field_is_required(value: ast.expr | None) -> bool:
    if value is None:
        return True
    if not _is_field_call(value):
        return False

    assert isinstance(value, ast.Call)
    if value.args:
        return _is_ellipsis(value.args[0])
    for keyword in value.keywords:
        if keyword.arg == "default":
            return _is_ellipsis(keyword.value)
        if keyword.arg == "default_factory":
            return False
    return True


def _assert_supported_annotation(
    annotation: ast.expr,
    enum_names: set[str],
) -> None:
    if isinstance(annotation, ast.Name):
        if annotation.id in PRIMITIVE_TYPES | enum_names | {MODEL_CLASS_NAME}:
            return
    elif isinstance(annotation, ast.Constant) and annotation.value is None:
        return
    elif isinstance(annotation, ast.BinOp) and isinstance(annotation.op, ast.BitOr):
        _assert_supported_annotation(annotation.left, enum_names)
        _assert_supported_annotation(annotation.right, enum_names)
        return
    elif (
        isinstance(annotation, ast.Subscript)
        and isinstance(annotation.value, ast.Name)
        and annotation.value.id == "list"
    ):
        _assert_supported_annotation(annotation.slice, enum_names)
        return

    raise RuntimeError(
        "Unsupported upstream type annotation: " + ast.unparse(annotation)
    )


def load_spoolman_contract(source: str) -> SpoolmanContract:
    """Parse the upstream contract statically without executing downloaded code."""
    parsed = ast.parse(source)
    classes = {
        node.name: node for node in parsed.body if isinstance(node, ast.ClassDef)
    }
    required_classes = ENUM_CLASS_NAMES | {
        MODEL_CLASS_NAME,
        ROOT_MODEL_CLASS_NAME,
    }
    missing = required_classes - classes.keys()
    if missing:
        raise RuntimeError(
            "Spoolman external DB contract changed; missing classes: "
            + ", ".join(sorted(missing))
        )

    enum_values = {
        name: _extract_enum_values(classes[name]) for name in ENUM_CLASS_NAMES
    }
    model_class = classes[MODEL_CLASS_NAME]
    if model_class.decorator_list or not (
        len(model_class.bases) == 1
        and isinstance(model_class.bases[0], ast.Name)
        and model_class.bases[0].id == "BaseModel"
    ):
        raise RuntimeError(f"Upstream {MODEL_CLASS_NAME} base or decorators changed")

    fields: dict[str, FieldContract] = {}
    for child in model_class.body:
        if (
            isinstance(child, ast.Expr)
            and isinstance(child.value, ast.Constant)
            and isinstance(child.value.value, str)
        ):
            continue
        if not isinstance(child, ast.AnnAssign) or not isinstance(child.target, ast.Name):
            raise RuntimeError(
                f"Unsupported statement in upstream {MODEL_CLASS_NAME}; manual review required"
            )
        _validate_field_definition(child.value, child.target.id)
        _assert_supported_annotation(child.annotation, set(enum_values))
        fields[child.target.id] = FieldContract(
            annotation=child.annotation,
            required=_field_is_required(child.value),
        )

    if not fields:
        raise RuntimeError(f"No fields found in upstream {MODEL_CLASS_NAME}")

    root_class = classes[ROOT_MODEL_CLASS_NAME]
    if root_class.decorator_list or not (
        len(root_class.bases) == 1
        and isinstance(root_class.bases[0], ast.Name)
        and root_class.bases[0].id == "RootModel"
    ):
        raise RuntimeError(f"Upstream {ROOT_MODEL_CLASS_NAME} base or decorators changed")

    root_fields: list[ast.AnnAssign] = []
    for child in root_class.body:
        if (
            isinstance(child, ast.AnnAssign)
            and isinstance(child.target, ast.Name)
            and child.target.id == "root"
        ):
            root_fields.append(child)
        elif isinstance(child, ast.FunctionDef) and child.name in {
            "__iter__",
            "__getitem__",
        }:
            continue
        elif (
            isinstance(child, ast.Expr)
            and isinstance(child.value, ast.Constant)
            and isinstance(child.value.value, str)
        ):
            continue
        else:
            raise RuntimeError(
                f"Unsupported statement in upstream {ROOT_MODEL_CLASS_NAME}; "
                "manual review required"
            )
    if len(root_fields) != 1:
        raise RuntimeError("Upstream ExternalFilamentsFile.root contract changed")
    root_annotation = root_fields[0].annotation
    _assert_supported_annotation(root_annotation, set(enum_values))
    if not (
        isinstance(root_annotation, ast.Subscript)
        and isinstance(root_annotation.value, ast.Name)
        and root_annotation.value.id == "list"
        and isinstance(root_annotation.slice, ast.Name)
        and root_annotation.slice.id == MODEL_CLASS_NAME
    ):
        raise RuntimeError("Upstream ExternalFilamentsFile.root is no longer a list")

    return SpoolmanContract(enum_values=enum_values, fields=fields)


def _matches_annotation(
    value: Any,
    annotation: ast.expr,
    contract: SpoolmanContract,
) -> bool:
    if isinstance(annotation, ast.BinOp) and isinstance(annotation.op, ast.BitOr):
        return _matches_annotation(
            value, annotation.left, contract
        ) or _matches_annotation(value, annotation.right, contract)
    if isinstance(annotation, ast.Constant) and annotation.value is None:
        return value is None
    if isinstance(annotation, ast.Subscript):
        return isinstance(value, list) and all(
            _matches_annotation(item, annotation.slice, contract) for item in value
        )
    if not isinstance(annotation, ast.Name):
        return False

    type_name = annotation.id
    if type_name in contract.enum_values:
        return isinstance(value, str) and value in contract.enum_values[type_name]
    if type_name == "Any":
        return True
    if type_name == "str":
        return isinstance(value, str)
    if type_name == "bool":
        return isinstance(value, bool)
    if type_name == "int":
        return isinstance(value, int) and not isinstance(value, bool)
    if type_name == "float":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return False


def validate_schema_spool_types(
    schema: dict[str, Any],
    contract: SpoolmanContract,
) -> None:
    """Ensure every value our compiled schema permits is accepted by Spoolman."""
    schema_enum = schema["items"]["properties"]["spool_type"]["enum"]
    spool_field = contract.fields.get("spool_type")
    if spool_field is None:
        raise RuntimeError("Upstream ExternalFilament no longer defines spool_type")
    unsupported = [
        value
        for value in schema_enum
        if not _matches_annotation(value, spool_field.annotation, contract)
    ]

    if unsupported:
        raise RuntimeError(
            "Compiled schema permits spool_type values rejected by Spoolman: "
            + ", ".join(repr(value) for value in unsupported)
        )


def validate_compiled_data(
    compiled_data: list[dict[str, Any]],
    contract: SpoolmanContract,
) -> None:
    """Validate known fields in every record against the live upstream AST contract."""
    if not isinstance(compiled_data, list):
        raise RuntimeError("Compiled filament data must be a list")

    for index, record in enumerate(compiled_data):
        if not isinstance(record, dict):
            raise RuntimeError(f"Compiled record {index} must be an object")
        record_id = record.get("id", "<missing id>")
        for name, field in contract.fields.items():
            if name not in record:
                if field.required:
                    raise RuntimeError(
                        f"Record {index} ({record_id}) is missing required field {name}"
                    )
                continue
            if not _matches_annotation(record[name], field.annotation, contract):
                raise RuntimeError(
                    f"Record {index} ({record_id}) has incompatible {name}: "
                    f"expected {ast.unparse(field.annotation)}, got {record[name]!r}"
                )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check compiled filaments against Spoolman's current external DB contract."
    )
    parser.add_argument(
        "--compiled",
        type=Path,
        default=ROOT / "filaments.json",
        help="Path to compiled filaments.json.",
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=ROOT / "filaments.compiled.schema.json",
        help="Path to the compiled JSON schema.",
    )
    source_group = parser.add_mutually_exclusive_group()
    source_group.add_argument(
        "--upstream-url",
        help=(
            "Raw URL for Spoolman's authoritative externaldb.py model. "
            "Defaults to the current upstream branch."
        ),
    )
    source_group.add_argument(
        "--upstream-file",
        type=Path,
        help="Reviewed local externaldb.py contract snapshot for offline validation.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if not args.compiled.exists():
        print(
            f"ERROR: {args.compiled} does not exist; run compile_filaments.py first.",
            file=sys.stderr,
        )
        return 1

    try:
        if args.upstream_file:
            source = args.upstream_file.read_text(encoding="utf-8")
            etag = None
            source_label = str(args.upstream_file)
        else:
            source_url = args.upstream_url or DEFAULT_UPSTREAM_URL
            source, etag = fetch_upstream_source(source_url)
            source_label = source_url
        contract = load_spoolman_contract(source)

        with args.schema.open(encoding="utf-8") as file:
            schema = json.load(file)
        with args.compiled.open(encoding="utf-8") as file:
            compiled_data = json.load(file)

        validate_schema_spool_types(schema, contract)
        validate_compiled_data(compiled_data, contract)
    except Exception as exc:
        print(f"ERROR: Spoolman compatibility check failed: {exc}", file=sys.stderr)
        return 1

    source_version = f" (ETag {etag})" if etag else ""
    print(f"✓ Upstream contract: {source_label}{source_version}")
    print(
        f"✓ Statically checked {len(contract.fields)} upstream fields; "
        "contract source was not executed."
    )
    print(f"✓ {len(compiled_data)} compiled filaments accepted by the contract.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
