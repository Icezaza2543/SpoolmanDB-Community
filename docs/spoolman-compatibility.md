# Spoolman compatibility CI

This repository validates compiled filament data against Spoolman's
`ExternalFilament` model without executing upstream Python.

## Single pin configuration

**All stable version/commit values live only in**
[`contracts/spoolman_upstream.json`](../contracts/spoolman_upstream.json).
Do not hardcode Spoolman SHAs or release tags in workflows, tests, scripts, or
docs. Read the pin from that file (or via `scripts/check_spoolman_compat.py`).

| Key | Purpose |
| --- | --- |
| `stable.version` | Human-readable Spoolman release tag |
| `stable.commit` | Full git SHA of the required compatibility contract |
| `canary.ref` | Branch/ref for advisory drift detection (default `master`) |
| `local_snapshot` | Offline reviewed AST snapshot used by stable CI |
| `repository` / `contract_path` | Source of `externaldb.py` on GitHub |

## Modes

### Stable (required, merge-blocking, offline)

```bash
python scripts/check_spoolman_compat.py --mode stable
```

- Uses the local snapshot path from the config (`local_snapshot`).
- No network access; same inputs always produce the same result.
- Validates every compiled record and the compiled schema enum against the pin.
- Runs in the required `compile` job of `.github/workflows/build.yml`.
- Failure **blocks merge**.

Current pin values: see [`contracts/spoolman_upstream.json`](../contracts/spoolman_upstream.json).

### Canary (advisory, non-blocking)

```bash
python scripts/check_spoolman_compat.py --mode canary
```

- Fetches the canary ref from config (default `Donkie/Spoolman:master`).
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

### Pin integrity (weekly / explicit only)

```bash
python scripts/check_spoolman_compat.py --mode verify-pin
```

- Fetches `stable_url` derived from `contracts/spoolman_upstream.json`
  (`repository` + `stable.commit` + `contract_path`).
- Parses remote source **AST-only** (never executed).
- Asserts `ExternalFilament` fields, types, requiredness, and related enums
  equal the local stable snapshot.
- Used by the weekly [Spoolman compatibility workflow](../.github/workflows/spoolman-compatibility.yml)
  and manual `workflow_dispatch` — **not** by normal PR build stable checks.
- Failure means the local snapshot is out of sync with the configured commit.

## Determinism proof

Stable mode resolves the contract solely from the local snapshot path recorded in
`spoolman_upstream.json`. Unit tests assert:

1. Two successive stable resolutions return identical source bytes and labels.
2. Labels include the version/commit **loaded from the config file**.
3. Stable CLI mode never calls the network fetcher.

## Drift detection proof

Canary mode loads the stable snapshot and the master source, then runs
`compare_external_filament_fields`. Unit tests inject synthetic type/field/enum
changes and assert the report names each changed field and kind
(`added` / `removed` / `type_changed` / `required_changed`).

## Pin integrity proof

`verify-pin` loads remote source for the configured stable commit and compares it
to the local snapshot. Unit tests mock the fetcher to prove match and mismatch
paths without scattering pin SHAs in the test module.

## Updating the pin

1. Edit `stable.version` and `stable.commit` in `contracts/spoolman_upstream.json`
   only.
2. Refresh `contracts/spoolman_externaldb.py` from that commit's `externaldb.py`
   (reviewed AST-only extract of enums + `ExternalFilament` + `ExternalFilamentsFile`).
3. Run `python scripts/check_spoolman_compat.py --mode stable` (offline).
4. Run `python scripts/check_spoolman_compat.py --mode verify-pin` (network).
5. Treat pin bumps as explicit contract changes, not as part of routine data PRs.
