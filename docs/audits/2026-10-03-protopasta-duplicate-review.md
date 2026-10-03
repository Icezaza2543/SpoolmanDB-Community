# Protopasta approved duplicate migration and printing metadata

Date: 2026-10-03. Source/catalog base: `221035dc71d94b72c5837e6606eafa71df8a3976`.

Owner approval: 38 groups / 41 retired IDs, the three Simply line/color bindings, 19 printing fields on nine survivors, and correction/removal of eight wrong document links on four PETG survivors. P004/P009/P012/P016 are deferred. STEP 4 is authorized for local application and one focused data commit only; no push, main update or GitHub comments. Packaging/spool/tare and tooling remain unchanged.

The [review JSON](2026-10-03-protopasta-duplicate-review.json) contains every approved group, exact source records, keys, survivor, retired mapping, conflicts and the Simply bindings. Current official product-line printing guidance is valid evidence without production-lot binding; exact lot binding remains required only for packaging/spool/tare.

## Owner-approved printing metadata changes

| Group / survivor | Field | Old | Proposed new | Source / qualification |
| --- | --- | --- | --- | --- |
| P011 / `protopasta_petg_staticdissipativeblack_1000_175_c` | `density` | `1.24` | `1.2` | [source 1](https://proto-pasta.com/products/static-dissipative-petg), [source 2](https://proto-pasta.com/pages/material-data-table), [source 3](https://cdn.shopify.com/s/files/1/0717/9095/files/PETG_ESD.pdf?v=1773099686); Current product-specific manufacturer SDS, issued 2026-03-09, section 9: relative density 1.2 g/cc. SDS is not a guaranteed chemical specification. |
| P011 / `protopasta_petg_staticdissipativeblack_1000_175_c` | `extruder_temp_range` | `[195, 225]` | `[250, 290]` | [source 1](https://proto-pasta.com/products/static-dissipative-petg), [source 2](https://proto-pasta.com/pages/material-data-table), [source 3](https://cdn.shopify.com/s/files/1/0717/9095/files/PETGxxxx-ESD_TDS.pdf?v=1731010137); Manufacturer TDS issued 2024-11-01, currently linked: printing nozzle 250-290 C, up to 8 mm3/s. Do not use SDS melting point as printing range. |
| P011 / `protopasta_petg_staticdissipativeblack_1000_175_c` | `bed_temp` | `60` | `null` | [source 1](https://cdn.shopify.com/s/files/1/0717/9095/files/PETGxxxx-ESD_TDS.pdf?v=1731010137); Remove old scalar so it does not coexist with the supported range. |
| P011 / `protopasta_petg_staticdissipativeblack_1000_175_c` | `bed_temp_range` | `null` | `[70, 80]` | [source 1](https://cdn.shopify.com/s/files/1/0717/9095/files/PETGxxxx-ESD_TDS.pdf?v=1731010137); Same currently linked manufacturer TDS: bed 70-80 C. |
| P015 / `protopasta_petg_simplyclear_1000_175_c` | `extruder_temp` | `210` | `255` | [source 1](https://proto-pasta.com/products/simply-clear-petg); Product page explicitly recommends 255 C as a compromise; not a min/max range. Keep supported bed 70 C and density 1.2 unchanged. |
| P020 / `protopasta_petg_simplyblack_1000_175_c` | `extruder_temp` | `210` | `255` | [source 1](https://proto-pasta.com/products/simply-black-petg); Product page explicitly recommends 255 C as a compromise; not a min/max range. Keep supported bed 70 C and density 1.2 unchanged. |
| P022 / `protopasta_petg_simplyblack_3000_175_c` | `extruder_temp` | `210` | `255` | [source 1](https://proto-pasta.com/products/simply-black-petg); Product page explicitly recommends 255 C as a compromise; not a min/max range. Keep supported bed 70 C and density 1.2 unchanged. |
| P026 / `protopasta_petg_simplywhite_3000_175_c` | `extruder_temp` | `210` | `255` | [source 1](https://proto-pasta.com/products/simply-white-petg); Product page explicitly recommends 255 C as a compromise; not a min/max range. Keep supported bed 70 C and density 1.2 unchanged. |
| P028 / `protopasta_petg_staticdissipativeblack_500_175_c` | `density` | `1.24` | `1.2` | [source 1](https://proto-pasta.com/products/static-dissipative-petg), [source 2](https://proto-pasta.com/pages/material-data-table), [source 3](https://cdn.shopify.com/s/files/1/0717/9095/files/PETG_ESD.pdf?v=1773099686); Current product-specific manufacturer SDS, issued 2026-03-09, section 9: relative density 1.2 g/cc. SDS is not a guaranteed chemical specification. |
| P028 / `protopasta_petg_staticdissipativeblack_500_175_c` | `extruder_temp_range` | `[195, 225]` | `[250, 290]` | [source 1](https://proto-pasta.com/products/static-dissipative-petg), [source 2](https://proto-pasta.com/pages/material-data-table), [source 3](https://cdn.shopify.com/s/files/1/0717/9095/files/PETGxxxx-ESD_TDS.pdf?v=1731010137); Manufacturer TDS issued 2024-11-01, currently linked: printing nozzle 250-290 C, up to 8 mm3/s. Do not use SDS melting point as printing range. |
| P028 / `protopasta_petg_staticdissipativeblack_500_175_c` | `bed_temp` | `60` | `null` | [source 1](https://cdn.shopify.com/s/files/1/0717/9095/files/PETGxxxx-ESD_TDS.pdf?v=1731010137); Remove old scalar so it does not coexist with the supported range. |
| P028 / `protopasta_petg_staticdissipativeblack_500_175_c` | `bed_temp_range` | `null` | `[70, 80]` | [source 1](https://cdn.shopify.com/s/files/1/0717/9095/files/PETGxxxx-ESD_TDS.pdf?v=1731010137); Same currently linked manufacturer TDS: bed 70-80 C. |
| P034 / `protopasta_petg_recycledblack_1000_175_c` | `extruder_temp` | `null` | `250` | [source 1](https://proto-pasta.com/products/black-recycled-petg), [source 2](https://proto-pasta.com/pages/material-data-table); Owner-approved family-level PETG material-table point at 12 mm3/s, not a universal min/max or exact RPET-specific TDS. |
| P034 / `protopasta_petg_recycledblack_1000_175_c` | `extruder_temp_range` | `[195, 225]` | `null` | [source 1](https://proto-pasta.com/products/black-recycled-petg), [source 2](https://proto-pasta.com/pages/material-data-table); Remove unsupported PLA-default range 195-225 C; do not synthesize a range from flow-dependent points. |
| P034 / `protopasta_petg_recycledblack_1000_175_c` | `bed_temp` | `60` | `80` | [source 1](https://proto-pasta.com/products/black-recycled-petg), [source 2](https://proto-pasta.com/pages/material-data-table); Manufacturer PETG / Carbon Fiber PETG table point: 80 C plate, paired with 250 C at 12 mm3/s. |
| P038 / `protopasta_petg_simplywhite_1000_175_c` | `extruder_temp` | `210` | `255` | [source 1](https://proto-pasta.com/products/simply-white-petg); Product page explicitly recommends 255 C as a compromise; not a min/max range. Keep supported bed 70 C and density 1.2 unchanged. |
| P041 / `protopasta_petg_recycledcarbonfiberblack_1000_175_c` | `extruder_temp` | `null` | `250` | [source 1](https://proto-pasta.com/products/recycled-carbon-fiber-petg), [source 2](https://proto-pasta.com/pages/material-data-table); Owner-approved family-level PETG-CF7 material-table point at 12 mm3/s, not a universal min/max or exact RPET-CF7-specific TDS. |
| P041 / `protopasta_petg_recycledcarbonfiberblack_1000_175_c` | `extruder_temp_range` | `[195, 225]` | `null` | [source 1](https://proto-pasta.com/products/recycled-carbon-fiber-petg), [source 2](https://proto-pasta.com/pages/material-data-table); Remove unsupported PLA-default range 195-225 C; do not synthesize a range from flow-dependent points. |
| P041 / `protopasta_petg_recycledcarbonfiberblack_1000_175_c` | `bed_temp` | `60` | `80` | [source 1](https://proto-pasta.com/products/recycled-carbon-fiber-petg), [source 2](https://proto-pasta.com/pages/material-data-table); Manufacturer PETG / Carbon Fiber PETG table point: 80 C plate, paired with 250 C at 12 mm3/s. |

All nine records retain their exact historical ID and baseline key. Density and bed remain unchanged for Simply PETG. ESD scalar bed temperature is removed only to replace it with the TDS range. The owner explicitly approved P034/P041 as **family-level evidence from the PETG / PETG-CF7 material table**: 250 C at 12 mm3/s / 80 C plate, not an invented range. The table does not separately name RPET; recycled density remains 1.24 unresolved. This is printing/product-line evidence, not evidence of a production lot or a packaging change.

## Unresolved / retained

- `protopasta_petg_simplywhite_3000_175_c` / `lower_nozzle_endpoint`: retain `null`. White page says 235+ C in prose but 230+ C at 2 mm3/s in bullets. No lower endpoint/range proposed; explicit compromise point 255 C is unambiguous. [Official source](https://proto-pasta.com/products/simply-white-petg).
- `protopasta_petg_recycledblack_1000_175_c` / `density`: retain `1.24`, unresolved as explicitly approved by the owner. Current base PETG SDS says 1.2 g/cc but does not explicitly include RPET; no density transfer. [Contextual base-family source](https://cdn.shopify.com/s/files/1/0717/9095/files/PETG_Colors.pdf?v=1773099686), not an asserted RPET document link.
- `protopasta_petg_simplywhite_1000_175_c` / `lower_nozzle_endpoint`: retain `null`. White page says 235+ C in prose but 230+ C at 2 mm3/s in bullets. No lower endpoint/range proposed; explicit compromise point 255 C is unambiguous. [Official source](https://proto-pasta.com/products/simply-white-petg).
- `protopasta_petg_recycledcarbonfiberblack_1000_175_c` / `density`: retain `1.24`, unresolved as explicitly approved by the owner. Current base PETG-CF7 SDS says 1.2 g/cc but does not explicitly include RPET-CF7; no density transfer. [Contextual base-family source](https://cdn.shopify.com/s/files/1/0717/9095/files/PETG_CF7.pdf?v=1773099686), not an asserted RPET-CF7 document link.

## Owner-approved document-link corrections

The current official material table links exact PETG-ESD documents. Both URLs returned HTTP 200 and byte-identical SHA256 values to the reviewed manufacturer PDFs when rechecked before application. Current recycled product pages link the material table, but it provides only base PETG/PETG-CF7 SDS and no exact RPET TDS/SDS; therefore remove the wrong recycled PLA links instead of asserting unconfirmed safety-document coverage.

| Group / survivor | Field | Old link | Replacement |
| --- | --- | --- | --- |
| P011 / `protopasta_petg_staticdissipativeblack_1000_175_c` | `tds_url` | `PLA1xxxx-ESD_TDS.pdf?v=1731010137` | [PETGxxxx-ESD TDS](https://cdn.shopify.com/s/files/1/0717/9095/files/PETGxxxx-ESD_TDS.pdf?v=1731010137) |
| P011 / same survivor | `sds_url` | `PLA_ESD.pdf?v=1773099686` | [PETG-ESD SDS](https://cdn.shopify.com/s/files/1/0717/9095/files/PETG_ESD.pdf?v=1773099686) |
| P028 / `protopasta_petg_staticdissipativeblack_500_175_c` | `tds_url` | `PLA1xxxx-ESD_TDS.pdf?v=1731010137` | [PETGxxxx-ESD TDS](https://cdn.shopify.com/s/files/1/0717/9095/files/PETGxxxx-ESD_TDS.pdf?v=1731010137) |
| P028 / same survivor | `sds_url` | `PLA_ESD.pdf?v=1773099686` | [PETG-ESD SDS](https://cdn.shopify.com/s/files/1/0717/9095/files/PETG_ESD.pdf?v=1773099686) |
| P034 / `protopasta_petg_recycledblack_1000_175_c` | `tds_url` | `TDS__Translucent_Sparkly_HTPLA_1.0.0.pdf?1759` | Removed (`null`) |
| P034 / same survivor | `sds_url` | `PLA_Colors.pdf?v=1773099686` | Removed (`null`) |
| P041 / `protopasta_petg_recycledcarbonfiberblack_1000_175_c` | `tds_url` | `TDS__Translucent_Sparkly_HTPLA_1.0.0.pdf?1759` | Removed (`null`) |
| P041 / same survivor | `sds_url` | `PLA_Colors.pdf?v=1773099686` | Removed (`null`) |

Full old/new URLs are retained in the JSON audit's `document_link_changes`. These eight link-field changes are additional to the 19 approved printing fields.

## Deferred groups

| Group | IDs preserved | Reason |
| --- | --- | --- |
| P004 | `protopasta_tpe_blackflexible_1000_175_c`<br>`protopasta_tpe_tpeblackflexible_1000_175_c` | Rule 5 line/color decomposition differs because Flexible/Glitter is positioned in the source color versus the family template. No tooling change or retirement authorized now. |
| P009 | `protopasta_pla_platexasteablackwithgoldglitter_1000_175_c`<br>`protopasta_pla_texasteablackwithgoldglitter_1000_175_c` | Rule 5 line/color decomposition differs because Flexible/Glitter is positioned in the source color versus the family template. No tooling change or retirement authorized now. |
| P012 | `protopasta_tpe_blackflexible_500_175_c`<br>`protopasta_tpe_tpeblackflexible_500_175_c` | Rule 5 line/color decomposition differs because Flexible/Glitter is positioned in the source color versus the family template. No tooling change or retirement authorized now. |
| P016 | `protopasta_pla_platexasteablackwithgoldglitter_500_175_c`<br>`protopasta_pla_texasteablackwithgoldglitter_500_175_c` | Rule 5 line/color decomposition differs because Flexible/Glitter is positioned in the source color versus the family template. No tooling change or retirement authorized now. |

## Complete approved retired-ID list

| Group | Retired ID | Survivor | Rule |
| --- | --- | --- | --- |
| P001 | `protopasta_pla_basicplanatural_1000_175_c` | `protopasta_pla_basicnatural_1000_175_c` | 1 |
| P002 | `protopasta_pla_opaqueplawhite_3000_175_c` | `protopasta_pla_opaquewhite_3000_175_c` | 1 |
| P003 | `protopasta_pla_basicplawhite_1000_175_c` | `protopasta_pla_basicwhite_1000_175_c` | 1 |
| P005 | `protopasta_pla_recycledplablack_500_175_c` | `protopasta_pla_recycledblack_500_175_c` | 1 |
| P006 | `protopasta_pla_opaqueplared_1000_175_c` | `protopasta_pla_opaquered_1000_175_c` | 1 |
| P007 | `protopasta_pla_opaqueplablack_1000_175_c` | `protopasta_pla_opaqueblack_1000_175_c` | 1 |
| P008 | `protopasta_pla_opaqueplanatural_1000_175_c` | `protopasta_pla_opaquenatural_1000_175_c` | 1 |
| P010 | `protopasta_pla_plagreenglow-in-the-darknatural_500_175_c` | `protopasta_pla_greenglow-in-the-darknatural_500_175_c` | 1 |
| P011 | `protopasta_petg_staticdissipativepetgblack_1000_175_c` | `protopasta_petg_staticdissipativeblack_1000_175_c` | 1 |
| P013 | `protopasta_pla_basicplablack_1000_175_c` | `protopasta_pla_basicblack_1000_175_c` | 1 |
| P014 | `protopasta_pla_basicplablack_3000_175_c` | `protopasta_pla_basicblack_3000_175_c` | 1 |
| P015 | `protopasta_petg_petgsimplyclear_1000_175_c` | `protopasta_petg_simplyclear_1000_175_c` | 1 |
| P015 | `protopasta_petg_simplypetgclear_1000_175_c` | `protopasta_petg_simplyclear_1000_175_c` | 1 |
| P017 | `protopasta_pla_basicplawhite_3000_175_c` | `protopasta_pla_basicwhite_3000_175_c` | 1 |
| P018 | `protopasta_pla_staticdissipativeplablack_1000_175_c` | `protopasta_pla_staticdissipativeblack_1000_175_c` | 1 |
| P019 | `protopasta_pla_staticdissipativecarbonfiberplablack_500_175_c` | `protopasta_pla_staticdissipativecarbonfiberblack_500_175_c` | 1 |
| P020 | `protopasta_petg_petgsimplyblack_1000_175_c` | `protopasta_petg_simplyblack_1000_175_c` | 1 |
| P020 | `protopasta_petg_simplypetgblack_1000_175_c` | `protopasta_petg_simplyblack_1000_175_c` | 1 |
| P021 | `protopasta_pla_plagreenglow-in-the-darkyellow_500_175_c` | `protopasta_pla_greenglow-in-the-darkyellow_500_175_c` | 1 |
| P022 | `protopasta_petg_simplypetgblack_3000_175_c` | `protopasta_petg_simplyblack_3000_175_c` | 1 |
| P023 | `protopasta_pla_plagreenglow-in-the-darkwhite_500_175_c` | `protopasta_pla_greenglow-in-the-darkwhite_500_175_c` | 1 |
| P024 | `protopasta_pla_staticdissipativeplablack_500_175_c` | `protopasta_pla_staticdissipativeblack_500_175_c` | 1 |
| P025 | `protopasta_pla_opaqueplablack_3000_175_c` | `protopasta_pla_opaqueblack_3000_175_c` | 1 |
| P026 | `protopasta_petg_simplypetgwhite_3000_175_c` | `protopasta_petg_simplywhite_3000_175_c` | 1 |
| P027 | `protopasta_pla_plagreenglow-in-the-darkyellow_1000_175_c` | `protopasta_pla_greenglow-in-the-darkyellow_1000_175_c` | 1 |
| P028 | `protopasta_petg_staticdissipativepetgblack_500_175_c` | `protopasta_petg_staticdissipativeblack_500_175_c` | 1 |
| P029 | `protopasta_pla_plaautumnorange_500_175_c` | `protopasta_pla_autumnorange_500_175_c` | 1 |
| P030 | `protopasta_pla_staticdissipativecarbonfiberplablack_1000_175_c` | `protopasta_pla_staticdissipativecarbonfiberblack_1000_175_c` | 1 |
| P031 | `protopasta_pla_fluorescentplayellow_1000_175_c` | `protopasta_pla_fluorescentyellow_1000_175_c` | 1 |
| P032 | `protopasta_pla_fluorescentplayellow_500_175_c` | `protopasta_pla_fluorescentyellow_500_175_c` | 1 |
| P033 | `protopasta_pla_plagreenglow-in-the-darkwhite_1000_175_c` | `protopasta_pla_greenglow-in-the-darkwhite_1000_175_c` | 1 |
| P034 | `protopasta_petg_recycledpetgblack_1000_175_c` | `protopasta_petg_recycledblack_1000_175_c` | 1 |
| P035 | `protopasta_pla_opaqueplablue_1000_175_c` | `protopasta_pla_opaqueblue_1000_175_c` | 1 |
| P036 | `protopasta_pla_plaautumnorange_1000_175_c` | `protopasta_pla_autumnorange_1000_175_c` | 1 |
| P037 | `protopasta_pla_recycledplablack_1000_175_c` | `protopasta_pla_recycledblack_1000_175_c` | 1 |
| P038 | `protopasta_petg_petgsimplywhite_1000_175_c` | `protopasta_petg_simplywhite_1000_175_c` | 1 |
| P038 | `protopasta_petg_simplypetgwhite_1000_175_c` | `protopasta_petg_simplywhite_1000_175_c` | 1 |
| P039 | `protopasta_pla_opaqueplablue_3000_175_c` | `protopasta_pla_opaqueblue_3000_175_c` | 1 |
| P040 | `protopasta_pla_plagreenglow-in-the-darknatural_1000_175_c` | `protopasta_pla_greenglow-in-the-darknatural_1000_175_c` | 1 |
| P041 | `protopasta_petg_recycledpetgcarbonfiberblack_1000_175_c` | `protopasta_petg_recycledcarbonfiberblack_1000_175_c` | 1 |
| P042 | `protopasta_pla_opaqueplawhite_1000_175_c` | `protopasta_pla_opaquewhite_1000_175_c` | 1 |

## STEP 3 identity-only dry-run (before metadata approval)

- Compiled total: 53,084 -> 53,043; Protopasta: 889 -> 848.
- Registry: 350 -> 391; 41 approved retirements, 0 new IDs, 0 changed/rekeyed surviving identities.
- Protopasta SKU bindings: 234 -> 234, no lost binding; EAN bindings: 0 -> 0.
- Rule 4 did not decide any survivor; no Rule 4 Cartesian warning.
- Four deferred groups and all out-of-scope records are preserved. No data, baseline or registry changes have been applied.

## STEP 3 verification results (before metadata approval)

`python scripts/merge_duplicates.py --brand protopasta --review docs/audits/2026-10-03-protopasta-duplicate-review.json` exited 0 in dry-run mode. No `--apply` was used. The executable review contains the approved identities and Simply bindings, but `metadata: []`; the pending metadata values are not marked approved.

Independent in-memory schema/compiler verification of the proposed printing metadata passed:

- 38 approved groups / 41 hypothetical retirements; compiled 53,084 -> 53,043; Protopasta 889 -> 848; registry 350 -> 391.
- Nine non-PLA survivors / 19 exact printing-field changes across four existing survivor definitions; no additional metadata splits needed.
- Surviving IDs and baseline keys unchanged; new IDs, rekeys, duplicates, phantom entries and unintended variants: 0.
- SKU bindings 234 -> 234 with exact binding-set equality; all eight deferred-group records unchanged.
- Packaging/spool/tare changes: 0; all other compiled metadata unchanged except the 19 explicitly listed fields.
- Catalog/contract byte digest unchanged before/after the dry-run and simulation.

`python scripts/compile_id_baseline.py --strict --base-ref 221035d` exited 0 on the actual working-tree data: baseline/current/matched 53,084; added/removed/changed/rekeyed 0; registered retired 350. The hypothetical retirement and printing state has not been written to the source catalog or contracts. No commits, push or GitHub comments were made in this review round.

## STEP 4 applied-state verification

After the owner's separate metadata/document-link approval, the reviewed dry-run passed and `python scripts/merge_duplicates.py --brand protopasta --apply --review docs/audits/2026-10-03-protopasta-duplicate-review.json` exited 0. The working-tree migration was compared independently against immutable base `221035d`, not merely against its edited baseline:

- Compiled 53,084 -> 53,043; Protopasta 889 -> 848; registry 350 -> 391.
- Exactly 41 approved retirements; new, changed identity, rekeyed and unregistered removals: 0.
- Exactly 19 approved printing-field changes plus eight document-link changes on nine survivors; no other surviving compiled metadata changes.
- SKU bindings 234 -> 234 with exact binding-set equality; no lost codes.
- All eight deferred-group records and packaging/spool/tare unchanged; duplicate IDs, phantom entries and unintended Cartesian variants: 0.
- `python scripts/readme_snapshot.py --write` and `--check`, compilation, strict validation with `--base-ref 221035d`, pytest, Node display-name tests, stable, canary, projection and strict baseline passed. Canary reported no ExternalFilament field/type drift; projection accepted 53,043 records.

Validation invocation note: before commit, `validate.py --strict` without a base rejects newly retired IDs because its default comparison manifest is the edited baseline while its previous registry comes from HEAD. The existing supported `--base-ref 221035d` option supplies the immutable historical identities and passes; no tooling change or baseline override was made. The first pytest run passed 203 tests with one Windows cache-permission warning; the final full rerun with a separate task-local cache passed **203 tests in 19.75s without warnings**, without repository configuration changes.

Fresh-context read-only review independently confirmed the exact retirement, identity, metadata, SKU, packaging and registry deltas, matched the original audit records to base `221035d`, and verified all 11 evidence snapshot SHA256 values. Critical/Important/Minor findings: none. Verdict: ready for the authorized local data commit. Deferred Flexible/Glitter groups, recycled density/document gaps and family-level (not lot-specific) printing guidance remain qualified as recorded; no tooling, schema, test source or workflow changed.
