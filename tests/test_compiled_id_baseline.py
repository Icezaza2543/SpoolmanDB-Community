"""Regression unit tests for Public Compiled ID baseline manifest checking."""

import json
from pathlib import Path
import tempfile
import pytest

from scripts.compile_id_baseline import (
    check_baseline_manifest,
    compile_current_id_manifest,
    make_canonical_identity_key,
)

ROOT = Path(__file__).parent.parent


def test_current_baseline_passes():
    """1. Current committed baseline passes against current source data."""
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

        # Create source filament
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

        # Create baseline with OLD ID
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

        # Baseline contains a variant that does not exist in source files
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
    """6. Simulating a new variant not in baseline passes and is counted as addition."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "baseline.json"

        # Baseline is empty
        baseline_payload = {"version": 1, "count": 0, "manifest": {}}
        baseline_file.write_text(json.dumps(baseline_payload), encoding="utf-8")

        # Source data has 1 filament
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


def test_malformed_or_duplicate_baseline_fails():
    """7. Malformed baseline file or missing manifest dictionary fails."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()

        # Non-existent baseline
        errors, _, _ = check_baseline_manifest(tmp_path / "non_existent.json", filaments_dir)
        assert any("Baseline file does not exist" in err for err in errors)

        # Invalid JSON
        bad_json_file = tmp_path / "bad.json"
        bad_json_file.write_text("{invalid_json", encoding="utf-8")
        errors, _, _ = check_baseline_manifest(bad_json_file, filaments_dir)
        assert any("Failed to parse baseline manifest" in err for err in errors)

        # Missing manifest key
        missing_key_file = tmp_path / "missing_manifest.json"
        missing_key_file.write_text(json.dumps({"version": 1}), encoding="utf-8")
        errors, _, _ = check_baseline_manifest(missing_key_file, filaments_dir)
        assert any("missing top-level 'manifest' dictionary" in err for err in errors)


def test_baseline_check_works_without_compiled_filaments_json():
    """8. Test baseline check works when generated/ignored filaments.json is absent."""
    # Run against repo filaments directory and baseline path without requiring filaments.json
    errors, warnings, stats = check_baseline_manifest(
        baseline_path=ROOT / "contracts" / "compiled_id_baseline.json",
        filaments_dir=ROOT / "filaments",
    )
    assert errors == []
    assert stats["matched"] == 51596


def test_baseline_check_does_not_rely_on_record_count_alone():
    """9. Baseline check fails if record count is identical but Public IDs were swapped."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        filaments_dir = tmp_path / "filaments"
        filaments_dir.mkdir()
        baseline_file = tmp_path / "baseline.json"

        # 2 filaments in source
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

        # Generate baseline with swapped IDs
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
        # Even though record count is 2 == 2, ID mismatch must fail
        assert stats["baseline_count"] == 2
        assert stats["current_count"] == 2
        assert stats["changed"] == 2
        assert len(errors) == 2
        assert any("Public ID regression detected for variant" in err for err in errors)
