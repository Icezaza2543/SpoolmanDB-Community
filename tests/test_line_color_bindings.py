"""Moved qualifiers must remain anchored to the other exact template."""
import pytest

from scripts import duplicate_catalog as catalog


def key(template, color, material="PLA", spool="plastic", weight=1000):
    return "::".join(("acme.json", "Acme", template, template.format(color_name=color),
                      material, str(weight), "1.75", spool, "False"))


@pytest.mark.parametrize("label,left,lc,right,rc,material,weight,line,color", [
    ("P004", "{color_name} Flexible", "Black", "TPE {color_name}", "Black Flexible", "TPE", 1000, ("flexible",), ("black",)),
    ("P012", "{color_name} Flexible", "Black", "TPE {color_name}", "Black Flexible", "TPE", 500, ("flexible",), ("black",)),
    ("P009", "{color_name} Glitter", "Texas Tea Black with Gold", "PLA {color_name}", "Texas Tea Black with Gold Glitter", "PLA", 1000, ("glitter",), ("texas", "tea", "black", "with", "gold")),
    ("P016", "{color_name} Glitter", "Texas Tea Black with Gold", "PLA {color_name}", "Texas Tea Black with Gold Glitter", "PLA", 500, ("glitter",), ("texas", "tea", "black", "with", "gold")),
    *[(f"D03{i}", "Galaxy PETG {color_name}", color, "{color_name}", "Galaxy " + color, "PETG", 1000, ("galaxy",), tuple(color.lower().split())) for i, color in enumerate(("Black", "Green", "Red", "Super Blue", "Violet"), 1)],
    ("PM070", "Matte PLA {color_name}", "( Black)", "Acme PLA {color_name}", "Matte Black", "PLA", 1000, ("matte",), ("black",)),
])
def test_named_backlog_qualifiers_are_lossless(label, left, lc, right, rc, material, weight, line, color):
    a, b = key(left, lc, material, weight=weight), key(right, rc, material, weight=weight)
    bindings = catalog.line_color_bindings(a, lc, b, rc)
    ai, bi = catalog.identity_from_key(a, bindings[0]), catalog.identity_from_key(b, bindings[1])
    assert ai == bi
    assert ai["line"] == line
    assert ai["color"] == color


@pytest.mark.parametrize("left,lc,right,rc,spool", [
    ("Silk PLA {color_name}", "Gold", "PLA {color_name}", "Gold", "plastic"),
    ("PLA {color_name}", "Silk Gold", "PLA {color_name}", "Gold", "plastic"),
    ("Silk PLA {color_name}", "Gold", "PLA {color_name}", "Silk White", "plastic"),
    ("Silk PLA {color_name}", "Gold", "PLA {color_name}", "Silk Extra Gold", "plastic"),
    ("Silk PLA {color_name}", "Gold Blue", "PLA {color_name}", "Silk Blue Gold", "plastic"),
    ("Silk PLA 2.0 {color_name}", "Gold", "PLA {color_name}", "Silk 2.0 Gold", "plastic"),
    ("Silk PLA {color_name}", "Gold", "PLA {color_name}", "Silk Gold", "cardboard"),
    ("HF PLA {color_name}", "Gold", "PLA {color_name}", "HF Gold", "plastic"),
])
def test_different_or_unanchored_identity_is_rejected(left, lc, right, rc, spool):
    with pytest.raises(ValueError):
        catalog.line_color_bindings(key(left, lc), lc, key(right, rc, spool=spool), rc)


def test_real_silk_gold_requires_counterpart_template_anchor():
    a, b = key("Silk PLA {color_name}", "Gold"), key("PLA {color_name}", "Silk Gold")
    bindings = catalog.line_color_bindings(a, "Gold", b, "Silk Gold")
    assert catalog.identity_from_key(a, bindings[0]) == catalog.identity_from_key(b, bindings[1])
    bindings[1]["anchor_key"] = key("PLA {color_name}", "Silk Gold")
    with pytest.raises(ValueError):
        catalog.identity_from_key(b, bindings[1])


def test_registry_rejects_fabricated_template_anchor():
    from scripts.retired_ids import check_registry
    a, b = key("Silk PLA {color_name}", "Gold"), key("PLA {color_name}", "Silk Gold")
    bindings = catalog.line_color_bindings(a, "Gold", b, "Silk Gold")
    fake = key("Acme Silk PLA {color_name}", "Gold")
    bindings[1]["anchor_key"] = fake
    payload = {"version": 1, "retired": {"old": {"replaced_by": "keep", "reason": "duplicate", "ref": "review", "source": "a" * 40, "retired_key": b}}}
    errors, _, _ = check_registry(payload, {"version": 1, "retired": {}}, {a: "keep", b: "old"}, {a: "keep"}, {a: "keep"}, {"old": bindings[1], "keep": bindings[0]})
    assert any("anchor" in error for error in errors)


def test_numeric_weight_representation_is_not_a_different_package():
    a, b = key("Matte PLA {color_name}", "Black"), key("PLA {color_name}", "Matte Black", weight=1000.0)
    bindings = catalog.line_color_bindings(a, "Black", b, "Matte Black")
    assert catalog.identity_from_key(a, bindings[0]) == catalog.identity_from_key(b, bindings[1])


@pytest.mark.parametrize("anchor", [[], {}, None, 42, ""])
def test_malformed_registry_anchor_returns_validation_error(anchor):
    from scripts.retired_ids import check_registry
    empty = {"version": 1, "retired": {}}
    errors, _, _ = check_registry(empty, empty, {}, {}, {}, {"bad": {"parts": [], "anchor_key": anchor}})
    assert errors
