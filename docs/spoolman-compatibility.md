# Spoolman compatibility CI

This repository validates compiled filament data against Spoolman's
`ExternalFilament` model without executing upstream Python.

## Single pin configuration

All upstream refs live in [`contracts/spoolman_upstream.json`](../contracts/spoolman_upstream.json):

| Key | Purpose |
| --- | --- |
| `stable.version` | Human-readable Spoolman release (e.g. `v0.25.0`) |
| `stable.commit` | Full git SHA of the required compatibility contract |
| `canary.ref` | Branch/ref for advisory drift detection (default `master`) |
| `local_snapshot` | Offline reviewed AST snapshot used by stable CI |
| `repository` / `contract_path` | Source of `externaldb.py` on GitHub |

Do not scatter Spoolman SHAs in workflows or scripts. Read the pin from this file
(or via `scripts/check_spoolman_compat.py`, which loads it).

## Modes

### Stable (required, merge-blocking)

```bash
python scripts/check_spoolman_compat.py --mode stable
```

- Uses the local snapshot at `contracts/spoolman_externaldb.py`.
- No network access; same inputs always produce the same result.
- Validates every compiled record and the compiled schema enum against the pin.
- Runs in the required `compile` job of `.github/workflows/build.yml`.
- Failure **blocks merge**.

Current pin: **Spoolman v0.25.0** /
`6e1065009c7c45c9e38d5e1bec21d47273442889`.

### Canary (advisory, non-blocking)

```bash
python scripts/check_spoolman_compat.py --mode canary
```

- Fetches `https://raw.githubusercontent.com/Donkie/Spoolman/master/spoolman/externaldb.py`
  (ref from config).
- Validates compiled data against master when not using `--diff-only`.
- Compares `ExternalFilament` field names, type annotations, requiredness, and
  related enum members to the stable pin.
- Prints an exact drift list, for example:

  ```text
  ~ density: type float -> int
  + is_refill: bool | None (optional) (present on canary only)
  - weight: float (required) (present on stable only)
  ```

- Exit code `2` when field/type drift is detected; other failures use `1`.
- CI runs this with `continue-on-error: true` and never gates data PRs on canary.

```bash
# Field/type report only (no filaments.json required):
python scripts/check_spoolman_compat.py --mode canary --diff-only
```

## Determinism proof

Stable mode resolves the contract solely from the local snapshot path recorded in
`spoolman_upstream.json`. Unit tests assert:

1. Two successive stable resolutions return identical source bytes and labels.
2. The configured commit is always `6e1065009c7c45c9e38d5e1bec21d47273442889`.
3. Stable CLI mode never calls the network fetcher.

## Drift detection proof

Canary mode loads the stable snapshot and the master source, then runs
`compare_external_filament_fields`. Unit tests inject synthetic type/field/enum
changes and assert the report names each changed field and kind
(`added` / `removed` / `type_changed` / `required_changed`).

## Updating the pin

1. Edit `stable.version` and `stable.commit` in `contracts/spoolman_upstream.json`.
2. Refresh `contracts/spoolman_externaldb.py` from that commit's `externaldb.py`
   (reviewed AST-only extract of enums + `ExternalFilament` + `ExternalFilamentsFile`).
3. Run `python scripts/check_spoolman_compat.py --mode stable` and the test suite.
4. Treat pin bumps as explicit contract changes, not as part of routine data PRs.
