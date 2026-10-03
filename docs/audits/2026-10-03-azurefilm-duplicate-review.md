# AzureFilm duplicate migration review

Base `c4661dd19ddbe82def150cec8b634cec4e99af11`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `6a59aa8101b950afa28e27c9eb9d2ebc2b68f1d7e06f1362e935c22940a2f20b`.

## Authorization and result

{"groups": 86, "approved_groups": 77, "retired": 77, "deferred": 9, "hard_stops": 0, "before_count": 52575, "after_count": 52498, "brand_before": 496, "brand_after": 419, "registry_before": 859, "registry_after": 936, "metadata_fields_changed": 260, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Official current exact-line TDS values applied only to approved survivor IDs. Scalars replaced by explicit recommendation ranges, not specimen test settings. ABS Plus density1.13→1.04; PCTG1.29→1.26. PLA Prime remains1.27/230/60. PLA Matte historical line is not equated with current Matte HS; Glitter lacks an exact bound technical source, so their survivor values stay unresolved. Silk product-page220-240/80 versus TDS210-240/70-80 retained in evidence. HEX/translucency, all packaging/tare and other variants unchanged.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://azurefilm.com/technical-data-sheets/", "scope": "Current manufacturer document index; separates PLA/PETG/PCTG/ASA/ABS and Prime lines"}
- {"url": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf", "material": "PLA", "template": "{color_name}", "values": {"extruder_temp": null, "extruder_temp_range": [200, 230], "bed_temp": null, "bed_temp_range": [50, 60]}, "scope": "Exact product-line printing values only; no packaging/tare or unique variants changed"}
- {"url": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ABS-plus.pdf", "material": "ABS", "template": "Plus {color_name}", "values": {"density": 1.04, "extruder_temp": null, "extruder_temp_range": [230, 260], "bed_temp": null, "bed_temp_range": [90, 120]}, "scope": "Exact product-line printing values only; no packaging/tare or unique variants changed"}
- {"url": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ASA.pdf", "material": "ASA", "template": "Original {color_name}", "values": {"extruder_temp": null, "extruder_temp_range": [240, 260], "bed_temp": null, "bed_temp_range": [90, 120]}, "scope": "Exact product-line printing values only; no packaging/tare or unique variants changed"}
- {"url": "https://azurefilm.com/wp-content/uploads/2024/04/TDS-ASA-Prime.pptx.pdf", "material": "ASA", "template": "Prime {color_name}", "values": {"extruder_temp": null, "extruder_temp_range": [230, 250]}, "scope": "Exact product-line printing values only; no packaging/tare or unique variants changed"}
- {"url": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-PETG.pdf", "material": "PETG", "template": "{color_name}", "values": {"extruder_temp": null, "extruder_temp_range": [220, 240], "bed_temp": null, "bed_temp_range": [80, 90]}, "scope": "Exact product-line printing values only; no packaging/tare or unique variants changed"}
- {"url": "https://azurefilm.com/wp-content/uploads/2026/03/PCTG_TDS.pdf", "material": "PCTG", "template": "{color_name}", "values": {"density": 1.26, "extruder_temp": null, "extruder_temp_range": [230, 250], "bed_temp": null, "bed_temp_range": [60, 80]}, "scope": "Exact product-line printing values only; no packaging/tare or unique variants changed"}
- {"url": "https://azurefilm.com/wp-content/uploads/2023/10/SILK_TDS.pdf", "material": "PLA", "template": "Silk {color_name}", "values": {"extruder_temp": null, "extruder_temp_range": [210, 240], "bed_temp": null, "bed_temp_range": [70, 80]}, "scope": "Exact product-line printing values only; no packaging/tare or unique variants changed"}
- {"url": "https://azurefilm.com/wp-content/uploads/2024/04/TDS-PLA-Prime.pptx.pdf", "scope": "PLA Prime 1.27 g/cc, 230 C nozzle/60 C bed match existing survivor; unchanged"}
- {"url": "https://azurefilm.com/product/pla-silk-filament-graphite-grey/", "scope": "Product page gives 220-240 C nozzle and80 C bed, within current TDS210-240/70-80; use broader explicitly recommended TDS range and retain page difference as unresolved"}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`azurefilm_abs_absplusblack_1000_175_p`|`azurefilm_abs_plusblack_1000_175_p`|`AzureFilm.json::AzureFilm::ABS Plus {color_name}::ABS Plus Black::ABS::1000::1.75::plastic::False`|
|`azurefilm_abs_absplusblue_1000_175_p`|`azurefilm_abs_plusblue_1000_175_p`|`AzureFilm.json::AzureFilm::ABS Plus {color_name}::ABS Plus Blue::ABS::1000::1.75::plastic::False`|
|`azurefilm_abs_absplusglitterblack_1000_175_p`|`azurefilm_abs_plusglitterblack_1000_175_p`|`AzureFilm.json::AzureFilm::ABS Plus {color_name}::ABS Plus Glitter Black::ABS::1000::1.75::plastic::False`|
|`azurefilm_abs_absplusgreen_1000_175_p`|`azurefilm_abs_plusgreen_1000_175_p`|`AzureFilm.json::AzureFilm::ABS Plus {color_name}::ABS Plus Green::ABS::1000::1.75::plastic::False`|
|`azurefilm_abs_absplusgrey_1000_175_p`|`azurefilm_abs_plusgrey_1000_175_p`|`AzureFilm.json::AzureFilm::ABS Plus {color_name}::ABS Plus Grey::ABS::1000::1.75::plastic::False`|
|`azurefilm_abs_absplusnature_1000_175_p`|`azurefilm_abs_plusnature_1000_175_p`|`AzureFilm.json::AzureFilm::ABS Plus {color_name}::ABS Plus Nature::ABS::1000::1.75::plastic::False`|
|`azurefilm_abs_absplusorange_1000_175_p`|`azurefilm_abs_plusorange_1000_175_p`|`AzureFilm.json::AzureFilm::ABS Plus {color_name}::ABS Plus Orange::ABS::1000::1.75::plastic::False`|
|`azurefilm_abs_absplusred_1000_175_p`|`azurefilm_abs_plusred_1000_175_p`|`AzureFilm.json::AzureFilm::ABS Plus {color_name}::ABS Plus Red::ABS::1000::1.75::plastic::False`|
|`azurefilm_abs_abspluswhite_1000_175_p`|`azurefilm_abs_pluswhite_1000_175_p`|`AzureFilm.json::AzureFilm::ABS Plus {color_name}::ABS Plus White::ABS::1000::1.75::plastic::False`|
|`azurefilm_abs_absplusyellow_1000_175_p`|`azurefilm_abs_plusyellow_1000_175_p`|`AzureFilm.json::AzureFilm::ABS Plus {color_name}::ABS Plus Yellow::ABS::1000::1.75::plastic::False`|
|`azurefilm_asa_asaoriginalblack_1000_175_p`|`azurefilm_asa_originalblack_1000_175_p`|`AzureFilm.json::AzureFilm::ASA Original {color_name}::ASA Original Black::ASA::1000::1.75::plastic::False`|
|`azurefilm_asa_asaoriginalblue_1000_175_p`|`azurefilm_asa_originalblue_1000_175_p`|`AzureFilm.json::AzureFilm::ASA Original {color_name}::ASA Original Blue::ASA::1000::1.75::plastic::False`|
|`azurefilm_asa_asaoriginalgreen_1000_175_p`|`azurefilm_asa_originalgreen_1000_175_p`|`AzureFilm.json::AzureFilm::ASA Original {color_name}::ASA Original Green::ASA::1000::1.75::plastic::False`|
|`azurefilm_asa_asaoriginalgrey_1000_175_p`|`azurefilm_asa_originalgrey_1000_175_p`|`AzureFilm.json::AzureFilm::ASA Original {color_name}::ASA Original Grey::ASA::1000::1.75::plastic::False`|
|`azurefilm_asa_asaoriginalnatural_1000_175_p`|`azurefilm_asa_originalnatural_1000_175_p`|`AzureFilm.json::AzureFilm::ASA Original {color_name}::ASA Original Natural::ASA::1000::1.75::plastic::False`|
|`azurefilm_asa_asaoriginalorange_1000_175_p`|`azurefilm_asa_originalorange_1000_175_p`|`AzureFilm.json::AzureFilm::ASA Original {color_name}::ASA Original Orange::ASA::1000::1.75::plastic::False`|
|`azurefilm_asa_asaoriginalred_1000_175_p`|`azurefilm_asa_originalred_1000_175_p`|`AzureFilm.json::AzureFilm::ASA Original {color_name}::ASA Original Red::ASA::1000::1.75::plastic::False`|
|`azurefilm_asa_asaoriginalsilver_1000_175_p`|`azurefilm_asa_originalsilver_1000_175_p`|`AzureFilm.json::AzureFilm::ASA Original {color_name}::ASA Original Silver::ASA::1000::1.75::plastic::False`|
|`azurefilm_asa_asaoriginalwhite_1000_175_p`|`azurefilm_asa_originalwhite_1000_175_p`|`AzureFilm.json::AzureFilm::ASA Original {color_name}::ASA Original White::ASA::1000::1.75::plastic::False`|
|`azurefilm_asa_asaoriginalyellow_1000_175_p`|`azurefilm_asa_originalyellow_1000_175_p`|`AzureFilm.json::AzureFilm::ASA Original {color_name}::ASA Original Yellow::ASA::1000::1.75::plastic::False`|
|`azurefilm_asa_asaprimeblack_1000_175_p`|`azurefilm_asa_primeblack_1000_175_p`|`AzureFilm.json::AzureFilm::ASA Prime {color_name}::ASA Prime Black::ASA::1000::1.75::plastic::False`|
|`azurefilm_asa_asaprimedarkblue_1000_175_p`|`azurefilm_asa_primedarkblue_1000_175_p`|`AzureFilm.json::AzureFilm::ASA Prime {color_name}::ASA Prime Dark Blue::ASA::1000::1.75::plastic::False`|
|`azurefilm_asa_asaprimered_1000_175_p`|`azurefilm_asa_primered_1000_175_p`|`AzureFilm.json::AzureFilm::ASA Prime {color_name}::ASA Prime Red::ASA::1000::1.75::plastic::False`|
|`azurefilm_asa_asaprimesilver_1000_175_p`|`azurefilm_asa_primesilver_1000_175_p`|`AzureFilm.json::AzureFilm::ASA Prime {color_name}::ASA Prime Silver::ASA::1000::1.75::plastic::False`|
|`azurefilm_asa_asaprimewhite_1000_175_p`|`azurefilm_asa_primewhite_1000_175_p`|`AzureFilm.json::AzureFilm::ASA Prime {color_name}::ASA Prime White::ASA::1000::1.75::plastic::False`|
|`azurefilm_pctg_pctgblack_1000_175_p`|`azurefilm_pctg_black_1000_175_p`|`AzureFilm.json::AzureFilm::PCTG {color_name}::PCTG Black::PCTG::1000::1.75::plastic::False`|
|`azurefilm_pctg_pctggrey_1000_175_p`|`azurefilm_pctg_grey_1000_175_p`|`AzureFilm.json::AzureFilm::PCTG {color_name}::PCTG Grey::PCTG::1000::1.75::plastic::False`|
|`azurefilm_pctg_pctgtransparent_1000_175_p`|`azurefilm_pctg_transparent_1000_175_p`|`AzureFilm.json::AzureFilm::PCTG {color_name}::PCTG Transparent::PCTG::1000::1.75::plastic::False`|
|`azurefilm_pctg_pctgwhite_1000_175_p`|`azurefilm_pctg_white_1000_175_p`|`AzureFilm.json::AzureFilm::PCTG {color_name}::PCTG White::PCTG::1000::1.75::plastic::False`|
|`azurefilm_petg_petgtransparent_1000_175_p`|`azurefilm_petg_transparent_1000_175_p`|`AzureFilm.json::AzureFilm::PETG {color_name}::PETG Transparent::PETG::1000::1.75::plastic::False`|
|`azurefilm_pla_glitterplablack_1000_175_p`|`azurefilm_pla_glitterblack_1000_175_p`|`AzureFilm.json::AzureFilm::Glitter PLA {color_name}::Glitter PLA Black::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_glitterplablue_1000_175_p`|`azurefilm_pla_glitterblue_1000_175_p`|`AzureFilm.json::AzureFilm::Glitter PLA {color_name}::Glitter PLA Blue::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_glitterplagreen_1000_175_p`|`azurefilm_pla_glittergreen_1000_175_p`|`AzureFilm.json::AzureFilm::Glitter PLA {color_name}::Glitter PLA Green::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_glitterplanature_1000_175_p`|`azurefilm_pla_glitternature_1000_175_p`|`AzureFilm.json::AzureFilm::Glitter PLA {color_name}::Glitter PLA Nature::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_glitterplared_1000_175_p`|`azurefilm_pla_glitterred_1000_175_p`|`AzureFilm.json::AzureFilm::Glitter PLA {color_name}::Glitter PLA Red::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_glitterplawhite_1000_175_p`|`azurefilm_pla_glitterwhite_1000_175_p`|`AzureFilm.json::AzureFilm::Glitter PLA {color_name}::Glitter PLA White::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plaanthracite_1000_175_p`|`azurefilm_pla_anthracite_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Anthracite::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plablack_1000_175_p`|`azurefilm_pla_black_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Black::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plablue_1000_175_p`|`azurefilm_pla_blue_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Blue::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plachampagne_1000_175_p`|`azurefilm_pla_champagne_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Champagne::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plachampagnegold_1000_175_p`|`azurefilm_pla_champagnegold_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Champagne Gold::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_placoralred_1000_175_p`|`azurefilm_pla_coralred_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Coral Red::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plafoggywhite_1000_175_p`|`azurefilm_pla_foggywhite_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Foggy White::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plafuchsiapink_1000_175_p`|`azurefilm_pla_fuchsiapink_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Fuchsia Pink::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plagalaxyblack_1000_175_p`|`azurefilm_pla_galaxyblack_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Galaxy Black::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plagold_1000_175_p`|`azurefilm_pla_gold_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Gold::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plagreen_1000_175_p`|`azurefilm_pla_green_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Green::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plalightgreen_1000_175_p`|`azurefilm_pla_lightgreen_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Light Green::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plalightgrey_1000_175_p`|`azurefilm_pla_lightgrey_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Light Grey::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plamarble_1000_175_p`|`azurefilm_pla_marble_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Marble::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_planavyblue_1000_175_p`|`azurefilm_pla_navyblue_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Navy Blue::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plaorange_1000_175_p`|`azurefilm_pla_orange_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Orange::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plapink_1000_175_p`|`azurefilm_pla_pink_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Pink::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plaprimeblack_1000_175_p`|`azurefilm_pla_primeblack_1000_175_p`|`AzureFilm.json::AzureFilm::PLA Prime {color_name}::PLA Prime Black::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plaprimedarkblue_1000_175_p`|`azurefilm_pla_primedarkblue_1000_175_p`|`AzureFilm.json::AzureFilm::PLA Prime {color_name}::PLA Prime Dark Blue::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plaprimedarkgrey_1000_175_p`|`azurefilm_pla_primedarkgrey_1000_175_p`|`AzureFilm.json::AzureFilm::PLA Prime {color_name}::PLA Prime Dark Grey::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plaprimelightgrey_1000_175_p`|`azurefilm_pla_primelightgrey_1000_175_p`|`AzureFilm.json::AzureFilm::PLA Prime {color_name}::PLA Prime Light Grey::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plaprimenature_1000_175_p`|`azurefilm_pla_primenature_1000_175_p`|`AzureFilm.json::AzureFilm::PLA Prime {color_name}::PLA Prime Nature::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plaprimered_1000_175_p`|`azurefilm_pla_primered_1000_175_p`|`AzureFilm.json::AzureFilm::PLA Prime {color_name}::PLA Prime Red::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plaprimewhite_1000_175_p`|`azurefilm_pla_primewhite_1000_175_p`|`AzureFilm.json::AzureFilm::PLA Prime {color_name}::PLA Prime White::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plaredwine_1000_175_p`|`azurefilm_pla_redwine_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Red Wine::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plasharkgrey_1000_175_p`|`azurefilm_pla_sharkgrey_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Shark Grey::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plasunsetorange_1000_175_p`|`azurefilm_pla_sunsetorange_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Sunset Orange::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_plawhite_1000_175_p`|`azurefilm_pla_white_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA White::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_playellow_1000_175_p`|`azurefilm_pla_yellow_1000_175_p`|`AzureFilm.json::AzureFilm::PLA {color_name}::PLA Yellow::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_silkpladarkcopper_1000_175_p`|`azurefilm_pla_silkdarkcopper_1000_175_p`|`AzureFilm.json::AzureFilm::Silk PLA {color_name}::Silk PLA Dark copper::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_silkplaflameorange_1000_175_p`|`azurefilm_pla_silkflameorange_1000_175_p`|`AzureFilm.json::AzureFilm::Silk PLA {color_name}::Silk PLA Flame orange::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_silkplajunglegold_1000_175_p`|`azurefilm_pla_silkjunglegold_1000_175_p`|`AzureFilm.json::AzureFilm::Silk PLA {color_name}::Silk PLA Jungle gold::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_silkplalime_1000_175_p`|`azurefilm_pla_silklime_1000_175_p`|`AzureFilm.json::AzureFilm::Silk PLA {color_name}::Silk PLA Lime::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_silkplaolivegold_1000_175_p`|`azurefilm_pla_silkolivegold_1000_175_p`|`AzureFilm.json::AzureFilm::Silk PLA {color_name}::Silk PLA Olive gold::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_silkplapink_1000_175_p`|`azurefilm_pla_silkpink_1000_175_p`|`AzureFilm.json::AzureFilm::Silk PLA {color_name}::Silk PLA Pink::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_silkplarainbowtropicana_1000_175_p`|`azurefilm_pla_silkrainbowtropicana_1000_175_p`|`AzureFilm.json::AzureFilm::Silk PLA {color_name}::Silk PLA Rainbow Tropicana::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_silkplarose_1000_175_p`|`azurefilm_pla_silkrose_1000_175_p`|`AzureFilm.json::AzureFilm::Silk PLA {color_name}::Silk PLA Rose::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_silkplasand_1000_175_p`|`azurefilm_pla_silksand_1000_175_p`|`AzureFilm.json::AzureFilm::Silk PLA {color_name}::Silk PLA Sand::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_silkplasilver_1000_175_p`|`azurefilm_pla_silksilver_1000_175_p`|`AzureFilm.json::AzureFilm::Silk PLA {color_name}::Silk PLA Silver::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_silkplaskyblue_1000_175_p`|`azurefilm_pla_silkskyblue_1000_175_p`|`AzureFilm.json::AzureFilm::Silk PLA {color_name}::Silk PLA Sky blue::PLA::1000::1.75::plastic::False`|
|`azurefilm_pla_silkplawhite_1000_175_p`|`azurefilm_pla_silkwhite_1000_175_p`|`AzureFilm.json::AzureFilm::Silk PLA {color_name}::Silk PLA White::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### AF001: dup-c69c07840581a40ded103bfaeaf0361af156abeb8d4296e28ab3c7d1855e90cd

Status: APPROVED; survivor `azurefilm_abs_plusblack_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_abs_absplusblack_1000_175_p`|`ABS Plus {color_name}`|`Black`|{"source_file": "AzureFilm.json", "definition_index": 16, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_abs_plusblack_1000_175_p`|`Plus {color_name}`|`BLACK`|{"source_file": "AzureFilm.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_abs_absplusblack_1000_175_p": null,
    "azurefilm_abs_plusblack_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_abs_absplusblack_1000_175_p": [
      250,
      250
    ],
    "azurefilm_abs_plusblack_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_abs_absplusblack_1000_175_p": null,
    "azurefilm_abs_plusblack_1000_175_p": 110
  },
  "bed_temp_range": {
    "azurefilm_abs_absplusblack_1000_175_p": [
      110,
      110
    ],
    "azurefilm_abs_plusblack_1000_175_p": null
  }
}
```

### AF002: dup-dbe49efc02c21ba8625ba2d502be1ee63fe1d67aeedd3fe067cb546dab1087b7

Status: APPROVED; survivor `azurefilm_abs_plusblue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_abs_absplusblue_1000_175_p`|`ABS Plus {color_name}`|`Blue`|{"source_file": "AzureFilm.json", "definition_index": 16, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_abs_plusblue_1000_175_p`|`Plus {color_name}`|`BLUE`|{"source_file": "AzureFilm.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_abs_absplusblue_1000_175_p": null,
    "azurefilm_abs_plusblue_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_abs_absplusblue_1000_175_p": [
      250,
      250
    ],
    "azurefilm_abs_plusblue_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_abs_absplusblue_1000_175_p": null,
    "azurefilm_abs_plusblue_1000_175_p": 110
  },
  "bed_temp_range": {
    "azurefilm_abs_absplusblue_1000_175_p": [
      110,
      110
    ],
    "azurefilm_abs_plusblue_1000_175_p": null
  }
}
```

### AF003: dup-71f83a3d30831c85ccb4cd5263aac581ef93a33eaa00e2d8fc3897db656c0f05

Status: APPROVED; survivor `azurefilm_abs_plusglitterblack_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_abs_absplusglitterblack_1000_175_p`|`ABS Plus {color_name}`|`Glitter Black`|{"source_file": "AzureFilm.json", "definition_index": 16, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_abs_plusglitterblack_1000_175_p`|`Plus {color_name}`|`GLITTER BLACK`|{"source_file": "AzureFilm.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_abs_absplusglitterblack_1000_175_p": null,
    "azurefilm_abs_plusglitterblack_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_abs_absplusglitterblack_1000_175_p": [
      250,
      250
    ],
    "azurefilm_abs_plusglitterblack_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_abs_absplusglitterblack_1000_175_p": null,
    "azurefilm_abs_plusglitterblack_1000_175_p": 110
  },
  "bed_temp_range": {
    "azurefilm_abs_absplusglitterblack_1000_175_p": [
      110,
      110
    ],
    "azurefilm_abs_plusglitterblack_1000_175_p": null
  }
}
```

### AF004: dup-69299ce832685f5e5f2499e5e6d5e03582a06160fae2ad4f221554975b4a51b7

Status: APPROVED; survivor `azurefilm_abs_plusgreen_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_abs_absplusgreen_1000_175_p`|`ABS Plus {color_name}`|`Green`|{"source_file": "AzureFilm.json", "definition_index": 16, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_abs_plusgreen_1000_175_p`|`Plus {color_name}`|`GREEN`|{"source_file": "AzureFilm.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_abs_absplusgreen_1000_175_p": null,
    "azurefilm_abs_plusgreen_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_abs_absplusgreen_1000_175_p": [
      250,
      250
    ],
    "azurefilm_abs_plusgreen_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_abs_absplusgreen_1000_175_p": null,
    "azurefilm_abs_plusgreen_1000_175_p": 110
  },
  "bed_temp_range": {
    "azurefilm_abs_absplusgreen_1000_175_p": [
      110,
      110
    ],
    "azurefilm_abs_plusgreen_1000_175_p": null
  }
}
```

### AF005: dup-ac93398477eed23a0b067a89289dc33dcf413c99e37558dfe0789e73dac7da53

Status: APPROVED; survivor `azurefilm_abs_plusgrey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_abs_absplusgrey_1000_175_p`|`ABS Plus {color_name}`|`Grey`|{"source_file": "AzureFilm.json", "definition_index": 16, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_abs_plusgrey_1000_175_p`|`Plus {color_name}`|`GREY`|{"source_file": "AzureFilm.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_abs_absplusgrey_1000_175_p": null,
    "azurefilm_abs_plusgrey_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_abs_absplusgrey_1000_175_p": [
      250,
      250
    ],
    "azurefilm_abs_plusgrey_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_abs_absplusgrey_1000_175_p": null,
    "azurefilm_abs_plusgrey_1000_175_p": 110
  },
  "bed_temp_range": {
    "azurefilm_abs_absplusgrey_1000_175_p": [
      110,
      110
    ],
    "azurefilm_abs_plusgrey_1000_175_p": null
  }
}
```

### AF006: dup-4009dc88f8f539b2ad52ce13a41c583292f01b5870a2a14d7cbd85d42a093345

Status: APPROVED; survivor `azurefilm_abs_plusnature_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_abs_absplusnature_1000_175_p`|`ABS Plus {color_name}`|`Nature`|{"source_file": "AzureFilm.json", "definition_index": 16, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_abs_plusnature_1000_175_p`|`Plus {color_name}`|`NATURE`|{"source_file": "AzureFilm.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_abs_absplusnature_1000_175_p": null,
    "azurefilm_abs_plusnature_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_abs_absplusnature_1000_175_p": [
      250,
      250
    ],
    "azurefilm_abs_plusnature_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_abs_absplusnature_1000_175_p": null,
    "azurefilm_abs_plusnature_1000_175_p": 110
  },
  "bed_temp_range": {
    "azurefilm_abs_absplusnature_1000_175_p": [
      110,
      110
    ],
    "azurefilm_abs_plusnature_1000_175_p": null
  }
}
```

### AF007: dup-a8707f3e4f5b692b74ada6b3a4e08296173b78b0026746a56fbce49cb0bbc3cc

Status: APPROVED; survivor `azurefilm_abs_plusorange_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_abs_absplusorange_1000_175_p`|`ABS Plus {color_name}`|`Orange`|{"source_file": "AzureFilm.json", "definition_index": 16, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_abs_plusorange_1000_175_p`|`Plus {color_name}`|`ORANGE`|{"source_file": "AzureFilm.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_abs_absplusorange_1000_175_p": null,
    "azurefilm_abs_plusorange_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_abs_absplusorange_1000_175_p": [
      250,
      250
    ],
    "azurefilm_abs_plusorange_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_abs_absplusorange_1000_175_p": null,
    "azurefilm_abs_plusorange_1000_175_p": 110
  },
  "bed_temp_range": {
    "azurefilm_abs_absplusorange_1000_175_p": [
      110,
      110
    ],
    "azurefilm_abs_plusorange_1000_175_p": null
  }
}
```

### AF008: dup-a8aad15ee3f5c5c880f31fd8fb76605ee4b34d18e0a3983255c6b915e728f847

Status: APPROVED; survivor `azurefilm_abs_plusred_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_abs_absplusred_1000_175_p`|`ABS Plus {color_name}`|`Red`|{"source_file": "AzureFilm.json", "definition_index": 16, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_abs_plusred_1000_175_p`|`Plus {color_name}`|`RED`|{"source_file": "AzureFilm.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_abs_absplusred_1000_175_p": null,
    "azurefilm_abs_plusred_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_abs_absplusred_1000_175_p": [
      250,
      250
    ],
    "azurefilm_abs_plusred_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_abs_absplusred_1000_175_p": null,
    "azurefilm_abs_plusred_1000_175_p": 110
  },
  "bed_temp_range": {
    "azurefilm_abs_absplusred_1000_175_p": [
      110,
      110
    ],
    "azurefilm_abs_plusred_1000_175_p": null
  }
}
```

### AF009: dup-835d90e714affb6db732047fa17a34517972605a1c2cbe4af14cd91b710ab1de

Status: APPROVED; survivor `azurefilm_abs_pluswhite_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_abs_abspluswhite_1000_175_p`|`ABS Plus {color_name}`|`White`|{"source_file": "AzureFilm.json", "definition_index": 16, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_abs_pluswhite_1000_175_p`|`Plus {color_name}`|`WHITE`|{"source_file": "AzureFilm.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_abs_abspluswhite_1000_175_p": null,
    "azurefilm_abs_pluswhite_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_abs_abspluswhite_1000_175_p": [
      250,
      250
    ],
    "azurefilm_abs_pluswhite_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_abs_abspluswhite_1000_175_p": null,
    "azurefilm_abs_pluswhite_1000_175_p": 110
  },
  "bed_temp_range": {
    "azurefilm_abs_abspluswhite_1000_175_p": [
      110,
      110
    ],
    "azurefilm_abs_pluswhite_1000_175_p": null
  }
}
```

### AF010: dup-5ef365bff869b961cf61c084da533f2b3ed37d1d6ffa152628ebe0ab0c9b17dd

Status: APPROVED; survivor `azurefilm_abs_plusyellow_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_abs_absplusyellow_1000_175_p`|`ABS Plus {color_name}`|`Yellow`|{"source_file": "AzureFilm.json", "definition_index": 16, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_abs_plusyellow_1000_175_p`|`Plus {color_name}`|`YELLOW`|{"source_file": "AzureFilm.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_abs_absplusyellow_1000_175_p": null,
    "azurefilm_abs_plusyellow_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_abs_absplusyellow_1000_175_p": [
      250,
      250
    ],
    "azurefilm_abs_plusyellow_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_abs_absplusyellow_1000_175_p": null,
    "azurefilm_abs_plusyellow_1000_175_p": 110
  },
  "bed_temp_range": {
    "azurefilm_abs_absplusyellow_1000_175_p": [
      110,
      110
    ],
    "azurefilm_abs_plusyellow_1000_175_p": null
  }
}
```

### AF011: dup-1a7f968e85cf6a58c5d4be8020adf115b569fd21b368b6da514ec312026464d3

Status: APPROVED; survivor `azurefilm_asa_originalblack_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_asa_asaoriginalblack_1000_175_p`|`ASA Original {color_name}`|`Black`|{"source_file": "AzureFilm.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_asa_originalblack_1000_175_p`|`Original {color_name}`|`BLACK`|{"source_file": "AzureFilm.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_asa_asaoriginalblack_1000_175_p": null,
    "azurefilm_asa_originalblack_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_asa_asaoriginalblack_1000_175_p": [
      250,
      250
    ],
    "azurefilm_asa_originalblack_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_asa_asaoriginalblack_1000_175_p": null,
    "azurefilm_asa_originalblack_1000_175_p": 100
  },
  "bed_temp_range": {
    "azurefilm_asa_asaoriginalblack_1000_175_p": [
      100,
      100
    ],
    "azurefilm_asa_originalblack_1000_175_p": null
  }
}
```

### AF012: dup-f7ab216c31435d084554ec0831b7855c689b7a61620a9c5a50c78bf54381e12a

Status: APPROVED; survivor `azurefilm_asa_originalblue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_asa_asaoriginalblue_1000_175_p`|`ASA Original {color_name}`|`Blue`|{"source_file": "AzureFilm.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_asa_originalblue_1000_175_p`|`Original {color_name}`|`BLUE`|{"source_file": "AzureFilm.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_asa_asaoriginalblue_1000_175_p": null,
    "azurefilm_asa_originalblue_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_asa_asaoriginalblue_1000_175_p": [
      250,
      250
    ],
    "azurefilm_asa_originalblue_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_asa_asaoriginalblue_1000_175_p": null,
    "azurefilm_asa_originalblue_1000_175_p": 100
  },
  "bed_temp_range": {
    "azurefilm_asa_asaoriginalblue_1000_175_p": [
      100,
      100
    ],
    "azurefilm_asa_originalblue_1000_175_p": null
  }
}
```

### AF013: dup-496625f7009ad1cc6b3ae630a778928c3c196d63bab22383ff7a9eedc9935253

Status: APPROVED; survivor `azurefilm_asa_originalgreen_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_asa_asaoriginalgreen_1000_175_p`|`ASA Original {color_name}`|`Green`|{"source_file": "AzureFilm.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_asa_originalgreen_1000_175_p`|`Original {color_name}`|`GREEN`|{"source_file": "AzureFilm.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_asa_asaoriginalgreen_1000_175_p": null,
    "azurefilm_asa_originalgreen_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_asa_asaoriginalgreen_1000_175_p": [
      250,
      250
    ],
    "azurefilm_asa_originalgreen_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_asa_asaoriginalgreen_1000_175_p": null,
    "azurefilm_asa_originalgreen_1000_175_p": 100
  },
  "bed_temp_range": {
    "azurefilm_asa_asaoriginalgreen_1000_175_p": [
      100,
      100
    ],
    "azurefilm_asa_originalgreen_1000_175_p": null
  }
}
```

### AF014: dup-3698c381782e20e78f1782bdc09cb13499c3869cd41418a4eda14452506e5140

Status: APPROVED; survivor `azurefilm_asa_originalgrey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_asa_asaoriginalgrey_1000_175_p`|`ASA Original {color_name}`|`Grey`|{"source_file": "AzureFilm.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_asa_originalgrey_1000_175_p`|`Original {color_name}`|`GREY`|{"source_file": "AzureFilm.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_asa_asaoriginalgrey_1000_175_p": null,
    "azurefilm_asa_originalgrey_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_asa_asaoriginalgrey_1000_175_p": [
      250,
      250
    ],
    "azurefilm_asa_originalgrey_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_asa_asaoriginalgrey_1000_175_p": null,
    "azurefilm_asa_originalgrey_1000_175_p": 100
  },
  "bed_temp_range": {
    "azurefilm_asa_asaoriginalgrey_1000_175_p": [
      100,
      100
    ],
    "azurefilm_asa_originalgrey_1000_175_p": null
  }
}
```

### AF015: dup-f83ca56afb76f4f3e94e627576e83a1564d6cfb566cf8fbe5d56fac1277756b0

Status: APPROVED; survivor `azurefilm_asa_originalnatural_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_asa_asaoriginalnatural_1000_175_p`|`ASA Original {color_name}`|`Natural`|{"source_file": "AzureFilm.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_asa_originalnatural_1000_175_p`|`Original {color_name}`|`NATURAL`|{"source_file": "AzureFilm.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_asa_asaoriginalnatural_1000_175_p": null,
    "azurefilm_asa_originalnatural_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_asa_asaoriginalnatural_1000_175_p": [
      250,
      250
    ],
    "azurefilm_asa_originalnatural_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_asa_asaoriginalnatural_1000_175_p": null,
    "azurefilm_asa_originalnatural_1000_175_p": 100
  },
  "bed_temp_range": {
    "azurefilm_asa_asaoriginalnatural_1000_175_p": [
      100,
      100
    ],
    "azurefilm_asa_originalnatural_1000_175_p": null
  }
}
```

### AF016: dup-6a2b22e55d6436787babd71f6e26c73a137976753059335a5363fe9106a6bd23

Status: APPROVED; survivor `azurefilm_asa_originalorange_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_asa_asaoriginalorange_1000_175_p`|`ASA Original {color_name}`|`Orange`|{"source_file": "AzureFilm.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_asa_originalorange_1000_175_p`|`Original {color_name}`|`ORANGE`|{"source_file": "AzureFilm.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_asa_asaoriginalorange_1000_175_p": null,
    "azurefilm_asa_originalorange_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_asa_asaoriginalorange_1000_175_p": [
      250,
      250
    ],
    "azurefilm_asa_originalorange_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_asa_asaoriginalorange_1000_175_p": null,
    "azurefilm_asa_originalorange_1000_175_p": 100
  },
  "bed_temp_range": {
    "azurefilm_asa_asaoriginalorange_1000_175_p": [
      100,
      100
    ],
    "azurefilm_asa_originalorange_1000_175_p": null
  }
}
```

### AF017: dup-6312ae09b844634c9147a566fce92af223d6baee9fdb57617e82d15907ca1414

Status: APPROVED; survivor `azurefilm_asa_originalred_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_asa_asaoriginalred_1000_175_p`|`ASA Original {color_name}`|`Red`|{"source_file": "AzureFilm.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_asa_originalred_1000_175_p`|`Original {color_name}`|`RED`|{"source_file": "AzureFilm.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_asa_asaoriginalred_1000_175_p": null,
    "azurefilm_asa_originalred_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_asa_asaoriginalred_1000_175_p": [
      250,
      250
    ],
    "azurefilm_asa_originalred_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_asa_asaoriginalred_1000_175_p": null,
    "azurefilm_asa_originalred_1000_175_p": 100
  },
  "bed_temp_range": {
    "azurefilm_asa_asaoriginalred_1000_175_p": [
      100,
      100
    ],
    "azurefilm_asa_originalred_1000_175_p": null
  }
}
```

### AF018: dup-1222b3e2e6878ad884f0e5485a5f60a0086170f8edc538c4a76ea841d8f91fc0

Status: APPROVED; survivor `azurefilm_asa_originalsilver_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_asa_asaoriginalsilver_1000_175_p`|`ASA Original {color_name}`|`Silver`|{"source_file": "AzureFilm.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_asa_originalsilver_1000_175_p`|`Original {color_name}`|`SILVER`|{"source_file": "AzureFilm.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_asa_asaoriginalsilver_1000_175_p": null,
    "azurefilm_asa_originalsilver_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_asa_asaoriginalsilver_1000_175_p": [
      250,
      250
    ],
    "azurefilm_asa_originalsilver_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_asa_asaoriginalsilver_1000_175_p": null,
    "azurefilm_asa_originalsilver_1000_175_p": 100
  },
  "bed_temp_range": {
    "azurefilm_asa_asaoriginalsilver_1000_175_p": [
      100,
      100
    ],
    "azurefilm_asa_originalsilver_1000_175_p": null
  }
}
```

### AF019: dup-23c9c627e7b1308adea2c38d10e47abbaef809dc4129c7ead8b8bf211847fce0

Status: APPROVED; survivor `azurefilm_asa_originalwhite_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_asa_asaoriginalwhite_1000_175_p`|`ASA Original {color_name}`|`White`|{"source_file": "AzureFilm.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_asa_originalwhite_1000_175_p`|`Original {color_name}`|`WHITE`|{"source_file": "AzureFilm.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_asa_asaoriginalwhite_1000_175_p": null,
    "azurefilm_asa_originalwhite_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_asa_asaoriginalwhite_1000_175_p": [
      250,
      250
    ],
    "azurefilm_asa_originalwhite_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_asa_asaoriginalwhite_1000_175_p": null,
    "azurefilm_asa_originalwhite_1000_175_p": 100
  },
  "bed_temp_range": {
    "azurefilm_asa_asaoriginalwhite_1000_175_p": [
      100,
      100
    ],
    "azurefilm_asa_originalwhite_1000_175_p": null
  }
}
```

### AF020: dup-91468c857ce4aa928b96e4b5b9ebfd38bf2b4a2fef7d6fab1460b2c3413beea6

Status: APPROVED; survivor `azurefilm_asa_originalyellow_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_asa_asaoriginalyellow_1000_175_p`|`ASA Original {color_name}`|`Yellow`|{"source_file": "AzureFilm.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`azurefilm_asa_originalyellow_1000_175_p`|`Original {color_name}`|`YELLOW`|{"source_file": "AzureFilm.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_asa_asaoriginalyellow_1000_175_p": null,
    "azurefilm_asa_originalyellow_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_asa_asaoriginalyellow_1000_175_p": [
      250,
      250
    ],
    "azurefilm_asa_originalyellow_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_asa_asaoriginalyellow_1000_175_p": null,
    "azurefilm_asa_originalyellow_1000_175_p": 100
  },
  "bed_temp_range": {
    "azurefilm_asa_asaoriginalyellow_1000_175_p": [
      100,
      100
    ],
    "azurefilm_asa_originalyellow_1000_175_p": null
  }
}
```

### AF021: dup-b777e37c43d19c8968a9cce3204f9dcee7e519d5bc2d86c2c18492ee6108074a

Status: APPROVED; survivor `azurefilm_asa_primeblack_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_asa_asaprimeblack_1000_175_p`|`ASA Prime {color_name}`|`Black`|{"source_file": "AzureFilm.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / False|
|`azurefilm_asa_primeblack_1000_175_p`|`Prime {color_name}`|`BLACK`|{"source_file": "AzureFilm.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_asa_asaprimeblack_1000_175_p": null,
    "azurefilm_asa_primeblack_1000_175_p": 245
  },
  "extruder_temp_range": {
    "azurefilm_asa_asaprimeblack_1000_175_p": [
      245,
      245
    ],
    "azurefilm_asa_primeblack_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_asa_asaprimeblack_1000_175_p": null,
    "azurefilm_asa_primeblack_1000_175_p": 90
  },
  "bed_temp_range": {
    "azurefilm_asa_asaprimeblack_1000_175_p": [
      90,
      90
    ],
    "azurefilm_asa_primeblack_1000_175_p": null
  }
}
```

### AF022: dup-9199ecad9efe27865566ba96bb94f44d549164f5497de39e748a9cf94d53aad6

Status: APPROVED; survivor `azurefilm_asa_primedarkblue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_asa_asaprimedarkblue_1000_175_p`|`ASA Prime {color_name}`|`Dark Blue`|{"source_file": "AzureFilm.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / False|
|`azurefilm_asa_primedarkblue_1000_175_p`|`Prime {color_name}`|`DARK BLUE`|{"source_file": "AzureFilm.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_asa_asaprimedarkblue_1000_175_p": null,
    "azurefilm_asa_primedarkblue_1000_175_p": 245
  },
  "extruder_temp_range": {
    "azurefilm_asa_asaprimedarkblue_1000_175_p": [
      245,
      245
    ],
    "azurefilm_asa_primedarkblue_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_asa_asaprimedarkblue_1000_175_p": null,
    "azurefilm_asa_primedarkblue_1000_175_p": 90
  },
  "bed_temp_range": {
    "azurefilm_asa_asaprimedarkblue_1000_175_p": [
      90,
      90
    ],
    "azurefilm_asa_primedarkblue_1000_175_p": null
  }
}
```

### AF023: dup-7c9fc231d77636895ede8d99f1bbeaf3dd841979f4695fff70d66f7cbea9cff0

Status: APPROVED; survivor `azurefilm_asa_primered_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_asa_asaprimered_1000_175_p`|`ASA Prime {color_name}`|`Red`|{"source_file": "AzureFilm.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / False|
|`azurefilm_asa_primered_1000_175_p`|`Prime {color_name}`|`RED`|{"source_file": "AzureFilm.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_asa_asaprimered_1000_175_p": null,
    "azurefilm_asa_primered_1000_175_p": 245
  },
  "extruder_temp_range": {
    "azurefilm_asa_asaprimered_1000_175_p": [
      245,
      245
    ],
    "azurefilm_asa_primered_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_asa_asaprimered_1000_175_p": null,
    "azurefilm_asa_primered_1000_175_p": 90
  },
  "bed_temp_range": {
    "azurefilm_asa_asaprimered_1000_175_p": [
      90,
      90
    ],
    "azurefilm_asa_primered_1000_175_p": null
  }
}
```

### AF024: dup-4bc613ced3b662339c9b06c90bb6c3d34a51e5401850c1212a826b7dd002da6f

Status: APPROVED; survivor `azurefilm_asa_primesilver_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_asa_asaprimesilver_1000_175_p`|`ASA Prime {color_name}`|`Silver`|{"source_file": "AzureFilm.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / False|
|`azurefilm_asa_primesilver_1000_175_p`|`Prime {color_name}`|`SILVER`|{"source_file": "AzureFilm.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_asa_asaprimesilver_1000_175_p": null,
    "azurefilm_asa_primesilver_1000_175_p": 245
  },
  "extruder_temp_range": {
    "azurefilm_asa_asaprimesilver_1000_175_p": [
      245,
      245
    ],
    "azurefilm_asa_primesilver_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_asa_asaprimesilver_1000_175_p": null,
    "azurefilm_asa_primesilver_1000_175_p": 90
  },
  "bed_temp_range": {
    "azurefilm_asa_asaprimesilver_1000_175_p": [
      90,
      90
    ],
    "azurefilm_asa_primesilver_1000_175_p": null
  }
}
```

### AF025: dup-2f3d0a289cf9e2debf9eababad09aee82b8a46b825747ae8c14f7a3143e068a6

Status: APPROVED; survivor `azurefilm_asa_primewhite_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_asa_asaprimewhite_1000_175_p`|`ASA Prime {color_name}`|`White`|{"source_file": "AzureFilm.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / False|
|`azurefilm_asa_primewhite_1000_175_p`|`Prime {color_name}`|`WHITE`|{"source_file": "AzureFilm.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_asa_asaprimewhite_1000_175_p": null,
    "azurefilm_asa_primewhite_1000_175_p": 245
  },
  "extruder_temp_range": {
    "azurefilm_asa_asaprimewhite_1000_175_p": [
      245,
      245
    ],
    "azurefilm_asa_primewhite_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_asa_asaprimewhite_1000_175_p": null,
    "azurefilm_asa_primewhite_1000_175_p": 90
  },
  "bed_temp_range": {
    "azurefilm_asa_asaprimewhite_1000_175_p": [
      90,
      90
    ],
    "azurefilm_asa_primewhite_1000_175_p": null
  }
}
```

### AF026: dup-a35495b3b81b38b96fb1117566f418283af830eab0b509bf3f7c7adecef5273f

Status: APPROVED; survivor `azurefilm_pctg_black_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pctg_black_1000_175_p`|`{color_name}`|`BLACK`|{"source_file": "AzureFilm.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / True|
|`azurefilm_pctg_pctgblack_1000_175_p`|`PCTG {color_name}`|`Black`|{"source_file": "AzureFilm.json", "definition_index": 21, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_pctg_black_1000_175_p": 250,
    "azurefilm_pctg_pctgblack_1000_175_p": null
  },
  "extruder_temp_range": {
    "azurefilm_pctg_black_1000_175_p": null,
    "azurefilm_pctg_pctgblack_1000_175_p": [
      250,
      250
    ]
  },
  "bed_temp": {
    "azurefilm_pctg_black_1000_175_p": 80,
    "azurefilm_pctg_pctgblack_1000_175_p": null
  },
  "bed_temp_range": {
    "azurefilm_pctg_black_1000_175_p": null,
    "azurefilm_pctg_pctgblack_1000_175_p": [
      80,
      80
    ]
  }
}
```

### AF027: dup-6c6658c259bac8deac03d276ca44b39df48512c36d80c849a512f2d8d0728eed

Status: APPROVED; survivor `azurefilm_pctg_grey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pctg_grey_1000_175_p`|`{color_name}`|`GREY`|{"source_file": "AzureFilm.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / True|
|`azurefilm_pctg_pctggrey_1000_175_p`|`PCTG {color_name}`|`Grey`|{"source_file": "AzureFilm.json", "definition_index": 21, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_pctg_grey_1000_175_p": 250,
    "azurefilm_pctg_pctggrey_1000_175_p": null
  },
  "extruder_temp_range": {
    "azurefilm_pctg_grey_1000_175_p": null,
    "azurefilm_pctg_pctggrey_1000_175_p": [
      250,
      250
    ]
  },
  "bed_temp": {
    "azurefilm_pctg_grey_1000_175_p": 80,
    "azurefilm_pctg_pctggrey_1000_175_p": null
  },
  "bed_temp_range": {
    "azurefilm_pctg_grey_1000_175_p": null,
    "azurefilm_pctg_pctggrey_1000_175_p": [
      80,
      80
    ]
  }
}
```

### AF028: dup-345305b520acb5f06c314e92ed556bd0201f02e34294ce0c098706ebc50a333b

Status: APPROVED; survivor `azurefilm_pctg_transparent_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pctg_pctgtransparent_1000_175_p`|`PCTG {color_name}`|`Transparent`|{"source_file": "AzureFilm.json", "definition_index": 21, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|
|`azurefilm_pctg_transparent_1000_175_p`|`{color_name}`|`TRANSPARENT`|{"source_file": "AzureFilm.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_pctg_pctgtransparent_1000_175_p": null,
    "azurefilm_pctg_transparent_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_pctg_pctgtransparent_1000_175_p": [
      250,
      250
    ],
    "azurefilm_pctg_transparent_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_pctg_pctgtransparent_1000_175_p": null,
    "azurefilm_pctg_transparent_1000_175_p": 80
  },
  "bed_temp_range": {
    "azurefilm_pctg_pctgtransparent_1000_175_p": [
      80,
      80
    ],
    "azurefilm_pctg_transparent_1000_175_p": null
  },
  "translucent": {
    "azurefilm_pctg_pctgtransparent_1000_175_p": false,
    "azurefilm_pctg_transparent_1000_175_p": true
  }
}
```

### AF029: dup-19895653db8a3207f46f94ab81307675d7b511b9265d924db6e359d9c5bb3c5b

Status: APPROVED; survivor `azurefilm_pctg_white_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pctg_pctgwhite_1000_175_p`|`PCTG {color_name}`|`White`|{"source_file": "AzureFilm.json", "definition_index": 21, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|
|`azurefilm_pctg_white_1000_175_p`|`{color_name}`|`WHITE`|{"source_file": "AzureFilm.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_pctg_pctgwhite_1000_175_p": null,
    "azurefilm_pctg_white_1000_175_p": 250
  },
  "extruder_temp_range": {
    "azurefilm_pctg_pctgwhite_1000_175_p": [
      250,
      250
    ],
    "azurefilm_pctg_white_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_pctg_pctgwhite_1000_175_p": null,
    "azurefilm_pctg_white_1000_175_p": 80
  },
  "bed_temp_range": {
    "azurefilm_pctg_pctgwhite_1000_175_p": [
      80,
      80
    ],
    "azurefilm_pctg_white_1000_175_p": null
  }
}
```

### AF030: dup-e02860946600983f47b9cecb7de1f7660e78c74f443e8f64e17cc2b019489684

Status: APPROVED; survivor `azurefilm_petg_transparent_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_petg_petgtransparent_1000_175_p`|`PETG {color_name}`|`Transparent`|{"source_file": "AzureFilm.json", "definition_index": 23, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|
|`azurefilm_petg_transparent_1000_175_p`|`{color_name}`|`Transparent`|{"source_file": "AzureFilm.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "azurefilm_petg_petgtransparent_1000_175_p": 1.27,
    "azurefilm_petg_transparent_1000_175_p": 1.29
  },
  "color_hex": {
    "azurefilm_petg_petgtransparent_1000_175_p": "EDEDED",
    "azurefilm_petg_transparent_1000_175_p": "D5D4D9"
  },
  "extruder_temp": {
    "azurefilm_petg_petgtransparent_1000_175_p": 240,
    "azurefilm_petg_transparent_1000_175_p": 230
  },
  "bed_temp": {
    "azurefilm_petg_petgtransparent_1000_175_p": 75,
    "azurefilm_petg_transparent_1000_175_p": 80
  },
  "translucent": {
    "azurefilm_petg_petgtransparent_1000_175_p": false,
    "azurefilm_petg_transparent_1000_175_p": true
  }
}
```

### AF031: dup-aa69430d4fd0118a788abc3cc0e0a8b20d88f646bea28feb5d7b5506c4a70d76

Status: APPROVED; survivor `azurefilm_pla_anthracite_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_anthracite_1000_175_p`|`{color_name}`|`ANTHRACITE`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|
|`azurefilm_pla_plaanthracite_1000_175_p`|`PLA {color_name}`|`Anthracite`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_anthracite_1000_175_p": "666465",
    "azurefilm_pla_plaanthracite_1000_175_p": "50514C"
  },
  "extruder_temp": {
    "azurefilm_pla_anthracite_1000_175_p": 220,
    "azurefilm_pla_plaanthracite_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_anthracite_1000_175_p": 55,
    "azurefilm_pla_plaanthracite_1000_175_p": 60
  }
}
```

### AF032: dup-5ffdfa5798c9410983369b20ecbc09ffef531432121a94f8be6b5e4c3c21310e

Status: APPROVED; survivor `azurefilm_pla_black_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_black_1000_175_p`|`{color_name}`|`BLACK`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|
|`azurefilm_pla_plablack_1000_175_p`|`PLA {color_name}`|`Black`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_black_1000_175_p": "414141",
    "azurefilm_pla_plablack_1000_175_p": "000000"
  },
  "extruder_temp": {
    "azurefilm_pla_black_1000_175_p": 220,
    "azurefilm_pla_plablack_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_black_1000_175_p": 55,
    "azurefilm_pla_plablack_1000_175_p": 60
  }
}
```

### AF033: dup-8e5f273793be083492e4ec24afc9ccc857fdc516b914f49daa7fbb75bbcf8c50

Status: APPROVED; survivor `azurefilm_pla_blue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_blue_1000_175_p`|`{color_name}`|`BLUE`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|
|`azurefilm_pla_plablue_1000_175_p`|`PLA {color_name}`|`Blue`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_blue_1000_175_p": "3971A8",
    "azurefilm_pla_plablue_1000_175_p": "3C7ECE"
  },
  "extruder_temp": {
    "azurefilm_pla_blue_1000_175_p": 220,
    "azurefilm_pla_plablue_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_blue_1000_175_p": 55,
    "azurefilm_pla_plablue_1000_175_p": 60
  }
}
```

### AF034: dup-fcaf245584acec1db8141fac2cde69cd0b22d28ebff721b798a0972dbd2c3ec4

Status: APPROVED; survivor `azurefilm_pla_champagne_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_champagne_1000_175_p`|`{color_name}`|`CHAMPAGNE`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|
|`azurefilm_pla_plachampagne_1000_175_p`|`PLA {color_name}`|`Champagne`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_champagne_1000_175_p": "E5DAC3",
    "azurefilm_pla_plachampagne_1000_175_p": "E3D4AA"
  },
  "extruder_temp": {
    "azurefilm_pla_champagne_1000_175_p": 220,
    "azurefilm_pla_plachampagne_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_champagne_1000_175_p": 55,
    "azurefilm_pla_plachampagne_1000_175_p": 60
  }
}
```

### AF035: dup-26d7cf88923767556f26d196572efd691b4604d0ea461a6e3b17e9e38d4f36fe

Status: APPROVED; survivor `azurefilm_pla_champagnegold_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_champagnegold_1000_175_p`|`{color_name}`|`CHAMPAGNE GOLD`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|
|`azurefilm_pla_plachampagnegold_1000_175_p`|`PLA {color_name}`|`Champagne Gold`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_champagnegold_1000_175_p": "9D7A3F",
    "azurefilm_pla_plachampagnegold_1000_175_p": "DDB05C"
  },
  "extruder_temp": {
    "azurefilm_pla_champagnegold_1000_175_p": 220,
    "azurefilm_pla_plachampagnegold_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_champagnegold_1000_175_p": 55,
    "azurefilm_pla_plachampagnegold_1000_175_p": 60
  }
}
```

### AF036: dup-1a2bbcda7c1d9390cf01886042a4aedf30465d154111836f4c6044c9863082ff

Status: APPROVED; survivor `azurefilm_pla_coralred_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_coralred_1000_175_p`|`{color_name}`|`CORAL RED`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|
|`azurefilm_pla_placoralred_1000_175_p`|`PLA {color_name}`|`Coral Red`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_coralred_1000_175_p": "B44954",
    "azurefilm_pla_placoralred_1000_175_p": "E63049"
  },
  "extruder_temp": {
    "azurefilm_pla_coralred_1000_175_p": 220,
    "azurefilm_pla_placoralred_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_coralred_1000_175_p": 55,
    "azurefilm_pla_placoralred_1000_175_p": 60
  }
}
```

### AF037: dup-ccd1797cfee0569da5769dd9b1e38ea03a81dfbafabe427fc81dda3059ec70a0

Status: APPROVED; survivor `azurefilm_pla_foggywhite_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_foggywhite_1000_175_p`|`{color_name}`|`FOGGY WHITE`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|
|`azurefilm_pla_plafoggywhite_1000_175_p`|`PLA {color_name}`|`Foggy White`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_foggywhite_1000_175_p": "E8E7E3",
    "azurefilm_pla_plafoggywhite_1000_175_p": "DFD9CC"
  },
  "extruder_temp": {
    "azurefilm_pla_foggywhite_1000_175_p": 220,
    "azurefilm_pla_plafoggywhite_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_foggywhite_1000_175_p": 55,
    "azurefilm_pla_plafoggywhite_1000_175_p": 60
  }
}
```

### AF038: dup-47250cca92679aaad98fa57825e28b18eecbe154f00a66df5dd85c43840b506e

Status: APPROVED; survivor `azurefilm_pla_fuchsiapink_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_fuchsiapink_1000_175_p`|`{color_name}`|`FUCHSIA PINK`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|
|`azurefilm_pla_plafuchsiapink_1000_175_p`|`PLA {color_name}`|`Fuchsia Pink`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_fuchsiapink_1000_175_p": "DD5F93",
    "azurefilm_pla_plafuchsiapink_1000_175_p": "F51E91"
  },
  "extruder_temp": {
    "azurefilm_pla_fuchsiapink_1000_175_p": 220,
    "azurefilm_pla_plafuchsiapink_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_fuchsiapink_1000_175_p": 55,
    "azurefilm_pla_plafuchsiapink_1000_175_p": 60
  }
}
```

### AF039: dup-7ec4d7d2ec5a6d56c26121d144ae982d24433db5178303045748d2e577ed4336

Status: APPROVED; survivor `azurefilm_pla_galaxyblack_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_galaxyblack_1000_175_p`|`{color_name}`|`GALAXY BLACK`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|
|`azurefilm_pla_plagalaxyblack_1000_175_p`|`PLA {color_name}`|`Galaxy Black`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_galaxyblack_1000_175_p": "3F3F3F",
    "azurefilm_pla_plagalaxyblack_1000_175_p": "000000"
  },
  "extruder_temp": {
    "azurefilm_pla_galaxyblack_1000_175_p": 220,
    "azurefilm_pla_plagalaxyblack_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_galaxyblack_1000_175_p": 55,
    "azurefilm_pla_plagalaxyblack_1000_175_p": 60
  }
}
```

### AF040: dup-db974e875c04f6f924d085720b2dd5e82b79b92556648fc689b72a1be9c65805

Status: APPROVED; survivor `azurefilm_pla_glitterblack_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_glitterblack_1000_175_p`|`Glitter {color_name}`|`BLACK`|{"source_file": "AzureFilm.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / True|
|`azurefilm_pla_glitterplablack_1000_175_p`|`Glitter PLA {color_name}`|`Black`|{"source_file": "AzureFilm.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_pla_glitterblack_1000_175_p": 225,
    "azurefilm_pla_glitterplablack_1000_175_p": null
  },
  "extruder_temp_range": {
    "azurefilm_pla_glitterblack_1000_175_p": null,
    "azurefilm_pla_glitterplablack_1000_175_p": [
      225,
      225
    ]
  },
  "bed_temp": {
    "azurefilm_pla_glitterblack_1000_175_p": 55,
    "azurefilm_pla_glitterplablack_1000_175_p": null
  },
  "bed_temp_range": {
    "azurefilm_pla_glitterblack_1000_175_p": null,
    "azurefilm_pla_glitterplablack_1000_175_p": [
      55,
      55
    ]
  }
}
```

### AF041: dup-7cd3e4d9847ad189161ccfa102606715f7a3dd6525e9c44abb2e87d0e72f5750

Status: APPROVED; survivor `azurefilm_pla_glitterblue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_glitterblue_1000_175_p`|`Glitter {color_name}`|`BLUE`|{"source_file": "AzureFilm.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / True|
|`azurefilm_pla_glitterplablue_1000_175_p`|`Glitter PLA {color_name}`|`Blue`|{"source_file": "AzureFilm.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_pla_glitterblue_1000_175_p": 225,
    "azurefilm_pla_glitterplablue_1000_175_p": null
  },
  "extruder_temp_range": {
    "azurefilm_pla_glitterblue_1000_175_p": null,
    "azurefilm_pla_glitterplablue_1000_175_p": [
      225,
      225
    ]
  },
  "bed_temp": {
    "azurefilm_pla_glitterblue_1000_175_p": 55,
    "azurefilm_pla_glitterplablue_1000_175_p": null
  },
  "bed_temp_range": {
    "azurefilm_pla_glitterblue_1000_175_p": null,
    "azurefilm_pla_glitterplablue_1000_175_p": [
      55,
      55
    ]
  }
}
```

### AF042: dup-6d513281897edc7ef19d8257956edfba83bb2c6b765472b0b3330cc4331fb730

Status: APPROVED; survivor `azurefilm_pla_glittergreen_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_glittergreen_1000_175_p`|`Glitter {color_name}`|`GREEN`|{"source_file": "AzureFilm.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / True|
|`azurefilm_pla_glitterplagreen_1000_175_p`|`Glitter PLA {color_name}`|`Green`|{"source_file": "AzureFilm.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_pla_glittergreen_1000_175_p": 225,
    "azurefilm_pla_glitterplagreen_1000_175_p": null
  },
  "extruder_temp_range": {
    "azurefilm_pla_glittergreen_1000_175_p": null,
    "azurefilm_pla_glitterplagreen_1000_175_p": [
      225,
      225
    ]
  },
  "bed_temp": {
    "azurefilm_pla_glittergreen_1000_175_p": 55,
    "azurefilm_pla_glitterplagreen_1000_175_p": null
  },
  "bed_temp_range": {
    "azurefilm_pla_glittergreen_1000_175_p": null,
    "azurefilm_pla_glitterplagreen_1000_175_p": [
      55,
      55
    ]
  }
}
```

### AF043: dup-d0896c649e0fcf7803386cc599b3bae97308bc03ef6f4fbf4cd7d02c84ec1925

Status: APPROVED; survivor `azurefilm_pla_glitternature_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_glitternature_1000_175_p`|`Glitter {color_name}`|`NATURE`|{"source_file": "AzureFilm.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / True|
|`azurefilm_pla_glitterplanature_1000_175_p`|`Glitter PLA {color_name}`|`Nature`|{"source_file": "AzureFilm.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_pla_glitternature_1000_175_p": 225,
    "azurefilm_pla_glitterplanature_1000_175_p": null
  },
  "extruder_temp_range": {
    "azurefilm_pla_glitternature_1000_175_p": null,
    "azurefilm_pla_glitterplanature_1000_175_p": [
      225,
      225
    ]
  },
  "bed_temp": {
    "azurefilm_pla_glitternature_1000_175_p": 55,
    "azurefilm_pla_glitterplanature_1000_175_p": null
  },
  "bed_temp_range": {
    "azurefilm_pla_glitternature_1000_175_p": null,
    "azurefilm_pla_glitterplanature_1000_175_p": [
      55,
      55
    ]
  }
}
```

### AF044: dup-2b149760aa32abc951a588365da793a78afb4ae1d256edcc5583b40c322beacf

Status: APPROVED; survivor `azurefilm_pla_glitterred_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_glitterplared_1000_175_p`|`Glitter PLA {color_name}`|`Red`|{"source_file": "AzureFilm.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|
|`azurefilm_pla_glitterred_1000_175_p`|`Glitter {color_name}`|`RED`|{"source_file": "AzureFilm.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_pla_glitterplared_1000_175_p": null,
    "azurefilm_pla_glitterred_1000_175_p": 225
  },
  "extruder_temp_range": {
    "azurefilm_pla_glitterplared_1000_175_p": [
      225,
      225
    ],
    "azurefilm_pla_glitterred_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_pla_glitterplared_1000_175_p": null,
    "azurefilm_pla_glitterred_1000_175_p": 55
  },
  "bed_temp_range": {
    "azurefilm_pla_glitterplared_1000_175_p": [
      55,
      55
    ],
    "azurefilm_pla_glitterred_1000_175_p": null
  }
}
```

### AF045: dup-faf47bb5337529be663b761bb93aa196c6093a215bb29821445390f42c6306ed

Status: APPROVED; survivor `azurefilm_pla_glitterwhite_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_glitterplawhite_1000_175_p`|`Glitter PLA {color_name}`|`White`|{"source_file": "AzureFilm.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|
|`azurefilm_pla_glitterwhite_1000_175_p`|`Glitter {color_name}`|`WHITE`|{"source_file": "AzureFilm.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_pla_glitterplawhite_1000_175_p": null,
    "azurefilm_pla_glitterwhite_1000_175_p": 225
  },
  "extruder_temp_range": {
    "azurefilm_pla_glitterplawhite_1000_175_p": [
      225,
      225
    ],
    "azurefilm_pla_glitterwhite_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_pla_glitterplawhite_1000_175_p": null,
    "azurefilm_pla_glitterwhite_1000_175_p": 55
  },
  "bed_temp_range": {
    "azurefilm_pla_glitterplawhite_1000_175_p": [
      55,
      55
    ],
    "azurefilm_pla_glitterwhite_1000_175_p": null
  }
}
```

### AF046: dup-c639195d266131c34c3286d011bd3651512293452b71d84e5571bf125c4380e7

Status: APPROVED; survivor `azurefilm_pla_gold_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_gold_1000_175_p`|`{color_name}`|`GOLD`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|
|`azurefilm_pla_plagold_1000_175_p`|`PLA {color_name}`|`Gold`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_gold_1000_175_p": "67553F",
    "azurefilm_pla_plagold_1000_175_p": "DFB960"
  },
  "extruder_temp": {
    "azurefilm_pla_gold_1000_175_p": 220,
    "azurefilm_pla_plagold_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_gold_1000_175_p": 55,
    "azurefilm_pla_plagold_1000_175_p": 60
  }
}
```

### AF047: dup-8987b6918b59faa6135c1c12c5638dde14a32b36718b0672dfac8e9816f953fb

Status: APPROVED; survivor `azurefilm_pla_green_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_green_1000_175_p`|`{color_name}`|`GREEN`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|
|`azurefilm_pla_plagreen_1000_175_p`|`PLA {color_name}`|`Green`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_green_1000_175_p": "4EAC57",
    "azurefilm_pla_plagreen_1000_175_p": "7CE326"
  },
  "extruder_temp": {
    "azurefilm_pla_green_1000_175_p": 220,
    "azurefilm_pla_plagreen_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_green_1000_175_p": 55,
    "azurefilm_pla_plagreen_1000_175_p": 60
  }
}
```

### AF048: dup-6ff1ee6730004c2eeeed2d3d1a86944212e4a494416e6def63da1c0ffe2db7e1

Status: APPROVED; survivor `azurefilm_pla_lightgreen_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_lightgreen_1000_175_p`|`{color_name}`|`LIGHT GREEN`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|
|`azurefilm_pla_plalightgreen_1000_175_p`|`PLA {color_name}`|`Light Green`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_lightgreen_1000_175_p": "61B458",
    "azurefilm_pla_plalightgreen_1000_175_p": "29DA2D"
  },
  "extruder_temp": {
    "azurefilm_pla_lightgreen_1000_175_p": 220,
    "azurefilm_pla_plalightgreen_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_lightgreen_1000_175_p": 55,
    "azurefilm_pla_plalightgreen_1000_175_p": 60
  }
}
```

### AF049: dup-d427bdb23dadbd33e8ff4fdc68b892161dcf2cb022d862bd16e9a5ce645114a2

Status: APPROVED; survivor `azurefilm_pla_lightgrey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_lightgrey_1000_175_p`|`{color_name}`|`LIGHT GREY`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|
|`azurefilm_pla_plalightgrey_1000_175_p`|`PLA {color_name}`|`Light Grey`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_lightgrey_1000_175_p": "959CA2",
    "azurefilm_pla_plalightgrey_1000_175_p": "C1C3C2"
  },
  "extruder_temp": {
    "azurefilm_pla_lightgrey_1000_175_p": 220,
    "azurefilm_pla_plalightgrey_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_lightgrey_1000_175_p": 55,
    "azurefilm_pla_plalightgrey_1000_175_p": 60
  }
}
```

### AF050: dup-903fc265f3a43eec2783dba56661042b452dbbb91affe6b99a78700842b45884

Status: APPROVED; survivor `azurefilm_pla_marble_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_marble_1000_175_p`|`{color_name}`|`MARBLE`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|
|`azurefilm_pla_plamarble_1000_175_p`|`PLA {color_name}`|`Marble`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_marble_1000_175_p": "DADADA",
    "azurefilm_pla_plamarble_1000_175_p": "D0D0D0"
  },
  "extruder_temp": {
    "azurefilm_pla_marble_1000_175_p": 220,
    "azurefilm_pla_plamarble_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_marble_1000_175_p": 55,
    "azurefilm_pla_plamarble_1000_175_p": 60
  }
}
```

### AF051: dup-7f44091bd2c2293070157b3efce55144258069316f8f5993b5aa3673efbe8ee6

Status: DEFERRED; survivor `azurefilm_pla_mattehsblack_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_mattehsblack_1000_175_p`|`Matte {color_name}`|`HS BLACK`|{"source_file": "AzureFilm.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`azurefilm_pla_mattehsplablack_1000_175_p`|`Matte HS PLA {color_name}`|`Black`|{"source_file": "AzureFilm.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_mattehsblack_1000_175_p": "292B2D",
    "azurefilm_pla_mattehsplablack_1000_175_p": "000000"
  },
  "extruder_temp": {
    "azurefilm_pla_mattehsblack_1000_175_p": 215,
    "azurefilm_pla_mattehsplablack_1000_175_p": 210
  }
}
```

### AF052: dup-285f0a6649135aaf28429108fc112860df53e0a5fffbffd90f56ba5b4ef07a3a

Status: DEFERRED; survivor `azurefilm_pla_mattehsblue_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_mattehsblue_1000_175_p`|`Matte {color_name}`|`HS BLUE`|{"source_file": "AzureFilm.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`azurefilm_pla_mattehsplablue_1000_175_p`|`Matte HS PLA {color_name}`|`Blue`|{"source_file": "AzureFilm.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_mattehsblue_1000_175_p": "5FB0C7",
    "azurefilm_pla_mattehsplablue_1000_175_p": "2B8DA7"
  },
  "extruder_temp": {
    "azurefilm_pla_mattehsblue_1000_175_p": 215,
    "azurefilm_pla_mattehsplablue_1000_175_p": 210
  }
}
```

### AF053: dup-b3dc1bac9b53cc26222d57c64fc036e7c6b4a5ad8d87e79e0d4c641b0121cd04

Status: DEFERRED; survivor `azurefilm_pla_mattehsbordeaux_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_mattehsbordeaux_1000_175_p`|`Matte {color_name}`|`HS BORDEAUX`|{"source_file": "AzureFilm.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`azurefilm_pla_mattehsplabordeaux_1000_175_p`|`Matte HS PLA {color_name}`|`Bordeaux`|{"source_file": "AzureFilm.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_mattehsbordeaux_1000_175_p": "7F5053",
    "azurefilm_pla_mattehsplabordeaux_1000_175_p": "844C54"
  },
  "extruder_temp": {
    "azurefilm_pla_mattehsbordeaux_1000_175_p": 215,
    "azurefilm_pla_mattehsplabordeaux_1000_175_p": 210
  }
}
```

### AF054: dup-2af7be97eb338059760f3cde01f9c04ba8e59cd7f30127beac17f680f1383df6

Status: DEFERRED; survivor `azurefilm_pla_mattehslime_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_mattehslime_1000_175_p`|`Matte {color_name}`|`HS LIME`|{"source_file": "AzureFilm.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`azurefilm_pla_mattehsplalime_1000_175_p`|`Matte HS PLA {color_name}`|`Lime`|{"source_file": "AzureFilm.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_mattehslime_1000_175_p": "BFE368",
    "azurefilm_pla_mattehsplalime_1000_175_p": "8CB712"
  },
  "extruder_temp": {
    "azurefilm_pla_mattehslime_1000_175_p": 215,
    "azurefilm_pla_mattehsplalime_1000_175_p": 210
  }
}
```

### AF055: dup-704595e937257a1223e60a78e5bec31a7287db49a8902f5ff6258e1256820f02

Status: DEFERRED; survivor `azurefilm_pla_mattehsmint_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_mattehsmint_1000_175_p`|`Matte {color_name}`|`HS MINT`|{"source_file": "AzureFilm.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`azurefilm_pla_mattehsplamint_1000_175_p`|`Matte HS PLA {color_name}`|`Mint`|{"source_file": "AzureFilm.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_mattehsmint_1000_175_p": "BAC4C7",
    "azurefilm_pla_mattehsplamint_1000_175_p": "B0C0C4"
  },
  "extruder_temp": {
    "azurefilm_pla_mattehsmint_1000_175_p": 215,
    "azurefilm_pla_mattehsplamint_1000_175_p": 210
  }
}
```

### AF056: dup-d60901d911794e51fb95373a84491743c024db3fb24f1b2d964f33ef9e959927

Status: DEFERRED; survivor `azurefilm_pla_mattehsoff-white_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_mattehsoff-white_1000_175_p`|`Matte {color_name}`|`HS OFF-WHITE`|{"source_file": "AzureFilm.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`azurefilm_pla_mattehsplaoff-white_1000_175_p`|`Matte HS PLA {color_name}`|`Off-White`|{"source_file": "AzureFilm.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_mattehsoff-white_1000_175_p": "C9C2BC",
    "azurefilm_pla_mattehsplaoff-white_1000_175_p": "CFC6BB"
  },
  "extruder_temp": {
    "azurefilm_pla_mattehsoff-white_1000_175_p": 215,
    "azurefilm_pla_mattehsplaoff-white_1000_175_p": 210
  }
}
```

### AF057: dup-56b44cdab4af07af4bcbd0113d6cb71da7137d26b0ba57f9f8ebffb1d924d4b9

Status: DEFERRED; survivor `azurefilm_pla_mattehsrosy_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_mattehsplarosy_1000_175_p`|`Matte HS PLA {color_name}`|`Rosy`|{"source_file": "AzureFilm.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`azurefilm_pla_mattehsrosy_1000_175_p`|`Matte {color_name}`|`HS ROSY`|{"source_file": "AzureFilm.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_mattehsplarosy_1000_175_p": "D9BEC0",
    "azurefilm_pla_mattehsrosy_1000_175_p": "D3C1C0"
  },
  "extruder_temp": {
    "azurefilm_pla_mattehsplarosy_1000_175_p": 210,
    "azurefilm_pla_mattehsrosy_1000_175_p": 215
  }
}
```

### AF058: dup-5d3f76d17092e0376d881a93c47a3a4218eff9ea954967a0cd079b46fac1ffb7

Status: DEFERRED; survivor `azurefilm_pla_mattehssage_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_mattehsplasage_1000_175_p`|`Matte HS PLA {color_name}`|`Sage`|{"source_file": "AzureFilm.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`azurefilm_pla_mattehssage_1000_175_p`|`Matte {color_name}`|`HS SAGE`|{"source_file": "AzureFilm.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_mattehsplasage_1000_175_p": "A1A397",
    "azurefilm_pla_mattehssage_1000_175_p": "ADAFA4"
  },
  "extruder_temp": {
    "azurefilm_pla_mattehsplasage_1000_175_p": 210,
    "azurefilm_pla_mattehssage_1000_175_p": 215
  }
}
```

### AF059: dup-037d58f2258e645378e82715b1f5212e5b4fd665be2fbd0f8be977924f8e4498

Status: DEFERRED; survivor `azurefilm_pla_mattehswhite_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_mattehsplawhite_1000_175_p`|`Matte HS PLA {color_name}`|`White`|{"source_file": "AzureFilm.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`azurefilm_pla_mattehswhite_1000_175_p`|`Matte {color_name}`|`HS WHITE`|{"source_file": "AzureFilm.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_mattehsplawhite_1000_175_p": "FFFFFF",
    "azurefilm_pla_mattehswhite_1000_175_p": "E7E7E7"
  },
  "extruder_temp": {
    "azurefilm_pla_mattehsplawhite_1000_175_p": 210,
    "azurefilm_pla_mattehswhite_1000_175_p": 215
  }
}
```

### AF060: dup-bf69c3829787afe0c6686554d4f26953e25286745567ad96adadb272055a788d

Status: APPROVED; survivor `azurefilm_pla_navyblue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_navyblue_1000_175_p`|`{color_name}`|`NAVY BLUE`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|
|`azurefilm_pla_planavyblue_1000_175_p`|`PLA {color_name}`|`Navy Blue`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_navyblue_1000_175_p": "151B30",
    "azurefilm_pla_planavyblue_1000_175_p": "28314F"
  },
  "extruder_temp": {
    "azurefilm_pla_navyblue_1000_175_p": 220,
    "azurefilm_pla_planavyblue_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_navyblue_1000_175_p": 55,
    "azurefilm_pla_planavyblue_1000_175_p": 60
  }
}
```

### AF061: dup-b29b55f565e756b16c728ff228761c9f50ae7f3c3e25de751348c7886648c487

Status: APPROVED; survivor `azurefilm_pla_orange_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_orange_1000_175_p`|`{color_name}`|`ORANGE`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|
|`azurefilm_pla_plaorange_1000_175_p`|`PLA {color_name}`|`Orange`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_orange_1000_175_p": "E06640",
    "azurefilm_pla_plaorange_1000_175_p": "E2650B"
  },
  "extruder_temp": {
    "azurefilm_pla_orange_1000_175_p": 220,
    "azurefilm_pla_plaorange_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_orange_1000_175_p": 55,
    "azurefilm_pla_plaorange_1000_175_p": 60
  }
}
```

### AF062: dup-deafa7b93342bb579f7d5164481adc22662a64df4eb5ce5675c395f215189562

Status: APPROVED; survivor `azurefilm_pla_pink_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_pink_1000_175_p`|`{color_name}`|`PINK`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|
|`azurefilm_pla_plapink_1000_175_p`|`PLA {color_name}`|`Pink`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_pink_1000_175_p": "CB5086",
    "azurefilm_pla_plapink_1000_175_p": "E65CAE"
  },
  "extruder_temp": {
    "azurefilm_pla_pink_1000_175_p": 220,
    "azurefilm_pla_plapink_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_pink_1000_175_p": 55,
    "azurefilm_pla_plapink_1000_175_p": 60
  }
}
```

### AF063: dup-c3226174fe8cec49f32b01f3c597aba790024b3bf84a10bd919ffe2b8066094a

Status: APPROVED; survivor `azurefilm_pla_primeblack_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_plaprimeblack_1000_175_p`|`PLA Prime {color_name}`|`Black`|{"source_file": "AzureFilm.json", "definition_index": 27, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`azurefilm_pla_primeblack_1000_175_p`|`Prime {color_name}`|`BLACK`|{"source_file": "AzureFilm.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_pla_plaprimeblack_1000_175_p": null,
    "azurefilm_pla_primeblack_1000_175_p": 230
  },
  "extruder_temp_range": {
    "azurefilm_pla_plaprimeblack_1000_175_p": [
      230,
      230
    ],
    "azurefilm_pla_primeblack_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_pla_plaprimeblack_1000_175_p": null,
    "azurefilm_pla_primeblack_1000_175_p": 60
  },
  "bed_temp_range": {
    "azurefilm_pla_plaprimeblack_1000_175_p": [
      60,
      60
    ],
    "azurefilm_pla_primeblack_1000_175_p": null
  }
}
```

### AF064: dup-6ef658c8d1978d43c47985d3975a7558a2bcf0c46b35805840d334790e809a79

Status: APPROVED; survivor `azurefilm_pla_primedarkblue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_plaprimedarkblue_1000_175_p`|`PLA Prime {color_name}`|`Dark Blue`|{"source_file": "AzureFilm.json", "definition_index": 27, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`azurefilm_pla_primedarkblue_1000_175_p`|`Prime {color_name}`|`DARK BLUE`|{"source_file": "AzureFilm.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_pla_plaprimedarkblue_1000_175_p": null,
    "azurefilm_pla_primedarkblue_1000_175_p": 230
  },
  "extruder_temp_range": {
    "azurefilm_pla_plaprimedarkblue_1000_175_p": [
      230,
      230
    ],
    "azurefilm_pla_primedarkblue_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_pla_plaprimedarkblue_1000_175_p": null,
    "azurefilm_pla_primedarkblue_1000_175_p": 60
  },
  "bed_temp_range": {
    "azurefilm_pla_plaprimedarkblue_1000_175_p": [
      60,
      60
    ],
    "azurefilm_pla_primedarkblue_1000_175_p": null
  }
}
```

### AF065: dup-24aa1c66707a3b9a24fb7a282b566fd56c7a6089e595a0e0f9c80016ba466fc6

Status: APPROVED; survivor `azurefilm_pla_primedarkgrey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_plaprimedarkgrey_1000_175_p`|`PLA Prime {color_name}`|`Dark Grey`|{"source_file": "AzureFilm.json", "definition_index": 27, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`azurefilm_pla_primedarkgrey_1000_175_p`|`Prime {color_name}`|`DARK GREY`|{"source_file": "AzureFilm.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_pla_plaprimedarkgrey_1000_175_p": null,
    "azurefilm_pla_primedarkgrey_1000_175_p": 230
  },
  "extruder_temp_range": {
    "azurefilm_pla_plaprimedarkgrey_1000_175_p": [
      230,
      230
    ],
    "azurefilm_pla_primedarkgrey_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_pla_plaprimedarkgrey_1000_175_p": null,
    "azurefilm_pla_primedarkgrey_1000_175_p": 60
  },
  "bed_temp_range": {
    "azurefilm_pla_plaprimedarkgrey_1000_175_p": [
      60,
      60
    ],
    "azurefilm_pla_primedarkgrey_1000_175_p": null
  }
}
```

### AF066: dup-bbf3bbcea7c6df6450c8ac3fe2c18b2dc276c4d9610e73d6ab5f7ec282e47d1d

Status: APPROVED; survivor `azurefilm_pla_primelightgrey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_plaprimelightgrey_1000_175_p`|`PLA Prime {color_name}`|`Light Grey`|{"source_file": "AzureFilm.json", "definition_index": 27, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`azurefilm_pla_primelightgrey_1000_175_p`|`Prime {color_name}`|`LIGHT GREY`|{"source_file": "AzureFilm.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_pla_plaprimelightgrey_1000_175_p": null,
    "azurefilm_pla_primelightgrey_1000_175_p": 230
  },
  "extruder_temp_range": {
    "azurefilm_pla_plaprimelightgrey_1000_175_p": [
      230,
      230
    ],
    "azurefilm_pla_primelightgrey_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_pla_plaprimelightgrey_1000_175_p": null,
    "azurefilm_pla_primelightgrey_1000_175_p": 60
  },
  "bed_temp_range": {
    "azurefilm_pla_plaprimelightgrey_1000_175_p": [
      60,
      60
    ],
    "azurefilm_pla_primelightgrey_1000_175_p": null
  }
}
```

### AF067: dup-1bc2623b477a8b83a4afd1c2f568a6cce33b86da30ab10494edc84914591d3b7

Status: APPROVED; survivor `azurefilm_pla_primenature_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_plaprimenature_1000_175_p`|`PLA Prime {color_name}`|`Nature`|{"source_file": "AzureFilm.json", "definition_index": 27, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`azurefilm_pla_primenature_1000_175_p`|`Prime {color_name}`|`NATURE`|{"source_file": "AzureFilm.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_pla_plaprimenature_1000_175_p": null,
    "azurefilm_pla_primenature_1000_175_p": 230
  },
  "extruder_temp_range": {
    "azurefilm_pla_plaprimenature_1000_175_p": [
      230,
      230
    ],
    "azurefilm_pla_primenature_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_pla_plaprimenature_1000_175_p": null,
    "azurefilm_pla_primenature_1000_175_p": 60
  },
  "bed_temp_range": {
    "azurefilm_pla_plaprimenature_1000_175_p": [
      60,
      60
    ],
    "azurefilm_pla_primenature_1000_175_p": null
  }
}
```

### AF068: dup-75869edce09c0f178911e651fe137f9c7ebec369412a8b28907472fe03a29741

Status: APPROVED; survivor `azurefilm_pla_primered_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_plaprimered_1000_175_p`|`PLA Prime {color_name}`|`Red`|{"source_file": "AzureFilm.json", "definition_index": 27, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`azurefilm_pla_primered_1000_175_p`|`Prime {color_name}`|`RED`|{"source_file": "AzureFilm.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_pla_plaprimered_1000_175_p": null,
    "azurefilm_pla_primered_1000_175_p": 230
  },
  "extruder_temp_range": {
    "azurefilm_pla_plaprimered_1000_175_p": [
      230,
      230
    ],
    "azurefilm_pla_primered_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_pla_plaprimered_1000_175_p": null,
    "azurefilm_pla_primered_1000_175_p": 60
  },
  "bed_temp_range": {
    "azurefilm_pla_plaprimered_1000_175_p": [
      60,
      60
    ],
    "azurefilm_pla_primered_1000_175_p": null
  }
}
```

### AF069: dup-f54455ba18d2cf97fddd02fc55616c5fa1ab28afa39072053cae628f1a83e0bf

Status: APPROVED; survivor `azurefilm_pla_primewhite_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_plaprimewhite_1000_175_p`|`PLA Prime {color_name}`|`White`|{"source_file": "AzureFilm.json", "definition_index": 27, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`azurefilm_pla_primewhite_1000_175_p`|`Prime {color_name}`|`WHITE`|{"source_file": "AzureFilm.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "azurefilm_pla_plaprimewhite_1000_175_p": null,
    "azurefilm_pla_primewhite_1000_175_p": 230
  },
  "extruder_temp_range": {
    "azurefilm_pla_plaprimewhite_1000_175_p": [
      230,
      230
    ],
    "azurefilm_pla_primewhite_1000_175_p": null
  },
  "bed_temp": {
    "azurefilm_pla_plaprimewhite_1000_175_p": null,
    "azurefilm_pla_primewhite_1000_175_p": 60
  },
  "bed_temp_range": {
    "azurefilm_pla_plaprimewhite_1000_175_p": [
      60,
      60
    ],
    "azurefilm_pla_primewhite_1000_175_p": null
  }
}
```

### AF070: dup-f28e4ae3c486802de3ef71c070b236ce991a416cc816eee1d54c542722fd6b47

Status: APPROVED; survivor `azurefilm_pla_redwine_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_plaredwine_1000_175_p`|`PLA {color_name}`|`Red Wine`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|
|`azurefilm_pla_redwine_1000_175_p`|`{color_name}`|`RED WINE`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_plaredwine_1000_175_p": "A83D43",
    "azurefilm_pla_redwine_1000_175_p": "AD5051"
  },
  "extruder_temp": {
    "azurefilm_pla_plaredwine_1000_175_p": 210,
    "azurefilm_pla_redwine_1000_175_p": 220
  },
  "bed_temp": {
    "azurefilm_pla_plaredwine_1000_175_p": 60,
    "azurefilm_pla_redwine_1000_175_p": 55
  }
}
```

### AF071: dup-566a7a61a41af40bd2875fb0daed4ae4b76c85bf8f2ac3d0b2875bc991a73622

Status: APPROVED; survivor `azurefilm_pla_sharkgrey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_plasharkgrey_1000_175_p`|`PLA {color_name}`|`Shark Grey`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|
|`azurefilm_pla_sharkgrey_1000_175_p`|`{color_name}`|`SHARK GREY`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_plasharkgrey_1000_175_p": "5E6D78",
    "azurefilm_pla_sharkgrey_1000_175_p": "7A8690"
  },
  "extruder_temp": {
    "azurefilm_pla_plasharkgrey_1000_175_p": 210,
    "azurefilm_pla_sharkgrey_1000_175_p": 220
  },
  "bed_temp": {
    "azurefilm_pla_plasharkgrey_1000_175_p": 60,
    "azurefilm_pla_sharkgrey_1000_175_p": 55
  }
}
```

### AF072: dup-8979d34c72f1735a323f1935b22714d6d7ce62189f6253b4c65cacbc7627b2fa

Status: APPROVED; survivor `azurefilm_pla_sunsetorange_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_plasunsetorange_1000_175_p`|`PLA {color_name}`|`Sunset Orange`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|
|`azurefilm_pla_sunsetorange_1000_175_p`|`{color_name}`|`SUNSET ORANGE`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_plasunsetorange_1000_175_p": "B24D2F",
    "azurefilm_pla_sunsetorange_1000_175_p": "B25D37"
  },
  "extruder_temp": {
    "azurefilm_pla_plasunsetorange_1000_175_p": 210,
    "azurefilm_pla_sunsetorange_1000_175_p": 220
  },
  "bed_temp": {
    "azurefilm_pla_plasunsetorange_1000_175_p": 60,
    "azurefilm_pla_sunsetorange_1000_175_p": 55
  }
}
```

### AF073: dup-189a88ab32d16f2ad1b9cd819e04a2a6a4ff9c3946fc29c8f6c12fcbb7b98654

Status: APPROVED; survivor `azurefilm_pla_white_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_plawhite_1000_175_p`|`PLA {color_name}`|`White`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|
|`azurefilm_pla_white_1000_175_p`|`{color_name}`|`WHITE`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_plawhite_1000_175_p": "FFFFFF",
    "azurefilm_pla_white_1000_175_p": "E5E5E5"
  },
  "extruder_temp": {
    "azurefilm_pla_plawhite_1000_175_p": 210,
    "azurefilm_pla_white_1000_175_p": 220
  },
  "bed_temp": {
    "azurefilm_pla_plawhite_1000_175_p": 60,
    "azurefilm_pla_white_1000_175_p": 55
  }
}
```

### AF074: dup-2cb10da22dd329eabb5e17bc9edd6af27770825a7d4558a9489be01edb9dc718

Status: APPROVED; survivor `azurefilm_pla_yellow_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_playellow_1000_175_p`|`PLA {color_name}`|`Yellow`|{"source_file": "AzureFilm.json", "definition_index": 25, "weights": 4, "diameters": 1, "colors": 37, "compiled_records": 148} / False|
|`azurefilm_pla_yellow_1000_175_p`|`{color_name}`|`YELLOW`|{"source_file": "AzureFilm.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 67, "compiled_records": 67} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_playellow_1000_175_p": "F0D100",
    "azurefilm_pla_yellow_1000_175_p": "EFD65B"
  },
  "extruder_temp": {
    "azurefilm_pla_playellow_1000_175_p": 210,
    "azurefilm_pla_yellow_1000_175_p": 220
  },
  "bed_temp": {
    "azurefilm_pla_playellow_1000_175_p": 60,
    "azurefilm_pla_yellow_1000_175_p": 55
  }
}
```

### AF075: dup-916325aeaaf8673ad6e7ab730b0e4fee7f1422442bcb8fcdc44bbc68c9588227

Status: APPROVED; survivor `azurefilm_pla_silkdarkcopper_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_silkdarkcopper_1000_175_p`|`Silk {color_name}`|`DARK COPPER`|{"source_file": "AzureFilm.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 39, "compiled_records": 39} / True|
|`azurefilm_pla_silkpladarkcopper_1000_175_p`|`Silk PLA {color_name}`|`Dark copper`|{"source_file": "AzureFilm.json", "definition_index": 28, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_silkdarkcopper_1000_175_p": "956161",
    "azurefilm_pla_silkpladarkcopper_1000_175_p": "90535A"
  },
  "extruder_temp": {
    "azurefilm_pla_silkdarkcopper_1000_175_p": 230,
    "azurefilm_pla_silkpladarkcopper_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_silkdarkcopper_1000_175_p": 80,
    "azurefilm_pla_silkpladarkcopper_1000_175_p": 60
  }
}
```

### AF076: dup-8bc5c2cbb475410a8b59471011dba1d1ead869998621d42dc0d1cf12300f8921

Status: APPROVED; survivor `azurefilm_pla_silkflameorange_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_silkflameorange_1000_175_p`|`Silk {color_name}`|`FLAME ORANGE`|{"source_file": "AzureFilm.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 39, "compiled_records": 39} / True|
|`azurefilm_pla_silkplaflameorange_1000_175_p`|`Silk PLA {color_name}`|`Flame orange`|{"source_file": "AzureFilm.json", "definition_index": 28, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_silkflameorange_1000_175_p": "D68534",
    "azurefilm_pla_silkplaflameorange_1000_175_p": "F3C053"
  },
  "extruder_temp": {
    "azurefilm_pla_silkflameorange_1000_175_p": 230,
    "azurefilm_pla_silkplaflameorange_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_silkflameorange_1000_175_p": 80,
    "azurefilm_pla_silkplaflameorange_1000_175_p": 60
  }
}
```

### AF077: dup-244d2812e8ae23a8753378d986c258ff7dee52b2a7289a3c820eace0f275516e

Status: APPROVED; survivor `azurefilm_pla_silkjunglegold_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_silkjunglegold_1000_175_p`|`Silk {color_name}`|`JUNGLE GOLD`|{"source_file": "AzureFilm.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 39, "compiled_records": 39} / True|
|`azurefilm_pla_silkplajunglegold_1000_175_p`|`Silk PLA {color_name}`|`Jungle gold`|{"source_file": "AzureFilm.json", "definition_index": 28, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_silkjunglegold_1000_175_p": "B1B43C",
    "azurefilm_pla_silkplajunglegold_1000_175_p": "B4C500"
  },
  "extruder_temp": {
    "azurefilm_pla_silkjunglegold_1000_175_p": 230,
    "azurefilm_pla_silkplajunglegold_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_silkjunglegold_1000_175_p": 80,
    "azurefilm_pla_silkplajunglegold_1000_175_p": 60
  }
}
```

### AF078: dup-2fa7f1aef041f74e98df631aac5068551e64b79dbd30a7d7b22a2aa041f7c596

Status: APPROVED; survivor `azurefilm_pla_silklime_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_silklime_1000_175_p`|`Silk {color_name}`|`LIME`|{"source_file": "AzureFilm.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 39, "compiled_records": 39} / True|
|`azurefilm_pla_silkplalime_1000_175_p`|`Silk PLA {color_name}`|`Lime`|{"source_file": "AzureFilm.json", "definition_index": 28, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_silklime_1000_175_p": "A6CC51",
    "azurefilm_pla_silkplalime_1000_175_p": "CEF157"
  },
  "extruder_temp": {
    "azurefilm_pla_silklime_1000_175_p": 230,
    "azurefilm_pla_silkplalime_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_silklime_1000_175_p": 80,
    "azurefilm_pla_silkplalime_1000_175_p": 60
  }
}
```

### AF079: dup-931b916b2517f1145271ddc6d6c04d2e93092d6a7a32e8542312644121b83fa2

Status: APPROVED; survivor `azurefilm_pla_silkolivegold_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_silkolivegold_1000_175_p`|`Silk {color_name}`|`OLIVE GOLD`|{"source_file": "AzureFilm.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 39, "compiled_records": 39} / True|
|`azurefilm_pla_silkplaolivegold_1000_175_p`|`Silk PLA {color_name}`|`Olive gold`|{"source_file": "AzureFilm.json", "definition_index": 28, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_silkolivegold_1000_175_p": "898463",
    "azurefilm_pla_silkplaolivegold_1000_175_p": "FFF480"
  },
  "extruder_temp": {
    "azurefilm_pla_silkolivegold_1000_175_p": 230,
    "azurefilm_pla_silkplaolivegold_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_silkolivegold_1000_175_p": 80,
    "azurefilm_pla_silkplaolivegold_1000_175_p": 60
  }
}
```

### AF080: dup-e5abad04ef5d37d2c9ad0525c224dad180eb86a99fbe743054713e87849d5ef1

Status: APPROVED; survivor `azurefilm_pla_silkpink_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_silkpink_1000_175_p`|`Silk {color_name}`|`PINK`|{"source_file": "AzureFilm.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 39, "compiled_records": 39} / True|
|`azurefilm_pla_silkplapink_1000_175_p`|`Silk PLA {color_name}`|`Pink`|{"source_file": "AzureFilm.json", "definition_index": 28, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_silkpink_1000_175_p": "BC71C4",
    "azurefilm_pla_silkplapink_1000_175_p": "F088E5"
  },
  "extruder_temp": {
    "azurefilm_pla_silkpink_1000_175_p": 230,
    "azurefilm_pla_silkplapink_1000_175_p": 210
  },
  "bed_temp": {
    "azurefilm_pla_silkpink_1000_175_p": 80,
    "azurefilm_pla_silkplapink_1000_175_p": 60
  }
}
```

### AF081: dup-937f6979f5c07237b57381f9d618f25ef2942803f3d98ab268f56e3811bc704d

Status: APPROVED; survivor `azurefilm_pla_silkrainbowtropicana_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_silkplarainbowtropicana_1000_175_p`|`Silk PLA {color_name}`|`Rainbow Tropicana`|{"source_file": "AzureFilm.json", "definition_index": 28, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|
|`azurefilm_pla_silkrainbowtropicana_1000_175_p`|`Silk {color_name}`|`Rainbow TROPICANA`|{"source_file": "AzureFilm.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 39, "compiled_records": 39} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_silkplarainbowtropicana_1000_175_p": "D0A6A9",
    "azurefilm_pla_silkrainbowtropicana_1000_175_p": "B8866F"
  },
  "extruder_temp": {
    "azurefilm_pla_silkplarainbowtropicana_1000_175_p": 210,
    "azurefilm_pla_silkrainbowtropicana_1000_175_p": 230
  },
  "bed_temp": {
    "azurefilm_pla_silkplarainbowtropicana_1000_175_p": 60,
    "azurefilm_pla_silkrainbowtropicana_1000_175_p": 80
  }
}
```

### AF082: dup-cee24546ceb7a75bea8f05a984b43d280d3c37aad3be07430945179d414309ae

Status: APPROVED; survivor `azurefilm_pla_silkrose_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_silkplarose_1000_175_p`|`Silk PLA {color_name}`|`Rose`|{"source_file": "AzureFilm.json", "definition_index": 28, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|
|`azurefilm_pla_silkrose_1000_175_p`|`Silk {color_name}`|`ROSE`|{"source_file": "AzureFilm.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 39, "compiled_records": 39} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_silkplarose_1000_175_p": "D72830",
    "azurefilm_pla_silkrose_1000_175_p": "CC6671"
  },
  "extruder_temp": {
    "azurefilm_pla_silkplarose_1000_175_p": 210,
    "azurefilm_pla_silkrose_1000_175_p": 230
  },
  "bed_temp": {
    "azurefilm_pla_silkplarose_1000_175_p": 60,
    "azurefilm_pla_silkrose_1000_175_p": 80
  }
}
```

### AF083: dup-70643d4f428642d4182dd554730d0ec9aa19239846efed683ab76f779af27f0d

Status: APPROVED; survivor `azurefilm_pla_silksand_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_silkplasand_1000_175_p`|`Silk PLA {color_name}`|`Sand`|{"source_file": "AzureFilm.json", "definition_index": 28, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|
|`azurefilm_pla_silksand_1000_175_p`|`Silk {color_name}`|`SAND`|{"source_file": "AzureFilm.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 39, "compiled_records": 39} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_silkplasand_1000_175_p": "D0A85E",
    "azurefilm_pla_silksand_1000_175_p": "D0BA97"
  },
  "extruder_temp": {
    "azurefilm_pla_silkplasand_1000_175_p": 210,
    "azurefilm_pla_silksand_1000_175_p": 230
  },
  "bed_temp": {
    "azurefilm_pla_silkplasand_1000_175_p": 60,
    "azurefilm_pla_silksand_1000_175_p": 80
  }
}
```

### AF084: dup-5ad957080191b3d38bf9fa5c4f15e290ae5b6ebb9211d567829a899ee4d90ca4

Status: APPROVED; survivor `azurefilm_pla_silksilver_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_silkplasilver_1000_175_p`|`Silk PLA {color_name}`|`Silver`|{"source_file": "AzureFilm.json", "definition_index": 28, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|
|`azurefilm_pla_silksilver_1000_175_p`|`Silk {color_name}`|`SILVER`|{"source_file": "AzureFilm.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 39, "compiled_records": 39} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_silkplasilver_1000_175_p": "D6D6D6",
    "azurefilm_pla_silksilver_1000_175_p": "969CA6"
  },
  "extruder_temp": {
    "azurefilm_pla_silkplasilver_1000_175_p": 210,
    "azurefilm_pla_silksilver_1000_175_p": 230
  },
  "bed_temp": {
    "azurefilm_pla_silkplasilver_1000_175_p": 60,
    "azurefilm_pla_silksilver_1000_175_p": 80
  }
}
```

### AF085: dup-e40a419a67ea78d366bb2eb85f6629342e1e3ed6251b333422a2641ca227c8af

Status: APPROVED; survivor `azurefilm_pla_silkskyblue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_silkplaskyblue_1000_175_p`|`Silk PLA {color_name}`|`Sky blue`|{"source_file": "AzureFilm.json", "definition_index": 28, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|
|`azurefilm_pla_silkskyblue_1000_175_p`|`Silk {color_name}`|`SKY BLUE`|{"source_file": "AzureFilm.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 39, "compiled_records": 39} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_silkplaskyblue_1000_175_p": "5ACDEC",
    "azurefilm_pla_silkskyblue_1000_175_p": "54ABEA"
  },
  "extruder_temp": {
    "azurefilm_pla_silkplaskyblue_1000_175_p": 210,
    "azurefilm_pla_silkskyblue_1000_175_p": 230
  },
  "bed_temp": {
    "azurefilm_pla_silkplaskyblue_1000_175_p": 60,
    "azurefilm_pla_silkskyblue_1000_175_p": 80
  }
}
```

### AF086: dup-f1c85d3937559cfb475bbb4bd2fc7589a2fde3cd360f69412418b569f6f38c66

Status: APPROVED; survivor `azurefilm_pla_silkwhite_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`azurefilm_pla_silkplawhite_1000_175_p`|`Silk PLA {color_name}`|`White`|{"source_file": "AzureFilm.json", "definition_index": 28, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|
|`azurefilm_pla_silkwhite_1000_175_p`|`Silk {color_name}`|`WHITE`|{"source_file": "AzureFilm.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 39, "compiled_records": 39} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "azurefilm_pla_silkplawhite_1000_175_p": "E4E8E7",
    "azurefilm_pla_silkwhite_1000_175_p": "C0C5C8"
  },
  "extruder_temp": {
    "azurefilm_pla_silkplawhite_1000_175_p": 210,
    "azurefilm_pla_silkwhite_1000_175_p": 230
  },
  "bed_temp": {
    "azurefilm_pla_silkplawhite_1000_175_p": 60,
    "azurefilm_pla_silkwhite_1000_175_p": 80
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "azurefilm_asa_originalsilver_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          240,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ASA.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 100,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_white_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pctg_white_1000_175_p",
      "values": {
        "density": 1.26,
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": null,
        "bed_temp_range": [
          60,
          80
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2026/03/PCTG_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.29,
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 80,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_coralred_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_asa_originalblack_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          240,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ASA.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 100,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_asa_originalwhite_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          240,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ASA.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 100,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_silkjunglegold_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          210,
          240
        ],
        "bed_temp": null,
        "bed_temp_range": [
          70,
          80
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/SILK_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 230,
        "extruder_temp_range": null,
        "bed_temp": 80,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_champagnegold_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_yellow_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_asa_primewhite_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          250
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2024/04/TDS-ASA-Prime.pptx.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 245,
        "extruder_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_silklime_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          210,
          240
        ],
        "bed_temp": null,
        "bed_temp_range": [
          70,
          80
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/SILK_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 230,
        "extruder_temp_range": null,
        "bed_temp": 80,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pctg_transparent_1000_175_p",
      "values": {
        "density": 1.26,
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": null,
        "bed_temp_range": [
          60,
          80
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2026/03/PCTG_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.29,
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 80,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_asa_originalgrey_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          240,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ASA.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 100,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_abs_plusnature_1000_175_p",
      "values": {
        "density": 1.04,
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ABS-plus.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.13,
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 110,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_fuchsiapink_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_asa_originalgreen_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          240,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ASA.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 100,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_asa_primesilver_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          250
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2024/04/TDS-ASA-Prime.pptx.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 245,
        "extruder_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_sharkgrey_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_silksilver_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          210,
          240
        ],
        "bed_temp": null,
        "bed_temp_range": [
          70,
          80
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/SILK_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 230,
        "extruder_temp_range": null,
        "bed_temp": 80,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_abs_plusyellow_1000_175_p",
      "values": {
        "density": 1.04,
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ABS-plus.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.13,
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 110,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_black_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_asa_originalred_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          240,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ASA.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 100,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_abs_plusgreen_1000_175_p",
      "values": {
        "density": 1.04,
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ABS-plus.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.13,
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 110,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_asa_originalorange_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          240,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ASA.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 100,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pctg_grey_1000_175_p",
      "values": {
        "density": 1.26,
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": null,
        "bed_temp_range": [
          60,
          80
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2026/03/PCTG_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.29,
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 80,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_lightgreen_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_silksand_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          210,
          240
        ],
        "bed_temp": null,
        "bed_temp_range": [
          70,
          80
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/SILK_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 230,
        "extruder_temp_range": null,
        "bed_temp": 80,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_abs_plusglitterblack_1000_175_p",
      "values": {
        "density": 1.04,
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ABS-plus.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.13,
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 110,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_asa_primered_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          250
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2024/04/TDS-ASA-Prime.pptx.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 245,
        "extruder_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_galaxyblack_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_abs_pluswhite_1000_175_p",
      "values": {
        "density": 1.04,
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ABS-plus.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.13,
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 110,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_sunsetorange_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_green_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_silkflameorange_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          210,
          240
        ],
        "bed_temp": null,
        "bed_temp_range": [
          70,
          80
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/SILK_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 230,
        "extruder_temp_range": null,
        "bed_temp": 80,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_blue_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_marble_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_asa_originalyellow_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          240,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ASA.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 100,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_silkdarkcopper_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          210,
          240
        ],
        "bed_temp": null,
        "bed_temp_range": [
          70,
          80
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/SILK_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 230,
        "extruder_temp_range": null,
        "bed_temp": 80,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_asa_primedarkblue_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          250
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2024/04/TDS-ASA-Prime.pptx.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 245,
        "extruder_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_silkolivegold_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          210,
          240
        ],
        "bed_temp": null,
        "bed_temp_range": [
          70,
          80
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/SILK_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 230,
        "extruder_temp_range": null,
        "bed_temp": 80,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_silkrainbowtropicana_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          210,
          240
        ],
        "bed_temp": null,
        "bed_temp_range": [
          70,
          80
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/SILK_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 230,
        "extruder_temp_range": null,
        "bed_temp": 80,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pctg_black_1000_175_p",
      "values": {
        "density": 1.26,
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": null,
        "bed_temp_range": [
          60,
          80
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2026/03/PCTG_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.29,
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 80,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_abs_plusorange_1000_175_p",
      "values": {
        "density": 1.04,
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ABS-plus.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.13,
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 110,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_abs_plusred_1000_175_p",
      "values": {
        "density": 1.04,
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ABS-plus.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.13,
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 110,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_anthracite_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_abs_plusgrey_1000_175_p",
      "values": {
        "density": 1.04,
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ABS-plus.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.13,
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 110,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_orange_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_asa_primeblack_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          250
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2024/04/TDS-ASA-Prime.pptx.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 245,
        "extruder_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_navyblue_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_gold_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_abs_plusblack_1000_175_p",
      "values": {
        "density": 1.04,
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ABS-plus.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.13,
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 110,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_foggywhite_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_silkrose_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          210,
          240
        ],
        "bed_temp": null,
        "bed_temp_range": [
          70,
          80
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/SILK_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 230,
        "extruder_temp_range": null,
        "bed_temp": 80,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_lightgrey_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_abs_plusblue_1000_175_p",
      "values": {
        "density": 1.04,
        "extruder_temp": null,
        "extruder_temp_range": [
          230,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ABS-plus.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.13,
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 110,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_pink_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_petg_transparent_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          220,
          240
        ],
        "bed_temp": null,
        "bed_temp_range": [
          80,
          90
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-PETG.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 230,
        "extruder_temp_range": null,
        "bed_temp": 80,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_silkskyblue_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          210,
          240
        ],
        "bed_temp": null,
        "bed_temp_range": [
          70,
          80
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/SILK_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 230,
        "extruder_temp_range": null,
        "bed_temp": 80,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_silkpink_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          210,
          240
        ],
        "bed_temp": null,
        "bed_temp_range": [
          70,
          80
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/SILK_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 230,
        "extruder_temp_range": null,
        "bed_temp": 80,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_silkwhite_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          210,
          240
        ],
        "bed_temp": null,
        "bed_temp_range": [
          70,
          80
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/SILK_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 230,
        "extruder_temp_range": null,
        "bed_temp": 80,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_redwine_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_asa_originalblue_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          240,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ASA.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 100,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_asa_originalnatural_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          240,
          260
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          120
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/TDS-ASA.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 250,
        "extruder_temp_range": null,
        "bed_temp": 100,
        "bed_temp_range": null
      }
    },
    {
      "id": "azurefilm_pla_champagne_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          60
        ]
      },
      "source": "https://azurefilm.com/wp-content/uploads/2023/10/PLA_TDS.pdf",
      "lot": "Current official product-line TDS linked on manufacturer documents page, retrieved 2026-10-03; no packaging evidence asserted",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "extruder_temp": 220,
        "extruder_temp_range": null,
        "bed_temp": 55,
        "bed_temp_range": null
      }
    }
  ],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `azurefilm_pla_red_1000_175_p` — RED
- `azurefilm_pla_magenta_1000_175_p` — MAGENTA
- `azurefilm_pla_purple_1000_175_p` — PURPLE
- `azurefilm_pla_cyan_1000_175_p` — CYAN
- `azurefilm_pla_pistachio_1000_175_p` — PISTACHIO
- `azurefilm_pla_caribbean_1000_175_p` — CARIBBEAN
- `azurefilm_pla_lagoon_1000_175_p` — LAGOON
- `azurefilm_pla_silver_1000_175_p` — SILVER
- `azurefilm_pla_emerald_1000_175_p` — EMERALD
- `azurefilm_pla_brown_1000_175_p` — BROWN
- `azurefilm_pla_pearlred_1000_175_p` — Pearl RED
- `azurefilm_pla_pearlpurple_1000_175_p` — Pearl PURPLE
- `azurefilm_pla_pearlblue_1000_175_p` — Pearl BLUE
- `azurefilm_pla_pearlnightblue_1000_175_p` — Pearl NIGHT BLUE
- `azurefilm_pla_pearlgreen_1000_175_p` — Pearl GREEN
- `azurefilm_pla_lumoslithowhite_1000_175_p` — Lumos LITHO WHITE
- `azurefilm_pla_lumosglowinthedark_1000_175_p` — Lumos GLOW IN THE DARK
- `azurefilm_pla_lumosuvlight_1000_175_p` — Lumos UV LIGHT
- `azurefilm_pla_neonyellow_1000_175_p` — Neon YELLOW
- `azurefilm_pla_neonlime_1000_175_p` — Neon LIME
- `azurefilm_pla_neonorange_1000_175_p` — Neon ORANGE
- `azurefilm_pla_neonred_1000_175_p` — Neon RED
- `azurefilm_pla_neonpink_1000_175_p` — Neon PINK
- `azurefilm_pla_pastelbannayellow_1000_175_p` — Pastel BANNA YELLOW
- `azurefilm_pla_pastelicecreampink_1000_175_p` — Pastel ICE CREAM PINK
- `azurefilm_pla_pastelbabyblue_1000_175_p` — Pastel BABY BLUE
- `azurefilm_pla_pastelmintgreen_1000_175_p` — Pastel MINT GREEN
- `azurefilm_pla_skinlatte_1000_175_p` — Skin LATTE
- `azurefilm_pla_skincappuccino_1000_175_p` — Skin CAPPUCCINO
- `azurefilm_pla_transparenttransparent_1000_175_p` — Transparent TRANSPARENT
- `azurefilm_pla_transparentyellow_1000_175_p` — Transparent YELLOW
- `azurefilm_pla_transparentred_1000_175_p` — Transparent RED
- `azurefilm_pla_transparentblue_1000_175_p` — Transparent BLUE
- `azurefilm_pla_strongmannature_1000_175_p` — Strongman NATURE
- `azurefilm_pla_strongmanred_1000_175_p` — Strongman RED
- `azurefilm_pla_strongmanblue_1000_175_p` — Strongman BLUE
- `azurefilm_pla_strongmangrey_1000_175_p` — Strongman GREY
- `azurefilm_pla_strongmanblack_1000_175_p` — Strongman BLACK
- `azurefilm_pla_lumberlaywhitewood_1000_175_p` — Lumber Lay WHITE WOOD
- `azurefilm_pla_lumberlaypine_1000_175_p` — Lumber Lay PINE
- `azurefilm_pla_lumberlaybamboo_1000_175_p` — Lumber Lay BAMBOO
- `azurefilm_pla_lumberlaycork_1000_175_p` — Lumber Lay CORK
- `azurefilm_pla_lumberlaygreenpolar_1000_175_p` — Lumber Lay GREEN POLAR
- `azurefilm_pla_lumberlaygreyoak_1000_175_p` — Lumber Lay GREY OAK
- `azurefilm_pla_lumberlayblackebony_1000_175_p` — Lumber Lay BLACK EBONY
- `azurefilm_pla_silkgold18k_1000_175_p` — Silk GOLD 18K
- `azurefilm_pla_silkgold24k_1000_175_p` — Silk GOLD 24K
- `azurefilm_pla_silklila_1000_175_p` — Silk LILA
- `azurefilm_pla_silkhawaiian_1000_175_p` — Silk HAWAIIAN
- `azurefilm_pla_silkoceanbllue_1000_175_p` — Silk OCEAN BLLUE
- `azurefilm_pla_silkpistachio_1000_175_p` — Silk PISTACHIO
- `azurefilm_pla_silkgraphitegrey_1000_175_p` — Silk GRAPHITE GREY
- `azurefilm_pla_silkaquamarine_1000_175_p` — Silk AQUA MARINE
- `azurefilm_pla_silkturquoise_1000_175_p` — Silk TURQUOISE
- `azurefilm_pla_silkrainbowlavander_1000_175_p` — Silk Rainbow LAVANDER
- `azurefilm_pla_silkrainbowaurora_1000_175_p` — Silk Rainbow AURORA
- `azurefilm_pla_silkrainbowcandy_1000_175_p` — Silk Rainbow CANDY
- `azurefilm_pla_silkrainbowharmony_1000_175_p` — Silk Rainbow HARMONY
- `azurefilm_pla_silkrainbowamber_1000_175_p` — Silk Rainbow AMBER
- `azurefilm_pla_silkdualcolorobsidianmoss_1000_175_p` — Silk Dual Color Obsidian Moss
- `azurefilm_pla_silkdualcolorvelvetbloom_1000_175_p` — Silk Dual Color Velvet Bloom
- `azurefilm_pla_silkdualcoloremeraldsurf_1000_175_p` — Silk Dual Color Emerald Surf
- `azurefilm_pla_silkdualcolormidnightchrome_1000_175_p` — Silk Dual Color Midnight Chrome
- `azurefilm_pla_silkdualcolorcrimsonsteel_1000_175_p` — Silk Dual Color Crimson Steel
- `azurefilm_pla_silkdualcolorrosefortune_1000_175_p` — Silk Dual Color Rose Fortune
- `azurefilm_pla_silkdualcolorgoldenshadow_1000_175_p` — Silk Dual Color Golden Shadow
- `azurefilm_pla_silkdualcoloryinyang_1000_175_p` — Silk Dual Color Yin Yang
- `azurefilm_pla_silktricolorpeacockbloom_1000_175_p` — Silk Tri Color Peacock Bloom
- `azurefilm_pla_silktricolormermaiddream_1000_175_p` — Silk Tri Color Mermaid Dream
- `azurefilm_pla_silktricolorsunrisepop_1000_175_p` — Silk Tri Color Sunrise Pop
- `azurefilm_pla_silktricolorroyalfizz_1000_175_p` — Silk Tri Color Royal Fizz
- `azurefilm_pla_silktricolorsunsetblaze_1000_175_p` — Silk Tri Color Sunset Blaze
- `azurefilm_pla_mattehsred_1000_175_p` — Matte HS RED
- `azurefilm_petg_originalwhite_1000_175_p` — Original WHITE
- `azurefilm_petg_originalyellow_1000_175_p` — Original YELLOW
- `azurefilm_petg_originalorange_1000_175_p` — Original ORANGE
- `azurefilm_petg_originaltigerorange_1000_175_p` — Original TIGER ORANGE
- `azurefilm_petg_originallipstickred_1000_175_p` — Original LIPSTICK RED
- `azurefilm_petg_originalraspberryred_1000_175_p` — Original RASPBERRY RED
- `azurefilm_petg_originalfuchsiapink_1000_175_p` — Original FUCHSIA PINK
- `azurefilm_petg_originallila_1000_175_p` — Original LILA
- `azurefilm_petg_originalblue_1000_175_p` — Original BLUE
- `azurefilm_petg_originaldarkblue_1000_175_p` — Original DARK BLUE
- `azurefilm_petg_originalturquoise_1000_175_p` — Original TURQUOISE
- `azurefilm_petg_originallightgreen_1000_175_p` — Original LIGHT GREEN
- `azurefilm_petg_originalgrassgreen_1000_175_p` — Original GRASS GREEN
- `azurefilm_petg_originalsilver_1000_175_p` — Original SILVER
- `azurefilm_petg_originalgrey_1000_175_p` — Original GREY
- `azurefilm_petg_originalblack_1000_175_p` — Original BLACK
- `azurefilm_petg_transparentyellow_1000_175_p` — Transparent YELLOW
- `azurefilm_petg_transparentred_1000_175_p` — Transparent RED
- `azurefilm_petg_transparentpurple_1000_175_p` — Transparent PURPLE
- `azurefilm_petg_transparentblue_1000_175_p` — Transparent BLUE
- `azurefilm_petg_transparentgreen_1000_175_p` — Transparent GREEN
- `azurefilm_petg_pastelyellow_1000_175_p` — Pastel YELLOW
- `azurefilm_petg_pastelpink_1000_175_p` — Pastel PINK
- `azurefilm_petg_pastelmintgreen_1000_175_p` — Pastel MINT GREEN
- `azurefilm_petg_pastelblue_1000_175_p` — Pastel BLUE
- `azurefilm_petg_skinlatte_1000_175_p` — Skin LATTE
- `azurefilm_petg_skinmacchiato_1000_175_p` — Skin MACCHIATO
- `azurefilm_petg_skincappuccino_1000_175_p` — Skin CAPPUCCINO
- `azurefilm_petg_skinespresso_1000_175_p` — Skin ESPRESSO
- `azurefilm_abs_primeprimewhite_1000_175_p` — Prime Prime WHITE
- `azurefilm_abs_primeprimered_1000_175_p` — Prime Prime RED
- `azurefilm_abs_primeprimedarkblue_1000_175_p` — Prime Prime DARK BLUE
- `azurefilm_abs_primeprimesilver_1000_175_p` — Prime Prime SILVER
- `azurefilm_abs_primeprimeblack_1000_175_p` — Prime Prime BLACK
- `azurefilm_tpu_85a85atransparent_1000_175_p` — 85A 85A TRANSPARENT
- `azurefilm_tpu_85a85awhite_1000_175_p` — 85A 85A WHITE
- `azurefilm_tpu_85a85aneonyellow_1000_175_p` — 85A 85A NEON YELLOW
- `azurefilm_tpu_85a85aneonorange_1000_175_p` — 85A 85A NEON ORANGE
- `azurefilm_tpu_85a85ared_1000_175_p` — 85A 85A RED
- `azurefilm_tpu_85a85aneongreen_1000_175_p` — 85A 85A NEON GREEN
- `azurefilm_tpu_85a85ablue_1000_175_p` — 85A 85A BLUE
- `azurefilm_tpu_85a85ablack_1000_175_p` — 85A 85A BLACK
- `azurefilm_tpu_98a98atransparent_1000_175_p` — 98A 98A TRANSPARENT
- `azurefilm_tpu_98a98awhite_1000_175_p` — 98A 98A WHITE
- `azurefilm_tpu_98a98aneonyellow_1000_175_p` — 98A 98A NEON YELLOW
- `azurefilm_tpu_98a98aneonorange_1000_175_p` — 98A 98A NEON ORANGE
- `azurefilm_tpu_98a98ared_1000_175_p` — 98A 98A RED
- `azurefilm_tpu_98a98aneongreen_1000_175_p` — 98A 98A NEON GREEN
- `azurefilm_tpu_98a98ablue_1000_175_p` — 98A 98A BLUE
- `azurefilm_tpu_98a98ablack_1000_175_p` — 98A 98A BLACK
- `azurefilm_cf_carbonfiberpet_1000_175_p` — Carbon Fiber PET
- `azurefilm_cf_carbonfiberpaht_1000_175_p` — Carbon Fiber PAHT
- `azurefilm_pc_pcabswhite_1000_175_p` — PC ABS WHITE
- `azurefilm_pc_pcabsnatur_1000_175_p` — PC ABS NATUR
- `azurefilm_pc_pcabsblack_1000_175_p` — PC ABS BLACK
- `azurefilm_abs_absprimeblack_1000_175_p` — ABS Prime Black
- `azurefilm_abs_absprimedarkblue_1000_175_p` — ABS Prime Dark Blue
- `azurefilm_abs_absprimered_1000_175_p` — ABS Prime Red
- `azurefilm_abs_absprimesilver_1000_175_p` — ABS Prime Silver
- `azurefilm_abs_absprimewhite_1000_175_p` — ABS Prime White
- `azurefilm_pa6_pa6carbonfibernylonblack_500_175_p` — PA6 Carbonfiber nylon Black
- `azurefilm_pet_carbonfiberpetblack_500_175_p` — Carbonfiber PET Black
- `azurefilm_petg_petgblack_1000_175_p` — PETG Black
- `azurefilm_petg_petgblue_1000_175_p` — PETG Blue
- `azurefilm_petg_petgbrightgreen_1000_175_p` — PETG Bright green
- `azurefilm_petg_petggrey_1000_175_p` — PETG Grey
- `azurefilm_petg_petgneonlime_1000_175_p` — PETG Neon lime
- `azurefilm_petg_petgorange_1000_175_p` — PETG Orange
- `azurefilm_petg_petgpurple_1000_175_p` — PETG Purple
- `azurefilm_petg_petgraspberry_1000_175_p` — PETG Raspberry
- `azurefilm_petg_petgred_1000_175_p` — PETG Red
- `azurefilm_petg_petgtranslucentblue_1000_175_p` — PETG Translucent blue
- `azurefilm_petg_petgtranslucentdarkblue_1000_175_p` — PETG Translucent dark blue
- `azurefilm_petg_petgtranslucentgreen_1000_175_p` — PETG Translucent green
- `azurefilm_petg_petgtranslucentpurple_1000_175_p` — PETG Translucent purple
- `azurefilm_petg_petgtranslucentyellow_1000_175_p` — PETG Translucent yellow
- `azurefilm_petg_petgturquoise_1000_175_p` — PETG Turquoise
- `azurefilm_petg_petgwhite_1000_175_p` — PETG White
- `azurefilm_petg_petgblack_2100_175_p` — PETG Black
- `azurefilm_petg_petgblue_2100_175_p` — PETG Blue
- `azurefilm_petg_petgbrightgreen_2100_175_p` — PETG Bright green
- `azurefilm_petg_petggrey_2100_175_p` — PETG Grey
- `azurefilm_petg_petgneonlime_2100_175_p` — PETG Neon lime
- `azurefilm_petg_petgorange_2100_175_p` — PETG Orange
- `azurefilm_petg_petgpurple_2100_175_p` — PETG Purple
- `azurefilm_petg_petgraspberry_2100_175_p` — PETG Raspberry
- `azurefilm_petg_petgred_2100_175_p` — PETG Red
- `azurefilm_petg_petgtranslucentblue_2100_175_p` — PETG Translucent blue
- `azurefilm_petg_petgtranslucentdarkblue_2100_175_p` — PETG Translucent dark blue
- `azurefilm_petg_petgtranslucentgreen_2100_175_p` — PETG Translucent green
- `azurefilm_petg_petgtranslucentpurple_2100_175_p` — PETG Translucent purple
- `azurefilm_petg_petgtranslucentyellow_2100_175_p` — PETG Translucent yellow
- `azurefilm_petg_petgtransparent_2100_175_p` — PETG Transparent
- `azurefilm_petg_petgturquoise_2100_175_p` — PETG Turquoise
- `azurefilm_petg_petgwhite_2100_175_p` — PETG White
- `azurefilm_pla_plababybluepastel_1000_175_p` — PLA Baby Blue Pastel
- `azurefilm_pla_plabananayellowpastel_1000_175_p` — PLA Banana Yellow Pastel
- `azurefilm_pla_plablackglitter_1000_175_p` — PLA Black glitter
- `azurefilm_pla_plablueglitter_1000_175_p` — PLA Blue glitter
- `azurefilm_pla_placaribbeangreen_1000_175_p` — PLA Caribbean Green
- `azurefilm_pla_plaemeraldgreen_1000_175_p` — PLA Emerald Green
- `azurefilm_pla_plagreenglitter_1000_175_p` — PLA Green glitter
- `azurefilm_pla_plagrey_1000_175_p` — PLA Grey
- `azurefilm_pla_plaicecreampinkpastel_1000_175_p` — PLA Ice Cream Pink Pastel
- `azurefilm_pla_plalagoongreen_1000_175_p` — PLA Lagoon Green
- `azurefilm_pla_plamintgreenpastel_1000_175_p` — PLA Mint Green Pastel
- `azurefilm_pla_planeutralglitter_1000_175_p` — PLA Neutral glitter
- `azurefilm_pla_plapistachiogreen_1000_175_p` — PLA Pistachio Green
- `azurefilm_pla_plaredglitter_1000_175_p` — PLA Red glitter
- `azurefilm_pla_plawhiteglitter_1000_175_p` — PLA White glitter
- `azurefilm_pla_plaanthracite_2100_175_p` — PLA Anthracite
- `azurefilm_pla_plababybluepastel_2100_175_p` — PLA Baby Blue Pastel
- `azurefilm_pla_plabananayellowpastel_2100_175_p` — PLA Banana Yellow Pastel
- `azurefilm_pla_plablack_2100_175_p` — PLA Black
- `azurefilm_pla_plablackglitter_2100_175_p` — PLA Black glitter
- `azurefilm_pla_plablue_2100_175_p` — PLA Blue
- `azurefilm_pla_plablueglitter_2100_175_p` — PLA Blue glitter
- `azurefilm_pla_placaribbeangreen_2100_175_p` — PLA Caribbean Green
- `azurefilm_pla_plachampagne_2100_175_p` — PLA Champagne
- `azurefilm_pla_plachampagnegold_2100_175_p` — PLA Champagne Gold
- `azurefilm_pla_placoralred_2100_175_p` — PLA Coral Red
- `azurefilm_pla_plaemeraldgreen_2100_175_p` — PLA Emerald Green
- `azurefilm_pla_plafoggywhite_2100_175_p` — PLA Foggy White
- `azurefilm_pla_plafuchsiapink_2100_175_p` — PLA Fuchsia Pink
- `azurefilm_pla_plagalaxyblack_2100_175_p` — PLA Galaxy Black
- `azurefilm_pla_plagold_2100_175_p` — PLA Gold
- `azurefilm_pla_plagreen_2100_175_p` — PLA Green
- `azurefilm_pla_plagreenglitter_2100_175_p` — PLA Green glitter
- `azurefilm_pla_plagrey_2100_175_p` — PLA Grey
- `azurefilm_pla_plaicecreampinkpastel_2100_175_p` — PLA Ice Cream Pink Pastel
- `azurefilm_pla_plalagoongreen_2100_175_p` — PLA Lagoon Green
- `azurefilm_pla_plalightgreen_2100_175_p` — PLA Light Green
- `azurefilm_pla_plalightgrey_2100_175_p` — PLA Light Grey
- `azurefilm_pla_plamarble_2100_175_p` — PLA Marble
- `azurefilm_pla_plamintgreenpastel_2100_175_p` — PLA Mint Green Pastel
- `azurefilm_pla_planavyblue_2100_175_p` — PLA Navy Blue
- `azurefilm_pla_planeutralglitter_2100_175_p` — PLA Neutral glitter
- `azurefilm_pla_plaorange_2100_175_p` — PLA Orange
- `azurefilm_pla_plapink_2100_175_p` — PLA Pink
- `azurefilm_pla_plapistachiogreen_2100_175_p` — PLA Pistachio Green
- `azurefilm_pla_plaredglitter_2100_175_p` — PLA Red glitter
- `azurefilm_pla_plaredwine_2100_175_p` — PLA Red Wine
- `azurefilm_pla_plasharkgrey_2100_175_p` — PLA Shark Grey
- `azurefilm_pla_plasunsetorange_2100_175_p` — PLA Sunset Orange
- `azurefilm_pla_plawhite_2100_175_p` — PLA White
- `azurefilm_pla_plawhiteglitter_2100_175_p` — PLA White glitter
- `azurefilm_pla_playellow_2100_175_p` — PLA Yellow
- `azurefilm_pla_plaanthracite_5000_175_p` — PLA Anthracite
- `azurefilm_pla_plababybluepastel_5000_175_p` — PLA Baby Blue Pastel
- `azurefilm_pla_plabananayellowpastel_5000_175_p` — PLA Banana Yellow Pastel
- `azurefilm_pla_plablack_5000_175_p` — PLA Black
- `azurefilm_pla_plablackglitter_5000_175_p` — PLA Black glitter
- `azurefilm_pla_plablue_5000_175_p` — PLA Blue
- `azurefilm_pla_plablueglitter_5000_175_p` — PLA Blue glitter
- `azurefilm_pla_placaribbeangreen_5000_175_p` — PLA Caribbean Green
- `azurefilm_pla_plachampagne_5000_175_p` — PLA Champagne
- `azurefilm_pla_plachampagnegold_5000_175_p` — PLA Champagne Gold
- `azurefilm_pla_placoralred_5000_175_p` — PLA Coral Red
- `azurefilm_pla_plaemeraldgreen_5000_175_p` — PLA Emerald Green
- `azurefilm_pla_plafoggywhite_5000_175_p` — PLA Foggy White
- `azurefilm_pla_plafuchsiapink_5000_175_p` — PLA Fuchsia Pink
- `azurefilm_pla_plagalaxyblack_5000_175_p` — PLA Galaxy Black
- `azurefilm_pla_plagold_5000_175_p` — PLA Gold
- `azurefilm_pla_plagreen_5000_175_p` — PLA Green
- `azurefilm_pla_plagreenglitter_5000_175_p` — PLA Green glitter
- `azurefilm_pla_plagrey_5000_175_p` — PLA Grey
- `azurefilm_pla_plaicecreampinkpastel_5000_175_p` — PLA Ice Cream Pink Pastel
- `azurefilm_pla_plalagoongreen_5000_175_p` — PLA Lagoon Green
- `azurefilm_pla_plalightgreen_5000_175_p` — PLA Light Green
- `azurefilm_pla_plalightgrey_5000_175_p` — PLA Light Grey
- `azurefilm_pla_plamarble_5000_175_p` — PLA Marble
- `azurefilm_pla_plamintgreenpastel_5000_175_p` — PLA Mint Green Pastel
- `azurefilm_pla_planavyblue_5000_175_p` — PLA Navy Blue
- `azurefilm_pla_planeutralglitter_5000_175_p` — PLA Neutral glitter
- `azurefilm_pla_plaorange_5000_175_p` — PLA Orange
- `azurefilm_pla_plapink_5000_175_p` — PLA Pink
- `azurefilm_pla_plapistachiogreen_5000_175_p` — PLA Pistachio Green
- `azurefilm_pla_plaredglitter_5000_175_p` — PLA Red glitter
- `azurefilm_pla_plaredwine_5000_175_p` — PLA Red Wine
- `azurefilm_pla_plasharkgrey_5000_175_p` — PLA Shark Grey
- `azurefilm_pla_plasunsetorange_5000_175_p` — PLA Sunset Orange
- `azurefilm_pla_plawhite_5000_175_p` — PLA White
- `azurefilm_pla_plawhiteglitter_5000_175_p` — PLA White glitter
- `azurefilm_pla_playellow_5000_175_p` — PLA Yellow
- `azurefilm_pla_plaanthracite_10000_175_p` — PLA Anthracite
- `azurefilm_pla_plababybluepastel_10000_175_p` — PLA Baby Blue Pastel
- `azurefilm_pla_plabananayellowpastel_10000_175_p` — PLA Banana Yellow Pastel
- `azurefilm_pla_plablack_10000_175_p` — PLA Black
- `azurefilm_pla_plablackglitter_10000_175_p` — PLA Black glitter
- `azurefilm_pla_plablue_10000_175_p` — PLA Blue
- `azurefilm_pla_plablueglitter_10000_175_p` — PLA Blue glitter
- `azurefilm_pla_placaribbeangreen_10000_175_p` — PLA Caribbean Green
- `azurefilm_pla_plachampagne_10000_175_p` — PLA Champagne
- `azurefilm_pla_plachampagnegold_10000_175_p` — PLA Champagne Gold
- `azurefilm_pla_placoralred_10000_175_p` — PLA Coral Red
- `azurefilm_pla_plaemeraldgreen_10000_175_p` — PLA Emerald Green
- `azurefilm_pla_plafoggywhite_10000_175_p` — PLA Foggy White
- `azurefilm_pla_plafuchsiapink_10000_175_p` — PLA Fuchsia Pink
- `azurefilm_pla_plagalaxyblack_10000_175_p` — PLA Galaxy Black
- `azurefilm_pla_plagold_10000_175_p` — PLA Gold
- `azurefilm_pla_plagreen_10000_175_p` — PLA Green
- `azurefilm_pla_plagreenglitter_10000_175_p` — PLA Green glitter
- `azurefilm_pla_plagrey_10000_175_p` — PLA Grey
- `azurefilm_pla_plaicecreampinkpastel_10000_175_p` — PLA Ice Cream Pink Pastel
- `azurefilm_pla_plalagoongreen_10000_175_p` — PLA Lagoon Green
- `azurefilm_pla_plalightgreen_10000_175_p` — PLA Light Green
- `azurefilm_pla_plalightgrey_10000_175_p` — PLA Light Grey
- `azurefilm_pla_plamarble_10000_175_p` — PLA Marble
- `azurefilm_pla_plamintgreenpastel_10000_175_p` — PLA Mint Green Pastel
- `azurefilm_pla_planavyblue_10000_175_p` — PLA Navy Blue
- `azurefilm_pla_planeutralglitter_10000_175_p` — PLA Neutral glitter
- `azurefilm_pla_plaorange_10000_175_p` — PLA Orange
- `azurefilm_pla_plapink_10000_175_p` — PLA Pink
- `azurefilm_pla_plapistachiogreen_10000_175_p` — PLA Pistachio Green
- `azurefilm_pla_plaredglitter_10000_175_p` — PLA Red glitter
- `azurefilm_pla_plaredwine_10000_175_p` — PLA Red Wine
- `azurefilm_pla_plasharkgrey_10000_175_p` — PLA Shark Grey
- `azurefilm_pla_plasunsetorange_10000_175_p` — PLA Sunset Orange
- `azurefilm_pla_plawhite_10000_175_p` — PLA White
- `azurefilm_pla_plawhiteglitter_10000_175_p` — PLA White glitter
- `azurefilm_pla_playellow_10000_175_p` — PLA Yellow
- `azurefilm_pla_mattehsplaarmygreen_1000_175_p` — Matte HS PLA Army Green
- `azurefilm_pla_mattehsplacoral_1000_175_p` — Matte HS PLA Coral
- `azurefilm_pla_mattehsplacreamstone_1000_175_p` — Matte HS PLA Creamstone
- `azurefilm_pla_mattehsplamistgrey_1000_175_p` — Matte HS PLA Mist Grey
- `azurefilm_pla_silkplaakvamarin_1000_175_p` — Silk PLA Akvamarin
- `azurefilm_pla_silkplagold_1000_175_p` — Silk PLA Gold
- `azurefilm_pla_silkplaoceanblue_1000_175_p` — Silk PLA Ocean blue
- `azurefilm_pla_silkplaturquoiseblue_1000_175_p` — Silk PLA Turquoise blue
- `azurefilm_pla_woodplabamboo_750_175_p` — Wood PLA Bamboo
- `azurefilm_pla_woodplacork_750_175_p` — Wood PLA Cork
- `azurefilm_pla_woodplacorkglitter_750_175_p` — Wood PLA Cork glitter
- `azurefilm_pla_woodplapine_750_175_p` — Wood PLA Pine
- `azurefilm_tpu_tpu85ablack_1000_175_p` — TPU 85A Black
- `azurefilm_tpu_tpu85ablue_1000_175_p` — TPU 85A Blue
- `azurefilm_tpu_tpu85aneongreen_1000_175_p` — TPU 85A Neon Green
- `azurefilm_tpu_tpu85aneonorange_1000_175_p` — TPU 85A Neon Orange
- `azurefilm_tpu_tpu85aneonyellow_1000_175_p` — TPU 85A Neon Yellow
- `azurefilm_tpu_tpu85ared_1000_175_p` — TPU 85A Red
- `azurefilm_tpu_tpu85atransparent_1000_175_p` — TPU 85A Transparent
- `azurefilm_tpu_tpu85awhite_1000_175_p` — TPU 85A White
- `azurefilm_tpu_tpu/tpeblack85a_300_175_p` — TPU/TPE Black 85A
- `azurefilm_tpu_tpu/tpeblack98a_300_175_p` — TPU/TPE Black 98A
- `azurefilm_tpu_tpu/tpeblue98a_300_175_p` — TPU/TPE Blue 98A
- `azurefilm_tpu_tpu/tpeneonorange98a_300_175_p` — TPU/TPE Neon orange 98A
- `azurefilm_tpu_tpu/tpeneonyellow98a_300_175_p` — TPU/TPE Neon yellow 98A
- `azurefilm_tpu_tpu/tpered98a_300_175_p` — TPU/TPE Red 98A
- `azurefilm_tpu_tpu/tpetransparent85a_300_175_p` — TPU/TPE Transparent 85A
- `azurefilm_tpu_tpu/tpetransparent98a_300_175_p` — TPU/TPE Transparent 98A
- `azurefilm_tpu_tpu/tpewhite85a_300_175_p` — TPU/TPE White 85A
- `azurefilm_tpu_tpu/tpewhite98a_300_175_p` — TPU/TPE White 98A
