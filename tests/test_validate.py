import json
import pytest
import jsonschema
from pathlib import Path

from scripts.validate import FORMAT_CHECKER

ROOT = Path(__file__).parent.parent


def test_schema_rejects_unknown_properties():
    schema_path = ROOT / "filaments.schema.json"
    with schema_path.open(encoding="utf-8") as f:
        schema = json.load(f)

    validator = jsonschema.Draft7Validator(
        schema, format_checker=FORMAT_CHECKER
    )

    base_data = {
        "manufacturer": "TestBrand",
        "filaments": [
            {
                "name": "PLA {color_name}",
                "material": "PLA",
                "density": 1.24,
                "weights": [{"weight": 1000}],
                "diameters": [1.75],
                "colors": [{"name": "Red", "hex": "FF0000"}],
            }
        ],
    }

    # Valid data passes
    assert validator.is_valid(base_data)

    # Unknown root property
    bad_root = dict(base_data, unknown_root="invalid")
    assert not validator.is_valid(bad_root)

    # Unknown filament property
    bad_filament = {
        "manufacturer": "TestBrand",
        "filaments": [
            dict(base_data["filaments"][0], unknown_filament_field=123)
        ],
    }
    assert not validator.is_valid(bad_filament)

    # Unknown weight property (e.g. legacy typo spool_material)
    bad_weight = {
        "manufacturer": "TestBrand",
        "filaments": [
            {
                "name": "PLA {color_name}",
                "material": "PLA",
                "density": 1.24,
                "weights": [{"weight": 1000, "spool_material": "plastic"}],
                "diameters": [1.75],
                "colors": [{"name": "Red", "hex": "FF0000"}],
            }
        ],
    }
    assert not validator.is_valid(bad_weight)

    # Unknown color property
    bad_color = {
        "manufacturer": "TestBrand",
        "filaments": [
            {
                "name": "PLA {color_name}",
                "material": "PLA",
                "density": 1.24,
                "weights": [{"weight": 1000}],
                "diameters": [1.75],
                "colors": [{"name": "Red", "hex": "FF0000", "typo_color_key": True}],
            }
        ],
    }
    assert not validator.is_valid(bad_color)


def test_schema_validates_uri_format():
    schema_path = ROOT / "filaments.schema.json"
    with schema_path.open(encoding="utf-8") as f:
        schema = json.load(f)

    validator = jsonschema.Draft7Validator(
        schema, format_checker=FORMAT_CHECKER
    )

    data_invalid_uri = {
        "manufacturer": "TestBrand",
        "filaments": [
            {
                "name": "PLA {color_name}",
                "material": "PLA",
                "density": 1.24,
                "weights": [{"weight": 1000}],
                "diameters": [1.75],
                "colors": [{"name": "Red", "hex": "FF0000"}],
                "sds_url": "invalid-not-a-uri",
            }
        ],
    }

    assert not validator.is_valid(data_invalid_uri)


def test_materials_schema_rejects_unknown_properties():
    schema_path = ROOT / "materials.schema.json"
    with schema_path.open(encoding="utf-8") as f:
        schema = json.load(f)

    validator = jsonschema.Draft7Validator(schema)

    valid_materials = [{"material": "PLA", "density": 1.24}]
    assert validator.is_valid(valid_materials)

    invalid_materials = [{"material": "PLA", "density": 1.24, "unknown_prop": "val"}]
    assert not validator.is_valid(invalid_materials)
