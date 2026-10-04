"""Read-only duplicate proposals; only a later owner review authorizes apply."""

import argparse
from collections import Counter, defaultdict
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


def official_line_tokens(name, manufacturer, material):
    """Compare product names without deleting the material or its position."""
    if material == "PETG":
        name = re.sub(r"\bPET[\s-]+G\b", "PETG", name, flags=re.IGNORECASE)
    return normalize_name(name, manufacturer)


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
    family_axes = defaultdict(lambda: {axis: set() for axis in ("weight", "diameter", "color")})
    for row in records:
        for axis in ("weight", "diameter", "color"):
            family_axes[(row["filename"], row["definition_index"])][axis].add(row[axis + "_index"])
    shapes = {key: {"source_file": key[0], "definition_index": key[1],
                   **{axis + "s": len(values) for axis, values in axes.items()},
                   "compiled_records": family_counts[key]} for key, axes in family_axes.items()}
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
                official_match = official_line_tokens(row["line"], rec["manufacturer"], rec["material"]) == official_line_tokens(official["name"], rec["manufacturer"], rec["material"])
            proposals.append(((int(upstream and not exception), int(not has_prefix), int(official_match), family_counts[(row["filename"], row["definition_index"])]), row))
        # Evaluate the priority rules explicitly. Name evidence (R3) cannot be
        # outweighed by a larger weight x diameter x color expansion (R4).
        contenders, deciding_rule = proposals, None
        for index in range(4):
            best = max(score[index] for score, _ in contenders)
            narrowed = [(score, row) for score, row in contenders if score[index] == best]
            if len(narrowed) < len(contenders):
                deciding_rule = index + 1
            contenders = narrowed
            if len(contenders) == 1:
                break
        winners = [row for _, row in contenders]
        survivor = winners[0]["record"]["id"] if len(winners) == 1 else None
        cartesian_warning = None
        if survivor and deciding_rule == 4:
            shape = shapes[(winners[0]["filename"], winners[0]["definition_index"])]
            if sum(shape[axis] > 1 for axis in ("weights", "diameters", "colors")) >= 2:
                cartesian_warning = {"message": "Rule 4 count is a Cartesian expansion, not verified sales coverage; owner review required.",
                                     "definitions": [shape]}
        conflicts = {}
        for field in rows[0]["record"]:
            if field not in ("id", "name") and any(row["record"][field] != rows[0]["record"][field] for row in rows[1:]):
                conflicts[field] = {row["record"]["id"]: row["record"][field] for row in rows}
        groups.append({"group_id": gid, "ids": [row["record"]["id"] for row in rows], "proposed_survivor": survivor,
                       "survivor_rule": deciding_rule if survivor else None, "rule4_cartesian_warning": cartesian_warning,
                       "proposed_retirements": {row["record"]["id"]: survivor for row in rows if survivor and row["record"]["id"] != survivor},
                       "records": [{**row["record"], "key": row["key"], "template": row["template"], "source_color": row["color"], "source_line": row["line"], "source_file": row["filename"], "source_definition": shapes[(row["filename"], row["definition_index"])], "upstream": (row["record"]["manufacturer"], row["template"]) in upstream_families} for row in rows],
                       "metadata_conflicts": conflicts, "evidence": [], "approved": False,
                       "notes": "Candidate only; owner must confirm physical identity. Keep survivor metadata unless newer-lot evidence is supplied."})
    return {"version": 1, "brand": brand, "digest": catalog_digest(root), "upstream_sha": upstream_sha,
            "upstream_status": "PINNED" if upstream_sha else "NOT_PROVIDED", "groups": groups,
            "official_name_evidence": official_names, "upstream_exceptions": upstream_exceptions}


def audit_all(root):
    from scripts.duplicate_guard import duplicate_review_state
    rows = catalog_records(root)
    current, confirmed, pending = duplicate_review_state(root, rows)
    groups = []
    for gid, members in sorted(current.items()):
        status = "NOT_DUPLICATE" if gid in confirmed else "OWNER_PENDING" if gid in pending else "UNRESOLVED"
        groups.append({"group_id": gid, "status": status,
                       "ids": sorted(row["record"]["id"] for row in members),
                       "sources": sorted({row["filename"] for row in members})})
    summary = {"sources": len(list((Path(root) / "filaments").glob("*.json"))), "records": len(rows),
               "candidates": len(groups), "not_duplicates": sum(g["status"] == "NOT_DUPLICATE" for g in groups),
               "owner_pending": sum(g["status"] == "OWNER_PENDING" for g in groups),
               "unresolved": sum(g["status"] == "UNRESOLVED" for g in groups)}
    return {"version": 1, "scope": "ENTIRE catalog", "digest": catalog_digest(root), "summary": summary, "groups": groups}


def markdown_report(report):
    if "summary" in report:
        return "# Entire-catalog duplicate audit\n\n```json\n" + json.dumps(report["summary"], indent=2) + "\n```\n\n" + "\n".join(f'- {g["group_id"]}: {g["status"]} — ' + ", ".join(g["ids"]) for g in report["groups"]) + "\n"
    lines = [f"# Duplicate audit: {report['brand']}", "", "Unconfirmed candidates — no retirement authorization.",
             f"Upstream: {report['upstream_sha'] or 'not provided; upstream preference unresolved'}", f"Snapshot: {report['digest']}", ""]
    for group in report["groups"]:
        lines += [f"## {group['group_id']}", "", f"Proposed survivor: {group['proposed_survivor'] or 'OWNER SELECTION REQUIRED'}", ""]
        lines += [f"Deciding survivor rule: {group['survivor_rule'] or 'tie; owner selection required'}", ""]
        if group["rule4_cartesian_warning"]:
            lines += ["WARNING: " + group["rule4_cartesian_warning"]["message"],
                      "```json", json.dumps(group["rule4_cartesian_warning"]["definitions"], indent=2), "```", ""]
        lines += [f"- `{record['id']}` — {record['name']} / {record['weight']} g / {record['diameter']} mm / {record['spool_type']} / refill={record['is_refill']} / upstream={record['upstream']}" for record in group["records"]]
        lines += ["", "Proposed retirements: `" + json.dumps(group["proposed_retirements"], ensure_ascii=False) + "`", "",
                  "Metadata conflicts (older values/evidence retained here; unresolved by default):", "```json", json.dumps(group["metadata_conflicts"], ensure_ascii=False, indent=2), "```", "", group["notes"], ""]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument("--brand")
    scope.add_argument("--all", action="store_true", help="Scan every source; nonzero exit for unresolved candidates outside exact review exemptions")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--upstream-ref", help="Already fetched read-only upstream ref; resolved to a commit")
    parser.add_argument("--evidence", type=Path, help="Reviewed official_names/upstream_exceptions JSON")
    parser.add_argument("--output", type=Path, help="Report directory outside filaments/contracts; stdout JSON otherwise")
    args = parser.parse_args()
    try:
        evidence = json.loads(args.evidence.read_text(encoding="utf-8")) if args.evidence else {}
        if args.all and (args.evidence or args.upstream_ref):
            raise ValueError("--all classifies current memberships; use --brand for survivor/name evidence")
        report = audit_all(args.root) if args.all else audit_brand(args.root, args.brand, args.upstream_ref, **evidence)
        if args.output:
            output = args.output.resolve()
            if any(output.is_relative_to((args.root / directory).resolve()) for directory in ("filaments", "contracts")):
                raise ValueError("reports cannot overwrite catalog sources/contracts")
            output.mkdir(parents=True, exist_ok=True)
            for suffix, content in (("json", json.dumps(report, indent=2, ensure_ascii=False) + "\n"), ("md", markdown_report(report))):
                path = output / f"{'all' if args.all else args.brand}.{suffix}"
                if path.exists():
                    raise ValueError(f"report already exists: {path}")
                path.write_text(content, encoding="utf-8")
        else:
            print(json.dumps(report, indent=2, ensure_ascii=False))
        if args.all and report["summary"]["unresolved"]:
            parser.exit(1)
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")


if __name__ == "__main__":
    main()
