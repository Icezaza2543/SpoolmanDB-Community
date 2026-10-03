# geeetech duplicate migration review

Base `cacf61398af2f10c6344f3c5dff132bba0bd5e68`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `568b4eed28c9f1d5216d30734e0fcaf3707c3137e33d4a6e757fc611342b58a9`.

## Authorization and result

{"groups": 23, "approved_groups": 23, "retired": 23, "deferred": 0, "hard_stops": 0, "before_count": 51889, "after_count": 51866, "brand_before": 161, "brand_after": 138, "registry_before": 1545, "registry_after": 1568, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

23Rule1 exact matches, no code/EAN transfers. Current exact pages corroborate existing Matte220/60, PLA205/60, PETG220–240/80–90 printing settings; keep. No density/TDS provided by those current pages, so retain original Matte1.31,PLA1.24,PETG1.25 unresolved rather than copy genericPLA or newer-source defaults. No wrongdoclinks, packaging/tare/HEX changes.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://www.geeetech.com/products/pla-matte-3d-printer-filament-1-75mm-1kg-roll", "nozzle": [190, 220], "bed": [50, 70]}
- {"url": "https://www.geeetech.com/collections/pla/products/pla-3d-printer-filament-1-75mm-1kg-roll", "nozzle": [185, 215], "bed": [25, 60]}
- {"url": "https://www.geeetech.com/products/petg-3d-printer-filament-1-75mm-1kg-roll", "nozzle": [220, 240], "bed": [80, 90]}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`geeetech_petg_petgblack_1000_175_p`|`geeetech_petg_black_1000_175_p`|`geeetech.json::GEEETECH::PETG {color_name}::PETG Black::PETG::1000::1.75::plastic::False`|
|`geeetech_petg_petgblue_1000_175_p`|`geeetech_petg_blue_1000_175_p`|`geeetech.json::GEEETECH::PETG {color_name}::PETG Blue::PETG::1000::1.75::plastic::False`|
|`geeetech_petg_petgbrown_1000_175_p`|`geeetech_petg_brown_1000_175_p`|`geeetech.json::GEEETECH::PETG {color_name}::PETG Brown::PETG::1000::1.75::plastic::False`|
|`geeetech_petg_petggreen_1000_175_p`|`geeetech_petg_green_1000_175_p`|`geeetech.json::GEEETECH::PETG {color_name}::PETG Green::PETG::1000::1.75::plastic::False`|
|`geeetech_petg_petgorange_1000_175_p`|`geeetech_petg_orange_1000_175_p`|`geeetech.json::GEEETECH::PETG {color_name}::PETG Orange::PETG::1000::1.75::plastic::False`|
|`geeetech_petg_petgpink_1000_175_p`|`geeetech_petg_pink_1000_175_p`|`geeetech.json::GEEETECH::PETG {color_name}::PETG Pink::PETG::1000::1.75::plastic::False`|
|`geeetech_petg_petgpurple_1000_175_p`|`geeetech_petg_purple_1000_175_p`|`geeetech.json::GEEETECH::PETG {color_name}::PETG Purple::PETG::1000::1.75::plastic::False`|
|`geeetech_petg_petgsilver_1000_175_p`|`geeetech_petg_silver_1000_175_p`|`geeetech.json::GEEETECH::PETG {color_name}::PETG Silver::PETG::1000::1.75::plastic::False`|
|`geeetech_petg_petgtransparent_1000_175_p`|`geeetech_petg_transparent_1000_175_p`|`geeetech.json::GEEETECH::PETG {color_name}::PETG Transparent::PETG::1000::1.75::plastic::False`|
|`geeetech_petg_petgwhite_1000_175_p`|`geeetech_petg_white_1000_175_p`|`geeetech.json::GEEETECH::PETG {color_name}::PETG White::PETG::1000::1.75::plastic::False`|
|`geeetech_petg_petgyellow_1000_175_p`|`geeetech_petg_yellow_1000_175_p`|`geeetech.json::GEEETECH::PETG {color_name}::PETG Yellow::PETG::1000::1.75::plastic::False`|
|`geeetech_pla_mattepladarkgrey_1000_175_p`|`geeetech_pla_mattedarkgrey_1000_175_p`|`geeetech.json::GEEETECH::Matte PLA {color_name}::Matte PLA Dark Grey::PLA::1000::1.75::plastic::False`|
|`geeetech_pla_matteplagrey_1000_175_p`|`geeetech_pla_mattegrey_1000_175_p`|`geeetech.json::GEEETECH::Matte PLA {color_name}::Matte PLA Grey::PLA::1000::1.75::plastic::False`|
|`geeetech_pla_matteplaorange_1000_175_p`|`geeetech_pla_matteorange_1000_175_p`|`geeetech.json::GEEETECH::Matte PLA {color_name}::Matte PLA Orange::PLA::1000::1.75::plastic::False`|
|`geeetech_pla_matteplaskin_1000_175_p`|`geeetech_pla_matteskin_1000_175_p`|`geeetech.json::GEEETECH::Matte PLA {color_name}::Matte PLA Skin::PLA::1000::1.75::plastic::False`|
|`geeetech_pla_plaapplegreen_1000_175_p`|`geeetech_pla_applegreen_1000_175_p`|`geeetech.json::GEEETECH::PLA {color_name}::PLA Apple Green::PLA::1000::1.75::plastic::False`|
|`geeetech_pla_plablack_1000_175_p`|`geeetech_pla_black_1000_175_p`|`geeetech.json::GEEETECH::PLA {color_name}::PLA Black::PLA::1000::1.75::plastic::False`|
|`geeetech_pla_plablue_1000_175_p`|`geeetech_pla_blue_1000_175_p`|`geeetech.json::GEEETECH::PLA {color_name}::PLA Blue::PLA::1000::1.75::plastic::False`|
|`geeetech_pla_plagrey_1000_175_p`|`geeetech_pla_grey_1000_175_p`|`geeetech.json::GEEETECH::PLA {color_name}::PLA Grey::PLA::1000::1.75::plastic::False`|
|`geeetech_pla_plaorange_1000_175_p`|`geeetech_pla_orange_1000_175_p`|`geeetech.json::GEEETECH::PLA {color_name}::PLA Orange::PLA::1000::1.75::plastic::False`|
|`geeetech_pla_plared_1000_175_p`|`geeetech_pla_red_1000_175_p`|`geeetech.json::GEEETECH::PLA {color_name}::PLA Red::PLA::1000::1.75::plastic::False`|
|`geeetech_pla_plawaterblue_1000_175_p`|`geeetech_pla_waterblue_1000_175_p`|`geeetech.json::GEEETECH::PLA {color_name}::PLA Water Blue::PLA::1000::1.75::plastic::False`|
|`geeetech_pla_plawhite_1000_175_p`|`geeetech_pla_white_1000_175_p`|`geeetech.json::GEEETECH::PLA {color_name}::PLA White::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### GT001: dup-bcceac9d891d10c9500d005df87eccd174c1305f99603f992d6633cda48da326

Status: APPROVED; survivor `geeetech_petg_black_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_petg_black_1000_175_p`|`{color_name}`|`Black`|{"source_file": "geeetech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / True|
|`geeetech_petg_petgblack_1000_175_p`|`PETG {color_name}`|`Black`|{"source_file": "geeetech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "geeetech_petg_black_1000_175_p": 1.25,
    "geeetech_petg_petgblack_1000_175_p": 1.27
  },
  "spool_weight": {
    "geeetech_petg_black_1000_175_p": 180.0,
    "geeetech_petg_petgblack_1000_175_p": null
  },
  "bed_temp_range": {
    "geeetech_petg_black_1000_175_p": [
      80,
      90
    ],
    "geeetech_petg_petgblack_1000_175_p": [
      70,
      90
    ]
  },
  "finish": {
    "geeetech_petg_black_1000_175_p": "glossy",
    "geeetech_petg_petgblack_1000_175_p": null
  }
}
```

### GT002: dup-77d8ed759bd5c932198a061643ba2960b82be9e3963540bea4e42f7562698791

Status: APPROVED; survivor `geeetech_petg_blue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_petg_blue_1000_175_p`|`{color_name}`|`Blue`|{"source_file": "geeetech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / True|
|`geeetech_petg_petgblue_1000_175_p`|`PETG {color_name}`|`Blue`|{"source_file": "geeetech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "geeetech_petg_blue_1000_175_p": 1.25,
    "geeetech_petg_petgblue_1000_175_p": 1.27
  },
  "spool_weight": {
    "geeetech_petg_blue_1000_175_p": 180.0,
    "geeetech_petg_petgblue_1000_175_p": null
  },
  "color_hex": {
    "geeetech_petg_blue_1000_175_p": "0067ea",
    "geeetech_petg_petgblue_1000_175_p": "0E21AE"
  },
  "bed_temp_range": {
    "geeetech_petg_blue_1000_175_p": [
      80,
      90
    ],
    "geeetech_petg_petgblue_1000_175_p": [
      70,
      90
    ]
  },
  "finish": {
    "geeetech_petg_blue_1000_175_p": "glossy",
    "geeetech_petg_petgblue_1000_175_p": null
  }
}
```

### GT003: dup-7118e5e31cf93248041edf966517f3f22c37b48a0b9e086a673c939cb3137287

Status: APPROVED; survivor `geeetech_petg_brown_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_petg_brown_1000_175_p`|`{color_name}`|`Brown`|{"source_file": "geeetech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / True|
|`geeetech_petg_petgbrown_1000_175_p`|`PETG {color_name}`|`Brown`|{"source_file": "geeetech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "geeetech_petg_brown_1000_175_p": 1.25,
    "geeetech_petg_petgbrown_1000_175_p": 1.27
  },
  "spool_weight": {
    "geeetech_petg_brown_1000_175_p": 180.0,
    "geeetech_petg_petgbrown_1000_175_p": null
  },
  "color_hex": {
    "geeetech_petg_brown_1000_175_p": "b56b58",
    "geeetech_petg_petgbrown_1000_175_p": "A54830"
  },
  "bed_temp_range": {
    "geeetech_petg_brown_1000_175_p": [
      80,
      90
    ],
    "geeetech_petg_petgbrown_1000_175_p": [
      70,
      90
    ]
  },
  "finish": {
    "geeetech_petg_brown_1000_175_p": "glossy",
    "geeetech_petg_petgbrown_1000_175_p": null
  }
}
```

### GT004: dup-b64023b8acdf74bae6cc6af5c2e7eaaeac43d3a3ce816af509492f0e1a90938a

Status: APPROVED; survivor `geeetech_petg_green_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_petg_green_1000_175_p`|`{color_name}`|`Green`|{"source_file": "geeetech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / True|
|`geeetech_petg_petggreen_1000_175_p`|`PETG {color_name}`|`Green`|{"source_file": "geeetech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "geeetech_petg_green_1000_175_p": 1.25,
    "geeetech_petg_petggreen_1000_175_p": 1.27
  },
  "spool_weight": {
    "geeetech_petg_green_1000_175_p": 180.0,
    "geeetech_petg_petggreen_1000_175_p": null
  },
  "color_hex": {
    "geeetech_petg_green_1000_175_p": "1c8c04",
    "geeetech_petg_petggreen_1000_175_p": "089A45"
  },
  "bed_temp_range": {
    "geeetech_petg_green_1000_175_p": [
      80,
      90
    ],
    "geeetech_petg_petggreen_1000_175_p": [
      70,
      90
    ]
  },
  "finish": {
    "geeetech_petg_green_1000_175_p": "glossy",
    "geeetech_petg_petggreen_1000_175_p": null
  }
}
```

### GT005: dup-447ea776c4b3f4301b1c12f374877f9ee300edea6e0f9a9f9079f59d4f46b6fe

Status: APPROVED; survivor `geeetech_petg_orange_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_petg_orange_1000_175_p`|`{color_name}`|`Orange`|{"source_file": "geeetech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / True|
|`geeetech_petg_petgorange_1000_175_p`|`PETG {color_name}`|`Orange`|{"source_file": "geeetech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "geeetech_petg_orange_1000_175_p": 1.25,
    "geeetech_petg_petgorange_1000_175_p": 1.27
  },
  "spool_weight": {
    "geeetech_petg_orange_1000_175_p": 180.0,
    "geeetech_petg_petgorange_1000_175_p": null
  },
  "color_hex": {
    "geeetech_petg_orange_1000_175_p": "f65d33",
    "geeetech_petg_petgorange_1000_175_p": "F55928"
  },
  "bed_temp_range": {
    "geeetech_petg_orange_1000_175_p": [
      80,
      90
    ],
    "geeetech_petg_petgorange_1000_175_p": [
      70,
      90
    ]
  },
  "finish": {
    "geeetech_petg_orange_1000_175_p": "glossy",
    "geeetech_petg_petgorange_1000_175_p": null
  }
}
```

### GT006: dup-814bdb8b92992dc6e4b639576533ac10eb7db8eb60d7b5d467a5b268bb44d389

Status: APPROVED; survivor `geeetech_petg_pink_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_petg_petgpink_1000_175_p`|`PETG {color_name}`|`Pink`|{"source_file": "geeetech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|
|`geeetech_petg_pink_1000_175_p`|`{color_name}`|`Pink`|{"source_file": "geeetech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "geeetech_petg_petgpink_1000_175_p": 1.27,
    "geeetech_petg_pink_1000_175_p": 1.25
  },
  "spool_weight": {
    "geeetech_petg_petgpink_1000_175_p": null,
    "geeetech_petg_pink_1000_175_p": 180.0
  },
  "color_hex": {
    "geeetech_petg_petgpink_1000_175_p": "B645A9",
    "geeetech_petg_pink_1000_175_p": "ec58b8"
  },
  "bed_temp_range": {
    "geeetech_petg_petgpink_1000_175_p": [
      70,
      90
    ],
    "geeetech_petg_pink_1000_175_p": [
      80,
      90
    ]
  },
  "finish": {
    "geeetech_petg_petgpink_1000_175_p": null,
    "geeetech_petg_pink_1000_175_p": "glossy"
  }
}
```

### GT007: dup-e05510e1c21ac86353df9a4283e8aca1e6b3c08eb60c8928c48443e46dea246c

Status: APPROVED; survivor `geeetech_petg_purple_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_petg_petgpurple_1000_175_p`|`PETG {color_name}`|`Purple`|{"source_file": "geeetech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|
|`geeetech_petg_purple_1000_175_p`|`{color_name}`|`Purple`|{"source_file": "geeetech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "geeetech_petg_petgpurple_1000_175_p": 1.27,
    "geeetech_petg_purple_1000_175_p": 1.25
  },
  "spool_weight": {
    "geeetech_petg_petgpurple_1000_175_p": null,
    "geeetech_petg_purple_1000_175_p": 180.0
  },
  "color_hex": {
    "geeetech_petg_petgpurple_1000_175_p": "6C47B2",
    "geeetech_petg_purple_1000_175_p": "6a24b6"
  },
  "bed_temp_range": {
    "geeetech_petg_petgpurple_1000_175_p": [
      70,
      90
    ],
    "geeetech_petg_purple_1000_175_p": [
      80,
      90
    ]
  },
  "finish": {
    "geeetech_petg_petgpurple_1000_175_p": null,
    "geeetech_petg_purple_1000_175_p": "glossy"
  }
}
```

### GT008: dup-d5e33376b740f483dffef50779cdb81e3a5be82076bf8c5452a59b29d722ea46

Status: APPROVED; survivor `geeetech_petg_silver_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_petg_petgsilver_1000_175_p`|`PETG {color_name}`|`Silver`|{"source_file": "geeetech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|
|`geeetech_petg_silver_1000_175_p`|`{color_name}`|`Silver`|{"source_file": "geeetech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "geeetech_petg_petgsilver_1000_175_p": 1.27,
    "geeetech_petg_silver_1000_175_p": 1.25
  },
  "spool_weight": {
    "geeetech_petg_petgsilver_1000_175_p": null,
    "geeetech_petg_silver_1000_175_p": 180.0
  },
  "color_hex": {
    "geeetech_petg_petgsilver_1000_175_p": "A8B0BD",
    "geeetech_petg_silver_1000_175_p": "e7ecf0"
  },
  "bed_temp_range": {
    "geeetech_petg_petgsilver_1000_175_p": [
      70,
      90
    ],
    "geeetech_petg_silver_1000_175_p": [
      80,
      90
    ]
  },
  "finish": {
    "geeetech_petg_petgsilver_1000_175_p": null,
    "geeetech_petg_silver_1000_175_p": "glossy"
  }
}
```

### GT009: dup-89f989de72f8e0f81f5c9ad4df8ac9cf72644904302aaf7344b5dd9db27a6b31

Status: APPROVED; survivor `geeetech_petg_transparent_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_petg_petgtransparent_1000_175_p`|`PETG {color_name}`|`Transparent`|{"source_file": "geeetech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|
|`geeetech_petg_transparent_1000_175_p`|`{color_name}`|`Transparent`|{"source_file": "geeetech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "geeetech_petg_petgtransparent_1000_175_p": 1.27,
    "geeetech_petg_transparent_1000_175_p": 1.25
  },
  "spool_weight": {
    "geeetech_petg_petgtransparent_1000_175_p": null,
    "geeetech_petg_transparent_1000_175_p": 180.0
  },
  "color_hex": {
    "geeetech_petg_petgtransparent_1000_175_p": "E4E7E5",
    "geeetech_petg_transparent_1000_175_p": "ededed"
  },
  "bed_temp_range": {
    "geeetech_petg_petgtransparent_1000_175_p": [
      70,
      90
    ],
    "geeetech_petg_transparent_1000_175_p": [
      80,
      90
    ]
  },
  "finish": {
    "geeetech_petg_petgtransparent_1000_175_p": null,
    "geeetech_petg_transparent_1000_175_p": "glossy"
  }
}
```

### GT010: dup-1d65eb5a782504ca1179d0d428509453432f66aec79651d512b11c65bb605a7f

Status: APPROVED; survivor `geeetech_petg_white_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_petg_petgwhite_1000_175_p`|`PETG {color_name}`|`White`|{"source_file": "geeetech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|
|`geeetech_petg_white_1000_175_p`|`{color_name}`|`White`|{"source_file": "geeetech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "geeetech_petg_petgwhite_1000_175_p": 1.27,
    "geeetech_petg_white_1000_175_p": 1.25
  },
  "spool_weight": {
    "geeetech_petg_petgwhite_1000_175_p": null,
    "geeetech_petg_white_1000_175_p": 180.0
  },
  "color_hex": {
    "geeetech_petg_petgwhite_1000_175_p": "FFFFFF",
    "geeetech_petg_white_1000_175_p": "fcfefb"
  },
  "bed_temp_range": {
    "geeetech_petg_petgwhite_1000_175_p": [
      70,
      90
    ],
    "geeetech_petg_white_1000_175_p": [
      80,
      90
    ]
  },
  "finish": {
    "geeetech_petg_petgwhite_1000_175_p": null,
    "geeetech_petg_white_1000_175_p": "glossy"
  }
}
```

### GT011: dup-b01a69a036a4f420cce9ad6e7ac8432653418bf083d20905881ceb14cc753b14

Status: APPROVED; survivor `geeetech_petg_yellow_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_petg_petgyellow_1000_175_p`|`PETG {color_name}`|`Yellow`|{"source_file": "geeetech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|
|`geeetech_petg_yellow_1000_175_p`|`{color_name}`|`Yellow`|{"source_file": "geeetech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "geeetech_petg_petgyellow_1000_175_p": 1.27,
    "geeetech_petg_yellow_1000_175_p": 1.25
  },
  "spool_weight": {
    "geeetech_petg_petgyellow_1000_175_p": null,
    "geeetech_petg_yellow_1000_175_p": 180.0
  },
  "color_hex": {
    "geeetech_petg_petgyellow_1000_175_p": "FFFB00",
    "geeetech_petg_yellow_1000_175_p": "feea00"
  },
  "bed_temp_range": {
    "geeetech_petg_petgyellow_1000_175_p": [
      70,
      90
    ],
    "geeetech_petg_yellow_1000_175_p": [
      80,
      90
    ]
  },
  "finish": {
    "geeetech_petg_petgyellow_1000_175_p": null,
    "geeetech_petg_yellow_1000_175_p": "glossy"
  }
}
```

### GT012: dup-8e445b704e33fa964fc76d31cccb78513595c8f6053b0ebf23c196bd0b42bd6a

Status: APPROVED; survivor `geeetech_pla_applegreen_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_pla_applegreen_1000_175_p`|`{color_name}`|`Apple Green`|{"source_file": "geeetech.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`geeetech_pla_plaapplegreen_1000_175_p`|`PLA {color_name}`|`Apple Green`|{"source_file": "geeetech.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "geeetech_pla_applegreen_1000_175_p": 180.0,
    "geeetech_pla_plaapplegreen_1000_175_p": null
  },
  "color_hex": {
    "geeetech_pla_applegreen_1000_175_p": "B6D649",
    "geeetech_pla_plaapplegreen_1000_175_p": "BBDB4B"
  },
  "extruder_temp": {
    "geeetech_pla_applegreen_1000_175_p": 205,
    "geeetech_pla_plaapplegreen_1000_175_p": null
  },
  "extruder_temp_range": {
    "geeetech_pla_applegreen_1000_175_p": null,
    "geeetech_pla_plaapplegreen_1000_175_p": [
      185,
      215
    ]
  },
  "bed_temp": {
    "geeetech_pla_applegreen_1000_175_p": 60,
    "geeetech_pla_plaapplegreen_1000_175_p": null
  },
  "bed_temp_range": {
    "geeetech_pla_applegreen_1000_175_p": null,
    "geeetech_pla_plaapplegreen_1000_175_p": [
      25,
      60
    ]
  }
}
```

### GT013: dup-10244e015c63527b206b788627445633c00bd611c6f78c1ee33e08f4d77a16da

Status: APPROVED; survivor `geeetech_pla_black_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_pla_black_1000_175_p`|`{color_name}`|`Black`|{"source_file": "geeetech.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`geeetech_pla_plablack_1000_175_p`|`PLA {color_name}`|`Black`|{"source_file": "geeetech.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "geeetech_pla_black_1000_175_p": 180.0,
    "geeetech_pla_plablack_1000_175_p": null
  },
  "color_hex": {
    "geeetech_pla_black_1000_175_p": "3C3C3C",
    "geeetech_pla_plablack_1000_175_p": "000000"
  },
  "extruder_temp": {
    "geeetech_pla_black_1000_175_p": 205,
    "geeetech_pla_plablack_1000_175_p": null
  },
  "extruder_temp_range": {
    "geeetech_pla_black_1000_175_p": null,
    "geeetech_pla_plablack_1000_175_p": [
      185,
      215
    ]
  },
  "bed_temp": {
    "geeetech_pla_black_1000_175_p": 60,
    "geeetech_pla_plablack_1000_175_p": null
  },
  "bed_temp_range": {
    "geeetech_pla_black_1000_175_p": null,
    "geeetech_pla_plablack_1000_175_p": [
      25,
      60
    ]
  }
}
```

### GT014: dup-685ceae1b708f06f472a79675b7008fb4e030dcc93ec0d695d242220ea0b956e

Status: APPROVED; survivor `geeetech_pla_blue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_pla_blue_1000_175_p`|`{color_name}`|`Blue`|{"source_file": "geeetech.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`geeetech_pla_plablue_1000_175_p`|`PLA {color_name}`|`Blue`|{"source_file": "geeetech.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "geeetech_pla_blue_1000_175_p": 180.0,
    "geeetech_pla_plablue_1000_175_p": null
  },
  "color_hex": {
    "geeetech_pla_blue_1000_175_p": "0071AE",
    "geeetech_pla_plablue_1000_175_p": "2E56F1"
  },
  "extruder_temp": {
    "geeetech_pla_blue_1000_175_p": 205,
    "geeetech_pla_plablue_1000_175_p": null
  },
  "extruder_temp_range": {
    "geeetech_pla_blue_1000_175_p": null,
    "geeetech_pla_plablue_1000_175_p": [
      185,
      215
    ]
  },
  "bed_temp": {
    "geeetech_pla_blue_1000_175_p": 60,
    "geeetech_pla_plablue_1000_175_p": null
  },
  "bed_temp_range": {
    "geeetech_pla_blue_1000_175_p": null,
    "geeetech_pla_plablue_1000_175_p": [
      25,
      60
    ]
  }
}
```

### GT015: dup-16f8932d15f57305a590445de733ff47da12dd639aa954ee7a14136f665a4aa3

Status: APPROVED; survivor `geeetech_pla_grey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_pla_grey_1000_175_p`|`{color_name}`|`Grey`|{"source_file": "geeetech.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`geeetech_pla_plagrey_1000_175_p`|`PLA {color_name}`|`Grey`|{"source_file": "geeetech.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "geeetech_pla_grey_1000_175_p": 180.0,
    "geeetech_pla_plagrey_1000_175_p": null
  },
  "color_hex": {
    "geeetech_pla_grey_1000_175_p": "82868A",
    "geeetech_pla_plagrey_1000_175_p": "C3CCD5"
  },
  "extruder_temp": {
    "geeetech_pla_grey_1000_175_p": 205,
    "geeetech_pla_plagrey_1000_175_p": null
  },
  "extruder_temp_range": {
    "geeetech_pla_grey_1000_175_p": null,
    "geeetech_pla_plagrey_1000_175_p": [
      185,
      215
    ]
  },
  "bed_temp": {
    "geeetech_pla_grey_1000_175_p": 60,
    "geeetech_pla_plagrey_1000_175_p": null
  },
  "bed_temp_range": {
    "geeetech_pla_grey_1000_175_p": null,
    "geeetech_pla_plagrey_1000_175_p": [
      25,
      60
    ]
  }
}
```

### GT016: dup-8303ff6f34bb5ab656a635968bba93d9664e258e395c3208a04f8119e5abf198

Status: APPROVED; survivor `geeetech_pla_mattedarkgrey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_pla_mattedarkgrey_1000_175_p`|`Matte {color_name}`|`Dark Grey`|{"source_file": "geeetech.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / True|
|`geeetech_pla_mattepladarkgrey_1000_175_p`|`Matte PLA {color_name}`|`Dark Grey`|{"source_file": "geeetech.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "geeetech_pla_mattedarkgrey_1000_175_p": 1.31,
    "geeetech_pla_mattepladarkgrey_1000_175_p": 1.24
  },
  "spool_weight": {
    "geeetech_pla_mattedarkgrey_1000_175_p": 180.0,
    "geeetech_pla_mattepladarkgrey_1000_175_p": null
  },
  "color_hex": {
    "geeetech_pla_mattedarkgrey_1000_175_p": "282A2E",
    "geeetech_pla_mattepladarkgrey_1000_175_p": "A2AAAD"
  },
  "extruder_temp": {
    "geeetech_pla_mattedarkgrey_1000_175_p": 220,
    "geeetech_pla_mattepladarkgrey_1000_175_p": null
  },
  "extruder_temp_range": {
    "geeetech_pla_mattedarkgrey_1000_175_p": null,
    "geeetech_pla_mattepladarkgrey_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp": {
    "geeetech_pla_mattedarkgrey_1000_175_p": 60,
    "geeetech_pla_mattepladarkgrey_1000_175_p": null
  },
  "bed_temp_range": {
    "geeetech_pla_mattedarkgrey_1000_175_p": null,
    "geeetech_pla_mattepladarkgrey_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GT017: dup-0b2bd39d055396c2b4613ee7fe3819905c6956c8d379eb31e983a785a5490246

Status: APPROVED; survivor `geeetech_pla_mattegrey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_pla_mattegrey_1000_175_p`|`Matte {color_name}`|`Grey`|{"source_file": "geeetech.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / True|
|`geeetech_pla_matteplagrey_1000_175_p`|`Matte PLA {color_name}`|`Grey`|{"source_file": "geeetech.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "geeetech_pla_mattegrey_1000_175_p": 1.31,
    "geeetech_pla_matteplagrey_1000_175_p": 1.24
  },
  "spool_weight": {
    "geeetech_pla_mattegrey_1000_175_p": 180.0,
    "geeetech_pla_matteplagrey_1000_175_p": null
  },
  "color_hex": {
    "geeetech_pla_mattegrey_1000_175_p": "4A4B52",
    "geeetech_pla_matteplagrey_1000_175_p": "959FA1"
  },
  "extruder_temp": {
    "geeetech_pla_mattegrey_1000_175_p": 220,
    "geeetech_pla_matteplagrey_1000_175_p": null
  },
  "extruder_temp_range": {
    "geeetech_pla_mattegrey_1000_175_p": null,
    "geeetech_pla_matteplagrey_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp": {
    "geeetech_pla_mattegrey_1000_175_p": 60,
    "geeetech_pla_matteplagrey_1000_175_p": null
  },
  "bed_temp_range": {
    "geeetech_pla_mattegrey_1000_175_p": null,
    "geeetech_pla_matteplagrey_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GT018: dup-de192a0448604ea35bdfb7744dc155f9dce9de0342e1f93c5d1a93e6e222f4b7

Status: APPROVED; survivor `geeetech_pla_matteorange_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_pla_matteorange_1000_175_p`|`Matte {color_name}`|`Orange`|{"source_file": "geeetech.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / True|
|`geeetech_pla_matteplaorange_1000_175_p`|`Matte PLA {color_name}`|`Orange`|{"source_file": "geeetech.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "geeetech_pla_matteorange_1000_175_p": 1.31,
    "geeetech_pla_matteplaorange_1000_175_p": 1.24
  },
  "spool_weight": {
    "geeetech_pla_matteorange_1000_175_p": 180.0,
    "geeetech_pla_matteplaorange_1000_175_p": null
  },
  "color_hex": {
    "geeetech_pla_matteorange_1000_175_p": "CB8863",
    "geeetech_pla_matteplaorange_1000_175_p": "DD9879"
  },
  "extruder_temp": {
    "geeetech_pla_matteorange_1000_175_p": 220,
    "geeetech_pla_matteplaorange_1000_175_p": null
  },
  "extruder_temp_range": {
    "geeetech_pla_matteorange_1000_175_p": null,
    "geeetech_pla_matteplaorange_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp": {
    "geeetech_pla_matteorange_1000_175_p": 60,
    "geeetech_pla_matteplaorange_1000_175_p": null
  },
  "bed_temp_range": {
    "geeetech_pla_matteorange_1000_175_p": null,
    "geeetech_pla_matteplaorange_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GT019: dup-495e5352ed458919fb79a6cf3866b7b428319cf4d0c5269cf01b1e9aea8ab494

Status: APPROVED; survivor `geeetech_pla_matteskin_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_pla_matteplaskin_1000_175_p`|`Matte PLA {color_name}`|`Skin`|{"source_file": "geeetech.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`geeetech_pla_matteskin_1000_175_p`|`Matte {color_name}`|`Skin`|{"source_file": "geeetech.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "geeetech_pla_matteplaskin_1000_175_p": 1.24,
    "geeetech_pla_matteskin_1000_175_p": 1.31
  },
  "spool_weight": {
    "geeetech_pla_matteplaskin_1000_175_p": null,
    "geeetech_pla_matteskin_1000_175_p": 180.0
  },
  "color_hex": {
    "geeetech_pla_matteplaskin_1000_175_p": "E6BA83",
    "geeetech_pla_matteskin_1000_175_p": "EBB791"
  },
  "extruder_temp": {
    "geeetech_pla_matteplaskin_1000_175_p": null,
    "geeetech_pla_matteskin_1000_175_p": 220
  },
  "extruder_temp_range": {
    "geeetech_pla_matteplaskin_1000_175_p": [
      190,
      220
    ],
    "geeetech_pla_matteskin_1000_175_p": null
  },
  "bed_temp": {
    "geeetech_pla_matteplaskin_1000_175_p": null,
    "geeetech_pla_matteskin_1000_175_p": 60
  },
  "bed_temp_range": {
    "geeetech_pla_matteplaskin_1000_175_p": [
      50,
      70
    ],
    "geeetech_pla_matteskin_1000_175_p": null
  }
}
```

### GT020: dup-a9b9e5b816b46d742324c484fb30ecf72838a32cac9759c42faedef7d9e08221

Status: APPROVED; survivor `geeetech_pla_orange_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_pla_orange_1000_175_p`|`{color_name}`|`Orange`|{"source_file": "geeetech.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`geeetech_pla_plaorange_1000_175_p`|`PLA {color_name}`|`Orange`|{"source_file": "geeetech.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "geeetech_pla_orange_1000_175_p": 180.0,
    "geeetech_pla_plaorange_1000_175_p": null
  },
  "color_hex": {
    "geeetech_pla_orange_1000_175_p": "E99D48",
    "geeetech_pla_plaorange_1000_175_p": "FF9100"
  },
  "extruder_temp": {
    "geeetech_pla_orange_1000_175_p": 205,
    "geeetech_pla_plaorange_1000_175_p": null
  },
  "extruder_temp_range": {
    "geeetech_pla_orange_1000_175_p": null,
    "geeetech_pla_plaorange_1000_175_p": [
      185,
      215
    ]
  },
  "bed_temp": {
    "geeetech_pla_orange_1000_175_p": 60,
    "geeetech_pla_plaorange_1000_175_p": null
  },
  "bed_temp_range": {
    "geeetech_pla_orange_1000_175_p": null,
    "geeetech_pla_plaorange_1000_175_p": [
      25,
      60
    ]
  }
}
```

### GT021: dup-b13c3a23b4ef51d8bada1e5b0254be507c75bed51df3b18a814c7197ccd336c9

Status: APPROVED; survivor `geeetech_pla_red_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_pla_plared_1000_175_p`|`PLA {color_name}`|`Red`|{"source_file": "geeetech.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`geeetech_pla_red_1000_175_p`|`{color_name}`|`Red`|{"source_file": "geeetech.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "geeetech_pla_plared_1000_175_p": null,
    "geeetech_pla_red_1000_175_p": 180.0
  },
  "color_hex": {
    "geeetech_pla_plared_1000_175_p": "000000",
    "geeetech_pla_red_1000_175_p": "FA0000"
  },
  "extruder_temp": {
    "geeetech_pla_plared_1000_175_p": null,
    "geeetech_pla_red_1000_175_p": 205
  },
  "extruder_temp_range": {
    "geeetech_pla_plared_1000_175_p": [
      185,
      215
    ],
    "geeetech_pla_red_1000_175_p": null
  },
  "bed_temp": {
    "geeetech_pla_plared_1000_175_p": null,
    "geeetech_pla_red_1000_175_p": 60
  },
  "bed_temp_range": {
    "geeetech_pla_plared_1000_175_p": [
      25,
      60
    ],
    "geeetech_pla_red_1000_175_p": null
  }
}
```

### GT022: dup-c4ef92c03345c5c3cb8dec2a7286ee1edb5185e2258c809a446381df46e9be89

Status: APPROVED; survivor `geeetech_pla_waterblue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_pla_plawaterblue_1000_175_p`|`PLA {color_name}`|`Water Blue`|{"source_file": "geeetech.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`geeetech_pla_waterblue_1000_175_p`|`{color_name}`|`Water Blue`|{"source_file": "geeetech.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "geeetech_pla_plawaterblue_1000_175_p": null,
    "geeetech_pla_waterblue_1000_175_p": 180.0
  },
  "color_hex": {
    "geeetech_pla_plawaterblue_1000_175_p": "1ADAFB",
    "geeetech_pla_waterblue_1000_175_p": "04AACB"
  },
  "extruder_temp": {
    "geeetech_pla_plawaterblue_1000_175_p": null,
    "geeetech_pla_waterblue_1000_175_p": 205
  },
  "extruder_temp_range": {
    "geeetech_pla_plawaterblue_1000_175_p": [
      185,
      215
    ],
    "geeetech_pla_waterblue_1000_175_p": null
  },
  "bed_temp": {
    "geeetech_pla_plawaterblue_1000_175_p": null,
    "geeetech_pla_waterblue_1000_175_p": 60
  },
  "bed_temp_range": {
    "geeetech_pla_plawaterblue_1000_175_p": [
      25,
      60
    ],
    "geeetech_pla_waterblue_1000_175_p": null
  }
}
```

### GT023: dup-b35d44db1e8c4f24ce49fca3eba5297c92da6bd12acde4445dd4efa10e8a25c6

Status: APPROVED; survivor `geeetech_pla_white_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`geeetech_pla_plawhite_1000_175_p`|`PLA {color_name}`|`White`|{"source_file": "geeetech.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`geeetech_pla_white_1000_175_p`|`{color_name}`|`White`|{"source_file": "geeetech.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "geeetech_pla_plawhite_1000_175_p": null,
    "geeetech_pla_white_1000_175_p": 180.0
  },
  "color_hex": {
    "geeetech_pla_plawhite_1000_175_p": "FFFFFF",
    "geeetech_pla_white_1000_175_p": "Dee2E7"
  },
  "extruder_temp": {
    "geeetech_pla_plawhite_1000_175_p": null,
    "geeetech_pla_white_1000_175_p": 205
  },
  "extruder_temp_range": {
    "geeetech_pla_plawhite_1000_175_p": [
      185,
      215
    ],
    "geeetech_pla_white_1000_175_p": null
  },
  "bed_temp": {
    "geeetech_pla_plawhite_1000_175_p": null,
    "geeetech_pla_white_1000_175_p": 60
  },
  "bed_temp_range": {
    "geeetech_pla_plawhite_1000_175_p": [
      25,
      60
    ],
    "geeetech_pla_white_1000_175_p": null
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

- `geeetech_pla_newpurple_1000_175_p` — New Purple
- `geeetech_pla_brown_1000_175_p` — Brown
- `geeetech_pla_luminousgreen_1000_175_p` — Luminous Green
- `geeetech_pla_luminousyellow_1000_175_p` — Luminous Yellow
- `geeetech_pla_luminousorange_1000_175_p` — Luminous Orange
- `geeetech_pla_luminouswhite_1000_175_p` — Luminous White
- `geeetech_pla_luminousblue_1000_175_p` — Luminous Blue
- `geeetech_pla_luminouspurple_1000_175_p` — Luminous Purple
- `geeetech_pla_luminousrosered_1000_175_p` — Luminous Rose red
- `geeetech_pla_mattelightgray_1000_175_p` — Matte Light Gray
- `geeetech_petg_apple_1000_175_p` — Apple
- `geeetech_petg_darkgray_1000_175_p` — Dark Gray
- `geeetech_petg_red_1000_175_p` — Red
- `geeetech_petg_skin_1000_175_p` — Skin
- `geeetech_petg_waterblue_1000_175_p` — Water Blue
- `geeetech_abs+_apple_1000_175_p` — Apple
- `geeetech_abs+_black_1000_175_p` — Black
- `geeetech_abs+_blue_1000_175_p` — Blue
- `geeetech_abs+_brown_1000_175_p` — Brown
- `geeetech_abs+_darkgray_1000_175_p` — Dark Gray
- `geeetech_abs+_green_1000_175_p` — Green
- `geeetech_abs+_orange_1000_175_p` — Orange
- `geeetech_abs+_pink_1000_175_p` — Pink
- `geeetech_abs+_purple_1000_175_p` — Purple
- `geeetech_abs+_red_1000_175_p` — Red
- `geeetech_abs+_silver_1000_175_p` — Silver
- `geeetech_abs+_skin_1000_175_p` — Skin
- `geeetech_abs+_waterblue_1000_175_p` — Water Blue
- `geeetech_abs+_white_1000_175_p` — White
- `geeetech_abs+_yellow_1000_175_p` — Yellow
- `geeetech_abs_abs+applegreen_1000_175_p` — ABS+ Apple Green
- `geeetech_abs_abs+black_1000_175_p` — ABS+ Black
- `geeetech_abs_abs+blue_1000_175_p` — ABS+ Blue
- `geeetech_abs_abs+brown_1000_175_p` — ABS+ Brown
- `geeetech_abs_abs+green_1000_175_p` — ABS+ Green
- `geeetech_abs_abs+grey_1000_175_p` — ABS+ Grey
- `geeetech_abs_abs+orange_1000_175_p` — ABS+ Orange
- `geeetech_abs_abs+pink_1000_175_p` — ABS+ Pink
- `geeetech_abs_abs+purple_1000_175_p` — ABS+ Purple
- `geeetech_abs_abs+red_1000_175_p` — ABS+ Red
- `geeetech_abs_abs+silver_1000_175_p` — ABS+ Silver
- `geeetech_abs_abs+skin_1000_175_p` — ABS+ Skin
- `geeetech_abs_abs+waterblue_1000_175_p` — ABS+ Water Blue
- `geeetech_abs_abs+white_1000_175_p` — ABS+ White
- `geeetech_abs_abs+yellow_1000_175_p` — ABS+ Yellow
- `geeetech_abs_upgradeabsblack_1000_175_p` — Upgrade ABS Black
- `geeetech_abs_upgradeabsblue_1000_175_p` — Upgrade ABS Blue
- `geeetech_petg_petggray_1000_175_p` — PETG Gray
- `geeetech_pla_luminousglowplablue_1000_175_p` — Luminous Glow PLA Blue
- `geeetech_pla_luminousglowplamulticolor_1000_175_p` — Luminous Glow PLA Multicolor
- `geeetech_pla_plamarblegrey_1000_175_p` — PLA Marble Grey
- `geeetech_pla_plamarblemarblewhite-bluestone_1000_175_p` — PLA Marble Marble White-Blue Stone
- `geeetech_pla_plamarblemarblewhite-brownstone_1000_175_p` — PLA Marble Marble White-Brown Stone
- `geeetech_pla_matteplablack_1000_175_p` — Matte PLA Black
- `geeetech_pla_matteplablue_1000_175_p` — Matte PLA Blue
- `geeetech_pla_matteplabrown_1000_175_p` — Matte PLA Brown
- `geeetech_pla_matteplanavyblue_1000_175_p` — Matte PLA Navy Blue
- `geeetech_pla_matteplaolivegreen_1000_175_p` — Matte PLA Olive Green
- `geeetech_pla_matteplawhite_1000_175_p` — Matte PLA White
- `geeetech_pla_plabone_1000_175_p` — PLA Bone
- `geeetech_pla_placlear_1000_175_p` — PLA Clear
- `geeetech_pla_pladarkgreenbronze_1000_175_p` — PLA Dark Green Bronze
- `geeetech_pla_pladefault_1000_175_p` — PLA Default
- `geeetech_pla_plagreen_1000_175_p` — PLA Green
- `geeetech_pla_planewsilver_1000_175_p` — PLA New Silver
- `geeetech_pla_plapurple_1000_175_p` — PLA Purple
- `geeetech_pla_plarainbow_1000_175_p` — PLA Rainbow
- `geeetech_pla_platransparent_1000_175_p` — PLA Transparent
- `geeetech_pla_playellow_1000_175_p` — PLA Yellow
- `geeetech_pla_placfblue_1000_175_p` — PLA CF Blue
- `geeetech_pla_placfbrickred_1000_175_p` — PLA CF Brick Red
- `geeetech_pla_placfmatchagreen_1000_175_p` — PLA CF Matcha Green
- `geeetech_pla_silkpladualcolorblackred_1000_175_p` — Silk PLA Dual Color Black Red
- `geeetech_pla_silkpladualcolorbluegreen_1000_175_p` — Silk PLA Dual Color Blue Green
- `geeetech_pla_silkpladualcolorgoldblack_1000_175_p` — Silk PLA Dual Color Gold Black
- `geeetech_pla_silkpladualcolorgoldcopper_1000_175_p` — Silk PLA Dual Color Gold Copper
- `geeetech_pla_silkpladualcolorgoldpurple_1000_175_p` — Silk PLA Dual Color Gold Purple
- `geeetech_pla_silkpladualcolorgoldred_1000_175_p` — Silk PLA Dual Color Gold Red
- `geeetech_pla_silkpladualcolorgoldsilver_1000_175_p` — Silk PLA Dual Color Gold Silver
- `geeetech_pla_silkpladualcolorgreenred_1000_175_p` — Silk PLA Dual Color Green Red
- `geeetech_pla_silkplagold_1000_175_p` — Silk PLA Gold
- `geeetech_pla_silkplagreen_1000_175_p` — Silk PLA Green
- `geeetech_pla_silkplametallicblack_1000_175_p` — Silk PLA Metallic Black
- `geeetech_pla_silkplametalliccopper_1000_175_p` — Silk PLA Metallic Copper
- `geeetech_pla_silkplametallicpink(magenta)_1000_175_p` — Silk PLA Metallic Pink (Magenta)
- `geeetech_pla_silkplametallicpurple_1000_175_p` — Silk PLA Metallic Purple
- `geeetech_pla_silkplametallicroyalblue_1000_175_p` — Silk PLA Metallic Royal Blue
- `geeetech_pla_silkplametallicsilver_1000_175_p` — Silk PLA Metallic Silver
- `geeetech_pla_silkplametallicwhite_1000_175_p` — Silk PLA Metallic White
- `geeetech_pla_silkplarainbow_1000_175_p` — Silk PLA Rainbow
- `geeetech_pla_silkplatricolorbluepurpleblack_1000_175_p` — Silk PLA Tri Color Blue Purple Black
- `geeetech_pla_silkplatri-colorgoldsilvercopper_1000_175_p` — Silk PLA Tri-Color Gold Silver Copper
- `geeetech_pla_silkplatri-colororangebluegreen_1000_175_p` — Silk PLA Tri-Color Orange Blue Green
- `geeetech_pla_silkplatricolorpurplegoldblack_1000_175_p` — Silk PLA Tri Color Purple Gold Black
- `geeetech_pla_silkplatricolorredgoldblack_1000_175_p` — Silk PLA Tri Color Red Gold Black
- `geeetech_pla_silkplatricolorredgoldpurple_1000_175_p` — Silk PLA Tri Color Red Gold Purple
- `geeetech_pla_silkplatri-colorredyellowblue_1000_175_p` — Silk PLA Tri-Color Red Yellow Blue
- `geeetech_pla_plawoodblackwalnut_1000_175_p` — PLA Wood Black Walnut
- `geeetech_pla_plawoodebony_1000_175_p` — PLA Wood Ebony
- `geeetech_pla_plawoodpoplar_1000_175_p` — PLA Wood Poplar
- `geeetech_pla_plawoodwood_1000_175_p` — PLA Wood Wood
- `geeetech_pla_plawoodwoodebony_1000_175_p` — PLA Wood Wood Ebony
- `geeetech_pla_plawoodwoodpor_1000_175_p` — PLA Wood Wood Por
- `geeetech_tpu_tpu95ablack_1000_175_p` — TPU 95A Black
- `geeetech_tpu_tpu95ablue_1000_175_p` — TPU 95A Blue
- `geeetech_tpu_tpu95abrown_1000_175_p` — TPU 95A Brown
- `geeetech_tpu_tpu95acleargold_1000_175_p` — TPU 95A Clear Gold
- `geeetech_tpu_tpu95agrey_1000_175_p` — TPU 95A Grey
- `geeetech_tpu_tpu95aorange_1000_175_p` — TPU 95A Orange
- `geeetech_tpu_tpu95apink_1000_175_p` — TPU 95A Pink
- `geeetech_tpu_tpu95apurple_1000_175_p` — TPU 95A Purple
- `geeetech_tpu_tpu95ared_1000_175_p` — TPU 95A Red
- `geeetech_tpu_tpu95atransparent_1000_175_p` — TPU 95A Transparent
- `geeetech_tpu_tpu95awhite_1000_175_p` — TPU 95A White
- `geeetech_tpu_tpuclear_1000_175_p` — TPU Clear
