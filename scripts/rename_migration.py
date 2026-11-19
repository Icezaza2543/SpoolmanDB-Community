"""Plan or apply a reviewed rename migration for a manufacturer file.

In standard mode, a rename changes a filament group's ``name`` template only. Because the
template is part of ``generate_id``, every compiled variant of a renamed group
gets a new public ID. This tool keeps that auditable: each old ID is retired in
``contracts/retired_ids.json`` with ``reason: "rename"`` and points at its new
ID, then the baseline enrolls the new IDs. ``scripts/retired_ids.py`` verifies
every pair (same file, manufacturer, material, package and color; the product
line may differ only by text repeating the manufacturer or material).

Renames come from ``--rename OLD NEW MATERIAL`` pairs, or from an upstream
SpoolmanDB change with ``--upstream BEFORE AFTER`` (same-material name changes
only; material changes are reported and skipped). Without ``--apply`` nothing
is written.

A reviewed manufacturer spelling correction can additionally specify
``--previous-file``, ``--manufacturer-rename OLD NEW`` and ``--audit``. That
mode records exact old/new identity-key pairs in a tracked audit so validation
can allow only the approved label, filename and manufacturer changes while
still requiring material, package and color identity to match.

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
it with ``--if-renames`` on every change that adds a rename retirement.

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
from scripts.duplicate_catalog import catalog_records, corrected_rename_identity, rename_identity  # noqa: E402
from scripts.retired_ids import load_contract, reviewed_bindings, valid_source  # noqa: E402

REGISTRY_PATH = ROOT / "contracts" / "retired_ids.json"
# The only compiled fields a rename may change.
RENAME_FIELDS = {"id", "name"}
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


def rename_manufacturer_source(text, old, new):
    """Replace the exact top-level manufacturer while preserving source formatting."""
    data = json.loads(text)
    if data.get("manufacturer") != old:
        raise ValueError(f"source manufacturer is {data.get('manufacturer')!r}, not {old!r}")
    expected = copy.deepcopy(data)
    expected["manufacturer"] = new
    old_value = json.dumps(old, ensure_ascii=False)
    new_value = json.dumps(new, ensure_ascii=False)
    result = text.replace(f'"manufacturer": {old_value}', f'"manufacturer": {new_value}', 1)
    if json.loads(result) != expected:
        raise ValueError("cannot update manufacturer without reformatting the file")
    return result


def display_name_groups(text, renames):
    """Renamed groups whose colors carry a ``display_name`` override.

    A rename migration never edits ``display_name``: the override stays the
    published name while the template (and so the ID) changes, which the
    rename identity check cannot pair. Such groups need a separate review."""
    return sorted({f"{group['name']!r} [{group['material']}]" for group in json.loads(text)["filaments"]
                   if (group["name"], group["material"]) in renames
                   and any("display_name" in color for color in group.get("colors", []))})


def plan(root, filename, renames, base_manifest, previous_file=None, manufacturer_rename=None):
    """Compile before/after in a scratch copy and pair every removed ID with its new ID."""
    previous_file = previous_file or filename
    old_source = root / "filaments" / previous_file
    overrides = display_name_groups(old_source.read_text(encoding="utf-8"), renames)
    if overrides:
        return [], 0, None, [f"{group}: has display_name overrides; rename migrations leave display_name "
                             "unchanged and cannot rename this group" for group in overrides]
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / "filaments"
        shutil.copytree(root / "filaments", work)
        before, errors = compile_current_id_manifest(work)
        if errors:
            raise ValueError("catalog does not compile before renaming:\n" + "\n".join(errors))
        old_path = work / previous_file
        path = work / filename
        if old_path != path and path.exists():
            return [], 0, None, [f"destination source file already exists: {filename}"]
        new_text, groups = rename_source(old_path.read_text(encoding="utf-8"), renames)
        if manufacturer_rename:
            new_text = rename_manufacturer_source(new_text, *manufacturer_rename)
        path.write_bytes(new_text.encode("utf-8"))
        if old_path != path:
            old_path.unlink()
        after, errors = compile_current_id_manifest(work)
        if errors:
            raise ValueError("renamed catalog does not compile (a rename probably collides with "
                             "an existing record; resolve that as a duplicate first):\n" + "\n".join(errors))
    removed = {key: pid for key, pid in before.items() if key not in after}
    added = {key: pid for key, pid in after.items() if key not in before}
    pairs, problems = [], []

    identity_fn = corrected_rename_identity if manufacturer_rename else rename_identity

    def identity(key, pid):
        try:
            return json.dumps(identity_fn(key), sort_keys=True)
        except ValueError as exc:
            problems.append(f"{pid}: cannot pair as a rename ({exc})")
            return None

    by_identity = {}
    for key, pid in added.items():
        ident = identity(key, pid)
        if ident is not None:
            by_identity.setdefault(ident, []).append((key, pid))
    historical = set(base_manifest.values())
    base_keys = {pid: key for key, pid in base_manifest.items()}
    for key, old_id in sorted(removed.items(), key=lambda kv: kv[1]):
        ident = identity(key, old_id)
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
    """New registry with one rename entry per pair; existing entries pointing at a
    renamed ID are re-pointed to its replacement (A -> B, B -> C gives A -> C)."""
    registry = copy.deepcopy(registry)
    retired = registry["retired"]
    mapping = {old_id: new_id for old_id, new_id, _old_key, _new_key in pairs}
    problems = [f"{old_id}: already retired" for old_id in mapping if old_id in retired]
    repointed = []
    for old_id, entry in retired.items():
        target = mapping.get(entry["replaced_by"])
        if target is not None:
            repointed.append((old_id, entry["replaced_by"], target))
            entry["replaced_by"] = target
    for old_id, new_id, old_key, _new_key in pairs:
        retired.setdefault(old_id, {"replaced_by": new_id, "reason": "rename", "ref": ref,
                                    "source": source, "retired_key": old_key})
    return registry, repointed, problems


def build_correction_audit(pairs, evidence):
    """Persist exact pairings for an approved brand/file spelling correction."""
    bindings = {
        old_id: {"key": old_key, "rename": {"replaced_by": new_id, "new_key": new_key}}
        for old_id, new_id, old_key, new_key in pairs
    }
    return {"version": 1, "evidence": evidence, "bindings": bindings}


def records_by_id(rows):
    return {row["record"]["id"]: (row["key"], row["record"]) for row in rows}


def _sample(ids, limit=5):
    ids = sorted(ids)
    return ", ".join(ids[:limit]) + (f" (+{len(ids) - limit} more)" if len(ids) > limit else "")


def verify_rename_scope(base_records, base_registry, head_records, head_registry, rename_bindings=None):
    """Prove a change is a pure rename migration, independent of the baseline check.

    ``*_records`` map public ID -> (identity key, compiled record). Requires that
    the change adds only ``rename`` retirements, re-points existing entries only
    onto the final ID of a newly renamed target, retires exactly the renamed old
    IDs, adds exactly their one-to-one replacements, and leaves every other
    record's key and fields untouched. Normal renames may change only ``id`` and
    ``name``; an audited manufacturer correction may also change ``manufacturer``.
    Returns (errors, {old_id: new_id}).
    """
    errors = []
    rename_bindings = rename_bindings or {}
    before, after = base_registry["retired"], head_registry["retired"]
    pairs = {}
    for old_id, entry in after.items():
        if old_id not in before:
            if entry.get("reason") == "rename":
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
        binding = rename_bindings.get(old_id, {})
        reviewed = binding.get("rename") if isinstance(binding, dict) else None
        (old_key, old_rec), (_new_key, new_rec) = base_records[old_id], head_records[new_id]
        if reviewed is not None:
            if (binding.get("key") != old_key or reviewed.get("replaced_by") != new_id or
                    reviewed.get("new_key") != head_records[new_id][0]):
                errors.append(f"{old_id}: reviewed correction audit does not match replacement {new_id}")
            else:
                try:
                    if corrected_rename_identity(old_key) != corrected_rename_identity(head_records[new_id][0]):
                        errors.append(f"{old_id} -> {new_id}: reviewed correction changes physical identity")
                except ValueError as exc:
                    errors.append(f"{old_id} -> {new_id}: invalid reviewed correction identity: {exc}")
        if after[old_id].get("retired_key") != old_key:
            errors.append(f"registry {old_id}: retired_key is not the record's identity key")
        allowed_fields = RENAME_FIELDS | ({"manufacturer"} if reviewed is not None else set())
        fields = sorted(f for f in old_rec.keys() | new_rec.keys()
                        if f not in allowed_fields and old_rec.get(f) != new_rec.get(f))
        if fields:
            errors.append(f"{old_id} -> {new_id}: rename also changes {', '.join(fields)}")
    return errors, pairs


def dirty_paths(root):
    """Uncommitted (including untracked) changes under the directories a migration reads."""
    out = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all", "--", *STAGED_DIRS],
                         cwd=root, capture_output=True, text=True, encoding="utf-8", check=True).stdout
    return [line[3:] for line in out.splitlines() if line.strip()]


def stage_and_validate(root, filename, previous_file, new_text, registry, base_payload, base_registry, base_ref,
                       audit_path=None, audit_text=None):
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
        previous_source_path = stage / "filaments" / previous_file
        registry_path = stage / "contracts" / "retired_ids.json"
        baseline_path = stage / "contracts" / BASELINE_PATH.name
        if source_path != previous_source_path and source_path.exists():
            return {}, [f"destination source file already exists: {filename}"]
        source_path.write_bytes(new_text.encode("utf-8"))
        if source_path != previous_source_path:
            previous_source_path.unlink()
        staged_audit_path = stage / audit_path if audit_path else None
        if staged_audit_path and audit_text:
            staged_audit_path.parent.mkdir(parents=True, exist_ok=True)
            staged_audit_path.write_text(audit_text, encoding="utf-8")
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
        scope_errors, _pairs = verify_rename_scope(
            records_by_id(catalog_records(root, base_ref)), base_registry,
            records_by_id(catalog_records(stage)), registry,
            rename_bindings=reviewed_bindings(registry, stage),
        )
        errors.extend(scope_errors)
        outputs = {root / "filaments" / filename: source_path.read_bytes(),
                   root / "contracts" / "retired_ids.json": registry_path.read_bytes(),
                   root / "contracts" / BASELINE_PATH.name: baseline_path.read_bytes()}
        if source_path != previous_source_path:
            outputs[root / "filaments" / previous_file] = None
        if audit_path and staged_audit_path:
            outputs[root / audit_path] = staged_audit_path.read_bytes()
    return outputs, errors


def write_all(outputs):
    """Replace each file atomically; restore every original if any write fails."""
    originals = {path: path.read_bytes() if path.exists() else None for path in outputs}
    try:
        for path, data in outputs.items():
            if data is None:
                path.unlink(missing_ok=True)
            else:
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
    if if_renames and not any(entry.get("reason") == "rename" for old_id, entry in head_registry["retired"].items()
                              if old_id not in base_registry["retired"]):
        print(f"No new rename retirements against {base_ref}; rename scope check not needed.")
        return 0
    base_records = records_by_id(catalog_records(ROOT, base_ref))
    try:
        rename_bindings = reviewed_bindings(head_registry, ROOT)
    except (ValueError, OSError, subprocess.SubprocessError, TypeError) as exc:
        print(f"ERROR: cannot load rename correction audit: {exc}", file=sys.stderr)
        return 1
    errors, pairs = verify_rename_scope(base_records, base_registry, records_by_id(catalog_records(ROOT)),
                                        head_registry, rename_bindings=rename_bindings)
    if errors:
        print("ERROR: not a rename-only migration:", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1
    print(f"OK: rename-only migration, {len(pairs)} public ID(s) renamed against {base_ref}")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--file", help="destination manufacturer file name in filaments/, e.g. addnorth.json")
    parser.add_argument("--previous-file", help="existing manufacturer file when its filename is also corrected")
    parser.add_argument("--manufacturer-rename", nargs=2, metavar=("OLD", "NEW"),
                        help="reviewed correction to the top-level manufacturer spelling")
    parser.add_argument("--audit", help="new audit path under docs/audits/ for a manufacturer spelling correction")
    parser.add_argument("--rename", nargs=3, action="append", default=[], metavar=("OLD", "NEW", "MATERIAL"),
                        help="rename group template OLD to NEW for groups of MATERIAL (repeatable)")
    parser.add_argument("--upstream", nargs=2, metavar=("BEFORE", "AFTER"),
                        help="take same-material renames from an upstream change of the same file")
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
    previous_file = args.previous_file or args.file
    correction_mode = args.manufacturer_rename is not None or args.previous_file is not None or args.audit is not None
    if correction_mode and (args.manufacturer_rename is None or args.audit is None):
        parser.error("--manufacturer-rename and --audit are required together for a manufacturer spelling correction")
    if correction_mode and args.upstream:
        parser.error("manufacturer spelling corrections require explicit --rename pairs, not --upstream")
    for source_file in (previous_file, args.file):
        source_path = Path(source_file)
        if source_path.name != source_file or source_path.suffix != ".json":
            parser.error("--file and --previous-file must be JSON filenames, not paths")
    audit_path = None
    if args.audit:
        audit_path = Path(args.audit)
        if (audit_path.is_absolute() or len(audit_path.parts) != 3 or
                audit_path.parts[:2] != ("docs", "audits") or ".." in audit_path.parts or
                audit_path.suffix != ".json"):
            parser.error("--audit must be a new .json file directly under docs/audits/")
        if (ROOT / audit_path).exists():
            parser.error(f"--audit file already exists: {audit_path.as_posix()}")
    if args.manufacturer_rename:
        old_manufacturer, new_manufacturer = args.manufacturer_rename
        if not old_manufacturer.strip() or not new_manufacturer.strip() or old_manufacturer == new_manufacturer:
            parser.error("--manufacturer-rename requires two different nonempty names")
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

    pairs, groups, new_text, problems = plan(
        ROOT, args.file, renames, base["manifest"], previous_file=previous_file,
        manufacturer_rename=args.manufacturer_rename,
    )
    registry_ref = audit_path.as_posix() if audit_path else args.ref
    audit_text = None
    if audit_path and new_text is not None:
        audit = build_correction_audit(pairs, args.ref)
        audit_text = json.dumps(audit, indent=2, ensure_ascii=False) + "\n"
    registry, repointed, registry_problems = build_registry(
        load_contract(REGISTRY_PATH, ROOT, "retired_ids.json", "retired"), pairs, registry_ref, args.source)
    problems += registry_problems
    for (old, material), new in sorted(renames.items()):
        print(f"RENAME [{material}] {old!r} -> {new!r}")
    print(f"{groups} group(s) renamed, {len(pairs)} public ID(s) retired as renames")
    for old_id, new_id, _old_key, _new_key in pairs:
        print(f"  {old_id} -> {new_id}")
    if repointed:
        print(f"{len(repointed)} existing retirement(s) re-pointed to the final ID (evidence unchanged)")
        for old_id, previous, new_id in repointed:
            print(f"  {old_id}: {previous} -> {new_id}")
    if not problems:
        base_registry = load_contract(args.base_ref, ROOT, "retired_ids.json", "retired")
        outputs, validation = stage_and_validate(
            ROOT, args.file, previous_file, new_text, registry, base, base_registry, args.base_ref,
            audit_path=audit_path, audit_text=audit_text,
        )
        problems += validation
    if problems:
        print("\nERROR: rename migration is not safe; nothing was written:", file=sys.stderr)
        for problem in problems:
            print(f"  {problem}", file=sys.stderr)
        return 1
    if not args.apply:
        print("\nValidated. Dry run only; re-run with --apply to write changes.")
        return 0
    write_all(outputs)
    touched = [f"filaments/{args.file}", "contracts/retired_ids.json", f"contracts/{BASELINE_PATH.name}"]
    if previous_file != args.file:
        touched.append(f"deleted filaments/{previous_file}")
    if audit_path:
        touched.append(audit_path.as_posix())
    print("Applied: " + ", ".join(touched))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
