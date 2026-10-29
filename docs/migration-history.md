# Historical duplicate migration notes

Archived from the README on 2026-10-30. These record prior approved campaigns, not authorization for new migrations.

[Maintenance rules](maintenance.md) · [Backlog](coverage-backlog.md)

## Maintenance stance

Owner-approved duplicate migrations are recorded in the [retired-ID registry](../contracts/retired_ids.json). The tooling retires no data automatically. Each approved true-duplicate migration intentionally removes its listed IDs from the catalog: existing Spoolman spools keep their local imported data, but Spoolman does not read the registry, redirect old catalog lookups or migrate stored external IDs. Other consumers must apply the old-to-survivor mapping themselves. See the [review, ID-safety and exact-reinstatement rules](maintenance.md#4-public-id-immutability-rule).

### Current duplicate campaign status

The campaign **closed on 2026-10-05** with **2,022 registered retirements** and **51,412 catalog records**. The owner resolved all 180 final decision-sheet groups: 179 merged, and OV083 (Overture TPU Gray/Grey) retained as a confirmed non-duplicate. The owner-pending list is empty; the full-catalog audit reports **0 unresolved groups**.

CI rejects unresolved candidates under the documented duplicate-matching rules. The only current exemption is the exact OV083 membership in `not_duplicates.json`; detection does not prove that every physically equivalent product is identifiable. See [the campaign closure](audits/2026-10-04-duplicate-campaign-final.md#closure-2026-10-05) and [the remaining future-work backlog](audits/duplicate-backlog.md). The brand sections below retain their original migration checkpoints.

### Kingroon duplicate migration (2026-10-03)

This is an **intentional breaking catalog migration** approved by the owner for [issue #66](https://github.com/Icezaza2543/SpoolmanDB-Community/issues/66). It retires exactly five duplicate records, reducing the compiled catalog from 53,434 to 53,429 records without creating replacement IDs. Each survivor already exists, and its identity and metadata are unchanged.

| Retired public ID | Existing survivor public ID |
| --- | --- |
| `kingroon_pla_kingroonplablack_1000_175_p` | `kingroon_pla_plablack_1000_175_p` |
| `kingroon_petg_kingroonpetgblack_1000_175_p` | `kingroon_petg_petgblack_1000_175_p` |
| `kingroon_petg_kingroonpetggrey_1000_175_p` | `kingroon_petg_petggray_1000_175_p` |
| `kingroon_pla_kingroonplawhite_1000_175_p` | `kingroon_pla_plawhite_1000_175_p` |
| `kingroon_petg_kingroonpetgwhite_1000_175_p` | `kingroon_petg_petgwhite_1000_175_p` |

PETG Basic remains a separate family: all ten of its records are untouched. The unique `Kingroon PLA` Grey, Red and Blue records retain their original IDs and metadata, as do all refill variants. No other brand is included.

The [reviewed decisions and original audit](audits/2026-10-03-kingroon-duplicate-review.json) retain unresolved conflicts: PLA Black/White density 1.23 versus 1.24 g/cm³ and nozzle 190–210 versus 190–230 °C; PETG White HEX `FFFFFF` versus `F5F5F5`. Survivor values are kept. The official PLA Basic page and general filament guide are not yet bound to these historical variants or their production lots, so they do not authorize changing those values. The registry preserves each retired record's exact original baseline key for audit and exact reinstatement.

### Nebula duplicate migration (2026-10-03)

This is an **intentional breaking catalog migration** approved for groups N001–N345. It retires 345 matched OFD `PLA Premium` / `PETG Premium` records, reducing the compiled catalog from 53,429 to 53,084 and Nebula from 1,623 to 1,278 records. The existing `Premium PLA` / `Premium PETG` IDs survive by Rule 3, following Nebula's official `PREMIUM PLA` / `PREMIUM PET-G` product names; Cartesian record counts do not decide the direction. No new IDs are created, and all survivor and unique identities and metadata stay unchanged.

The [complete list of 345 retired IDs and their survivors](audits/2026-10-03-nebula-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-nebula-duplicate-review.json) retain each original baseline key, source record and unresolved conflict. All 773 Nebula SKU/code bindings are preserved. PETG page-versus-TDS ranges and PETG 5kg density/temperature conflicts remain unresolved; survivor values are kept because no matching newer-lot evidence establishes a correction.

All 505 non-matching or otherwise out-of-scope OFD variants remain untouched, including all 2.85mm and Silk records. No other brand is changed. Retired IDs disappear from catalog lookups; existing Spoolman spools keep their local imported data, but Spoolman does not read the registry, redirect those lookups or migrate stored external IDs. Other consumers must apply the old-to-survivor mapping themselves.

### Protopasta duplicate migration (2026-10-03)

This is an **intentional breaking catalog migration** approved for 38 groups. It retires 41 duplicate IDs, reducing the compiled catalog from 53,084 to 53,043 and Protopasta from 889 to 848 records. Existing upstream-preferred IDs survive by Rule 1; no new IDs or changed/rekeyed survivor identities are introduced. Existing Spoolman spools retain their local imported data, but old catalog lookups disappear and Spoolman does not follow the retired-ID registry automatically.

The [complete list of 41 retired IDs and their survivors](audits/2026-10-03-protopasta-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-protopasta-duplicate-review.json) retain exact original baseline keys, source templates, unresolved conflicts and the three approved Simply line/color bindings. All 234 Protopasta SKU/code bindings are preserved. P004/P009/P012/P016 remain deferred and untouched; packaging/spool/tare and all other brands are unchanged.

The owner also approved 19 printing-field corrections on nine PETG survivors using current official product-line evidence, plus eight wrong-document-link corrections on four survivors. P034/P041 use explicitly approved **family-level PETG/PETG-CF7 material-table evidence** (250°C at 12 mm³/s, 80°C plate), not a manufactured min/max range or production-lot claim. Their recycled density stays 1.24 g/cm³ unresolved. Static Dissipative PETG now links matching PETG-ESD TDS/SDS; wrong PLA/HTPLA links on the two recycled survivors were removed because exact RPET document coverage is not confirmed. See the audit for every old/new field and source.

### Bambu Lab duplicate migration (2026-10-03)

This is an **intentional breaking catalog migration** approved for 124 groups: 117 Rule 1 groups, five Rule 3 Dual Color groups, and B043/B044 with the official **Blue Grey** survivor name. It retires 124 duplicate IDs, reducing the catalog from 53,043 to 52,919 and Bambu Lab from 614 to 490 records. No new IDs or changed/rekeyed survivor identities are introduced. Existing Spoolman spools keep their local imported data, but retired catalog lookups disappear; Spoolman does not follow the registry automatically.

The [complete list of 124 retired IDs and existing survivors](audits/2026-10-03-bambulab-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-bambulab-duplicate-review.json) retain exact original baseline keys, source-definition locations/templates, conflicts and ten lossless Dual Color bindings; full source definitions remain available at the pinned audit base. Existing codes are transferred only to the 24 approved target IDs, with no identifier changes to other weights/refills: Bambu code bindings become 734 → 723 as redundant bindings collapse, while all 678 unique values are preserved. EAN and refill-EAN bindings remain 18 and three respectively.

The owner also approved 15 printing-field changes on ten survivors using current official TDS: Aero uses raw-filament density 1.21 g/cm³ for length calculation; PC nozzle is 260–280°C; PC FR density is 1.18 g/cm³; PVA nozzle is 220–250°C. Silk/Lite values and 20 non-case HEX/representation differences remain unresolved, retaining survivor values. All 366 out-of-scope Bambu records, packaging/spool/tare and other manufacturers are unchanged.

### Fillamentum duplicate migration (2026-10-03)

This is an **intentional breaking catalog migration** approved for F001–F120: 60 ASA and 60 PLA groups. It retires exactly 120 duplicate IDs, reducing the catalog from 52,919 to 52,799 and Fillamentum from 244 to 124 records. Existing upstream-preferred `Extrafill {color_name}` IDs survive by Rule 1; no new IDs or changed/rekeyed survivor identities are introduced. Existing Spoolman spools retain their imported local data, but retired catalog lookups disappear; Spoolman does not consume the registry or redirect those lookups automatically.

The [complete list of 120 retired IDs and existing survivors](audits/2026-10-03-fillamentum-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-fillamentum-duplicate-review.json) retain each byte-identical original baseline key, all four full source definitions, compiled records and official evidence. All survivor metadata is unchanged, including packaging/spool/tare; four unique PLA Lilac records and every other manufacturer's compiled data are untouched. Codes/EAN bindings and unique values remain zero, with no transfers or losses.

Temperature-profile, density-document and 210/230/250 g tare conflicts remain documented and unresolved; 16 HEX differences are case-only. The current shop confirms 41 matching weight/diameter/color combinations, not the entire historical Cartesian matrix. The remaining 79 groups are current-unconfirmed, not declared unavailable or removed as obsolete. This approval authorizes duplicate retirement only, not new 1 kg variants, name changes or packaging corrections.

### Devil Design duplicate migration (2026-10-03)

This is an **intentional breaking catalog migration** approved for 110 duplicate groups, excluding D031–D035. It retires exactly 110 IDs, reducing the catalog from 52,799 to 52,689 and Devil Design from 608 to 498 records; the registry grows from 635 to 745 entries. Existing upstream-preferred IDs survive by Rule 1. There are no new IDs or changed/rekeyed survivor identities, metadata updates, or SKU/EAN transfers or losses.

The [complete list of 110 retired IDs and existing survivors](audits/2026-10-03-devildesign-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-devildesign-duplicate-review.json) preserve original baseline keys, source definitions, compiled records, official evidence and unresolved conflicts. D031–D035 (Galaxy PETG line/color decomposition) remain deferred in the [running duplicate backlog](audits/duplicate-backlog.md); all ten IDs and 378 other unique/out-of-scope Devil Design records are untouched. Survivor printing values, HEX, packaging and tare are retained.

Retired IDs disappear from the published catalog. Existing Spoolman spools retain their imported local data, but Spoolman does not read the registry, redirect old catalog lookups or migrate stored external IDs. Other consumers must follow the exact mappings themselves; rollback requires exact original-key reinstatement and baseline re-enrollment. This approval does not authorize retirement of Galaxy PETG, new variants, naming changes or packaging corrections.

### Paramount 3D duplicate migration (2026-10-03)

This is an **intentional breaking catalog migration** retiring 114 duplicate OFD IDs: the catalog decreases from 52,689 to 52,575 records, Paramount 3D from 266 to 152, and the registry grows from 745 to 859 entries. The owner-selected older, well-formed `Paramount 3D PLA/PETG/ABS/ASA` families survive; their prefixes are not renamed. Survivor/unique identities, metadata, packaging and tare are unchanged, with no new IDs or identifier transfers. All 109 SKU bindings and 108 unique SKU values remain.

The [exact retired IDs, survivors and original keys](audits/2026-10-03-paramount3d-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-paramount3d-duplicate-review.json) record the explicit owner-pattern override and unresolved metadata. PM070 (Matte Black) and prefix cleanup remain in the [backlog](audits/duplicate-backlog.md). Existing Spoolman spools keep local imported data, but Spoolman does not consume the registry or redirect retired external lookups.

This community extension complements the original SpoolmanDB while maintaining its own data-quality tooling and public explorer. Upstream changes are monitored, and suitable source-backed corrections may be proposed back through focused PRs following review and an explicit contribution decision. Community-only extensions remain documented separately, with careful attention to public-ID stability, validation, and a green GitHub Pages deployment.

### AzureFilm duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 77 exact duplicate IDs in 77 reviewed groups: 52,575 → 52,498 catalog records, with 9 tooling/decomposition groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-azurefilm-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-azurefilm-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 260 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### elegoo duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 49 exact duplicate IDs in 49 reviewed groups: 52,498 → 52,449 catalog records, with 37 tooling/decomposition groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-elegoo-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-elegoo-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 160 official-evidence printing/document field changes and 10 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### overture duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 81 exact duplicate IDs in 81 reviewed groups: 52,449 → 52,368 catalog records, with 2 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-overture-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-overture-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 4 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### prusament duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 74 exact duplicate IDs in 74 reviewed groups: 52,368 → 52,294 catalog records, with 1 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-prusament-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-prusament-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 116 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### Print With Smile duplicate audit (2026-10-03)

All 68 candidate groups are deferred for identity or line/color-decomposition review. No migration was applied: the catalog remains at 52,294 records, and all Print With Smile IDs, compiled metadata and identifiers are unchanged.

The [review and conflicts](audits/2026-10-03-printwithsmile-duplicate-review.md) and [JSON audit](audits/2026-10-03-printwithsmile-duplicate-review.json) retain the original source definitions and keys. The [running backlog](audits/duplicate-backlog.md) lists every preserved group and its blocker.

### gizmodorks duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 55 exact duplicate IDs in 55 reviewed groups: 52,294 → 52,239 catalog records, with 10 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-gizmodorks-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-gizmodorks-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 165 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### sunlu duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 47 exact duplicate IDs in 47 reviewed groups: 52,239 → 52,192 catalog records, with 15 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-sunlu-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-sunlu-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 202 official-evidence printing/document field changes and 39 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### dasfilament duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 51 exact duplicate IDs in 51 reviewed groups: 52,192 → 52,141 catalog records, with 2 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-dasfilament-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-dasfilament-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### sakata3d duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 28 exact duplicate IDs in 28 reviewed groups: 52,141 → 52,113 catalog records, with 13 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-sakata3d-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-sakata3d-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 10 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### polarfilament duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 40 exact duplicate IDs in 40 reviewed groups: 52,113 → 52,073 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-polarfilament-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-polarfilament-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### buddy3d duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 36 exact duplicate IDs in 36 reviewed groups: 52,073 → 52,037 catalog records, with 1 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-buddy3d-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-buddy3d-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### anycubic duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 36 exact duplicate IDs in 36 reviewed groups: 52,037 → 52,001 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-anycubic-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-anycubic-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 9 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### winkle duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 27 exact duplicate IDs in 27 reviewed groups: 52,001 → 51,974 catalog records, with 3 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-winkle-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-winkle-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 8 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### extrudr duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 29 exact duplicate IDs in 29 reviewed groups: 51,974 → 51,945 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-extrudr-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-extrudr-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 32 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### pushplastic duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 29 exact duplicate IDs in 29 reviewed groups: 51,945 → 51,916 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-pushplastic-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-pushplastic-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 34 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### 3djake duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 27 exact duplicate IDs in 27 reviewed groups: 51,916 → 51,889 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-3djake-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-3djake-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 29 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### fiberlogy duplicate audit (2026-10-03)

All 27 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,889 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-fiberlogy-duplicate-review.md) and [JSON audit](audits/2026-10-03-fiberlogy-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md). Exact-target EAN transfers conflicted with the current source-level duplicate-GTIN checker while unrelated 1 kg bindings remained intact, so all data changes were withdrawn before commit.

### filatech duplicate audit (2026-10-03)

All 24 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,889 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-filatech-duplicate-review.md) and [JSON audit](audits/2026-10-03-filatech-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).

### geeetech duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 23 exact duplicate IDs in 23 reviewed groups: 51,889 → 51,866 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-geeetech-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-geeetech-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### verbatim duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 5 exact duplicate IDs in 5 reviewed groups: 51,866 → 51,861 catalog records, with 17 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-verbatim-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-verbatim-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 15 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### ninjatek duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 20 exact duplicate IDs in 20 reviewed groups: 51,861 → 51,841 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-ninjatek-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-ninjatek-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### aurapol duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 15 exact duplicate IDs in 15 reviewed groups: 51,841 → 51,826 catalog records, with 3 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-aurapol-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-aurapol-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### americanfilament duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 13 exact duplicate IDs in 13 reviewed groups: 51,826 → 51,813 catalog records, with 4 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-americanfilament-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-americanfilament-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 13 official-evidence printing/document field changes and 13 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### 22network duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 12 exact duplicate IDs in 12 reviewed groups: 51,813 → 51,801 catalog records, with 3 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-22network-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-22network-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### ic3d duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 14 exact duplicate IDs in 14 reviewed groups: 51,801 → 51,787 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-ic3d-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-ic3d-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 42 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### tecbears duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 12 exact duplicate IDs in 12 reviewed groups: 51,787 → 51,775 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-tecbears-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-tecbears-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 24 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### ldo duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 11 exact duplicate IDs in 11 reviewed groups: 51,775 → 51,764 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-ldo-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-ldo-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### francofil duplicate audit (2026-10-03)

All 10 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,764 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-francofil-duplicate-review.md) and [JSON audit](audits/2026-10-03-francofil-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).

### polymaker duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 8 exact duplicate IDs in 8 reviewed groups: 51,764 → 51,756 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-polymaker-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-polymaker-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### qiditech duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 8 exact duplicate IDs in 8 reviewed groups: 51,756 → 51,748 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-qiditech-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-qiditech-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### eryone duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 2 exact duplicate IDs in 2 reviewed groups: 51,748 → 51,746 catalog records, with 5 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-eryone-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-eryone-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 1 official-evidence printing/document field changes and 1 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### jayo duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 6 exact duplicate IDs in 6 reviewed groups: 51,746 → 51,740 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-jayo-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-jayo-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### teqstone duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 6 exact duplicate IDs in 6 reviewed groups: 51,740 → 51,734 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-teqstone-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-teqstone-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### zyltech duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 6 exact duplicate IDs in 6 reviewed groups: 51,734 → 51,728 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-zyltech-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-zyltech-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 10 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### aceaddity duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 4 exact duplicate IDs in 4 reviewed groups: 51,728 → 51,724 catalog records, with 1 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-aceaddity-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-aceaddity-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### nobufil duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 5 exact duplicate IDs in 5 reviewed groups: 51,724 → 51,719 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-nobufil-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-nobufil-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### arianeplast duplicate audit (2026-10-03)

All 4 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,719 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-arianeplast-duplicate-review.md) and [JSON audit](audits/2026-10-03-arianeplast-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).

### gst3d duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 4 exact duplicate IDs in 4 reviewed groups: 51,719 → 51,715 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-gst3d-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-gst3d-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 2 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### 3de duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 3 exact duplicate IDs in 3 reviewed groups: 51,715 → 51,712 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-3de-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-3de-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### AmazonBasics duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 3 exact duplicate IDs in 3 reviewed groups: 51,712 → 51,709 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-amazonbasics-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-amazonbasics-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### iemai duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 3 exact duplicate IDs in 3 reviewed groups: 51,709 → 51,706 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-iemai-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-iemai-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 3 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### voxelpla duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 3 exact duplicate IDs in 3 reviewed groups: 51,706 → 51,703 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-voxelpla-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-voxelpla-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### alzament duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 1 exact duplicate IDs in 1 reviewed groups: 51,703 → 51,702 catalog records, with 1 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-alzament-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-alzament-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 2 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### creality duplicate audit (2026-10-03)

All 2 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,702 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-creality-duplicate-review.md) and [JSON audit](audits/2026-10-03-creality-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).

### flashforge duplicate audit (2026-10-03)

All 2 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,702 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-flashforge-duplicate-review.md) and [JSON audit](audits/2026-10-03-flashforge-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).

### r3d duplicate audit (2026-10-03)

All 2 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,702 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-r3d-duplicate-review.md) and [JSON audit](audits/2026-10-03-r3d-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).

### chckx duplicate audit (2026-10-03)

All 1 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,702 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-chckx-duplicate-review.md) and [JSON audit](audits/2026-10-03-chckx-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).

### conjure duplicate audit (2026-10-03)

All 1 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,702 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-conjure-duplicate-review.md) and [JSON audit](audits/2026-10-03-conjure-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).

### filamentsdepot duplicate audit (2026-10-03)

All 1 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,702 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-filamentsdepot-duplicate-review.md) and [JSON audit](audits/2026-10-03-filamentsdepot-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).

### filamentworld duplicate audit (2026-10-03)

All 1 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,702 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-filamentworld-duplicate-review.md) and [JSON audit](audits/2026-10-03-filamentworld-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).

### iboss duplicate audit (2026-10-03)

All 1 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,702 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-iboss-duplicate-review.md) and [JSON audit](audits/2026-10-03-iboss-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).

### inland duplicate audit (2026-10-03)

All 1 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,702 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-inland-duplicate-review.md) and [JSON audit](audits/2026-10-03-inland-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).

### l3d duplicate audit (2026-10-03)

All 1 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,702 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-l3d-duplicate-review.md) and [JSON audit](audits/2026-10-03-l3d-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).

### matterhackers duplicate audit (2026-10-03)

All 1 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,702 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-matterhackers-duplicate-review.md) and [JSON audit](audits/2026-10-03-matterhackers-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).

### polyterra duplicate migration (2026-10-03)

This **intentional breaking catalog migration** retires 1 exact duplicate IDs in 1 reviewed groups: 51,702 → 51,701 catalog records, with 0 tooling/identity groups deferred. No new IDs or changed/rekeyed survivor/unique identities are introduced. Packaging and tare are unchanged.

The [complete mappings and conflicts](audits/2026-10-03-polyterra-duplicate-review.md#complete-approved-retired-id-list) and [reviewed JSON audit](audits/2026-10-03-polyterra-duplicate-review.json) retain each original baseline key, source definition and exact metadata/identifier decision. This commit lists 0 official-evidence printing/document field changes and 0 exact-target identifier transfers; unrelated variants are unchanged and unique identifier values are preserved. Existing Spoolman spools retain local data; Spoolman does not follow the retirement registry automatically.

### professionallab duplicate audit (2026-10-03)

All 1 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,701 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-professionallab-duplicate-review.md) and [JSON audit](audits/2026-10-03-professionallab-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).

### sirayatech duplicate audit (2026-10-03)

All 1 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,701 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-sirayatech-duplicate-review.md) and [JSON audit](audits/2026-10-03-sirayatech-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).

### smartprint duplicate audit (2026-10-03)

All 1 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,701 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-smartprint-duplicate-review.md) and [JSON audit](audits/2026-10-03-smartprint-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).

### spectrum duplicate audit (2026-10-03)

All 1 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,701 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-spectrum-duplicate-review.md) and [JSON audit](audits/2026-10-03-spectrum-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).

### splice3d duplicate audit (2026-10-03)

All 1 candidate groups are deferred for identity or tooling review. No migration was applied; the catalog remains at 51,701 records. Original IDs, compiled metadata, identifiers, packaging and tare are unchanged.

The [review](audits/2026-10-03-splice3d-duplicate-review.md) and [JSON audit](audits/2026-10-03-splice3d-duplicate-review.json) retain the complete candidates, evidence and conflicts; all blockers are recorded in the [running backlog](audits/duplicate-backlog.md).
