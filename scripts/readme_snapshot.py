import argparse
import difflib
import json
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.compile_filaments import get_filaments_from_data


SNAPSHOT_START = "<!-- readme-snapshot:start -->"
SNAPSHOT_END = "<!-- readme-snapshot:end -->"

# Curated brand-location registry. Never infer it from country_of_origin, which
# records manufacturing origin and can differ from the manufacturer's location.
ASEAN_MANUFACTURERS_PATH = Path("scripts") / "asean_manufacturers.json"
SPOOL_TYPES = (
    "plastic",
    "cardboard",
    "metal",
    "refill",
    "unknow",
    "null",
    "omitted",
)


class SnapshotError(RuntimeError):
    pass


@dataclass(frozen=True)
class Snapshot:
    manufacturer_files: int
    material_definitions: int
    source_filaments: int
    color_entries: int
    compiled_variants: int
    country_of_origin: int
    tds_links: int
    sds_links: int
    product_codes: int
    ean_gtins: int
    asean_manufacturers: int
    asean_filaments: int
    effective_refills: int
    spool_counts: dict[str, int]


def load_json(path: Path):
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def collect_snapshot(
    root: Path = ROOT,
    *,
    asean_manufacturer_files: Iterable[str] | None = None,
) -> Snapshot:
    filament_files = sorted((root / "filaments").glob("*.json"))
    materials = load_json(root / "materials.json")
    if asean_manufacturer_files is None:
        asean_manufacturer_files = load_json(root / ASEAN_MANUFACTURERS_PATH)
    asean_files = tuple(asean_manufacturer_files)
    if len(asean_files) != len(set(asean_files)):
        raise SnapshotError("ASEAN manufacturer file list contains duplicates.")
    source_by_filename: dict[str, list[dict]] = {}

    source_filaments = 0
    color_entries = 0
    compiled_variants = 0
    country_of_origin = 0
    tds_links = 0
    sds_links = 0
    product_codes = 0
    ean_gtins = 0
    effective_refills = 0
    spool_counts: Counter[str] = Counter()

    for path in filament_files:
        data = load_json(path)
        filaments = data["filaments"]
        source_by_filename[path.name] = filaments
        source_filaments += len(filaments)
        compiled_variants += sum(1 for _ in get_filaments_from_data(data))

        for filament in filaments:
            colors = filament["colors"]
            color_entries += len(colors)
            country_of_origin += bool(filament.get("country_of_origin"))
            tds_links += bool(filament.get("tds_url"))
            sds_links += bool(filament.get("sds_url"))

            for weight in filament["weights"]:
                if (
                    weight.get("is_refill") is True
                    or weight.get("spool_type") == "refill"
                ):
                    effective_refills += 1
                if "spool_type" not in weight:
                    spool_type = "omitted"
                elif weight["spool_type"] is None:
                    spool_type = "null"
                else:
                    spool_type = weight["spool_type"]
                spool_counts[spool_type] += 1

            for color in colors:
                product_codes += len(color.get("codes") or ())
                ean_gtins += len(color.get("eans") or ())
                ean_gtins += len(color.get("eans_refill") or ())

    missing_asean_files = sorted(set(asean_files) - source_by_filename.keys())
    if missing_asean_files:
        names = ", ".join(missing_asean_files)
        raise SnapshotError(f"ASEAN manufacturer files are missing: {names}")

    unexpected_spool_types = sorted(set(spool_counts) - set(SPOOL_TYPES))
    if unexpected_spool_types:
        names = ", ".join(unexpected_spool_types)
        raise SnapshotError(f"README has no spool rows for: {names}")

    return Snapshot(
        manufacturer_files=len(filament_files),
        material_definitions=len(materials),
        source_filaments=source_filaments,
        color_entries=color_entries,
        compiled_variants=compiled_variants,
        country_of_origin=country_of_origin,
        tds_links=tds_links,
        sds_links=sds_links,
        product_codes=product_codes,
        ean_gtins=ean_gtins,
        asean_manufacturers=len(asean_files),
        asean_filaments=sum(
            len(source_by_filename[filename]) for filename in asean_files
        ),
        effective_refills=effective_refills,
        spool_counts={name: spool_counts[name] for name in SPOOL_TYPES},
    )


def format_count(value: int) -> str:
    return f"{value:,}"


def render_snapshot(snapshot: Snapshot) -> str:
    lines = [
        "| Source | Count |",
        "| --- | ---: |",
        f"| Manufacturer source files | {format_count(snapshot.manufacturer_files)} |",
        f"| Material definitions | {format_count(snapshot.material_definitions)} |",
        f"| Source filament objects | {format_count(snapshot.source_filaments)} |",
        f"| Color entries | {format_count(snapshot.color_entries)} |",
        f"| Compiled filament variants | {format_count(snapshot.compiled_variants)} |",
        (
            "| Source filaments with country of origin | "
            f"{format_count(snapshot.country_of_origin)} |"
        ),
        (
            "| Source filaments with TDS/product links | "
            f"{format_count(snapshot.tds_links)} |"
        ),
        f"| Source filaments with SDS links | {format_count(snapshot.sds_links)} |",
        (
            "| Manufacturer product code/ID entries | "
            f"{format_count(snapshot.product_codes)} |"
        ),
        f"| EAN/GTIN entries | {format_count(snapshot.ean_gtins)} |",
        (
            "| ASEAN manufacturer coverage | "
            f"{format_count(snapshot.asean_manufacturers)} brands / "
            f"{format_count(snapshot.asean_filaments)} source filaments |"
        ),
        "",
        (
            "Counts in this block are generated from the current repository state. "
            "Run `python scripts/readme_snapshot.py --write` after source-data changes. "
            "The compiled variant count expands source data across color, diameter, "
            "weight, and spool combinations."
        ),
        "",
        "### Spool metadata snapshot",
        "",
        "| Source weight metadata | Entries |",
        "| --- | ---: |",
    ]
    for spool_type in SPOOL_TYPES:
        if spool_type == "omitted":
            label = "`spool_type` omitted"
        elif spool_type in {"refill", "unknow"}:
            label = f"`spool_type: {spool_type}` (legacy)"
        else:
            label = f"`spool_type: {spool_type}`"
        lines.append(
            f"| {label} | {format_count(snapshot.spool_counts[spool_type])} |"
        )
    lines.append(
        "| Effective refill (`is_refill: true` or legacy `spool_type: refill`) | "
        f"{format_count(snapshot.effective_refills)} |"
    )
    return "\n".join(lines)


def replace_snapshot_block(readme: str, rendered_snapshot: str) -> str:
    if readme.count(SNAPSHOT_START) != 1 or readme.count(SNAPSHOT_END) != 1:
        raise SnapshotError(
            "README must contain exactly one readme-snapshot start/end marker pair."
        )

    start = readme.index(SNAPSHOT_START) + len(SNAPSHOT_START)
    end = readme.index(SNAPSHOT_END, start)
    if readme.startswith("\r\n", start):
        newline = "\r\n"
    elif readme.startswith("\n", start):
        newline = "\n"
    elif readme.startswith("\r", start):
        newline = "\r"
    else:
        raise SnapshotError("README snapshot start marker must end its line.")
    rendered = rendered_snapshot.replace("\n", newline)
    return readme[:start] + newline + rendered + newline + readme[end:]


def read_text(path: Path) -> str:
    with path.open(encoding="utf-8", newline="") as file:
        return file.read()


def write_text(path: Path, content: str) -> None:
    with path.open("w", encoding="utf-8", newline="") as file:
        file.write(content)


def normalize_newlines(content: str) -> str:
    return content.replace("\r\n", "\n").replace("\r", "\n")


def snapshot_is_current(current: str, expected: str) -> bool:
    return normalize_newlines(current) == normalize_newlines(expected)


def expected_readme(root: Path = ROOT) -> tuple[str, str]:
    readme_path = root / "README.md"
    current = read_text(readme_path)
    expected = replace_snapshot_block(current, render_snapshot(collect_snapshot(root)))
    return current, expected


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check or refresh generated README repository metrics."
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--check",
        action="store_true",
        help="Fail if the generated README snapshot is stale (default).",
    )
    mode.add_argument(
        "--write",
        action="store_true",
        help="Replace the generated README snapshot with current metrics.",
    )
    args = parser.parse_args()

    try:
        current, expected = expected_readme()
    except (OSError, KeyError, TypeError, ValueError, SnapshotError) as error:
        print(f"ERROR: Unable to generate README snapshot: {error}")
        return 1

    if snapshot_is_current(current, expected):
        print("✓ README snapshot is current.")
        return 0

    if args.write:
        write_text(ROOT / "README.md", expected)
        print("✓ README snapshot updated.")
        return 0

    print("ERROR: README snapshot is stale.")
    print("Run: python scripts/readme_snapshot.py --write")
    current_normalized = normalize_newlines(current)
    expected_normalized = normalize_newlines(expected)
    sys.stdout.writelines(
        difflib.unified_diff(
            current_normalized.splitlines(keepends=True),
            expected_normalized.splitlines(keepends=True),
            fromfile="README.md",
            tofile="README.md (expected)",
        )
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
