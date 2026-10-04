"""Full-catalog duplicate enforcement with exact reviewed exemptions only."""

import csv
from pathlib import Path
import subprocess

from scripts.duplicate_catalog import candidate_groups, catalog_records, confirmed_nonduplicates
from scripts.retired_ids import load_contract

OWNER_SHEET = "docs/audits/backlog-decisions.csv"
OWNER_FIELDS = {"group_id", "brand", "side_a_name", "side_a_id", "side_a_hex",
                "side_b_name", "side_b_id", "side_b_hex", "evidence_url", "reason", "recommendation"}


def duplicate_review_state(root, rows=None, base_ref=None):
    """Validate review contracts and return current exact membership classes."""
    root = Path(root)
    if base_ref:
        subprocess.run(["git", "rev-parse", "--verify", "--end-of-options", f"{base_ref}^{{commit}}"], cwd=root, capture_output=True, check=True)
    current = candidate_groups(catalog_records(root) if rows is None else rows)
    confirmed = confirmed_nonduplicates(load_contract(None, root, "not_duplicates.json", "groups"))
    payload = load_contract(None, root, "owner_pending_duplicates.json", "groups")
    pending = confirmed_nonduplicates(payload)
    if pending & confirmed:
        raise ValueError("owner-pending and not-duplicate memberships overlap")
    if pending - set(current):
        raise ValueError("stale owner-pending membership is not a current candidate")
    if pending:
        sheet = root / OWNER_SHEET
        with sheet.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            headers = reader.fieldnames or []
            if set(headers) != OWNER_FIELDS or len(headers) != len(OWNER_FIELDS):
                raise ValueError("owner sheet requires the complete unique 11-column schema")
            reviewed = {}
            for row in reader:
                if set(row) != OWNER_FIELDS or not all(isinstance(row.get(field), str) for field in OWNER_FIELDS):
                    raise ValueError("owner sheet has incomplete or surplus cells")
                if any(not row[field].strip() for field in OWNER_FIELDS - {"evidence_url"}):
                    raise ValueError("owner sheet lost required review values")
                gid = row["group_id"]
                if not gid or gid in reviewed:
                    raise ValueError("owner sheet has blank/duplicate group")
                ids = [identity for field in ("side_a_id", "side_b_id") for identity in row[field].split(";")]
                if any(not identity for identity in ids) or len(set(ids)) != len(ids):
                    raise ValueError("owner sheet has blank/duplicate member")
                reviewed[gid] = set(ids)
        if set(reviewed) != pending:
            raise ValueError("owner sheet and pending contract groups differ")
        for gid in pending:
            entry = payload["groups"][gid]
            ids = {row["record"]["id"] for row in current[gid]}
            if entry["ref"] != OWNER_SHEET or set(entry["ids"]) != ids or reviewed[gid] != ids:
                raise ValueError(f"owner-pending {gid}: sheet/current membership mismatch")
    return current, confirmed, pending


def check_duplicate_candidates(root, base_ref=None):
    errors = []
    try:
        current, confirmed, pending = duplicate_review_state(root, base_ref=base_ref)
        for gid, rows in sorted(current.items()):
            if gid not in confirmed | pending:
                ids = sorted(row["record"]["id"] for row in rows)
                errors.append(f"Unresolved duplicate candidate {gid}: {', '.join(ids)}; physical identity requires review")
    except (ValueError, OSError, KeyError, TypeError, csv.Error, subprocess.SubprocessError) as exc:
        errors.append(f"Duplicate review guard failed closed: {exc}")
    return errors, []
