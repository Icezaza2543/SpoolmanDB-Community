from scripts.reconcile_upstream import compare_records


def row(id, name="Basic Black", **fields):
    return dict(id=id, manufacturer="Example", material="PLA", name=name,
                weight=1000, diameter=1.75, spool_type=None, **fields)


def test_differences_preserve_extensions_and_never_authorize_overwrite():
    result = compare_records([row("a", density=1.2)],
                             [row("a", density=1.3, sds_url="https://example.com/sds")])
    assert result[0]["category"] == "conflicting_definitions"
    assert result[0]["differences"] == {"density": {"upstream": 1.2, "community": 1.3}}
    assert result[0]["community_extensions"] == {"sds_url": "https://example.com/sds"}
    assert result[0]["action"] == "defer"


def test_renames_and_packaging_differences_are_candidates_not_new_records():
    result = compare_records([row("new")], [row("old", name="PLA Basic Black")])
    assert result[0]["category"] == "duplicate_candidates"
    assert result[0]["community_ids"] == ["old"]


def test_categories_include_identical_new_and_community_only():
    result = compare_records([row("a"), row("b", name="White")],
                             [row("a"), row("c", name="Red")])
    assert [r["category"] for r in result] == [
        "existing_identical", "new_upstream_records", "community_only_records"]
    assert result[1]["action"] == "review_evidence"
