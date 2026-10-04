import importlib
import json
import subprocess

import pytest

from scripts.compile_id_baseline import write_baseline_manifest


@pytest.fixture
def git_catalog(tmp_path):
    def git(*args):
        return subprocess.run(["git", *args], cwd=tmp_path, check=True, capture_output=True, text=True).stdout.strip()
    (tmp_path / "filaments").mkdir()
    (tmp_path / "contracts").mkdir()
    definition = {"name": "PETG {color_name}", "material": "PETG", "density": 1.27, "weights": [{"weight": 1000, "spool_type": "plastic"}], "diameters": [1.75], "colors": [{"name": "Gray", "hex": "888888"}]}
    source = tmp_path / "filaments/acme.json"
    source.write_text(json.dumps({"manufacturer": "Acme", "filaments": [definition]}))
    for name, section in (("retired_ids", "retired"), ("not_duplicates", "groups")):
        (tmp_path / f"contracts/{name}.json").write_text(json.dumps({"version": 1, section: {}}))
    write_baseline_manifest(tmp_path / "contracts/compiled_id_baseline.json", tmp_path / "filaments")
    git("init")
    git("config", "user.name", "Fixture")
    git("config", "user.email", "fixture@example.invalid")
    git("add", ".")
    git("commit", "-m", "baseline fixture")
    return tmp_path, git("rev-parse", "HEAD"), git


def add_duplicate(root, template="Acme PETG {color_name}"):
    source = root / "filaments/acme.json"
    data = json.loads(source.read_text())
    data["filaments"].append({**data["filaments"][0], "name": template})
    source.write_text(json.dumps(data))


def guard(root, base=None):
    return importlib.import_module("scripts.duplicate_guard").check_duplicate_candidates(root, base)


def test_new_and_existing_groups_both_fail(git_catalog):
    root, base, git = git_catalog
    add_duplicate(root)
    errors, warnings = guard(root, base)
    assert len(errors) == 1
    assert "Unresolved" in errors[0]
    assert warnings == []
    git("add", ".")
    git("commit", "-m", "existing candidate fixture")
    errors, warnings = guard(root, git("rev-parse", "HEAD"))
    assert len(errors) == 1
    assert warnings == []


def test_head_only_candidates_are_errors(git_catalog):
    root, _, _ = git_catalog
    add_duplicate(root)
    assert len(guard(root)[0]) == 1
    assert guard(root)[1] == []


def test_guard_uses_existing_compiler_source_json_semantics(git_catalog):
    root, base, _ = git_catalog
    source = root / "filaments/acme.json"
    source.write_text(source.read_text().replace('"density": 1.27', '"density": 1.27, "bed_temp": 70, "bed_temp": 80'))
    assert guard(root, base) == ([], [])
    catalog = importlib.import_module("scripts.duplicate_catalog")
    assert catalog.catalog_records(root)[0]["record"]["bed_temp"] == 80


def test_exact_nonduplicate_exemption_does_not_cover_new_member(git_catalog):
    root, base, _ = git_catalog
    add_duplicate(root)
    catalog = importlib.import_module("scripts.duplicate_catalog")
    groups = catalog.candidate_groups(catalog.catalog_records(root))
    gid, rows = next(iter(groups.items()))
    path = root / "contracts/not_duplicates.json"
    path.write_text(json.dumps({"version": 1, "groups": {gid: {"ids": [row["record"]["id"] for row in rows], "reason": "different confirmed products", "ref": "owner review", "source": "a" * 40}}}))
    assert guard(root, base) == ([], [])
    add_duplicate(root, "PETG ({color_name})")
    assert len(guard(root, base)[0]) == 1


def test_malformed_exemption_and_unavailable_base_fail_closed(git_catalog):
    root, base, _ = git_catalog
    (root / "contracts/not_duplicates.json").write_text('{"version":1,"groups":{"all":{"manufacturer":"Acme"}}}')
    assert guard(root, base)[0]
    assert guard(root, "f" * 40)[0]


def test_auditor_skips_only_reviewed_exact_group(git_catalog):
    root, _, _ = git_catalog
    add_duplicate(root)
    audit = importlib.import_module("scripts.audit_duplicates").audit_brand
    group = audit(root, "acme")["groups"][0]
    (root / "contracts/not_duplicates.json").write_text(json.dumps({"version": 1, "groups": {group["group_id"]: {"ids": group["ids"], "reason": "different confirmed products", "ref": "owner review", "source": "a" * 40}}}))
    assert audit(root, "acme")["groups"] == []
    add_duplicate(root, "PETG ({color_name})")
    assert len(audit(root, "acme")["groups"]) == 1


def test_push_and_pr_use_their_resolved_trusted_base(git_catalog):
    root, base, _ = git_catalog
    resolve = importlib.import_module("scripts.ci_base_ref").resolve_base
    assert resolve("push", before=base, root=root) == base
    assert resolve("pull_request", pr_base=base, root=root) == base


def test_zero_push_base_is_explicit_head_only_but_missing_or_unknown_is_error(git_catalog):
    root, _, _ = git_catalog
    resolve = importlib.import_module("scripts.ci_base_ref").resolve_base
    assert resolve("push", before="0" * 40, root=root) is None
    for before in ("", "f" * 40, "--help", "main; echo unsafe"):
        with pytest.raises(ValueError):
            resolve("push", before=before, root=root)
    with pytest.raises(ValueError):
        resolve("pull_request", pr_base="0" * 40, root=root)
