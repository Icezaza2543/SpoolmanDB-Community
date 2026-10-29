"""Read-only field-level upstream audit. Candidates never authorize data edits."""

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from scripts.compile_filaments import get_filaments_from_data
from scripts.duplicate_catalog import normalize_name


def candidate_key(record):
    # Ignore packaging here deliberately: an unknown spool is not a new product.
    return (record["manufacturer"].casefold(), record["material"].casefold(),
            normalize_name(record["name"], record["manufacturer"], record["material"]),
            record["weight"], record["diameter"])


def compare_records(upstream, community):
    by_id = {r["id"]: r for r in community}
    candidates = defaultdict(list)
    for record in community:
        candidates[candidate_key(record)].append(record)
    matched = set()
    rows = []
    for record in upstream:
        exact = by_id.get(record["id"])
        matches = [exact] if exact else candidates[candidate_key(record)]
        row = {"upstream_id": record["id"], "manufacturer": record["manufacturer"],
               "community_ids": [r["id"] for r in matches]}
        matched.update(row["community_ids"])
        if exact is not None:
            differences = {k: {"upstream": v, "community": exact.get(k)}
                           for k, v in record.items() if v is not None and v != exact.get(k)}
            row.update(category="conflicting_definitions" if differences else "existing_identical",
                       differences=differences,
                       community_extensions={k: v for k, v in exact.items()
                                             if record.get(k) is None and v is not None},
                       action="defer" if differences else "retain")
        elif matches:
            row.update(category="duplicate_candidates", action="defer",
                       differences={r["id"]: {k: {"upstream": v, "community": r.get(k)}
                                              for k, v in record.items() if v != r.get(k)}
                                    for r in matches})
        else:
            row.update(category="new_upstream_records", action="review_evidence")
        rows.append(row)
    rows.extend({"category": "community_only_records", "manufacturer": r["manufacturer"],
                 "community_ids": [r["id"]], "action": "retain"}
                for r in community if r["id"] not in matched)
    return rows


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True, encoding="utf-8")


def read_sources(ref):
    sha = git("rev-parse", "--verify", f"{ref}^{{commit}}").strip()
    paths = git("ls-tree", "-r", "--name-only", sha, "--", "filaments").splitlines()
    sources = {p: json.loads(git("show", f"{sha}:{p}")) for p in paths
               if p.endswith(".json") and Path(p).parent.as_posix() == "filaments"}
    return sha, sources


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upstream-ref", required=True)
    parser.add_argument("--community-ref", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    upstream_sha, upstream = read_sources(args.upstream_ref)
    community_sha, community = read_sources(args.community_ref)
    def expand(sources):
        return [record for data in sources.values() for record in get_filaments_from_data(data)]
    rows = compare_records(expand(upstream), expand(community))
    summary = {"upstream_commit": upstream_sha, "community_commit": community_sha,
               "method": "Exact IDs first, then ordered normalized names/material/mass/diameter; packaging ignored only for candidate detection. No fuzzy match is proof of identity. No writes to source data.",
               "counts": dict(Counter(r["category"] for r in rows)),
               "manufacturers": {}}
    for manufacturer in sorted({r["manufacturer"] for r in rows}):
        summary["manufacturers"][manufacturer] = dict(Counter(
            r["category"] for r in rows if r["manufacturer"] == manufacturer))
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    with (args.output / "records.jsonl").open("w", encoding="utf-8") as output:
        for row in rows:
            output.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(json.dumps(summary["counts"], indent=2))


if __name__ == "__main__":
    main()
