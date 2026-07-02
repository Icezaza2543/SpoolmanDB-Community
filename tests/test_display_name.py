from scripts.display_name import (
    collect_ambiguous_display_name_warnings,
    get_display_name,
    material_appears_in_name,
)


def test_material_appears_in_name():
    assert material_appears_in_name("ABS Prime White", "ABS")
    assert material_appears_in_name("HT-PLA Red", "PLA")
    assert material_appears_in_name("EasyFil ePLA Red", "PLA") is False
    assert material_appears_in_name("Plus BLACK", "ABS") is False


def test_get_display_name():
    assert get_display_name("ABS Prime White", "ABS") == "ABS Prime White"
    assert get_display_name("Plus BLACK", "ABS") == "ABS Plus BLACK"
    assert get_display_name("ePLA Matte BLACK", "PLA") == "PLA ePLA Matte BLACK"


def test_collect_ambiguous_display_name_warnings(tmp_path):
    source = tmp_path / "AzureFilm.json"
    source.write_text(
        """
        {
            "manufacturer": "AzureFilm",
            "filaments": [
                {
                    "name": "Plus {color_name}",
                    "material": "ABS",
                    "density": 1.13,
                    "weights": [{"weight": 1000}],
                    "diameters": [1.75],
                    "colors": [{"name": "BLACK", "hex": "000000"}]
                }
            ]
        }
        """.strip(),
        encoding="utf-8",
    )

    warnings = collect_ambiguous_display_name_warnings(tmp_path)
    assert len(warnings) == 1
    assert "AzureFilm / ABS" in warnings[0]
    assert '"Plus {color_name}"' in warnings[0]
    assert 'compiles to "Plus BLACK"' in warnings[0]
    assert 'Explorer will display "ABS Plus BLACK"' in warnings[0]