"""Unit tests to validate upstream compatibility tracker and documentation integrity."""

import json
from pathlib import Path
import pytest

ROOT = Path(__file__).parent.parent
TRACKER_PATH = ROOT / "contracts" / "upstream_status.json"
UPSTREAM_CONFIG_PATH = ROOT / "contracts" / "spoolman_upstream.json"
DOCS_PATH = ROOT / "docs" / "UPSTREAM_COMPATIBILITY.md"

ALLOWED_STATUS_ENUMS = {"supported", "upstream-pending", "community-extension", "hold"}
ALLOWED_REPO_STATUS_ENUMS = {"active_upstream", "inactive_upstream"}
REQUIRED_CAPABILITIES = {
    "spool_type",
    "refill_is_refill",
    "country_of_origin",
    "sds_tds_urls",
    "codes",
    "eans_gtin",
    "legacy_public_id_compat",
}


def test_upstream_status_json_exists_and_valid():
    """1. Verify upstream_status.json exists and parses as valid JSON."""
    assert TRACKER_PATH.exists(), f"Tracker file missing at {TRACKER_PATH}"
    with TRACKER_PATH.open(encoding="utf-8") as f:
        data = json.load(f)

    assert data.get("schema_version") == 1
    assert "last_reviewed" in data
    assert "upstreams" in data
    assert "capabilities" in data


def test_upstream_config_reference():
    """2. Verify tracker correctly references spoolman_upstream.json without duplicating the stable pin."""
    with TRACKER_PATH.open(encoding="utf-8") as f:
        tracker = json.load(f)

    spoolman_meta = tracker["upstreams"]["spoolman"]
    assert spoolman_meta["status"] in ALLOWED_REPO_STATUS_ENUMS
    config_ref_path = ROOT / spoolman_meta["config_ref"]
    assert config_ref_path.exists(), f"Referenced config file missing: {config_ref_path}"

    with config_ref_path.open(encoding="utf-8") as f:
        upstream_config = json.load(f)

    assert "stable" in upstream_config
    assert "version" in upstream_config["stable"]
    assert "commit" in upstream_config["stable"]


def test_active_vs_inactive_upstreams_distinction():
    """3. Verify distinct labeling of active Spoolman server vs inactive SpoolmanDB data repo."""
    with TRACKER_PATH.open(encoding="utf-8") as f:
        tracker = json.load(f)

    upstreams = tracker["upstreams"]
    assert upstreams["spoolman"]["status"] == "active_upstream"
    assert upstreams["spoolmandb_upstream"]["status"] == "inactive_upstream"


def test_capabilities_schema_and_enums():
    """4. Verify all required capability matrix entries exist and use allowed status enums."""
    with TRACKER_PATH.open(encoding="utf-8") as f:
        tracker = json.load(f)

    caps = tracker["capabilities"]
    assert set(caps.keys()) == REQUIRED_CAPABILITIES

    for cap_name, cap_info in caps.items():
        assert "feature" in cap_info
        assert "status" in cap_info
        assert (
            cap_info["status"] in ALLOWED_STATUS_ENUMS
        ), f"Invalid status enum '{cap_info['status']}' in capability '{cap_name}'"
        assert "spoolman_support" in cap_info
        assert "community_status" in cap_info
        assert "upstream_references" in cap_info
        assert isinstance(cap_info["upstream_references"], list)


def test_documentation_file_exists():
    """5. Verify UPSTREAM_COMPATIBILITY.md exists and contains required sections."""
    assert DOCS_PATH.exists(), f"Documentation file missing at {DOCS_PATH}"
    content = DOCS_PATH.read_text(encoding="utf-8")

    assert "# Upstream Compatibility & Divergence Tracker" in content
    assert "Donkie/Spoolman" in content
    assert "Donkie/SpoolmanDB" in content
    assert "Capability & Divergence Matrix" in content
