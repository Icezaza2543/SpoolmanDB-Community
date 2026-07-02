import pytest
from scripts.compile_filaments import (
    expand_filament_data,
    generate_id,
    SpoolType,
    Finish,
    MultiColorDirection,
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