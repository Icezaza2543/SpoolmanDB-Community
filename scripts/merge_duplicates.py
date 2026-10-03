"""Plan exact owner-reviewed retirements; dry-run is the CLI default."""

import argparse
import copy
import json
import os
import re
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.audit_duplicates import audit_brand, brand_filename
from scripts.compile_filaments import expand_filament_data
from scripts.compile_id_baseline import make_canonical_identity_key, parse_json_without_duplicates, validate_baseline_structure
from scripts.duplicate_catalog import catalog_digest, catalog_records
from scripts.retired_ids import check_registry, load_contract, reviewed_bindings, valid_source

COLOR_FIELDS = {"color_hex": "hex", "color_hexes": "hexes", **{field: field for field in ("codes", "eans", "eans_refill", "fill", "finish", "pattern", "multi_color_direction", "translucent", "glow")}}
FAMILY_FIELDS = {"density", "extruder_temp", "extruder_temp_range", "bed_temp", "bed_temp_range", "country_of_origin", "sds_url", "tds_url"}


def plan_merge(root, brand, review, exclude=()):
    root = Path(root).resolve()
    filename = brand_filename(brand)
    if not isinstance(review, dict) or review.get("version") != 1 or review.get("approved") is not True or not isinstance(review.get("groups"), dict):
        raise ValueError("explicit owner-approved review groups required")
    if not isinstance(review.get("upstream_ref"), str) or not re.fullmatch(r"[0-9a-fA-F]{40}", review["upstream_ref"]):
        raise ValueError("review requires a pinned upstream commit SHA, not an unresolved preference")
    report = audit_brand(root, brand, review.get("upstream_ref"), review.get("official_names"), review.get("upstream_exceptions"))
    if review.get("audit_digest") != report["digest"]:
        raise ValueError("stale audit digest; review current data before applying")
    rows = catalog_records(root)
    by_id = {row["record"]["id"]: row for row in rows}
    before = {row["key"]: row["record"]["id"] for row in rows}
    baseline = load_contract(root / "contracts/compiled_id_baseline.json", root, "compiled_id_baseline.json", "manifest")
    if validate_baseline_structure(baseline) or baseline.get("manifest") != before:
        raise ValueError("starting baseline must exactly match compiled catalog")
    registry = load_contract(None, root, "retired_ids.json", "retired")
    previous = copy.deepcopy(registry)
    groups = {group["group_id"]: group for group in report["groups"]}
    if set(exclude) - set(review["groups"]):
        raise ValueError("exclude must reference a reviewed group")
    mapping, updates = {}, {}
    bindings = review.get("bindings", {})
    if not isinstance(bindings, dict):
        raise ValueError("review bindings must be an object")
    for identity, binding in bindings.items():
        if identity in by_id and (not isinstance(binding, dict) or binding.get("key") != by_id[identity]["key"] or ("source_color" in binding and binding["source_color"] != by_id[identity]["color"])):
            raise ValueError("reviewed binding must retain the actual source key/color")
    for gid, decision in review["groups"].items():
        if gid in exclude:
            continue
        if gid not in groups or not isinstance(decision, dict) or decision.get("approved") is not True or not valid_source(decision.get("source")) or not isinstance(decision.get("ref"), str) or not decision["ref"].strip():
            raise ValueError(f"unreviewed or unproven group: {gid}")
        keep, retire = decision.get("survivor"), decision.get("retire")
        if not isinstance(retire, list) or not retire or not all(isinstance(identity, str) for identity in retire) or len(set(retire)) != len(retire) or keep in retire or keep not in groups[gid]["ids"] or not set(retire) <= set(groups[gid]["ids"]):
            raise ValueError(f"exact surviving/retired group membership required: {gid}")
        proposed = groups[gid]["proposed_survivor"]
        if proposed and keep != proposed:
            raise ValueError(f"survivor contradicts approved priority/evidence: {gid}")
        for old in retire:
            if old in mapping or old in registry["retired"]:
                raise ValueError(f"duplicate retirement decision: {old}")
            mapping[old] = keep
            registry["retired"][old] = {"replaced_by": keep, "reason": "duplicate", "ref": decision["ref"], "source": decision["source"], "retired_key": by_id[old]["key"]}
    for old, entry in previous["retired"].items():
        if entry["replaced_by"] in mapping:
            registry["retired"][old]["replaced_by"] = mapping[entry["replaced_by"]]
    for evidence in review.get("metadata", []):
        identity, values = evidence.get("id"), evidence.get("values")
        if identity not in set(mapping.values()) or evidence.get("approved") is not True or evidence.get("same_variant") is not True or not valid_source(evidence.get("source")) or not isinstance(evidence.get("lot"), str) or not evidence["lot"].strip():
            raise ValueError("metadata requires matching survivor/SKU/package and newest-lot review evidence")
        if not isinstance(values, dict) or not values or set(values) - (FAMILY_FIELDS | set(COLOR_FIELDS) | {"spool_weight"}):
            raise ValueError("only supported ID-neutral metadata fields may change")
        if identity in updates:
            raise ValueError("conflicting metadata decisions for survivor")
        updates[identity] = values
    source_path = root / "filaments" / filename
    source = json.loads(source_path.read_text(encoding="utf-8"))
    affected = {by_id[identity]["definition_index"] for identity in set(mapping) | set(updates)}
    new_definitions = []
    for index, definition in enumerate(source["filaments"]):
        if index not in affected:
            new_definitions.append(definition)
            continue
        for row in rows:
            if row["filename"] != filename or row["definition_index"] != index or row["record"]["id"] in mapping:
                continue
            cell = copy.deepcopy(row["cell"])
            for field, value in updates.get(row["record"]["id"], {}).items():
                target = cell if field in FAMILY_FIELDS else cell["weights"][0] if field == "spool_weight" else cell["colors"][0]
                source_field = COLOR_FIELDS.get(field, field)
                if value is None:
                    target.pop(source_field, None)
                else:
                    target[source_field] = value
            new_definitions.append(cell)
    new_source = {**source, "filaments": new_definitions}
    # Validate schema before compiling; metadata cannot sneak invalid types into data.
    import jsonschema
    try:
        jsonschema.validate(new_source, json.loads((ROOT / "filaments.schema.json").read_text(encoding="utf-8")))
    except jsonschema.ValidationError as exc:
        raise ValueError(f"reviewed metadata violates source schema: {exc.message}") from exc
    after_records, after = {}, {}
    for row in rows:
        if row["filename"] != filename:
            after[row["key"]] = row["record"]["id"]
            after_records[row["record"]["id"]] = row["record"]
    for definition in new_definitions:
        for record in expand_filament_data(source["manufacturer"], definition):
            key = make_canonical_identity_key(filename, source["manufacturer"], definition["name"], record["name"], record["material"], record["weight"], record["diameter"], record["spool_type"], record["is_refill"])
            if key in after or record["id"] in after_records:
                raise ValueError("merge creates duplicate ID/identity")
            after[key], after_records[record["id"]] = record["id"], record
    expected = {key: identity for key, identity in before.items() if identity not in mapping}
    if after != expected:
        raise ValueError("merge changes unique/survivor identity or creates Cartesian variants")
    for identity, row in by_id.items():
        if identity in mapping:
            continue
        expected_record = {**row["record"], **updates.get(identity, {})}
        if after_records[identity] != expected_record:
            raise ValueError(f"merge changes unintended compiled metadata: {identity}")
    persisted_bindings = reviewed_bindings(registry, root)
    if any(persisted_bindings.get(identity) != binding for identity, binding in bindings.items()):
        raise ValueError("reviewed decompositions must be retained in registry ref JSON for later checks")
    registry_errors, _, _ = check_registry(registry, previous, before, after, after, audits=persisted_bindings)
    if registry_errors:
        raise ValueError("; ".join(registry_errors))
    changes = {}
    if mapping or updates:
        changes = {f"filaments/{filename}": new_source, "contracts/retired_ids.json": registry,
                   "contracts/compiled_id_baseline.json": {"version": 1, "count": len(after), "manifest": dict(sorted(after.items()))}}
    return {"version": 1, "brand": brand, "digest": report["digest"], "changes": changes, "exclude": list(exclude),
            "retired_ids": mapping, "new_ids": [], "before_count": len(before), "after_count": len(after),
            "audit": report, "review": copy.deepcopy(review),
            "metadata_note": "manufacturer revised recommended values in newer lot" if updates else "No supplied lot evidence; survivor values retained, conflicts unresolved."}


def apply_plan(root, plan):
    """Re-plan untrusted input, then stage replacements; restore originals on I/O failure."""
    root = Path(root).resolve()
    if plan.get("digest") != catalog_digest(root):
        raise ValueError("stale plan; catalog/contracts changed")
    # Never execute arbitrary changes injected into a saved plan.
    verified = plan_merge(root, plan["brand"], plan["review"], exclude=plan.get("exclude", ()))
    if verified["changes"] != plan["changes"]:
        raise ValueError("plan payload differs from reviewed source changes")
    originals, staged, replaced = {}, {}, []
    try:
        for relative, payload in verified["changes"].items():
            target = (root / relative).resolve()
            if not target.is_relative_to(root) or not target.is_file():
                raise ValueError("apply target must be an existing repository data file")
            originals[target] = target.read_bytes()
            with tempfile.NamedTemporaryFile(dir=target.parent, prefix=".duplicate-", suffix=".tmp", delete=False) as handle:
                staged[target] = Path(handle.name)
                handle.write((json.dumps(payload, indent=2, ensure_ascii=False) + "\n").encode("utf-8"))
                handle.flush()
                os.fsync(handle.fileno())
        for target, temporary in staged.items():
            os.replace(temporary, target)
            replaced.append(target)
    except Exception:
        for target in reversed(replaced):
            with tempfile.NamedTemporaryFile(dir=target.parent, prefix=".duplicate-rollback-", delete=False) as handle:
                rollback = Path(handle.name)
                handle.write(originals[target])
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(rollback, target)
        raise
    finally:
        for temporary in staged.values():
            temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--brand", required=True)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--review", type=Path, help="Owner-reviewed JSON; without it, only show audit proposals")
    parser.add_argument("--exclude", action="append", default=[], help="Exact group ID (repeatable)")
    parser.add_argument("--upstream-ref", help="Already fetched upstream ref for unreviewed dry-run")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    try:
        if not args.review:
            if args.apply:
                raise ValueError("--apply requires --review; candidates alone never authorize retirement")
            report = audit_brand(args.root, args.brand, args.upstream_ref)
            print("DRY RUN: unreviewed candidate proposals only")
            print(json.dumps(report, indent=2, ensure_ascii=False))
            return
        review = parse_json_without_duplicates(args.review.read_text(encoding="utf-8"))
        plan = plan_merge(args.root, args.brand, review, args.exclude)
        plan["exclude"] = args.exclude
        if args.apply:
            apply_plan(args.root, plan)
        print("APPLIED reviewed changes" if args.apply else "DRY RUN: no catalog/contract writes")
        print(json.dumps(plan, indent=2, ensure_ascii=False))
    except (ValueError, OSError, KeyError) as exc:
        parser.exit(1, f"ERROR: {exc}\n")


if __name__ == "__main__":
    main()
