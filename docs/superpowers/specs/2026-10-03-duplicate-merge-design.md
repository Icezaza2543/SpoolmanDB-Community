# Duplicate Filament Merge — Design

Date: 2026-10-03 · Related: fork issue #66 (Kingroon PETG duplicates)

## Problem

Commit `9b88f22` (2026-06-28, "enrich brand filament models and colors from Open Filament Database (OFD)") added families next to existing ones using a different naming style, without matching them. Result: the same physical product appears twice, e.g. Bambu Lab `Matte Lemon Yellow` / `PLA Matte Lemon Yellow`, Kingroon `Kingroon PETG Black` / `PETG Black`.

A scan of the compiled catalog (2026-10-03) found about 2,283 candidate groups across 72 brands, from 239 family pairings that involve 405 families. Merging them would retire about 2,300 records. Of these groups:

- 1,224 pair an upstream (Donkie/SpoolmanDB) family with a non-upstream one.
- 892 belong to brands that are not in upstream.
- 164 have no upstream side.

Many groups also have conflicting metadata.

The current contract forbids any public ID from disappearing (`docs/maintenance.md` §4), so duplicates cannot be merged today.

## Goals

- Merge true duplicates so each physical product has exactly one record.
- Do not add any new filament schema field.
- Record every retired ID and its replacement in an auditable, machine-readable way.
- Prevent new duplicates from entering the catalog.
- Define naming rules for future product lines (e.g. `PETG Basic`, `PETG 2.0`).

Out of scope: removing brand prefixes from names that are not part of a duplicate group (about 1,172 records).

## 1. Retired-ID registry

New contract file `contracts/retired_ids.json`:

```json
{
  "version": 1,
  "retired": {
    "<old_id>": { "replaced_by": "<new_id>", "reason": "duplicate", "ref": "#66" }
  }
}
```

`reason` is an enum that currently has one value, `duplicate`. `ref` is an issue or PR reference.

`scripts/compile_id_baseline.py --strict` enforces these rules:

1. A baseline ID may be missing from the current data only if it is listed in `retired`. Any other removal stays a breaking error.
2. `replaced_by` must exist in the current compiled data.
3. No chains. `replaced_by` must not itself be retired. When a target is retired, every entry pointing to it is re-pointed to the final target in the same PR.
4. A retired ID must never reappear in the compiled data.
5. The retired record and its replacement must match on manufacturer, material, weight, diameter, `spool_type` and `is_refill`. The checker reads these values from the base-ref compiled data.
6. Entries are append-only against `--base-ref`. Deleting or editing an entry is an error. The only exception is re-pointing `replaced_by` as required by rule 3.

`--update` drops retired keys from the baseline manifest without needing `--accept-breaking-baseline-changes`. Unregistered removals still require that flag.

The build workflow publishes `retired_ids.json` to GitHub Pages next to `filaments.json`. Spoolman ignores it, and other tools can use it to follow old IDs.

## 2. Duplicate definition and merge rules

**Duplicate candidate:** two compiled records that match on manufacturer, material, weight, diameter, `spool_type` and `is_refill`, and whose normalized names are equal. Name normalization:

- lowercase
- remove brackets and punctuation separators
- strip a leading manufacturer name
- remove the standalone material token
- treat `gray` and `grey` as the same word
- compare words as an unordered set

Line and version tokens stay significant: `+`, `plus`, `pro`, `basic`, `hs`/`high speed`, `rapid`, `matte`, `silk`, `cf`, `v2`/`2.0` and similar. So PLA vs PLA+ and PETG vs PETG Basic are never candidates.

Candidates are proposals. A human confirms each group in the brand PR.

**Survivor family:**

1. Prefer the family that exists in `upstream/main`.
2. If neither or both sides are in upstream, prefer the name without a manufacturer prefix.
3. Then prefer the name closest to the manufacturer's current product name.
4. If still tied, prefer the family with more records.

**Colors:** colors that exist only in the retired family move into the survivor family. Their IDs change, so they are also registered in `retired_ids.json`. Each product line ends with exactly one family.

**Metadata conflicts:**

1. Prefer the value from the manufacturer's current product page or TDS that can be found at merge time.
2. Otherwise, use the value added to the repo most recently, by git history.

Every conflict, the chosen value and its source (tier 1 or tier 2) are listed in the PR report. Values are never guessed.

**Future product lines** (documented in `docs/maintenance.md`):

- A new version or line (`PETG 2.0`, `PETG Basic`) is a separate family, named as the manufacturer names it, with no manufacturer prefix. The old family stays.
- A pure rename of the same product uses `display_name`, not a new family.
- Different lines are merged only with evidence (SKU, label or TDS). For example, Kingroon `PETG` vs `PETG Basic` stays unmerged until such evidence exists.

## 3. Tooling, CI guard and rollout

- `scripts/audit_duplicates.py` is read-only. It writes a per-brand JSON and Markdown report: candidate groups, upstream side, proposed survivor and metadata conflicts.
- `scripts/merge_duplicates.py --brand <slug> [--exclude <group>]` edits source files (removes duplicates, moves colors, applies metadata rules), appends to `retired_ids.json` and updates the baseline. Manufacturer-sourced values from tier 1 are edited by hand.
- `scripts/validate.py`: a PR that introduces a new duplicate group compared with `--base-ref` fails. Existing groups only produce warnings.
- Tests:
  - one test for each registry rule (1–6)
  - normalization does not merge different lines (PLA vs PLA+, PETG vs PETG Basic)
  - the merge script moves colors and writes the mapping correctly
  - the CI guard catches a new duplicate group
- Documentation: update `docs/maintenance.md` §4 and add the naming rules.

Rollout:

1. A tooling and docs PR with no data changes.
2. A Kingroon pilot PR that closes #66 with an explanation to the reporter.
3. Brand PRs in order of group count (Nebula, Protopasta, Bambu Lab, …). Each PR covers one large brand or several small ones.
