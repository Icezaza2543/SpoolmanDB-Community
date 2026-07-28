"""Script and library to generate, check, and update the Public Compiled ID baseline manifest."""

import argparse
import json
import os
from pathlib import Path
import subprocess
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


def load_baseline_payload(
    source: Path | str | dict,
    repository_root: Path = ROOT,
) -> Tuple[Dict[str, Any], List[str]]:
    """Load baseline dictionary payload from a file Path, dict, JSON string, or git reference."""
    errors: List[str] = []

    if isinstance(source, dict):
        return source, errors

    if isinstance(source, Path):
        if not source.exists():
            errors.append(f"Baseline file does not exist at '{source}'")
            return {}, errors
        try:
            raw_content = source.read_text(encoding="utf-8")
            data = parse_json_without_duplicates(raw_content)
            return data, errors
        except Exception as exc:
            errors.append(f"Failed to parse baseline manifest '{source}': {exc}")
            return {}, errors

    src_str = str(source).strip()
    path_obj = Path(src_str)

    if path_obj.exists() and path_obj.is_file():
        try:
            raw_content = path_obj.read_text(encoding="utf-8")
            data = parse_json_without_duplicates(raw_content)
            return data, errors
        except Exception as exc:
            errors.append(f"Failed to parse baseline manifest '{src_str}': {exc}")
            return {}, errors

    # Git ref string (e.g. commit SHA or ref like origin/main)
    try:
        rel_path = BASELINE_PATH.relative_to(repository_root).as_posix()
        git_cmd = ["git", "show", f"{src_str}:{rel_path}"]
        proc = subprocess.run(
            git_cmd,
            cwd=repository_root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True,
        )
        data = parse_json_without_duplicates(proc.stdout)
        return data, errors
    except subprocess.CalledProcessError as exc:
        stderr_msg = exc.stderr.strip() if exc.stderr else str(exc)
        errors.append(f"Failed to load baseline from git ref '{src_str}': {stderr_msg}")
        return {}, errors
    except Exception as exc:
        errors.append(f"Failed to load baseline from git ref '{src_str}': {exc}")
        return {}, errors


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
    baseline_path: Path | str | dict = BASELINE_PATH,
    filaments_dir: Path = FILAMENTS_DIR,
    base_baseline_path: Path | str | dict | None = None,
) -> BaselineCheckResult:
    """Compare current in-memory compiled IDs and PR HEAD baseline against trusted BASE baseline."""
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

    # 1. Load HEAD baseline
    head_data, head_load_errs = load_baseline_payload(baseline_path)
    if head_load_errs:
        structural_errors.extend(head_load_errs)
        return BaselineCheckResult(
            structural_errors, changed_errors, removed_errors, added_diagnostics, rekeyed_diagnostics, warnings, stats
        )

    head_struct_errs = validate_baseline_structure(head_data)
    if head_struct_errs:
        structural_errors.extend(head_struct_errs)
        return BaselineCheckResult(
            structural_errors, changed_errors, removed_errors, added_diagnostics, rekeyed_diagnostics, warnings, stats
        )

    head_manifest: Dict[str, str] = head_data["manifest"]

    # 2. Load BASE baseline (trusted baseline)
    if base_baseline_path is not None:
        base_data, base_load_errs = load_baseline_payload(base_baseline_path)
        if base_load_errs:
            structural_errors.extend(base_load_errs)
            return BaselineCheckResult(
                structural_errors, changed_errors, removed_errors, added_diagnostics, rekeyed_diagnostics, warnings, stats
            )
        base_struct_errs = validate_baseline_structure(base_data)
        if base_struct_errs:
            structural_errors.extend(base_struct_errs)
            return BaselineCheckResult(
                structural_errors, changed_errors, removed_errors, added_diagnostics, rekeyed_diagnostics, warnings, stats
            )
        base_manifest: Dict[str, str] = base_data["manifest"]
        is_trusted_base_mode = True
    else:
        base_manifest = head_manifest
        is_trusted_base_mode = False

    stats["baseline_count"] = len(base_manifest)

    # 3. Compile current source manifest from filaments_dir
    current_manifest, compile_errors = compile_current_id_manifest(filaments_dir)
    if compile_errors:
        structural_errors.extend(compile_errors)
        return BaselineCheckResult(
            structural_errors, changed_errors, removed_errors, added_diagnostics, rekeyed_diagnostics, warnings, stats
        )

    stats["current_count"] = len(current_manifest)

    base_id_to_ckey: Dict[str, str] = {pub_id: ckey for ckey, pub_id in base_manifest.items()}
    current_id_to_ckey: Dict[str, str] = {pub_id: ckey for ckey, pub_id in current_manifest.items()}
    head_id_to_ckey: Dict[str, str] = {pub_id: ckey for ckey, pub_id in head_manifest.items()}

    # --- CHECK A: Current Source vs Trusted BASE Baseline ---
    for ckey, current_id in sorted(current_manifest.items()):
        if ckey in base_manifest:
            base_id = base_manifest[ckey]
            if current_id == base_id:
                stats["matched"] += 1
            else:
                stats["changed"] += 1
                changed_errors.append(
                    f"Public ID regression detected for variant '{ckey}':\n"
                    f"  Historical BASE ID: '{base_id}'\n"
                    f"  Current Source ID:  '{current_id}'"
                )
        else:
            if current_id in base_id_to_ckey:
                base_ckey = base_id_to_ckey[current_id]
                stats["rekeyed"] += 1
                msg = (
                    f"Source identity rekey with unchanged public ID: ID '{current_id}'\n"
                    f"  Historical key: '{base_ckey}'\n"
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

    for ckey_old, base_id in sorted(base_manifest.items()):
        if ckey_old not in current_manifest:
            if base_id not in current_id_to_ckey:
                stats["removed"] += 1
                removed_errors.append(
                    f"Historical baseline variant missing from current source data:\n"
                    f"  Historical BASE ID: '{base_id}'\n"
                    f"  Historical key:     '{ckey_old}'"
                )

    # --- CHECK B: PR HEAD Baseline vs Trusted BASE Baseline ---
    if is_trusted_base_mode:
        for ckey_base, base_id in sorted(base_manifest.items()):
            if ckey_base in head_manifest:
                head_id = head_manifest[ckey_base]
                if head_id != base_id:
                    msg = (
                        f"PR baseline tampering detected for variant '{ckey_base}':\n"
                        f"  Historical BASE ID: '{base_id}'\n"
                        f"  PR HEAD Baseline ID: '{head_id}'"
                    )
                    if msg not in changed_errors:
                        changed_errors.append(msg)
                        stats["changed"] += 1
            else:
                if base_id not in head_id_to_ckey:
                    msg = (
                        f"PR baseline tampering detected: Historical BASE ID '{base_id}' (key: '{ckey_base}') "
                        f"was removed from PR baseline manifest."
                    )
                    if msg not in removed_errors:
                        removed_errors.append(msg)
                        stats["removed"] += 1

        for ckey_head, head_id in sorted(head_manifest.items()):
            if ckey_head in current_manifest:
                curr_id = current_manifest[ckey_head]
                if head_id != curr_id:
                    msg = (
                        f"PR baseline mismatch vs current source for variant '{ckey_head}':\n"
                        f"  PR HEAD Baseline ID: '{head_id}'\n"
                        f"  Current Source ID:  '{curr_id}'"
                    )
                    if msg not in changed_errors:
                        changed_errors.append(msg)
                        stats["changed"] += 1

    stats["missing"] = stats["removed"]
    return BaselineCheckResult(
        structural_errors, changed_errors, removed_errors, added_diagnostics, rekeyed_diagnostics, warnings, stats
    )


def check_baseline_manifest(
    baseline_path: Path | str = BASELINE_PATH,
    filaments_dir: Path = FILAMENTS_DIR,
    base_baseline_path: Path | str | None = None,
) -> Tuple[List[str], List[str], Dict[str, int]]:
    """Compare current in-memory compiled IDs against committed baseline.

    Returns:
        (errors, warnings, stats): Tuple of all error strings, warning strings, and stats dict.
    """
    result = check_baseline_manifest_detailed(
        baseline_path=baseline_path, filaments_dir=filaments_dir, base_baseline_path=base_baseline_path
    )
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
    parser.add_argument(
        "--base-ref",
        "--base-baseline",
        dest="base_ref",
        default=None,
        help="Git ref (e.g. commit SHA or 'origin/main') or file path to trusted base baseline manifest for PR checking.",
    )
    parser.add_argument(
        "--baseline",
        dest="baseline_path",
        default=BASELINE_PATH,
        help="Path to baseline manifest JSON file (defaults to contracts/compiled_id_baseline.json).",
    )
    args = parser.parse_args()

    if args.accept_breaking_baseline_changes and not args.update:
        print("ERROR: '--accept-breaking-baseline-changes' can only be used together with '--update'.", file=sys.stderr)
        sys.exit(1)

    if args.update:
        write_baseline_manifest(
            baseline_path=Path(args.baseline_path),
            accept_breaking_changes=args.accept_breaking_baseline_changes,
        )
        sys.exit(0)

    print(f"Checking Public Compiled ID baseline against '{args.baseline_path}'...")
    if args.base_ref:
        print(f"Trusted BASE baseline ref/file: '{args.base_ref}'")

    result = check_baseline_manifest_detailed(
        baseline_path=args.baseline_path,
        base_baseline_path=args.base_ref,
    )

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
        print("\nERROR: Changed ID mappings (Public ID regressions / tampering):", file=sys.stderr)
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
