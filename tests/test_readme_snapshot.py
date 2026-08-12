import json
from pathlib import Path

import pytest

from scripts.readme_snapshot import (
    SNAPSHOT_END,
    SNAPSHOT_START,
    SnapshotError,
    collect_snapshot,
    expected_readme,
    render_snapshot,
    replace_published_records,
    replace_snapshot_block,
    snapshot_is_current,
)


ROOT = Path(__file__).resolve().parent.parent


def write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data), encoding="utf-8")


def test_collect_snapshot_counts_source_and_compiled_metrics(tmp_path):
    write_json(
        tmp_path / "materials.json",
        [{"material": "PLA"}, {"material": "PETG"}],
    )
    write_json(
        tmp_path / "filaments" / "asean.json",
        {
            "manufacturer": "ASEAN Brand",
            "filaments": [
                {
                    "name": "{color_name}",
                    "material": "PLA",
                    "density": 1.24,
                    "weights": [
                        {"weight": 1000, "spool_type": "plastic"},
                        {"weight": 500},
                        {"weight": 250, "spool_type": None},
                        {"weight": 100, "is_refill": True},
                        {"weight": 750, "spool_type": "refill"},
                    ],
                    "diameters": [1.75, 2.85],
                    "colors": [
                        {
                            "name": "Black",
                            "hex": "000000",
                            "codes": ["CODE-1", "PLATFORM-2"],
                            "eans": ["12345678"],
                            "eans_refill": ["1234567890123"],
                        },
                        {
                            "name": "White",
                            "hex": "FFFFFF",
                            "codes": ["CODE-3"],
                        },
                    ],
                    "country_of_origin": "CN",
                    "tds_url": "https://example.com/tds",
                    "sds_url": "https://example.com/sds",
                }
            ],
        },
    )
    write_json(
        tmp_path / "filaments" / "other.json",
        {
            "manufacturer": "Other Brand",
            "filaments": [
                {
                    "name": "{color_name}",
                    "material": "PETG",
                    "density": 1.27,
                    "weights": [
                        {"weight": 1000, "spool_type": "cardboard"},
                    ],
                    "diameters": [1.75],
                    "colors": [{"name": "Clear", "hex": "FFFFFF"}],
                    "country_of_origin": "MY",
                }
            ],
        },
    )

    snapshot = collect_snapshot(
        tmp_path,
        asean_manufacturer_files=("asean.json",),
    )

    assert snapshot.manufacturer_files == 2
    assert snapshot.material_definitions == 2
    assert snapshot.source_filaments == 2
    assert snapshot.color_entries == 3
    assert snapshot.compiled_variants == 21
    assert snapshot.country_of_origin == 2
    assert snapshot.tds_links == 1
    assert snapshot.sds_links == 1
    assert snapshot.product_codes == 3
    assert snapshot.ean_gtins == 2
    assert snapshot.asean_manufacturers == 1
    assert snapshot.asean_filaments == 1
    assert snapshot.effective_refills == 2
    assert snapshot.spool_counts == {
        "plastic": 1,
        "cardboard": 1,
        "metal": 0,
        "refill": 1,
        "unknow": 0,
        "null": 1,
        "omitted": 2,
    }


def test_replace_snapshot_block_preserves_crlf(tmp_path):
    write_json(tmp_path / "materials.json", [])
    write_json(
        tmp_path / "filaments" / "asean.json",
        {"manufacturer": "ASEAN Brand", "filaments": []},
    )
    snapshot = collect_snapshot(
        tmp_path,
        asean_manufacturer_files=("asean.json",),
    )
    readme = (
        "# Test\r\n\r\n"
        f"{SNAPSHOT_START}\r\nstale\r\n{SNAPSHOT_END}\r\n"
    )

    updated = replace_snapshot_block(readme, render_snapshot(snapshot))

    assert "stale" not in updated
    assert "| Manufacturer source files | 1 |" in updated
    assert "\n" not in updated.replace("\r\n", "")


def test_replace_snapshot_block_uses_marker_line_ending(tmp_path):
    write_json(tmp_path / "materials.json", [])
    write_json(
        tmp_path / "filaments" / "asean.json",
        {"manufacturer": "ASEAN Brand", "filaments": []},
    )
    snapshot = collect_snapshot(
        tmp_path,
        asean_manufacturer_files=("asean.json",),
    )
    readme = f"{SNAPSHOT_START}\nstale\n{SNAPSHOT_END}\nother\r\n"

    updated = replace_snapshot_block(readme, render_snapshot(snapshot))

    generated = updated.split(SNAPSHOT_END, maxsplit=1)[0]
    assert "\r" not in generated


def test_replace_published_records_preserves_line_ending():
    readme = "# Test\r\n\r\n* **Published records**: 12\r\n"

    updated = replace_published_records(readme, 12345)

    assert updated == "# Test\r\n\r\n* **Published records**: 12,345\r\n"


@pytest.mark.parametrize(
    "readme",
    (
        "# no published count\n",
        "* **Published records**: 1\n* **Published records**: 2\n",
    ),
)
def test_replace_published_records_requires_exactly_one_line(readme):
    with pytest.raises(SnapshotError, match="exactly one"):
        replace_published_records(readme, 1)


def test_collect_snapshot_rejects_duplicate_asean_files(tmp_path):
    write_json(tmp_path / "materials.json", [])
    write_json(
        tmp_path / "filaments" / "asean.json",
        {"manufacturer": "ASEAN Brand", "filaments": []},
    )

    with pytest.raises(SnapshotError, match="duplicates"):
        collect_snapshot(
            tmp_path,
            asean_manufacturer_files=("asean.json", "asean.json"),
        )


@pytest.mark.parametrize(
    "readme",
    (
        "# no markers\n",
        f"{SNAPSHOT_START}\nmissing end\n",
        f"{SNAPSHOT_START}\n{SNAPSHOT_START}\n{SNAPSHOT_END}\n",
    ),
)
def test_replace_snapshot_block_rejects_missing_or_duplicate_markers(readme):
    with pytest.raises(SnapshotError, match="exactly one"):
        replace_snapshot_block(readme, "generated")


def test_repository_readme_snapshot_is_current():
    current, expected = expected_readme(ROOT)
    assert snapshot_is_current(current, expected)
