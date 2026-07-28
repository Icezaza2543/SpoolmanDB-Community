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
        "extruder_temp": 210,
        "bed_temp": 60,
        "finish": "matte",
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

    # Extension fields stripped
    extension_keys = {"is_refill", "country_of_origin", "sds_url", "tds_url", "codes", "eans", "eans_refill", "extra_community_field"}
    for ext_key in extension_keys:
        assert ext_key not in projected, f"Extension key '{ext_key}' was not stripped from projected output"


def test_required_field_missing_fails():
    """2. Projection fails if a required native field is missing from record."""
    contract = get_native_contract()
    incomplete_record = {
        # Missing required 'id' or 'name' or 'material'
        "manufacturer": "BrandA",
        "density": 1.24,
    }

    with pytest.raises(ValueError, match="missing required native field"):
        project_single_record(incomplete_record, contract)


def test_required_field_none_fails():
    """3. Projection fails if a required native field is None."""
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
    """4. Projection fails if spool_type is invalid according to contract SpoolType enum."""
    contract = get_native_contract()
    bad_record = dict(sample_community_record)
    bad_record["spool_type"] = "invalid_type_wood"

    with pytest.raises(ValueError, match="invalid spool_type 'invalid_type_wood'"):
        project_single_record(bad_record, contract)


def test_project_compiled_records_full_dataset():
    """5. Verify project_compiled_records projects compiled filaments.json without error."""
    assert FILAMENTS_JSON_PATH.exists()
    records = json.loads(FILAMENTS_JSON_PATH.read_text(encoding="utf-8"))
    contract = get_native_contract()

    projected_list = project_compiled_records(records[:100], contract)
    assert len(projected_list) == 100

    # Ensure every projected item only contains native fields
    native_keys = set(contract.fields.keys())
    for item in projected_list:
        item_keys = set(item.keys())
        assert item_keys.issubset(native_keys)
        assert "is_refill" not in item
        assert "country_of_origin" not in item


def test_future_contract_field_behavior(sample_community_record):
    """6. Future contract field behavior: if contract adds a new native field, projection includes it."""
    # Custom contract source simulating a future Spoolman version with new field 'sds_url'
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
