"""Exact manufacturer-evidenced identifier bindings must not fan out to other variants."""

from pathlib import Path

import pytest

from scripts.duplicate_catalog import catalog_records

ROOT = Path(__file__).resolve().parents[1]

# Independently transcribed from the manufacturer's ABS ProductGroup JSON-LD,
# checked 2026-10-18: https://www.3d4makers.com/products/abs-filament
# Each tuple is (exact public ID, manufacturer SKU, GTIN, product variant ID).
ABS_BINDINGS = [
    ("3d4makers_abs_absfilamentblue(ral5002)_750_175_p", "ABSXX-5002-175-750-3D4M", "8721632470086", "3497129540"),
    ("3d4makers_abs_absfilamentblue(ral5002)_2300_175_p", "ABSXX-5002-175-2300-3D4M", "8721632470093", "40215259152431"),
    ("3d4makers_abs_absfilamentgreen(ral6029)_750_175_p", "ABSXX-6029-175-750-3D4M", "8721632470123", "3497129604"),
    ("3d4makers_abs_absfilamentgreen(ral6029)_2300_175_p", "ABSXX-6029-175-2300-3D4M", "8721632470130", "40215259250735"),
    ("3d4makers_abs_absfilamentblack(ral9011)_750_175_p", "ABSXX-9011-175-750-3D4M", "8721632470161", "2697752516"),
    ("3d4makers_abs_absfilamentblack(ral9011)_2300_175_p", "ABSXX-9011-175-2300-3D4M", "8721632470178", "40218889125935"),
    ("3d4makers_abs_absfilamentwhite(ral9016)_750_175_p", "ABSXX-9016-175-750-3D4M", "8721632470208", "3497129412"),
    ("3d4makers_abs_absfilamentwhite(ral9016)_2300_175_p", "ABSXX-9016-175-2300-3D4M", "8721632470215", "40218889224239"),
    ("3d4makers_abs_absfilamentred(ral3020)_750_175_p", "ABSXX-3020-175-750-3D4M", "8721632470246", "3497129476"),
    ("3d4makers_abs_absfilamentred(ral3020)_2300_175_p", "ABSXX-3020-175-2300-3D4M", "8721632470253", "40218889289775"),
    ("3d4makers_abs_absfilamentnatural_750_175_p", "ABSXX-0000-175-750-3D4M", "8721632470284", "3549458820"),
    ("3d4makers_abs_absfilamentnatural_2300_175_p", "ABSXX-0000-175-2300-3D4M", "8721632470291", "40218889355311"),
]


@pytest.fixture(scope="module")
def compiled_catalog():
    return {row["record"]["id"]: row["record"] for row in catalog_records(ROOT)}


@pytest.mark.parametrize("target_id,sku,gtin,variant", ABS_BINDINGS, ids=[row[0] for row in ABS_BINDINGS])
def test_3d4makers_abs_identifiers_only_match_exact_variant(compiled_catalog, target_id, sku, gtin, variant):
    """Catch cross-weight/diameter/package/color identifier inheritance in real output."""
    code_targets = {rid for rid, record in compiled_catalog.items()
                    if record["manufacturer"] == "3D4Makers" and sku in (record.get("codes") or [])}
    assert code_targets == {target_id}, f"SKU leaked beyond manufacturer variant {variant}"
    gtin_targets = {rid for rid, record in compiled_catalog.items()
                    if any(gtin in (record.get(field) or []) for field in ("eans", "eans_refill"))}
    assert gtin_targets == {target_id}, f"GTIN leaked beyond manufacturer variant {variant}"
    target = compiled_catalog[target_id]
    assert target["codes"] == [sku]
    assert target["eans"] == [gtin]
    assert not target["eans_refill"]
