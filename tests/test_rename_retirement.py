import json

import pytest

from scripts.compile_id_baseline import make_canonical_identity_key
from scripts.duplicate_catalog import corrected_rename_identity, rename_identity
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


def check(head, *, historical=None, current=None, audits=None):
    from scripts.retired_ids import check_registry
    current = current if current is not None else {NEW_KEY: NEW}
    return check_registry(head, {"version": 1, "retired": {}},
                          historical if historical is not None else {OLD_KEY: OLD},
                          current, current, audits=audits)


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


def test_reviewed_manufacturer_correction_matches_physical_identity():
    old_key = key("grillon3 PLA | {color_name}", "Black", material="PLA", manufacturer="NTH Grillon",
                  filename="NTHGrillon.json")
    new_key = key("grilon3 {color_name}", "Black", material="PLA", manufacturer="NTH Grilon",
                  filename="NTHGrilon.json")
    old_id, new_id = "old-nth-id", "new-nth-id"
    audited = {old_id: {"key": old_key,
                        "rename": {"replaced_by": new_id, "new_key": new_key},
                        "correction": {
                            "manufacturer": ["NTH Grillon", "NTH Grilon"],
                            "file": ["NTHGrillon.json", "NTHGrilon.json"],
                            "spelling": ["Grillon", "Grilon"],
                        }}}
    assert corrected_rename_identity(old_key) == corrected_rename_identity(new_key)
    errors, retired, _ = check(
        {"version": 1, "retired": {old_id: {**entry(), "replaced_by": new_id, "retired_key": old_key}}},
        historical={old_key: old_id}, current={new_key: new_id}, audits=audited,
    )
    assert errors == []
    assert retired == {old_id}


def test_reviewed_manufacturer_correction_audit_must_match_exact_target():
    old_key = key("grillon3 PLA | {color_name}", "Black", material="PLA", manufacturer="NTH Grillon",
                  filename="NTHGrillon.json")
    new_key = key("grilon3 {color_name}", "Black", material="PLA", manufacturer="NTH Grilon",
                  filename="NTHGrilon.json")
    old_id, new_id = "old-nth-id", "new-nth-id"
    audited = {old_id: {"key": old_key,
                        "rename": {"replaced_by": new_id, "new_key": OLD_KEY},
                        "correction": {
                            "manufacturer": ["NTH Grillon", "NTH Grilon"],
                            "file": ["NTHGrillon.json", "NTHGrilon.json"],
                            "spelling": ["Grillon", "Grilon"],
                        }}}
    errors, _, _ = check(
        {"version": 1, "retired": {old_id: {**entry(), "replaced_by": new_id, "retired_key": old_key}}},
        historical={old_key: old_id}, current={new_key: new_id}, audits=audited,
    )
    assert "reviewed correction mapping does not match" in " ".join(errors)


def test_reviewed_manufacturer_correction_rejects_unapproved_product_line():
    from scripts.duplicate_catalog import corrected_rename_pair
    old_key = key("grillon3 PLA | {color_name}", "Black", material="PLA", manufacturer="NTH Grillon",
                  filename="NTHGrillon.json")
    different_key = key("Totally Different {color_name}", "Black", material="PLA",
                        manufacturer="NTH Grilon", filename="NTHGrilon.json")
    correction = {
        "manufacturer": ["NTH Grillon", "NTH Grilon"],
        "file": ["NTHGrillon.json", "NTHGrilon.json"],
        "spelling": ["Grillon", "Grilon"],
    }
    assert corrected_rename_pair(old_key, different_key, correction) is False


def test_reviewed_manufacturer_correction_accepts_spelling_and_material_line():
    from scripts.duplicate_catalog import corrected_rename_pair
    old_key = key("grillon3 PLA | {color_name}", "Black", material="PLA", manufacturer="NTH Grillon",
                  filename="NTHGrillon.json")
    new_key = key("grilon3 {color_name}", "Black", material="PLA", manufacturer="NTH Grilon",
                  filename="NTHGrilon.json")
    correction = {
        "manufacturer": ["NTH Grillon", "NTH Grilon"],
        "file": ["NTHGrillon.json", "NTHGrilon.json"],
        "spelling": ["Grillon", "Grilon"],
    }
    assert corrected_rename_pair(old_key, new_key, correction) is True


def test_reviewed_manufacturer_correction_never_rewrites_color_label():
    from scripts.duplicate_catalog import corrected_rename_pair
    old_key = key("{color_name}", "Grillon", material="PLA", manufacturer="NTH Grillon",
                  filename="NTHGrillon.json")
    new_key = key("{color_name}", "Grilon", material="PLA", manufacturer="NTH Grilon",
                  filename="NTHGrilon.json")
    correction = {
        "manufacturer": ["NTH Grillon", "NTH Grilon"],
        "file": ["NTHGrillon.json", "NTHGrilon.json"],
        "spelling": ["Grillon", "Grilon"],
    }
    assert corrected_rename_pair(old_key, new_key, correction) is False


def test_reviewed_manufacturer_correction_rejects_unrelated_line_change():
    from scripts.duplicate_catalog import corrected_rename_pair
    old_key = key("grillon3 Basic | {color_name}", "Black", material="PLA",
                  manufacturer="NTH Grillon", filename="NTHGrillon.json")
    new_key = key("grilon3 HF | {color_name}", "Black", material="PLA",
                  manufacturer="NTH Grilon", filename="NTHGrilon.json")
    correction = {
        "manufacturer": ["NTH Grillon", "NTH Grilon"],
        "file": ["NTHGrillon.json", "NTHGrilon.json"],
        "spelling": ["Grillon", "Grilon"],
    }
    assert corrected_rename_pair(old_key, new_key, correction) is False


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


def test_registry_repointed_duplicate_through_correction_passes_check_registry():
    from scripts.retired_ids import check_registry
    old_key = key("grillon3 PLA | {color_name}", "Black", material="PLA", manufacturer="NTH Grillon",
                  filename="NTHGrillon.json")
    new_key = key("grilon3 {color_name}", "Black", material="PLA", manufacturer="NTH Grilon",
                  filename="NTHGrilon.json")
    old_id, target_id, newer_id = "older", "old-target", "new-target"
    prior = {"replaced_by": target_id, "reason": "duplicate", "ref": "#66",
             "source": "a" * 40, "retired_key": old_key}
    base_registry = {"version": 1, "retired": {"older": prior}}
    head_registry = {"version": 1, "retired": {
        "older": {**prior, "replaced_by": newer_id},
        target_id: {"replaced_by": newer_id, "reason": "rename", "ref": "#76",
                    "source": "b" * 40, "retired_key": old_key},
    }}
    audited = {
        target_id: {"key": old_key, "rename": {"replaced_by": newer_id, "new_key": new_key},
                    "correction": {
                        "manufacturer": ["NTH Grillon", "NTH Grilon"],
                        "file": ["NTHGrillon.json", "NTHGrilon.json"],
                        "spelling": ["Grillon", "Grilon"],
                    }},
    }
    errors, _, _ = check_registry(
        head_registry, base_registry,
        {old_key: target_id},
        {new_key: newer_id},
        {new_key: newer_id},
        audits=audited,
    )
    assert errors == []


def test_registry_repoint_rejects_unrelated_correction_binding():
    from scripts.retired_ids import check_registry
    old_key = key("grillon3 PLA | {color_name}", "Black", material="PLA", manufacturer="NTH Grillon",
                  filename="NTHGrillon.json")
    new_key = key("grilon3 {color_name}", "Black", material="PLA", manufacturer="NTH Grilon",
                  filename="NTHGrilon.json")
    unrelated_key = key("Totally Different {color_name}", "Black", material="PLA",
                        manufacturer="NTH Grillon", filename="NTHGrillon.json")
    base_registry = {"version": 1, "retired": {
        "older": {"replaced_by": "old-target", "reason": "duplicate", "ref": "#66",
                  "source": "a" * 40, "retired_key": old_key},
    }}
    head_registry = {"version": 1, "retired": {
        "older": {"replaced_by": "new-target", "reason": "duplicate", "ref": "#66",
                  "source": "a" * 40, "retired_key": old_key},
        "old-target": {"replaced_by": "new-target", "reason": "rename", "ref": "#76",
                       "source": "b" * 40, "retired_key": unrelated_key},
    }}
    audited = {
        "old-target": {"key": unrelated_key,
                       "rename": {"replaced_by": "new-target", "new_key": new_key},
                       "correction": {
                           "manufacturer": ["NTH Grillon", "NTH Grilon"],
                           "file": ["NTHGrillon.json", "NTHGrilon.json"],
                           "spelling": ["Grillon", "Grilon"],
                       }},
    }
    errors, _, _ = check_registry(
        head_registry, base_registry,
        {unrelated_key: "old-target"},
        {new_key: "new-target"},
        {new_key: "new-target"},
        audits=audited,
    )
    assert any("identity mismatch" in error for error in errors)


@pytest.mark.parametrize("order", ["correction-then-rename", "rename-then-correction"])
def test_registry_repoint_alias_survives_sequential_correction_and_rename(order):
    from scripts.retired_ids import check_registry

    if order == "correction-then-rename":
        correction_old = key("grillon3 PLA | {color_name}", "Black", material="PLA",
                             manufacturer="NTH Grillon", filename="NTHGrillon.json")
        correction_new = key("grilon3 PLA | {color_name}", "Black", material="PLA",
                             manufacturer="NTH Grilon", filename="NTHGrilon.json")
        final_key = key("grilon3 {color_name}", "Black", material="PLA",
                        manufacturer="NTH Grilon", filename="NTHGrilon.json")
        correction_id, intermediate_id = "correction-old", "intermediate"
        alias_key = key("grilon3 PLA PLA | {color_name}", "Black", material="PLA",
                        manufacturer="NTH Grilon", filename="NTHGrilon.json")
        base_retired = {
            correction_id: {"replaced_by": intermediate_id, "reason": "rename", "ref": "#76",
                            "source": "b" * 40, "retired_key": correction_old},
            "alias": {"replaced_by": intermediate_id, "reason": "duplicate", "ref": "#66",
                      "source": "a" * 40, "retired_key": alias_key},
        }
        head_retired = {
            correction_id: {**base_retired[correction_id], "replaced_by": "final"},
            "alias": {**base_retired["alias"], "replaced_by": "final"},
            intermediate_id: {"replaced_by": "final", "reason": "rename", "ref": "#77",
                              "source": "c" * 40, "retired_key": correction_new},
        }
        base_manifest = {correction_old: correction_id, correction_new: intermediate_id,
                         alias_key: "alias"}
        audits = {
            correction_id: {"key": correction_old,
                            "rename": {"replaced_by": intermediate_id, "new_key": correction_new},
                            "correction": {
                                "manufacturer": ["NTH Grillon", "NTH Grilon"],
                                "file": ["NTHGrillon.json", "NTHGrilon.json"],
                                "spelling": ["Grillon", "Grilon"],
                            }},
        }
    else:
        ordinary_old = key("NTH Grillon grillon3 PLA | {color_name}", "Black", material="PLA",
                           manufacturer="NTH Grillon", filename="NTHGrillon.json")
        correction_old = key("grillon3 PLA | {color_name}", "Black", material="PLA",
                             manufacturer="NTH Grillon", filename="NTHGrillon.json")
        final_key = key("grilon3 PLA | {color_name}", "Black", material="PLA",
                        manufacturer="NTH Grilon", filename="NTHGrilon.json")
        correction_id = "correction-old"
        alias_key = key("grillon3 PLA PLA | {color_name}", "Black", material="PLA",
                        manufacturer="NTH Grillon", filename="NTHGrillon.json")
        base_retired = {
            "ordinary-old": {"replaced_by": correction_id, "reason": "rename", "ref": "#76",
                             "source": "b" * 40, "retired_key": ordinary_old},
            "alias": {"replaced_by": correction_id, "reason": "duplicate", "ref": "#66",
                      "source": "a" * 40, "retired_key": alias_key},
        }
        head_retired = {
            "ordinary-old": {**base_retired["ordinary-old"], "replaced_by": "final"},
            "alias": {**base_retired["alias"], "replaced_by": "final"},
            correction_id: {"replaced_by": "final", "reason": "rename", "ref": "#77",
                            "source": "c" * 40, "retired_key": correction_old},
        }
        base_manifest = {ordinary_old: "ordinary-old", correction_old: correction_id,
                         alias_key: "alias"}
        audits = {
            correction_id: {"key": correction_old,
                            "rename": {"replaced_by": "final", "new_key": final_key},
                            "correction": {
                                "manufacturer": ["NTH Grillon", "NTH Grilon"],
                                "file": ["NTHGrillon.json", "NTHGrilon.json"],
                                "spelling": ["Grillon", "Grilon"],
                            }},
        }

    errors, _, _ = check_registry(
        {"version": 1, "retired": head_retired},
        {"version": 1, "retired": base_retired},
        base_manifest,
        {final_key: "final"},
        {final_key: "final"},
        audits=audits,
    )
    assert errors == []
    assert head_retired["alias"]["retired_key"] == base_retired["alias"]["retired_key"]
    assert head_retired["alias"]["ref"] == base_retired["alias"]["ref"]


def test_registry_repoint_duplicate_validates_against_next_base_after_correction():
    from scripts.retired_ids import check_registry

    old_key = key("grillon3 PLA | {color_name}", "Black", material="PLA",
                  manufacturer="NTH Grillon", filename="NTHGrillon.json")
    alias_key = key("NTH Grillon grillon3 PLA | {color_name}", "Black", material="PLA",
                    manufacturer="NTH Grillon", filename="NTHGrillon.json")
    new_key = key("grilon3 PLA | {color_name}", "Black", material="PLA",
                  manufacturer="NTH Grilon", filename="NTHGrilon.json")
    alias_id, target_id, new_id = "old-alias", "old-target", "new-target"
    retired = {
        alias_id: {"replaced_by": new_id, "reason": "duplicate", "ref": "#66",
                   "source": "a" * 40, "retired_key": alias_key},
        target_id: {"replaced_by": new_id, "reason": "rename", "ref": "#76",
                    "source": "b" * 40, "retired_key": old_key},
    }
    registry = {"version": 1, "retired": retired}
    audited = {
        target_id: {"key": old_key,
                    "rename": {"replaced_by": new_id, "new_key": new_key},
                    "correction": {
                        "manufacturer": ["NTH Grillon", "NTH Grilon"],
                        "file": ["NTHGrillon.json", "NTHGrilon.json"],
                        "spelling": ["Grillon", "Grilon"],
                    }},
    }

    errors, _, _ = check_registry(
        registry, registry,
        {alias_key: alias_id, old_key: target_id},
        {new_key: new_id},
        {new_key: new_id},
        audits=audited,
    )
    assert errors == []
    assert retired[alias_id]["replaced_by"] == new_id
    assert retired[alias_id]["retired_key"] == alias_key
    assert retired[alias_id]["ref"] == "#66"


def test_registry_rejects_rewriting_preserved_correction_audit():
    from scripts.retired_ids import check_registry
    b_key = key("grillon3 PLA | {color_name}", "Black", material="PLA",
                manufacturer="NTH Grillon", filename="NTHGrillon.json")
    c_key = key("grilon3 PLA | {color_name}", "Black", material="PLA",
                manufacturer="NTH Grilon", filename="NTHGrilon.json")
    d_key = key("grilon3 {color_name}", "Black", material="PLA",
                manufacturer="NTH Grilon", filename="NTHGrilon.json")
    base = {"version": 1, "retired": {
        "b": {"replaced_by": "c", "reason": "rename", "ref": "#76",
              "source": "b" * 40, "retired_key": b_key},
    }}
    head = {"version": 1, "retired": {
        "b": {**base["retired"]["b"], "replaced_by": "d"},
        "c": {"replaced_by": "d", "reason": "rename", "ref": "#77",
              "source": "c" * 40, "retired_key": c_key},
    }}
    audited = {
        "b": {"key": b_key,
              "rename": {"replaced_by": "d", "new_key": d_key},
              "correction": {
                  "manufacturer": ["NTH Grillon", "NTH Grilon"],
                  "file": ["NTHGrillon.json", "NTHGrilon.json"],
                  "spelling": ["Grillon", "Grilon"],
              }},
    }
    errors, _, _ = check_registry(
        head, base, {b_key: "b", c_key: "c"},
        {d_key: "d"}, {d_key: "d"}, audits=audited,
    )
    assert any("audit was rewritten" in error for error in errors)


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


def test_apply_reviewed_manufacturer_and_source_file_correction(repo):
    root, _ = repo
    (root / "docs" / "audits").mkdir(parents=True)
    args = [
        "--file", "newbrand.json", "--previous-file", "acme.json",
        "--manufacturer-rename", "Acme", "New Brand",
        "--rename", "PETG - {color_name}", "PETG {color_name}", "PETG",
        "--ref", "https://github.com/Donkie/SpoolmanDB/pull/546",
        "--source", "b" * 40, "--audit", "docs/audits/brand-correction.json",
        "--base-ref", "HEAD",
    ]
    assert migration.main(args) == 0
    assert migration.main([*args, "--apply"]) == 0
    assert not (root / "filaments" / "acme.json").exists()
    corrected = json.loads((root / "filaments" / "newbrand.json").read_text())
    assert corrected["manufacturer"] == "New Brand"
    registry = json.loads((root / "contracts" / "retired_ids.json").read_text())["retired"]
    assert all(entry["ref"] == "docs/audits/brand-correction.json" for entry in registry.values()
               if entry["source"] == "b" * 40)
    assert migration.main(["--verify", "--base-ref", "HEAD"]) == 0


def test_failed_validation_writes_nothing_in_dry_run_or_apply(repo, monkeypatch):
    root, _ = repo
    before = snapshot(root)
    monkeypatch.setattr(migration, "verify_rename_scope", lambda *a, **kwargs: (["boom"], {}))
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


def commit(root, message):
    subprocess.run(["git", "add", "-A"], cwd=root, check=True)
    subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@example.invalid", "commit", "-qm", message],
                   cwd=root, check=True)


def test_group_with_display_name_override_is_refused(repo, capsys):
    root, _ = repo
    source = root / "filaments" / "acme.json"
    data = json.loads(source.read_text())
    data["filaments"][0]["colors"][0]["display_name"] = "PETG Light Gray"
    source.write_text(json.dumps(data, indent=2) + "\n")
    commit(root, "display name")
    before = snapshot(root)
    assert run("--apply") == 1
    assert "has display_name overrides" in capsys.readouterr().err
    assert snapshot(root) == before


def test_ci_verify_runs_only_when_renames_are_added(repo):
    root, _ = repo
    verify = ["--verify", "--if-renames", "--base-ref"]
    assert migration.main([*verify, "HEAD"]) == 0              # no rename retirements: skipped
    assert migration.main(["--verify", "--base-ref", "HEAD"]) == 1  # without the flag it is required
    assert run("--apply") == 0
    commit(root, "rename")
    assert migration.main([*verify, "HEAD~1"]) == 0
    source = root / "filaments" / "acme.json"
    data = json.loads(source.read_text())
    data["filaments"][1]["colors"][0]["hex"] = "EE0000"
    source.write_text(json.dumps(data, indent=2) + "\n")
    commit(root, "unrelated")
    assert migration.main([*verify, "HEAD~2"]) == 1           # rename mixed with another change fails


# --- --keep and unmatched renames ---

from scripts.rename_migration import unmatched_renames  # noqa: E402


def keep_source(*groups):
    return json.dumps({"manufacturer": "Acme", "filaments": list(groups)}, indent=2) + "\n"


def petg(name, *colors):
    return {"name": name, "material": "PETG", "colors": [{"name": color} for color in colors]}


def test_rename_source_keep_skips_fully_kept_group_and_splits_partly_kept_group():
    text = keep_source(petg("PETG - {color_name}", "White"), petg("PETG - {color_name}", "Red", "Rock White", "Blue"),
                       petg("HF {color_name}", "Black"))
    result, count = rename_source(text, {("PETG - {color_name}", "PETG"): "{color_name}"},
                                  keep={("PETG - {color_name}", "White"), ("PETG - {color_name}", "Rock White")})
    groups = json.loads(result)["filaments"]
    assert count == 1
    assert [(g["name"], [c["name"] for c in g["colors"]]) for g in groups] == [
        ("PETG - {color_name}", ["White"]),
        ("{color_name}", ["Red", "Blue"]),
        ("PETG - {color_name}", ["Rock White"]),
        ("HF {color_name}", ["Black"]),
    ]
    assert result == json.dumps(json.loads(result), indent=2, ensure_ascii=False) + "\n"


def test_rename_source_keep_must_match_a_renamed_color():
    text = keep_source(petg("PETG - {color_name}", "Red"), petg("HF {color_name}", "Black"))
    renames = {("PETG - {color_name}", "PETG"): "{color_name}"}
    with pytest.raises(ValueError, match="--keep matched no color"):
        rename_source(text, renames, keep={("PETG - {color_name}", "Purple")})
    with pytest.raises(ValueError, match="--keep matched no color"):
        rename_source(text, renames, keep={("HF {color_name}", "Black")})  # group is not being renamed


def test_rename_source_split_refuses_non_standard_formatting():
    text = keep_source(petg("PETG - {color_name}", "Red", "Rock White")).replace("\n  ", "\n    ")
    with pytest.raises(ValueError, match="without reformatting"):
        rename_source(text, {("PETG - {color_name}", "PETG"): "{color_name}"},
                      keep={("PETG - {color_name}", "Rock White")})


def test_apply_with_keep_leaves_kept_color_on_its_id_and_passes_checks(repo, capsys):
    root, dup_id = repo
    before_ids = set(json.loads((root / "contracts" / "compiled_id_baseline.json").read_text())["manifest"].values())
    assert run("--keep", "PETG - {color_name}", "Black", "--apply") == 0
    out = capsys.readouterr().out
    assert "KEEP 'Black' in 'PETG - {color_name}'" in out
    assert "1 group(s) renamed, 1 public ID(s) retired as renames" in out
    retired = json.loads((root / "contracts" / "retired_ids.json").read_text())["retired"]
    assert "acme_petg_petg-black_1000_175_p" not in retired
    assert retired["acme_petg_petg-gray_1000_175_p"]["replaced_by"] == "acme_petg_gray_1000_175_p"
    assert retired[dup_id]["replaced_by"] == "acme_petg_gray_1000_175_p"
    after_ids = set(json.loads((root / "contracts" / "compiled_id_baseline.json").read_text())["manifest"].values())
    assert "acme_petg_petg-black_1000_175_p" in before_ids & after_ids
    groups = json.loads((root / "filaments" / "acme.json").read_text())["filaments"]
    assert [(g["name"], [c["name"] for c in g["colors"]]) for g in groups] == [
        ("{color_name}", ["Gray"]), ("PETG - {color_name}", ["Black"]), ("HF {color_name}", ["Red"])]
    assert migration.main(["--verify", "--base-ref", "HEAD"]) == 0


def test_unmatched_keep_is_reported_and_writes_nothing(repo, capsys):
    root, _ = repo
    before = snapshot(root)
    assert run("--keep", "PETG - {color_name}", "Purple", "--apply") == 1
    assert "--keep matched no color of a renamed group: 'PETG - {color_name}' 'Purple'" in capsys.readouterr().err
    assert snapshot(root) == before


def test_unmatched_renames_lists_missing_groups():
    text = keep_source(petg("PETG - {color_name}", "Red"))
    assert unmatched_renames(text, {("PETG - {color_name}", "PETG"): "a", ("PETG - {color_name}", "PLA"): "b",
                                    ("Ghost {color_name}", "PETG"): "c"}) == [
        ("Ghost {color_name}", "PETG"), ("PETG - {color_name}", "PLA")]


def test_explicit_rename_of_missing_group_is_an_error(repo, capsys):
    root, _ = repo
    before = snapshot(root)
    with pytest.raises(SystemExit) as exc:
        run("--rename", "Ghost {color_name}", "{color_name}", "PLA")
    assert exc.value.code == 2
    assert "--rename names a group that does not exist: 'Ghost {color_name}' [PLA]" in capsys.readouterr().err
    assert snapshot(root) == before


def upstream_args():
    return ["--file", "acme.json", "--upstream", "HEAD", "HEAD", "--ref", REVIEW, "--source", "b" * 40,
            "--base-ref", "HEAD"]


def test_upstream_renames_missing_here_are_skipped(repo, monkeypatch, capsys):
    root, _ = repo
    monkeypatch.setattr(migration, "upstream_renames", lambda *a: ({
        ("Ghost {color_name}", "PLA"): "{color_name}", ("PETG - {color_name}", "PETG"): "{color_name}"}, []))
    assert migration.main([*upstream_args(), "--apply"]) == 0
    out = capsys.readouterr().out
    assert "SKIP (no group named 'Ghost {color_name}' [PLA] in acme.json)" in out
    assert "2 public ID(s) retired as renames" in out


def test_upstream_with_no_matching_group_fails_cleanly(repo, monkeypatch, capsys):
    root, _ = repo
    before = snapshot(root)
    monkeypatch.setattr(migration, "upstream_renames", lambda *a: ({("Ghost {color_name}", "PLA"): "{color_name}"}, []))
    assert migration.main([*upstream_args(), "--apply"]) == 1
    assert "none of the requested renames match a group in acme.json" in capsys.readouterr().err
    assert snapshot(root) == before
