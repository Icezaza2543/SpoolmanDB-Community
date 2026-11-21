# Upstream imports (no ID changes) — 2026-11-16

## Baseline and method

Originally prepared on the fork's `main` at `63c67d4`; rebased on 2026-11-20 onto Community `main` at `f195426ddd9e4f0d2f589d0bc3b8943d25016496`, after the rename migrations #75 to #84. See [Status on 2026-11-20](#status-on-2026-11-20) for what changed since. Upstream: Donkie/SpoolmanDB `main` at `3cf89fbb291865a80dd6b857396e963b9e15531c` (2026-11-15). This covers every upstream merge since the [2026-10-30 reconciliation](2026-10-30-reconciliation.md) (`c67dcd85`). It also covers three open upstream PRs, reviewed at their head SHAs: Donkie/SpoolmanDB#512 `e322c009`, #531 `374784ed` and #532 `a5b86712`.

For each upstream PR, earlier Community decisions in `docs/audits/` were checked first; Donkie/SpoolmanDB#500, #501 and #502 were already decided on 2026-11-07, and those decisions stand. Then the before/after source JSON was expanded with `scripts/compile_filaments.py`. Every added or changed record was compared with Community in two ways:

1. Exact ID and the `reconcile_upstream.py` candidate key.
2. A looser check: same manufacturer, same material and same colour name, in any product line.

Only additions and value corrections that leave existing IDs unchanged are applied here. Renames that change IDs (the queengooborg cleanups and the spelling fixes inside data PRs) wait for the rename-retirement process proposed in Icezaza2543/SpoolmanDB-Community#72.

Results:

| Check | Result |
|---|---|
| New public IDs | 188 (NOVTAU is not included; see the 2026-11-18 table) |
| Changed, rekeyed or removed historical IDs | 0 |
| Duplicate candidates | 0 unresolved (the 1 existing candidate is a reviewed non-duplicate) |
| `validate.py --strict` | Pass |
| `pytest` | 355 passed |
| Stable Spoolman contract | Pass |
| Baseline check (`compile_id_baseline.py --strict --base-ref f195426`) | Pass: 188 added, 0 removed, changed or rekeyed |

## Decisions per upstream PR

| Upstream PR | Decision | New IDs | Notes |
|---|---|---:|---|
| #506 Tinmorry TPU 95A Black hex | **Applied** | 0 | `3E413F` → `000000`. The Community value was the old upstream value. The PR says the earlier hex showed the unprinted filament. |
| #505 Extrudr PLA NX2 Matt | **Applied** | 56 | New 1 kg / 1.75 mm group copied as-is. It also gets the line's existing `country_of_origin` and `tds_url`, which are line-level. Hexes are converted from manufacturer RAL numbers ([source](https://extrudr.com/en/de/products/pla-nx2-matt/)). |
| #500 Deeplee PLA+ High Speed 2.0 | **No change (blocked)** | 0 | Still blocked under the [2026-11-07 decision](2026-11-07-release-catalog.md#deeplee--block_evidence): no manufacturer evidence for this SKU, its density or its plastic spool and 113 g tare. The upstream PR adds only a third-party profile. |
| #501 Fusion PCTG | **No change (blocked)** | 0 | Still blocked under the [2026-11-07 decision](2026-11-07-release-catalog.md#fusion--block_evidence): density, tare, hex and print values come only from third-party profiles. Also, the existing Community PCTG line lives under "Fusion Filaments", not "Fusion". |
| #503 Polymaker Panchroma | **Partially applied** | 1 | Panchroma Matte: 37 hexes updated to the manufacturer's published values ([source](https://shop.polymaker.com/en-eu/products/matte-pla)). Electric Magenta added as a **refill-only** group (`is_refill: true`) because it is published only on the refill variant. The removal of "Formerly …" from names is deferred to the rename process. Dual Matte colours and hexes were already in Community. |
| #504 Numakers PLA+ | **Partially applied** | 8 | 32 hexes updated (the Community values were the old upstream values). Eight missing colours added. Spelling renames (Flourescent → Fluorescent, Lavendar → Lavender, Grey → Gray, Fuscia/Magenta → Magenta, Cool (Lithophane) White → Cool White) are deferred to the rename process. |
| #529 Bambu Lab PLA Palette, TPU-75A | **Applied, tare left out** | 15 | Both products confirmed as current Bambu products: the PLA Palette CMYKW five-spool kit, and TPU 75A at 2.85 mm for the H3C. See [3DJake TPU 75A](https://www.3djake.com/bambu-lab/tpu-75a-pink) and [ALL3DP](https://all3dp.com/4/bambu-labs-new-tpu-75a-is-ultra-soft-prints-fast-brings-back-2-85-mm-filament/). The PR's 250 g tare and spool type have no source, so they are left out. Note that adding a spool type later will change these IDs (`_n` suffix). New material `TPU-75A` (density 1.17) added to `materials.json`. |
| #508 NOVTAU | **Not included here** | 0 | New manufacturer file. Superseded by #530 (see below), which Icezaza2543/SpoolmanDB-Community#77 imports. |
| #512 Voxelab (open) | **Partially applied** | 28 | Colours missing from the existing Community `High Speed` PLA+ and PLA groups were added to those groups. Upstream lists Abyssal Red under PLA with a different hex, while Community lists it under PLA+, so that colour is left out as a conflict. PLA+, PETG-CF and ASA-CF were already present. Source: Amazon listings in the PR. |
| #531 Giantarm (open) | **Applied** | 80 | Fourteen colours added to the existing `Giantarm PLA` group. The Red placeholder `FF0000` was replaced with the listed `C41D26`. New Silk PLA, PETG and TPU-95A groups use upstream naming. No tare information is available. Source: Amazon listings in the PR. |
| #532 Overture Easy (open) | **No change** | 0 | All 28 records already exist as Community `PLA Easy` / `PLA Easy Glow`. Renamed to upstream's IDs in Icezaza2543/SpoolmanDB-Community#85. |
| #511 Hatchbox ABS Black | **No change** | 0 | Already present as `hatchbox_abs_absblack_1000_175_c`. |
| #516 RatRig field fix | **No change** | 0 | Community already has the corrected `spool_type`, with the same IDs. |
| #507 ELEGOO Marble colours | **No change (conflict)** | 0 | Both colours exist. The Community hexes came from the Open Filament Database, the upstream hexes from 3dfilamentprofiles. Neither is a manufacturer source, so the Community values are kept. |
| #502 Das Filament | **No change** | 0 | Matches the [2026-11-07 decision](2026-11-07-release-catalog.md#das-filament--partial-safe-addition): the Community 1 kg variants and the TPU V2 Flexibel line already cover this. The upstream tare of 214 g has no measurement evidence and does not identify the spool type. |
| #509, #514, #519–#524, #536 and open #515, #517, #518, #525–#527 | **Deferred** | — | Name and material cleanups that change IDs, file reformatting, linter and docs. These wait for the rename-retirement process (Icezaza2543/SpoolmanDB-Community#72). Checked for field fixes that leave IDs unchanged (density, temperatures, hex, tare, finish and similar): none apply. The only one, Inland Silk Grey in #525, has no Community counterpart; the Community `Silk PLA Gray` is a different record with its own values. |

## Upstream merges reviewed on 2026-11-18

Upstream `main` moved from `3cf89fbb` to `8e391c16be4bfde29dfc184e2f0b9a8d154ab550` (2026-11-18). That range merged the cleanup PRs deferred above, plus two data PRs. Only #530 (NOVTAU) is applied in this PR. The rename counts come from dry runs of `scripts/rename_migration.py --upstream <merge>^1 <merge>` against Community data, using the tooling proposed in Icezaza2543/SpoolmanDB-Community#73. Nothing was written.

| Upstream PR (merge) | Decision | Notes |
|---|---|---|
| #527 various brands (`772db673`) | **Deferred: rename + reclassify** | Same-material renames that match Community: 13 files, 740 IDs. The files are ambrosia, cr3d, creality, elegoo, flashforge, formfutura, NTHGrillon, printedsolid, prusament, qiditech, rosa3d, soleyin and sunlu. 8 groups change material (cc3d, gst3d, kexcelled, qiditech, tecbears, teqstone, tinmorry, xzn; e.g. `TPU` → `TPU-95A`) and wait for the reclassify process. r3d and smartfil: no Community group has the upstream template name, so they need a manual mapping. |
| #518 Polymaker (`e86be9f1`) | **Deferred: rename + reclassify** | 9 groups / 858 IDs rename cleanly. 9 groups change material (Fiberon PA grades, PolyFlex TPU hardness). Run after this PR, which also edits `polymaker.json`. |
| #526 Overture (`641226c7`) | **Deferred: rename + reclassify** | 57 groups / 93 IDs rename cleanly, and existing retirements pointing at renamed IDs are re-pointed. 1 group (`High Speed 95A`, TPU → TPU-95A) changes material. |
| #515 AzureFilm (`f320e26d`) | **Deferred: reclassify** | All 5 changed groups also change material (`TPU` → `TPU-85A`/`TPU-98A`, `CF` → `PETG-CF`/`PA-CF`, `PC` → `PC+ABS`). |
| #525 Inland (`df5d1400`) | **Deferred: needs binding** | Moves `Silk` from colour names into the template (`Silk Grey` → `Grey`), like #522 and #524. Drops Inland Silk Grey `BBC6CE`, which has no Community counterpart (see above). |
| #536 eSun formatting | **No change** | Whitespace only at the end of `esun.json`, merged together with #518. |
| #532 Overture Easy (`8e391c16`) | **No change** | Merged unchanged from the head reviewed above. All 28 records already exist as Community `PLA Easy` / `PLA Easy Glow`. |
| #528 ELEGOO PAHT-CF (`7ff6b0f`) | **No change** | Icezaza's upstream PR for the measured 169 g cardboard tare (see `docs/evidence/elegoo/paht-cf-2026-11-12/`). Community already has it. |
| #530 NOVTAU update (`bb7a5ab`) | **Not included here** | Imported by Icezaza2543/SpoolmanDB-Community#77 (the same data). An open upstream follow-up, Donkie/SpoolmanDB#548, changes NOVTAU again. |

Upstream PRs still open by the same author: #512 Voxelab and #531 Giantarm (both partially applied above), and #517 (spool_weight lint warning; tooling, not data). On 2026-11-20 #512 (`83a14cf7`) and #531 (`ab6cb0cc`) each gained one commit, "Add spool weight (sourced from SpoolmanDB-Community)", which adds tares Community already has. Nothing more to import.

## Follow-ups

- Some cleanups are restructures, not plain renames: #522 (eSun) moves words between colour names and templates (`PLA-Luminous {color_name}` + `Cored Luminous Orange` → `Cored Luminous {color_name}` + `Orange`), and #524 (Professional LAB) splits groups. The rename-retirement rule rejects colour-name changes, so these need a reviewed line/colour binding before they can be migrated.

- The other Polymaker Panchroma Matte groups (`Army/Muted/Pastel Panchroma Matte PLA`) still carry the older hexes. Aligning them needs a separate review.
- Bambu PLA Palette and TPU-75A are missing tare and spool type until a measurement or manufacturer source is found.

## Status on 2026-11-20

Donkie/SpoolmanDB `main` is still at `8e391c16`. The deferred cleanups above have since gone through the rename process (Icezaza2543/SpoolmanDB-Community#72):

| Upstream PR | Status |
|---|---|
| #521 add:north | Migrated in Icezaza2543/SpoolmanDB-Community#75. |
| #526 Overture | Migrated in Icezaza2543/SpoolmanDB-Community#78 (`High Speed 95A` waits for reclassification). |
| #527 various brands | Same-material renames migrated in Icezaza2543/SpoolmanDB-Community#80 to #84. CR3D and FlashForge keep their Community IDs; NTH Grillon waits for Donkie/SpoolmanDB#546; the material changes wait for reclassification. |
| #532 Overture Easy | Icezaza2543/SpoolmanDB-Community#85. |
| #515 AzureFilm | Material changes only; proposed as the reclassification pilot in Icezaza2543/SpoolmanDB-Community#86. |
| #518 Polymaker | Next, after this PR (both edit `polymaker.json`). |
| #525 Inland, #522 eSun, #524 Professional LAB | Still need a reviewed line/colour binding. |
