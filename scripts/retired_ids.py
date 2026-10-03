"""Fail-closed retirement contracts; retired identities never require Git recovery."""

import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlparse

from scripts.duplicate_catalog import identity_from_key

ENTRY_FIELDS = {"replaced_by", "reason", "ref", "source", "retired_key"}


def valid_source(source):
    if not isinstance(source, str):
        return False
    parsed = urlparse(source)
    return bool(re.fullmatch(r"[0-9a-fA-F]{40}", source) or
                (parsed.scheme in ("http", "https") and parsed.hostname))


def load_contract(source, root, filename, section):
    """Missing files at an existing pre-contract commit mean an empty contract."""
    empty = {"version": 1, section: {}}
    if isinstance(source, dict):
        return source
    if source is None:
        source = Path(root) / "contracts" / filename
    if isinstance(source, Path) or Path(str(source)).is_file():
        path = Path(source)
        if not path.exists():
            return empty
        raw = path.read_text(encoding="utf-8")
    else:
        ref = str(source)
        subprocess.run(["git", "rev-parse", "--verify", f"{ref}^{{commit}}"], cwd=root, capture_output=True, check=True)
        rel = f"contracts/{filename}"
        listing = subprocess.run(["git", "ls-tree", ref, "--", rel], cwd=root, capture_output=True, text=True, check=True)
        if not listing.stdout.strip():
            return empty
        raw = subprocess.run(["git", "show", f"{ref}:{rel}"], cwd=root, capture_output=True, text=True, encoding="utf-8", check=True).stdout
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate contract key: {key}")
            result[key] = value
        return result
    return json.loads(raw, object_pairs_hook=unique)


def registry_structure(payload):
    errors = []
    if not isinstance(payload, dict) or set(payload) != {"version", "retired"} or type(payload.get("version")) is not int or payload["version"] != 1 or not isinstance(payload.get("retired"), dict):
        return ["registry version/fields must be version 1 and a retired object"]
    for old_id, entry in payload["retired"].items():
        if not isinstance(old_id, str) or not old_id or not isinstance(entry, dict) or set(entry) != ENTRY_FIELDS or not all(isinstance(value, str) and value.strip() for value in entry.values()):
            errors.append(f"registry {old_id}: invalid entry fields")
            continue
        if entry["reason"] != "duplicate":
            errors.append(f"registry {old_id}: invalid reason")
        if not valid_source(entry["source"]):
            errors.append(f"registry {old_id}: invalid source (expected commit SHA or URL)")
        try:
            # Decomposition is separately checked with reviewed bindings.
            if len(entry["retired_key"].split("::")) != 9:
                raise ValueError("expected nine components")
        except ValueError as exc:
            errors.append(f"registry {old_id}: invalid retired_key: {exc}")
    return errors


def check_registry(head, base, base_manifest, current_manifest, head_manifest, audits=None):
    errors = registry_structure(head) + registry_structure(base)
    if errors:
        return errors, set(), set()
    retired, previous = head["retired"], base["retired"]
    current_ids = {value: key for key, value in current_manifest.items()}
    historical_ids = set(base_manifest.values())
    restored = set()
    audits = audits or {}
    for old_id, old_entry in previous.items():
        if old_id not in retired:
            exact_key = old_entry["retired_key"]
            if current_ids.get(old_id) != exact_key or head_manifest.get(exact_key) != old_id:
                errors.append(f"registry {old_id}: deletion requires exact reinstatement and baseline re-enrollment")
            else:
                restored.add(old_id)
            continue
        entry = retired[old_id]
        if any(entry[field] != old_entry[field] for field in ENTRY_FIELDS - {"replaced_by"}):
            errors.append(f"registry {old_id}: original evidence/retired_key fields are immutable")
        old_target = old_entry["replaced_by"]
        if entry["replaced_by"] != old_target:
            if old_target not in retired or old_target in previous or retired[old_target]["replaced_by"] != entry["replaced_by"]:
                errors.append(f"registry {old_id}: re-point only when the old target is newly retired to the same final target")
    for old_id, entry in retired.items():
        target = entry["replaced_by"]
        stored_key = entry["retired_key"]
        if old_id not in previous:
            if old_id not in historical_ids:
                errors.append(f"registry {old_id}: new retirement must refer to a historical ID")
            if base_manifest.get(stored_key) != old_id:
                errors.append(f"registry {old_id}: retired_key does not match trusted baseline")
        elif old_id in historical_ids and base_manifest.get(stored_key) != old_id:
            errors.append(f"registry {old_id}: stored key does not match trusted baseline")
        if old_id == target:
            errors.append(f"registry {old_id}: self-mapping forbidden")
        if target in retired:
            errors.append(f"registry {old_id}: chain/cycle forbidden")
        if target not in current_ids:
            errors.append(f"registry {old_id}: replacement must be a surviving compiled record")
        if old_id not in previous and target not in historical_ids:
            errors.append(f"registry {old_id}: replacement must be an existing historical record")
        if old_id in current_ids:
            errors.append(f"registry {old_id}: retired ID must not reappear")
        if target in current_ids:
            try:
                old = identity_from_key(stored_key, audits.get(old_id))
                new = identity_from_key(current_ids[target], audits.get(target))
                if old != new:
                    raise ValueError("physical color/line or package identity differs")
            except (ValueError, TypeError) as exc:
                errors.append(f"registry {old_id}: identity mismatch: {exc}")
    return errors, set(retired) if not errors else set(), restored if not errors else set()


def reviewed_bindings(payload, root):
    """Local tracked review references can carry lossless per-ID decompositions."""
    bindings = {}
    for entry in payload.get("retired", {}).values():
        ref = entry.get("ref", "") if isinstance(entry, dict) else ""
        if not isinstance(ref, str) or not ref.endswith(".json"):
            continue
        path = (Path(root) / ref).resolve()
        if not path.is_relative_to(Path(root).resolve()):
            raise ValueError("review reference escapes repository")
        if not path.is_file():
            raise ValueError(f"referenced review audit must exist: {ref}")
        review = load_contract(path, root, path.name, "bindings")
        if not isinstance(review.get("bindings"), dict):
            raise ValueError(f"review {ref} requires identity bindings")
        for identity, binding in review["bindings"].items():
            if identity in bindings and bindings[identity] != binding:
                raise ValueError(f"conflicting reviewed bindings for {identity}")
            bindings[identity] = binding
    return bindings
