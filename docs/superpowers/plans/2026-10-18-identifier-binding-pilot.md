# Identifier Binding Pilot Implementation Plan

> **For agentic workers:** Use superpowers:executing-plans to implement this owner-authorized plan inline. Deliver one final commit under maintenance guide section 8, not intermediate commits or a PR.

**Goal:** Inventory SKU/EAN fanout and correct one evidenced Community product family without changing any public identity.

**Architecture:** Keep the existing source schema and compiler. Split the existing 3D4Makers ABS definition by its two weights, bind each SKU and manufacturer GTIN to the exact existing 1.75 mm variant, and keep compiled extension fields unchanged in shape.

**Tech Stack:** Python, pytest, JSON source data, existing compatibility and baseline tools.

**Spec:** Owner request in this task; docs/maintenance.md sections 3-8.

## Global Constraints

- Community only; no upstream writes, PR, or remote feature branch.
- Starting main: df9fcf53eb4b02ee58d47a0b88a6d3a4e8ab41a2; 51,412 records.
- No public ID additions, removals, rekeys, baseline changes, or retirement changes.
- No schema/compiler/workflow changes or non-identifier catalog metadata changes.
- Manufacturer remains 3D4Makers despite the current site's 3D4M rebranding.
- Preserve unknown/unaudited bindings elsewhere; a shared identifier is an audit candidate, not proof of an error.
- Run the full maintenance suite, compare complete manifests and native projections, then push main once and verify CI/Pages.

## Review Focus

- A 750 g SKU must never be inherited by the 2,300 g variant, or vice versa.
- New GTINs must resolve to only their exact target IDs, including checks across other brands and fields.
- Splitting definitions must preserve color names, HEX, packaging, tare, temperatures and every identity key.
- No 2.85 mm records or identifiers may be added merely because the current product page lists them.
- Existing reviewed GTIN contracts and all identifiers outside the pilot must remain untouched.

### Task 1: Audit and reproduce

**Files:** Create docs/audits/2026-10-18-sku-ean-pilot.md; retain full local inventory in this task's writable visualization artifact directory (`sku-ean-pilot/`). The environment restricts direct file edits inside `.git`.

- [x] Inventory all source/compiled bindings; distinguish raw-value sharing from manufacturer-scoped SKU sharing.
- [x] Verify exact variant tuples using the manufacturer's ProductGroup JSON-LD on https://www.3d4makers.com/products/abs-filament.
- [x] Write literal regression cases for all 12 existing target IDs in tests/test_identifier_bindings.py; compile actual catalog data and assert exact global memberships.
- [x] Run the regression test before editing data. Expected: failure on the cross-weight SKU fanout. Actual: 12 failures on exactly that condition.

### Task 2: Correct bindings and verify

**Files:** Modify filaments/3d4makers.json; README.md only if snapshot generation changes it.

- [x] Split only the ABS Filament definition into 750 g and 2,300 g definitions. Keep each exact original weight object and all non-identifier fields.
- [x] Each source color gets its own matching SKU and the exact manufacturer GTIN; no other definitions change.
- [x] Run regression tests. Expected: all 12 cases pass, with no manufacturer-scoped SKU/global GTIN leakage. Actual: 12 passed.
- [x] Compare against the starting commit: same IDs/keys/count; only codes/eans change on the 12 target IDs; native projections identical; unique existing identifier values preserved.
- [x] Run every maintenance section 7 command with the starting SHA. Expected: all pass; zero baseline/registry diff, zero unresolved duplicate candidates. Actual: all passed; 277 pytest tests.
- [x] Review the entire diff and evidence in a separate review pass. Record actual validation results in the audit. Actual: independent reviewer approved; no Critical/Important/Minor findings.

**Authorized delivery procedure:** Create one focused commit, fast-forward main, push main once, verify Build/CodeQL/Pages and published bindings, then delete only the local pilot branch. Delivery verification is recorded in the final task response after the push, rather than pre-recorded as successful in this commit.
