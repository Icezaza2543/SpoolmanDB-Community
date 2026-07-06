import pytest
from scripts.compile_filaments import (
    expand_filament_data,
    generate_id,
    SpoolType,
    Finish,
    MultiColorDirection,
    normalize_spool_type_for_spoolman,
)

def test_generate_id_normalization():
    # Test lowercase, ascii-stripping, and space removal
    result = generate_id(
        manufacturer="Bambu Lab",
        name="PLA Basic 🔵 Blue",
        material="PLA",
        weight=1000.0,
        diameter=1.75,
        spool_type=SpoolType.PLASTIC
    )
    # "🔵" is non-ascii, so encoded to ascii with ignore becomes ""
    # Spaces are stripped. everything becomes lowercase.
    assert result == "bambulab_pla_plabasicblue_1000_175_p"

def test_generate_id_no_spool_type():
    result = generate_id(
        manufacturer="Generic",
        name="Standard",
        material="PETG",
        weight=750.0,
        diameter=2.85,
        spool_type=None
    )
    assert result == "generic_petg_standard_750_285_n"

def test_expand_filament_data_invalid_hex():
    # Neither hex nor hexes specified
    filament_data = {
        "name": "Test PLA",
        "material": "PLA",
        "density": 1.24,
        "weights": [{"weight": 1000}],
        "diameters": [1.75],
        "colors": [{"name": "Red"}] # missing hex and hexes
    }
    with pytest.raises(ValueError, match="has no hex or hexes specified"):
        list(expand_filament_data("Test Brand", filament_data))

    # Both hex and hexes specified
    filament_data["colors"][0] = {
        "name": "Red",
        "hex": "FF0000",
        "hexes": ["FF0000", "00FF00"]
    }
    with pytest.raises(ValueError, match="has both hex and hexes specified"):
        list(expand_filament_data("Test Brand", filament_data))

def test_expand_filament_data_invalid_multicolor():
    # hexes specified but no direction
    filament_data = {
        "name": "Test PLA",
        "material": "PLA",
        "density": 1.24,
        "weights": [{"weight": 1000}],
        "diameters": [1.75],
        "colors": [{
            "name": "Multi",
            "hexes": ["FF0000", "00FF00"]
        }]
    }
    with pytest.raises(ValueError, match="has hexes specified but no multi_color_direction is set"):
        list(expand_filament_data("Test Brand", filament_data))

    # direction specified but no hexes
    filament_data["colors"][0] = {
        "name": "Single",
        "hex": "FF0000",
        "multi_color_direction": MultiColorDirection.COAXIAL
    }
    with pytest.raises(ValueError, match="has no hexes specified but multi_color_direction is set"):
        list(expand_filament_data("Test Brand", filament_data))

def test_expand_filament_data_valid():
    filament_data = {
        "name": "Super {color_name} PLA",
        "material": "PLA",
        "density": 1.24,
        "weights": [
            {"weight": 1000.0, "spool_weight": 250.0, "spool_type": SpoolType.PLASTIC},
            {"weight": 500.0}
        ],
        "diameters": [1.75, 2.85],
        "colors": [
            {"name": "Fire Red", "hex": "FF0000", "finish": Finish.GLOSSY},
            {"name": "Matte Black", "hex": "000000", "finish": Finish.MATTE}
        ]
    }
    results = list(expand_filament_data("BrandX", filament_data))
    
    # Total combinations = 2 weights * 2 diameters * 2 colors = 8 filaments
    assert len(results) == 8
    
    first = results[0]
    assert first["manufacturer"] == "BrandX"
    assert first["name"] == "Super Fire Red PLA"
    assert first["id"] == "brandx_pla_superfireredpla_1000_175_p"
    assert first["weight"] == 1000.0
    assert first["spool_weight"] == 250.0
    assert first["spool_type"] == SpoolType.PLASTIC
    assert first["diameter"] == 1.75
    assert first["color_hex"] == "FF0000"
    assert first["finish"] == Finish.GLOSSY


def test_expand_filament_data_upstream_compatible_name():
    """Compiled name must stay template + color only; material remains a separate field."""
    filament_data = {
        "name": "Plus {color_name}",
        "material": "ABS",
        "density": 1.04,
        "weights": [{"weight": 1000, "spool_type": SpoolType.PLASTIC}],
        "diameters": [1.75],
        "colors": [{"name": "BLACK", "hex": "000000"}],
    }
    result = list(expand_filament_data("AzureFilm", filament_data))[0]
    assert result["name"] == "Plus BLACK"
    assert result["material"] == "ABS"
    assert result["id"] == "azurefilm_abs_plusblack_1000_175_p"


def test_spool_type_normalization_and_id_stability():
    # Test normalization helper
    assert normalize_spool_type_for_spoolman(SpoolType.REFILL) is None
    assert normalize_spool_type_for_spoolman(SpoolType.UNKNOW) is None
    assert normalize_spool_type_for_spoolman("refill") is None
    assert normalize_spool_type_for_spoolman("unknow") is None
    assert normalize_spool_type_for_spoolman("unknown") is None
    assert normalize_spool_type_for_spoolman(None) is None
    
    assert normalize_spool_type_for_spoolman(SpoolType.PLASTIC) == "plastic"
    assert normalize_spool_type_for_spoolman(SpoolType.CARDBOARD) == "cardboard"
    assert normalize_spool_type_for_spoolman(SpoolType.METAL) == "metal"
    assert normalize_spool_type_for_spoolman("plastic") == "plastic"
    assert normalize_spool_type_for_spoolman("cardboard") == "cardboard"
    assert normalize_spool_type_for_spoolman("metal") == "metal"
    
    # Test expand_filament_data with refill, unknow, metal, plastic, cardboard, and unknown
    filament_data = {
        "name": "{color_name} PLA",
        "material": "PLA",
        "density": 1.24,
        "weights": [
            {"weight": 1000.0, "spool_type": SpoolType.REFILL},
            {"weight": 1000.0, "spool_type": SpoolType.UNKNOW},
            {"weight": 1000.0, "spool_type": SpoolType.METAL},
            {"weight": 1000.0, "spool_type": SpoolType.PLASTIC},
            {"weight": 1000.0, "spool_type": SpoolType.CARDBOARD},
            {"weight": 1000.0, "spool_type": "unknown"}
        ],
        "diameters": [1.75],
        "colors": [
            {"name": "Red", "hex": "FF0000"}
        ]
    }
    
    results = list(expand_filament_data("TestBrand", filament_data))
    assert len(results) == 6
    
    # 1. refill -> normalized to None, ID suffix remains _r
    assert results[0]["spool_type"] is None
    assert results[0]["id"] == "testbrand_pla_redpla_1000_175_r"
    
    # 2. unknow -> normalized to None, ID suffix remains _u
    assert results[1]["spool_type"] is None
    assert results[1]["id"] == "testbrand_pla_redpla_1000_175_u"
    
    # 3. metal -> kept as metal, ID suffix is _m
    assert results[2]["spool_type"] == "metal"
    assert results[2]["id"] == "testbrand_pla_redpla_1000_175_m"
    
    # 4. plastic -> kept as plastic, ID suffix is _p
    assert results[3]["spool_type"] == "plastic"
    assert results[3]["id"] == "testbrand_pla_redpla_1000_175_p"
    
    # 5. cardboard -> kept as cardboard, ID suffix is _c
    assert results[4]["spool_type"] == "cardboard"
    assert results[4]["id"] == "testbrand_pla_redpla_1000_175_c"
    
    # 6. unknown (string) -> normalized to None, ID suffix falls back to _n
    assert results[5]["spool_type"] is None
    assert results[5]["id"] == "testbrand_pla_redpla_1000_175_n"

    # 7. unexpected invalid spool type -> raises KeyError
    with pytest.raises(KeyError):
        generate_id(
            manufacturer="TestBrand",
            name="PLA",
            material="PLA",
            weight=1000.0,
            diameter=1.75,
            spool_type="invalid_value"
        )