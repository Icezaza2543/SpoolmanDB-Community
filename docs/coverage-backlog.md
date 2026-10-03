# Coverage Backlog

This document records established, unresolved coverage and schema items reserved for future maintenance cycles.

## Phase Status

- **P0 Status:** `SATURATED_WITH_WATCHLIST`
- **P1 Status:** `SATURATED_WITH_BACKLOG`
- **Reopening Condition:** Reopen items when new official/user-approved evidence or explicit identity/schema authorization addresses the recorded blocker.

## Maintenance Posture

Active development is paused after the completed maintenance and frontend/documentation fixes. This backlog is a handoff, not authorization to start another audit, import, migration, or upstream contribution. Resume focused work when the owner requests it, a reported defect is accepted for correction, or new evidence is approved for an unresolved item.

Historical public IDs and baseline identity keys remain immutable. Do not remove or rekey legacy records merely to standardize names or packaging. See [the maintenance guide](maintenance.md) for validation and delivery requirements.

## Evidence Backlog

- **SABIC**: Net mass / current package matrix verification
- **Creality**: Incomplete exact bindings and packaging matrices
- **eSUN**: Incomplete package/SKU bindings
- **MatterHackers**: Namespace ambiguity across product lines
- **FlashForge**: HS/Rapid variant and packaging ambiguity
- **Bambu Lab**: Remaining package and refill bindings
- **Prusament**: Recycled batch-color ambiguity
- **Raise3D**: Multi-weight identifier ambiguity

## Schema Backlog

- **Xioneer VXL**: Material and support filament schema support
- **eSUN**: Package-specific identifier extensions
- **Raise3D**: Multi-weight SKU binding schema support

## Recent Evidence and Identity Handoff — 2026-09-05

These findings were recorded during the evidence-maintenance audit ending at `6525b45630e7f313dea6cf39673ea0a95968386d`. The subsequent frontend/documentation commit `d3c4a04ceb18b8ccb63c5d88115e3aa5138c0838` did not change filament data. This section preserves that audit's evidence; it is not a claim that the linked catalogs were re-audited when this document was updated.

### Smartfil PLA BASIC — BLOCK_EVIDENCE / IDENTITY_REVIEW

- **Finding:** The [official PLA BASIC product](https://www.smartmaterials3d.com/en/pla-basic-filament) is distinct from standard PLA. The manufacturer-linked [TDS attachment](https://www.smartmaterials3d.com/en/index.php?controller=attachment&id_attachment=475) could not be retrieved during the audit. Existing Smartfil / Smart Materials naming also needs a physical-product comparison before importing anything.
- **To unblock:** Obtain the official TDS, including a manufacturer PDF supplied by the owner, and establish the exact family/color/package/identifier mapping against existing records. Do not reuse a generic PLA density, infer spool construction, or expand one verified SKU across other colors.
- **Accepted change in that audit:** None.

### Das Filament 1 kg refills — IDENTITY_DESIGN_REQUIRED

- **Finding:** The [official 1 kg spool/refill FAQ](https://dasfilament.de/2025/10/16/faq-zu-1-kg-spulen-und-1-kg-refills/) provides refill-construction evidence, including the absence of a cardboard core. Legacy PLA/PETG refill definitions retain cardboard/non-refill encoding. Changing their refill semantics changes generated public IDs under current compiler logic.
- **To unblock:** Design and explicitly approve an identity-safe correction/migration, with tests proving preservation of all historical public IDs and baseline keys. `legacy_id_spool_type` alone does not neutralize a change to refill status. Do not create duplicate refills as a workaround.
- **Accepted change in that audit:** None; legacy records preserved.

### NinjaTek Chinchilla — IDENTITY_DESIGN_REQUIRED

- **Finding:** The [official product page](https://ninjatek.com/shop/chinchilla/) and [TDS](https://ninjatek.com/wp-content/uploads/Chinchilla-TDS.pdf) describe a TPE blend; existing names/material identities use TPU.
- **Already completed:** Density 1.13 g/cc, nozzle guidance 225–235°C, matte finish and TDS link. Unsupported numeric bed endpoints were removed; the manufacturer gives a qualitative room-temperature lower bound. Do not repeat those corrections.
- **To unblock:** Establish how to represent the material terminology accurately without renaming/rekeying the historical TPU identities, then obtain approval for that design. No material or identity migration is currently authorized.

### Snapmaker TPU 90A — BLOCK_EVIDENCE

- **Finding:** Nozzle guidance on the [product page](https://shop.snapmaker.com/products/tpu-90a-filament-1kg) differs from the historical database range. The [official TDS V1.0.0](https://s3.us-west-2.amazonaws.com/snapmaker.com/download/manual/Snapmaker+TPU+90A+Technical+Data+Sheet+V1.0.0.pdf) was linked without overwriting the numerical range.
- **To unblock:** Reconcile the product page, the relevant TDS printing table, and the exact product generation. Apply only a supported ID-neutral metadata correction; do not overwrite previously approved data merely because one page differs.

### Snapmaker ASA — BLOCK_EVIDENCE / IDENTITY_REVIEW

- **Finding:** The [current product page](https://shop.snapmaker.com/products/asa-filament-1kg) and [TDS V1.0.1](https://s3.us-west-2.amazonaws.com/snapmaker.com/download/manual/Snapmaker+ASA+Technical+Data+Sheet+V1.0.1.pdf) differ from legacy plastic-generation records in technical guidance and Black naming.
- **To unblock:** Verify the generation/package matrix and whether Black corresponds to the existing Carbon Black identity. Do not blindly overwrite legacy specifications or create a duplicate color identity.
- **Accepted change in that audit:** None.

### Snapmaker PVA packaging — IDENTITY_REVIEW

- **Finding:** The [official PVA page](https://www.snapmaker.com/en/filaments/pva/) shows a current package that needs comparison against the existing unspecified-spool identity. Current imagery alone does not establish that an older public identity should be changed.
- **To unblock:** Establish an exact product-generation/package match and prove baseline preservation before proposing a packaging correction. Do not rekey a historical record or infer a second product solely from imagery.
- **Accepted change in that audit:** None.

### Recent no-delta checks

Snapmaker Matte PLA and SnapSpeed PLA were also inspected; no independently safe additional delta was accepted. This is not a claim of permanent worldwide completeness. Do not rerun those checks without a concrete new gap or evidence trigger.

## Kingroon PETG Basic evidence handoff — 2026-10-03

- **Accepted evidence:** The owner confirms that PETG and PETG Basic are separate product lines and approves the ten-color/SKU set contributed in [Community PR #65](https://github.com/Icezaza2543/SpoolmanDB-Community/pull/65). The [contributor's package-label photo](https://github.com/Icezaza2543/SpoolmanDB-Community/issues/66#issuecomment-5938025135) explicitly identifies PETG Basic White, SKU `NPETG088`, diameter 1.75 mm, nozzle 230–260°C and bed 70–90°C. The other nine SKU/color bindings are accepted contributor data, not independently photographed labels.
- **Current official page:** [Kingroon PETG Basic](https://kingroon.com/products/kingroon-petg-basic), checked in Chrome on this date, lists a 1 kg product, 1.75 mm technical guidance, density 1.26 g/cm³, nozzle 230–250°C and bed 70–90°C. The [10 kg pack page](https://kingroon.com/products/10kg-petg-filament-1-75mm-3d-print-materials) is the contributor's original source; 10 kg is the pack total, not the mass of one spool. This import is limited to the approved ten-color set, not every current selector option.
- **Implementation:** Two source definitions generate exactly ten 1 kg / 1.75 mm records. White is separated to retain its photographed 230–260°C nozzle range; the other nine use the current page's 230–250°C range. All ten use density 1.26. HEX swatches are representative contributor values, not official manufacturer HEX specifications. Spool material and tare remain unknown; no refill or legacy plastic-ID marker is introduced.

| Accepted color | SKU | New public ID |
| --- | --- | --- |
| Black | NPETG087 | `kingroon_petg_petgbasicblack_1000_175_n` |
| Dark Blue | NPETG019 | `kingroon_petg_petgbasicdarkblue_1000_175_n` |
| Green | NPETG018 | `kingroon_petg_petgbasicgreen_1000_175_n` |
| Grey | NPETG006 | `kingroon_petg_petgbasicgrey_1000_175_n` |
| Yellow | NPETG003 | `kingroon_petg_petgbasicyellow_1000_175_n` |
| Orange | NPETG017 | `kingroon_petg_petgbasicorange_1000_175_n` |
| Red | NPETG001 | `kingroon_petg_petgbasicred_1000_175_n` |
| Silver | NPETG016 | `kingroon_petg_petgbasicsilver_1000_175_n` |
| White | NPETG088 | `kingroon_petg_petgbasicwhite_1000_175_n` |
| Transparent | NPETG007 | `kingroon_petg_petgbasictransparent_1000_175_n` |

### Older generic PETG overlaps — HISTORICAL_ID_REVIEW

[Issue #66](https://github.com/Icezaza2543/SpoolmanDB-Community/issues/66) remains open for the overlapping historical `Kingroon PETG {color_name}` and `PETG {color_name}` groups. Adding the evidenced PETG Basic line does not resolve those older overlaps. All older definitions, metadata, public IDs and baseline keys are preserved; no rename, deletion, rekey or namespace consolidation is authorized by this import. Reopen that part only for an explicitly approved, identity-safe resolution.

## Protopasta duplicate-review deferrals — 2026-10-03

The owner approved and authorized local application of 38 other Protopasta duplicate groups (41 retirements), including the three Simply line/color bindings, but deferred the following four groups. Exact identities, approved mappings, printing-metadata evidence and document-link decisions are retained in the [review audit](audits/2026-10-03-protopasta-duplicate-review.json). The migration does not authorize changes to these deferred groups.

| Group | Preserved source pair | Blocker |
| --- | --- | --- |
| P004 | `protopasta_tpe_blackflexible_1000_175_c` / `protopasta_tpe_tpeblackflexible_1000_175_c` | Flexible qualifier is in the survivor family template versus the other source color; current Rule 5 decomposition rejects the mapping. |
| P012 | `protopasta_tpe_blackflexible_500_175_c` / `protopasta_tpe_tpeblackflexible_500_175_c` | Same Flexible line/color decomposition blocker. |
| P009 | `protopasta_pla_texasteablackwithgoldglitter_1000_175_c` / `protopasta_pla_platexasteablackwithgoldglitter_1000_175_c` | Glitter qualifier is in the survivor family template versus the other source color; current Rule 5 decomposition rejects the mapping. |
| P016 | `protopasta_pla_texasteablackwithgoldglitter_500_175_c` / `protopasta_pla_platexasteablackwithgoldglitter_500_175_c` | Same Glitter line/color decomposition blocker. |

No tooling change or retirement of these four groups is authorized now. All eight IDs remain intact. Recycled PETG and Recycled Carbon Fiber PETG density also remain unresolved: current base-line SDS documents report 1.2 g/cc but do not explicitly identify the RPET variants; the owner approved retaining survivor density 1.24 unresolved. P034/P041 printing values use owner-approved family-level PETG/PETG-CF7 material-table evidence, not an inferred temperature range. Current official product-line printing guidance is valid evidence without lot binding; exact lot binding is required only for packaging/spool/tare, which remain untouched. Wrong PLA/HTPLA document links were removed from these two recycled survivors; exact RPET documents remain an evidence gap.
