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
