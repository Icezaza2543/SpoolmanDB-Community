import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft7Validator

from scripts.check_spoolman_compat import (
    load_spoolman_contract,
    validate_compiled_data,
    validate_schema_spool_types,
)


UPSTREAM_MODEL = """
from collections.abc import Iterator
from enum import Enum
from pydantic import BaseModel, Field, RootModel

class SpoolType(Enum):
    PLASTIC = "plastic"
    CARDBOARD = "cardboard"
    METAL = "metal"

class Finish(Enum):
    MATTE = "matte"
    GLOSSY = "glossy"

class MultiColorDirection(Enum):
    COAXIAL = "coaxial"
    LONGITUDINAL = "longitudinal"

class Pattern(Enum):
    MARBLE = "marble"
    SPARKLE = "sparkle"

class ExternalFilament(BaseModel):
    id: str = Field(description="id")
    manufacturer: str = Field(description="manufacturer")
    name: str = Field(description="name")
    material: str = Field(description="material")
    density: float = Field(description="density")
    weight: float = Field(description="weight")
    spool_weight: float | None = Field(default=None, description="spool weight")
    spool_type: SpoolType | None = Field(None, description="spool type")
    diameter: float = Field(description="diameter")
    color_hex: str | None = Field(default=None, description="color")
    color_hexes: list[str] | None = Field(default=None, description="colors")
    extruder_temp: int | None = Field(default=None, description="extruder")
    bed_temp: int | None = Field(default=None, description="bed")
    finish: Finish | None = Field(default=None, description="finish")
    multi_color_direction: MultiColorDirection | None = Field(default=None, description="direction")
    pattern: Pattern | None = Field(default=None, description="pattern")
    translucent: bool = Field(default=False, description="translucent")
    glow: bool = Field(default=False, description="glow")

class ExternalFilamentsFile(RootModel):
    root: list[ExternalFilament]

    def __iter__(self) -> Iterator[ExternalFilament]:
        return iter(self.root)
"""


def compiled_record(**overrides):
    record = {
        "id": "test_pla_black_1000_175_r",
        "manufacturer": "Test",
        "name": "Black",
        "material": "PLA",
        "density": 1.24,
        "weight": 1000,
        "spool_weight": None,
        "spool_type": None,
        "is_refill": True,
        "diameter": 1.75,
        "color_hex": "000000",
        "color_hexes": None,
        "extruder_temp": None,
        "bed_temp": None,
        "finish": None,
        "multi_color_direction": None,
        "pattern": None,
        "translucent": False,
        "glow": False,
        "codes": ["TEST-001"],
    }
    record.update(overrides)
    return record


def test_upstream_model_accepts_community_metadata_and_rejects_bad_spool_type():
    contract = load_spoolman_contract(UPSTREAM_MODEL)

    validate_compiled_data([compiled_record()], contract)

    with pytest.raises(RuntimeError, match="incompatible spool_type"):
        validate_compiled_data(
            [compiled_record(spool_type="refill")],
            contract,
        )

    without_required_id = compiled_record()
    del without_required_id["id"]
    with pytest.raises(RuntimeError, match="missing required field id"):
        validate_compiled_data([without_required_id], contract)


def test_upstream_source_is_parsed_without_execution():
    source_with_top_level_side_effect = (
        'raise RuntimeError("downloaded source was executed")\n' + UPSTREAM_MODEL
    )
    contract = load_spoolman_contract(source_with_top_level_side_effect)
    validate_compiled_data([compiled_record()], contract)

    source_with_model_config = UPSTREAM_MODEL.replace(
        "class ExternalFilament(BaseModel):",
        'class ExternalFilament(BaseModel):\n    model_config = {"extra": "forbid"}',
    )
    with pytest.raises(RuntimeError, match="manual review required"):
        load_spoolman_contract(source_with_model_config)

    source_with_constraint = UPSTREAM_MODEL.replace(
        'weight: float = Field(description="weight")',
        'weight: float = Field(description="weight", gt=0)',
    )
    with pytest.raises(RuntimeError, match="added validation options: gt"):
        load_spoolman_contract(source_with_constraint)

    source_with_dynamic_default = (
        "REQUIRED = ...\n"
        + UPSTREAM_MODEL.replace(
            'id: str = Field(description="id")',
            'id: str = Field(REQUIRED, description="id")',
        )
    )
    with pytest.raises(RuntimeError, match="dynamic default"):
        load_spoolman_contract(source_with_dynamic_default)


def test_compiled_schema_spool_values_must_be_upstream_compatible():
    contract = load_spoolman_contract(UPSTREAM_MODEL)
    schema = {
        "items": {
            "properties": {
                "spool_type": {
                    "enum": ["plastic", "cardboard", "metal", None]
                }
            }
        }
    }

    validate_schema_spool_types(schema, contract)

    incompatible = copy.deepcopy(schema)
    incompatible["items"]["properties"]["spool_type"]["enum"].append("refill")
    with pytest.raises(RuntimeError, match="rejected by Spoolman"):
        validate_schema_spool_types(incompatible, contract)

    non_nullable_source = UPSTREAM_MODEL.replace(
        "spool_type: SpoolType | None",
        "spool_type: SpoolType",
    )
    non_nullable_contract = load_spoolman_contract(non_nullable_source)
    with pytest.raises(RuntimeError, match="None"):
        validate_schema_spool_types(schema, non_nullable_contract)


def test_source_schema_enforces_refill_metadata_consistency():
    root = Path(__file__).parent.parent
    with (root / "filaments.schema.json").open(encoding="utf-8") as file:
        schema = json.load(file)

    weight_schema = schema["properties"]["filaments"]["items"]["properties"][
        "weights"
    ]["items"]
    validator = Draft7Validator(weight_schema)

    assert validator.is_valid({"weight": 1000, "is_refill": True})
    assert validator.is_valid({"weight": 1000, "spool_type": "refill"})
    assert not validator.is_valid(
        {"weight": 1000, "spool_type": "plastic", "is_refill": True}
    )
    assert not validator.is_valid(
        {"weight": 1000, "spool_type": "unknow", "is_refill": True}
    )
    assert not validator.is_valid(
        {"weight": 1000, "spool_type": "refill", "is_refill": False}
    )


def test_compiled_schema_enforces_refill_output_invariants():
    root = Path(__file__).parent.parent
    with (root / "filaments.compiled.schema.json").open(encoding="utf-8") as file:
        schema = json.load(file)

    validator = Draft7Validator(schema["items"])
    assert validator.is_valid(compiled_record())
    assert not validator.is_valid(compiled_record(spool_type="plastic"))
    assert not validator.is_valid(compiled_record(id="test_pla_black_1000_175_p"))
    assert not validator.is_valid(compiled_record(is_refill=False))

    missing_spool_type = compiled_record()
    del missing_spool_type["spool_type"]
    assert not validator.is_valid(missing_spool_type)
