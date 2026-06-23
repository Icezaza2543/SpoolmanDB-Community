#!/usr/bin/env python3
"""Compare 3DFP brand list against SpoolmanDB using brand_aliases.json."""
from __future__ import annotations

import json
from pathlib import Path

from scripts.brand_aliases import all_merge_entries, load_merges, repo_slugs, resolve_slug

ROOT = Path(__file__).parent.parent
LOGO_FILE = ROOT / "_3dfp_logos.json"
RESULT_FILE = ROOT / "_3dfp_compare_result.json"


def main() -> int:
    logos = json.loads(LOGO_FILE.read_text(encoding="utf-8"))["logos"]
    repo = repo_slugs()
    merges = load_merges()
    repo_keys = sorted(set(repo.values()))

    matched: list[tuple[str, str]] = []
    missing: list[str] = []

    for slug in sorted(logos):
        hit = resolve_slug(slug, repo=repo, merges=merges)
        if hit:
            matched.append((slug, hit))
        else:
            missing.append(slug)

    print(f"3DFP brands: {len(logos)}")
    print(f"DB manufacturers: {len(repo_keys)}")
    print(f"Matched (exact + alias): {len(matched)}")
    print(f"Truly missing: {len(missing)}")
    print(f"Alias map entries: {len(merges)}")
    print(f"Documented merges (external != db): {len(all_merge_entries())}")

    if missing:
        print("\n=== TRULY MISSING ===")
        for slug in missing:
            print(slug)

    result = {
        "summary": {
            "3dfp_total": len(logos),
            "db_total": len(repo_keys),
            "matched": len(matched),
            "missing": len(missing),
            "alias_entries": len(merges),
        },
        "missing": missing,
        "matched_aliases": [
            {"3dfp": external, "db": db}
            for external, db in matched
            if external != db
        ],
    }
    RESULT_FILE.write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())