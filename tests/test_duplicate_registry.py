import copy
import json

import pytest

from scripts.compile_id_baseline import (
    check_baseline_manifest_detailed,
    compile_current_id_manifest,
    make_canonical_identity_key,
    write_baseline_manifest,
)


def key(template, name, *, weight=1000, diameter=1.75, spool="plastic", refill=False):
    return make_canonical_identity_key("acme.json", "Acme", template, name, "PETG", weight, diameter, spool, refill)


OLD_KEY = key("Acme PETG {color_name}", "Acme PETG Grey")
KEEP_KEY = key("PETG {color_name}", "PETG Gray")
THIRD_KEY = key("PETG ({color_name})", "PETG (Gray)")
OLD, KEEP, THIRD = "old_id", "keep_id", "third_id"


def registry(entries=None):
    return {"version": 1, "retired": entries or {}}


def entry(target=KEEP, retired_key=OLD_KEY):
    return {"replaced_by": target, "reason": "duplicate", "ref": "#66", "source": "a" * 40, "retired_key": retired_key}


def check(head=None, base=None, historical=None, current=None, enrolled=None, audits=None):
    from scripts.retired_ids import check_registry
    return check_registry(
        head or registry({OLD: entry()}), base or registry(),
        historical if historical is not None else {OLD_KEY: OLD, KEEP_KEY: KEEP},
        current if current is not None else {KEEP_KEY: KEEP},
        enrolled if enrolled is not None else {KEEP_KEY: KEEP}, audits=audits,
    )


def test_registered_retirement_passes_and_is_counted():
    errors, retired, restored = check()
    assert errors == []
    assert retired == {OLD}
    assert restored == set()


@pytest.mark.parametrize("mutation, expected", [
    (lambda r: r["retired"][OLD].update(replaced_by="absent"), "surviving"),
    (lambda r: r["retired"][OLD].update(replaced_by=OLD), "self"),
    (lambda r: r["retired"][OLD].update(retired_key=KEEP_KEY), "trusted"),
    (lambda r: r["retired"][OLD].update(source="unverified"), "source"),
    (lambda r: r["retired"][OLD].pop("retired_key"), "fields"),
    (lambda r: r.update(version=True), "version"),
])
def test_invalid_registry_fails_closed(mutation, expected):
    payload = registry({OLD: entry()})
    mutation(payload)
    assert expected in " ".join(check(head=payload)[0])


def test_fabricated_retired_id_is_rejected():
    assert "historical" in " ".join(check(head=registry({"fake_id": entry()}))[0])


def test_new_replacement_id_is_rejected():
    assert "existing" in " ".join(check(current={KEEP_KEY: "new_id"}, enrolled={KEEP_KEY: "new_id"}, head=registry({OLD: entry("new_id")}))[0])


@pytest.mark.parametrize("replacement", [
    key("PETG {color_name}", "PETG White"),
    key("PETG Basic {color_name}", "PETG Basic Gray"),
    key("PETG {color_name}", "PETG Gray", weight=500),
    key("PETG {color_name}", "PETG Gray", diameter=2.85),
    key("PETG {color_name}", "PETG Gray", spool="cardboard"),
    key("PETG {color_name}", "PETG Gray", spool=None, refill=True),
])
def test_cross_identity_mapping_fails(replacement):
    errors, _, _ = check(historical={OLD_KEY: OLD, replacement: KEEP}, current={replacement: KEEP}, enrolled={replacement: KEEP})
    assert "identity" in " ".join(errors)


def test_registered_id_must_not_reappear():
    assert "reappear" in " ".join(check(current={OLD_KEY: OLD, KEEP_KEY: KEEP}, enrolled={OLD_KEY: OLD, KEEP_KEY: KEEP})[0])


def test_cycles_and_chains_fail():
    payload = registry({OLD: entry(KEEP), KEEP: entry(OLD, KEEP_KEY)})
    assert "chain" in " ".join(check(head=payload)[0])


def test_old_entries_need_no_git_history_and_can_repoint_newly_retired_target():
    base = registry({OLD: entry()})
    head = registry({OLD: entry(THIRD), KEEP: entry(THIRD, KEEP_KEY)})
    errors, retired, _ = check(head=head, base=base, historical={KEEP_KEY: KEEP, THIRD_KEY: THIRD}, current={THIRD_KEY: THIRD}, enrolled={THIRD_KEY: THIRD})
    assert errors == []
    assert retired == {OLD, KEEP}


def test_arbitrary_repoint_and_evidence_edits_fail():
    base = registry({OLD: entry()})
    head = copy.deepcopy(base)
    head["retired"][OLD]["source"] = "b" * 40
    assert "immutable" in " ".join(check(head=head, base=base)[0])
    head = registry({OLD: entry(THIRD)})
    assert "re-point" in " ".join(check(head=head, base=base, current={KEEP_KEY: KEEP, THIRD_KEY: THIRD}, enrolled={KEEP_KEY: KEEP, THIRD_KEY: THIRD})[0])


def test_exact_reinstatement_passes():
    errors, retired, restored = check(head=registry(), base=registry({OLD: entry()}), historical={KEEP_KEY: KEEP}, current={OLD_KEY: OLD, KEEP_KEY: KEEP}, enrolled={OLD_KEY: OLD, KEEP_KEY: KEEP})
    assert errors == []
    assert retired == set()
    assert restored == {OLD}


def test_reinstatement_with_different_key_fails():
    renamed = OLD_KEY.replace("Grey", "Gray")
    assert "exact reinstatement" in " ".join(check(head=registry(), base=registry({OLD: entry()}), historical={KEEP_KEY: KEEP}, current={renamed: OLD, KEEP_KEY: KEEP}, enrolled={renamed: OLD, KEEP_KEY: KEEP})[0])


def test_registry_deletion_without_reinstatement_fails():
    assert "exact reinstatement" in " ".join(check(head=registry(), base=registry({OLD: entry()}))[0])


def test_reinstatement_requires_baseline_reenrollment():
    assert "exact reinstatement" in " ".join(check(head=registry(), base=registry({OLD: entry()}), current={OLD_KEY: OLD, KEEP_KEY: KEEP})[0])


def test_reviewed_decomposition_keeps_physical_color_words():
    old_key = key("{color_name}", "Acme PETG Grey")
    audit = {OLD: {"key": old_key, "line": "PETG", "color": "Grey"}, KEEP: {"key": KEEP_KEY, "line": "PETG", "color": "Gray"}}
    args = dict(head=registry({OLD: entry(retired_key=old_key)}), historical={old_key: OLD, KEEP_KEY: KEEP})
    assert check(**args, audits=audit)[0] == []
    audit[OLD]["color"] = "White"
    assert "identity" in " ".join(check(**args, audits=audit)[0])


def test_display_name_cannot_hide_basic_qualifier_from_reviewed_identity():
    old_key = key("PETG Basic {color_name}", "Black")
    keep_key = key("PETG {color_name}", "Black")
    bindings = {OLD: {"key": old_key, "line": "PETG", "color": "Black"}, KEEP: {"key": keep_key, "line": "PETG", "color": "Black"}}
    errors, _, _ = check(head=registry({OLD: entry(retired_key=old_key)}), historical={old_key: OLD, keep_key: KEEP}, current={keep_key: KEEP}, enrolled={keep_key: KEEP}, audits=bindings)
    assert "identity" in " ".join(errors)


def test_legitimate_display_name_binding_preserves_source_line_and_color():
    old_key = key("Acme PETG Basic {color_name}", "Black")
    keep_key = key("PETG Basic {color_name}", "PETG Basic Black")
    bindings = {OLD: {"key": old_key, "line": "PETG Basic", "color": "Black", "source_color": "Black"}}
    errors, _, _ = check(head=registry({OLD: entry(retired_key=old_key)}), historical={old_key: OLD, keep_key: KEEP}, current={keep_key: KEEP}, enrolled={keep_key: KEEP}, audits=bindings)
    assert errors == []


@pytest.mark.parametrize("fabricated", [False, True])
def test_no_base_enrollment_rejects_new_target_and_fabricated_retirement(tmp_path, fabricated):
    sources, contracts = tmp_path / "filaments", tmp_path / "contracts"
    sources.mkdir()
    contracts.mkdir()
    source = sources / "acme.json"
    old_definition = {"name": "Acme PETG {color_name}", "material": "PETG", "density": 1.27, "weights": [{"weight": 1000, "spool_type": "plastic"}], "diameters": [1.75], "colors": [{"name": "Grey", "hex": "888888"}]}
    survivor = {**old_definition, "name": "PETG {color_name}", "colors": [{"name": "Gray", "hex": "888888"}]}
    source.write_text(json.dumps({"manufacturer": "Acme", "filaments": [survivor if fabricated else old_definition]}))
    baseline = contracts / "compiled_id_baseline.json"
    write_baseline_manifest(baseline, sources)
    before = json.loads(baseline.read_text())["manifest"]
    source.write_text(json.dumps({"manufacturer": "Acme", "filaments": [survivor]}))
    after, _ = compile_current_id_manifest(sources)
    keep_id = after[KEEP_KEY]
    old_id = "fabricated" if fabricated else before[OLD_KEY]
    (contracts / "retired_ids.json").write_text(json.dumps(registry({old_id: entry(keep_id)})))
    result = check_baseline_manifest_detailed(baseline, sources, enrollment=True)
    assert ("historical" if fabricated else "existing") in " ".join(result.all_errors)
    with pytest.raises(SystemExit):
        write_baseline_manifest(baseline, sources)


def test_missing_local_audit_reference_fails_closed(tmp_path):
    from scripts.retired_ids import reviewed_bindings
    payload = registry({OLD: {**entry(), "ref": "docs/missing-audit.json"}})
    with pytest.raises(ValueError, match="exist"):
        reviewed_bindings(payload, tmp_path)


def test_safe_baseline_enrollment_drops_only_registered_key(tmp_path):
    sources = tmp_path / "filaments"
    contracts = tmp_path / "contracts"
    sources.mkdir()
    contracts.mkdir()
    source = sources / "acme.json"
    definition = {"name": "Acme PETG {color_name}", "material": "PETG", "density": 1.27, "weights": [{"weight": 1000, "spool_type": "plastic"}], "diameters": [1.75], "colors": [{"name": "Grey", "hex": "888888"}]}
    survivor = {**definition, "name": "PETG {color_name}", "colors": [{"name": "Gray", "hex": "888888"}]}
    source.write_text(json.dumps({"manufacturer": "Acme", "filaments": [definition, survivor]}))
    baseline = contracts / "compiled_id_baseline.json"
    write_baseline_manifest(baseline, sources)
    historical = json.loads(baseline.read_text())
    old_id, keep_id = historical["manifest"][OLD_KEY], historical["manifest"][KEEP_KEY]
    source.write_text(json.dumps({"manufacturer": "Acme", "filaments": [survivor]}))
    (contracts / "retired_ids.json").write_text(json.dumps(registry({old_id: entry(keep_id)})))
    write_baseline_manifest(baseline, sources)
    current, errors = compile_current_id_manifest(sources)
    assert errors == []
    assert json.loads(baseline.read_text())["manifest"] == current == {KEEP_KEY: keep_id}
    result = check_baseline_manifest_detailed(baseline, sources, historical, True, base_retired=registry())
    assert result.all_errors == []
    assert result.stats["retired"] == 1


def test_unregistered_removal_still_refuses_update(tmp_path):
    sources = tmp_path / "filaments"
    sources.mkdir()
    baseline = tmp_path / "compiled_id_baseline.json"
    baseline.write_text(json.dumps({"version": 1, "count": 1, "manifest": {OLD_KEY: OLD}}))
    with pytest.raises(SystemExit):
        write_baseline_manifest(baseline, sources)
