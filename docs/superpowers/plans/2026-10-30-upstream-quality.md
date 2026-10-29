# Upstream reconciliation and quality recovery

**Goal:** Reconcile current upstream evidence without losing historical IDs or Community metadata, then improve documentation and the static Explorer.

**Architecture:** Keep source JSON, the Python compiler and vanilla HTML/CSS/JS. Compare expanded source records field by field against pinned upstream and the immutable starting commit. Conflicts remain explicit audit entries, never silent overwrites.

**Spec:** User task supplied on 2026-10-30 (Priorities 1–8).

**Constraints:** Feature branch only; atomic brand/feature commits; no fabricated data, breaking baseline override, mass material migration, upstream PR, production deployment or automatic merge. Issue #309 remains HOLD.

## Ordered work and verification

- [x] P1: Record baseline tests/metrics/CI; inspect upstream guide and PRs; produce reproducible field-level reconciliation and explicit deferrals. Add only evidence-backed non-conflicting variants in separate brand commits. Implement per-color TD support with schema/compiler regression tests; compare ISO country codes.
- [x] P2: Fix confirmed regressions with failing tests first; compile, strict validation, ID gate against `2a2c6370292b30732ddc80921fa67d65f4e7abf4`, pytest, JS tests, stable/canary and projection checks.
- [x] P3: Condense README, preserve snapshot markers and technical history under docs, credit upstream accurately, check generated metrics and links.
- [x] P4: Audit current routes and static assets; improve catalog usability, accessibility and responsive layout; verify actual desktop/tablet/mobile rendering and preserve analytics/schema/contribution routes.
- [x] P5: Research current official OrcaSlicer plugin/cloud status; document value, effort, risk, compatibility and maintenance by roadmap horizon.
- [x] P6–7: Update compatibility status from checked pins; preserve material HOLD and report identity impacts without applying migrations.
- [x] P8: Audit manufacturer identities and internal records for Silver3D, CC3D and Alchemakes; record sources, tare gaps and alias uncertainty.
- [ ] Delivery: Full checks, independent whole-branch review, atomic commits, Community Draft PR if access permits, concise Thai report with evidence and limitations.

## Review focus

- Same physical product under a different source name: defer ambiguous matches and retain IDs.
- Per-color fields through multiple weights/diameters: test distinct values, omitted values and invalid values.
- Community metadata and production-lot differences: compare every old compiled field and retain evidence gaps.
- Long names, empty results and hostile source strings: verify responsive, keyboard-safe rendering.
- Remote CI and local checks are distinct evidence; never infer CI success from local success.

## Execution ledger

- Starting tree clean on main, same as origin/main. Created `maintenance/upstream-quality-2026-10-30`.
- Baseline: 490 manufacturer files, 12,308 source groups, 51,412 compiled records, 154 material definitions.
- Upstream fetched: `c67dcd85dd4ff8de9bbc4f1eaa617aa837e95b1a` (commit date 2026-10-29), checked 2026-10-30. Prior observation `9d53d28703ba1bcc97ab504e069d437ae2053c5a`.
- Ruling: proceed inline with the user's explicitly requested execution; no extra plan approval. The current task's feature-branch/Draft-PR instructions supersede the older no-PR maintenance procedure.

- Completed P1–8 with explicit evidence-based deferrals in the reconciliation and coverage reports. Accepted only 20 Sunlu PETG 2.0 variants; all old IDs and fields preserved.
- Final local checks: 294 tests, strict gates, stable/canary/projection and README snapshot passed. Three browser engines passed source/staged-site QA; axe reported zero scoped violations on five routes.
- Independent review approved code through `6fa6cf9`; final documentation links and whitespace checked. Draft PR delivery remains the final step.
