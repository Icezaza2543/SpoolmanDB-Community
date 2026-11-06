"""Explicit unknown swatches must not become invented physical colors."""
import json
from pathlib import Path

import jsonschema
import pytest

from scripts.compile_filaments import expand_filament_data

ROOT = Path(__file__).resolve().parents[1]


def source(color):
    return {"manufacturer": "Layr175", "filaments": [{
        "name": "{color_name}", "material": "PLA", "density": 1.24,
        "weights": [{"weight": 1000}], "diameters": [1.75], "colors": [color],
    }]}


def test_explicit_null_color_compiles_without_inventing_a_swatch():
    data = source({"name": "MORPH", "hex": None})
    record, = expand_filament_data(data["manufacturer"], data["filaments"][0])
    assert record["id"] == "layr175_pla_morph_1000_175_n"
    assert record["color_hex"] is None
    assert record["color_hexes"] is None
    assert record["multi_color_direction"] is None
    jsonschema.validate([record], json.loads((ROOT / "filaments.compiled.schema.json").read_text()))


def test_source_schema_accepts_explicit_null_color():
    jsonschema.validate(source({"name": "MORPH", "hex": None}),
                        json.loads((ROOT / "filaments.schema.json").read_text()))


@pytest.mark.parametrize("color", [
    {"name": "MORPH"},
    {"name": "MORPH", "hex": None, "hexes": ["FF0000", "0000FF"],
     "multi_color_direction": "longitudinal"},
])
def test_missing_or_conflicting_color_is_still_rejected(color):
    data = source(color)
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(data, json.loads((ROOT / "filaments.schema.json").read_text()))
    with pytest.raises(ValueError):
        list(expand_filament_data(data["manufacturer"], data["filaments"][0]))
