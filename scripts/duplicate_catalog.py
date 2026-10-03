"""Ordered candidate comparison; matching names are never merge evidence."""

import math
import re
import copy
import hashlib
import json
from pathlib import Path
import subprocess


def normalize_name(name, manufacturer="", material="", color=False):
    """Keep order, repetitions, plus signs and version/line qualifiers."""
    def tokens(value):
        return tuple("gray" if token == "grey" else token for token in
                     re.findall(r"v?\d+(?:\.\d+)+|[^\W_]+|\+|[^\w\s\[\](){}.,:;\-_/]", value.casefold()))
    result = tokens(name)
    if color:
        return result
    prefix = tokens(manufacturer)
    if prefix and result[:len(prefix)] == prefix:
        result = result[len(prefix):]
    mat = tokens(material)
    # A standalone PLA token is removable; PLA+ is not standalone.
    if len(mat) == 1:
        result = tuple(token for i, token in enumerate(result)
                       if not (token == mat[0] and (i + 1 == len(result) or result[i + 1] != "+")))
    return result


def identity_from_key(key, binding=None):
    """Decode stored identity, optionally using a lossless reviewed line/color split."""
    if not isinstance(key, str) or len(key.split("::")) != 9:
        raise ValueError("identity key must contain exactly nine components")
    filename, manufacturer, template, name, material, weight, diameter, spool, refill = key.split("::")
    if not all((filename, manufacturer, template, name, material)) or refill not in ("True", "False") or spool not in ("None", "plastic", "cardboard", "metal"):
        raise ValueError("invalid identity key fields")
    numbers = tuple(float(value) for value in (weight, diameter))
    if any(not math.isfinite(value) or value <= 0 for value in numbers):
        raise ValueError("identity weight/diameter must be positive finite numbers")
    if binding is not None:
        if not isinstance(binding, dict) or binding.get("key") != key or not all(isinstance(binding.get(field), str) and binding[field] for field in ("line", "color")):
            raise ValueError("reviewed identity binding must match the exact stored key")
        line, color = binding["line"], binding["color"]
        source_color = binding.get("source_color")
        if source_color is not None:
            if not isinstance(source_color, str) or not source_color:
                raise ValueError("reviewed source_color must be a nonempty string")
            physical_name = template.format(color_name=source_color)
        elif template.count("{color_name}") == 1:
            prefix, suffix = template.split("{color_name}")
            if not name.startswith(prefix) or (suffix and not name.endswith(suffix)):
                raise ValueError("display-name identity requires reviewed original source_color")
            physical_name = name
        elif "{" not in template:
            physical_name = template
        else:
            raise ValueError("ambiguous identity template")
        if normalize_name(line + " " + color, manufacturer, material) != normalize_name(physical_name, manufacturer, material):
            raise ValueError("reviewed identity decomposition drops or changes name tokens")
        if template.count("{color_name}") == 1:
            required_line = normalize_name(template.replace("{color_name}", ""), manufacturer, material)
            reviewed_line = iter(normalize_name(line, manufacturer, material))
            if not all(any(token == candidate for candidate in reviewed_line) for token in required_line):
                raise ValueError("reviewed identity drops retained template line qualifiers")
    else:
        if template.count("{color_name}") != 1:
            raise ValueError("ambiguous identity requires a reviewed line/color decomposition")
        prefix, suffix = template.split("{color_name}")
        if not name.startswith(prefix) or (suffix and not name.endswith(suffix)):
            raise ValueError("display-name identity requires a reviewed line/color decomposition")
        end = len(name) - len(suffix) if suffix else len(name)
        color, line = name[len(prefix):end], prefix + suffix
        if not color:
            raise ValueError("empty physical color in identity")
        physical_name = name
    return {
        "manufacturer": manufacturer, "material": material, "weight": numbers[0],
        "diameter": numbers[1], "spool_type": None if spool == "None" else spool,
        "is_refill": refill == "True", "line": normalize_name(line, manufacturer, material),
        "color": normalize_name(color, color=True),
        "name": normalize_name(physical_name, manufacturer, material),
    }


def git_output(root, *args):
    return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, encoding="utf-8", check=True).stdout


def catalog_records(root, ref=None):
    """Expand exact source cells, retaining their locations for a reviewed planner."""
    from scripts.compile_filaments import expand_filament_data
    from scripts.compile_id_baseline import make_canonical_identity_key
    root = Path(root)
    if ref:
        ref = git_output(root, "rev-parse", "--verify", f"{ref}^{{commit}}").strip()
        files = git_output(root, "ls-tree", "-r", "--name-only", ref, "--", "filaments").splitlines()
        sources = [(Path(name).name, json.loads(git_output(root, "show", f"{ref}:{name}"))) for name in files if name.endswith(".json") and Path(name).parent.as_posix() == "filaments"]
    else:
        # Match the existing compiler's JSON loader; contract/review parsing is stricter.
        sources = [(path.name, json.loads(path.read_text(encoding="utf-8"))) for path in sorted((root / "filaments").glob("*.json"))]
    result, seen_ids, seen_keys = [], set(), set()
    for filename, source in sources:
        for fi, definition in enumerate(source["filaments"]):
            for wi, weight in enumerate(definition["weights"]):
                for di, diameter in enumerate(definition["diameters"]):
                    for ci, color in enumerate(definition["colors"]):
                        cell = {**definition, "weights": [weight], "diameters": [diameter], "colors": [color]}
                        rec = next(expand_filament_data(source["manufacturer"], cell))
                        key = make_canonical_identity_key(filename, source["manufacturer"], definition["name"], rec["name"], rec["material"], rec["weight"], rec["diameter"], rec["spool_type"], rec["is_refill"])
                        if rec["id"] in seen_ids or key in seen_keys:
                            raise ValueError(f"duplicate compiled public ID/key: {rec['id']}")
                        seen_ids.add(rec["id"])
                        seen_keys.add(key)
                        result.append({"record": rec, "key": key, "filename": filename, "definition_index": fi,
                                       "weight_index": wi, "diameter_index": di, "color_index": ci,
                                       "template": definition["name"], "color": color["name"], "line": definition["name"].replace("{color_name}", "").strip(), "cell": copy.deepcopy(cell)})
    return result


def group_id(ids):
    return "dup-" + hashlib.sha256(json.dumps(sorted(ids), ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()


def candidate_groups(records):
    buckets = {}
    for row in records:
        rec = row["record"]
        identity = tuple(rec[field] for field in ("manufacturer", "material", "weight", "diameter", "spool_type", "is_refill")) + (normalize_name(rec["name"], rec["manufacturer"], rec["material"]),)
        buckets.setdefault(identity, []).append(row)
    return {group_id(row["record"]["id"] for row in rows): sorted(rows, key=lambda row: row["record"]["id"])
            for rows in buckets.values() if len(rows) > 1}


def catalog_digest(root):
    """Byte fingerprint for stale review/plan detection, including contracts."""
    root = Path(root)
    files = sorted((root / "filaments").glob("*.json")) + [root / "contracts" / name for name in ("compiled_id_baseline.json", "retired_ids.json", "not_duplicates.json")]
    digest = hashlib.sha256()
    for path in files:
        digest.update(path.relative_to(root).as_posix().encode() + b"\0")
        digest.update(path.read_bytes() if path.exists() else b"<missing>")
        digest.update(b"\0")
    return digest.hexdigest()


def confirmed_nonduplicates(payload):
    from scripts.retired_ids import valid_source
    if not isinstance(payload, dict) or set(payload) != {"version", "groups"} or type(payload.get("version")) is not int or payload["version"] != 1 or not isinstance(payload.get("groups"), dict):
        raise ValueError("not_duplicates requires version 1 and exact groups")
    confirmed = set()
    for gid, entry in payload["groups"].items():
        if not isinstance(entry, dict) or set(entry) != {"ids", "reason", "ref", "source"}:
            raise ValueError(f"not_duplicates {gid}: invalid fields")
        ids = entry["ids"]
        if not isinstance(ids, list) or len(ids) < 2 or not all(isinstance(identity, str) and identity for identity in ids) or len(set(ids)) != len(ids) or gid != group_id(ids):
            raise ValueError(f"not_duplicates {gid}: invalid exact membership")
        if not all(isinstance(entry[field], str) and entry[field].strip() for field in ("reason", "ref")) or not valid_source(entry["source"]):
            raise ValueError(f"not_duplicates {gid}: missing review evidence")
        confirmed.add(gid)
    return confirmed
