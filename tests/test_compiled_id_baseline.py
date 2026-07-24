"""Comprehensive unit tests for Public Compiled ID baseline manifest checking and update safety."""

import json
from pathlib import Path
import tempfile
import pytest

from scripts.compile_id_baseline import (
    check_baseline_manifest,
    compile_current_id_manifest,
    make_canonical_identity_key,
    write_baseline_manifest,
    write_baseline_manifest_atomic,
)

ROOT = Path(__file__).parent.parent


def test_current_baseline_passes():
    """1. Current committed baseline passes against repository source files."""
    errors, warnings, stats = check_baseline_manifest(
        baseline_path=ROOT / "contracts" / "compiled_id_baseline.json",
        filaments_dir=ROOT / "filaments",
    )
    assert errors == []
    assert stats["baseline_count"] == 51596
    assert stats["current_count"] == 51596
    assert stats["matched"] == 51596
    assert stats["changed"] == 0
    assert stats["missing"] == 0


def test_compiled_public_ids_are_unique():
    """2. Compiled Public IDs are unique across all variants compiled in memory."""
    current_manifest, errors = compile_current_id_manifest(ROOT / "filaments")
    assert errors == []
    assert len(current_manifest) == 51596
    id_set = set(current_manifest.values())
    assert len(id_set) == 51596


def test_identity_keys_are_unique():
    """3. Canonical identity keys are unique across all variants compiled in memory."""
    current_manifest, errors = compile_current_id_manifest(ROOT / "filaments")
    assert errors == []
    assert len(current_manifest) == 51596


def test_simulated_id_change_fails():
    """4. Simulating a change in Public ID for an existing identity key fails."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "baseline.json"

        fil_data = {
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
        (filaments_dir / "branda.json").write_text(json.dumps(fil_data), encoding="utf-8")

        ckey = make_canonical_identity_key(
            "branda.json", "BrandA", "PLA {color_name}", "PLA Red", "PLA", 1000, 1.75, None, False
        )
        baseline_payload = {
            "version": 1,
            "count": 1,
            "manifest": {ckey: "old_historical_id_123"},
        }
        baseline_file.write_text(json.dumps(baseline_payload), encoding="utf-8")

        errors, warnings, stats = check_baseline_manifest(baseline_file, filaments_dir)
        assert stats["changed"] == 1
        assert any("Public ID regression detected for variant" in err for err in errors)
        assert any("old_historical_id_123" in err for err in errors)


def test_simulated_missing_variant_fails():
    """5. Simulating a missing baseline variant in current source fails."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "baseline.json"

        missing_ckey = "deleted.json::BrandX::PLA {color_name}::PLA Blue::PLA::1000::1.75::None::False"
        baseline_payload = {
            "version": 1,
            "count": 1,
            "manifest": {missing_ckey: "brandx_pla_plablue_1000_175_n"},
        }
        baseline_file.write_text(json.dumps(baseline_payload), encoding="utf-8")

        errors, warnings, stats = check_baseline_manifest(baseline_file, filaments_dir)
        assert stats["missing"] == 1
        assert any("Historical baseline variant missing from current source data" in err for err in errors)
        assert any(missing_ckey in err for err in errors)


def test_simulated_new_variant_passes_as_addition():
    """6. Simulating a new variant not in baseline passes check mode with clear warning."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "baseline.json"

        baseline_payload = {"version": 1, "count": 0, "manifest": {}}
        baseline_file.write_text(json.dumps(baseline_payload), encoding="utf-8")

        fil_data = {
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
        (filaments_dir / "branda.json").write_text(json.dumps(fil_data), encoding="utf-8")

        errors, warnings, stats = check_baseline_manifest(baseline_file, filaments_dir)
        assert errors == []
        assert stats["added"] == 1
        assert len(warnings) == 1
        assert "New variant added (not in baseline)" in warnings[0]
        assert "Note: New variants are not protected against historical ID regression" in warnings[0]


def test_missing_baseline_file_fails():
    """7. Missing baseline file fails with clear error."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()

        errors, _, _ = check_baseline_manifest(tmp_path / "non_existent.json", filaments_dir)
        assert any("Baseline file does not exist" in err for err in errors)


def test_invalid_json_baseline_fails():
    """8. Syntax error in baseline JSON fails with clear error."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()

        bad_json_file = tmp_path / "bad.json"
        bad_json_file.write_text("{invalid_json: 123", encoding="utf-8")
        errors, _, _ = check_baseline_manifest(bad_json_file, filaments_dir)
        assert any("Failed to parse baseline manifest" in err for err in errors)


def test_duplicate_top_level_json_key_fails():
    """9. Duplicate top-level JSON key in baseline fails."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "dup_top.json"

        raw_json = '{\n  "version": 1,\n  "version": 1,\n  "count": 0,\n  "manifest": {}\n}'
        baseline_file.write_text(raw_json, encoding="utf-8")

        errors, _, _ = check_baseline_manifest(baseline_file, filaments_dir)
        assert any("Duplicate JSON key detected: 'version'" in err for err in errors)


def test_duplicate_manifest_identity_key_fails():
    """10. Duplicate manifest identity key in baseline fails."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "dup_manifest.json"

        raw_json = '{\n  "version": 1,\n  "count": 2,\n  "manifest": {\n    "k1": "id1",\n    "k1": "id2"\n  }\n}'
        baseline_file.write_text(raw_json, encoding="utf-8")

        errors, _, _ = check_baseline_manifest(baseline_file, filaments_dir)
        assert any("Duplicate JSON key detected: 'k1'" in err for err in errors)


def test_unsupported_version_fails():
    """11. Baseline version != 1 fails."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "bad_ver.json"

        baseline_file.write_text(json.dumps({"version": 2, "count": 0, "manifest": {}}), encoding="utf-8")
        errors, _, _ = check_baseline_manifest(baseline_file, filaments_dir)
        assert any("unsupported version 2" in err for err in errors)


def test_version_type_invalid_fails():
    """12. Non-integer or boolean version fails."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "bad_ver_type.json"

        baseline_file.write_text(json.dumps({"version": True, "count": 0, "manifest": {}}), encoding="utf-8")
        errors, _, _ = check_baseline_manifest(baseline_file, filaments_dir)
        assert any("'version' field must be an integer, got bool" in err for err in errors)


def test_count_negative_fails():
    """13. Negative count fails."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "neg_count.json"

        baseline_file.write_text(json.dumps({"version": 1, "count": -1, "manifest": {}}), encoding="utf-8")
        errors, _, _ = check_baseline_manifest(baseline_file, filaments_dir)
        assert any("'count' field cannot be negative" in err for err in errors)


def test_count_type_invalid_fails():
    """14. Non-integer or boolean count fails."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "bad_count_type.json"

        baseline_file.write_text(json.dumps({"version": 1, "count": "0", "manifest": {}}), encoding="utf-8")
        errors, _, _ = check_baseline_manifest(baseline_file, filaments_dir)
        assert any("'count' field must be a non-negative integer, got str" in err for err in errors)


def test_count_mismatch_fails():
    """15. Count field not matching manifest entry count fails."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "mismatch_count.json"

        baseline_file.write_text(json.dumps({"version": 1, "count": 99, "manifest": {}}), encoding="utf-8")
        errors, _, _ = check_baseline_manifest(baseline_file, filaments_dir)
        assert any("'count' field (99) does not match actual manifest entry count (0)" in err for err in errors)


def test_manifest_not_object_fails():
    """16. Manifest field not being a JSON object fails."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "bad_manifest_obj.json"

        baseline_file.write_text(json.dumps({"version": 1, "count": 0, "manifest": []}), encoding="utf-8")
        errors, _, _ = check_baseline_manifest(baseline_file, filaments_dir)
        assert any("'manifest' field must be a JSON object" in err for err in errors)


def test_empty_or_non_string_identity_key_fails():
    """17. Empty string or non-string identity key in manifest fails."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "empty_key.json"

        baseline_file.write_text(json.dumps({"version": 1, "count": 1, "manifest": {"": "some_id"}}), encoding="utf-8")
        errors, _, _ = check_baseline_manifest(baseline_file, filaments_dir)
        assert any("manifest identity keys must be non-empty strings" in err for err in errors)


def test_empty_or_non_string_public_id_fails():
    """18. Empty string or non-string Public ID in manifest fails."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "empty_val.json"

        baseline_file.write_text(json.dumps({"version": 1, "count": 1, "manifest": {"ckey1": ""}}), encoding="utf-8")
        errors, _, _ = check_baseline_manifest(baseline_file, filaments_dir)
        assert any("manifest Public ID for variant 'ckey1' must be a non-empty string" in err for err in errors)


def test_duplicate_public_ids_in_baseline_fails():
    """19. Two different identity keys mapping to the same Public ID in baseline fails."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "dup_ids.json"

        payload = {
            "version": 1,
            "count": 2,
            "manifest": {
                "ckey1": "shared_public_id",
                "ckey2": "shared_public_id",
            },
        }
        baseline_file.write_text(json.dumps(payload), encoding="utf-8")
        errors, _, _ = check_baseline_manifest(baseline_file, filaments_dir)
        assert any("Duplicate Public ID 'shared_public_id' found in baseline for different identity keys" in err for err in errors)


def test_baseline_check_works_without_compiled_filaments_json():
    """20. Test baseline check works when generated/ignored filaments.json is absent."""
    errors, warnings, stats = check_baseline_manifest(
        baseline_path=ROOT / "contracts" / "compiled_id_baseline.json",
        filaments_dir=ROOT / "filaments",
    )
    assert errors == []
    assert stats["matched"] == 51596


def test_baseline_check_does_not_rely_on_record_count_alone():
    """21. Baseline check fails if record count is identical but Public IDs were swapped."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "baseline.json"

        fil_data = {
            "manufacturer": "BrandA",
            "filaments": [
                {
                    "name": "PLA {color_name}",
                    "material": "PLA",
                    "density": 1.24,
                    "weights": [{"weight": 1000}],
                    "diameters": [1.75],
                    "colors": [
                        {"name": "Red", "hex": "FF0000"},
                        {"name": "Blue", "hex": "0000FF"},
                    ],
                }
            ],
        }
        (filaments_dir / "branda.json").write_text(json.dumps(fil_data), encoding="utf-8")

        current_manifest, _ = compile_current_id_manifest(filaments_dir)
        keys = list(current_manifest.keys())
        swapped_manifest = {
            keys[0]: current_manifest[keys[1]],
            keys[1]: current_manifest[keys[0]],
        }
        baseline_payload = {
            "version": 1,
            "count": len(swapped_manifest),
            "manifest": swapped_manifest,
        }
        baseline_file.write_text(json.dumps(baseline_payload), encoding="utf-8")

        errors, warnings, stats = check_baseline_manifest(baseline_file, filaments_dir)
        assert stats["baseline_count"] == 2
        assert stats["current_count"] == 2
        assert stats["changed"] == 2
        assert len(errors) == 2
        assert any("Public ID regression detected for variant" in err for err in errors)


def test_update_additions_only_succeeds():
    """22. Baseline --update succeeds when only additions are present."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "baseline.json"

        fil_data = {
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
        (filaments_dir / "branda.json").write_text(json.dumps(fil_data), encoding="utf-8")

        # Initial baseline write
        write_baseline_manifest(baseline_file, filaments_dir)
        assert baseline_file.exists()
        _, _, stats1 = check_baseline_manifest(baseline_file, filaments_dir)
        assert stats1["baseline_count"] == 1

        # Add second color
        fil_data["filaments"][0]["colors"].append({"name": "Blue", "hex": "0000FF"})
        (filaments_dir / "branda.json").write_text(json.dumps(fil_data), encoding="utf-8")

        # Additions-only update should succeed without breaking flag
        write_baseline_manifest(baseline_file, filaments_dir, accept_breaking_changes=False)
        _, _, stats2 = check_baseline_manifest(baseline_file, filaments_dir)
        assert stats2["baseline_count"] == 2
        assert stats2["matched"] == 2


def test_update_rejects_changed_id_without_flag():
    """23. Baseline --update rejects updating when a historical ID changes unless breaking flag is given."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "baseline.json"

        fil_data = {
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
        (filaments_dir / "branda.json").write_text(json.dumps(fil_data), encoding="utf-8")
        write_baseline_manifest(baseline_file, filaments_dir)

        # Manually alter ID in baseline file
        raw = json.loads(baseline_file.read_text(encoding="utf-8"))
        ckey = list(raw["manifest"].keys())[0]
        raw["manifest"][ckey] = "altered_id"
        baseline_file.write_text(json.dumps(raw), encoding="utf-8")

        # Without flag, write_baseline_manifest should sys.exit(1)
        with pytest.raises(SystemExit) as exc_info:
            write_baseline_manifest(baseline_file, filaments_dir, accept_breaking_changes=False)
        assert exc_info.value.code == 1


def test_update_rejects_missing_variant_without_flag():
    """24. Baseline --update rejects updating when a historical variant is missing unless breaking flag is given."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "baseline.json"

        fil_data = {
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
        (filaments_dir / "branda.json").write_text(json.dumps(fil_data), encoding="utf-8")
        write_baseline_manifest(baseline_file, filaments_dir)

        # Delete source file
        (filaments_dir / "branda.json").unlink()

        # Without flag, write_baseline_manifest should sys.exit(1)
        with pytest.raises(SystemExit) as exc_info:
            write_baseline_manifest(baseline_file, filaments_dir, accept_breaking_changes=False)
        assert exc_info.value.code == 1


def test_update_accepts_breaking_changes_with_flag():
    """25. Baseline --update accepts breaking changes when accept_breaking_changes=True."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "baseline.json"

        fil_data = {
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
        (filaments_dir / "branda.json").write_text(json.dumps(fil_data), encoding="utf-8")
        write_baseline_manifest(baseline_file, filaments_dir)

        # Remove source file
        (filaments_dir / "branda.json").unlink()

        # With breaking flag, update should succeed
        write_baseline_manifest(baseline_file, filaments_dir, accept_breaking_changes=True)
        _, _, stats = check_baseline_manifest(baseline_file, filaments_dir)
        assert stats["baseline_count"] == 0


def test_write_baseline_atomic_safety():
    """26. Atomic write leaves target baseline file undamaged if validation or payload fails."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        baseline_file = tmp_path / "baseline.json"

        # Create original valid baseline
        original_payload = {"version": 1, "count": 0, "manifest": {}}
        write_baseline_manifest_atomic(original_payload, baseline_file)
        assert baseline_file.exists()
        original_content = baseline_file.read_text(encoding="utf-8")

        # Attempt atomic write of invalid payload
        invalid_payload = {"version": 999, "count": 0, "manifest": {}}
        with pytest.raises(ValueError) as exc_info:
            write_baseline_manifest_atomic(invalid_payload, baseline_file)
        assert "Refusing to write invalid baseline payload" in str(exc_info.value)

        # Target file must remain untouched and intact
        assert baseline_file.read_text(encoding="utf-8") == original_content
