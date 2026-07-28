"""Validate compiled data against Spoolman's external DB contract.

Upstream refs are configured only in contracts/spoolman_upstream.json:

- stable  (required): pinned Spoolman release / commit; blocks merge
- canary  (advisory): current master; reports ExternalFilament drift

Stable mode uses the reviewed local snapshot by default (deterministic, offline).
Canary mode fetches master and compares ExternalFilament fields/types to stable.
"""

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
UPSTREAM_CONFIG_PATH = ROOT / "contracts" / "spoolman_upstream.json"
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


@dataclass(frozen=True)
class UpstreamConfig:
    repository: str
    contract_path: str
    local_snapshot: Path
    stable_version: str
    stable_commit: str
    canary_ref: str

    def raw_url(self, ref: str) -> str:
        return (
            f"https://raw.githubusercontent.com/{self.repository}/"
            f"{ref}/{self.contract_path}"
        )

    @property
    def stable_url(self) -> str:
        return self.raw_url(self.stable_commit)

    @property
    def canary_url(self) -> str:
        return self.raw_url(self.canary_ref)

    @property
    def stable_blob_url(self) -> str:
        return (
            f"https://github.com/{self.repository}/blob/"
            f"{self.stable_commit}/{self.contract_path}"
        )


@dataclass(frozen=True)
class FieldChange:
    """One ExternalFilament field/type difference between two contracts."""

    field: str
    kind: str
    stable: str | None
    canary: str | None

    def format(self) -> str:
        if self.kind == "added":
            return f"+ {self.field}: {self.canary} (present on canary only)"
        if self.kind == "removed":
            return f"- {self.field}: {self.stable} (present on stable only)"
        if self.kind == "type_changed":
            return f"~ {self.field}: type {self.stable} -> {self.canary}"
        if self.kind == "required_changed":
            return (
                f"~ {self.field}: required {self.stable} -> {self.canary}"
            )
        return f"? {self.field}: {self.kind} ({self.stable} -> {self.canary})"


def load_upstream_config(path: Path = UPSTREAM_CONFIG_PATH) -> UpstreamConfig:
    """Load the single upstream pin / canary configuration file."""
    if not path.is_file():
        raise RuntimeError(f"Missing Spoolman upstream config: {path}")

    with path.open(encoding="utf-8") as file:
        raw = json.load(file)

    try:
        stable = raw["stable"]
        canary = raw["canary"]
        return UpstreamConfig(
            repository=raw["repository"],
            contract_path=raw["contract_path"],
            local_snapshot=(ROOT / raw["local_snapshot"]).resolve(),
            stable_version=stable["version"],
            stable_commit=stable["commit"],
            canary_ref=canary["ref"],
        )
    except (KeyError, TypeError) as exc:
        raise RuntimeError(
            f"Invalid Spoolman upstream config in {path}: missing {exc}"
        ) from exc


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


def field_signature(field: FieldContract) -> str:
    """Human-readable type signature for an ExternalFilament field."""
    required = "required" if field.required else "optional"
    return f"{ast.unparse(field.annotation)} ({required})"


def compare_external_filament_fields(
    stable: SpoolmanContract,
    canary: SpoolmanContract,
) -> list[FieldChange]:
    """Report exact ExternalFilament field/type changes between two contracts."""
    changes: list[FieldChange] = []
    stable_names = set(stable.fields)
    canary_names = set(canary.fields)

    for name in sorted(canary_names - stable_names):
        changes.append(
            FieldChange(
                field=name,
                kind="added",
                stable=None,
                canary=field_signature(canary.fields[name]),
            )
        )
    for name in sorted(stable_names - canary_names):
        changes.append(
            FieldChange(
                field=name,
                kind="removed",
                stable=field_signature(stable.fields[name]),
                canary=None,
            )
        )
    for name in sorted(stable_names & canary_names):
        left = stable.fields[name]
        right = canary.fields[name]
        left_type = ast.unparse(left.annotation)
        right_type = ast.unparse(right.annotation)
        if left_type != right_type:
            changes.append(
                FieldChange(
                    field=name,
                    kind="type_changed",
                    stable=left_type,
                    canary=right_type,
                )
            )
        if left.required != right.required:
            changes.append(
                FieldChange(
                    field=name,
                    kind="required_changed",
                    stable="required" if left.required else "optional",
                    canary="required" if right.required else "optional",
                )
            )

    for enum_name in sorted(ENUM_CLASS_NAMES):
        left_values = stable.enum_values.get(enum_name, frozenset())
        right_values = canary.enum_values.get(enum_name, frozenset())
        if left_values == right_values:
            continue
        added = sorted(right_values - left_values)
        removed = sorted(left_values - right_values)
        if added:
            changes.append(
                FieldChange(
                    field=f"enum:{enum_name}",
                    kind="added",
                    stable=None,
                    canary=", ".join(added),
                )
            )
        if removed:
            changes.append(
                FieldChange(
                    field=f"enum:{enum_name}",
                    kind="removed",
                    stable=", ".join(removed),
                    canary=None,
                )
            )

    return changes


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


def resolve_contract_source(
    *,
    mode: str,
    config: UpstreamConfig,
    upstream_url: str | None,
    upstream_file: Path | None,
) -> tuple[str, str, str | None]:
    """Return (source_text, source_label, etag) for the selected mode."""
    if upstream_file is not None:
        source = upstream_file.read_text(encoding="utf-8")
        return source, str(upstream_file), None

    if upstream_url is not None:
        source, etag = fetch_upstream_source(upstream_url)
        return source, upstream_url, etag

    if mode == "stable":
        # Deterministic offline path: reviewed snapshot pinned in config.
        snapshot = config.local_snapshot
        if not snapshot.is_file():
            raise RuntimeError(
                f"Stable snapshot missing at {snapshot}; expected pin "
                f"{config.stable_version} ({config.stable_commit})"
            )
        source = snapshot.read_text(encoding="utf-8")
        label = (
            f"{snapshot} [stable {config.stable_version} "
            f"@ {config.stable_commit}]"
        )
        return source, label, None

    if mode == "canary":
        source, etag = fetch_upstream_source(config.canary_url)
        label = (
            f"{config.canary_url} [canary {config.repository}:"
            f"{config.canary_ref}]"
        )
        return source, label, etag

    raise RuntimeError(f"Unknown compatibility mode: {mode}")


def load_stable_contract(config: UpstreamConfig) -> SpoolmanContract:
    """Load the deterministic stable (pinned) contract from the local snapshot."""
    source = config.local_snapshot.read_text(encoding="utf-8")
    return load_spoolman_contract(source)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Check compiled filaments against Spoolman's external DB contract. "
            "Stable pin and canary ref live in contracts/spoolman_upstream.json."
        )
    )
    parser.add_argument(
        "--mode",
        choices=("stable", "canary"),
        default="stable",
        help=(
            "stable: required pin from contracts/spoolman_upstream.json "
            "(default, offline snapshot). "
            "canary: advisory check against Donkie/Spoolman master plus "
            "ExternalFilament field/type drift report vs stable."
        ),
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
    parser.add_argument(
        "--config",
        type=Path,
        default=UPSTREAM_CONFIG_PATH,
        help="Path to the Spoolman upstream pin config JSON.",
    )
    source_group = parser.add_mutually_exclusive_group()
    source_group.add_argument(
        "--upstream-url",
        help=(
            "Override raw URL for Spoolman's externaldb.py model. "
            "When omitted, stable uses the local snapshot and canary uses "
            "the canary ref from the config file."
        ),
    )
    source_group.add_argument(
        "--upstream-file",
        type=Path,
        help="Reviewed local externaldb.py contract snapshot for offline validation.",
    )
    parser.add_argument(
        "--diff-only",
        action="store_true",
        help=(
            "In canary mode, only compare ExternalFilament fields/types to "
            "stable and skip compiled data validation."
        ),
    )
    return parser.parse_args(argv)


def run_check(args: argparse.Namespace) -> int:
    config = load_upstream_config(args.config)

    if not args.compiled.exists() and not args.diff_only:
        print(
            f"ERROR: {args.compiled} does not exist; run compile_filaments.py first.",
            file=sys.stderr,
        )
        return 1

    try:
        source, source_label, etag = resolve_contract_source(
            mode=args.mode,
            config=config,
            upstream_url=args.upstream_url,
            upstream_file=args.upstream_file,
        )
        contract = load_spoolman_contract(source)

        field_changes: list[FieldChange] = []
        if args.mode == "canary":
            stable_contract = load_stable_contract(config)
            field_changes = compare_external_filament_fields(
                stable_contract, contract
            )

        if not args.diff_only:
            with args.schema.open(encoding="utf-8") as file:
                schema = json.load(file)
            with args.compiled.open(encoding="utf-8") as file:
                compiled_data = json.load(file)

            validate_schema_spool_types(schema, contract)
            validate_compiled_data(compiled_data, contract)
        else:
            compiled_data = []
    except Exception as exc:
        print(f"ERROR: Spoolman compatibility check failed: {exc}", file=sys.stderr)
        return 1

    mode_label = args.mode.upper()
    source_version = f" (ETag {etag})" if etag else ""
    print(f"✓ Mode: {mode_label}")
    if args.mode == "stable":
        print(
            f"✓ Stable pin: {config.stable_version} "
            f"({config.stable_commit})"
        )
        print(f"✓ Stable blob: {config.stable_blob_url}")
    else:
        print(
            f"✓ Canary ref: {config.repository}:{config.canary_ref}"
        )
        print(
            f"✓ Compared to stable: {config.stable_version} "
            f"({config.stable_commit})"
        )
    print(f"✓ Upstream contract: {source_label}{source_version}")
    print(
        f"✓ Statically checked {len(contract.fields)} upstream fields; "
        "contract source was not executed."
    )
    if not args.diff_only:
        print(f"✓ {len(compiled_data)} compiled filaments accepted by the contract.")

    if args.mode == "canary":
        if field_changes:
            print(
                "⚠ CANARY DRIFT: ExternalFilament fields/types differ "
                "between stable pin and master:",
                file=sys.stderr,
            )
            for change in field_changes:
                print(f"  {change.format()}", file=sys.stderr)
            print(
                "CANARY: drift detected "
                f"({len(field_changes)} change(s)). "
                "This is advisory and does not block data PRs.",
                file=sys.stderr,
            )
            return 2
        print(
            "✓ CANARY: no ExternalFilament field/type drift vs stable pin."
        )

    return 0


def main(argv: list[str] | None = None) -> int:
    return run_check(parse_args(argv))


if __name__ == "__main__":
    raise SystemExit(main())
