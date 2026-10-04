"""Unit tests for semantic data integrity checks and GTIN validation."""

import json
from pathlib import Path
import pytest

from scripts.data_semantics import check_source_data_semantics, validate_gtin_checksum

ROOT = Path(__file__).parent.parent


def test_gtin_checksum_validation():
    # 1. GTIN-8 valid/invalid
    assert validate_gtin_checksum("01234565")
    assert not validate_gtin_checksum("01234560")

    # 2. GTIN-12 valid/invalid
    assert validate_gtin_checksum("012345678905")
    assert not validate_gtin_checksum("012345678900")

    # 3. GTIN-13 valid/invalid
    assert validate_gtin_checksum("4006381333931")
    assert not validate_gtin_checksum("4006381333930")

    # 4. GTIN-14 valid/invalid
    assert validate_gtin_checksum("10012345678902")
    assert not validate_gtin_checksum("10012345678900")

    # 5. Reject lengths 9, 10, 11 and non-numeric
    assert not validate_gtin_checksum("123456789")  # 9
    assert not validate_gtin_checksum("1234567890")  # 10
    assert not validate_gtin_checksum("12345678901")  # 11
    assert not validate_gtin_checksum("ABCDEFGH")


def test_eans_refill_validation(tmp_path):
    filaments_dir = tmp_path / "filaments"
    filaments_dir.mkdir()
    materials_file = tmp_path / "materials.json"

    materials_file.write_text(
        json.dumps([{"material": "PLA", "density": 1.24}]), encoding="utf-8"
    )

    data = {
        "manufacturer": "BrandA",
        "filaments": [
            {
                "name": "PLA {color_name}",
                "material": "PLA",
                "density": 1.24,
                "weights": [{"weight": 1000}],
                "diameters": [1.75],
                "colors": [
                    {
                        "name": "Red",
                        "hex": "FF0000",
                        "eans_refill": ["4006381333930"],  # invalid checksum GTIN-13
                    }
                ],
            }
        ],
    }
    (filaments_dir / "branda.json").write_text(json.dumps(data), encoding="utf-8")

    errors, warnings = check_source_data_semantics(filaments_dir, materials_file)
    assert len(errors) == 1
    assert "Invalid GTIN Mod-10 checksum" in errors[0]
    assert "eans_refill" in errors[0]


def test_material_referential_integrity(tmp_path):
    filaments_dir = tmp_path / "filaments"
    filaments_dir.mkdir()
    materials_file = tmp_path / "materials.json"

    materials_file.write_text(
        json.dumps([{"material": "PLA", "density": 1.24}]), encoding="utf-8"
    )

    # 7. Material in materials.json passes
    valid_data = {
        "manufacturer": "BrandA",
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
    (filaments_dir / "valid.json").write_text(json.dumps(valid_data), encoding="utf-8")
    errors, _ = check_source_data_semantics(filaments_dir, materials_file)
    assert errors == []

    # 8. Non-existent material fails
    invalid_data = {
        "manufacturer": "BrandB",
        "filaments": [
            {
                "name": "Unknown {color_name}",
                "material": "NON_EXISTENT_MATERIAL",
                "density": 1.24,
                "weights": [{"weight": 1000}],
                "diameters": [1.75],
                "colors": [{"name": "Red", "hex": "FF0000"}],
            }
        ],
    }
    (filaments_dir / "invalid.json").write_text(json.dumps(invalid_data), encoding="utf-8")
    errors, _ = check_source_data_semantics(filaments_dir, materials_file)
    assert any("references unknown material 'NON_EXISTENT_MATERIAL'" in e for e in errors)


def test_temperature_range_ordering(tmp_path):
    filaments_dir = tmp_path / "filaments"
    filaments_dir.mkdir()
    materials_file = tmp_path / "materials.json"

    materials_file.write_text(
        json.dumps([{"material": "PLA", "density": 1.24}]), encoding="utf-8"
    )

    # 9. Temperature range ordered correctly passes
    ordered_data = {
        "manufacturer": "BrandA",
        "filaments": [
            {
                "name": "PLA {color_name}",
                "material": "PLA",
                "extruder_temp_range": [190, 220],
                "bed_temp_range": [50, 60],
                "colors": [{"name": "Red", "hex": "FF0000"}],
            }
        ],
    }
    (filaments_dir / "ordered.json").write_text(json.dumps(ordered_data), encoding="utf-8")
    errors, _ = check_source_data_semantics(filaments_dir, materials_file)
    assert errors == []

    # 10. Temperature range reversed fails
    reversed_data = {
        "manufacturer": "BrandB",
        "filaments": [
            {
                "name": "PLA {color_name}",
                "material": "PLA",
                "extruder_temp_range": [220, 190],  # reversed
                "colors": [{"name": "Red", "hex": "FF0000"}],
            }
        ],
    }
    (filaments_dir / "reversed.json").write_text(json.dumps(reversed_data), encoding="utf-8")
    errors, _ = check_source_data_semantics(filaments_dir, materials_file)
    assert any("invalid extruder_temp_range [220, 190]: min > max" in e for e in errors)


def test_duplicate_manufacturer_casing(tmp_path):
    filaments_dir = tmp_path / "filaments"
    filaments_dir.mkdir()
    materials_file = tmp_path / "materials.json"

    materials_file.write_text(
        json.dumps([{"material": "PLA", "density": 1.24}]), encoding="utf-8"
    )

    # 11. Duplicate manufacturer with different casing fails
    (filaments_dir / "file1.json").write_text(
        json.dumps({"manufacturer": "MyBrand", "filaments": []}), encoding="utf-8"
    )
    (filaments_dir / "file2.json").write_text(
        json.dumps({"manufacturer": "mybrand", "filaments": []}), encoding="utf-8"
    )

    errors, _ = check_source_data_semantics(filaments_dir, materials_file)
    assert any("Duplicate manufacturer 'mybrand'" in e or "Duplicate manufacturer 'MyBrand'" in e for e in errors)


def test_duplicate_ean_reporting(tmp_path):
    filaments_dir = tmp_path / "filaments"
    filaments_dir.mkdir()
    materials_file = tmp_path / "materials.json"

    materials_file.write_text(
        json.dumps([{"material": "PLA", "density": 1.24}]), encoding="utf-8"
    )

    # 12. Duplicate EAN reporting as warning
    fil1 = {
        "manufacturer": "BrandA",
        "filaments": [
            {
                "name": "PLA {color_name}",
                "material": "PLA",
                "colors": [{"name": "Red", "hex": "FF0000", "eans": ["4006381333931"]}],
            }
        ],
    }
    fil2 = {
        "manufacturer": "BrandB",
        "filaments": [
            {
                "name": "PLA {color_name}",
                "material": "PLA",
                "colors": [{"name": "Red", "hex": "FF0000", "eans": ["4006381333931"]}],
            }
        ],
    }
    (filaments_dir / "f1.json").write_text(json.dumps(fil1), encoding="utf-8")
    (filaments_dir / "f2.json").write_text(json.dumps(fil2), encoding="utf-8")

    errors, warnings = check_source_data_semantics(filaments_dir, materials_file)
    assert errors == []
    assert len(warnings) == 1
    assert "Duplicate GTIN '4006381333931'" in warnings[0]


def test_country_of_origin_requires_iso_alpha2(tmp_path):
    filaments_dir = tmp_path / "filaments"
    filaments_dir.mkdir()
    materials_file = tmp_path / "materials.json"
    materials_file.write_text(
        json.dumps([{"material": "PLA", "density": 1.24}]), encoding="utf-8"
    )

    valid = {
        "manufacturer": "BrandA",
        "filaments": [
            {
                "name": "PLA {color_name}",
                "material": "PLA",
                "density": 1.24,
                "weights": [{"weight": 1000}],
                "diameters": [1.75],
                "colors": [{"name": "Red", "hex": "FF0000"}],
                "country_of_origin": "CN",
            }
        ],
    }
    (filaments_dir / "valid.json").write_text(json.dumps(valid), encoding="utf-8")
    errors, _ = check_source_data_semantics(filaments_dir, materials_file)
    assert errors == []

    invalid = {
        "manufacturer": "BrandB",
        "filaments": [
            {
                "name": "PLA {color_name}",
                "material": "PLA",
                "density": 1.24,
                "weights": [{"weight": 1000}],
                "diameters": [1.75],
                "colors": [{"name": "Red", "hex": "FF0000"}],
                "country_of_origin": "China",
            }
        ],
    }
    (filaments_dir / "invalid.json").write_text(json.dumps(invalid), encoding="utf-8")
    errors, _ = check_source_data_semantics(filaments_dir, materials_file)
    assert any("invalid country_of_origin 'China'" in e for e in errors)
    assert any("ISO 3166-1 alpha-2" in e for e in errors)


def test_existing_repository_passes_semantics():
    # 13. Existing repository passes all semantic checks
    filaments_dir = ROOT / "filaments"
    materials_file = ROOT / "materials.json"

    errors, warnings = check_source_data_semantics(filaments_dir, materials_file)
    assert errors == []
    assert_reviewed_gtin_warnings(ROOT, warnings)


def assert_reviewed_gtin_warnings(root, warnings):
    from scripts.duplicate_catalog import catalog_records
    import re
    rows = catalog_records(root)
    approved_values = set()
    audited_brands = set()
    for path in sorted((root / "docs/audits").glob("2026-10-04-*-owner-closure.json")):
        review = json.loads(path.read_text(encoding="utf-8"))
        contract = review.get("identifier_bindings_after")
        if contract is None:
            continue
        assert review["version"] == 1 and review["approved"] is True
        brand = review["brand"]
        assert brand not in audited_brands
        audited_brands.add(brand)
        current = [row["record"] for row in rows if row["filename"] == brand + ".json"]
        assert set(contract) == {"eans", "eans_refill"}
        for field, expected in contract.items():
            actual = {}
            for record in current:
                for value in record.get(field) or []:
                    actual.setdefault(value, []).append(record["id"])
            assert {value: sorted(ids) for value, ids in actual.items()} == expected
            for value, ids in expected.items():
                assert sorted(row["record"]["id"] for row in rows
                    if value in (row["record"].get(field) or [])) == ids
            approved_values.update(expected)
    for warning in warnings:
        match = re.match(r"Duplicate GTIN '([0-9]+)'", warning)
        assert match and match.group(1) in approved_values, warning


@pytest.mark.parametrize("extra_weight", [False, True, "other_brand"])
def test_reviewed_definition_split_accepts_only_exact_gtin_target_ids(tmp_path, extra_weight):
    (tmp_path / "filaments").mkdir()
    (tmp_path / "docs/audits").mkdir(parents=True)
    (tmp_path / "contracts").mkdir()
    (tmp_path / "contracts/retired_ids.json").write_text(json.dumps({"version": 1, "retired": {}}))
    definition = {"name": "PLA {color_name}", "material": "PLA", "density": 1.24,
        "diameters": [1.75], "colors": [{"name": "Black", "hex": "000000", "eans": ["4006381333931"]}]}
    weights = [750, 1000] + ([2000] if extra_weight is True else [])
    (tmp_path / "filaments/acme.json").write_text(json.dumps({"manufacturer": "Acme", "filaments": [
        {**definition, "weights": [{"weight": weight, "spool_type": "plastic"}]} for weight in weights]}))
    (tmp_path / "materials.json").write_text(json.dumps([{"material": "PLA"}]))
    if extra_weight == "other_brand":
        (tmp_path / "filaments/other.json").write_text(json.dumps({"manufacturer": "Other", "filaments": [
            {**definition, "weights": [{"weight": 1000, "spool_type": "plastic"}]}]}))
    (tmp_path / "docs/audits/2026-10-04-acme-owner-closure.json").write_text(json.dumps({
        "version": 1, "approved": True, "brand": "acme", "identifier_bindings_after": {
            "eans": {"4006381333931": ["acme_pla_plablack_1000_175_p", "acme_pla_plablack_750_175_p"]},
            "eans_refill": {}}}))
    errors, warnings = check_source_data_semantics(tmp_path / "filaments", tmp_path / "materials.json")
    assert errors == []
    assert len(warnings) == 1
    if extra_weight:
        with pytest.raises(AssertionError):
            assert_reviewed_gtin_warnings(tmp_path, warnings)
    else:
        assert_reviewed_gtin_warnings(tmp_path, warnings)


def test_compiled_public_ids_are_unique():
    from scripts.compile_filaments import expand_filament_data, load_json

    filaments_dir = ROOT / "filaments"
    compiled_records = []
    for fpath in sorted(filaments_dir.glob("*.json")):
        data = load_json(fpath)
        mfr = data.get("manufacturer")
        for fil in data.get("filaments", []):
            compiled_records.extend(expand_filament_data(mfr, fil))

    id_set = {item["id"] for item in compiled_records}
    assert len(id_set) == len(compiled_records)
