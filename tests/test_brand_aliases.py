import json
from pathlib import Path

import pytest

from scripts.brand_aliases import (
    ALIAS_FILE,
    is_rejected_pair,
    load_merges,
    resolve_slug,
)


@pytest.fixture
def alias_data():
    return json.loads(ALIAS_FILE.read_text(encoding="utf-8"))


def test_alias_file_structure(alias_data):
    assert alias_data["version"] == 1
    assert isinstance(alias_data["merges"], dict)
    assert isinstance(alias_data["sub_brands"], dict)
    assert isinstance(alias_data["rejected"], list)
    assert len(alias_data["merges"]) > 0


def test_user_confirmed_merges():
    merges = load_merges()
    assert merges["yoyi-yoyi"] == "yoyi"
    assert merges["solutech"] == "3dsolutech"
    assert merges["esun-3d"] == "esun"
    assert merges["panchroma"] == "polymaker"
    assert merges["fiberon"] == "polymaker"


def test_user_confirmed_rejections():
    assert is_rejected_pair("fdplast", "3dplast")
    assert is_rejected_pair("colorful", "colorfil")
    assert is_rejected_pair("copper-3d", "r3d")
    assert is_rejected_pair("fiberon", "fiberlogy")
    assert not is_rejected_pair("yoyi-yoyi", "yoyi")


def test_resolve_slug_exact_and_alias():
    repo = {
        "yoyi": "yoyi",
        "esun": "esun",
        "polymaker": "polymaker",
        "3dsolutech": "3dsolutech",
    }
    merges = load_merges()

    assert resolve_slug("yoyi", repo=repo, merges=merges) == "yoyi"
    assert resolve_slug("yoyi-yoyi", repo=repo, merges=merges) == "yoyi"
    assert resolve_slug("esun-3d", repo=repo, merges=merges) == "esun"
    assert resolve_slug("panchroma", repo=repo, merges=merges) == "polymaker"
    assert resolve_slug("fdplast", repo=repo, merges=merges) is None


def test_sub_brands_include_polymaker_lines(alias_data):
    polymaker = alias_data["sub_brands"]["polymaker"]
    assert polymaker["db"] == "polymaker"
    for line in ("polylite", "polymax", "polyflex", "polymide", "polysonic"):
        assert line in polymaker["aliases"]