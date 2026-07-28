import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft7Validator

from scripts.check_spoolman_compat import (
    compare_external_filament_fields,
    load_spoolman_contract,
    load_stable_contract,
    load_upstream_config,
    main,
    resolve_contract_source,
    validate_compiled_data,
    validate_schema_spool_types,
    verify_pin_integrity,
)

ROOT = Path(__file__).parent.parent
UPSTREAM_CONFIG = ROOT / "contracts" / "spoolman_upstream.json"
# Version/commit come only from contracts/spoolman_upstream.json (no hardcoded pin).
_UPSTREAM = load_upstream_config(UPSTREAM_CONFIG)
STABLE_SNAPSHOT = _UPSTREAM.local_snapshot


UPSTREAM_MODEL = """
from collections.abc import Iterator
from enum import Enum
from pydantic import BaseModel, Field, RootModel

class SpoolType(Enum):
    PLASTIC = "plastic"
    CARDBOARD = "cardboard"
    METAL = "metal"

class Finish(Enum):
    MATTE = "matte"
    GLOSSY = "glossy"

class MultiColorDirection(Enum):
    COAXIAL = "coaxial"
    LONGITUDINAL = "longitudinal"

class Pattern(Enum):
    MARBLE = "marble"
    SPARKLE = "sparkle"

class ExternalFilament(BaseModel):
    id: str = Field(description="id")
    manufacturer: str = Field(description="manufacturer")
    name: str = Field(description="name")
    material: str = Field(description="material")
    density: float = Field(description="density")
    weight: float = Field(description="weight")
    spool_weight: float | None = Field(default=None, description="spool weight")
    spool_type: SpoolType | None = Field(None, description="spool type")
    diameter: float = Field(description="diameter")
    color_hex: str | None = Field(default=None, description="color")
    color_hexes: list[str] | None = Field(default=None, description="colors")
    extruder_temp: int | None = Field(default=None, description="extruder")
    bed_temp: int | None = Field(default=None, description="bed")
    finish: Finish | None = Field(default=None, description="finish")
    multi_color_direction: MultiColorDirection | None = Field(default=None, description="direction")
    pattern: Pattern | None = Field(default=None, description="pattern")
    translucent: bool = Field(default=False, description="translucent")
    glow: bool = Field(default=False, description="glow")

class ExternalFilamentsFile(RootModel):
    root: list[ExternalFilament]

    def __iter__(self) -> Iterator[ExternalFilament]:
        return iter(self.root)
"""


def compiled_record(**overrides):
    record = {
        "id": "test_pla_black_1000_175_r",
        "manufacturer": "Test",
        "name": "Black",
        "material": "PLA",
        "density": 1.24,
        "weight": 1000,
        "spool_weight": None,
        "spool_type": None,
        "is_refill": True,
        "diameter": 1.75,
        "color_hex": "000000",
        "color_hexes": None,
        "extruder_temp": None,
        "bed_temp": None,
        "finish": None,
        "multi_color_direction": None,
        "pattern": None,
        "translucent": False,
        "glow": False,
        "codes": ["TEST-001"],
    }
    record.update(overrides)
    return record


def test_upstream_model_accepts_community_metadata_and_rejects_bad_spool_type():
    contract = load_spoolman_contract(UPSTREAM_MODEL)

    validate_compiled_data([compiled_record()], contract)

    with pytest.raises(RuntimeError, match="incompatible spool_type"):
        validate_compiled_data(
            [compiled_record(spool_type="refill")],
            contract,
        )

    without_required_id = compiled_record()
    del without_required_id["id"]
    with pytest.raises(RuntimeError, match="missing required field id"):
        validate_compiled_data([without_required_id], contract)


def test_upstream_source_is_parsed_without_execution():
    source_with_top_level_side_effect = (
        'raise RuntimeError("downloaded source was executed")\n' + UPSTREAM_MODEL
    )
    contract = load_spoolman_contract(source_with_top_level_side_effect)
    validate_compiled_data([compiled_record()], contract)

    source_with_model_config = UPSTREAM_MODEL.replace(
        "class ExternalFilament(BaseModel):",
        'class ExternalFilament(BaseModel):\n    model_config = {"extra": "forbid"}',
    )
    with pytest.raises(RuntimeError, match="manual review required"):
        load_spoolman_contract(source_with_model_config)

    source_with_constraint = UPSTREAM_MODEL.replace(
        'weight: float = Field(description="weight")',
        'weight: float = Field(description="weight", gt=0)',
    )
    with pytest.raises(RuntimeError, match="added validation options: gt"):
        load_spoolman_contract(source_with_constraint)

    source_with_dynamic_default = (
        "REQUIRED = ...\n"
        + UPSTREAM_MODEL.replace(
            'id: str = Field(description="id")',
            'id: str = Field(REQUIRED, description="id")',
        )
    )
    with pytest.raises(RuntimeError, match="dynamic default"):
        load_spoolman_contract(source_with_dynamic_default)


def test_compiled_schema_spool_values_must_be_upstream_compatible():
    contract = load_spoolman_contract(UPSTREAM_MODEL)
    schema = {
        "items": {
            "properties": {
                "spool_type": {
                    "enum": ["plastic", "cardboard", "metal", None]
                }
            }
        }
    }

    validate_schema_spool_types(schema, contract)

    incompatible = copy.deepcopy(schema)
    incompatible["items"]["properties"]["spool_type"]["enum"].append("refill")
    with pytest.raises(RuntimeError, match="rejected by Spoolman"):
        validate_schema_spool_types(incompatible, contract)

    non_nullable_source = UPSTREAM_MODEL.replace(
        "spool_type: SpoolType | None",
        "spool_type: SpoolType",
    )
    non_nullable_contract = load_spoolman_contract(non_nullable_source)
    with pytest.raises(RuntimeError, match="None"):
        validate_schema_spool_types(schema, non_nullable_contract)


def test_source_schema_enforces_refill_metadata_consistency():
    root = Path(__file__).parent.parent
    with (root / "filaments.schema.json").open(encoding="utf-8") as file:
        schema = json.load(file)

    weight_schema = schema["properties"]["filaments"]["items"]["properties"][
        "weights"
    ]["items"]
    validator = Draft7Validator(weight_schema)

    assert validator.is_valid({"weight": 1000, "is_refill": True})
    assert validator.is_valid({"weight": 1000, "spool_type": "refill"})
    assert not validator.is_valid(
        {"weight": 1000, "spool_type": "plastic", "is_refill": True}
    )
    assert not validator.is_valid(
        {"weight": 1000, "spool_type": "unknow", "is_refill": True}
    )
    assert not validator.is_valid(
        {"weight": 1000, "spool_type": "refill", "is_refill": False}
    )


def test_compiled_schema_enforces_refill_output_invariants():
    root = Path(__file__).parent.parent
    with (root / "filaments.compiled.schema.json").open(encoding="utf-8") as file:
        schema = json.load(file)

    validator = Draft7Validator(schema["items"])
    assert validator.is_valid(compiled_record())
    assert not validator.is_valid(compiled_record(spool_type="plastic"))
    assert not validator.is_valid(compiled_record(id="test_pla_black_1000_175_p"))
    assert not validator.is_valid(compiled_record(is_refill=False))

    missing_spool_type = compiled_record()
    del missing_spool_type["spool_type"]
    assert not validator.is_valid(missing_spool_type)


def test_upstream_config_is_sole_stable_pin_source():
    """Stable pin lives only in contracts/spoolman_upstream.json."""
    config = load_upstream_config(UPSTREAM_CONFIG)

    with UPSTREAM_CONFIG.open(encoding="utf-8") as file:
        raw = json.load(file)

    assert config.stable_version == raw["stable"]["version"]
    assert config.stable_commit == raw["stable"]["commit"]
    assert config.canary_ref == raw["canary"]["ref"]
    assert config.repository == raw["repository"]
    assert config.contract_path == raw["contract_path"]
    assert config.local_snapshot == (ROOT / raw["local_snapshot"]).resolve()
    assert config.stable_url.endswith(
        f"/{raw['stable']['commit']}/{raw['contract_path']}"
    )
    assert config.canary_url.endswith(
        f"/{raw['canary']['ref']}/{raw['contract_path']}"
    )
    # Structured pin fields must be non-empty and not redefined in this test module.
    assert config.stable_commit
    assert config.stable_version
    assert len(config.stable_commit) == 40


def test_stable_mode_is_deterministic_offline():
    """Pinned mode always resolves the same local snapshot and contract fields."""
    config = load_upstream_config(UPSTREAM_CONFIG)

    source_a, label_a, etag_a = resolve_contract_source(
        mode="stable",
        config=config,
        upstream_url=None,
        upstream_file=None,
    )
    source_b, label_b, etag_b = resolve_contract_source(
        mode="stable",
        config=config,
        upstream_url=None,
        upstream_file=None,
    )

    assert source_a == source_b == STABLE_SNAPSHOT.read_text(encoding="utf-8")
    assert etag_a is None and etag_b is None
    assert config.stable_commit in label_a
    assert config.stable_version in label_a
    assert label_a == label_b

    contract_a = load_spoolman_contract(source_a)
    contract_b = load_stable_contract(config)
    assert set(contract_a.fields) == set(contract_b.fields)
    assert {
        name: (ast_unparse(field.annotation), field.required)
        for name, field in contract_a.fields.items()
    } == {
        name: (ast_unparse(field.annotation), field.required)
        for name, field in contract_b.fields.items()
    }


def ast_unparse(node):
    import ast

    return ast.unparse(node)


def test_compare_external_filament_fields_reports_exact_drift():
    """Master/canary mode detects field and type drift vs the stable pin."""
    stable = load_spoolman_contract(UPSTREAM_MODEL)

    drifted_source = UPSTREAM_MODEL.replace(
        "    density: float = Field(description=\"density\")",
        "    density: int = Field(description=\"density\")",
    ).replace(
        "    glow: bool = Field(default=False, description=\"glow\")",
        "    glow: bool = Field(default=False, description=\"glow\")\n"
        "    is_refill: bool | None = Field(default=None, description=\"refill\")",
    ).replace(
        "    weight: float = Field(description=\"weight\")\n",
        "",
    ).replace(
        "    spool_weight: float | None = Field(default=None, description=\"spool weight\")",
        "    spool_weight: float = Field(description=\"spool weight\")",
    )
    canary = load_spoolman_contract(drifted_source)
    changes = compare_external_filament_fields(stable, canary)
    by_field = {(change.field, change.kind): change for change in changes}

    assert ("density", "type_changed") in by_field
    assert by_field[("density", "type_changed")].stable == "float"
    assert by_field[("density", "type_changed")].canary == "int"

    assert ("is_refill", "added") in by_field
    assert by_field[("is_refill", "added")].canary is not None
    assert "bool" in by_field[("is_refill", "added")].canary

    assert ("weight", "removed") in by_field
    assert by_field[("weight", "removed")].stable is not None

    assert ("spool_weight", "type_changed") in by_field
    assert by_field[("spool_weight", "type_changed")].stable == "float | None"
    assert by_field[("spool_weight", "type_changed")].canary == "float"

    assert ("spool_weight", "required_changed") in by_field
    assert by_field[("spool_weight", "required_changed")].stable == "optional"
    assert by_field[("spool_weight", "required_changed")].canary == "required"

    # Identical contracts produce no drift.
    assert compare_external_filament_fields(stable, stable) == []


def test_compare_reports_enum_member_drift():
    stable = load_spoolman_contract(UPSTREAM_MODEL)
    canary_source = UPSTREAM_MODEL.replace(
        'METAL = "metal"',
        'METAL = "metal"\n    WOOD = "wood"',
    )
    canary = load_spoolman_contract(canary_source)
    changes = compare_external_filament_fields(stable, canary)
    assert any(
        change.field == "enum:SpoolType"
        and change.kind == "added"
        and change.canary == "wood"
        for change in changes
    )


def test_cli_stable_mode_default_uses_pinned_snapshot(tmp_path, monkeypatch, capsys):
    """CLI stable mode is offline and deterministic (no network)."""
    config = load_upstream_config(UPSTREAM_CONFIG)
    compiled = tmp_path / "filaments.json"
    schema = ROOT / "filaments.compiled.schema.json"
    compiled.write_text(
        json.dumps([compiled_record()]),
        encoding="utf-8",
    )

    def fail_fetch(*_args, **_kwargs):
        raise AssertionError("stable mode must not fetch the network")

    monkeypatch.setattr(
        "scripts.check_spoolman_compat.fetch_upstream_source",
        fail_fetch,
    )

    exit_code = main(
        [
            "--mode",
            "stable",
            "--compiled",
            str(compiled),
            "--schema",
            str(schema),
            "--config",
            str(UPSTREAM_CONFIG),
        ]
    )
    captured = capsys.readouterr()
    assert exit_code == 0
    assert "STABLE" in captured.out
    assert config.stable_commit in captured.out
    assert config.stable_version in captured.out


def test_cli_canary_diff_only_detects_master_drift(tmp_path, monkeypatch, capsys):
    """Canary mode reports ExternalFilament drift and exits non-zero without failing data validation path when --diff-only."""
    config = load_upstream_config(UPSTREAM_CONFIG)
    stable_source = STABLE_SNAPSHOT.read_text(encoding="utf-8")
    drifted = stable_source.replace(
        "density: float = Field(description=\"Density in g/cm3.\")",
        "density: int = Field(description=\"Density in g/cm3.\")",
    )
    assert drifted != stable_source

    def fake_fetch(url, **_kwargs):
        assert config.canary_ref in url
        return drifted, '"etag-canary"'

    monkeypatch.setattr(
        "scripts.check_spoolman_compat.fetch_upstream_source",
        fake_fetch,
    )

    exit_code = main(
        [
            "--mode",
            "canary",
            "--diff-only",
            "--config",
            str(UPSTREAM_CONFIG),
        ]
    )
    captured = capsys.readouterr()
    assert exit_code == 2
    assert "CANARY DRIFT" in captured.err
    assert "density" in captured.err
    assert "float" in captured.err
    assert "int" in captured.err
    assert config.stable_commit in captured.out


def test_verify_pin_integrity_matches_when_remote_equals_local():
    """Pin integrity compares remote stable commit contract to local snapshot."""
    config = load_upstream_config(UPSTREAM_CONFIG)
    # Remote full upstream files may include extra modules; field contracts must match.
    remote = STABLE_SNAPSHOT.read_text(encoding="utf-8")
    changes, label, etag = verify_pin_integrity(config, remote_source=remote)
    assert changes == []
    assert label == config.stable_url
    assert etag is None


def test_verify_pin_integrity_detects_snapshot_drift():
    config = load_upstream_config(UPSTREAM_CONFIG)
    drifted = STABLE_SNAPSHOT.read_text(encoding="utf-8").replace(
        "density: float = Field(description=\"Density in g/cm3.\")",
        "density: int = Field(description=\"Density in g/cm3.\")",
    )
    changes, _label, _etag = verify_pin_integrity(config, remote_source=drifted)
    assert any(
        change.field == "density" and change.kind == "type_changed"
        for change in changes
    )


def test_cli_verify_pin_fetches_stable_url_only(monkeypatch, capsys):
    """verify-pin uses config stable_url; not used by offline stable PR CI."""
    config = load_upstream_config(UPSTREAM_CONFIG)
    calls: list[str] = []

    def fake_fetch(url, **_kwargs):
        calls.append(url)
        assert url == config.stable_url
        assert config.stable_commit in url
        return STABLE_SNAPSHOT.read_text(encoding="utf-8"), '"etag-pin"'

    monkeypatch.setattr(
        "scripts.check_spoolman_compat.fetch_upstream_source",
        fake_fetch,
    )

    exit_code = main(["--mode", "verify-pin", "--config", str(UPSTREAM_CONFIG)])
    captured = capsys.readouterr()
    assert exit_code == 0
    assert calls == [config.stable_url]
    assert "PIN INTEGRITY" in captured.out
    assert config.stable_commit in captured.out


def test_cli_verify_pin_fails_on_drift(monkeypatch, capsys):
    config = load_upstream_config(UPSTREAM_CONFIG)
    drifted = STABLE_SNAPSHOT.read_text(encoding="utf-8").replace(
        "density: float = Field(description=\"Density in g/cm3.\")",
        "density: int = Field(description=\"Density in g/cm3.\")",
    )

    monkeypatch.setattr(
        "scripts.check_spoolman_compat.fetch_upstream_source",
        lambda url, **_kwargs: (drifted, None),
    )

    exit_code = main(["--mode", "verify-pin", "--config", str(UPSTREAM_CONFIG)])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert "does not match" in captured.err
    assert "density" in captured.err
