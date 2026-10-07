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

Historical public IDs and their enrolled identity keys in `contracts/compiled_id_baseline.json` must not change, disappear or be rekeyed during ordinary maintenance. New identities are allowed only for verified additions. Metadata corrections must preserve identity. Do not use a breaking-baseline override to deliver ordinary maintenance.

The sole removal exception is an exact, owner-approved true-duplicate migration recorded in `contracts/retired_ids.json`, checked against a trusted starting commit and a reviewed brand audit. This is an **intentional breaking migration**: retired entries disappear from the published catalog. Existing Spoolman spools retain their local imported data; Spoolman does not consume the registry or redirect stored external IDs. Publish no separate compatibility catalog. The tooling commit starts with an empty registry and retires nothing.

Each registry entry stores `replaced_by`, `reason: "duplicate"`, `ref`, `source` (evidence URL or commit SHA), and `retired_key` (the byte-identical original baseline key). The replacement must already exist and match physical identity, including normalized ordered line and color tokens. No chains, cycles, invented historical IDs or Black-to-White mappings are allowed. Later target retirement must re-point existing entries to the final survivor without altering their original key/evidence.

Rollback permits **exact reinstatement only**: deleting a registry entry must restore its original ID under its byte-identical `retired_key` and re-enroll that mapping in the same commit. A different key, missing re-enrollment or registry deletion without reinstatement fails validation. Use normal commits/reverts, never history rewriting.

Record the starting main SHA before editing. Compare the final manifest against that immutable starting SHA, not only against a baseline file edited in the same change. Replace `STARTING_MAIN_SHA` in the validation command below with the recorded commit. Require zero historical changed, removed or rekeyed identities, and inspect every new ID and baseline addition.

For an approved duplicate migration, report the exact registered retirements separately; require zero **unregistered** removals, zero changed/rekeyed survivor or unique identities and zero new IDs. `--update --base-ref STARTING_MAIN_SHA` enrolls only the reviewed removals without a breaking override. Strict checking must still match the HEAD baseline exactly.

### Naming and production-lot evidence

- Keep distinct product versions/lines (`PETG 2.0`, `PETG Basic`, `Sunlu PETG v2`). Do not merge Kingroon PETG with PETG Basic without exact SKU/label evidence and owner approval.
- New families use the manufacturer's product name without a redundant manufacturer prefix. A pure rename uses `display_name`, preserves its ID and requires separate approval for any baseline-key refresh.
- For the same family/SKU and packaging, evidence from the newest production lot wins, including buyer-submitted manufacturer labels. Record the lot/revision and source proving recency. Never average or use Git recency. Report “manufacturer revised recommended values in newer lot”, not a presumed formula change.
- If neither duplicate has evidence, retain survivor metadata and record both values/conflicts. That alone does not block an owner-confirmed identity merge.

### Reviewed duplicate tooling

Current official TDS/product pages are valid evidence for the exact product line's printing density/nozzle/bed. Lot/package binding remains required for packaging, spool material and tare. A product-line table does not establish every historical package's availability.

The auditor is read-only on catalog sources. Matching normalized names are candidates, not merge evidence. Ordered normalization retains `+`, versions, qualifiers and repeated tokens; `gray`/`grey` equivalence is comparison-only. `contracts/not_duplicates.json` exempts only exact, human-reviewed ID memberships with evidence, never whole brands or patterns.

The duplicate guard enforces **every current candidate**, existing or new. The temporary `contracts/owner_pending_duplicates.json` exempts only exact memberships also present in [the single owner decision sheet](audits/backlog-decisions.csv). Missing, stale, overlapping or mismatched pending entries fail closed. New members require review. This list authorizes no merge; remove its entries as the owner resolves the corresponding groups. Full closure requires an empty pending list.

The owner sheet requires all 11 columns: `group_id, brand, side_a_name, side_a_id, side_a_hex, side_b_name, side_b_id, side_b_hex, evidence_url, reason, recommendation`. Duplicate/unexpected headers, missing/surplus cells and empty required review values are rejected. Evidence URL cells may be empty when no binding evidence is available; the reason must retain that uncertainty.

`python scripts/audit_duplicates.py --all` enumerates every source file and reports confirmed non-duplicates, owner-pending groups and unresolved candidates separately. It exits nonzero for unresolved candidates outside those exact lists; zero unresolved does **not** mean that pending groups have been decided.

After separate authorization for a brand, create an audit outside `filaments/` and `contracts/` using an already fetched read-only upstream commit:

```bash
python scripts/audit_duplicates.py --brand BRAND --upstream-ref UPSTREAM_SHA --output .git/duplicate-audit
python scripts/merge_duplicates.py --brand BRAND --review docs/audits/BRAND-review.json
# Only after owner approval of exact mappings:
python scripts/merge_duplicates.py --brand BRAND --review docs/audits/BRAND-review.json --apply
```

The review JSON contains `version: 1`, `approved: true`, the audit's `audit_digest`, a pinned full `upstream_ref` SHA, `groups`, `bindings` and `metadata`. Each exact group ID maps to `{approved: true, survivor: ID, retire: [IDs], ref: REVIEW_REFERENCE, source: SHA_OR_URL}`. The selected survivor follows upstream preference, then no manufacturer prefix, evidenced official name, family size; ties require owner selection. Optional `official_names`/`upstream_exceptions` provide manufacturer evidence. `--exclude GROUP_ID` is repeatable. Without a review file the merge command only shows unreviewed proposals; without `--apply` it writes no data.

Ambiguous source decomposition requires a lossless binding `{key: EXACT_KEY, line: PRODUCT_LINE, color: PHYSICAL_COLOR}` keyed by public ID. When a `display_name` hides the source name, also retain `source_color` with its exact original source value; template qualifiers such as `Basic` cannot be discarded or relabeled as a color. Keep those bindings in a repository JSON audit referenced by each affected registry entry's `ref`; the audit file must exist and remain available for later checks. The checker reads the stored key plus that reviewed decomposition, never historical source recovery. Without an explicit base, baseline checks use the committed HEAD registry as their prior state, never the edited registry as its own authorization.

Metadata decisions are explicit objects `{id: SURVIVOR, values: {...}, source: SHA_OR_URL, lot: LOT_OR_REVISION, same_variant: true, approved: true}`. The reviewer establishes newest-lot recency and matching SKU/package; tooling does not infer it from arbitrary lot strings. Only supported ID-neutral fields are accepted. The plan retains the audit's older values/conflicts and supplied evidence. Apply splits exact source cells, preserves untouched compiled metadata/identities, rejects stale reviews, and restores original files after an ordinary write failure. It cannot promise a multi-file transaction across power loss; do not run it concurrently with catalog edits.

CI checks the full current catalog and rejects every unresolved duplicate candidate, existing or new, including surviving subsets after a retirement. Only exact reviewed memberships in `not_duplicates.json` or the owner-pending contract permit exemptions; the owner-pending list is empty after campaign closure. Candidate detection uses the documented normalized-name and physical-identity matching rules and requests review, not automatic consolidation.

Baseline and retirement checks use a trusted event base: `github.event.before` for pushes and the base SHA for PRs. Only an all-zero push base permits explicit HEAD-only checks; an unavailable nonzero base fails closed. The duplicate guard still checks the full catalog, rather than grandfathering existing candidates as warnings.

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
python scripts/audit_duplicates.py --all
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
