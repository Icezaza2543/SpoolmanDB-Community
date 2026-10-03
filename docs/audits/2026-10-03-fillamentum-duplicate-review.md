# Fillamentum approved duplicate migration

The owner approved F001–F120 as duplicates, keeping all survivor metadata. This tracked audit retains the original values and evidence; original unreviewed snapshots are explicitly historical.

Base: `e5e15c65934a92c99654b44d22a74e2926cdfe4a`. Upstream read-only comparison: `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`.
Audit digest: `af2a73cfc1b350ffde847569c7a851a3d1bcb8a883af1b749ac05f73ddffcb22`.

## Owner-approved outcome

Global 52,919 → 52,799; Fillamentum 244 → 124; registry 515 → 635. Retired 120, new/changed identity/rekeyed/unregistered removal 0/0/0/0. Codes/EAN/refill-EAN bindings and unique values 0 → 0; code-changed target IDs: empty.

F001–F060: ASA; F061–F120: PLA. Within material: exact color alphabetical, weight 750 then 2500 g, diameter 1.75 then 2.85 mm. All source records are plastic, refill=false. Each alias is one exact 2-record group, not a family-wide approval.

All 120 survivors are `Extrafill {color_name}` by Rule 1 (pinned upstream family); retirees are `ASA Extrafill {color_name}` or `PLA Extrafill {color_name}`. Rule 3 precedes Rule 4 in tooling. No Rule 4 decisions or Rule 4 Cartesian warnings. All four definitions use weight×diameter×color expansion; this is not evidence that every physical variant is current.

Current exact listed matrix matches: {"CURRENT_LISTED": 41, "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX": 79}. Missing current combinations are historical/current-unconfirmed, not asserted nonexistent. This duplicate review does not add any current 1 kg PLA products or delete unconfirmed unique variants.

## Source definitions

| Index | Template | Material | Weights | Diameters | Colors | Compiled |
| --- | --- | --- | --- | --- | ---: | ---: |
| 0 | `Extrafill {color_name}` | ASA | 750, 2500 | 1.75, 2.85 | 15 | 60 |
| 1 | `Extrafill {color_name}` | PLA | 750, 2500 | 1.75, 2.85 | 16 | 64 |
| 2 | `ASA Extrafill {color_name}` | ASA | 750, 2500 | 1.75, 2.85 | 15 | 60 |
| 3 | `PLA Extrafill {color_name}` | PLA | 750, 2500 | 1.75, 2.85 | 15 | 60 |

## Approved metadata disposition: retain survivor values

| Material | Field | Survivor | Retiree |
| --- | --- | --- | --- |
| ASA | density | 1.07 | 1.07 |
| ASA | nozzle | scalar 250 | range 240–255 |
| ASA | bed | scalar 95 | range 80–105 |
| PLA | density | 1.24 | 1.24 |
| PLA | nozzle | scalar 200 | range 190–210 |
| PLA | bed | scalar 55 | range 50–60 |
| Both | tare 750/2500 g | 230/590 | null/null |

No DB survivor carries the other material's defaults. Sixteen HEX conflicts (Concrete Grey, Peppered Mustard, Rapunzel Silver, Turquoise Blue ×4) are case-only; same RGB, keep survivor string. All exact per-ID values remain below and in the [reviewed JSON audit](2026-10-03-fillamentum-duplicate-review.json).

Current printing evidence is valid without lot binding, but conflicting documents must be explicit:

- [PLA TDS, page 1](https://fillamentum.com/wp-content/uploads/2020/10/Technical-Data-Sheet_PLA-Extrafill_03012019.pdf): density 1.24, nozzle 190–210, bed 50–60; 750 g tare 250. Source: supplied/current-linked PDF, page 1, physical/printing tables.
- [PLA guide 8/2024, page 1](https://fillamentum.com/wp-content/uploads/2024/10/PRINT_GUIDE_PLA_EXTRAFILL_8_2024.pdf): basic nozzle 190–210, bed 0–55; separate high-speed glossy/matte profiles. Detailed-view density 1.8 and resistance 180 C contradict TDS (possible template/copy error, not established); density update NOT proposed. Source: current manufacturer-linked PDF, page 1, setup and Detailed View.
- [ASA TDS, page 1](https://fillamentum.com/wp-content/uploads/2020/10/Technical-Data-Sheet_ASA-Extrafill_03012019.pdf): density 1.07, nozzle 240–255, bed 90–105. [Current family page](https://fillamentum.com/collections/asa-filament/) says bed 80–105. Source: current-linked PDF, page 1, physical/printing tables.
- [ASA guide 8/2024, page 1](https://fillamentum.com/wp-content/uploads/2025/08/3D_PRINTING_GUIDE_ASA_EXTRAFILL_8_2024.pdf): basic bed 65–75, tips bed 90–105 on the same page; high-speed 90–110. No universal union or guessed replacement. Source: current manufacturer-linked PDF, page 1, basic/high-speed/tips sections.
- Tare conflict: current family pages 230/590 g, current exact 750 g product pages 210 g, 2019 TDS 250 g for 750 g. No matching lot evidence; packaging/tare remain unchanged. Sustainable-spool wording/images alone do not authorize cardboard/refill conversion.
- Manufacturer [ASA family](https://fillamentum.com/collections/asa-filament/) caption Show White explicitly links to [Snow White](https://shop.fillamentum.com/products/asa-extrafill-snow-white). Preserve both DB source spellings/IDs; no rename proposed.

## Complete approved retired ID list

| Group | Material / color | g / mm | Survivor ID | Retire ID | Rule | Current matrix |
| --- | --- | --- | --- | --- | --- | --- |
| F001 | ASA / Anthracite Grey | 750 / 1.75 | `fillamentum_asa_extrafillanthracitegrey_750_175_p` | `fillamentum_asa_asaextrafillanthracitegrey_750_175_p` | R1 | CURRENT_LISTED |
| F002 | ASA / Anthracite Grey | 750 / 2.85 | `fillamentum_asa_extrafillanthracitegrey_750_285_p` | `fillamentum_asa_asaextrafillanthracitegrey_750_285_p` | R1 | CURRENT_LISTED |
| F003 | ASA / Anthracite Grey | 2500 / 1.75 | `fillamentum_asa_extrafillanthracitegrey_2500_175_p` | `fillamentum_asa_asaextrafillanthracitegrey_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F004 | ASA / Anthracite Grey | 2500 / 2.85 | `fillamentum_asa_extrafillanthracitegrey_2500_285_p` | `fillamentum_asa_asaextrafillanthracitegrey_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F005 | ASA / Dijon Mustard | 750 / 1.75 | `fillamentum_asa_extrafilldijonmustard_750_175_p` | `fillamentum_asa_asaextrafilldijonmustard_750_175_p` | R1 | CURRENT_LISTED |
| F006 | ASA / Dijon Mustard | 750 / 2.85 | `fillamentum_asa_extrafilldijonmustard_750_285_p` | `fillamentum_asa_asaextrafilldijonmustard_750_285_p` | R1 | CURRENT_LISTED |
| F007 | ASA / Dijon Mustard | 2500 / 1.75 | `fillamentum_asa_extrafilldijonmustard_2500_175_p` | `fillamentum_asa_asaextrafilldijonmustard_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F008 | ASA / Dijon Mustard | 2500 / 2.85 | `fillamentum_asa_extrafilldijonmustard_2500_285_p` | `fillamentum_asa_asaextrafilldijonmustard_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F009 | ASA / Green Grass | 750 / 1.75 | `fillamentum_asa_extrafillgreengrass_750_175_p` | `fillamentum_asa_asaextrafillgreengrass_750_175_p` | R1 | CURRENT_LISTED |
| F010 | ASA / Green Grass | 750 / 2.85 | `fillamentum_asa_extrafillgreengrass_750_285_p` | `fillamentum_asa_asaextrafillgreengrass_750_285_p` | R1 | CURRENT_LISTED |
| F011 | ASA / Green Grass | 2500 / 1.75 | `fillamentum_asa_extrafillgreengrass_2500_175_p` | `fillamentum_asa_asaextrafillgreengrass_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F012 | ASA / Green Grass | 2500 / 2.85 | `fillamentum_asa_extrafillgreengrass_2500_285_p` | `fillamentum_asa_asaextrafillgreengrass_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F013 | ASA / Grey Blue | 750 / 1.75 | `fillamentum_asa_extrafillgreyblue_750_175_p` | `fillamentum_asa_asaextrafillgreyblue_750_175_p` | R1 | CURRENT_LISTED |
| F014 | ASA / Grey Blue | 750 / 2.85 | `fillamentum_asa_extrafillgreyblue_750_285_p` | `fillamentum_asa_asaextrafillgreyblue_750_285_p` | R1 | CURRENT_LISTED |
| F015 | ASA / Grey Blue | 2500 / 1.75 | `fillamentum_asa_extrafillgreyblue_2500_175_p` | `fillamentum_asa_asaextrafillgreyblue_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F016 | ASA / Grey Blue | 2500 / 2.85 | `fillamentum_asa_extrafillgreyblue_2500_285_p` | `fillamentum_asa_asaextrafillgreyblue_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F017 | ASA / Metallic Grey | 750 / 1.75 | `fillamentum_asa_extrafillmetallicgrey_750_175_p` | `fillamentum_asa_asaextrafillmetallicgrey_750_175_p` | R1 | CURRENT_LISTED |
| F018 | ASA / Metallic Grey | 750 / 2.85 | `fillamentum_asa_extrafillmetallicgrey_750_285_p` | `fillamentum_asa_asaextrafillmetallicgrey_750_285_p` | R1 | CURRENT_LISTED |
| F019 | ASA / Metallic Grey | 2500 / 1.75 | `fillamentum_asa_extrafillmetallicgrey_2500_175_p` | `fillamentum_asa_asaextrafillmetallicgrey_2500_175_p` | R1 | CURRENT_LISTED |
| F020 | ASA / Metallic Grey | 2500 / 2.85 | `fillamentum_asa_extrafillmetallicgrey_2500_285_p` | `fillamentum_asa_asaextrafillmetallicgrey_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F021 | ASA / Natural | 750 / 1.75 | `fillamentum_asa_extrafillnatural_750_175_p` | `fillamentum_asa_asaextrafillnatural_750_175_p` | R1 | CURRENT_LISTED |
| F022 | ASA / Natural | 750 / 2.85 | `fillamentum_asa_extrafillnatural_750_285_p` | `fillamentum_asa_asaextrafillnatural_750_285_p` | R1 | CURRENT_LISTED |
| F023 | ASA / Natural | 2500 / 1.75 | `fillamentum_asa_extrafillnatural_2500_175_p` | `fillamentum_asa_asaextrafillnatural_2500_175_p` | R1 | CURRENT_LISTED |
| F024 | ASA / Natural | 2500 / 2.85 | `fillamentum_asa_extrafillnatural_2500_285_p` | `fillamentum_asa_asaextrafillnatural_2500_285_p` | R1 | CURRENT_LISTED |
| F025 | ASA / Show White | 750 / 1.75 | `fillamentum_asa_extrafillshowwhite_750_175_p` | `fillamentum_asa_asaextrafillshowwhite_750_175_p` | R1 | CURRENT_LISTED |
| F026 | ASA / Show White | 750 / 2.85 | `fillamentum_asa_extrafillshowwhite_750_285_p` | `fillamentum_asa_asaextrafillshowwhite_750_285_p` | R1 | CURRENT_LISTED |
| F027 | ASA / Show White | 2500 / 1.75 | `fillamentum_asa_extrafillshowwhite_2500_175_p` | `fillamentum_asa_asaextrafillshowwhite_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F028 | ASA / Show White | 2500 / 2.85 | `fillamentum_asa_extrafillshowwhite_2500_285_p` | `fillamentum_asa_asaextrafillshowwhite_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F029 | ASA / Sky Blue | 750 / 1.75 | `fillamentum_asa_extrafillskyblue_750_175_p` | `fillamentum_asa_asaextrafillskyblue_750_175_p` | R1 | CURRENT_LISTED |
| F030 | ASA / Sky Blue | 750 / 2.85 | `fillamentum_asa_extrafillskyblue_750_285_p` | `fillamentum_asa_asaextrafillskyblue_750_285_p` | R1 | CURRENT_LISTED |
| F031 | ASA / Sky Blue | 2500 / 1.75 | `fillamentum_asa_extrafillskyblue_2500_175_p` | `fillamentum_asa_asaextrafillskyblue_2500_175_p` | R1 | CURRENT_LISTED |
| F032 | ASA / Sky Blue | 2500 / 2.85 | `fillamentum_asa_extrafillskyblue_2500_285_p` | `fillamentum_asa_asaextrafillskyblue_2500_285_p` | R1 | CURRENT_LISTED |
| F033 | ASA / Traffic Black | 750 / 1.75 | `fillamentum_asa_extrafilltrafficblack_750_175_p` | `fillamentum_asa_asaextrafilltrafficblack_750_175_p` | R1 | CURRENT_LISTED |
| F034 | ASA / Traffic Black | 750 / 2.85 | `fillamentum_asa_extrafilltrafficblack_750_285_p` | `fillamentum_asa_asaextrafilltrafficblack_750_285_p` | R1 | CURRENT_LISTED |
| F035 | ASA / Traffic Black | 2500 / 1.75 | `fillamentum_asa_extrafilltrafficblack_2500_175_p` | `fillamentum_asa_asaextrafilltrafficblack_2500_175_p` | R1 | CURRENT_LISTED |
| F036 | ASA / Traffic Black | 2500 / 2.85 | `fillamentum_asa_extrafilltrafficblack_2500_285_p` | `fillamentum_asa_asaextrafilltrafficblack_2500_285_p` | R1 | CURRENT_LISTED |
| F037 | ASA / Traffic Red | 750 / 1.75 | `fillamentum_asa_extrafilltrafficred_750_175_p` | `fillamentum_asa_asaextrafilltrafficred_750_175_p` | R1 | CURRENT_LISTED |
| F038 | ASA / Traffic Red | 750 / 2.85 | `fillamentum_asa_extrafilltrafficred_750_285_p` | `fillamentum_asa_asaextrafilltrafficred_750_285_p` | R1 | CURRENT_LISTED |
| F039 | ASA / Traffic Red | 2500 / 1.75 | `fillamentum_asa_extrafilltrafficred_2500_175_p` | `fillamentum_asa_asaextrafilltrafficred_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F040 | ASA / Traffic Red | 2500 / 2.85 | `fillamentum_asa_extrafilltrafficred_2500_285_p` | `fillamentum_asa_asaextrafilltrafficred_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F041 | ASA / Traffic White | 750 / 1.75 | `fillamentum_asa_extrafilltrafficwhite_750_175_p` | `fillamentum_asa_asaextrafilltrafficwhite_750_175_p` | R1 | CURRENT_LISTED |
| F042 | ASA / Traffic White | 750 / 2.85 | `fillamentum_asa_extrafilltrafficwhite_750_285_p` | `fillamentum_asa_asaextrafilltrafficwhite_750_285_p` | R1 | CURRENT_LISTED |
| F043 | ASA / Traffic White | 2500 / 1.75 | `fillamentum_asa_extrafilltrafficwhite_2500_175_p` | `fillamentum_asa_asaextrafilltrafficwhite_2500_175_p` | R1 | CURRENT_LISTED |
| F044 | ASA / Traffic White | 2500 / 2.85 | `fillamentum_asa_extrafilltrafficwhite_2500_285_p` | `fillamentum_asa_asaextrafilltrafficwhite_2500_285_p` | R1 | CURRENT_LISTED |
| F045 | ASA / Traffic Yellow | 750 / 1.75 | `fillamentum_asa_extrafilltrafficyellow_750_175_p` | `fillamentum_asa_asaextrafilltrafficyellow_750_175_p` | R1 | CURRENT_LISTED |
| F046 | ASA / Traffic Yellow | 750 / 2.85 | `fillamentum_asa_extrafilltrafficyellow_750_285_p` | `fillamentum_asa_asaextrafilltrafficyellow_750_285_p` | R1 | CURRENT_LISTED |
| F047 | ASA / Traffic Yellow | 2500 / 1.75 | `fillamentum_asa_extrafilltrafficyellow_2500_175_p` | `fillamentum_asa_asaextrafilltrafficyellow_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F048 | ASA / Traffic Yellow | 2500 / 2.85 | `fillamentum_asa_extrafilltrafficyellow_2500_285_p` | `fillamentum_asa_asaextrafilltrafficyellow_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F049 | ASA / Vertigo Grey | 750 / 1.75 | `fillamentum_asa_extrafillvertigogrey_750_175_p` | `fillamentum_asa_asaextrafillvertigogrey_750_175_p` | R1 | CURRENT_LISTED |
| F050 | ASA / Vertigo Grey | 750 / 2.85 | `fillamentum_asa_extrafillvertigogrey_750_285_p` | `fillamentum_asa_asaextrafillvertigogrey_750_285_p` | R1 | CURRENT_LISTED |
| F051 | ASA / Vertigo Grey | 2500 / 1.75 | `fillamentum_asa_extrafillvertigogrey_2500_175_p` | `fillamentum_asa_asaextrafillvertigogrey_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F052 | ASA / Vertigo Grey | 2500 / 2.85 | `fillamentum_asa_extrafillvertigogrey_2500_285_p` | `fillamentum_asa_asaextrafillvertigogrey_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F053 | ASA / Vivid Pink | 750 / 1.75 | `fillamentum_asa_extrafillvividpink_750_175_p` | `fillamentum_asa_asaextrafillvividpink_750_175_p` | R1 | CURRENT_LISTED |
| F054 | ASA / Vivid Pink | 750 / 2.85 | `fillamentum_asa_extrafillvividpink_750_285_p` | `fillamentum_asa_asaextrafillvividpink_750_285_p` | R1 | CURRENT_LISTED |
| F055 | ASA / Vivid Pink | 2500 / 1.75 | `fillamentum_asa_extrafillvividpink_2500_175_p` | `fillamentum_asa_asaextrafillvividpink_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F056 | ASA / Vivid Pink | 2500 / 2.85 | `fillamentum_asa_extrafillvividpink_2500_285_p` | `fillamentum_asa_asaextrafillvividpink_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F057 | ASA / White Aluminium | 750 / 1.75 | `fillamentum_asa_extrafillwhitealuminium_750_175_p` | `fillamentum_asa_asaextrafillwhitealuminium_750_175_p` | R1 | CURRENT_LISTED |
| F058 | ASA / White Aluminium | 750 / 2.85 | `fillamentum_asa_extrafillwhitealuminium_750_285_p` | `fillamentum_asa_asaextrafillwhitealuminium_750_285_p` | R1 | CURRENT_LISTED |
| F059 | ASA / White Aluminium | 2500 / 1.75 | `fillamentum_asa_extrafillwhitealuminium_2500_175_p` | `fillamentum_asa_asaextrafillwhitealuminium_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F060 | ASA / White Aluminium | 2500 / 2.85 | `fillamentum_asa_extrafillwhitealuminium_2500_285_p` | `fillamentum_asa_asaextrafillwhitealuminium_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F061 | PLA / Cobalt Blue | 750 / 1.75 | `fillamentum_pla_extrafillcobaltblue_750_175_p` | `fillamentum_pla_plaextrafillcobaltblue_750_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F062 | PLA / Cobalt Blue | 750 / 2.85 | `fillamentum_pla_extrafillcobaltblue_750_285_p` | `fillamentum_pla_plaextrafillcobaltblue_750_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F063 | PLA / Cobalt Blue | 2500 / 1.75 | `fillamentum_pla_extrafillcobaltblue_2500_175_p` | `fillamentum_pla_plaextrafillcobaltblue_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F064 | PLA / Cobalt Blue | 2500 / 2.85 | `fillamentum_pla_extrafillcobaltblue_2500_285_p` | `fillamentum_pla_plaextrafillcobaltblue_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F065 | PLA / Concrete Grey | 750 / 1.75 | `fillamentum_pla_extrafillconcretegrey_750_175_p` | `fillamentum_pla_plaextrafillconcretegrey_750_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F066 | PLA / Concrete Grey | 750 / 2.85 | `fillamentum_pla_extrafillconcretegrey_750_285_p` | `fillamentum_pla_plaextrafillconcretegrey_750_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F067 | PLA / Concrete Grey | 2500 / 1.75 | `fillamentum_pla_extrafillconcretegrey_2500_175_p` | `fillamentum_pla_plaextrafillconcretegrey_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F068 | PLA / Concrete Grey | 2500 / 2.85 | `fillamentum_pla_extrafillconcretegrey_2500_285_p` | `fillamentum_pla_plaextrafillconcretegrey_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F069 | PLA / Everybody's Magenta | 750 / 1.75 | `fillamentum_pla_extrafilleverybody'smagenta_750_175_p` | `fillamentum_pla_plaextrafilleverybody'smagenta_750_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F070 | PLA / Everybody's Magenta | 750 / 2.85 | `fillamentum_pla_extrafilleverybody'smagenta_750_285_p` | `fillamentum_pla_plaextrafilleverybody'smagenta_750_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F071 | PLA / Everybody's Magenta | 2500 / 1.75 | `fillamentum_pla_extrafilleverybody'smagenta_2500_175_p` | `fillamentum_pla_plaextrafilleverybody'smagenta_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F072 | PLA / Everybody's Magenta | 2500 / 2.85 | `fillamentum_pla_extrafilleverybody'smagenta_2500_285_p` | `fillamentum_pla_plaextrafilleverybody'smagenta_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F073 | PLA / Green Grass | 750 / 1.75 | `fillamentum_pla_extrafillgreengrass_750_175_p` | `fillamentum_pla_plaextrafillgreengrass_750_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F074 | PLA / Green Grass | 750 / 2.85 | `fillamentum_pla_extrafillgreengrass_750_285_p` | `fillamentum_pla_plaextrafillgreengrass_750_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F075 | PLA / Green Grass | 2500 / 1.75 | `fillamentum_pla_extrafillgreengrass_2500_175_p` | `fillamentum_pla_plaextrafillgreengrass_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F076 | PLA / Green Grass | 2500 / 2.85 | `fillamentum_pla_extrafillgreengrass_2500_285_p` | `fillamentum_pla_plaextrafillgreengrass_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F077 | PLA / Metallic Grey | 750 / 1.75 | `fillamentum_pla_extrafillmetallicgrey_750_175_p` | `fillamentum_pla_plaextrafillmetallicgrey_750_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F078 | PLA / Metallic Grey | 750 / 2.85 | `fillamentum_pla_extrafillmetallicgrey_750_285_p` | `fillamentum_pla_plaextrafillmetallicgrey_750_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F079 | PLA / Metallic Grey | 2500 / 1.75 | `fillamentum_pla_extrafillmetallicgrey_2500_175_p` | `fillamentum_pla_plaextrafillmetallicgrey_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F080 | PLA / Metallic Grey | 2500 / 2.85 | `fillamentum_pla_extrafillmetallicgrey_2500_285_p` | `fillamentum_pla_plaextrafillmetallicgrey_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F081 | PLA / Natural | 750 / 1.75 | `fillamentum_pla_extrafillnatural_750_175_p` | `fillamentum_pla_plaextrafillnatural_750_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F082 | PLA / Natural | 750 / 2.85 | `fillamentum_pla_extrafillnatural_750_285_p` | `fillamentum_pla_plaextrafillnatural_750_285_p` | R1 | CURRENT_LISTED |
| F083 | PLA / Natural | 2500 / 1.75 | `fillamentum_pla_extrafillnatural_2500_175_p` | `fillamentum_pla_plaextrafillnatural_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F084 | PLA / Natural | 2500 / 2.85 | `fillamentum_pla_extrafillnatural_2500_285_p` | `fillamentum_pla_plaextrafillnatural_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F085 | PLA / Peppered Mustard | 750 / 1.75 | `fillamentum_pla_extrafillpepperedmustard_750_175_p` | `fillamentum_pla_plaextrafillpepperedmustard_750_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F086 | PLA / Peppered Mustard | 750 / 2.85 | `fillamentum_pla_extrafillpepperedmustard_750_285_p` | `fillamentum_pla_plaextrafillpepperedmustard_750_285_p` | R1 | CURRENT_LISTED |
| F087 | PLA / Peppered Mustard | 2500 / 1.75 | `fillamentum_pla_extrafillpepperedmustard_2500_175_p` | `fillamentum_pla_plaextrafillpepperedmustard_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F088 | PLA / Peppered Mustard | 2500 / 2.85 | `fillamentum_pla_extrafillpepperedmustard_2500_285_p` | `fillamentum_pla_plaextrafillpepperedmustard_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F089 | PLA / Rapunzel Silver | 750 / 1.75 | `fillamentum_pla_extrafillrapunzelsilver_750_175_p` | `fillamentum_pla_plaextrafillrapunzelsilver_750_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F090 | PLA / Rapunzel Silver | 750 / 2.85 | `fillamentum_pla_extrafillrapunzelsilver_750_285_p` | `fillamentum_pla_plaextrafillrapunzelsilver_750_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F091 | PLA / Rapunzel Silver | 2500 / 1.75 | `fillamentum_pla_extrafillrapunzelsilver_2500_175_p` | `fillamentum_pla_plaextrafillrapunzelsilver_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F092 | PLA / Rapunzel Silver | 2500 / 2.85 | `fillamentum_pla_extrafillrapunzelsilver_2500_285_p` | `fillamentum_pla_plaextrafillrapunzelsilver_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F093 | PLA / Sky Blue | 750 / 1.75 | `fillamentum_pla_extrafillskyblue_750_175_p` | `fillamentum_pla_plaextrafillskyblue_750_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F094 | PLA / Sky Blue | 750 / 2.85 | `fillamentum_pla_extrafillskyblue_750_285_p` | `fillamentum_pla_plaextrafillskyblue_750_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F095 | PLA / Sky Blue | 2500 / 1.75 | `fillamentum_pla_extrafillskyblue_2500_175_p` | `fillamentum_pla_plaextrafillskyblue_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F096 | PLA / Sky Blue | 2500 / 2.85 | `fillamentum_pla_extrafillskyblue_2500_285_p` | `fillamentum_pla_plaextrafillskyblue_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F097 | PLA / Traffic Black | 750 / 1.75 | `fillamentum_pla_extrafilltrafficblack_750_175_p` | `fillamentum_pla_plaextrafilltrafficblack_750_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F098 | PLA / Traffic Black | 750 / 2.85 | `fillamentum_pla_extrafilltrafficblack_750_285_p` | `fillamentum_pla_plaextrafilltrafficblack_750_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F099 | PLA / Traffic Black | 2500 / 1.75 | `fillamentum_pla_extrafilltrafficblack_2500_175_p` | `fillamentum_pla_plaextrafilltrafficblack_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F100 | PLA / Traffic Black | 2500 / 2.85 | `fillamentum_pla_extrafilltrafficblack_2500_285_p` | `fillamentum_pla_plaextrafilltrafficblack_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F101 | PLA / Traffic Red | 750 / 1.75 | `fillamentum_pla_extrafilltrafficred_750_175_p` | `fillamentum_pla_plaextrafilltrafficred_750_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F102 | PLA / Traffic Red | 750 / 2.85 | `fillamentum_pla_extrafilltrafficred_750_285_p` | `fillamentum_pla_plaextrafilltrafficred_750_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F103 | PLA / Traffic Red | 2500 / 1.75 | `fillamentum_pla_extrafilltrafficred_2500_175_p` | `fillamentum_pla_plaextrafilltrafficred_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F104 | PLA / Traffic Red | 2500 / 2.85 | `fillamentum_pla_extrafilltrafficred_2500_285_p` | `fillamentum_pla_plaextrafilltrafficred_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F105 | PLA / Traffic White | 750 / 1.75 | `fillamentum_pla_extrafilltrafficwhite_750_175_p` | `fillamentum_pla_plaextrafilltrafficwhite_750_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F106 | PLA / Traffic White | 750 / 2.85 | `fillamentum_pla_extrafilltrafficwhite_750_285_p` | `fillamentum_pla_plaextrafilltrafficwhite_750_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F107 | PLA / Traffic White | 2500 / 1.75 | `fillamentum_pla_extrafilltrafficwhite_2500_175_p` | `fillamentum_pla_plaextrafilltrafficwhite_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F108 | PLA / Traffic White | 2500 / 2.85 | `fillamentum_pla_extrafilltrafficwhite_2500_285_p` | `fillamentum_pla_plaextrafilltrafficwhite_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F109 | PLA / Traffic Yellow | 750 / 1.75 | `fillamentum_pla_extrafilltrafficyellow_750_175_p` | `fillamentum_pla_plaextrafilltrafficyellow_750_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F110 | PLA / Traffic Yellow | 750 / 2.85 | `fillamentum_pla_extrafilltrafficyellow_750_285_p` | `fillamentum_pla_plaextrafilltrafficyellow_750_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F111 | PLA / Traffic Yellow | 2500 / 1.75 | `fillamentum_pla_extrafilltrafficyellow_2500_175_p` | `fillamentum_pla_plaextrafilltrafficyellow_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F112 | PLA / Traffic Yellow | 2500 / 2.85 | `fillamentum_pla_extrafilltrafficyellow_2500_285_p` | `fillamentum_pla_plaextrafilltrafficyellow_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F113 | PLA / Turquoise Blue | 750 / 1.75 | `fillamentum_pla_extrafillturquoiseblue_750_175_p` | `fillamentum_pla_plaextrafillturquoiseblue_750_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F114 | PLA / Turquoise Blue | 750 / 2.85 | `fillamentum_pla_extrafillturquoiseblue_750_285_p` | `fillamentum_pla_plaextrafillturquoiseblue_750_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F115 | PLA / Turquoise Blue | 2500 / 1.75 | `fillamentum_pla_extrafillturquoiseblue_2500_175_p` | `fillamentum_pla_plaextrafillturquoiseblue_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F116 | PLA / Turquoise Blue | 2500 / 2.85 | `fillamentum_pla_extrafillturquoiseblue_2500_285_p` | `fillamentum_pla_plaextrafillturquoiseblue_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F117 | PLA / Vertigo Grey | 750 / 1.75 | `fillamentum_pla_extrafillvertigogrey_750_175_p` | `fillamentum_pla_plaextrafillvertigogrey_750_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F118 | PLA / Vertigo Grey | 750 / 2.85 | `fillamentum_pla_extrafillvertigogrey_750_285_p` | `fillamentum_pla_plaextrafillvertigogrey_750_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F119 | PLA / Vertigo Grey | 2500 / 1.75 | `fillamentum_pla_extrafillvertigogrey_2500_175_p` | `fillamentum_pla_plaextrafillvertigogrey_2500_175_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |
| F120 | PLA / Vertigo Grey | 2500 / 2.85 | `fillamentum_pla_extrafillvertigogrey_2500_285_p` | `fillamentum_pla_plaextrafillvertigogrey_2500_285_p` | R1 | CURRENT_UNCONFIRMED_HISTORICAL_MATRIX |

## Exact mappings, keys, conflicts and evidence per group

### F001

Group ID: `dup-a3572693c44ce7bb705208cf6a0eca381119819f120fa9a407f898956328c3de`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillanthracitegrey_750_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Anthracite Grey`, name `ASA Extrafill Anthracite Grey`.
- `fillamentum_asa_extrafillanthracitegrey_750_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Anthracite Grey`, name `Extrafill Anthracite Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillanthracitegrey_750_175_p": {
    "replaced_by": "fillamentum_asa_extrafillanthracitegrey_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Anthracite Grey::ASA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillanthracitegrey_750_175_p": null,
    "fillamentum_asa_extrafillanthracitegrey_750_175_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillanthracitegrey_750_175_p": null,
    "fillamentum_asa_extrafillanthracitegrey_750_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillanthracitegrey_750_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillanthracitegrey_750_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillanthracitegrey_750_175_p": null,
    "fillamentum_asa_extrafillanthracitegrey_750_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillanthracitegrey_750_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillanthracitegrey_750_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Anthracite Grey",
      "diameter": 1.75,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-anthracite-grey",
      "variant_title": "1.75 mm",
      "sku_as_listed": "8595632824107",
      "variant_id": 12233849602146,
      "available": false,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-anthracite-grey"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F002

Group ID: `dup-83f36cdc212d860eaf7e4b37c915a28d245497703cdae0c92e6b4ddd49c3ef4d`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillanthracitegrey_750_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Anthracite Grey`, name `ASA Extrafill Anthracite Grey`.
- `fillamentum_asa_extrafillanthracitegrey_750_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Anthracite Grey`, name `Extrafill Anthracite Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillanthracitegrey_750_285_p": {
    "replaced_by": "fillamentum_asa_extrafillanthracitegrey_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Anthracite Grey::ASA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillanthracitegrey_750_285_p": null,
    "fillamentum_asa_extrafillanthracitegrey_750_285_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillanthracitegrey_750_285_p": null,
    "fillamentum_asa_extrafillanthracitegrey_750_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillanthracitegrey_750_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillanthracitegrey_750_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillanthracitegrey_750_285_p": null,
    "fillamentum_asa_extrafillanthracitegrey_750_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillanthracitegrey_750_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillanthracitegrey_750_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Anthracite Grey",
      "diameter": 2.85,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-anthracite-grey",
      "variant_title": "2.85 mm",
      "sku_as_listed": "8595632825104",
      "variant_id": 12233849634914,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-anthracite-grey"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F003

Group ID: `dup-a22c7ef013a5d9fb9d0e6fc16d8c3e126bc1286eca4fa4ee8a39edd28e562fc4`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillanthracitegrey_2500_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Anthracite Grey`, name `ASA Extrafill Anthracite Grey`.
- `fillamentum_asa_extrafillanthracitegrey_2500_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Anthracite Grey`, name `Extrafill Anthracite Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillanthracitegrey_2500_175_p": {
    "replaced_by": "fillamentum_asa_extrafillanthracitegrey_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Anthracite Grey::ASA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillanthracitegrey_2500_175_p": null,
    "fillamentum_asa_extrafillanthracitegrey_2500_175_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillanthracitegrey_2500_175_p": null,
    "fillamentum_asa_extrafillanthracitegrey_2500_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillanthracitegrey_2500_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillanthracitegrey_2500_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillanthracitegrey_2500_175_p": null,
    "fillamentum_asa_extrafillanthracitegrey_2500_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillanthracitegrey_2500_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillanthracitegrey_2500_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-anthracite-grey"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F004

Group ID: `dup-c824db9fc9534f532492eea18d62f938847f5f05550a4a11808fdf12a51a4a75`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillanthracitegrey_2500_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Anthracite Grey`, name `ASA Extrafill Anthracite Grey`.
- `fillamentum_asa_extrafillanthracitegrey_2500_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Anthracite Grey`, name `Extrafill Anthracite Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillanthracitegrey_2500_285_p": {
    "replaced_by": "fillamentum_asa_extrafillanthracitegrey_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Anthracite Grey::ASA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillanthracitegrey_2500_285_p": null,
    "fillamentum_asa_extrafillanthracitegrey_2500_285_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillanthracitegrey_2500_285_p": null,
    "fillamentum_asa_extrafillanthracitegrey_2500_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillanthracitegrey_2500_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillanthracitegrey_2500_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillanthracitegrey_2500_285_p": null,
    "fillamentum_asa_extrafillanthracitegrey_2500_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillanthracitegrey_2500_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillanthracitegrey_2500_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-anthracite-grey"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F005

Group ID: `dup-ee80290f1d7ccee36c4626c22e6a878772c1615b43eb96b62552083b6dd4aea9`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilldijonmustard_750_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Dijon Mustard`, name `ASA Extrafill Dijon Mustard`.
- `fillamentum_asa_extrafilldijonmustard_750_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Dijon Mustard`, name `Extrafill Dijon Mustard`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilldijonmustard_750_175_p": {
    "replaced_by": "fillamentum_asa_extrafilldijonmustard_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Dijon Mustard::ASA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilldijonmustard_750_175_p": null,
    "fillamentum_asa_extrafilldijonmustard_750_175_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilldijonmustard_750_175_p": null,
    "fillamentum_asa_extrafilldijonmustard_750_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilldijonmustard_750_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilldijonmustard_750_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilldijonmustard_750_175_p": null,
    "fillamentum_asa_extrafilldijonmustard_750_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilldijonmustard_750_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilldijonmustard_750_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Dijon Mustard",
      "diameter": 1.75,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-dijon-mustard",
      "variant_title": "1.75 mm",
      "sku_as_listed": "8595632824220",
      "variant_id": 39289060425826,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-dijon-mustard"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F006

Group ID: `dup-4a11850d9e06608a2fddabe152158d06674f41e8eebadccf12b42b03ba2a55a1`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilldijonmustard_750_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Dijon Mustard`, name `ASA Extrafill Dijon Mustard`.
- `fillamentum_asa_extrafilldijonmustard_750_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Dijon Mustard`, name `Extrafill Dijon Mustard`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilldijonmustard_750_285_p": {
    "replaced_by": "fillamentum_asa_extrafilldijonmustard_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Dijon Mustard::ASA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilldijonmustard_750_285_p": null,
    "fillamentum_asa_extrafilldijonmustard_750_285_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilldijonmustard_750_285_p": null,
    "fillamentum_asa_extrafilldijonmustard_750_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilldijonmustard_750_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilldijonmustard_750_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilldijonmustard_750_285_p": null,
    "fillamentum_asa_extrafilldijonmustard_750_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilldijonmustard_750_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilldijonmustard_750_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Dijon Mustard",
      "diameter": 2.85,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-dijon-mustard",
      "variant_title": "2.85 mm",
      "sku_as_listed": "8595632825142",
      "variant_id": 39289060458594,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-dijon-mustard"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F007

Group ID: `dup-e468d1a5eecbede6ef59e93884b1182176b77887ba2c00f2b8bf324740bf007a`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilldijonmustard_2500_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Dijon Mustard`, name `ASA Extrafill Dijon Mustard`.
- `fillamentum_asa_extrafilldijonmustard_2500_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Dijon Mustard`, name `Extrafill Dijon Mustard`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilldijonmustard_2500_175_p": {
    "replaced_by": "fillamentum_asa_extrafilldijonmustard_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Dijon Mustard::ASA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilldijonmustard_2500_175_p": null,
    "fillamentum_asa_extrafilldijonmustard_2500_175_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilldijonmustard_2500_175_p": null,
    "fillamentum_asa_extrafilldijonmustard_2500_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilldijonmustard_2500_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilldijonmustard_2500_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilldijonmustard_2500_175_p": null,
    "fillamentum_asa_extrafilldijonmustard_2500_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilldijonmustard_2500_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilldijonmustard_2500_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-dijon-mustard"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F008

Group ID: `dup-d28c7d3d68f5be64e3a6aa452040f54382fd40b9ca704aba9ec265ea062b8156`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilldijonmustard_2500_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Dijon Mustard`, name `ASA Extrafill Dijon Mustard`.
- `fillamentum_asa_extrafilldijonmustard_2500_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Dijon Mustard`, name `Extrafill Dijon Mustard`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilldijonmustard_2500_285_p": {
    "replaced_by": "fillamentum_asa_extrafilldijonmustard_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Dijon Mustard::ASA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilldijonmustard_2500_285_p": null,
    "fillamentum_asa_extrafilldijonmustard_2500_285_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilldijonmustard_2500_285_p": null,
    "fillamentum_asa_extrafilldijonmustard_2500_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilldijonmustard_2500_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilldijonmustard_2500_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilldijonmustard_2500_285_p": null,
    "fillamentum_asa_extrafilldijonmustard_2500_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilldijonmustard_2500_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilldijonmustard_2500_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-dijon-mustard"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F009

Group ID: `dup-a0a919bbfbb369e6c7d8027209591798fab07ce244608e4848ad38895a664fbc`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillgreengrass_750_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Green Grass`, name `ASA Extrafill Green Grass`.
- `fillamentum_asa_extrafillgreengrass_750_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Green Grass`, name `Extrafill Green Grass`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillgreengrass_750_175_p": {
    "replaced_by": "fillamentum_asa_extrafillgreengrass_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Green Grass::ASA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillgreengrass_750_175_p": null,
    "fillamentum_asa_extrafillgreengrass_750_175_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillgreengrass_750_175_p": null,
    "fillamentum_asa_extrafillgreengrass_750_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillgreengrass_750_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillgreengrass_750_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillgreengrass_750_175_p": null,
    "fillamentum_asa_extrafillgreengrass_750_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillgreengrass_750_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillgreengrass_750_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Green Grass",
      "diameter": 1.75,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-green-grass",
      "variant_title": "1.75 mm",
      "sku_as_listed": "8595632824077",
      "variant_id": 15822607110,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-green-grass"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F010

Group ID: `dup-638163793fccc19294440cd2b67cbfb5ec42ac841211b37a4c9615897662fcc7`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillgreengrass_750_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Green Grass`, name `ASA Extrafill Green Grass`.
- `fillamentum_asa_extrafillgreengrass_750_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Green Grass`, name `Extrafill Green Grass`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillgreengrass_750_285_p": {
    "replaced_by": "fillamentum_asa_extrafillgreengrass_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Green Grass::ASA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillgreengrass_750_285_p": null,
    "fillamentum_asa_extrafillgreengrass_750_285_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillgreengrass_750_285_p": null,
    "fillamentum_asa_extrafillgreengrass_750_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillgreengrass_750_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillgreengrass_750_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillgreengrass_750_285_p": null,
    "fillamentum_asa_extrafillgreengrass_750_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillgreengrass_750_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillgreengrass_750_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Green Grass",
      "diameter": 2.85,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-green-grass",
      "variant_title": "2.85 mm",
      "sku_as_listed": "8595632825074",
      "variant_id": 15822607174,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-green-grass"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F011

Group ID: `dup-f2ced9fb8d46d197c8687343f645a2a9b4a2ec8820d641ff2cb45f7f217ad950`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillgreengrass_2500_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Green Grass`, name `ASA Extrafill Green Grass`.
- `fillamentum_asa_extrafillgreengrass_2500_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Green Grass`, name `Extrafill Green Grass`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillgreengrass_2500_175_p": {
    "replaced_by": "fillamentum_asa_extrafillgreengrass_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Green Grass::ASA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillgreengrass_2500_175_p": null,
    "fillamentum_asa_extrafillgreengrass_2500_175_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillgreengrass_2500_175_p": null,
    "fillamentum_asa_extrafillgreengrass_2500_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillgreengrass_2500_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillgreengrass_2500_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillgreengrass_2500_175_p": null,
    "fillamentum_asa_extrafillgreengrass_2500_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillgreengrass_2500_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillgreengrass_2500_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-green-grass"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F012

Group ID: `dup-a03853f7faef0ca2f02d69a48a1aa0c4a8e9c7b26912aa020d150b33ca2b557f`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillgreengrass_2500_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Green Grass`, name `ASA Extrafill Green Grass`.
- `fillamentum_asa_extrafillgreengrass_2500_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Green Grass`, name `Extrafill Green Grass`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillgreengrass_2500_285_p": {
    "replaced_by": "fillamentum_asa_extrafillgreengrass_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Green Grass::ASA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillgreengrass_2500_285_p": null,
    "fillamentum_asa_extrafillgreengrass_2500_285_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillgreengrass_2500_285_p": null,
    "fillamentum_asa_extrafillgreengrass_2500_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillgreengrass_2500_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillgreengrass_2500_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillgreengrass_2500_285_p": null,
    "fillamentum_asa_extrafillgreengrass_2500_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillgreengrass_2500_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillgreengrass_2500_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-green-grass"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F013

Group ID: `dup-45d1bb9e3fb496f17fd23719e3ec87b9da28e2e91b4782560fd072ac6e207676`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillgreyblue_750_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Grey Blue`, name `ASA Extrafill Grey Blue`.
- `fillamentum_asa_extrafillgreyblue_750_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Grey Blue`, name `Extrafill Grey Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillgreyblue_750_175_p": {
    "replaced_by": "fillamentum_asa_extrafillgreyblue_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Grey Blue::ASA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillgreyblue_750_175_p": null,
    "fillamentum_asa_extrafillgreyblue_750_175_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillgreyblue_750_175_p": null,
    "fillamentum_asa_extrafillgreyblue_750_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillgreyblue_750_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillgreyblue_750_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillgreyblue_750_175_p": null,
    "fillamentum_asa_extrafillgreyblue_750_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillgreyblue_750_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillgreyblue_750_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Grey Blue",
      "diameter": 1.75,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-grey-blue",
      "variant_title": "1.75 mm",
      "sku_as_listed": "8595632824084",
      "variant_id": 12233848881250,
      "available": false,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-grey-blue"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F014

Group ID: `dup-b20df69cfb217306c6304f7aab439e4fe1b789d434bbe2824fbbda124af471a4`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillgreyblue_750_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Grey Blue`, name `ASA Extrafill Grey Blue`.
- `fillamentum_asa_extrafillgreyblue_750_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Grey Blue`, name `Extrafill Grey Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillgreyblue_750_285_p": {
    "replaced_by": "fillamentum_asa_extrafillgreyblue_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Grey Blue::ASA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillgreyblue_750_285_p": null,
    "fillamentum_asa_extrafillgreyblue_750_285_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillgreyblue_750_285_p": null,
    "fillamentum_asa_extrafillgreyblue_750_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillgreyblue_750_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillgreyblue_750_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillgreyblue_750_285_p": null,
    "fillamentum_asa_extrafillgreyblue_750_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillgreyblue_750_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillgreyblue_750_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Grey Blue",
      "diameter": 2.85,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-grey-blue",
      "variant_title": "2.85 mm",
      "sku_as_listed": "8595632825081",
      "variant_id": 12233848914018,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-grey-blue"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F015

Group ID: `dup-568225b4bcd90604a3b794fb7b14c76dd664bf82e14b0db1e11e5197bb038f30`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillgreyblue_2500_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Grey Blue`, name `ASA Extrafill Grey Blue`.
- `fillamentum_asa_extrafillgreyblue_2500_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Grey Blue`, name `Extrafill Grey Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillgreyblue_2500_175_p": {
    "replaced_by": "fillamentum_asa_extrafillgreyblue_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Grey Blue::ASA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillgreyblue_2500_175_p": null,
    "fillamentum_asa_extrafillgreyblue_2500_175_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillgreyblue_2500_175_p": null,
    "fillamentum_asa_extrafillgreyblue_2500_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillgreyblue_2500_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillgreyblue_2500_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillgreyblue_2500_175_p": null,
    "fillamentum_asa_extrafillgreyblue_2500_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillgreyblue_2500_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillgreyblue_2500_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-grey-blue"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F016

Group ID: `dup-b2aeb63389610146471e99c61d71e976f1f96e5ee05c24a1f3b3e8d4df74b04c`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillgreyblue_2500_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Grey Blue`, name `ASA Extrafill Grey Blue`.
- `fillamentum_asa_extrafillgreyblue_2500_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Grey Blue`, name `Extrafill Grey Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillgreyblue_2500_285_p": {
    "replaced_by": "fillamentum_asa_extrafillgreyblue_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Grey Blue::ASA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillgreyblue_2500_285_p": null,
    "fillamentum_asa_extrafillgreyblue_2500_285_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillgreyblue_2500_285_p": null,
    "fillamentum_asa_extrafillgreyblue_2500_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillgreyblue_2500_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillgreyblue_2500_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillgreyblue_2500_285_p": null,
    "fillamentum_asa_extrafillgreyblue_2500_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillgreyblue_2500_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillgreyblue_2500_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-grey-blue"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F017

Group ID: `dup-ee15c0c4c654cf9e16c0bf2357d1857adaa660635d53aafb62dcc38344d66368`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillmetallicgrey_750_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Metallic Grey`, name `ASA Extrafill Metallic Grey`.
- `fillamentum_asa_extrafillmetallicgrey_750_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Metallic Grey`, name `Extrafill Metallic Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillmetallicgrey_750_175_p": {
    "replaced_by": "fillamentum_asa_extrafillmetallicgrey_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Metallic Grey::ASA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillmetallicgrey_750_175_p": null,
    "fillamentum_asa_extrafillmetallicgrey_750_175_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillmetallicgrey_750_175_p": null,
    "fillamentum_asa_extrafillmetallicgrey_750_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillmetallicgrey_750_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillmetallicgrey_750_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillmetallicgrey_750_175_p": null,
    "fillamentum_asa_extrafillmetallicgrey_750_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillmetallicgrey_750_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillmetallicgrey_750_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Metallic Grey",
      "diameter": 1.75,
      "weight": 750.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-metallic-grey",
      "variant_title": "1.75 mm / 750 g",
      "sku_as_listed": "8595632824046",
      "variant_id": 15822608390,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-metallic-grey"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F018

Group ID: `dup-c08975de8e24288ac46f37a80d9787de875557fb6d789c689e027d568f8b1302`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillmetallicgrey_750_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Metallic Grey`, name `ASA Extrafill Metallic Grey`.
- `fillamentum_asa_extrafillmetallicgrey_750_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Metallic Grey`, name `Extrafill Metallic Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillmetallicgrey_750_285_p": {
    "replaced_by": "fillamentum_asa_extrafillmetallicgrey_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Metallic Grey::ASA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillmetallicgrey_750_285_p": null,
    "fillamentum_asa_extrafillmetallicgrey_750_285_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillmetallicgrey_750_285_p": null,
    "fillamentum_asa_extrafillmetallicgrey_750_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillmetallicgrey_750_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillmetallicgrey_750_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillmetallicgrey_750_285_p": null,
    "fillamentum_asa_extrafillmetallicgrey_750_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillmetallicgrey_750_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillmetallicgrey_750_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Metallic Grey",
      "diameter": 2.85,
      "weight": 750.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-metallic-grey",
      "variant_title": "2.85 mm / 750 g",
      "sku_as_listed": "8595632825043",
      "variant_id": 15822608454,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-metallic-grey"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F019

Group ID: `dup-4444e65c0adc4482e395a33af41a4fff3d97deec4ef80e917586bd64b7f6fcd0`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillmetallicgrey_2500_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Metallic Grey`, name `ASA Extrafill Metallic Grey`.
- `fillamentum_asa_extrafillmetallicgrey_2500_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Metallic Grey`, name `Extrafill Metallic Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillmetallicgrey_2500_175_p": {
    "replaced_by": "fillamentum_asa_extrafillmetallicgrey_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Metallic Grey::ASA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillmetallicgrey_2500_175_p": null,
    "fillamentum_asa_extrafillmetallicgrey_2500_175_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillmetallicgrey_2500_175_p": null,
    "fillamentum_asa_extrafillmetallicgrey_2500_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillmetallicgrey_2500_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillmetallicgrey_2500_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillmetallicgrey_2500_175_p": null,
    "fillamentum_asa_extrafillmetallicgrey_2500_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillmetallicgrey_2500_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillmetallicgrey_2500_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Metallic Grey",
      "diameter": 1.75,
      "weight": 2500.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-metallic-grey",
      "variant_title": "1.75 mm / 2.5 Kg",
      "sku_as_listed": "8595632828174",
      "variant_id": 46802080301382,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-metallic-grey"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F020

Group ID: `dup-2fe1edfdf4c97f575a149495ce6a5d941fbf5fcd3d14cb2d2079a0329684840d`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillmetallicgrey_2500_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Metallic Grey`, name `ASA Extrafill Metallic Grey`.
- `fillamentum_asa_extrafillmetallicgrey_2500_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Metallic Grey`, name `Extrafill Metallic Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillmetallicgrey_2500_285_p": {
    "replaced_by": "fillamentum_asa_extrafillmetallicgrey_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Metallic Grey::ASA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillmetallicgrey_2500_285_p": null,
    "fillamentum_asa_extrafillmetallicgrey_2500_285_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillmetallicgrey_2500_285_p": null,
    "fillamentum_asa_extrafillmetallicgrey_2500_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillmetallicgrey_2500_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillmetallicgrey_2500_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillmetallicgrey_2500_285_p": null,
    "fillamentum_asa_extrafillmetallicgrey_2500_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillmetallicgrey_2500_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillmetallicgrey_2500_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-metallic-grey"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F021

Group ID: `dup-b330f4cc95c85462348ee6e1c595524e5604fc4002591a12d61235364f37d112`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillnatural_750_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Natural`, name `ASA Extrafill Natural`.
- `fillamentum_asa_extrafillnatural_750_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Natural`, name `Extrafill Natural`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillnatural_750_175_p": {
    "replaced_by": "fillamentum_asa_extrafillnatural_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Natural::ASA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillnatural_750_175_p": null,
    "fillamentum_asa_extrafillnatural_750_175_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillnatural_750_175_p": null,
    "fillamentum_asa_extrafillnatural_750_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillnatural_750_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillnatural_750_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillnatural_750_175_p": null,
    "fillamentum_asa_extrafillnatural_750_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillnatural_750_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillnatural_750_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Natural",
      "diameter": 1.75,
      "weight": 750.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-natural",
      "variant_title": "1.75 mm / 750 g",
      "sku_as_listed": "8595632824008",
      "variant_id": 2068215491,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-natural"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F022

Group ID: `dup-ff28080fdde84215c2a388a435838d6138585ade57c3eef0d1c00b6df5661ff9`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillnatural_750_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Natural`, name `ASA Extrafill Natural`.
- `fillamentum_asa_extrafillnatural_750_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Natural`, name `Extrafill Natural`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillnatural_750_285_p": {
    "replaced_by": "fillamentum_asa_extrafillnatural_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Natural::ASA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillnatural_750_285_p": null,
    "fillamentum_asa_extrafillnatural_750_285_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillnatural_750_285_p": null,
    "fillamentum_asa_extrafillnatural_750_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillnatural_750_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillnatural_750_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillnatural_750_285_p": null,
    "fillamentum_asa_extrafillnatural_750_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillnatural_750_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillnatural_750_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Natural",
      "diameter": 2.85,
      "weight": 750.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-natural",
      "variant_title": "2.85 mm / 750 g",
      "sku_as_listed": "8595632825005",
      "variant_id": 2068413571,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-natural"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F023

Group ID: `dup-202b86464a84977182ebfe78ba4c16a9e194508a130d8c0ef0f7ec83060690d8`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillnatural_2500_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Natural`, name `ASA Extrafill Natural`.
- `fillamentum_asa_extrafillnatural_2500_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Natural`, name `Extrafill Natural`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillnatural_2500_175_p": {
    "replaced_by": "fillamentum_asa_extrafillnatural_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Natural::ASA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillnatural_2500_175_p": null,
    "fillamentum_asa_extrafillnatural_2500_175_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillnatural_2500_175_p": null,
    "fillamentum_asa_extrafillnatural_2500_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillnatural_2500_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillnatural_2500_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillnatural_2500_175_p": null,
    "fillamentum_asa_extrafillnatural_2500_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillnatural_2500_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillnatural_2500_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Natural",
      "diameter": 1.75,
      "weight": 2500.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-natural",
      "variant_title": "1.75 mm / 2.5 Kg",
      "sku_as_listed": "8595632824213",
      "variant_id": 53604293214534,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-natural"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F024

Group ID: `dup-853b41ad42c9d2fdb5896d6b623432284829fae4180d37896dd262e079af0e17`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillnatural_2500_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Natural`, name `ASA Extrafill Natural`.
- `fillamentum_asa_extrafillnatural_2500_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Natural`, name `Extrafill Natural`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillnatural_2500_285_p": {
    "replaced_by": "fillamentum_asa_extrafillnatural_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Natural::ASA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillnatural_2500_285_p": null,
    "fillamentum_asa_extrafillnatural_2500_285_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillnatural_2500_285_p": null,
    "fillamentum_asa_extrafillnatural_2500_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillnatural_2500_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillnatural_2500_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillnatural_2500_285_p": null,
    "fillamentum_asa_extrafillnatural_2500_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillnatural_2500_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillnatural_2500_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Natural",
      "diameter": 2.85,
      "weight": 2500.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-natural",
      "variant_title": "2.85 mm / 2.5 Kg",
      "sku_as_listed": "8595632825135",
      "variant_id": 53604293247302,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-natural"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F025

Group ID: `dup-9e0bf8a74eb8e79ec9372fd4cdfa856763f661eb70a693584f483b6fec836ea3`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillshowwhite_750_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Show White`, name `ASA Extrafill Show White`.
- `fillamentum_asa_extrafillshowwhite_750_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Show White`, name `Extrafill Show White`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillshowwhite_750_175_p": {
    "replaced_by": "fillamentum_asa_extrafillshowwhite_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Show White::ASA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillshowwhite_750_175_p": null,
    "fillamentum_asa_extrafillshowwhite_750_175_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillshowwhite_750_175_p": null,
    "fillamentum_asa_extrafillshowwhite_750_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillshowwhite_750_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillshowwhite_750_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillshowwhite_750_175_p": null,
    "fillamentum_asa_extrafillshowwhite_750_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillshowwhite_750_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillshowwhite_750_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Snow White",
      "diameter": 1.75,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-snow-white",
      "variant_title": "1.75 mm",
      "sku_as_listed": "8595632824244",
      "variant_id": 39289150734434,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-snow-white"
  ],
  "alias": {
    "source_color": "Show White",
    "shop_color": "Snow White",
    "source": "https://fillamentum.com/collections/asa-filament/",
    "linked_product": "https://shop.fillamentum.com/collections/asa-filament/products/asa-extrafill-snow-white",
    "note": "Manufacturer family caption explicitly links to Snow White. No source name or ID rename proposed."
  },
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F026

Group ID: `dup-a15de5d45585e6cb4c85b432660c9436349693fa764923c8b957f204868ccf50`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillshowwhite_750_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Show White`, name `ASA Extrafill Show White`.
- `fillamentum_asa_extrafillshowwhite_750_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Show White`, name `Extrafill Show White`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillshowwhite_750_285_p": {
    "replaced_by": "fillamentum_asa_extrafillshowwhite_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Show White::ASA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillshowwhite_750_285_p": null,
    "fillamentum_asa_extrafillshowwhite_750_285_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillshowwhite_750_285_p": null,
    "fillamentum_asa_extrafillshowwhite_750_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillshowwhite_750_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillshowwhite_750_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillshowwhite_750_285_p": null,
    "fillamentum_asa_extrafillshowwhite_750_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillshowwhite_750_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillshowwhite_750_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Snow White",
      "diameter": 2.85,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-snow-white",
      "variant_title": "2.85 mm",
      "sku_as_listed": "8595632825166",
      "variant_id": 39289150767202,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-snow-white"
  ],
  "alias": {
    "source_color": "Show White",
    "shop_color": "Snow White",
    "source": "https://fillamentum.com/collections/asa-filament/",
    "linked_product": "https://shop.fillamentum.com/collections/asa-filament/products/asa-extrafill-snow-white",
    "note": "Manufacturer family caption explicitly links to Snow White. No source name or ID rename proposed."
  },
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F027

Group ID: `dup-6a30fb68d204e285493906ca6bf9f8bf215c888813c54d84f47a60fb03c57ac5`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillshowwhite_2500_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Show White`, name `ASA Extrafill Show White`.
- `fillamentum_asa_extrafillshowwhite_2500_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Show White`, name `Extrafill Show White`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillshowwhite_2500_175_p": {
    "replaced_by": "fillamentum_asa_extrafillshowwhite_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Show White::ASA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillshowwhite_2500_175_p": null,
    "fillamentum_asa_extrafillshowwhite_2500_175_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillshowwhite_2500_175_p": null,
    "fillamentum_asa_extrafillshowwhite_2500_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillshowwhite_2500_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillshowwhite_2500_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillshowwhite_2500_175_p": null,
    "fillamentum_asa_extrafillshowwhite_2500_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillshowwhite_2500_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillshowwhite_2500_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-snow-white"
  ],
  "alias": {
    "source_color": "Show White",
    "shop_color": "Snow White",
    "source": "https://fillamentum.com/collections/asa-filament/",
    "linked_product": "https://shop.fillamentum.com/collections/asa-filament/products/asa-extrafill-snow-white",
    "note": "Manufacturer family caption explicitly links to Snow White. No source name or ID rename proposed."
  },
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F028

Group ID: `dup-05abdad851067ceab900542ea8c1ea15517a351d6af1f247532cd0d621d01ac6`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillshowwhite_2500_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Show White`, name `ASA Extrafill Show White`.
- `fillamentum_asa_extrafillshowwhite_2500_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Show White`, name `Extrafill Show White`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillshowwhite_2500_285_p": {
    "replaced_by": "fillamentum_asa_extrafillshowwhite_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Show White::ASA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillshowwhite_2500_285_p": null,
    "fillamentum_asa_extrafillshowwhite_2500_285_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillshowwhite_2500_285_p": null,
    "fillamentum_asa_extrafillshowwhite_2500_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillshowwhite_2500_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillshowwhite_2500_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillshowwhite_2500_285_p": null,
    "fillamentum_asa_extrafillshowwhite_2500_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillshowwhite_2500_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillshowwhite_2500_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-snow-white"
  ],
  "alias": {
    "source_color": "Show White",
    "shop_color": "Snow White",
    "source": "https://fillamentum.com/collections/asa-filament/",
    "linked_product": "https://shop.fillamentum.com/collections/asa-filament/products/asa-extrafill-snow-white",
    "note": "Manufacturer family caption explicitly links to Snow White. No source name or ID rename proposed."
  },
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F029

Group ID: `dup-3c9aa059bdec297b6df67c0d5c17d3b81b39a849c19c7b869dbbfe544fac3e0f`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillskyblue_750_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Sky Blue`, name `ASA Extrafill Sky Blue`.
- `fillamentum_asa_extrafillskyblue_750_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Sky Blue`, name `Extrafill Sky Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillskyblue_750_175_p": {
    "replaced_by": "fillamentum_asa_extrafillskyblue_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Sky Blue::ASA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillskyblue_750_175_p": null,
    "fillamentum_asa_extrafillskyblue_750_175_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillskyblue_750_175_p": null,
    "fillamentum_asa_extrafillskyblue_750_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillskyblue_750_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillskyblue_750_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillskyblue_750_175_p": null,
    "fillamentum_asa_extrafillskyblue_750_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillskyblue_750_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillskyblue_750_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Sky Blue",
      "diameter": 1.75,
      "weight": 750.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-sky-blue",
      "variant_title": "1.75 mm / 750 g",
      "sku_as_listed": "8595632824053",
      "variant_id": 15822606278,
      "available": false,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-sky-blue"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F030

Group ID: `dup-fe5fa4f2aa0f26c1aa5abd301964b8f8f16d5d1eae854f113b7a921245cbdfe9`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillskyblue_750_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Sky Blue`, name `ASA Extrafill Sky Blue`.
- `fillamentum_asa_extrafillskyblue_750_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Sky Blue`, name `Extrafill Sky Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillskyblue_750_285_p": {
    "replaced_by": "fillamentum_asa_extrafillskyblue_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Sky Blue::ASA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillskyblue_750_285_p": null,
    "fillamentum_asa_extrafillskyblue_750_285_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillskyblue_750_285_p": null,
    "fillamentum_asa_extrafillskyblue_750_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillskyblue_750_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillskyblue_750_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillskyblue_750_285_p": null,
    "fillamentum_asa_extrafillskyblue_750_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillskyblue_750_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillskyblue_750_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Sky Blue",
      "diameter": 2.85,
      "weight": 750.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-sky-blue",
      "variant_title": "2.85 mm / 750 g",
      "sku_as_listed": "8595632825050",
      "variant_id": 15822606342,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-sky-blue"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F031

Group ID: `dup-cdeb67d01bf8b106ae344af2e85462312b44db00533f37c8a28f5a5b40a8a91e`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillskyblue_2500_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Sky Blue`, name `ASA Extrafill Sky Blue`.
- `fillamentum_asa_extrafillskyblue_2500_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Sky Blue`, name `Extrafill Sky Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillskyblue_2500_175_p": {
    "replaced_by": "fillamentum_asa_extrafillskyblue_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Sky Blue::ASA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillskyblue_2500_175_p": null,
    "fillamentum_asa_extrafillskyblue_2500_175_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillskyblue_2500_175_p": null,
    "fillamentum_asa_extrafillskyblue_2500_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillskyblue_2500_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillskyblue_2500_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillskyblue_2500_175_p": null,
    "fillamentum_asa_extrafillskyblue_2500_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillskyblue_2500_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillskyblue_2500_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Sky Blue",
      "diameter": 1.75,
      "weight": 2500.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-sky-blue",
      "variant_title": "1.75 mm / 2.5 Kg",
      "sku_as_listed": "8595632828167",
      "variant_id": 46802010997062,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-sky-blue"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F032

Group ID: `dup-bcbc45e20cf2872eeb770228899d70de09e7e19841d85c1d3d2a1b7b5d59349b`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillskyblue_2500_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Sky Blue`, name `ASA Extrafill Sky Blue`.
- `fillamentum_asa_extrafillskyblue_2500_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Sky Blue`, name `Extrafill Sky Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillskyblue_2500_285_p": {
    "replaced_by": "fillamentum_asa_extrafillskyblue_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Sky Blue::ASA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillskyblue_2500_285_p": null,
    "fillamentum_asa_extrafillskyblue_2500_285_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillskyblue_2500_285_p": null,
    "fillamentum_asa_extrafillskyblue_2500_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillskyblue_2500_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillskyblue_2500_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillskyblue_2500_285_p": null,
    "fillamentum_asa_extrafillskyblue_2500_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillskyblue_2500_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillskyblue_2500_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Sky Blue",
      "diameter": 2.85,
      "weight": 2500.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-sky-blue",
      "variant_title": "2.85 mm / 2.5 Kg",
      "sku_as_listed": "8595632829140",
      "variant_id": 55250369773894,
      "available": false,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-sky-blue"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F033

Group ID: `dup-9ad79e5b8fcb9482419a03e07b1e177628e1f65c5fe4918177443d476d7e3ade`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilltrafficblack_750_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Traffic Black`, name `ASA Extrafill Traffic Black`.
- `fillamentum_asa_extrafilltrafficblack_750_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Traffic Black`, name `Extrafill Traffic Black`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilltrafficblack_750_175_p": {
    "replaced_by": "fillamentum_asa_extrafilltrafficblack_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Traffic Black::ASA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilltrafficblack_750_175_p": null,
    "fillamentum_asa_extrafilltrafficblack_750_175_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilltrafficblack_750_175_p": null,
    "fillamentum_asa_extrafilltrafficblack_750_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilltrafficblack_750_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilltrafficblack_750_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilltrafficblack_750_175_p": null,
    "fillamentum_asa_extrafilltrafficblack_750_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilltrafficblack_750_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilltrafficblack_750_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Traffic Black",
      "diameter": 1.75,
      "weight": 750.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-traffic-black",
      "variant_title": "1.75 mm / 750 g",
      "sku_as_listed": "8595632824039",
      "variant_id": 15822601478,
      "available": false,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-traffic-black"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F034

Group ID: `dup-919577580681bdee5c47f5e24ce06455bcc759fb051658f3f8a594a9ab29244a`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilltrafficblack_750_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Traffic Black`, name `ASA Extrafill Traffic Black`.
- `fillamentum_asa_extrafilltrafficblack_750_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Traffic Black`, name `Extrafill Traffic Black`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilltrafficblack_750_285_p": {
    "replaced_by": "fillamentum_asa_extrafilltrafficblack_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Traffic Black::ASA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilltrafficblack_750_285_p": null,
    "fillamentum_asa_extrafilltrafficblack_750_285_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilltrafficblack_750_285_p": null,
    "fillamentum_asa_extrafilltrafficblack_750_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilltrafficblack_750_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilltrafficblack_750_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilltrafficblack_750_285_p": null,
    "fillamentum_asa_extrafilltrafficblack_750_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilltrafficblack_750_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilltrafficblack_750_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Traffic Black",
      "diameter": 2.85,
      "weight": 750.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-traffic-black",
      "variant_title": "2.85 mm / 750 g",
      "sku_as_listed": "8595632825036",
      "variant_id": 15822601542,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-traffic-black"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F035

Group ID: `dup-3a5d3d7ddde7982eb2fd3edbc03369921292269f6b94c31264d39578270774b3`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilltrafficblack_2500_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Traffic Black`, name `ASA Extrafill Traffic Black`.
- `fillamentum_asa_extrafilltrafficblack_2500_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Traffic Black`, name `Extrafill Traffic Black`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilltrafficblack_2500_175_p": {
    "replaced_by": "fillamentum_asa_extrafilltrafficblack_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Traffic Black::ASA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilltrafficblack_2500_175_p": null,
    "fillamentum_asa_extrafilltrafficblack_2500_175_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilltrafficblack_2500_175_p": null,
    "fillamentum_asa_extrafilltrafficblack_2500_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilltrafficblack_2500_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilltrafficblack_2500_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilltrafficblack_2500_175_p": null,
    "fillamentum_asa_extrafilltrafficblack_2500_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilltrafficblack_2500_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilltrafficblack_2500_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Traffic Black",
      "diameter": 1.75,
      "weight": 2500.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-traffic-black",
      "variant_title": "1.75 mm / 2.5 Kg",
      "sku_as_listed": "8595632824114",
      "variant_id": 29540521214050,
      "available": false,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-traffic-black"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F036

Group ID: `dup-a45a687b59d97e3743613315a8a758b655c013e91ed2c76cd24600c7272c5742`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilltrafficblack_2500_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Traffic Black`, name `ASA Extrafill Traffic Black`.
- `fillamentum_asa_extrafilltrafficblack_2500_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Traffic Black`, name `Extrafill Traffic Black`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilltrafficblack_2500_285_p": {
    "replaced_by": "fillamentum_asa_extrafilltrafficblack_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Traffic Black::ASA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilltrafficblack_2500_285_p": null,
    "fillamentum_asa_extrafilltrafficblack_2500_285_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilltrafficblack_2500_285_p": null,
    "fillamentum_asa_extrafilltrafficblack_2500_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilltrafficblack_2500_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilltrafficblack_2500_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilltrafficblack_2500_285_p": null,
    "fillamentum_asa_extrafilltrafficblack_2500_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilltrafficblack_2500_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilltrafficblack_2500_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Traffic Black",
      "diameter": 2.85,
      "weight": 2500.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-traffic-black",
      "variant_title": "2.85 mm / 2.5 Kg",
      "sku_as_listed": "8595632825111",
      "variant_id": 29540521312354,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-traffic-black"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F037

Group ID: `dup-83ca798751e231bf03cc79b48be4efd81b46f480270ef796022ed8fe8a3e76a8`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilltrafficred_750_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Traffic Red`, name `ASA Extrafill Traffic Red`.
- `fillamentum_asa_extrafilltrafficred_750_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Traffic Red`, name `Extrafill Traffic Red`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilltrafficred_750_175_p": {
    "replaced_by": "fillamentum_asa_extrafilltrafficred_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Traffic Red::ASA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilltrafficred_750_175_p": null,
    "fillamentum_asa_extrafilltrafficred_750_175_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilltrafficred_750_175_p": null,
    "fillamentum_asa_extrafilltrafficred_750_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilltrafficred_750_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilltrafficred_750_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilltrafficred_750_175_p": null,
    "fillamentum_asa_extrafilltrafficred_750_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilltrafficred_750_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilltrafficred_750_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Traffic Red",
      "diameter": 1.75,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-traffic-red",
      "variant_title": "1.75 mm",
      "sku_as_listed": "8595632824060",
      "variant_id": 15822603846,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-traffic-red"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F038

Group ID: `dup-5396064b4e24d70887f8e5d375c6ce0acaac3635d7de5b0bae824e614520a9ad`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilltrafficred_750_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Traffic Red`, name `ASA Extrafill Traffic Red`.
- `fillamentum_asa_extrafilltrafficred_750_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Traffic Red`, name `Extrafill Traffic Red`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilltrafficred_750_285_p": {
    "replaced_by": "fillamentum_asa_extrafilltrafficred_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Traffic Red::ASA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilltrafficred_750_285_p": null,
    "fillamentum_asa_extrafilltrafficred_750_285_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilltrafficred_750_285_p": null,
    "fillamentum_asa_extrafilltrafficred_750_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilltrafficred_750_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilltrafficred_750_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilltrafficred_750_285_p": null,
    "fillamentum_asa_extrafilltrafficred_750_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilltrafficred_750_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilltrafficred_750_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Traffic Red",
      "diameter": 2.85,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-traffic-red",
      "variant_title": "2.85 mm",
      "sku_as_listed": "8595632825067",
      "variant_id": 15822603910,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-traffic-red"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F039

Group ID: `dup-495661adffac0f97c543e4adb152090b75c5abe8822df7c11752b6013e5ec728`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilltrafficred_2500_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Traffic Red`, name `ASA Extrafill Traffic Red`.
- `fillamentum_asa_extrafilltrafficred_2500_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Traffic Red`, name `Extrafill Traffic Red`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilltrafficred_2500_175_p": {
    "replaced_by": "fillamentum_asa_extrafilltrafficred_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Traffic Red::ASA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilltrafficred_2500_175_p": null,
    "fillamentum_asa_extrafilltrafficred_2500_175_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilltrafficred_2500_175_p": null,
    "fillamentum_asa_extrafilltrafficred_2500_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilltrafficred_2500_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilltrafficred_2500_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilltrafficred_2500_175_p": null,
    "fillamentum_asa_extrafilltrafficred_2500_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilltrafficred_2500_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilltrafficred_2500_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-traffic-red"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F040

Group ID: `dup-209b538e91da1d7032841122697c8b61d878a2729d4d38dfa26231bb6c98122f`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilltrafficred_2500_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Traffic Red`, name `ASA Extrafill Traffic Red`.
- `fillamentum_asa_extrafilltrafficred_2500_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Traffic Red`, name `Extrafill Traffic Red`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilltrafficred_2500_285_p": {
    "replaced_by": "fillamentum_asa_extrafilltrafficred_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Traffic Red::ASA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilltrafficred_2500_285_p": null,
    "fillamentum_asa_extrafilltrafficred_2500_285_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilltrafficred_2500_285_p": null,
    "fillamentum_asa_extrafilltrafficred_2500_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilltrafficred_2500_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilltrafficred_2500_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilltrafficred_2500_285_p": null,
    "fillamentum_asa_extrafilltrafficred_2500_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilltrafficred_2500_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilltrafficred_2500_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-traffic-red"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F041

Group ID: `dup-10142ff5e4fe838dea07433a38527878a111dc28a4d1ec617105c2ae14f3296f`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilltrafficwhite_750_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Traffic White`, name `ASA Extrafill Traffic White`.
- `fillamentum_asa_extrafilltrafficwhite_750_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Traffic White`, name `Extrafill Traffic White`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilltrafficwhite_750_175_p": {
    "replaced_by": "fillamentum_asa_extrafilltrafficwhite_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Traffic White::ASA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilltrafficwhite_750_175_p": null,
    "fillamentum_asa_extrafilltrafficwhite_750_175_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilltrafficwhite_750_175_p": null,
    "fillamentum_asa_extrafilltrafficwhite_750_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilltrafficwhite_750_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilltrafficwhite_750_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilltrafficwhite_750_175_p": null,
    "fillamentum_asa_extrafilltrafficwhite_750_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilltrafficwhite_750_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilltrafficwhite_750_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Traffic White",
      "diameter": 1.75,
      "weight": 750.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-traffic-white",
      "variant_title": "1.75 mm / 750 g",
      "sku_as_listed": "8595632824015",
      "variant_id": 15822597510,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-traffic-white"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F042

Group ID: `dup-0f72c452e62f7b6befa7d29ccfa6a2f5c99b7f5c787870728a4ac61c058a2400`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilltrafficwhite_750_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Traffic White`, name `ASA Extrafill Traffic White`.
- `fillamentum_asa_extrafilltrafficwhite_750_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Traffic White`, name `Extrafill Traffic White`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilltrafficwhite_750_285_p": {
    "replaced_by": "fillamentum_asa_extrafilltrafficwhite_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Traffic White::ASA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilltrafficwhite_750_285_p": null,
    "fillamentum_asa_extrafilltrafficwhite_750_285_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilltrafficwhite_750_285_p": null,
    "fillamentum_asa_extrafilltrafficwhite_750_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilltrafficwhite_750_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilltrafficwhite_750_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilltrafficwhite_750_285_p": null,
    "fillamentum_asa_extrafilltrafficwhite_750_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilltrafficwhite_750_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilltrafficwhite_750_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Traffic White",
      "diameter": 2.85,
      "weight": 750.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-traffic-white",
      "variant_title": "2.85 mm / 750 g",
      "sku_as_listed": "8595632825029",
      "variant_id": 15822597574,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-traffic-white"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F043

Group ID: `dup-f7bd3d20914fec1dacfd0ae1830d99d826b8984a5b6677141f454e5baedadc00`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilltrafficwhite_2500_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Traffic White`, name `ASA Extrafill Traffic White`.
- `fillamentum_asa_extrafilltrafficwhite_2500_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Traffic White`, name `Extrafill Traffic White`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilltrafficwhite_2500_175_p": {
    "replaced_by": "fillamentum_asa_extrafilltrafficwhite_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Traffic White::ASA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilltrafficwhite_2500_175_p": null,
    "fillamentum_asa_extrafilltrafficwhite_2500_175_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilltrafficwhite_2500_175_p": null,
    "fillamentum_asa_extrafilltrafficwhite_2500_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilltrafficwhite_2500_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilltrafficwhite_2500_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilltrafficwhite_2500_175_p": null,
    "fillamentum_asa_extrafilltrafficwhite_2500_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilltrafficwhite_2500_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilltrafficwhite_2500_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Traffic White",
      "diameter": 1.75,
      "weight": 2500.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-traffic-white",
      "variant_title": "1.75 mm / 2.5 Kg",
      "sku_as_listed": "8595632824121",
      "variant_id": 29540517937250,
      "available": false,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-traffic-white"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F044

Group ID: `dup-6ce25c376ecc608f052233713129ed769554476e40ab27a12a1f5afde36c72cb`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilltrafficwhite_2500_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Traffic White`, name `ASA Extrafill Traffic White`.
- `fillamentum_asa_extrafilltrafficwhite_2500_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Traffic White`, name `Extrafill Traffic White`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilltrafficwhite_2500_285_p": {
    "replaced_by": "fillamentum_asa_extrafilltrafficwhite_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Traffic White::ASA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilltrafficwhite_2500_285_p": null,
    "fillamentum_asa_extrafilltrafficwhite_2500_285_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilltrafficwhite_2500_285_p": null,
    "fillamentum_asa_extrafilltrafficwhite_2500_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilltrafficwhite_2500_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilltrafficwhite_2500_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilltrafficwhite_2500_285_p": null,
    "fillamentum_asa_extrafilltrafficwhite_2500_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilltrafficwhite_2500_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilltrafficwhite_2500_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Traffic White",
      "diameter": 2.85,
      "weight": 2500.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-traffic-white",
      "variant_title": "2.85 mm / 2.5 Kg",
      "sku_as_listed": "8595632825128",
      "variant_id": 29540518985826,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-traffic-white"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F045

Group ID: `dup-9a2c2ab3ed254d324ba05ddbff6029eb66a57f313d97125b80c3467f7bc0c21d`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilltrafficyellow_750_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Traffic Yellow`, name `ASA Extrafill Traffic Yellow`.
- `fillamentum_asa_extrafilltrafficyellow_750_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Traffic Yellow`, name `Extrafill Traffic Yellow`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilltrafficyellow_750_175_p": {
    "replaced_by": "fillamentum_asa_extrafilltrafficyellow_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Traffic Yellow::ASA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilltrafficyellow_750_175_p": null,
    "fillamentum_asa_extrafilltrafficyellow_750_175_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilltrafficyellow_750_175_p": null,
    "fillamentum_asa_extrafilltrafficyellow_750_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilltrafficyellow_750_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilltrafficyellow_750_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilltrafficyellow_750_175_p": null,
    "fillamentum_asa_extrafilltrafficyellow_750_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilltrafficyellow_750_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilltrafficyellow_750_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Traffic Yellow",
      "diameter": 1.75,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-traffic-yellow",
      "variant_title": "1.75 mm",
      "sku_as_listed": "8595632824022",
      "variant_id": 15822604486,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-traffic-yellow"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F046

Group ID: `dup-e776dcef017f43b13c2d9fbf0bcc904a7a19f83c9447800f01bb2a66d6bee0d6`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilltrafficyellow_750_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Traffic Yellow`, name `ASA Extrafill Traffic Yellow`.
- `fillamentum_asa_extrafilltrafficyellow_750_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Traffic Yellow`, name `Extrafill Traffic Yellow`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilltrafficyellow_750_285_p": {
    "replaced_by": "fillamentum_asa_extrafilltrafficyellow_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Traffic Yellow::ASA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilltrafficyellow_750_285_p": null,
    "fillamentum_asa_extrafilltrafficyellow_750_285_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilltrafficyellow_750_285_p": null,
    "fillamentum_asa_extrafilltrafficyellow_750_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilltrafficyellow_750_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilltrafficyellow_750_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilltrafficyellow_750_285_p": null,
    "fillamentum_asa_extrafilltrafficyellow_750_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilltrafficyellow_750_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilltrafficyellow_750_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Traffic Yellow",
      "diameter": 2.85,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-traffic-yellow",
      "variant_title": "2.85 mm",
      "sku_as_listed": "8595632825012",
      "variant_id": 15822604550,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-traffic-yellow"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F047

Group ID: `dup-89ff0b3ff553a4329412c64d5728cc8c9da209b7378c17744318607d27694fc7`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilltrafficyellow_2500_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Traffic Yellow`, name `ASA Extrafill Traffic Yellow`.
- `fillamentum_asa_extrafilltrafficyellow_2500_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Traffic Yellow`, name `Extrafill Traffic Yellow`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilltrafficyellow_2500_175_p": {
    "replaced_by": "fillamentum_asa_extrafilltrafficyellow_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Traffic Yellow::ASA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilltrafficyellow_2500_175_p": null,
    "fillamentum_asa_extrafilltrafficyellow_2500_175_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilltrafficyellow_2500_175_p": null,
    "fillamentum_asa_extrafilltrafficyellow_2500_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilltrafficyellow_2500_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilltrafficyellow_2500_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilltrafficyellow_2500_175_p": null,
    "fillamentum_asa_extrafilltrafficyellow_2500_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilltrafficyellow_2500_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilltrafficyellow_2500_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-traffic-yellow"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F048

Group ID: `dup-646e4ccfb9ce608df43ffd06c2309d50aa107230dc7120c6c51f84526db4505f`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafilltrafficyellow_2500_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Traffic Yellow`, name `ASA Extrafill Traffic Yellow`.
- `fillamentum_asa_extrafilltrafficyellow_2500_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Traffic Yellow`, name `Extrafill Traffic Yellow`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafilltrafficyellow_2500_285_p": {
    "replaced_by": "fillamentum_asa_extrafilltrafficyellow_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Traffic Yellow::ASA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafilltrafficyellow_2500_285_p": null,
    "fillamentum_asa_extrafilltrafficyellow_2500_285_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafilltrafficyellow_2500_285_p": null,
    "fillamentum_asa_extrafilltrafficyellow_2500_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafilltrafficyellow_2500_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafilltrafficyellow_2500_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafilltrafficyellow_2500_285_p": null,
    "fillamentum_asa_extrafilltrafficyellow_2500_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafilltrafficyellow_2500_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafilltrafficyellow_2500_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-traffic-yellow"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F049

Group ID: `dup-dbf3f1baf545d1a05b0726d00079046864c7e7e9b63fa83c04cc5cbdb6908141`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillvertigogrey_750_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Vertigo Grey`, name `ASA Extrafill Vertigo Grey`.
- `fillamentum_asa_extrafillvertigogrey_750_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Vertigo Grey`, name `Extrafill Vertigo Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillvertigogrey_750_175_p": {
    "replaced_by": "fillamentum_asa_extrafillvertigogrey_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Vertigo Grey::ASA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillvertigogrey_750_175_p": null,
    "fillamentum_asa_extrafillvertigogrey_750_175_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillvertigogrey_750_175_p": null,
    "fillamentum_asa_extrafillvertigogrey_750_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillvertigogrey_750_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillvertigogrey_750_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillvertigogrey_750_175_p": null,
    "fillamentum_asa_extrafillvertigogrey_750_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillvertigogrey_750_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillvertigogrey_750_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Vertigo Grey",
      "diameter": 1.75,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-vertigo-grey",
      "variant_title": "1.75 mm",
      "sku_as_listed": "8595632824251",
      "variant_id": 39289141854306,
      "available": false,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-vertigo-grey"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F050

Group ID: `dup-74d579e6723a25c4b26c8cc6402480fff49cc71bef4b87731683eb613384769c`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillvertigogrey_750_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Vertigo Grey`, name `ASA Extrafill Vertigo Grey`.
- `fillamentum_asa_extrafillvertigogrey_750_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Vertigo Grey`, name `Extrafill Vertigo Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillvertigogrey_750_285_p": {
    "replaced_by": "fillamentum_asa_extrafillvertigogrey_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Vertigo Grey::ASA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillvertigogrey_750_285_p": null,
    "fillamentum_asa_extrafillvertigogrey_750_285_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillvertigogrey_750_285_p": null,
    "fillamentum_asa_extrafillvertigogrey_750_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillvertigogrey_750_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillvertigogrey_750_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillvertigogrey_750_285_p": null,
    "fillamentum_asa_extrafillvertigogrey_750_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillvertigogrey_750_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillvertigogrey_750_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Vertigo Grey",
      "diameter": 2.85,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-vertigo-grey",
      "variant_title": "2.85 mm",
      "sku_as_listed": "8595632825173",
      "variant_id": 39289141887074,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-vertigo-grey"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F051

Group ID: `dup-601685ba39e7bb0de573dc73f6e9dc2720705f14bda11b44e75496d8c940b2dc`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillvertigogrey_2500_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Vertigo Grey`, name `ASA Extrafill Vertigo Grey`.
- `fillamentum_asa_extrafillvertigogrey_2500_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Vertigo Grey`, name `Extrafill Vertigo Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillvertigogrey_2500_175_p": {
    "replaced_by": "fillamentum_asa_extrafillvertigogrey_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Vertigo Grey::ASA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillvertigogrey_2500_175_p": null,
    "fillamentum_asa_extrafillvertigogrey_2500_175_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillvertigogrey_2500_175_p": null,
    "fillamentum_asa_extrafillvertigogrey_2500_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillvertigogrey_2500_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillvertigogrey_2500_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillvertigogrey_2500_175_p": null,
    "fillamentum_asa_extrafillvertigogrey_2500_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillvertigogrey_2500_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillvertigogrey_2500_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-vertigo-grey"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F052

Group ID: `dup-842ba1d2cce8512b02695f3a453d766ec1865742ad848483f6331bea5d6aa50b`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillvertigogrey_2500_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Vertigo Grey`, name `ASA Extrafill Vertigo Grey`.
- `fillamentum_asa_extrafillvertigogrey_2500_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Vertigo Grey`, name `Extrafill Vertigo Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillvertigogrey_2500_285_p": {
    "replaced_by": "fillamentum_asa_extrafillvertigogrey_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Vertigo Grey::ASA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillvertigogrey_2500_285_p": null,
    "fillamentum_asa_extrafillvertigogrey_2500_285_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillvertigogrey_2500_285_p": null,
    "fillamentum_asa_extrafillvertigogrey_2500_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillvertigogrey_2500_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillvertigogrey_2500_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillvertigogrey_2500_285_p": null,
    "fillamentum_asa_extrafillvertigogrey_2500_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillvertigogrey_2500_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillvertigogrey_2500_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-vertigo-grey"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F053

Group ID: `dup-e6bf4c497d6ecb8ab4e7ded1bf6a15b2739fbd75b6ef0f70595510d97569a369`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillvividpink_750_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Vivid Pink`, name `ASA Extrafill Vivid Pink`.
- `fillamentum_asa_extrafillvividpink_750_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Vivid Pink`, name `Extrafill Vivid Pink`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillvividpink_750_175_p": {
    "replaced_by": "fillamentum_asa_extrafillvividpink_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Vivid Pink::ASA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillvividpink_750_175_p": null,
    "fillamentum_asa_extrafillvividpink_750_175_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillvividpink_750_175_p": null,
    "fillamentum_asa_extrafillvividpink_750_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillvividpink_750_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillvividpink_750_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillvividpink_750_175_p": null,
    "fillamentum_asa_extrafillvividpink_750_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillvividpink_750_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillvividpink_750_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Vivid Pink",
      "diameter": 1.75,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-vivid-pink",
      "variant_title": "1.75 mm",
      "sku_as_listed": "8595632824237",
      "variant_id": 39289137496162,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-vivid-pink"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F054

Group ID: `dup-5780b104fcfefcaf0c52b626cc8a4b8296b5b1b179392dc34de744b541262c9f`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillvividpink_750_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Vivid Pink`, name `ASA Extrafill Vivid Pink`.
- `fillamentum_asa_extrafillvividpink_750_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Vivid Pink`, name `Extrafill Vivid Pink`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillvividpink_750_285_p": {
    "replaced_by": "fillamentum_asa_extrafillvividpink_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Vivid Pink::ASA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillvividpink_750_285_p": null,
    "fillamentum_asa_extrafillvividpink_750_285_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillvividpink_750_285_p": null,
    "fillamentum_asa_extrafillvividpink_750_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillvividpink_750_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillvividpink_750_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillvividpink_750_285_p": null,
    "fillamentum_asa_extrafillvividpink_750_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillvividpink_750_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillvividpink_750_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "Vivid Pink",
      "diameter": 2.85,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-vivid-pink",
      "variant_title": "2.85 mm",
      "sku_as_listed": "8595632825159",
      "variant_id": 39289137528930,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-vivid-pink"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F055

Group ID: `dup-e3576aba8d7faeaf9d9b0f207d3d6090cbcf531444b7d7b742e2f149f9db4fcb`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillvividpink_2500_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Vivid Pink`, name `ASA Extrafill Vivid Pink`.
- `fillamentum_asa_extrafillvividpink_2500_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Vivid Pink`, name `Extrafill Vivid Pink`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillvividpink_2500_175_p": {
    "replaced_by": "fillamentum_asa_extrafillvividpink_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Vivid Pink::ASA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillvividpink_2500_175_p": null,
    "fillamentum_asa_extrafillvividpink_2500_175_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillvividpink_2500_175_p": null,
    "fillamentum_asa_extrafillvividpink_2500_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillvividpink_2500_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillvividpink_2500_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillvividpink_2500_175_p": null,
    "fillamentum_asa_extrafillvividpink_2500_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillvividpink_2500_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillvividpink_2500_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-vivid-pink"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F056

Group ID: `dup-07a37f9709e488f24f508a39d52ee5ef8081d84d3f32f5ccb4b15ccc7cd685ea`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillvividpink_2500_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `Vivid Pink`, name `ASA Extrafill Vivid Pink`.
- `fillamentum_asa_extrafillvividpink_2500_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `Vivid Pink`, name `Extrafill Vivid Pink`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillvividpink_2500_285_p": {
    "replaced_by": "fillamentum_asa_extrafillvividpink_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill Vivid Pink::ASA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillvividpink_2500_285_p": null,
    "fillamentum_asa_extrafillvividpink_2500_285_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillvividpink_2500_285_p": null,
    "fillamentum_asa_extrafillvividpink_2500_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillvividpink_2500_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillvividpink_2500_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillvividpink_2500_285_p": null,
    "fillamentum_asa_extrafillvividpink_2500_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillvividpink_2500_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillvividpink_2500_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-vivid-pink"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F057

Group ID: `dup-28c9c7e79cb7facf0dbce5803d0cd2ea23473128420ac309f5135d3e779797aa`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillwhitealuminium_750_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `White Aluminium`, name `ASA Extrafill White Aluminium`.
- `fillamentum_asa_extrafillwhitealuminium_750_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `White Aluminium`, name `Extrafill White Aluminium`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillwhitealuminium_750_175_p": {
    "replaced_by": "fillamentum_asa_extrafillwhitealuminium_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill White Aluminium::ASA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillwhitealuminium_750_175_p": null,
    "fillamentum_asa_extrafillwhitealuminium_750_175_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillwhitealuminium_750_175_p": null,
    "fillamentum_asa_extrafillwhitealuminium_750_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillwhitealuminium_750_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillwhitealuminium_750_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillwhitealuminium_750_175_p": null,
    "fillamentum_asa_extrafillwhitealuminium_750_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillwhitealuminium_750_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillwhitealuminium_750_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "White Aluminium",
      "diameter": 1.75,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-white-aluminium",
      "variant_title": "1.75 mm",
      "sku_as_listed": "8595632824091",
      "variant_id": 12233847767138,
      "available": false,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-white-aluminium"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F058

Group ID: `dup-874563a52bdedb3a60a4a873c4ca75911f009fa09c1e640420863449d2f9c449`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillwhitealuminium_750_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `White Aluminium`, name `ASA Extrafill White Aluminium`.
- `fillamentum_asa_extrafillwhitealuminium_750_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `White Aluminium`, name `Extrafill White Aluminium`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillwhitealuminium_750_285_p": {
    "replaced_by": "fillamentum_asa_extrafillwhitealuminium_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill White Aluminium::ASA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillwhitealuminium_750_285_p": null,
    "fillamentum_asa_extrafillwhitealuminium_750_285_p": 230.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillwhitealuminium_750_285_p": null,
    "fillamentum_asa_extrafillwhitealuminium_750_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillwhitealuminium_750_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillwhitealuminium_750_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillwhitealuminium_750_285_p": null,
    "fillamentum_asa_extrafillwhitealuminium_750_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillwhitealuminium_750_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillwhitealuminium_750_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "ASA",
      "color": "White Aluminium",
      "diameter": 2.85,
      "weight": 750,
      "weight_evidence": "Exact product page PRODUCT INFORMATION: 750 g of filament",
      "product_url": "https://shop.fillamentum.com/products/asa-extrafill-white-aluminium",
      "variant_title": "2.85 mm",
      "sku_as_listed": "8595632825098",
      "variant_id": 12233847799906,
      "available": false,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-white-aluminium"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F059

Group ID: `dup-aa83702bf0cee2747a27e4c6fffaa6beae575841d337f3303312ded72b2cbe63`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillwhitealuminium_2500_175_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `White Aluminium`, name `ASA Extrafill White Aluminium`.
- `fillamentum_asa_extrafillwhitealuminium_2500_175_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `White Aluminium`, name `Extrafill White Aluminium`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillwhitealuminium_2500_175_p": {
    "replaced_by": "fillamentum_asa_extrafillwhitealuminium_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill White Aluminium::ASA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillwhitealuminium_2500_175_p": null,
    "fillamentum_asa_extrafillwhitealuminium_2500_175_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillwhitealuminium_2500_175_p": null,
    "fillamentum_asa_extrafillwhitealuminium_2500_175_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillwhitealuminium_2500_175_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillwhitealuminium_2500_175_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillwhitealuminium_2500_175_p": null,
    "fillamentum_asa_extrafillwhitealuminium_2500_175_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillwhitealuminium_2500_175_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillwhitealuminium_2500_175_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-white-aluminium"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F060

Group ID: `dup-79874029d5a4f81155852744239801e52dbb55623bd48a04bc7747f12b67424e`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_asa_asaextrafillwhitealuminium_2500_285_p` — fillamentum.json index 2, template `ASA Extrafill {color_name}`, source color `White Aluminium`, name `ASA Extrafill White Aluminium`.
- `fillamentum_asa_extrafillwhitealuminium_2500_285_p` — fillamentum.json index 0, template `Extrafill {color_name}`, source color `White Aluminium`, name `Extrafill White Aluminium`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_asa_asaextrafillwhitealuminium_2500_285_p": {
    "replaced_by": "fillamentum_asa_extrafillwhitealuminium_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::ASA Extrafill {color_name}::ASA Extrafill White Aluminium::ASA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_asa_asaextrafillwhitealuminium_2500_285_p": null,
    "fillamentum_asa_extrafillwhitealuminium_2500_285_p": 590.0
  },
  "extruder_temp": {
    "fillamentum_asa_asaextrafillwhitealuminium_2500_285_p": null,
    "fillamentum_asa_extrafillwhitealuminium_2500_285_p": 250
  },
  "extruder_temp_range": {
    "fillamentum_asa_asaextrafillwhitealuminium_2500_285_p": [
      240,
      255
    ],
    "fillamentum_asa_extrafillwhitealuminium_2500_285_p": null
  },
  "bed_temp": {
    "fillamentum_asa_asaextrafillwhitealuminium_2500_285_p": null,
    "fillamentum_asa_extrafillwhitealuminium_2500_285_p": 95
  },
  "bed_temp_range": {
    "fillamentum_asa_asaextrafillwhitealuminium_2500_285_p": [
      80,
      105
    ],
    "fillamentum_asa_extrafillwhitealuminium_2500_285_p": null
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/asa-extrafill-white-aluminium"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F061

Group ID: `dup-5579b6eb7fce243ba4f961cafa25b0abfe983ec7ee2917829ff9e610f36e6a2d`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillcobaltblue_750_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Cobalt Blue`, name `Extrafill Cobalt Blue`.
- `fillamentum_pla_plaextrafillcobaltblue_750_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Cobalt Blue`, name `PLA Extrafill Cobalt Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillcobaltblue_750_175_p": {
    "replaced_by": "fillamentum_pla_extrafillcobaltblue_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Cobalt Blue::PLA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillcobaltblue_750_175_p": 230.0,
    "fillamentum_pla_plaextrafillcobaltblue_750_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillcobaltblue_750_175_p": 200,
    "fillamentum_pla_plaextrafillcobaltblue_750_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillcobaltblue_750_175_p": null,
    "fillamentum_pla_plaextrafillcobaltblue_750_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillcobaltblue_750_175_p": 55,
    "fillamentum_pla_plaextrafillcobaltblue_750_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillcobaltblue_750_175_p": null,
    "fillamentum_pla_plaextrafillcobaltblue_750_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-cobalt-blue-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F062

Group ID: `dup-a839438c0e28c7a06eb967ad49b7bc8fafbdb6455a36dff9bfa489ea7e0de3ca`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillcobaltblue_750_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Cobalt Blue`, name `Extrafill Cobalt Blue`.
- `fillamentum_pla_plaextrafillcobaltblue_750_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Cobalt Blue`, name `PLA Extrafill Cobalt Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillcobaltblue_750_285_p": {
    "replaced_by": "fillamentum_pla_extrafillcobaltblue_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Cobalt Blue::PLA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillcobaltblue_750_285_p": 230.0,
    "fillamentum_pla_plaextrafillcobaltblue_750_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillcobaltblue_750_285_p": 200,
    "fillamentum_pla_plaextrafillcobaltblue_750_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillcobaltblue_750_285_p": null,
    "fillamentum_pla_plaextrafillcobaltblue_750_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillcobaltblue_750_285_p": 55,
    "fillamentum_pla_plaextrafillcobaltblue_750_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillcobaltblue_750_285_p": null,
    "fillamentum_pla_plaextrafillcobaltblue_750_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-cobalt-blue-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F063

Group ID: `dup-b50ddd84870048f491ae6043ca65cd850545850473d409b5cfde93e9a22faa2a`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillcobaltblue_2500_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Cobalt Blue`, name `Extrafill Cobalt Blue`.
- `fillamentum_pla_plaextrafillcobaltblue_2500_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Cobalt Blue`, name `PLA Extrafill Cobalt Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillcobaltblue_2500_175_p": {
    "replaced_by": "fillamentum_pla_extrafillcobaltblue_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Cobalt Blue::PLA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillcobaltblue_2500_175_p": 590.0,
    "fillamentum_pla_plaextrafillcobaltblue_2500_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillcobaltblue_2500_175_p": 200,
    "fillamentum_pla_plaextrafillcobaltblue_2500_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillcobaltblue_2500_175_p": null,
    "fillamentum_pla_plaextrafillcobaltblue_2500_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillcobaltblue_2500_175_p": 55,
    "fillamentum_pla_plaextrafillcobaltblue_2500_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillcobaltblue_2500_175_p": null,
    "fillamentum_pla_plaextrafillcobaltblue_2500_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-cobalt-blue-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F064

Group ID: `dup-26e5a5e828c238a2b56a47d7938c557ac66bb1ea5018b4ecf825bc893672dc7b`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillcobaltblue_2500_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Cobalt Blue`, name `Extrafill Cobalt Blue`.
- `fillamentum_pla_plaextrafillcobaltblue_2500_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Cobalt Blue`, name `PLA Extrafill Cobalt Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillcobaltblue_2500_285_p": {
    "replaced_by": "fillamentum_pla_extrafillcobaltblue_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Cobalt Blue::PLA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillcobaltblue_2500_285_p": 590.0,
    "fillamentum_pla_plaextrafillcobaltblue_2500_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillcobaltblue_2500_285_p": 200,
    "fillamentum_pla_plaextrafillcobaltblue_2500_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillcobaltblue_2500_285_p": null,
    "fillamentum_pla_plaextrafillcobaltblue_2500_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillcobaltblue_2500_285_p": 55,
    "fillamentum_pla_plaextrafillcobaltblue_2500_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillcobaltblue_2500_285_p": null,
    "fillamentum_pla_plaextrafillcobaltblue_2500_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-cobalt-blue-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F065

Group ID: `dup-b46ada5c92fc7d2fae0f6d46e56934e668193b6ec8a1dceb0ba001fcb1913f56`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillconcretegrey_750_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Concrete Grey`, name `Extrafill Concrete Grey`.
- `fillamentum_pla_plaextrafillconcretegrey_750_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Concrete Grey`, name `PLA Extrafill Concrete Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillconcretegrey_750_175_p": {
    "replaced_by": "fillamentum_pla_extrafillconcretegrey_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Concrete Grey::PLA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillconcretegrey_750_175_p": 230.0,
    "fillamentum_pla_plaextrafillconcretegrey_750_175_p": null
  },
  "color_hex": {
    "fillamentum_pla_extrafillconcretegrey_750_175_p": "9f9c89",
    "fillamentum_pla_plaextrafillconcretegrey_750_175_p": "9F9C89"
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillconcretegrey_750_175_p": 200,
    "fillamentum_pla_plaextrafillconcretegrey_750_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillconcretegrey_750_175_p": null,
    "fillamentum_pla_plaextrafillconcretegrey_750_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillconcretegrey_750_175_p": 55,
    "fillamentum_pla_plaextrafillconcretegrey_750_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillconcretegrey_750_175_p": null,
    "fillamentum_pla_plaextrafillconcretegrey_750_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-concrete-grey-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F066

Group ID: `dup-c26c09e8294081ddaeb245e8082762ed025cd78218e41a5b87578c2605e6511d`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillconcretegrey_750_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Concrete Grey`, name `Extrafill Concrete Grey`.
- `fillamentum_pla_plaextrafillconcretegrey_750_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Concrete Grey`, name `PLA Extrafill Concrete Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillconcretegrey_750_285_p": {
    "replaced_by": "fillamentum_pla_extrafillconcretegrey_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Concrete Grey::PLA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillconcretegrey_750_285_p": 230.0,
    "fillamentum_pla_plaextrafillconcretegrey_750_285_p": null
  },
  "color_hex": {
    "fillamentum_pla_extrafillconcretegrey_750_285_p": "9f9c89",
    "fillamentum_pla_plaextrafillconcretegrey_750_285_p": "9F9C89"
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillconcretegrey_750_285_p": 200,
    "fillamentum_pla_plaextrafillconcretegrey_750_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillconcretegrey_750_285_p": null,
    "fillamentum_pla_plaextrafillconcretegrey_750_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillconcretegrey_750_285_p": 55,
    "fillamentum_pla_plaextrafillconcretegrey_750_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillconcretegrey_750_285_p": null,
    "fillamentum_pla_plaextrafillconcretegrey_750_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-concrete-grey-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F067

Group ID: `dup-08a492a00a8b2835d3f85f80d22d9f90061aac3cc8b7c09a23a23634e788c2f4`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillconcretegrey_2500_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Concrete Grey`, name `Extrafill Concrete Grey`.
- `fillamentum_pla_plaextrafillconcretegrey_2500_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Concrete Grey`, name `PLA Extrafill Concrete Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillconcretegrey_2500_175_p": {
    "replaced_by": "fillamentum_pla_extrafillconcretegrey_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Concrete Grey::PLA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillconcretegrey_2500_175_p": 590.0,
    "fillamentum_pla_plaextrafillconcretegrey_2500_175_p": null
  },
  "color_hex": {
    "fillamentum_pla_extrafillconcretegrey_2500_175_p": "9f9c89",
    "fillamentum_pla_plaextrafillconcretegrey_2500_175_p": "9F9C89"
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillconcretegrey_2500_175_p": 200,
    "fillamentum_pla_plaextrafillconcretegrey_2500_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillconcretegrey_2500_175_p": null,
    "fillamentum_pla_plaextrafillconcretegrey_2500_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillconcretegrey_2500_175_p": 55,
    "fillamentum_pla_plaextrafillconcretegrey_2500_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillconcretegrey_2500_175_p": null,
    "fillamentum_pla_plaextrafillconcretegrey_2500_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-concrete-grey-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F068

Group ID: `dup-0b058ebc3d6efa758cb2a3581bcf65e8206aba0c6a5068362dc8e30ceb08bd05`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillconcretegrey_2500_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Concrete Grey`, name `Extrafill Concrete Grey`.
- `fillamentum_pla_plaextrafillconcretegrey_2500_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Concrete Grey`, name `PLA Extrafill Concrete Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillconcretegrey_2500_285_p": {
    "replaced_by": "fillamentum_pla_extrafillconcretegrey_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Concrete Grey::PLA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillconcretegrey_2500_285_p": 590.0,
    "fillamentum_pla_plaextrafillconcretegrey_2500_285_p": null
  },
  "color_hex": {
    "fillamentum_pla_extrafillconcretegrey_2500_285_p": "9f9c89",
    "fillamentum_pla_plaextrafillconcretegrey_2500_285_p": "9F9C89"
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillconcretegrey_2500_285_p": 200,
    "fillamentum_pla_plaextrafillconcretegrey_2500_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillconcretegrey_2500_285_p": null,
    "fillamentum_pla_plaextrafillconcretegrey_2500_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillconcretegrey_2500_285_p": 55,
    "fillamentum_pla_plaextrafillconcretegrey_2500_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillconcretegrey_2500_285_p": null,
    "fillamentum_pla_plaextrafillconcretegrey_2500_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-concrete-grey-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F069

Group ID: `dup-d9074718c86ef9a0abf394a86b5a90ea64184dd4ce6964a447e3e76c0a17cdfc`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilleverybody'smagenta_750_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Everybody's Magenta`, name `Extrafill Everybody's Magenta`.
- `fillamentum_pla_plaextrafilleverybody'smagenta_750_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Everybody's Magenta`, name `PLA Extrafill Everybody's Magenta`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilleverybody'smagenta_750_175_p": {
    "replaced_by": "fillamentum_pla_extrafilleverybody'smagenta_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Everybody's Magenta::PLA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilleverybody'smagenta_750_175_p": 230.0,
    "fillamentum_pla_plaextrafilleverybody'smagenta_750_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilleverybody'smagenta_750_175_p": 200,
    "fillamentum_pla_plaextrafilleverybody'smagenta_750_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilleverybody'smagenta_750_175_p": null,
    "fillamentum_pla_plaextrafilleverybody'smagenta_750_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilleverybody'smagenta_750_175_p": 55,
    "fillamentum_pla_plaextrafilleverybody'smagenta_750_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilleverybody'smagenta_750_175_p": null,
    "fillamentum_pla_plaextrafilleverybody'smagenta_750_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-everybodys-magenta-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F070

Group ID: `dup-04bf751985ff58f0a75aa8d3e05a7b75ec47ea8da6a1cd7cb130c9867f403979`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilleverybody'smagenta_750_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Everybody's Magenta`, name `Extrafill Everybody's Magenta`.
- `fillamentum_pla_plaextrafilleverybody'smagenta_750_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Everybody's Magenta`, name `PLA Extrafill Everybody's Magenta`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilleverybody'smagenta_750_285_p": {
    "replaced_by": "fillamentum_pla_extrafilleverybody'smagenta_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Everybody's Magenta::PLA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilleverybody'smagenta_750_285_p": 230.0,
    "fillamentum_pla_plaextrafilleverybody'smagenta_750_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilleverybody'smagenta_750_285_p": 200,
    "fillamentum_pla_plaextrafilleverybody'smagenta_750_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilleverybody'smagenta_750_285_p": null,
    "fillamentum_pla_plaextrafilleverybody'smagenta_750_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilleverybody'smagenta_750_285_p": 55,
    "fillamentum_pla_plaextrafilleverybody'smagenta_750_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilleverybody'smagenta_750_285_p": null,
    "fillamentum_pla_plaextrafilleverybody'smagenta_750_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-everybodys-magenta-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F071

Group ID: `dup-0b52e924bd4763cc40770d0008e1f279abb9cb288456f09b9f5fccf500d2e83a`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilleverybody'smagenta_2500_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Everybody's Magenta`, name `Extrafill Everybody's Magenta`.
- `fillamentum_pla_plaextrafilleverybody'smagenta_2500_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Everybody's Magenta`, name `PLA Extrafill Everybody's Magenta`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilleverybody'smagenta_2500_175_p": {
    "replaced_by": "fillamentum_pla_extrafilleverybody'smagenta_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Everybody's Magenta::PLA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilleverybody'smagenta_2500_175_p": 590.0,
    "fillamentum_pla_plaextrafilleverybody'smagenta_2500_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilleverybody'smagenta_2500_175_p": 200,
    "fillamentum_pla_plaextrafilleverybody'smagenta_2500_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilleverybody'smagenta_2500_175_p": null,
    "fillamentum_pla_plaextrafilleverybody'smagenta_2500_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilleverybody'smagenta_2500_175_p": 55,
    "fillamentum_pla_plaextrafilleverybody'smagenta_2500_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilleverybody'smagenta_2500_175_p": null,
    "fillamentum_pla_plaextrafilleverybody'smagenta_2500_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-everybodys-magenta-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F072

Group ID: `dup-0b04cc8f4fc22d4a11eff0c5682dd602056169ad75106f92c3d7a4ac92127a98`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilleverybody'smagenta_2500_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Everybody's Magenta`, name `Extrafill Everybody's Magenta`.
- `fillamentum_pla_plaextrafilleverybody'smagenta_2500_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Everybody's Magenta`, name `PLA Extrafill Everybody's Magenta`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilleverybody'smagenta_2500_285_p": {
    "replaced_by": "fillamentum_pla_extrafilleverybody'smagenta_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Everybody's Magenta::PLA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilleverybody'smagenta_2500_285_p": 590.0,
    "fillamentum_pla_plaextrafilleverybody'smagenta_2500_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilleverybody'smagenta_2500_285_p": 200,
    "fillamentum_pla_plaextrafilleverybody'smagenta_2500_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilleverybody'smagenta_2500_285_p": null,
    "fillamentum_pla_plaextrafilleverybody'smagenta_2500_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilleverybody'smagenta_2500_285_p": 55,
    "fillamentum_pla_plaextrafilleverybody'smagenta_2500_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilleverybody'smagenta_2500_285_p": null,
    "fillamentum_pla_plaextrafilleverybody'smagenta_2500_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-everybodys-magenta-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F073

Group ID: `dup-82df1cfcee36a07930e43ccd73e3a5ed0d9052edab333e377b20beed6f3f7236`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillgreengrass_750_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Green Grass`, name `Extrafill Green Grass`.
- `fillamentum_pla_plaextrafillgreengrass_750_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Green Grass`, name `PLA Extrafill Green Grass`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillgreengrass_750_175_p": {
    "replaced_by": "fillamentum_pla_extrafillgreengrass_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Green Grass::PLA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillgreengrass_750_175_p": 230.0,
    "fillamentum_pla_plaextrafillgreengrass_750_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillgreengrass_750_175_p": 200,
    "fillamentum_pla_plaextrafillgreengrass_750_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillgreengrass_750_175_p": null,
    "fillamentum_pla_plaextrafillgreengrass_750_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillgreengrass_750_175_p": 55,
    "fillamentum_pla_plaextrafillgreengrass_750_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillgreengrass_750_175_p": null,
    "fillamentum_pla_plaextrafillgreengrass_750_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-green-grass-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F074

Group ID: `dup-944d9503f55fe0bc5de11ea367ff466814ed56b2173bdeb3baedf1deb2b41e86`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillgreengrass_750_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Green Grass`, name `Extrafill Green Grass`.
- `fillamentum_pla_plaextrafillgreengrass_750_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Green Grass`, name `PLA Extrafill Green Grass`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillgreengrass_750_285_p": {
    "replaced_by": "fillamentum_pla_extrafillgreengrass_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Green Grass::PLA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillgreengrass_750_285_p": 230.0,
    "fillamentum_pla_plaextrafillgreengrass_750_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillgreengrass_750_285_p": 200,
    "fillamentum_pla_plaextrafillgreengrass_750_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillgreengrass_750_285_p": null,
    "fillamentum_pla_plaextrafillgreengrass_750_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillgreengrass_750_285_p": 55,
    "fillamentum_pla_plaextrafillgreengrass_750_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillgreengrass_750_285_p": null,
    "fillamentum_pla_plaextrafillgreengrass_750_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-green-grass-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F075

Group ID: `dup-ad3405ca9bbbc5de5c936b05f4afd4654f8e00eb5ba784aa4d389f991f8d90f2`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillgreengrass_2500_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Green Grass`, name `Extrafill Green Grass`.
- `fillamentum_pla_plaextrafillgreengrass_2500_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Green Grass`, name `PLA Extrafill Green Grass`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillgreengrass_2500_175_p": {
    "replaced_by": "fillamentum_pla_extrafillgreengrass_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Green Grass::PLA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillgreengrass_2500_175_p": 590.0,
    "fillamentum_pla_plaextrafillgreengrass_2500_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillgreengrass_2500_175_p": 200,
    "fillamentum_pla_plaextrafillgreengrass_2500_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillgreengrass_2500_175_p": null,
    "fillamentum_pla_plaextrafillgreengrass_2500_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillgreengrass_2500_175_p": 55,
    "fillamentum_pla_plaextrafillgreengrass_2500_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillgreengrass_2500_175_p": null,
    "fillamentum_pla_plaextrafillgreengrass_2500_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-green-grass-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F076

Group ID: `dup-06b387c15172c360db318af0cc1919d36846e191cb23f071eee0ba3c93100a74`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillgreengrass_2500_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Green Grass`, name `Extrafill Green Grass`.
- `fillamentum_pla_plaextrafillgreengrass_2500_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Green Grass`, name `PLA Extrafill Green Grass`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillgreengrass_2500_285_p": {
    "replaced_by": "fillamentum_pla_extrafillgreengrass_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Green Grass::PLA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillgreengrass_2500_285_p": 590.0,
    "fillamentum_pla_plaextrafillgreengrass_2500_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillgreengrass_2500_285_p": 200,
    "fillamentum_pla_plaextrafillgreengrass_2500_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillgreengrass_2500_285_p": null,
    "fillamentum_pla_plaextrafillgreengrass_2500_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillgreengrass_2500_285_p": 55,
    "fillamentum_pla_plaextrafillgreengrass_2500_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillgreengrass_2500_285_p": null,
    "fillamentum_pla_plaextrafillgreengrass_2500_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-green-grass-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F077

Group ID: `dup-4b672cee128e5dc990a2ec84b25f8c0ea2350663c5974a57a2fd4d3688003b5d`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillmetallicgrey_750_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Metallic Grey`, name `Extrafill Metallic Grey`.
- `fillamentum_pla_plaextrafillmetallicgrey_750_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Metallic Grey`, name `PLA Extrafill Metallic Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillmetallicgrey_750_175_p": {
    "replaced_by": "fillamentum_pla_extrafillmetallicgrey_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Metallic Grey::PLA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillmetallicgrey_750_175_p": 230.0,
    "fillamentum_pla_plaextrafillmetallicgrey_750_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillmetallicgrey_750_175_p": 200,
    "fillamentum_pla_plaextrafillmetallicgrey_750_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillmetallicgrey_750_175_p": null,
    "fillamentum_pla_plaextrafillmetallicgrey_750_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillmetallicgrey_750_175_p": 55,
    "fillamentum_pla_plaextrafillmetallicgrey_750_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillmetallicgrey_750_175_p": null,
    "fillamentum_pla_plaextrafillmetallicgrey_750_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-metallic-grey-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F078

Group ID: `dup-df958ba47eda4d3f1cf2a2184b5c2dfdf881fd92bd2a5b30e563346a29d92cdc`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillmetallicgrey_750_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Metallic Grey`, name `Extrafill Metallic Grey`.
- `fillamentum_pla_plaextrafillmetallicgrey_750_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Metallic Grey`, name `PLA Extrafill Metallic Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillmetallicgrey_750_285_p": {
    "replaced_by": "fillamentum_pla_extrafillmetallicgrey_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Metallic Grey::PLA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillmetallicgrey_750_285_p": 230.0,
    "fillamentum_pla_plaextrafillmetallicgrey_750_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillmetallicgrey_750_285_p": 200,
    "fillamentum_pla_plaextrafillmetallicgrey_750_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillmetallicgrey_750_285_p": null,
    "fillamentum_pla_plaextrafillmetallicgrey_750_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillmetallicgrey_750_285_p": 55,
    "fillamentum_pla_plaextrafillmetallicgrey_750_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillmetallicgrey_750_285_p": null,
    "fillamentum_pla_plaextrafillmetallicgrey_750_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-metallic-grey-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F079

Group ID: `dup-3b05456f2f1c94fde68718bcb3a7cac453ae1eedfd8c6c93e5b6db973f59d90a`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillmetallicgrey_2500_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Metallic Grey`, name `Extrafill Metallic Grey`.
- `fillamentum_pla_plaextrafillmetallicgrey_2500_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Metallic Grey`, name `PLA Extrafill Metallic Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillmetallicgrey_2500_175_p": {
    "replaced_by": "fillamentum_pla_extrafillmetallicgrey_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Metallic Grey::PLA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillmetallicgrey_2500_175_p": 590.0,
    "fillamentum_pla_plaextrafillmetallicgrey_2500_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillmetallicgrey_2500_175_p": 200,
    "fillamentum_pla_plaextrafillmetallicgrey_2500_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillmetallicgrey_2500_175_p": null,
    "fillamentum_pla_plaextrafillmetallicgrey_2500_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillmetallicgrey_2500_175_p": 55,
    "fillamentum_pla_plaextrafillmetallicgrey_2500_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillmetallicgrey_2500_175_p": null,
    "fillamentum_pla_plaextrafillmetallicgrey_2500_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-metallic-grey-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F080

Group ID: `dup-d786c7682c40fe487005343ee32dc0aaf30872c29fca9a70be84b1ec4f015982`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillmetallicgrey_2500_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Metallic Grey`, name `Extrafill Metallic Grey`.
- `fillamentum_pla_plaextrafillmetallicgrey_2500_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Metallic Grey`, name `PLA Extrafill Metallic Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillmetallicgrey_2500_285_p": {
    "replaced_by": "fillamentum_pla_extrafillmetallicgrey_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Metallic Grey::PLA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillmetallicgrey_2500_285_p": 590.0,
    "fillamentum_pla_plaextrafillmetallicgrey_2500_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillmetallicgrey_2500_285_p": 200,
    "fillamentum_pla_plaextrafillmetallicgrey_2500_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillmetallicgrey_2500_285_p": null,
    "fillamentum_pla_plaextrafillmetallicgrey_2500_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillmetallicgrey_2500_285_p": 55,
    "fillamentum_pla_plaextrafillmetallicgrey_2500_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillmetallicgrey_2500_285_p": null,
    "fillamentum_pla_plaextrafillmetallicgrey_2500_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-metallic-grey-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F081

Group ID: `dup-7be55bd67349e1f06e064420c51be82822cf7613e31690469c49242d9c060ed0`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillnatural_750_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Natural`, name `Extrafill Natural`.
- `fillamentum_pla_plaextrafillnatural_750_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Natural`, name `PLA Extrafill Natural`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillnatural_750_175_p": {
    "replaced_by": "fillamentum_pla_extrafillnatural_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Natural::PLA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillnatural_750_175_p": 230.0,
    "fillamentum_pla_plaextrafillnatural_750_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillnatural_750_175_p": 200,
    "fillamentum_pla_plaextrafillnatural_750_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillnatural_750_175_p": null,
    "fillamentum_pla_plaextrafillnatural_750_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillnatural_750_175_p": 55,
    "fillamentum_pla_plaextrafillnatural_750_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillnatural_750_175_p": null,
    "fillamentum_pla_plaextrafillnatural_750_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-natural-1kg",
    "https://shop.fillamentum.com/products/pla-extrafill-natural"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F082

Group ID: `dup-f1e6b17bebe7d36cb2591754b0645333a8da8190837d318a076fa240ac0d065d`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillnatural_750_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Natural`, name `Extrafill Natural`.
- `fillamentum_pla_plaextrafillnatural_750_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Natural`, name `PLA Extrafill Natural`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillnatural_750_285_p": {
    "replaced_by": "fillamentum_pla_extrafillnatural_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Natural::PLA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillnatural_750_285_p": 230.0,
    "fillamentum_pla_plaextrafillnatural_750_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillnatural_750_285_p": 200,
    "fillamentum_pla_plaextrafillnatural_750_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillnatural_750_285_p": null,
    "fillamentum_pla_plaextrafillnatural_750_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillnatural_750_285_p": 55,
    "fillamentum_pla_plaextrafillnatural_750_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillnatural_750_285_p": null,
    "fillamentum_pla_plaextrafillnatural_750_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "PLA",
      "color": "Natural",
      "diameter": 2.85,
      "weight": 750.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/pla-extrafill-natural",
      "variant_title": "2.85 mm / 750 g",
      "sku_as_listed": "8595632814009",
      "variant_id": 941541155,
      "available": false,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-natural-1kg",
    "https://shop.fillamentum.com/products/pla-extrafill-natural"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F083

Group ID: `dup-90475bfab91761e6586ebc4ab495ec94542dde049a32c927adb35e9b6f48441e`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillnatural_2500_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Natural`, name `Extrafill Natural`.
- `fillamentum_pla_plaextrafillnatural_2500_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Natural`, name `PLA Extrafill Natural`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillnatural_2500_175_p": {
    "replaced_by": "fillamentum_pla_extrafillnatural_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Natural::PLA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillnatural_2500_175_p": 590.0,
    "fillamentum_pla_plaextrafillnatural_2500_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillnatural_2500_175_p": 200,
    "fillamentum_pla_plaextrafillnatural_2500_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillnatural_2500_175_p": null,
    "fillamentum_pla_plaextrafillnatural_2500_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillnatural_2500_175_p": 55,
    "fillamentum_pla_plaextrafillnatural_2500_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillnatural_2500_175_p": null,
    "fillamentum_pla_plaextrafillnatural_2500_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-natural-1kg",
    "https://shop.fillamentum.com/products/pla-extrafill-natural"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F084

Group ID: `dup-fbd5a34a3f79eee63fa6f42bbad028070aaa54e58af7b7eaba009734cb0281db`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillnatural_2500_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Natural`, name `Extrafill Natural`.
- `fillamentum_pla_plaextrafillnatural_2500_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Natural`, name `PLA Extrafill Natural`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillnatural_2500_285_p": {
    "replaced_by": "fillamentum_pla_extrafillnatural_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Natural::PLA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillnatural_2500_285_p": 590.0,
    "fillamentum_pla_plaextrafillnatural_2500_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillnatural_2500_285_p": 200,
    "fillamentum_pla_plaextrafillnatural_2500_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillnatural_2500_285_p": null,
    "fillamentum_pla_plaextrafillnatural_2500_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillnatural_2500_285_p": 55,
    "fillamentum_pla_plaextrafillnatural_2500_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillnatural_2500_285_p": null,
    "fillamentum_pla_plaextrafillnatural_2500_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-natural-1kg",
    "https://shop.fillamentum.com/products/pla-extrafill-natural"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F085

Group ID: `dup-f2ed47923dd8f442b28aa5058f189cf534a215a183cf558487fcaa7efe06024b`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillpepperedmustard_750_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Peppered Mustard`, name `Extrafill Peppered Mustard`.
- `fillamentum_pla_plaextrafillpepperedmustard_750_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Peppered Mustard`, name `PLA Extrafill Peppered Mustard`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillpepperedmustard_750_175_p": {
    "replaced_by": "fillamentum_pla_extrafillpepperedmustard_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Peppered Mustard::PLA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillpepperedmustard_750_175_p": 230.0,
    "fillamentum_pla_plaextrafillpepperedmustard_750_175_p": null
  },
  "color_hex": {
    "fillamentum_pla_extrafillpepperedmustard_750_175_p": "a67123",
    "fillamentum_pla_plaextrafillpepperedmustard_750_175_p": "A67123"
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillpepperedmustard_750_175_p": 200,
    "fillamentum_pla_plaextrafillpepperedmustard_750_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillpepperedmustard_750_175_p": null,
    "fillamentum_pla_plaextrafillpepperedmustard_750_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillpepperedmustard_750_175_p": 55,
    "fillamentum_pla_plaextrafillpepperedmustard_750_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillpepperedmustard_750_175_p": null,
    "fillamentum_pla_plaextrafillpepperedmustard_750_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-peppered-mustard"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F086

Group ID: `dup-fd025e8b086226a2e65f4abffd35e9d7d9b15850e94d2122193da23a7a6e2602`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillpepperedmustard_750_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Peppered Mustard`, name `Extrafill Peppered Mustard`.
- `fillamentum_pla_plaextrafillpepperedmustard_750_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Peppered Mustard`, name `PLA Extrafill Peppered Mustard`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillpepperedmustard_750_285_p": {
    "replaced_by": "fillamentum_pla_extrafillpepperedmustard_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Peppered Mustard::PLA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillpepperedmustard_750_285_p": 230.0,
    "fillamentum_pla_plaextrafillpepperedmustard_750_285_p": null
  },
  "color_hex": {
    "fillamentum_pla_extrafillpepperedmustard_750_285_p": "a67123",
    "fillamentum_pla_plaextrafillpepperedmustard_750_285_p": "A67123"
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillpepperedmustard_750_285_p": 200,
    "fillamentum_pla_plaextrafillpepperedmustard_750_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillpepperedmustard_750_285_p": null,
    "fillamentum_pla_plaextrafillpepperedmustard_750_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillpepperedmustard_750_285_p": 55,
    "fillamentum_pla_plaextrafillpepperedmustard_750_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillpepperedmustard_750_285_p": null,
    "fillamentum_pla_plaextrafillpepperedmustard_750_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_LISTED",
  "exact_variants": [
    {
      "material": "PLA",
      "color": "Peppered Mustard",
      "diameter": 2.85,
      "weight": 750.0,
      "weight_evidence": "Exact variant Weight option; never Shopify shipping grams",
      "product_url": "https://shop.fillamentum.com/products/pla-extrafill-peppered-mustard",
      "variant_title": "2.85 mm / 750 g",
      "sku_as_listed": "8595632814719",
      "variant_id": 39441428119650,
      "available": true,
      "source_only_no_identifier_enrichment": true
    }
  ],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-peppered-mustard"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F087

Group ID: `dup-1a6d992bf5a435a34a61f6117d95553c38ea0d7b2af5c25774b94d5d2f3c5de6`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillpepperedmustard_2500_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Peppered Mustard`, name `Extrafill Peppered Mustard`.
- `fillamentum_pla_plaextrafillpepperedmustard_2500_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Peppered Mustard`, name `PLA Extrafill Peppered Mustard`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillpepperedmustard_2500_175_p": {
    "replaced_by": "fillamentum_pla_extrafillpepperedmustard_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Peppered Mustard::PLA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillpepperedmustard_2500_175_p": 590.0,
    "fillamentum_pla_plaextrafillpepperedmustard_2500_175_p": null
  },
  "color_hex": {
    "fillamentum_pla_extrafillpepperedmustard_2500_175_p": "a67123",
    "fillamentum_pla_plaextrafillpepperedmustard_2500_175_p": "A67123"
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillpepperedmustard_2500_175_p": 200,
    "fillamentum_pla_plaextrafillpepperedmustard_2500_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillpepperedmustard_2500_175_p": null,
    "fillamentum_pla_plaextrafillpepperedmustard_2500_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillpepperedmustard_2500_175_p": 55,
    "fillamentum_pla_plaextrafillpepperedmustard_2500_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillpepperedmustard_2500_175_p": null,
    "fillamentum_pla_plaextrafillpepperedmustard_2500_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-peppered-mustard"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F088

Group ID: `dup-9905da46d04cd4c58184552204077f3de88094ed84ff51c582172d25ca83d2f1`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillpepperedmustard_2500_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Peppered Mustard`, name `Extrafill Peppered Mustard`.
- `fillamentum_pla_plaextrafillpepperedmustard_2500_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Peppered Mustard`, name `PLA Extrafill Peppered Mustard`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillpepperedmustard_2500_285_p": {
    "replaced_by": "fillamentum_pla_extrafillpepperedmustard_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Peppered Mustard::PLA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillpepperedmustard_2500_285_p": 590.0,
    "fillamentum_pla_plaextrafillpepperedmustard_2500_285_p": null
  },
  "color_hex": {
    "fillamentum_pla_extrafillpepperedmustard_2500_285_p": "a67123",
    "fillamentum_pla_plaextrafillpepperedmustard_2500_285_p": "A67123"
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillpepperedmustard_2500_285_p": 200,
    "fillamentum_pla_plaextrafillpepperedmustard_2500_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillpepperedmustard_2500_285_p": null,
    "fillamentum_pla_plaextrafillpepperedmustard_2500_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillpepperedmustard_2500_285_p": 55,
    "fillamentum_pla_plaextrafillpepperedmustard_2500_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillpepperedmustard_2500_285_p": null,
    "fillamentum_pla_plaextrafillpepperedmustard_2500_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-peppered-mustard"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F089

Group ID: `dup-85ddb873c5f1930df85022766e3d2cb31ec0c39ddbeeb3ae5aa79d0788b167a6`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillrapunzelsilver_750_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Rapunzel Silver`, name `Extrafill Rapunzel Silver`.
- `fillamentum_pla_plaextrafillrapunzelsilver_750_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Rapunzel Silver`, name `PLA Extrafill Rapunzel Silver`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillrapunzelsilver_750_175_p": {
    "replaced_by": "fillamentum_pla_extrafillrapunzelsilver_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Rapunzel Silver::PLA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillrapunzelsilver_750_175_p": 230.0,
    "fillamentum_pla_plaextrafillrapunzelsilver_750_175_p": null
  },
  "color_hex": {
    "fillamentum_pla_extrafillrapunzelsilver_750_175_p": "c2c3be",
    "fillamentum_pla_plaextrafillrapunzelsilver_750_175_p": "C2C3BE"
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillrapunzelsilver_750_175_p": 200,
    "fillamentum_pla_plaextrafillrapunzelsilver_750_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillrapunzelsilver_750_175_p": null,
    "fillamentum_pla_plaextrafillrapunzelsilver_750_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillrapunzelsilver_750_175_p": 55,
    "fillamentum_pla_plaextrafillrapunzelsilver_750_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillrapunzelsilver_750_175_p": null,
    "fillamentum_pla_plaextrafillrapunzelsilver_750_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-rapunzel-silver-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F090

Group ID: `dup-dd7ddbcc5f87a4068a499997fee561da5b7f5c5adacfd47e7fbe36b2a88045c6`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillrapunzelsilver_750_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Rapunzel Silver`, name `Extrafill Rapunzel Silver`.
- `fillamentum_pla_plaextrafillrapunzelsilver_750_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Rapunzel Silver`, name `PLA Extrafill Rapunzel Silver`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillrapunzelsilver_750_285_p": {
    "replaced_by": "fillamentum_pla_extrafillrapunzelsilver_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Rapunzel Silver::PLA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillrapunzelsilver_750_285_p": 230.0,
    "fillamentum_pla_plaextrafillrapunzelsilver_750_285_p": null
  },
  "color_hex": {
    "fillamentum_pla_extrafillrapunzelsilver_750_285_p": "c2c3be",
    "fillamentum_pla_plaextrafillrapunzelsilver_750_285_p": "C2C3BE"
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillrapunzelsilver_750_285_p": 200,
    "fillamentum_pla_plaextrafillrapunzelsilver_750_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillrapunzelsilver_750_285_p": null,
    "fillamentum_pla_plaextrafillrapunzelsilver_750_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillrapunzelsilver_750_285_p": 55,
    "fillamentum_pla_plaextrafillrapunzelsilver_750_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillrapunzelsilver_750_285_p": null,
    "fillamentum_pla_plaextrafillrapunzelsilver_750_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-rapunzel-silver-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F091

Group ID: `dup-678f9865ea4f0a337c14da4e1a5864e4ef1ddce0bd9f4f5090bda953728dafb6`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillrapunzelsilver_2500_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Rapunzel Silver`, name `Extrafill Rapunzel Silver`.
- `fillamentum_pla_plaextrafillrapunzelsilver_2500_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Rapunzel Silver`, name `PLA Extrafill Rapunzel Silver`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillrapunzelsilver_2500_175_p": {
    "replaced_by": "fillamentum_pla_extrafillrapunzelsilver_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Rapunzel Silver::PLA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillrapunzelsilver_2500_175_p": 590.0,
    "fillamentum_pla_plaextrafillrapunzelsilver_2500_175_p": null
  },
  "color_hex": {
    "fillamentum_pla_extrafillrapunzelsilver_2500_175_p": "c2c3be",
    "fillamentum_pla_plaextrafillrapunzelsilver_2500_175_p": "C2C3BE"
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillrapunzelsilver_2500_175_p": 200,
    "fillamentum_pla_plaextrafillrapunzelsilver_2500_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillrapunzelsilver_2500_175_p": null,
    "fillamentum_pla_plaextrafillrapunzelsilver_2500_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillrapunzelsilver_2500_175_p": 55,
    "fillamentum_pla_plaextrafillrapunzelsilver_2500_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillrapunzelsilver_2500_175_p": null,
    "fillamentum_pla_plaextrafillrapunzelsilver_2500_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-rapunzel-silver-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F092

Group ID: `dup-305937d5d7c1b820c394af3d04e81b7d7c15219c3ed8f6f75ec9da7f403fb1a9`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillrapunzelsilver_2500_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Rapunzel Silver`, name `Extrafill Rapunzel Silver`.
- `fillamentum_pla_plaextrafillrapunzelsilver_2500_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Rapunzel Silver`, name `PLA Extrafill Rapunzel Silver`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillrapunzelsilver_2500_285_p": {
    "replaced_by": "fillamentum_pla_extrafillrapunzelsilver_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Rapunzel Silver::PLA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillrapunzelsilver_2500_285_p": 590.0,
    "fillamentum_pla_plaextrafillrapunzelsilver_2500_285_p": null
  },
  "color_hex": {
    "fillamentum_pla_extrafillrapunzelsilver_2500_285_p": "c2c3be",
    "fillamentum_pla_plaextrafillrapunzelsilver_2500_285_p": "C2C3BE"
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillrapunzelsilver_2500_285_p": 200,
    "fillamentum_pla_plaextrafillrapunzelsilver_2500_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillrapunzelsilver_2500_285_p": null,
    "fillamentum_pla_plaextrafillrapunzelsilver_2500_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillrapunzelsilver_2500_285_p": 55,
    "fillamentum_pla_plaextrafillrapunzelsilver_2500_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillrapunzelsilver_2500_285_p": null,
    "fillamentum_pla_plaextrafillrapunzelsilver_2500_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-rapunzel-silver-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F093

Group ID: `dup-0729f1a2c6f794f2ef5cc4f82b8d2d984abd3f20825a920600e09681e3ae8ff1`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillskyblue_750_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Sky Blue`, name `Extrafill Sky Blue`.
- `fillamentum_pla_plaextrafillskyblue_750_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Sky Blue`, name `PLA Extrafill Sky Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillskyblue_750_175_p": {
    "replaced_by": "fillamentum_pla_extrafillskyblue_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Sky Blue::PLA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillskyblue_750_175_p": 230.0,
    "fillamentum_pla_plaextrafillskyblue_750_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillskyblue_750_175_p": 200,
    "fillamentum_pla_plaextrafillskyblue_750_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillskyblue_750_175_p": null,
    "fillamentum_pla_plaextrafillskyblue_750_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillskyblue_750_175_p": 55,
    "fillamentum_pla_plaextrafillskyblue_750_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillskyblue_750_175_p": null,
    "fillamentum_pla_plaextrafillskyblue_750_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-sky-blue-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F094

Group ID: `dup-d38a46a83e5fb5c78e5d8833004dc835d506f6593d6136f4bcc4bd6f7ad6e9af`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillskyblue_750_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Sky Blue`, name `Extrafill Sky Blue`.
- `fillamentum_pla_plaextrafillskyblue_750_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Sky Blue`, name `PLA Extrafill Sky Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillskyblue_750_285_p": {
    "replaced_by": "fillamentum_pla_extrafillskyblue_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Sky Blue::PLA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillskyblue_750_285_p": 230.0,
    "fillamentum_pla_plaextrafillskyblue_750_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillskyblue_750_285_p": 200,
    "fillamentum_pla_plaextrafillskyblue_750_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillskyblue_750_285_p": null,
    "fillamentum_pla_plaextrafillskyblue_750_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillskyblue_750_285_p": 55,
    "fillamentum_pla_plaextrafillskyblue_750_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillskyblue_750_285_p": null,
    "fillamentum_pla_plaextrafillskyblue_750_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-sky-blue-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F095

Group ID: `dup-f7a08c51b4c21326f0243acd49fef2bdb4bae1ff35e7e79cd6b9474f25d550e4`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillskyblue_2500_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Sky Blue`, name `Extrafill Sky Blue`.
- `fillamentum_pla_plaextrafillskyblue_2500_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Sky Blue`, name `PLA Extrafill Sky Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillskyblue_2500_175_p": {
    "replaced_by": "fillamentum_pla_extrafillskyblue_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Sky Blue::PLA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillskyblue_2500_175_p": 590.0,
    "fillamentum_pla_plaextrafillskyblue_2500_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillskyblue_2500_175_p": 200,
    "fillamentum_pla_plaextrafillskyblue_2500_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillskyblue_2500_175_p": null,
    "fillamentum_pla_plaextrafillskyblue_2500_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillskyblue_2500_175_p": 55,
    "fillamentum_pla_plaextrafillskyblue_2500_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillskyblue_2500_175_p": null,
    "fillamentum_pla_plaextrafillskyblue_2500_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-sky-blue-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F096

Group ID: `dup-6361360574af95c724a3de80296aecdea65f269dd1e9466d14153f6d5a2cab97`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillskyblue_2500_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Sky Blue`, name `Extrafill Sky Blue`.
- `fillamentum_pla_plaextrafillskyblue_2500_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Sky Blue`, name `PLA Extrafill Sky Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillskyblue_2500_285_p": {
    "replaced_by": "fillamentum_pla_extrafillskyblue_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Sky Blue::PLA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillskyblue_2500_285_p": 590.0,
    "fillamentum_pla_plaextrafillskyblue_2500_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillskyblue_2500_285_p": 200,
    "fillamentum_pla_plaextrafillskyblue_2500_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillskyblue_2500_285_p": null,
    "fillamentum_pla_plaextrafillskyblue_2500_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillskyblue_2500_285_p": 55,
    "fillamentum_pla_plaextrafillskyblue_2500_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillskyblue_2500_285_p": null,
    "fillamentum_pla_plaextrafillskyblue_2500_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-sky-blue-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F097

Group ID: `dup-b88caa9b48341674a845824377ecbff77444c88f5c9c0c3b6928a53e5de02ef6`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilltrafficblack_750_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Traffic Black`, name `Extrafill Traffic Black`.
- `fillamentum_pla_plaextrafilltrafficblack_750_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Traffic Black`, name `PLA Extrafill Traffic Black`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilltrafficblack_750_175_p": {
    "replaced_by": "fillamentum_pla_extrafilltrafficblack_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Traffic Black::PLA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilltrafficblack_750_175_p": 230.0,
    "fillamentum_pla_plaextrafilltrafficblack_750_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilltrafficblack_750_175_p": 200,
    "fillamentum_pla_plaextrafilltrafficblack_750_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilltrafficblack_750_175_p": null,
    "fillamentum_pla_plaextrafilltrafficblack_750_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilltrafficblack_750_175_p": 55,
    "fillamentum_pla_plaextrafilltrafficblack_750_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilltrafficblack_750_175_p": null,
    "fillamentum_pla_plaextrafilltrafficblack_750_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-traffic-black-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F098

Group ID: `dup-8c02d3ab87d8e0389630e0d86418c15c07292a95f3ff8f9557006300d83d0265`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilltrafficblack_750_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Traffic Black`, name `Extrafill Traffic Black`.
- `fillamentum_pla_plaextrafilltrafficblack_750_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Traffic Black`, name `PLA Extrafill Traffic Black`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilltrafficblack_750_285_p": {
    "replaced_by": "fillamentum_pla_extrafilltrafficblack_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Traffic Black::PLA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilltrafficblack_750_285_p": 230.0,
    "fillamentum_pla_plaextrafilltrafficblack_750_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilltrafficblack_750_285_p": 200,
    "fillamentum_pla_plaextrafilltrafficblack_750_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilltrafficblack_750_285_p": null,
    "fillamentum_pla_plaextrafilltrafficblack_750_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilltrafficblack_750_285_p": 55,
    "fillamentum_pla_plaextrafilltrafficblack_750_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilltrafficblack_750_285_p": null,
    "fillamentum_pla_plaextrafilltrafficblack_750_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-traffic-black-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F099

Group ID: `dup-d999ef830ab097ba944c5b6f3de7a814251da2ff0fbde69359f9dea54771ea9f`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilltrafficblack_2500_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Traffic Black`, name `Extrafill Traffic Black`.
- `fillamentum_pla_plaextrafilltrafficblack_2500_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Traffic Black`, name `PLA Extrafill Traffic Black`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilltrafficblack_2500_175_p": {
    "replaced_by": "fillamentum_pla_extrafilltrafficblack_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Traffic Black::PLA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilltrafficblack_2500_175_p": 590.0,
    "fillamentum_pla_plaextrafilltrafficblack_2500_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilltrafficblack_2500_175_p": 200,
    "fillamentum_pla_plaextrafilltrafficblack_2500_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilltrafficblack_2500_175_p": null,
    "fillamentum_pla_plaextrafilltrafficblack_2500_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilltrafficblack_2500_175_p": 55,
    "fillamentum_pla_plaextrafilltrafficblack_2500_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilltrafficblack_2500_175_p": null,
    "fillamentum_pla_plaextrafilltrafficblack_2500_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-traffic-black-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F100

Group ID: `dup-eae7c7cbde7994f8914413f6bd9f1e4cdd8d0940e37e8d707dd2976224bd2ad8`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilltrafficblack_2500_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Traffic Black`, name `Extrafill Traffic Black`.
- `fillamentum_pla_plaextrafilltrafficblack_2500_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Traffic Black`, name `PLA Extrafill Traffic Black`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilltrafficblack_2500_285_p": {
    "replaced_by": "fillamentum_pla_extrafilltrafficblack_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Traffic Black::PLA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilltrafficblack_2500_285_p": 590.0,
    "fillamentum_pla_plaextrafilltrafficblack_2500_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilltrafficblack_2500_285_p": 200,
    "fillamentum_pla_plaextrafilltrafficblack_2500_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilltrafficblack_2500_285_p": null,
    "fillamentum_pla_plaextrafilltrafficblack_2500_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilltrafficblack_2500_285_p": 55,
    "fillamentum_pla_plaextrafilltrafficblack_2500_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilltrafficblack_2500_285_p": null,
    "fillamentum_pla_plaextrafilltrafficblack_2500_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-traffic-black-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F101

Group ID: `dup-e77e7fcf2f1a8a661ff4010db4e7c829d6eb7a9b53fea1d281ee8ac96895cd08`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilltrafficred_750_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Traffic Red`, name `Extrafill Traffic Red`.
- `fillamentum_pla_plaextrafilltrafficred_750_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Traffic Red`, name `PLA Extrafill Traffic Red`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilltrafficred_750_175_p": {
    "replaced_by": "fillamentum_pla_extrafilltrafficred_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Traffic Red::PLA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilltrafficred_750_175_p": 230.0,
    "fillamentum_pla_plaextrafilltrafficred_750_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilltrafficred_750_175_p": 200,
    "fillamentum_pla_plaextrafilltrafficred_750_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilltrafficred_750_175_p": null,
    "fillamentum_pla_plaextrafilltrafficred_750_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilltrafficred_750_175_p": 55,
    "fillamentum_pla_plaextrafilltrafficred_750_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilltrafficred_750_175_p": null,
    "fillamentum_pla_plaextrafilltrafficred_750_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-traffic-red-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F102

Group ID: `dup-3b9fb702f7f0127a67d7ead288278b30c723a3b22e471c88a2d426328c10721d`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilltrafficred_750_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Traffic Red`, name `Extrafill Traffic Red`.
- `fillamentum_pla_plaextrafilltrafficred_750_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Traffic Red`, name `PLA Extrafill Traffic Red`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilltrafficred_750_285_p": {
    "replaced_by": "fillamentum_pla_extrafilltrafficred_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Traffic Red::PLA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilltrafficred_750_285_p": 230.0,
    "fillamentum_pla_plaextrafilltrafficred_750_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilltrafficred_750_285_p": 200,
    "fillamentum_pla_plaextrafilltrafficred_750_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilltrafficred_750_285_p": null,
    "fillamentum_pla_plaextrafilltrafficred_750_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilltrafficred_750_285_p": 55,
    "fillamentum_pla_plaextrafilltrafficred_750_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilltrafficred_750_285_p": null,
    "fillamentum_pla_plaextrafilltrafficred_750_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-traffic-red-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F103

Group ID: `dup-ae787200550105686e7de5e72bf4b0bee601b96f8c4317689ca394ad42407ec3`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilltrafficred_2500_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Traffic Red`, name `Extrafill Traffic Red`.
- `fillamentum_pla_plaextrafilltrafficred_2500_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Traffic Red`, name `PLA Extrafill Traffic Red`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilltrafficred_2500_175_p": {
    "replaced_by": "fillamentum_pla_extrafilltrafficred_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Traffic Red::PLA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilltrafficred_2500_175_p": 590.0,
    "fillamentum_pla_plaextrafilltrafficred_2500_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilltrafficred_2500_175_p": 200,
    "fillamentum_pla_plaextrafilltrafficred_2500_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilltrafficred_2500_175_p": null,
    "fillamentum_pla_plaextrafilltrafficred_2500_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilltrafficred_2500_175_p": 55,
    "fillamentum_pla_plaextrafilltrafficred_2500_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilltrafficred_2500_175_p": null,
    "fillamentum_pla_plaextrafilltrafficred_2500_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-traffic-red-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F104

Group ID: `dup-915ec9f3e90817e99f8807dc2986d3532989abec7a776f7245e6d7e829ab00f7`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilltrafficred_2500_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Traffic Red`, name `Extrafill Traffic Red`.
- `fillamentum_pla_plaextrafilltrafficred_2500_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Traffic Red`, name `PLA Extrafill Traffic Red`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilltrafficred_2500_285_p": {
    "replaced_by": "fillamentum_pla_extrafilltrafficred_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Traffic Red::PLA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilltrafficred_2500_285_p": 590.0,
    "fillamentum_pla_plaextrafilltrafficred_2500_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilltrafficred_2500_285_p": 200,
    "fillamentum_pla_plaextrafilltrafficred_2500_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilltrafficred_2500_285_p": null,
    "fillamentum_pla_plaextrafilltrafficred_2500_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilltrafficred_2500_285_p": 55,
    "fillamentum_pla_plaextrafilltrafficred_2500_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilltrafficred_2500_285_p": null,
    "fillamentum_pla_plaextrafilltrafficred_2500_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-traffic-red-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F105

Group ID: `dup-c530a35a20a92d76c833f3d4154553864779b5f7fca7d93ec0b930d69418cc18`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilltrafficwhite_750_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Traffic White`, name `Extrafill Traffic White`.
- `fillamentum_pla_plaextrafilltrafficwhite_750_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Traffic White`, name `PLA Extrafill Traffic White`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilltrafficwhite_750_175_p": {
    "replaced_by": "fillamentum_pla_extrafilltrafficwhite_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Traffic White::PLA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilltrafficwhite_750_175_p": 230.0,
    "fillamentum_pla_plaextrafilltrafficwhite_750_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilltrafficwhite_750_175_p": 200,
    "fillamentum_pla_plaextrafilltrafficwhite_750_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilltrafficwhite_750_175_p": null,
    "fillamentum_pla_plaextrafilltrafficwhite_750_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilltrafficwhite_750_175_p": 55,
    "fillamentum_pla_plaextrafilltrafficwhite_750_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilltrafficwhite_750_175_p": null,
    "fillamentum_pla_plaextrafilltrafficwhite_750_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-traffic-white-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F106

Group ID: `dup-136f97cefbedb02dcb5b4a0261a3aa3be85d9314c14e61ad93cfc2d2a69fc796`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilltrafficwhite_750_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Traffic White`, name `Extrafill Traffic White`.
- `fillamentum_pla_plaextrafilltrafficwhite_750_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Traffic White`, name `PLA Extrafill Traffic White`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilltrafficwhite_750_285_p": {
    "replaced_by": "fillamentum_pla_extrafilltrafficwhite_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Traffic White::PLA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilltrafficwhite_750_285_p": 230.0,
    "fillamentum_pla_plaextrafilltrafficwhite_750_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilltrafficwhite_750_285_p": 200,
    "fillamentum_pla_plaextrafilltrafficwhite_750_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilltrafficwhite_750_285_p": null,
    "fillamentum_pla_plaextrafilltrafficwhite_750_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilltrafficwhite_750_285_p": 55,
    "fillamentum_pla_plaextrafilltrafficwhite_750_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilltrafficwhite_750_285_p": null,
    "fillamentum_pla_plaextrafilltrafficwhite_750_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-traffic-white-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F107

Group ID: `dup-fd85cf17108c7a1670ac51845943954fab0eb9f6eecfdcb921b1a97ad655151e`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilltrafficwhite_2500_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Traffic White`, name `Extrafill Traffic White`.
- `fillamentum_pla_plaextrafilltrafficwhite_2500_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Traffic White`, name `PLA Extrafill Traffic White`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilltrafficwhite_2500_175_p": {
    "replaced_by": "fillamentum_pla_extrafilltrafficwhite_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Traffic White::PLA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilltrafficwhite_2500_175_p": 590.0,
    "fillamentum_pla_plaextrafilltrafficwhite_2500_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilltrafficwhite_2500_175_p": 200,
    "fillamentum_pla_plaextrafilltrafficwhite_2500_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilltrafficwhite_2500_175_p": null,
    "fillamentum_pla_plaextrafilltrafficwhite_2500_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilltrafficwhite_2500_175_p": 55,
    "fillamentum_pla_plaextrafilltrafficwhite_2500_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilltrafficwhite_2500_175_p": null,
    "fillamentum_pla_plaextrafilltrafficwhite_2500_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-traffic-white-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F108

Group ID: `dup-aecb2023014eaefadc4046ba396ab9766beeb93615e8eec6300dfba8baf767c1`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilltrafficwhite_2500_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Traffic White`, name `Extrafill Traffic White`.
- `fillamentum_pla_plaextrafilltrafficwhite_2500_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Traffic White`, name `PLA Extrafill Traffic White`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilltrafficwhite_2500_285_p": {
    "replaced_by": "fillamentum_pla_extrafilltrafficwhite_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Traffic White::PLA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilltrafficwhite_2500_285_p": 590.0,
    "fillamentum_pla_plaextrafilltrafficwhite_2500_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilltrafficwhite_2500_285_p": 200,
    "fillamentum_pla_plaextrafilltrafficwhite_2500_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilltrafficwhite_2500_285_p": null,
    "fillamentum_pla_plaextrafilltrafficwhite_2500_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilltrafficwhite_2500_285_p": 55,
    "fillamentum_pla_plaextrafilltrafficwhite_2500_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilltrafficwhite_2500_285_p": null,
    "fillamentum_pla_plaextrafilltrafficwhite_2500_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-traffic-white-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F109

Group ID: `dup-c4415b0268237864cbaf76cdb53a79db78d5b53dd72d60470a6beb5b9cdb7c2e`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilltrafficyellow_750_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Traffic Yellow`, name `Extrafill Traffic Yellow`.
- `fillamentum_pla_plaextrafilltrafficyellow_750_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Traffic Yellow`, name `PLA Extrafill Traffic Yellow`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilltrafficyellow_750_175_p": {
    "replaced_by": "fillamentum_pla_extrafilltrafficyellow_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Traffic Yellow::PLA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilltrafficyellow_750_175_p": 230.0,
    "fillamentum_pla_plaextrafilltrafficyellow_750_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilltrafficyellow_750_175_p": 200,
    "fillamentum_pla_plaextrafilltrafficyellow_750_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilltrafficyellow_750_175_p": null,
    "fillamentum_pla_plaextrafilltrafficyellow_750_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilltrafficyellow_750_175_p": 55,
    "fillamentum_pla_plaextrafilltrafficyellow_750_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilltrafficyellow_750_175_p": null,
    "fillamentum_pla_plaextrafilltrafficyellow_750_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-traffic-yellow-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F110

Group ID: `dup-2c8dcec36cb6319fa26245e7482f794812e48d550010e09d19afedae78e220ea`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilltrafficyellow_750_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Traffic Yellow`, name `Extrafill Traffic Yellow`.
- `fillamentum_pla_plaextrafilltrafficyellow_750_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Traffic Yellow`, name `PLA Extrafill Traffic Yellow`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilltrafficyellow_750_285_p": {
    "replaced_by": "fillamentum_pla_extrafilltrafficyellow_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Traffic Yellow::PLA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilltrafficyellow_750_285_p": 230.0,
    "fillamentum_pla_plaextrafilltrafficyellow_750_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilltrafficyellow_750_285_p": 200,
    "fillamentum_pla_plaextrafilltrafficyellow_750_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilltrafficyellow_750_285_p": null,
    "fillamentum_pla_plaextrafilltrafficyellow_750_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilltrafficyellow_750_285_p": 55,
    "fillamentum_pla_plaextrafilltrafficyellow_750_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilltrafficyellow_750_285_p": null,
    "fillamentum_pla_plaextrafilltrafficyellow_750_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-traffic-yellow-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F111

Group ID: `dup-03008fd0c824b233c4880347f45f4f7d92274e1dd647e327a320b3ddce599bee`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilltrafficyellow_2500_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Traffic Yellow`, name `Extrafill Traffic Yellow`.
- `fillamentum_pla_plaextrafilltrafficyellow_2500_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Traffic Yellow`, name `PLA Extrafill Traffic Yellow`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilltrafficyellow_2500_175_p": {
    "replaced_by": "fillamentum_pla_extrafilltrafficyellow_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Traffic Yellow::PLA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilltrafficyellow_2500_175_p": 590.0,
    "fillamentum_pla_plaextrafilltrafficyellow_2500_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilltrafficyellow_2500_175_p": 200,
    "fillamentum_pla_plaextrafilltrafficyellow_2500_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilltrafficyellow_2500_175_p": null,
    "fillamentum_pla_plaextrafilltrafficyellow_2500_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilltrafficyellow_2500_175_p": 55,
    "fillamentum_pla_plaextrafilltrafficyellow_2500_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilltrafficyellow_2500_175_p": null,
    "fillamentum_pla_plaextrafilltrafficyellow_2500_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-traffic-yellow-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F112

Group ID: `dup-189eb78c5f7b4b679cee575e33600caf87c6f380918e1789fe65870195319a34`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafilltrafficyellow_2500_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Traffic Yellow`, name `Extrafill Traffic Yellow`.
- `fillamentum_pla_plaextrafilltrafficyellow_2500_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Traffic Yellow`, name `PLA Extrafill Traffic Yellow`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafilltrafficyellow_2500_285_p": {
    "replaced_by": "fillamentum_pla_extrafilltrafficyellow_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Traffic Yellow::PLA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafilltrafficyellow_2500_285_p": 590.0,
    "fillamentum_pla_plaextrafilltrafficyellow_2500_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafilltrafficyellow_2500_285_p": 200,
    "fillamentum_pla_plaextrafilltrafficyellow_2500_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafilltrafficyellow_2500_285_p": null,
    "fillamentum_pla_plaextrafilltrafficyellow_2500_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafilltrafficyellow_2500_285_p": 55,
    "fillamentum_pla_plaextrafilltrafficyellow_2500_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafilltrafficyellow_2500_285_p": null,
    "fillamentum_pla_plaextrafilltrafficyellow_2500_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-traffic-yellow-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F113

Group ID: `dup-d04a5fc2fbc4d6e65e2bca19f2cebeafa16611a7b4c1a5863738e9b314a91c3a`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillturquoiseblue_750_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Turquoise Blue`, name `Extrafill Turquoise Blue`.
- `fillamentum_pla_plaextrafillturquoiseblue_750_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Turquoise Blue`, name `PLA Extrafill Turquoise Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillturquoiseblue_750_175_p": {
    "replaced_by": "fillamentum_pla_extrafillturquoiseblue_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Turquoise Blue::PLA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillturquoiseblue_750_175_p": 230.0,
    "fillamentum_pla_plaextrafillturquoiseblue_750_175_p": null
  },
  "color_hex": {
    "fillamentum_pla_extrafillturquoiseblue_750_175_p": "83bdc3",
    "fillamentum_pla_plaextrafillturquoiseblue_750_175_p": "83BDC3"
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillturquoiseblue_750_175_p": 200,
    "fillamentum_pla_plaextrafillturquoiseblue_750_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillturquoiseblue_750_175_p": null,
    "fillamentum_pla_plaextrafillturquoiseblue_750_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillturquoiseblue_750_175_p": 55,
    "fillamentum_pla_plaextrafillturquoiseblue_750_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillturquoiseblue_750_175_p": null,
    "fillamentum_pla_plaextrafillturquoiseblue_750_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-turquoise-blue-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F114

Group ID: `dup-96d542cb29e7924edf1fece4d1cb75904857a8fb08c82fcb9748c84c02d30d35`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillturquoiseblue_750_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Turquoise Blue`, name `Extrafill Turquoise Blue`.
- `fillamentum_pla_plaextrafillturquoiseblue_750_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Turquoise Blue`, name `PLA Extrafill Turquoise Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillturquoiseblue_750_285_p": {
    "replaced_by": "fillamentum_pla_extrafillturquoiseblue_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Turquoise Blue::PLA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillturquoiseblue_750_285_p": 230.0,
    "fillamentum_pla_plaextrafillturquoiseblue_750_285_p": null
  },
  "color_hex": {
    "fillamentum_pla_extrafillturquoiseblue_750_285_p": "83bdc3",
    "fillamentum_pla_plaextrafillturquoiseblue_750_285_p": "83BDC3"
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillturquoiseblue_750_285_p": 200,
    "fillamentum_pla_plaextrafillturquoiseblue_750_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillturquoiseblue_750_285_p": null,
    "fillamentum_pla_plaextrafillturquoiseblue_750_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillturquoiseblue_750_285_p": 55,
    "fillamentum_pla_plaextrafillturquoiseblue_750_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillturquoiseblue_750_285_p": null,
    "fillamentum_pla_plaextrafillturquoiseblue_750_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-turquoise-blue-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F115

Group ID: `dup-b010afdc9abb461f15625d75063580e8f556d052e07379c2149709bf724a6d68`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillturquoiseblue_2500_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Turquoise Blue`, name `Extrafill Turquoise Blue`.
- `fillamentum_pla_plaextrafillturquoiseblue_2500_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Turquoise Blue`, name `PLA Extrafill Turquoise Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillturquoiseblue_2500_175_p": {
    "replaced_by": "fillamentum_pla_extrafillturquoiseblue_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Turquoise Blue::PLA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillturquoiseblue_2500_175_p": 590.0,
    "fillamentum_pla_plaextrafillturquoiseblue_2500_175_p": null
  },
  "color_hex": {
    "fillamentum_pla_extrafillturquoiseblue_2500_175_p": "83bdc3",
    "fillamentum_pla_plaextrafillturquoiseblue_2500_175_p": "83BDC3"
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillturquoiseblue_2500_175_p": 200,
    "fillamentum_pla_plaextrafillturquoiseblue_2500_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillturquoiseblue_2500_175_p": null,
    "fillamentum_pla_plaextrafillturquoiseblue_2500_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillturquoiseblue_2500_175_p": 55,
    "fillamentum_pla_plaextrafillturquoiseblue_2500_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillturquoiseblue_2500_175_p": null,
    "fillamentum_pla_plaextrafillturquoiseblue_2500_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-turquoise-blue-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F116

Group ID: `dup-0b08547e17c3cdfe2a692629f30c9775700b210cb606940c79e3e574d870ad70`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillturquoiseblue_2500_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Turquoise Blue`, name `Extrafill Turquoise Blue`.
- `fillamentum_pla_plaextrafillturquoiseblue_2500_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Turquoise Blue`, name `PLA Extrafill Turquoise Blue`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillturquoiseblue_2500_285_p": {
    "replaced_by": "fillamentum_pla_extrafillturquoiseblue_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Turquoise Blue::PLA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillturquoiseblue_2500_285_p": 590.0,
    "fillamentum_pla_plaextrafillturquoiseblue_2500_285_p": null
  },
  "color_hex": {
    "fillamentum_pla_extrafillturquoiseblue_2500_285_p": "83bdc3",
    "fillamentum_pla_plaextrafillturquoiseblue_2500_285_p": "83BDC3"
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillturquoiseblue_2500_285_p": 200,
    "fillamentum_pla_plaextrafillturquoiseblue_2500_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillturquoiseblue_2500_285_p": null,
    "fillamentum_pla_plaextrafillturquoiseblue_2500_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillturquoiseblue_2500_285_p": 55,
    "fillamentum_pla_plaextrafillturquoiseblue_2500_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillturquoiseblue_2500_285_p": null,
    "fillamentum_pla_plaextrafillturquoiseblue_2500_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-turquoise-blue-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F117

Group ID: `dup-431399fd0007c11269c544631c0939d4f6cefdb860e5c424891fbd526b021fa6`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillvertigogrey_750_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Vertigo Grey`, name `Extrafill Vertigo Grey`.
- `fillamentum_pla_plaextrafillvertigogrey_750_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Vertigo Grey`, name `PLA Extrafill Vertigo Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillvertigogrey_750_175_p": {
    "replaced_by": "fillamentum_pla_extrafillvertigogrey_750_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Vertigo Grey::PLA::750::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillvertigogrey_750_175_p": 230.0,
    "fillamentum_pla_plaextrafillvertigogrey_750_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillvertigogrey_750_175_p": 200,
    "fillamentum_pla_plaextrafillvertigogrey_750_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillvertigogrey_750_175_p": null,
    "fillamentum_pla_plaextrafillvertigogrey_750_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillvertigogrey_750_175_p": 55,
    "fillamentum_pla_plaextrafillvertigogrey_750_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillvertigogrey_750_175_p": null,
    "fillamentum_pla_plaextrafillvertigogrey_750_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-vertigo-grey-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F118

Group ID: `dup-1d08c05671876c167bcf1c2adf1c4077e65ca3a9b849d8a85f6eaa70c421b0a3`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillvertigogrey_750_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Vertigo Grey`, name `Extrafill Vertigo Grey`.
- `fillamentum_pla_plaextrafillvertigogrey_750_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Vertigo Grey`, name `PLA Extrafill Vertigo Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillvertigogrey_750_285_p": {
    "replaced_by": "fillamentum_pla_extrafillvertigogrey_750_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Vertigo Grey::PLA::750::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillvertigogrey_750_285_p": 230.0,
    "fillamentum_pla_plaextrafillvertigogrey_750_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillvertigogrey_750_285_p": 200,
    "fillamentum_pla_plaextrafillvertigogrey_750_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillvertigogrey_750_285_p": null,
    "fillamentum_pla_plaextrafillvertigogrey_750_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillvertigogrey_750_285_p": 55,
    "fillamentum_pla_plaextrafillvertigogrey_750_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillvertigogrey_750_285_p": null,
    "fillamentum_pla_plaextrafillvertigogrey_750_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-vertigo-grey-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F119

Group ID: `dup-aa5eac10a28bd958076435baad591f3303b31e9358b6f13419a1fd977fa07e65`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillvertigogrey_2500_175_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Vertigo Grey`, name `Extrafill Vertigo Grey`.
- `fillamentum_pla_plaextrafillvertigogrey_2500_175_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Vertigo Grey`, name `PLA Extrafill Vertigo Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillvertigogrey_2500_175_p": {
    "replaced_by": "fillamentum_pla_extrafillvertigogrey_2500_175_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Vertigo Grey::PLA::2500::1.75::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillvertigogrey_2500_175_p": 590.0,
    "fillamentum_pla_plaextrafillvertigogrey_2500_175_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillvertigogrey_2500_175_p": 200,
    "fillamentum_pla_plaextrafillvertigogrey_2500_175_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillvertigogrey_2500_175_p": null,
    "fillamentum_pla_plaextrafillvertigogrey_2500_175_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillvertigogrey_2500_175_p": 55,
    "fillamentum_pla_plaextrafillvertigogrey_2500_175_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillvertigogrey_2500_175_p": null,
    "fillamentum_pla_plaextrafillvertigogrey_2500_175_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-vertigo-grey-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

### F120

Group ID: `dup-718968c330bd01c6f1f8600aaeffa7effdc743ab33fe3edf6b15f52f25c45ea5`. Owner approved this exact group; survivor metadata remains unchanged.

Source templates/colors:

- `fillamentum_pla_extrafillvertigogrey_2500_285_p` — fillamentum.json index 1, template `Extrafill {color_name}`, source color `Vertigo Grey`, name `Extrafill Vertigo Grey`.
- `fillamentum_pla_plaextrafillvertigogrey_2500_285_p` — fillamentum.json index 3, template `PLA Extrafill {color_name}`, source color `Vertigo Grey`, name `PLA Extrafill Vertigo Grey`.

Proposed registry entry (reason=duplicate; source is immutable audit/base commit):

```json
{
  "fillamentum_pla_plaextrafillvertigogrey_2500_285_p": {
    "replaced_by": "fillamentum_pla_extrafillvertigogrey_2500_285_p",
    "reason": "duplicate",
    "ref": "docs/audits/2026-10-03-fillamentum-duplicate-review.json",
    "source": "e5e15c65934a92c99654b44d22a74e2926cdfe4a",
    "retired_key": "fillamentum.json::Fillamentum::PLA Extrafill {color_name}::PLA Extrafill Vertigo Grey::PLA::2500::2.85::plastic::False"
  }
}
```

Both metadata values (unchanged/unresolved; HEX case-only where present):

```json
{
  "spool_weight": {
    "fillamentum_pla_extrafillvertigogrey_2500_285_p": 590.0,
    "fillamentum_pla_plaextrafillvertigogrey_2500_285_p": null
  },
  "extruder_temp": {
    "fillamentum_pla_extrafillvertigogrey_2500_285_p": 200,
    "fillamentum_pla_plaextrafillvertigogrey_2500_285_p": null
  },
  "extruder_temp_range": {
    "fillamentum_pla_extrafillvertigogrey_2500_285_p": null,
    "fillamentum_pla_plaextrafillvertigogrey_2500_285_p": [
      190,
      210
    ]
  },
  "bed_temp": {
    "fillamentum_pla_extrafillvertigogrey_2500_285_p": 55,
    "fillamentum_pla_plaextrafillvertigogrey_2500_285_p": null
  },
  "bed_temp_range": {
    "fillamentum_pla_extrafillvertigogrey_2500_285_p": null,
    "fillamentum_pla_plaextrafillvertigogrey_2500_285_p": [
      50,
      60
    ]
  }
}
```

Current exact product/SKU evidence (evidence only; no SKU/EAN import):

```json
{
  "status": "CURRENT_UNCONFIRMED_HISTORICAL_MATRIX",
  "exact_variants": [],
  "named_product_pages": [
    "https://shop.fillamentum.com/products/pla-extrafill-vertigo-grey-1kg"
  ],
  "alias": null,
  "note": "Current listing does not establish the production lot/spool type/tare of either historical DB record. Sold-out variants remain listed, with availability recorded."
}
```

## Out of scope — preserve

- `fillamentum_pla_extrafilllilac_750_175_p` — 750 g / 1.75 mm, PLA Lilac; original key and metadata retained in JSON.
- `fillamentum_pla_extrafilllilac_750_285_p` — 750 g / 2.85 mm, PLA Lilac; original key and metadata retained in JSON.
- `fillamentum_pla_extrafilllilac_2500_175_p` — 2500 g / 1.75 mm, PLA Lilac; original key and metadata retained in JSON.
- `fillamentum_pla_extrafilllilac_2500_285_p` — 2500 g / 2.85 mm, PLA Lilac; original key and metadata retained in JSON.

Current 1 kg PLA matrix, missing current-only colors, SKU/EAN enrichment, product spelling changes, packaging generation changes, and unrelated brands are out of scope. No work on these is authorized by this review.

## Documentation clarifications included

- The Bambu audit now labels original STEP 3 OWNER_APPROVAL_REQUIRED/newer-lot-only notes as historical snapshots; current approved decisions supersede them. Original audit content is preserved.
- The Bambu Markdown/README now correctly describe retained definition locations/counts/templates/colors/keys/compiled records, with full definitions available from pinned source base 139a98e rather than embedded in that audit.

## Verification

The original audit and unreviewed dry-run are retained as historical review-stage evidence. The owner then approved all 120 exact groups, retaining metadata. Reviewed dry-run and --apply use the tracked JSON audit; the independent before/after check requires exactly these 120 retirements and identical keys/compiled metadata for every surviving record. Full maintenance §7 and baseline --strict --base-ref e5e15c6 are required before delivery.

Original four full source definitions are embedded in the [reviewed JSON audit](2026-10-03-fillamentum-duplicate-review.json). Its raw generated audit and proposal/evidence fields are historical review-stage snapshots; approved root decisions supersede pending-approval wording. Owner approval and delivery authorization are recorded above.


## Breaking catalog migration

The approved 120 retired IDs disappear from published filaments.json. Existing Spoolman spools retain their imported local data; Spoolman does not consume retired_ids.json, redirect old catalog lookups or migrate stored external IDs. Consumers must follow these exact old-to-survivor mappings themselves. Rollback requires exact original-key reinstatement and baseline re-enrollment.
