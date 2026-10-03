import copy
import importlib
import json
from pathlib import Path
import subprocess
import sys

import pytest

from scripts.compile_id_baseline import compile_current_id_manifest, write_baseline_manifest


def module(name):
    return importlib.import_module("scripts." + name)


@pytest.mark.parametrize("left,right", [
    ("PLA Black", "PLA+ Black"), ("PETG Black", "PETG Basic Black"),
    ("PETG 2.0 Gray", "PETG v2 Gray"), ("PETG HF Black", "PETG HS Black"),
    ("PLA Red Blue", "PLA Blue Red"), ("PLA Red Red Blue", "PLA Red Blue"),
])
def test_protected_ordered_names_are_distinct(left, right):
    normalize = module("duplicate_catalog").normalize_name
    assert normalize(left, "Acme", "PLA" if left.startswith("PLA") else "PETG") != normalize(right, "Acme", "PLA" if left.startswith("PLA") else "PETG")


def test_prefix_gray_and_brackets_normalize_without_losing_contents():
    normalize = module("duplicate_catalog").normalize_name
    assert normalize("Acme PETG (Grey)", "Acme", "PETG") == normalize("PETG Gray", "Acme", "PETG")
    assert normalize("AcmeX PETG Gray", "Acme", "PETG") != normalize("PETG Gray", "Acme", "PETG")
    assert normalize("PLA (Silk) Gray", "Acme", "PLA") == ("silk", "gray")


@pytest.fixture
def catalog(tmp_path):
    (tmp_path / "filaments").mkdir()
    (tmp_path / "contracts").mkdir()
    definition = {"name": "Acme PETG {color_name}", "material": "PETG", "density": 1.27,
                  "weights": [{"weight": 500, "spool_type": "plastic"}, {"weight": 1000, "spool_type": "plastic"}],
                  "diameters": [1.75, 2.85], "colors": [{"name": "Grey", "hex": "888888"}, {"name": "Blue", "hex": "0000FF"}]}
    survivor = {**definition, "name": "PETG {color_name}", "density": 1.25,
                "weights": [{"weight": 1000, "spool_type": "plastic"}], "diameters": [1.75], "colors": [{"name": "Gray", "hex": "999999"}]}
    (tmp_path / "filaments/acme.json").write_text(json.dumps({"manufacturer": "Acme", "filaments": [definition, survivor]}))
    for name, section in (("retired_ids", "retired"), ("not_duplicates", "groups")):
        (tmp_path / f"contracts/{name}.json").write_text(json.dumps({"version": 1, section: {}}))
    write_baseline_manifest(tmp_path / "contracts/compiled_id_baseline.json", tmp_path / "filaments")
    for args in (("init",), ("config", "user.name", "Fixture"), ("config", "user.email", "fixture@example.invalid"), ("add", "."), ("commit", "-m", "trusted fixture")):
        subprocess.run(["git", *args], cwd=tmp_path, check=True, capture_output=True)
    return tmp_path


def review_for(root):
    report = module("audit_duplicates").audit_brand(root, "acme")
    group = report["groups"][0]
    keep = next(rec["id"] for rec in group["records"] if rec["template"] == "PETG {color_name}")
    old = next(rec["id"] for rec in group["records"] if rec["id"] != keep)
    upstream = subprocess.run(["git", "rev-parse", "HEAD"], cwd=root, check=True, capture_output=True, text=True).stdout.strip()
    review = {"version": 1, "approved": True, "upstream_ref": upstream, "audit_digest": report["digest"], "groups": {
        group["group_id"]: {"approved": True, "survivor": keep, "retire": [old], "ref": "#66", "source": "a" * 40}}, "bindings": {}, "metadata": []}
    return review, old, keep


def test_audit_is_read_only_and_records_exact_conflicts(catalog):
    before = {path: path.read_bytes() for path in catalog.rglob("*.json")}
    report = module("audit_duplicates").audit_brand(catalog, "acme")
    assert len(report["groups"]) == 1
    group = report["groups"][0]
    assert group["proposed_survivor"] == next(rec["id"] for rec in group["records"] if rec["template"] == "PETG {color_name}")
    assert "density" in group["metadata_conflicts"]
    assert "color_hex" in group["metadata_conflicts"]
    assert report["upstream_sha"] is None
    assert before == {path: path.read_bytes() for path in catalog.rglob("*.json")}


def test_pinned_upstream_family_wins(catalog):
    def git(*args):
        return subprocess.run(["git", *args], cwd=catalog, check=True, capture_output=True, text=True).stdout.strip()
    git("init")
    git("config", "user.name", "Fixture")
    git("config", "user.email", "fixture@example.invalid")
    source = catalog / "filaments/acme.json"
    full = json.loads(source.read_text())
    source.write_text(json.dumps({**full, "filaments": [full["filaments"][0]]}))
    git("add", ".")
    git("commit", "-m", "upstream fixture")
    sha = git("rev-parse", "HEAD")
    source.write_text(json.dumps(full))
    report = module("audit_duplicates").audit_brand(catalog, "acme", upstream_ref=sha)
    assert report["upstream_sha"] == sha
    group = report["groups"][0]
    assert group["proposed_survivor"] == next(rec["id"] for rec in group["records"] if rec["template"].startswith("Acme"))


def test_merge_preserves_partial_matrix_unique_colors_and_compiled_metadata(catalog):
    review, old, keep = review_for(catalog)
    records = module("duplicate_catalog").catalog_records(catalog)
    before = {row["record"]["id"]: row["record"] for row in records}
    plan = module("merge_duplicates").plan_merge(catalog, "acme", review)
    assert plan["new_ids"] == []
    assert plan["retired_ids"] == {old: keep}
    module("merge_duplicates").apply_plan(catalog, plan)
    after = {row["record"]["id"]: row["record"] for row in module("duplicate_catalog").catalog_records(catalog)}
    assert after == {identity: record for identity, record in before.items() if identity != old}
    manifest, errors = compile_current_id_manifest(catalog / "filaments")
    assert errors == []
    assert json.loads((catalog / "contracts/compiled_id_baseline.json").read_text())["manifest"] == manifest
    entry = json.loads((catalog / "contracts/retired_ids.json").read_text())["retired"][old]
    assert entry["retired_key"] == next(row["key"] for row in records if row["record"]["id"] == old)


def test_dry_run_cli_does_not_write_sources_or_contracts(catalog, tmp_path):
    review, _, _ = review_for(catalog)
    review_path = tmp_path / "review.json"
    review_path.write_text(json.dumps(review))
    before = {path: path.read_bytes() for path in catalog.rglob("*.json")}
    result = subprocess.run([sys.executable, "scripts/merge_duplicates.py", "--root", str(catalog), "--brand", "acme", "--review", str(review_path)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert "DRY RUN" in result.stdout
    assert before == {path: path.read_bytes() for path in catalog.rglob("*.json")}


@pytest.mark.parametrize("mutation", [
    lambda r: r.update(approved=False),
    lambda r: r.update(audit_digest="stale"),
    lambda r: next(iter(r["groups"].values())).update(source="no evidence"),
    lambda r: next(iter(r["groups"].values())).update(survivor="invented"),
])
def test_apply_requires_current_exact_owner_review(catalog, mutation):
    review, _, _ = review_for(catalog)
    mutation(review)
    with pytest.raises(ValueError):
        module("merge_duplicates").plan_merge(catalog, "acme", review)


def test_excluded_group_has_no_delta(catalog):
    review, _, _ = review_for(catalog)
    plan = module("merge_duplicates").plan_merge(catalog, "acme", review, exclude=list(review["groups"]))
    assert plan["retired_ids"] == {}
    assert plan["changes"] == {}


def test_review_requires_pinned_upstream_and_respects_survivor_priority(catalog):
    review, old, keep = review_for(catalog)
    merge = module("merge_duplicates")
    no_upstream = copy.deepcopy(review)
    no_upstream.pop("upstream_ref")
    with pytest.raises(ValueError, match="upstream"):
        merge.plan_merge(catalog, "acme", no_upstream)
    decision = next(iter(review["groups"].values()))
    decision.update(survivor=old, retire=[keep])
    with pytest.raises(ValueError, match="survivor"):
        merge.plan_merge(catalog, "acme", review)


def test_metadata_requires_same_variant_lot_evidence_and_changes_only_survivor(catalog):
    review, old, keep = review_for(catalog)
    metadata = {"id": keep, "values": {"density": 1.3}, "source": "https://example.invalid/label", "lot": "2026-09", "same_variant": True, "approved": True}
    review["metadata"] = [metadata]
    merge = module("merge_duplicates")
    before = {row["record"]["id"]: row["record"] for row in module("duplicate_catalog").catalog_records(catalog)}
    plan = merge.plan_merge(catalog, "acme", review)
    merge.apply_plan(catalog, plan)
    after = {row["record"]["id"]: row["record"] for row in module("duplicate_catalog").catalog_records(catalog)}
    assert after[keep]["density"] == 1.3
    assert all(after[identity] == record for identity, record in before.items() if identity not in (old, keep))


@pytest.mark.parametrize("field,value", [("country_of_origin", "BR"), ("sds_url", "https://example.invalid/sds.pdf"), ("tds_url", "https://example.invalid/tds.pdf")])
def test_family_metadata_corrections_are_confined_to_reviewed_variant(catalog, field, value):
    review, old, keep = review_for(catalog)
    review["metadata"] = [{"id": keep, "values": {field: value}, "source": "a" * 40, "lot": "2026-09", "same_variant": True, "approved": True}]
    before = {row["record"]["id"]: row["record"] for row in module("duplicate_catalog").catalog_records(catalog)}
    merge = module("merge_duplicates")
    merge.apply_plan(catalog, merge.plan_merge(catalog, "acme", review))
    after = {row["record"]["id"]: row["record"] for row in module("duplicate_catalog").catalog_records(catalog)}
    assert after[keep][field] == value
    assert all(after[identity] == record for identity, record in before.items() if identity not in (old, keep))


@pytest.mark.parametrize("change", [{"lot": ""}, {"same_variant": False}, {"values": {"name": "New name"}}, {"values": {"density": -1}}])
def test_unproven_or_identity_changing_metadata_is_rejected(catalog, change):
    review, _, keep = review_for(catalog)
    review["metadata"] = [{"id": keep, "values": {"density": 1.3}, "source": "a" * 40, "lot": "2026-09", "same_variant": True, "approved": True, **change}]
    with pytest.raises(ValueError):
        module("merge_duplicates").plan_merge(catalog, "acme", review)


def test_stale_plan_refuses_writes(catalog):
    review, _, _ = review_for(catalog)
    merge = module("merge_duplicates")
    plan = merge.plan_merge(catalog, "acme", review)
    source = catalog / "filaments/acme.json"
    source.write_text(source.read_text() + "\n")
    before = {path: path.read_bytes() for path in catalog.rglob("*.json")}
    with pytest.raises(ValueError, match="stale"):
        merge.apply_plan(catalog, plan)
    assert before == {path: path.read_bytes() for path in catalog.rglob("*.json")}


def test_transaction_restores_all_files_after_write_failure(catalog, monkeypatch):
    review, _, _ = review_for(catalog)
    merge = module("merge_duplicates")
    plan = merge.plan_merge(catalog, "acme", review)
    before = {path: path.read_bytes() for path in catalog.rglob("*.json")}
    real_replace = merge.os.replace
    calls = 0
    def fail_once(source, target):
        nonlocal calls
        calls += 1
        if calls == 2:
            raise OSError("synthetic write failure")
        return real_replace(source, target)
    monkeypatch.setattr(merge.os, "replace", fail_once)
    with pytest.raises(OSError, match="synthetic"):
        merge.apply_plan(catalog, plan)
    assert before == {path: path.read_bytes() for path in catalog.rglob("*.json")}
