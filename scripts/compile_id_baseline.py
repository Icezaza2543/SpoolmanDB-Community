"""Script and library to generate, check, and update the Public Compiled ID baseline manifest."""

import argparse
import json
import os
from pathlib import Path
import sys
import tempfile
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.compile_filaments import expand_filament_data, load_json

BASELINE_PATH = ROOT / "contracts" / "compiled_id_baseline.json"
FILAMENTS_DIR = ROOT / "filaments"
ALLOWED_TOP_LEVEL_KEYS = {"version", "count", "manifest"}


class BaselineCheckResult:
    """Structured check result separating structural errors, historical ID changes, rekeys, and additions."""

    def __init__(
        self,
        structural_errors: List[str],
        changed_errors: List[str],
        removed_errors: List[str],
        added_diagnostics: List[str],
        rekeyed_diagnostics: List[str],
        warnings: List[str],
        stats: Dict[str, int],
    ):
        self.structural_errors = structural_errors
        self.changed_errors = changed_errors
        self.removed_errors = removed_errors
        self.missing_errors = removed_errors  # Backward compatibility alias
        self.added_diagnostics = added_diagnostics
        self.rekeyed_diagnostics = rekeyed_diagnostics
        self.warnings = warnings
        self.stats = stats

    @property
    def all_errors(self) -> List[str]:
        return self.structural_errors + self.changed_errors + self.removed_errors

    @property
    def is_valid_structure(self) -> bool:
        return len(self.structural_errors) == 0

    @property
    def has_breaking_changes(self) -> bool:
        return (
            (self.stats.get("changed", 0) > 0)
            or (self.stats.get("removed", 0) > 0)
            or (self.stats.get("missing", 0) > 0)
        )


def parse_json_without_duplicates(json_str: str) -> Any:
    """Parse JSON string and raise ValueError if duplicate keys exist at any object level."""

    def dict_raise_on_duplicates(pairs):
        d = {}
        for k, v in pairs:
            if k in d:
                raise ValueError(f"Duplicate JSON key detected: '{k}'")
            d[k] = v
        return d

    return json.loads(json_str, object_pairs_hook=dict_raise_on_duplicates)


def make_canonical_identity_key(
    fname: str,
    manufacturer: str,
    fil_template_name: str,
    compiled_name: str,
    material: str,
    weight: float,
    diameter: float,
    spool_type: str | None,
    is_refill: bool,
) -> str:
    """Generate a deterministic physical identity key for a filament variant."""
    return f"{fname}::{manufacturer}::{fil_template_name}::{compiled_name}::{material}::{weight}::{diameter}::{spool_type}::{is_refill}"


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
                compiled_name = rec["name"]
                w = rec["weight"]
                d = rec["diameter"]
                st = rec["spool_type"]
                is_refill = rec["is_refill"]
                pub_id = rec["id"]

                ckey = make_canonical_identity_key(
                    fname=fname,
                    manufacturer=mfr,
                    fil_template_name=fil_template_name,
                    compiled_name=compiled_name,
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


def validate_baseline_structure(baseline_data: Any) -> List[str]:
    """Validate top-level metadata schema and internal consistency of baseline object."""
    errors: List[str] = []

    if not isinstance(baseline_data, dict):
        errors.append("Invalid baseline format: top-level element must be a JSON object")
        return errors

    unexpected_keys = set(baseline_data.keys()) - ALLOWED_TOP_LEVEL_KEYS
    if unexpected_keys:
        unexpected_fmt = ", ".join(sorted(f"'{k}'" for k in unexpected_keys))
        errors.append(
            f"Invalid baseline format: unexpected top-level field(s) {unexpected_fmt}. Allowed fields: 'version', 'count', 'manifest'"
        )

    if "version" not in baseline_data:
        errors.append("Invalid baseline format: missing top-level 'version' field")
    else:
        version_val = baseline_data["version"]
        if isinstance(version_val, bool) or not isinstance(version_val, int):
            errors.append(
                f"Invalid baseline format: 'version' field must be an integer, got {type(version_val).__name__}"
            )
        elif version_val != 1:
            errors.append(
                f"Invalid baseline format: unsupported version {version_val}. Only version 1 is supported."
            )

    if "manifest" not in baseline_data:
        errors.append("Invalid baseline format: missing top-level 'manifest' dictionary")
        manifest_obj = None
    else:
        manifest_obj = baseline_data["manifest"]
        if not isinstance(manifest_obj, dict):
            errors.append("Invalid baseline format: 'manifest' field must be a JSON object")
            manifest_obj = None

    if "count" not in baseline_data:
        errors.append("Invalid baseline format: missing top-level 'count' field")
    else:
        count_val = baseline_data["count"]
        if isinstance(count_val, bool) or not isinstance(count_val, int):
            errors.append(
                f"Invalid baseline format: 'count' field must be a non-negative integer, got {type(count_val).__name__}"
            )
        elif count_val < 0:
            errors.append(
                f"Invalid baseline format: 'count' field cannot be negative, got {count_val}"
            )
        elif manifest_obj is not None and count_val != len(manifest_obj):
            errors.append(
                f"Invalid baseline format: 'count' field ({count_val}) does not match actual manifest entry count ({len(manifest_obj)})"
            )

    if manifest_obj is not None:
        seen_baseline_ids: Dict[str, str] = {}
        for ckey, pub_id in manifest_obj.items():
            if not isinstance(ckey, str) or not ckey:
                errors.append(
                    "Invalid baseline format: manifest identity keys must be non-empty strings"
                )
                break
            if not isinstance(pub_id, str) or not pub_id:
                errors.append(
                    f"Invalid baseline format: manifest Public ID for variant '{ckey}' must be a non-empty string"
                )
                break

            if pub_id in seen_baseline_ids:
                errors.append(
                    f"Duplicate Public ID '{pub_id}' found in baseline for different identity keys:\n"
                    f"  1) '{seen_baseline_ids[pub_id]}'\n"
                    f"  2) '{ckey}'"
                )
            else:
                seen_baseline_ids[pub_id] = ckey

    return errors


def check_baseline_manifest_detailed(
    baseline_path: Path = BASELINE_PATH,
    filaments_dir: Path = FILAMENTS_DIR,
) -> BaselineCheckResult:
    """Compare current in-memory compiled IDs against committed baseline and return detailed result."""
    structural_errors: List[str] = []
    changed_errors: List[str] = []
    removed_errors: List[str] = []
    added_diagnostics: List[str] = []
    rekeyed_diagnostics: List[str] = []
    warnings: List[str] = []
    stats = {
        "baseline_count": 0,
        "current_count": 0,
        "matched": 0,
        "added": 0,
        "removed": 0,
        "changed": 0,
        "rekeyed": 0,
        "missing": 0,
    }

    if not baseline_path.exists():
        structural_errors.append(f"Baseline file does not exist at '{baseline_path}'")
        return BaselineCheckResult(
            structural_errors, changed_errors, removed_errors, added_diagnostics, rekeyed_diagnostics, warnings, stats
        )

    try:
        raw_content = baseline_path.read_text(encoding="utf-8")
        baseline_data = parse_json_without_duplicates(raw_content)
    except Exception as exc:
        structural_errors.append(f"Failed to parse baseline manifest '{baseline_path}': {exc}")
        return BaselineCheckResult(
            structural_errors, changed_errors, removed_errors, added_diagnostics, rekeyed_diagnostics, warnings, stats
        )

    struct_errors = validate_baseline_structure(baseline_data)
    if struct_errors:
        structural_errors.extend(struct_errors)
        return BaselineCheckResult(
            structural_errors, changed_errors, removed_errors, added_diagnostics, rekeyed_diagnostics, warnings, stats
        )

    baseline_manifest: Dict[str, str] = baseline_data["manifest"]
    stats["baseline_count"] = len(baseline_manifest)

    current_manifest, compile_errors = compile_current_id_manifest(filaments_dir)
    if compile_errors:
        structural_errors.extend(compile_errors)
        return BaselineCheckResult(
            structural_errors, changed_errors, removed_errors, added_diagnostics, rekeyed_diagnostics, warnings, stats
        )

    stats["current_count"] = len(current_manifest)

    historical_id_to_ckey: Dict[str, str] = {pub_id: ckey for ckey, pub_id in baseline_manifest.items()}
    current_id_to_ckey: Dict[str, str] = {pub_id: ckey for ckey, pub_id in current_manifest.items()}

    for ckey, current_id in sorted(current_manifest.items()):
        if ckey in baseline_manifest:
            historical_id = baseline_manifest[ckey]
            if current_id == historical_id:
                stats["matched"] += 1
            else:
                stats["changed"] += 1
                changed_errors.append(
                    f"Public ID regression detected for variant '{ckey}':\n"
                    f"  Historical ID: '{historical_id}'\n"
                    f"  Current ID:    '{current_id}'"
                )
        else:
            if current_id in historical_id_to_ckey:
                historical_ckey = historical_id_to_ckey[current_id]
                stats["rekeyed"] += 1
                msg = (
                    f"Source identity rekey with unchanged public ID: ID '{current_id}'\n"
                    f"  Historical key: '{historical_ckey}'\n"
                    f"  Current key:    '{ckey}'"
                )
                rekeyed_diagnostics.append(msg)
                warnings.append(msg)
            else:
                stats["added"] += 1
                msg = (
                    f"New variant added (not in baseline): '{current_id}'\n"
                    f"  Current key: '{ckey}'\n"
                    f"  Note: New variants are not protected against historical ID regression until the baseline is updated via 'python scripts/compile_id_baseline.py --update'."
                )
                added_diagnostics.append(msg)
                warnings.append(msg)

    for ckey_old, historical_id in sorted(baseline_manifest.items()):
        if ckey_old not in current_manifest:
            if historical_id not in current_id_to_ckey:
                stats["removed"] += 1
                removed_errors.append(
                    f"Historical baseline variant missing from current source data:\n"
                    f"  Historical ID:  '{historical_id}'\n"
                    f"  Historical key: '{ckey_old}'"
                )

    stats["missing"] = stats["removed"]
    return BaselineCheckResult(
        structural_errors, changed_errors, removed_errors, added_diagnostics, rekeyed_diagnostics, warnings, stats
    )


def check_baseline_manifest(
    baseline_path: Path = BASELINE_PATH,
    filaments_dir: Path = FILAMENTS_DIR,
) -> Tuple[List[str], List[str], Dict[str, int]]:
    """Compare current in-memory compiled IDs against committed baseline.

    Returns:
        (errors, warnings, stats): Tuple of all error strings, warning strings, and stats dict.
    """
    result = check_baseline_manifest_detailed(baseline_path, filaments_dir)
    return result.all_errors, result.warnings, result.stats


def write_baseline_manifest_atomic(
    payload: dict,
    baseline_path: Path = BASELINE_PATH,
) -> None:
    """Atomic write of baseline payload to baseline_path using a unique temporary file."""
    struct_errors = validate_baseline_structure(payload)
    if struct_errors:
        raise ValueError(f"Refusing to write invalid baseline payload: {struct_errors}")

    baseline_dir = baseline_path.parent
    baseline_dir.mkdir(parents=True, exist_ok=True)

    tmp_file = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=baseline_dir,
        prefix=f".{baseline_path.name}.",
        suffix=".tmp",
        delete=False,
    )
    tmp_path = Path(tmp_file.name)

    try:
        json.dump(payload, tmp_file, indent=2, ensure_ascii=False)
        tmp_file.write("\n")
        tmp_file.flush()
        os.fsync(tmp_file.fileno())
        tmp_file.close()

        os.replace(tmp_path, baseline_path)
    except Exception as exc:
        if tmp_file and not tmp_file.closed:
            try:
                tmp_file.close()
            except Exception:
                pass
        if tmp_path.exists():
            try:
                tmp_path.unlink()
            except Exception:
                pass
        raise RuntimeError(f"Failed atomic write to '{baseline_path}': {exc}") from exc


def write_baseline_manifest(
    baseline_path: Path = BASELINE_PATH,
    filaments_dir: Path = FILAMENTS_DIR,
    accept_breaking_changes: bool = False,
) -> None:
    """Generate and write a baseline manifest file with safety checks and atomic write."""
    current_manifest, compile_errors = compile_current_id_manifest(filaments_dir)
    if compile_errors:
        print("ERROR: Cannot generate baseline manifest due to source compilation errors:", file=sys.stderr)
        for err in compile_errors:
            print(f"  {err}", file=sys.stderr)
        sys.exit(1)

    if baseline_path.exists():
        result = check_baseline_manifest_detailed(
            baseline_path=baseline_path, filaments_dir=filaments_dir
        )

        if not result.is_valid_structure:
            print(
                f"ERROR: Refusing to update baseline '{baseline_path.name}': existing baseline file is malformed or invalid!\n"
                f"  Existing baseline must be structurally valid before automated updates can proceed.\n"
                f"  Structural errors:\n" + "\n".join(f"    - {err}" for err in result.structural_errors),
                file=sys.stderr,
            )
            sys.exit(1)

        if result.has_breaking_changes and not accept_breaking_changes:
            print(
                f"ERROR: Refusing to update baseline '{baseline_path.name}': breaking baseline changes detected!\n"
                f"  Matched: {result.stats['matched']} | Added: {result.stats['added']} | Rekeyed: {result.stats['rekeyed']} | Changed: {result.stats['changed']} | Removed: {result.stats['removed']}\n"
                f"  If these breaking changes are intentional, re-run with '--accept-breaking-baseline-changes'.",
                file=sys.stderr,
            )
            sys.exit(1)

        if accept_breaking_changes:
            print(
                f"Updating baseline with breaking changes explicitly enabled:\n"
                f"  Matched: {result.stats['matched']} | Added: {result.stats['added']} | Rekeyed: {result.stats['rekeyed']} | Changed: {result.stats['changed']} | Removed: {result.stats['removed']}"
            )
        else:
            print(
                f"Updating baseline (additions & rekeys safe update):\n"
                f"  Matched: {result.stats['matched']} | Added: {result.stats['added']} | Rekeyed: {result.stats['rekeyed']} | Changed: 0 | Removed: 0"
            )

    payload = {
        "version": 1,
        "count": len(current_manifest),
        "manifest": dict(sorted(current_manifest.items())),
    }

    write_baseline_manifest_atomic(payload, baseline_path=baseline_path)
    update_mode_str = "breaking" if accept_breaking_changes else "safe"
    print(f"✓ Baseline manifest successfully written to '{baseline_path}' ({len(current_manifest)} records, mode: {update_mode_str}).")


def main():
    parser = argparse.ArgumentParser(
        description="Check or update the Public Compiled ID baseline manifest."
    )
    parser.add_argument(
        "--update",
        action="store_true",
        help="Explicitly update the committed baseline manifest file.",
    )
    parser.add_argument(
        "--accept-breaking-baseline-changes",
        action="store_true",
        help="Allow baseline update even when breaking changes (changed or missing historical IDs) are detected. Must be used with --update.",
    )
    args = parser.parse_args()

    if args.accept_breaking_baseline_changes and not args.update:
        print("ERROR: '--accept-breaking-baseline-changes' can only be used together with '--update'.", file=sys.stderr)
        sys.exit(1)

    if args.update:
        write_baseline_manifest(
            accept_breaking_changes=args.accept_breaking_baseline_changes
        )
        sys.exit(0)

    print(f"Checking Public Compiled ID baseline against '{BASELINE_PATH.name}'...")
    result = check_baseline_manifest_detailed()

    print(
        f"Baseline records: {result.stats['baseline_count']} | Current compiled: {result.stats['current_count']} | "
        f"Matched: {result.stats['matched']} | Added: {result.stats['added']} | Removed: {result.stats['removed']} | "
        f"Changed: {result.stats['changed']} | Rekeyed: {result.stats['rekeyed']}"
    )

    if result.rekeyed_diagnostics:
        print("\nSource identity rekeys (unchanged public ID):")
        for diag in result.rekeyed_diagnostics:
            print(f"  {diag}")

    if result.added_diagnostics:
        print("\nAdded public IDs:")
        for diag in result.added_diagnostics:
            print(f"  {diag}")

    if result.changed_errors:
        print("\nERROR: Changed ID mappings (Public ID regressions):", file=sys.stderr)
        for err in result.changed_errors:
            print(f"  {err}", file=sys.stderr)

    if result.removed_errors:
        print("\nERROR: Removed public IDs:", file=sys.stderr)
        for err in result.removed_errors:
            print(f"  {err}", file=sys.stderr)

    if result.structural_errors:
        print("\nERROR: Structural / compilation errors:", file=sys.stderr)
        for err in result.structural_errors:
            print(f"  {err}", file=sys.stderr)

    if not result.all_errors:
        print("✓ Public Compiled ID baseline check passed successfully.")
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
