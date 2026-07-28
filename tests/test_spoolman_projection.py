"""Unit tests for strict Spoolman contract projection architecture."""

import json
from pathlib import Path
import pytest

from scripts.check_spoolman_compat import load_spoolman_contract
from scripts.project_spoolman import (
    get_native_contract,
    project_compiled_records,
    project_single_record,
)

ROOT = Path(__file__).parent.parent
FILAMENTS_JSON_PATH = ROOT / "filaments.json"


@pytest.fixture
def sample_community_record():
    return {
        "id": "branda_pla_plared_1000_175_n",
        "manufacturer": "BrandA",
        "name": "PLA Red",
        "material": "PLA",
        "density": 1.24,
        "weight": 1000,
        "diameter": 1.75,
        "spool_weight": 200,
        "spool_type": "plastic",
        "color_hex": "FF0000",
        "color_hexes": ["FF0000"],
        "extruder_temp": 210,
        "bed_temp": 60,
        "finish": "matte",
        "pattern": "marble",
        "multi_color_direction": "coaxial",
        # Community-only extension fields:
        "is_refill": True,
        "country_of_origin": "DE",
        "sds_url": "https://example.com/sds.pdf",
        "tds_url": "https://example.com/tds.pdf",
        "codes": ["BA-PLA-RED"],
        "eans": ["1234567890123"],
        "eans_refill": ["9876543210987"],
        "extra_community_field": "test_val",
    }


def test_native_field_projection_and_extension_stripping(sample_community_record):
    """1. Native fields retained, extension fields stripped, public ID preserved exactly."""
    contract = get_native_contract()
    projected = project_single_record(sample_community_record, contract)

    # Public ID preserved exactly
    assert projected["id"] == "branda_pla_plared_1000_175_n"

    # Native fields present
    assert projected["manufacturer"] == "BrandA"
    assert projected["name"] == "PLA Red"
    assert projected["material"] == "PLA"
    assert projected["density"] == 1.24
    assert projected["weight"] == 1000
    assert projected["diameter"] == 1.75
    assert projected["spool_type"] == "plastic"
    assert projected["color_hexes"] == ["FF0000"]
    assert projected["finish"] == "matte"
    assert projected["pattern"] == "marble"
    assert projected["multi_color_direction"] == "coaxial"

    # Extension fields stripped
    extension_keys = {"is_refill", "country_of_origin", "sds_url", "tds_url", "codes", "eans", "eans_refill", "extra_community_field"}
    for ext_key in extension_keys:
        assert ext_key not in projected, f"Extension key '{ext_key}' was not stripped from projected output"


def test_incompatible_primitive_types_fail(sample_community_record):
    """2. Projection fails if primitive types are incompatible (e.g. density as string, extruder_temp as string)."""
    contract = get_native_contract()

    # Density as string
    bad_density = dict(sample_community_record)
    bad_density["density"] = "1.24"
    with pytest.raises(ValueError, match="field 'density' has invalid value '1.24'"):
        project_single_record(bad_density, contract)

    # Extruder temp as string
    bad_temp = dict(sample_community_record)
    bad_temp["extruder_temp"] = "210"
    with pytest.raises(ValueError, match="field 'extruder_temp' has invalid value '210'"):
        project_single_record(bad_temp, contract)


def test_invalid_non_spool_enums_fail(sample_community_record):
    """3. Projection fails for invalid non-spool enums (Finish, Pattern, MultiColorDirection)."""
    contract = get_native_contract()

    # Invalid Finish
    bad_finish = dict(sample_community_record)
    bad_finish["finish"] = "invalid_finish_value"
    with pytest.raises(ValueError, match="field 'finish' has invalid value 'invalid_finish_value'"):
        project_single_record(bad_finish, contract)

    # Invalid Pattern
    bad_pattern = dict(sample_community_record)
    bad_pattern["pattern"] = "invalid_pattern_value"
    with pytest.raises(ValueError, match="field 'pattern' has invalid value 'invalid_pattern_value'"):
        project_single_record(bad_pattern, contract)

    # Invalid MultiColorDirection
    bad_direction = dict(sample_community_record)
    bad_direction["multi_color_direction"] = "invalid_direction_value"
    with pytest.raises(ValueError, match="field 'multi_color_direction' has invalid value 'invalid_direction_value'"):
        project_single_record(bad_direction, contract)


def test_invalid_list_element_types_fail(sample_community_record):
    """4. Projection fails if a list field (e.g. color_hexes) is non-list or contains invalid element types."""
    contract = get_native_contract()

    # Color hexes as single string instead of list
    bad_list_type = dict(sample_community_record)
    bad_list_type["color_hexes"] = "FF0000"
    with pytest.raises(ValueError, match="field 'color_hexes' has invalid value 'FF0000'"):
        project_single_record(bad_list_type, contract)

    # Color hexes containing integer instead of string
    bad_list_elem = dict(sample_community_record)
    bad_list_elem["color_hexes"] = [123456]
    with pytest.raises(ValueError, match="field 'color_hexes' has invalid value \\[123456\\]"):
        project_single_record(bad_list_elem, contract)


def test_required_field_missing_fails():
    """5. Projection fails if a required native field is missing from record."""
    contract = get_native_contract()
    incomplete_record = {
        "manufacturer": "BrandA",
        "density": 1.24,
    }

    with pytest.raises(ValueError, match="missing required native field"):
        project_single_record(incomplete_record, contract)


def test_required_field_none_fails():
    """6. Projection fails if a required native field is None."""
    contract = get_native_contract()
    record_with_none_id = {
        "id": None,
        "manufacturer": "BrandA",
        "name": "PLA Red",
        "material": "PLA",
        "density": 1.24,
        "weight": 1000,
        "diameter": 1.75,
    }

    with pytest.raises(ValueError, match="missing required native field 'id'"):
        project_single_record(record_with_none_id, contract)


def test_invalid_enum_spool_type_fails(sample_community_record):
    """7. Projection fails if spool_type is invalid according to contract SpoolType enum."""
    contract = get_native_contract()
    bad_record = dict(sample_community_record)
    bad_record["spool_type"] = "invalid_type_wood"

    with pytest.raises(ValueError, match="field 'spool_type' has invalid value 'invalid_type_wood'"):
        project_single_record(bad_record, contract)


def test_project_entire_committed_filaments_json_dataset():
    """8. Project the ENTIRE committed filaments.json. Verify exact ID order & native key matching."""
    assert FILAMENTS_JSON_PATH.exists()
    records = json.loads(FILAMENTS_JSON_PATH.read_text(encoding="utf-8"))
    contract = get_native_contract()

    # Project the entire dataset
    projected_list = project_compiled_records(records, contract)
    assert len(projected_list) == len(records)

    # Assert all IDs are preserved exactly and in the same order
    src_ids = [r["id"] for r in records]
    proj_ids = [p["id"] for p in projected_list]
    assert src_ids == proj_ids

    # Assert every projected key belongs to pinned contract.fields
    native_keys = set(contract.fields.keys())
    for item in projected_list:
        item_keys = set(item.keys())
        assert item_keys.issubset(native_keys)
        assert "is_refill" not in item
        assert "country_of_origin" not in item


def test_future_contract_field_behavior(sample_community_record):
    """9. Future contract field behavior: if contract adds a new native field, projection includes and validates it."""
    future_contract_source = """
from enum import Enum

from pydantic import BaseModel, Field, RootModel

class SpoolType(Enum):
    PLASTIC = "plastic"
    CARDBOARD = "cardboard"
    METAL = "metal"

class Finish(Enum):
    MATTE = "matte"

class MultiColorDirection(Enum):
    COAXIAL = "coaxial"

class Pattern(Enum):
    MARBLE = "marble"

class ExternalFilament(BaseModel):
    id: str = Field(description="A unique ID for this filament.")
    manufacturer: str = Field(description="Filament manufacturer.")
    name: str = Field(description="Filament name.")
    material: str = Field(description="Filament material.")
    density: float = Field(description="Density in g/cm3.")
    weight: float = Field(description="Net weight of a single spool.")
    diameter: float = Field(description="Diameter in mm.")
    sds_url: str | None = Field(default=None, description="Safety data sheet URL.")

class ExternalFilamentsFile(RootModel):
    root: list[ExternalFilament] = Field(...)
"""
    future_contract = load_spoolman_contract(future_contract_source)
    assert "sds_url" in future_contract.fields

    projected = project_single_record(sample_community_record, future_contract)
    assert projected["sds_url"] == "https://example.com/sds.pdf"
    assert "tds_url" not in projected
    assert "is_refill" not in projected
