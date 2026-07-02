import argparse
import sys
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    import jsonschema
except ImportError:
    print("ERROR: 'jsonschema' package not found.")
    print("Please install it by running: pip install jsonschema")
    sys.exit(1)

from scripts.display_name import collect_ambiguous_display_name_warnings


def validate_json(schema_path: Path, data_path: Path) -> bool:
    try:
        with schema_path.open(encoding="utf-8") as f:
            schema = json.load(f)
        with data_path.open(encoding="utf-8") as f:
            data = json.load(f)
        
        jsonschema.validate(instance=data, schema=schema)
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
            jsonschema.validate(instance=data, schema=schema)
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
        print("✓ All filaments are valid.")
    else:
        success = False

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