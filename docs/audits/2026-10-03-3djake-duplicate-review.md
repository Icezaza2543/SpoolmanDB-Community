# 3djake duplicate migration review

Base `17b1a8381e510ea30545fc1c66954c9ccc27a2dc`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `e6af047f71baab1ff84ffbdb3b549263a794fcbd39751aa486bc3f26659689e7`.

## Authorization and result

{"groups": 27, "approved_groups": 27, "retired": 27, "deferred": 0, "hard_stops": 0, "before_count": 51916, "after_count": 51889, "brand_before": 281, "brand_after": 254, "registry_before": 1518, "registry_after": 1545, "metadata_fields_changed": 29, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

27 Rule1 normalized matches. Current own-brandTDS v2 dated2024-03-01 supports ASA1.07→1.10, PCTG1.24→1.23 and PETG1.24→1.27; remove PETGbed90 invalid point and use60–80 range. Existing scalar nozzle/ASA/PCTG beds valid within official ranges. PCTG/PETG1.24 flagged as PLA-like default and corrected. HEX/COO/translucency/tare conflicts kept unresolved. No packaging/tare changes, no newproduct/identifier claims. Other-material-default review: [{"id": "3djake_pctg_darkgreen_1000_175_c", "material": "PCTG", "density": 1.24, "nozzle": 260, "resolution": "Current exact-line evidence correction", "unresolved_fields": []}, {"id": "3djake_pctg_white_1000_175_c", "material": "PCTG", "density": 1.24, "nozzle": 260, "resolution": "Current exact-line evidence correction", "unresolved_fields": []}, {"id": "3djake_pctg_black_1000_175_c", "material": "PCTG", "density": 1.24, "nozzle": 260, "resolution": "Current exact-line evidence correction", "unresolved_fields": []}, {"id": "3djake_pctg_silver_1000_175_c", "material": "PCTG", "density": 1.24, "nozzle": 260, "resolution": "Current exact-line evidence correction", "unresolved_fields": []}, {"id": "3djake_pctg_transparentred_1000_175_c", "material": "PCTG", "density": 1.24, "nozzle": 260, "resolution": "Current exact-line evidence correction", "unresolved_fields": []}, {"id": "3djake_pctg_darkblue_1000_175_c", "material": "PCTG", "density": 1.24, "nozzle": 260, "resolution": "Current exact-line evidence correction", "unresolved_fields": []}, {"id": "3djake_petg_darkgray_1000_175_c", "material": "PETG", "density": 1.24, "nozzle": 240, "resolution": "Current exact-line evidence correction", "unresolved_fields": []}, {"id": "3djake_pctg_lightgreen_1000_175_c", "material": "PCTG", "density": 1.24, "nozzle": 260, "resolution": "Current exact-line evidence correction", "unresolved_fields": []}, {"id": "3djake_pctg_transparentyellow_1000_175_c", "material": "PCTG", "density": 1.24, "nozzle": 260, "resolution": "Current exact-line evidence correction", "unresolved_fields": []}, {"id": "3djake_pctg_transparent_1000_175_c", "material": "PCTG", "density": 1.24, "nozzle": 260, "resolution": "Current exact-line evidence correction", "unresolved_fields": []}, {"id": "3djake_pctg_red_1000_175_c", "material": "PCTG", "density": 1.24, "nozzle": 260, "resolution": "Current exact-line evidence correction", "unresolved_fields": []}, {"id": "3djake_pctg_transparentblue_1000_175_c", "material": "PCTG", "density": 1.24, "nozzle": 260, "resolution": "Current exact-line evidence correction", "unresolved_fields": []}, {"id": "3djake_pctg_transparentgreen_1000_175_c", "material": "PCTG", "density": 1.24, "nozzle": 260, "resolution": "Current exact-line evidence correction", "unresolved_fields": []}, {"id": "3djake_pctg_lightblue_1000_175_c", "material": "PCTG", "density": 1.24, "nozzle": 260, "resolution": "Current exact-line evidence correction", "unresolved_fields": []}]

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://www.3djake.com/3djake/asa-black", "tds": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_ASA_V2.pdf", "density": 1.1, "nozzle": [210, 250], "bed": [60, 100]}
- {"url": "https://www.3djake.com/3djake/pctg-black-1", "tds": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_PCTG_V2.pdf", "density": 1.23, "nozzle": [250, 270], "bed": [90, 110]}
- {"url": "https://www.3djake.com/3djake/petg-dark-grey", "tds": "https://3d.nice-cdn.com/upload/file/TDS_PETG.pdf", "density": 1.27, "nozzle": [230, 250], "bed": [60, 80], "note": "Exact discontinued own-brand product uses DarkGrey title and DarkGray description. This is an ordinary cross-template Rule1 match, not an unresolved intra-template spelling tie."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`3djake_asa_asablack_1000_175_c`|`3djake_asa_black_1000_175_c`|`3djake.json::3DJAKE::ASA {color_name}::ASA Black::ASA::1000::1.75::cardboard::False`|
|`3djake_asa_asadarkblue_1000_175_c`|`3djake_asa_darkblue_1000_175_c`|`3djake.json::3DJAKE::ASA {color_name}::ASA Dark Blue::ASA::1000::1.75::cardboard::False`|
|`3djake_asa_asadarkgreen_1000_175_c`|`3djake_asa_darkgreen_1000_175_c`|`3djake.json::3DJAKE::ASA {color_name}::ASA Dark Green::ASA::1000::1.75::cardboard::False`|
|`3djake_asa_asadarkgrey_1000_175_c`|`3djake_asa_darkgrey_1000_175_c`|`3djake.json::3DJAKE::ASA {color_name}::ASA Dark Grey::ASA::1000::1.75::cardboard::False`|
|`3djake_asa_asalightblue_1000_175_c`|`3djake_asa_lightblue_1000_175_c`|`3djake.json::3DJAKE::ASA {color_name}::ASA Light Blue::ASA::1000::1.75::cardboard::False`|
|`3djake_asa_asalightgreen_1000_175_c`|`3djake_asa_lightgreen_1000_175_c`|`3djake.json::3DJAKE::ASA {color_name}::ASA Light Green::ASA::1000::1.75::cardboard::False`|
|`3djake_asa_asalightgrey_1000_175_c`|`3djake_asa_lightgrey_1000_175_c`|`3djake.json::3DJAKE::ASA {color_name}::ASA Light Grey::ASA::1000::1.75::cardboard::False`|
|`3djake_asa_asaorange_1000_175_c`|`3djake_asa_orange_1000_175_c`|`3djake.json::3DJAKE::ASA {color_name}::ASA Orange::ASA::1000::1.75::cardboard::False`|
|`3djake_asa_asapurple_1000_175_c`|`3djake_asa_purple_1000_175_c`|`3djake.json::3DJAKE::ASA {color_name}::ASA Purple::ASA::1000::1.75::cardboard::False`|
|`3djake_asa_asared_1000_175_c`|`3djake_asa_red_1000_175_c`|`3djake.json::3DJAKE::ASA {color_name}::ASA Red::ASA::1000::1.75::cardboard::False`|
|`3djake_asa_asasilver_1000_175_c`|`3djake_asa_silver_1000_175_c`|`3djake.json::3DJAKE::ASA {color_name}::ASA Silver::ASA::1000::1.75::cardboard::False`|
|`3djake_asa_asawhite_1000_175_c`|`3djake_asa_white_1000_175_c`|`3djake.json::3DJAKE::ASA {color_name}::ASA White::ASA::1000::1.75::cardboard::False`|
|`3djake_asa_asayellow_1000_175_c`|`3djake_asa_yellow_1000_175_c`|`3djake.json::3DJAKE::ASA {color_name}::ASA Yellow::ASA::1000::1.75::cardboard::False`|
|`3djake_pctg_pctgblack_1000_175_c`|`3djake_pctg_black_1000_175_c`|`3djake.json::3DJAKE::PCTG {color_name}::PCTG Black::PCTG::1000::1.75::cardboard::False`|
|`3djake_pctg_pctgdarkblue_1000_175_c`|`3djake_pctg_darkblue_1000_175_c`|`3djake.json::3DJAKE::PCTG {color_name}::PCTG Dark Blue::PCTG::1000::1.75::cardboard::False`|
|`3djake_pctg_pctgdarkgreen_1000_175_c`|`3djake_pctg_darkgreen_1000_175_c`|`3djake.json::3DJAKE::PCTG {color_name}::PCTG Dark Green::PCTG::1000::1.75::cardboard::False`|
|`3djake_pctg_pctglightblue_1000_175_c`|`3djake_pctg_lightblue_1000_175_c`|`3djake.json::3DJAKE::PCTG {color_name}::PCTG Light Blue::PCTG::1000::1.75::cardboard::False`|
|`3djake_pctg_pctglightgreen_1000_175_c`|`3djake_pctg_lightgreen_1000_175_c`|`3djake.json::3DJAKE::PCTG {color_name}::PCTG Light Green::PCTG::1000::1.75::cardboard::False`|
|`3djake_pctg_pctgred_1000_175_c`|`3djake_pctg_red_1000_175_c`|`3djake.json::3DJAKE::PCTG {color_name}::PCTG Red::PCTG::1000::1.75::cardboard::False`|
|`3djake_pctg_pctgsilver_1000_175_c`|`3djake_pctg_silver_1000_175_c`|`3djake.json::3DJAKE::PCTG {color_name}::PCTG Silver::PCTG::1000::1.75::cardboard::False`|
|`3djake_pctg_pctgtransparent_1000_175_c`|`3djake_pctg_transparent_1000_175_c`|`3djake.json::3DJAKE::PCTG {color_name}::PCTG Transparent::PCTG::1000::1.75::cardboard::False`|
|`3djake_pctg_pctgtransparentblue_1000_175_c`|`3djake_pctg_transparentblue_1000_175_c`|`3djake.json::3DJAKE::PCTG {color_name}::PCTG Transparent Blue::PCTG::1000::1.75::cardboard::False`|
|`3djake_pctg_pctgtransparentgreen_1000_175_c`|`3djake_pctg_transparentgreen_1000_175_c`|`3djake.json::3DJAKE::PCTG {color_name}::PCTG Transparent Green::PCTG::1000::1.75::cardboard::False`|
|`3djake_pctg_pctgtransparentred_1000_175_c`|`3djake_pctg_transparentred_1000_175_c`|`3djake.json::3DJAKE::PCTG {color_name}::PCTG Transparent Red::PCTG::1000::1.75::cardboard::False`|
|`3djake_pctg_pctgtransparentyellow_1000_175_c`|`3djake_pctg_transparentyellow_1000_175_c`|`3djake.json::3DJAKE::PCTG {color_name}::PCTG Transparent Yellow::PCTG::1000::1.75::cardboard::False`|
|`3djake_pctg_pctgwhite_1000_175_c`|`3djake_pctg_white_1000_175_c`|`3djake.json::3DJAKE::PCTG {color_name}::PCTG White::PCTG::1000::1.75::cardboard::False`|
|`3djake_petg_petgdarkgrey_1000_175_c`|`3djake_petg_darkgray_1000_175_c`|`3djake.json::3DJAKE::PETG {color_name}::PETG Dark Grey::PETG::1000::1.75::cardboard::False`|

## Per-group decisions and unresolved metadata

### DJ001: dup-b03fb1613e5c4ac67ad870792f32cc52a202edc0d49483a97b887327d31675b6

Status: APPROVED; survivor `3djake_asa_black_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_asa_asablack_1000_175_c`|`ASA {color_name}`|`Black`|{"source_file": "3djake.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`3djake_asa_black_1000_175_c`|`{color_name}`|`Black`|{"source_file": "3djake.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "3djake_asa_asablack_1000_175_c": null,
    "3djake_asa_black_1000_175_c": 240
  },
  "color_hex": {
    "3djake_asa_asablack_1000_175_c": "292824",
    "3djake_asa_black_1000_175_c": "414040"
  },
  "extruder_temp": {
    "3djake_asa_asablack_1000_175_c": null,
    "3djake_asa_black_1000_175_c": 250
  },
  "extruder_temp_range": {
    "3djake_asa_asablack_1000_175_c": [
      235,
      260
    ],
    "3djake_asa_black_1000_175_c": null
  },
  "bed_temp": {
    "3djake_asa_asablack_1000_175_c": null,
    "3djake_asa_black_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_asa_asablack_1000_175_c": [
      90,
      110
    ],
    "3djake_asa_black_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_asa_asablack_1000_175_c": "CZ",
    "3djake_asa_black_1000_175_c": "AT"
  }
}
```

### DJ002: dup-37ba1e2e321d69cc221b3019e3ed34375ee50e88758f13a6532f8e41ddfc290e

Status: APPROVED; survivor `3djake_asa_darkblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_asa_asadarkblue_1000_175_c`|`ASA {color_name}`|`Dark Blue`|{"source_file": "3djake.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`3djake_asa_darkblue_1000_175_c`|`{color_name}`|`Dark Blue`|{"source_file": "3djake.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "3djake_asa_asadarkblue_1000_175_c": null,
    "3djake_asa_darkblue_1000_175_c": 240
  },
  "color_hex": {
    "3djake_asa_asadarkblue_1000_175_c": "0353BA",
    "3djake_asa_darkblue_1000_175_c": "2F4D86"
  },
  "extruder_temp": {
    "3djake_asa_asadarkblue_1000_175_c": null,
    "3djake_asa_darkblue_1000_175_c": 250
  },
  "extruder_temp_range": {
    "3djake_asa_asadarkblue_1000_175_c": [
      235,
      260
    ],
    "3djake_asa_darkblue_1000_175_c": null
  },
  "bed_temp": {
    "3djake_asa_asadarkblue_1000_175_c": null,
    "3djake_asa_darkblue_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_asa_asadarkblue_1000_175_c": [
      90,
      110
    ],
    "3djake_asa_darkblue_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_asa_asadarkblue_1000_175_c": "CZ",
    "3djake_asa_darkblue_1000_175_c": "AT"
  }
}
```

### DJ003: dup-55954a8164a3e9d857d3719c4529aa655e55347182503764d3d824ca09899e61

Status: APPROVED; survivor `3djake_asa_darkgreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_asa_asadarkgreen_1000_175_c`|`ASA {color_name}`|`Dark Green`|{"source_file": "3djake.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`3djake_asa_darkgreen_1000_175_c`|`{color_name}`|`Dark Green`|{"source_file": "3djake.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "3djake_asa_asadarkgreen_1000_175_c": null,
    "3djake_asa_darkgreen_1000_175_c": 240
  },
  "color_hex": {
    "3djake_asa_asadarkgreen_1000_175_c": "11784F",
    "3djake_asa_darkgreen_1000_175_c": "187359"
  },
  "extruder_temp": {
    "3djake_asa_asadarkgreen_1000_175_c": null,
    "3djake_asa_darkgreen_1000_175_c": 250
  },
  "extruder_temp_range": {
    "3djake_asa_asadarkgreen_1000_175_c": [
      235,
      260
    ],
    "3djake_asa_darkgreen_1000_175_c": null
  },
  "bed_temp": {
    "3djake_asa_asadarkgreen_1000_175_c": null,
    "3djake_asa_darkgreen_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_asa_asadarkgreen_1000_175_c": [
      90,
      110
    ],
    "3djake_asa_darkgreen_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_asa_asadarkgreen_1000_175_c": "CZ",
    "3djake_asa_darkgreen_1000_175_c": "AT"
  }
}
```

### DJ004: dup-9f5b84f58ebc7f99a19e665c759611de010fae4c7b14719a4cda21969e24c223

Status: APPROVED; survivor `3djake_asa_darkgrey_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_asa_asadarkgrey_1000_175_c`|`ASA {color_name}`|`Dark Grey`|{"source_file": "3djake.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`3djake_asa_darkgrey_1000_175_c`|`{color_name}`|`Dark Grey`|{"source_file": "3djake.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "3djake_asa_asadarkgrey_1000_175_c": null,
    "3djake_asa_darkgrey_1000_175_c": 240
  },
  "color_hex": {
    "3djake_asa_asadarkgrey_1000_175_c": "3F4647",
    "3djake_asa_darkgrey_1000_175_c": "5D6366"
  },
  "extruder_temp": {
    "3djake_asa_asadarkgrey_1000_175_c": null,
    "3djake_asa_darkgrey_1000_175_c": 250
  },
  "extruder_temp_range": {
    "3djake_asa_asadarkgrey_1000_175_c": [
      235,
      260
    ],
    "3djake_asa_darkgrey_1000_175_c": null
  },
  "bed_temp": {
    "3djake_asa_asadarkgrey_1000_175_c": null,
    "3djake_asa_darkgrey_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_asa_asadarkgrey_1000_175_c": [
      90,
      110
    ],
    "3djake_asa_darkgrey_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_asa_asadarkgrey_1000_175_c": "CZ",
    "3djake_asa_darkgrey_1000_175_c": "AT"
  }
}
```

### DJ005: dup-767b794b66433c00d318962aa9634dad5e0e5a2f1198b7107237bf0e97ec75c5

Status: APPROVED; survivor `3djake_asa_lightblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_asa_asalightblue_1000_175_c`|`ASA {color_name}`|`Light Blue`|{"source_file": "3djake.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`3djake_asa_lightblue_1000_175_c`|`{color_name}`|`Light Blue`|{"source_file": "3djake.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "3djake_asa_asalightblue_1000_175_c": null,
    "3djake_asa_lightblue_1000_175_c": 240
  },
  "color_hex": {
    "3djake_asa_asalightblue_1000_175_c": "0378D0",
    "3djake_asa_lightblue_1000_175_c": "0083B4"
  },
  "extruder_temp": {
    "3djake_asa_asalightblue_1000_175_c": null,
    "3djake_asa_lightblue_1000_175_c": 250
  },
  "extruder_temp_range": {
    "3djake_asa_asalightblue_1000_175_c": [
      235,
      260
    ],
    "3djake_asa_lightblue_1000_175_c": null
  },
  "bed_temp": {
    "3djake_asa_asalightblue_1000_175_c": null,
    "3djake_asa_lightblue_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_asa_asalightblue_1000_175_c": [
      90,
      110
    ],
    "3djake_asa_lightblue_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_asa_asalightblue_1000_175_c": "CZ",
    "3djake_asa_lightblue_1000_175_c": "AT"
  }
}
```

### DJ006: dup-2395c1cd15bc289f40c32b5941677745ecb9723ddfbde9a92f4e801b58600466

Status: APPROVED; survivor `3djake_asa_lightgreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_asa_asalightgreen_1000_175_c`|`ASA {color_name}`|`Light Green`|{"source_file": "3djake.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`3djake_asa_lightgreen_1000_175_c`|`{color_name}`|`Light Green`|{"source_file": "3djake.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "3djake_asa_asalightgreen_1000_175_c": null,
    "3djake_asa_lightgreen_1000_175_c": 240
  },
  "color_hex": {
    "3djake_asa_asalightgreen_1000_175_c": "06B100",
    "3djake_asa_lightgreen_1000_175_c": "699E4B"
  },
  "extruder_temp": {
    "3djake_asa_asalightgreen_1000_175_c": null,
    "3djake_asa_lightgreen_1000_175_c": 250
  },
  "extruder_temp_range": {
    "3djake_asa_asalightgreen_1000_175_c": [
      235,
      260
    ],
    "3djake_asa_lightgreen_1000_175_c": null
  },
  "bed_temp": {
    "3djake_asa_asalightgreen_1000_175_c": null,
    "3djake_asa_lightgreen_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_asa_asalightgreen_1000_175_c": [
      90,
      110
    ],
    "3djake_asa_lightgreen_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_asa_asalightgreen_1000_175_c": "CZ",
    "3djake_asa_lightgreen_1000_175_c": "AT"
  }
}
```

### DJ007: dup-6106a472b278c5f4f735ccd2ae7d434a12d106f6caf8db6be36abf9e853f9909

Status: APPROVED; survivor `3djake_asa_lightgrey_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_asa_asalightgrey_1000_175_c`|`ASA {color_name}`|`Light Grey`|{"source_file": "3djake.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`3djake_asa_lightgrey_1000_175_c`|`{color_name}`|`Light Grey`|{"source_file": "3djake.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "3djake_asa_asalightgrey_1000_175_c": null,
    "3djake_asa_lightgrey_1000_175_c": 240
  },
  "color_hex": {
    "3djake_asa_asalightgrey_1000_175_c": "DED9D4",
    "3djake_asa_lightgrey_1000_175_c": "C8CBC8"
  },
  "extruder_temp": {
    "3djake_asa_asalightgrey_1000_175_c": null,
    "3djake_asa_lightgrey_1000_175_c": 250
  },
  "extruder_temp_range": {
    "3djake_asa_asalightgrey_1000_175_c": [
      235,
      260
    ],
    "3djake_asa_lightgrey_1000_175_c": null
  },
  "bed_temp": {
    "3djake_asa_asalightgrey_1000_175_c": null,
    "3djake_asa_lightgrey_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_asa_asalightgrey_1000_175_c": [
      90,
      110
    ],
    "3djake_asa_lightgrey_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_asa_asalightgrey_1000_175_c": "CZ",
    "3djake_asa_lightgrey_1000_175_c": "AT"
  }
}
```

### DJ008: dup-f7611570ca919579a98e0d33169813febabfbbbb742c7c7d5d38afd63e7243d5

Status: APPROVED; survivor `3djake_asa_orange_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_asa_asaorange_1000_175_c`|`ASA {color_name}`|`Orange`|{"source_file": "3djake.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`3djake_asa_orange_1000_175_c`|`{color_name}`|`Orange`|{"source_file": "3djake.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "3djake_asa_asaorange_1000_175_c": null,
    "3djake_asa_orange_1000_175_c": 240
  },
  "color_hex": {
    "3djake_asa_asaorange_1000_175_c": "F55928",
    "3djake_asa_orange_1000_175_c": "EE713A"
  },
  "extruder_temp": {
    "3djake_asa_asaorange_1000_175_c": null,
    "3djake_asa_orange_1000_175_c": 250
  },
  "extruder_temp_range": {
    "3djake_asa_asaorange_1000_175_c": [
      235,
      260
    ],
    "3djake_asa_orange_1000_175_c": null
  },
  "bed_temp": {
    "3djake_asa_asaorange_1000_175_c": null,
    "3djake_asa_orange_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_asa_asaorange_1000_175_c": [
      90,
      110
    ],
    "3djake_asa_orange_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_asa_asaorange_1000_175_c": "CZ",
    "3djake_asa_orange_1000_175_c": "AT"
  }
}
```

### DJ009: dup-6ce141f69401b9ed92b4ab9303dca08bc8ffe15b3cb2f408257aaef677aa5c5e

Status: APPROVED; survivor `3djake_asa_purple_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_asa_asapurple_1000_175_c`|`ASA {color_name}`|`Purple`|{"source_file": "3djake.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`3djake_asa_purple_1000_175_c`|`{color_name}`|`Purple`|{"source_file": "3djake.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "3djake_asa_asapurple_1000_175_c": null,
    "3djake_asa_purple_1000_175_c": 240
  },
  "color_hex": {
    "3djake_asa_asapurple_1000_175_c": "A368BB",
    "3djake_asa_purple_1000_175_c": "8072A1"
  },
  "extruder_temp": {
    "3djake_asa_asapurple_1000_175_c": null,
    "3djake_asa_purple_1000_175_c": 250
  },
  "extruder_temp_range": {
    "3djake_asa_asapurple_1000_175_c": [
      235,
      260
    ],
    "3djake_asa_purple_1000_175_c": null
  },
  "bed_temp": {
    "3djake_asa_asapurple_1000_175_c": null,
    "3djake_asa_purple_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_asa_asapurple_1000_175_c": [
      90,
      110
    ],
    "3djake_asa_purple_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_asa_asapurple_1000_175_c": "CZ",
    "3djake_asa_purple_1000_175_c": "AT"
  }
}
```

### DJ010: dup-892df7432ec1cd6475fb795800fefe282fe0a825d63e2ebc03f68207e6fe1393

Status: APPROVED; survivor `3djake_asa_red_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_asa_asared_1000_175_c`|`ASA {color_name}`|`Red`|{"source_file": "3djake.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`3djake_asa_red_1000_175_c`|`{color_name}`|`Red`|{"source_file": "3djake.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "3djake_asa_asared_1000_175_c": null,
    "3djake_asa_red_1000_175_c": 240
  },
  "color_hex": {
    "3djake_asa_asared_1000_175_c": "EC0000",
    "3djake_asa_red_1000_175_c": "BE3B37"
  },
  "extruder_temp": {
    "3djake_asa_asared_1000_175_c": null,
    "3djake_asa_red_1000_175_c": 250
  },
  "extruder_temp_range": {
    "3djake_asa_asared_1000_175_c": [
      235,
      260
    ],
    "3djake_asa_red_1000_175_c": null
  },
  "bed_temp": {
    "3djake_asa_asared_1000_175_c": null,
    "3djake_asa_red_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_asa_asared_1000_175_c": [
      90,
      110
    ],
    "3djake_asa_red_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_asa_asared_1000_175_c": "CZ",
    "3djake_asa_red_1000_175_c": "AT"
  }
}
```

### DJ011: dup-c672ac410ca2dea271a96525fd69ba2bee8046f3dca68a4ca1a6868bb4940a42

Status: APPROVED; survivor `3djake_asa_silver_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_asa_asasilver_1000_175_c`|`ASA {color_name}`|`Silver`|{"source_file": "3djake.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`3djake_asa_silver_1000_175_c`|`{color_name}`|`Silver`|{"source_file": "3djake.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "3djake_asa_asasilver_1000_175_c": null,
    "3djake_asa_silver_1000_175_c": 240
  },
  "color_hex": {
    "3djake_asa_asasilver_1000_175_c": "808080",
    "3djake_asa_silver_1000_175_c": "A5A5A4"
  },
  "extruder_temp": {
    "3djake_asa_asasilver_1000_175_c": null,
    "3djake_asa_silver_1000_175_c": 250
  },
  "extruder_temp_range": {
    "3djake_asa_asasilver_1000_175_c": [
      235,
      260
    ],
    "3djake_asa_silver_1000_175_c": null
  },
  "bed_temp": {
    "3djake_asa_asasilver_1000_175_c": null,
    "3djake_asa_silver_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_asa_asasilver_1000_175_c": [
      90,
      110
    ],
    "3djake_asa_silver_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_asa_asasilver_1000_175_c": "CZ",
    "3djake_asa_silver_1000_175_c": "AT"
  }
}
```

### DJ012: dup-002a72fe0a83852fb7ef0704065f7bd08a87cc6990c7b06c091d3b3eb0d27439

Status: APPROVED; survivor `3djake_asa_white_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_asa_asawhite_1000_175_c`|`ASA {color_name}`|`White`|{"source_file": "3djake.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`3djake_asa_white_1000_175_c`|`{color_name}`|`White`|{"source_file": "3djake.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "3djake_asa_asawhite_1000_175_c": null,
    "3djake_asa_white_1000_175_c": 240
  },
  "color_hex": {
    "3djake_asa_asawhite_1000_175_c": "F5F5F5",
    "3djake_asa_white_1000_175_c": "EEEEED"
  },
  "extruder_temp": {
    "3djake_asa_asawhite_1000_175_c": null,
    "3djake_asa_white_1000_175_c": 250
  },
  "extruder_temp_range": {
    "3djake_asa_asawhite_1000_175_c": [
      235,
      260
    ],
    "3djake_asa_white_1000_175_c": null
  },
  "bed_temp": {
    "3djake_asa_asawhite_1000_175_c": null,
    "3djake_asa_white_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_asa_asawhite_1000_175_c": [
      90,
      110
    ],
    "3djake_asa_white_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_asa_asawhite_1000_175_c": "CZ",
    "3djake_asa_white_1000_175_c": "AT"
  }
}
```

### DJ013: dup-eb29318ff94ccf7d1704d1748e178bfb17e6c9307fe1fa19f244de16e84d3f93

Status: APPROVED; survivor `3djake_asa_yellow_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_asa_asayellow_1000_175_c`|`ASA {color_name}`|`Yellow`|{"source_file": "3djake.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`3djake_asa_yellow_1000_175_c`|`{color_name}`|`Yellow`|{"source_file": "3djake.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "3djake_asa_asayellow_1000_175_c": null,
    "3djake_asa_yellow_1000_175_c": 240
  },
  "color_hex": {
    "3djake_asa_asayellow_1000_175_c": "F8CC00",
    "3djake_asa_yellow_1000_175_c": "F9BA09"
  },
  "extruder_temp": {
    "3djake_asa_asayellow_1000_175_c": null,
    "3djake_asa_yellow_1000_175_c": 250
  },
  "extruder_temp_range": {
    "3djake_asa_asayellow_1000_175_c": [
      235,
      260
    ],
    "3djake_asa_yellow_1000_175_c": null
  },
  "bed_temp": {
    "3djake_asa_asayellow_1000_175_c": null,
    "3djake_asa_yellow_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_asa_asayellow_1000_175_c": [
      90,
      110
    ],
    "3djake_asa_yellow_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_asa_asayellow_1000_175_c": "CZ",
    "3djake_asa_yellow_1000_175_c": "AT"
  }
}
```

### DJ014: dup-18c8ef5c2c5c0de16aaf43990b5ce34732427f08827b003063873aa34886e36f

Status: APPROVED; survivor `3djake_pctg_black_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_pctg_black_1000_175_c`|`{color_name}`|`Black`|{"source_file": "3djake.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|
|`3djake_pctg_pctgblack_1000_175_c`|`PCTG {color_name}`|`Black`|{"source_file": "3djake.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "3djake_pctg_black_1000_175_c": 1.24,
    "3djake_pctg_pctgblack_1000_175_c": 1.23
  },
  "spool_weight": {
    "3djake_pctg_black_1000_175_c": 231,
    "3djake_pctg_pctgblack_1000_175_c": null
  },
  "color_hex": {
    "3djake_pctg_black_1000_175_c": "000000",
    "3djake_pctg_pctgblack_1000_175_c": "292824"
  },
  "extruder_temp": {
    "3djake_pctg_black_1000_175_c": 260,
    "3djake_pctg_pctgblack_1000_175_c": null
  },
  "extruder_temp_range": {
    "3djake_pctg_black_1000_175_c": null,
    "3djake_pctg_pctgblack_1000_175_c": [
      230,
      260
    ]
  },
  "bed_temp": {
    "3djake_pctg_black_1000_175_c": 100,
    "3djake_pctg_pctgblack_1000_175_c": null
  },
  "bed_temp_range": {
    "3djake_pctg_black_1000_175_c": null,
    "3djake_pctg_pctgblack_1000_175_c": [
      70,
      90
    ]
  },
  "country_of_origin": {
    "3djake_pctg_black_1000_175_c": "AT",
    "3djake_pctg_pctgblack_1000_175_c": "CZ"
  }
}
```

### DJ015: dup-4683b30e7368e8725959399b1351077e8f27300db5c25b89c7bb4c8729c26e07

Status: APPROVED; survivor `3djake_pctg_darkblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_pctg_darkblue_1000_175_c`|`{color_name}`|`Dark Blue`|{"source_file": "3djake.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|
|`3djake_pctg_pctgdarkblue_1000_175_c`|`PCTG {color_name}`|`Dark Blue`|{"source_file": "3djake.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "3djake_pctg_darkblue_1000_175_c": 1.24,
    "3djake_pctg_pctgdarkblue_1000_175_c": 1.23
  },
  "spool_weight": {
    "3djake_pctg_darkblue_1000_175_c": 231,
    "3djake_pctg_pctgdarkblue_1000_175_c": null
  },
  "color_hex": {
    "3djake_pctg_darkblue_1000_175_c": "002351",
    "3djake_pctg_pctgdarkblue_1000_175_c": "09048E"
  },
  "extruder_temp": {
    "3djake_pctg_darkblue_1000_175_c": 260,
    "3djake_pctg_pctgdarkblue_1000_175_c": null
  },
  "extruder_temp_range": {
    "3djake_pctg_darkblue_1000_175_c": null,
    "3djake_pctg_pctgdarkblue_1000_175_c": [
      230,
      260
    ]
  },
  "bed_temp": {
    "3djake_pctg_darkblue_1000_175_c": 100,
    "3djake_pctg_pctgdarkblue_1000_175_c": null
  },
  "bed_temp_range": {
    "3djake_pctg_darkblue_1000_175_c": null,
    "3djake_pctg_pctgdarkblue_1000_175_c": [
      70,
      90
    ]
  },
  "country_of_origin": {
    "3djake_pctg_darkblue_1000_175_c": "AT",
    "3djake_pctg_pctgdarkblue_1000_175_c": "CZ"
  }
}
```

### DJ016: dup-0a48f4d259d17a779755c0e7d7caf89b4fa3b9cb6f669e938c2c72c1aa004faf

Status: APPROVED; survivor `3djake_pctg_darkgreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_pctg_darkgreen_1000_175_c`|`{color_name}`|`Dark Green`|{"source_file": "3djake.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|
|`3djake_pctg_pctgdarkgreen_1000_175_c`|`PCTG {color_name}`|`Dark Green`|{"source_file": "3djake.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "3djake_pctg_darkgreen_1000_175_c": 1.24,
    "3djake_pctg_pctgdarkgreen_1000_175_c": 1.23
  },
  "spool_weight": {
    "3djake_pctg_darkgreen_1000_175_c": 231,
    "3djake_pctg_pctgdarkgreen_1000_175_c": null
  },
  "color_hex": {
    "3djake_pctg_darkgreen_1000_175_c": "036606",
    "3djake_pctg_pctgdarkgreen_1000_175_c": "37823F"
  },
  "extruder_temp": {
    "3djake_pctg_darkgreen_1000_175_c": 260,
    "3djake_pctg_pctgdarkgreen_1000_175_c": null
  },
  "extruder_temp_range": {
    "3djake_pctg_darkgreen_1000_175_c": null,
    "3djake_pctg_pctgdarkgreen_1000_175_c": [
      230,
      260
    ]
  },
  "bed_temp": {
    "3djake_pctg_darkgreen_1000_175_c": 100,
    "3djake_pctg_pctgdarkgreen_1000_175_c": null
  },
  "bed_temp_range": {
    "3djake_pctg_darkgreen_1000_175_c": null,
    "3djake_pctg_pctgdarkgreen_1000_175_c": [
      70,
      90
    ]
  },
  "country_of_origin": {
    "3djake_pctg_darkgreen_1000_175_c": "AT",
    "3djake_pctg_pctgdarkgreen_1000_175_c": "CZ"
  }
}
```

### DJ017: dup-f545cec9675c10197fd2590a87907504abdbcc4249735bfdec9e8a38b6071995

Status: APPROVED; survivor `3djake_pctg_lightblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_pctg_lightblue_1000_175_c`|`{color_name}`|`Light Blue`|{"source_file": "3djake.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|
|`3djake_pctg_pctglightblue_1000_175_c`|`PCTG {color_name}`|`Light Blue`|{"source_file": "3djake.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "3djake_pctg_lightblue_1000_175_c": 1.24,
    "3djake_pctg_pctglightblue_1000_175_c": 1.23
  },
  "spool_weight": {
    "3djake_pctg_lightblue_1000_175_c": 231,
    "3djake_pctg_pctglightblue_1000_175_c": null
  },
  "color_hex": {
    "3djake_pctg_lightblue_1000_175_c": "017cff",
    "3djake_pctg_pctglightblue_1000_175_c": "0078BF"
  },
  "extruder_temp": {
    "3djake_pctg_lightblue_1000_175_c": 260,
    "3djake_pctg_pctglightblue_1000_175_c": null
  },
  "extruder_temp_range": {
    "3djake_pctg_lightblue_1000_175_c": null,
    "3djake_pctg_pctglightblue_1000_175_c": [
      230,
      260
    ]
  },
  "bed_temp": {
    "3djake_pctg_lightblue_1000_175_c": 100,
    "3djake_pctg_pctglightblue_1000_175_c": null
  },
  "bed_temp_range": {
    "3djake_pctg_lightblue_1000_175_c": null,
    "3djake_pctg_pctglightblue_1000_175_c": [
      70,
      90
    ]
  },
  "country_of_origin": {
    "3djake_pctg_lightblue_1000_175_c": "AT",
    "3djake_pctg_pctglightblue_1000_175_c": "CZ"
  }
}
```

### DJ018: dup-a3a36d984e9a57c0c1a887dce932204a84a35f97d545005b0e5ab69d0b5765d5

Status: APPROVED; survivor `3djake_pctg_lightgreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_pctg_lightgreen_1000_175_c`|`{color_name}`|`Light Green`|{"source_file": "3djake.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|
|`3djake_pctg_pctglightgreen_1000_175_c`|`PCTG {color_name}`|`Light Green`|{"source_file": "3djake.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "3djake_pctg_lightgreen_1000_175_c": 1.24,
    "3djake_pctg_pctglightgreen_1000_175_c": 1.23
  },
  "spool_weight": {
    "3djake_pctg_lightgreen_1000_175_c": 231,
    "3djake_pctg_pctglightgreen_1000_175_c": null
  },
  "color_hex": {
    "3djake_pctg_lightgreen_1000_175_c": "65c525",
    "3djake_pctg_pctglightgreen_1000_175_c": "26A648"
  },
  "extruder_temp": {
    "3djake_pctg_lightgreen_1000_175_c": 260,
    "3djake_pctg_pctglightgreen_1000_175_c": null
  },
  "extruder_temp_range": {
    "3djake_pctg_lightgreen_1000_175_c": null,
    "3djake_pctg_pctglightgreen_1000_175_c": [
      230,
      260
    ]
  },
  "bed_temp": {
    "3djake_pctg_lightgreen_1000_175_c": 100,
    "3djake_pctg_pctglightgreen_1000_175_c": null
  },
  "bed_temp_range": {
    "3djake_pctg_lightgreen_1000_175_c": null,
    "3djake_pctg_pctglightgreen_1000_175_c": [
      70,
      90
    ]
  },
  "country_of_origin": {
    "3djake_pctg_lightgreen_1000_175_c": "AT",
    "3djake_pctg_pctglightgreen_1000_175_c": "CZ"
  }
}
```

### DJ019: dup-b259cc112655dad29d1b1819ddaecaeea5edf512ddcd76049f5f00afad5743be

Status: APPROVED; survivor `3djake_pctg_red_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_pctg_pctgred_1000_175_c`|`PCTG {color_name}`|`Red`|{"source_file": "3djake.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|
|`3djake_pctg_red_1000_175_c`|`{color_name}`|`Red`|{"source_file": "3djake.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "3djake_pctg_pctgred_1000_175_c": 1.23,
    "3djake_pctg_red_1000_175_c": 1.24
  },
  "spool_weight": {
    "3djake_pctg_pctgred_1000_175_c": null,
    "3djake_pctg_red_1000_175_c": 231
  },
  "color_hex": {
    "3djake_pctg_pctgred_1000_175_c": "C01616",
    "3djake_pctg_red_1000_175_c": "d80000"
  },
  "extruder_temp": {
    "3djake_pctg_pctgred_1000_175_c": null,
    "3djake_pctg_red_1000_175_c": 260
  },
  "extruder_temp_range": {
    "3djake_pctg_pctgred_1000_175_c": [
      230,
      260
    ],
    "3djake_pctg_red_1000_175_c": null
  },
  "bed_temp": {
    "3djake_pctg_pctgred_1000_175_c": null,
    "3djake_pctg_red_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_pctg_pctgred_1000_175_c": [
      70,
      90
    ],
    "3djake_pctg_red_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_pctg_pctgred_1000_175_c": "CZ",
    "3djake_pctg_red_1000_175_c": "AT"
  }
}
```

### DJ020: dup-1dcb9ff32bdcd9ab95d8492e3d4f978f41ee8856c1137d1d0970770a93c30aef

Status: APPROVED; survivor `3djake_pctg_silver_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_pctg_pctgsilver_1000_175_c`|`PCTG {color_name}`|`Silver`|{"source_file": "3djake.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|
|`3djake_pctg_silver_1000_175_c`|`{color_name}`|`Silver`|{"source_file": "3djake.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "3djake_pctg_pctgsilver_1000_175_c": 1.23,
    "3djake_pctg_silver_1000_175_c": 1.24
  },
  "spool_weight": {
    "3djake_pctg_pctgsilver_1000_175_c": null,
    "3djake_pctg_silver_1000_175_c": 231
  },
  "color_hex": {
    "3djake_pctg_pctgsilver_1000_175_c": "9C9D9D",
    "3djake_pctg_silver_1000_175_c": "cecece"
  },
  "extruder_temp": {
    "3djake_pctg_pctgsilver_1000_175_c": null,
    "3djake_pctg_silver_1000_175_c": 260
  },
  "extruder_temp_range": {
    "3djake_pctg_pctgsilver_1000_175_c": [
      230,
      260
    ],
    "3djake_pctg_silver_1000_175_c": null
  },
  "bed_temp": {
    "3djake_pctg_pctgsilver_1000_175_c": null,
    "3djake_pctg_silver_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_pctg_pctgsilver_1000_175_c": [
      70,
      90
    ],
    "3djake_pctg_silver_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_pctg_pctgsilver_1000_175_c": "CZ",
    "3djake_pctg_silver_1000_175_c": "AT"
  }
}
```

### DJ021: dup-aff94b7ad1f1f47cc1aaac5384230dde834ce1a490249c5959cf92a5f9d96252

Status: APPROVED; survivor `3djake_pctg_transparent_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_pctg_pctgtransparent_1000_175_c`|`PCTG {color_name}`|`Transparent`|{"source_file": "3djake.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|
|`3djake_pctg_transparent_1000_175_c`|`{color_name}`|`Transparent`|{"source_file": "3djake.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "3djake_pctg_pctgtransparent_1000_175_c": 1.23,
    "3djake_pctg_transparent_1000_175_c": 1.24
  },
  "spool_weight": {
    "3djake_pctg_pctgtransparent_1000_175_c": null,
    "3djake_pctg_transparent_1000_175_c": 231
  },
  "color_hex": {
    "3djake_pctg_pctgtransparent_1000_175_c": "DEE2DA",
    "3djake_pctg_transparent_1000_175_c": "ffffff"
  },
  "extruder_temp": {
    "3djake_pctg_pctgtransparent_1000_175_c": null,
    "3djake_pctg_transparent_1000_175_c": 260
  },
  "extruder_temp_range": {
    "3djake_pctg_pctgtransparent_1000_175_c": [
      230,
      260
    ],
    "3djake_pctg_transparent_1000_175_c": null
  },
  "bed_temp": {
    "3djake_pctg_pctgtransparent_1000_175_c": null,
    "3djake_pctg_transparent_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_pctg_pctgtransparent_1000_175_c": [
      70,
      90
    ],
    "3djake_pctg_transparent_1000_175_c": null
  },
  "translucent": {
    "3djake_pctg_pctgtransparent_1000_175_c": false,
    "3djake_pctg_transparent_1000_175_c": true
  },
  "country_of_origin": {
    "3djake_pctg_pctgtransparent_1000_175_c": "CZ",
    "3djake_pctg_transparent_1000_175_c": "AT"
  }
}
```

### DJ022: dup-c1fc147a32c79c141362a4b3446c8314c6e36a8bb31785da22563b607ef595a1

Status: APPROVED; survivor `3djake_pctg_transparentblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_pctg_pctgtransparentblue_1000_175_c`|`PCTG {color_name}`|`Transparent Blue`|{"source_file": "3djake.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|
|`3djake_pctg_transparentblue_1000_175_c`|`{color_name}`|`Transparent Blue`|{"source_file": "3djake.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "3djake_pctg_pctgtransparentblue_1000_175_c": 1.23,
    "3djake_pctg_transparentblue_1000_175_c": 1.24
  },
  "spool_weight": {
    "3djake_pctg_pctgtransparentblue_1000_175_c": null,
    "3djake_pctg_transparentblue_1000_175_c": 231
  },
  "color_hex": {
    "3djake_pctg_pctgtransparentblue_1000_175_c": "0078BF",
    "3djake_pctg_transparentblue_1000_175_c": "0039bf"
  },
  "extruder_temp": {
    "3djake_pctg_pctgtransparentblue_1000_175_c": null,
    "3djake_pctg_transparentblue_1000_175_c": 260
  },
  "extruder_temp_range": {
    "3djake_pctg_pctgtransparentblue_1000_175_c": [
      230,
      260
    ],
    "3djake_pctg_transparentblue_1000_175_c": null
  },
  "bed_temp": {
    "3djake_pctg_pctgtransparentblue_1000_175_c": null,
    "3djake_pctg_transparentblue_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_pctg_pctgtransparentblue_1000_175_c": [
      70,
      90
    ],
    "3djake_pctg_transparentblue_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_pctg_pctgtransparentblue_1000_175_c": "CZ",
    "3djake_pctg_transparentblue_1000_175_c": "AT"
  }
}
```

### DJ023: dup-e7c5b9d965ea632178095deda9489d2fb3592c4d43aa4a6ecb0055d5f2adea1d

Status: APPROVED; survivor `3djake_pctg_transparentgreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_pctg_pctgtransparentgreen_1000_175_c`|`PCTG {color_name}`|`Transparent Green`|{"source_file": "3djake.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|
|`3djake_pctg_transparentgreen_1000_175_c`|`{color_name}`|`Transparent Green`|{"source_file": "3djake.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "3djake_pctg_pctgtransparentgreen_1000_175_c": 1.23,
    "3djake_pctg_transparentgreen_1000_175_c": 1.24
  },
  "spool_weight": {
    "3djake_pctg_pctgtransparentgreen_1000_175_c": null,
    "3djake_pctg_transparentgreen_1000_175_c": 231
  },
  "color_hex": {
    "3djake_pctg_pctgtransparentgreen_1000_175_c": "62E480",
    "3djake_pctg_transparentgreen_1000_175_c": "00b01d"
  },
  "extruder_temp": {
    "3djake_pctg_pctgtransparentgreen_1000_175_c": null,
    "3djake_pctg_transparentgreen_1000_175_c": 260
  },
  "extruder_temp_range": {
    "3djake_pctg_pctgtransparentgreen_1000_175_c": [
      230,
      260
    ],
    "3djake_pctg_transparentgreen_1000_175_c": null
  },
  "bed_temp": {
    "3djake_pctg_pctgtransparentgreen_1000_175_c": null,
    "3djake_pctg_transparentgreen_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_pctg_pctgtransparentgreen_1000_175_c": [
      70,
      90
    ],
    "3djake_pctg_transparentgreen_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_pctg_pctgtransparentgreen_1000_175_c": "CZ",
    "3djake_pctg_transparentgreen_1000_175_c": "AT"
  }
}
```

### DJ024: dup-2a778ba045d6f6fe27ca0261f8735097da692e40b6e1f617f1065f7cbc85b9e8

Status: APPROVED; survivor `3djake_pctg_transparentred_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_pctg_pctgtransparentred_1000_175_c`|`PCTG {color_name}`|`Transparent Red`|{"source_file": "3djake.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|
|`3djake_pctg_transparentred_1000_175_c`|`{color_name}`|`Transparent Red`|{"source_file": "3djake.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "3djake_pctg_pctgtransparentred_1000_175_c": 1.23,
    "3djake_pctg_transparentred_1000_175_c": 1.24
  },
  "spool_weight": {
    "3djake_pctg_pctgtransparentred_1000_175_c": null,
    "3djake_pctg_transparentred_1000_175_c": 231
  },
  "color_hex": {
    "3djake_pctg_pctgtransparentred_1000_175_c": "EC0000",
    "3djake_pctg_transparentred_1000_175_c": "c50000"
  },
  "extruder_temp": {
    "3djake_pctg_pctgtransparentred_1000_175_c": null,
    "3djake_pctg_transparentred_1000_175_c": 260
  },
  "extruder_temp_range": {
    "3djake_pctg_pctgtransparentred_1000_175_c": [
      230,
      260
    ],
    "3djake_pctg_transparentred_1000_175_c": null
  },
  "bed_temp": {
    "3djake_pctg_pctgtransparentred_1000_175_c": null,
    "3djake_pctg_transparentred_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_pctg_pctgtransparentred_1000_175_c": [
      70,
      90
    ],
    "3djake_pctg_transparentred_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_pctg_pctgtransparentred_1000_175_c": "CZ",
    "3djake_pctg_transparentred_1000_175_c": "AT"
  }
}
```

### DJ025: dup-aa0cbad140123989d321364d3df9cf7312fdcf719d85f10ad9e3fb71a84d47c1

Status: APPROVED; survivor `3djake_pctg_transparentyellow_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_pctg_pctgtransparentyellow_1000_175_c`|`PCTG {color_name}`|`Transparent Yellow`|{"source_file": "3djake.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|
|`3djake_pctg_transparentyellow_1000_175_c`|`{color_name}`|`Transparent Yellow`|{"source_file": "3djake.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "3djake_pctg_pctgtransparentyellow_1000_175_c": 1.23,
    "3djake_pctg_transparentyellow_1000_175_c": 1.24
  },
  "spool_weight": {
    "3djake_pctg_pctgtransparentyellow_1000_175_c": null,
    "3djake_pctg_transparentyellow_1000_175_c": 231
  },
  "color_hex": {
    "3djake_pctg_pctgtransparentyellow_1000_175_c": "FFFC6A",
    "3djake_pctg_transparentyellow_1000_175_c": "deae00"
  },
  "extruder_temp": {
    "3djake_pctg_pctgtransparentyellow_1000_175_c": null,
    "3djake_pctg_transparentyellow_1000_175_c": 260
  },
  "extruder_temp_range": {
    "3djake_pctg_pctgtransparentyellow_1000_175_c": [
      230,
      260
    ],
    "3djake_pctg_transparentyellow_1000_175_c": null
  },
  "bed_temp": {
    "3djake_pctg_pctgtransparentyellow_1000_175_c": null,
    "3djake_pctg_transparentyellow_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_pctg_pctgtransparentyellow_1000_175_c": [
      70,
      90
    ],
    "3djake_pctg_transparentyellow_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_pctg_pctgtransparentyellow_1000_175_c": "CZ",
    "3djake_pctg_transparentyellow_1000_175_c": "AT"
  }
}
```

### DJ026: dup-0e93a27b1f6694cb44a50aeda66b404c2e6bfb514def93c11ba946fe5b7a8cd7

Status: APPROVED; survivor `3djake_pctg_white_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_pctg_pctgwhite_1000_175_c`|`PCTG {color_name}`|`White`|{"source_file": "3djake.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|
|`3djake_pctg_white_1000_175_c`|`{color_name}`|`White`|{"source_file": "3djake.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "3djake_pctg_pctgwhite_1000_175_c": 1.23,
    "3djake_pctg_white_1000_175_c": 1.24
  },
  "spool_weight": {
    "3djake_pctg_pctgwhite_1000_175_c": null,
    "3djake_pctg_white_1000_175_c": 231
  },
  "color_hex": {
    "3djake_pctg_pctgwhite_1000_175_c": "F5F5F5",
    "3djake_pctg_white_1000_175_c": "FFFFFF"
  },
  "extruder_temp": {
    "3djake_pctg_pctgwhite_1000_175_c": null,
    "3djake_pctg_white_1000_175_c": 260
  },
  "extruder_temp_range": {
    "3djake_pctg_pctgwhite_1000_175_c": [
      230,
      260
    ],
    "3djake_pctg_white_1000_175_c": null
  },
  "bed_temp": {
    "3djake_pctg_pctgwhite_1000_175_c": null,
    "3djake_pctg_white_1000_175_c": 100
  },
  "bed_temp_range": {
    "3djake_pctg_pctgwhite_1000_175_c": [
      70,
      90
    ],
    "3djake_pctg_white_1000_175_c": null
  },
  "country_of_origin": {
    "3djake_pctg_pctgwhite_1000_175_c": "CZ",
    "3djake_pctg_white_1000_175_c": "AT"
  }
}
```

### DJ027: dup-6ddc787260cf6f67c1af6813ff91f0827faeffa3da3d2b424e092702e07b4b16

Status: APPROVED; survivor `3djake_petg_darkgray_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3djake_petg_darkgray_1000_175_c`|`{color_name}`|`Dark Gray`|{"source_file": "3djake.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / True|
|`3djake_petg_petgdarkgrey_1000_175_c`|`PETG {color_name}`|`Dark Grey`|{"source_file": "3djake.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 1, "compiled_records": 1} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "3djake_petg_darkgray_1000_175_c": 1.24,
    "3djake_petg_petgdarkgrey_1000_175_c": 1.27
  },
  "spool_weight": {
    "3djake_petg_darkgray_1000_175_c": 231,
    "3djake_petg_petgdarkgrey_1000_175_c": null
  },
  "color_hex": {
    "3djake_petg_darkgray_1000_175_c": "484848",
    "3djake_petg_petgdarkgrey_1000_175_c": "88899D"
  },
  "extruder_temp": {
    "3djake_petg_darkgray_1000_175_c": 240,
    "3djake_petg_petgdarkgrey_1000_175_c": null
  },
  "extruder_temp_range": {
    "3djake_petg_darkgray_1000_175_c": null,
    "3djake_petg_petgdarkgrey_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "3djake_petg_darkgray_1000_175_c": 90,
    "3djake_petg_petgdarkgrey_1000_175_c": null
  },
  "bed_temp_range": {
    "3djake_petg_darkgray_1000_175_c": null,
    "3djake_petg_petgdarkgrey_1000_175_c": [
      70,
      90
    ]
  },
  "country_of_origin": {
    "3djake_petg_darkgray_1000_175_c": "AT",
    "3djake_petg_petgdarkgrey_1000_175_c": "CZ"
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "3djake_asa_white_1000_175_c",
      "values": {
        "density": 1.1
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_ASA_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_pctg_darkgreen_1000_175_c",
      "values": {
        "density": 1.23
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_PCTG_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_pctg_white_1000_175_c",
      "values": {
        "density": 1.23
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_PCTG_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_pctg_black_1000_175_c",
      "values": {
        "density": 1.23
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_PCTG_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_pctg_silver_1000_175_c",
      "values": {
        "density": 1.23
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_PCTG_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_asa_lightgreen_1000_175_c",
      "values": {
        "density": 1.1
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_ASA_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_pctg_transparentred_1000_175_c",
      "values": {
        "density": 1.23
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_PCTG_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_asa_darkblue_1000_175_c",
      "values": {
        "density": 1.1
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_ASA_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_pctg_darkblue_1000_175_c",
      "values": {
        "density": 1.23
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_PCTG_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_asa_darkgreen_1000_175_c",
      "values": {
        "density": 1.1
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_ASA_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_asa_lightgrey_1000_175_c",
      "values": {
        "density": 1.1
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_ASA_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_asa_purple_1000_175_c",
      "values": {
        "density": 1.1
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_ASA_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_petg_darkgray_1000_175_c",
      "values": {
        "density": 1.27,
        "bed_temp": null,
        "bed_temp_range": [
          60,
          80
        ]
      },
      "source": "https://3d.nice-cdn.com/upload/file/TDS_PETG.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_asa_lightblue_1000_175_c",
      "values": {
        "density": 1.1
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_ASA_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_asa_red_1000_175_c",
      "values": {
        "density": 1.1
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_ASA_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_asa_darkgrey_1000_175_c",
      "values": {
        "density": 1.1
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_ASA_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_pctg_lightgreen_1000_175_c",
      "values": {
        "density": 1.23
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_PCTG_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_pctg_transparentyellow_1000_175_c",
      "values": {
        "density": 1.23
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_PCTG_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_pctg_transparent_1000_175_c",
      "values": {
        "density": 1.23
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_PCTG_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_asa_black_1000_175_c",
      "values": {
        "density": 1.1
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_ASA_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_pctg_red_1000_175_c",
      "values": {
        "density": 1.23
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_PCTG_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_pctg_transparentblue_1000_175_c",
      "values": {
        "density": 1.23
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_PCTG_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_asa_silver_1000_175_c",
      "values": {
        "density": 1.1
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_ASA_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_pctg_transparentgreen_1000_175_c",
      "values": {
        "density": 1.23
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_PCTG_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_asa_yellow_1000_175_c",
      "values": {
        "density": 1.1
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_ASA_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_pctg_lightblue_1000_175_c",
      "values": {
        "density": 1.23
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_PCTG_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "3djake_asa_orange_1000_175_c",
      "values": {
        "density": 1.1
      },
      "source": "https://3d.nice-cdn.com/upload/file/Technical_Data_Sheet_ASA_V2.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    }
  ],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `3djake_petg_white_1000_175_c` — White
- `3djake_petg_black_1000_175_c` — Black
- `3djake_petg_silver_1000_175_c` — Silver
- `3djake_petg_bronze_1000_175_c` — Bronze
- `3djake_petg_darkblue_1000_175_c` — Dark Blue
- `3djake_petg_skyblue_1000_175_c` — Sky Blue
- `3djake_petg_lightgreen_1000_175_c` — Light Green
- `3djake_petg_neonorange_1000_175_c` — Neon Orange
- `3djake_petg_red_1000_175_c` — Red
- `3djake_petg_neonyellow_1000_175_c` — Neon Yellow
- `3djake_petg_pastellpink_1000_175_c` — Pastell pink
- `3djake_petg_pastelblue_1000_175_c` — Pastel blue
- `3djake_petg_transparent_1000_175_c` — Transparent
- `3djake_petg_redtransparent_1000_175_c` — Red Transparent
- `3djake_petg_greentransparent_1000_175_c` — Green Transparent
- `3djake_petg_bluetransparent_1000_175_c` — Blue Transparent
- `3djake_petg_yellowtransparent_1000_175_c` — Yellow Transparent
- `3djake_pla_transparent_1000_175_c` — Transparent
- `3djake_pla_cmykwhite_1000_175_c` — CMYK White
- `3djake_pla_white_1000_175_c` — White
- `3djake_pla_lightgray_1000_175_c` — Light Gray
- `3djake_pla_neonyellow_1000_175_c` — Neon Yellow
- `3djake_pla_cmykyellow_1000_175_c` — CMYK Yellow
- `3djake_pla_yellow_1000_175_c` — Yellow
- `3djake_pla_orange_1000_175_c` — Orange
- `3djake_pla_neonorange_1000_175_c` — Neon Orange
- `3djake_pla_pastelpink_1000_175_c` — Pastel Pink
- `3djake_pla_red_1000_175_c` — Red
- `3djake_pla_pink_1000_175_c` — Pink
- `3djake_pla_cmykmagenta_1000_175_c` — CMYK Magenta
- `3djake_pla_violet_1000_175_c` — Violet
- `3djake_pla_pastelblue_1000_175_c` — Pastel Blue
- `3djake_pla_lightblue_1000_175_c` — Light Blue
- `3djake_pla_darkblue_1000_175_c` — Dark Blue
- `3djake_pla_pastelgreen_1000_175_c` — Pastel Green
- `3djake_pla_lightgreen_1000_175_c` — Light Green
- `3djake_pla_neongreen_1000_175_c` — Neon Green
- `3djake_pla_cmykcyan_1000_175_c` — CMYK Cyan
- `3djake_pla_darkgreen_1000_175_c` — Dark Green
- `3djake_pla_gold_1000_175_c` — Gold
- `3djake_pla_bronze_1000_175_c` — Bronze
- `3djake_pla_brown_1000_175_c` — Brown
- `3djake_pla_silver_1000_175_c` — Silver
- `3djake_pla_darkgray_1000_175_c` — Dark Gray
- `3djake_pla_black_1000_175_c` — Black
- `3djake_pla_silkraspberry_1000_175_c` — Silk Raspberry
- `3djake_pla_silkyellow_1000_175_c` — Silk Yellow
- `3djake_pla_silkgold_1000_175_c` — Silk Gold
- `3djake_pla_silkcopper_1000_175_c` — Silk Copper
- `3djake_pla_silkviolet_1000_175_c` — Silk Violet
- `3djake_pla_silkblue_1000_175_c` — Silk Blue
- `3djake_pla_silkgreen_1000_175_c` — Silk Green
- `3djake_pla_silksilver_1000_175_c` — Silk Silver
- `3djake_pla_silkblack_1000_175_c` — Silk Black
- `3djake_abs_absblack_1000_175_c` — ABS Black
- `3djake_abs_absbronze_1000_175_c` — ABS Bronze
- `3djake_abs_absbrown_1000_175_c` — ABS Brown
- `3djake_abs_absdarkblue_1000_175_c` — ABS Dark Blue
- `3djake_abs_absdarkgreen_1000_175_c` — ABS Dark Green
- `3djake_abs_absdarkgrey_1000_175_c` — ABS Dark Grey
- `3djake_abs_abslightblue_1000_175_c` — ABS Light Blue
- `3djake_abs_abslightgreen_1000_175_c` — ABS Light Green
- `3djake_abs_abslightgrey_1000_175_c` — ABS Light Grey
- `3djake_abs_absneongreen_1000_175_c` — ABS Neon Green
- `3djake_abs_absneonorange_1000_175_c` — ABS Neon Orange
- `3djake_abs_absneonyellow_1000_175_c` — ABS Neon Yellow
- `3djake_abs_absorange_1000_175_c` — ABS Orange
- `3djake_abs_abspastelblue_1000_175_c` — ABS Pastel Blue
- `3djake_abs_abspastelgreen_1000_175_c` — ABS Pastel Green
- `3djake_abs_abspastelpink_1000_175_c` — ABS Pastel Pink
- `3djake_abs_abspink_1000_175_c` — ABS Pink
- `3djake_abs_abspurple_1000_175_c` — ABS Purple
- `3djake_abs_abssilver_1000_175_c` — ABS Silver
- `3djake_abs_abswhite_1000_175_c` — ABS White
- `3djake_abs_absyellow_1000_175_c` — ABS Yellow
- `3djake_pctg_pctgpurple_1000_175_c` — PCTG Purple
- `3djake_pctg_pctgyellow_1000_175_c` — PCTG Yellow
- `3djake_petg_easymattepetgblack_1000_175_c` — Easy Matte PETG Black
- `3djake_petg_easymattepetgbronze_1000_175_c` — Easy Matte PETG Bronze
- `3djake_petg_easymattepetgbrown_1000_175_c` — Easy Matte PETG Brown
- `3djake_petg_easymattepetgdarkblue_1000_175_c` — Easy Matte PETG Dark Blue
- `3djake_petg_easymattepetgdarkgreen_1000_175_c` — Easy Matte PETG Dark Green
- `3djake_petg_easymattepetgdarkgrey_1000_175_c` — Easy Matte PETG Dark Grey
- `3djake_petg_easymattepetglightgreen_1000_175_c` — Easy Matte PETG Light Green
- `3djake_petg_easymattepetglightgrey_1000_175_c` — Easy Matte PETG Light Grey
- `3djake_petg_easymattepetgneongreen_1000_175_c` — Easy Matte PETG Neon Green
- `3djake_petg_easymattepetgneonorange_1000_175_c` — Easy Matte PETG Neon Orange
- `3djake_petg_easymattepetgneonyellow_1000_175_c` — Easy Matte PETG Neon Yellow
- `3djake_petg_easymattepetgorange_1000_175_c` — Easy Matte PETG Orange
- `3djake_petg_easymattepetgpastelblue_1000_175_c` — Easy Matte PETG Pastel Blue
- `3djake_petg_easymattepetgpastelgreen_1000_175_c` — Easy Matte PETG Pastel Green
- `3djake_petg_easymattepetgpastelpink_1000_175_c` — Easy Matte PETG Pastel Pink
- `3djake_petg_easymattepetgpink_1000_175_c` — Easy Matte PETG Pink
- `3djake_petg_easymattepetgpurple_1000_175_c` — Easy Matte PETG Purple
- `3djake_petg_easymattepetgred_1000_175_c` — Easy Matte PETG Red
- `3djake_petg_easymattepetgsilver_1000_175_c` — Easy Matte PETG Silver
- `3djake_petg_easymattepetgskyblue_1000_175_c` — Easy Matte PETG Sky Blue
- `3djake_petg_easymattepetgwhite_1000_175_c` — Easy Matte PETG White
- `3djake_petg_easymattepetgyellow_1000_175_c` — Easy Matte PETG Yellow
- `3djake_petg_easypetgblack_1000_175_c` — easy PETG Black
- `3djake_petg_easypetgbronze_1000_175_c` — easy PETG Bronze
- `3djake_petg_easypetgbrown_1000_175_c` — easy PETG Brown
- `3djake_petg_easypetgdarkblue_1000_175_c` — easy PETG Dark Blue
- `3djake_petg_easypetgdarkgreen_1000_175_c` — easy PETG Dark Green
- `3djake_petg_easypetgdarkgrey_1000_175_c` — easy PETG Dark Grey
- `3djake_petg_easypetglightgreen_1000_175_c` — easy PETG Light Green
- `3djake_petg_easypetglightgrey_1000_175_c` — easy PETG Light Grey
- `3djake_petg_easypetgneongreen_1000_175_c` — easy PETG Neon Green
- `3djake_petg_easypetgneonorange_1000_175_c` — easy PETG Neon Orange
- `3djake_petg_easypetgneonyellow_1000_175_c` — easy PETG Neon Yellow
- `3djake_petg_easypetgorange_1000_175_c` — easy PETG Orange
- `3djake_petg_easypetgpastelblue_1000_175_c` — easy PETG Pastel Blue
- `3djake_petg_easypetgpastelgreen_1000_175_c` — easy PETG Pastel Green
- `3djake_petg_easypetgpastelpink_1000_175_c` — easy PETG Pastel Pink
- `3djake_petg_easypetgpink_1000_175_c` — easy PETG Pink
- `3djake_petg_easypetgpurple_1000_175_c` — easy PETG Purple
- `3djake_petg_easypetgred_1000_175_c` — easy PETG Red
- `3djake_petg_easypetgsilver_1000_175_c` — easy PETG Silver
- `3djake_petg_easypetgskyblue_1000_175_c` — easy PETG Sky Blue
- `3djake_petg_easypetgtransparent_1000_175_c` — easy PETG Transparent
- `3djake_petg_easypetgtransparentblue_1000_175_c` — easy PETG Transparent Blue
- `3djake_petg_easypetgtransparentgreen_1000_175_c` — easy PETG Transparent Green
- `3djake_petg_easypetgtransparentred_1000_175_c` — easy PETG Transparent Red
- `3djake_petg_easypetgtransparentyellow_1000_175_c` — easy PETG Transparent Yellow
- `3djake_petg_easypetgwhite_1000_175_c` — easy PETG White
- `3djake_petg_easypetgyellow_1000_175_c` — easy PETG Yellow
- `3djake_petg_glowpetgeasyglow_1000_175_c` — Glow PETG easy Glow
- `3djake_pla_ecoglowplaglow_1000_175_c` — eco Glow PLA Glow
- `3djake_pla_ecomatteplamattmossgrey_1000_175_c` — eco Matte PLA Matt Moss Grey
- `3djake_pla_ecoplablack_1000_175_c` — eco PLA Black
- `3djake_pla_ecoplabronze_1000_175_c` — eco PLA Bronze
- `3djake_pla_ecoplabrown_1000_175_c` — eco PLA Brown
- `3djake_pla_ecoplacmykcyan_1000_175_c` — eco PLA CMYK Cyan
- `3djake_pla_ecoplacmykmagenta_1000_175_c` — eco PLA CMYK Magenta
- `3djake_pla_ecoplacmykwhite_1000_175_c` — eco PLA CMYK White
- `3djake_pla_ecoplacmykyellow_1000_175_c` — eco PLA CMYK Yellow
- `3djake_pla_ecopladarkblue_1000_175_c` — eco PLA Dark Blue
- `3djake_pla_ecopladarkgreen_1000_175_c` — eco PLA Dark Green
- `3djake_pla_ecopladarkgrey_1000_175_c` — eco PLA Dark Grey
- `3djake_pla_ecoplalightgreen_1000_175_c` — eco PLA Light Green
- `3djake_pla_ecoplalightgrey_1000_175_c` — eco PLA Light Grey
- `3djake_pla_ecoplamarble_1000_175_c` — eco PLA Marble
- `3djake_pla_ecoplaneongreen_1000_175_c` — eco PLA Neon Green
- `3djake_pla_ecoplaneonorange_1000_175_c` — eco PLA Neon Orange
- `3djake_pla_ecoplaneonyellow_1000_175_c` — eco PLA Neon Yellow
- `3djake_pla_ecoplaorange_1000_175_c` — eco PLA Orange
- `3djake_pla_ecoplapastelblue_1000_175_c` — eco PLA Pastel Blue
- `3djake_pla_ecoplapastelgreen_1000_175_c` — eco PLA Pastel Green
- `3djake_pla_ecoplapastelpink_1000_175_c` — eco PLA Pastel Pink
- `3djake_pla_ecoplapink_1000_175_c` — eco PLA Pink
- `3djake_pla_ecoplapurple_1000_175_c` — eco PLA Purple
- `3djake_pla_ecoplared_1000_175_c` — eco PLA Red
- `3djake_pla_ecoplasilver_1000_175_c` — eco PLA Silver
- `3djake_pla_ecoplaskyblue_1000_175_c` — eco PLA Sky Blue
- `3djake_pla_ecoplasparklingblue_1000_175_c` — eco PLA Sparkling Blue
- `3djake_pla_ecoplasparklinggold_1000_175_c` — eco PLA Sparkling Gold
- `3djake_pla_ecoplasparklinggreen_1000_175_c` — eco PLA Sparkling Green
- `3djake_pla_ecoplasparklinggrey_1000_175_c` — eco PLA Sparkling Grey
- `3djake_pla_ecoplasparklingpurple_1000_175_c` — eco PLA Sparkling Purple
- `3djake_pla_ecoplasparklingred_1000_175_c` — eco PLA Sparkling Red
- `3djake_pla_ecoplasparklingsilver_1000_175_c` — eco PLA Sparkling Silver
- `3djake_pla_ecoplatransparent_1000_175_c` — eco PLA Transparent
- `3djake_pla_ecoplawhite_1000_175_c` — eco PLA White
- `3djake_pla_ecoplawooddarkbrown_1000_175_c` — eco PLA Wood Dark Brown
- `3djake_pla_ecoplawoodlightbrown_1000_175_c` — eco PLA Wood Light Brown
- `3djake_pla_ecoplayellow_1000_175_c` — eco PLA Yellow
- `3djake_pla_ecosilkplablack_1000_175_c` — eco Silk PLA Black
- `3djake_pla_ecosilkplablue_1000_175_c` — eco Silk PLA Blue
- `3djake_pla_ecosilkplacopper_1000_175_c` — eco Silk PLA Copper
- `3djake_pla_ecosilkplagold_1000_175_c` — eco Silk PLA Gold
- `3djake_pla_ecosilkplagreen_1000_175_c` — eco Silk PLA Green
- `3djake_pla_ecosilkplapurple_1000_175_c` — eco Silk PLA Purple
- `3djake_pla_ecosilkplarainbowcandyshop_1000_175_c` — eco Silk PLA Rainbow Candyshop
- `3djake_pla_ecosilkplarainbowlollipop_1000_175_c` — eco Silk PLA Rainbow Lollipop
- `3djake_pla_ecosilkplaraspberry_1000_175_c` — eco Silk PLA Raspberry
- `3djake_pla_ecosilkplasilver_1000_175_c` — eco Silk PLA Silver
- `3djake_pla_ecosilkplayellow_1000_175_c` — eco Silk PLA Yellow
- `3djake_pla_magicplaarabiannights_1000_175_c` — magic PLA Arabian Nights
- `3djake_pla_magicplacottoncandy_1000_175_c` — magic PLA Cotton Candy
- `3djake_pla_magicplafrozenraspberry_1000_175_c` — magic PLA Frozen Raspberry
- `3djake_pla_magicplagoldenalloy_1000_175_c` — magic PLA Golden Alloy
- `3djake_pla_magicplalemongrass_1000_175_c` — magic PLA Lemon Grass
- `3djake_pla_magicplamintblush_1000_175_c` — magic PLA Mint Blush
- `3djake_pla_magicplapurpledelirium_1000_175_c` — magic PLA Purple Delirium
- `3djake_pla_magicplatropicalsea_1000_175_c` — magic PLA Tropical Sea
- `3djake_pla_matteplablack_1000_175_c` — Matte PLA Black
- `3djake_pla_matteplabronze_1000_175_c` — Matte PLA Bronze
- `3djake_pla_matteplabrown_1000_175_c` — Matte PLA Brown
- `3djake_pla_mattepladarkblue_1000_175_c` — Matte PLA Dark Blue
- `3djake_pla_mattepladarkgreen_1000_175_c` — Matte PLA Dark Green
- `3djake_pla_mattepladarkgrey_1000_175_c` — Matte PLA Dark Grey
- `3djake_pla_matteplalightblue_1000_175_c` — Matte PLA Light Blue
- `3djake_pla_matteplalightgreen_1000_175_c` — Matte PLA Light Green
- `3djake_pla_matteplalightgrey_1000_175_c` — Matte PLA Light Grey
- `3djake_pla_matteplaneongreen_1000_175_c` — Matte PLA Neon Green
- `3djake_pla_matteplaneonorange_1000_175_c` — Matte PLA Neon Orange
- `3djake_pla_matteplaneonyellow_1000_175_c` — Matte PLA Neon Yellow
- `3djake_pla_matteplaorange_1000_175_c` — Matte PLA Orange
- `3djake_pla_matteplapastelblue_1000_175_c` — Matte PLA Pastel Blue
- `3djake_pla_matteplapastelgreen_1000_175_c` — Matte PLA Pastel Green
- `3djake_pla_matteplapastelpink_1000_175_c` — Matte PLA Pastel Pink
- `3djake_pla_matteplapink_1000_175_c` — Matte PLA Pink
- `3djake_pla_matteplapurple_1000_175_c` — Matte PLA Purple
- `3djake_pla_matteplared_1000_175_c` — Matte PLA Red
- `3djake_pla_matteplasilver_1000_175_c` — Matte PLA Silver
- `3djake_pla_matteplawhite_1000_175_c` — Matte PLA White
- `3djake_pla_matteplayellow_1000_175_c` — Matte PLA Yellow
- `3djake_pla_mysteryplaamethystdream_1000_175_c` — mystery PLA Amethyst Dream
- `3djake_pla_mysteryplaberrypopsicle_1000_175_c` — mystery PLA Berry Popsicle
- `3djake_pla_mysteryplaepicthunderstorm_1000_175_c` — mystery PLA Epic Thunderstorm
- `3djake_pla_mysteryplamagicinajar_1000_175_c` — mystery PLA Magic in a Jar
- `3djake_pla_mysteryplanorthernlights_1000_175_c` — mystery PLA Northern Lights
- `3djake_pla_mysteryplaorionnebula_1000_175_c` — mystery PLA Orion Nebula
- `3djake_tpu_tpua95black_1000_175_c` — TPU A95 Black
- `3djake_tpu_tpua95darkblue_1000_175_c` — TPU A95 Dark Blue
- `3djake_tpu_tpua95darkgreen_1000_175_c` — TPU A95 Dark Green
- `3djake_tpu_tpua95darkgrey_1000_175_c` — TPU A95 Dark Grey
- `3djake_tpu_tpua95lightblue_1000_175_c` — TPU A95 Light Blue
- `3djake_tpu_tpua95lightgreen_1000_175_c` — TPU A95 Light Green
- `3djake_tpu_tpua95lightgrey_1000_175_c` — TPU A95 Light Grey
- `3djake_tpu_tpua95orange_1000_175_c` — TPU A95 Orange
- `3djake_tpu_tpua95purple_1000_175_c` — TPU A95 Purple
- `3djake_tpu_tpua95red_1000_175_c` — TPU A95 Red
- `3djake_tpu_tpua95silver_1000_175_c` — TPU A95 Silver
- `3djake_tpu_tpua95transparent_1000_175_c` — TPU A95 Transparent
- `3djake_tpu_tpua95white_1000_175_c` — TPU A95 White
- `3djake_tpu_tpua95yellow_1000_175_c` — TPU A95 Yellow
