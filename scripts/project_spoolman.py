"""Script and library to project Community compiled filament records to Spoolman-native fields only.

Note on Architecture & Intent:
This module provides a deterministic projection layer for architectural preparedness in case
a future Spoolman release enforces strict contract field parsing (rejecting extra/unknown fields).
It is NOT a claim that current Spoolman releases require a stripped export, nor does it alter
the primary rich 'filaments.json' artifact published by SpoolmanDB-Community.
"""

from __future__ import annotations

import argparse
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


def project_single_record(
    record: Dict[str, Any],
    contract: SpoolmanContract,
) -> Dict[str, Any]:
    """Project a single Community compiled filament dictionary to Spoolman-native fields.

    Requirements:
    1. Only include keys present in contract.fields.
    2. Preserve public `id` exactly.
    3. Fail (raise ValueError) if any required field according to the contract is missing or None.
    4. Validate enum fields (e.g. spool_type) if present and non-null.
    """
    projected: Dict[str, Any] = {}

    for field_name, field_contract in contract.fields.items():
        if field_name in record:
            val = record[field_name]
            if val is None and field_contract.required:
                raise ValueError(
                    f"Record '{record.get('id', '<unknown>')}' missing required native field '{field_name}' (value is None)"
                )

            if val is not None:
                if field_name == "spool_type":
                    valid_spool_types = contract.enum_values.get("SpoolType", set())
                    if valid_spool_types and val not in valid_spool_types:
                        raise ValueError(
                            f"Record '{record.get('id', '<unknown>')}' has invalid spool_type '{val}'. Allowed: {sorted(valid_spool_types)}"
                        )

            projected[field_name] = val
        else:
            if field_contract.required:
                raise ValueError(
                    f"Record '{record.get('id', '<unknown>')}' missing required native field '{field_name}'"
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
        description="Project compiled filaments to Spoolman-native fields."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=FILAMENTS_JSON_PATH,
        help="Input filaments JSON file (defaults to filaments.json).",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Run projection in memory and report stats without writing output.",
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
