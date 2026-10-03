# jayo duplicate migration review

Base `ec02e18cff8ad7d785007d5cd6906025bb71a5af`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `1da635d6d3f9ec3dc5c3d67077643c0fdabfa3050bed86dfed022226f42295d3`.

## Authorization and result

{"groups": 6, "approved_groups": 6, "retired": 6, "deferred": 0, "hard_stops": 0, "before_count": 51746, "after_count": 51740, "brand_before": 146, "brand_after": 140, "registry_before": 1688, "registry_after": 1694, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Six Rule1 strict duplicates. Existing nominal PLA210/60 and PETG250/80 remain valid within current recommendations; no unnecessary range enrichment. Density1.24/1.25 unverified, retained unresolved. Current1.1kgPLA page does not establish unrelated110g/1kg variants or packaging/tare. No identifiers.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://jayo3d.com/products/pla", "nozzle": [200, 210], "bed": [60, 80], "weight": 1100}
- {"url": "https://jayo3d.com/products/jayo-petg", "nozzle": [220, 250], "bed": [75, 85]}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`jayo_petg_petgblack_1100_175_p`|`jayo_petg_black_1100_175_p`|`jayo.json::JAYO::PETG {color_name}::PETG Black::PETG::1100::1.75::plastic::False`|
|`jayo_petg_petgmintgreen_1100_175_p`|`jayo_petg_mintgreen_1100_175_p`|`jayo.json::JAYO::PETG {color_name}::PETG Mint Green::PETG::1100::1.75::plastic::False`|
|`jayo_petg_petgorange_1100_175_p`|`jayo_petg_orange_1100_175_p`|`jayo.json::JAYO::PETG {color_name}::PETG Orange::PETG::1100::1.75::plastic::False`|
|`jayo_petg_petgred_1100_175_p`|`jayo_petg_red_1100_175_p`|`jayo.json::JAYO::PETG {color_name}::PETG Red::PETG::1100::1.75::plastic::False`|
|`jayo_petg_petgwhite_1100_175_p`|`jayo_petg_white_1100_175_p`|`jayo.json::JAYO::PETG {color_name}::PETG White::PETG::1100::1.75::plastic::False`|
|`jayo_pla_plaolivegreen_1100_175_p`|`jayo_pla_olivegreen_1100_175_p`|`jayo.json::JAYO::PLA {color_name}::PLA Olive Green::PLA::1100::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### JA001: dup-a1226d8ad3f090abb67feebab362637dbf16df660b62e261aeb6c6fb25d488d3

Status: APPROVED; survivor `jayo_petg_black_1100_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`jayo_petg_black_1100_175_p`|`{color_name}`|`Black`|{"source_file": "jayo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / True|
|`jayo_petg_petgblack_1100_175_p`|`PETG {color_name}`|`Black`|{"source_file": "jayo.json", "definition_index": 5, "weights": 3, "diameters": 1, "colors": 14, "compiled_records": 42} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "jayo_petg_black_1100_175_p": 1.25,
    "jayo_petg_petgblack_1100_175_p": 1.27
  },
  "spool_weight": {
    "jayo_petg_black_1100_175_p": 120.0,
    "jayo_petg_petgblack_1100_175_p": null
  },
  "extruder_temp": {
    "jayo_petg_black_1100_175_p": 250,
    "jayo_petg_petgblack_1100_175_p": null
  },
  "extruder_temp_range": {
    "jayo_petg_black_1100_175_p": null,
    "jayo_petg_petgblack_1100_175_p": [
      220,
      250
    ]
  },
  "bed_temp": {
    "jayo_petg_black_1100_175_p": 80,
    "jayo_petg_petgblack_1100_175_p": null
  },
  "bed_temp_range": {
    "jayo_petg_black_1100_175_p": null,
    "jayo_petg_petgblack_1100_175_p": [
      70,
      90
    ]
  },
  "country_of_origin": {
    "jayo_petg_black_1100_175_p": "CN",
    "jayo_petg_petgblack_1100_175_p": "HK"
  }
}
```

### JA002: dup-4563f539b46b062116053c0dd8bb4c73f43523bd51e8aa31a8bfb843946e340c

Status: APPROVED; survivor `jayo_petg_mintgreen_1100_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`jayo_petg_mintgreen_1100_175_p`|`{color_name}`|`Mint Green`|{"source_file": "jayo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / True|
|`jayo_petg_petgmintgreen_1100_175_p`|`PETG {color_name}`|`Mint Green`|{"source_file": "jayo.json", "definition_index": 5, "weights": 3, "diameters": 1, "colors": 14, "compiled_records": 42} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "jayo_petg_mintgreen_1100_175_p": 1.25,
    "jayo_petg_petgmintgreen_1100_175_p": 1.27
  },
  "spool_weight": {
    "jayo_petg_mintgreen_1100_175_p": 120.0,
    "jayo_petg_petgmintgreen_1100_175_p": null
  },
  "color_hex": {
    "jayo_petg_mintgreen_1100_175_p": "7FFFD4",
    "jayo_petg_petgmintgreen_1100_175_p": "22F4D3"
  },
  "extruder_temp": {
    "jayo_petg_mintgreen_1100_175_p": 250,
    "jayo_petg_petgmintgreen_1100_175_p": null
  },
  "extruder_temp_range": {
    "jayo_petg_mintgreen_1100_175_p": null,
    "jayo_petg_petgmintgreen_1100_175_p": [
      220,
      250
    ]
  },
  "bed_temp": {
    "jayo_petg_mintgreen_1100_175_p": 80,
    "jayo_petg_petgmintgreen_1100_175_p": null
  },
  "bed_temp_range": {
    "jayo_petg_mintgreen_1100_175_p": null,
    "jayo_petg_petgmintgreen_1100_175_p": [
      70,
      90
    ]
  },
  "country_of_origin": {
    "jayo_petg_mintgreen_1100_175_p": "CN",
    "jayo_petg_petgmintgreen_1100_175_p": "HK"
  }
}
```

### JA003: dup-2df533a3cfca83c54846ada99c6352a90b936df4f158e5ebf7e48f4ae3783490

Status: APPROVED; survivor `jayo_petg_orange_1100_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`jayo_petg_orange_1100_175_p`|`{color_name}`|`Orange`|{"source_file": "jayo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / True|
|`jayo_petg_petgorange_1100_175_p`|`PETG {color_name}`|`Orange`|{"source_file": "jayo.json", "definition_index": 5, "weights": 3, "diameters": 1, "colors": 14, "compiled_records": 42} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "jayo_petg_orange_1100_175_p": 1.25,
    "jayo_petg_petgorange_1100_175_p": 1.27
  },
  "spool_weight": {
    "jayo_petg_orange_1100_175_p": 120.0,
    "jayo_petg_petgorange_1100_175_p": null
  },
  "color_hex": {
    "jayo_petg_orange_1100_175_p": "F2552A",
    "jayo_petg_petgorange_1100_175_p": "FF8F41"
  },
  "extruder_temp": {
    "jayo_petg_orange_1100_175_p": 250,
    "jayo_petg_petgorange_1100_175_p": null
  },
  "extruder_temp_range": {
    "jayo_petg_orange_1100_175_p": null,
    "jayo_petg_petgorange_1100_175_p": [
      220,
      250
    ]
  },
  "bed_temp": {
    "jayo_petg_orange_1100_175_p": 80,
    "jayo_petg_petgorange_1100_175_p": null
  },
  "bed_temp_range": {
    "jayo_petg_orange_1100_175_p": null,
    "jayo_petg_petgorange_1100_175_p": [
      70,
      90
    ]
  },
  "country_of_origin": {
    "jayo_petg_orange_1100_175_p": "CN",
    "jayo_petg_petgorange_1100_175_p": "HK"
  }
}
```

### JA004: dup-f4e4055fc6ac201fe70e01af0b102ed5386a59d0521ddb431b90ee05f4c6cacc

Status: APPROVED; survivor `jayo_petg_red_1100_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`jayo_petg_petgred_1100_175_p`|`PETG {color_name}`|`Red`|{"source_file": "jayo.json", "definition_index": 5, "weights": 3, "diameters": 1, "colors": 14, "compiled_records": 42} / False|
|`jayo_petg_red_1100_175_p`|`{color_name}`|`Red`|{"source_file": "jayo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "jayo_petg_petgred_1100_175_p": 1.27,
    "jayo_petg_red_1100_175_p": 1.25
  },
  "spool_weight": {
    "jayo_petg_petgred_1100_175_p": null,
    "jayo_petg_red_1100_175_p": 120.0
  },
  "color_hex": {
    "jayo_petg_petgred_1100_175_p": "FF0000",
    "jayo_petg_red_1100_175_p": "F55C3D"
  },
  "extruder_temp": {
    "jayo_petg_petgred_1100_175_p": null,
    "jayo_petg_red_1100_175_p": 250
  },
  "extruder_temp_range": {
    "jayo_petg_petgred_1100_175_p": [
      220,
      250
    ],
    "jayo_petg_red_1100_175_p": null
  },
  "bed_temp": {
    "jayo_petg_petgred_1100_175_p": null,
    "jayo_petg_red_1100_175_p": 80
  },
  "bed_temp_range": {
    "jayo_petg_petgred_1100_175_p": [
      70,
      90
    ],
    "jayo_petg_red_1100_175_p": null
  },
  "country_of_origin": {
    "jayo_petg_petgred_1100_175_p": "HK",
    "jayo_petg_red_1100_175_p": "CN"
  }
}
```

### JA005: dup-a85b5d61738c705090f25a79a564e44f1801249c7d7e03603f83f9213770855a

Status: APPROVED; survivor `jayo_petg_white_1100_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`jayo_petg_petgwhite_1100_175_p`|`PETG {color_name}`|`White`|{"source_file": "jayo.json", "definition_index": 5, "weights": 3, "diameters": 1, "colors": 14, "compiled_records": 42} / False|
|`jayo_petg_white_1100_175_p`|`{color_name}`|`White`|{"source_file": "jayo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "jayo_petg_petgwhite_1100_175_p": 1.27,
    "jayo_petg_white_1100_175_p": 1.25
  },
  "spool_weight": {
    "jayo_petg_petgwhite_1100_175_p": null,
    "jayo_petg_white_1100_175_p": 120.0
  },
  "extruder_temp": {
    "jayo_petg_petgwhite_1100_175_p": null,
    "jayo_petg_white_1100_175_p": 250
  },
  "extruder_temp_range": {
    "jayo_petg_petgwhite_1100_175_p": [
      220,
      250
    ],
    "jayo_petg_white_1100_175_p": null
  },
  "bed_temp": {
    "jayo_petg_petgwhite_1100_175_p": null,
    "jayo_petg_white_1100_175_p": 80
  },
  "bed_temp_range": {
    "jayo_petg_petgwhite_1100_175_p": [
      70,
      90
    ],
    "jayo_petg_white_1100_175_p": null
  },
  "country_of_origin": {
    "jayo_petg_petgwhite_1100_175_p": "HK",
    "jayo_petg_white_1100_175_p": "CN"
  }
}
```

### JA006: dup-07867ae383703f4a96e51be1ab47e77de9fdef44a27ea6312ed99dfe71b794f6

Status: APPROVED; survivor `jayo_pla_olivegreen_1100_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`jayo_pla_olivegreen_1100_175_p`|`{color_name}`|`Olive green`|{"source_file": "jayo.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / True|
|`jayo_pla_plaolivegreen_1100_175_p`|`PLA {color_name}`|`Olive Green`|{"source_file": "jayo.json", "definition_index": 8, "weights": 2, "diameters": 1, "colors": 26, "compiled_records": 52} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "jayo_pla_olivegreen_1100_175_p": 120.0,
    "jayo_pla_plaolivegreen_1100_175_p": null
  },
  "color_hex": {
    "jayo_pla_olivegreen_1100_175_p": "6A845B",
    "jayo_pla_plaolivegreen_1100_175_p": "808000"
  },
  "extruder_temp": {
    "jayo_pla_olivegreen_1100_175_p": 210,
    "jayo_pla_plaolivegreen_1100_175_p": null
  },
  "extruder_temp_range": {
    "jayo_pla_olivegreen_1100_175_p": null,
    "jayo_pla_plaolivegreen_1100_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "jayo_pla_olivegreen_1100_175_p": 60,
    "jayo_pla_plaolivegreen_1100_175_p": null
  },
  "bed_temp_range": {
    "jayo_pla_olivegreen_1100_175_p": null,
    "jayo_pla_plaolivegreen_1100_175_p": [
      50,
      70
    ]
  },
  "country_of_origin": {
    "jayo_pla_olivegreen_1100_175_p": "CN",
    "jayo_pla_plaolivegreen_1100_175_p": "HK"
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

- `jayo_pla+_black_1100_175_c` — Black
- `jayo_pla+_green_1100_175_c` — Green
- `jayo_pla+_red_1100_175_c` — Red
- `jayo_pla+_yellow_1100_175_c` — Yellow
- `jayo_pla+_pureyellow_1100_175_c` — Pure Yellow
- `jayo_pla+_grey-blue_1100_175_c` — Grey-Blue
- `jayo_pla+_orange_1100_175_c` — Orange
- `jayo_pla+_blue_1100_175_c` — Blue
- `jayo_pla+_grassgreen_1100_175_c` — Grass Green
- `jayo_pla+_wood_1100_175_c` — Wood
- `jayo_pla+_whitetransparent_1100_175_c` — White Transparent
- `jayo_pla+_goldsilk_1100_175_c` — Gold Silk
- `jayo_pla+_bluesilk_1100_175_c` — Blue Silk
- `jayo_pla_mattepink_1100_175_p` — Matte Pink
- `jayo_pla_mattepurple_1100_175_p` — Matte Purple
- `jayo_pla_matteblack_1100_175_p` — Matte Black
- `jayo_pla_mattewhite_1100_175_p` — Matte White
- `jayo_petg_gray_1100_175_p` — Gray
- `jayo_tpu_silkcreamwhite_1100_175_c` — Silk Cream White
- `jayo_tpu_silkblack_1100_175_c` — Silk Black
- `jayo_tpu_silklightblue_1100_175_c` — Silk Light Blue
- `jayo_tpu_silkdarkblue_1100_175_c` — Silk Dark Blue
- `jayo_tpu_silkburgundy_1100_175_c` — Silk Burgundy
- `jayo_pla_white(glowgreen)_1100_175_c` — White (Glow Green)
- `jayo_pla_white(glowblue)_1100_175_c` — White (Glow Blue)
- `jayo_pla_yellow(glowyellow)_1100_175_c` — Yellow (Glow Yellow)
- `jayo_pla_red(gloworange)_1100_175_c` — Red (Glow Orange)
- `jayo_petg_petgblack_110_175_p` — PETG Black
- `jayo_petg_petgblue_110_175_p` — PETG Blue
- `jayo_petg_petgcherryred_110_175_p` — PETG Cherry Red
- `jayo_petg_petgcyan_110_175_p` — PETG Cyan
- `jayo_petg_petggreen_110_175_p` — PETG Green
- `jayo_petg_petglemonyellow_110_175_p` — PETG Lemon Yellow
- `jayo_petg_petgmintgreen_110_175_p` — PETG Mint Green
- `jayo_petg_petgorange_110_175_p` — PETG Orange
- `jayo_petg_petgred_110_175_p` — PETG Red
- `jayo_petg_petgsakurapink_110_175_p` — PETG Sakura Pink
- `jayo_petg_petgsilver_110_175_p` — PETG Silver
- `jayo_petg_petgskyblue_110_175_p` — PETG Sky Blue
- `jayo_petg_petgwhite_110_175_p` — PETG White
- `jayo_petg_petgyellow_110_175_p` — PETG Yellow
- `jayo_petg_petgblack_1000_175_p` — PETG Black
- `jayo_petg_petgblue_1000_175_p` — PETG Blue
- `jayo_petg_petgcherryred_1000_175_p` — PETG Cherry Red
- `jayo_petg_petgcyan_1000_175_p` — PETG Cyan
- `jayo_petg_petggreen_1000_175_p` — PETG Green
- `jayo_petg_petglemonyellow_1000_175_p` — PETG Lemon Yellow
- `jayo_petg_petgmintgreen_1000_175_p` — PETG Mint Green
- `jayo_petg_petgorange_1000_175_p` — PETG Orange
- `jayo_petg_petgred_1000_175_p` — PETG Red
- `jayo_petg_petgsakurapink_1000_175_p` — PETG Sakura Pink
- `jayo_petg_petgsilver_1000_175_p` — PETG Silver
- `jayo_petg_petgskyblue_1000_175_p` — PETG Sky Blue
- `jayo_petg_petgwhite_1000_175_p` — PETG White
- `jayo_petg_petgyellow_1000_175_p` — PETG Yellow
- `jayo_petg_petgblue_1100_175_p` — PETG Blue
- `jayo_petg_petgcherryred_1100_175_p` — PETG Cherry Red
- `jayo_petg_petgcyan_1100_175_p` — PETG Cyan
- `jayo_petg_petggreen_1100_175_p` — PETG Green
- `jayo_petg_petglemonyellow_1100_175_p` — PETG Lemon Yellow
- `jayo_petg_petgsakurapink_1100_175_p` — PETG Sakura Pink
- `jayo_petg_petgsilver_1100_175_p` — PETG Silver
- `jayo_petg_petgskyblue_1100_175_p` — PETG Sky Blue
- `jayo_petg_petgyellow_1100_175_p` — PETG Yellow
- `jayo_pla_highspeedmatteplablack_1100_175_p` — High Speed Matte PLA Black
- `jayo_pla_matteplablack_1000_175_p` — Matte PLA Black
- `jayo_pla_matteplablue_1000_175_p` — Matte PLA Blue
- `jayo_pla_matteplagreen_1000_175_p` — Matte PLA Green
- `jayo_pla_matteplagrey_1000_175_p` — Matte PLA Grey
- `jayo_pla_matteplalightblue_1000_175_p` — Matte PLA Light Blue
- `jayo_pla_matteplaolivegreen_1000_175_p` — Matte PLA Olive Green
- `jayo_pla_matteplaorange_1000_175_p` — Matte PLA Orange
- `jayo_pla_matteplapink_1000_175_p` — Matte PLA Pink
- `jayo_pla_matteplapurple_1000_175_p` — Matte PLA Purple
- `jayo_pla_matteplared_1000_175_p` — Matte PLA Red
- `jayo_pla_matteplawhite_1000_175_p` — Matte PLA White
- `jayo_pla_plablack_1000_175_p` — PLA Black
- `jayo_pla_plablue_1000_175_p` — PLA Blue
- `jayo_pla_placherryred_1000_175_p` — PLA Cherry Red
- `jayo_pla_plachocolate_1000_175_p` — PLA Chocolate
- `jayo_pla_placoffee_1000_175_p` — PLA Coffee
- `jayo_pla_placyan_1000_175_p` — PLA Cyan
- `jayo_pla_plafuchsia_1000_175_p` — PLA Fuchsia
- `jayo_pla_plagrassgreen_1000_175_p` — PLA Grass Green
- `jayo_pla_plagray_1000_175_p` — PLA Gray
- `jayo_pla_plagreen_1000_175_p` — PLA Green
- `jayo_pla_plalemonyellow_1000_175_p` — PLA Lemon Yellow
- `jayo_pla_plamintgreen_1000_175_p` — PLA Mint Green
- `jayo_pla_plaolivegreen_1000_175_p` — PLA Olive Green
- `jayo_pla_plapurple_1000_175_p` — PLA Purple
- `jayo_pla_plared_1000_175_p` — PLA Red
- `jayo_pla_plasakurapink_1000_175_p` — PLA Sakura Pink
- `jayo_pla_plasilver_1000_175_p` — PLA Silver
- `jayo_pla_plaskyblue_1000_175_p` — PLA Sky Blue
- `jayo_pla_plasunnyorange_1000_175_p` — PLA Sunny Orange
- `jayo_pla_platransparent_1000_175_p` — PLA Transparent
- `jayo_pla_platransparentblue_1000_175_p` — PLA Transparent Blue
- `jayo_pla_platransparentpurple_1000_175_p` — PLA Transparent Purple
- `jayo_pla_platransparentred_1000_175_p` — PLA Transparent Red
- `jayo_pla_platransparentyellow_1000_175_p` — PLA Transparent Yellow
- `jayo_pla_plawhite_1000_175_p` — PLA White
- `jayo_pla_playellow_1000_175_p` — PLA Yellow
- `jayo_pla_plablack_1100_175_p` — PLA Black
- `jayo_pla_plablue_1100_175_p` — PLA Blue
- `jayo_pla_placherryred_1100_175_p` — PLA Cherry Red
- `jayo_pla_plachocolate_1100_175_p` — PLA Chocolate
- `jayo_pla_placoffee_1100_175_p` — PLA Coffee
- `jayo_pla_placyan_1100_175_p` — PLA Cyan
- `jayo_pla_plafuchsia_1100_175_p` — PLA Fuchsia
- `jayo_pla_plagrassgreen_1100_175_p` — PLA Grass Green
- `jayo_pla_plagray_1100_175_p` — PLA Gray
- `jayo_pla_plagreen_1100_175_p` — PLA Green
- `jayo_pla_plalemonyellow_1100_175_p` — PLA Lemon Yellow
- `jayo_pla_plamintgreen_1100_175_p` — PLA Mint Green
- `jayo_pla_plapurple_1100_175_p` — PLA Purple
- `jayo_pla_plared_1100_175_p` — PLA Red
- `jayo_pla_plasakurapink_1100_175_p` — PLA Sakura Pink
- `jayo_pla_plasilver_1100_175_p` — PLA Silver
- `jayo_pla_plaskyblue_1100_175_p` — PLA Sky Blue
- `jayo_pla_plasunnyorange_1100_175_p` — PLA Sunny Orange
- `jayo_pla_platransparent_1100_175_p` — PLA Transparent
- `jayo_pla_platransparentblue_1100_175_p` — PLA Transparent Blue
- `jayo_pla_platransparentpurple_1100_175_p` — PLA Transparent Purple
- `jayo_pla_platransparentred_1100_175_p` — PLA Transparent Red
- `jayo_pla_platransparentyellow_1100_175_p` — PLA Transparent Yellow
- `jayo_pla_plawhite_1100_175_p` — PLA White
- `jayo_pla_playellow_1100_175_p` — PLA Yellow
- `jayo_pla_pla+black_1100_175_p` — PLA+ Black
- `jayo_pla_pla+white_1100_175_p` — PLA+ White
- `jayo_pla_silkplablack+goldmulti-color_1000_175_p` — Silk PLA Black+Gold Multi-Color
- `jayo_pla_silkplablue+greenmulti-color_1000_175_p` — Silk PLA Blue+Green Multi-Color
- `jayo_pla_silkplapink+goldmulti-color_1000_175_p` — Silk PLA Pink+Gold Multi-Color
- `jayo_pla_silkplared+goldmulti-color_1000_175_p` — Silk PLA Red+Gold Multi-Color
- `jayo_pla_silkplared+yellow+greenmulti-color_1000_175_p` — Silk PLA Red+Yellow+Green Multi-Color
