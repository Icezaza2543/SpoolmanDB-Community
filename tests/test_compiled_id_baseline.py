"""Comprehensive unit tests for Public Compiled ID baseline manifest checking, malformed protection, and atomic update safety."""

import json
import os
from pathlib import Path
import tempfile
import pytest

from scripts.compile_id_baseline import (
    check_baseline_manifest,
    check_baseline_manifest_detailed,
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
    assert stats["baseline_count"] == 51626
    assert stats["current_count"] == 51626
    assert stats["matched"] == 51626
    assert stats["changed"] == 0
    assert stats["missing"] == 0


def test_compiled_public_ids_are_unique():
    """2. Compiled Public IDs are unique across all variants compiled in memory."""
    current_manifest, errors = compile_current_id_manifest(ROOT / "filaments")
    assert errors == []
    assert len(current_manifest) == 51626
    id_set = set(current_manifest.values())
    assert len(id_set) == 51626


def test_identity_keys_are_unique():
    """3. Canonical identity keys are unique across all variants compiled in memory."""
    current_manifest, errors = compile_current_id_manifest(ROOT / "filaments")
    assert errors == []
    assert len(current_manifest) == 51626


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
    assert stats["matched"] == 51626


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


def test_update_refuses_malformed_baselines(tmp_path):
    """22-28. --update refuses to overwrite malformed baselines even with --accept-breaking-baseline-changes."""
    filaments_dir = tmp_path / "filaments"
    filaments_dir.mkdir()

    malformed_cases = [
        ("invalid_json", "{invalid json syntax: 123"),
        ("dup_top_key", '{\n "version": 1,\n "version": 1,\n "count": 0,\n "manifest": {}\n}'),
        ("dup_manifest_key", '{\n "version": 1,\n "count": 2,\n "manifest": {"k1":"id1", "k1":"id2"}\n}'),
        ("unsupported_version", json.dumps({"version": 99, "count": 0, "manifest": {}})),
        ("count_mismatch", json.dumps({"version": 1, "count": 999, "manifest": {}})),
        ("duplicate_public_id", json.dumps({"version": 1, "count": 2, "manifest": {"k1": "id1", "k2": "id1"}})),
        ("invalid_manifest_type", json.dumps({"version": 1, "count": 0, "manifest": [1, 2, 3]})),
    ]

    for case_name, raw_content in malformed_cases:
        baseline_file = tmp_path / f"malformed_{case_name}.json"
        baseline_file.write_text(raw_content, encoding="utf-8")
        original_bytes = baseline_file.read_bytes()

        # Without breaking flag
        with pytest.raises(SystemExit) as exc1:
            write_baseline_manifest(baseline_file, filaments_dir, accept_breaking_changes=False)
        assert exc1.value.code == 1
        assert baseline_file.read_bytes() == original_bytes

        # WITH breaking flag (breaking flag CANNOT bypass malformed baseline!)
        with pytest.raises(SystemExit) as exc2:
            write_baseline_manifest(baseline_file, filaments_dir, accept_breaking_changes=True)
        assert exc2.value.code == 1
        assert baseline_file.read_bytes() == original_bytes

        # Verify no temp files left behind
        temp_files = list(tmp_path.glob(".malformed_*.tmp"))
        assert temp_files == []


def test_fresh_baseline_creation(tmp_path):
    """29. Fresh baseline file creation when baseline does not exist."""
    filaments_dir = tmp_path / "filaments"
    filaments_dir.mkdir()
    baseline_file = tmp_path / "fresh_baseline.json"

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

    assert not baseline_file.exists()
    write_baseline_manifest(baseline_file, filaments_dir)
    assert baseline_file.exists()

    errors, warnings, stats = check_baseline_manifest(baseline_file, filaments_dir)
    assert errors == []
    assert stats["matched"] == 1


def test_atomic_write_failure_json_dump_error(tmp_path, monkeypatch):
    """30. Atomic write failure during json.dump leaves target baseline untouched and cleans up temp file."""
    baseline_file = tmp_path / "target_baseline.json"
    original_payload = {"version": 1, "count": 0, "manifest": {}}
    write_baseline_manifest_atomic(original_payload, baseline_file)
    original_bytes = baseline_file.read_bytes()

    def mock_dump(*args, **kwargs):
        raise OSError("Simulated JSON dump disk failure")

    monkeypatch.setattr(json, "dump", mock_dump)

    with pytest.raises(RuntimeError) as exc_info:
        write_baseline_manifest_atomic({"version": 1, "count": 0, "manifest": {}}, baseline_file)

    assert "Simulated JSON dump disk failure" in str(exc_info.value)
    assert baseline_file.read_bytes() == original_bytes
    assert list(tmp_path.glob(".target_baseline.json.*.tmp")) == []


def test_atomic_write_failure_flush_error(tmp_path, monkeypatch):
    """31. Atomic write failure during flush leaves target baseline untouched and cleans up temp file."""
    baseline_file = tmp_path / "target_baseline.json"
    original_payload = {"version": 1, "count": 0, "manifest": {}}
    write_baseline_manifest_atomic(original_payload, baseline_file)
    original_bytes = baseline_file.read_bytes()

    real_named_tempfile = tempfile.NamedTemporaryFile

    def mock_named_tempfile(*args, **kwargs):
        f = real_named_tempfile(*args, **kwargs)
        f.flush = lambda: (_ for _ in ()).throw(OSError("Simulated flush failure"))
        return f

    monkeypatch.setattr(tempfile, "NamedTemporaryFile", mock_named_tempfile)

    with pytest.raises(RuntimeError) as exc_info:
        write_baseline_manifest_atomic({"version": 1, "count": 0, "manifest": {}}, baseline_file)

    assert "Simulated flush failure" in str(exc_info.value)
    assert baseline_file.read_bytes() == original_bytes
    assert list(tmp_path.glob(".target_baseline.json.*.tmp")) == []


def test_atomic_write_failure_fsync_error(tmp_path, monkeypatch):
    """32. Atomic write failure during os.fsync leaves target baseline untouched and cleans up temp file."""
    baseline_file = tmp_path / "target_baseline.json"
    original_payload = {"version": 1, "count": 0, "manifest": {}}
    write_baseline_manifest_atomic(original_payload, baseline_file)
    original_bytes = baseline_file.read_bytes()

    def mock_fsync(fd):
        raise OSError("Simulated fsync I/O failure")

    monkeypatch.setattr(os, "fsync", mock_fsync)

    with pytest.raises(RuntimeError) as exc_info:
        write_baseline_manifest_atomic({"version": 1, "count": 0, "manifest": {}}, baseline_file)

    assert "Simulated fsync I/O failure" in str(exc_info.value)
    assert baseline_file.read_bytes() == original_bytes
    assert list(tmp_path.glob(".target_baseline.json.*.tmp")) == []


def test_atomic_write_failure_replace_error(tmp_path, monkeypatch):
    """33. Atomic write failure during os.replace leaves target baseline untouched and cleans up temp file."""
    baseline_file = tmp_path / "target_baseline.json"
    original_payload = {"version": 1, "count": 0, "manifest": {}}
    write_baseline_manifest_atomic(original_payload, baseline_file)
    original_bytes = baseline_file.read_bytes()

    def mock_replace(src, dst):
        raise OSError("Simulated os.replace permission/I/O failure")

    monkeypatch.setattr(os, "replace", mock_replace)

    with pytest.raises(RuntimeError) as exc_info:
        write_baseline_manifest_atomic({"version": 1, "count": 0, "manifest": {}}, baseline_file)

    assert "Simulated os.replace permission/I/O failure" in str(exc_info.value)
    assert baseline_file.read_bytes() == original_bytes
    assert list(tmp_path.glob(".target_baseline.json.*.tmp")) == []


def test_successful_atomic_replacement(tmp_path):
    """34. Successful atomic replacement writes valid JSON, correct count, and cleans temp files."""
    baseline_file = tmp_path / "target_baseline.json"
    initial_payload = {"version": 1, "count": 0, "manifest": {}}
    write_baseline_manifest_atomic(initial_payload, baseline_file)

    new_payload = {
        "version": 1,
        "count": 1,
        "manifest": {"key1": "id1"},
    }
    write_baseline_manifest_atomic(new_payload, baseline_file)

    assert baseline_file.exists()
    data = json.loads(baseline_file.read_text(encoding="utf-8"))
    assert data["count"] == 1
    assert data["manifest"] == {"key1": "id1"}
    assert list(tmp_path.glob(".target_baseline.json.*.tmp")) == []


def test_update_additions_only_succeeds(tmp_path):
    """35. Baseline --update succeeds when only additions are present."""
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
    assert baseline_file.exists()
    _, _, stats1 = check_baseline_manifest(baseline_file, filaments_dir)
    assert stats1["baseline_count"] == 1

    fil_data["filaments"][0]["colors"].append({"name": "Blue", "hex": "0000FF"})
    (filaments_dir / "branda.json").write_text(json.dumps(fil_data), encoding="utf-8")

    write_baseline_manifest(baseline_file, filaments_dir, accept_breaking_changes=False)
    _, _, stats2 = check_baseline_manifest(baseline_file, filaments_dir)
    assert stats2["baseline_count"] == 2
    assert stats2["matched"] == 2


def test_update_rejects_changed_id_without_flag(tmp_path):
    """36. Baseline --update rejects updating when a historical ID changes unless breaking flag is given."""
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

    raw = json.loads(baseline_file.read_text(encoding="utf-8"))
    ckey = list(raw["manifest"].keys())[0]
    raw["manifest"][ckey] = "altered_id"
    baseline_file.write_text(json.dumps(raw), encoding="utf-8")

    with pytest.raises(SystemExit) as exc_info:
        write_baseline_manifest(baseline_file, filaments_dir, accept_breaking_changes=False)
    assert exc_info.value.code == 1


def test_update_rejects_missing_variant_without_flag(tmp_path):
    """37. Baseline --update rejects updating when a historical variant is missing unless breaking flag is given."""
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

    (filaments_dir / "branda.json").unlink()

    with pytest.raises(SystemExit) as exc_info:
        write_baseline_manifest(baseline_file, filaments_dir, accept_breaking_changes=False)
    assert exc_info.value.code == 1


def test_update_accepts_breaking_changes_with_flag(tmp_path):
    """38. Baseline --update accepts breaking changes when accept_breaking_changes=True on a valid baseline."""
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

    (filaments_dir / "branda.json").unlink()

    write_baseline_manifest(baseline_file, filaments_dir, accept_breaking_changes=True)
    _, _, stats = check_baseline_manifest(baseline_file, filaments_dir)
    assert stats["baseline_count"] == 0


def test_malformed_baseline_rejects_update_even_with_breaking_flag(tmp_path):
    """39. Malformed baseline is strictly rejected during update even when --accept-breaking-baseline-changes is set."""
    filaments_dir = tmp_path / "filaments"
    filaments_dir.mkdir()
    baseline_file = tmp_path / "corrupted_baseline.json"

    # Write malformed JSON (missing closing brace)
    baseline_file.write_text('{\n "version": 1,\n "count": 1,\n "manifest": {"key1": "id1"', encoding="utf-8")
    original_bytes = baseline_file.read_bytes()

    with pytest.raises(SystemExit) as exc_info:
        write_baseline_manifest(baseline_file, filaments_dir, accept_breaking_changes=True)

    assert exc_info.value.code == 1
    assert baseline_file.read_bytes() == original_bytes


def test_regression_normal_metadata_only_correction(tmp_path):
    """40. Regression test: Normal metadata-only correction (temp, hex, url) preserves ID and key."""
    filaments_dir = tmp_path / "filaments"
    filaments_dir.mkdir()
    baseline_file = tmp_path / "baseline.json"

    fil_data_v1 = {
        "manufacturer": "BrandA",
        "filaments": [
            {
                "name": "PLA {color_name}",
                "material": "PLA",
                "density": 1.24,
                "weights": [{"weight": 1000}],
                "diameters": [1.75],
                "colors": [{"name": "Red", "hex": "FF0000"}],
                "extruder_temp": 200,
            }
        ],
    }
    (filaments_dir / "branda.json").write_text(json.dumps(fil_data_v1), encoding="utf-8")
    write_baseline_manifest(baseline_file, filaments_dir)

    # Modify metadata only (no change to identity key or ID)
    fil_data_v2 = {
        "manufacturer": "BrandA",
        "filaments": [
            {
                "name": "PLA {color_name}",
                "material": "PLA",
                "density": 1.24,
                "weights": [{"weight": 1000}],
                "diameters": [1.75],
                "colors": [{"name": "Red", "hex": "DD0000", "tds_url": "https://example.com/tds.pdf"}],
                "extruder_temp": 210,
                "bed_temp": 60,
            }
        ],
    }
    (filaments_dir / "branda.json").write_text(json.dumps(fil_data_v2), encoding="utf-8")

    res = check_baseline_manifest_detailed(baseline_file, filaments_dir)
    assert res.all_errors == []
    assert res.stats["matched"] == 1
    assert res.stats["changed"] == 0
    assert res.stats["removed"] == 0
    assert res.stats["rekeyed"] == 0


def test_regression_legitimate_new_variant(tmp_path):
    """41. Regression test: Legitimate new variant is reported as added public ID and passes check."""
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

    # Add a legitimate new color variant
    fil_data["filaments"][0]["colors"].append({"name": "Blue", "hex": "0000FF"})
    (filaments_dir / "branda.json").write_text(json.dumps(fil_data), encoding="utf-8")

    res = check_baseline_manifest_detailed(baseline_file, filaments_dir)
    assert res.all_errors == []
    assert res.stats["matched"] == 1
    assert res.stats["added"] == 1
    assert res.stats["removed"] == 0
    assert res.stats["changed"] == 0
    assert any("New variant added (not in baseline)" in item for item in res.added_diagnostics)


def test_regression_legacy_identity_rekey_preserving_public_id(tmp_path):
    """42. Regression test: Legacy identity rekeying preserves historical public ID."""
    filaments_dir = tmp_path / "filaments"
    filaments_dir.mkdir()
    baseline_file = tmp_path / "baseline.json"

    # Historical data had spool_type: plastic
    fil_data_v1 = {
        "manufacturer": "BrandA",
        "filaments": [
            {
                "name": "PLA {color_name}",
                "material": "PLA",
                "density": 1.24,
                "weights": [{"weight": 1000, "spool_type": "plastic"}],
                "diameters": [1.75],
                "colors": [{"name": "Red", "hex": "FF0000"}],
            }
        ],
    }
    (filaments_dir / "branda.json").write_text(json.dumps(fil_data_v1), encoding="utf-8")
    write_baseline_manifest(baseline_file, filaments_dir)

    # Rekey source identity to spool_type: cardboard with legacy_id_spool_type: plastic
    fil_data_v2 = {
        "manufacturer": "BrandA",
        "filaments": [
            {
                "name": "PLA {color_name}",
                "material": "PLA",
                "density": 1.24,
                "weights": [
                    {
                        "weight": 1000,
                        "spool_type": "cardboard",
                        "legacy_id_spool_type": "plastic",
                    }
                ],
                "diameters": [1.75],
                "colors": [{"name": "Red", "hex": "FF0000"}],
            }
        ],
    }
    (filaments_dir / "branda.json").write_text(json.dumps(fil_data_v2), encoding="utf-8")

    res = check_baseline_manifest_detailed(baseline_file, filaments_dir)
    assert res.all_errors == []
    assert res.stats["matched"] == 0
    assert res.stats["rekeyed"] == 1
    assert res.stats["removed"] == 0
    assert res.stats["changed"] == 0
    assert any("Source identity rekey with unchanged public ID" in item for item in res.rekeyed_diagnostics)


def test_regression_accidental_id_removal(tmp_path):
    """43. Regression test: Accidental removal of a published public ID fails CI gate."""
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
                "colors": [{"name": "Red", "hex": "FF0000"}, {"name": "Green", "hex": "00FF00"}],
            }
        ],
    }
    (filaments_dir / "branda.json").write_text(json.dumps(fil_data), encoding="utf-8")
    write_baseline_manifest(baseline_file, filaments_dir)

    # Accidentally delete Green color variant
    fil_data["filaments"][0]["colors"] = [{"name": "Red", "hex": "FF0000"}]
    (filaments_dir / "branda.json").write_text(json.dumps(fil_data), encoding="utf-8")

    res = check_baseline_manifest_detailed(baseline_file, filaments_dir)
    assert res.has_breaking_changes is True
    assert res.stats["removed"] == 1
    assert any("Historical baseline variant missing from current source data" in err for err in res.removed_errors)


def test_regression_accidental_id_migration(tmp_path):
    """44. Regression test: Accidental migration of an existing public ID fails CI gate."""
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

    # Change template name without legacy compatibility, causing ID migration
    fil_data["filaments"][0]["name"] = "Standard PLA {color_name}"
    (filaments_dir / "branda.json").write_text(json.dumps(fil_data), encoding="utf-8")

    res = check_baseline_manifest_detailed(baseline_file, filaments_dir)
    assert res.has_breaking_changes is True
    assert res.stats["changed"] == 0
    assert res.stats["removed"] == 1
    assert res.stats["added"] == 1
    assert any("Historical baseline variant missing from current source data" in err for err in res.removed_errors)


def test_regression_baseline_tampering(tmp_path):
    """45. Regression test: Baseline file tampering is detected and fails CI gate."""
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

    # Tamper with baseline file (corrupt count)
    raw = json.loads(baseline_file.read_text(encoding="utf-8"))
    raw["count"] = 9999
    baseline_file.write_text(json.dumps(raw), encoding="utf-8")

    res = check_baseline_manifest_detailed(baseline_file, filaments_dir)
    assert res.is_valid_structure is False
    assert any("does not match actual manifest entry count" in err for err in res.structural_errors)


def test_regression_trusted_base_detects_coordinated_tampering(tmp_path):
    """46. Regression test: Coordinated source ID migration + PR baseline rewrite fails trusted-base gate."""
    filaments_dir = tmp_path / "filaments"
    filaments_dir.mkdir()
    base_file = tmp_path / "base_baseline.json"
    head_file = tmp_path / "head_baseline.json"

    # Base state: BrandA PLA Red mapped to old ID
    fil_data_v1 = {
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
    (filaments_dir / "branda.json").write_text(json.dumps(fil_data_v1), encoding="utf-8")
    write_baseline_manifest(base_file, filaments_dir)

    # Coordinated change: source template renamed to "Standard PLA {color_name}" (generates new_id)
    fil_data_v2 = {
        "manufacturer": "BrandA",
        "filaments": [
            {
                "name": "Standard PLA {color_name}",
                "material": "PLA",
                "density": 1.24,
                "weights": [{"weight": 1000}],
                "diameters": [1.75],
                "colors": [{"name": "Red", "hex": "FF0000"}],
            }
        ],
    }
    (filaments_dir / "branda.json").write_text(json.dumps(fil_data_v2), encoding="utf-8")

    # PR author rewrites PR HEAD baseline to match the new source ID using --accept-breaking-baseline-changes
    write_baseline_manifest(head_file, filaments_dir, accept_breaking_changes=True)

    # HEAD-only check mode would PASS because current source matches HEAD baseline
    head_only_res = check_baseline_manifest_detailed(head_file, filaments_dir, base_baseline_path=None)
    assert head_only_res.all_errors == []
    assert head_only_res.stats["matched"] == 1

    # Trusted-BASE mode MUST FAIL because current source and HEAD baseline deviate from trusted BASE baseline!
    trusted_res = check_baseline_manifest_detailed(head_file, filaments_dir, base_baseline_path=base_file)
    assert trusted_res.has_breaking_changes is True
    assert trusted_res.stats["changed"] > 0 or trusted_res.stats["removed"] > 0
    assert any("Public ID regression" in err or "tampering" in err for err in trusted_res.all_errors)


def test_regression_trusted_base_detects_deletion_from_pr_baseline(tmp_path):
    """47. Regression test: Deleting a historical entry from PR baseline while source still exists fails trusted-base gate."""
    filaments_dir = tmp_path / "filaments"
    filaments_dir.mkdir()
    base_file = tmp_path / "base_baseline.json"
    head_file = tmp_path / "head_baseline.json"

    # Base state: 2 variants
    fil_data = {
        "manufacturer": "BrandA",
        "filaments": [
            {
                "name": "PLA {color_name}",
                "material": "PLA",
                "density": 1.24,
                "weights": [{"weight": 1000}],
                "diameters": [1.75],
                "colors": [{"name": "Red", "hex": "FF0000"}, {"name": "Blue", "hex": "0000FF"}],
            }
        ],
    }
    (filaments_dir / "branda.json").write_text(json.dumps(fil_data), encoding="utf-8")
    write_baseline_manifest(base_file, filaments_dir)

    # PR HEAD baseline deletes entry for Blue color from PR baseline manifest
    base_data = json.loads(base_file.read_text(encoding="utf-8"))
    manifest = base_data["manifest"]
    blue_key = [k for k in manifest.keys() if "PLA Blue" in k][0]
    del manifest[blue_key]
    base_data["count"] = len(manifest)
    head_file.write_text(json.dumps(base_data), encoding="utf-8")

    # Source files still contain both Red and Blue
    trusted_res = check_baseline_manifest_detailed(head_file, filaments_dir, base_baseline_path=base_file)
    assert trusted_res.has_breaking_changes is True
    assert any("PR baseline tampering detected" in err for err in trusted_res.removed_errors)
