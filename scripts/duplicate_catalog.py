"""Ordered candidate comparison; matching names are never merge evidence."""

import math
import re
import copy
import hashlib
import json
from pathlib import Path
import subprocess

# Only named product-line words; never versions, materials, CF/HF/HS or colors.
MOVABLE_LINE_QUALIFIERS = frozenset({
    "galaxy", "flexible", "glitter", "silk", "matte", "dual", "metallic",
    "rapid", "plus", "basic", "hyper", "fluorescent", "glow", "crystal",
    "his", "toms3d",
})


def line_color_bindings(left_key, left_color, right_key, right_color):
    """Bind exact paired templates without deleting or reordering name tokens.

    A word in a color label is movable only when the counterpart template
    explicitly anchors it. Ambiguous repeated occurrences fail closed.
    """
    keys, colors = (left_key, right_key), (left_color, right_color)
    if not all(isinstance(key, str) for key in keys):
        raise ValueError("paired identity keys must be strings")
    fields = [key.split("::") for key in keys]
    if any(len(f) != 9 for f in fields):
        raise ValueError("invalid paired identity key")
    if (any(fields[0][i] != fields[1][i] for i in (0, 1, 4, 7, 8)) or
            any(float(fields[0][i]) != float(fields[1][i]) for i in (5, 6))):
        raise ValueError("different material or package identity")
    parts, lines, names = [], [], []
    for f, color in zip(fields, colors):
        template, manufacturer, material = f[2], f[1], f[4]
        if template.count("{color_name}") != 1 or not isinstance(color, str) or not color:
            raise ValueError("exact source color and single placeholder required")
        prefix, suffix = template.split("{color_name}")
        pre = normalize_name(prefix, manufacturer, material)
        post = normalize_name(suffix, manufacturer, material)
        middle = normalize_name(color, color=True)
        physical = normalize_name(template.format(color_name=color), manufacturer, material)
        if pre + middle + post != physical:
            raise ValueError("color tokens cannot be dropped by material normalization")
        parts.append([{"role": role, "token": token} for role, tokens in
                      (("line", pre), ("color", middle), ("line", post)) for token in tokens])
        lines.append(pre + post)
        names.append(physical)
    if names[0] != names[1]:
        raise ValueError("remaining name tokens differ in exact order")
    target = max(lines, key=len)
    for side in range(2):
        needed = list(target)
        for token in lines[side]:
            if token not in needed:
                raise ValueError("different product lines")
            needed.remove(token)
        for token in needed:
            if token not in MOVABLE_LINE_QUALIFIERS or token not in lines[1 - side]:
                raise ValueError("qualifier not allowlisted or anchored")
            occurrences = [p for p in parts[side] if p["role"] == "color" and p["token"] == token]
            if len(occurrences) != 1:
                raise ValueError("ambiguous qualifier occurrence")
            occurrences[0]["role"] = "line"
        if tuple(p["token"] for p in parts[side] if p["role"] == "line") != target:
            raise ValueError("line token order differs")
    physical_colors = [tuple(p["token"] for p in side if p["role"] == "color") for side in parts]
    if not physical_colors[0] or physical_colors[0] != physical_colors[1]:
        raise ValueError("remaining color tokens differ")
    return tuple({"key": keys[i], "source_color": colors[i], "line": " ".join(target) or fields[i][4],
                  "color": " ".join(physical_colors[i]), "parts": parts[i],
                  "anchor_key": keys[1 - i], "anchor_source_color": colors[1 - i]} for i in range(2))


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
        if "parts" in binding:
            expected = line_color_bindings(key, source_color, binding.get("anchor_key", ""),
                                           binding.get("anchor_source_color"))[0]
            if binding != expected:
                raise ValueError("reviewed ordered parts or template anchor changed")
        elif normalize_name(line + " " + color, manufacturer, material) != normalize_name(physical_name, manufacturer, material):
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


# Spelled-out reinforcement names that a material code abbreviates.
RENAME_TOKEN_ALIASES = {("carbon", "fiber"): "cf", ("carbon", "fibre"): "cf",
                        ("glass", "fiber"): "gf", ("glass", "fibre"): "gf"}


def _rename_line_tokens(line, manufacturer, material):
    """Product-line tokens with name text that repeats the manufacturer/material removed.

    Only symbols other than ``+`` (``™``, ``®``, ``|``) are discarded besides
    redundant tokens; versions, qualifiers and order are kept, so dropping any
    real line word (``HF``, ``2.0``, ``Basic``) still changes the result.
    """
    def tokens(value):
        raw = normalize_name(value, color=True)
        return [t for t in raw if t == "+" or re.fullmatch(r"[\w.]+", t)]
    result = tokens(line)
    for words, alias in RENAME_TOKEN_ALIASES.items():
        i = 0
        while i + len(words) <= len(result):
            if tuple(result[i:i + len(words)]) == words:
                result[i:i + len(words)] = [alias]
            i += 1
    prefix = tokens(manufacturer)
    if prefix and result[:len(prefix)] == prefix:
        result = result[len(prefix):]
    mat = tokens(material)
    i = 0
    while mat and i + len(mat) <= len(result):
        if result[i:i + len(mat)] == mat:
            del result[i:i + len(mat)]
        else:
            i += 1
    parts = {t for t in mat if t != "+"}
    return tuple(t for i, t in enumerate(result)
                 if not (t in parts and (i + 1 == len(result) or result[i + 1] != "+")))


def rename_identity(key):
    """Physical identity for a pure rename: same file, package, material and color.

    The product line may differ only by text that repeats the manufacturer or
    material (``"PETG - {color_name}"`` -> ``"{color_name}"`` for PETG), which is
    the upstream SpoolmanDB naming convention. Material changes are not renames.
    """
    if not isinstance(key, str) or len(key.split("::")) != 9:
        raise ValueError("identity key must contain exactly nine components")
    filename, manufacturer, template, name, material = key.split("::")[:5]
    if template.count("{color_name}") != 1:
        raise ValueError("rename requires a single {color_name} template")
    base = identity_from_key(key)
    prefix, suffix = template.split("{color_name}")
    return {"filename": filename, **{field: base[field] for field in
            ("manufacturer", "material", "weight", "diameter", "spool_type", "is_refill", "color")},
            # Text before and after the color is kept apart: a rename never moves
            # a qualifier across the color.
            "line": (_rename_line_tokens(prefix, manufacturer, material),
                     _rename_line_tokens(suffix, "", material))}


def corrected_rename_identity(key):
    """Physical identity for a reviewed correction that also changes the brand label.

    The correction audit separately records the exact source filename,
    manufacturer and product-line changes. This identity retains the material,
    package and physical color checks while allowing those reviewed labels to
    change.
    """
    identity = identity_from_key(key)
    return {field: identity[field] for field in
            ("material", "weight", "diameter", "spool_type", "is_refill", "color")}


def manufacturer_spelling(old, new):
    left, right = old.split(), new.split()
    changed = [[a, b] for a, b in zip(left, right) if a.casefold() != b.casefold()]
    return changed[0] if len(left) == len(right) and len(changed) == 1 else [old, new]


def corrected_rename_pair(old_key, new_key, correction):
    """Validate a reviewed manufacturer/file/spelling correction and its product line."""
    if not isinstance(correction, dict):
        raise ValueError("manufacturer correction metadata is required")
    manufacturers = correction.get("manufacturer")
    files = correction.get("file")
    spelling = correction.get("spelling")
    if (not isinstance(manufacturers, list) or len(manufacturers) != 2 or
            not isinstance(files, list) or len(files) != 2 or
            not isinstance(spelling, list) or len(spelling) != 2):
        raise ValueError("invalid manufacturer correction metadata")
    old_manufacturer, new_manufacturer = manufacturers
    old_file, new_file = files
    old_spelling, new_spelling = spelling
    if not all(isinstance(value, str) and value for value in
               (*manufacturers, *files, *spelling)):
        raise ValueError("manufacturer correction metadata values must be nonempty")
    if spelling != manufacturer_spelling(*manufacturers):
        raise ValueError("spelling does not match reviewed manufacturer correction")

    old_parts = old_key.split("::")
    new_parts = new_key.split("::")
    if len(old_parts) != 9 or len(new_parts) != 9:
        raise ValueError("invalid correction identity key")
    if (old_parts[0], old_parts[1]) != (old_file, old_manufacturer):
        raise ValueError("old identity key does not match reviewed manufacturer/file correction")
    if (new_parts[0], new_parts[1]) != (new_file, new_manufacturer):
        raise ValueError("new identity key does not match reviewed manufacturer/file correction")

    corrected_old = list(old_parts)
    corrected_old[0] = new_file
    corrected_old[1] = new_manufacturer
    pattern = re.compile(re.escape(old_spelling), re.IGNORECASE)
    corrected_old[2] = pattern.sub(new_spelling, corrected_old[2])
    if corrected_old[2].count("{color_name}") != 1:
        return False
    prefix, suffix = corrected_old[2].split("{color_name}")
    old_prefix, old_suffix = old_parts[2].split("{color_name}") if old_parts[2].count("{color_name}") == 1 else ("", "")
    old_end = len(old_parts[3]) - len(old_suffix) if old_suffix else len(old_parts[3])
    if not old_parts[3].startswith(old_prefix):
        return False
    if old_suffix and not old_parts[3].endswith(old_suffix):
        return False
    color = old_parts[3][len(old_prefix):old_end]
    if not color:
        return False
    corrected_old[3] = prefix + color + suffix
    return rename_identity("::".join(corrected_old)) == rename_identity(new_key)


def material_parts(material):
    """Alphanumeric parts of a material code: ``TPU-85A`` -> {"tpu", "85a"}."""
    return {token for token in normalize_name(material, color=True) if re.fullmatch(r"[\w.]+", token)}


def refines_material(old, new):
    """True when ``new`` keeps every part of ``old`` and adds detail.

    ``TPU`` -> ``TPU-85A`` (hardness), ``CF`` -> ``PA-CF`` (base polymer) and
    ``PC`` -> ``PC+ABS`` refine; ``PLA`` -> ``PLA+`` adds no part and ``PA`` ->
    ``PETG`` drops one, so neither does.
    """
    return material_parts(old) < material_parts(new)


def _compact_hardness_tokens(material):
    """Name tokens that write a material's polymer and Shore hardness as one word.

    Product names often run them together: ``TPU90`` or ``TPU95A`` for
    ``TPU-90A`` / ``TPU-95A``. Only a Shore hardness part (``90A``, ``72D``)
    qualifies, and only directly after a polymer part of the same code, so
    ``TPU90`` is not covered by ``TPU-95A`` and ``PA6`` is not a hardness. The
    scale letter may be left out only for Shore A, the convention for filament
    names; a Shore D code needs the ``D`` (``TPU72D``, not ``TPU72``).
    """
    parts = material_parts(material)
    hardness = {part for part in parts if re.fullmatch(r"\d+[ad]", part)}
    polymers = parts - hardness
    return {polymer + form for polymer in polymers for part in hardness
            for form in ((part, part[:-1]) if part.endswith("a") else (part,))}


def reclassification_identity(key, material):
    """Physical identity of ``key`` as a record of the refined ``material``.

    Like ``rename_identity`` but without the material, and with any line text
    that ``material`` now carries removed (``"85A {color_name}"`` as TPU equals
    ``"{color_name}"`` as TPU-85A). Everything else, colour included, must match.
    """
    base = rename_identity(key)
    _filename, manufacturer, template, _name, own_material = key.split("::")[:5]
    parts = material_parts(material) | _compact_hardness_tokens(material)
    prefix, suffix = template.split("{color_name}")
    line = tuple(tuple(token for token in _rename_line_tokens(text, owner, own_material) if token not in parts)
                 for text, owner in ((prefix, manufacturer), (suffix, "")))
    return {**{field: value for field, value in base.items() if field != "material"},
            "material": material, "line": line}


def check_reclassification(old_key, new_key):
    """Raise ValueError unless ``new_key`` is ``old_key`` under a refined material code."""
    old_material, new_material = old_key.split("::")[4], new_key.split("::")[4]
    if not refines_material(old_material, new_material):
        raise ValueError(f"{new_material} does not refine {old_material}")
    if reclassification_identity(old_key, new_material) != reclassification_identity(new_key, new_material):
        raise ValueError("physical color/line or package identity differs")


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
