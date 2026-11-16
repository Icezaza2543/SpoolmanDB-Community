"""Plan or apply a reviewed rename migration for one manufacturer file.

A rename changes a filament group's ``name`` template only. Because the
template is part of ``generate_id``, every compiled variant of a renamed group
gets a new public ID. This tool keeps that auditable: each old ID is retired in
``contracts/retired_ids.json`` with ``reason: "rename"`` and points at its new
ID, then the baseline enrolls the new IDs. ``scripts/retired_ids.py`` verifies
every pair (same file, manufacturer, material, package and color; the product
line may differ only by text repeating the manufacturer or material).

Renames come from ``--rename OLD NEW`` pairs, or from an upstream SpoolmanDB
change with ``--upstream BEFORE AFTER`` (same-material name changes only;
material changes are reported and skipped). Without ``--apply`` nothing is
written.

    python scripts/rename_migration.py --file addnorth.json \\
        --upstream 'donkie/main~1' donkie/main \\
        --ref https://github.com/Donkie/SpoolmanDB/pull/521 --source <SHA or URL>
"""

import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.compile_id_baseline import (  # noqa: E402
    BASELINE_PATH, compile_current_id_manifest, load_baseline_payload, write_baseline_manifest,
)
from scripts.duplicate_catalog import rename_identity  # noqa: E402
from scripts.retired_ids import valid_source  # noqa: E402

REGISTRY_PATH = ROOT / "contracts" / "retired_ids.json"


def upstream_renames(root, filename, before, after):
    """Same-material name changes between two refs, as {(old, material): new}."""
    def load(ref):
        out = subprocess.run(["git", "show", f"{ref}:filaments/{filename}"], cwd=root,
                             capture_output=True, text=True, encoding="utf-8", check=True)
        return json.loads(out.stdout)["filaments"]
    old_groups, new_groups = load(before), load(after)
    if len(old_groups) != len(new_groups):
        raise ValueError(f"upstream {filename}: group count changed ({len(old_groups)} -> "
                         f"{len(new_groups)}); give explicit --rename pairs instead")
    renames, skipped = {}, []
    for old, new in zip(old_groups, new_groups):
        if old["name"] == new["name"]:
            continue
        if old["material"] != new["material"]:
            skipped.append(f"{old['name']!r} [{old['material']}] -> {new['name']!r} [{new['material']}]")
            continue
        key = (old["name"], old["material"])
        if renames.setdefault(key, new["name"]) != new["name"]:
            raise ValueError(f"upstream renames {key} inconsistently")
    return renames, skipped


def rename_source(text, groups_renamed):
    """Rename group templates textually so unrelated formatting is untouched."""
    data = json.loads(text)
    expected = json.loads(text)
    count = 0
    for group in expected["filaments"]:
        new = groups_renamed.get((group["name"], group["material"]))
        if new is not None:
            group["name"] = new
            count += 1
    if not count:
        raise ValueError("no group matched the requested renames")
    result = text
    for (old, _material), new in groups_renamed.items():
        for encode in (lambda s: json.dumps(s, ensure_ascii=False), json.dumps):
            result = result.replace(f'"name": {encode(old)}', f'"name": {json.dumps(new, ensure_ascii=False)}')
    if json.loads(result) != expected:
        # A template shared across materials with only some renamed cannot be
        # edited textually; fall back to a full rewrite only if it is lossless.
        if json.dumps(data, indent=2, ensure_ascii=False) + "\n" != text:
            raise ValueError("cannot apply renames without reformatting the file")
        result = json.dumps(expected, indent=2, ensure_ascii=False) + "\n"
    return result, count


def plan(root, filename, renames, base_manifest):
    """Compile before/after in a scratch copy and pair every removed ID with its new ID."""
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / "filaments"
        shutil.copytree(root / "filaments", work)
        before, errors = compile_current_id_manifest(work)
        if errors:
            raise ValueError("catalog does not compile before renaming:\n" + "\n".join(errors))
        path = work / filename
        new_text, groups = rename_source(path.read_text(encoding="utf-8"), renames)
        path.write_bytes(new_text.encode("utf-8"))
        after, errors = compile_current_id_manifest(work)
        if errors:
            raise ValueError("renamed catalog does not compile (a rename probably collides with "
                             "an existing record; resolve that as a duplicate first):\n" + "\n".join(errors))
    removed = {key: pid for key, pid in before.items() if key not in after}
    added = {key: pid for key, pid in after.items() if key not in before}
    by_identity = {}
    for key, pid in added.items():
        by_identity.setdefault(json.dumps(rename_identity(key), sort_keys=True), []).append((key, pid))
    historical = set(base_manifest.values())
    base_keys = {pid: key for key, pid in base_manifest.items()}
    pairs, problems = [], []
    for key, old_id in sorted(removed.items(), key=lambda kv: kv[1]):
        matches = by_identity.pop(json.dumps(rename_identity(key), sort_keys=True), [])
        if len(matches) != 1:
            problems.append(f"{old_id}: {len(matches)} rename candidates")
            continue
        new_key, new_id = matches[0]
        if new_id == old_id:
            continue  # template text changed but the ID did not (e.g. a non-ASCII symbol)
        if new_id in historical:
            problems.append(f"{old_id}: new ID {new_id} already exists; this is a duplicate merge")
        if old_id not in historical:
            problems.append(f"{old_id}: not in the baseline; enroll it before renaming")
        elif base_keys[old_id] != key:
            problems.append(f"{old_id}: baseline key differs from source key; rekey first")
        pairs.append((old_id, new_id, key, new_key))
    for leftovers in by_identity.values():
        problems.extend(f"{pid}: new ID has no retired predecessor" for _key, pid in leftovers)
    return pairs, groups, new_text, problems


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--file", required=True, help="manufacturer file name in filaments/, e.g. addnorth.json")
    parser.add_argument("--rename", nargs=3, action="append", default=[], metavar=("OLD", "NEW", "MATERIAL"),
                        help="rename group template OLD to NEW for groups of MATERIAL (repeatable)")
    parser.add_argument("--upstream", nargs=2, metavar=("BEFORE", "AFTER"),
                        help="take same-material renames from an upstream change of the same file")
    parser.add_argument("--ref", required=True, help="review reference (upstream PR URL, issue, audit)")
    parser.add_argument("--source", required=True, help="evidence: commit SHA or URL")
    parser.add_argument("--base-ref", default="HEAD", help="trusted baseline commit (default HEAD)")
    parser.add_argument("--apply", action="store_true", help="write source, registry and baseline")
    args = parser.parse_args(argv)

    if not valid_source(args.source):
        parser.error("--source must be a 40-character commit SHA or an http(s) URL")
    renames = {(old, material): new for old, new, material in args.rename}
    if args.upstream:
        found, skipped = upstream_renames(ROOT, args.file, *args.upstream)
        for item in skipped:
            print(f"SKIP (material change, not a rename): {item}")
        for key, new in found.items():
            if renames.setdefault(key, new) != new:
                parser.error(f"conflicting renames for {key}")
    if not renames:
        parser.error("no renames given")
    base, errors = load_baseline_payload(args.base_ref, ROOT)
    if errors:
        parser.error("; ".join(errors))

    pairs, groups, new_text, problems = plan(ROOT, args.file, renames, base["manifest"])
    for (old, material), new in sorted(renames.items()):
        print(f"RENAME [{material}] {old!r} -> {new!r}")
    print(f"{groups} group(s) renamed, {len(pairs)} public ID(s) retired as renames")
    for old_id, new_id, _old_key, _new_key in pairs:
        print(f"  {old_id} -> {new_id}")
    if problems:
        print("\nERROR: rename migration is not safe:", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1
    if not args.apply:
        print("\nDry run only; re-run with --apply to write changes.")
        return 0

    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    for old_id, new_id, old_key, _new_key in pairs:
        if old_id in registry["retired"]:
            print(f"ERROR: {old_id} is already retired", file=sys.stderr)
            return 1
        registry["retired"][old_id] = {"replaced_by": new_id, "reason": "rename", "ref": args.ref,
                                       "source": args.source, "retired_key": old_key}
    (ROOT / "filaments" / args.file).write_bytes(new_text.encode("utf-8"))
    REGISTRY_PATH.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_baseline_manifest(baseline_path=BASELINE_PATH, base_baseline_path=args.base_ref)
    print(f"Applied: {args.file}, contracts/retired_ids.json, contracts/compiled_id_baseline.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
