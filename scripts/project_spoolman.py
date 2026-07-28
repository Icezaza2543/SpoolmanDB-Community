"""Script and library to project Community compiled filament records to Spoolman-native fields only.

Note on Architecture & Intent:
This module provides a deterministic projection layer for architectural preparedness in case
a future Spoolman release enforces strict contract field parsing (rejecting extra/unknown fields).
It is NOT a claim that current Spoolman releases require a stripped export, nor does it alter
the primary rich 'filaments.json' artifact published by SpoolmanDB-Community.
"""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import sys
from typing import Any, Dict, List, Sequence

ROOT = Path(__file__).parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.check_spoolman_compat import (
    load_spoolman_contract,
    load_upstream_config,
    SpoolmanContract,
)

FILAMENTS_JSON_PATH = ROOT / "filaments.json"


def get_native_contract(config_path: Path | None = None) -> SpoolmanContract:
    """Load and parse the pinned Spoolman contract using authoritative config."""
    cfg = load_upstream_config(config_path) if config_path else load_upstream_config()
    snapshot_path = cfg.local_snapshot
    if not snapshot_path.is_file():
        raise RuntimeError(f"Spoolman contract snapshot file missing at {snapshot_path}")
    source = snapshot_path.read_text(encoding="utf-8")
    return load_spoolman_contract(source)


def check_value_matches_annotation(
    val: Any,
    annotation: ast.expr,
    contract: SpoolmanContract,
) -> bool:
    """Recursively check if a python value satisfies an AST type annotation from SpoolmanContract."""
    if isinstance(annotation, ast.Name):
        tname = annotation.id
        if tname == "str":
            return isinstance(val, str)
        if tname == "float":
            return isinstance(val, (float, int)) and not isinstance(val, bool)
        if tname == "int":
            return isinstance(val, int) and not isinstance(val, bool)
        if tname == "bool":
            return isinstance(val, bool)
        if tname == "Any":
            return True
        if tname in contract.enum_values:
            return isinstance(val, str) and val in contract.enum_values[tname]
        return False

    if isinstance(annotation, ast.Constant) and annotation.value is None:
        return val is None

    if isinstance(annotation, ast.BinOp) and isinstance(annotation.op, ast.BitOr):
        return check_value_matches_annotation(val, annotation.left, contract) or check_value_matches_annotation(
            val, annotation.right, contract
        )

    if (
        isinstance(annotation, ast.Subscript)
        and isinstance(annotation.value, ast.Name)
        and annotation.value.id == "list"
    ):
        if not isinstance(val, list):
            return False
        return all(check_value_matches_annotation(elem, annotation.slice, contract) for elem in val)

    return False


def project_single_record(
    record: Dict[str, Any],
    contract: SpoolmanContract,
) -> Dict[str, Any]:
    """Project a single Community compiled filament dictionary to Spoolman-native fields.

    Requirements:
    1. Only include keys present in contract.fields.
    2. Preserve public `id` exactly.
    3. Fail (raise ValueError) if any required field according to the contract is missing or None.
    4. Validate every retained native field against its pinned AST annotation / enum constraints.
    """
    rec_id = record.get("id", "<unknown_id>")
    projected: Dict[str, Any] = {}

    for field_name, field_contract in contract.fields.items():
        if field_name in record:
            val = record[field_name]
            if val is None:
                if field_contract.required:
                    raise ValueError(
                        f"Record '{rec_id}' missing required native field '{field_name}' (value is None)"
                    )
                if not check_value_matches_annotation(val, field_contract.annotation, contract):
                    raise ValueError(
                        f"Record '{rec_id}' field '{field_name}' is None but annotation '{ast.unparse(field_contract.annotation)}' does not accept None"
                    )
                projected[field_name] = None
            else:
                if not check_value_matches_annotation(val, field_contract.annotation, contract):
                    annot_str = ast.unparse(field_contract.annotation)
                    raise ValueError(
                        f"Record '{rec_id}' field '{field_name}' has invalid value {val!r} of type {type(val).__name__}; expected annotation '{annot_str}'"
                    )
                projected[field_name] = val
        else:
            if field_contract.required:
                raise ValueError(
                    f"Record '{rec_id}' missing required native field '{field_name}'"
                )

    return projected


def project_compiled_records(
    records: Sequence[Dict[str, Any]],
    contract: SpoolmanContract | None = None,
) -> List[Dict[str, Any]]:
    """Project a sequence of compiled filament records to Spoolman-native fields."""
    if contract is None:
        contract = get_native_contract()

    projected_list: List[Dict[str, Any]] = []
    for idx, rec in enumerate(records):
        try:
            proj = project_single_record(rec, contract)
            projected_list.append(proj)
        except ValueError as exc:
            rec_id = rec.get("id", f"index {idx}")
            raise ValueError(f"Failed to project record '{rec_id}': {exc}") from exc

    return projected_list


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate and project compiled filaments to Spoolman-native fields."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=FILAMENTS_JSON_PATH,
        help="Input filaments JSON file (defaults to filaments.json).",
    )
    args = parser.parse_args()

    if not args.input.is_file():
        print(f"ERROR: Input file missing at {args.input}", file=sys.stderr)
        sys.exit(1)

    try:
        records = json.loads(args.input.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"ERROR: Failed to parse input file {args.input}: {exc}", file=sys.stderr)
        sys.exit(1)

    contract = get_native_contract()
    print(f"Loaded Spoolman native contract ({len(contract.fields)} fields).")
    print(f"Projecting {len(records)} compiled filament records...")

    try:
        projected = project_compiled_records(records, contract)
        print(f"✓ Projection successful ({len(projected)} records).")
        if records:
            sample_in_keys = set(records[0].keys())
            sample_out_keys = set(projected[0].keys())
            stripped_keys = sample_in_keys - sample_out_keys
            print(f"  Native fields retained ({len(sample_out_keys)}): {sorted(sample_out_keys)}")
            print(f"  Extension fields stripped ({len(stripped_keys)}): {sorted(stripped_keys)}")
    except ValueError as exc:
        print(f"ERROR: Projection failed: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
