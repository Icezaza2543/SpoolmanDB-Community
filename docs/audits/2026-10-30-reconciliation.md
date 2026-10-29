# Upstream reconciliation — 2026-10-30

## Baseline and method

Starting Community commit: `2a2c6370292b30732ddc80921fa67d65f4e7abf4` (clean, equal to origin/main). 490 manufacturer files, 12,308 source groups, 34,845 colors, 51,412 compiled variants, 154 material definitions. Baseline compile, validation, ID gate and stable contract passed; pytest **277 passed**. Windows pytest reported a cache-directory permission warning, not a test failure. GitHub connector and `gh run list --commit` both returned no runs for this SHA: remote baseline CI is **unavailable**, not assumed green.

Fetched upstream main: `c67dcd85dd4ff8de9bbc4f1eaa617aa837e95b1a`, commit date 2026-10-29. Previous observation: `9d53d28703ba1bcc97ab504e069d437ae2053c5a`; historical fork base remains `5b61e755926568ec3b3235701684595872b70b49`.

All upstream source JSON was parsed and expanded against all Community source JSON, matching exact public IDs first and then ordered normalized manufacturer/material/name/weight/diameter. Packaging is ignored only to flag candidates, never to conclude equivalence. Null upstream metadata does not erase Community extensions. Full non-null field differences and candidate IDs are generated, not inferred from filenames.

Reproduce the complete per-record inventory (including Community-only IDs):

```sh
python scripts/reconcile_upstream.py --upstream-ref c67dcd85dd4ff8de9bbc4f1eaa617aa837e95b1a --community-ref 2a2c6370292b30732ddc80921fa67d65f4e7abf4 --output .git/reconciliation/audit
```

The [machine summary](2026-10-30-reconciliation-summary.json) includes manufacturer counts and the SHA-256 of `records.jsonl`. The audit does not modify sources. “New” and “Community-only” mean unmatched by this conservative comparison; spelling, aliases or material differences can still conceal duplicates.

| Baseline category | Expanded records | Decision |
| --- | ---: | --- |
| Existing identical upstream values | 4,617 | Retain Community metadata |
| Upstream-only candidates | 1,345 | Accept 20 Sunlu PETG 2.0; defer remaining 1,325 pending evidence/identity review |
| Conflicting definitions | 527 | Preserve Community values; no automatic corrections |
| Duplicate / packaging / name candidates | 2,968 | Defer; matching is not merge authorization |
| Community-only by comparison | 43,261 | Retain unchanged |
| Applied upstream corrections to existing variants | 0 | No unambiguous newer-lot binding established |
| Historical public ID changes/removals/rekeys | 0 | No new retirements or material migrations |

## Review decisions and deferred list

| Scope | Decision and reason | Reopen with |
| --- | --- | --- |
| Sunlu #487 PETG 2.0 | **Accepted**, 20 new variants; official fields and directly reported tare measurement. [Brand evidence](2026-10-30-sunlu-petg-2.md). | — |
| Sunlu #485, #490–493 | Defer overlapping names, PLA vs PLA+ classification, old/new spool lots, and assumed 189 g tare on unmeasured lines. Keep existing SKU/EAN/SDS/TDS and packaging matrices. | Exact SKU/package/lot bindings; reviewed ID-neutral field decisions |
| Bambu #486 | Ten Silk colors overlap Community Silk/Dual definitions under other names and packaging suffixes. Do not import new IDs for a rename. | Exact line/color/packaging review |
| Bambu #494 PETG Matte | Eight genuinely unmatched candidates; density/colors have official PDF sources, but the PR provides no traceable tare measurement for its 250 g value. Deferred under the task's evidence rule. | Measurement or manufacturer package-specific tare source |
| Kingroon #484/#499 | PETG and PLA Basic overlap Community; 13 PLA Basic colors appear new. #484 explicitly measured PETG tare, but does not establish PLA Basic tare. Do not combine PETG with PETG Basic or change legacy suffixes. | Product/package-specific tare, identity and color binding |
| eSUN #488 | Upstream Morandi Purple change is backed by a third-party profile; Community has a different product/color representation. No guessed mapping. | Exact official SKU/color identity and current HEX evidence |
| Inslogic #297 | Five upstream groups are a deliberately reduced subset of Community's 22 groups. Composite spools explain some suffix differences; extensions stay intact. | Exact variant-level correction evidence |
| All remaining unmatched/conflicting rows | Deferred inventory in reproducible `records.jsonl`, with both values and candidate IDs. No blanket copying of old upstream additions. | Focused manufacturer review of sources and measured tare |
| #495 | Not merged at inspection; not imported. | Merged, reviewed evidence |
| #489 | PR metadata unavailable from connector; no data imported on that reference. | Accessible issue/PR evidence |

The [PR evidence snapshot](2026-10-30-upstream-pr-evidence.json) records #283, #297, #316, #484–497 and #499 responses. #314 documents Donkie's focused manufacturer PRs, source links, four-space upstream JSON, generated-output exclusion, strict spelling and package Cartesian-product checks. #316 extends preview tooling to existing PRs. These upstream conventions do not authorize rewriting Community historical names or adopting privileged bot workflows wholesale.

## Schema/compiler and workflow review

- #497: added optional positive per-color `transmission_distance`, emitted as nullable mm. All 51,412 prior records compared equal field-for-field after excluding that new null field. No measured values fabricated.
- #283: copied the assigned ISO alpha-2 enum from pinned upstream. All existing COO values already belong to that set. No HQ-origin inference or data rewrite.
- #496: Community already accepts fixed single-color names. Its broader historical naming compatibility remains; no mass naming restriction imposed on legacy records.
- Material additions and naming conventions were inspected. Issue #309 stays **HOLD**. Generic-to-specific substitutions change `generate_id` input; adding a nominal replacement would create another identity, not repair the old one. Example: existing Sunlu PLA / `PLA+ 2.0 …` cannot be switched to PLA+ / `2.0 …` without an ID migration.
- The only changes since the previous observed upstream commit are Bambu data, Kingroon data and an upstream issue-manager delay typo. Earlier changes since the historical base include the compiler/schema work and the merged manufacturer PRs enumerated by `git log 5b61e755..c67dcd85 -- filaments`.
- Community's required strict ID/duplicate gates and metadata passthrough remain. No upstream workflow replacement, schema breaking migration, baseline override or production deployment.
