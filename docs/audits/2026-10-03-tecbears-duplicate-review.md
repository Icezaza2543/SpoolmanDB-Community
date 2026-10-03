# tecbears duplicate migration review

Base `a56f7022d670af5a42ce82bcf06fcbb29209970b`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `440ef62592cc35f42d205eb0ff0a656440904eb7023787091e529745c492ccc3`.

## Authorization and result

{"groups": 12, "approved_groups": 12, "retired": 12, "deferred": 0, "hard_stops": 0, "before_count": 51787, "after_count": 51775, "brand_before": 85, "brand_after": 73, "registry_before": 1647, "registry_after": 1659, "metadata_fields_changed": 24, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Correct exact12 PLA/PETG survivor density/nozzle using current actively linked exact-line TDS. No plainPLA defaults carried ontoPETG. Bed values differ by surface between TDS and current glue-assisted product recommendations; retain survivor bed unresolved rather than invent one conditional range. No identifier transfer. HEX/translucency conflicts unresolved. Packaging/tare unchanged. Other-material-default review: [{"id": "tecbears_petg_petgblack_1000_175_p", "material": "PETG", "density": 1.24, "nozzle": [220, 250], "resolution": "Current exact-line evidence correction", "unresolved_fields": []}, {"id": "tecbears_petg_petgblue_1000_175_p", "material": "PETG", "density": 1.24, "nozzle": [220, 250], "resolution": "Current exact-line evidence correction", "unresolved_fields": []}, {"id": "tecbears_petg_petgwhite_1000_175_p", "material": "PETG", "density": 1.24, "nozzle": [220, 250], "resolution": "Current exact-line evidence correction", "unresolved_fields": []}]

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://cdn.shopify.com/s/files/1/0684/8744/6698/files/TB-TE-WI-077_Tecbears_TDS_ISO_PLA_A2.pdf?v=1780739644", "density": 1.23, "nozzle": [200, 240], "bed": [60, 70], "condition": "texturedPEI bed; different glue-assisted page recommendation remains unresolved"}
- {"url": "https://cdn.shopify.com/s/files/1/0684/8744/6698/files/TB-TE-WI-076_Tecbears_TDS_ISO_PETG_A1.pdf?v=1780993239", "density": 1.27, "nozzle": [240, 260], "bed": [70, 80], "condition": "texturedPEI bed; different glue-assisted page recommendation remains unresolved"}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`tecbears_petg_tecbearspetgblack_1000_175_p`|`tecbears_petg_petgblack_1000_175_p`|`tecbears.json::Tecbears::Tecbears PETG {color_name}::Tecbears PETG Black::PETG::1000::1.75::plastic::False`|
|`tecbears_petg_tecbearspetgblue_1000_175_p`|`tecbears_petg_petgblue_1000_175_p`|`tecbears.json::Tecbears::Tecbears PETG {color_name}::Tecbears PETG Blue::PETG::1000::1.75::plastic::False`|
|`tecbears_petg_tecbearspetgwhite_1000_175_p`|`tecbears_petg_petgwhite_1000_175_p`|`tecbears.json::Tecbears::Tecbears PETG {color_name}::Tecbears PETG White::PETG::1000::1.75::plastic::False`|
|`tecbears_pla_tecbearsplablack_1000_175_p`|`tecbears_pla_plablack_1000_175_p`|`tecbears.json::Tecbears::Tecbears PLA {color_name}::Tecbears PLA Black::PLA::1000::1.75::plastic::False`|
|`tecbears_pla_tecbearsplablue_1000_175_p`|`tecbears_pla_plablue_1000_175_p`|`tecbears.json::Tecbears::Tecbears PLA {color_name}::Tecbears PLA Blue::PLA::1000::1.75::plastic::False`|
|`tecbears_pla_tecbearsplagreen_1000_175_p`|`tecbears_pla_plagreen_1000_175_p`|`tecbears.json::Tecbears::Tecbears PLA {color_name}::Tecbears PLA Green::PLA::1000::1.75::plastic::False`|
|`tecbears_pla_tecbearsplagrey_1000_175_p`|`tecbears_pla_plagrey_1000_175_p`|`tecbears.json::Tecbears::Tecbears PLA {color_name}::Tecbears PLA Grey::PLA::1000::1.75::plastic::False`|
|`tecbears_pla_tecbearsplaorange_1000_175_p`|`tecbears_pla_plaorange_1000_175_p`|`tecbears.json::Tecbears::Tecbears PLA {color_name}::Tecbears PLA Orange::PLA::1000::1.75::plastic::False`|
|`tecbears_pla_tecbearsplapink_1000_175_p`|`tecbears_pla_plapink_1000_175_p`|`tecbears.json::Tecbears::Tecbears PLA {color_name}::Tecbears PLA Pink::PLA::1000::1.75::plastic::False`|
|`tecbears_pla_tecbearsplapurple_1000_175_p`|`tecbears_pla_plapurple_1000_175_p`|`tecbears.json::Tecbears::Tecbears PLA {color_name}::Tecbears PLA Purple::PLA::1000::1.75::plastic::False`|
|`tecbears_pla_tecbearsplared_1000_175_p`|`tecbears_pla_plared_1000_175_p`|`tecbears.json::Tecbears::Tecbears PLA {color_name}::Tecbears PLA Red::PLA::1000::1.75::plastic::False`|
|`tecbears_pla_tecbearsplawhite_1000_175_p`|`tecbears_pla_plawhite_1000_175_p`|`tecbears.json::Tecbears::Tecbears PLA {color_name}::Tecbears PLA White::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### TB001: dup-7604cb656b22fa9f25ca19573817655ce44f7f4a31ecdfe21e457a5609322f73

Status: APPROVED; survivor `tecbears_petg_petgblack_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`tecbears_petg_petgblack_1000_175_p`|`PETG {color_name}`|`Black`|{"source_file": "tecbears.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`tecbears_petg_tecbearspetgblack_1000_175_p`|`Tecbears PETG {color_name}`|`Black`|{"source_file": "tecbears.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "tecbears_petg_petgblack_1000_175_p": 1.24,
    "tecbears_petg_tecbearspetgblack_1000_175_p": 1.27
  },
  "spool_weight": {
    "tecbears_petg_petgblack_1000_175_p": null,
    "tecbears_petg_tecbearspetgblack_1000_175_p": 230
  },
  "color_hex": {
    "tecbears_petg_petgblack_1000_175_p": "010101",
    "tecbears_petg_tecbearspetgblack_1000_175_p": "1a1a1a"
  },
  "extruder_temp_range": {
    "tecbears_petg_petgblack_1000_175_p": [
      220,
      250
    ],
    "tecbears_petg_tecbearspetgblack_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "tecbears_petg_petgblack_1000_175_p": [
      70,
      90
    ],
    "tecbears_petg_tecbearspetgblack_1000_175_p": [
      70,
      85
    ]
  }
}
```

### TB002: dup-ba5c0b9689f990f00833a6a1e5daab4e371a908025971e88cb71f8fbb7a77321

Status: APPROVED; survivor `tecbears_petg_petgblue_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`tecbears_petg_petgblue_1000_175_p`|`PETG {color_name}`|`Blue`|{"source_file": "tecbears.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`tecbears_petg_tecbearspetgblue_1000_175_p`|`Tecbears PETG {color_name}`|`Blue`|{"source_file": "tecbears.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "tecbears_petg_petgblue_1000_175_p": 1.24,
    "tecbears_petg_tecbearspetgblue_1000_175_p": 1.27
  },
  "spool_weight": {
    "tecbears_petg_petgblue_1000_175_p": null,
    "tecbears_petg_tecbearspetgblue_1000_175_p": 230
  },
  "color_hex": {
    "tecbears_petg_petgblue_1000_175_p": "0000FF",
    "tecbears_petg_tecbearspetgblue_1000_175_p": "1b4e9b"
  },
  "extruder_temp_range": {
    "tecbears_petg_petgblue_1000_175_p": [
      220,
      250
    ],
    "tecbears_petg_tecbearspetgblue_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "tecbears_petg_petgblue_1000_175_p": [
      70,
      90
    ],
    "tecbears_petg_tecbearspetgblue_1000_175_p": [
      70,
      85
    ]
  }
}
```

### TB003: dup-d604110a2d31cb0846caf17ffde62efc7cba92ca42f186c2e4dbd142c90956bd

Status: APPROVED; survivor `tecbears_petg_petgwhite_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`tecbears_petg_petgwhite_1000_175_p`|`PETG {color_name}`|`White`|{"source_file": "tecbears.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`tecbears_petg_tecbearspetgwhite_1000_175_p`|`Tecbears PETG {color_name}`|`White`|{"source_file": "tecbears.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "tecbears_petg_petgwhite_1000_175_p": 1.24,
    "tecbears_petg_tecbearspetgwhite_1000_175_p": 1.27
  },
  "spool_weight": {
    "tecbears_petg_petgwhite_1000_175_p": null,
    "tecbears_petg_tecbearspetgwhite_1000_175_p": 230
  },
  "color_hex": {
    "tecbears_petg_petgwhite_1000_175_p": "FFFFFF",
    "tecbears_petg_tecbearspetgwhite_1000_175_p": "f5f5f5"
  },
  "extruder_temp_range": {
    "tecbears_petg_petgwhite_1000_175_p": [
      220,
      250
    ],
    "tecbears_petg_tecbearspetgwhite_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "tecbears_petg_petgwhite_1000_175_p": [
      70,
      90
    ],
    "tecbears_petg_tecbearspetgwhite_1000_175_p": [
      70,
      85
    ]
  }
}
```

### TB004: dup-0c5be2ddaa658d0c5aef93fd3e369d41c51d4d8c60bd10636764e67a77361e48

Status: APPROVED; survivor `tecbears_pla_plablack_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`tecbears_pla_plablack_1000_175_p`|`PLA {color_name}`|`Black`|{"source_file": "tecbears.json", "definition_index": 6, "weights": 2, "diameters": 1, "colors": 22, "compiled_records": 44} / False|
|`tecbears_pla_tecbearsplablack_1000_175_p`|`Tecbears PLA {color_name}`|`Black`|{"source_file": "tecbears.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "tecbears_pla_plablack_1000_175_p": 1.25,
    "tecbears_pla_tecbearsplablack_1000_175_p": 1.24
  },
  "spool_weight": {
    "tecbears_pla_plablack_1000_175_p": null,
    "tecbears_pla_tecbearsplablack_1000_175_p": 230
  },
  "color_hex": {
    "tecbears_pla_plablack_1000_175_p": "000000",
    "tecbears_pla_tecbearsplablack_1000_175_p": "1a1a1a"
  },
  "extruder_temp_range": {
    "tecbears_pla_plablack_1000_175_p": [
      190,
      230
    ],
    "tecbears_pla_tecbearsplablack_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "tecbears_pla_plablack_1000_175_p": [
      50,
      70
    ],
    "tecbears_pla_tecbearsplablack_1000_175_p": [
      50,
      60
    ]
  }
}
```

### TB005: dup-5cd71eac08ba983bc2bbee6520744b3a972130e8a655ed31e7cc25609abe320f

Status: APPROVED; survivor `tecbears_pla_plablue_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`tecbears_pla_plablue_1000_175_p`|`PLA {color_name}`|`Blue`|{"source_file": "tecbears.json", "definition_index": 6, "weights": 2, "diameters": 1, "colors": 22, "compiled_records": 44} / False|
|`tecbears_pla_tecbearsplablue_1000_175_p`|`Tecbears PLA {color_name}`|`Blue`|{"source_file": "tecbears.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "tecbears_pla_plablue_1000_175_p": 1.25,
    "tecbears_pla_tecbearsplablue_1000_175_p": 1.24
  },
  "spool_weight": {
    "tecbears_pla_plablue_1000_175_p": null,
    "tecbears_pla_tecbearsplablue_1000_175_p": 230
  },
  "color_hex": {
    "tecbears_pla_plablue_1000_175_p": "0353BA",
    "tecbears_pla_tecbearsplablue_1000_175_p": "1b4e9b"
  },
  "extruder_temp_range": {
    "tecbears_pla_plablue_1000_175_p": [
      190,
      230
    ],
    "tecbears_pla_tecbearsplablue_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "tecbears_pla_plablue_1000_175_p": [
      50,
      70
    ],
    "tecbears_pla_tecbearsplablue_1000_175_p": [
      50,
      60
    ]
  }
}
```

### TB006: dup-0098a7f5f8d435b3dd9958771aadc8248d5043377f726ed9bea9e56584c999fc

Status: APPROVED; survivor `tecbears_pla_plagreen_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`tecbears_pla_plagreen_1000_175_p`|`PLA {color_name}`|`Green`|{"source_file": "tecbears.json", "definition_index": 6, "weights": 2, "diameters": 1, "colors": 22, "compiled_records": 44} / False|
|`tecbears_pla_tecbearsplagreen_1000_175_p`|`Tecbears PLA {color_name}`|`Green`|{"source_file": "tecbears.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "tecbears_pla_plagreen_1000_175_p": 1.25,
    "tecbears_pla_tecbearsplagreen_1000_175_p": 1.24
  },
  "spool_weight": {
    "tecbears_pla_plagreen_1000_175_p": null,
    "tecbears_pla_tecbearsplagreen_1000_175_p": 230
  },
  "color_hex": {
    "tecbears_pla_plagreen_1000_175_p": "00FF00",
    "tecbears_pla_tecbearsplagreen_1000_175_p": "2e7d32"
  },
  "extruder_temp_range": {
    "tecbears_pla_plagreen_1000_175_p": [
      190,
      230
    ],
    "tecbears_pla_tecbearsplagreen_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "tecbears_pla_plagreen_1000_175_p": [
      50,
      70
    ],
    "tecbears_pla_tecbearsplagreen_1000_175_p": [
      50,
      60
    ]
  }
}
```

### TB007: dup-af6739e8eab319b3001b0d1ceba8206054d311ba2bb59a9ecc71988a7c336a6a

Status: APPROVED; survivor `tecbears_pla_plagrey_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`tecbears_pla_plagrey_1000_175_p`|`PLA {color_name}`|`Grey`|{"source_file": "tecbears.json", "definition_index": 6, "weights": 2, "diameters": 1, "colors": 22, "compiled_records": 44} / False|
|`tecbears_pla_tecbearsplagrey_1000_175_p`|`Tecbears PLA {color_name}`|`Grey`|{"source_file": "tecbears.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "tecbears_pla_plagrey_1000_175_p": 1.25,
    "tecbears_pla_tecbearsplagrey_1000_175_p": 1.24
  },
  "spool_weight": {
    "tecbears_pla_plagrey_1000_175_p": null,
    "tecbears_pla_tecbearsplagrey_1000_175_p": 230
  },
  "extruder_temp_range": {
    "tecbears_pla_plagrey_1000_175_p": [
      190,
      230
    ],
    "tecbears_pla_tecbearsplagrey_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "tecbears_pla_plagrey_1000_175_p": [
      50,
      70
    ],
    "tecbears_pla_tecbearsplagrey_1000_175_p": [
      50,
      60
    ]
  }
}
```

### TB008: dup-de75b05f6a37a1c91e7f6d7fc7650444118cb82ec44c1682dfaba40d41efab53

Status: APPROVED; survivor `tecbears_pla_plaorange_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`tecbears_pla_plaorange_1000_175_p`|`PLA {color_name}`|`Orange`|{"source_file": "tecbears.json", "definition_index": 6, "weights": 2, "diameters": 1, "colors": 22, "compiled_records": 44} / False|
|`tecbears_pla_tecbearsplaorange_1000_175_p`|`Tecbears PLA {color_name}`|`Orange`|{"source_file": "tecbears.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "tecbears_pla_plaorange_1000_175_p": 1.25,
    "tecbears_pla_tecbearsplaorange_1000_175_p": 1.24
  },
  "spool_weight": {
    "tecbears_pla_plaorange_1000_175_p": null,
    "tecbears_pla_tecbearsplaorange_1000_175_p": 230
  },
  "color_hex": {
    "tecbears_pla_plaorange_1000_175_p": "F67405",
    "tecbears_pla_tecbearsplaorange_1000_175_p": "f57c00"
  },
  "extruder_temp_range": {
    "tecbears_pla_plaorange_1000_175_p": [
      190,
      230
    ],
    "tecbears_pla_tecbearsplaorange_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "tecbears_pla_plaorange_1000_175_p": [
      50,
      70
    ],
    "tecbears_pla_tecbearsplaorange_1000_175_p": [
      50,
      60
    ]
  }
}
```

### TB009: dup-e1d0186a84b2d8e472635418bc0fa2c2c77c2b60e0b8dc29962757357842111e

Status: APPROVED; survivor `tecbears_pla_plapink_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`tecbears_pla_plapink_1000_175_p`|`PLA {color_name}`|`Pink`|{"source_file": "tecbears.json", "definition_index": 6, "weights": 2, "diameters": 1, "colors": 22, "compiled_records": 44} / False|
|`tecbears_pla_tecbearsplapink_1000_175_p`|`Tecbears PLA {color_name}`|`Pink`|{"source_file": "tecbears.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "tecbears_pla_plapink_1000_175_p": 1.25,
    "tecbears_pla_tecbearsplapink_1000_175_p": 1.24
  },
  "spool_weight": {
    "tecbears_pla_plapink_1000_175_p": null,
    "tecbears_pla_tecbearsplapink_1000_175_p": 230
  },
  "color_hex": {
    "tecbears_pla_plapink_1000_175_p": "FF00CB",
    "tecbears_pla_tecbearsplapink_1000_175_p": "f48fb1"
  },
  "extruder_temp_range": {
    "tecbears_pla_plapink_1000_175_p": [
      190,
      230
    ],
    "tecbears_pla_tecbearsplapink_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "tecbears_pla_plapink_1000_175_p": [
      50,
      70
    ],
    "tecbears_pla_tecbearsplapink_1000_175_p": [
      50,
      60
    ]
  }
}
```

### TB010: dup-796f962c4bb34b2445b534ff46bc86a0b20ae8bcafb627921db9d0436f8cb3e4

Status: APPROVED; survivor `tecbears_pla_plapurple_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`tecbears_pla_plapurple_1000_175_p`|`PLA {color_name}`|`Purple`|{"source_file": "tecbears.json", "definition_index": 6, "weights": 2, "diameters": 1, "colors": 22, "compiled_records": 44} / False|
|`tecbears_pla_tecbearsplapurple_1000_175_p`|`Tecbears PLA {color_name}`|`Purple`|{"source_file": "tecbears.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "tecbears_pla_plapurple_1000_175_p": 1.25,
    "tecbears_pla_tecbearsplapurple_1000_175_p": 1.24
  },
  "spool_weight": {
    "tecbears_pla_plapurple_1000_175_p": null,
    "tecbears_pla_tecbearsplapurple_1000_175_p": 230
  },
  "color_hex": {
    "tecbears_pla_plapurple_1000_175_p": "6C47B2",
    "tecbears_pla_tecbearsplapurple_1000_175_p": "6a1b9a"
  },
  "extruder_temp_range": {
    "tecbears_pla_plapurple_1000_175_p": [
      190,
      230
    ],
    "tecbears_pla_tecbearsplapurple_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "tecbears_pla_plapurple_1000_175_p": [
      50,
      70
    ],
    "tecbears_pla_tecbearsplapurple_1000_175_p": [
      50,
      60
    ]
  }
}
```

### TB011: dup-a2b4e2c5cdfe26d1f1d32f1c208b66576a110465992e265368e6f32d15f17a19

Status: APPROVED; survivor `tecbears_pla_plared_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`tecbears_pla_plared_1000_175_p`|`PLA {color_name}`|`Red`|{"source_file": "tecbears.json", "definition_index": 6, "weights": 2, "diameters": 1, "colors": 22, "compiled_records": 44} / False|
|`tecbears_pla_tecbearsplared_1000_175_p`|`Tecbears PLA {color_name}`|`Red`|{"source_file": "tecbears.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "tecbears_pla_plared_1000_175_p": 1.25,
    "tecbears_pla_tecbearsplared_1000_175_p": 1.24
  },
  "spool_weight": {
    "tecbears_pla_plared_1000_175_p": null,
    "tecbears_pla_tecbearsplared_1000_175_p": 230
  },
  "color_hex": {
    "tecbears_pla_plared_1000_175_p": "FF0000",
    "tecbears_pla_tecbearsplared_1000_175_p": "c41e2a"
  },
  "extruder_temp_range": {
    "tecbears_pla_plared_1000_175_p": [
      190,
      230
    ],
    "tecbears_pla_tecbearsplared_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "tecbears_pla_plared_1000_175_p": [
      50,
      70
    ],
    "tecbears_pla_tecbearsplared_1000_175_p": [
      50,
      60
    ]
  }
}
```

### TB012: dup-a7c94969596dbf2f9d17035f5dbf8a2a3a0feddd1810d0b4b241aff67b9ac16d

Status: APPROVED; survivor `tecbears_pla_plawhite_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`tecbears_pla_plawhite_1000_175_p`|`PLA {color_name}`|`White`|{"source_file": "tecbears.json", "definition_index": 6, "weights": 2, "diameters": 1, "colors": 22, "compiled_records": 44} / False|
|`tecbears_pla_tecbearsplawhite_1000_175_p`|`Tecbears PLA {color_name}`|`White`|{"source_file": "tecbears.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "tecbears_pla_plawhite_1000_175_p": 1.25,
    "tecbears_pla_tecbearsplawhite_1000_175_p": 1.24
  },
  "spool_weight": {
    "tecbears_pla_plawhite_1000_175_p": null,
    "tecbears_pla_tecbearsplawhite_1000_175_p": 230
  },
  "color_hex": {
    "tecbears_pla_plawhite_1000_175_p": "FFFFFF",
    "tecbears_pla_tecbearsplawhite_1000_175_p": "f5f5f5"
  },
  "extruder_temp_range": {
    "tecbears_pla_plawhite_1000_175_p": [
      190,
      230
    ],
    "tecbears_pla_tecbearsplawhite_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "tecbears_pla_plawhite_1000_175_p": [
      50,
      70
    ],
    "tecbears_pla_tecbearsplawhite_1000_175_p": [
      50,
      60
    ]
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "tecbears_pla_plagreen_1000_175_p",
      "values": {
        "density": 1.23,
        "extruder_temp_range": [
          200,
          240
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0684/8744/6698/files/TB-TE-WI-077_Tecbears_TDS_ISO_PLA_A2.pdf?v=1780739644",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "tecbears_pla_plablack_1000_175_p",
      "values": {
        "density": 1.23,
        "extruder_temp_range": [
          200,
          240
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0684/8744/6698/files/TB-TE-WI-077_Tecbears_TDS_ISO_PLA_A2.pdf?v=1780739644",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "tecbears_pla_plablue_1000_175_p",
      "values": {
        "density": 1.23,
        "extruder_temp_range": [
          200,
          240
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0684/8744/6698/files/TB-TE-WI-077_Tecbears_TDS_ISO_PLA_A2.pdf?v=1780739644",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "tecbears_petg_petgblack_1000_175_p",
      "values": {
        "density": 1.27,
        "extruder_temp_range": [
          240,
          260
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0684/8744/6698/files/TB-TE-WI-076_Tecbears_TDS_ISO_PETG_A1.pdf?v=1780993239",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "tecbears_pla_plapurple_1000_175_p",
      "values": {
        "density": 1.23,
        "extruder_temp_range": [
          200,
          240
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0684/8744/6698/files/TB-TE-WI-077_Tecbears_TDS_ISO_PLA_A2.pdf?v=1780739644",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "tecbears_pla_plared_1000_175_p",
      "values": {
        "density": 1.23,
        "extruder_temp_range": [
          200,
          240
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0684/8744/6698/files/TB-TE-WI-077_Tecbears_TDS_ISO_PLA_A2.pdf?v=1780739644",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "tecbears_pla_plawhite_1000_175_p",
      "values": {
        "density": 1.23,
        "extruder_temp_range": [
          200,
          240
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0684/8744/6698/files/TB-TE-WI-077_Tecbears_TDS_ISO_PLA_A2.pdf?v=1780739644",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "tecbears_pla_plagrey_1000_175_p",
      "values": {
        "density": 1.23,
        "extruder_temp_range": [
          200,
          240
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0684/8744/6698/files/TB-TE-WI-077_Tecbears_TDS_ISO_PLA_A2.pdf?v=1780739644",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "tecbears_petg_petgblue_1000_175_p",
      "values": {
        "density": 1.27,
        "extruder_temp_range": [
          240,
          260
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0684/8744/6698/files/TB-TE-WI-076_Tecbears_TDS_ISO_PETG_A1.pdf?v=1780993239",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "tecbears_petg_petgwhite_1000_175_p",
      "values": {
        "density": 1.27,
        "extruder_temp_range": [
          240,
          260
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0684/8744/6698/files/TB-TE-WI-076_Tecbears_TDS_ISO_PETG_A1.pdf?v=1780993239",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "tecbears_pla_plaorange_1000_175_p",
      "values": {
        "density": 1.23,
        "extruder_temp_range": [
          200,
          240
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0684/8744/6698/files/TB-TE-WI-077_Tecbears_TDS_ISO_PLA_A2.pdf?v=1780739644",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "tecbears_pla_plapink_1000_175_p",
      "values": {
        "density": 1.23,
        "extruder_temp_range": [
          200,
          240
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0684/8744/6698/files/TB-TE-WI-077_Tecbears_TDS_ISO_PLA_A2.pdf?v=1780739644",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    }
  ],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `tecbears_pla_tecbearsplayellow_1000_175_p` — Tecbears PLA Yellow
- `tecbears_pla+_tecbearspla+black_1000_175_p` — Tecbears PLA+ Black
- `tecbears_pla+_tecbearspla+white_1000_175_p` — Tecbears PLA+ White
- `tecbears_pla+_tecbearspla+red_1000_175_p` — Tecbears PLA+ Red
- `tecbears_pla+_tecbearspla+blue_1000_175_p` — Tecbears PLA+ Blue
- `tecbears_pla+_tecbearspla+grey_1000_175_p` — Tecbears PLA+ Grey
- `tecbears_petg_tecbearspetgclear_1000_175_p` — Tecbears PETG Clear
- `tecbears_petg_glowpetgblue_1000_175_p` — Glow PETG Blue
- `tecbears_petg_glowpetgwhitetoglowblue_1000_175_p` — Glow PETG White to Glow Blue
- `tecbears_petg_glowpetgyellow_1000_175_p` — Glow PETG Yellow
- `tecbears_petg_petggrey_1000_175_p` — PETG Grey
- `tecbears_petg_petgorange_1000_175_p` — PETG Orange
- `tecbears_petg_petgred_1000_175_p` — PETG Red
- `tecbears_petg_petgtransparent_1000_175_p` — PETG Transparent
- `tecbears_pla_glowplablue_1000_175_p` — Glow PLA Blue
- `tecbears_pla_glowplagreen_1000_175_p` — Glow PLA Green
- `tecbears_pla_glowplawhitetoglowblue_1000_175_p` — Glow PLA White to Glow Blue
- `tecbears_pla_glowplawhitetoglowgreen_1000_175_p` — Glow PLA White to Glow Green
- `tecbears_pla_glowplayellow_1000_175_p` — Glow PLA Yellow
- `tecbears_pla_plabeige_1000_175_p` — PLA Beige
- `tecbears_pla_placherrywood_1000_175_p` — PLA Cherry Wood
- `tecbears_pla_placyan_1000_175_p` — PLA Cyan
- `tecbears_pla_plamaplewood_1000_175_p` — PLA Maple Wood
- `tecbears_pla_plaolivegreen_1000_175_p` — PLA Olive Green
- `tecbears_pla_platransparentblue_1000_175_p` — PLA Transparent Blue
- `tecbears_pla_platransparentgreen_1000_175_p` — PLA Transparent Green
- `tecbears_pla_platransparentorange_1000_175_p` — PLA Transparent Orange
- `tecbears_pla_platransparentpurple_1000_175_p` — PLA Transparent Purple
- `tecbears_pla_platransparentred_1000_175_p` — PLA Transparent Red
- `tecbears_pla_platransparentyellow_1000_175_p` — PLA Transparent Yellow
- `tecbears_pla_plawalnutwood_1000_175_p` — PLA Walnut Wood
- `tecbears_pla_plawood_1000_175_p` — PLA Wood
- `tecbears_pla_plabeige_1100_175_p` — PLA Beige
- `tecbears_pla_plablack_1100_175_p` — PLA Black
- `tecbears_pla_plablue_1100_175_p` — PLA Blue
- `tecbears_pla_placherrywood_1100_175_p` — PLA Cherry Wood
- `tecbears_pla_placyan_1100_175_p` — PLA Cyan
- `tecbears_pla_plagreen_1100_175_p` — PLA Green
- `tecbears_pla_plagrey_1100_175_p` — PLA Grey
- `tecbears_pla_plamaplewood_1100_175_p` — PLA Maple Wood
- `tecbears_pla_plaolivegreen_1100_175_p` — PLA Olive Green
- `tecbears_pla_plaorange_1100_175_p` — PLA Orange
- `tecbears_pla_plapink_1100_175_p` — PLA Pink
- `tecbears_pla_plapurple_1100_175_p` — PLA Purple
- `tecbears_pla_plared_1100_175_p` — PLA Red
- `tecbears_pla_platransparentblue_1100_175_p` — PLA Transparent Blue
- `tecbears_pla_platransparentgreen_1100_175_p` — PLA Transparent Green
- `tecbears_pla_platransparentorange_1100_175_p` — PLA Transparent Orange
- `tecbears_pla_platransparentpurple_1100_175_p` — PLA Transparent Purple
- `tecbears_pla_platransparentred_1100_175_p` — PLA Transparent Red
- `tecbears_pla_platransparentyellow_1100_175_p` — PLA Transparent Yellow
- `tecbears_pla_plawalnutwood_1100_175_p` — PLA Walnut Wood
- `tecbears_pla_plawhite_1100_175_p` — PLA White
- `tecbears_pla_plawood_1100_175_p` — PLA Wood
- `tecbears_pla_plushighspeedplaolivegreen_1000_175_p` — Plus High Speed PLA Olive Green
- `tecbears_pla_plushighspeedplaorange_1000_175_p` — Plus High Speed PLA Orange
- `tecbears_pla_silkplagold_1000_175_p` — Silk PLA Gold
- `tecbears_pla_silkplasilver_1000_175_p` — Silk PLA Silver
- `tecbears_tpu_95atpublack_1000_175_p` — 95A TPU Black
- `tecbears_tpu_95atpuorange_1000_175_p` — 95A TPU Orange
- `tecbears_tpu_95atpuwhite_1000_175_p` — 95A TPU White
