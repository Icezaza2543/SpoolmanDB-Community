"""Resolve external manufacturer slugs to SpoolmanDB filament file slugs."""
from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).parent.parent
ALIAS_FILE = Path(__file__).parent / "brand_aliases.json"


def norm_slug(slug: str) -> str:
    return re.sub(r"[^a-z0-9]", "", slug.lower())


@lru_cache(maxsize=1)
def load_alias_data() -> dict:
    with ALIAS_FILE.open(encoding="utf-8") as f:
        return json.load(f)


def load_merges() -> dict[str, str]:
    return load_alias_data().get("merges", {})


def load_sub_brands() -> dict[str, dict]:
    return load_alias_data().get("sub_brands", {})


def load_rejected_pairs() -> set[tuple[str, str]]:
    pairs: set[tuple[str, str]] = set()
    for item in load_alias_data().get("rejected", []):
        pairs.add((item["external"], item["db"]))
    # Legacy key support
    for pair in load_alias_data().get("rejected_fuzzy", []):
        pairs.add((pair[0], pair[1]))
    return pairs


def repo_slugs(filaments_dir: Path | None = None) -> dict[str, str]:
    """Map normalized slug -> canonical filaments/*.json stem."""
    base = filaments_dir or (ROOT / "filaments")
    out: dict[str, str] = {}
    for path in base.glob("*.json"):
        slug = path.stem.lower()
        out[slug] = slug
        out[norm_slug(slug)] = slug
    return out


def resolve_slug(
    external_slug: str,
    repo: dict[str, str] | None = None,
    merges: dict[str, str] | None = None,
) -> str | None:
    """Return SpoolmanDB slug if external slug is known, else None."""
    external_slug = external_slug.lower()
    repo = repo or repo_slugs()
    merges = merges or load_merges()

    if external_slug in repo:
        return external_slug

    if external_slug in merges:
        target = merges[external_slug]
        if target in repo or norm_slug(target) in repo:
            return target if target in repo else repo[norm_slug(target)]

    normalized = norm_slug(external_slug)
    if normalized in repo:
        return repo[normalized]

    return None


def is_rejected_pair(external_slug: str, db_slug: str) -> bool:
    return (external_slug.lower(), db_slug.lower()) in load_rejected_pairs()


def all_merge_entries() -> list[dict[str, str]]:
    merges = load_merges()
    return [
        {"external": external, "db": db}
        for external, db in sorted(merges.items())
        if external != db
    ]