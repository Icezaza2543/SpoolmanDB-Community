# SpoolmanDB-Community Maintenance Guide

This document defines standard procedures for maintaining the SpoolmanDB-Community database in Maintenance Mode.

## 1. Adding a Manufacturer or Filament Family

1. Create or edit a JSON profile under `filaments/<manufacturer_slug>.json`.
2. Match existing casing and schema definitions in `filaments.schema.json`.
3. If introducing a new manufacturer, add standard metadata (`name`, `url`) to `filaments/<manufacturer_slug>.json`.

## 2. Required Fields

Every source filament entry must contain:
- `name`: Model/family name (string).
- `material`: Valid material key present in `materials.json`.
- `density`: Positive float in g/cm³.
- `diameter`: Positive float in mm (typically `1.75` or `2.85`).
- `weight`: Net weight in grams (positive integer).
- `color_hex` or `color_hexes`: Valid 6-character hex code(s).

## 3. Evidence Policy

- All additions and modifications require user-approved, verifiable manufacturer evidence (TDS, SDS, official store specs, EAN label scans).
- Do not infer, guess, or create unverified speculative variants.

## 4. Public-ID Immutability Rule

- Historical published public IDs (`<manufacturer_slug>_<material>_<name_slug>_<hex>...`) are strictly immutable.
- Rekeying, renaming, or deleting existing public IDs is forbidden.
- The baseline gate `python scripts/compile_id_baseline.py` enforces zero historical modifications.

## 5. Spool/Refill & Package-Matrix Rules

- `spool_type`: Must be `plastic`, `cardboard`, `metal`, or `null`.
- Refills: Set `is_refill: true` (or legacy `spool_type: refill`).
- Packaging matrices must expand explicitly per physical SKU to avoid Cartesian explosion or invalid combinations.

## 6. SKU / EAN Binding Rule

- `codes` (SKU/Article numbers) and `eans` (GTIN/EAN barcodes) must map strictly to verified physical packages.
- Array order must align with exact color/variant indices if array-mapped.

## 7. Validation Commands

Run the full local validation suite prior to commit:

```bash
python scripts/readme_snapshot.py --write
python scripts/readme_snapshot.py --check
python scripts/compile_filaments.py
python scripts/validate.py --strict
python -m pytest -q --basetemp=./.pytest_temp
python scripts/check_spoolman_compat.py --mode stable
python scripts/check_spoolman_compat.py --mode canary
python scripts/project_spoolman.py
python scripts/compile_id_baseline.py
git diff --check
git status
```

## 8. Delivery Procedure

- Always create exactly one clean commit per maintenance task.
- Target branch: `main`.
- Rebase cleanly on `origin/main` before pushing.
- Push directly to `main` exactly once and wait for CI/CD checks.

## 9. Backlog Reopening Conditions

- Items documented in `docs/coverage-backlog.md` remain frozen.
- Backlog items reopen only when new user-approved official evidence or explicit schema updates are authorized.
