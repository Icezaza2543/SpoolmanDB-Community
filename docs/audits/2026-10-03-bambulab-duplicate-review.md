# Bambu Lab approved duplicate migration and printing metadata

Date: 2026-10-03.

Source/catalog base: `139a98e6edf87d7158318d6b42ee649cabfad88f`. Read-only upstream comparison: `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`.

Owner approval covers all 122 Rule 1/3 groups plus B043/B044, choosing the official **Blue Grey** name. Rule 3 precedes Rule 4; no Rule 4 or Cartesian family-size preference decides this migration. Ten lossless Dual Color bindings are persisted in the [review JSON](2026-10-03-bambulab-duplicate-review.json).

This is an **intentional breaking catalog migration**: 124 old IDs disappear. Existing Spoolman spools retain their local imported data, but Spoolman does not consume the registry or redirect old external-ID lookups. Consumers needing those IDs must follow the exact registry mappings themselves.

Expected global records: 53,043 → 52,919; Bambu Lab: 614 → 490; registry: 391 → 515. New/changed identity/rekeyed/unregistered removals: 0/0/0/0. All 366 out-of-scope Bambu records and all other manufacturers are unchanged. Packaging/spool/tare, unique colors, weights and refill semantics are untouched.

## Approved printing metadata

Current official TDS/product pages are owner-accepted product-line evidence; lot binding remains necessary only for packaging/spool/tare. These corrections do not assert a formulation change or a production-lot revision.

| Group / survivor | Field | Old | New | Official source |
| --- | --- | --- | --- | --- |
| B020 / `bambulab_pc_black_1000_175_p` | `extruder_temp` | `250` | `null` | [TDS](https://store.bblcdn.com/a52afdccddfd448583d119587122c8c5.pdf) |
| B020 / `bambulab_pc_black_1000_175_p` | `extruder_temp_range` | `null` | `[260, 280]` | [TDS](https://store.bblcdn.com/a52afdccddfd448583d119587122c8c5.pdf) |
| B021 / `bambulab_pc_clearblack_1000_175_p` | `extruder_temp` | `250` | `null` | [TDS](https://store.bblcdn.com/a52afdccddfd448583d119587122c8c5.pdf) |
| B021 / `bambulab_pc_clearblack_1000_175_p` | `extruder_temp_range` | `null` | `[260, 280]` | [TDS](https://store.bblcdn.com/a52afdccddfd448583d119587122c8c5.pdf) |
| B022 / `bambulab_pc_transparent_1000_175_p` | `extruder_temp` | `250` | `null` | [TDS](https://store.bblcdn.com/a52afdccddfd448583d119587122c8c5.pdf) |
| B022 / `bambulab_pc_transparent_1000_175_p` | `extruder_temp_range` | `null` | `[260, 280]` | [TDS](https://store.bblcdn.com/a52afdccddfd448583d119587122c8c5.pdf) |
| B023 / `bambulab_pc_white_1000_175_p` | `extruder_temp` | `250` | `null` | [TDS](https://store.bblcdn.com/a52afdccddfd448583d119587122c8c5.pdf) |
| B023 / `bambulab_pc_white_1000_175_p` | `extruder_temp_range` | `null` | `[260, 280]` | [TDS](https://store.bblcdn.com/a52afdccddfd448583d119587122c8c5.pdf) |
| B024 / `bambulab_pc_frblack_1000_175_p` | `density` | `1.19` | `1.18` | [TDS](https://store.bblcdn.com/s1/default/4adf3c9827a0475d8777e9b8cfd11fbe.pdf) |
| B025 / `bambulab_pc_frgrey_1000_175_p` | `density` | `1.19` | `1.18` | [TDS](https://store.bblcdn.com/s1/default/4adf3c9827a0475d8777e9b8cfd11fbe.pdf) |
| B026 / `bambulab_pc_frwhite_1000_175_p` | `density` | `1.19` | `1.18` | [TDS](https://store.bblcdn.com/s1/default/4adf3c9827a0475d8777e9b8cfd11fbe.pdf) |
| B041 / `bambulab_pla_aerogray_1000_175_p` | `density` | `0.74` | `1.21` | [TDS](https://store.bblcdn.com/cbc8b808aaf84ead9bb3b0b9b43e66af.pdf) |
| B042 / `bambulab_pla_aerowhite_1000_175_p` | `density` | `0.74` | `1.21` | [TDS](https://store.bblcdn.com/cbc8b808aaf84ead9bb3b0b9b43e66af.pdf) |
| B117 / `bambulab_pva_clear_500_175_p` | `extruder_temp` | `240` | `null` | [TDS](https://store.bblcdn.com/s7/default/868930e5a44944258586caa250cc8143/Bambu_PVA_Technical_Data_Sheet.pdf) |
| B117 / `bambulab_pva_clear_500_175_p` | `extruder_temp_range` | `null` | `[220, 250]` | [TDS](https://store.bblcdn.com/s7/default/868930e5a44944258586caa250cc8143/Bambu_PVA_Technical_Data_Sheet.pdf) |

Aero density uses 1.21 g/cm³ for **raw filament**, not foamed printed material. PC/PVA scalar nozzle values are cleared when their approved ranges are installed. Bed values and document-link fields remain unchanged.

## Exact identifier transfers

Only the following 24 survivor IDs may gain `codes`. Source colors are split into exact weight/diameter/package cells when needed; every other surviving record must retain its identifier arrays byte-for-byte. These are transfers of existing owner-approved identifiers, not new manufacturer SKU assertions or a new packaging audit.

| Metric | Before | After |
| --- | ---: | ---: |
| Bambu code bindings | 734 | 723 |
| Unique code values | 678 | 678 |
| EAN bindings / unique values | 18 / 18 | 18 / 18 |
| Refill EAN bindings / unique values | 3 / 3 | 3 / 3 |

The 11 redundant bindings collapse onto survivors; the full remapped ID/value binding set is conserved.

| Group | Exact target ID | Old codes | Approved codes |
| --- | --- | --- | --- |
| B001 | `bambulab_abs_azure_1000_175_p` | `null` | `["40601", "42078846124147", "42720053362824"]` |
| B002 | `bambulab_abs_bambugreen_1000_175_p` | `null` | `["40500", "41898393436275", "42512928833672"]` |
| B004 | `bambulab_abs_black_1000_175_p` | `null` | `["40101", "40204456067187", "40883035046003", "40475105460360", "41216786432136"]` |
| B005 | `bambulab_abs_blue_1000_175_p` | `null` | `["40600", "40204456198259", "40475105591432"]` |
| B007 | `bambulab_abs_navyblue_1000_175_p` | `null` | `["40602", "42078845599859", "42720052707464"]` |
| B008 | `bambulab_abs_olive_1000_175_p` | `null` | `["40502", "42078846615667", "42720053952648"]` |
| B009 | `bambulab_abs_orange_1000_175_p` | `null` | `["40300", "41898393993331", "42512931750024"]` |
| B010 | `bambulab_abs_red_1000_175_p` | `null` | `["40200", "40204456132723", "40475105525896"]` |
| B011 | `bambulab_abs_silver_1000_175_p` | `null` | `["40102", "40830227710067", "500089458897068033", "41195746295944", "42851556556936"]` |
| B012 | `bambulab_abs_tangerineyellow_1000_175_p` | `null` | `["40402", "42078846713971", "42720059097224"]` |
| B013 | `bambulab_abs_white_1000_175_p` | `null` | `["40100", "40204456099955", "40883033702515", "40475105493128", "41216786694280"]` |
| B014 | `bambulab_asa_black_1000_175_p` | `null` | `["45101", "40896410648691", "41227780817032"]` |
| B015 | `bambulab_asa_blue_1000_175_p` | `null` | `["45600", "40896410615923", "41227780784264"]` |
| B016 | `bambulab_asa_gray_1000_175_p` | `null` | `["45102", "40896410714227", "41227780882568"]` |
| B017 | `bambulab_asa_green_1000_175_p` | `null` | `["45500", "40896410583155", "41227780751496"]` |
| B018 | `bambulab_asa_red_1000_175_p` | `null` | `["45200", "40896410550387", "41227780718728"]` |
| B019 | `bambulab_asa_white_1000_175_p` | `null` | `["45100", "40896410681459", "41227780849800"]` |
| B020 | `bambulab_pc_black_1000_175_p` | `null` | `["60101", "40404317241459", "41135409528968"]` |
| B021 | `bambulab_pc_clearblack_1000_175_p` | `null` | `["60102", "40821570863219", "40741214617736"]` |
| B022 | `bambulab_pc_transparent_1000_175_p` | `null` | `["60103", "40821570895987", "41135409496200"]` |
| B023 | `bambulab_pc_white_1000_175_p` | `null` | `["60100", "40404317208691", "40741214650504"]` |
| B024 | `bambulab_pc_frblack_1000_175_p` | `null` | `["63100", "546457940221771784"]` |
| B025 | `bambulab_pc_frgrey_1000_175_p` | `null` | `["63102", "546457940221771796"]` |
| B026 | `bambulab_pc_frwhite_1000_175_p` | `null` | `["63101", "546457940221771790"]` |

## Unresolved metadata

Survivor values are kept for PLA Silk single-color and PLA Lite (seven groups); their exact standalone current pages returned 404. Do not borrow Silk+, Multi Color, Basic or another line's TDS. All 20 non-case HEX/representation differences remain unresolved: 15 different single HEX values and five Dual Color single-HEX versus multi-HEX representations. The two Blue Gray/Grey HEX differences are case-only, and the owner-selected Grey values remain. Other field conflicts and current TDS discrepancies not explicitly approved for correction are retained in each reviewed group's JSON audit. No unrelated evidence cleanup is authorized.

| Group | Survivor | Both HEX values |
| --- | --- | --- |
| B003 | `bambulab_abs_beige_1000_175_p` | `{"bambulab_abs_absbeige_1000_175_p": "DACF9D", "bambulab_abs_beige_1000_175_p": "DFD1A7"}` |
| B006 | `bambulab_abs_lavender_1000_175_p` | `{"bambulab_abs_abslavender_1000_175_p": "543C7A", "bambulab_abs_lavender_1000_175_p": "7248BD"}` |
| B021 | `bambulab_pc_clearblack_1000_175_p` | `{"bambulab_pc_clearblack_1000_175_p": "000000", "bambulab_pc_pcclearblack_1000_175_p": "5A5061"}` |
| B041 | `bambulab_pla_aerogray_1000_175_p` | `{"bambulab_pla_aerogray_1000_175_p": "CECDCA", "bambulab_pla_plaaerogray_1000_175_p": "CDCDCB"}` |
| B042 | `bambulab_pla_aerowhite_1000_175_p` | `{"bambulab_pla_aerowhite_1000_175_p": "F5F1DD", "bambulab_pla_plaaerowhite_1000_175_p": "FFFFFF"}` |
| B050 | `bambulab_pla_litered_1000_175_p` | `{"bambulab_pla_litered_1000_175_p": "C6001A", "bambulab_pla_plalitered_1000_175_p": "FF0000"}` |
| B058 | `bambulab_pla_mattedarkchocolate_1000_175_p` | `{"bambulab_pla_mattedarkchocolate_1000_175_p": "4D3324", "bambulab_pla_plamattedarkchocolate_1000_175_p": "3F3730"}` |
| B070 | `bambulab_pla_mattenardogray_1000_175_p` | `{"bambulab_pla_mattenardogray_1000_175_p": "757575", "bambulab_pla_plamattenardogrey_1000_175_p": "737375"}` |
| B071 | `bambulab_pla_matteplum_1000_175_p` | `{"bambulab_pla_matteplum_1000_175_p": "950051", "bambulab_pla_plamatteplum_1000_175_p": "9B3A5F"}` |
| B075 | `bambulab_pla_matteterracotta_1000_175_p` | `{"bambulab_pla_matteterracotta_1000_175_p": "B15533", "bambulab_pla_plamatteterracotta_1000_175_p": "A15636"}` |
| B076 | `bambulab_pla_silkblue_1000_175_p` | `{"bambulab_pla_silkblue_1000_175_p": "147BD1", "bambulab_pla_silkplablue_1000_175_p": "005DA4"}` |
| B077 | `bambulab_pla_silkgold_1000_175_p` | `{"bambulab_pla_silkgold_1000_175_p": "E5B03D", "bambulab_pla_silkplagold_1000_175_p": "F6C500"}` |
| B078 | `bambulab_pla_silkpink_1000_175_p` | `{"bambulab_pla_silkpink_1000_175_p": "EEB1C1", "bambulab_pla_silkplapink_1000_175_p": "F8B9A6"}` |
| B079 | `bambulab_pla_silkpurple_1000_175_p` | `{"bambulab_pla_silkplapurple_1000_175_p": "8D65C7", "bambulab_pla_silkpurple_1000_175_p": "854CE4"}` |
| B080 | `bambulab_pla_silksilver_1000_175_p` | `{"bambulab_pla_silkplasilver_1000_175_p": "ABACB0", "bambulab_pla_silksilver_1000_175_p": "EAECEB"}` |
| B082 | `bambulab_pla_plasilkdualcolorbluehawaii(blue-green)_1000_175_p` | `{"bambulab_pla_plasilkdualcolorbluehawaii(blue-green)_1000_175_p": null, "bambulab_pla_silkpladualcolorbluehawaii(blue-green)_1000_175_p": "39B9DB"}` |
| B083 | `bambulab_pla_plasilkdualcolorgildedrose(pink-gold)_1000_175_p` | `{"bambulab_pla_plasilkdualcolorgildedrose(pink-gold)_1000_175_p": null, "bambulab_pla_silkpladualcolorgildedrose(pink-gold)_1000_175_p": "E3B145"}` |
| B084 | `bambulab_pla_plasilkdualcolormidnightblaze(blue-red)_1000_175_p` | `{"bambulab_pla_plasilkdualcolormidnightblaze(blue-red)_1000_175_p": null, "bambulab_pla_silkpladualcolormidnightblaze(blue-red)_1000_175_p": "0E21AE"}` |
| B085 | `bambulab_pla_plasilkdualcolorneoncity(blue-magenta)_1000_175_p` | `{"bambulab_pla_plasilkdualcolorneoncity(blue-magenta)_1000_175_p": null, "bambulab_pla_silkpladualcolorneoncity(blue-magenta)_1000_175_p": "0E21AE"}` |
| B086 | `bambulab_pla_plasilkdualcolorvelveteclipse(black-red)_1000_175_p` | `{"bambulab_pla_plasilkdualcolorvelveteclipse(black-red)_1000_175_p": null, "bambulab_pla_silkpladualcolorvelveteclipse(black-red)_1000_175_p": "8B3A3A"}` |

## Complete approved retired ID list

The JSON audit retains every exact original baseline key, source-definition location/counts, source template/color, compiled record, metadata conflict and decision. Complete original source definitions remain available at the pinned source base `139a98e6edf87d7158318d6b42ee649cabfad88f`. Each registry entry references that tracked JSON file and the immutable source/audit base commit.

Original STEP 3 candidate notes and nested `OWNER_APPROVAL_REQUIRED` identifier-transfer statuses are preserved historical proposal snapshots, not pending approval gates. The approved root decisions and metadata entries supersede those notes, including their older newer-lot-only wording for printing evidence. Packaging/spool/tare still requires exact lot binding.

| Group | Retired ID | Existing survivor | Rule |
| --- | --- | --- | --- |
| B001 | `bambulab_abs_absazure_1000_175_p` | `bambulab_abs_azure_1000_175_p` | 1 |
| B002 | `bambulab_abs_absbambugreen_1000_175_p` | `bambulab_abs_bambugreen_1000_175_p` | 1 |
| B003 | `bambulab_abs_absbeige_1000_175_p` | `bambulab_abs_beige_1000_175_p` | 1 |
| B004 | `bambulab_abs_absblack_1000_175_p` | `bambulab_abs_black_1000_175_p` | 1 |
| B005 | `bambulab_abs_absblue_1000_175_p` | `bambulab_abs_blue_1000_175_p` | 1 |
| B006 | `bambulab_abs_abslavender_1000_175_p` | `bambulab_abs_lavender_1000_175_p` | 1 |
| B007 | `bambulab_abs_absnavyblue_1000_175_p` | `bambulab_abs_navyblue_1000_175_p` | 1 |
| B008 | `bambulab_abs_absolive_1000_175_p` | `bambulab_abs_olive_1000_175_p` | 1 |
| B009 | `bambulab_abs_absorange_1000_175_p` | `bambulab_abs_orange_1000_175_p` | 1 |
| B010 | `bambulab_abs_absred_1000_175_p` | `bambulab_abs_red_1000_175_p` | 1 |
| B011 | `bambulab_abs_abssilver_1000_175_p` | `bambulab_abs_silver_1000_175_p` | 1 |
| B012 | `bambulab_abs_abstangerineyellow_1000_175_p` | `bambulab_abs_tangerineyellow_1000_175_p` | 1 |
| B013 | `bambulab_abs_abswhite_1000_175_p` | `bambulab_abs_white_1000_175_p` | 1 |
| B014 | `bambulab_asa_asablack_1000_175_p` | `bambulab_asa_black_1000_175_p` | 1 |
| B015 | `bambulab_asa_asablue_1000_175_p` | `bambulab_asa_blue_1000_175_p` | 1 |
| B016 | `bambulab_asa_asagray_1000_175_p` | `bambulab_asa_gray_1000_175_p` | 1 |
| B017 | `bambulab_asa_asagreen_1000_175_p` | `bambulab_asa_green_1000_175_p` | 1 |
| B018 | `bambulab_asa_asared_1000_175_p` | `bambulab_asa_red_1000_175_p` | 1 |
| B019 | `bambulab_asa_asawhite_1000_175_p` | `bambulab_asa_white_1000_175_p` | 1 |
| B020 | `bambulab_pc_pcblack_1000_175_p` | `bambulab_pc_black_1000_175_p` | 1 |
| B021 | `bambulab_pc_pcclearblack_1000_175_p` | `bambulab_pc_clearblack_1000_175_p` | 1 |
| B022 | `bambulab_pc_pctransparent_1000_175_p` | `bambulab_pc_transparent_1000_175_p` | 1 |
| B023 | `bambulab_pc_pcwhite_1000_175_p` | `bambulab_pc_white_1000_175_p` | 1 |
| B024 | `bambulab_pc_pcfrblack_1000_175_p` | `bambulab_pc_frblack_1000_175_p` | 1 |
| B025 | `bambulab_pc_pcfrgray_1000_175_p` | `bambulab_pc_frgrey_1000_175_p` | 1 |
| B026 | `bambulab_pc_pcfrwhite_1000_175_p` | `bambulab_pc_frwhite_1000_175_p` | 1 |
| B027 | `bambulab_petg_petghfblack_1000_175_p` | `bambulab_petg_hfblack_1000_175_p` | 1 |
| B028 | `bambulab_petg_petghfblue_1000_175_p` | `bambulab_petg_hfblue_1000_175_p` | 1 |
| B029 | `bambulab_petg_petghfcream_1000_175_p` | `bambulab_petg_hfcream_1000_175_p` | 1 |
| B030 | `bambulab_petg_petghfdarkgray_1000_175_p` | `bambulab_petg_hfdarkgray_1000_175_p` | 1 |
| B031 | `bambulab_petg_petghfforestgreen_1000_175_p` | `bambulab_petg_hfforestgreen_1000_175_p` | 1 |
| B032 | `bambulab_petg_petghfgray_1000_175_p` | `bambulab_petg_hfgray_1000_175_p` | 1 |
| B033 | `bambulab_petg_petghfgreen_1000_175_p` | `bambulab_petg_hfgreen_1000_175_p` | 1 |
| B034 | `bambulab_petg_petghflakeblue_1000_175_p` | `bambulab_petg_hflakeblue_1000_175_p` | 1 |
| B035 | `bambulab_petg_petghflimegreen_1000_175_p` | `bambulab_petg_hflimegreen_1000_175_p` | 1 |
| B036 | `bambulab_petg_petghforange_1000_175_p` | `bambulab_petg_hforange_1000_175_p` | 1 |
| B037 | `bambulab_petg_petghfpeanutbrown_1000_175_p` | `bambulab_petg_hfpeanutbrown_1000_175_p` | 1 |
| B038 | `bambulab_petg_petghfred_1000_175_p` | `bambulab_petg_hfred_1000_175_p` | 1 |
| B039 | `bambulab_petg_petghfwhite_1000_175_p` | `bambulab_petg_hfwhite_1000_175_p` | 1 |
| B040 | `bambulab_petg_petghfyellow_1000_175_p` | `bambulab_petg_hfyellow_1000_175_p` | 1 |
| B041 | `bambulab_pla_plaaerogray_1000_175_p` | `bambulab_pla_aerogray_1000_175_p` | 1 |
| B042 | `bambulab_pla_plaaerowhite_1000_175_p` | `bambulab_pla_aerowhite_1000_175_p` | 1 |
| B043 | `bambulab_pla_plabasicbluegray_1000_175_p` | `bambulab_pla_plabasicbluegrey_1000_175_p` | owner selection: official Blue Grey |
| B044 | `bambulab_pla_plabasicbluegray_1000_175_r` | `bambulab_pla_plabasicbluegrey_1000_175_r` | owner selection: official Blue Grey |
| B045 | `bambulab_pla_plaglowblue_1000_175_p` | `bambulab_pla_glowblue_1000_175_p` | 1 |
| B046 | `bambulab_pla_plaglowgreen_1000_175_p` | `bambulab_pla_glowgreen_1000_175_p` | 1 |
| B047 | `bambulab_pla_plagloworange_1000_175_p` | `bambulab_pla_gloworange_1000_175_p` | 1 |
| B048 | `bambulab_pla_plaglowpink_1000_175_p` | `bambulab_pla_glowpink_1000_175_p` | 1 |
| B049 | `bambulab_pla_plaglowyellow_1000_175_p` | `bambulab_pla_glowyellow_1000_175_p` | 1 |
| B050 | `bambulab_pla_plalitered_1000_175_p` | `bambulab_pla_litered_1000_175_p` | 1 |
| B051 | `bambulab_pla_plamatteapplegreen_1000_175_p` | `bambulab_pla_matteapplegreen_1000_175_p` | 1 |
| B052 | `bambulab_pla_plamatteashgray_1000_175_p` | `bambulab_pla_matteashgray_1000_175_p` | 1 |
| B053 | `bambulab_pla_plamattebonewhite_1000_175_p` | `bambulab_pla_mattebonewhite_1000_175_p` | 1 |
| B054 | `bambulab_pla_plamattecaramel_1000_175_p` | `bambulab_pla_mattecaramel_1000_175_p` | 1 |
| B055 | `bambulab_pla_plamattecharcoal_1000_175_p` | `bambulab_pla_mattecharcoal_1000_175_p` | 1 |
| B056 | `bambulab_pla_plamattedarkblue_1000_175_p` | `bambulab_pla_mattedarkblue_1000_175_p` | 1 |
| B057 | `bambulab_pla_plamattedarkbrown_1000_175_p` | `bambulab_pla_mattedarkbrown_1000_175_p` | 1 |
| B058 | `bambulab_pla_plamattedarkchocolate_1000_175_p` | `bambulab_pla_mattedarkchocolate_1000_175_p` | 1 |
| B059 | `bambulab_pla_plamattedarkgreen_1000_175_p` | `bambulab_pla_mattedarkgreen_1000_175_p` | 1 |
| B060 | `bambulab_pla_plamattedarkred_1000_175_p` | `bambulab_pla_mattedarkred_1000_175_p` | 1 |
| B061 | `bambulab_pla_plamattedeserttan_1000_175_p` | `bambulab_pla_mattedeserttan_1000_175_p` | 1 |
| B062 | `bambulab_pla_plamattegrassgreen_1000_175_p` | `bambulab_pla_mattegrassgreen_1000_175_p` | 1 |
| B063 | `bambulab_pla_plamatteiceblue_1000_175_p` | `bambulab_pla_matteiceblue_1000_175_p` | 1 |
| B064 | `bambulab_pla_plamatteivorywhite_1000_175_p` | `bambulab_pla_matteivorywhite_1000_175_p` | 1 |
| B065 | `bambulab_pla_plamattelattebrown_1000_175_p` | `bambulab_pla_mattelattebrown_1000_175_p` | 1 |
| B066 | `bambulab_pla_plamattelemonyellow_1000_175_p` | `bambulab_pla_mattelemonyellow_1000_175_p` | 1 |
| B067 | `bambulab_pla_plamattelilacpurple_1000_175_p` | `bambulab_pla_mattelilacpurple_1000_175_p` | 1 |
| B068 | `bambulab_pla_plamattemandarinorange_1000_175_p` | `bambulab_pla_mattemandarinorange_1000_175_p` | 1 |
| B069 | `bambulab_pla_plamattemarineblue_1000_175_p` | `bambulab_pla_mattemarineblue_1000_175_p` | 1 |
| B070 | `bambulab_pla_plamattenardogrey_1000_175_p` | `bambulab_pla_mattenardogray_1000_175_p` | 1 |
| B071 | `bambulab_pla_plamatteplum_1000_175_p` | `bambulab_pla_matteplum_1000_175_p` | 1 |
| B072 | `bambulab_pla_plamattesakurapink_1000_175_p` | `bambulab_pla_mattesakurapink_1000_175_p` | 1 |
| B073 | `bambulab_pla_plamattescarletred_1000_175_p` | `bambulab_pla_mattescarletred_1000_175_p` | 1 |
| B074 | `bambulab_pla_plamatteskyblue_1000_175_p` | `bambulab_pla_matteskyblue_1000_175_p` | 1 |
| B075 | `bambulab_pla_plamatteterracotta_1000_175_p` | `bambulab_pla_matteterracotta_1000_175_p` | 1 |
| B076 | `bambulab_pla_silkplablue_1000_175_p` | `bambulab_pla_silkblue_1000_175_p` | 1 |
| B077 | `bambulab_pla_silkplagold_1000_175_p` | `bambulab_pla_silkgold_1000_175_p` | 1 |
| B078 | `bambulab_pla_silkplapink_1000_175_p` | `bambulab_pla_silkpink_1000_175_p` | 1 |
| B079 | `bambulab_pla_silkplapurple_1000_175_p` | `bambulab_pla_silkpurple_1000_175_p` | 1 |
| B080 | `bambulab_pla_silkplasilver_1000_175_p` | `bambulab_pla_silksilver_1000_175_p` | 1 |
| B081 | `bambulab_pla_silkplawhite_1000_175_p` | `bambulab_pla_silkwhite_1000_175_p` | 1 |
| B082 | `bambulab_pla_silkpladualcolorbluehawaii(blue-green)_1000_175_p` | `bambulab_pla_plasilkdualcolorbluehawaii(blue-green)_1000_175_p` | 3 |
| B083 | `bambulab_pla_silkpladualcolorgildedrose(pink-gold)_1000_175_p` | `bambulab_pla_plasilkdualcolorgildedrose(pink-gold)_1000_175_p` | 3 |
| B084 | `bambulab_pla_silkpladualcolormidnightblaze(blue-red)_1000_175_p` | `bambulab_pla_plasilkdualcolormidnightblaze(blue-red)_1000_175_p` | 3 |
| B085 | `bambulab_pla_silkpladualcolorneoncity(blue-magenta)_1000_175_p` | `bambulab_pla_plasilkdualcolorneoncity(blue-magenta)_1000_175_p` | 3 |
| B086 | `bambulab_pla_silkpladualcolorvelveteclipse(black-red)_1000_175_p` | `bambulab_pla_plasilkdualcolorvelveteclipse(black-red)_1000_175_p` | 3 |
| B087 | `bambulab_pla_plasilk+babyblue_1000_175_p` | `bambulab_pla_silk+babyblue_1000_175_p` | 1 |
| B088 | `bambulab_pla_plasilk+blue_1000_175_p` | `bambulab_pla_silk+blue_1000_175_p` | 1 |
| B089 | `bambulab_pla_plasilk+candygreen_1000_175_p` | `bambulab_pla_silk+candygreen_1000_175_p` | 1 |
| B090 | `bambulab_pla_plasilk+candyred_1000_175_p` | `bambulab_pla_silk+candyred_1000_175_p` | 1 |
| B091 | `bambulab_pla_plasilk+champagne_1000_175_p` | `bambulab_pla_silk+champagne_1000_175_p` | 1 |
| B092 | `bambulab_pla_plasilk+gold_1000_175_p` | `bambulab_pla_silk+gold_1000_175_p` | 1 |
| B093 | `bambulab_pla_plasilk+mint_1000_175_p` | `bambulab_pla_silk+mint_1000_175_p` | 1 |
| B094 | `bambulab_pla_plasilk+pink_1000_175_p` | `bambulab_pla_silk+pink_1000_175_p` | 1 |
| B095 | `bambulab_pla_plasilk+purple_1000_175_p` | `bambulab_pla_silk+purple_1000_175_p` | 1 |
| B096 | `bambulab_pla_plasilk+rosegold_1000_175_p` | `bambulab_pla_silk+rosegold_1000_175_p` | 1 |
| B097 | `bambulab_pla_plasilk+silver_1000_175_p` | `bambulab_pla_silk+silver_1000_175_p` | 1 |
| B098 | `bambulab_pla_plasilk+titangray_1000_175_p` | `bambulab_pla_silk+titangray_1000_175_p` | 1 |
| B099 | `bambulab_pla_plasilk+white_1000_175_p` | `bambulab_pla_silk+white_1000_175_p` | 1 |
| B100 | `bambulab_pla_platough+black_1000_175_p` | `bambulab_pla_tough+black_1000_175_p` | 1 |
| B101 | `bambulab_pla_platough+cyan_1000_175_p` | `bambulab_pla_tough+cyan_1000_175_p` | 1 |
| B102 | `bambulab_pla_platough+gray_1000_175_p` | `bambulab_pla_tough+gray_1000_175_p` | 1 |
| B103 | `bambulab_pla_platough+orange_1000_175_p` | `bambulab_pla_tough+orange_1000_175_p` | 1 |
| B104 | `bambulab_pla_platough+silver_1000_175_p` | `bambulab_pla_tough+silver_1000_175_p` | 1 |
| B105 | `bambulab_pla_platough+white_1000_175_p` | `bambulab_pla_tough+white_1000_175_p` | 1 |
| B106 | `bambulab_pla_platough+yellow_1000_175_p` | `bambulab_pla_tough+yellow_1000_175_p` | 1 |
| B107 | `bambulab_pla_platranslucentblue_1000_175_p` | `bambulab_pla_translucentblue_1000_175_p` | 1 |
| B108 | `bambulab_pla_platranslucentcherrypink_1000_175_p` | `bambulab_pla_translucentcherrypink_1000_175_p` | 1 |
| B109 | `bambulab_pla_platranslucenticeblue_1000_175_p` | `bambulab_pla_translucenticeblue_1000_175_p` | 1 |
| B110 | `bambulab_pla_platranslucentlavender_1000_175_p` | `bambulab_pla_translucentlavender_1000_175_p` | 1 |
| B111 | `bambulab_pla_platranslucentlightjade_1000_175_p` | `bambulab_pla_translucentlightjade_1000_175_p` | 1 |
| B112 | `bambulab_pla_platranslucentmellowyellow_1000_175_p` | `bambulab_pla_translucentmellowyellow_1000_175_p` | 1 |
| B113 | `bambulab_pla_platranslucentorange_1000_175_p` | `bambulab_pla_translucentorange_1000_175_p` | 1 |
| B114 | `bambulab_pla_platranslucentpurple_1000_175_p` | `bambulab_pla_translucentpurple_1000_175_p` | 1 |
| B115 | `bambulab_pla_platranslucentred_1000_175_p` | `bambulab_pla_translucentred_1000_175_p` | 1 |
| B116 | `bambulab_pla_platranslucentteal_1000_175_p` | `bambulab_pla_translucentteal_1000_175_p` | 1 |
| B117 | `bambulab_pva_pvaclear_500_175_p` | `bambulab_pva_clear_500_175_p` | 1 |
| B118 | `bambulab_tpu_tpuforamsblack_1000_175_p` | `bambulab_tpu_foramsblack_1000_175_p` | 1 |
| B119 | `bambulab_tpu_tpuforamsblue_1000_175_p` | `bambulab_tpu_foramsblue_1000_175_p` | 1 |
| B120 | `bambulab_tpu_tpuforamsgray_1000_175_p` | `bambulab_tpu_foramsgray_1000_175_p` | 1 |
| B121 | `bambulab_tpu_tpuforamsneongreen_1000_175_p` | `bambulab_tpu_foramsneongreen_1000_175_p` | 1 |
| B122 | `bambulab_tpu_tpuforamsred_1000_175_p` | `bambulab_tpu_foramsred_1000_175_p` | 1 |
| B123 | `bambulab_tpu_tpuforamswhite_1000_175_p` | `bambulab_tpu_foramswhite_1000_175_p` | 1 |
| B124 | `bambulab_tpu_tpuforamsyellow_1000_175_p` | `bambulab_tpu_foramsyellow_1000_175_p` | 1 |

## Evidence and scope

Official pages and currently linked TDS URLs, retrieval times and SHA-256 hashes are retained in `current_evidence_manifest`; current product-line findings and original conflicts remain in `reviewed_audit`. The 366 out-of-scope records are listed individually in `out_of_scope`. No unreviewed imports, renames, rekeys, packaging changes or namespace cleanup are included.

## Stop gate

One focused local data commit only. Do not fast-forward main, push, post GitHub comments or start another brand without further authorization.
