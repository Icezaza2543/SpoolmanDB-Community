import copy
import json
from pathlib import Path

import jsonschema
import pytest

from scripts.compile_filaments import expand_filament_data

ROOT = Path(__file__).resolve().parents[1]


def definition():
    return {"name": "{color_name}", "material": "PLA", "density": 1.24,
            "weights": [{"weight": 500}, {"weight": 1000}], "diameters": [1.75, 2.85],
            "colors": [{"name": "Black", "hex": "111111", "transmission_distance": 0.7},
                       {"name": "White", "hex": "EEEEEE", "transmission_distance": 4.2},
                       {"name": "Gray", "hex": "777777"}]}


def test_td_is_per_color_and_preserves_all_existing_fields():
    data = definition()
    original = copy.deepcopy(data)
    for color in original["colors"]:
        color.pop("transmission_distance", None)
    before = list(expand_filament_data("Example", original))
    after = list(expand_filament_data("Example", data))
    assert len(after) == 12
    assert [r["transmission_distance"] for r in after] == [0.7, 4.2, None] * 4
    assert [{k: v for k, v in r.items() if k != "transmission_distance"} for r in after] == [
        {k: v for k, v in r.items() if k != "transmission_distance"} for r in before]
    schema = json.loads((ROOT / "filaments.compiled.schema.json").read_text())
    jsonschema.validate(after, schema)


@pytest.mark.parametrize("value,valid", [(0.1, True), (5, True), (0, False),
                                         (-1, False), (None, False), ("2", False), (True, False)])
def test_source_td_schema(value, valid):
    data = definition()
    data["colors"][0]["transmission_distance"] = value
    schema = json.loads((ROOT / "filaments.schema.json").read_text())
    assert jsonschema.Draft7Validator(schema).is_valid({"manufacturer": "Example", "filaments": [data]}) == valid


@pytest.mark.parametrize("country,valid", [("CN", True), ("TH", True), ("GB", True),
                                           ("ZZ", False), ("UK", False), ("cn", False)])
def test_country_uses_assigned_upstream_codes(country, valid):
    data = definition()
    for color in data["colors"]:
        color.pop("transmission_distance", None)
    data["country_of_origin"] = country
    schema = json.loads((ROOT / "filaments.schema.json").read_text())
    assert jsonschema.Draft7Validator(schema).is_valid({"manufacturer": "Example", "filaments": [data]}) == valid
