# overture duplicate migration review

Base `c87c3db5cf850d7ab7c2c108b5412f1c8240dcef`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `e0dfb50d9b4ba7bc4ecc980104abe046e22ece4731d7b1079acfb2b57d52d83c`.

## Authorization and result

{"groups": 83, "approved_groups": 81, "retired": 81, "deferred": 2, "hard_stops": 0, "before_count": 52449, "after_count": 52368, "brand_before": 582, "brand_after": 501, "registry_before": 985, "registry_after": 1066, "metadata_fields_changed": 0, "code_transfers": 4, "new": 0, "changed_identity": 0, "rekeyed": 0}

Owner approved the80 prior proposals andOV066 with survivor metadata retained. All original density/nozzle/bed/HEX conflicts remain unresolved; packaging/tare are unchanged. OV083 and Rule5 decomposition blocks are deferred.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://overture3d.com/products/overture-matte-pla", "structured_url": "https://overture3d.com/products/overture-matte-pla.js", "variant": "Light gray / 1.75mm / 1 kg", "sku": "VFFMLGR17511", "hex": "BAC4C4", "binding": "OV066 explicit owner approval"}
- {"url": "https://overture3d.com/products/overture-tpu", "structured_url": "https://overture3d.com/products/overture-tpu.js", "variant": "Matte Gray", "sku": "VFTGRY11-010058", "hex": "E2E7E9", "binding": "OV083 unresolved; no changes"}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`overture_abs_absblack_1000_175_c`|`overture_abs_black_1000_175_c`|`overture.json::Overture::ABS {color_name}::ABS Black::ABS::1000::1.75::cardboard::False`|
|`overture_abs_absblue_1000_175_c`|`overture_abs_blue_1000_175_c`|`overture.json::Overture::ABS {color_name}::ABS Blue::ABS::1000::1.75::cardboard::False`|
|`overture_abs_absdarkred_1000_175_c`|`overture_abs_darkred_1000_175_c`|`overture.json::Overture::ABS {color_name}::ABS Dark Red::ABS::1000::1.75::cardboard::False`|
|`overture_abs_absdiamondgray_1000_175_c`|`overture_abs_diamondgray_1000_175_c`|`overture.json::Overture::ABS {color_name}::ABS Diamond Gray::ABS::1000::1.75::cardboard::False`|
|`overture_abs_absdiamondorange_1000_175_c`|`overture_abs_diamondorange_1000_175_c`|`overture.json::Overture::ABS {color_name}::ABS Diamond Orange::ABS::1000::1.75::cardboard::False`|
|`overture_abs_absdiamondpurple_1000_175_c`|`overture_abs_diamondpurple_1000_175_c`|`overture.json::Overture::ABS {color_name}::ABS Diamond Purple::ABS::1000::1.75::cardboard::False`|
|`overture_abs_absgray_1000_175_c`|`overture_abs_gray_1000_175_c`|`overture.json::Overture::ABS {color_name}::ABS Gray::ABS::1000::1.75::cardboard::False`|
|`overture_abs_absgreen_1000_175_c`|`overture_abs_green_1000_175_c`|`overture.json::Overture::ABS {color_name}::ABS Green::ABS::1000::1.75::cardboard::False`|
|`overture_abs_absnatural_1000_175_c`|`overture_abs_natural_1000_175_c`|`overture.json::Overture::ABS {color_name}::ABS Natural::ABS::1000::1.75::cardboard::False`|
|`overture_abs_abspurple_1000_175_c`|`overture_abs_purple_1000_175_c`|`overture.json::Overture::ABS {color_name}::ABS Purple::ABS::1000::1.75::cardboard::False`|
|`overture_abs_absslategray_1000_175_c`|`overture_abs_slategray_1000_175_c`|`overture.json::Overture::ABS {color_name}::ABS Slate Gray::ABS::1000::1.75::cardboard::False`|
|`overture_abs_abswhite_1000_175_c`|`overture_abs_white_1000_175_c`|`overture.json::Overture::ABS {color_name}::ABS White::ABS::1000::1.75::cardboard::False`|
|`overture_abs_absyellow_1000_175_c`|`overture_abs_yellow_1000_175_c`|`overture.json::Overture::ABS {color_name}::ABS Yellow::ABS::1000::1.75::cardboard::False`|
|`overture_asa_asablack_1000_175_c`|`overture_asa_black_1000_175_c`|`overture.json::Overture::ASA {color_name}::ASA Black::ASA::1000::1.75::cardboard::False`|
|`overture_asa_asablue_1000_175_c`|`overture_asa_blue_1000_175_c`|`overture.json::Overture::ASA {color_name}::ASA Blue::ASA::1000::1.75::cardboard::False`|
|`overture_asa_asabrown_1000_175_c`|`overture_asa_brown_1000_175_c`|`overture.json::Overture::ASA {color_name}::ASA Brown::ASA::1000::1.75::cardboard::False`|
|`overture_asa_asadiamondblue_1000_175_c`|`overture_asa_diamondblue_1000_175_c`|`overture.json::Overture::ASA {color_name}::ASA Diamond Blue::ASA::1000::1.75::cardboard::False`|
|`overture_asa_asadiamondgreen_1000_175_c`|`overture_asa_diamondgreen_1000_175_c`|`overture.json::Overture::ASA {color_name}::ASA Diamond Green::ASA::1000::1.75::cardboard::False`|
|`overture_asa_asadiamondred_1000_175_c`|`overture_asa_diamondred_1000_175_c`|`overture.json::Overture::ASA {color_name}::ASA Diamond Red::ASA::1000::1.75::cardboard::False`|
|`overture_asa_asagray_1000_175_c`|`overture_asa_gray_1000_175_c`|`overture.json::Overture::ASA {color_name}::ASA Gray::ASA::1000::1.75::cardboard::False`|
|`overture_asa_asagreen_1000_175_c`|`overture_asa_green_1000_175_c`|`overture.json::Overture::ASA {color_name}::ASA Green::ASA::1000::1.75::cardboard::False`|
|`overture_asa_asanatural_1000_175_c`|`overture_asa_natural_1000_175_c`|`overture.json::Overture::ASA {color_name}::ASA Natural::ASA::1000::1.75::cardboard::False`|
|`overture_asa_asaolivegreen_1000_175_c`|`overture_asa_olivegreen_1000_175_c`|`overture.json::Overture::ASA {color_name}::ASA Olive Green::ASA::1000::1.75::cardboard::False`|
|`overture_asa_asaorange_1000_175_c`|`overture_asa_orange_1000_175_c`|`overture.json::Overture::ASA {color_name}::ASA Orange::ASA::1000::1.75::cardboard::False`|
|`overture_asa_asared_1000_175_c`|`overture_asa_red_1000_175_c`|`overture.json::Overture::ASA {color_name}::ASA Red::ASA::1000::1.75::cardboard::False`|
|`overture_asa_asawhite_1000_175_c`|`overture_asa_white_1000_175_c`|`overture.json::Overture::ASA {color_name}::ASA White::ASA::1000::1.75::cardboard::False`|
|`overture_asa_asayellow_1000_175_c`|`overture_asa_yellow_1000_175_c`|`overture.json::Overture::ASA {color_name}::ASA Yellow::ASA::1000::1.75::cardboard::False`|
|`overture_petg_petgarmygreen_1000_175_c`|`overture_petg_armygreen_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Army Green::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgblack_1000_175_c`|`overture_petg_black_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Black::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgblue_1000_175_c`|`overture_petg_blue_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Blue::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgbrown_1000_175_c`|`overture_petg_brown_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Brown::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgdigitalblue_1000_175_c`|`overture_petg_digitalblue_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Digital Blue::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petggold_1000_175_c`|`overture_petg_gold_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Gold::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petggrassgreen_1000_175_c`|`overture_petg_grassgreen_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Grass Green::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petggreen_1000_175_c`|`overture_petg_green_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Green::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petglightgray_1000_175_c`|`overture_petg_lightgray_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Light Gray::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgmagenta_1000_175_c`|`overture_petg_magenta_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Magenta::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgorange_1000_175_c`|`overture_petg_orange_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Orange::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgpink_1000_175_c`|`overture_petg_pink_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Pink::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgpurple_1000_175_c`|`overture_petg_purple_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Purple::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgred_1000_175_c`|`overture_petg_red_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Red::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgrockwhite_1000_175_c`|`overture_petg_rockwhite_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Rock White::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgspacegray_1000_175_c`|`overture_petg_spacegray_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Space Gray::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgsparkleblue_1000_175_c`|`overture_petg_sparkleblue_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Sparkle Blue::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgstarryblue_1000_175_c`|`overture_petg_starryblue_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Starry Blue::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgtransparent_1000_175_c`|`overture_petg_transparent_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Transparent::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgtransparentblue_1000_175_c`|`overture_petg_transparentblue_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Transparent Blue::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgtransparentgreen_1000_175_c`|`overture_petg_transparentgreen_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Transparent Green::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgtransparentred_1000_175_c`|`overture_petg_transparentred_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Transparent Red::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgwhite_1000_175_c`|`overture_petg_white_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG White::PETG::1000::1.75::cardboard::False`|
|`overture_petg_petgyellow_1000_175_c`|`overture_petg_yellow_1000_175_c`|`overture.json::Overture::PETG {color_name}::PETG Yellow::PETG::1000::1.75::cardboard::False`|
|`overture_pla_matteplalightgrey_1000_175_c`|`overture_pla_matteplalightgray_1000_175_c`|`overture.json::Overture::Matte PLA {color_name}::Matte PLA Light Grey::PLA::1000.0::1.75::cardboard::False`|
|`overture_pla_plablack_1000_175_c`|`overture_pla_black_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Black::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plablue_1000_175_c`|`overture_pla_blue_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Blue::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plabrown_1000_175_c`|`overture_pla_brown_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Brown::PLA::1000::1.75::cardboard::False`|
|`overture_pla_placementgray_1000_175_c`|`overture_pla_cementgray_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Cement Gray::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plachocolate_1000_175_c`|`overture_pla_chocolate_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Chocolate::PLA::1000::1.75::cardboard::False`|
|`overture_pla_placoldwhite_1000_175_c`|`overture_pla_coldwhite_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Cold White::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plafreshred_1000_175_c`|`overture_pla_freshred_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Fresh Red::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plaglowindark_1000_175_c`|`overture_pla_glowindark_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Glow in Dark::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plagrayblue_1000_175_c`|`overture_pla_grayblue_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Gray Blue::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plagreen_1000_175_c`|`overture_pla_green_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Green::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plahighlightyellow_1000_175_c`|`overture_pla_highlightyellow_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Highlight Yellow::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plalightblue_1000_175_c`|`overture_pla_lightblue_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Light Blue::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plalightgray_1000_175_c`|`overture_pla_lightgray_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Light Gray::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plamidnightblack_1000_175_c`|`overture_pla_midnightblack_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Midnight Black::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plaolivegreen_1000_175_c`|`overture_pla_olivegreen_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Olive Green::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plaorange_1000_175_c`|`overture_pla_orange_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Orange::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plapink_1000_175_c`|`overture_pla_pink_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Pink::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plapurple_1000_175_c`|`overture_pla_purple_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Purple::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plared_1000_175_c`|`overture_pla_red_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Red::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plarockfossilrock_1000_175_c`|`overture_pla_rockplafossilrock_1000_175_c`|`overture.json::Overture::PLA Rock {color_name}::PLA Rock Fossil Rock::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plarockglacierblue_1000_175_c`|`overture_pla_rockplaglacierblue_1000_175_c`|`overture.json::Overture::PLA Rock {color_name}::PLA Rock Glacier Blue::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plarockmarsred_1000_175_c`|`overture_pla_rockplamarsred_1000_175_c`|`overture.json::Overture::PLA Rock {color_name}::PLA Rock Mars Red::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plarockrockrainbow_1000_175_c`|`overture_pla_rockplarockrainbow_1000_175_c`|`overture.json::Overture::PLA Rock {color_name}::PLA Rock Rock Rainbow::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plarockrockwhite_1000_175_c`|`overture_pla_rockplarockwhite_1000_175_c`|`overture.json::Overture::PLA Rock {color_name}::PLA Rock Rock White::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plarocksedimentaryrock_1000_175_c`|`overture_pla_rockplasedimentaryrock_1000_175_c`|`overture.json::Overture::PLA Rock {color_name}::PLA Rock Sedimentary Rock::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plaroyalgold_1000_175_c`|`overture_pla_royalgold_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Royal Gold::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plaspacegray_1000_175_c`|`overture_pla_spacegray_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Space Gray::PLA::1000::1.75::cardboard::False`|
|`overture_pla_plawhite_1000_175_c`|`overture_pla_white_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA White::PLA::1000::1.75::cardboard::False`|
|`overture_pla_playellow_1000_175_c`|`overture_pla_yellow_1000_175_c`|`overture.json::Overture::PLA {color_name}::PLA Yellow::PLA::1000::1.75::cardboard::False`|

## Per-group decisions and unresolved metadata

### OV001: dup-68a9afee2264954a70b328050a06706673f4adf6720f0372868d6fbae322853c

Status: APPROVED; survivor `overture_abs_black_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_abs_absblack_1000_175_c`|`ABS {color_name}`|`Black`|{"source_file": "overture.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`overture_abs_black_1000_175_c`|`{color_name}`|`Black`|{"source_file": "overture.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_abs_absblack_1000_175_c": 1.04,
    "overture_abs_black_1000_175_c": 1.15
  },
  "spool_weight": {
    "overture_abs_absblack_1000_175_c": 173,
    "overture_abs_black_1000_175_c": 147
  },
  "extruder_temp_range": {
    "overture_abs_absblack_1000_175_c": [
      230,
      260
    ],
    "overture_abs_black_1000_175_c": [
      245,
      265
    ]
  },
  "bed_temp_range": {
    "overture_abs_absblack_1000_175_c": [
      90,
      110
    ],
    "overture_abs_black_1000_175_c": [
      80,
      100
    ]
  }
}
```

### OV002: dup-0b449e889c3a914d20ad2708359045762cd615a29d92983c8da1136aa237c937

Status: APPROVED; survivor `overture_abs_blue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_abs_absblue_1000_175_c`|`ABS {color_name}`|`Blue`|{"source_file": "overture.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`overture_abs_blue_1000_175_c`|`{color_name}`|`Blue`|{"source_file": "overture.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_abs_absblue_1000_175_c": 1.04,
    "overture_abs_blue_1000_175_c": 1.15
  },
  "spool_weight": {
    "overture_abs_absblue_1000_175_c": 173,
    "overture_abs_blue_1000_175_c": 147
  },
  "color_hex": {
    "overture_abs_absblue_1000_175_c": "0E21AE",
    "overture_abs_blue_1000_175_c": "00628f"
  },
  "extruder_temp_range": {
    "overture_abs_absblue_1000_175_c": [
      230,
      260
    ],
    "overture_abs_blue_1000_175_c": [
      245,
      265
    ]
  },
  "bed_temp_range": {
    "overture_abs_absblue_1000_175_c": [
      90,
      110
    ],
    "overture_abs_blue_1000_175_c": [
      80,
      100
    ]
  }
}
```

### OV003: dup-cfeda7c2121b2eebdb30acb9e5cdb53b0734004acce0f075b81bffb60ad26a12

Status: APPROVED; survivor `overture_abs_darkred_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_abs_absdarkred_1000_175_c`|`ABS {color_name}`|`Dark Red`|{"source_file": "overture.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`overture_abs_darkred_1000_175_c`|`{color_name}`|`Dark Red`|{"source_file": "overture.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_abs_absdarkred_1000_175_c": 1.04,
    "overture_abs_darkred_1000_175_c": 1.15
  },
  "spool_weight": {
    "overture_abs_absdarkred_1000_175_c": 173,
    "overture_abs_darkred_1000_175_c": 147
  },
  "color_hex": {
    "overture_abs_absdarkred_1000_175_c": "DE1619",
    "overture_abs_darkred_1000_175_c": "ff311f"
  },
  "extruder_temp_range": {
    "overture_abs_absdarkred_1000_175_c": [
      230,
      260
    ],
    "overture_abs_darkred_1000_175_c": [
      245,
      265
    ]
  },
  "bed_temp_range": {
    "overture_abs_absdarkred_1000_175_c": [
      90,
      110
    ],
    "overture_abs_darkred_1000_175_c": [
      80,
      100
    ]
  }
}
```

### OV004: dup-e6aa98ec699b07dc03aa877987b6b6e70b441fa7db9323024b7315285abd9319

Status: APPROVED; survivor `overture_abs_diamondgray_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_abs_absdiamondgray_1000_175_c`|`ABS {color_name}`|`Diamond Gray`|{"source_file": "overture.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`overture_abs_diamondgray_1000_175_c`|`{color_name}`|`Diamond Gray`|{"source_file": "overture.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_abs_absdiamondgray_1000_175_c": 1.04,
    "overture_abs_diamondgray_1000_175_c": 1.15
  },
  "spool_weight": {
    "overture_abs_absdiamondgray_1000_175_c": 173,
    "overture_abs_diamondgray_1000_175_c": 147
  },
  "color_hex": {
    "overture_abs_absdiamondgray_1000_175_c": "697272",
    "overture_abs_diamondgray_1000_175_c": "8c8c8c"
  },
  "extruder_temp_range": {
    "overture_abs_absdiamondgray_1000_175_c": [
      230,
      260
    ],
    "overture_abs_diamondgray_1000_175_c": [
      245,
      265
    ]
  },
  "bed_temp_range": {
    "overture_abs_absdiamondgray_1000_175_c": [
      90,
      110
    ],
    "overture_abs_diamondgray_1000_175_c": [
      80,
      100
    ]
  },
  "pattern": {
    "overture_abs_absdiamondgray_1000_175_c": null,
    "overture_abs_diamondgray_1000_175_c": "sparkle"
  }
}
```

### OV005: dup-acaadbce807ac734371d8f89fe611c5b484efff511d121175b71c550f0bd661d

Status: APPROVED; survivor `overture_abs_diamondorange_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_abs_absdiamondorange_1000_175_c`|`ABS {color_name}`|`Diamond Orange`|{"source_file": "overture.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`overture_abs_diamondorange_1000_175_c`|`{color_name}`|`Diamond Orange`|{"source_file": "overture.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_abs_absdiamondorange_1000_175_c": 1.04,
    "overture_abs_diamondorange_1000_175_c": 1.15
  },
  "spool_weight": {
    "overture_abs_absdiamondorange_1000_175_c": 173,
    "overture_abs_diamondorange_1000_175_c": 147
  },
  "color_hex": {
    "overture_abs_absdiamondorange_1000_175_c": "FF8133",
    "overture_abs_diamondorange_1000_175_c": "ff8133"
  },
  "extruder_temp_range": {
    "overture_abs_absdiamondorange_1000_175_c": [
      230,
      260
    ],
    "overture_abs_diamondorange_1000_175_c": [
      245,
      265
    ]
  },
  "bed_temp_range": {
    "overture_abs_absdiamondorange_1000_175_c": [
      90,
      110
    ],
    "overture_abs_diamondorange_1000_175_c": [
      80,
      100
    ]
  },
  "pattern": {
    "overture_abs_absdiamondorange_1000_175_c": null,
    "overture_abs_diamondorange_1000_175_c": "sparkle"
  }
}
```

### OV006: dup-32305f12de141f693d774c6159e203e754937aad3c296e53e2e39f289699dae6

Status: APPROVED; survivor `overture_abs_diamondpurple_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_abs_absdiamondpurple_1000_175_c`|`ABS {color_name}`|`Diamond Purple`|{"source_file": "overture.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`overture_abs_diamondpurple_1000_175_c`|`{color_name}`|`Diamond Purple`|{"source_file": "overture.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_abs_absdiamondpurple_1000_175_c": 1.04,
    "overture_abs_diamondpurple_1000_175_c": 1.15
  },
  "spool_weight": {
    "overture_abs_absdiamondpurple_1000_175_c": 173,
    "overture_abs_diamondpurple_1000_175_c": 147
  },
  "color_hex": {
    "overture_abs_absdiamondpurple_1000_175_c": "8873C7",
    "overture_abs_diamondpurple_1000_175_c": "a04ed0"
  },
  "extruder_temp_range": {
    "overture_abs_absdiamondpurple_1000_175_c": [
      230,
      260
    ],
    "overture_abs_diamondpurple_1000_175_c": [
      245,
      265
    ]
  },
  "bed_temp_range": {
    "overture_abs_absdiamondpurple_1000_175_c": [
      90,
      110
    ],
    "overture_abs_diamondpurple_1000_175_c": [
      80,
      100
    ]
  },
  "pattern": {
    "overture_abs_absdiamondpurple_1000_175_c": null,
    "overture_abs_diamondpurple_1000_175_c": "sparkle"
  }
}
```

### OV007: dup-dfb4382f0b6e467d945eefe73bf6acfc199a2e323753963994efc516e7acc6ac

Status: APPROVED; survivor `overture_abs_gray_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_abs_absgray_1000_175_c`|`ABS {color_name}`|`Gray`|{"source_file": "overture.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`overture_abs_gray_1000_175_c`|`{color_name}`|`Gray`|{"source_file": "overture.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_abs_absgray_1000_175_c": 1.04,
    "overture_abs_gray_1000_175_c": 1.15
  },
  "spool_weight": {
    "overture_abs_absgray_1000_175_c": 173,
    "overture_abs_gray_1000_175_c": 147
  },
  "color_hex": {
    "overture_abs_absgray_1000_175_c": "94A7B7",
    "overture_abs_gray_1000_175_c": "cacac9"
  },
  "extruder_temp_range": {
    "overture_abs_absgray_1000_175_c": [
      230,
      260
    ],
    "overture_abs_gray_1000_175_c": [
      245,
      265
    ]
  },
  "bed_temp_range": {
    "overture_abs_absgray_1000_175_c": [
      90,
      110
    ],
    "overture_abs_gray_1000_175_c": [
      80,
      100
    ]
  }
}
```

### OV008: dup-dc36a9490c1059cb913b25749d61c850d058d83d40369fbd6b983d1d8c6b6d0c

Status: APPROVED; survivor `overture_abs_green_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_abs_absgreen_1000_175_c`|`ABS {color_name}`|`Green`|{"source_file": "overture.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`overture_abs_green_1000_175_c`|`{color_name}`|`Green`|{"source_file": "overture.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_abs_absgreen_1000_175_c": 1.04,
    "overture_abs_green_1000_175_c": 1.15
  },
  "spool_weight": {
    "overture_abs_absgreen_1000_175_c": 173,
    "overture_abs_green_1000_175_c": 147
  },
  "color_hex": {
    "overture_abs_absgreen_1000_175_c": "3D9441",
    "overture_abs_green_1000_175_c": "3d9441"
  },
  "extruder_temp_range": {
    "overture_abs_absgreen_1000_175_c": [
      230,
      260
    ],
    "overture_abs_green_1000_175_c": [
      245,
      265
    ]
  },
  "bed_temp_range": {
    "overture_abs_absgreen_1000_175_c": [
      90,
      110
    ],
    "overture_abs_green_1000_175_c": [
      80,
      100
    ]
  }
}
```

### OV009: dup-b739131a26c52ec25769d1d2470b60392e8f5ed48d9c7a423fc57d1e422031b0

Status: APPROVED; survivor `overture_abs_natural_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_abs_absnatural_1000_175_c`|`ABS {color_name}`|`Natural`|{"source_file": "overture.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`overture_abs_natural_1000_175_c`|`{color_name}`|`Natural`|{"source_file": "overture.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_abs_absnatural_1000_175_c": 1.04,
    "overture_abs_natural_1000_175_c": 1.15
  },
  "spool_weight": {
    "overture_abs_absnatural_1000_175_c": 173,
    "overture_abs_natural_1000_175_c": 147
  },
  "color_hex": {
    "overture_abs_absnatural_1000_175_c": "D9D8DE",
    "overture_abs_natural_1000_175_c": "f8f8ee"
  },
  "extruder_temp_range": {
    "overture_abs_absnatural_1000_175_c": [
      230,
      260
    ],
    "overture_abs_natural_1000_175_c": [
      245,
      265
    ]
  },
  "bed_temp_range": {
    "overture_abs_absnatural_1000_175_c": [
      90,
      110
    ],
    "overture_abs_natural_1000_175_c": [
      80,
      100
    ]
  }
}
```

### OV010: dup-66fed424e182bd444d9027e157f89341c854510a44b2bfc93486ea9a87728601

Status: APPROVED; survivor `overture_abs_purple_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_abs_abspurple_1000_175_c`|`ABS {color_name}`|`Purple`|{"source_file": "overture.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`overture_abs_purple_1000_175_c`|`{color_name}`|`Purple`|{"source_file": "overture.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_abs_abspurple_1000_175_c": 1.04,
    "overture_abs_purple_1000_175_c": 1.15
  },
  "spool_weight": {
    "overture_abs_abspurple_1000_175_c": 173,
    "overture_abs_purple_1000_175_c": 147
  },
  "color_hex": {
    "overture_abs_abspurple_1000_175_c": "8D65C7",
    "overture_abs_purple_1000_175_c": "7142a3"
  },
  "extruder_temp_range": {
    "overture_abs_abspurple_1000_175_c": [
      230,
      260
    ],
    "overture_abs_purple_1000_175_c": [
      245,
      265
    ]
  },
  "bed_temp_range": {
    "overture_abs_abspurple_1000_175_c": [
      90,
      110
    ],
    "overture_abs_purple_1000_175_c": [
      80,
      100
    ]
  }
}
```

### OV011: dup-f14ec266ceecd63e5567a7157982faf75850a4b2c638fdc1dab99352f3067467

Status: APPROVED; survivor `overture_abs_slategray_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_abs_absslategray_1000_175_c`|`ABS {color_name}`|`Slate Gray`|{"source_file": "overture.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`overture_abs_slategray_1000_175_c`|`{color_name}`|`Slate Gray`|{"source_file": "overture.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_abs_absslategray_1000_175_c": 1.04,
    "overture_abs_slategray_1000_175_c": 1.15
  },
  "spool_weight": {
    "overture_abs_absslategray_1000_175_c": 173,
    "overture_abs_slategray_1000_175_c": 147
  },
  "color_hex": {
    "overture_abs_absslategray_1000_175_c": "7D8EAA",
    "overture_abs_slategray_1000_175_c": "91a0b6"
  },
  "extruder_temp_range": {
    "overture_abs_absslategray_1000_175_c": [
      230,
      260
    ],
    "overture_abs_slategray_1000_175_c": [
      245,
      265
    ]
  },
  "bed_temp_range": {
    "overture_abs_absslategray_1000_175_c": [
      90,
      110
    ],
    "overture_abs_slategray_1000_175_c": [
      80,
      100
    ]
  }
}
```

### OV012: dup-def73bc9ff82ec930c955bfbc67adf97b77ded35f3b247f7bd80e4ff1a869646

Status: APPROVED; survivor `overture_abs_white_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_abs_abswhite_1000_175_c`|`ABS {color_name}`|`White`|{"source_file": "overture.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`overture_abs_white_1000_175_c`|`{color_name}`|`White`|{"source_file": "overture.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_abs_abswhite_1000_175_c": 1.04,
    "overture_abs_white_1000_175_c": 1.15
  },
  "spool_weight": {
    "overture_abs_abswhite_1000_175_c": 173,
    "overture_abs_white_1000_175_c": 147
  },
  "extruder_temp_range": {
    "overture_abs_abswhite_1000_175_c": [
      230,
      260
    ],
    "overture_abs_white_1000_175_c": [
      245,
      265
    ]
  },
  "bed_temp_range": {
    "overture_abs_abswhite_1000_175_c": [
      90,
      110
    ],
    "overture_abs_white_1000_175_c": [
      80,
      100
    ]
  }
}
```

### OV013: dup-963fb1791809eada7c61a1b0af49fdd1a36b190e0abc36e3e4b62c9af95828f7

Status: APPROVED; survivor `overture_abs_yellow_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_abs_absyellow_1000_175_c`|`ABS {color_name}`|`Yellow`|{"source_file": "overture.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`overture_abs_yellow_1000_175_c`|`{color_name}`|`Yellow`|{"source_file": "overture.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_abs_absyellow_1000_175_c": 1.04,
    "overture_abs_yellow_1000_175_c": 1.15
  },
  "spool_weight": {
    "overture_abs_absyellow_1000_175_c": 173,
    "overture_abs_yellow_1000_175_c": 147
  },
  "color_hex": {
    "overture_abs_absyellow_1000_175_c": "EEEA44",
    "overture_abs_yellow_1000_175_c": "ffff47"
  },
  "extruder_temp_range": {
    "overture_abs_absyellow_1000_175_c": [
      230,
      260
    ],
    "overture_abs_yellow_1000_175_c": [
      245,
      265
    ]
  },
  "bed_temp_range": {
    "overture_abs_absyellow_1000_175_c": [
      90,
      110
    ],
    "overture_abs_yellow_1000_175_c": [
      80,
      100
    ]
  }
}
```

### OV014: dup-4dc70411fa661ded642ce1542cc3ac566cfa4a9d4ad6bfaf2509a4edb46a7f15

Status: DEFERRED; survivor `overture_abs_glowgreen_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_abs_glowabsgreen_1000_175_c`|`Glow ABS {color_name}`|`Green`|{"source_file": "overture.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 1, "compiled_records": 1} / False|
|`overture_abs_glowgreen_1000_175_c`|`{color_name}`|`Glow Green`|{"source_file": "overture.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_abs_glowabsgreen_1000_175_c": 1.04,
    "overture_abs_glowgreen_1000_175_c": 1.15
  },
  "spool_weight": {
    "overture_abs_glowabsgreen_1000_175_c": 173,
    "overture_abs_glowgreen_1000_175_c": 147
  },
  "color_hex": {
    "overture_abs_glowabsgreen_1000_175_c": "4DFF64",
    "overture_abs_glowgreen_1000_175_c": "ebefee"
  },
  "extruder_temp_range": {
    "overture_abs_glowabsgreen_1000_175_c": [
      230,
      260
    ],
    "overture_abs_glowgreen_1000_175_c": [
      245,
      265
    ]
  },
  "bed_temp_range": {
    "overture_abs_glowabsgreen_1000_175_c": [
      90,
      110
    ],
    "overture_abs_glowgreen_1000_175_c": [
      80,
      100
    ]
  }
}
```

### OV015: dup-2deb01fa8fa1a5ad55b8e0a7532204a4b4b978a8920ce1440a6629155c35d1c5

Status: APPROVED; survivor `overture_asa_black_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_asa_asablack_1000_175_c`|`ASA {color_name}`|`Black`|{"source_file": "overture.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|
|`overture_asa_black_1000_175_c`|`{color_name}`|`Black`|{"source_file": "overture.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_asa_asablack_1000_175_c": 1.07,
    "overture_asa_black_1000_175_c": 1.14
  },
  "spool_weight": {
    "overture_asa_asablack_1000_175_c": 173,
    "overture_asa_black_1000_175_c": 132
  },
  "extruder_temp_range": {
    "overture_asa_asablack_1000_175_c": [
      235,
      260
    ],
    "overture_asa_black_1000_175_c": [
      240,
      270
    ]
  },
  "bed_temp_range": {
    "overture_asa_asablack_1000_175_c": [
      90,
      110
    ],
    "overture_asa_black_1000_175_c": [
      70,
      95
    ]
  }
}
```

### OV016: dup-776e381b2420f6329cea85b1a5e4f77b21ded17487ee48c32747174398278e24

Status: APPROVED; survivor `overture_asa_blue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_asa_asablue_1000_175_c`|`ASA {color_name}`|`Blue`|{"source_file": "overture.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|
|`overture_asa_blue_1000_175_c`|`{color_name}`|`Blue`|{"source_file": "overture.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_asa_asablue_1000_175_c": 1.07,
    "overture_asa_blue_1000_175_c": 1.14
  },
  "spool_weight": {
    "overture_asa_asablue_1000_175_c": 173,
    "overture_asa_blue_1000_175_c": 132
  },
  "color_hex": {
    "overture_asa_asablue_1000_175_c": "0353BA",
    "overture_asa_blue_1000_175_c": "002979"
  },
  "extruder_temp_range": {
    "overture_asa_asablue_1000_175_c": [
      235,
      260
    ],
    "overture_asa_blue_1000_175_c": [
      240,
      270
    ]
  },
  "bed_temp_range": {
    "overture_asa_asablue_1000_175_c": [
      90,
      110
    ],
    "overture_asa_blue_1000_175_c": [
      70,
      95
    ]
  }
}
```

### OV017: dup-44ab6a34236e1e0601429580f814d31309d953166a12b3b4f610110104b25b29

Status: APPROVED; survivor `overture_asa_brown_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_asa_asabrown_1000_175_c`|`ASA {color_name}`|`Brown`|{"source_file": "overture.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|
|`overture_asa_brown_1000_175_c`|`{color_name}`|`Brown`|{"source_file": "overture.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_asa_asabrown_1000_175_c": 1.07,
    "overture_asa_brown_1000_175_c": 1.14
  },
  "spool_weight": {
    "overture_asa_asabrown_1000_175_c": 173,
    "overture_asa_brown_1000_175_c": 132
  },
  "color_hex": {
    "overture_asa_asabrown_1000_175_c": "926043",
    "overture_asa_brown_1000_175_c": "785F53"
  },
  "extruder_temp_range": {
    "overture_asa_asabrown_1000_175_c": [
      235,
      260
    ],
    "overture_asa_brown_1000_175_c": [
      240,
      270
    ]
  },
  "bed_temp_range": {
    "overture_asa_asabrown_1000_175_c": [
      90,
      110
    ],
    "overture_asa_brown_1000_175_c": [
      70,
      95
    ]
  }
}
```

### OV018: dup-3306ec9aef10b106c0a8187cc0d8ccb6f57989430b10720bf68d6834dd36f317

Status: APPROVED; survivor `overture_asa_diamondblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_asa_asadiamondblue_1000_175_c`|`ASA {color_name}`|`Diamond Blue`|{"source_file": "overture.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|
|`overture_asa_diamondblue_1000_175_c`|`{color_name}`|`Diamond Blue`|{"source_file": "overture.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_asa_asadiamondblue_1000_175_c": 1.07,
    "overture_asa_diamondblue_1000_175_c": 1.14
  },
  "spool_weight": {
    "overture_asa_asadiamondblue_1000_175_c": 173,
    "overture_asa_diamondblue_1000_175_c": 132
  },
  "color_hex": {
    "overture_asa_asadiamondblue_1000_175_c": "2C3294",
    "overture_asa_diamondblue_1000_175_c": "324485"
  },
  "extruder_temp_range": {
    "overture_asa_asadiamondblue_1000_175_c": [
      235,
      260
    ],
    "overture_asa_diamondblue_1000_175_c": [
      240,
      270
    ]
  },
  "bed_temp_range": {
    "overture_asa_asadiamondblue_1000_175_c": [
      90,
      110
    ],
    "overture_asa_diamondblue_1000_175_c": [
      70,
      95
    ]
  },
  "pattern": {
    "overture_asa_asadiamondblue_1000_175_c": null,
    "overture_asa_diamondblue_1000_175_c": "sparkle"
  }
}
```

### OV019: dup-693136eeb2e9209f2e68d478e10bf6a9c1b2f4a05cb35a8961982ff08fc4ce49

Status: APPROVED; survivor `overture_asa_diamondgreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_asa_asadiamondgreen_1000_175_c`|`ASA {color_name}`|`Diamond Green`|{"source_file": "overture.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|
|`overture_asa_diamondgreen_1000_175_c`|`{color_name}`|`Diamond Green`|{"source_file": "overture.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_asa_asadiamondgreen_1000_175_c": 1.07,
    "overture_asa_diamondgreen_1000_175_c": 1.14
  },
  "spool_weight": {
    "overture_asa_asadiamondgreen_1000_175_c": 173,
    "overture_asa_diamondgreen_1000_175_c": 132
  },
  "extruder_temp_range": {
    "overture_asa_asadiamondgreen_1000_175_c": [
      235,
      260
    ],
    "overture_asa_diamondgreen_1000_175_c": [
      240,
      270
    ]
  },
  "bed_temp_range": {
    "overture_asa_asadiamondgreen_1000_175_c": [
      90,
      110
    ],
    "overture_asa_diamondgreen_1000_175_c": [
      70,
      95
    ]
  },
  "pattern": {
    "overture_asa_asadiamondgreen_1000_175_c": null,
    "overture_asa_diamondgreen_1000_175_c": "sparkle"
  }
}
```

### OV020: dup-d22f2e86369b01e2c080b55a44e3fa8e700c07ed461a950a87d47b1a57a60198

Status: APPROVED; survivor `overture_asa_diamondred_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_asa_asadiamondred_1000_175_c`|`ASA {color_name}`|`Diamond Red`|{"source_file": "overture.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|
|`overture_asa_diamondred_1000_175_c`|`{color_name}`|`Diamond Red`|{"source_file": "overture.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_asa_asadiamondred_1000_175_c": 1.07,
    "overture_asa_diamondred_1000_175_c": 1.14
  },
  "spool_weight": {
    "overture_asa_asadiamondred_1000_175_c": 173,
    "overture_asa_diamondred_1000_175_c": 132
  },
  "color_hex": {
    "overture_asa_asadiamondred_1000_175_c": "D32E1A",
    "overture_asa_diamondred_1000_175_c": "C01616"
  },
  "extruder_temp_range": {
    "overture_asa_asadiamondred_1000_175_c": [
      235,
      260
    ],
    "overture_asa_diamondred_1000_175_c": [
      240,
      270
    ]
  },
  "bed_temp_range": {
    "overture_asa_asadiamondred_1000_175_c": [
      90,
      110
    ],
    "overture_asa_diamondred_1000_175_c": [
      70,
      95
    ]
  },
  "pattern": {
    "overture_asa_asadiamondred_1000_175_c": null,
    "overture_asa_diamondred_1000_175_c": "sparkle"
  }
}
```

### OV021: dup-8a2b00c3e2744dc2c019b1769fc73f767b6cf718d14fd68d57b729ccd147f744

Status: APPROVED; survivor `overture_asa_gray_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_asa_asagray_1000_175_c`|`ASA {color_name}`|`Gray`|{"source_file": "overture.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|
|`overture_asa_gray_1000_175_c`|`{color_name}`|`Gray`|{"source_file": "overture.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_asa_asagray_1000_175_c": 1.07,
    "overture_asa_gray_1000_175_c": 1.14
  },
  "spool_weight": {
    "overture_asa_asagray_1000_175_c": 173,
    "overture_asa_gray_1000_175_c": 132
  },
  "color_hex": {
    "overture_asa_asagray_1000_175_c": "BDC8C8",
    "overture_asa_gray_1000_175_c": "B5B9BA"
  },
  "extruder_temp_range": {
    "overture_asa_asagray_1000_175_c": [
      235,
      260
    ],
    "overture_asa_gray_1000_175_c": [
      240,
      270
    ]
  },
  "bed_temp_range": {
    "overture_asa_asagray_1000_175_c": [
      90,
      110
    ],
    "overture_asa_gray_1000_175_c": [
      70,
      95
    ]
  }
}
```

### OV022: dup-2635c810154a1e40b9d42f6a036e16f3f29f047be612d7fca35a3570ff5434ef

Status: APPROVED; survivor `overture_asa_green_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_asa_asagreen_1000_175_c`|`ASA {color_name}`|`Green`|{"source_file": "overture.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|
|`overture_asa_green_1000_175_c`|`{color_name}`|`Green`|{"source_file": "overture.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_asa_asagreen_1000_175_c": 1.07,
    "overture_asa_green_1000_175_c": 1.14
  },
  "spool_weight": {
    "overture_asa_asagreen_1000_175_c": 173,
    "overture_asa_green_1000_175_c": 132
  },
  "color_hex": {
    "overture_asa_asagreen_1000_175_c": "3D9441",
    "overture_asa_green_1000_175_c": "01AA5E"
  },
  "extruder_temp_range": {
    "overture_asa_asagreen_1000_175_c": [
      235,
      260
    ],
    "overture_asa_green_1000_175_c": [
      240,
      270
    ]
  },
  "bed_temp_range": {
    "overture_asa_asagreen_1000_175_c": [
      90,
      110
    ],
    "overture_asa_green_1000_175_c": [
      70,
      95
    ]
  }
}
```

### OV023: dup-cd47c93b14fc6ab7c20e1aa2ab575b3797a0155cd3bdfd2491c9de0fcac9cd4b

Status: APPROVED; survivor `overture_asa_natural_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_asa_asanatural_1000_175_c`|`ASA {color_name}`|`Natural`|{"source_file": "overture.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|
|`overture_asa_natural_1000_175_c`|`{color_name}`|`Natural`|{"source_file": "overture.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_asa_asanatural_1000_175_c": 1.07,
    "overture_asa_natural_1000_175_c": 1.14
  },
  "spool_weight": {
    "overture_asa_asanatural_1000_175_c": 173,
    "overture_asa_natural_1000_175_c": 132
  },
  "color_hex": {
    "overture_asa_asanatural_1000_175_c": "D9D8DE",
    "overture_asa_natural_1000_175_c": "F1E6B3"
  },
  "extruder_temp_range": {
    "overture_asa_asanatural_1000_175_c": [
      235,
      260
    ],
    "overture_asa_natural_1000_175_c": [
      240,
      270
    ]
  },
  "bed_temp_range": {
    "overture_asa_asanatural_1000_175_c": [
      90,
      110
    ],
    "overture_asa_natural_1000_175_c": [
      70,
      95
    ]
  }
}
```

### OV024: dup-c1680487dd4edcdfa89f65ec37bcebd4a1067af07813398ec2f29b14c2aad7f5

Status: APPROVED; survivor `overture_asa_olivegreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_asa_asaolivegreen_1000_175_c`|`ASA {color_name}`|`Olive Green`|{"source_file": "overture.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|
|`overture_asa_olivegreen_1000_175_c`|`{color_name}`|`Olive Green`|{"source_file": "overture.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_asa_asaolivegreen_1000_175_c": 1.07,
    "overture_asa_olivegreen_1000_175_c": 1.14
  },
  "spool_weight": {
    "overture_asa_asaolivegreen_1000_175_c": 173,
    "overture_asa_olivegreen_1000_175_c": 132
  },
  "color_hex": {
    "overture_asa_asaolivegreen_1000_175_c": "857C00",
    "overture_asa_olivegreen_1000_175_c": "6B7550"
  },
  "extruder_temp_range": {
    "overture_asa_asaolivegreen_1000_175_c": [
      235,
      260
    ],
    "overture_asa_olivegreen_1000_175_c": [
      240,
      270
    ]
  },
  "bed_temp_range": {
    "overture_asa_asaolivegreen_1000_175_c": [
      90,
      110
    ],
    "overture_asa_olivegreen_1000_175_c": [
      70,
      95
    ]
  }
}
```

### OV025: dup-c319a8608fb985fb52d36895e6941f07a57d2e94bcc613b5fca664de20e3401e

Status: APPROVED; survivor `overture_asa_orange_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_asa_asaorange_1000_175_c`|`ASA {color_name}`|`Orange`|{"source_file": "overture.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|
|`overture_asa_orange_1000_175_c`|`{color_name}`|`Orange`|{"source_file": "overture.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_asa_asaorange_1000_175_c": 1.07,
    "overture_asa_orange_1000_175_c": 1.14
  },
  "spool_weight": {
    "overture_asa_asaorange_1000_175_c": 173,
    "overture_asa_orange_1000_175_c": 132
  },
  "color_hex": {
    "overture_asa_asaorange_1000_175_c": "FF8E24",
    "overture_asa_orange_1000_175_c": "FF9A40"
  },
  "extruder_temp_range": {
    "overture_asa_asaorange_1000_175_c": [
      235,
      260
    ],
    "overture_asa_orange_1000_175_c": [
      240,
      270
    ]
  },
  "bed_temp_range": {
    "overture_asa_asaorange_1000_175_c": [
      90,
      110
    ],
    "overture_asa_orange_1000_175_c": [
      70,
      95
    ]
  }
}
```

### OV026: dup-f0434445309e98f6f0b4fa9943c1311e9e361c60b911405c766040b118f1416f

Status: APPROVED; survivor `overture_asa_red_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_asa_asared_1000_175_c`|`ASA {color_name}`|`Red`|{"source_file": "overture.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|
|`overture_asa_red_1000_175_c`|`{color_name}`|`Red`|{"source_file": "overture.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_asa_asared_1000_175_c": 1.07,
    "overture_asa_red_1000_175_c": 1.14
  },
  "spool_weight": {
    "overture_asa_asared_1000_175_c": 173,
    "overture_asa_red_1000_175_c": 132
  },
  "color_hex": {
    "overture_asa_asared_1000_175_c": "E60000",
    "overture_asa_red_1000_175_c": "AF251E"
  },
  "extruder_temp_range": {
    "overture_asa_asared_1000_175_c": [
      235,
      260
    ],
    "overture_asa_red_1000_175_c": [
      240,
      270
    ]
  },
  "bed_temp_range": {
    "overture_asa_asared_1000_175_c": [
      90,
      110
    ],
    "overture_asa_red_1000_175_c": [
      70,
      95
    ]
  }
}
```

### OV027: dup-9af656bd57d333a76179cae2aee931e66b4cb4a34be983b14d9c05c5f605fec9

Status: APPROVED; survivor `overture_asa_white_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_asa_asawhite_1000_175_c`|`ASA {color_name}`|`White`|{"source_file": "overture.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|
|`overture_asa_white_1000_175_c`|`{color_name}`|`White`|{"source_file": "overture.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_asa_asawhite_1000_175_c": 1.07,
    "overture_asa_white_1000_175_c": 1.14
  },
  "spool_weight": {
    "overture_asa_asawhite_1000_175_c": 173,
    "overture_asa_white_1000_175_c": 132
  },
  "extruder_temp_range": {
    "overture_asa_asawhite_1000_175_c": [
      235,
      260
    ],
    "overture_asa_white_1000_175_c": [
      240,
      270
    ]
  },
  "bed_temp_range": {
    "overture_asa_asawhite_1000_175_c": [
      90,
      110
    ],
    "overture_asa_white_1000_175_c": [
      70,
      95
    ]
  }
}
```

### OV028: dup-4db9a48d6b2073a2edfdfa39c7fc5afbe801f2674b8ce7842778552b67b6a56b

Status: APPROVED; survivor `overture_asa_yellow_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_asa_asayellow_1000_175_c`|`ASA {color_name}`|`Yellow`|{"source_file": "overture.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|
|`overture_asa_yellow_1000_175_c`|`{color_name}`|`Yellow`|{"source_file": "overture.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_asa_asayellow_1000_175_c": 1.07,
    "overture_asa_yellow_1000_175_c": 1.14
  },
  "spool_weight": {
    "overture_asa_asayellow_1000_175_c": 173,
    "overture_asa_yellow_1000_175_c": 132
  },
  "color_hex": {
    "overture_asa_asayellow_1000_175_c": "EEEA44",
    "overture_asa_yellow_1000_175_c": "FFE802"
  },
  "extruder_temp_range": {
    "overture_asa_asayellow_1000_175_c": [
      235,
      260
    ],
    "overture_asa_yellow_1000_175_c": [
      240,
      270
    ]
  },
  "bed_temp_range": {
    "overture_asa_asayellow_1000_175_c": [
      90,
      110
    ],
    "overture_asa_yellow_1000_175_c": [
      70,
      95
    ]
  }
}
```

### OV029: dup-e41392609abb8dd701f9ee868c94c89cda0c5dfc6320e86cbac1bc30bd688213

Status: APPROVED; survivor `overture_petg_armygreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_armygreen_1000_175_c`|`{color_name}`|`Army green`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_petg_petgarmygreen_1000_175_c`|`PETG {color_name}`|`Army Green`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_armygreen_1000_175_c": 1.25,
    "overture_petg_petgarmygreen_1000_175_c": 1.27
  },
  "spool_weight": {
    "overture_petg_armygreen_1000_175_c": 132,
    "overture_petg_petgarmygreen_1000_175_c": 173
  },
  "extruder_temp_range": {
    "overture_petg_armygreen_1000_175_c": [
      230,
      250
    ],
    "overture_petg_petgarmygreen_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_armygreen_1000_175_c": [
      80,
      90
    ],
    "overture_petg_petgarmygreen_1000_175_c": [
      70,
      90
    ]
  }
}
```

### OV030: dup-b9136ebbf7e0c698b8774808763e188479f26db04687cac204b6cc17f190c715

Status: APPROVED; survivor `overture_petg_black_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_black_1000_175_c`|`{color_name}`|`Black`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_petg_petgblack_1000_175_c`|`PETG {color_name}`|`Black`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_black_1000_175_c": 1.25,
    "overture_petg_petgblack_1000_175_c": 1.27
  },
  "spool_weight": {
    "overture_petg_black_1000_175_c": 132,
    "overture_petg_petgblack_1000_175_c": 173
  },
  "extruder_temp_range": {
    "overture_petg_black_1000_175_c": [
      230,
      250
    ],
    "overture_petg_petgblack_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_black_1000_175_c": [
      80,
      90
    ],
    "overture_petg_petgblack_1000_175_c": [
      70,
      90
    ]
  }
}
```

### OV031: dup-94cc01a07ce6324562d74ab4c6a392d0ede1bc2a9363953aeac81b564bf63b0e

Status: APPROVED; survivor `overture_petg_blue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_blue_1000_175_c`|`{color_name}`|`Blue`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_petg_petgblue_1000_175_c`|`PETG {color_name}`|`Blue`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_blue_1000_175_c": 1.25,
    "overture_petg_petgblue_1000_175_c": 1.27
  },
  "spool_weight": {
    "overture_petg_blue_1000_175_c": 132,
    "overture_petg_petgblue_1000_175_c": 173
  },
  "color_hex": {
    "overture_petg_blue_1000_175_c": "034E89",
    "overture_petg_petgblue_1000_175_c": "0E21AE"
  },
  "extruder_temp_range": {
    "overture_petg_blue_1000_175_c": [
      230,
      250
    ],
    "overture_petg_petgblue_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_blue_1000_175_c": [
      80,
      90
    ],
    "overture_petg_petgblue_1000_175_c": [
      70,
      90
    ]
  }
}
```

### OV032: dup-6f04820343d34e9bb44fa48ba3535c7be2b3a7d76d4a6f2e6f5d4aa9c427922a

Status: APPROVED; survivor `overture_petg_brown_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_brown_1000_175_c`|`{color_name}`|`Brown`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_petg_petgbrown_1000_175_c`|`PETG {color_name}`|`Brown`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_brown_1000_175_c": 1.25,
    "overture_petg_petgbrown_1000_175_c": 1.27
  },
  "spool_weight": {
    "overture_petg_brown_1000_175_c": 132,
    "overture_petg_petgbrown_1000_175_c": 173
  },
  "extruder_temp_range": {
    "overture_petg_brown_1000_175_c": [
      230,
      250
    ],
    "overture_petg_petgbrown_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_brown_1000_175_c": [
      80,
      90
    ],
    "overture_petg_petgbrown_1000_175_c": [
      70,
      90
    ]
  }
}
```

### OV033: dup-2ce144c0f53d231fabc4f709b1397e813813087568e24c6269e11f02db97f789

Status: APPROVED; survivor `overture_petg_digitalblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_digitalblue_1000_175_c`|`{color_name}`|`Digital Blue`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_petg_petgdigitalblue_1000_175_c`|`PETG {color_name}`|`Digital Blue`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_digitalblue_1000_175_c": 1.25,
    "overture_petg_petgdigitalblue_1000_175_c": 1.27
  },
  "spool_weight": {
    "overture_petg_digitalblue_1000_175_c": 132,
    "overture_petg_petgdigitalblue_1000_175_c": 173
  },
  "extruder_temp_range": {
    "overture_petg_digitalblue_1000_175_c": [
      230,
      250
    ],
    "overture_petg_petgdigitalblue_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_digitalblue_1000_175_c": [
      80,
      90
    ],
    "overture_petg_petgdigitalblue_1000_175_c": [
      70,
      90
    ]
  }
}
```

### OV034: dup-1f49248cd32a390bce454f7aff7c742886e91492d46f36377329acd586600301

Status: APPROVED; survivor `overture_petg_gold_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_gold_1000_175_c`|`{color_name}`|`Gold`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_petg_petggold_1000_175_c`|`PETG {color_name}`|`Gold`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_gold_1000_175_c": 1.25,
    "overture_petg_petggold_1000_175_c": 1.27
  },
  "spool_weight": {
    "overture_petg_gold_1000_175_c": 132,
    "overture_petg_petggold_1000_175_c": 173
  },
  "extruder_temp_range": {
    "overture_petg_gold_1000_175_c": [
      230,
      250
    ],
    "overture_petg_petggold_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_gold_1000_175_c": [
      80,
      90
    ],
    "overture_petg_petggold_1000_175_c": [
      70,
      90
    ]
  }
}
```

### OV035: dup-857af0e90d228d4c9d1ca3498bd4c945b6327eeaa347993bdde06840bab0e74e

Status: APPROVED; survivor `overture_petg_grassgreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_grassgreen_1000_175_c`|`{color_name}`|`Grass Green`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_petg_petggrassgreen_1000_175_c`|`PETG {color_name}`|`Grass Green`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_grassgreen_1000_175_c": 1.25,
    "overture_petg_petggrassgreen_1000_175_c": 1.27
  },
  "spool_weight": {
    "overture_petg_grassgreen_1000_175_c": 132,
    "overture_petg_petggrassgreen_1000_175_c": 173
  },
  "color_hex": {
    "overture_petg_grassgreen_1000_175_c": "C4D802",
    "overture_petg_petggrassgreen_1000_175_c": "61C680"
  },
  "extruder_temp_range": {
    "overture_petg_grassgreen_1000_175_c": [
      230,
      250
    ],
    "overture_petg_petggrassgreen_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_grassgreen_1000_175_c": [
      80,
      90
    ],
    "overture_petg_petggrassgreen_1000_175_c": [
      70,
      90
    ]
  }
}
```

### OV036: dup-b8b7ab80fe56186eea9229ee405a26e7e452d681b54ca87eea8cf93f1904af8b

Status: APPROVED; survivor `overture_petg_green_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_green_1000_175_c`|`{color_name}`|`Green`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_petg_petggreen_1000_175_c`|`PETG {color_name}`|`Green`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_green_1000_175_c": 1.25,
    "overture_petg_petggreen_1000_175_c": 1.27
  },
  "spool_weight": {
    "overture_petg_green_1000_175_c": 132,
    "overture_petg_petggreen_1000_175_c": 173
  },
  "color_hex": {
    "overture_petg_green_1000_175_c": "38AF69",
    "overture_petg_petggreen_1000_175_c": "089A45"
  },
  "extruder_temp_range": {
    "overture_petg_green_1000_175_c": [
      230,
      250
    ],
    "overture_petg_petggreen_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_green_1000_175_c": [
      80,
      90
    ],
    "overture_petg_petggreen_1000_175_c": [
      70,
      90
    ]
  }
}
```

### OV037: dup-7cec91ebf0d5eeef01769021e17b1bfd0089fcfb472242e131ceda00df808224

Status: APPROVED; survivor `overture_petg_lightgray_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_lightgray_1000_175_c`|`{color_name}`|`Light Gray`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_petg_petglightgray_1000_175_c`|`PETG {color_name}`|`Light Gray`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_lightgray_1000_175_c": 1.25,
    "overture_petg_petglightgray_1000_175_c": 1.27
  },
  "spool_weight": {
    "overture_petg_lightgray_1000_175_c": 132,
    "overture_petg_petglightgray_1000_175_c": 173
  },
  "color_hex": {
    "overture_petg_lightgray_1000_175_c": "D5D8DD",
    "overture_petg_petglightgray_1000_175_c": "949A9E"
  },
  "extruder_temp_range": {
    "overture_petg_lightgray_1000_175_c": [
      230,
      250
    ],
    "overture_petg_petglightgray_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_lightgray_1000_175_c": [
      80,
      90
    ],
    "overture_petg_petglightgray_1000_175_c": [
      70,
      90
    ]
  }
}
```

### OV038: dup-2c58f37830f14e92ef33be8612d4e40a216fc2b1afc6d7065f90deabb8050637

Status: APPROVED; survivor `overture_petg_magenta_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_magenta_1000_175_c`|`{color_name}`|`Magenta`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_petg_petgmagenta_1000_175_c`|`PETG {color_name}`|`Magenta`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_magenta_1000_175_c": 1.25,
    "overture_petg_petgmagenta_1000_175_c": 1.27
  },
  "spool_weight": {
    "overture_petg_magenta_1000_175_c": 132,
    "overture_petg_petgmagenta_1000_175_c": 173
  },
  "extruder_temp_range": {
    "overture_petg_magenta_1000_175_c": [
      230,
      250
    ],
    "overture_petg_petgmagenta_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_magenta_1000_175_c": [
      80,
      90
    ],
    "overture_petg_petgmagenta_1000_175_c": [
      70,
      90
    ]
  }
}
```

### OV039: dup-3d96415e4722e29b35109b1d048a244404bd06a7055128fcc5dcfb387530170d

Status: APPROVED; survivor `overture_petg_orange_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_orange_1000_175_c`|`{color_name}`|`Orange`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_petg_petgorange_1000_175_c`|`PETG {color_name}`|`Orange`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_orange_1000_175_c": 1.25,
    "overture_petg_petgorange_1000_175_c": 1.27
  },
  "spool_weight": {
    "overture_petg_orange_1000_175_c": 132,
    "overture_petg_petgorange_1000_175_c": 173
  },
  "extruder_temp_range": {
    "overture_petg_orange_1000_175_c": [
      230,
      250
    ],
    "overture_petg_petgorange_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_orange_1000_175_c": [
      80,
      90
    ],
    "overture_petg_petgorange_1000_175_c": [
      70,
      90
    ]
  }
}
```

### OV040: dup-84b11aa3961db4fb1991d0798ebb4153d2de138e1dce53cccc0ee4d9fa768415

Status: APPROVED; survivor `overture_petg_pink_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_petgpink_1000_175_c`|`PETG {color_name}`|`Pink`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|
|`overture_petg_pink_1000_175_c`|`{color_name}`|`Pink`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_petgpink_1000_175_c": 1.27,
    "overture_petg_pink_1000_175_c": 1.25
  },
  "spool_weight": {
    "overture_petg_petgpink_1000_175_c": 173,
    "overture_petg_pink_1000_175_c": 132
  },
  "extruder_temp_range": {
    "overture_petg_petgpink_1000_175_c": [
      220,
      250
    ],
    "overture_petg_pink_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_petgpink_1000_175_c": [
      70,
      90
    ],
    "overture_petg_pink_1000_175_c": [
      80,
      90
    ]
  }
}
```

### OV041: dup-0318833ad45395768f2ec422c826161d224c7038f64400e77419a97fa24cd409

Status: APPROVED; survivor `overture_petg_purple_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_petgpurple_1000_175_c`|`PETG {color_name}`|`Purple`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|
|`overture_petg_purple_1000_175_c`|`{color_name}`|`Purple`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_petgpurple_1000_175_c": 1.27,
    "overture_petg_purple_1000_175_c": 1.25
  },
  "spool_weight": {
    "overture_petg_petgpurple_1000_175_c": 173,
    "overture_petg_purple_1000_175_c": 132
  },
  "extruder_temp_range": {
    "overture_petg_petgpurple_1000_175_c": [
      220,
      250
    ],
    "overture_petg_purple_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_petgpurple_1000_175_c": [
      70,
      90
    ],
    "overture_petg_purple_1000_175_c": [
      80,
      90
    ]
  }
}
```

### OV042: dup-f2dfbc133275bef19408a699c594311ff23267bbd448e6e1a6da1214dfc97697

Status: APPROVED; survivor `overture_petg_red_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_petgred_1000_175_c`|`PETG {color_name}`|`Red`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|
|`overture_petg_red_1000_175_c`|`{color_name}`|`Red`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_petgred_1000_175_c": 1.27,
    "overture_petg_red_1000_175_c": 1.25
  },
  "spool_weight": {
    "overture_petg_petgred_1000_175_c": 173,
    "overture_petg_red_1000_175_c": 132
  },
  "color_hex": {
    "overture_petg_petgred_1000_175_c": "E72F1D",
    "overture_petg_red_1000_175_c": "FF0000"
  },
  "extruder_temp_range": {
    "overture_petg_petgred_1000_175_c": [
      220,
      250
    ],
    "overture_petg_red_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_petgred_1000_175_c": [
      70,
      90
    ],
    "overture_petg_red_1000_175_c": [
      80,
      90
    ]
  }
}
```

### OV043: dup-1471f832d16efca49de875fca223db123d750d29384a3f930b0dbec831fdcaed

Status: APPROVED; survivor `overture_petg_rockwhite_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_petgrockwhite_1000_175_c`|`PETG {color_name}`|`Rock White`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|
|`overture_petg_rockwhite_1000_175_c`|`{color_name}`|`Rock White`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_petgrockwhite_1000_175_c": 1.27,
    "overture_petg_rockwhite_1000_175_c": 1.25
  },
  "spool_weight": {
    "overture_petg_petgrockwhite_1000_175_c": 173,
    "overture_petg_rockwhite_1000_175_c": 132
  },
  "color_hex": {
    "overture_petg_petgrockwhite_1000_175_c": "EDF0F2",
    "overture_petg_rockwhite_1000_175_c": "F5F5F4"
  },
  "extruder_temp_range": {
    "overture_petg_petgrockwhite_1000_175_c": [
      220,
      250
    ],
    "overture_petg_rockwhite_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_petgrockwhite_1000_175_c": [
      70,
      90
    ],
    "overture_petg_rockwhite_1000_175_c": [
      80,
      90
    ]
  },
  "pattern": {
    "overture_petg_petgrockwhite_1000_175_c": null,
    "overture_petg_rockwhite_1000_175_c": "marble"
  }
}
```

### OV044: dup-d0ebd0460034bdfe7a836c1dbfb18a86621e049feffefdc17ea259d7890a99d1

Status: APPROVED; survivor `overture_petg_spacegray_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_petgspacegray_1000_175_c`|`PETG {color_name}`|`Space Gray`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|
|`overture_petg_spacegray_1000_175_c`|`{color_name}`|`Space Gray`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_petgspacegray_1000_175_c": 1.27,
    "overture_petg_spacegray_1000_175_c": 1.25
  },
  "spool_weight": {
    "overture_petg_petgspacegray_1000_175_c": 173,
    "overture_petg_spacegray_1000_175_c": 132
  },
  "color_hex": {
    "overture_petg_petgspacegray_1000_175_c": "7A838E",
    "overture_petg_spacegray_1000_175_c": "76797D"
  },
  "extruder_temp_range": {
    "overture_petg_petgspacegray_1000_175_c": [
      220,
      250
    ],
    "overture_petg_spacegray_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_petgspacegray_1000_175_c": [
      70,
      90
    ],
    "overture_petg_spacegray_1000_175_c": [
      80,
      90
    ]
  }
}
```

### OV045: dup-84e9eab61915fc9d7d93832b995eeecd7adb5deb8ced831bcfecb658fb815167

Status: APPROVED; survivor `overture_petg_sparkleblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_petgsparkleblue_1000_175_c`|`PETG {color_name}`|`Sparkle Blue`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|
|`overture_petg_sparkleblue_1000_175_c`|`{color_name}`|`Sparkle Blue`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_petgsparkleblue_1000_175_c": 1.27,
    "overture_petg_sparkleblue_1000_175_c": 1.25
  },
  "spool_weight": {
    "overture_petg_petgsparkleblue_1000_175_c": 173,
    "overture_petg_sparkleblue_1000_175_c": 132
  },
  "extruder_temp_range": {
    "overture_petg_petgsparkleblue_1000_175_c": [
      220,
      250
    ],
    "overture_petg_sparkleblue_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_petgsparkleblue_1000_175_c": [
      70,
      90
    ],
    "overture_petg_sparkleblue_1000_175_c": [
      80,
      90
    ]
  },
  "pattern": {
    "overture_petg_petgsparkleblue_1000_175_c": null,
    "overture_petg_sparkleblue_1000_175_c": "sparkle"
  }
}
```

### OV046: dup-3f5c549379ae148e4e7d493e732f1652beac1611f68479c820c11438c3c0d8ba

Status: APPROVED; survivor `overture_petg_starryblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_petgstarryblue_1000_175_c`|`PETG {color_name}`|`Starry Blue`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|
|`overture_petg_starryblue_1000_175_c`|`{color_name}`|`Starry Blue`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_petgstarryblue_1000_175_c": 1.27,
    "overture_petg_starryblue_1000_175_c": 1.25
  },
  "spool_weight": {
    "overture_petg_petgstarryblue_1000_175_c": 173,
    "overture_petg_starryblue_1000_175_c": 132
  },
  "color_hex": {
    "overture_petg_petgstarryblue_1000_175_c": "492972",
    "overture_petg_starryblue_1000_175_c": "142B4B"
  },
  "extruder_temp_range": {
    "overture_petg_petgstarryblue_1000_175_c": [
      220,
      250
    ],
    "overture_petg_starryblue_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_petgstarryblue_1000_175_c": [
      70,
      90
    ],
    "overture_petg_starryblue_1000_175_c": [
      80,
      90
    ]
  }
}
```

### OV047: dup-98e01c4db33dee24d8f895bda2d8e86619eaf0db383df7a4aa29397f26f61215

Status: APPROVED; survivor `overture_petg_transparent_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_petgtransparent_1000_175_c`|`PETG {color_name}`|`Transparent`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|
|`overture_petg_transparent_1000_175_c`|`{color_name}`|`Transparent`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_petgtransparent_1000_175_c": 1.27,
    "overture_petg_transparent_1000_175_c": 1.25
  },
  "spool_weight": {
    "overture_petg_petgtransparent_1000_175_c": 173,
    "overture_petg_transparent_1000_175_c": 132
  },
  "color_hex": {
    "overture_petg_petgtransparent_1000_175_c": "F5F5F4",
    "overture_petg_transparent_1000_175_c": "FFFFFF"
  },
  "extruder_temp_range": {
    "overture_petg_petgtransparent_1000_175_c": [
      220,
      250
    ],
    "overture_petg_transparent_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_petgtransparent_1000_175_c": [
      70,
      90
    ],
    "overture_petg_transparent_1000_175_c": [
      80,
      90
    ]
  }
}
```

### OV048: dup-ac1358d1038fc705b4de408dc784e7260dd4406a17f1eaea6e6ba24a950be17c

Status: APPROVED; survivor `overture_petg_transparentblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_petgtransparentblue_1000_175_c`|`PETG {color_name}`|`Transparent Blue`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|
|`overture_petg_transparentblue_1000_175_c`|`{color_name}`|`Transparent Blue`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_petgtransparentblue_1000_175_c": 1.27,
    "overture_petg_transparentblue_1000_175_c": 1.25
  },
  "spool_weight": {
    "overture_petg_petgtransparentblue_1000_175_c": 173,
    "overture_petg_transparentblue_1000_175_c": 132
  },
  "color_hex": {
    "overture_petg_petgtransparentblue_1000_175_c": "09048E",
    "overture_petg_transparentblue_1000_175_c": "0933a5"
  },
  "extruder_temp_range": {
    "overture_petg_petgtransparentblue_1000_175_c": [
      220,
      250
    ],
    "overture_petg_transparentblue_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_petgtransparentblue_1000_175_c": [
      70,
      90
    ],
    "overture_petg_transparentblue_1000_175_c": [
      80,
      90
    ]
  }
}
```

### OV049: dup-fef8f515e0e004f531657b06b3e7589e8b446708c8de39d3c2ae3f7e823ac390

Status: APPROVED; survivor `overture_petg_transparentgreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_petgtransparentgreen_1000_175_c`|`PETG {color_name}`|`Transparent Green`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|
|`overture_petg_transparentgreen_1000_175_c`|`{color_name}`|`Transparent Green`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_petgtransparentgreen_1000_175_c": 1.27,
    "overture_petg_transparentgreen_1000_175_c": 1.25
  },
  "spool_weight": {
    "overture_petg_petgtransparentgreen_1000_175_c": 173,
    "overture_petg_transparentgreen_1000_175_c": 132
  },
  "color_hex": {
    "overture_petg_petgtransparentgreen_1000_175_c": "089A45",
    "overture_petg_transparentgreen_1000_175_c": "29b646"
  },
  "extruder_temp_range": {
    "overture_petg_petgtransparentgreen_1000_175_c": [
      220,
      250
    ],
    "overture_petg_transparentgreen_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_petgtransparentgreen_1000_175_c": [
      70,
      90
    ],
    "overture_petg_transparentgreen_1000_175_c": [
      80,
      90
    ]
  }
}
```

### OV050: dup-3c0e0094dcc921c05a10630474ca0bd5583660d1bba2fdd04ec2a043e3203270

Status: APPROVED; survivor `overture_petg_transparentred_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_petgtransparentred_1000_175_c`|`PETG {color_name}`|`Transparent Red`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|
|`overture_petg_transparentred_1000_175_c`|`{color_name}`|`Transparent Red`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_petgtransparentred_1000_175_c": 1.27,
    "overture_petg_transparentred_1000_175_c": 1.25
  },
  "spool_weight": {
    "overture_petg_petgtransparentred_1000_175_c": 173,
    "overture_petg_transparentred_1000_175_c": 132
  },
  "color_hex": {
    "overture_petg_petgtransparentred_1000_175_c": "B7293E",
    "overture_petg_transparentred_1000_175_c": "FF0000"
  },
  "extruder_temp_range": {
    "overture_petg_petgtransparentred_1000_175_c": [
      220,
      250
    ],
    "overture_petg_transparentred_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_petgtransparentred_1000_175_c": [
      70,
      90
    ],
    "overture_petg_transparentred_1000_175_c": [
      80,
      90
    ]
  }
}
```

### OV051: dup-2ed055154e5581826371fe8c2c648b1b4f31b8016ba1f889847f00983360aec6

Status: APPROVED; survivor `overture_petg_white_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_petgwhite_1000_175_c`|`PETG {color_name}`|`White`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|
|`overture_petg_white_1000_175_c`|`{color_name}`|`White`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_petgwhite_1000_175_c": 1.27,
    "overture_petg_white_1000_175_c": 1.25
  },
  "spool_weight": {
    "overture_petg_petgwhite_1000_175_c": 173,
    "overture_petg_white_1000_175_c": 132
  },
  "extruder_temp_range": {
    "overture_petg_petgwhite_1000_175_c": [
      220,
      250
    ],
    "overture_petg_white_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_petgwhite_1000_175_c": [
      70,
      90
    ],
    "overture_petg_white_1000_175_c": [
      80,
      90
    ]
  }
}
```

### OV052: dup-a8b37c38a8fca1d30d890bccbe016de10499e84c4fd0ad9194d072819f2e018f

Status: APPROVED; survivor `overture_petg_yellow_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_petg_petgyellow_1000_175_c`|`PETG {color_name}`|`Yellow`|{"source_file": "overture.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|
|`overture_petg_yellow_1000_175_c`|`{color_name}`|`Yellow`|{"source_file": "overture.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_petg_petgyellow_1000_175_c": 1.27,
    "overture_petg_yellow_1000_175_c": 1.25
  },
  "spool_weight": {
    "overture_petg_petgyellow_1000_175_c": 173,
    "overture_petg_yellow_1000_175_c": 132
  },
  "extruder_temp_range": {
    "overture_petg_petgyellow_1000_175_c": [
      220,
      250
    ],
    "overture_petg_yellow_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "overture_petg_petgyellow_1000_175_c": [
      70,
      90
    ],
    "overture_petg_yellow_1000_175_c": [
      80,
      90
    ]
  }
}
```

### OV053: dup-d59a544b4951deafc11541ca49da2cce6cb85cea7a71ae465f67e119f1c4da7e

Status: APPROVED; survivor `overture_pla_black_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_black_1000_175_c`|`{color_name}`|`Black`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_pla_plablack_1000_175_c`|`PLA {color_name}`|`Black`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_black_1000_175_c": 1.24,
    "overture_pla_plablack_1000_175_c": 1.16
  },
  "spool_weight": {
    "overture_pla_black_1000_175_c": 155,
    "overture_pla_plablack_1000_175_c": 173
  },
  "extruder_temp": {
    "overture_pla_black_1000_175_c": 210,
    "overture_pla_plablack_1000_175_c": null
  },
  "extruder_temp_range": {
    "overture_pla_black_1000_175_c": null,
    "overture_pla_plablack_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "overture_pla_black_1000_175_c": 60,
    "overture_pla_plablack_1000_175_c": null
  },
  "bed_temp_range": {
    "overture_pla_black_1000_175_c": null,
    "overture_pla_plablack_1000_175_c": [
      50,
      70
    ]
  }
}
```

### OV054: dup-190da8887143b4c7e0619ffc73cc1279d22177f14e35655e003719ed3a35b3d0

Status: APPROVED; survivor `overture_pla_blue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_blue_1000_175_c`|`{color_name}`|`Blue`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_pla_plablue_1000_175_c`|`PLA {color_name}`|`Blue`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_blue_1000_175_c": 1.24,
    "overture_pla_plablue_1000_175_c": 1.16
  },
  "spool_weight": {
    "overture_pla_blue_1000_175_c": 155,
    "overture_pla_plablue_1000_175_c": 173
  },
  "extruder_temp": {
    "overture_pla_blue_1000_175_c": 210,
    "overture_pla_plablue_1000_175_c": null
  },
  "extruder_temp_range": {
    "overture_pla_blue_1000_175_c": null,
    "overture_pla_plablue_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "overture_pla_blue_1000_175_c": 60,
    "overture_pla_plablue_1000_175_c": null
  },
  "bed_temp_range": {
    "overture_pla_blue_1000_175_c": null,
    "overture_pla_plablue_1000_175_c": [
      50,
      70
    ]
  }
}
```

### OV055: dup-9ab9b2c7a915e6f7da9cc7e301f713e412ff3d1e9036dcf806c927afd908aa65

Status: APPROVED; survivor `overture_pla_brown_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_brown_1000_175_c`|`{color_name}`|`Brown`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_pla_plabrown_1000_175_c`|`PLA {color_name}`|`Brown`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_brown_1000_175_c": 1.24,
    "overture_pla_plabrown_1000_175_c": 1.16
  },
  "spool_weight": {
    "overture_pla_brown_1000_175_c": 155,
    "overture_pla_plabrown_1000_175_c": 173
  },
  "extruder_temp": {
    "overture_pla_brown_1000_175_c": 210,
    "overture_pla_plabrown_1000_175_c": null
  },
  "extruder_temp_range": {
    "overture_pla_brown_1000_175_c": null,
    "overture_pla_plabrown_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "overture_pla_brown_1000_175_c": 60,
    "overture_pla_plabrown_1000_175_c": null
  },
  "bed_temp_range": {
    "overture_pla_brown_1000_175_c": null,
    "overture_pla_plabrown_1000_175_c": [
      50,
      70
    ]
  }
}
```

### OV056: dup-8d05ccddc254128ca1c3b71e87665acfdfa8a5f595313a3a9c39d4ce1c57b2ac

Status: APPROVED; survivor `overture_pla_cementgray_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_cementgray_1000_175_c`|`{color_name}`|`Cement Gray`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_pla_placementgray_1000_175_c`|`PLA {color_name}`|`Cement Gray`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_cementgray_1000_175_c": 1.24,
    "overture_pla_placementgray_1000_175_c": 1.16
  },
  "spool_weight": {
    "overture_pla_cementgray_1000_175_c": 155,
    "overture_pla_placementgray_1000_175_c": 173
  },
  "extruder_temp": {
    "overture_pla_cementgray_1000_175_c": 210,
    "overture_pla_placementgray_1000_175_c": null
  },
  "extruder_temp_range": {
    "overture_pla_cementgray_1000_175_c": null,
    "overture_pla_placementgray_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "overture_pla_cementgray_1000_175_c": 60,
    "overture_pla_placementgray_1000_175_c": null
  },
  "bed_temp_range": {
    "overture_pla_cementgray_1000_175_c": null,
    "overture_pla_placementgray_1000_175_c": [
      50,
      70
    ]
  }
}
```

### OV057: dup-2a2ef06e1b65f76452b025a9c7af0d9a2a5239e5d14d9d881f3f7c9272b1d060

Status: APPROVED; survivor `overture_pla_chocolate_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_chocolate_1000_175_c`|`{color_name}`|`Chocolate`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_pla_plachocolate_1000_175_c`|`PLA {color_name}`|`Chocolate`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_chocolate_1000_175_c": 1.24,
    "overture_pla_plachocolate_1000_175_c": 1.16
  },
  "spool_weight": {
    "overture_pla_chocolate_1000_175_c": 155,
    "overture_pla_plachocolate_1000_175_c": 173
  },
  "extruder_temp": {
    "overture_pla_chocolate_1000_175_c": 210,
    "overture_pla_plachocolate_1000_175_c": null
  },
  "extruder_temp_range": {
    "overture_pla_chocolate_1000_175_c": null,
    "overture_pla_plachocolate_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "overture_pla_chocolate_1000_175_c": 60,
    "overture_pla_plachocolate_1000_175_c": null
  },
  "bed_temp_range": {
    "overture_pla_chocolate_1000_175_c": null,
    "overture_pla_plachocolate_1000_175_c": [
      50,
      70
    ]
  }
}
```

### OV058: dup-9d2feea99084cb4dd750b963a47357d9ab8edf0cd2388afdac0001a58848dafc

Status: APPROVED; survivor `overture_pla_coldwhite_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_coldwhite_1000_175_c`|`{color_name}`|`Cold White`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_pla_placoldwhite_1000_175_c`|`PLA {color_name}`|`Cold White`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_coldwhite_1000_175_c": 1.24,
    "overture_pla_placoldwhite_1000_175_c": 1.16
  },
  "spool_weight": {
    "overture_pla_coldwhite_1000_175_c": 155,
    "overture_pla_placoldwhite_1000_175_c": 173
  },
  "extruder_temp": {
    "overture_pla_coldwhite_1000_175_c": 210,
    "overture_pla_placoldwhite_1000_175_c": null
  },
  "extruder_temp_range": {
    "overture_pla_coldwhite_1000_175_c": null,
    "overture_pla_placoldwhite_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "overture_pla_coldwhite_1000_175_c": 60,
    "overture_pla_placoldwhite_1000_175_c": null
  },
  "bed_temp_range": {
    "overture_pla_coldwhite_1000_175_c": null,
    "overture_pla_placoldwhite_1000_175_c": [
      50,
      70
    ]
  }
}
```

### OV059: dup-64a8319406dcf6f34ae9dafd24e44adb9fc061c94d06d8f3e0abd077993f21f1

Status: APPROVED; survivor `overture_pla_freshred_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_freshred_1000_175_c`|`{color_name}`|`Fresh Red`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_pla_plafreshred_1000_175_c`|`PLA {color_name}`|`Fresh Red`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_freshred_1000_175_c": 1.24,
    "overture_pla_plafreshred_1000_175_c": 1.16
  },
  "spool_weight": {
    "overture_pla_freshred_1000_175_c": 155,
    "overture_pla_plafreshred_1000_175_c": 173
  },
  "extruder_temp": {
    "overture_pla_freshred_1000_175_c": 210,
    "overture_pla_plafreshred_1000_175_c": null
  },
  "extruder_temp_range": {
    "overture_pla_freshred_1000_175_c": null,
    "overture_pla_plafreshred_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "overture_pla_freshred_1000_175_c": 60,
    "overture_pla_plafreshred_1000_175_c": null
  },
  "bed_temp_range": {
    "overture_pla_freshred_1000_175_c": null,
    "overture_pla_plafreshred_1000_175_c": [
      50,
      70
    ]
  }
}
```

### OV060: dup-863d3d1708370e540491be5fb7987904ceec9604d11103f3f0f73b2f09bcceae

Status: APPROVED; survivor `overture_pla_glowindark_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_glowindark_1000_175_c`|`{color_name}`|`Glow in Dark`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_pla_plaglowindark_1000_175_c`|`PLA {color_name}`|`Glow in Dark`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_glowindark_1000_175_c": 1.24,
    "overture_pla_plaglowindark_1000_175_c": 1.16
  },
  "spool_weight": {
    "overture_pla_glowindark_1000_175_c": 155,
    "overture_pla_plaglowindark_1000_175_c": 173
  },
  "extruder_temp": {
    "overture_pla_glowindark_1000_175_c": 210,
    "overture_pla_plaglowindark_1000_175_c": null
  },
  "extruder_temp_range": {
    "overture_pla_glowindark_1000_175_c": null,
    "overture_pla_plaglowindark_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "overture_pla_glowindark_1000_175_c": 60,
    "overture_pla_plaglowindark_1000_175_c": null
  },
  "bed_temp_range": {
    "overture_pla_glowindark_1000_175_c": null,
    "overture_pla_plaglowindark_1000_175_c": [
      50,
      70
    ]
  }
}
```

### OV061: dup-270a54bd13c816e99b9098c5e9cd7a8adac275d8e8d6e64907f3747af23ffecf

Status: APPROVED; survivor `overture_pla_grayblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_grayblue_1000_175_c`|`{color_name}`|`Gray Blue`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_pla_plagrayblue_1000_175_c`|`PLA {color_name}`|`Gray Blue`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_grayblue_1000_175_c": 1.24,
    "overture_pla_plagrayblue_1000_175_c": 1.16
  },
  "spool_weight": {
    "overture_pla_grayblue_1000_175_c": 155,
    "overture_pla_plagrayblue_1000_175_c": 173
  },
  "extruder_temp": {
    "overture_pla_grayblue_1000_175_c": 210,
    "overture_pla_plagrayblue_1000_175_c": null
  },
  "extruder_temp_range": {
    "overture_pla_grayblue_1000_175_c": null,
    "overture_pla_plagrayblue_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "overture_pla_grayblue_1000_175_c": 60,
    "overture_pla_plagrayblue_1000_175_c": null
  },
  "bed_temp_range": {
    "overture_pla_grayblue_1000_175_c": null,
    "overture_pla_plagrayblue_1000_175_c": [
      50,
      70
    ]
  }
}
```

### OV062: dup-f5325becc01e225c7fadb7864fe3904027a1657928847b7b11f7a84a64e8b6c2

Status: APPROVED; survivor `overture_pla_green_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_green_1000_175_c`|`{color_name}`|`Green`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_pla_plagreen_1000_175_c`|`PLA {color_name}`|`Green`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_green_1000_175_c": 1.24,
    "overture_pla_plagreen_1000_175_c": 1.16
  },
  "spool_weight": {
    "overture_pla_green_1000_175_c": 155,
    "overture_pla_plagreen_1000_175_c": 173
  },
  "extruder_temp": {
    "overture_pla_green_1000_175_c": 210,
    "overture_pla_plagreen_1000_175_c": null
  },
  "extruder_temp_range": {
    "overture_pla_green_1000_175_c": null,
    "overture_pla_plagreen_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "overture_pla_green_1000_175_c": 60,
    "overture_pla_plagreen_1000_175_c": null
  },
  "bed_temp_range": {
    "overture_pla_green_1000_175_c": null,
    "overture_pla_plagreen_1000_175_c": [
      50,
      70
    ]
  }
}
```

### OV063: dup-e3b3e3dbea0a9452da3f5407effe885dc8cfc8a856081271967620a2f1ea4ed8

Status: APPROVED; survivor `overture_pla_highlightyellow_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_highlightyellow_1000_175_c`|`{color_name}`|`Highlight Yellow`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_pla_plahighlightyellow_1000_175_c`|`PLA {color_name}`|`Highlight Yellow`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_highlightyellow_1000_175_c": 1.24,
    "overture_pla_plahighlightyellow_1000_175_c": 1.16
  },
  "spool_weight": {
    "overture_pla_highlightyellow_1000_175_c": 155,
    "overture_pla_plahighlightyellow_1000_175_c": 173
  },
  "extruder_temp": {
    "overture_pla_highlightyellow_1000_175_c": 210,
    "overture_pla_plahighlightyellow_1000_175_c": null
  },
  "extruder_temp_range": {
    "overture_pla_highlightyellow_1000_175_c": null,
    "overture_pla_plahighlightyellow_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "overture_pla_highlightyellow_1000_175_c": 60,
    "overture_pla_plahighlightyellow_1000_175_c": null
  },
  "bed_temp_range": {
    "overture_pla_highlightyellow_1000_175_c": null,
    "overture_pla_plahighlightyellow_1000_175_c": [
      50,
      70
    ]
  }
}
```

### OV064: dup-6f550b95541a27a0fc6c7d9d500aeea350588200a6cc8641f3478b45be22fa66

Status: APPROVED; survivor `overture_pla_lightblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_lightblue_1000_175_c`|`{color_name}`|`Light Blue`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_pla_plalightblue_1000_175_c`|`PLA {color_name}`|`Light Blue`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_lightblue_1000_175_c": 1.24,
    "overture_pla_plalightblue_1000_175_c": 1.16
  },
  "spool_weight": {
    "overture_pla_lightblue_1000_175_c": 155,
    "overture_pla_plalightblue_1000_175_c": 173
  },
  "extruder_temp": {
    "overture_pla_lightblue_1000_175_c": 210,
    "overture_pla_plalightblue_1000_175_c": null
  },
  "extruder_temp_range": {
    "overture_pla_lightblue_1000_175_c": null,
    "overture_pla_plalightblue_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "overture_pla_lightblue_1000_175_c": 60,
    "overture_pla_plalightblue_1000_175_c": null
  },
  "bed_temp_range": {
    "overture_pla_lightblue_1000_175_c": null,
    "overture_pla_plalightblue_1000_175_c": [
      50,
      70
    ]
  }
}
```

### OV065: dup-edfee6c817c84e6dcbf67b532fe2f7645d9f74da9584dc18f2bc0aa9a46df2f0

Status: APPROVED; survivor `overture_pla_lightgray_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_lightgray_1000_175_c`|`{color_name}`|`Light Gray`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_pla_plalightgray_1000_175_c`|`PLA {color_name}`|`Light Gray`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_lightgray_1000_175_c": 1.24,
    "overture_pla_plalightgray_1000_175_c": 1.16
  },
  "spool_weight": {
    "overture_pla_lightgray_1000_175_c": 155,
    "overture_pla_plalightgray_1000_175_c": 173
  },
  "extruder_temp": {
    "overture_pla_lightgray_1000_175_c": 210,
    "overture_pla_plalightgray_1000_175_c": null
  },
  "extruder_temp_range": {
    "overture_pla_lightgray_1000_175_c": null,
    "overture_pla_plalightgray_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "overture_pla_lightgray_1000_175_c": 60,
    "overture_pla_plalightgray_1000_175_c": null
  },
  "bed_temp_range": {
    "overture_pla_lightgray_1000_175_c": null,
    "overture_pla_plalightgray_1000_175_c": [
      50,
      70
    ]
  }
}
```

### OV066: dup-b5b9367a126e21efa019f5335384a57a77fa4332674e7c4b28488cccc2d39170

Status: APPROVED; survivor `overture_pla_matteplalightgray_1000_175_c`; Owner-approved official spelling (rule5 amendment).

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_matteplalightgray_1000_175_c`|`Matte PLA {color_name}`|`Light gray`|{"source_file": "overture.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 51, "compiled_records": 51} / True|
|`overture_pla_matteplalightgrey_1000_175_c`|`Matte PLA {color_name}`|`Light Grey`|{"source_file": "overture.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 51, "compiled_records": 51} / True|

Explicit owner approval OV066: current official Matte PLA color Light gray, https://overture3d.com/products/overture-matte-pla ; product variant SKU VFFMLGR17511. Identical HEX BAC4C4; owner approved historical binding.

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{}
```

### OV067: dup-b4627b984f2a81c224b2932b288f5e21fa3a8468e69f9f99196b1f9693f899dc

Status: APPROVED; survivor `overture_pla_midnightblack_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_midnightblack_1000_175_c`|`{color_name}`|`Midnight Black`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_pla_plamidnightblack_1000_175_c`|`PLA {color_name}`|`Midnight Black`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_midnightblack_1000_175_c": 1.24,
    "overture_pla_plamidnightblack_1000_175_c": 1.16
  },
  "spool_weight": {
    "overture_pla_midnightblack_1000_175_c": 155,
    "overture_pla_plamidnightblack_1000_175_c": 173
  },
  "extruder_temp": {
    "overture_pla_midnightblack_1000_175_c": 210,
    "overture_pla_plamidnightblack_1000_175_c": null
  },
  "extruder_temp_range": {
    "overture_pla_midnightblack_1000_175_c": null,
    "overture_pla_plamidnightblack_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "overture_pla_midnightblack_1000_175_c": 60,
    "overture_pla_plamidnightblack_1000_175_c": null
  },
  "bed_temp_range": {
    "overture_pla_midnightblack_1000_175_c": null,
    "overture_pla_plamidnightblack_1000_175_c": [
      50,
      70
    ]
  }
}
```

### OV068: dup-ec4c26fbfc1957fff85b4a25091032332a0104b4dda0f7acfa573e83441504a2

Status: APPROVED; survivor `overture_pla_olivegreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_olivegreen_1000_175_c`|`{color_name}`|`Olive Green`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_pla_plaolivegreen_1000_175_c`|`PLA {color_name}`|`Olive Green`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_olivegreen_1000_175_c": 1.24,
    "overture_pla_plaolivegreen_1000_175_c": 1.16
  },
  "spool_weight": {
    "overture_pla_olivegreen_1000_175_c": 155,
    "overture_pla_plaolivegreen_1000_175_c": 173
  },
  "extruder_temp": {
    "overture_pla_olivegreen_1000_175_c": 210,
    "overture_pla_plaolivegreen_1000_175_c": null
  },
  "extruder_temp_range": {
    "overture_pla_olivegreen_1000_175_c": null,
    "overture_pla_plaolivegreen_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "overture_pla_olivegreen_1000_175_c": 60,
    "overture_pla_plaolivegreen_1000_175_c": null
  },
  "bed_temp_range": {
    "overture_pla_olivegreen_1000_175_c": null,
    "overture_pla_plaolivegreen_1000_175_c": [
      50,
      70
    ]
  }
}
```

### OV069: dup-610318fa09f1e3d4b1ae2ad032fe1c0372a25fc7e50f06d4ed0a39fcf5198af6

Status: APPROVED; survivor `overture_pla_orange_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_orange_1000_175_c`|`{color_name}`|`Orange`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_pla_plaorange_1000_175_c`|`PLA {color_name}`|`Orange`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_orange_1000_175_c": 1.24,
    "overture_pla_plaorange_1000_175_c": 1.16
  },
  "spool_weight": {
    "overture_pla_orange_1000_175_c": 155,
    "overture_pla_plaorange_1000_175_c": 173
  },
  "extruder_temp": {
    "overture_pla_orange_1000_175_c": 210,
    "overture_pla_plaorange_1000_175_c": null
  },
  "extruder_temp_range": {
    "overture_pla_orange_1000_175_c": null,
    "overture_pla_plaorange_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "overture_pla_orange_1000_175_c": 60,
    "overture_pla_plaorange_1000_175_c": null
  },
  "bed_temp_range": {
    "overture_pla_orange_1000_175_c": null,
    "overture_pla_plaorange_1000_175_c": [
      50,
      70
    ]
  }
}
```

### OV070: dup-3a25af28cb57c03eaa3253be62709470a67a204aad08ce98aae4c3c76c823202

Status: APPROVED; survivor `overture_pla_pink_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_pink_1000_175_c`|`{color_name}`|`Pink`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|
|`overture_pla_plapink_1000_175_c`|`PLA {color_name}`|`Pink`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_pink_1000_175_c": 1.24,
    "overture_pla_plapink_1000_175_c": 1.16
  },
  "spool_weight": {
    "overture_pla_pink_1000_175_c": 155,
    "overture_pla_plapink_1000_175_c": 173
  },
  "extruder_temp": {
    "overture_pla_pink_1000_175_c": 210,
    "overture_pla_plapink_1000_175_c": null
  },
  "extruder_temp_range": {
    "overture_pla_pink_1000_175_c": null,
    "overture_pla_plapink_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "overture_pla_pink_1000_175_c": 60,
    "overture_pla_plapink_1000_175_c": null
  },
  "bed_temp_range": {
    "overture_pla_pink_1000_175_c": null,
    "overture_pla_plapink_1000_175_c": [
      50,
      70
    ]
  }
}
```

### OV071: dup-3d6fd3a016b48525eccebc7f26793953111c7feb333f6b02ce41aac55154a6d1

Status: APPROVED; survivor `overture_pla_purple_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_plapurple_1000_175_c`|`PLA {color_name}`|`Purple`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|
|`overture_pla_purple_1000_175_c`|`{color_name}`|`Purple`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_plapurple_1000_175_c": 1.16,
    "overture_pla_purple_1000_175_c": 1.24
  },
  "spool_weight": {
    "overture_pla_plapurple_1000_175_c": 173,
    "overture_pla_purple_1000_175_c": 155
  },
  "extruder_temp": {
    "overture_pla_plapurple_1000_175_c": null,
    "overture_pla_purple_1000_175_c": 210
  },
  "extruder_temp_range": {
    "overture_pla_plapurple_1000_175_c": [
      190,
      230
    ],
    "overture_pla_purple_1000_175_c": null
  },
  "bed_temp": {
    "overture_pla_plapurple_1000_175_c": null,
    "overture_pla_purple_1000_175_c": 60
  },
  "bed_temp_range": {
    "overture_pla_plapurple_1000_175_c": [
      50,
      70
    ],
    "overture_pla_purple_1000_175_c": null
  }
}
```

### OV072: dup-5625e26458233293a55e8bad55bd8a043da38a297cb2dee933f887db2e21435e

Status: APPROVED; survivor `overture_pla_red_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_plared_1000_175_c`|`PLA {color_name}`|`Red`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|
|`overture_pla_red_1000_175_c`|`{color_name}`|`Red`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_plared_1000_175_c": 1.16,
    "overture_pla_red_1000_175_c": 1.24
  },
  "spool_weight": {
    "overture_pla_plared_1000_175_c": 173,
    "overture_pla_red_1000_175_c": 155
  },
  "extruder_temp": {
    "overture_pla_plared_1000_175_c": null,
    "overture_pla_red_1000_175_c": 210
  },
  "extruder_temp_range": {
    "overture_pla_plared_1000_175_c": [
      190,
      230
    ],
    "overture_pla_red_1000_175_c": null
  },
  "bed_temp": {
    "overture_pla_plared_1000_175_c": null,
    "overture_pla_red_1000_175_c": 60
  },
  "bed_temp_range": {
    "overture_pla_plared_1000_175_c": [
      50,
      70
    ],
    "overture_pla_red_1000_175_c": null
  }
}
```

### OV073: dup-9b28b4459d637b0f6a7b1547ac129e135a6da8d8559a50d3eeeaf3d7e2a7d897

Status: APPROVED; survivor `overture_pla_rockplafossilrock_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_plarockfossilrock_1000_175_c`|`PLA Rock {color_name}`|`Fossil Rock`|{"source_file": "overture.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|
|`overture_pla_rockplafossilrock_1000_175_c`|`Rock PLA {color_name}`|`Fossil Rock`|{"source_file": "overture.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_plarockfossilrock_1000_175_c": 1.24,
    "overture_pla_rockplafossilrock_1000_175_c": 1.3
  },
  "spool_weight": {
    "overture_pla_plarockfossilrock_1000_175_c": 173,
    "overture_pla_rockplafossilrock_1000_175_c": 155
  },
  "finish": {
    "overture_pla_plarockfossilrock_1000_175_c": null,
    "overture_pla_rockplafossilrock_1000_175_c": "matte"
  },
  "pattern": {
    "overture_pla_plarockfossilrock_1000_175_c": null,
    "overture_pla_rockplafossilrock_1000_175_c": "marble"
  },
  "codes": {
    "overture_pla_plarockfossilrock_1000_175_c": [
      "VSA110001"
    ],
    "overture_pla_rockplafossilrock_1000_175_c": null
  }
}
```

### OV074: dup-3ff5a2855f547d1319b8a267cb2cea1660ede11eb1d1e9b46d7bdea2df7e1412

Status: APPROVED; survivor `overture_pla_rockplaglacierblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_plarockglacierblue_1000_175_c`|`PLA Rock {color_name}`|`Glacier Blue`|{"source_file": "overture.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|
|`overture_pla_rockplaglacierblue_1000_175_c`|`Rock PLA {color_name}`|`Glacier Blue`|{"source_file": "overture.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_plarockglacierblue_1000_175_c": 1.24,
    "overture_pla_rockplaglacierblue_1000_175_c": 1.3
  },
  "spool_weight": {
    "overture_pla_plarockglacierblue_1000_175_c": 173,
    "overture_pla_rockplaglacierblue_1000_175_c": 155
  },
  "color_hex": {
    "overture_pla_plarockglacierblue_1000_175_c": "FFFFFF",
    "overture_pla_rockplaglacierblue_1000_175_c": null
  },
  "color_hexes": {
    "overture_pla_plarockglacierblue_1000_175_c": null,
    "overture_pla_rockplaglacierblue_1000_175_c": [
      "A3EAFF",
      "FFFFFF"
    ]
  },
  "finish": {
    "overture_pla_plarockglacierblue_1000_175_c": null,
    "overture_pla_rockplaglacierblue_1000_175_c": "matte"
  },
  "multi_color_direction": {
    "overture_pla_plarockglacierblue_1000_175_c": null,
    "overture_pla_rockplaglacierblue_1000_175_c": "longitudinal"
  }
}
```

### OV075: dup-010c887752b1cba880700f2447d8cb5b4307d05b641f8853406e44affa93bb6d

Status: APPROVED; survivor `overture_pla_rockplamarsred_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_plarockmarsred_1000_175_c`|`PLA Rock {color_name}`|`Mars Red`|{"source_file": "overture.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|
|`overture_pla_rockplamarsred_1000_175_c`|`Rock PLA {color_name}`|`Mars Red`|{"source_file": "overture.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_plarockmarsred_1000_175_c": 1.24,
    "overture_pla_rockplamarsred_1000_175_c": 1.3
  },
  "spool_weight": {
    "overture_pla_plarockmarsred_1000_175_c": 173,
    "overture_pla_rockplamarsred_1000_175_c": 155
  },
  "finish": {
    "overture_pla_plarockmarsred_1000_175_c": null,
    "overture_pla_rockplamarsred_1000_175_c": "matte"
  }
}
```

### OV076: dup-068123d5ff024de6d58e18395a8e3630a5355501d40af6839df6eee298e2059b

Status: APPROVED; survivor `overture_pla_rockplarockrainbow_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_plarockrockrainbow_1000_175_c`|`PLA Rock {color_name}`|`Rock Rainbow`|{"source_file": "overture.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|
|`overture_pla_rockplarockrainbow_1000_175_c`|`Rock PLA {color_name}`|`Rock Rainbow`|{"source_file": "overture.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_plarockrockrainbow_1000_175_c": 1.24,
    "overture_pla_rockplarockrainbow_1000_175_c": 1.3
  },
  "spool_weight": {
    "overture_pla_plarockrockrainbow_1000_175_c": 173,
    "overture_pla_rockplarockrainbow_1000_175_c": 155
  },
  "color_hex": {
    "overture_pla_plarockrockrainbow_1000_175_c": "1AB790",
    "overture_pla_rockplarockrainbow_1000_175_c": null
  },
  "color_hexes": {
    "overture_pla_plarockrockrainbow_1000_175_c": null,
    "overture_pla_rockplarockrainbow_1000_175_c": [
      "FF0000",
      "FF7F00",
      "FFFF00",
      "00FF00",
      "0000FF",
      "4B0082",
      "8B00FF"
    ]
  },
  "finish": {
    "overture_pla_plarockrockrainbow_1000_175_c": null,
    "overture_pla_rockplarockrainbow_1000_175_c": "matte"
  },
  "multi_color_direction": {
    "overture_pla_plarockrockrainbow_1000_175_c": null,
    "overture_pla_rockplarockrainbow_1000_175_c": "longitudinal"
  },
  "codes": {
    "overture_pla_plarockrockrainbow_1000_175_c": [
      "VSA110006"
    ],
    "overture_pla_rockplarockrainbow_1000_175_c": null
  }
}
```

### OV077: dup-56b9129b15d08ef7b9019de70b5f88797db6008793d9798574e02537cba19c56

Status: APPROVED; survivor `overture_pla_rockplarockwhite_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_plarockrockwhite_1000_175_c`|`PLA Rock {color_name}`|`Rock White`|{"source_file": "overture.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|
|`overture_pla_rockplarockwhite_1000_175_c`|`Rock PLA {color_name}`|`Rock White`|{"source_file": "overture.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_plarockrockwhite_1000_175_c": 1.24,
    "overture_pla_rockplarockwhite_1000_175_c": 1.3
  },
  "spool_weight": {
    "overture_pla_plarockrockwhite_1000_175_c": 173,
    "overture_pla_rockplarockwhite_1000_175_c": 155
  },
  "finish": {
    "overture_pla_plarockrockwhite_1000_175_c": null,
    "overture_pla_rockplarockwhite_1000_175_c": "matte"
  },
  "pattern": {
    "overture_pla_plarockrockwhite_1000_175_c": null,
    "overture_pla_rockplarockwhite_1000_175_c": "marble"
  },
  "codes": {
    "overture_pla_plarockrockwhite_1000_175_c": [
      "VFFRWT17511"
    ],
    "overture_pla_rockplarockwhite_1000_175_c": null
  }
}
```

### OV078: dup-205a0731d6c89f6d6984660db31eede9f6e88eb958a8f8b4e31d73c19d55c9a8

Status: APPROVED; survivor `overture_pla_rockplasedimentaryrock_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_plarocksedimentaryrock_1000_175_c`|`PLA Rock {color_name}`|`Sedimentary Rock`|{"source_file": "overture.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|
|`overture_pla_rockplasedimentaryrock_1000_175_c`|`Rock PLA {color_name}`|`Sedimentary Rock`|{"source_file": "overture.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_plarocksedimentaryrock_1000_175_c": 1.24,
    "overture_pla_rockplasedimentaryrock_1000_175_c": 1.3
  },
  "spool_weight": {
    "overture_pla_plarocksedimentaryrock_1000_175_c": 173,
    "overture_pla_rockplasedimentaryrock_1000_175_c": 155
  },
  "color_hex": {
    "overture_pla_plarocksedimentaryrock_1000_175_c": "765540",
    "overture_pla_rockplasedimentaryrock_1000_175_c": "C4B199"
  },
  "finish": {
    "overture_pla_plarocksedimentaryrock_1000_175_c": null,
    "overture_pla_rockplasedimentaryrock_1000_175_c": "matte"
  },
  "codes": {
    "overture_pla_plarocksedimentaryrock_1000_175_c": [
      "VSA110002"
    ],
    "overture_pla_rockplasedimentaryrock_1000_175_c": null
  }
}
```

### OV079: dup-a80738fe3cb6c22097769471549693f4cac2d259173bc3e22eb795de61cb6cbe

Status: APPROVED; survivor `overture_pla_royalgold_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_plaroyalgold_1000_175_c`|`PLA {color_name}`|`Royal Gold`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|
|`overture_pla_royalgold_1000_175_c`|`{color_name}`|`Royal Gold`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_plaroyalgold_1000_175_c": 1.16,
    "overture_pla_royalgold_1000_175_c": 1.24
  },
  "spool_weight": {
    "overture_pla_plaroyalgold_1000_175_c": 173,
    "overture_pla_royalgold_1000_175_c": 155
  },
  "extruder_temp": {
    "overture_pla_plaroyalgold_1000_175_c": null,
    "overture_pla_royalgold_1000_175_c": 210
  },
  "extruder_temp_range": {
    "overture_pla_plaroyalgold_1000_175_c": [
      190,
      230
    ],
    "overture_pla_royalgold_1000_175_c": null
  },
  "bed_temp": {
    "overture_pla_plaroyalgold_1000_175_c": null,
    "overture_pla_royalgold_1000_175_c": 60
  },
  "bed_temp_range": {
    "overture_pla_plaroyalgold_1000_175_c": [
      50,
      70
    ],
    "overture_pla_royalgold_1000_175_c": null
  }
}
```

### OV080: dup-ba6510e8290f5d95c048dcf4c648e6d57f005774a70e3597c93de86ecdf09a5d

Status: APPROVED; survivor `overture_pla_spacegray_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_plaspacegray_1000_175_c`|`PLA {color_name}`|`Space Gray`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|
|`overture_pla_spacegray_1000_175_c`|`{color_name}`|`Space Gray`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_plaspacegray_1000_175_c": 1.16,
    "overture_pla_spacegray_1000_175_c": 1.24
  },
  "spool_weight": {
    "overture_pla_plaspacegray_1000_175_c": 173,
    "overture_pla_spacegray_1000_175_c": 155
  },
  "extruder_temp": {
    "overture_pla_plaspacegray_1000_175_c": null,
    "overture_pla_spacegray_1000_175_c": 210
  },
  "extruder_temp_range": {
    "overture_pla_plaspacegray_1000_175_c": [
      190,
      230
    ],
    "overture_pla_spacegray_1000_175_c": null
  },
  "bed_temp": {
    "overture_pla_plaspacegray_1000_175_c": null,
    "overture_pla_spacegray_1000_175_c": 60
  },
  "bed_temp_range": {
    "overture_pla_plaspacegray_1000_175_c": [
      50,
      70
    ],
    "overture_pla_spacegray_1000_175_c": null
  }
}
```

### OV081: dup-a7de8b1df77a55dfb97acdd7ff2e75be1760f1077b74b3a84c5a0265ca7daf92

Status: APPROVED; survivor `overture_pla_white_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_plawhite_1000_175_c`|`PLA {color_name}`|`White`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|
|`overture_pla_white_1000_175_c`|`{color_name}`|`White`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_plawhite_1000_175_c": 1.16,
    "overture_pla_white_1000_175_c": 1.24
  },
  "spool_weight": {
    "overture_pla_plawhite_1000_175_c": 173,
    "overture_pla_white_1000_175_c": 155
  },
  "extruder_temp": {
    "overture_pla_plawhite_1000_175_c": null,
    "overture_pla_white_1000_175_c": 210
  },
  "extruder_temp_range": {
    "overture_pla_plawhite_1000_175_c": [
      190,
      230
    ],
    "overture_pla_white_1000_175_c": null
  },
  "bed_temp": {
    "overture_pla_plawhite_1000_175_c": null,
    "overture_pla_white_1000_175_c": 60
  },
  "bed_temp_range": {
    "overture_pla_plawhite_1000_175_c": [
      50,
      70
    ],
    "overture_pla_white_1000_175_c": null
  }
}
```

### OV082: dup-b9296e5817949f52dd40db425923272cd23f1bbb75ac69b451299d9c54de6be9

Status: APPROVED; survivor `overture_pla_yellow_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_pla_playellow_1000_175_c`|`PLA {color_name}`|`Yellow`|{"source_file": "overture.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 37, "compiled_records": 74} / False|
|`overture_pla_yellow_1000_175_c`|`{color_name}`|`Yellow`|{"source_file": "overture.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "overture_pla_playellow_1000_175_c": 1.16,
    "overture_pla_yellow_1000_175_c": 1.24
  },
  "spool_weight": {
    "overture_pla_playellow_1000_175_c": 173,
    "overture_pla_yellow_1000_175_c": 155
  },
  "extruder_temp": {
    "overture_pla_playellow_1000_175_c": null,
    "overture_pla_yellow_1000_175_c": 210
  },
  "extruder_temp_range": {
    "overture_pla_playellow_1000_175_c": [
      190,
      230
    ],
    "overture_pla_yellow_1000_175_c": null
  },
  "bed_temp": {
    "overture_pla_playellow_1000_175_c": null,
    "overture_pla_yellow_1000_175_c": 60
  },
  "bed_temp_range": {
    "overture_pla_playellow_1000_175_c": [
      50,
      70
    ],
    "overture_pla_yellow_1000_175_c": null
  }
}
```

### OV083: dup-6321b0a86399b6b15f11f4dc4f1454071e35125f57ab956e45bdcdbacf2f3ef7

Status: DEFERRED; survivor `None`; Explicit owner deferral OV083: TPU Gray HEX9F9F9F vs Grey HEXE2E7E9 visibly differ; both cannot be bound to one current SKU. Keep both exact original records; current Matte Gray VFTGRY11-010058 is not sufficient proof..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`overture_tpu_tpugray_1000_175_c`|`TPU {color_name}`|`Gray`|{"source_file": "overture.json", "definition_index": 30, "weights": 1, "diameters": 1, "colors": 19, "compiled_records": 19} / False|
|`overture_tpu_tpugrey_1000_175_c`|`TPU {color_name}`|`Grey`|{"source_file": "overture.json", "definition_index": 30, "weights": 1, "diameters": 1, "colors": 19, "compiled_records": 19} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "overture_tpu_tpugray_1000_175_c": "9F9F9F",
    "overture_tpu_tpugrey_1000_175_c": "E2E7E9"
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "overture_pla_rockplafossilrock_1000_175_c",
      "values": {
        "codes": [
          "VSA110001"
        ]
      },
      "source": "c87c3db5cf850d7ab7c2c108b5412f1c8240dcef",
      "lot": "reviewed historical identifier preservation",
      "same_variant": true,
      "approved": true,
      "field_sources": {
        "codes": "c87c3db5cf850d7ab7c2c108b5412f1c8240dcef"
      }
    },
    {
      "id": "overture_pla_rockplarockrainbow_1000_175_c",
      "values": {
        "codes": [
          "VSA110006"
        ]
      },
      "source": "c87c3db5cf850d7ab7c2c108b5412f1c8240dcef",
      "lot": "reviewed historical identifier preservation",
      "same_variant": true,
      "approved": true,
      "field_sources": {
        "codes": "c87c3db5cf850d7ab7c2c108b5412f1c8240dcef"
      }
    },
    {
      "id": "overture_pla_rockplarockwhite_1000_175_c",
      "values": {
        "codes": [
          "VFFRWT17511"
        ]
      },
      "source": "c87c3db5cf850d7ab7c2c108b5412f1c8240dcef",
      "lot": "reviewed historical identifier preservation",
      "same_variant": true,
      "approved": true,
      "field_sources": {
        "codes": "c87c3db5cf850d7ab7c2c108b5412f1c8240dcef"
      }
    },
    {
      "id": "overture_pla_rockplasedimentaryrock_1000_175_c",
      "values": {
        "codes": [
          "VSA110002"
        ]
      },
      "source": "c87c3db5cf850d7ab7c2c108b5412f1c8240dcef",
      "lot": "reviewed historical identifier preservation",
      "same_variant": true,
      "approved": true,
      "field_sources": {
        "codes": "c87c3db5cf850d7ab7c2c108b5412f1c8240dcef"
      }
    }
  ],
  "transfers": [
    {
      "old_id": "overture_pla_plarockfossilrock_1000_175_c",
      "target_id": "overture_pla_rockplafossilrock_1000_175_c",
      "field": "codes",
      "values": [
        "VSA110001"
      ],
      "source": "c87c3db5cf850d7ab7c2c108b5412f1c8240dcef"
    },
    {
      "old_id": "overture_pla_plarockrockrainbow_1000_175_c",
      "target_id": "overture_pla_rockplarockrainbow_1000_175_c",
      "field": "codes",
      "values": [
        "VSA110006"
      ],
      "source": "c87c3db5cf850d7ab7c2c108b5412f1c8240dcef"
    },
    {
      "old_id": "overture_pla_plarockrockwhite_1000_175_c",
      "target_id": "overture_pla_rockplarockwhite_1000_175_c",
      "field": "codes",
      "values": [
        "VFFRWT17511"
      ],
      "source": "c87c3db5cf850d7ab7c2c108b5412f1c8240dcef"
    },
    {
      "old_id": "overture_pla_plarocksedimentaryrock_1000_175_c",
      "target_id": "overture_pla_rockplasedimentaryrock_1000_175_c",
      "field": "codes",
      "values": [
        "VSA110002"
      ],
      "source": "c87c3db5cf850d7ab7c2c108b5412f1c8240dcef"
    }
  ]
}
```

## Preserved out-of-scope IDs

- `overture_pla_marble_1000_175_c` — Marble
- `overture_pla_silkplawhite_1000_175_c` — Silk PLA White
- `overture_pla_silkplacopper_1000_175_c` — Silk PLA Copper
- `overture_pla_silkplagray_1000_175_c` — Silk PLA Gray
- `overture_pla_silkplagold_1000_175_c` — Silk PLA Gold
- `overture_pla_silkplaneongreen_1000_175_c` — Silk PLA Neon green
- `overture_pla_silkplagreen_1000_175_c` — Silk PLA Green
- `overture_pla_silkplablue_1000_175_c` — Silk PLA Blue
- `overture_pla_silkplared_1000_175_c` — Silk PLA Red
- `overture_pla_silkplasilkpurple_1000_175_c` — Silk PLA Silk Purple
- `overture_pla_silkplasilver_1000_175_c` — Silk PLA Silver
- `overture_pla_silkplafreshred_1000_175_c` — Silk PLA Fresh Red
- `overture_pla_silkplachristmasred_1000_175_c` — Silk PLA Christmas Red
- `overture_pla_silkplacaramel_1000_175_c` — Silk PLA Caramel
- `overture_pla_silkplachromegray_1000_175_c` — Silk PLA Chrome Gray
- `overture_pla_silkplacoppershore_1000_175_c` — Silk PLA Copper Shore
- `overture_pla_silkpladualcolorsblue-silver_1000_175_c` — Silk PLA Dual Colors Blue-Silver
- `overture_pla_silkpladualcolorsblue-yellow_1000_175_c` — Silk PLA Dual Colors Blue-Yellow
- `overture_pla_silkpladualcolorsgold-silver_1000_175_c` — Silk PLA Dual Colors Gold-Silver
- `overture_pla_silkpladualcolorsgreen-blue_1000_175_c` — Silk PLA Dual Colors Green-Blue
- `overture_pla_silkpladualcolorsgreen-magenta_1000_175_c` — Silk PLA Dual Colors Green-Magenta
- `overture_pla_silkpladualcolorsgreen-silver_1000_175_c` — Silk PLA Dual Colors Green-Silver
- `overture_pla_silkpladualcolorsmagenta-gold_1000_175_c` — Silk PLA Dual Colors Magenta-Gold
- `overture_pla_silkpladualcolorspurple-gold_1000_175_c` — Silk PLA Dual Colors Purple-Gold
- `overture_pla_silkpladualcolorsred-gold_1000_175_c` — Silk PLA Dual Colors Red-Gold
- `overture_pla_silkplaevergreenbronze_1000_175_c` — Silk PLA Evergreen Bronze
- `overture_pla_silkplaglacierflash_1000_175_c` — Silk PLA Glacier Flash
- `overture_pla_silkplagoldenember_1000_175_c` — Silk PLA Golden Ember
- `overture_pla_silkplalettucetomato_1000_175_c` — Silk PLA Lettuce Tomato
- `overture_pla_silkplalimesurge_1000_175_c` — Silk PLA Lime Surge
- `overture_pla_silkplaparakeet_1000_175_c` — Silk PLA Parakeet
- `overture_pla_silkplaperiwinkle_1000_175_c` — Silk PLA Periwinkle
- `overture_pla_silkplapunchpink_1000_175_c` — Silk PLA Punch Pink
- `overture_pla_silkplapurple_1000_175_c` — Silk PLA Purple
- `overture_pla_silkplapurplechrome_1000_175_c` — Silk PLA Purple Chrome
- `overture_pla_silkplatigereye_1000_175_c` — Silk PLA Tiger Eye
- `overture_pla_silkplatropic_1000_175_c` — Silk PLA Tropic
- `overture_pla_silkplavaporwave_1000_175_c` — Silk PLA Vaporwave
- `overture_pla_matteplacarbonfiberblack_1000_175_c` — Matte PLA Carbon Fiber Black
- `overture_pla_mattepladarkorange_1000_175_c` — Matte PLA Dark Orange
- `overture_pla_matteplagraygreen_1000_175_c` — Matte PLA Gray Green
- `overture_pla_matteplanavyblue_1000_175_c` — Matte PLA Navy Blue
- `overture_pla_matteplablack_1000_175_c` — Matte PLA Black
- `overture_pla_matteplaorange_1000_175_c` — Matte PLA Orange
- `overture_pla_matteplaarmygreen_1000_175_c` — Matte PLA Army Green
- `overture_pla_matteplalavender_1000_175_c` — Matte PLA Lavender
- `overture_pla_matteplareposegray_1000_175_c` — Matte PLA Repose Gray
- `overture_pla_matteplayellow_1000_175_c` — Matte PLA Yellow
- `overture_pla_matteplagreen_1000_175_c` — Matte PLA Green
- `overture_pla_matteplapurple_1000_175_c` — Matte PLA Purple
- `overture_pla_matteplalightorange_1000_175_c` — Matte PLA Light Orange
- `overture_pla_matteplapalegreen_1000_175_c` — Matte PLA Pale Green
- `overture_pla_matteplablack-white_1000_175_c` — Matte PLA Black-White
- `overture_pla_matteplawhite_1000_175_c` — Matte PLA White
- `overture_pla_matteplaskin_1000_175_c` — Matte PLA Skin
- `overture_pla_matteplalightgreen_1000_175_c` — Matte PLA Light Green
- `overture_pla_matteplaorange-red_1000_175_c` — Matte PLA Orange-Red
- `overture_pla_matteplalightpink_1000_175_c` — Matte PLA Light Pink
- `overture_pla_matteplalightbrown_1000_175_c` — Matte PLA Light Brown
- `overture_pla_matteplalightteal_1000_175_c` — Matte PLA Light Teal
- `overture_pla_matteplablue-red_1000_175_c` — Matte PLA Blue-Red
- `overture_pla_matteplapink_1000_175_c` — Matte PLA Pink
- `overture_pla_matteplawood_1000_175_c` — Matte PLA Wood
- `overture_pla_matteplalightblue_1000_175_c` — Matte PLA Light Blue
- `overture_pla_matteplalightblue-yellow_1000_175_c` — Matte PLA Light Blue-Yellow
- `overture_pla_matteplajeansred_1000_175_c` — Matte PLA Jeans Red
- `overture_pla_matteplaolivegreen_1000_175_c` — Matte PLA Olive Green
- `overture_pla_matteplajeansblue_1000_175_c` — Matte PLA Jeans Blue
- `overture_pla_matteplarainbow_1000_175_c` — Matte PLA Rainbow
- `overture_pla_matteplared_1000_175_c` — Matte PLA Red
- `overture_pla_matteplachocolate_1000_175_c` — Matte PLA Chocolate
- `overture_pla_matteplaslategray_1000_175_c` — Matte PLA Slate Gray
- `overture_pla_matteplarainbowa1_1000_175_c` — Matte PLA Rainbow A1
- `overture_pla_matteplabrickred_1000_175_c` — Matte PLA Brick Red
- `overture_pla_matteplagrassgreen_1000_175_c` — Matte PLA Grass Green
- `overture_pla_matteplablue_1000_175_c` — Matte PLA Blue
- `overture_pla_mattepla6-color_1000_175_c` — Matte PLA 6-Color
- `overture_pla_matteplababypink_1000_175_c` — Matte PLA Baby Pink
- `overture_pla_matteplabamboogreen_1000_175_c` — Matte PLA Bamboo Green
- `overture_pla_matteplabeige_1000_175_c` — Matte PLA Beige
- `overture_pla_matteplablack&white_1000_175_c` — Matte PLA Black & White
- `overture_pla_matteplabutteryellow_1000_175_c` — Matte PLA Butter Yellow
- `overture_pla_matteplacandyrainbow_1000_175_c` — Matte PLA Candy Rainbow
- `overture_pla_matteplaecomidnightblack_1000_175_c` — Matte PLA Eco Midnight Black
- `overture_pla_matteplalilac_1000_175_c` — Matte PLA Lilac
- `overture_pla_matteplapastelred_1000_175_c` — Matte PLA Pastel Red
- `overture_pla_matteplaturquoise_1000_175_c` — Matte PLA Turquoise
- `overture_tpu_highspeed95ablack_1000_175_c` — High Speed 95A Black
- `overture_tpu_highspeed95awhite_1000_175_c` — High Speed 95A White
- `overture_tpu_highspeed95aclear_1000_175_c` — High Speed 95A Clear
- `overture_tpu_highspeed95agrassgreen_1000_175_c` — High Speed 95A Grass Green
- `overture_tpu_highspeed95atranslucentred_1000_175_c` — High Speed 95A Translucent Red
- `overture_tpu_highspeed95aorange_1000_175_c` — High Speed 95A Orange
- `overture_tpu_highspeed95apink_1000_175_c` — High Speed 95A Pink
- `overture_tpu_highspeed95agray_1000_175_c` — High Speed 95A Gray
- `overture_tpu_highspeed95atranslucentblue_1000_175_c` — High Speed 95A Translucent Blue
- `overture_abs_absbasicblack_1000_175_c` — ABS Basic Black
- `overture_abs_absbasicblue_1000_175_c` — ABS Basic Blue
- `overture_abs_absbasicdarkred_1000_175_c` — ABS Basic Dark Red
- `overture_abs_absbasicdiamondgray_1000_175_c` — ABS Basic Diamond Gray
- `overture_abs_absbasicdiamondorange_1000_175_c` — ABS Basic Diamond Orange
- `overture_abs_absbasicdiamondpurple_1000_175_c` — ABS Basic Diamond Purple
- `overture_abs_absbasicglowgreen_1000_175_c` — ABS Basic Glow Green
- `overture_abs_absbasicgray_1000_175_c` — ABS Basic Gray
- `overture_abs_absbasicgreen_1000_175_c` — ABS Basic Green
- `overture_abs_absbasicnatural_1000_175_c` — ABS Basic Natural
- `overture_abs_absbasicpurple_1000_175_c` — ABS Basic Purple
- `overture_abs_absbasicslategray_1000_175_c` — ABS Basic Slate Gray
- `overture_abs_absbasicwhite_1000_175_c` — ABS Basic White
- `overture_abs_absbasicyellow_1000_175_c` — ABS Basic Yellow
- `overture_asa_asabasicblack_1000_175_c` — ASA Basic Black
- `overture_asa_asabasicblue_1000_175_c` — ASA Basic Blue
- `overture_asa_asabasicbrown_1000_175_c` — ASA Basic Brown
- `overture_asa_asabasicdiamondblue_1000_175_c` — ASA Basic Diamond Blue
- `overture_asa_asabasicdiamondgreen_1000_175_c` — ASA Basic Diamond Green
- `overture_asa_asabasicdiamondred_1000_175_c` — ASA Basic Diamond Red
- `overture_asa_asabasicgray_1000_175_c` — ASA Basic Gray
- `overture_asa_asabasicgreen_1000_175_c` — ASA Basic Green
- `overture_asa_asabasicnatural_1000_175_c` — ASA Basic Natural
- `overture_asa_asabasicolivegreen_1000_175_c` — ASA Basic Olive Green
- `overture_asa_asabasicorange_1000_175_c` — ASA Basic Orange
- `overture_asa_asabasicred_1000_175_c` — ASA Basic Red
- `overture_asa_asabasicwhite_1000_175_c` — ASA Basic White
- `overture_asa_asabasicyellow_1000_175_c` — ASA Basic Yellow
- `overture_pc_pcprofessionalblack_1000_175_c` — PC Professional Black
- `overture_pc_pcprofessionalblue_1000_175_c` — PC Professional Blue
- `overture_pc_pcprofessionaltransparent_1000_175_c` — PC Professional Transparent
- `overture_pc_pcprofessionalwhite_1000_175_c` — PC Professional White
- `overture_petg_petgbasicarmygreen_1000_175_c` — PETG Basic Army Green
- `overture_petg_petgbasicblack_1000_175_c` — PETG Basic Black
- `overture_petg_petgbasicblue_1000_175_c` — PETG Basic Blue
- `overture_petg_petgbasicbrown_1000_175_c` — PETG Basic Brown
- `overture_petg_petgbasicdigitalblue_1000_175_c` — PETG Basic Digital Blue
- `overture_petg_petgbasicgold_1000_175_c` — PETG Basic Gold
- `overture_petg_petgbasicgrassgreen_1000_175_c` — PETG Basic Grass Green
- `overture_petg_petgbasicgreen_1000_175_c` — PETG Basic Green
- `overture_petg_petgbasiclightgray_1000_175_c` — PETG Basic Light Gray
- `overture_petg_petgbasicmagenta_1000_175_c` — PETG Basic Magenta
- `overture_petg_petgbasicorange_1000_175_c` — PETG Basic Orange
- `overture_petg_petgbasicpink_1000_175_c` — PETG Basic Pink
- `overture_petg_petgbasicpurple_1000_175_c` — PETG Basic Purple
- `overture_petg_petgbasicred_1000_175_c` — PETG Basic Red
- `overture_petg_petgbasicrockwhite_1000_175_c` — PETG Basic Rock White
- `overture_petg_petgbasicspacegray_1000_175_c` — PETG Basic Space Gray
- `overture_petg_petgbasicsparkleblue_1000_175_c` — PETG Basic Sparkle Blue
- `overture_petg_petgbasicstarryblue_1000_175_c` — PETG Basic Starry Blue
- `overture_petg_petgbasictransparent_1000_175_c` — PETG Basic Transparent
- `overture_petg_petgbasictransparentblue_1000_175_c` — PETG Basic Transparent Blue
- `overture_petg_petgbasictransparentgreen_1000_175_c` — PETG Basic Transparent Green
- `overture_petg_petgbasictransparentred_1000_175_c` — PETG Basic Transparent Red
- `overture_petg_petgbasicwhite_1000_175_c` — PETG Basic White
- `overture_petg_petgbasicyellow_1000_175_c` — PETG Basic Yellow
- `overture_petg_petgclear_1000_175_c` — PETG Clear
- `overture_petg_petgarmygreen_1000_175_r` — PETG Army Green
- `overture_petg_petgblack_1000_175_r` — PETG Black
- `overture_petg_petgblue_1000_175_r` — PETG Blue
- `overture_petg_petgbrown_1000_175_r` — PETG Brown
- `overture_petg_petgdigitalblue_1000_175_r` — PETG Digital Blue
- `overture_petg_petggold_1000_175_r` — PETG Gold
- `overture_petg_petggrassgreen_1000_175_r` — PETG Grass Green
- `overture_petg_petggreen_1000_175_r` — PETG Green
- `overture_petg_petglightgray_1000_175_r` — PETG Light Gray
- `overture_petg_petgmagenta_1000_175_r` — PETG Magenta
- `overture_petg_petgorange_1000_175_r` — PETG Orange
- `overture_petg_petgpink_1000_175_r` — PETG Pink
- `overture_petg_petgpurple_1000_175_r` — PETG Purple
- `overture_petg_petgred_1000_175_r` — PETG Red
- `overture_petg_petgrockwhite_1000_175_r` — PETG Rock White
- `overture_petg_petgspacegray_1000_175_r` — PETG Space Gray
- `overture_petg_petgsparkleblue_1000_175_r` — PETG Sparkle Blue
- `overture_petg_petgstarryblue_1000_175_r` — PETG Starry Blue
- `overture_petg_petgtransparent_1000_175_r` — PETG Transparent
- `overture_petg_petgtransparentblue_1000_175_r` — PETG Transparent Blue
- `overture_petg_petgtransparentgreen_1000_175_r` — PETG Transparent Green
- `overture_petg_petgtransparentred_1000_175_r` — PETG Transparent Red
- `overture_petg_petgwhite_1000_175_r` — PETG White
- `overture_petg_petgyellow_1000_175_r` — PETG Yellow
- `overture_petg_petgclear_1000_175_r` — PETG Clear
- `overture_pla_plaairblack_1000_175_c` — PLA Air Black
- `overture_pla_plaairlightgray_1000_175_c` — PLA Air Light Gray
- `overture_pla_plaairneongreen_1000_175_c` — PLA Air Neon Green
- `overture_pla_plaairorange_1000_175_c` — PLA Air Orange
- `overture_pla_plaairwhite_1000_175_c` — PLA Air White
- `overture_pla_plaairwood_1000_175_c` — PLA Air Wood
- `overture_pla_plaairyellow_1000_175_c` — PLA Air Yellow
- `overture_pla_placfmidnightblack_1000_175_c` — PLA CF Midnight Black
- `overture_pla_placreamblack_1000_175_c` — PLA Cream Black
- `overture_pla_placreamblue_1000_175_c` — PLA Cream Blue
- `overture_pla_placreamgrassgreen_1000_175_c` — PLA Cream Grass Green
- `overture_pla_placreamgray_1000_175_c` — PLA Cream Gray
- `overture_pla_placreamgreen_1000_175_c` — PLA Cream Green
- `overture_pla_placreamlightblue_1000_175_c` — PLA Cream Light Blue
- `overture_pla_placreamlightbrown_1000_175_c` — PLA Cream Light Brown
- `overture_pla_placreamlightgray_1000_175_c` — PLA Cream Light Gray
- `overture_pla_placreamorange_1000_175_c` — PLA Cream Orange
- `overture_pla_placreampink_1000_175_c` — PLA Cream Pink
- `overture_pla_placreampurple_1000_175_c` — PLA Cream Purple
- `overture_pla_placreamred_1000_175_c` — PLA Cream Red
- `overture_pla_placreamwhite_1000_175_c` — PLA Cream White
- `overture_pla_placreamyellow_1000_175_c` — PLA Cream Yellow
- `overture_pla_plaeasybeige_1000_175_c` — PLA Easy Beige
- `overture_pla_plaeasyblack_1000_175_c` — PLA Easy Black
- `overture_pla_plaeasycaramel_1000_175_c` — PLA Easy Caramel
- `overture_pla_plaeasycobaltblue_1000_175_c` — PLA Easy Cobalt Blue
- `overture_pla_plaeasydigitalblue_1000_175_c` — PLA Easy Digital Blue
- `overture_pla_plaeasygreen_1000_175_c` — PLA Easy Green
- `overture_pla_plaeasymagenta_1000_175_c` — PLA Easy Magenta
- `overture_pla_plaeasynatural_1000_175_c` — PLA Easy Natural
- `overture_pla_plaeasyorange_1000_175_c` — PLA Easy Orange
- `overture_pla_plaeasypinegreen_1000_175_c` — PLA Easy Pine Green
- `overture_pla_plaeasypink_1000_175_c` — PLA Easy Pink
- `overture_pla_plaeasypumpkinorange_1000_175_c` — PLA Easy Pumpkin Orange
- `overture_pla_plaeasypurple_1000_175_c` — PLA Easy Purple
- `overture_pla_plaeasyred_1000_175_c` — PLA Easy Red
- `overture_pla_plaeasyrockwhite_1000_175_c` — PLA Easy Rock White
- `overture_pla_plaeasyshimmerbronze_1000_175_c` — PLA Easy Shimmer Bronze
- `overture_pla_plaeasyshimmerdarkgreen_1000_175_c` — PLA Easy Shimmer Dark Green
- `overture_pla_plaeasyshimmerpurple_1000_175_c` — PLA Easy Shimmer Purple
- `overture_pla_plaeasyshimmersilvergreen_1000_175_c` — PLA Easy Shimmer Silver Green
- `overture_pla_plaeasyskyblue_1000_175_c` — PLA Easy Sky Blue
- `overture_pla_plaeasyspacegray_1000_175_c` — PLA Easy Space Gray
- `overture_pla_plaeasywhite_1000_175_c` — PLA Easy White
- `overture_pla_plaeasyyellow_1000_175_c` — PLA Easy Yellow
- `overture_pla_plaeasyyolkyellow_1000_175_c` — PLA Easy Yolk Yellow
- `overture_pla_plaeasyglowblue_1000_175_c` — PLA Easy Glow Blue
- `overture_pla_plaeasygloworange_1000_175_c` — PLA Easy Glow Orange
- `overture_pla_plaeasyglowred_1000_175_c` — PLA Easy Glow Red
- `overture_pla_plaeasyglowyellow_1000_175_c` — PLA Easy Glow Yellow
- `overture_pla_glowplawhite(greenindark)_1000_175_c` — Glow PLA White (Green in Dark)
- `overture_pla_plaauroraberry_1000_175_c` — PLA Aurora Berry
- `overture_pla_plaavocado_1000_175_c` — PLA Avocado
- `overture_pla_plachampagnefrost_1000_175_c` — PLA Champagne Frost
- `overture_pla_plachristmasprism_1000_175_c` — PLA Christmas Prism
- `overture_pla_plahightlightyellow_1000_175_c` — PLA Hightlight Yellow
- `overture_pla_plalemonyellow_1000_175_c` — PLA Lemon Yellow
- `overture_pla_plalightgreen_1000_175_c` — PLA Light Green
- `overture_pla_plametallicgray_1000_175_c` — PLA Metallic Gray
- `overture_pla_planorthernlights_1000_175_c` — PLA Northern Lights
- `overture_pla_plarainbow_1000_175_c` — PLA Rainbow
- `overture_pla_plarocketpop_1000_175_c` — PLA Rocket Pop
- `overture_pla_plasparkleblack_1000_175_c` — PLA Sparkle Black
- `overture_pla_plasparklepurple_1000_175_c` — PLA Sparkle Purple
- `overture_pla_platequilasunrise_1000_175_c` — PLA Tequila Sunrise
- `overture_pla_plaauroraberry_1000_175_r` — PLA Aurora Berry
- `overture_pla_plaavocado_1000_175_r` — PLA Avocado
- `overture_pla_plablack_1000_175_r` — PLA Black
- `overture_pla_plablue_1000_175_r` — PLA Blue
- `overture_pla_plabrown_1000_175_r` — PLA Brown
- `overture_pla_placementgray_1000_175_r` — PLA Cement Gray
- `overture_pla_plachampagnefrost_1000_175_r` — PLA Champagne Frost
- `overture_pla_plachocolate_1000_175_r` — PLA Chocolate
- `overture_pla_plachristmasprism_1000_175_r` — PLA Christmas Prism
- `overture_pla_placoldwhite_1000_175_r` — PLA Cold White
- `overture_pla_plafreshred_1000_175_r` — PLA Fresh Red
- `overture_pla_plaglowindark_1000_175_r` — PLA Glow in Dark
- `overture_pla_plagrayblue_1000_175_r` — PLA Gray Blue
- `overture_pla_plagreen_1000_175_r` — PLA Green
- `overture_pla_plahighlightyellow_1000_175_r` — PLA Highlight Yellow
- `overture_pla_plahightlightyellow_1000_175_r` — PLA Hightlight Yellow
- `overture_pla_plalemonyellow_1000_175_r` — PLA Lemon Yellow
- `overture_pla_plalightblue_1000_175_r` — PLA Light Blue
- `overture_pla_plalightgray_1000_175_r` — PLA Light Gray
- `overture_pla_plalightgreen_1000_175_r` — PLA Light Green
- `overture_pla_plametallicgray_1000_175_r` — PLA Metallic Gray
- `overture_pla_plamidnightblack_1000_175_r` — PLA Midnight Black
- `overture_pla_planorthernlights_1000_175_r` — PLA Northern Lights
- `overture_pla_plaolivegreen_1000_175_r` — PLA Olive Green
- `overture_pla_plaorange_1000_175_r` — PLA Orange
- `overture_pla_plapink_1000_175_r` — PLA Pink
- `overture_pla_plapurple_1000_175_r` — PLA Purple
- `overture_pla_plarainbow_1000_175_r` — PLA Rainbow
- `overture_pla_plared_1000_175_r` — PLA Red
- `overture_pla_plarocketpop_1000_175_r` — PLA Rocket Pop
- `overture_pla_plaroyalgold_1000_175_r` — PLA Royal Gold
- `overture_pla_plaspacegray_1000_175_r` — PLA Space Gray
- `overture_pla_plasparkleblack_1000_175_r` — PLA Sparkle Black
- `overture_pla_plasparklepurple_1000_175_r` — PLA Sparkle Purple
- `overture_pla_platequilasunrise_1000_175_r` — PLA Tequila Sunrise
- `overture_pla_plawhite_1000_175_r` — PLA White
- `overture_pla_playellow_1000_175_r` — PLA Yellow
- `overture_pla_plarefillblack_1000_175_c` — PLA Refill Black
- `overture_pla_plarockalpineforest_1000_175_c` — PLA Rock Alpine Forest
- `overture_pla_plarockbarrierreef_1000_175_c` — PLA Rock Barrier Reef
- `overture_pla_plarockcheesewood_1000_175_c` — PLA Rock Cheesewood
- `overture_pla_plarockhazegray_1000_175_c` — PLA Rock Haze Gray
- `overture_pla_plarockjarrah_1000_175_c` — PLA Rock Jarrah
- `overture_pla_plarockmarigoldyellow_1000_175_c` — PLA Rock Marigold Yellow
- `overture_pla_plarockmistgray_1000_175_c` — PLA Rock Mist Gray
- `overture_pla_plarockmoonlightgray_1000_175_c` — PLA Rock Moonlight Gray
- `overture_pla_plarockmutedgray_1000_175_c` — PLA Rock Muted Gray
- `overture_pla_plarockpaintedhills_1000_175_c` — PLA Rock Painted Hills
- `overture_pla_plarocksedonared_1000_175_c` — PLA Rock Sedona Red
- `overture_pla_plarockslategray_1000_175_c` — PLA Rock Slate Gray
- `overture_pla_plarockwalnutwood_1000_175_c` — PLA Rock Walnut Wood
- `overture_pla_plarockwetlandgreen_1000_175_c` — PLA Rock Wetland Green
- `overture_pla_plarockwhiteoak_1000_175_c` — PLA Rock White Oak
- `overture_pla_plaprofessionalarmygreen_1000_175_c` — PLA Professional Army Green
- `overture_pla_plaprofessionalblack_1000_175_c` — PLA Professional Black
- `overture_pla_plaprofessionalbronze_1000_175_c` — PLA Professional Bronze
- `overture_pla_plaprofessionalbrown_1000_175_c` — PLA Professional Brown
- `overture_pla_plaprofessionalchampagne_1000_175_c` — PLA Professional Champagne
- `overture_pla_plaprofessionalchocolate_1000_175_c` — PLA Professional Chocolate
- `overture_pla_plaprofessionalcopper_1000_175_c` — PLA Professional Copper
- `overture_pla_plaprofessionaldarkblue_1000_175_c` — PLA Professional Dark Blue
- `overture_pla_plaprofessionaldigitalblue_1000_175_c` — PLA Professional Digital Blue
- `overture_pla_plaprofessionalfreshred_1000_175_c` — PLA Professional Fresh Red
- `overture_pla_plaprofessionalgrayblue_1000_175_c` — PLA Professional Gray Blue
- `overture_pla_plaprofessionalgreen_1000_175_c` — PLA Professional Green
- `overture_pla_plaprofessionalhighlightyellow_1000_175_c` — PLA Professional Highlight Yellow
- `overture_pla_plaprofessionallightblue_1000_175_c` — PLA Professional Light Blue
- `overture_pla_plaprofessionallightgray_1000_175_c` — PLA Professional Light Gray
- `overture_pla_plaprofessionallightgreen_1000_175_c` — PLA Professional Light Green
- `overture_pla_plaprofessionalmoonlightsilver_1000_175_c` — PLA Professional Moonlight Silver
- `overture_pla_plaprofessionalolivegreen_1000_175_c` — PLA Professional Olive Green
- `overture_pla_plaprofessionalorange_1000_175_c` — PLA Professional Orange
- `overture_pla_plaprofessionalpink_1000_175_c` — PLA Professional Pink
- `overture_pla_plaprofessionalpurple_1000_175_c` — PLA Professional Purple
- `overture_pla_plaprofessionalred_1000_175_c` — PLA Professional Red
- `overture_pla_plaprofessionalroyalgold_1000_175_c` — PLA Professional Royal Gold
- `overture_pla_plaprofessionalsilvermetal_1000_175_c` — PLA Professional Silver Metal
- `overture_pla_plaprofessionalspacegray_1000_175_c` — PLA Professional Space Gray
- `overture_pla_plaprofessionalsunsetrainbow_1000_175_c` — PLA Professional Sunset Rainbow
- `overture_pla_plaprofessionalwhite_1000_175_c` — PLA Professional White
- `overture_pla_plaprofessionalwine_1000_175_c` — PLA Professional Wine
- `overture_pla_plaprofessionalyellow_1000_175_c` — PLA Professional Yellow
- `overture_pla_plasuperblack_1000_175_c` — PLA Super Black
- `overture_pla_plasuperdarkblue_1000_175_c` — PLA Super Dark Blue
- `overture_pla_plasupergreen_1000_175_c` — PLA Super Green
- `overture_pla_plasuperlightbrown_1000_175_c` — PLA Super Light Brown
- `overture_pla_plasuperlightgray_1000_175_c` — PLA Super Light Gray
- `overture_pla_plasuperorange_1000_175_c` — PLA Super Orange
- `overture_pla_plasuperpink_1000_175_c` — PLA Super Pink
- `overture_pla_plasuperpurple_1000_175_c` — PLA Super Purple
- `overture_pla_plasuperred_1000_175_c` — PLA Super Red
- `overture_pla_plasupersakurapink_1000_175_c` — PLA Super Sakura Pink
- `overture_pla_plasuperwhite_1000_175_c` — PLA Super White
- `overture_pla_plasuperyellow_1000_175_c` — PLA Super Yellow
- `overture_pla_platurborapidblack_1000_175_c` — PLA Turbo Rapid Black
- `overture_pla_platurborapidblue_1000_175_c` — PLA Turbo Rapid Blue
- `overture_pla_platurborapidbrown_1000_175_c` — PLA Turbo Rapid Brown
- `overture_pla_platurborapidgray_1000_175_c` — PLA Turbo Rapid Gray
- `overture_pla_platurborapidgreen_1000_175_c` — PLA Turbo Rapid Green
- `overture_pla_platurborapidmarblegray_1000_175_c` — PLA Turbo Rapid Marble Gray
- `overture_pla_platurborapidred_1000_175_c` — PLA Turbo Rapid Red
- `overture_pla_platurborapidsterwhite_1000_175_c` — PLA Turbo Rapid Ster White
- `overture_tpu_highspeedtpublack_1000_175_c` — High Speed TPU Black
- `overture_tpu_highspeedtpuclear_1000_175_c` — High Speed TPU Clear
- `overture_tpu_highspeedtpugrassgreen_1000_175_c` — High Speed TPU Grass Green
- `overture_tpu_highspeedtpugray_1000_175_c` — High Speed TPU Gray
- `overture_tpu_highspeedtpuluminouspink_1000_175_c` — High Speed TPU Luminous Pink
- `overture_tpu_highspeedtpuneonmagenta_1000_175_c` — High Speed TPU Neon Magenta
- `overture_tpu_highspeedtpuneonyellow_1000_175_c` — High Speed TPU Neon Yellow
- `overture_tpu_highspeedtpuorange_1000_175_c` — High Speed TPU Orange
- `overture_tpu_highspeedtpupastelrose_1000_175_c` — High Speed TPU Pastel Rose
- `overture_tpu_highspeedtpupink_1000_175_c` — High Speed TPU Pink
- `overture_tpu_highspeedtputranslucentblue_1000_175_c` — High Speed TPU Translucent Blue
- `overture_tpu_highspeedtputranslucentgreen_1000_175_c` — High Speed TPU Translucent Green
- `overture_tpu_highspeedtputranslucentorange_1000_175_c` — High Speed TPU Translucent Orange
- `overture_tpu_highspeedtputranslucentpurple_1000_175_c` — High Speed TPU Translucent Purple
- `overture_tpu_highspeedtputranslucentred_1000_175_c` — High Speed TPU Translucent Red
- `overture_tpu_highspeedtpuwhite_1000_175_c` — High Speed TPU White
- `overture_tpu_luminoushighspeedglowtpublue_1000_175_c` — Luminous High Speed Glow TPU Blue
- `overture_tpu_luminoushighspeedglowtpuelectricindigo_1000_175_c` — Luminous High Speed Glow TPU Electric Indigo
- `overture_tpu_luminoushighspeedglowtpugreen_1000_175_c` — Luminous High Speed Glow TPU Green
- `overture_tpu_luminoushighspeedglowtpuorange_1000_175_c` — Luminous High Speed Glow TPU Orange
- `overture_tpu_tpublack_1000_175_c` — TPU Black
- `overture_tpu_tpublue_1000_175_c` — TPU Blue
- `overture_tpu_tpubrightpink_1000_175_c` — TPU Bright Pink
- `overture_tpu_tpubrown_1000_175_c` — TPU Brown
- `overture_tpu_tpudigitalblue_1000_175_c` — TPU Digital Blue
- `overture_tpu_tpugreen_1000_175_c` — TPU Green
- `overture_tpu_tpulightgreen_1000_175_c` — TPU Light Green
- `overture_tpu_tpuneongreen_1000_175_c` — TPU Neon Green
- `overture_tpu_tpuneonorange_1000_175_c` — TPU Neon Orange
- `overture_tpu_tpuneonred_1000_175_c` — TPU Neon Red
- `overture_tpu_tpuorange_1000_175_c` — TPU Orange
- `overture_tpu_tpupurple_1000_175_c` — TPU Purple
- `overture_tpu_tpured_1000_175_c` — TPU Red
- `overture_tpu_tpuspacegrey_1000_175_c` — TPU Space Grey
- `overture_tpu_tputransparent_1000_175_c` — TPU Transparent
- `overture_tpu_tpuwhite_1000_175_c` — TPU White
- `overture_tpu_tpuyellow_1000_175_c` — TPU Yellow
- `overture_pla+_pla+black_1000_175_n` — PLA+ Black
- `overture_pla+_pla+white_1000_175_n` — PLA+ White
- `overture_pla+_pla+yellow_1000_175_n` — PLA+ Yellow
- `overture_pla+_pla+coldwhite_1000_175_n` — PLA+ Cold White
- `overture_pla+_pla+orange_1000_175_n` — PLA+ Orange
- `overture_pla+_pla+lightgray_1000_175_n` — PLA+ Light Gray
- `overture_pla+_pla+purple_1000_175_n` — PLA+ Purple
- `overture_pla+_pla+pink_1000_175_n` — PLA+ Pink
- `overture_pla+_pla+freshred_1000_175_n` — PLA+ Fresh Red
- `overture_pla+_pla+red_1000_175_n` — PLA+ Red
- `overture_pla+_pla+blue_1000_175_n` — PLA+ Blue
- `overture_pla+_pla+green_1000_175_n` — PLA+ Green
- `overture_pla+_pla+grayblue_1000_175_n` — PLA+ Gray Blue
- `overture_pla+_pla+olivegreen_1000_175_n` — PLA+ Olive Green
- `overture_pla+_pla+spacegray_1000_175_n` — PLA+ Space Gray
- `overture_pla+_pla+chocolate_1000_175_n` — PLA+ Chocolate
- `overture_pla+_pla+black_1000_175_r` — PLA+ Black
- `overture_pla+_pla+white_1000_175_r` — PLA+ White
- `overture_pla+_pla+coldwhite_1000_175_r` — PLA+ Cold White
- `overture_pla+_pla+red_1000_175_r` — PLA+ Red
- `overture_pla+_pla+freshred_1000_175_r` — PLA+ Fresh Red
- `overture_pla+_pla+orange_1000_175_r` — PLA+ Orange
- `overture_pla+_pla+pink_1000_175_r` — PLA+ Pink
- `overture_pla+_pla+spacegray_1000_175_r` — PLA+ Space Gray
- `overture_pla+_pla+lightgray_1000_175_r` — PLA+ Light Gray
- `overture_pla+_pla+chocolate_1000_175_r` — PLA+ Chocolate
- `overture_pla+_pla+purple_1000_175_r` — PLA+ Purple
- `overture_pla+_pla+blue_1000_175_r` — PLA+ Blue
- `overture_pla+_pla+grayblue_1000_175_r` — PLA+ Gray Blue
- `overture_pla+_pla+yellow_1000_175_r` — PLA+ Yellow
- `overture_pla+_pla+green_1000_175_r` — PLA+ Green
- `overture_pla+_pla+olivegreen_1000_175_r` — PLA+ Olive Green
- `overture_pa_easynylonblack_1000_175_n` — Easy Nylon Black
- `overture_pa_easynylongray_1000_175_n` — Easy Nylon Gray
