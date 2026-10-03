# prusament duplicate migration review

Base `4d5382a6105c6571187daff94a0964304c982bf3`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `bddc79b07dffc8679dc82ed1fed9fc4aca3a22dca4a8d9f613f905405876c1f6`.

## Authorization and result

{"groups": 75, "approved_groups": 74, "retired": 74, "deferred": 1, "hard_stops": 0, "before_count": 52368, "after_count": 52294, "brand_before": 378, "brand_after": 304, "registry_before": 1066, "registry_after": 1140, "metadata_fields_changed": 116, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Apply current exact-line manufacturer printing recommendations only to the74 approved survivor IDs: PLA scalar215→210 and range205–225→200–220, PETG scalarbed90→80. Matte PETG Black/Matte Black line-color decomposition is deferred unchanged. Density and all HEX, packaging, tare and unrelated variants remain unchanged. Both normal PLA and PLA Blend current linked TDS agree; specimen testing settings are not treated as recommendations.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://prusament.com/materials/pla/", "tds_bundle": "https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-prusament-prod/2024/05/7ca620c4-prusament-pla-plablend.zip", "members": ["Prusament PLA/1_PLA_Prusament_TDS_2022_EN.pdf", "Prusament PLA Blend/TDS_Prusament_PLA-Blend_EN.pdf"], "recommended": {"density": 1.24, "nozzle": [200, 220], "bed": [40, 60]}, "note": "Both exact currently linked PLA and PLA Blend TDS recommend210±10, not215 specimen testing temperature."}
- {"url": "https://prusament.com/materials/prusament-petg/", "tds": "https://storage.googleapis.com/prusa3d-content-prod-14e8-wordpress-prusament-prod/2023/10/9f8d2165-tds_prusament-petg_n_en.pdf", "recommended": {"density": 1.27, "nozzle": [240, 260], "bed": [70, 90]}, "note": "TDS and current product page agree on80±10 bed; survivor range already correct, scalar90 corrected to80."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`prusament_petg_petganthracitegrey_1000_175_c`|`prusament_petg_anthracitegrey_1000_175_c`|`prusament.json::Prusament::PETG {color_name}::PETG Anthracite Grey::PETG::1000::1.75::cardboard::False`|
|`prusament_petg_petganthracitegrey_2000_175_p`|`prusament_petg_anthracitegrey_2000_175_p`|`prusament.json::Prusament::PETG {color_name}::PETG Anthracite Grey::PETG::2000::1.75::plastic::False`|
|`prusament_petg_petgcarminered_1000_175_c`|`prusament_petg_carminered_1000_175_c`|`prusament.json::Prusament::PETG {color_name}::PETG Carmine Red::PETG::1000::1.75::cardboard::False`|
|`prusament_petg_petgcarminered_2000_175_p`|`prusament_petg_carminered_2000_175_p`|`prusament.json::Prusament::PETG {color_name}::PETG Carmine Red::PETG::2000::1.75::plastic::False`|
|`prusament_petg_petgchalkyblue_1000_175_c`|`prusament_petg_chalkyblue_1000_175_c`|`prusament.json::Prusament::PETG {color_name}::PETG Chalky Blue::PETG::1000::1.75::cardboard::False`|
|`prusament_petg_petgchalkyblue_2000_175_p`|`prusament_petg_chalkyblue_2000_175_p`|`prusament.json::Prusament::PETG {color_name}::PETG Chalky Blue::PETG::2000::1.75::plastic::False`|
|`prusament_petg_petgclear_1000_175_c`|`prusament_petg_clear_1000_175_c`|`prusament.json::Prusament::PETG {color_name}::PETG Clear::PETG::1000::1.75::cardboard::False`|
|`prusament_petg_petgclear_2000_175_p`|`prusament_petg_clear_2000_175_p`|`prusament.json::Prusament::PETG {color_name}::PETG Clear::PETG::2000::1.75::plastic::False`|
|`prusament_petg_petgjetblack_1000_175_c`|`prusament_petg_jetblack_1000_175_c`|`prusament.json::Prusament::PETG {color_name}::PETG Jet Black::PETG::1000::1.75::cardboard::False`|
|`prusament_petg_petgjetblack_2000_175_p`|`prusament_petg_jetblack_2000_175_p`|`prusament.json::Prusament::PETG {color_name}::PETG Jet Black::PETG::2000::1.75::plastic::False`|
|`prusament_petg_petgjunglegreen_1000_175_c`|`prusament_petg_junglegreen_1000_175_c`|`prusament.json::Prusament::PETG {color_name}::PETG Jungle Green::PETG::1000::1.75::cardboard::False`|
|`prusament_petg_petgjunglegreen_2000_175_p`|`prusament_petg_junglegreen_2000_175_p`|`prusament.json::Prusament::PETG {color_name}::PETG Jungle Green::PETG::2000::1.75::plastic::False`|
|`prusament_petg_petglipstickred_1000_175_c`|`prusament_petg_lipstickred_1000_175_c`|`prusament.json::Prusament::PETG {color_name}::PETG Lipstick Red::PETG::1000::1.75::cardboard::False`|
|`prusament_petg_petglipstickred_2000_175_p`|`prusament_petg_lipstickred_2000_175_p`|`prusament.json::Prusament::PETG {color_name}::PETG Lipstick Red::PETG::2000::1.75::plastic::False`|
|`prusament_petg_petgmangoyellow_1000_175_c`|`prusament_petg_mangoyellow_1000_175_c`|`prusament.json::Prusament::PETG {color_name}::PETG Mango Yellow::PETG::1000::1.75::cardboard::False`|
|`prusament_petg_petgmangoyellow_2000_175_p`|`prusament_petg_mangoyellow_2000_175_p`|`prusament.json::Prusament::PETG {color_name}::PETG Mango Yellow::PETG::2000::1.75::plastic::False`|
|`prusament_petg_petgoceanblue_1000_175_c`|`prusament_petg_oceanblue_1000_175_c`|`prusament.json::Prusament::PETG {color_name}::PETG Ocean Blue::PETG::1000::1.75::cardboard::False`|
|`prusament_petg_petgoceanblue_2000_175_p`|`prusament_petg_oceanblue_2000_175_p`|`prusament.json::Prusament::PETG {color_name}::PETG Ocean Blue::PETG::2000::1.75::plastic::False`|
|`prusament_petg_petgpistachiogreen_1000_175_c`|`prusament_petg_pistachiogreen_1000_175_c`|`prusament.json::Prusament::PETG {color_name}::PETG Pistachio Green::PETG::1000::1.75::cardboard::False`|
|`prusament_petg_petgpistachiogreen_2000_175_p`|`prusament_petg_pistachiogreen_2000_175_p`|`prusament.json::Prusament::PETG {color_name}::PETG Pistachio Green::PETG::2000::1.75::plastic::False`|
|`prusament_petg_petgprusaorange_1000_175_c`|`prusament_petg_prusaorange_1000_175_c`|`prusament.json::Prusament::PETG {color_name}::PETG Prusa Orange::PETG::1000::1.75::cardboard::False`|
|`prusament_petg_petgprusaorange_2000_175_p`|`prusament_petg_prusaorange_2000_175_p`|`prusament.json::Prusament::PETG {color_name}::PETG Prusa Orange::PETG::2000::1.75::plastic::False`|
|`prusament_petg_petgsignalwhite_1000_175_c`|`prusament_petg_signalwhite_1000_175_c`|`prusament.json::Prusament::PETG {color_name}::PETG Signal White::PETG::1000::1.75::cardboard::False`|
|`prusament_petg_petgsignalwhite_2000_175_p`|`prusament_petg_signalwhite_2000_175_p`|`prusament.json::Prusament::PETG {color_name}::PETG Signal White::PETG::2000::1.75::plastic::False`|
|`prusament_petg_petgterracottalight_1000_175_c`|`prusament_petg_terracottalight_1000_175_c`|`prusament.json::Prusament::PETG {color_name}::PETG Terracotta Light::PETG::1000::1.75::cardboard::False`|
|`prusament_petg_petgterracottalight_2000_175_p`|`prusament_petg_terracottalight_2000_175_p`|`prusament.json::Prusament::PETG {color_name}::PETG Terracotta Light::PETG::2000::1.75::plastic::False`|
|`prusament_petg_petgultramarineblue_1000_175_c`|`prusament_petg_ultramarineblue_1000_175_c`|`prusament.json::Prusament::PETG {color_name}::PETG Ultramarine Blue::PETG::1000::1.75::cardboard::False`|
|`prusament_petg_petgultramarineblue_2000_175_p`|`prusament_petg_ultramarineblue_2000_175_p`|`prusament.json::Prusament::PETG {color_name}::PETG Ultramarine Blue::PETG::2000::1.75::plastic::False`|
|`prusament_petg_petgurbangrey_1000_175_c`|`prusament_petg_urbangrey_1000_175_c`|`prusament.json::Prusament::PETG {color_name}::PETG Urban Grey::PETG::1000::1.75::cardboard::False`|
|`prusament_petg_petgurbangrey_2000_175_p`|`prusament_petg_urbangrey_2000_175_p`|`prusament.json::Prusament::PETG {color_name}::PETG Urban Grey::PETG::2000::1.75::plastic::False`|
|`prusament_petg_petgyellowgold_1000_175_c`|`prusament_petg_yellowgold_1000_175_c`|`prusament.json::Prusament::PETG {color_name}::PETG Yellow Gold::PETG::1000::1.75::cardboard::False`|
|`prusament_petg_petgyellowgold_2000_175_p`|`prusament_petg_yellowgold_2000_175_p`|`prusament.json::Prusament::PETG {color_name}::PETG Yellow Gold::PETG::2000::1.75::plastic::False`|
|`prusament_pla_plaarmygreen_1000_175_c`|`prusament_pla_armygreen_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Army Green::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plaarmygreen_2000_175_p`|`prusament_pla_armygreen_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Army Green::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plaazureblue_1000_175_c`|`prusament_pla_azureblue_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Azure Blue::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plaazureblue_2000_175_p`|`prusament_pla_azureblue_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Azure Blue::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plagalaxyblack_1000_175_c`|`prusament_pla_galaxyblack_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Galaxy Black::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plagalaxyblack_2000_175_p`|`prusament_pla_galaxyblack_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Galaxy Black::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plagalaxygreen_1000_175_c`|`prusament_pla_galaxygreen_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Galaxy Green::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plagalaxygreen_2000_175_p`|`prusament_pla_galaxygreen_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Galaxy Green::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plagalaxypurple_1000_175_c`|`prusament_pla_galaxypurple_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Galaxy Purple::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plagalaxypurple_2000_175_p`|`prusament_pla_galaxypurple_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Galaxy Purple::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plagalaxyred_1000_175_c`|`prusament_pla_galaxyred_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Galaxy Red::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plagalaxyred_2000_175_p`|`prusament_pla_galaxyred_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Galaxy Red::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plagalaxysilver_1000_175_c`|`prusament_pla_galaxysilver_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Galaxy Silver::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plagalaxysilver_2000_175_p`|`prusament_pla_galaxysilver_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Galaxy Silver::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plagentleman'sgrey_1000_175_c`|`prusament_pla_gentleman'sgrey_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Gentleman's Grey::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plagentleman'sgrey_2000_175_p`|`prusament_pla_gentleman'sgrey_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Gentleman's Grey::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plagravitygrey_1000_175_c`|`prusament_pla_gravitygrey_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Gravity Grey::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plagravitygrey_2000_175_p`|`prusament_pla_gravitygrey_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Gravity Grey::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plajetblack_1000_175_c`|`prusament_pla_jetblack_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Jet Black::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plajetblack_2000_175_p`|`prusament_pla_jetblack_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Jet Black::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plalipstickred_1000_175_c`|`prusament_pla_lipstickred_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Lipstick Red::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plalipstickred_2000_175_p`|`prusament_pla_lipstickred_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Lipstick Red::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plamarblegrey_1000_175_c`|`prusament_pla_marblegrey_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Marble Grey::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plamarblegrey_2000_175_p`|`prusament_pla_marblegrey_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Marble Grey::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plams.pink_1000_175_c`|`prusament_pla_ms.pink_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Ms. Pink::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plams.pink_2000_175_p`|`prusament_pla_ms.pink_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Ms. Pink::PLA::2000::1.75::plastic::False`|
|`prusament_pla_planatural_1000_175_c`|`prusament_pla_natural_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Natural::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_planatural_2000_175_p`|`prusament_pla_natural_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Natural::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plaopalgreen_1000_175_c`|`prusament_pla_opalgreen_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Opal Green::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plaopalgreen_2000_175_p`|`prusament_pla_opalgreen_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Opal Green::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plapearlmouse_1000_175_c`|`prusament_pla_pearlmouse_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Pearl Mouse::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plapearlmouse_2000_175_p`|`prusament_pla_pearlmouse_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Pearl Mouse::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plapineappleyellow_1000_175_c`|`prusament_pla_pineappleyellow_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Pineapple Yellow::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plapineappleyellow_2000_175_p`|`prusament_pla_pineappleyellow_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Pineapple Yellow::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plapristinewhite_1000_175_c`|`prusament_pla_pristinewhite_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Pristine White::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plapristinewhite_2000_175_p`|`prusament_pla_pristinewhite_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Pristine White::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plaprusaorange_1000_175_c`|`prusament_pla_prusaorange_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Prusa Orange::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plaprusaorange_2000_175_p`|`prusament_pla_prusaorange_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Prusa Orange::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plasimplygreen_1000_175_c`|`prusament_pla_simplygreen_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Simply Green::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plasimplygreen_2000_175_p`|`prusament_pla_simplygreen_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Simply Green::PLA::2000::1.75::plastic::False`|
|`prusament_pla_plavanillawhite_1000_175_c`|`prusament_pla_vanillawhite_1000_175_c`|`prusament.json::Prusament::PLA {color_name}::PLA Vanilla White::PLA::1000::1.75::cardboard::False`|
|`prusament_pla_plavanillawhite_2000_175_p`|`prusament_pla_vanillawhite_2000_175_p`|`prusament.json::Prusament::PLA {color_name}::PLA Vanilla White::PLA::2000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### PR001: dup-827c983d34b725fd7016db93273ae4bf2a899654d2d9df43d34efadf1633b7fb

Status: APPROVED; survivor `prusament_petg_anthracitegrey_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_anthracitegrey_2000_175_p`|`{color_name}`|`Anthracite Grey`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_petganthracitegrey_2000_175_p`|`PETG {color_name}`|`Anthracite Grey`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_anthracitegrey_2000_175_p": 219.0,
    "prusament_petg_petganthracitegrey_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_petg_anthracitegrey_2000_175_p": 250,
    "prusament_petg_petganthracitegrey_2000_175_p": null
  },
  "bed_temp": {
    "prusament_petg_anthracitegrey_2000_175_p": 90,
    "prusament_petg_petganthracitegrey_2000_175_p": null
  },
  "tds_url": {
    "prusament_petg_anthracitegrey_2000_175_p": "https://prusament.com/materials/",
    "prusament_petg_petganthracitegrey_2000_175_p": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR002: dup-967e6065b4c0cfb636b9818d9a3a69566d17d90ebd42af6aecd109cf3d266520

Status: APPROVED; survivor `prusament_petg_anthracitegrey_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_anthracitegrey_1000_175_c`|`{color_name}`|`Anthracite Grey`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_petganthracitegrey_1000_175_c`|`PETG {color_name}`|`Anthracite Grey`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_anthracitegrey_1000_175_c": 193.0,
    "prusament_petg_petganthracitegrey_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_petg_anthracitegrey_1000_175_c": 250,
    "prusament_petg_petganthracitegrey_1000_175_c": null
  },
  "bed_temp": {
    "prusament_petg_anthracitegrey_1000_175_c": 90,
    "prusament_petg_petganthracitegrey_1000_175_c": null
  },
  "tds_url": {
    "prusament_petg_anthracitegrey_1000_175_c": "https://prusament.com/materials/",
    "prusament_petg_petganthracitegrey_1000_175_c": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR003: dup-c41baf62d7050ca9bbdefd9ca6e3baf5a39d52598c6eb675187179a530e749d5

Status: APPROVED; survivor `prusament_petg_carminered_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_carminered_2000_175_p`|`{color_name}`|`Carmine Red`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_petgcarminered_2000_175_p`|`PETG {color_name}`|`Carmine Red`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_carminered_2000_175_p": 219.0,
    "prusament_petg_petgcarminered_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_petg_carminered_2000_175_p": 250,
    "prusament_petg_petgcarminered_2000_175_p": null
  },
  "bed_temp": {
    "prusament_petg_carminered_2000_175_p": 90,
    "prusament_petg_petgcarminered_2000_175_p": null
  },
  "translucent": {
    "prusament_petg_carminered_2000_175_p": false,
    "prusament_petg_petgcarminered_2000_175_p": true
  },
  "tds_url": {
    "prusament_petg_carminered_2000_175_p": "https://prusament.com/materials/",
    "prusament_petg_petgcarminered_2000_175_p": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR004: dup-f1384cd8964e80d1af89893d3ba84839c6c3beea46877b427ad4442f7fcbc2d5

Status: APPROVED; survivor `prusament_petg_carminered_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_carminered_1000_175_c`|`{color_name}`|`Carmine Red`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_petgcarminered_1000_175_c`|`PETG {color_name}`|`Carmine Red`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_carminered_1000_175_c": 193.0,
    "prusament_petg_petgcarminered_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_petg_carminered_1000_175_c": 250,
    "prusament_petg_petgcarminered_1000_175_c": null
  },
  "bed_temp": {
    "prusament_petg_carminered_1000_175_c": 90,
    "prusament_petg_petgcarminered_1000_175_c": null
  },
  "translucent": {
    "prusament_petg_carminered_1000_175_c": false,
    "prusament_petg_petgcarminered_1000_175_c": true
  },
  "tds_url": {
    "prusament_petg_carminered_1000_175_c": "https://prusament.com/materials/",
    "prusament_petg_petgcarminered_1000_175_c": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR005: dup-7d0a45a1d5ef2ceaba585ee83e13e866289e00f596d2fc306737f65835823daa

Status: APPROVED; survivor `prusament_petg_chalkyblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_chalkyblue_1000_175_c`|`{color_name}`|`Chalky Blue`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_petgchalkyblue_1000_175_c`|`PETG {color_name}`|`Chalky Blue`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_chalkyblue_1000_175_c": 193.0,
    "prusament_petg_petgchalkyblue_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_petg_chalkyblue_1000_175_c": 250,
    "prusament_petg_petgchalkyblue_1000_175_c": null
  },
  "bed_temp": {
    "prusament_petg_chalkyblue_1000_175_c": 90,
    "prusament_petg_petgchalkyblue_1000_175_c": null
  },
  "tds_url": {
    "prusament_petg_chalkyblue_1000_175_c": "https://prusament.com/materials/",
    "prusament_petg_petgchalkyblue_1000_175_c": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR006: dup-ad9a5b4e444624ea6a3c6b93ba6425f3c3c60332547040c7da1b0f6e4faf9aed

Status: APPROVED; survivor `prusament_petg_chalkyblue_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_chalkyblue_2000_175_p`|`{color_name}`|`Chalky Blue`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_petgchalkyblue_2000_175_p`|`PETG {color_name}`|`Chalky Blue`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_chalkyblue_2000_175_p": 219.0,
    "prusament_petg_petgchalkyblue_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_petg_chalkyblue_2000_175_p": 250,
    "prusament_petg_petgchalkyblue_2000_175_p": null
  },
  "bed_temp": {
    "prusament_petg_chalkyblue_2000_175_p": 90,
    "prusament_petg_petgchalkyblue_2000_175_p": null
  },
  "tds_url": {
    "prusament_petg_chalkyblue_2000_175_p": "https://prusament.com/materials/",
    "prusament_petg_petgchalkyblue_2000_175_p": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR007: dup-b9fad4e62c45f9008e42b425e47fb2a8f716a826963aba168b4da3c6c364c906

Status: APPROVED; survivor `prusament_petg_clear_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_clear_2000_175_p`|`{color_name}`|`Clear`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_petgclear_2000_175_p`|`PETG {color_name}`|`Clear`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_clear_2000_175_p": 219.0,
    "prusament_petg_petgclear_2000_175_p": 380
  },
  "color_hex": {
    "prusament_petg_clear_2000_175_p": "dcdcdc",
    "prusament_petg_petgclear_2000_175_p": "E4E7E5"
  },
  "extruder_temp": {
    "prusament_petg_clear_2000_175_p": 250,
    "prusament_petg_petgclear_2000_175_p": null
  },
  "bed_temp": {
    "prusament_petg_clear_2000_175_p": 90,
    "prusament_petg_petgclear_2000_175_p": null
  },
  "tds_url": {
    "prusament_petg_clear_2000_175_p": "https://prusament.com/materials/",
    "prusament_petg_petgclear_2000_175_p": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR008: dup-ccf2d332086e88b33737d20628b4c2f1d1156d389a453f8319a3079abb2c428f

Status: APPROVED; survivor `prusament_petg_clear_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_clear_1000_175_c`|`{color_name}`|`Clear`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_petgclear_1000_175_c`|`PETG {color_name}`|`Clear`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_clear_1000_175_c": 193.0,
    "prusament_petg_petgclear_1000_175_c": null
  },
  "color_hex": {
    "prusament_petg_clear_1000_175_c": "dcdcdc",
    "prusament_petg_petgclear_1000_175_c": "E4E7E5"
  },
  "extruder_temp": {
    "prusament_petg_clear_1000_175_c": 250,
    "prusament_petg_petgclear_1000_175_c": null
  },
  "bed_temp": {
    "prusament_petg_clear_1000_175_c": 90,
    "prusament_petg_petgclear_1000_175_c": null
  },
  "tds_url": {
    "prusament_petg_clear_1000_175_c": "https://prusament.com/materials/",
    "prusament_petg_petgclear_1000_175_c": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR009: dup-cb0fdf124b973d3df47e966aeddee39d13f2b86cb5f0585edfb311f7b1de749e

Status: APPROVED; survivor `prusament_petg_jetblack_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_jetblack_2000_175_p`|`{color_name}`|`Jet Black`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_petgjetblack_2000_175_p`|`PETG {color_name}`|`Jet Black`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_jetblack_2000_175_p": 219.0,
    "prusament_petg_petgjetblack_2000_175_p": 380
  },
  "color_hex": {
    "prusament_petg_jetblack_2000_175_p": "24292A",
    "prusament_petg_petgjetblack_2000_175_p": "292B2B"
  },
  "extruder_temp": {
    "prusament_petg_jetblack_2000_175_p": 250,
    "prusament_petg_petgjetblack_2000_175_p": null
  },
  "bed_temp": {
    "prusament_petg_jetblack_2000_175_p": 90,
    "prusament_petg_petgjetblack_2000_175_p": null
  },
  "tds_url": {
    "prusament_petg_jetblack_2000_175_p": "https://prusament.com/materials/",
    "prusament_petg_petgjetblack_2000_175_p": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR010: dup-ce7c5fa15ee01fa3efce5844745daa249eb3a6467ad614ed6d1d1d9006cece18

Status: APPROVED; survivor `prusament_petg_jetblack_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_jetblack_1000_175_c`|`{color_name}`|`Jet Black`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_petgjetblack_1000_175_c`|`PETG {color_name}`|`Jet Black`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_jetblack_1000_175_c": 193.0,
    "prusament_petg_petgjetblack_1000_175_c": null
  },
  "color_hex": {
    "prusament_petg_jetblack_1000_175_c": "24292A",
    "prusament_petg_petgjetblack_1000_175_c": "292B2B"
  },
  "extruder_temp": {
    "prusament_petg_jetblack_1000_175_c": 250,
    "prusament_petg_petgjetblack_1000_175_c": null
  },
  "bed_temp": {
    "prusament_petg_jetblack_1000_175_c": 90,
    "prusament_petg_petgjetblack_1000_175_c": null
  },
  "tds_url": {
    "prusament_petg_jetblack_1000_175_c": "https://prusament.com/materials/",
    "prusament_petg_petgjetblack_1000_175_c": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR011: dup-783bc2c4116389fe521f1f83ef2dda2fa9aa0234d97cb0fb81c75612df4ce035

Status: APPROVED; survivor `prusament_petg_junglegreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_junglegreen_1000_175_c`|`{color_name}`|`Jungle Green`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_petgjunglegreen_1000_175_c`|`PETG {color_name}`|`Jungle Green`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_junglegreen_1000_175_c": 193.0,
    "prusament_petg_petgjunglegreen_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_petg_junglegreen_1000_175_c": 250,
    "prusament_petg_petgjunglegreen_1000_175_c": null
  },
  "bed_temp": {
    "prusament_petg_junglegreen_1000_175_c": 90,
    "prusament_petg_petgjunglegreen_1000_175_c": null
  },
  "tds_url": {
    "prusament_petg_junglegreen_1000_175_c": "https://prusament.com/materials/",
    "prusament_petg_petgjunglegreen_1000_175_c": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR012: dup-976b89e6cd676ebae2ed6c7d05fe8dd0b3ab06cfb861a8beee07a094ae7ad17e

Status: APPROVED; survivor `prusament_petg_junglegreen_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_junglegreen_2000_175_p`|`{color_name}`|`Jungle Green`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_petgjunglegreen_2000_175_p`|`PETG {color_name}`|`Jungle Green`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_junglegreen_2000_175_p": 219.0,
    "prusament_petg_petgjunglegreen_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_petg_junglegreen_2000_175_p": 250,
    "prusament_petg_petgjunglegreen_2000_175_p": null
  },
  "bed_temp": {
    "prusament_petg_junglegreen_2000_175_p": 90,
    "prusament_petg_petgjunglegreen_2000_175_p": null
  },
  "tds_url": {
    "prusament_petg_junglegreen_2000_175_p": "https://prusament.com/materials/",
    "prusament_petg_petgjunglegreen_2000_175_p": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR013: dup-7d78e6d8e4b540021ee7fd087e4156de1745c47e152fff095f53276cbf99e9d7

Status: APPROVED; survivor `prusament_petg_lipstickred_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_lipstickred_2000_175_p`|`{color_name}`|`Lipstick Red`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_petglipstickred_2000_175_p`|`PETG {color_name}`|`Lipstick Red`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_lipstickred_2000_175_p": 219.0,
    "prusament_petg_petglipstickred_2000_175_p": 380
  },
  "color_hex": {
    "prusament_petg_lipstickred_2000_175_p": "D02F37",
    "prusament_petg_petglipstickred_2000_175_p": "BB2E33"
  },
  "extruder_temp": {
    "prusament_petg_lipstickred_2000_175_p": 250,
    "prusament_petg_petglipstickred_2000_175_p": null
  },
  "bed_temp": {
    "prusament_petg_lipstickred_2000_175_p": 90,
    "prusament_petg_petglipstickred_2000_175_p": null
  },
  "tds_url": {
    "prusament_petg_lipstickred_2000_175_p": "https://prusament.com/materials/",
    "prusament_petg_petglipstickred_2000_175_p": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR014: dup-9f31d53a0668a0fcb8c9114b2d9ebd2c677f8b66f853b703efe019c5bca55c7b

Status: APPROVED; survivor `prusament_petg_lipstickred_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_lipstickred_1000_175_c`|`{color_name}`|`Lipstick Red`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_petglipstickred_1000_175_c`|`PETG {color_name}`|`Lipstick Red`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_lipstickred_1000_175_c": 193.0,
    "prusament_petg_petglipstickred_1000_175_c": null
  },
  "color_hex": {
    "prusament_petg_lipstickred_1000_175_c": "D02F37",
    "prusament_petg_petglipstickred_1000_175_c": "BB2E33"
  },
  "extruder_temp": {
    "prusament_petg_lipstickred_1000_175_c": 250,
    "prusament_petg_petglipstickred_1000_175_c": null
  },
  "bed_temp": {
    "prusament_petg_lipstickred_1000_175_c": 90,
    "prusament_petg_petglipstickred_1000_175_c": null
  },
  "tds_url": {
    "prusament_petg_lipstickred_1000_175_c": "https://prusament.com/materials/",
    "prusament_petg_petglipstickred_1000_175_c": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR015: dup-4e43898c47b27a5e6ebd0ec93bb39fc5331237b36c8fa5d579719dfb2e0ccc9d

Status: APPROVED; survivor `prusament_petg_mangoyellow_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_mangoyellow_1000_175_c`|`{color_name}`|`Mango Yellow`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_petgmangoyellow_1000_175_c`|`PETG {color_name}`|`Mango Yellow`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_mangoyellow_1000_175_c": 193.0,
    "prusament_petg_petgmangoyellow_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_petg_mangoyellow_1000_175_c": 250,
    "prusament_petg_petgmangoyellow_1000_175_c": null
  },
  "bed_temp": {
    "prusament_petg_mangoyellow_1000_175_c": 90,
    "prusament_petg_petgmangoyellow_1000_175_c": null
  },
  "tds_url": {
    "prusament_petg_mangoyellow_1000_175_c": "https://prusament.com/materials/",
    "prusament_petg_petgmangoyellow_1000_175_c": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR016: dup-855cfbd25ea18bbbf8b95cdf5117b635272044d07d52dbb55daa7207e864dc4e

Status: APPROVED; survivor `prusament_petg_mangoyellow_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_mangoyellow_2000_175_p`|`{color_name}`|`Mango Yellow`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_petgmangoyellow_2000_175_p`|`PETG {color_name}`|`Mango Yellow`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_mangoyellow_2000_175_p": 219.0,
    "prusament_petg_petgmangoyellow_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_petg_mangoyellow_2000_175_p": 250,
    "prusament_petg_petgmangoyellow_2000_175_p": null
  },
  "bed_temp": {
    "prusament_petg_mangoyellow_2000_175_p": 90,
    "prusament_petg_petgmangoyellow_2000_175_p": null
  },
  "tds_url": {
    "prusament_petg_mangoyellow_2000_175_p": "https://prusament.com/materials/",
    "prusament_petg_petgmangoyellow_2000_175_p": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR017: dup-d5990b44fc6c4d56820254fd79bcff19e1876b68ae74a3bef6e0f34c0df6f06f

Status: DEFERRED; survivor `prusament_petg_matteblack_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_matteblack_1000_175_c`|`{color_name}`|`Matte Black`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_mattepetgblack_1000_175_c`|`Matte PETG {color_name}`|`Black`|{"source_file": "prusament.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 1, "compiled_records": 1} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "prusament_petg_matteblack_1000_175_c": 1.27,
    "prusament_petg_mattepetgblack_1000_175_c": 1.4
  },
  "spool_weight": {
    "prusament_petg_matteblack_1000_175_c": 193.0,
    "prusament_petg_mattepetgblack_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_petg_matteblack_1000_175_c": 250,
    "prusament_petg_mattepetgblack_1000_175_c": null
  },
  "bed_temp": {
    "prusament_petg_matteblack_1000_175_c": 90,
    "prusament_petg_mattepetgblack_1000_175_c": null
  },
  "tds_url": {
    "prusament_petg_matteblack_1000_175_c": "https://prusament.com/materials/",
    "prusament_petg_mattepetgblack_1000_175_c": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR018: dup-d3ded36b1fde26f96f08fad927a1d9fd4a689881c44f3ff641d1ccad1b957404

Status: APPROVED; survivor `prusament_petg_oceanblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_oceanblue_1000_175_c`|`{color_name}`|`Ocean Blue`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_petgoceanblue_1000_175_c`|`PETG {color_name}`|`Ocean Blue`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_oceanblue_1000_175_c": 193.0,
    "prusament_petg_petgoceanblue_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_petg_oceanblue_1000_175_c": 250,
    "prusament_petg_petgoceanblue_1000_175_c": null
  },
  "bed_temp": {
    "prusament_petg_oceanblue_1000_175_c": 90,
    "prusament_petg_petgoceanblue_1000_175_c": null
  },
  "tds_url": {
    "prusament_petg_oceanblue_1000_175_c": "https://prusament.com/materials/",
    "prusament_petg_petgoceanblue_1000_175_c": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR019: dup-d71e9201730b466b266193573aea5d344d0512ab19cea5c525e5d3c4a09642d1

Status: APPROVED; survivor `prusament_petg_oceanblue_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_oceanblue_2000_175_p`|`{color_name}`|`Ocean Blue`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|
|`prusament_petg_petgoceanblue_2000_175_p`|`PETG {color_name}`|`Ocean Blue`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_oceanblue_2000_175_p": 219.0,
    "prusament_petg_petgoceanblue_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_petg_oceanblue_2000_175_p": 250,
    "prusament_petg_petgoceanblue_2000_175_p": null
  },
  "bed_temp": {
    "prusament_petg_oceanblue_2000_175_p": 90,
    "prusament_petg_petgoceanblue_2000_175_p": null
  },
  "tds_url": {
    "prusament_petg_oceanblue_2000_175_p": "https://prusament.com/materials/",
    "prusament_petg_petgoceanblue_2000_175_p": "https://prusament.com/materials/prusament-petg/"
  }
}
```

### PR020: dup-76f73de234e24c1929c3b2e06364f6d869404df5732a600402bdbade9f690f7d

Status: APPROVED; survivor `prusament_petg_pistachiogreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_petgpistachiogreen_1000_175_c`|`PETG {color_name}`|`Pistachio Green`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|
|`prusament_petg_pistachiogreen_1000_175_c`|`{color_name}`|`Pistachio Green`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_petgpistachiogreen_1000_175_c": null,
    "prusament_petg_pistachiogreen_1000_175_c": 193.0
  },
  "extruder_temp": {
    "prusament_petg_petgpistachiogreen_1000_175_c": null,
    "prusament_petg_pistachiogreen_1000_175_c": 250
  },
  "bed_temp": {
    "prusament_petg_petgpistachiogreen_1000_175_c": null,
    "prusament_petg_pistachiogreen_1000_175_c": 90
  },
  "tds_url": {
    "prusament_petg_petgpistachiogreen_1000_175_c": "https://prusament.com/materials/prusament-petg/",
    "prusament_petg_pistachiogreen_1000_175_c": "https://prusament.com/materials/"
  }
}
```

### PR021: dup-f22f1a37436624dd2c371e16174d923dfd83a0a28c70a3edb5eb0d3fb51e863b

Status: APPROVED; survivor `prusament_petg_pistachiogreen_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_petgpistachiogreen_2000_175_p`|`PETG {color_name}`|`Pistachio Green`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|
|`prusament_petg_pistachiogreen_2000_175_p`|`{color_name}`|`Pistachio Green`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_petgpistachiogreen_2000_175_p": 380,
    "prusament_petg_pistachiogreen_2000_175_p": 219.0
  },
  "extruder_temp": {
    "prusament_petg_petgpistachiogreen_2000_175_p": null,
    "prusament_petg_pistachiogreen_2000_175_p": 250
  },
  "bed_temp": {
    "prusament_petg_petgpistachiogreen_2000_175_p": null,
    "prusament_petg_pistachiogreen_2000_175_p": 90
  },
  "tds_url": {
    "prusament_petg_petgpistachiogreen_2000_175_p": "https://prusament.com/materials/prusament-petg/",
    "prusament_petg_pistachiogreen_2000_175_p": "https://prusament.com/materials/"
  }
}
```

### PR022: dup-62bf17e5a7954e78c13a7cf4247ce1e559c3c845e9d2e0308dfbac786bc909ff

Status: APPROVED; survivor `prusament_petg_prusaorange_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_petgprusaorange_1000_175_c`|`PETG {color_name}`|`Prusa Orange`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|
|`prusament_petg_prusaorange_1000_175_c`|`{color_name}`|`Prusa Orange`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_petgprusaorange_1000_175_c": null,
    "prusament_petg_prusaorange_1000_175_c": 193.0
  },
  "color_hex": {
    "prusament_petg_petgprusaorange_1000_175_c": "EB5405",
    "prusament_petg_prusaorange_1000_175_c": "EA5E1A"
  },
  "extruder_temp": {
    "prusament_petg_petgprusaorange_1000_175_c": null,
    "prusament_petg_prusaorange_1000_175_c": 250
  },
  "bed_temp": {
    "prusament_petg_petgprusaorange_1000_175_c": null,
    "prusament_petg_prusaorange_1000_175_c": 90
  },
  "tds_url": {
    "prusament_petg_petgprusaorange_1000_175_c": "https://prusament.com/materials/prusament-petg/",
    "prusament_petg_prusaorange_1000_175_c": "https://prusament.com/materials/"
  }
}
```

### PR023: dup-94ded62a9e85bb48b107720717e1f63cca9940b7fd761777569d8a54a337688f

Status: APPROVED; survivor `prusament_petg_prusaorange_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_petgprusaorange_2000_175_p`|`PETG {color_name}`|`Prusa Orange`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|
|`prusament_petg_prusaorange_2000_175_p`|`{color_name}`|`Prusa Orange`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_petgprusaorange_2000_175_p": 380,
    "prusament_petg_prusaorange_2000_175_p": 219.0
  },
  "color_hex": {
    "prusament_petg_petgprusaorange_2000_175_p": "EB5405",
    "prusament_petg_prusaorange_2000_175_p": "EA5E1A"
  },
  "extruder_temp": {
    "prusament_petg_petgprusaorange_2000_175_p": null,
    "prusament_petg_prusaorange_2000_175_p": 250
  },
  "bed_temp": {
    "prusament_petg_petgprusaorange_2000_175_p": null,
    "prusament_petg_prusaorange_2000_175_p": 90
  },
  "tds_url": {
    "prusament_petg_petgprusaorange_2000_175_p": "https://prusament.com/materials/prusament-petg/",
    "prusament_petg_prusaorange_2000_175_p": "https://prusament.com/materials/"
  }
}
```

### PR024: dup-2cb49d01ef1a3c4e97f443749bc5ae03cf146150c16d5f6fda0d65a979ebb0c4

Status: APPROVED; survivor `prusament_petg_signalwhite_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_petgsignalwhite_2000_175_p`|`PETG {color_name}`|`Signal White`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|
|`prusament_petg_signalwhite_2000_175_p`|`{color_name}`|`Signal White`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_petgsignalwhite_2000_175_p": 380,
    "prusament_petg_signalwhite_2000_175_p": 219.0
  },
  "color_hex": {
    "prusament_petg_petgsignalwhite_2000_175_p": "E5E0E3",
    "prusament_petg_signalwhite_2000_175_p": "E3DFD9"
  },
  "extruder_temp": {
    "prusament_petg_petgsignalwhite_2000_175_p": null,
    "prusament_petg_signalwhite_2000_175_p": 250
  },
  "bed_temp": {
    "prusament_petg_petgsignalwhite_2000_175_p": null,
    "prusament_petg_signalwhite_2000_175_p": 90
  },
  "tds_url": {
    "prusament_petg_petgsignalwhite_2000_175_p": "https://prusament.com/materials/prusament-petg/",
    "prusament_petg_signalwhite_2000_175_p": "https://prusament.com/materials/"
  }
}
```

### PR025: dup-5ccbea6e52c3fad5e0f2f370ddc178b40c4be3177836ecd6e56b8e3cecf15d72

Status: APPROVED; survivor `prusament_petg_signalwhite_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_petgsignalwhite_1000_175_c`|`PETG {color_name}`|`Signal White`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|
|`prusament_petg_signalwhite_1000_175_c`|`{color_name}`|`Signal White`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_petgsignalwhite_1000_175_c": null,
    "prusament_petg_signalwhite_1000_175_c": 193.0
  },
  "color_hex": {
    "prusament_petg_petgsignalwhite_1000_175_c": "E5E0E3",
    "prusament_petg_signalwhite_1000_175_c": "E3DFD9"
  },
  "extruder_temp": {
    "prusament_petg_petgsignalwhite_1000_175_c": null,
    "prusament_petg_signalwhite_1000_175_c": 250
  },
  "bed_temp": {
    "prusament_petg_petgsignalwhite_1000_175_c": null,
    "prusament_petg_signalwhite_1000_175_c": 90
  },
  "tds_url": {
    "prusament_petg_petgsignalwhite_1000_175_c": "https://prusament.com/materials/prusament-petg/",
    "prusament_petg_signalwhite_1000_175_c": "https://prusament.com/materials/"
  }
}
```

### PR026: dup-022b36599e0cebc79451b25de776d0ace292fe6f9afb140b40411066216d7a1b

Status: APPROVED; survivor `prusament_petg_terracottalight_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_petgterracottalight_1000_175_c`|`PETG {color_name}`|`Terracotta Light`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|
|`prusament_petg_terracottalight_1000_175_c`|`{color_name}`|`Terracotta Light`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_petgterracottalight_1000_175_c": null,
    "prusament_petg_terracottalight_1000_175_c": 193.0
  },
  "extruder_temp": {
    "prusament_petg_petgterracottalight_1000_175_c": null,
    "prusament_petg_terracottalight_1000_175_c": 250
  },
  "bed_temp": {
    "prusament_petg_petgterracottalight_1000_175_c": null,
    "prusament_petg_terracottalight_1000_175_c": 90
  },
  "tds_url": {
    "prusament_petg_petgterracottalight_1000_175_c": "https://prusament.com/materials/prusament-petg/",
    "prusament_petg_terracottalight_1000_175_c": "https://prusament.com/materials/"
  }
}
```

### PR027: dup-1c89904e1e244d6b99a1633f39a15e15d32d30135894e26d86752c77c791dd53

Status: APPROVED; survivor `prusament_petg_terracottalight_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_petgterracottalight_2000_175_p`|`PETG {color_name}`|`Terracotta Light`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|
|`prusament_petg_terracottalight_2000_175_p`|`{color_name}`|`Terracotta Light`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_petgterracottalight_2000_175_p": 380,
    "prusament_petg_terracottalight_2000_175_p": 219.0
  },
  "extruder_temp": {
    "prusament_petg_petgterracottalight_2000_175_p": null,
    "prusament_petg_terracottalight_2000_175_p": 250
  },
  "bed_temp": {
    "prusament_petg_petgterracottalight_2000_175_p": null,
    "prusament_petg_terracottalight_2000_175_p": 90
  },
  "tds_url": {
    "prusament_petg_petgterracottalight_2000_175_p": "https://prusament.com/materials/prusament-petg/",
    "prusament_petg_terracottalight_2000_175_p": "https://prusament.com/materials/"
  }
}
```

### PR028: dup-4e153e28606bb83554d9b06654b2cee049686f64e6807b432753708fbbfffdcf

Status: APPROVED; survivor `prusament_petg_ultramarineblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_petgultramarineblue_1000_175_c`|`PETG {color_name}`|`Ultramarine Blue`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|
|`prusament_petg_ultramarineblue_1000_175_c`|`{color_name}`|`Ultramarine Blue`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_petgultramarineblue_1000_175_c": null,
    "prusament_petg_ultramarineblue_1000_175_c": 193.0
  },
  "extruder_temp": {
    "prusament_petg_petgultramarineblue_1000_175_c": null,
    "prusament_petg_ultramarineblue_1000_175_c": 250
  },
  "bed_temp": {
    "prusament_petg_petgultramarineblue_1000_175_c": null,
    "prusament_petg_ultramarineblue_1000_175_c": 90
  },
  "translucent": {
    "prusament_petg_petgultramarineblue_1000_175_c": true,
    "prusament_petg_ultramarineblue_1000_175_c": false
  },
  "tds_url": {
    "prusament_petg_petgultramarineblue_1000_175_c": "https://prusament.com/materials/prusament-petg/",
    "prusament_petg_ultramarineblue_1000_175_c": "https://prusament.com/materials/"
  }
}
```

### PR029: dup-d4ac927c2cdeea75d60219c83e06b0a701db0015ab2fdffe2971aa131ddfbbf7

Status: APPROVED; survivor `prusament_petg_ultramarineblue_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_petgultramarineblue_2000_175_p`|`PETG {color_name}`|`Ultramarine Blue`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|
|`prusament_petg_ultramarineblue_2000_175_p`|`{color_name}`|`Ultramarine Blue`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_petgultramarineblue_2000_175_p": 380,
    "prusament_petg_ultramarineblue_2000_175_p": 219.0
  },
  "extruder_temp": {
    "prusament_petg_petgultramarineblue_2000_175_p": null,
    "prusament_petg_ultramarineblue_2000_175_p": 250
  },
  "bed_temp": {
    "prusament_petg_petgultramarineblue_2000_175_p": null,
    "prusament_petg_ultramarineblue_2000_175_p": 90
  },
  "translucent": {
    "prusament_petg_petgultramarineblue_2000_175_p": true,
    "prusament_petg_ultramarineblue_2000_175_p": false
  },
  "tds_url": {
    "prusament_petg_petgultramarineblue_2000_175_p": "https://prusament.com/materials/prusament-petg/",
    "prusament_petg_ultramarineblue_2000_175_p": "https://prusament.com/materials/"
  }
}
```

### PR030: dup-248f37831a3f4a6e5840c95d2eefd64108732e58d89858fcbcab19078989001f

Status: APPROVED; survivor `prusament_petg_urbangrey_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_petgurbangrey_1000_175_c`|`PETG {color_name}`|`Urban Grey`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|
|`prusament_petg_urbangrey_1000_175_c`|`{color_name}`|`Urban Grey`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_petgurbangrey_1000_175_c": null,
    "prusament_petg_urbangrey_1000_175_c": 193.0
  },
  "color_hex": {
    "prusament_petg_petgurbangrey_1000_175_c": "95908D",
    "prusament_petg_urbangrey_1000_175_c": "999596"
  },
  "extruder_temp": {
    "prusament_petg_petgurbangrey_1000_175_c": null,
    "prusament_petg_urbangrey_1000_175_c": 250
  },
  "bed_temp": {
    "prusament_petg_petgurbangrey_1000_175_c": null,
    "prusament_petg_urbangrey_1000_175_c": 90
  },
  "tds_url": {
    "prusament_petg_petgurbangrey_1000_175_c": "https://prusament.com/materials/prusament-petg/",
    "prusament_petg_urbangrey_1000_175_c": "https://prusament.com/materials/"
  }
}
```

### PR031: dup-bd7a61ac2b6b79ccf9621c72d6d215cf74d10fc8fb5c553c45bba9fae45fb0ca

Status: APPROVED; survivor `prusament_petg_urbangrey_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_petgurbangrey_2000_175_p`|`PETG {color_name}`|`Urban Grey`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|
|`prusament_petg_urbangrey_2000_175_p`|`{color_name}`|`Urban Grey`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_petgurbangrey_2000_175_p": 380,
    "prusament_petg_urbangrey_2000_175_p": 219.0
  },
  "color_hex": {
    "prusament_petg_petgurbangrey_2000_175_p": "95908D",
    "prusament_petg_urbangrey_2000_175_p": "999596"
  },
  "extruder_temp": {
    "prusament_petg_petgurbangrey_2000_175_p": null,
    "prusament_petg_urbangrey_2000_175_p": 250
  },
  "bed_temp": {
    "prusament_petg_petgurbangrey_2000_175_p": null,
    "prusament_petg_urbangrey_2000_175_p": 90
  },
  "tds_url": {
    "prusament_petg_petgurbangrey_2000_175_p": "https://prusament.com/materials/prusament-petg/",
    "prusament_petg_urbangrey_2000_175_p": "https://prusament.com/materials/"
  }
}
```

### PR032: dup-4d0cf41497802acc902a187044ec0b2c2f9dcfd46596cabf9aa7b4024a417032

Status: APPROVED; survivor `prusament_petg_yellowgold_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_petgyellowgold_1000_175_c`|`PETG {color_name}`|`Yellow Gold`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|
|`prusament_petg_yellowgold_1000_175_c`|`{color_name}`|`Yellow Gold`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_petgyellowgold_1000_175_c": null,
    "prusament_petg_yellowgold_1000_175_c": 193.0
  },
  "extruder_temp": {
    "prusament_petg_petgyellowgold_1000_175_c": null,
    "prusament_petg_yellowgold_1000_175_c": 250
  },
  "bed_temp": {
    "prusament_petg_petgyellowgold_1000_175_c": null,
    "prusament_petg_yellowgold_1000_175_c": 90
  },
  "tds_url": {
    "prusament_petg_petgyellowgold_1000_175_c": "https://prusament.com/materials/prusament-petg/",
    "prusament_petg_yellowgold_1000_175_c": "https://prusament.com/materials/"
  }
}
```

### PR033: dup-7f93534f9a12300863e80ec481a54bd387d3dc7b1459292711e547decacbd58d

Status: APPROVED; survivor `prusament_petg_yellowgold_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_petg_petgyellowgold_2000_175_p`|`PETG {color_name}`|`Yellow Gold`|{"source_file": "prusament.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 29, "compiled_records": 58} / False|
|`prusament_petg_yellowgold_2000_175_p`|`{color_name}`|`Yellow Gold`|{"source_file": "prusament.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_petg_petgyellowgold_2000_175_p": 380,
    "prusament_petg_yellowgold_2000_175_p": 219.0
  },
  "extruder_temp": {
    "prusament_petg_petgyellowgold_2000_175_p": null,
    "prusament_petg_yellowgold_2000_175_p": 250
  },
  "bed_temp": {
    "prusament_petg_petgyellowgold_2000_175_p": null,
    "prusament_petg_yellowgold_2000_175_p": 90
  },
  "tds_url": {
    "prusament_petg_petgyellowgold_2000_175_p": "https://prusament.com/materials/prusament-petg/",
    "prusament_petg_yellowgold_2000_175_p": "https://prusament.com/materials/"
  }
}
```

### PR034: dup-4df65d94c73d8ba4f4ea53a76ed7e95ae920b94d55174ea5781ae64b5b2eaf07

Status: APPROVED; survivor `prusament_pla_armygreen_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_armygreen_2000_175_p`|`{color_name}`|`Army Green`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plaarmygreen_2000_175_p`|`PLA {color_name}`|`Army Green`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_armygreen_2000_175_p": 219.0,
    "prusament_pla_plaarmygreen_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_pla_armygreen_2000_175_p": 215,
    "prusament_pla_plaarmygreen_2000_175_p": null
  },
  "bed_temp": {
    "prusament_pla_armygreen_2000_175_p": 50,
    "prusament_pla_plaarmygreen_2000_175_p": null
  },
  "tds_url": {
    "prusament_pla_armygreen_2000_175_p": "https://prusament.com/materials/",
    "prusament_pla_plaarmygreen_2000_175_p": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR035: dup-94fa61fcb9bd7f8483374d86c63b71e74ba48325e9a07fc692fc7bcec5859b9f

Status: APPROVED; survivor `prusament_pla_armygreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_armygreen_1000_175_c`|`{color_name}`|`Army Green`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plaarmygreen_1000_175_c`|`PLA {color_name}`|`Army Green`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_armygreen_1000_175_c": 193.0,
    "prusament_pla_plaarmygreen_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_pla_armygreen_1000_175_c": 215,
    "prusament_pla_plaarmygreen_1000_175_c": null
  },
  "bed_temp": {
    "prusament_pla_armygreen_1000_175_c": 50,
    "prusament_pla_plaarmygreen_1000_175_c": null
  },
  "tds_url": {
    "prusament_pla_armygreen_1000_175_c": "https://prusament.com/materials/",
    "prusament_pla_plaarmygreen_1000_175_c": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR036: dup-6d5f134620ffd4e15bd55654589e1f5acd8a4dca64dad7bbfcaa6df257c870c8

Status: APPROVED; survivor `prusament_pla_azureblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_azureblue_1000_175_c`|`{color_name}`|`Azure Blue`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plaazureblue_1000_175_c`|`PLA {color_name}`|`Azure Blue`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_azureblue_1000_175_c": 193.0,
    "prusament_pla_plaazureblue_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_pla_azureblue_1000_175_c": 215,
    "prusament_pla_plaazureblue_1000_175_c": null
  },
  "bed_temp": {
    "prusament_pla_azureblue_1000_175_c": 50,
    "prusament_pla_plaazureblue_1000_175_c": null
  },
  "tds_url": {
    "prusament_pla_azureblue_1000_175_c": "https://prusament.com/materials/",
    "prusament_pla_plaazureblue_1000_175_c": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR037: dup-825f78931f509e99db11cccecd7bda49233e88e0c26145fbff40c92936a4f1a3

Status: APPROVED; survivor `prusament_pla_azureblue_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_azureblue_2000_175_p`|`{color_name}`|`Azure Blue`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plaazureblue_2000_175_p`|`PLA {color_name}`|`Azure Blue`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_azureblue_2000_175_p": 219.0,
    "prusament_pla_plaazureblue_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_pla_azureblue_2000_175_p": 215,
    "prusament_pla_plaazureblue_2000_175_p": null
  },
  "bed_temp": {
    "prusament_pla_azureblue_2000_175_p": 50,
    "prusament_pla_plaazureblue_2000_175_p": null
  },
  "tds_url": {
    "prusament_pla_azureblue_2000_175_p": "https://prusament.com/materials/",
    "prusament_pla_plaazureblue_2000_175_p": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR038: dup-ab082ae24687089a8f8a826ac6d54e9745cc910abe9ff3c6b6357098d44c4f8b

Status: APPROVED; survivor `prusament_pla_galaxyblack_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_galaxyblack_2000_175_p`|`{color_name}`|`Galaxy Black`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plagalaxyblack_2000_175_p`|`PLA {color_name}`|`Galaxy Black`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_galaxyblack_2000_175_p": 219.0,
    "prusament_pla_plagalaxyblack_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_pla_galaxyblack_2000_175_p": 215,
    "prusament_pla_plagalaxyblack_2000_175_p": null
  },
  "bed_temp": {
    "prusament_pla_galaxyblack_2000_175_p": 50,
    "prusament_pla_plagalaxyblack_2000_175_p": null
  },
  "tds_url": {
    "prusament_pla_galaxyblack_2000_175_p": "https://prusament.com/materials/",
    "prusament_pla_plagalaxyblack_2000_175_p": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR039: dup-d5fd7632884fc002fc16f38563bb317d2e07af6abbeba6ef7b3be157da883a13

Status: APPROVED; survivor `prusament_pla_galaxyblack_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_galaxyblack_1000_175_c`|`{color_name}`|`Galaxy Black`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plagalaxyblack_1000_175_c`|`PLA {color_name}`|`Galaxy Black`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_galaxyblack_1000_175_c": 193.0,
    "prusament_pla_plagalaxyblack_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_pla_galaxyblack_1000_175_c": 215,
    "prusament_pla_plagalaxyblack_1000_175_c": null
  },
  "bed_temp": {
    "prusament_pla_galaxyblack_1000_175_c": 50,
    "prusament_pla_plagalaxyblack_1000_175_c": null
  },
  "tds_url": {
    "prusament_pla_galaxyblack_1000_175_c": "https://prusament.com/materials/",
    "prusament_pla_plagalaxyblack_1000_175_c": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR040: dup-b34ade5f13139a319b0202dcef9c3ac0b3125096b57859e35c08a754340bdbcb

Status: APPROVED; survivor `prusament_pla_galaxygreen_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_galaxygreen_2000_175_p`|`{color_name}`|`Galaxy Green`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plagalaxygreen_2000_175_p`|`PLA {color_name}`|`Galaxy Green`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_galaxygreen_2000_175_p": 219.0,
    "prusament_pla_plagalaxygreen_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_pla_galaxygreen_2000_175_p": 215,
    "prusament_pla_plagalaxygreen_2000_175_p": null
  },
  "bed_temp": {
    "prusament_pla_galaxygreen_2000_175_p": 50,
    "prusament_pla_plagalaxygreen_2000_175_p": null
  },
  "tds_url": {
    "prusament_pla_galaxygreen_2000_175_p": "https://prusament.com/materials/",
    "prusament_pla_plagalaxygreen_2000_175_p": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR041: dup-d0d534ddf56eeceeedffa01d6e13b68f534a01b2d08bb2c4926644bd8e260cb8

Status: APPROVED; survivor `prusament_pla_galaxygreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_galaxygreen_1000_175_c`|`{color_name}`|`Galaxy Green`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plagalaxygreen_1000_175_c`|`PLA {color_name}`|`Galaxy Green`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_galaxygreen_1000_175_c": 193.0,
    "prusament_pla_plagalaxygreen_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_pla_galaxygreen_1000_175_c": 215,
    "prusament_pla_plagalaxygreen_1000_175_c": null
  },
  "bed_temp": {
    "prusament_pla_galaxygreen_1000_175_c": 50,
    "prusament_pla_plagalaxygreen_1000_175_c": null
  },
  "tds_url": {
    "prusament_pla_galaxygreen_1000_175_c": "https://prusament.com/materials/",
    "prusament_pla_plagalaxygreen_1000_175_c": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR042: dup-98c883aa8b28a2a489ea99050c2304f7653fdc133706c6c1ece22bc6d188aa89

Status: APPROVED; survivor `prusament_pla_galaxypurple_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_galaxypurple_2000_175_p`|`{color_name}`|`Galaxy Purple`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plagalaxypurple_2000_175_p`|`PLA {color_name}`|`Galaxy Purple`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_galaxypurple_2000_175_p": 219.0,
    "prusament_pla_plagalaxypurple_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_pla_galaxypurple_2000_175_p": 215,
    "prusament_pla_plagalaxypurple_2000_175_p": null
  },
  "bed_temp": {
    "prusament_pla_galaxypurple_2000_175_p": 50,
    "prusament_pla_plagalaxypurple_2000_175_p": null
  },
  "tds_url": {
    "prusament_pla_galaxypurple_2000_175_p": "https://prusament.com/materials/",
    "prusament_pla_plagalaxypurple_2000_175_p": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR043: dup-d00af3d8fd6e686f51523c8ae4e72f096ad82334698c186fce1b250282d809d4

Status: APPROVED; survivor `prusament_pla_galaxypurple_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_galaxypurple_1000_175_c`|`{color_name}`|`Galaxy Purple`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plagalaxypurple_1000_175_c`|`PLA {color_name}`|`Galaxy Purple`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_galaxypurple_1000_175_c": 193.0,
    "prusament_pla_plagalaxypurple_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_pla_galaxypurple_1000_175_c": 215,
    "prusament_pla_plagalaxypurple_1000_175_c": null
  },
  "bed_temp": {
    "prusament_pla_galaxypurple_1000_175_c": 50,
    "prusament_pla_plagalaxypurple_1000_175_c": null
  },
  "tds_url": {
    "prusament_pla_galaxypurple_1000_175_c": "https://prusament.com/materials/",
    "prusament_pla_plagalaxypurple_1000_175_c": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR044: dup-4748cc8d00d305b480d4c1fa956ec244391e599da0f6a88eae3fa02a382e1d42

Status: APPROVED; survivor `prusament_pla_galaxyred_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_galaxyred_2000_175_p`|`{color_name}`|`Galaxy Red`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plagalaxyred_2000_175_p`|`PLA {color_name}`|`Galaxy Red`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_galaxyred_2000_175_p": 219.0,
    "prusament_pla_plagalaxyred_2000_175_p": 380
  },
  "color_hex": {
    "prusament_pla_galaxyred_2000_175_p": "D94A5A",
    "prusament_pla_plagalaxyred_2000_175_p": "B13941"
  },
  "extruder_temp": {
    "prusament_pla_galaxyred_2000_175_p": 215,
    "prusament_pla_plagalaxyred_2000_175_p": null
  },
  "bed_temp": {
    "prusament_pla_galaxyred_2000_175_p": 50,
    "prusament_pla_plagalaxyred_2000_175_p": null
  },
  "tds_url": {
    "prusament_pla_galaxyred_2000_175_p": "https://prusament.com/materials/",
    "prusament_pla_plagalaxyred_2000_175_p": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR045: dup-e653023d6d7cb6131b1fa8d43f964f67985f689832b92eb70b9f9fb580e43cf2

Status: APPROVED; survivor `prusament_pla_galaxyred_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_galaxyred_1000_175_c`|`{color_name}`|`Galaxy Red`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plagalaxyred_1000_175_c`|`PLA {color_name}`|`Galaxy Red`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_galaxyred_1000_175_c": 193.0,
    "prusament_pla_plagalaxyred_1000_175_c": null
  },
  "color_hex": {
    "prusament_pla_galaxyred_1000_175_c": "D94A5A",
    "prusament_pla_plagalaxyred_1000_175_c": "B13941"
  },
  "extruder_temp": {
    "prusament_pla_galaxyred_1000_175_c": 215,
    "prusament_pla_plagalaxyred_1000_175_c": null
  },
  "bed_temp": {
    "prusament_pla_galaxyred_1000_175_c": 50,
    "prusament_pla_plagalaxyred_1000_175_c": null
  },
  "tds_url": {
    "prusament_pla_galaxyred_1000_175_c": "https://prusament.com/materials/",
    "prusament_pla_plagalaxyred_1000_175_c": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR046: dup-a7414d2ebbe0f32a2caf28945771339567b2461e84e2aaee16996f193f889191

Status: APPROVED; survivor `prusament_pla_galaxysilver_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_galaxysilver_2000_175_p`|`{color_name}`|`Galaxy Silver`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plagalaxysilver_2000_175_p`|`PLA {color_name}`|`Galaxy Silver`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_galaxysilver_2000_175_p": 219.0,
    "prusament_pla_plagalaxysilver_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_pla_galaxysilver_2000_175_p": 215,
    "prusament_pla_plagalaxysilver_2000_175_p": null
  },
  "bed_temp": {
    "prusament_pla_galaxysilver_2000_175_p": 50,
    "prusament_pla_plagalaxysilver_2000_175_p": null
  },
  "tds_url": {
    "prusament_pla_galaxysilver_2000_175_p": "https://prusament.com/materials/",
    "prusament_pla_plagalaxysilver_2000_175_p": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR047: dup-ab16e52f6823725ceb6ff391f6254a9e84612bfac10681904f2203bf155ffcde

Status: APPROVED; survivor `prusament_pla_galaxysilver_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_galaxysilver_1000_175_c`|`{color_name}`|`Galaxy Silver`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plagalaxysilver_1000_175_c`|`PLA {color_name}`|`Galaxy Silver`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_galaxysilver_1000_175_c": 193.0,
    "prusament_pla_plagalaxysilver_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_pla_galaxysilver_1000_175_c": 215,
    "prusament_pla_plagalaxysilver_1000_175_c": null
  },
  "bed_temp": {
    "prusament_pla_galaxysilver_1000_175_c": 50,
    "prusament_pla_plagalaxysilver_1000_175_c": null
  },
  "tds_url": {
    "prusament_pla_galaxysilver_1000_175_c": "https://prusament.com/materials/",
    "prusament_pla_plagalaxysilver_1000_175_c": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR048: dup-50bd237d5ce14263dc2cba99901b1b7bc2f8b52fd3c8fa566df2bc5ebeeca2ee

Status: APPROVED; survivor `prusament_pla_gentleman'sgrey_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_gentleman'sgrey_1000_175_c`|`{color_name}`|`Gentleman's Grey`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plagentleman'sgrey_1000_175_c`|`PLA {color_name}`|`Gentleman's Grey`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_gentleman'sgrey_1000_175_c": 193.0,
    "prusament_pla_plagentleman'sgrey_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_pla_gentleman'sgrey_1000_175_c": 215,
    "prusament_pla_plagentleman'sgrey_1000_175_c": null
  },
  "bed_temp": {
    "prusament_pla_gentleman'sgrey_1000_175_c": 50,
    "prusament_pla_plagentleman'sgrey_1000_175_c": null
  },
  "tds_url": {
    "prusament_pla_gentleman'sgrey_1000_175_c": "https://prusament.com/materials/",
    "prusament_pla_plagentleman'sgrey_1000_175_c": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR049: dup-e2dfc1a102d9204d5e434f096de300a5aee82828e85e21f0e0376fe5c5e8b0bb

Status: APPROVED; survivor `prusament_pla_gentleman'sgrey_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_gentleman'sgrey_2000_175_p`|`{color_name}`|`Gentleman's Grey`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plagentleman'sgrey_2000_175_p`|`PLA {color_name}`|`Gentleman's Grey`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_gentleman'sgrey_2000_175_p": 219.0,
    "prusament_pla_plagentleman'sgrey_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_pla_gentleman'sgrey_2000_175_p": 215,
    "prusament_pla_plagentleman'sgrey_2000_175_p": null
  },
  "bed_temp": {
    "prusament_pla_gentleman'sgrey_2000_175_p": 50,
    "prusament_pla_plagentleman'sgrey_2000_175_p": null
  },
  "tds_url": {
    "prusament_pla_gentleman'sgrey_2000_175_p": "https://prusament.com/materials/",
    "prusament_pla_plagentleman'sgrey_2000_175_p": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR050: dup-b54fe87d58cb473baf64c3ae8627a77617fa3ac8022b1cd405431354df491c10

Status: APPROVED; survivor `prusament_pla_gravitygrey_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_gravitygrey_2000_175_p`|`{color_name}`|`Gravity Grey`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plagravitygrey_2000_175_p`|`PLA {color_name}`|`Gravity Grey`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_gravitygrey_2000_175_p": 219.0,
    "prusament_pla_plagravitygrey_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_pla_gravitygrey_2000_175_p": 215,
    "prusament_pla_plagravitygrey_2000_175_p": null
  },
  "bed_temp": {
    "prusament_pla_gravitygrey_2000_175_p": 50,
    "prusament_pla_plagravitygrey_2000_175_p": null
  },
  "tds_url": {
    "prusament_pla_gravitygrey_2000_175_p": "https://prusament.com/materials/",
    "prusament_pla_plagravitygrey_2000_175_p": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR051: dup-f2b2e9f6ac2361cde51f94e01b80840661f80a37be75e33b26d173e12be63104

Status: APPROVED; survivor `prusament_pla_gravitygrey_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_gravitygrey_1000_175_c`|`{color_name}`|`Gravity Grey`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plagravitygrey_1000_175_c`|`PLA {color_name}`|`Gravity Grey`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_gravitygrey_1000_175_c": 193.0,
    "prusament_pla_plagravitygrey_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_pla_gravitygrey_1000_175_c": 215,
    "prusament_pla_plagravitygrey_1000_175_c": null
  },
  "bed_temp": {
    "prusament_pla_gravitygrey_1000_175_c": 50,
    "prusament_pla_plagravitygrey_1000_175_c": null
  },
  "tds_url": {
    "prusament_pla_gravitygrey_1000_175_c": "https://prusament.com/materials/",
    "prusament_pla_plagravitygrey_1000_175_c": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR052: dup-4fca921297018a97d34c4f464d5e5a7e43f9d263fa5057f24f535d95c6e8dec8

Status: APPROVED; survivor `prusament_pla_jetblack_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_jetblack_1000_175_c`|`{color_name}`|`Jet Black`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plajetblack_1000_175_c`|`PLA {color_name}`|`Jet Black`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_jetblack_1000_175_c": 193.0,
    "prusament_pla_plajetblack_1000_175_c": null
  },
  "color_hex": {
    "prusament_pla_jetblack_1000_175_c": "24292A",
    "prusament_pla_plajetblack_1000_175_c": "393C3C"
  },
  "extruder_temp": {
    "prusament_pla_jetblack_1000_175_c": 215,
    "prusament_pla_plajetblack_1000_175_c": null
  },
  "bed_temp": {
    "prusament_pla_jetblack_1000_175_c": 50,
    "prusament_pla_plajetblack_1000_175_c": null
  },
  "tds_url": {
    "prusament_pla_jetblack_1000_175_c": "https://prusament.com/materials/",
    "prusament_pla_plajetblack_1000_175_c": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR053: dup-943a23598f207a465c2e8e7b6d0177799c58c069408acacf5f455341cf844fa9

Status: APPROVED; survivor `prusament_pla_jetblack_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_jetblack_2000_175_p`|`{color_name}`|`Jet Black`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plajetblack_2000_175_p`|`PLA {color_name}`|`Jet Black`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_jetblack_2000_175_p": 219.0,
    "prusament_pla_plajetblack_2000_175_p": 380
  },
  "color_hex": {
    "prusament_pla_jetblack_2000_175_p": "24292A",
    "prusament_pla_plajetblack_2000_175_p": "393C3C"
  },
  "extruder_temp": {
    "prusament_pla_jetblack_2000_175_p": 215,
    "prusament_pla_plajetblack_2000_175_p": null
  },
  "bed_temp": {
    "prusament_pla_jetblack_2000_175_p": 50,
    "prusament_pla_plajetblack_2000_175_p": null
  },
  "tds_url": {
    "prusament_pla_jetblack_2000_175_p": "https://prusament.com/materials/",
    "prusament_pla_plajetblack_2000_175_p": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR054: dup-39874c7d66017b60c6373ea9eb4c280d39b400a0eff16314483c4bf3dbfb69b1

Status: APPROVED; survivor `prusament_pla_lipstickred_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_lipstickred_2000_175_p`|`{color_name}`|`Lipstick Red`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plalipstickred_2000_175_p`|`PLA {color_name}`|`Lipstick Red`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_lipstickred_2000_175_p": 219.0,
    "prusament_pla_plalipstickred_2000_175_p": 380
  },
  "color_hex": {
    "prusament_pla_lipstickred_2000_175_p": "D02F37",
    "prusament_pla_plalipstickred_2000_175_p": "BF2B2B"
  },
  "extruder_temp": {
    "prusament_pla_lipstickred_2000_175_p": 215,
    "prusament_pla_plalipstickred_2000_175_p": null
  },
  "bed_temp": {
    "prusament_pla_lipstickred_2000_175_p": 50,
    "prusament_pla_plalipstickred_2000_175_p": null
  },
  "tds_url": {
    "prusament_pla_lipstickred_2000_175_p": "https://prusament.com/materials/",
    "prusament_pla_plalipstickred_2000_175_p": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR055: dup-de770c2e50cd11f0088e1d1cba33160d327296b6b21fd6205acd06b1548d5378

Status: APPROVED; survivor `prusament_pla_lipstickred_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_lipstickred_1000_175_c`|`{color_name}`|`Lipstick Red`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plalipstickred_1000_175_c`|`PLA {color_name}`|`Lipstick Red`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_lipstickred_1000_175_c": 193.0,
    "prusament_pla_plalipstickred_1000_175_c": null
  },
  "color_hex": {
    "prusament_pla_lipstickred_1000_175_c": "D02F37",
    "prusament_pla_plalipstickred_1000_175_c": "BF2B2B"
  },
  "extruder_temp": {
    "prusament_pla_lipstickred_1000_175_c": 215,
    "prusament_pla_plalipstickred_1000_175_c": null
  },
  "bed_temp": {
    "prusament_pla_lipstickred_1000_175_c": 50,
    "prusament_pla_plalipstickred_1000_175_c": null
  },
  "tds_url": {
    "prusament_pla_lipstickred_1000_175_c": "https://prusament.com/materials/",
    "prusament_pla_plalipstickred_1000_175_c": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR056: dup-29bb3f4df262be621d2ae9ddebb8a188bf9d14c8a0577c03af776ec4d10a8b56

Status: APPROVED; survivor `prusament_pla_marblegrey_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_marblegrey_2000_175_p`|`{color_name}`|`Marble Grey`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plamarblegrey_2000_175_p`|`PLA {color_name}`|`Marble Grey`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_marblegrey_2000_175_p": 219.0,
    "prusament_pla_plamarblegrey_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_pla_marblegrey_2000_175_p": 215,
    "prusament_pla_plamarblegrey_2000_175_p": null
  },
  "bed_temp": {
    "prusament_pla_marblegrey_2000_175_p": 50,
    "prusament_pla_plamarblegrey_2000_175_p": null
  },
  "tds_url": {
    "prusament_pla_marblegrey_2000_175_p": "https://prusament.com/materials/",
    "prusament_pla_plamarblegrey_2000_175_p": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR057: dup-7d44ec6eefe21e5ec74749ab5496704cca487795a14c20fe39db7d4e7b8ac1a0

Status: APPROVED; survivor `prusament_pla_marblegrey_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_marblegrey_1000_175_c`|`{color_name}`|`Marble Grey`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plamarblegrey_1000_175_c`|`PLA {color_name}`|`Marble Grey`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_marblegrey_1000_175_c": 193.0,
    "prusament_pla_plamarblegrey_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_pla_marblegrey_1000_175_c": 215,
    "prusament_pla_plamarblegrey_1000_175_c": null
  },
  "bed_temp": {
    "prusament_pla_marblegrey_1000_175_c": 50,
    "prusament_pla_plamarblegrey_1000_175_c": null
  },
  "tds_url": {
    "prusament_pla_marblegrey_1000_175_c": "https://prusament.com/materials/",
    "prusament_pla_plamarblegrey_1000_175_c": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR058: dup-50cf5bd977c62d280f6e692d37ba87db5ed16a5692648c623a7c76a6aba3b3a2

Status: APPROVED; survivor `prusament_pla_ms.pink_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_ms.pink_1000_175_c`|`{color_name}`|`Ms. Pink`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plams.pink_1000_175_c`|`PLA {color_name}`|`Ms. Pink`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_ms.pink_1000_175_c": 193.0,
    "prusament_pla_plams.pink_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_pla_ms.pink_1000_175_c": 215,
    "prusament_pla_plams.pink_1000_175_c": null
  },
  "bed_temp": {
    "prusament_pla_ms.pink_1000_175_c": 50,
    "prusament_pla_plams.pink_1000_175_c": null
  },
  "tds_url": {
    "prusament_pla_ms.pink_1000_175_c": "https://prusament.com/materials/",
    "prusament_pla_plams.pink_1000_175_c": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR059: dup-b0abfff77667f184a8213f3f0e3d547f24e796f1114cfa70ccf2e38a387d212c

Status: APPROVED; survivor `prusament_pla_ms.pink_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_ms.pink_2000_175_p`|`{color_name}`|`Ms. Pink`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plams.pink_2000_175_p`|`PLA {color_name}`|`Ms. Pink`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_ms.pink_2000_175_p": 219.0,
    "prusament_pla_plams.pink_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_pla_ms.pink_2000_175_p": 215,
    "prusament_pla_plams.pink_2000_175_p": null
  },
  "bed_temp": {
    "prusament_pla_ms.pink_2000_175_p": 50,
    "prusament_pla_plams.pink_2000_175_p": null
  },
  "tds_url": {
    "prusament_pla_ms.pink_2000_175_p": "https://prusament.com/materials/",
    "prusament_pla_plams.pink_2000_175_p": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR060: dup-0ed616418f05205219a50efa7a7e913489b823d07a79f12c90182df3b1582dc4

Status: APPROVED; survivor `prusament_pla_natural_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_natural_2000_175_p`|`{color_name}`|`Natural`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_planatural_2000_175_p`|`PLA {color_name}`|`Natural`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_natural_2000_175_p": 219.0,
    "prusament_pla_planatural_2000_175_p": 380
  },
  "color_hex": {
    "prusament_pla_natural_2000_175_p": "DFDFD3",
    "prusament_pla_planatural_2000_175_p": "DEE2DA"
  },
  "extruder_temp": {
    "prusament_pla_natural_2000_175_p": 215,
    "prusament_pla_planatural_2000_175_p": null
  },
  "bed_temp": {
    "prusament_pla_natural_2000_175_p": 50,
    "prusament_pla_planatural_2000_175_p": null
  },
  "tds_url": {
    "prusament_pla_natural_2000_175_p": "https://prusament.com/materials/",
    "prusament_pla_planatural_2000_175_p": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR061: dup-34c33f2b7d6e4720c752cebacdffb2c1824fcbe33dffeb2c566fb589dcb124e6

Status: APPROVED; survivor `prusament_pla_natural_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_natural_1000_175_c`|`{color_name}`|`Natural`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_planatural_1000_175_c`|`PLA {color_name}`|`Natural`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_natural_1000_175_c": 193.0,
    "prusament_pla_planatural_1000_175_c": null
  },
  "color_hex": {
    "prusament_pla_natural_1000_175_c": "DFDFD3",
    "prusament_pla_planatural_1000_175_c": "DEE2DA"
  },
  "extruder_temp": {
    "prusament_pla_natural_1000_175_c": 215,
    "prusament_pla_planatural_1000_175_c": null
  },
  "bed_temp": {
    "prusament_pla_natural_1000_175_c": 50,
    "prusament_pla_planatural_1000_175_c": null
  },
  "tds_url": {
    "prusament_pla_natural_1000_175_c": "https://prusament.com/materials/",
    "prusament_pla_planatural_1000_175_c": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR062: dup-64221a7f693529def59b104638d41252fa90a27a49f6e392bd7c8942d940a04f

Status: APPROVED; survivor `prusament_pla_opalgreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_opalgreen_1000_175_c`|`{color_name}`|`Opal Green`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plaopalgreen_1000_175_c`|`PLA {color_name}`|`Opal Green`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_opalgreen_1000_175_c": 193.0,
    "prusament_pla_plaopalgreen_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_pla_opalgreen_1000_175_c": 215,
    "prusament_pla_plaopalgreen_1000_175_c": null
  },
  "bed_temp": {
    "prusament_pla_opalgreen_1000_175_c": 50,
    "prusament_pla_plaopalgreen_1000_175_c": null
  },
  "tds_url": {
    "prusament_pla_opalgreen_1000_175_c": "https://prusament.com/materials/",
    "prusament_pla_plaopalgreen_1000_175_c": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR063: dup-8e7b69d0a3746e20cf4363b6cd6f7885cb47bdfe00c5d9ced5595dbed2bc6679

Status: APPROVED; survivor `prusament_pla_opalgreen_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_opalgreen_2000_175_p`|`{color_name}`|`Opal Green`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plaopalgreen_2000_175_p`|`PLA {color_name}`|`Opal Green`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_opalgreen_2000_175_p": 219.0,
    "prusament_pla_plaopalgreen_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_pla_opalgreen_2000_175_p": 215,
    "prusament_pla_plaopalgreen_2000_175_p": null
  },
  "bed_temp": {
    "prusament_pla_opalgreen_2000_175_p": 50,
    "prusament_pla_plaopalgreen_2000_175_p": null
  },
  "tds_url": {
    "prusament_pla_opalgreen_2000_175_p": "https://prusament.com/materials/",
    "prusament_pla_plaopalgreen_2000_175_p": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR064: dup-7a27d8d492673c67f24ac4dc85bf047d459b19d55a7fd9fb8b903c03c1bbfdca

Status: APPROVED; survivor `prusament_pla_pearlmouse_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_pearlmouse_2000_175_p`|`{color_name}`|`Pearl Mouse`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plapearlmouse_2000_175_p`|`PLA {color_name}`|`Pearl Mouse`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_pearlmouse_2000_175_p": 219.0,
    "prusament_pla_plapearlmouse_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_pla_pearlmouse_2000_175_p": 215,
    "prusament_pla_plapearlmouse_2000_175_p": null
  },
  "bed_temp": {
    "prusament_pla_pearlmouse_2000_175_p": 50,
    "prusament_pla_plapearlmouse_2000_175_p": null
  },
  "tds_url": {
    "prusament_pla_pearlmouse_2000_175_p": "https://prusament.com/materials/",
    "prusament_pla_plapearlmouse_2000_175_p": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR065: dup-8d8e7ba0a234a942eb7bde7ace7d52d0498da29e23756b7b6a4d6dbb68743b34

Status: APPROVED; survivor `prusament_pla_pearlmouse_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_pearlmouse_1000_175_c`|`{color_name}`|`Pearl Mouse`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plapearlmouse_1000_175_c`|`PLA {color_name}`|`Pearl Mouse`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_pearlmouse_1000_175_c": 193.0,
    "prusament_pla_plapearlmouse_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_pla_pearlmouse_1000_175_c": 215,
    "prusament_pla_plapearlmouse_1000_175_c": null
  },
  "bed_temp": {
    "prusament_pla_pearlmouse_1000_175_c": 50,
    "prusament_pla_plapearlmouse_1000_175_c": null
  },
  "tds_url": {
    "prusament_pla_pearlmouse_1000_175_c": "https://prusament.com/materials/",
    "prusament_pla_plapearlmouse_1000_175_c": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR066: dup-2dffef4cb56071858ed27cc076c7c789eb5d75c7c007b1f3df9073db421df02a

Status: APPROVED; survivor `prusament_pla_pineappleyellow_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_pineappleyellow_2000_175_p`|`{color_name}`|`Pineapple Yellow`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plapineappleyellow_2000_175_p`|`PLA {color_name}`|`Pineapple Yellow`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_pineappleyellow_2000_175_p": 219.0,
    "prusament_pla_plapineappleyellow_2000_175_p": 380
  },
  "extruder_temp": {
    "prusament_pla_pineappleyellow_2000_175_p": 215,
    "prusament_pla_plapineappleyellow_2000_175_p": null
  },
  "bed_temp": {
    "prusament_pla_pineappleyellow_2000_175_p": 50,
    "prusament_pla_plapineappleyellow_2000_175_p": null
  },
  "tds_url": {
    "prusament_pla_pineappleyellow_2000_175_p": "https://prusament.com/materials/",
    "prusament_pla_plapineappleyellow_2000_175_p": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR067: dup-5c8c314092f5a28fdf4e14458dee81ef91c734ccbe61467ebbc3b839424c4360

Status: APPROVED; survivor `prusament_pla_pineappleyellow_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_pineappleyellow_1000_175_c`|`{color_name}`|`Pineapple Yellow`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|
|`prusament_pla_plapineappleyellow_1000_175_c`|`PLA {color_name}`|`Pineapple Yellow`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_pineappleyellow_1000_175_c": 193.0,
    "prusament_pla_plapineappleyellow_1000_175_c": null
  },
  "extruder_temp": {
    "prusament_pla_pineappleyellow_1000_175_c": 215,
    "prusament_pla_plapineappleyellow_1000_175_c": null
  },
  "bed_temp": {
    "prusament_pla_pineappleyellow_1000_175_c": 50,
    "prusament_pla_plapineappleyellow_1000_175_c": null
  },
  "tds_url": {
    "prusament_pla_pineappleyellow_1000_175_c": "https://prusament.com/materials/",
    "prusament_pla_plapineappleyellow_1000_175_c": "https://prusament.com/materials/prusament-pla/"
  }
}
```

### PR068: dup-15869a6472bc386168b596de611406b258ee2ad211c61d814bdc4e93d544e3ef

Status: APPROVED; survivor `prusament_pla_pristinewhite_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_plapristinewhite_2000_175_p`|`PLA {color_name}`|`Pristine White`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|
|`prusament_pla_pristinewhite_2000_175_p`|`{color_name}`|`Pristine White`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_plapristinewhite_2000_175_p": 380,
    "prusament_pla_pristinewhite_2000_175_p": 219.0
  },
  "extruder_temp": {
    "prusament_pla_plapristinewhite_2000_175_p": null,
    "prusament_pla_pristinewhite_2000_175_p": 215
  },
  "bed_temp": {
    "prusament_pla_plapristinewhite_2000_175_p": null,
    "prusament_pla_pristinewhite_2000_175_p": 50
  },
  "tds_url": {
    "prusament_pla_plapristinewhite_2000_175_p": "https://prusament.com/materials/prusament-pla/",
    "prusament_pla_pristinewhite_2000_175_p": "https://prusament.com/materials/"
  }
}
```

### PR069: dup-62636ff72c314ed908e46319481ae1a738016069a366dc2c0e8005f50c00ff1e

Status: APPROVED; survivor `prusament_pla_pristinewhite_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_plapristinewhite_1000_175_c`|`PLA {color_name}`|`Pristine White`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|
|`prusament_pla_pristinewhite_1000_175_c`|`{color_name}`|`Pristine White`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_plapristinewhite_1000_175_c": null,
    "prusament_pla_pristinewhite_1000_175_c": 193.0
  },
  "extruder_temp": {
    "prusament_pla_plapristinewhite_1000_175_c": null,
    "prusament_pla_pristinewhite_1000_175_c": 215
  },
  "bed_temp": {
    "prusament_pla_plapristinewhite_1000_175_c": null,
    "prusament_pla_pristinewhite_1000_175_c": 50
  },
  "tds_url": {
    "prusament_pla_plapristinewhite_1000_175_c": "https://prusament.com/materials/prusament-pla/",
    "prusament_pla_pristinewhite_1000_175_c": "https://prusament.com/materials/"
  }
}
```

### PR070: dup-3f05d6440b9855d1776a200fa39cdf4810e8d61ac8d78bc4933c981b3156057c

Status: APPROVED; survivor `prusament_pla_prusaorange_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_plaprusaorange_1000_175_c`|`PLA {color_name}`|`Prusa Orange`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|
|`prusament_pla_prusaorange_1000_175_c`|`{color_name}`|`Prusa Orange`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_plaprusaorange_1000_175_c": null,
    "prusament_pla_prusaorange_1000_175_c": 193.0
  },
  "color_hex": {
    "prusament_pla_plaprusaorange_1000_175_c": "FE6E32",
    "prusament_pla_prusaorange_1000_175_c": "EA5E1A"
  },
  "extruder_temp": {
    "prusament_pla_plaprusaorange_1000_175_c": null,
    "prusament_pla_prusaorange_1000_175_c": 215
  },
  "bed_temp": {
    "prusament_pla_plaprusaorange_1000_175_c": null,
    "prusament_pla_prusaorange_1000_175_c": 50
  },
  "tds_url": {
    "prusament_pla_plaprusaorange_1000_175_c": "https://prusament.com/materials/prusament-pla/",
    "prusament_pla_prusaorange_1000_175_c": "https://prusament.com/materials/"
  }
}
```

### PR071: dup-b2d370775a95457bd39cfb6aa3780bf265f779fef3ef1bff505843daab2de690

Status: APPROVED; survivor `prusament_pla_prusaorange_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_plaprusaorange_2000_175_p`|`PLA {color_name}`|`Prusa Orange`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|
|`prusament_pla_prusaorange_2000_175_p`|`{color_name}`|`Prusa Orange`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_plaprusaorange_2000_175_p": 380,
    "prusament_pla_prusaorange_2000_175_p": 219.0
  },
  "color_hex": {
    "prusament_pla_plaprusaorange_2000_175_p": "FE6E32",
    "prusament_pla_prusaorange_2000_175_p": "EA5E1A"
  },
  "extruder_temp": {
    "prusament_pla_plaprusaorange_2000_175_p": null,
    "prusament_pla_prusaorange_2000_175_p": 215
  },
  "bed_temp": {
    "prusament_pla_plaprusaorange_2000_175_p": null,
    "prusament_pla_prusaorange_2000_175_p": 50
  },
  "tds_url": {
    "prusament_pla_plaprusaorange_2000_175_p": "https://prusament.com/materials/prusament-pla/",
    "prusament_pla_prusaorange_2000_175_p": "https://prusament.com/materials/"
  }
}
```

### PR072: dup-1ec793b0e0f5a974151cde1cb6cd5e2c5384a8d71464859c7aaf3fb7649ee8e6

Status: APPROVED; survivor `prusament_pla_simplygreen_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_plasimplygreen_2000_175_p`|`PLA {color_name}`|`Simply Green`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|
|`prusament_pla_simplygreen_2000_175_p`|`{color_name}`|`Simply Green`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_plasimplygreen_2000_175_p": 380,
    "prusament_pla_simplygreen_2000_175_p": 219.0
  },
  "extruder_temp": {
    "prusament_pla_plasimplygreen_2000_175_p": null,
    "prusament_pla_simplygreen_2000_175_p": 215
  },
  "bed_temp": {
    "prusament_pla_plasimplygreen_2000_175_p": null,
    "prusament_pla_simplygreen_2000_175_p": 50
  },
  "tds_url": {
    "prusament_pla_plasimplygreen_2000_175_p": "https://prusament.com/materials/prusament-pla/",
    "prusament_pla_simplygreen_2000_175_p": "https://prusament.com/materials/"
  }
}
```

### PR073: dup-e9e1e73da421a4a2f95b830911608b2f44bec44dab8f1140078a8b3636160a04

Status: APPROVED; survivor `prusament_pla_simplygreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_plasimplygreen_1000_175_c`|`PLA {color_name}`|`Simply Green`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|
|`prusament_pla_simplygreen_1000_175_c`|`{color_name}`|`Simply Green`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_plasimplygreen_1000_175_c": null,
    "prusament_pla_simplygreen_1000_175_c": 193.0
  },
  "extruder_temp": {
    "prusament_pla_plasimplygreen_1000_175_c": null,
    "prusament_pla_simplygreen_1000_175_c": 215
  },
  "bed_temp": {
    "prusament_pla_plasimplygreen_1000_175_c": null,
    "prusament_pla_simplygreen_1000_175_c": 50
  },
  "tds_url": {
    "prusament_pla_plasimplygreen_1000_175_c": "https://prusament.com/materials/prusament-pla/",
    "prusament_pla_simplygreen_1000_175_c": "https://prusament.com/materials/"
  }
}
```

### PR074: dup-a807a4e43a21e63dc7707a52f51917a14980f01b828bba038fb86d66be134034

Status: APPROVED; survivor `prusament_pla_vanillawhite_2000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_plavanillawhite_2000_175_p`|`PLA {color_name}`|`Vanilla White`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|
|`prusament_pla_vanillawhite_2000_175_p`|`{color_name}`|`Vanilla White`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_plavanillawhite_2000_175_p": 380,
    "prusament_pla_vanillawhite_2000_175_p": 219.0
  },
  "extruder_temp": {
    "prusament_pla_plavanillawhite_2000_175_p": null,
    "prusament_pla_vanillawhite_2000_175_p": 215
  },
  "bed_temp": {
    "prusament_pla_plavanillawhite_2000_175_p": null,
    "prusament_pla_vanillawhite_2000_175_p": 50
  },
  "tds_url": {
    "prusament_pla_plavanillawhite_2000_175_p": "https://prusament.com/materials/prusament-pla/",
    "prusament_pla_vanillawhite_2000_175_p": "https://prusament.com/materials/"
  }
}
```

### PR075: dup-adac827600373301c2cae03ffe083486d849ad6ad8afd2c9111a62e869170c48

Status: APPROVED; survivor `prusament_pla_vanillawhite_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`prusament_pla_plavanillawhite_1000_175_c`|`PLA {color_name}`|`Vanilla White`|{"source_file": "prusament.json", "definition_index": 20, "weights": 3, "diameters": 1, "colors": 44, "compiled_records": 132} / False|
|`prusament_pla_vanillawhite_1000_175_c`|`{color_name}`|`Vanilla White`|{"source_file": "prusament.json", "definition_index": 7, "weights": 2, "diameters": 1, "colors": 21, "compiled_records": 42} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "prusament_pla_plavanillawhite_1000_175_c": null,
    "prusament_pla_vanillawhite_1000_175_c": 193.0
  },
  "extruder_temp": {
    "prusament_pla_plavanillawhite_1000_175_c": null,
    "prusament_pla_vanillawhite_1000_175_c": 215
  },
  "bed_temp": {
    "prusament_pla_plavanillawhite_1000_175_c": null,
    "prusament_pla_vanillawhite_1000_175_c": 50
  },
  "tds_url": {
    "prusament_pla_plavanillawhite_1000_175_c": "https://prusament.com/materials/prusament-pla/",
    "prusament_pla_vanillawhite_1000_175_c": "https://prusament.com/materials/"
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "prusament_petg_terracottalight_1000_175_c",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_natural_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_pristinewhite_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_terracottalight_2000_175_p",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_simplygreen_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_urbangrey_1000_175_c",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_marblegrey_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_signalwhite_2000_175_p",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_pineappleyellow_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_natural_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_lipstickred_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_prusaorange_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_galaxyred_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_yellowgold_1000_175_c",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_armygreen_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_ultramarineblue_1000_175_c",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_mangoyellow_1000_175_c",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_jetblack_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_gentleman'sgrey_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_ms.pink_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_pineappleyellow_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_signalwhite_1000_175_c",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_pristinewhite_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_prusaorange_1000_175_c",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_opalgreen_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_azureblue_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_pistachiogreen_1000_175_c",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_junglegreen_1000_175_c",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_pearlmouse_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_chalkyblue_1000_175_c",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_marblegrey_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_lipstickred_2000_175_p",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_yellowgold_2000_175_p",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_azureblue_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_anthracitegrey_2000_175_p",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_mangoyellow_2000_175_p",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_pearlmouse_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_opalgreen_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_jetblack_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_prusaorange_2000_175_p",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_armygreen_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_anthracitegrey_1000_175_c",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_junglegreen_2000_175_p",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_galaxypurple_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_lipstickred_1000_175_c",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_galaxysilver_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_vanillawhite_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_galaxyblack_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_galaxysilver_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_chalkyblue_2000_175_p",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_vanillawhite_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_ms.pink_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_prusaorange_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_galaxygreen_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_gravitygrey_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_clear_2000_175_p",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_urbangrey_2000_175_p",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_carminered_2000_175_p",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_jetblack_2000_175_p",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_clear_1000_175_c",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_jetblack_1000_175_c",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_galaxypurple_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_galaxygreen_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_oceanblue_1000_175_c",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_ultramarineblue_2000_175_p",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_galaxyblack_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_oceanblue_2000_175_p",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_lipstickred_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_gentleman'sgrey_2000_175_p",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_galaxyred_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_simplygreen_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_carminered_1000_175_c",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_petg_pistachiogreen_2000_175_p",
      "values": {
        "bed_temp": 80
      },
      "source": "https://prusament.com/materials/prusament-petg/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "prusament_pla_gravitygrey_1000_175_c",
      "values": {
        "extruder_temp": 210,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://prusament.com/materials/pla/",
      "lot": "current manufacturer product-line recommendations; packaging/tare not inferred",
      "same_variant": true,
      "approved": true
    }
  ],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `prusament_petg_galaxyblack_1000_175_c` — Galaxy Black
- `prusament_petg_neongreentransparent_1000_175_c` — Neon Green Transparent
- `prusament_petg_matteblack_2000_175_p` — Matte Black
- `prusament_petg_galaxyblack_2000_175_p` — Galaxy Black
- `prusament_petg_neongreentransparent_2000_175_p` — Neon Green Transparent
- `prusament_pc-cf_pcblendcarbonfiberblack_800_175_p` — PC Blend Carbon Fiber Black
- `prusament_pc_pcblendjetblack_1000_175_c` — PC Blend Jet Black
- `prusament_pc_pcblendprusaorange_1000_175_c` — PC Blend Prusa Orange
- `prusament_pc_pcblendprusaprogreen_1000_175_c` — PC Blend Prusa Pro Green
- `prusament_pc_pcblendnatural_1000_175_c` — PC Blend Natural
- `prusament_pc_pcblendurbangrey_1000_175_c` — PC Blend Urban Grey
- `prusament_tpu-95a_natural_500_175_p` — Natural
- `prusament_pvb_darkblue_1000_175_c` — Dark Blue
- `prusament_pvb_brightgreen_1000_175_c` — Bright Green
- `prusament_pvb_prusaorange_1000_175_c` — Prusa Orange
- `prusament_pvb_smokyblack_1000_175_c` — Smoky Black
- `prusament_pvb_lightyellow_1000_175_c` — Light Yellow
- `prusament_asa_natural_800_175_c` — Natural
- `prusament_asa_lipstickred_800_175_c` — Lipstick Red
- `prusament_asa_signalwhite_800_175_c` — Signal White
- `prusament_asa_prusaorange_800_175_c` — Prusa Orange
- `prusament_asa_jetblack_800_175_c` — Jet Black
- `prusament_asa_galaxyblack_800_175_c` — Galaxy Black
- `prusament_asa_prusaprogreen_800_175_c` — Prusa Pro Green
- `prusament_asa_sapphireblue_800_175_c` — Sapphire Blue
- `prusament_asa_olivegreen_800_175_c` — Olive Green
- `prusament_asa_natural(nfc)_800_175_p` — Natural (NFC)
- `prusament_asa_lipstickred(nfc)_800_175_p` — Lipstick Red (NFC)
- `prusament_asa_signalwhite(nfc)_800_175_p` — Signal White (NFC)
- `prusament_asa_prusaorange(nfc)_800_175_p` — Prusa Orange (NFC)
- `prusament_asa_jetblack(nfc)_800_175_p` — Jet Black (NFC)
- `prusament_asa_galaxyblack(nfc)_800_175_p` — Galaxy Black (NFC)
- `prusament_asa_prusaprogreen(nfc)_800_175_p` — Prusa Pro Green (NFC)
- `prusament_asa_sapphireblue(nfc)_800_175_p` — Sapphire Blue (NFC)
- `prusament_asa_olivegreen(nfc)_800_175_p` — Olive Green (NFC)
- `prusament_asa_asajetblack_800_175_p` — ASA Jet Black
- `prusament_asa_asalipstickred_800_175_p` — ASA Lipstick Red
- `prusament_asa_asanatural_800_175_p` — ASA Natural
- `prusament_asa_asaolivegreen_800_175_p` — ASA Olive Green
- `prusament_asa_asaprusagalaxyblack_800_175_p` — ASA Prusa Galaxy Black
- `prusament_asa_asaprusagreen_800_175_p` — ASA Prusa Green
- `prusament_asa_asaprusaorange_800_175_p` — ASA Prusa Orange
- `prusament_asa_asaprusaprogreen_800_175_p` — ASA Prusa Pro Green
- `prusament_asa_asasapphireblue_800_175_p` — ASA Sapphire Blue
- `prusament_asa_asasignalwhite_800_175_p` — ASA Signal White
- `prusament_asa_asajetblack_850_175_p` — ASA Jet Black
- `prusament_asa_asalipstickred_850_175_p` — ASA Lipstick Red
- `prusament_asa_asanatural_850_175_p` — ASA Natural
- `prusament_asa_asaolivegreen_850_175_p` — ASA Olive Green
- `prusament_asa_asaprusagalaxyblack_850_175_p` — ASA Prusa Galaxy Black
- `prusament_asa_asaprusagreen_850_175_p` — ASA Prusa Green
- `prusament_asa_asaprusaorange_850_175_p` — ASA Prusa Orange
- `prusament_asa_asaprusaprogreen_850_175_p` — ASA Prusa Pro Green
- `prusament_asa_asasapphireblue_850_175_p` — ASA Sapphire Blue
- `prusament_asa_asasignalwhite_850_175_p` — ASA Signal White
- `prusament_pa11_pa11-cfblack_25_175_p` — PA11-CF Black
- `prusament_pa11_pa11-cfblack_800_175_p` — PA11-CF Black
- `prusament_pc_pcblendprusagreen_850_175_p` — PC Blend Prusa Green
- `prusament_pc_pcspacegradeblack_850_175_p` — PC Space Grade Black
- `prusament_pc_pcblendprusagreen_970_175_p` — PC Blend Prusa Green
- `prusament_pc_pcspacegradeblack_970_175_p` — PC Space Grade Black
- `prusament_pc_pc-cfblack_25_175_p` — PC-CF Black
- `prusament_pc_pc-cfblendcarbonfiberblack_25_175_p` — PC-CF Blend Carbon Fiber Black
- `prusament_pc_pc-cfblack_800_175_p` — PC-CF Black
- `prusament_pc_pc-cfblendcarbonfiberblack_800_175_p` — PC-CF Blend Carbon Fiber Black
- `prusament_pc_pc-cfblack_2000_175_p` — PC-CF Black
- `prusament_pc_pc-cfblendcarbonfiberblack_2000_175_p` — PC-CF Blend Carbon Fiber Black
- `prusament_pei_pei1010natural_25_175_p` — PEI 1010 Natural
- `prusament_pei_pei1010natural_500_175_p` — PEI 1010 Natural
- `prusament_petg_petgcfblack_1000_175_c` — PETG CF Black
- `prusament_petg_petgmagnetite40%grey_1000_175_c` — PETG Magnetite 40% Grey
- `prusament_petg_petgneongreen_1000_175_c` — PETG Neon Green
- `prusament_petg_petgorangeforppe_1000_175_c` — PETG Orange for PPE
- `prusament_petg_petgprusagalaxyblack_1000_175_c` — PETG Prusa Galaxy Black
- `prusament_petg_petgprusagalaxyblack(nfc)_1000_175_c` — PETG Prusa Galaxy Black (NFC)
- `prusament_petg_petgprusagreen_1000_175_c` — PETG Prusa Green
- `prusament_petg_petgprusaorange(nfc)_1000_175_c` — PETG Prusa Orange (NFC)
- `prusament_petg_petgprusaorangetransparent_1000_175_c` — PETG Prusa Orange Transparent
- `prusament_petg_petgrecycled_1000_175_c` — PETG Recycled
- `prusament_petg_petgrecycledblack_1000_175_c` — PETG Recycled Black
- `prusament_petg_petgshimmeringviolet_1000_175_c` — PETG Shimmering Violet
- `prusament_petg_petgskyblue_1000_175_c` — PETG Sky Blue
- `prusament_petg_petgtungsten75%_1000_175_c` — PETG Tungsten 75%
- `prusament_petg_petgmagnetite40%grey_2000_175_p` — PETG Magnetite 40% Grey
- `prusament_petg_petgneongreen_2000_175_p` — PETG Neon Green
- `prusament_petg_petgorangeforppe_2000_175_p` — PETG Orange for PPE
- `prusament_petg_petgprusagalaxyblack_2000_175_p` — PETG Prusa Galaxy Black
- `prusament_petg_petgprusagalaxyblack(nfc)_2000_175_p` — PETG Prusa Galaxy Black (NFC)
- `prusament_petg_petgprusagreen_2000_175_p` — PETG Prusa Green
- `prusament_petg_petgprusaorange(nfc)_2000_175_p` — PETG Prusa Orange (NFC)
- `prusament_petg_petgprusaorangetransparent_2000_175_p` — PETG Prusa Orange Transparent
- `prusament_petg_petgrecycled_2000_175_p` — PETG Recycled
- `prusament_petg_petgrecycledblack_2000_175_p` — PETG Recycled Black
- `prusament_petg_petgshimmeringviolet_2000_175_p` — PETG Shimmering Violet
- `prusament_petg_petgskyblue_2000_175_p` — PETG Sky Blue
- `prusament_petg_petgtungsten75%_2000_175_p` — PETG Tungsten 75%
- `prusament_petg_petgmagnetitegrey_1000_175_c` — PETG Magnetite Grey
- `prusament_petg_petgv0jetblack_1000_175_c` — PETG V0 Jet Black
- `prusament_petg_petgv0natural_1000_175_c` — PETG V0 Natural
- `prusament_pla_blendsilkplalimegreen_970_175_p` — Blend Silk PLA Lime Green
- `prusament_pla_blendsilkplams.pink_970_175_p` — Blend Silk PLA Ms. Pink
- `prusament_pla_blendsilkplamysilverness_970_175_p` — Blend Silk PLA My Silverness
- `prusament_pla_blendsilkplaohmygold_970_175_p` — Blend Silk PLA Oh My Gold
- `prusament_pla_blendsilkplapearlwhite_970_175_p` — Blend Silk PLA Pearl White
- `prusament_pla_blendsilkplaroyalblue_970_175_p` — Blend Silk PLA Royal Blue
- `prusament_pla_blendsilkplavivalabronze_970_175_p` — Blend Silk PLA Viva La Bronze
- `prusament_pla_blendsilkplalimegreen_1000_175_c` — Blend Silk PLA Lime Green
- `prusament_pla_blendsilkplams.pink_1000_175_c` — Blend Silk PLA Ms. Pink
- `prusament_pla_blendsilkplamysilverness_1000_175_c` — Blend Silk PLA My Silverness
- `prusament_pla_blendsilkplaohmygold_1000_175_c` — Blend Silk PLA Oh My Gold
- `prusament_pla_blendsilkplapearlwhite_1000_175_c` — Blend Silk PLA Pearl White
- `prusament_pla_blendsilkplaroyalblue_1000_175_c` — Blend Silk PLA Royal Blue
- `prusament_pla_blendsilkplavivalabronze_1000_175_c` — Blend Silk PLA Viva La Bronze
- `prusament_pla_mysticpremiumplabrown_1000_175_c` — Mystic Premium PLA Brown
- `prusament_pla_mysticpremiumplagreen_1000_175_c` — Mystic Premium PLA Green
- `prusament_pla_plaanthracitegrey_970_175_p` — PLA Anthracite Grey
- `prusament_pla_plaarmygreen_970_175_p` — PLA Army Green
- `prusament_pla_plaazureblue_970_175_p` — PLA Azure Blue
- `prusament_pla_plabloodred_970_175_p` — PLA Blood Red
- `prusament_pla_plachalkyblue_970_175_p` — PLA Chalky Blue
- `prusament_pla_plagalaxyblack_970_175_p` — PLA Galaxy Black
- `prusament_pla_plagalaxygreen_970_175_p` — PLA Galaxy Green
- `prusament_pla_plagalaxygrey_970_175_p` — PLA Galaxy Grey
- `prusament_pla_plagalaxypurple_970_175_p` — PLA Galaxy Purple
- `prusament_pla_plagalaxyred_970_175_p` — PLA Galaxy Red
- `prusament_pla_plagalaxysilver_970_175_p` — PLA Galaxy Silver
- `prusament_pla_plagentleman'sgrey_970_175_p` — PLA Gentleman's Grey
- `prusament_pla_plagravitygrey_970_175_p` — PLA Gravity Grey
- `prusament_pla_plajetblack_970_175_p` — PLA Jet Black
- `prusament_pla_plalimegreen_970_175_p` — PLA Lime Green
- `prusament_pla_plalipstickred_970_175_p` — PLA Lipstick Red
- `prusament_pla_plamarblegrey_970_175_p` — PLA Marble Grey
- `prusament_pla_plams.pink_970_175_p` — PLA Ms. Pink
- `prusament_pla_plamysilverness_970_175_p` — PLA My Silverness
- `prusament_pla_plamysticbrown_970_175_p` — PLA Mystic Brown
- `prusament_pla_plamysticgreen_970_175_p` — PLA Mystic Green
- `prusament_pla_planatural_970_175_p` — PLA Natural
- `prusament_pla_planoctuabeige_970_175_p` — PLA Noctua Beige
- `prusament_pla_planoctuabrown_970_175_p` — PLA Noctua Brown
- `prusament_pla_plaohmygold_970_175_p` — PLA Oh My Gold
- `prusament_pla_plaopalgreen_970_175_p` — PLA Opal Green
- `prusament_pla_plapearlmouse_970_175_p` — PLA Pearl Mouse
- `prusament_pla_plapearlwhite_970_175_p` — PLA Pearl White
- `prusament_pla_plapineappleyellow_970_175_p` — PLA Pineapple Yellow
- `prusament_pla_plapistachiogreen_970_175_p` — PLA Pistachio Green
- `prusament_pla_plapristinewhite_970_175_p` — PLA Pristine White
- `prusament_pla_plaprusagalaxyblack_970_175_p` — PLA Prusa Galaxy Black
- `prusament_pla_plaprusagreen_970_175_p` — PLA Prusa Green
- `prusament_pla_plaprusaorange_970_175_p` — PLA Prusa Orange
- `prusament_pla_plaprusaprogreen_970_175_p` — PLA Prusa Pro Green
- `prusament_pla_plaralgaepigment_970_175_p` — PLA r Algae Pigment
- `prusament_pla_plarcornpigment_970_175_p` — PLA r Corn Pigment
- `prusament_pla_plarrisottopigment_970_175_p` — PLA r Risotto Pigment
- `prusament_pla_plarwinepigment_970_175_p` — PLA r Wine Pigment
- `prusament_pla_plarecycled_970_175_p` — PLA Recycled
- `prusament_pla_plaroyalblue_970_175_p` — PLA Royal Blue
- `prusament_pla_plasimplygreen_970_175_p` — PLA Simply Green
- `prusament_pla_plavanillawhite_970_175_p` — PLA Vanilla White
- `prusament_pla_plavivalabronze_970_175_p` — PLA Viva La Bronze
- `prusament_pla_plaanthracitegrey_1000_175_c` — PLA Anthracite Grey
- `prusament_pla_plabloodred_1000_175_c` — PLA Blood Red
- `prusament_pla_plachalkyblue_1000_175_c` — PLA Chalky Blue
- `prusament_pla_plagalaxygrey_1000_175_c` — PLA Galaxy Grey
- `prusament_pla_plalimegreen_1000_175_c` — PLA Lime Green
- `prusament_pla_plamysilverness_1000_175_c` — PLA My Silverness
- `prusament_pla_plamysticbrown_1000_175_c` — PLA Mystic Brown
- `prusament_pla_plamysticgreen_1000_175_c` — PLA Mystic Green
- `prusament_pla_planoctuabeige_1000_175_c` — PLA Noctua Beige
- `prusament_pla_planoctuabrown_1000_175_c` — PLA Noctua Brown
- `prusament_pla_plaohmygold_1000_175_c` — PLA Oh My Gold
- `prusament_pla_plapearlwhite_1000_175_c` — PLA Pearl White
- `prusament_pla_plapistachiogreen_1000_175_c` — PLA Pistachio Green
- `prusament_pla_plaprusagalaxyblack_1000_175_c` — PLA Prusa Galaxy Black
- `prusament_pla_plaprusagreen_1000_175_c` — PLA Prusa Green
- `prusament_pla_plaprusaprogreen_1000_175_c` — PLA Prusa Pro Green
- `prusament_pla_plaralgaepigment_1000_175_c` — PLA r Algae Pigment
- `prusament_pla_plarcornpigment_1000_175_c` — PLA r Corn Pigment
- `prusament_pla_plarrisottopigment_1000_175_c` — PLA r Risotto Pigment
- `prusament_pla_plarwinepigment_1000_175_c` — PLA r Wine Pigment
- `prusament_pla_plarecycled_1000_175_c` — PLA Recycled
- `prusament_pla_plaroyalblue_1000_175_c` — PLA Royal Blue
- `prusament_pla_plavivalabronze_1000_175_c` — PLA Viva La Bronze
- `prusament_pla_plaanthracitegrey_2000_175_p` — PLA Anthracite Grey
- `prusament_pla_plabloodred_2000_175_p` — PLA Blood Red
- `prusament_pla_plachalkyblue_2000_175_p` — PLA Chalky Blue
- `prusament_pla_plagalaxygrey_2000_175_p` — PLA Galaxy Grey
- `prusament_pla_plalimegreen_2000_175_p` — PLA Lime Green
- `prusament_pla_plamysilverness_2000_175_p` — PLA My Silverness
- `prusament_pla_plamysticbrown_2000_175_p` — PLA Mystic Brown
- `prusament_pla_plamysticgreen_2000_175_p` — PLA Mystic Green
- `prusament_pla_planoctuabeige_2000_175_p` — PLA Noctua Beige
- `prusament_pla_planoctuabrown_2000_175_p` — PLA Noctua Brown
- `prusament_pla_plaohmygold_2000_175_p` — PLA Oh My Gold
- `prusament_pla_plapearlwhite_2000_175_p` — PLA Pearl White
- `prusament_pla_plapistachiogreen_2000_175_p` — PLA Pistachio Green
- `prusament_pla_plaprusagalaxyblack_2000_175_p` — PLA Prusa Galaxy Black
- `prusament_pla_plaprusagreen_2000_175_p` — PLA Prusa Green
- `prusament_pla_plaprusaprogreen_2000_175_p` — PLA Prusa Pro Green
- `prusament_pla_plaralgaepigment_2000_175_p` — PLA r Algae Pigment
- `prusament_pla_plarcornpigment_2000_175_p` — PLA r Corn Pigment
- `prusament_pla_plarrisottopigment_2000_175_p` — PLA r Risotto Pigment
- `prusament_pla_plarwinepigment_2000_175_p` — PLA r Wine Pigment
- `prusament_pla_plarecycled_2000_175_p` — PLA Recycled
- `prusament_pla_plaroyalblue_2000_175_p` — PLA Royal Blue
- `prusament_pla_plavivalabronze_2000_175_p` — PLA Viva La Bronze
- `prusament_pla_plarecycledplarecycled_2000_175_p` — PLA Recycled PLA Recycled
- `prusament_pla_rplaalgae_1000_175_c` — rPLA Algae
- `prusament_pla_rplacorn_1000_175_c` — rPLA Corn
- `prusament_pla_rplawine_1000_175_c` — rPLA Wine
- `prusament_pla_plawoodfillchocolatebrown_1000_175_c` — PLA Woodfill Chocolate Brown
- `prusament_pla_plawoodfilllindenlight_1000_175_c` — PLA Woodfill Linden Light
- `prusament_pla_plawoodfillpastelbrown_1000_175_c` — PLA Woodfill Pastel Brown
- `prusament_pp_pp-cfblack_650_175_p` — PP-CF Black
- `prusament_pp_pp-gfnatural_850_175_p` — PP-GF Natural
- `prusament_pvb_pvbbrightgreen_500_175_p` — PVB Bright Green
- `prusament_pvb_pvbbrightgreentransparent_500_175_p` — PVB Bright Green Transparent
- `prusament_pvb_pvbdarkblue_500_175_p` — PVB Dark Blue
- `prusament_pvb_pvbdarkbluetransparent_500_175_p` — PVB Dark Blue Transparent
- `prusament_pvb_pvblightyellow_500_175_p` — PVB Light Yellow
- `prusament_pvb_pvblightyellowtransparent_500_175_p` — PVB Light Yellow Transparent
- `prusament_pvb_pvbnatural_500_175_p` — PVB Natural
- `prusament_pvb_pvbnaturaltransparent_500_175_p` — PVB Natural Transparent
- `prusament_pvb_pvbprusaorange_500_175_p` — PVB Prusa Orange
- `prusament_pvb_pvbprusaorangetransparent_500_175_p` — PVB Prusa Orange Transparent
- `prusament_pvb_pvbsmokyblack_500_175_p` — PVB Smoky Black
- `prusament_pvb_pvbsmokyblacktransparent_500_175_p` — PVB Smoky Black Transparent
- `prusament_tpu_tpu95ajetblack_500_175_p` — TPU 95A Jet Black
- `prusament_tpu_tpu95anatural_500_175_p` — TPU 95A Natural
