# anycubic duplicate migration review

Base `a4d9aed6ef055e4c351fe052cf9f850af0daa9a4`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `3338ecd3dbeb6d6bd9205b42f86aeddb641a8a2d1f8ac211dbcbddb373cd6b6b`.

## Authorization and result

{"groups": 36, "approved_groups": 36, "retired": 36, "deferred": 0, "hard_stops": 0, "before_count": 52037, "after_count": 52001, "brand_before": 254, "brand_after": 218, "registry_before": 1397, "registry_after": 1433, "metadata_fields_changed": 9, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

All36 Rule1 ordinary exact normalized identities pass. Retain survivor HEX/translucency/tare conflicts unresolved; no spelling ties or identifier losses. Current exact-line V3.0 TDS confirms existing scalar printing values for PLA210/60, PETG240/70, TPU220/55 and ABS260/90. Only proven incorrect PETG density1.30 is corrected to1.23 on nine targetIDs. No packaging/tare/doc guessing or additional variants.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://cdn.shopify.com/s/files/1/0698/1235/5357/files/ANYCUBIC_TDS_PLA_V3.0.pdf?v=1757585748", "family": "PLA Basic", "density": 1.24, "nozzle": [190, 230], "bed": [55, 65], "note": "Current linked V3.0 recommendation. Product-page55–56 differs; retain valid existing scalar60, not the apparent typo."}
- {"url": "https://cdn.shopify.com/s/files/1/0698/1235/5357/files/ANYCUBIC_TDS_PETG_V3.0.pdf?v=1757584046", "family": "PETG", "density": 1.23, "nozzle": [230, 250], "bed": [60, 70]}
- {"url": "https://cdn.shopify.com/s/files/1/0245/5519/2380/files/ANYCUBIC_TDS_TPU_V3.0.pdf?v=1758535420", "family": "TPU95A", "density": 1.23, "nozzle": [195, 230], "bed": [50, 60]}
- {"url": "https://cdn.shopify.com/s/files/1/0698/1235/5357/files/ANYCUBIC_TDS_ABS_V3.0.pdf?v=1757580251", "family": "ABS", "density": 1.05, "nozzle": [240, 280], "bed": [80, 100]}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`anycubic_abs_absblack_1000_175_p`|`anycubic_abs_black_1000_175_p`|`anycubic.json::ANYCUBIC::ABS {color_name}::ABS Black::ABS::1000::1.75::plastic::False`|
|`anycubic_abs_absgrey_1000_175_p`|`anycubic_abs_grey_1000_175_p`|`anycubic.json::ANYCUBIC::ABS {color_name}::ABS Grey::ABS::1000::1.75::plastic::False`|
|`anycubic_abs_abswhite_1000_175_p`|`anycubic_abs_white_1000_175_p`|`anycubic.json::ANYCUBIC::ABS {color_name}::ABS White::ABS::1000::1.75::plastic::False`|
|`anycubic_petg_petgblack_1000_175_p`|`anycubic_petg_black_1000_175_p`|`anycubic.json::ANYCUBIC::PETG {color_name}::PETG Black::PETG::1000::1.75::plastic::False`|
|`anycubic_petg_petgblue_1000_175_p`|`anycubic_petg_blue_1000_175_p`|`anycubic.json::ANYCUBIC::PETG {color_name}::PETG Blue::PETG::1000::1.75::plastic::False`|
|`anycubic_petg_petgclear_1000_175_p`|`anycubic_petg_clear_1000_175_p`|`anycubic.json::ANYCUBIC::PETG {color_name}::PETG Clear::PETG::1000::1.75::plastic::False`|
|`anycubic_petg_petggreen_1000_175_p`|`anycubic_petg_green_1000_175_p`|`anycubic.json::ANYCUBIC::PETG {color_name}::PETG Green::PETG::1000::1.75::plastic::False`|
|`anycubic_petg_petggrey_1000_175_p`|`anycubic_petg_grey_1000_175_p`|`anycubic.json::ANYCUBIC::PETG {color_name}::PETG Grey::PETG::1000::1.75::plastic::False`|
|`anycubic_petg_petgorange_1000_175_p`|`anycubic_petg_orange_1000_175_p`|`anycubic.json::ANYCUBIC::PETG {color_name}::PETG Orange::PETG::1000::1.75::plastic::False`|
|`anycubic_petg_petgpurple_1000_175_p`|`anycubic_petg_purple_1000_175_p`|`anycubic.json::ANYCUBIC::PETG {color_name}::PETG Purple::PETG::1000::1.75::plastic::False`|
|`anycubic_petg_petgwhite_1000_175_p`|`anycubic_petg_white_1000_175_p`|`anycubic.json::ANYCUBIC::PETG {color_name}::PETG White::PETG::1000::1.75::plastic::False`|
|`anycubic_petg_petgyellow_1000_175_p`|`anycubic_petg_yellow_1000_175_p`|`anycubic.json::ANYCUBIC::PETG {color_name}::PETG Yellow::PETG::1000::1.75::plastic::False`|
|`anycubic_pla_plabasicbeige_1000_175_p`|`anycubic_pla_basicbeige_1000_175_p`|`anycubic.json::ANYCUBIC::PLA Basic {color_name}::PLA Basic Beige::PLA::1000::1.75::plastic::False`|
|`anycubic_pla_plabasicblack_1000_175_p`|`anycubic_pla_basicblack_1000_175_p`|`anycubic.json::ANYCUBIC::PLA Basic {color_name}::PLA Basic Black::PLA::1000::1.75::plastic::False`|
|`anycubic_pla_plabasicbronze_1000_175_p`|`anycubic_pla_basicbronze_1000_175_p`|`anycubic.json::ANYCUBIC::PLA Basic {color_name}::PLA Basic Bronze::PLA::1000::1.75::plastic::False`|
|`anycubic_pla_plabasicbrown_1000_175_p`|`anycubic_pla_basicbrown_1000_175_p`|`anycubic.json::ANYCUBIC::PLA Basic {color_name}::PLA Basic Brown::PLA::1000::1.75::plastic::False`|
|`anycubic_pla_plabasicclear_1000_175_p`|`anycubic_pla_basicclear_1000_175_p`|`anycubic.json::ANYCUBIC::PLA Basic {color_name}::PLA Basic Clear::PLA::1000::1.75::plastic::False`|
|`anycubic_pla_plabasiccyan_1000_175_p`|`anycubic_pla_basiccyan_1000_175_p`|`anycubic.json::ANYCUBIC::PLA Basic {color_name}::PLA Basic Cyan::PLA::1000::1.75::plastic::False`|
|`anycubic_pla_plabasicdarkbrown_1000_175_p`|`anycubic_pla_basicdarkbrown_1000_175_p`|`anycubic.json::ANYCUBIC::PLA Basic {color_name}::PLA Basic Dark Brown::PLA::1000::1.75::plastic::False`|
|`anycubic_pla_plabasicgreenflash_1000_175_p`|`anycubic_pla_basicgreenflash_1000_175_p`|`anycubic.json::ANYCUBIC::PLA Basic {color_name}::PLA Basic Green Flash::PLA::1000::1.75::plastic::False`|
|`anycubic_pla_plabasicmagenta_1000_175_p`|`anycubic_pla_basicmagenta_1000_175_p`|`anycubic.json::ANYCUBIC::PLA Basic {color_name}::PLA Basic Magenta::PLA::1000::1.75::plastic::False`|
|`anycubic_pla_plabasicorange_1000_175_p`|`anycubic_pla_basicorange_1000_175_p`|`anycubic.json::ANYCUBIC::PLA Basic {color_name}::PLA Basic Orange::PLA::1000::1.75::plastic::False`|
|`anycubic_pla_plabasicpink_1000_175_p`|`anycubic_pla_basicpink_1000_175_p`|`anycubic.json::ANYCUBIC::PLA Basic {color_name}::PLA Basic Pink::PLA::1000::1.75::plastic::False`|
|`anycubic_pla_plabasicpurple_1000_175_p`|`anycubic_pla_basicpurple_1000_175_p`|`anycubic.json::ANYCUBIC::PLA Basic {color_name}::PLA Basic Purple::PLA::1000::1.75::plastic::False`|
|`anycubic_pla_plabasictexturegrey_1000_175_p`|`anycubic_pla_basictexturegrey_1000_175_p`|`anycubic.json::ANYCUBIC::PLA Basic {color_name}::PLA Basic Texture Grey::PLA::1000::1.75::plastic::False`|
|`anycubic_pla_plabasicwhite_1000_175_p`|`anycubic_pla_basicwhite_1000_175_p`|`anycubic.json::ANYCUBIC::PLA Basic {color_name}::PLA Basic White::PLA::1000::1.75::plastic::False`|
|`anycubic_pla_plabasicyellow_1000_175_p`|`anycubic_pla_basicyellow_1000_175_p`|`anycubic.json::ANYCUBIC::PLA Basic {color_name}::PLA Basic Yellow::PLA::1000::1.75::plastic::False`|
|`anycubic_tpu_tpublack_1000_175_p`|`anycubic_tpu_black_1000_175_p`|`anycubic.json::ANYCUBIC::TPU {color_name}::TPU Black::TPU::1000::1.75::plastic::False`|
|`anycubic_tpu_tpublue_1000_175_p`|`anycubic_tpu_blue_1000_175_p`|`anycubic.json::ANYCUBIC::TPU {color_name}::TPU Blue::TPU::1000::1.75::plastic::False`|
|`anycubic_tpu_tpuclear_1000_175_p`|`anycubic_tpu_clear_1000_175_p`|`anycubic.json::ANYCUBIC::TPU {color_name}::TPU Clear::TPU::1000::1.75::plastic::False`|
|`anycubic_tpu_tpugreen_1000_175_p`|`anycubic_tpu_green_1000_175_p`|`anycubic.json::ANYCUBIC::TPU {color_name}::TPU Green::TPU::1000::1.75::plastic::False`|
|`anycubic_tpu_tpugrey_1000_175_p`|`anycubic_tpu_grey_1000_175_p`|`anycubic.json::ANYCUBIC::TPU {color_name}::TPU Grey::TPU::1000::1.75::plastic::False`|
|`anycubic_tpu_tpumilkywhite_1000_175_p`|`anycubic_tpu_milkywhite_1000_175_p`|`anycubic.json::ANYCUBIC::TPU {color_name}::TPU Milky White::TPU::1000::1.75::plastic::False`|
|`anycubic_tpu_tpuorange_1000_175_p`|`anycubic_tpu_orange_1000_175_p`|`anycubic.json::ANYCUBIC::TPU {color_name}::TPU Orange::TPU::1000::1.75::plastic::False`|
|`anycubic_tpu_tpupurple_1000_175_p`|`anycubic_tpu_purple_1000_175_p`|`anycubic.json::ANYCUBIC::TPU {color_name}::TPU Purple::TPU::1000::1.75::plastic::False`|
|`anycubic_tpu_tpured_1000_175_p`|`anycubic_tpu_red_1000_175_p`|`anycubic.json::ANYCUBIC::TPU {color_name}::TPU Red::TPU::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### AC001: dup-49acbf8c26d5b29d66f2cca8b6b03ed583418e87489784df1688b05b79d113d6

Status: APPROVED; survivor `anycubic_abs_black_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_abs_absblack_1000_175_p`|`ABS {color_name}`|`Black`|{"source_file": "anycubic.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / False|
|`anycubic_abs_black_1000_175_p`|`{color_name}`|`Black`|{"source_file": "anycubic.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_abs_absblack_1000_175_p": null,
    "anycubic_abs_black_1000_175_p": 127
  },
  "color_hex": {
    "anycubic_abs_absblack_1000_175_p": "212721",
    "anycubic_abs_black_1000_175_p": "000000"
  },
  "extruder_temp": {
    "anycubic_abs_absblack_1000_175_p": 240,
    "anycubic_abs_black_1000_175_p": 260
  },
  "bed_temp": {
    "anycubic_abs_absblack_1000_175_p": 95,
    "anycubic_abs_black_1000_175_p": 90
  }
}
```

### AC002: dup-ce2067cdc226819148e00e533fb45e800cdfda8ef05a5505b612a1c5ad3546ce

Status: APPROVED; survivor `anycubic_abs_grey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_abs_absgrey_1000_175_p`|`ABS {color_name}`|`Grey`|{"source_file": "anycubic.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / False|
|`anycubic_abs_grey_1000_175_p`|`{color_name}`|`Grey`|{"source_file": "anycubic.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_abs_absgrey_1000_175_p": null,
    "anycubic_abs_grey_1000_175_p": 127
  },
  "color_hex": {
    "anycubic_abs_absgrey_1000_175_p": "A7A8AA",
    "anycubic_abs_grey_1000_175_p": "63666A"
  },
  "extruder_temp": {
    "anycubic_abs_absgrey_1000_175_p": 240,
    "anycubic_abs_grey_1000_175_p": 260
  },
  "bed_temp": {
    "anycubic_abs_absgrey_1000_175_p": 95,
    "anycubic_abs_grey_1000_175_p": 90
  }
}
```

### AC003: dup-27f9878de6e4d4052fbb0d85fe2f26dff6583a9b8f34315e09de26782c89eaf5

Status: APPROVED; survivor `anycubic_abs_white_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_abs_abswhite_1000_175_p`|`ABS {color_name}`|`White`|{"source_file": "anycubic.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / False|
|`anycubic_abs_white_1000_175_p`|`{color_name}`|`White`|{"source_file": "anycubic.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_abs_abswhite_1000_175_p": null,
    "anycubic_abs_white_1000_175_p": 127
  },
  "color_hex": {
    "anycubic_abs_abswhite_1000_175_p": "F1F0ED",
    "anycubic_abs_white_1000_175_p": "FFFFFF"
  },
  "extruder_temp": {
    "anycubic_abs_abswhite_1000_175_p": 240,
    "anycubic_abs_white_1000_175_p": 260
  },
  "bed_temp": {
    "anycubic_abs_abswhite_1000_175_p": 95,
    "anycubic_abs_white_1000_175_p": 90
  }
}
```

### AC004: dup-1cbdfe96e687357d27b7ecc6d06cba53b9bd943d514706dd88fabbaede1d5bda

Status: APPROVED; survivor `anycubic_petg_black_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_petg_black_1000_175_p`|`{color_name}`|`Black`|{"source_file": "anycubic.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|
|`anycubic_petg_petgblack_1000_175_p`|`PETG {color_name}`|`Black`|{"source_file": "anycubic.json", "definition_index": 12, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "anycubic_petg_black_1000_175_p": 1.3,
    "anycubic_petg_petgblack_1000_175_p": 1.23
  },
  "spool_weight": {
    "anycubic_petg_black_1000_175_p": 127,
    "anycubic_petg_petgblack_1000_175_p": null
  },
  "color_hex": {
    "anycubic_petg_black_1000_175_p": "000000",
    "anycubic_petg_petgblack_1000_175_p": "212721"
  },
  "extruder_temp": {
    "anycubic_petg_black_1000_175_p": 240,
    "anycubic_petg_petgblack_1000_175_p": 235
  },
  "bed_temp": {
    "anycubic_petg_black_1000_175_p": 70,
    "anycubic_petg_petgblack_1000_175_p": 80
  }
}
```

### AC005: dup-4a60e6e4d2b6d13b45de29981b5e2a7dfd8f56d90f59335c430103eb898d8979

Status: APPROVED; survivor `anycubic_petg_blue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_petg_blue_1000_175_p`|`{color_name}`|`Blue`|{"source_file": "anycubic.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|
|`anycubic_petg_petgblue_1000_175_p`|`PETG {color_name}`|`Blue`|{"source_file": "anycubic.json", "definition_index": 12, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "anycubic_petg_blue_1000_175_p": 1.3,
    "anycubic_petg_petgblue_1000_175_p": 1.23
  },
  "spool_weight": {
    "anycubic_petg_blue_1000_175_p": 127,
    "anycubic_petg_petgblue_1000_175_p": null
  },
  "color_hex": {
    "anycubic_petg_blue_1000_175_p": "0762C8",
    "anycubic_petg_petgblue_1000_175_p": "003594"
  },
  "extruder_temp": {
    "anycubic_petg_blue_1000_175_p": 240,
    "anycubic_petg_petgblue_1000_175_p": 235
  },
  "bed_temp": {
    "anycubic_petg_blue_1000_175_p": 70,
    "anycubic_petg_petgblue_1000_175_p": 80
  }
}
```

### AC006: dup-aa55dce6ea85b4582ed6e2a8ebcb1f774afd1757f66d5fd9ab1de3e0017b2f42

Status: APPROVED; survivor `anycubic_petg_clear_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_petg_clear_1000_175_p`|`{color_name}`|`Clear`|{"source_file": "anycubic.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|
|`anycubic_petg_petgclear_1000_175_p`|`PETG {color_name}`|`Clear`|{"source_file": "anycubic.json", "definition_index": 12, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "anycubic_petg_clear_1000_175_p": 1.3,
    "anycubic_petg_petgclear_1000_175_p": 1.23
  },
  "spool_weight": {
    "anycubic_petg_clear_1000_175_p": 127,
    "anycubic_petg_petgclear_1000_175_p": null
  },
  "color_hex": {
    "anycubic_petg_clear_1000_175_p": "00FFFFFF",
    "anycubic_petg_petgclear_1000_175_p": "FFFFFF"
  },
  "extruder_temp": {
    "anycubic_petg_clear_1000_175_p": 240,
    "anycubic_petg_petgclear_1000_175_p": 235
  },
  "bed_temp": {
    "anycubic_petg_clear_1000_175_p": 70,
    "anycubic_petg_petgclear_1000_175_p": 80
  },
  "translucent": {
    "anycubic_petg_clear_1000_175_p": true,
    "anycubic_petg_petgclear_1000_175_p": false
  }
}
```

### AC007: dup-404c456b14c993a5db938597669e40b22a80a3b037c4d147a3e1fb34e529c626

Status: APPROVED; survivor `anycubic_petg_green_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_petg_green_1000_175_p`|`{color_name}`|`Green`|{"source_file": "anycubic.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|
|`anycubic_petg_petggreen_1000_175_p`|`PETG {color_name}`|`Green`|{"source_file": "anycubic.json", "definition_index": 12, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "anycubic_petg_green_1000_175_p": 1.3,
    "anycubic_petg_petggreen_1000_175_p": 1.23
  },
  "spool_weight": {
    "anycubic_petg_green_1000_175_p": 127,
    "anycubic_petg_petggreen_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_petg_green_1000_175_p": 240,
    "anycubic_petg_petggreen_1000_175_p": 235
  },
  "bed_temp": {
    "anycubic_petg_green_1000_175_p": 70,
    "anycubic_petg_petggreen_1000_175_p": 80
  }
}
```

### AC008: dup-05b336109b6b5e3fc3176ddc0c959ee5e6c705135902a626c7181a44bd3fdf3e

Status: APPROVED; survivor `anycubic_petg_grey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_petg_grey_1000_175_p`|`{color_name}`|`Grey`|{"source_file": "anycubic.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|
|`anycubic_petg_petggrey_1000_175_p`|`PETG {color_name}`|`Grey`|{"source_file": "anycubic.json", "definition_index": 12, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "anycubic_petg_grey_1000_175_p": 1.3,
    "anycubic_petg_petggrey_1000_175_p": 1.23
  },
  "spool_weight": {
    "anycubic_petg_grey_1000_175_p": 127,
    "anycubic_petg_petggrey_1000_175_p": null
  },
  "color_hex": {
    "anycubic_petg_grey_1000_175_p": "B1B3B3",
    "anycubic_petg_petggrey_1000_175_p": "97999B"
  },
  "extruder_temp": {
    "anycubic_petg_grey_1000_175_p": 240,
    "anycubic_petg_petggrey_1000_175_p": 235
  },
  "bed_temp": {
    "anycubic_petg_grey_1000_175_p": 70,
    "anycubic_petg_petggrey_1000_175_p": 80
  }
}
```

### AC009: dup-6c7d5c3c0e05515fa2878b58edbf1774e5e65e85d74d97e071c221b604d1f9e4

Status: APPROVED; survivor `anycubic_petg_orange_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_petg_orange_1000_175_p`|`{color_name}`|`Orange`|{"source_file": "anycubic.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|
|`anycubic_petg_petgorange_1000_175_p`|`PETG {color_name}`|`Orange`|{"source_file": "anycubic.json", "definition_index": 12, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "anycubic_petg_orange_1000_175_p": 1.3,
    "anycubic_petg_petgorange_1000_175_p": 1.23
  },
  "spool_weight": {
    "anycubic_petg_orange_1000_175_p": 127,
    "anycubic_petg_petgorange_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_petg_orange_1000_175_p": 240,
    "anycubic_petg_petgorange_1000_175_p": 235
  },
  "bed_temp": {
    "anycubic_petg_orange_1000_175_p": 70,
    "anycubic_petg_petgorange_1000_175_p": 80
  }
}
```

### AC010: dup-0382e1c5f109644aa4d85d895722bb52b44ea61374b84964884c3ffaea75a1b6

Status: APPROVED; survivor `anycubic_petg_purple_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_petg_petgpurple_1000_175_p`|`PETG {color_name}`|`Purple`|{"source_file": "anycubic.json", "definition_index": 12, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|
|`anycubic_petg_purple_1000_175_p`|`{color_name}`|`Purple`|{"source_file": "anycubic.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "anycubic_petg_petgpurple_1000_175_p": 1.23,
    "anycubic_petg_purple_1000_175_p": 1.3
  },
  "spool_weight": {
    "anycubic_petg_petgpurple_1000_175_p": null,
    "anycubic_petg_purple_1000_175_p": 127
  },
  "extruder_temp": {
    "anycubic_petg_petgpurple_1000_175_p": 235,
    "anycubic_petg_purple_1000_175_p": 240
  },
  "bed_temp": {
    "anycubic_petg_petgpurple_1000_175_p": 80,
    "anycubic_petg_purple_1000_175_p": 70
  }
}
```

### AC011: dup-0d11bbb9d9d6a5dd0b2bb6275a0b5f34f18475f2ac6d56bc154fdff810b5c898

Status: APPROVED; survivor `anycubic_petg_white_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_petg_petgwhite_1000_175_p`|`PETG {color_name}`|`White`|{"source_file": "anycubic.json", "definition_index": 12, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|
|`anycubic_petg_white_1000_175_p`|`{color_name}`|`White`|{"source_file": "anycubic.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "anycubic_petg_petgwhite_1000_175_p": 1.23,
    "anycubic_petg_white_1000_175_p": 1.3
  },
  "spool_weight": {
    "anycubic_petg_petgwhite_1000_175_p": null,
    "anycubic_petg_white_1000_175_p": 127
  },
  "color_hex": {
    "anycubic_petg_petgwhite_1000_175_p": "EFF0F1",
    "anycubic_petg_white_1000_175_p": "FFFFFF"
  },
  "extruder_temp": {
    "anycubic_petg_petgwhite_1000_175_p": 235,
    "anycubic_petg_white_1000_175_p": 240
  },
  "bed_temp": {
    "anycubic_petg_petgwhite_1000_175_p": 80,
    "anycubic_petg_white_1000_175_p": 70
  }
}
```

### AC012: dup-3a48228f2b13ecd2fd49479868992193657b3429787d50eda5069f6c3d4ec33d

Status: APPROVED; survivor `anycubic_petg_yellow_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_petg_petgyellow_1000_175_p`|`PETG {color_name}`|`Yellow`|{"source_file": "anycubic.json", "definition_index": 12, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|
|`anycubic_petg_yellow_1000_175_p`|`{color_name}`|`Yellow`|{"source_file": "anycubic.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "anycubic_petg_petgyellow_1000_175_p": 1.23,
    "anycubic_petg_yellow_1000_175_p": 1.3
  },
  "spool_weight": {
    "anycubic_petg_petgyellow_1000_175_p": null,
    "anycubic_petg_yellow_1000_175_p": 127
  },
  "extruder_temp": {
    "anycubic_petg_petgyellow_1000_175_p": 235,
    "anycubic_petg_yellow_1000_175_p": 240
  },
  "bed_temp": {
    "anycubic_petg_petgyellow_1000_175_p": 80,
    "anycubic_petg_yellow_1000_175_p": 70
  }
}
```

### AC013: dup-15027301e451eafa7f76049efab907c997a45c6cf8fc1f978874e0a7bf69333b

Status: APPROVED; survivor `anycubic_pla_basicbeige_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_pla_basicbeige_1000_175_p`|`Basic {color_name}`|`Beige`|{"source_file": "anycubic.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`anycubic_pla_plabasicbeige_1000_175_p`|`PLA Basic {color_name}`|`Beige`|{"source_file": "anycubic.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 19, "compiled_records": 19} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_pla_basicbeige_1000_175_p": 127,
    "anycubic_pla_plabasicbeige_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_pla_basicbeige_1000_175_p": 210,
    "anycubic_pla_plabasicbeige_1000_175_p": 205
  },
  "bed_temp": {
    "anycubic_pla_basicbeige_1000_175_p": 60,
    "anycubic_pla_plabasicbeige_1000_175_p": 30
  }
}
```

### AC014: dup-1acbfe3aa4a7a08369066fb3cebf0f1253147ff7ec762b1ca94a231a0cc0f82b

Status: APPROVED; survivor `anycubic_pla_basicblack_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_pla_basicblack_1000_175_p`|`Basic {color_name}`|`Black`|{"source_file": "anycubic.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`anycubic_pla_plabasicblack_1000_175_p`|`PLA Basic {color_name}`|`Black`|{"source_file": "anycubic.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 19, "compiled_records": 19} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_pla_basicblack_1000_175_p": 127,
    "anycubic_pla_plabasicblack_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_pla_basicblack_1000_175_p": 210,
    "anycubic_pla_plabasicblack_1000_175_p": 205
  },
  "bed_temp": {
    "anycubic_pla_basicblack_1000_175_p": 60,
    "anycubic_pla_plabasicblack_1000_175_p": 30
  }
}
```

### AC015: dup-753ca62a3ad0d306b022aedfcdcaedd3568b2a4ac0d1d7345b6bcb0f382e3fa4

Status: APPROVED; survivor `anycubic_pla_basicbronze_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_pla_basicbronze_1000_175_p`|`Basic {color_name}`|`Bronze`|{"source_file": "anycubic.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`anycubic_pla_plabasicbronze_1000_175_p`|`PLA Basic {color_name}`|`Bronze`|{"source_file": "anycubic.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 19, "compiled_records": 19} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_pla_basicbronze_1000_175_p": 127,
    "anycubic_pla_plabasicbronze_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_pla_basicbronze_1000_175_p": 210,
    "anycubic_pla_plabasicbronze_1000_175_p": 205
  },
  "bed_temp": {
    "anycubic_pla_basicbronze_1000_175_p": 60,
    "anycubic_pla_plabasicbronze_1000_175_p": 30
  }
}
```

### AC016: dup-ac4c01b2829be123c7fdfcd3b705da793effb64aef0da605982cb13d55c6c9c6

Status: APPROVED; survivor `anycubic_pla_basicbrown_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_pla_basicbrown_1000_175_p`|`Basic {color_name}`|`Brown`|{"source_file": "anycubic.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`anycubic_pla_plabasicbrown_1000_175_p`|`PLA Basic {color_name}`|`Brown`|{"source_file": "anycubic.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 19, "compiled_records": 19} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_pla_basicbrown_1000_175_p": 127,
    "anycubic_pla_plabasicbrown_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_pla_basicbrown_1000_175_p": 210,
    "anycubic_pla_plabasicbrown_1000_175_p": 205
  },
  "bed_temp": {
    "anycubic_pla_basicbrown_1000_175_p": 60,
    "anycubic_pla_plabasicbrown_1000_175_p": 30
  }
}
```

### AC017: dup-71a67a404d5d32bdcdcd2227af77bfd40af15ef79c79321cf6ce657075794c78

Status: APPROVED; survivor `anycubic_pla_basicclear_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_pla_basicclear_1000_175_p`|`Basic {color_name}`|`Clear`|{"source_file": "anycubic.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`anycubic_pla_plabasicclear_1000_175_p`|`PLA Basic {color_name}`|`Clear`|{"source_file": "anycubic.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 19, "compiled_records": 19} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_pla_basicclear_1000_175_p": 127,
    "anycubic_pla_plabasicclear_1000_175_p": null
  },
  "color_hex": {
    "anycubic_pla_basicclear_1000_175_p": "00FFFFFF",
    "anycubic_pla_plabasicclear_1000_175_p": "FFFFFF"
  },
  "extruder_temp": {
    "anycubic_pla_basicclear_1000_175_p": 210,
    "anycubic_pla_plabasicclear_1000_175_p": 205
  },
  "bed_temp": {
    "anycubic_pla_basicclear_1000_175_p": 60,
    "anycubic_pla_plabasicclear_1000_175_p": 30
  }
}
```

### AC018: dup-bd474bc0f39534e0586121fd1199a772a6cebcaf2dc08bc7c4c7616a9e6385b3

Status: APPROVED; survivor `anycubic_pla_basiccyan_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_pla_basiccyan_1000_175_p`|`Basic {color_name}`|`Cyan`|{"source_file": "anycubic.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`anycubic_pla_plabasiccyan_1000_175_p`|`PLA Basic {color_name}`|`Cyan`|{"source_file": "anycubic.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 19, "compiled_records": 19} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_pla_basiccyan_1000_175_p": 127,
    "anycubic_pla_plabasiccyan_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_pla_basiccyan_1000_175_p": 210,
    "anycubic_pla_plabasiccyan_1000_175_p": 205
  },
  "bed_temp": {
    "anycubic_pla_basiccyan_1000_175_p": 60,
    "anycubic_pla_plabasiccyan_1000_175_p": 30
  }
}
```

### AC019: dup-626323cfad26fe8e9212b1dfe16bd4c8971d53ee415e626e02f5ba6954779bed

Status: APPROVED; survivor `anycubic_pla_basicdarkbrown_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_pla_basicdarkbrown_1000_175_p`|`Basic {color_name}`|`Dark Brown`|{"source_file": "anycubic.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`anycubic_pla_plabasicdarkbrown_1000_175_p`|`PLA Basic {color_name}`|`Dark Brown`|{"source_file": "anycubic.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 19, "compiled_records": 19} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_pla_basicdarkbrown_1000_175_p": 127,
    "anycubic_pla_plabasicdarkbrown_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_pla_basicdarkbrown_1000_175_p": 210,
    "anycubic_pla_plabasicdarkbrown_1000_175_p": 205
  },
  "bed_temp": {
    "anycubic_pla_basicdarkbrown_1000_175_p": 60,
    "anycubic_pla_plabasicdarkbrown_1000_175_p": 30
  }
}
```

### AC020: dup-eb76f90e971cd08dc0db85870aeacf0558929eb1c385f261e1dc6bc0ebe2c038

Status: APPROVED; survivor `anycubic_pla_basicgreenflash_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_pla_basicgreenflash_1000_175_p`|`Basic {color_name}`|`Green Flash`|{"source_file": "anycubic.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`anycubic_pla_plabasicgreenflash_1000_175_p`|`PLA Basic {color_name}`|`Green Flash`|{"source_file": "anycubic.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 19, "compiled_records": 19} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_pla_basicgreenflash_1000_175_p": 127,
    "anycubic_pla_plabasicgreenflash_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_pla_basicgreenflash_1000_175_p": 210,
    "anycubic_pla_plabasicgreenflash_1000_175_p": 205
  },
  "bed_temp": {
    "anycubic_pla_basicgreenflash_1000_175_p": 60,
    "anycubic_pla_plabasicgreenflash_1000_175_p": 30
  }
}
```

### AC021: dup-f9c55dbc2dccd65f6092acc45fb33969a09596cb44d0c0c1f283bebedb4c20f3

Status: APPROVED; survivor `anycubic_pla_basicmagenta_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_pla_basicmagenta_1000_175_p`|`Basic {color_name}`|`Magenta`|{"source_file": "anycubic.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`anycubic_pla_plabasicmagenta_1000_175_p`|`PLA Basic {color_name}`|`Magenta`|{"source_file": "anycubic.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 19, "compiled_records": 19} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_pla_basicmagenta_1000_175_p": 127,
    "anycubic_pla_plabasicmagenta_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_pla_basicmagenta_1000_175_p": 210,
    "anycubic_pla_plabasicmagenta_1000_175_p": 205
  },
  "bed_temp": {
    "anycubic_pla_basicmagenta_1000_175_p": 60,
    "anycubic_pla_plabasicmagenta_1000_175_p": 30
  }
}
```

### AC022: dup-d6cc2be98c7cc9335a1806e5aa2979f544406081e7365197f411bb2f709591ba

Status: APPROVED; survivor `anycubic_pla_basicorange_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_pla_basicorange_1000_175_p`|`Basic {color_name}`|`Orange`|{"source_file": "anycubic.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`anycubic_pla_plabasicorange_1000_175_p`|`PLA Basic {color_name}`|`Orange`|{"source_file": "anycubic.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 19, "compiled_records": 19} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_pla_basicorange_1000_175_p": 127,
    "anycubic_pla_plabasicorange_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_pla_basicorange_1000_175_p": 210,
    "anycubic_pla_plabasicorange_1000_175_p": 205
  },
  "bed_temp": {
    "anycubic_pla_basicorange_1000_175_p": 60,
    "anycubic_pla_plabasicorange_1000_175_p": 30
  }
}
```

### AC023: dup-1922438ef3fecadc15b5db74ebeb95b37def3d5ceb75e7855f30c63522f1a328

Status: APPROVED; survivor `anycubic_pla_basicpink_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_pla_basicpink_1000_175_p`|`Basic {color_name}`|`Pink`|{"source_file": "anycubic.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`anycubic_pla_plabasicpink_1000_175_p`|`PLA Basic {color_name}`|`Pink`|{"source_file": "anycubic.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 19, "compiled_records": 19} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_pla_basicpink_1000_175_p": 127,
    "anycubic_pla_plabasicpink_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_pla_basicpink_1000_175_p": 210,
    "anycubic_pla_plabasicpink_1000_175_p": 205
  },
  "bed_temp": {
    "anycubic_pla_basicpink_1000_175_p": 60,
    "anycubic_pla_plabasicpink_1000_175_p": 30
  }
}
```

### AC024: dup-7691b327ddbdf03e4169ded25a582ffd3303afe851fc2f0645fe3ac9cc4375c2

Status: APPROVED; survivor `anycubic_pla_basicpurple_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_pla_basicpurple_1000_175_p`|`Basic {color_name}`|`Purple`|{"source_file": "anycubic.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`anycubic_pla_plabasicpurple_1000_175_p`|`PLA Basic {color_name}`|`Purple`|{"source_file": "anycubic.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 19, "compiled_records": 19} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_pla_basicpurple_1000_175_p": 127,
    "anycubic_pla_plabasicpurple_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_pla_basicpurple_1000_175_p": 210,
    "anycubic_pla_plabasicpurple_1000_175_p": 205
  },
  "bed_temp": {
    "anycubic_pla_basicpurple_1000_175_p": 60,
    "anycubic_pla_plabasicpurple_1000_175_p": 30
  }
}
```

### AC025: dup-73e98363a5e57b791d3db20812decc74272550e093a5bf50cf4fadf056a99b4f

Status: APPROVED; survivor `anycubic_pla_basictexturegrey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_pla_basictexturegrey_1000_175_p`|`Basic {color_name}`|`Texture Grey`|{"source_file": "anycubic.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`anycubic_pla_plabasictexturegrey_1000_175_p`|`PLA Basic {color_name}`|`Texture Grey`|{"source_file": "anycubic.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 19, "compiled_records": 19} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_pla_basictexturegrey_1000_175_p": 127,
    "anycubic_pla_plabasictexturegrey_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_pla_basictexturegrey_1000_175_p": 210,
    "anycubic_pla_plabasictexturegrey_1000_175_p": 205
  },
  "bed_temp": {
    "anycubic_pla_basictexturegrey_1000_175_p": 60,
    "anycubic_pla_plabasictexturegrey_1000_175_p": 30
  }
}
```

### AC026: dup-4cd3e56237c34bf202cf2ff4920887d521064c5263b169d90f10cdb7dba83071

Status: APPROVED; survivor `anycubic_pla_basicwhite_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_pla_basicwhite_1000_175_p`|`Basic {color_name}`|`White`|{"source_file": "anycubic.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`anycubic_pla_plabasicwhite_1000_175_p`|`PLA Basic {color_name}`|`White`|{"source_file": "anycubic.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 19, "compiled_records": 19} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_pla_basicwhite_1000_175_p": 127,
    "anycubic_pla_plabasicwhite_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_pla_basicwhite_1000_175_p": 210,
    "anycubic_pla_plabasicwhite_1000_175_p": 205
  },
  "bed_temp": {
    "anycubic_pla_basicwhite_1000_175_p": 60,
    "anycubic_pla_plabasicwhite_1000_175_p": 30
  }
}
```

### AC027: dup-f66f190a5aa2c4710ef9274c4393610d03b0a1901c2cb982c5d3736f9bc77485

Status: APPROVED; survivor `anycubic_pla_basicyellow_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_pla_basicyellow_1000_175_p`|`Basic {color_name}`|`Yellow`|{"source_file": "anycubic.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`anycubic_pla_plabasicyellow_1000_175_p`|`PLA Basic {color_name}`|`Yellow`|{"source_file": "anycubic.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 19, "compiled_records": 19} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_pla_basicyellow_1000_175_p": 127,
    "anycubic_pla_plabasicyellow_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_pla_basicyellow_1000_175_p": 210,
    "anycubic_pla_plabasicyellow_1000_175_p": 205
  },
  "bed_temp": {
    "anycubic_pla_basicyellow_1000_175_p": 60,
    "anycubic_pla_plabasicyellow_1000_175_p": 30
  }
}
```

### AC028: dup-3bc05ef72e47b626384aa36e0f4304f6c0b3d30b20a1866809666e4c38af80c2

Status: APPROVED; survivor `anycubic_tpu_black_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_tpu_black_1000_175_p`|`{color_name}`|`Black`|{"source_file": "anycubic.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`anycubic_tpu_tpublack_1000_175_p`|`TPU {color_name}`|`Black`|{"source_file": "anycubic.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_tpu_black_1000_175_p": 127,
    "anycubic_tpu_tpublack_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_tpu_black_1000_175_p": 220,
    "anycubic_tpu_tpublack_1000_175_p": 225
  },
  "bed_temp": {
    "anycubic_tpu_black_1000_175_p": 55,
    "anycubic_tpu_tpublack_1000_175_p": 60
  }
}
```

### AC029: dup-2bc864deeb241204adf672f815994c336b18ff693cab2b7920dda47033e96be0

Status: APPROVED; survivor `anycubic_tpu_blue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_tpu_blue_1000_175_p`|`{color_name}`|`Blue`|{"source_file": "anycubic.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`anycubic_tpu_tpublue_1000_175_p`|`TPU {color_name}`|`Blue`|{"source_file": "anycubic.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_tpu_blue_1000_175_p": 127,
    "anycubic_tpu_tpublue_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_tpu_blue_1000_175_p": 220,
    "anycubic_tpu_tpublue_1000_175_p": 225
  },
  "bed_temp": {
    "anycubic_tpu_blue_1000_175_p": 55,
    "anycubic_tpu_tpublue_1000_175_p": 60
  }
}
```

### AC030: dup-a9c505940476644d11df4393fd8e9e28d3aac623b59b9024e9438d8e7df228ba

Status: APPROVED; survivor `anycubic_tpu_clear_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_tpu_clear_1000_175_p`|`{color_name}`|`Clear`|{"source_file": "anycubic.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`anycubic_tpu_tpuclear_1000_175_p`|`TPU {color_name}`|`Clear`|{"source_file": "anycubic.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_tpu_clear_1000_175_p": 127,
    "anycubic_tpu_tpuclear_1000_175_p": null
  },
  "color_hex": {
    "anycubic_tpu_clear_1000_175_p": "00FFFFFF",
    "anycubic_tpu_tpuclear_1000_175_p": "FFFFFF"
  },
  "extruder_temp": {
    "anycubic_tpu_clear_1000_175_p": 220,
    "anycubic_tpu_tpuclear_1000_175_p": 225
  },
  "bed_temp": {
    "anycubic_tpu_clear_1000_175_p": 55,
    "anycubic_tpu_tpuclear_1000_175_p": 60
  },
  "translucent": {
    "anycubic_tpu_clear_1000_175_p": true,
    "anycubic_tpu_tpuclear_1000_175_p": false
  }
}
```

### AC031: dup-4231b8a3e6126c5c486af84b502e6eb59c1f9f2e1940a3bad5b63642783ec1c7

Status: APPROVED; survivor `anycubic_tpu_green_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_tpu_green_1000_175_p`|`{color_name}`|`Green`|{"source_file": "anycubic.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`anycubic_tpu_tpugreen_1000_175_p`|`TPU {color_name}`|`Green`|{"source_file": "anycubic.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_tpu_green_1000_175_p": 127,
    "anycubic_tpu_tpugreen_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_tpu_green_1000_175_p": 220,
    "anycubic_tpu_tpugreen_1000_175_p": 225
  },
  "bed_temp": {
    "anycubic_tpu_green_1000_175_p": 55,
    "anycubic_tpu_tpugreen_1000_175_p": 60
  }
}
```

### AC032: dup-b85479792273729a22c9ba4c3a1bd5b9a1f2cf9ee91b9f685c13bfbfce36a721

Status: APPROVED; survivor `anycubic_tpu_grey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_tpu_grey_1000_175_p`|`{color_name}`|`Grey`|{"source_file": "anycubic.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`anycubic_tpu_tpugrey_1000_175_p`|`TPU {color_name}`|`Grey`|{"source_file": "anycubic.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_tpu_grey_1000_175_p": 127,
    "anycubic_tpu_tpugrey_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_tpu_grey_1000_175_p": 220,
    "anycubic_tpu_tpugrey_1000_175_p": 225
  },
  "bed_temp": {
    "anycubic_tpu_grey_1000_175_p": 55,
    "anycubic_tpu_tpugrey_1000_175_p": 60
  }
}
```

### AC033: dup-87d5154478fa4c3f2af59460c27e13d899f694183feacc5aa7b49a0c033fddae

Status: APPROVED; survivor `anycubic_tpu_milkywhite_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_tpu_milkywhite_1000_175_p`|`{color_name}`|`Milky White`|{"source_file": "anycubic.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`anycubic_tpu_tpumilkywhite_1000_175_p`|`TPU {color_name}`|`Milky White`|{"source_file": "anycubic.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_tpu_milkywhite_1000_175_p": 127,
    "anycubic_tpu_tpumilkywhite_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_tpu_milkywhite_1000_175_p": 220,
    "anycubic_tpu_tpumilkywhite_1000_175_p": 225
  },
  "bed_temp": {
    "anycubic_tpu_milkywhite_1000_175_p": 55,
    "anycubic_tpu_tpumilkywhite_1000_175_p": 60
  }
}
```

### AC034: dup-309e1239a2099795dfb4b767f333d54399cc826485d44ceac03891a5654835f8

Status: APPROVED; survivor `anycubic_tpu_orange_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_tpu_orange_1000_175_p`|`{color_name}`|`Orange`|{"source_file": "anycubic.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`anycubic_tpu_tpuorange_1000_175_p`|`TPU {color_name}`|`Orange`|{"source_file": "anycubic.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_tpu_orange_1000_175_p": 127,
    "anycubic_tpu_tpuorange_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_tpu_orange_1000_175_p": 220,
    "anycubic_tpu_tpuorange_1000_175_p": 225
  },
  "bed_temp": {
    "anycubic_tpu_orange_1000_175_p": 55,
    "anycubic_tpu_tpuorange_1000_175_p": 60
  }
}
```

### AC035: dup-517350b086bc7d4048b2d05ea8a2296b41f5f3df80d42fbce2b7b31721d169f0

Status: APPROVED; survivor `anycubic_tpu_purple_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_tpu_purple_1000_175_p`|`{color_name}`|`Purple`|{"source_file": "anycubic.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`anycubic_tpu_tpupurple_1000_175_p`|`TPU {color_name}`|`Purple`|{"source_file": "anycubic.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_tpu_purple_1000_175_p": 127,
    "anycubic_tpu_tpupurple_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_tpu_purple_1000_175_p": 220,
    "anycubic_tpu_tpupurple_1000_175_p": 225
  },
  "bed_temp": {
    "anycubic_tpu_purple_1000_175_p": 55,
    "anycubic_tpu_tpupurple_1000_175_p": 60
  }
}
```

### AC036: dup-3b9fc402fbecaa56567631ac92bb4a45ff688da49fbc01082650baaf62030a6d

Status: APPROVED; survivor `anycubic_tpu_red_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`anycubic_tpu_red_1000_175_p`|`{color_name}`|`Red`|{"source_file": "anycubic.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|
|`anycubic_tpu_tpured_1000_175_p`|`TPU {color_name}`|`Red`|{"source_file": "anycubic.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "anycubic_tpu_red_1000_175_p": 127,
    "anycubic_tpu_tpured_1000_175_p": null
  },
  "extruder_temp": {
    "anycubic_tpu_red_1000_175_p": 220,
    "anycubic_tpu_tpured_1000_175_p": 225
  },
  "bed_temp": {
    "anycubic_tpu_red_1000_175_p": 55,
    "anycubic_tpu_tpured_1000_175_p": 60
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "anycubic_petg_purple_1000_175_p",
      "values": {
        "density": 1.23
      },
      "source": "https://cdn.shopify.com/s/files/1/0698/1235/5357/files/ANYCUBIC_TDS_PETG_V3.0.pdf?v=1757584046",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "anycubic_petg_grey_1000_175_p",
      "values": {
        "density": 1.23
      },
      "source": "https://cdn.shopify.com/s/files/1/0698/1235/5357/files/ANYCUBIC_TDS_PETG_V3.0.pdf?v=1757584046",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "anycubic_petg_white_1000_175_p",
      "values": {
        "density": 1.23
      },
      "source": "https://cdn.shopify.com/s/files/1/0698/1235/5357/files/ANYCUBIC_TDS_PETG_V3.0.pdf?v=1757584046",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "anycubic_petg_black_1000_175_p",
      "values": {
        "density": 1.23
      },
      "source": "https://cdn.shopify.com/s/files/1/0698/1235/5357/files/ANYCUBIC_TDS_PETG_V3.0.pdf?v=1757584046",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "anycubic_petg_yellow_1000_175_p",
      "values": {
        "density": 1.23
      },
      "source": "https://cdn.shopify.com/s/files/1/0698/1235/5357/files/ANYCUBIC_TDS_PETG_V3.0.pdf?v=1757584046",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "anycubic_petg_green_1000_175_p",
      "values": {
        "density": 1.23
      },
      "source": "https://cdn.shopify.com/s/files/1/0698/1235/5357/files/ANYCUBIC_TDS_PETG_V3.0.pdf?v=1757584046",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "anycubic_petg_blue_1000_175_p",
      "values": {
        "density": 1.23
      },
      "source": "https://cdn.shopify.com/s/files/1/0698/1235/5357/files/ANYCUBIC_TDS_PETG_V3.0.pdf?v=1757584046",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "anycubic_petg_orange_1000_175_p",
      "values": {
        "density": 1.23
      },
      "source": "https://cdn.shopify.com/s/files/1/0698/1235/5357/files/ANYCUBIC_TDS_PETG_V3.0.pdf?v=1757584046",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "anycubic_petg_clear_1000_175_p",
      "values": {
        "density": 1.23
      },
      "source": "https://cdn.shopify.com/s/files/1/0698/1235/5357/files/ANYCUBIC_TDS_PETG_V3.0.pdf?v=1757584046",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    }
  ],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `anycubic_pla_black_1000_175_c` — Black
- `anycubic_pla_glowyellow_1000_175_p` — Glow Yellow
- `anycubic_pla_glowgreen_1000_175_p` — Glow Green
- `anycubic_pla_glowblue_1000_175_p` — Glow Blue
- `anycubic_pla_mattegrey_1000_175_c` — Matte Grey
- `anycubic_pla_matteblack_1000_175_c` — Matte Black
- `anycubic_pla_mattewhite_1000_175_c` — Matte White
- `anycubic_pla_matteyellow_1000_175_c` — Matte Yellow
- `anycubic_pla_matteblue_1000_175_c` — Matte Blue
- `anycubic_pla_mattegreen-brown_1000_175_c` — Matte Green-Brown
- `anycubic_pla_mattegreen_1000_175_c` — Matte Green
- `anycubic_pla_matteiceblue_1000_175_c` — Matte Ice Blue
- `anycubic_pla_matteorange_1000_175_c` — Matte Orange
- `anycubic_pla_mattepurple_1000_175_c` — Matte Purple
- `anycubic_pla_mattered-blue_1000_175_c` — Matte Red-Blue
- `anycubic_pla_mattered_1000_175_c` — Matte Red
- `anycubic_pla_mattesakurapink_1000_175_c` — Matte Sakura Pink
- `anycubic_pla_basicgrey_1000_175_p` — Basic Grey
- `anycubic_pla_basicred_1000_175_p` — Basic Red
- `anycubic_pla_basicblue(navyblue)_1000_175_p` — Basic Blue (Navy Blue)
- `anycubic_pla_basicgreen_1000_175_p` — Basic Green
- `anycubic_pla_basictexturesilver_1000_175_p` — Basic Texture Silver
- `anycubic_pla+_black_1000_175_p` — Black
- `anycubic_pla+_grey_1000_175_p` — Grey
- `anycubic_pla+_white_1000_175_p` — White
- `anycubic_pla+_red_1000_175_p` — Red
- `anycubic_pla+_orange_1000_175_p` — Orange
- `anycubic_pla+_purple_1000_175_p` — Purple
- `anycubic_pla+_blue_1000_175_p` — Blue
- `anycubic_pla+_green_1000_175_p` — Green
- `anycubic_pla+_yellow_1000_175_p` — Yellow
- `anycubic_pla+_silver_1000_175_p` — Silver
- `anycubic_pla+_lightblue_1000_175_p` — Light Blue
- `anycubic_pla_highspeedblack_1000_175_c` — High Speed Black
- `anycubic_pla_highspeedgrey_1000_175_c` — High Speed Grey
- `anycubic_pla_highspeedwhite_1000_175_c` — High Speed White
- `anycubic_pla_highspeedred_1000_175_c` — High Speed Red
- `anycubic_pla_highspeedorange_1000_175_c` — High Speed Orange
- `anycubic_pla_highspeedblue_1000_175_c` — High Speed Blue
- `anycubic_pla_highspeedgreen_1000_175_c` — High Speed Green
- `anycubic_pla_metalblack_1000_175_p` — Metal Black
- `anycubic_pla_metalblue_1000_175_p` — Metal Blue
- `anycubic_pla_metalcopper_1000_175_p` — Metal Copper
- `anycubic_pla_metalchampagne_1000_175_p` — Metal Champagne
- `anycubic_tpu_white_1000_175_p` — White
- `anycubic_asa_asaarmygreen_1000_175_p` — ASA Army Green
- `anycubic_asa_asablack_1000_175_p` — ASA Black
- `anycubic_asa_asablue_1000_175_p` — ASA Blue
- `anycubic_asa_asagrey_1000_175_p` — ASA Grey
- `anycubic_asa_asared_1000_175_p` — ASA Red
- `anycubic_asa_asawhite_1000_175_p` — ASA White
- `anycubic_petg_petgbeige_1000_175_p` — PETG Beige
- `anycubic_petg_petgbrown_1000_175_p` — PETG Brown
- `anycubic_petg_petgcream_1000_175_p` — PETG Cream
- `anycubic_petg_petgdarkgrey_1000_175_p` — PETG Dark Grey
- `anycubic_petg_petgforestgreen_1000_175_p` — PETG Forest Green
- `anycubic_petg_petglakeblue_1000_175_p` — PETG Lake Blue
- `anycubic_petg_petglimegreen_1000_175_p` — PETG Lime Green
- `anycubic_petg_petgpeanutbrown_1000_175_p` — PETG Peanut Brown
- `anycubic_petg_petgpink_1000_175_p` — PETG Pink
- `anycubic_petg_petgred_1000_175_p` — PETG Red
- `anycubic_petg_petgtexturegrey_1000_175_p` — PETG Texture Grey
- `anycubic_petg_petgtexturesilver_1000_175_p` — PETG Texture Silver
- `anycubic_petg_translucentpetgblue_1000_175_p` — Translucent PETG Blue
- `anycubic_petg_translucentpetgbrown_1000_175_p` — Translucent PETG Brown
- `anycubic_petg_translucentpetgclear_1000_175_p` — Translucent PETG Clear
- `anycubic_petg_translucentpetggreen_1000_175_p` — Translucent PETG Green
- `anycubic_petg_translucentpetggrey_1000_175_p` — Translucent PETG Grey
- `anycubic_petg_translucentpetgolive_1000_175_p` — Translucent PETG Olive
- `anycubic_petg_translucentpetgorange_1000_175_p` — Translucent PETG Orange
- `anycubic_petg_translucentpetgpink_1000_175_p` — Translucent PETG Pink
- `anycubic_petg_translucentpetgpurple_1000_175_p` — Translucent PETG Purple
- `anycubic_pla_high-speedplablack_1000_175_p` — High-Speed PLA Black
- `anycubic_pla_high-speedplablue_1000_175_p` — High-Speed PLA Blue
- `anycubic_pla_high-speedplagreen_1000_175_p` — High-Speed PLA Green
- `anycubic_pla_high-speedplagrey_1000_175_p` — High-Speed PLA Grey
- `anycubic_pla_high-speedplaorange_1000_175_p` — High-Speed PLA Orange
- `anycubic_pla_high-speedplapink_1000_175_p` — High-Speed PLA Pink
- `anycubic_pla_high-speedplapurple_1000_175_p` — High-Speed PLA Purple
- `anycubic_pla_high-speedplared_1000_175_p` — High-Speed PLA Red
- `anycubic_pla_high-speedplawhite_1000_175_p` — High-Speed PLA White
- `anycubic_pla_high-speedplayellow_1000_175_p` — High-Speed PLA Yellow
- `anycubic_pla_plabasicblue_1000_175_p` — PLA Basic Blue
- `anycubic_pla_plabasicbrightred_1000_175_p` — PLA Basic Bright Red
- `anycubic_pla_plabasicclassicgreen_1000_175_p` — PLA Basic Classic Green
- `anycubic_pla_plabasicsilver_1000_175_p` — PLA Basic Silver
- `anycubic_pla_plagalaxyblue_1000_175_p` — PLA Galaxy Blue
- `anycubic_pla_plagalaxybrown_1000_175_p` — PLA Galaxy Brown
- `anycubic_pla_plagalaxygreen_1000_175_p` — PLA Galaxy Green
- `anycubic_pla_plagalaxypurple_1000_175_p` — PLA Galaxy Purple
- `anycubic_pla_plamarblebrickred_1000_175_p` — PLA Marble Brick Red
- `anycubic_pla_plamarblemarblewhite_1000_175_p` — PLA Marble Marble White
- `anycubic_pla_plamatteblack_1000_175_p` — PLA Matte Black
- `anycubic_pla_plamattered_1000_175_p` — PLA Matte Red
- `anycubic_pla_plamatteredblue_1000_175_p` — PLA Matte Red Blue
- `anycubic_pla_plamattewhite_1000_175_p` — PLA Matte White
- `anycubic_pla_plametalmetallicblue_1000_175_p` — PLA Metal Metallic Blue
- `anycubic_pla_plaplusbeige_1000_175_p` — PLA Plus Beige
- `anycubic_pla_plaplusblack_1000_175_p` — PLA Plus Black
- `anycubic_pla_plaplusblue_1000_175_p` — PLA Plus Blue
- `anycubic_pla_plaplusbrown_1000_175_p` — PLA Plus Brown
- `anycubic_pla_plaplusgreen_1000_175_p` — PLA Plus Green
- `anycubic_pla_plaplusgrey_1000_175_p` — PLA Plus Grey
- `anycubic_pla_plaplusinterstellarviolet_1000_175_p` — PLA Plus Interstellar Violet
- `anycubic_pla_plapluslightblue_1000_175_p` — PLA Plus Light Blue
- `anycubic_pla_plaplusorange_1000_175_p` — PLA Plus Orange
- `anycubic_pla_plapluspeachpink_1000_175_p` — PLA Plus Peach Pink
- `anycubic_pla_plapluspurple_1000_175_p` — PLA Plus Purple
- `anycubic_pla_plaplusred_1000_175_p` — PLA Plus Red
- `anycubic_pla_plaplussilver_1000_175_p` — PLA Plus Silver
- `anycubic_pla_plaplusspringleaf_1000_175_p` — PLA Plus Spring Leaf
- `anycubic_pla_plaplustexturegrey_1000_175_p` — PLA Plus Texture Grey
- `anycubic_pla_plaplustropicalturquoise_1000_175_p` — PLA Plus Tropical Turquoise
- `anycubic_pla_plaplusvibrantyellow_1000_175_p` — PLA Plus Vibrant Yellow
- `anycubic_pla_plapluswhite_1000_175_p` — PLA Plus White
- `anycubic_pla_plasilkblue_1000_175_p` — PLA Silk Blue
- `anycubic_pla_plasilkchristmasgreen_1000_175_p` — PLA Silk Christmas Green
- `anycubic_pla_plasilkchristmasred_1000_175_p` — PLA Silk Christmas Red
- `anycubic_pla_plasilkcopper_1000_175_p` — PLA Silk Copper
- `anycubic_pla_plasilkgreen_1000_175_p` — PLA Silk Green
- `anycubic_pla_plasilklightgold_1000_175_p` — PLA Silk Light Gold
- `anycubic_pla_plasilkpink_1000_175_p` — PLA Silk Pink
- `anycubic_pla_plasilkpurple_1000_175_p` — PLA Silk Purple
- `anycubic_pla_plasilkrainbow_1000_175_p` — PLA Silk Rainbow
- `anycubic_pla_plasilkshinygold_1000_175_p` — PLA Silk Shiny Gold
- `anycubic_pla_plasilksilver_1000_175_p` — PLA Silk Silver
- `anycubic_pla_plasilkwhite_1000_175_p` — PLA Silk White
- `anycubic_pla_plasilkdual-tricolorblack-blue_1000_175_p` — PLA Silk Dual-Tricolor Black-Blue
- `anycubic_pla_plasilkdual-tricolorblack-gold_1000_175_p` — PLA Silk Dual-Tricolor Black-Gold
- `anycubic_pla_plasilkdual-tricolorblack-green_1000_175_p` — PLA Silk Dual-Tricolor Black-Green
- `anycubic_pla_plasilkdual-tricolorblack-purple_1000_175_p` — PLA Silk Dual-Tricolor Black-Purple
- `anycubic_pla_plasilkdual-tricolorblue-green-purple_1000_175_p` — PLA Silk Dual-Tricolor Blue-Green-Purple
- `anycubic_pla_plasilkdual-tricolorpink-gold_1000_175_p` — PLA Silk Dual-Tricolor Pink-Gold
- `anycubic_pla_plasilkdual-tricolorred-blue_1000_175_p` — PLA Silk Dual-Tricolor Red-Blue
- `anycubic_pla_plasilkdual-tricolorred-gold_1000_175_p` — PLA Silk Dual-Tricolor Red-Gold
- `anycubic_pla_plasilkdual-tricoloryellow-green_1000_175_p` — PLA Silk Dual-Tricolor Yellow-Green
- `anycubic_pla_plaspecialintersellarviolet_1000_175_p` — PLA Special Intersellar Violet
- `anycubic_pla_plaspecialpeachpink_1000_175_p` — PLA Special Peach Pink
- `anycubic_pla_plaspecialspringleaf_1000_175_p` — PLA Special Spring Leaf
- `anycubic_pla_plaspecialtropicalturquoise_1000_175_p` — PLA Special Tropical Turquoise
- `anycubic_pla_plabasicblack_1000_175_r` — PLA Basic Black
- `anycubic_pla_plabasicwhite_1000_175_r` — PLA Basic White
- `anycubic_pla_plabasictexturegrey_1000_175_r` — PLA Basic Texture Grey
- `anycubic_pla_plabasicred_1000_175_r` — PLA Basic Red
- `anycubic_pla_plabasicblue_1000_175_r` — PLA Basic Blue
- `anycubic_pla_plabasicyellow_1000_175_r` — PLA Basic Yellow
- `anycubic_pla_plabasicgreen_1000_175_r` — PLA Basic Green
- `anycubic_pla_plabasicorange_1000_175_r` — PLA Basic Orange
- `anycubic_pla_plabasicpurple_1000_175_r` — PLA Basic Purple
- `anycubic_pla_plabasicbeige_1000_175_r` — PLA Basic Beige
- `anycubic_pla_plabasictexturesilver_1000_175_r` — PLA Basic Texture Silver
- `anycubic_pla_plabasicpink_1000_175_r` — PLA Basic Pink
- `anycubic_pla_plabasicpeachpink_1000_175_r` — PLA Basic Peach Pink
- `anycubic_pla_plabasicspringleaf_1000_175_r` — PLA Basic Spring Leaf
- `anycubic_pla_plabasicbrown_1000_175_r` — PLA Basic Brown
- `anycubic_pla_plabasicmagenta_1000_175_r` — PLA Basic Magenta
- `anycubic_pla_plabasictropicalturquoise_1000_175_r` — PLA Basic Tropical Turquoise
- `anycubic_pla_plabasicclear_1000_175_r` — PLA Basic Clear
- `anycubic_pla_plabasiccyan_1000_175_r` — PLA Basic Cyan
- `anycubic_pla_plabasicinterstellarviolet_1000_175_r` — PLA Basic Interstellar Violet
- `anycubic_pla_plabasicgrey_1000_175_r` — PLA Basic Grey
- `anycubic_petg_petgclear_1000_175_r` — PETG Clear
- `anycubic_petg_petgwhite_1000_175_r` — PETG White
- `anycubic_petg_petggrey_1000_175_r` — PETG Grey
- `anycubic_petg_petgtexturegrey_1000_175_r` — PETG Texture Grey
- `anycubic_petg_petgyellow_1000_175_r` — PETG Yellow
- `anycubic_petg_petgorange_1000_175_r` — PETG Orange
- `anycubic_petg_petgred_1000_175_r` — PETG Red
- `anycubic_petg_petggreen_1000_175_r` — PETG Green
- `anycubic_petg_petgpurple_1000_175_r` — PETG Purple
- `anycubic_petg_petgblue_1000_175_r` — PETG Blue
- `anycubic_petg_petgblack_1000_175_r` — PETG Black
- `anycubic_pla_plaplusblack_1000_175_r` — PLA Plus Black
- `anycubic_pla_plapluswhite_1000_175_r` — PLA Plus White
- `anycubic_pla_plaplustexturegrey_1000_175_r` — PLA Plus Texture Grey
- `anycubic_pla_plaplusred_1000_175_r` — PLA Plus Red
- `anycubic_pla_plaplusblue_1000_175_r` — PLA Plus Blue
- `anycubic_pla_plaplusyellow_1000_175_r` — PLA Plus Yellow
- `anycubic_pla_plaplusgreen_1000_175_r` — PLA Plus Green
- `anycubic_pla_plaplusorange_1000_175_r` — PLA Plus Orange
- `anycubic_pla_plapluspink_1000_175_r` — PLA Plus Pink
- `anycubic_pla_plapluspurple_1000_175_r` — PLA Plus Purple
