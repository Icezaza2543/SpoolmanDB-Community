import json

import pytest

from scripts.compile_id_baseline import make_canonical_identity_key
from scripts.duplicate_catalog import rename_identity
from scripts.rename_migration import rename_source


def key(template, color, *, material="PETG", manufacturer="Acme", filename="acme.json",
        weight=1000, diameter=1.75, spool="plastic", refill=False):
    return make_canonical_identity_key(filename, manufacturer, template, template.replace("{color_name}", color),
                                       material, weight, diameter, spool, refill)


OLD_KEY = key("PETG - {color_name}", "Black")
NEW_KEY = key("{color_name}", "Black")
OLD, NEW = "acme_petg_petg-black_1000_175_p", "acme_petg_black_1000_175_p"


def entry(target=NEW, reason="rename"):
    return {"replaced_by": target, "reason": reason, "ref": "https://github.com/Donkie/SpoolmanDB/pull/521",
            "source": "b" * 40, "retired_key": OLD_KEY}


def check(head, *, historical=None, current=None):
    from scripts.retired_ids import check_registry
    current = current if current is not None else {NEW_KEY: NEW}
    return check_registry(head, {"version": 1, "retired": {}},
                          historical if historical is not None else {OLD_KEY: OLD},
                          current, current)


def test_registered_rename_passes():
    errors, retired, _ = check({"version": 1, "retired": {OLD: entry()}})
    assert errors == []
    assert retired == {OLD}


def test_rename_into_existing_record_must_be_a_duplicate():
    errors, _, _ = check({"version": 1, "retired": {OLD: entry()}}, historical={OLD_KEY: OLD, NEW_KEY: NEW})
    assert "must be a new ID" in " ".join(errors)


def test_duplicate_reason_still_requires_existing_record():
    errors, _, _ = check({"version": 1, "retired": {OLD: entry(reason="duplicate")}})
    assert "existing historical record" in " ".join(errors)


def test_unknown_reason_rejected():
    errors, _, _ = check({"version": 1, "retired": {OLD: entry(reason="cleanup")}})
    assert "invalid reason" in " ".join(errors)


@pytest.mark.parametrize("replacement", [
    key("{color_name}", "White"),                       # different color
    key("HF {color_name}", "Black"),                    # added line qualifier
    key("{color_name}", "Black", material="PETG-CF"),   # material change is not a rename
    key("{color_name}", "Black", weight=500),
    key("{color_name}", "Black", spool="cardboard"),
    key("{color_name}", "Black", filename="other.json"),
])
def test_rename_identity_mismatch_fails(replacement):
    errors, _, _ = check({"version": 1, "retired": {OLD: entry()}}, current={replacement: NEW})
    assert "identity mismatch" in " ".join(errors)


@pytest.mark.parametrize("old, new, material, manufacturer", [
    ("PETG - {color_name}", "{color_name}", "PETG", "Acme"),
    ("ESD PETG - {color_name}", "ESD - {color_name}", "PETG", "Acme"),
    ("E-PLA - {color_name}", "E - {color_name}", "PLA", "Acme"),
    ("PLA CF - {color_name}", "{color_name}", "PLA-CF", "Acme"),
    ("PLA Wood - {color_name}", "Wood - {color_name}", "PLA+WOOD", "Acme"),
    ("TPU Pro Matte 85A - {color_name}", "Pro Matte - {color_name}", "TPU-85A", "Acme"),
    ("RAPID PLA+ {color_name}", "RAPID {color_name}", "PLA+", "Acme"),
    ("3DXTECH™ {color_name}", "{color_name}", "ABS", "3DXTECH"),
    ("PolyLite™ PETG {color_name}", "PolyLite™ {color_name}", "PETG", "Polymaker"),
    ("{color_name} Hyper ABS", "{color_name} Hyper", "ABS", "Creality"),
    ("grillon3 PLA | {color_name}", "grillon3 {color_name}", "PLA", "NTH Grillon"),
    ("PC Blend Carbon Fiber {color_name}", "Blend {color_name}", "PC-CF", "Prusament"),
])
def test_upstream_cleanup_renames_keep_identity(old, new, material, manufacturer):
    assert rename_identity(key(old, "Black", material=material, manufacturer=manufacturer)) == \
        rename_identity(key(new, "Black", material=material, manufacturer=manufacturer))


@pytest.mark.parametrize("old, new, material", [
    ("PLA+ {color_name}", "{color_name}", "PLA"),         # "+" is meaningful when not the material
    ("PETG HF {color_name}", "{color_name}", "PETG"),     # drops a real line qualifier
    ("PETG 2.0 {color_name}", "{color_name}", "PETG"),    # drops a version
    ("Silk {color_name}", "Matte {color_name}", "PLA"),   # different line
    ("Basic {color_name}", "{color_name} Basic", "PLA"),  # order is kept
])
def test_non_rename_changes_fail(old, new, material):
    assert rename_identity(key(old, "Black", material=material)) != rename_identity(key(new, "Black", material=material))


def test_rename_identity_requires_single_placeholder():
    with pytest.raises(ValueError):
        rename_identity(make_canonical_identity_key("a.json", "Acme", "Fixed Name", "Fixed Name", "PLA",
                                                    1000, 1.75, None, False))


def test_rename_source_keeps_formatting_and_only_touches_matching_material():
    text = ('{\n  "manufacturer": "Acme",\n  "filaments": [\n'
            '    {"name": "PETG - {color_name}", "material": "PETG", "colors": [{"name": "PETG - x"}]},\n'
            '    {"name": "PETG - {color_name}", "material": "PETG-CF"}\n  ]\n}\n')
    with pytest.raises(ValueError, match="without reformatting"):
        rename_source(text, {("PETG - {color_name}", "PETG"): "{color_name}"})
    one_material = text.replace('"PETG-CF"', '"PETG"')
    result, count = rename_source(one_material, {("PETG - {color_name}", "PETG"): "{color_name}"})
    assert count == 2
    assert result == one_material.replace('"name": "PETG - {color_name}"', '"name": "{color_name}"')
    assert json.loads(result)["filaments"][0]["colors"][0]["name"] == "PETG - x"


# --- Rename-only scope check (Icezaza2543/SpoolmanDB-Community#72 review) ---

from scripts.rename_migration import build_registry, verify_rename_scope, write_all  # noqa: E402


def rec(pid, name, **fields):
    return {"id": pid, "name": name, "material": "PETG", "density": 1.27, "color_hex": "000000", **fields}


KEEP_KEY = key("PETG - {color_name}", "White")
BASE_RECORDS = {OLD: (OLD_KEY, rec(OLD, "PETG - Black")), "keep": (KEEP_KEY, rec("keep", "PETG - White"))}
HEAD_RECORDS = {NEW: (NEW_KEY, rec(NEW, "Black")), "keep": (KEEP_KEY, rec("keep", "PETG - White"))}


def scope(base=None, head=None, base_registry=None, head_registry=None):
    return verify_rename_scope(base if base is not None else BASE_RECORDS,
                               base_registry or {"version": 1, "retired": {}},
                               head if head is not None else HEAD_RECORDS,
                               head_registry or {"version": 1, "retired": {OLD: entry()}})


def test_scope_accepts_pure_rename():
    errors, pairs = scope()
    assert errors == []
    assert pairs == {OLD: NEW}


def test_scope_rejects_unrelated_new_record():
    # Review probe 1: the strict baseline check accepts this (added=2).
    head = {**HEAD_RECORDS, "extra": (key("{color_name}", "Red"), rec("extra", "Red"))}
    errors, _ = scope(head=head)
    assert any("not rename replacements: extra" in e for e in errors)


def test_scope_rejects_rekey_of_unchanged_id():
    # Review probe 2: the strict baseline check accepts this (rekeyed=1).
    head = {**HEAD_RECORDS, "keep": (key("PETG - {color_name}", "White", weight=1000.0, spool="metal"),
                                     rec("keep", "PETG - White"))}
    errors, _ = scope(head=head)
    assert any("identity keys changed on unchanged public IDs: keep" in e for e in errors)


@pytest.mark.parametrize("change", [{"density": 1.3}, {"color_hex": "111111"}, {"material": "PETG-CF"}])
def test_scope_rejects_field_changes_beyond_id_and_name(change):
    errors, _ = scope(head={**HEAD_RECORDS, NEW: (NEW_KEY, rec(NEW, "Black", **change))})
    assert any("rename also changes" in e for e in errors)
    errors, _ = scope(head={**HEAD_RECORDS, "keep": (KEEP_KEY, rec("keep", "PETG - White", **change))})
    assert any("fields changed on records that are not renamed: keep" in e for e in errors)


def test_scope_rejects_unregistered_removal_and_non_rename_entries():
    errors, _ = scope(head={NEW: HEAD_RECORDS[NEW]})
    assert any("removed without a rename retirement: keep" in e for e in errors)
    errors, _ = scope(head_registry={"version": 1, "retired": {OLD: entry(reason="duplicate")}})
    assert any("outside a rename migration" in e for e in errors)


def test_scope_rejects_many_to_one_and_wrong_retired_key():
    other_key = key("PETG - {color_name}", "Black", weight=500)
    base = {**BASE_RECORDS, "old2": (other_key, rec("old2", "PETG - Black"))}
    head_registry = {"version": 1, "retired": {OLD: entry(), "old2": {**entry(), "retired_key": other_key}}}
    errors, _ = scope(base=base, head_registry=head_registry)
    assert any("must be one-to-one" in e for e in errors)
    errors, _ = scope(head_registry={"version": 1, "retired": {OLD: {**entry(), "retired_key": KEEP_KEY}}})
    assert any("retired_key is not the record's identity key" in e for e in errors)


def test_scope_requires_chains_to_be_repointed_with_evidence_unchanged():
    prior = {"replaced_by": OLD, "reason": "duplicate", "ref": "docs/audits/x.json", "source": "c" * 40,
             "retired_key": "acme.json::Acme::Acme PETG - {color_name}::Acme PETG - Black::PETG::1000::1.75::plastic::False"}
    base_registry = {"version": 1, "retired": {"older": prior}}
    errors, _ = scope(base_registry=base_registry,
                      head_registry={"version": 1, "retired": {"older": prior, OLD: entry()}})
    assert any("points at renamed ID" in e for e in errors)
    errors, _ = scope(base_registry=base_registry,
                      head_registry={"version": 1, "retired": {"older": {**prior, "replaced_by": NEW}, OLD: entry()}})
    assert errors == []
    errors, _ = scope(base_registry=base_registry, head_registry={"version": 1, "retired": {
        "older": {**prior, "replaced_by": NEW, "ref": "edited"}, OLD: entry()}})
    assert any("existing entry changed ref" in e for e in errors)
    errors, _ = scope(base_registry=base_registry,
                      head_registry={"version": 1, "retired": {"older": {**prior, "replaced_by": "keep"}, OLD: entry()}})
    assert any("was not renamed to it" in e for e in errors)


def test_build_registry_repoints_existing_target():
    prior = {"replaced_by": OLD, "reason": "duplicate", "ref": "docs/audits/x.json", "source": "c" * 40,
             "retired_key": "k"}
    registry, repointed, problems = build_registry({"version": 1, "retired": {"older": prior}},
                                                   [(OLD, NEW, OLD_KEY, NEW_KEY)], "ref", "b" * 40)
    assert problems == []
    assert repointed == [("older", OLD, NEW)]
    assert registry["retired"]["older"] == {**prior, "replaced_by": NEW}
    assert registry["retired"][OLD]["replaced_by"] == NEW
    assert prior["replaced_by"] == OLD  # input registry untouched


# --- End-to-end helper runs in a scratch git repository ---

import subprocess  # noqa: E402

import scripts.compile_id_baseline as baseline_module  # noqa: E402
import scripts.rename_migration as migration  # noqa: E402

REVIEW = "https://github.com/Icezaza2543/SpoolmanDB-Community/issues/72"


@pytest.fixture
def repo(tmp_path, monkeypatch):
    """add:north-style file whose retired duplicate A points at B, which the rename turns into C."""
    sources, contracts = tmp_path / "filaments", tmp_path / "contracts"
    sources.mkdir()
    contracts.mkdir()
    group = {"name": "PETG - {color_name}", "material": "PETG", "density": 1.27,
             "weights": [{"weight": 1000, "spool_type": "plastic"}], "diameters": [1.75],
             "colors": [{"name": "Gray", "hex": "888888"}, {"name": "Black", "hex": "000000"}]}
    dup = {**group, "name": "Acme PETG - {color_name}", "colors": [{"name": "Grey", "hex": "888888"}]}
    keep = {**group, "name": "HF {color_name}", "colors": [{"name": "Red", "hex": "FF0000"}]}
    source = sources / "acme.json"
    baseline = contracts / "compiled_id_baseline.json"
    monkeypatch.setattr(baseline_module, "BASELINE_PATH", baseline)
    source.write_text(json.dumps({"manufacturer": "Acme", "filaments": [dup, group, keep]}, indent=2) + "\n")
    baseline_module.write_baseline_manifest(baseline, sources)
    manifest = json.loads(baseline.read_text())["manifest"]
    dup_key = next(k for k in manifest if "Acme PETG - Grey" in k)
    gray_key = next(k for k in manifest if "::PETG - Gray::" in k)
    source.write_text(json.dumps({"manufacturer": "Acme", "filaments": [group, keep]}, indent=2) + "\n")
    (contracts / "retired_ids.json").write_text(json.dumps({"version": 1, "retired": {manifest[dup_key]: {
        "replaced_by": manifest[gray_key], "reason": "duplicate", "ref": "#66", "source": "a" * 40,
        "retired_key": dup_key}}}, indent=2) + "\n")
    baseline_module.write_baseline_manifest(baseline, sources, base_baseline_path={"version": 1, "count": len(manifest), "manifest": manifest},
                                            base_retired={"version": 1, "retired": {}})
    git = ["git", "-c", "user.name=t", "-c", "user.email=t@example.invalid"]
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run([*git, "commit", "-qm", "base"], cwd=tmp_path, check=True)
    monkeypatch.setattr(migration, "ROOT", tmp_path)
    monkeypatch.setattr(migration, "REGISTRY_PATH", contracts / "retired_ids.json")
    return tmp_path, manifest[dup_key]


def run(*extra):
    return migration.main(["--file", "acme.json", "--rename", "PETG - {color_name}", "{color_name}", "PETG",
                           "--ref", REVIEW, "--source", "b" * 40, "--base-ref", "HEAD", *extra])


def snapshot(root):
    return {p: p.read_bytes() for p in sorted(root.glob("*/*.json"))}


def test_apply_repoints_existing_retirement_and_passes_checks(repo):
    root, dup_id = repo
    assert run() == 0
    assert run("--apply") == 0
    retired = json.loads((root / "contracts" / "retired_ids.json").read_text())["retired"]
    assert retired[dup_id] == {"replaced_by": "acme_petg_gray_1000_175_p", "reason": "duplicate", "ref": "#66",
                               "source": "a" * 40,
                               "retired_key": "acme.json::Acme::Acme PETG - {color_name}::Acme PETG - Grey::PETG::1000::1.75::plastic::False"}
    assert retired["acme_petg_petg-gray_1000_175_p"]["replaced_by"] == "acme_petg_gray_1000_175_p"
    assert retired["acme_petg_petg-black_1000_175_p"]["replaced_by"] == "acme_petg_black_1000_175_p"
    from scripts.retired_ids import load_contract
    base, errors = baseline_module.load_baseline_payload("HEAD", root)
    assert errors == []
    result = baseline_module.check_baseline_manifest_detailed(
        root / "contracts" / "compiled_id_baseline.json", root / "filaments", base, True,
        retired_path=root / "contracts" / "retired_ids.json",
        base_retired=load_contract("HEAD", root, "retired_ids.json", "retired"))
    assert result.all_errors == []
    assert migration.main(["--verify", "--base-ref", "HEAD"]) == 0


def test_failed_validation_writes_nothing_in_dry_run_or_apply(repo, monkeypatch):
    root, _ = repo
    before = snapshot(root)
    monkeypatch.setattr(migration, "verify_rename_scope", lambda *a: (["boom"], {}))
    assert run() == 1
    assert run("--apply") == 1
    assert snapshot(root) == before


def test_registry_problem_is_reported_by_dry_run(repo, monkeypatch):
    root, _ = repo
    before = snapshot(root)
    monkeypatch.setattr(migration, "build_registry", lambda registry, *a: (registry, [], ["already retired"]))
    assert run() == 1
    assert snapshot(root) == before


def test_write_all_restores_every_file_on_failure(tmp_path):
    first, second = tmp_path / "a.json", tmp_path / "b.json"
    first.write_text("a")
    second.write_text("b")
    with pytest.raises(OSError):
        write_all({first: b"new", second: b"new", tmp_path / "missing" / "c.json": b"new"})
    assert (first.read_text(), second.read_text()) == ("a", "b")
    assert not (tmp_path / "missing").exists()


def test_uncommitted_edit_in_renamed_file_is_refused(repo):
    root, _ = repo
    source = root / "filaments" / "acme.json"
    source.write_text(source.read_text().replace('"FF0000"', '"EE0000"'))
    before = snapshot(root)
    assert run() == 1
    assert run("--apply") == 1
    assert snapshot(root) == before


def test_uncommitted_other_manufacturer_file_is_refused(repo):
    root, _ = repo
    (root / "filaments" / "other.json").write_text(json.dumps({"manufacturer": "Other", "filaments": []}))
    before = snapshot(root)
    assert run("--apply") == 1
    assert snapshot(root) == before


def test_committed_unrelated_change_after_base_ref_fails_scope(repo, capsys):
    root, _ = repo
    source = root / "filaments" / "acme.json"
    data = json.loads(source.read_text())
    data["filaments"][1]["colors"].append({"name": "Blue", "hex": "0000FF"})
    source.write_text(json.dumps(data, indent=2) + "\n")
    subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@example.invalid",
                    "commit", "-qam", "unrelated"], cwd=root, check=True)
    before = snapshot(root)
    assert run("--base-ref", "HEAD~1") == 1
    assert "not rename replacements: acme_petg_hfblue_1000_175_p" in capsys.readouterr().err
    assert run("--base-ref", "HEAD~1", "--apply") == 1
    assert snapshot(root) == before
