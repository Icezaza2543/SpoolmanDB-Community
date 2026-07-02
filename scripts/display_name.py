"""Display-name helpers for validation and quality reporting."""

from __future__ import annotations

import json
import re
from pathlib import Path


def material_appears_in_name(name: str, material: str) -> bool:
    """Return True when the material code already appears as its own token in the name."""
    if not name or not material:
        return False

    pattern = r"(?<![A-Z0-9])" + re.escape(material.upper()) + r"(?![A-Z0-9])"
    return bool(re.search(pattern, name.upper()))


def get_display_name(name: str, material: str) -> str:
    """Compose the Explorer-facing display name without mutating compiled data."""
    if not name:
        return name
    if not material or material_appears_in_name(name, material):
        return name
    return f"{material} {name}"


def collect_ambiguous_display_name_warnings(
    filaments_dir: Path,
    *,
    sample_color_name: str = "BLACK",
) -> list[str]:
    """Return warning messages for source templates that need material prefixing in Explorer."""
    warnings: list[str] = []

    for file in sorted(filaments_dir.glob("*.json")):
        with file.open(encoding="utf-8") as handle:
            data = json.load(handle)

        manufacturer = data["manufacturer"]
        for filament in data["filaments"]:
            name_template = filament["name"]
            material = filament["material"]

            try:
                compiled_name = name_template.format(color_name=sample_color_name)
            except (KeyError, ValueError):
                continue

            if material_appears_in_name(compiled_name, material):
                continue

            display_name = get_display_name(compiled_name, material)
            warnings.append(
                f'WARN display-name: {manufacturer} / {material} / "{name_template}" '
                f'compiles to "{compiled_name}"; Explorer will display "{display_name}".'
            )

    return warnings