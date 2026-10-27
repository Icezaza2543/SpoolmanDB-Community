# Material Classification Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Implementation is not authorized by this planning deliverable.

**Goal:** Improve exact material classification without silently changing historical public IDs.

**Architecture:** Audit first, then choose an explicitly approved identity-preservation mechanism. Do not reuse the duplicate-retirement registry for material corrections: those are not duplicate retirements. Existing baseline identity keys include material, so preserving the ID string alone is insufficient.

**Tech Stack:** Python compiler, JSON Schema, pytest, compiled baseline and duplicate registry.

**Spec:** Owner request of 2026-10-27: finish #283 documentation, then plan #309 only. [Maintainer guidance](https://github.com/Donkie/SpoolmanDB/issues/309#issuecomment-6426915078) supports the most specific material the format allows, e.g. TPU-95A; it does not authorize Community ID migration.

## Verified starting evidence

- Community base: c6da23c88d75707a8faff5bae3d9c92481cb3a80; catalog 51,412 records.
- `scripts/compile_filaments.py::generate_id` incorporates lowercased material directly into each ID.
- In-memory experiment on the existing 3D4Makers `Luvocom® 3F PPS CF 9938 BK Filament {color_name}` definition: changing PLA to illustrative PPS-CF changes all 4 IDs. Example: `3d4makers_pla_luvocom3fppscf9938bkfilamentbk_500_175_p` becomes `3d4makers_pps-cf_luvocom3fppscf9938bkfilamentbk_500_175_p`.
- This experiment proves ID impact, not the manufacturer's exact material designation. No source data was changed. Density and temperatures also require separate evidence review for this suspicious definition.
- The 303-family figure in issue #309 is historical, not a current audited queue. Recompute it; do not import that count as verified current work.

## Global constraints

- No material, source data, schema, compiler, baseline or retirement edits during planning.
- Preserve historical public IDs; do not hide changes by re-enrolling the baseline.
- Exact current manufacturer TDS/product evidence or explicit owner-approved evidence required. Product-name tokens identify candidates, not verified classifications.
- Packaging, tare, SKU/EAN, colors, weights and diameters stay unchanged.
- No upstream writes or comments; no new PR or remote feature branch.

## Review focus

- Material changes alter both ID generation and baseline identity; test both.
- CF/GF percentage and Shore hardness must come from exact-line evidence, not inferred branding.
- Renaming a material can collide with an existing variant; check the whole catalog.
- Existing retired IDs may target an affected survivor; keep registry targets valid.
- Manufacturer branding such as HF/Tough is not automatically a new polymer type.

## Task 1: Build a reviewed inventory (next recommended step)

**Files:** Create `docs/audits/material-classification-review.csv` and a companion evidence report; read source JSON and compiler without modifying them.

- [ ] Inventory candidate definitions with manufacturer, source index, exact name, current material, proposed material, evidence URL, confidence and affected compiled IDs.
- [ ] Separate demonstrably wrong polymers (e.g. the PPS-named PLA candidate) from finer classification (TPU hardness, PA subtype, CF/GF content).
- [ ] Compile proposed changes in memory. List all old/new IDs, baseline key differences, collisions and affected retirement targets. Verify packaging and identifiers unchanged.
- [ ] Classify unresolved evidence as deferred. Present the reviewed queue and identity strategy for owner approval.

## Task 2: Choose the identity contract before implementation

**Files to assess:** `scripts/compile_filaments.py`, `scripts/compile_id_baseline.py`, `filaments.schema.json`, `contracts/compiled_id_baseline.json`, `retired_ids.json`, and their tests.

- [ ] Preferred direction to assess: keep original public IDs through an explicit, narrowly scoped identity override while correcting the visible material. Design a reviewed metadata-correction contract for baseline keys; never broadly disable baseline checks.
- [ ] Alternative: an additional precise-classification field preserves existing material/IDs, but stock Spoolman will not filter by an unsupported extension. Explain this limitation before selecting it.
- [ ] Do not implement either alternative until the owner approves its semantics and migration scope. A breaking rekey is not currently authorized.

## Task 3: Approved tooling and single-family pilot

- [ ] Write failing regression tests for approved material corrections with identical historical IDs, unchanged unrelated variants and identifiers, collision rejection, invalid evidence/override rejection, and retirement-target integrity.
- [ ] Implement only the approved contract; keep new-record ID generation unchanged unless separately authorized.
- [ ] Apply one evidence-complete family, then compare every compiled field and baseline key against the starting commit. List approved changes explicitly.
- [ ] Run the full maintenance section 7 suite, including stable/canary/projection, full duplicate audit and strict baseline comparison.
- [ ] Deliver under the existing no-PR Community workflow only after approval and all gates pass. Expand per reviewed manufacturer after the pilot.

## Current decision

Planning only. Recommended next action is Task 1 (evidence inventory), not bulk replacement of material strings. No SKU/EAN expansion or refill redesign is included.
