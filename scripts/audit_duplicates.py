"""Read-only duplicate proposals; only a later owner review authorizes apply."""

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.duplicate_catalog import (candidate_groups, catalog_digest, catalog_records,
                                       confirmed_nonduplicates, git_output, normalize_name)
from scripts.retired_ids import load_contract


def brand_filename(brand):
    if not re.fullmatch(r"[\w-]+", brand) or brand in (".", ".."):
        raise ValueError("brand must be a source filename slug, not a path")
    return brand + ".json"


def audit_brand(root, brand, upstream_ref=None, official_names=None, upstream_exceptions=None):
    filename = brand_filename(brand)
    all_records = catalog_records(root)
    records = [row for row in all_records if row["filename"] == filename]
    if not records:
        raise ValueError(f"brand source not found: {filename}")
    confirmed = confirmed_nonduplicates(load_contract(None, root, "not_duplicates.json", "groups"))
    upstream_sha, upstream_families = None, set()
    if upstream_ref:
        upstream_sha = git_output(root, "rev-parse", "--verify", f"{upstream_ref}^{{commit}}").strip()
        upstream_families = {(row["record"]["manufacturer"], row["template"]) for row in catalog_records(root, upstream_sha)}
    family_counts = Counter((row["filename"], row["definition_index"]) for row in records)
    groups = []
    official_names, upstream_exceptions = official_names or {}, upstream_exceptions or {}
    for gid, rows in sorted(candidate_groups(records).items()):
        if gid in confirmed:
            continue
        proposals = []
        for row in rows:
            rec = row["record"]
            upstream = (rec["manufacturer"], row["template"]) in upstream_families
            exception = upstream_exceptions.get(row["template"])
            if exception:
                from scripts.retired_ids import valid_source
                if not valid_source(exception.get("source")) or not exception.get("reason"):
                    raise ValueError("upstream-name exception requires manufacturer evidence and reason")
            has_prefix = row["template"].casefold().startswith(rec["manufacturer"].casefold() + " ")
            official = official_names.get(row["template"])
            official_match = False
            if official:
                from scripts.retired_ids import valid_source
                if not isinstance(official, dict) or not valid_source(official.get("source")) or not isinstance(official.get("name"), str):
                    raise ValueError("official name comparison requires manufacturer source")
                official_match = normalize_name(row["line"], rec["manufacturer"], rec["material"]) == normalize_name(official["name"], rec["manufacturer"], rec["material"])
            proposals.append(((int(upstream and not exception), int(not has_prefix), int(official_match), family_counts[(row["filename"], row["definition_index"])]), row))
        best = max(score for score, _ in proposals)
        winners = [row for score, row in proposals if score == best]
        survivor = winners[0]["record"]["id"] if len(winners) == 1 else None
        conflicts = {}
        for field in rows[0]["record"]:
            if field not in ("id", "name") and any(row["record"][field] != rows[0]["record"][field] for row in rows[1:]):
                conflicts[field] = {row["record"]["id"]: row["record"][field] for row in rows}
        groups.append({"group_id": gid, "ids": [row["record"]["id"] for row in rows], "proposed_survivor": survivor,
                       "proposed_retirements": {row["record"]["id"]: survivor for row in rows if survivor and row["record"]["id"] != survivor},
                       "records": [{**row["record"], "key": row["key"], "template": row["template"], "source_color": row["color"], "source_line": row["line"], "source_file": row["filename"], "upstream": (row["record"]["manufacturer"], row["template"]) in upstream_families} for row in rows],
                       "metadata_conflicts": conflicts, "evidence": [], "approved": False,
                       "notes": "Candidate only; owner must confirm physical identity. Keep survivor metadata unless newer-lot evidence is supplied."})
    return {"version": 1, "brand": brand, "digest": catalog_digest(root), "upstream_sha": upstream_sha,
            "upstream_status": "PINNED" if upstream_sha else "NOT_PROVIDED", "groups": groups,
            "official_name_evidence": official_names, "upstream_exceptions": upstream_exceptions}


def markdown_report(report):
    lines = [f"# Duplicate audit: {report['brand']}", "", "Unconfirmed candidates — no retirement authorization.",
             f"Upstream: {report['upstream_sha'] or 'not provided; upstream preference unresolved'}", f"Snapshot: {report['digest']}", ""]
    for group in report["groups"]:
        lines += [f"## {group['group_id']}", "", f"Proposed survivor: {group['proposed_survivor'] or 'OWNER SELECTION REQUIRED'}", ""]
        lines += [f"- `{record['id']}` — {record['name']} / {record['weight']} g / {record['diameter']} mm / {record['spool_type']} / refill={record['is_refill']} / upstream={record['upstream']}" for record in group["records"]]
        lines += ["", "Proposed retirements: `" + json.dumps(group["proposed_retirements"], ensure_ascii=False) + "`", "",
                  "Metadata conflicts (older values/evidence retained here; unresolved by default):", "```json", json.dumps(group["metadata_conflicts"], ensure_ascii=False, indent=2), "```", "", group["notes"], ""]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--brand", required=True)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--upstream-ref", help="Already fetched read-only upstream ref; resolved to a commit")
    parser.add_argument("--evidence", type=Path, help="Reviewed official_names/upstream_exceptions JSON")
    parser.add_argument("--output", type=Path, help="Report directory outside filaments/contracts; stdout JSON otherwise")
    args = parser.parse_args()
    try:
        evidence = json.loads(args.evidence.read_text(encoding="utf-8")) if args.evidence else {}
        report = audit_brand(args.root, args.brand, args.upstream_ref, **evidence)
        if args.output:
            output = args.output.resolve()
            if any(output.is_relative_to((args.root / directory).resolve()) for directory in ("filaments", "contracts")):
                raise ValueError("reports cannot overwrite catalog sources/contracts")
            output.mkdir(parents=True, exist_ok=True)
            for suffix, content in (("json", json.dumps(report, indent=2, ensure_ascii=False) + "\n"), ("md", markdown_report(report))):
                path = output / f"{args.brand}.{suffix}"
                if path.exists():
                    raise ValueError(f"report already exists: {path}")
                path.write_text(content, encoding="utf-8")
        else:
            print(json.dumps(report, indent=2, ensure_ascii=False))
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")


if __name__ == "__main__":
    main()
