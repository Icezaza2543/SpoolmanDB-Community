# teqstone duplicate migration review

Base `2e8cbe222f844100081edeef93fb607e76d35380`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `b50400b531876e879e983a39d8e324922bef8bbc1f97bb8ebb566a4437ec4694`.

## Authorization and result

{"groups": 6, "approved_groups": 6, "retired": 6, "deferred": 0, "hard_stops": 0, "before_count": 51740, "after_count": 51734, "brand_before": 98, "brand_after": 92, "registry_before": 1694, "registry_after": 1700, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Six Rule1 strict Glow/Silk/Marble PLA duplicates. No exact current first-party numeric evidence verified; retain survivor density and temperatures, record all conflicts unresolved. Do not borrow Geeetech formula or packaging/tare. No identifiers.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence


## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`teqstone_pla_glowplagreen_1000_175_p`|`teqstone_pla_glowgreen_1000_175_p`|`teqstone.json::TEQStone::Glow PLA {color_name}::Glow PLA Green::PLA::1000::1.75::plastic::False`|
|`teqstone_pla_glowplaorange_1000_175_p`|`teqstone_pla_gloworange_1000_175_p`|`teqstone.json::TEQStone::Glow PLA {color_name}::Glow PLA Orange::PLA::1000::1.75::plastic::False`|
|`teqstone_pla_marbleplabrown_1000_175_p`|`teqstone_pla_marblebrown_1000_175_p`|`teqstone.json::TEQStone::Marble PLA {color_name}::Marble PLA Brown::PLA::1000::1.75::plastic::False`|
|`teqstone_pla_marbleplagrey_1000_175_p`|`teqstone_pla_marblegrey_1000_175_p`|`teqstone.json::TEQStone::Marble PLA {color_name}::Marble PLA Grey::PLA::1000::1.75::plastic::False`|
|`teqstone_pla_silkplacopper_1000_175_p`|`teqstone_pla_silkcopper_1000_175_p`|`teqstone.json::TEQStone::Silk PLA {color_name}::Silk PLA Copper::PLA::1000::1.75::plastic::False`|
|`teqstone_pla_silkplagold_1000_175_p`|`teqstone_pla_silkgold_1000_175_p`|`teqstone.json::TEQStone::Silk PLA {color_name}::Silk PLA Gold::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### TQ001: dup-1c540072efafc6bc86bbd139ea45dbbe5971639da337e83676e01be05b28ee50

Status: APPROVED; survivor `teqstone_pla_glowgreen_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`teqstone_pla_glowgreen_1000_175_p`|`Glow {color_name}`|`Green`|{"source_file": "teqstone.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|
|`teqstone_pla_glowplagreen_1000_175_p`|`Glow PLA {color_name}`|`Green`|{"source_file": "teqstone.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "teqstone_pla_glowgreen_1000_175_p": "ADFF2F",
    "teqstone_pla_glowplagreen_1000_175_p": "39FF14"
  },
  "extruder_temp_range": {
    "teqstone_pla_glowgreen_1000_175_p": [
      190,
      230
    ],
    "teqstone_pla_glowplagreen_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "teqstone_pla_glowgreen_1000_175_p": [
      50,
      70
    ],
    "teqstone_pla_glowplagreen_1000_175_p": [
      0,
      60
    ]
  }
}
```

### TQ002: dup-fa45dc40c5dcf34102e82b180b70db151602eb88dbfe135b0f2dc94918cce7f2

Status: APPROVED; survivor `teqstone_pla_gloworange_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`teqstone_pla_gloworange_1000_175_p`|`Glow {color_name}`|`Orange`|{"source_file": "teqstone.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|
|`teqstone_pla_glowplaorange_1000_175_p`|`Glow PLA {color_name}`|`Orange`|{"source_file": "teqstone.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "teqstone_pla_gloworange_1000_175_p": "FFAA00",
    "teqstone_pla_glowplaorange_1000_175_p": "FF4500"
  },
  "extruder_temp_range": {
    "teqstone_pla_gloworange_1000_175_p": [
      190,
      230
    ],
    "teqstone_pla_glowplaorange_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "teqstone_pla_gloworange_1000_175_p": [
      50,
      70
    ],
    "teqstone_pla_glowplaorange_1000_175_p": [
      0,
      60
    ]
  }
}
```

### TQ003: dup-b46c7662301f09fe4dd59add0269b9dfe4ca946fecd9e1fa6b05f5049126d0c6

Status: APPROVED; survivor `teqstone_pla_marblebrown_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`teqstone_pla_marblebrown_1000_175_p`|`Marble {color_name}`|`Brown`|{"source_file": "teqstone.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / True|
|`teqstone_pla_marbleplabrown_1000_175_p`|`Marble PLA {color_name}`|`Brown`|{"source_file": "teqstone.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "teqstone_pla_marblebrown_1000_175_p": "8B6914",
    "teqstone_pla_marbleplabrown_1000_175_p": "D2B48C"
  },
  "bed_temp_range": {
    "teqstone_pla_marblebrown_1000_175_p": [
      50,
      60
    ],
    "teqstone_pla_marbleplabrown_1000_175_p": [
      0,
      60
    ]
  },
  "pattern": {
    "teqstone_pla_marblebrown_1000_175_p": "marble",
    "teqstone_pla_marbleplabrown_1000_175_p": null
  }
}
```

### TQ004: dup-6f4d9cc8b807863435f3d3e4c40a2e1524b9d2009ed28645a11d3e64df33fda6

Status: APPROVED; survivor `teqstone_pla_marblegrey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`teqstone_pla_marblegrey_1000_175_p`|`Marble {color_name}`|`Grey`|{"source_file": "teqstone.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / True|
|`teqstone_pla_marbleplagrey_1000_175_p`|`Marble PLA {color_name}`|`Grey`|{"source_file": "teqstone.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "teqstone_pla_marblegrey_1000_175_p": "808080",
    "teqstone_pla_marbleplagrey_1000_175_p": "B0B0B0"
  },
  "bed_temp_range": {
    "teqstone_pla_marblegrey_1000_175_p": [
      50,
      60
    ],
    "teqstone_pla_marbleplagrey_1000_175_p": [
      0,
      60
    ]
  },
  "pattern": {
    "teqstone_pla_marblegrey_1000_175_p": "marble",
    "teqstone_pla_marbleplagrey_1000_175_p": null
  }
}
```

### TQ005: dup-62f7d55805ca193ed3c8d037a9e1a8b6c6ce5a79540a2ea54beef230ed17b5e1

Status: APPROVED; survivor `teqstone_pla_silkcopper_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`teqstone_pla_silkcopper_1000_175_p`|`Silk {color_name}`|`Copper`|{"source_file": "teqstone.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|
|`teqstone_pla_silkplacopper_1000_175_p`|`Silk PLA {color_name}`|`Copper`|{"source_file": "teqstone.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "bed_temp_range": {
    "teqstone_pla_silkcopper_1000_175_p": [
      50,
      60
    ],
    "teqstone_pla_silkplacopper_1000_175_p": [
      0,
      60
    ]
  },
  "finish": {
    "teqstone_pla_silkcopper_1000_175_p": "glossy",
    "teqstone_pla_silkplacopper_1000_175_p": null
  }
}
```

### TQ006: dup-58106e62c51862ef9523bc290e2278ad646d7ecf08f484eea240acb468f863fa

Status: APPROVED; survivor `teqstone_pla_silkgold_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`teqstone_pla_silkgold_1000_175_p`|`Silk {color_name}`|`Gold`|{"source_file": "teqstone.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|
|`teqstone_pla_silkplagold_1000_175_p`|`Silk PLA {color_name}`|`Gold`|{"source_file": "teqstone.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "teqstone_pla_silkgold_1000_175_p": "D4AF37",
    "teqstone_pla_silkplagold_1000_175_p": "D4A017"
  },
  "bed_temp_range": {
    "teqstone_pla_silkgold_1000_175_p": [
      50,
      60
    ],
    "teqstone_pla_silkplagold_1000_175_p": [
      0,
      60
    ]
  },
  "finish": {
    "teqstone_pla_silkgold_1000_175_p": "glossy",
    "teqstone_pla_silkplagold_1000_175_p": null
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `teqstone_pla_plabasicbeige(bonewhite)_1000_175_p` — PLA Basic Beige (Bone White)
- `teqstone_pla_plabasicbrown_1000_175_p` — PLA Basic Brown
- `teqstone_pla_plabasicclear_1000_175_p` — PLA Basic Clear
- `teqstone_pla_plabasiccyan(waterblue)_1000_175_p` — PLA Basic Cyan (Water Blue)
- `teqstone_pla_plabasicneongreen_1000_175_p` — PLA Basic Neon Green
- `teqstone_pla_plabasicpink_1000_175_p` — PLA Basic Pink
- `teqstone_pla_plabasicpurple_1000_175_p` — PLA Basic Purple
- `teqstone_pla_silkblue(royal)_1000_175_p` — Silk Blue (Royal)
- `teqstone_pla_silkdarkpurple_1000_175_p` — Silk Dark Purple
- `teqstone_pla_silkgreen_1000_175_p` — Silk Green
- `teqstone_pla_silkpink(magenta)_1000_175_p` — Silk Pink (Magenta)
- `teqstone_pla_silksilver_1000_175_p` — Silk Silver
- `teqstone_pla_silkmulticolor_1000_175_p` — Silk Multicolor
- `teqstone_pla_silkmulticolor(pastel)_1000_175_p` — Silk Multicolor (Pastel)
- `teqstone_pla_dualsilkblack&red_1000_175_p` — Dual Silk Black & Red
- `teqstone_pla_dualsilkblue&green_1000_175_p` — Dual Silk Blue & Green
- `teqstone_pla_dualsilkgold&copper_1000_175_p` — Dual Silk Gold & Copper
- `teqstone_pla_dualsilkgold&purple_1000_175_p` — Dual Silk Gold & Purple
- `teqstone_pla_dualsilkgreen&red_1000_175_p` — Dual Silk Green & Red
- `teqstone_pla_trisilkbluegreenorange_1000_175_p` — Tri Silk Blue Green Orange
- `teqstone_pla_trisilkbluepurpleblack_1000_175_p` — Tri Silk Blue Purple Black
- `teqstone_pla_trisilkgoldpurpleblack_1000_175_p` — Tri Silk Gold Purple Black
- `teqstone_pla_trisilkgoldpurplered_1000_175_p` — Tri Silk Gold Purple Red
- `teqstone_pla_trisilkgoldsilvercopper_1000_175_p` — Tri Silk Gold Silver Copper
- `teqstone_pla_trisilkredgoldblack_1000_175_p` — Tri Silk Red Gold Black
- `teqstone_pla_trisilkredgreenblue_1000_175_p` — Tri Silk Red Green Blue
- `teqstone_pla_glowyellow_1000_175_p` — Glow Yellow
- `teqstone_pla_glowblue(brightblue)_1000_175_p` — Glow Blue (Bright Blue)
- `teqstone_pla_glowpurple(bluishpurple)_1000_175_p` — Glow Purple (Bluish Purple)
- `teqstone_pla_glowrosered_1000_175_p` — Glow Rose Red
- `teqstone_pla_glowpink_1000_175_p` — Glow Pink
- `teqstone_pla_glowwhite_1000_175_p` — Glow White
- `teqstone_pla_woodplabrown_1000_175_p` — Wood PLA Brown
- `teqstone_pla_woodplawalnut_1000_175_p` — Wood PLA Walnut
- `teqstone_pla-cf_pla-cfblack_1000_175_p` — PLA-CF Black
- `teqstone_petg_petgblack_1000_175_p` — PETG Black
- `teqstone_petg_petgwhite_1000_175_p` — PETG White
- `teqstone_petg_petgapplegreen_1000_175_p` — PETG Apple Green
- `teqstone_petg_petgbrown_1000_175_p` — PETG Brown
- `teqstone_petg_petgcyan(waterblue)_1000_175_p` — PETG Cyan (Water Blue)
- `teqstone_petg_petggreen_1000_175_p` — PETG Green
- `teqstone_petg_petglightskin_1000_175_p` — PETG Light Skin
- `teqstone_petg_petgpink_1000_175_p` — PETG Pink
- `teqstone_petg_petgblue_1000_175_p` — PETG Blue
- `teqstone_petg_petgsilver_1000_175_p` — PETG Silver
- `teqstone_petg_petgyellow_1000_175_p` — PETG Yellow
- `teqstone_petg_metallicpetgmetallicblue_1000_175_p` — Metallic PETG Metallic Blue
- `teqstone_petg_metallicpetgmetallicbrown_1000_175_p` — Metallic PETG Metallic Brown
- `teqstone_petg_metallicpetgmetallicpink_1000_175_p` — Metallic PETG Metallic Pink
- `teqstone_petg_metallicpetgmetallicsilver_1000_175_p` — Metallic PETG Metallic Silver
- `teqstone_abs_absblack_1000_175_p` — ABS Black
- `teqstone_abs_abswhite_1000_175_p` — ABS White
- `teqstone_abs_absgrey_1000_175_p` — ABS Grey
- `teqstone_asa_asablack_1000_175_p` — ASA Black
- `teqstone_asa_asawhite_1000_175_p` — ASA White
- `teqstone_asa_asagreen_1000_175_p` — ASA Green
- `teqstone_asa_asaorange_1000_175_p` — ASA Orange
- `teqstone_asa_asapurple_1000_175_p` — ASA Purple
- `teqstone_tpu-95a_tpu95ablack_1000_175_p` — TPU 95A Black
- `teqstone_tpu-95a_tpu95awhite_1000_175_p` — TPU 95A White
- `teqstone_tpu-95a_tpu95aclear_1000_175_p` — TPU 95A Clear
- `teqstone_tpu-95a_tpu95ablue(translucent)_1000_175_p` — TPU 95A Blue (Translucent)
- `teqstone_tpu-95a_tpu95ared(translucent)_1000_175_p` — TPU 95A Red (Translucent)
- `teqstone_pla_glowplablue_1000_175_p` — Glow PLA Blue
- `teqstone_pla_marbleplablue_1000_175_p` — Marble PLA Blue
- `teqstone_pla_plablack_1000_175_p` — PLA Black
- `teqstone_pla_plablue_1000_175_p` — PLA Blue
- `teqstone_pla_plabrown_1000_175_p` — PLA Brown
- `teqstone_pla_plagreen_1000_175_p` — PLA Green
- `teqstone_pla_plagrey_1000_175_p` — PLA Grey
- `teqstone_pla_plaorange_1000_175_p` — PLA Orange
- `teqstone_pla_plapink_1000_175_p` — PLA Pink
- `teqstone_pla_plared_1000_175_p` — PLA Red
- `teqstone_pla_plasilver_1000_175_p` — PLA Silver
- `teqstone_pla_plawhite_1000_175_p` — PLA White
- `teqstone_pla_playellow_1000_175_p` — PLA Yellow
- `teqstone_pla_placfblack_1000_175_p` — PLA CF Black
- `teqstone_pla_silkplabronze_1000_175_p` — Silk PLA Bronze
- `teqstone_pla_silkpladualgoldsilver_1000_175_p` — Silk PLA Dual Gold Silver
- `teqstone_pla_silkplarainbow_1000_175_p` — Silk PLA Rainbow
- `teqstone_pla_silkplaroyalblue_1000_175_p` — Silk PLA Royal Blue
- `teqstone_pla_silkplatriredbluegreen_1000_175_p` — Silk PLA Tri Red Blue Green
- `teqstone_pla_silkplawhite_1000_175_p` — Silk PLA White
- `teqstone_tpu_tpu95ablack_1000_175_p` — TPU 95A Black
- `teqstone_tpu_tpu95agreen_1000_175_p` — TPU 95A Green
- `teqstone_tpu_tpu95awhite_1000_175_p` — TPU 95A White
