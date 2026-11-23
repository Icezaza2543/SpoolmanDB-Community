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
material changes are reported and skipped). Upstream renames of groups that do
not exist in this file are reported and skipped; an explicit ``--rename`` of a
missing group is an error. Without ``--apply`` nothing is written.

``--reclassify OLD NEW OLD_MATERIAL NEW_MATERIAL`` moves a group to a more
specific material code (``TPU`` -> ``TPU-85A``, ``CF`` -> ``PA-CF``) and may drop
the name text the new code carries. Its IDs are retired with ``reason:
"reclassification"``. The new code must keep every part of the old one and add
detail (``scripts/duplicate_catalog.py::refines_material``). Reclassifications are
never taken from ``--upstream`` automatically: each needs product-specific
evidence for the added detail, so they are listed one by one; ``--keep`` leaves
unverified colours on their current material and ID.

``--keep TEMPLATE COLOR`` leaves one color of a renamed group on its current
ID, e.g. when upstream also changed that color's name and renaming it now would
publish an intermediate ID. A group whose colors are all kept is not renamed;
otherwise the kept colors move into a copy of the group under the old template,
placed directly after it, so their compiled records do not change.

An existing retirement that points at a renamed ID (A -> B, then B -> C) is
re-pointed to the final ID (A -> C) and keeps its original evidence, so the
registry never forms a chain. The complete result (source, registry and
baseline) is built and validated in a scratch copy first: the trusted baseline
and registry checks plus ``verify_rename_scope`` against ``--base-ref``. The
checkout must be clean under filaments/, contracts/ and docs/audits/, and any
change between ``--base-ref`` and the result other than the rename fails. Files are written only when
all of that passes, so the dry run and ``--apply`` fail on exactly the same
problems and a failed apply leaves the tree untouched.

``--verify`` runs the same rename-only scope check on an existing change
(working tree against ``--base-ref``), e.g. when reviewing a rename PR. CI runs
it with ``--if-renames`` on every change that adds a rename or reclassification
retirement. Only a reclassified record may change ``material``.

Groups whose colors have a ``display_name`` override are refused: a migration
never edits ``display_name``, and a baseline key change is never part of one.

    python scripts/rename_migration.py --file addnorth.json \\
        --upstream 'donkie/main~1' donkie/main \\
        --ref https://github.com/Donkie/SpoolmanDB/pull/521 --source <SHA or URL>
"""

import argparse
from collections import Counter
import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.compile_id_baseline import (  # noqa: E402
    BASELINE_PATH, check_baseline_manifest_detailed, compile_current_id_manifest, load_baseline_payload,
)
from scripts.duplicate_catalog import (  # noqa: E402
    catalog_records, reclassification_identity, refines_material, rename_identity,
)
from scripts.retired_ids import MIGRATION_REASONS, load_contract, valid_source  # noqa: E402

REGISTRY_PATH = ROOT / "contracts" / "retired_ids.json"
# The only compiled fields a rename may change; a reclassification may also change the material.
RENAME_FIELDS = {"id", "name"}
RECLASSIFICATION_FIELDS = RENAME_FIELDS | {"material"}
# Copied into the scratch tree: everything the baseline/registry checks read.
STAGED_DIRS = ("filaments", "contracts", "docs/audits")


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


def unmatched_renames(text, groups_renamed):
    """Requested (template, material) renames that no group in the source uses."""
    present = {(group["name"], group["material"]) for group in json.loads(text)["filaments"]}
    return sorted(key for key in groups_renamed if key not in present)


def target(key, value):
    """(new template, new material) for a requested change; a plain string keeps the material."""
    return (value, key[1]) if isinstance(value, str) else tuple(value)


def material_of(key):
    return key.split("::")[4]


def reason_for(old_key, new_key):
    return "rename" if material_of(old_key) == material_of(new_key) else "reclassification"


def rename_source(text, groups_renamed, keep=()):
    """Rename group templates textually so unrelated formatting is untouched.

    ``groups_renamed`` maps (template, material) to a new template, or to a
    (template, material) pair for a reclassification. ``keep`` holds (old
    template, color name) pairs that stay on their current
    IDs: a renamed group whose colors are all kept is left alone, and kept colors
    of a partly renamed group move into a copy of it under the old template,
    placed directly after it. Splitting needs a full rewrite, which is only done
    when it is lossless."""
    data = json.loads(text)
    expected = json.loads(text)
    keep, used = set(keep), set()
    count = 0
    groups = []
    for group in expected["filaments"]:
        groups.append(group)
        new = groups_renamed.get((group["name"], group["material"]))
        if new is None:
            continue
        kept = [color for color in group.get("colors", []) if (group["name"], color["name"]) in keep]
        used.update((group["name"], color["name"]) for color in kept)
        if kept and len(kept) == len(group.get("colors", [])):
            continue
        old = copy.deepcopy(group)
        group["name"], group["material"] = target((group["name"], group["material"]), new)
        count += 1
        if kept:
            group["colors"] = [color for color in group["colors"] if color not in kept]
            old["colors"] = kept
            groups.append(old)
    expected["filaments"] = groups
    unused = sorted(keep - used)
    if unused:
        raise ValueError("--keep matched no color of a renamed group: " +
                         ", ".join(f"{template!r} {color!r}" for template, color in unused))
    if not count:
        raise ValueError("no group matched the requested renames")
    result = text
    for key, value in groups_renamed.items():
        old, new = key[0], target(key, value)[0]
        for encode in (lambda s: json.dumps(s, ensure_ascii=False), json.dumps):
            result = result.replace(f'"name": {encode(old)}', f'"name": {json.dumps(new, ensure_ascii=False)}')
    if json.loads(result) != expected:
        # A template shared across materials with only some renamed, or a material
        # change, cannot be edited textually; fall back to a full rewrite only if it
        # is lossless.
        if json.dumps(data, indent=2, ensure_ascii=False) + "\n" != text:
            raise ValueError("cannot apply renames without reformatting the file "
                             "(it is not in the standard 2-space JSON format)")
        result = json.dumps(expected, indent=2, ensure_ascii=False) + "\n"
    return result, count


def display_name_groups(text, renames):
    """Renamed groups whose colors carry a ``display_name`` override.

    A rename migration never edits ``display_name``: the override stays the
    published name while the template (and so the ID) changes, which the
    rename identity check cannot pair. Such groups need a separate review."""
    return sorted({f"{group['name']!r} [{group['material']}]" for group in json.loads(text)["filaments"]
                   if (group["name"], group["material"]) in renames
                   and any("display_name" in color for color in group.get("colors", []))})


def plan(root, filename, renames, base_manifest, keep=()):
    """Compile before/after in a scratch copy and pair every removed ID with its new ID."""
    unrefined = sorted(f"{key[0]!r}: {key[1]} -> {target(key, value)[1]}" for key, value in renames.items()
                       if target(key, value)[1] != key[1] and not refines_material(key[1], target(key, value)[1]))
    if unrefined:
        return [], 0, None, [f"{item} is not a more specific material code; only refinements "
                             "(TPU -> TPU-85A, CF -> PA-CF) can be reclassified" for item in unrefined]
    materials_path = root / "materials.json"
    if materials_path.is_file():
        listed = {entry["material"] for entry in json.loads(materials_path.read_text(encoding="utf-8"))}
        unlisted = sorted({target(key, value)[1] for key, value in renames.items()
                           if target(key, value)[1] != key[1]} - listed)
        if unlisted:
            return [], 0, None, [f"{material} is not in materials.json; add it (with its density) before "
                                 "reclassifying into it" for material in unlisted]
    overrides = display_name_groups((root / "filaments" / filename).read_text(encoding="utf-8"), renames)
    if overrides:
        return [], 0, None, [f"{group}: has display_name overrides; rename migrations leave display_name "
                             "unchanged and cannot rename this group" for group in overrides]
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / "filaments"
        shutil.copytree(root / "filaments", work)
        before, errors = compile_current_id_manifest(work)
        if errors:
            raise ValueError("catalog does not compile before renaming:\n" + "\n".join(errors))
        path = work / filename
        try:
            new_text, groups = rename_source(path.read_text(encoding="utf-8"), renames, keep)
        except ValueError as exc:
            return [], 0, None, [str(exc)]
        path.write_bytes(new_text.encode("utf-8"))
        after, errors = compile_current_id_manifest(work)
        if errors:
            raise ValueError("renamed catalog does not compile (a rename probably collides with "
                             "an existing record; resolve that as a duplicate first):\n" + "\n".join(errors))
    removed = {key: pid for key, pid in before.items() if key not in after}
    added = {key: pid for key, pid in after.items() if key not in before}
    pairs, problems = [], []

    # Groups that change material, by old and by new (template, material).
    reclassified = {key: target(key, value) for key, value in renames.items() if target(key, value)[1] != key[1]}
    reclassified_into = set(reclassified.values())

    def identity(key, pid, removed_side):
        parts = key.split("::")
        group = (parts[2], parts[4])
        try:
            if removed_side and group in reclassified:
                return json.dumps(reclassification_identity(key, reclassified[group][1]), sort_keys=True)
            if not removed_side and group in reclassified_into:
                return json.dumps(reclassification_identity(key, group[1]), sort_keys=True)
            return json.dumps({"rename": rename_identity(key)}, sort_keys=True)
        except ValueError as exc:
            problems.append(f"{pid}: cannot pair as a rename ({exc})")
            return None

    by_identity = {}
    for key, pid in added.items():
        ident = identity(key, pid, False)
        if ident is not None:
            by_identity.setdefault(ident, []).append((key, pid))
    historical = set(base_manifest.values())
    base_keys = {pid: key for key, pid in base_manifest.items()}
    for key, old_id in sorted(removed.items(), key=lambda kv: kv[1]):
        ident = identity(key, old_id, True)
        if ident is None:
            continue
        matches = by_identity.pop(ident, [])
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


def build_registry(registry, pairs, ref, source):
    """New registry with one rename or reclassification entry per pair; existing
    entries pointing at a renamed ID are re-pointed to its replacement (A -> B,
    B -> C gives A -> C). An existing retirement cannot follow a material change:
    its own identity check would no longer match, so that is reported."""
    registry = copy.deepcopy(registry)
    retired = registry["retired"]
    mapping = {old_id: new_id for old_id, new_id, _old_key, _new_key in pairs}
    problems = [f"{old_id}: already retired" for old_id in mapping if old_id in retired]
    reclassified = {old_id for old_id, _new_id, old_key, new_key in pairs
                    if reason_for(old_key, new_key) == "reclassification"}
    problems += [f"{old_id}: existing retirement points at {entry['replaced_by']}, which this change reclassifies; "
                 "keep that colour with --keep and resolve the retirement first"
                 for old_id, entry in retired.items() if entry["replaced_by"] in reclassified]
    repointed = []
    for old_id, entry in retired.items():
        target = mapping.get(entry["replaced_by"])
        if target is not None:
            repointed.append((old_id, entry["replaced_by"], target))
            entry["replaced_by"] = target
    for old_id, new_id, old_key, _new_key in pairs:
        retired.setdefault(old_id, {"replaced_by": new_id, "reason": reason_for(old_key, _new_key), "ref": ref,
                                    "source": source, "retired_key": old_key})
    return registry, repointed, problems


def records_by_id(rows):
    return {row["record"]["id"]: (row["key"], row["record"]) for row in rows}


def _sample(ids, limit=5):
    ids = sorted(ids)
    return ", ".join(ids[:limit]) + (f" (+{len(ids) - limit} more)" if len(ids) > limit else "")


def verify_rename_scope(base_records, base_registry, head_records, head_registry):
    """Prove a change is a pure rename migration, independent of the baseline check.

    ``*_records`` map public ID -> (identity key, compiled record). Requires that
    the change adds only ``rename`` or ``reclassification`` retirements, re-points existing entries only
    onto the final ID of a newly renamed target, retires exactly the renamed old
    IDs, adds exactly their one-to-one replacements, leaves every other record's
    key and fields untouched, and changes nothing but ``id``/``name`` between a
    renamed record and its replacement (plus ``material`` for a reclassification,
    which must change it). Returns (errors, {old_id: new_id}).
    """
    errors = []
    before, after = base_registry["retired"], head_registry["retired"]
    pairs = {}
    for old_id, entry in after.items():
        if old_id not in before:
            if entry.get("reason") in MIGRATION_REASONS:
                pairs[old_id] = entry.get("replaced_by")
            else:
                errors.append(f"registry {old_id}: new {entry.get('reason')!r} retirement is outside a rename migration")
    for old_id, prev in before.items():
        entry = after.get(old_id)
        if entry is None:
            errors.append(f"registry {old_id}: existing retirement removed")
            continue
        changed = sorted(field for field in prev.keys() | entry.keys() if prev.get(field) != entry.get(field))
        if not changed:
            continue
        if changed != ["replaced_by"]:
            errors.append(f"registry {old_id}: existing entry changed {', '.join(changed)}")
        elif pairs.get(prev["replaced_by"]) != entry["replaced_by"]:
            errors.append(f"registry {old_id}: re-pointed to {entry['replaced_by']}, but its old target "
                          f"{prev['replaced_by']} was not renamed to it")
    if not pairs:
        errors.append("no rename retirements in this change")
    for target, count in Counter(pairs.values()).items():
        if count > 1:
            errors.append(f"{target}: replaces {count} renamed IDs; renames must be one-to-one")
    for old_id, entry in after.items():
        if entry.get("replaced_by") in pairs:
            errors.append(f"registry {old_id}: points at renamed ID {entry['replaced_by']}; re-point it to the final ID")

    removed = base_records.keys() - head_records.keys()
    added = head_records.keys() - base_records.keys()
    if removed - pairs.keys():
        errors.append(f"IDs removed without a rename retirement: {_sample(removed - pairs.keys())}")
    if pairs.keys() - removed:
        errors.append(f"rename retirements for IDs that were not removed: {_sample(pairs.keys() - removed)}")
    if added - set(pairs.values()):
        errors.append(f"new IDs that are not rename replacements: {_sample(added - set(pairs.values()))}")
    if set(pairs.values()) - added:
        errors.append(f"rename replacements that are not new IDs: {_sample(set(pairs.values()) - added)}")

    rekeyed, modified = [], []
    for pid in base_records.keys() & head_records.keys():
        (base_key, base_rec), (head_key, head_rec) = base_records[pid], head_records[pid]
        if base_key != head_key:
            rekeyed.append(pid)
        elif base_rec != head_rec:
            modified.append(pid)
    if rekeyed:
        errors.append(f"identity keys changed on unchanged public IDs: {_sample(rekeyed)}")
    if modified:
        errors.append(f"fields changed on records that are not renamed: {_sample(modified)}")

    for old_id, new_id in sorted(pairs.items()):
        if old_id not in base_records or new_id not in head_records:
            continue
        (old_key, old_rec), (_new_key, new_rec) = base_records[old_id], head_records[new_id]
        if after[old_id].get("retired_key") != old_key:
            errors.append(f"registry {old_id}: retired_key is not the record's identity key")
        reason = after[old_id].get("reason")
        allowed = RECLASSIFICATION_FIELDS if reason == "reclassification" else RENAME_FIELDS
        fields = sorted(f for f in old_rec.keys() | new_rec.keys()
                        if f not in allowed and old_rec.get(f) != new_rec.get(f))
        if fields:
            errors.append(f"{old_id} -> {new_id}: {reason} also changes {', '.join(fields)}")
        if reason == "reclassification" and old_rec.get("material") == new_rec.get("material"):
            errors.append(f"{old_id} -> {new_id}: reclassification keeps the material; use reason rename")
    return errors, pairs


def dirty_paths(root):
    """Uncommitted (including untracked) changes under the directories a migration reads."""
    out = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all", "--", *STAGED_DIRS],
                         cwd=root, capture_output=True, text=True, encoding="utf-8", check=True).stdout
    return [line[3:] for line in out.splitlines() if line.strip()]


def stage_and_validate(root, filename, new_text, registry, base_payload, base_registry, base_ref):
    """Build the full result in a scratch copy and validate it before anything is written.

    The scope check compares the staged result with the trusted ``base_ref`` (read
    from git), not with the working tree, so any change other than this rename,
    committed or not, fails.

    Returns ({path: bytes} to write, errors)."""
    with tempfile.TemporaryDirectory() as tmp:
        stage = Path(tmp)
        for sub in STAGED_DIRS:
            if (root / sub).is_dir():
                shutil.copytree(root / sub, stage / sub)
        source_path = stage / "filaments" / filename
        registry_path = stage / "contracts" / "retired_ids.json"
        baseline_path = stage / "contracts" / BASELINE_PATH.name
        source_path.write_bytes(new_text.encode("utf-8"))
        registry_path.write_text(json.dumps(registry, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        manifest, errors = compile_current_id_manifest(stage / "filaments")
        if errors:
            return {}, errors
        baseline = {"version": 1, "count": len(manifest), "manifest": dict(sorted(manifest.items()))}
        baseline_path.write_text(json.dumps(baseline, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

        result = check_baseline_manifest_detailed(
            baseline_path=baseline_path, filaments_dir=stage / "filaments", base_baseline_path=base_payload,
            strict_head_sync=True, retired_path=registry_path, base_retired=base_registry,
        )
        errors = list(result.all_errors)
        scope_errors, _pairs = verify_rename_scope(records_by_id(catalog_records(root, base_ref)), base_registry,
                                                   records_by_id(catalog_records(stage)), registry)
        errors.extend(scope_errors)
        outputs = {root / "filaments" / filename: source_path.read_bytes(),
                   root / "contracts" / "retired_ids.json": registry_path.read_bytes(),
                   root / "contracts" / BASELINE_PATH.name: baseline_path.read_bytes()}
    return outputs, errors


def write_all(outputs):
    """Replace each file atomically; restore every original if any write fails."""
    originals = {path: path.read_bytes() if path.exists() else None for path in outputs}
    try:
        for path, data in outputs.items():
            tmp = path.with_name(f".{path.name}.rename-tmp")
            tmp.write_bytes(data)
            os.replace(tmp, path)
    except BaseException:
        for path, data in originals.items():
            path.with_name(f".{path.name}.rename-tmp").unlink(missing_ok=True)
            if data is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(data)
        raise


def verify_main(base_ref, if_renames=False):
    """Check the working tree against ``base_ref`` as a rename-only migration.

    With ``if_renames`` (CI), a change that adds no rename retirement passes
    without checking, so ordinary data changes keep their own workflow."""
    base_registry = load_contract(base_ref, ROOT, "retired_ids.json", "retired")
    head_registry = load_contract(REGISTRY_PATH, ROOT, "retired_ids.json", "retired")
    if if_renames and not any(entry.get("reason") in MIGRATION_REASONS
                              for old_id, entry in head_registry["retired"].items()
                              if old_id not in base_registry["retired"]):
        print(f"No new rename or reclassification retirements against {base_ref}; rename scope check not needed.")
        return 0
    base_records = records_by_id(catalog_records(ROOT, base_ref))
    errors, pairs = verify_rename_scope(base_records, base_registry, records_by_id(catalog_records(ROOT)), head_registry)
    if errors:
        print("ERROR: not a rename-only migration:", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1
    reclassified = sum(head_registry["retired"][old_id]["reason"] == "reclassification" for old_id in pairs)
    detail = f" ({reclassified} reclassified)" if reclassified else ""
    print(f"OK: rename-only migration, {len(pairs)} public ID(s) renamed{detail} against {base_ref}")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--file", help="manufacturer file name in filaments/, e.g. addnorth.json")
    parser.add_argument("--rename", nargs=3, action="append", default=[], metavar=("OLD", "NEW", "MATERIAL"),
                        help="rename group template OLD to NEW for groups of MATERIAL (repeatable)")
    parser.add_argument("--reclassify", nargs=4, action="append", default=[],
                        metavar=("OLD", "NEW", "OLD_MATERIAL", "NEW_MATERIAL"),
                        help="move group OLD of OLD_MATERIAL to template NEW and the more specific "
                             "NEW_MATERIAL (repeatable; needs product-specific evidence)")
    parser.add_argument("--upstream", nargs=2, metavar=("BEFORE", "AFTER"),
                        help="take same-material renames from an upstream change of the same file")
    parser.add_argument("--keep", nargs=2, action="append", default=[], metavar=("TEMPLATE", "COLOR"),
                        help="leave COLOR of a group named TEMPLATE on its current ID (repeatable)")
    parser.add_argument("--ref", help="review reference (upstream PR URL, issue, audit)")
    parser.add_argument("--source", help="evidence: commit SHA or URL")
    parser.add_argument("--base-ref", default="HEAD", help="trusted baseline commit (default HEAD)")
    parser.add_argument("--apply", action="store_true", help="write source, registry and baseline")
    parser.add_argument("--verify", action="store_true",
                        help="check the working tree against --base-ref as a rename-only migration")
    parser.add_argument("--if-renames", action="store_true",
                        help="with --verify: pass without checking when no rename retirement is added (CI)")
    args = parser.parse_args(argv)

    if args.verify:
        return verify_main(args.base_ref, args.if_renames)
    for name in ("file", "ref", "source"):
        if not getattr(args, name):
            parser.error(f"--{name} is required unless --verify is given")
    dirty = dirty_paths(ROOT)
    if dirty:
        print("ERROR: run rename migrations from a clean checkout; uncommitted changes in:", file=sys.stderr)
        for path in dirty:
            print(f"  {path}", file=sys.stderr)
        return 1
    if not valid_source(args.source):
        parser.error("--source must be a 40-character commit SHA or an http(s) URL")
    renames = {(old, material): new for old, new, material in args.rename}
    for old, new, old_material, new_material in args.reclassify:
        if old_material == new_material:
            parser.error(f"--reclassify {old!r}: the material does not change; use --rename")
        if not refines_material(old_material, new_material):
            parser.error(f"--reclassify {old!r}: {new_material} is not a more specific code for {old_material}")
        if (old, old_material) in renames:
            parser.error(f"conflicting changes for {(old, old_material)}")
        renames[(old, old_material)] = (new, new_material)
    if args.upstream:
        try:
            found, skipped = upstream_renames(ROOT, args.file, *args.upstream)
        except (ValueError, subprocess.CalledProcessError) as exc:
            detail = exc.stderr.strip() if isinstance(exc, subprocess.CalledProcessError) else exc
            parser.error(f"cannot read upstream renames: {detail}")
        for item in skipped:
            print(f"SKIP (material change, not a rename): {item}")
        if skipped:
            print("  Material changes need product-specific evidence. Once confirmed, pass each with "
                  "--reclassify OLD NEW OLD_MATERIAL NEW_MATERIAL.")
        for key, new in found.items():
            if target(key, renames.setdefault(key, new)) != target(key, new):
                parser.error(f"conflicting renames for {key}")
    if not renames:
        parser.error("no renames given")
    source_path = ROOT / "filaments" / args.file
    if not source_path.is_file():
        parser.error(f"no such manufacturer file: filaments/{args.file}")
    missing = unmatched_renames(source_path.read_text(encoding="utf-8"), renames)
    for flag, requested in (("--rename", {(old, material) for old, _new, material in args.rename}),
                            ("--reclassify", {(old, material) for old, _new, material, _m in args.reclassify})):
        if requested & set(missing):
            parser.error(f"{flag} names a group that does not exist: " +
                         ", ".join(f"{old!r} [{material}]" for old, material in sorted(requested & set(missing))))
    for old, material in missing:
        print(f"SKIP (no group named {old!r} [{material}] in {args.file})")
    renames = {key: new for key, new in renames.items() if key not in missing}
    if not renames:
        print(f"ERROR: none of the requested renames match a group in {args.file}; nothing was written.",
              file=sys.stderr)
        return 1
    base, errors = load_baseline_payload(args.base_ref, ROOT)
    if errors:
        parser.error("; ".join(errors))

    pairs, groups, new_text, problems = plan(ROOT, args.file, renames, base["manifest"],
                                             keep={tuple(item) for item in args.keep})
    registry, repointed, registry_problems = build_registry(
        load_contract(REGISTRY_PATH, ROOT, "retired_ids.json", "retired"), pairs, args.ref, args.source)
    problems += registry_problems
    for (old, material), value in sorted(renames.items()):
        new, new_material = target((old, material), value)
        if new_material == material:
            print(f"RENAME [{material}] {old!r} -> {new!r}")
        else:
            print(f"RECLASSIFY [{material} -> {new_material}] {old!r} -> {new!r}")
    for template, color in sorted(args.keep):
        print(f"KEEP {color!r} in {template!r} on its current ID")
    reclassified = [pair for pair in pairs if reason_for(pair[2], pair[3]) == "reclassification"]
    if reclassified:
        print(f"{groups} group(s) changed, {len(pairs) - len(reclassified)} public ID(s) retired as renames, "
              f"{len(reclassified)} as reclassifications")
    else:
        print(f"{groups} group(s) renamed, {len(pairs)} public ID(s) retired as renames")
    for old_id, new_id, old_key, new_key in pairs:
        print(f"  {old_id} -> {new_id}" + (f" ({material_of(old_key)} -> {material_of(new_key)})"
                                           if reason_for(old_key, new_key) == "reclassification" else ""))
    if repointed:
        print(f"{len(repointed)} existing retirement(s) re-pointed to the final ID (evidence unchanged)")
        for old_id, previous, new_id in repointed:
            print(f"  {old_id}: {previous} -> {new_id}")
    if not problems:
        base_registry = load_contract(args.base_ref, ROOT, "retired_ids.json", "retired")
        outputs, validation = stage_and_validate(ROOT, args.file, new_text, registry, base, base_registry,
                                                 args.base_ref)
        problems += validation
    if problems:
        print("\nERROR: migration is not safe; nothing was written:", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1
    if not args.apply:
        print("\nValidated. Dry run only; re-run with --apply to write changes.")
        return 0
    write_all(outputs)
    print(f"Applied: filaments/{args.file}, contracts/retired_ids.json, contracts/{BASELINE_PATH.name}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
