"""Unit tests to validate upstream compatibility tracker and documentation integrity."""

from datetime import datetime
import json
from pathlib import Path
import re
import pytest

ROOT = Path(__file__).parent.parent
TRACKER_PATH = ROOT / "contracts" / "upstream_status.json"
UPSTREAM_CONFIG_PATH = ROOT / "contracts" / "spoolman_upstream.json"
EXTERNAL_DB_PATH = ROOT / "contracts" / "spoolman_externaldb.py"
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
REPO_QUALIFIED_REF_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+#\d+$")
HEX_SHA_40_PATTERN = re.compile(r"^[0-9a-f]{40}$")


def test_upstream_status_json_exists_and_valid():
    """1. Verify upstream_status.json exists, parses as valid JSON, and has valid ISO date."""
    assert TRACKER_PATH.exists(), f"Tracker file missing at {TRACKER_PATH}"
    with TRACKER_PATH.open(encoding="utf-8") as f:
        data = json.load(f)

    assert data.get("schema_version") == 1
    assert "last_reviewed" in data
    assert "upstreams" in data
    assert "capabilities" in data

    # Validate ISO date format YYYY-MM-DD
    date_str = data["last_reviewed"]
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        pytest.fail(f"last_reviewed date '{date_str}' is not a valid YYYY-MM-DD ISO date")


def test_upstream_config_reference_no_duplication():
    """2. Verify tracker references spoolman_upstream.json without duplicating stable pin version/SHA."""
    with TRACKER_PATH.open(encoding="utf-8") as f:
        tracker = json.load(f)

    spoolman_meta = tracker["upstreams"]["spoolman"]
    assert spoolman_meta["status"] in ALLOWED_REPO_STATUS_ENUMS
    assert "config_ref" in spoolman_meta

    # Must NOT duplicate stable version or commit in tracker
    assert "stable_version" not in spoolman_meta, "Tracker duplicates stable_version from config"
    assert "stable_commit" not in spoolman_meta, "Tracker duplicates stable_commit from config"

    config_ref_path = ROOT / spoolman_meta["config_ref"]
    assert config_ref_path.exists(), f"Referenced config file missing: {config_ref_path}"

    with config_ref_path.open(encoding="utf-8") as f:
        upstream_config = json.load(f)

    assert "stable" in upstream_config
    assert "version" in upstream_config["stable"]
    assert "commit" in upstream_config["stable"]


def test_active_vs_inactive_upstreams_distinction_and_sha_format():
    """3. Verify distinct labeling of active Spoolman vs inactive SpoolmanDB and exact 40-character hex SHA."""
    with TRACKER_PATH.open(encoding="utf-8") as f:
        tracker = json.load(f)

    upstreams = tracker["upstreams"]
    assert upstreams["spoolman"]["status"] == "active_upstream"
    
    spoolmandb = upstreams["spoolmandb_upstream"]
    assert spoolmandb["status"] == "inactive_upstream"
    assert "latest_known_commit" in spoolmandb
    assert "latest_known_commit_date" in spoolmandb

    sha = spoolmandb["latest_known_commit"]
    assert HEX_SHA_40_PATTERN.match(sha), f"SpoolmanDB commit SHA '{sha}' is not a valid 40-character hex SHA"

    commit_date = spoolmandb["latest_known_commit_date"]
    try:
        datetime.strptime(commit_date, "%Y-%m-%d")
    except ValueError:
        pytest.fail(f"latest_known_commit_date '{commit_date}' is not a valid YYYY-MM-DD ISO date")


def test_capabilities_schema_enums_and_qualified_refs():
    """4. Verify capability matrix entries, status enums, and repository-qualified upstream references."""
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
        
        refs = cap_info["upstream_references"]
        assert isinstance(refs, list)
        for ref in refs:
            assert REPO_QUALIFIED_REF_PATTERN.match(
                ref
            ), f"Upstream reference '{ref}' in capability '{cap_name}' must be repository-qualified (e.g. 'Donkie/SpoolmanDB#282')"


def test_no_false_native_contract_claims():
    """5. Verify no capability claims native Spoolman support for fields absent from ExternalFilament contract."""
    with TRACKER_PATH.open(encoding="utf-8") as f:
        tracker = json.load(f)

    # Load known ExternalFilament fields from contracts/spoolman_externaldb.py
    assert EXTERNAL_DB_PATH.exists()
    db_content = EXTERNAL_DB_PATH.read_text(encoding="utf-8")
    
    # Check that spool_type is the only capability marked as native 'supported'
    caps = tracker["capabilities"]
    for cap_name, cap_info in caps.items():
        if cap_name == "spool_type":
            assert cap_info["status"] == "supported"
        else:
            # Fields absent from ExternalFilament (is_refill, COO, SDS/TDS, codes, EAN/GTIN, legacy IDs) must be community-extension
            assert (
                cap_info["status"] == "community-extension"
            ), f"Capability '{cap_name}' must be 'community-extension' as field is absent from ExternalFilament contract"


def test_documentation_file_integrity_and_relative_links():
    """6. Verify UPSTREAM_COMPATIBILITY.md exists, has required content, and uses relative links (no file://)."""
    assert DOCS_PATH.exists(), f"Documentation file missing at {DOCS_PATH}"
    content = DOCS_PATH.read_text(encoding="utf-8")

    assert "# Upstream Compatibility & Divergence Tracker" in content
    assert "Donkie/Spoolman" in content
    assert "Donkie/SpoolmanDB" in content
    assert "Capability & Divergence Matrix" in content
    assert "compatible with the pinned stable Spoolman contract and monitored against the current master canary." in content
    assert "5b61e755926568ec3b3235701684595872b70b49" in content

    # Disallow file:/// absolute/file links in markdown documentation
    assert "file:///" not in content, "Documentation contains absolute file:/// links; use relative repository links instead"
