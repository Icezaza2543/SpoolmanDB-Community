"""Semantic data integrity checks for SpoolmanDB Community source files."""

json_module = None
import json
from pathlib import Path
from typing import Dict, List, Tuple


def validate_gtin_checksum(gtin_str: str) -> bool:
    """Validate GTIN Mod-10 checksum for 8, 12, 13, or 14 digit strings."""
    if not isinstance(gtin_str, str) or not gtin_str.isdigit():
        return False
    if len(gtin_str) not in (8, 12, 13, 14):
        return False
    digits = [int(c) for c in gtin_str]
    check_digit = digits[-1]
    payload = digits[:-1]
    payload.reverse()
    total = sum(d * (3 if i % 2 == 0 else 1) for i, d in enumerate(payload))
    calculated = (10 - (total % 10)) % 10
    return check_digit == calculated


def check_source_data_semantics(
    filaments_dir: Path, materials_path: Path
) -> Tuple[List[str], List[str]]:
    """Perform semantic validation on source filament JSON files.

    Returns:
        (errors, warnings): Tuple of error message strings and warning message strings.
    """
    errors: List[str] = []
    warnings: List[str] = []

    try:
        with materials_path.open(encoding="utf-8") as f:
            materials_data = json.load(f)
        valid_materials = {m["material"] for m in materials_data if "material" in m}
    except Exception as exc:
        errors.append(f"Failed to load materials from {materials_path}: {exc}")
        return errors, warnings

    mfr_to_file: Dict[str, str] = {}
    gtin_locations: Dict[str, List[Tuple[str, str, str, str, str]]] = {}

    for fpath in sorted(filaments_dir.glob("*.json")):
        fname = fpath.name
        try:
            with fpath.open(encoding="utf-8") as f:
                data = json.load(f)
        except Exception as exc:
            errors.append(f"Failed to parse JSON in {fname}: {exc}")
            continue

        mfr = data.get("manufacturer", "")
        if not mfr:
            errors.append(f"{fname}: missing top-level 'manufacturer'")
            continue

        mfr_lower = mfr.lower()
        if mfr_lower in mfr_to_file:
            other_file = mfr_to_file[mfr_lower]
            errors.append(
                f"Duplicate manufacturer '{mfr}' (case-insensitive) found in '{other_file}' and '{fname}'"
            )
        else:
            mfr_to_file[mfr_lower] = fname

        filaments = data.get("filaments", [])
        for fil in filaments:
            fil_name = fil.get("name", "<unnamed>")

            mat = fil.get("material")
            if mat and mat not in valid_materials:
                errors.append(
                    f"{fname}: manufacturer '{mfr}', filament '{fil_name}' references unknown material '{mat}'"
                )

            for temp_field in ("extruder_temp_range", "bed_temp_range"):
                trange = fil.get(temp_field)
                if trange and isinstance(trange, list) and len(trange) == 2:
                    if trange[0] > trange[1]:
                        errors.append(
                            f"{fname}: manufacturer '{mfr}', filament '{fil_name}' has invalid {temp_field} [{trange[0]}, {trange[1]}]: min > max"
                        )

            for c in fil.get("colors", []) or []:
                color_name = c.get("name", "<unnamed>")
                for field in ("eans", "eans_refill"):
                    for gtin in c.get(field, []) or []:
                        loc = (fname, mfr, fil_name, color_name, field)
                        if gtin not in gtin_locations:
                            gtin_locations[gtin] = []
                        gtin_locations[gtin].append(loc)

                        if len(gtin) not in (8, 12, 13, 14):
                            errors.append(
                                f"Invalid GTIN length ({len(gtin)}) for '{gtin}': manufacturer '{mfr}', filament '{fil_name}', color '{color_name}', field '{field}'"
                            )
                        elif not validate_gtin_checksum(gtin):
                            errors.append(
                                f"Invalid GTIN Mod-10 checksum for '{gtin}': manufacturer '{mfr}', filament '{fil_name}', color '{color_name}', field '{field}'"
                            )

    for gtin, locs in sorted(gtin_locations.items()):
        if len(locs) > 1:
            loc_descs = [f"'{l[0]}' ({l[1]} / {l[2]} / {l[3]} / {l[4]})" for l in locs]
            warnings.append(
                f"Duplicate GTIN '{gtin}' found in {len(locs)} places: {', '.join(loc_descs)}"
            )

    return errors, warnings
