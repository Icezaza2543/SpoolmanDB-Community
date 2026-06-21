import sys
import json
from pathlib import Path

try:
    import jsonschema
except ImportError:
    print("ERROR: 'jsonschema' package not found.")
    print("Please install it by running: pip install jsonschema")
    sys.exit(1)

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

def main():
    root = Path(__file__).parent.parent
    materials_schema = root / "materials.schema.json"
    materials_data = root / "materials.json"
    filaments_schema = root / "filaments.schema.json"
    filaments_dir = root / "filaments"
    
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
        
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
