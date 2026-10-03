"""Compare candidate memberships with trusted source snapshots, not edited baselines."""

import subprocess

from scripts.duplicate_catalog import candidate_groups, catalog_records, confirmed_nonduplicates
from scripts.retired_ids import load_contract


def check_duplicate_candidates(root, base_ref=None):
    errors, warnings = [], []
    try:
        current = candidate_groups(catalog_records(root))
        confirmed = confirmed_nonduplicates(load_contract(None, root, "not_duplicates.json", "groups"))
        historical = candidate_groups(catalog_records(root, base_ref)) if base_ref else current
        historical_memberships = [set(row["record"]["id"] for row in rows) for rows in historical.values()]
        for gid, rows in sorted(current.items()):
            if gid in confirmed:
                continue
            ids = {row["record"]["id"] for row in rows}
            # Retiring one member does not introduce a new duplicate relationship.
            existing = any(ids <= members for members in historical_memberships)
            message = f"{gid}: {', '.join(sorted(ids))}; candidate only, physical identity requires review"
            if existing:
                warnings.append("Existing duplicate candidate " + message)
            else:
                errors.append("NEW unreviewed duplicate candidate " + message)
    except (ValueError, OSError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        errors.append(f"Duplicate review guard failed closed: {exc}")
    return errors, warnings
