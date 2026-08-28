"""Unit tests for physical metadata audit tooling."""

import json
from pathlib import Path
import subprocess
import sys
import pytest

from scripts.audit_physical_metadata import (
    AuditFinding,
    audit_density,
    audit_identifiers,
    audit_package_weights,
    audit_temperatures,
    run_physical_metadata_audit,
)


def test_audit_temperatures_valid():
    fil = {
        "name": "PLA Basic {color_name}",
        "material": "PLA",
        "extruder_temp_range": [190, 220],
        "bed_temp_range": [50, 60],
    }
    findings = audit_temperatures(fil, "test.json", "TestBrand")
    assert len(findings) == 0


def test_audit_temperatures_min_greater_than_max():
    fil = {
        "name": "PLA Broken {color_name}",
        "material": "PLA",
        "extruder_temp_range": [230, 200],
        "bed_temp_range": [70, 50],
    }
    findings = audit_temperatures(fil, "test.json", "TestBrand")
    assert len(findings) == 2
    assert all(f.severity == "HIGH" for f in findings)
    assert any("Extruder min temperature" in f.reason for f in findings)
    assert any("Bed min temperature" in f.reason for f in findings)


def test_audit_temperatures_implausibly_low_and_high():
    fil = {
        "name": "Extreme {color_name}",
        "material": "PLA",
        "extruder_temp": 50,
        "bed_temp": 220,
    }
    findings = audit_temperatures(fil, "test.json", "TestBrand")
    assert len(findings) >= 2
    assert any(f.field == "extruder_temp" and f.severity == "HIGH" for f in findings)
    assert any(f.field == "bed_temp" and f.severity == "HIGH" for f in findings)


def test_audit_temperatures_pcl_exception():
    fil = {
        "name": "PCL {color_name}",
        "material": "PCL",
        "extruder_temp": 60,
        "bed_temp_range": [0, 0],
    }
    findings = audit_temperatures(fil, "test.json", "TestBrand")
    assert len(findings) == 0


def test_audit_temperature_swap_heuristic():
    fil = {
        "name": "Swapped {color_name}",
        "material": "PLA",
        "extruder_temp_range": [60, 80],
        "bed_temp_range": [215, 235],
    }
    findings = audit_temperatures(fil, "test.json", "TestBrand")
    swap_findings = [f for f in findings if f.category == "temp_swap"]
    assert len(swap_findings) == 1
    assert swap_findings[0].severity == "HIGH"
    assert "swapped" in swap_findings[0].reason.lower()


def test_audit_density_valid_and_anomalies():
    # Valid
    assert len(audit_density({"density": 1.24}, "test.json", "TestBrand")) == 0

    # Negative / Zero
    zero_res = audit_density({"density": 0}, "test.json", "TestBrand")
    assert len(zero_res) == 1
    assert zero_res[0].severity == "HIGH"

    neg_res = audit_density({"density": -1.2}, "test.json", "TestBrand")
    assert len(neg_res) == 1
    assert neg_res[0].severity == "HIGH"

    # Beyond physical ceiling
    high_res = audit_density({"density": 12.4}, "test.json", "TestBrand")
    assert len(high_res) == 1
    assert high_res[0].severity == "HIGH"

    # Suspicious low decimal
    low_res = audit_density({"density": 0.12}, "test.json", "TestBrand")
    assert len(low_res) == 1
    assert low_res[0].severity == "REVIEW"


def test_audit_package_weights():
    # Valid spooled
    valid_fil = {
        "weights": [{"weight": 1000, "spool_weight": 220, "spool_type": "plastic"}]
    }
    assert len(audit_package_weights(valid_fil, "test.json", "TestBrand")) == 0

    # Valid refill with 0g spool tare
    valid_refill = {
        "weights": [{"weight": 1000, "spool_weight": 0, "is_refill": True}]
    }
    assert len(audit_package_weights(valid_refill, "test.json", "TestBrand")) == 0

    # Invalid non-positive filament weight
    zero_weight = {"weights": [{"weight": 0, "spool_weight": 200}]}
    findings = audit_package_weights(zero_weight, "test.json", "TestBrand")
    assert len(findings) == 1
    assert findings[0].severity == "HIGH"

    # Spooled product with 0g tare
    zero_tare_spooled = {
        "weights": [{"weight": 1000, "spool_weight": 0, "spool_type": "plastic"}]
    }
    findings = audit_package_weights(zero_tare_spooled, "test.json", "TestBrand")
    assert len(findings) == 1
    assert findings[0].severity == "HIGH"

    # Implausibly large spool weight (e.g. gross weight entered)
    gross_tare = {
        "weights": [{"weight": 1000, "spool_weight": 2500, "spool_type": "plastic"}]
    }
    findings = audit_package_weights(gross_tare, "test.json", "TestBrand")
    assert len(findings) == 1
    assert findings[0].severity == "REVIEW"


def test_audit_identifiers_classification():
    all_data = [
        (
            "mfr1.json",
            "MfrOne",
            {
                "name": "PLA Family A",
                "colors": [
                    {"name": "Red", "codes": ["SKU-SAME-FAM", "SKU-CROSS-FAM", "SKU-CROSS-MFR"]},
                    {"name": "Blue", "codes": ["SKU-SAME-FAM"]},
                ],
            },
        ),
        (
            "mfr1.json",
            "MfrOne",
            {
                "name": "PETG Family B",
                "colors": [
                    {"name": "Green", "codes": ["SKU-CROSS-FAM"]},
                ],
            },
        ),
        (
            "mfr2.json",
            "MfrTwo",
            {
                "name": "ABS Family C",
                "colors": [
                    {"name": "Black", "codes": ["SKU-CROSS-MFR"]},
                ],
            },
        ),
    ]

    findings = audit_identifiers(all_data)
    cls_map = {f.value: f.classification for f in findings}

    assert cls_map["SKU-SAME-FAM"] == "SAME_FAMILY"
    assert cls_map["SKU-CROSS-FAM"] == "CROSS_FAMILY"
    assert cls_map["SKU-CROSS-MFR"] == "CROSS_MANUFACTURER"


def test_run_physical_metadata_audit_synthetic(tmp_path: Path):
    fil_dir = tmp_path / "filaments"
    fil_dir.mkdir()

    clean_file = fil_dir / "brand_a.json"
    clean_file.write_text(
        json.dumps(
            {
                "manufacturer": "Brand A",
                "filaments": [
                    {
                        "name": "PLA {color_name}",
                        "material": "PLA",
                        "density": 1.24,
                        "weights": [{"weight": 1000, "spool_weight": 200, "spool_type": "plastic"}],
                        "diameters": [1.75],
                        "extruder_temp_range": [200, 220],
                        "bed_temp_range": [50, 60],
                        "colors": [{"name": "Black", "hex": "000000", "codes": ["SKU-A1"]}],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    bad_file = fil_dir / "brand_b.json"
    bad_file.write_text(
        json.dumps(
            {
                "manufacturer": "Brand B",
                "filaments": [
                    {
                        "name": "Bad Temp {color_name}",
                        "material": "PLA",
                        "density": 1.24,
                        "weights": [{"weight": 1000, "spool_weight": 200, "spool_type": "plastic"}],
                        "diameters": [1.75],
                        "extruder_temp_range": [50, 60],
                        "bed_temp_range": [210, 230],
                        "colors": [{"name": "White", "hex": "FFFFFF", "codes": ["SKU-A1"]}],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    findings, summary = run_physical_metadata_audit(fil_dir)
    assert summary["total_files"] == 2
    assert summary["total_families"] == 2
    assert summary["high_severity_count"] >= 1  # Bad temp swap
    assert summary["review_severity_count"] >= 1  # SKU collision cross-mfr


def test_cli_execution(tmp_path: Path):
    fil_dir = tmp_path / "filaments"
    fil_dir.mkdir()

    test_file = fil_dir / "test.json"
    test_file.write_text(
        json.dumps(
            {
                "manufacturer": "Test Mfr",
                "filaments": [
                    {
                        "name": "Valid PLA {color_name}",
                        "material": "PLA",
                        "density": 1.24,
                        "weights": [{"weight": 1000, "spool_weight": 200, "spool_type": "plastic"}],
                        "diameters": [1.75],
                        "extruder_temp_range": [200, 220],
                        "bed_temp_range": [50, 60],
                        "colors": [{"name": "Black", "hex": "000000"}],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    # Test default mode (exit 0)
    proc = subprocess.run(
        [sys.executable, "scripts/audit_physical_metadata.py", "--filaments-dir", str(fil_dir)],
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0
    assert "No HIGH severity" in proc.stdout

    # Test json output
    proc_json = subprocess.run(
        [sys.executable, "scripts/audit_physical_metadata.py", "--filaments-dir", str(fil_dir), "--json"],
        capture_output=True,
        text=True,
    )
    assert proc_json.returncode == 0
    parsed = json.loads(proc_json.stdout)
    assert "summary" in parsed
    assert "findings" in parsed
