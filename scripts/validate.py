import argparse
import sys
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from urllib.parse import urlparse

try:
    import jsonschema
except ImportError:
    print("ERROR: 'jsonschema' package not found.")
    print("Please install it by running: pip install jsonschema")
    sys.exit(1)

FORMAT_CHECKER = jsonschema.FormatChecker()

@FORMAT_CHECKER.checks("uri")
def _check_uri(val):
    if not isinstance(val, str):
        return True
    try:
        parsed = urlparse(val)
        return parsed.scheme.lower() in ("http", "https") and bool(parsed.netloc and parsed.hostname)
    except Exception:
        return False

from scripts.display_name import collect_ambiguous_display_name_warnings


def validate_json(schema_path: Path, data_path: Path) -> bool:
    try:
        with schema_path.open(encoding="utf-8") as f:
            schema = json.load(f)
        with data_path.open(encoding="utf-8") as f:
            data = json.load(f)
        
        jsonschema.validate(
            instance=data, schema=schema, format_checker=FORMAT_CHECKER
        )
        return True
    except Exception as e:
        print(f"Validation failed for {data_path.name} with schema {schema_path.name}:")
        print(e)
        return False

def validate_directory(schema_path: Path, dir_path: Path) -> bool:
    all_valid = True
    with schema_path.open(encoding="utf-8") as f:
        schema = json.load(f)
    
    for file in dir_path.glob("*.json"):
        try:
            with file.open(encoding="utf-8") as f:
                data = json.load(f)
            jsonschema.validate(
                instance=data, schema=schema, format_checker=FORMAT_CHECKER
            )
        except Exception as e:
            print(f"Validation failed for {file.name} with schema {schema_path.name}:")
            print(e)
            all_valid = False
            
    return all_valid

def report_display_name_warnings(filaments_dir: Path, *, strict: bool) -> bool:
    warnings = collect_ambiguous_display_name_warnings(filaments_dir)
    if not warnings:
        print("✓ No ambiguous display-name templates detected.")
        return True

    print(f"\nDisplay-name warnings ({len(warnings)}):")
    for warning in warnings:
        print(warning)

    if strict:
        print("\nERROR: --strict-display-names enabled and ambiguous templates were found.")
        return False

    print("\nDisplay-name warnings are informational only and do not fail validation by default.")
    return True

def main():
    parser = argparse.ArgumentParser(description="Validate SpoolmanDB Community data files.")
    parser.add_argument(
        "--strict-display-names",
        action="store_true",
        help="Fail validation when source templates compile to names without a material token.",
    )
    parser.add_argument(
        "--base-ref",
        "--base-baseline",
        dest="base_ref",
        default=None,
        help="Git ref (e.g. commit SHA or 'origin/main') or file path to trusted base baseline manifest for PR checking.",
    )
    parser.add_argument(
        "--strict",
        "--strict-head-sync",
        dest="strict_head_sync",
        action="store_true",
        help="Strict mode: require PR HEAD baseline manifest to match current compiled source manifest exactly.",
    )
    args = parser.parse_args()

    materials_schema = ROOT / "materials.schema.json"
    materials_data = ROOT / "materials.json"
    filaments_schema = ROOT / "filaments.schema.json"
    filaments_dir = ROOT / "filaments"
    
    success = True
    
    print("Validating materials.json...")
    if validate_json(materials_schema, materials_data):
        print("✓ materials.json is valid.")
    else:
        success = False
        
    print("\nValidating filaments directory...")
    if validate_directory(filaments_schema, filaments_dir):
        print("✓ All filaments are valid against JSON schema.")
    else:
        success = False

    from scripts.data_semantics import check_source_data_semantics

    print("\nChecking semantic data integrity...")
    sem_errors, sem_warnings = check_source_data_semantics(filaments_dir, materials_data)
    for warn in sem_warnings:
        print(f"WARN semantics: {warn}")

    if sem_errors:
        for err in sem_errors:
            print(f"ERROR semantics: {err}", file=sys.stderr)
        success = False
    else:
        print("✓ Semantic data integrity passed.")

    from scripts.compile_id_baseline import check_baseline_manifest_detailed

    print("\nChecking Public Compiled ID baseline...")
    if args.base_ref:
        print(f"Trusted BASE baseline ref/file: '{args.base_ref}'")
    if args.strict_head_sync:
        print("Strict mode: HEAD baseline synchronization required.")
    base_result = check_baseline_manifest_detailed(
        filaments_dir=filaments_dir,
        base_baseline_path=args.base_ref,
        strict_head_sync=args.strict_head_sync,
    )
    print(
        f"Baseline: {base_result.stats['baseline_count']} | Current: {base_result.stats['current_count']} | "
        f"Matched: {base_result.stats['matched']} | Added: {base_result.stats['added']} | Removed: {base_result.stats['removed']} | "
        f"Changed: {base_result.stats['changed']} | Rekeyed: {base_result.stats['rekeyed']}"
    )

    for diag in base_result.rekeyed_diagnostics:
        print(f"REKEY baseline: {diag}")

    for diag in base_result.added_diagnostics:
        print(f"WARN baseline: {diag}")

    if base_result.all_errors:
        for err in base_result.all_errors:
            print(f"ERROR baseline: {err}", file=sys.stderr)
        success = False
    else:
        print("✓ Public Compiled ID baseline check passed.")

    if not report_display_name_warnings(filaments_dir, strict=args.strict_display_names):
        success = False
        
    compiled_data = ROOT / "filaments.json"
    compiled_schema = ROOT / "filaments.compiled.schema.json"
    if compiled_data.exists():
        print("\nValidating compiled filaments.json...")
        if validate_json(compiled_schema, compiled_data):
            print("✓ Compiled filaments.json is valid.")
        else:
            success = False
        
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()