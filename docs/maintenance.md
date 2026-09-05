# SpoolmanDB-Community Maintenance Guide

Use this guide for evidence-backed maintenance. The JSON schemas and compiler are authoritative; the Explorer's relationship diagram is conceptual, not a physical database schema.

## 1. Adding a Manufacturer or Filament Family

1. Create or edit a JSON profile under `filaments/<manufacturer_slug>.json`.
2. Match existing casing and schema definitions in `filaments.schema.json`.
3. A manufacturer source file has exactly the top-level fields `manufacturer` (string) and `filaments` (array). Do not add top-level `name` or `url`; the source schema rejects unsupported properties.

## 2. Required Fields

Each source filament definition requires:

- `name`: Product-name template, usually containing `{color_name}`.
- `material`: Material code with a matching entry in `materials.json`.
- `density`: Positive number in g/cm³, supported by evidence.
- `weights`: Array of objects containing `weight` in grams and optional packaging metadata.
- `diameters`: Array of positive numbers in mm.
- `colors`: Array of color objects using either `hex` or `hexes` as required by the schema. Hex strings contain 6 or 8 hexadecimal characters without `#`; use verified named colors for new catalog entries.

The compiler expands the explicitly defined weight × diameter × color combinations into a flat `filaments.json` array. Compiled records use singular `weight` and `diameter`, `color_hex` or `color_hexes`, and an opaque `id`. These are not the source field names. Do not edit or commit generated `filaments.json`.

See [the source schema](../filaments.schema.json), [the compiled schema](../filaments.compiled.schema.json), and [the contributor guide](../CONTRIBUTING.md).

## 3. Evidence Policy

- Use verifiable manufacturer evidence or explicitly user-approved data: exact product pages, TDS/SDS documents, or label evidence.
- Do not infer, guess, or create unverified speculative variants.
- Do not infer colors, weights, diameters, spool material, tare or identifiers from another family.
- Missing optional metadata is preferable to an unsupported value. Numeric fields cannot faithfully represent qualitative statements such as “room temperature”; do not encode that as 0°C.

## 4. Public-ID Immutability Rule

`scripts/compile_filaments.py::generate_id` derives IDs from manufacturer, material, the expanded source name, weight, diameter and the packaging suffix. Color HEX values are **not** part of the ID. The compiler applies its own normalization; do not construct replacement IDs by hand.

Historical public IDs and their enrolled identity keys in `contracts/compiled_id_baseline.json` must not change, disappear or be rekeyed. New identities are allowed only for verified additions. Metadata corrections must preserve identity. Do not use a breaking-baseline override to deliver ordinary maintenance.

Record the starting main SHA before editing. Compare the final manifest against that immutable starting SHA, not only against a baseline file edited in the same change. Replace `STARTING_MAIN_SHA` in the validation command below with the recorded commit. Require zero historical changed, removed or rekeyed identities, and inspect every new ID and baseline addition.

## 5. Spool/Refill & Package-Matrix Rules

Packaging belongs inside each source `weights` object:

- New physical spool types: `plastic`, `cardboard`, `metal`, or omitted/null when unknown.
- New spoolless products: `is_refill: true`; do not introduce new legacy `spool_type: "refill"` values.
- Source `refill` and `unknow` spellings remain accepted for historical compatibility. Published `spool_type` is only `plastic`, `cardboard`, `metal`, or null; refill status is separately emitted as `is_refill`.
- `legacy_id_spool_type` is source-only. It can preserve an old spool suffix in some corrections, but it does not automatically make a refill-status change ID-neutral: refill semantics take precedence in ID generation. Verify the complete baseline before considering such a correction safe.
- `spool_weight` is tare, not shipping weight or filament net mass. Preserve unknown values rather than guessing.
- Split definitions whenever available combinations differ. Every generated combination must correspond to an evidenced physical variant.

## 6. SKU / EAN Binding Rule

`codes`, `eans` and `eans_refill` are arrays on individual source color objects. The compiler carries those arrays to every weight/diameter combination generated for that color; array positions do **not** bind identifiers to different package variants.

Only add exact manufacturer or explicitly approved identifiers. Separate definitions when package-specific bindings differ, or retain the gap in the backlog if the current model cannot express it safely. Identifier enrichment must not alter public IDs.

## 7. Validation Commands

For verified new identities only, run enrollment and inspect the baseline diff. Skip this step for metadata, frontend or documentation-only changes:

```bash
python scripts/compile_id_baseline.py --update
git diff -- contracts/compiled_id_baseline.json
```

The diff must contain only the intended additions and the corresponding count change; never rewrite historical entries. Then run the full local validation suite prior to commit:

```bash
python scripts/readme_snapshot.py --write
python scripts/readme_snapshot.py --check
python scripts/compile_filaments.py
python scripts/validate.py --strict
python -m pytest -q
node tests/test_display_name.cjs
python scripts/check_spoolman_compat.py --mode stable
python scripts/check_spoolman_compat.py --mode canary
python scripts/project_spoolman.py
python scripts/compile_id_baseline.py --strict --base-ref STARTING_MAIN_SHA
git diff --check
git status --short
```

Stable is required; canary is advisory in hosted CI, so inspect its actual drift/failure output rather than assuming a green overall run means no drift. Frontend changes also require live-browser checks of affected routes and a check that deployed assets/data match the delivered commit.

## 8. Delivery Procedure

External contributors should follow [CONTRIBUTING.md](../CONTRIBUTING.md) and open a focused PR. The owner's explicitly authorized no-PR maintenance workflow is separate:

1. Start from clean, current main and record its SHA; create a local-only scratch branch.
2. Audit first, make only accepted changes, and pass all applicable gates.
3. Create one focused final commit, fast-forward local main, and push main once. Do not push a remote feature branch or open a fallback PR.
4. If branch protection blocks the push, stop without bypassing it or force-pushing.
5. Wait for Build, compatibility, security and deployment checks. Verify published data and any affected UI.
6. If the delivered change breaks CI, inspect the failure and use a normal revert commit when necessary; never rewrite main history.
7. Delete only the delivered local scratch branch after successful verification, and confirm clean main matches origin/main.

## 9. Backlog Reopening Conditions

Keep unresolved evidence, identity and schema items in [the coverage backlog](coverage-backlog.md). Reopen an item when new official/user-approved evidence or explicit schema authorization addresses its blocker. Maintenance Mode does not mean that every current product worldwide has been audited or represented.
