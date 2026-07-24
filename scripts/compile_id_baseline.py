"""Script and library to generate, check, and update the Public Compiled ID baseline manifest."""

import argparse
import json
from pathlib import Path
import sys
from typing import Dict, List, Tuple

ROOT = Path(__file__).parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.compile_filaments import expand_filament_data, load_json

BASELINE_PATH = ROOT / "contracts" / "compiled_id_baseline.json"
FILAMENTS_DIR = ROOT / "filaments"


def make_canonical_identity_key(
    fname: str,
    manufacturer: str,
    fil_template_name: str,
    color_name: str,
    material: str,
    weight: float,
    diameter: float,
    spool_type: str | None,
    is_refill: bool,
) -> str:
    """Generate a deterministic physical identity key for a filament variant."""
    return f"{fname}::{manufacturer}::{fil_template_name}::{color_name}::{material}::{weight}::{diameter}::{spool_type}::{is_refill}"


def compile_current_id_manifest(
    filaments_dir: Path = FILAMENTS_DIR,
) -> Tuple[Dict[str, str], List[str]]:
    """Compile all source files in filaments_dir in memory and produce mapping of canonical_key -> public_id.

    Returns:
        (manifest, errors): manifest mapping and list of compilation/uniqueness error strings.
    """
    manifest: Dict[str, str] = {}
    errors: List[str] = []
    seen_ids: Dict[str, str] = {}  # public_id -> canonical_key

    for fpath in sorted(filaments_dir.glob("*.json")):
        fname = fpath.name
        try:
            data = load_json(fpath)
        except Exception as exc:
            errors.append(f"Failed to load JSON file {fname}: {exc}")
            continue

        mfr = data.get("manufacturer")
        if not mfr:
            errors.append(f"{fname}: missing top-level 'manufacturer'")
            continue

        for fil in data.get("filaments", []):
            fil_template_name = fil.get("name", "<unnamed>")
            mat = fil.get("material", "<unnamed>")
            for rec in expand_filament_data(mfr, fil):
                color_name = rec["name"]
                w = rec["weight"]
                d = rec["diameter"]
                st = rec["spool_type"]
                is_refill = rec["is_refill"]
                pub_id = rec["id"]

                ckey = make_canonical_identity_key(
                    fname=fname,
                    manufacturer=mfr,
                    fil_template_name=fil_template_name,
                    color_name=color_name,
                    material=mat,
                    weight=w,
                    diameter=d,
                    spool_type=st,
                    is_refill=is_refill,
                )

                if ckey in manifest:
                    errors.append(
                        f"Duplicate canonical identity key detected in source data: '{ckey}'"
                    )
                else:
                    manifest[ckey] = pub_id

                if pub_id in seen_ids:
                    errors.append(
                        f"Duplicate Public ID '{pub_id}' generated for canonical keys:\n"
                        f"  1) '{seen_ids[pub_id]}'\n"
                        f"  2) '{ckey}'"
                    )
                else:
                    seen_ids[pub_id] = ckey

    return manifest, errors


def check_baseline_manifest(
    baseline_path: Path = BASELINE_PATH,
    filaments_dir: Path = FILAMENTS_DIR,
) -> Tuple[List[str], List[str], Dict[str, int]]:
    """Compare current in-memory compiled IDs against committed baseline.

    Returns:
        (errors, warnings, stats): Tuple of error list, warning list, and stats dict.
        stats = {"baseline_count": int, "current_count": int, "matched": int, "added": int, "changed": int, "missing": int}
    """
    errors: List[str] = []
    warnings: List[str] = []
    stats = {
        "baseline_count": 0,
        "current_count": 0,
        "matched": 0,
        "added": 0,
        "changed": 0,
        "missing": 0,
    }

    if not baseline_path.exists():
        errors.append(f"Baseline file does not exist at '{baseline_path}'")
        return errors, warnings, stats

    try:
        with baseline_path.open(encoding="utf-8") as f:
            baseline_data = json.load(f)
    except Exception as exc:
        errors.append(f"Failed to parse baseline manifest '{baseline_path}': {exc}")
        return errors, warnings, stats

    if not isinstance(baseline_data, dict) or "manifest" not in baseline_data:
        errors.append(
            f"Invalid baseline format in '{baseline_path}': missing top-level 'manifest' dictionary"
        )
        return errors, warnings, stats

    baseline_manifest = baseline_data["manifest"]
    if not isinstance(baseline_manifest, dict):
        errors.append(
            f"Invalid baseline format in '{baseline_path}': 'manifest' field must be a dict"
        )
        return errors, warnings, stats

    stats["baseline_count"] = len(baseline_manifest)

    current_manifest, compile_errors = compile_current_id_manifest(filaments_dir)
    errors.extend(compile_errors)
    stats["current_count"] = len(current_manifest)

    # Check for changes and additions
    for ckey, current_id in sorted(current_manifest.items()):
        if ckey in baseline_manifest:
            historical_id = baseline_manifest[ckey]
            if current_id == historical_id:
                stats["matched"] += 1
            else:
                stats["changed"] += 1
                errors.append(
                    f"Public ID regression detected for variant '{ckey}':\n"
                    f"  Historical ID: '{historical_id}'\n"
                    f"  Current ID:    '{current_id}'"
                )
        else:
            stats["added"] += 1
            warnings.append(
                f"New variant added (not in baseline): '{ckey}' -> '{current_id}'"
            )

    # Check for missing baseline variants
    for ckey, historical_id in sorted(baseline_manifest.items()):
        if ckey not in current_manifest:
            stats["missing"] += 1
            errors.append(
                f"Historical baseline variant missing from current source data:\n"
                f"  Identity key:   '{ckey}'\n"
                f"  Historical ID:  '{historical_id}'"
            )

    return errors, warnings, stats


def write_baseline_manifest(
    baseline_path: Path = BASELINE_PATH,
    filaments_dir: Path = FILAMENTS_DIR,
) -> None:
    """Generate and write a fresh baseline manifest file."""
    manifest, errors = compile_current_id_manifest(filaments_dir)
    if errors:
        print("ERROR: Cannot generate baseline manifest due to compilation errors:", file=sys.stderr)
        for err in errors:
            print(f"  {err}", file=sys.stderr)
        sys.exit(1)

    payload = {
        "version": 1,
        "count": len(manifest),
        "manifest": dict(sorted(manifest.items())),
    }

    baseline_path.parent.mkdir(parents=True, exist_ok=True)
    with baseline_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"✓ Baseline manifest successfully written to '{baseline_path}' ({len(manifest)} records).")


def main():
    parser = argparse.ArgumentParser(
        description="Check or update the Public Compiled ID baseline manifest."
    )
    parser.add_argument(
        "--update",
        action="store_true",
        help="Explicitly update the committed baseline manifest file.",
    )
    args = parser.parse_args()

    if args.update:
        write_baseline_manifest()
        sys.exit(0)

    print(f"Checking Public Compiled ID baseline against '{BASELINE_PATH.name}'...")
    errors, warnings, stats = check_baseline_manifest()

    print(
        f"Baseline records: {stats['baseline_count']} | Current compiled: {stats['current_count']} | "
        f"Matched: {stats['matched']} | Added: {stats['added']} | Changed: {stats['changed']} | Missing: {stats['missing']}"
    )

    if warnings:
        for w in warnings:
            print(f"WARN baseline: {w}")

    if errors:
        print("\nERROR: Public Compiled ID baseline check failed:", file=sys.stderr)
        for err in errors:
            print(f"  {err}", file=sys.stderr)
        sys.exit(1)

    print("✓ Public Compiled ID baseline check passed successfully.")


if __name__ == "__main__":
    main()
