# verbatim duplicate migration review

Base `c83ff290964208b2bc0e6e237a8803dd2d710e30`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `84d5f52300874e9c95ef9fda7c1388fa01b89d24a8957cd591301d3f4a7e45c0`.

## Authorization and result

{"groups": 22, "approved_groups": 5, "retired": 5, "deferred": 17, "hard_stops": 0, "before_count": 51866, "after_count": 51861, "brand_before": 70, "brand_after": 65, "registry_before": 1568, "registry_after": 1573, "metadata_fields_changed": 15, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Apply only five no-transfer strict groups, exact current family printing ranges/points on those survivors. Seventeen mixed-diameter code groups defer: current mechanical preservation copies every extra, but extras belong to still-live2.85 rows and must not move to1.75. No unique values or codes lost because deferred groups unchanged. PETG density1.27 retained unverified. Existing2018 third-party links are material-matched by URL, not freshly verified current docs; no proven wrong-material link. Ordinary HEX/translucency conflicts unresolved. Packaging/tare unchanged.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://www.verbatim-europe.com/en/3d/products/verbatim-pla-filament-175mm-1kg-black-55318", "density": 1.24, "nozzle": [200, 220], "bed": 60}
- {"url": "https://www.verbatim-europe.com/en/3d/products/verbatim-abs-filament-175mm-1kg-black-55026", "density": 1.05, "nozzle": [240, 260], "bed": 90}
- {"url": "https://www.verbatim-europe.com/en/3d/products/verbatim-pet-g-filament-175-mm-black-55052", "nozzle": [225, 245], "bed": 90, "note": "recommended extrusion range, not the separate process temperature240±10"}
- {"url": "https://www.verbatim-europe.com/en/3d-printing-filaments/products/verbatim-pla-filament-285mm-1kg-black-55327", "diameter": 2.85, "sku": "55327"}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`verbatim_abs_verbatimabsblue_1000_175_p`|`verbatim_abs_absblue_1000_175_p`|`verbatim.json::Verbatim::Verbatim ABS {color_name}::Verbatim ABS Blue::ABS::1000::1.75::plastic::False`|
|`verbatim_abs_verbatimabsgreen_1000_175_p`|`verbatim_abs_absgreen_1000_175_p`|`verbatim.json::Verbatim::Verbatim ABS {color_name}::Verbatim ABS Green::ABS::1000::1.75::plastic::False`|
|`verbatim_abs_verbatimabsred_1000_175_p`|`verbatim_abs_absred_1000_175_p`|`verbatim.json::Verbatim::Verbatim ABS {color_name}::Verbatim ABS Red::ABS::1000::1.75::plastic::False`|
|`verbatim_petg_verbatimpetgbluetransparent_1000_175_p`|`verbatim_petg_petgbluetransparent_1000_175_p`|`verbatim.json::Verbatim::Verbatim PETG {color_name}::Verbatim PETG Blue Transparent::PETG::1000::1.75::plastic::False`|
|`verbatim_pla_verbatimplanaturaltransparent_1000_175_p`|`verbatim_pla_planatural/transparent_1000_175_p`|`verbatim.json::Verbatim::Verbatim PLA {color_name}::Verbatim PLA Natural Transparent::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### VB001: dup-b805c0b67dcd8759004235bd08a5905b388e2cc42f3d7bcdeffa22b314f156c2

Status: DEFERRED; survivor `verbatim_abs_absaluminiumgrey_1000_175_p`; Mixed1.75/2.85 identifiers; extra55036 remains on live2.85 same-color row. Exact scoped reconciliation deferred..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_abs_absaluminiumgrey_1000_175_p`|`ABS {color_name}`|`Aluminium Grey`|{"source_file": "verbatim.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`verbatim_abs_verbatimabsaluminiumgrey_1000_175_p`|`Verbatim ABS {color_name}`|`Aluminium Grey`|{"source_file": "verbatim.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 7, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_abs_absaluminiumgrey_1000_175_p": "9F9F9F",
    "verbatim_abs_verbatimabsaluminiumgrey_1000_175_p": "666666"
  },
  "extruder_temp_range": {
    "verbatim_abs_absaluminiumgrey_1000_175_p": [
      230,
      260
    ],
    "verbatim_abs_verbatimabsaluminiumgrey_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "verbatim_abs_absaluminiumgrey_1000_175_p": [
      90,
      110
    ],
    "verbatim_abs_verbatimabsaluminiumgrey_1000_175_p": [
      0,
      100
    ]
  },
  "codes": {
    "verbatim_abs_absaluminiumgrey_1000_175_p": [
      "55032"
    ],
    "verbatim_abs_verbatimabsaluminiumgrey_1000_175_p": [
      "55032",
      "55036"
    ]
  }
}
```

### VB002: dup-916fa65e19d0cabea5e312de64659bd3f203f17a1956f99dd1eef9477f21bf56

Status: DEFERRED; survivor `verbatim_abs_absblack_1000_175_p`; Mixed1.75/2.85 identifiers; extra55033 remains on live2.85 same-color row. Exact scoped reconciliation deferred..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_abs_absblack_1000_175_p`|`ABS {color_name}`|`Black`|{"source_file": "verbatim.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`verbatim_abs_verbatimabsblack_1000_175_p`|`Verbatim ABS {color_name}`|`Black`|{"source_file": "verbatim.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 7, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_abs_absblack_1000_175_p": "000000",
    "verbatim_abs_verbatimabsblack_1000_175_p": "050505"
  },
  "extruder_temp_range": {
    "verbatim_abs_absblack_1000_175_p": [
      230,
      260
    ],
    "verbatim_abs_verbatimabsblack_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "verbatim_abs_absblack_1000_175_p": [
      90,
      110
    ],
    "verbatim_abs_verbatimabsblack_1000_175_p": [
      0,
      100
    ]
  },
  "codes": {
    "verbatim_abs_absblack_1000_175_p": [
      "55026"
    ],
    "verbatim_abs_verbatimabsblack_1000_175_p": [
      "55026",
      "55033"
    ]
  }
}
```

### VB003: dup-b3d6467a0b1d79dee9a351e682e9edc178cebb5ba2b9f148a24c18fdd3597974

Status: APPROVED; survivor `verbatim_abs_absblue_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_abs_absblue_1000_175_p`|`ABS {color_name}`|`Blue`|{"source_file": "verbatim.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`verbatim_abs_verbatimabsblue_1000_175_p`|`Verbatim ABS {color_name}`|`Blue`|{"source_file": "verbatim.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 7, "compiled_records": 14} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_abs_absblue_1000_175_p": "2C3294",
    "verbatim_abs_verbatimabsblue_1000_175_p": "1900ff"
  },
  "extruder_temp_range": {
    "verbatim_abs_absblue_1000_175_p": [
      230,
      260
    ],
    "verbatim_abs_verbatimabsblue_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "verbatim_abs_absblue_1000_175_p": [
      90,
      110
    ],
    "verbatim_abs_verbatimabsblue_1000_175_p": [
      0,
      100
    ]
  }
}
```

### VB004: dup-79db5a3b1eb80e9635ce492a89c10982fce464324fb00312975813e8a91c3df4

Status: APPROVED; survivor `verbatim_abs_absgreen_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_abs_absgreen_1000_175_p`|`ABS {color_name}`|`Green`|{"source_file": "verbatim.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`verbatim_abs_verbatimabsgreen_1000_175_p`|`Verbatim ABS {color_name}`|`Green`|{"source_file": "verbatim.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 7, "compiled_records": 14} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_abs_absgreen_1000_175_p": "739549",
    "verbatim_abs_verbatimabsgreen_1000_175_p": "005900"
  },
  "extruder_temp_range": {
    "verbatim_abs_absgreen_1000_175_p": [
      230,
      260
    ],
    "verbatim_abs_verbatimabsgreen_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "verbatim_abs_absgreen_1000_175_p": [
      90,
      110
    ],
    "verbatim_abs_verbatimabsgreen_1000_175_p": [
      0,
      100
    ]
  }
}
```

### VB005: dup-114d64ff6b49ef37c373cb709da039fc3ac6f59cdf9268fdf056ea7ca1a27024

Status: DEFERRED; survivor `verbatim_abs_absnatural/milky_1000_175_p`; Mixed1.75/2.85 identifiers; extra55035 remains on live2.85 same-color row. Exact scoped reconciliation deferred..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_abs_absnatural/milky_1000_175_p`|`ABS {color_name}`|`Natural/Milky`|{"source_file": "verbatim.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`verbatim_abs_verbatimabsnaturalmilky_1000_175_p`|`Verbatim ABS {color_name}`|`Natural Milky`|{"source_file": "verbatim.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 7, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_abs_absnatural/milky_1000_175_p": "DFDFD3",
    "verbatim_abs_verbatimabsnaturalmilky_1000_175_p": "fff0ba"
  },
  "extruder_temp_range": {
    "verbatim_abs_absnatural/milky_1000_175_p": [
      230,
      260
    ],
    "verbatim_abs_verbatimabsnaturalmilky_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "verbatim_abs_absnatural/milky_1000_175_p": [
      90,
      110
    ],
    "verbatim_abs_verbatimabsnaturalmilky_1000_175_p": [
      0,
      100
    ]
  },
  "translucent": {
    "verbatim_abs_absnatural/milky_1000_175_p": false,
    "verbatim_abs_verbatimabsnaturalmilky_1000_175_p": true
  },
  "codes": {
    "verbatim_abs_absnatural/milky_1000_175_p": [
      "55028"
    ],
    "verbatim_abs_verbatimabsnaturalmilky_1000_175_p": [
      "55028",
      "55035"
    ]
  }
}
```

### VB006: dup-cb1364b15c093caea35950df4922c6ef586d7596a3463395fc8a52fa74ed4e72

Status: APPROVED; survivor `verbatim_abs_absred_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_abs_absred_1000_175_p`|`ABS {color_name}`|`Red`|{"source_file": "verbatim.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`verbatim_abs_verbatimabsred_1000_175_p`|`Verbatim ABS {color_name}`|`Red`|{"source_file": "verbatim.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 7, "compiled_records": 14} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_abs_absred_1000_175_p": "E60000",
    "verbatim_abs_verbatimabsred_1000_175_p": "ff0000"
  },
  "extruder_temp_range": {
    "verbatim_abs_absred_1000_175_p": [
      230,
      260
    ],
    "verbatim_abs_verbatimabsred_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "verbatim_abs_absred_1000_175_p": [
      90,
      110
    ],
    "verbatim_abs_verbatimabsred_1000_175_p": [
      0,
      100
    ]
  }
}
```

### VB007: dup-74fedf2051869a03c8b38bddd15ee1d65607d6b067d1167f1ddd04e152e32597

Status: DEFERRED; survivor `verbatim_abs_abswhite_1000_175_p`; Mixed1.75/2.85 identifiers; extra55034 remains on live2.85 same-color row. Exact scoped reconciliation deferred..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_abs_abswhite_1000_175_p`|`ABS {color_name}`|`White`|{"source_file": "verbatim.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`verbatim_abs_verbatimabswhite_1000_175_p`|`Verbatim ABS {color_name}`|`White`|{"source_file": "verbatim.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 7, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_abs_abswhite_1000_175_p": "FFFFFF",
    "verbatim_abs_verbatimabswhite_1000_175_p": "ffffff"
  },
  "extruder_temp_range": {
    "verbatim_abs_abswhite_1000_175_p": [
      230,
      260
    ],
    "verbatim_abs_verbatimabswhite_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "verbatim_abs_abswhite_1000_175_p": [
      90,
      110
    ],
    "verbatim_abs_verbatimabswhite_1000_175_p": [
      0,
      100
    ]
  },
  "codes": {
    "verbatim_abs_abswhite_1000_175_p": [
      "55027"
    ],
    "verbatim_abs_verbatimabswhite_1000_175_p": [
      "55027",
      "55034"
    ]
  }
}
```

### VB008: dup-6131ee86aece8ff8cedcf8e5bac1a8565ec7090d27bde0c7a37a218aa2c5e844

Status: DEFERRED; survivor `verbatim_petg_petgblack_1000_175_p`; Mixed1.75/2.85 identifiers; extra55060 remains on live2.85 same-color row. Exact scoped reconciliation deferred..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_petg_petgblack_1000_175_p`|`PETG {color_name}`|`Black`|{"source_file": "verbatim.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`verbatim_petg_verbatimpetgblack_1000_175_p`|`Verbatim PETG {color_name}`|`Black`|{"source_file": "verbatim.json", "definition_index": 1, "weights": 1, "diameters": 2, "colors": 8, "compiled_records": 16} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_petg_petgblack_1000_175_p": "000000",
    "verbatim_petg_verbatimpetgblack_1000_175_p": "050505"
  },
  "extruder_temp_range": {
    "verbatim_petg_petgblack_1000_175_p": [
      220,
      250
    ],
    "verbatim_petg_verbatimpetgblack_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "verbatim_petg_petgblack_1000_175_p": [
      70,
      90
    ],
    "verbatim_petg_verbatimpetgblack_1000_175_p": [
      60,
      90
    ]
  },
  "codes": {
    "verbatim_petg_petgblack_1000_175_p": [
      "55052"
    ],
    "verbatim_petg_verbatimpetgblack_1000_175_p": [
      "55052",
      "55060"
    ]
  }
}
```

### VB009: dup-2df31c23b3d50696307d37ee4578eee16a9e863ef6a7492851fba01853200836

Status: DEFERRED; survivor `verbatim_petg_petgblue_1000_175_p`; Mixed1.75/2.85 identifiers; extra55063 remains on live2.85 same-color row. Exact scoped reconciliation deferred..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_petg_petgblue_1000_175_p`|`PETG {color_name}`|`Blue`|{"source_file": "verbatim.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`verbatim_petg_verbatimpetgblue_1000_175_p`|`Verbatim PETG {color_name}`|`Blue`|{"source_file": "verbatim.json", "definition_index": 1, "weights": 1, "diameters": 2, "colors": 8, "compiled_records": 16} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_petg_petgblue_1000_175_p": "2C3294",
    "verbatim_petg_verbatimpetgblue_1000_175_p": "1900ff"
  },
  "extruder_temp_range": {
    "verbatim_petg_petgblue_1000_175_p": [
      220,
      250
    ],
    "verbatim_petg_verbatimpetgblue_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "verbatim_petg_petgblue_1000_175_p": [
      70,
      90
    ],
    "verbatim_petg_verbatimpetgblue_1000_175_p": [
      60,
      90
    ]
  },
  "codes": {
    "verbatim_petg_petgblue_1000_175_p": [
      "55055"
    ],
    "verbatim_petg_verbatimpetgblue_1000_175_p": [
      "55055",
      "55063"
    ]
  }
}
```

### VB010: dup-1aa1352e7348822ce8700d8b878d3cdf1deb742977f25992083c2a5a26fbc737

Status: APPROVED; survivor `verbatim_petg_petgbluetransparent_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_petg_petgbluetransparent_1000_175_p`|`PETG {color_name}`|`Blue Transparent`|{"source_file": "verbatim.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`verbatim_petg_verbatimpetgbluetransparent_1000_175_p`|`Verbatim PETG {color_name}`|`Blue Transparent`|{"source_file": "verbatim.json", "definition_index": 1, "weights": 1, "diameters": 2, "colors": 8, "compiled_records": 16} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_petg_petgbluetransparent_1000_175_p": "0099E6",
    "verbatim_petg_verbatimpetgbluetransparent_1000_175_p": "1e16e0"
  },
  "extruder_temp_range": {
    "verbatim_petg_petgbluetransparent_1000_175_p": [
      220,
      250
    ],
    "verbatim_petg_verbatimpetgbluetransparent_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "verbatim_petg_petgbluetransparent_1000_175_p": [
      70,
      90
    ],
    "verbatim_petg_verbatimpetgbluetransparent_1000_175_p": [
      60,
      90
    ]
  }
}
```

### VB011: dup-b24d799e3652bc9149f7de83f882df74a9b5770e190bc0b5a827c3ccb3f4efb1

Status: DEFERRED; survivor `verbatim_petg_petgclear_1000_175_p`; Mixed1.75/2.85 identifiers; extra55059 remains on live2.85 same-color row. Exact scoped reconciliation deferred..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_petg_petgclear_1000_175_p`|`PETG {color_name}`|`Clear`|{"source_file": "verbatim.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`verbatim_petg_verbatimpetgclear_1000_175_p`|`Verbatim PETG {color_name}`|`Clear`|{"source_file": "verbatim.json", "definition_index": 1, "weights": 1, "diameters": 2, "colors": 8, "compiled_records": 16} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_petg_petgclear_1000_175_p": "DFDFD3",
    "verbatim_petg_verbatimpetgclear_1000_175_p": "d9fff8"
  },
  "extruder_temp_range": {
    "verbatim_petg_petgclear_1000_175_p": [
      220,
      250
    ],
    "verbatim_petg_verbatimpetgclear_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "verbatim_petg_petgclear_1000_175_p": [
      70,
      90
    ],
    "verbatim_petg_verbatimpetgclear_1000_175_p": [
      60,
      90
    ]
  },
  "codes": {
    "verbatim_petg_petgclear_1000_175_p": [
      "55051"
    ],
    "verbatim_petg_verbatimpetgclear_1000_175_p": [
      "55051",
      "55059"
    ]
  }
}
```

### VB012: dup-042d7cafd1740279066838fcc96aafa382b5a53b8e90c1fabc91dc767ada80ba

Status: DEFERRED; survivor `verbatim_petg_petggreentransparent_1000_175_p`; Mixed1.75/2.85 identifiers; extra55065 remains on live2.85 same-color row. Do not copy to1.75; exact scoped identifier reconciliation deferred..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_petg_petggreentransparent_1000_175_p`|`PETG {color_name}`|`Green Transparent`|{"source_file": "verbatim.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`verbatim_petg_verbatimpetggreentransparent_1000_175_p`|`Verbatim PETG {color_name}`|`Green Transparent`|{"source_file": "verbatim.json", "definition_index": 1, "weights": 1, "diameters": 2, "colors": 8, "compiled_records": 16} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_petg_petggreentransparent_1000_175_p": "58C91B",
    "verbatim_petg_verbatimpetggreentransparent_1000_175_p": "094709"
  },
  "extruder_temp_range": {
    "verbatim_petg_petggreentransparent_1000_175_p": [
      220,
      250
    ],
    "verbatim_petg_verbatimpetggreentransparent_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "verbatim_petg_petggreentransparent_1000_175_p": [
      70,
      90
    ],
    "verbatim_petg_verbatimpetggreentransparent_1000_175_p": [
      60,
      90
    ]
  },
  "codes": {
    "verbatim_petg_petggreentransparent_1000_175_p": [
      "55057"
    ],
    "verbatim_petg_verbatimpetggreentransparent_1000_175_p": [
      "55057",
      "55065"
    ]
  }
}
```

### VB013: dup-40902be25aa2ca5a52af464d090e0193141eb9bb970d70ead2f34ff4d4eff54d

Status: DEFERRED; survivor `verbatim_petg_petgred_1000_175_p`; Mixed1.75/2.85 identifiers; extra55061 remains on live2.85 same-color row. Exact scoped reconciliation deferred..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_petg_petgred_1000_175_p`|`PETG {color_name}`|`Red`|{"source_file": "verbatim.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`verbatim_petg_verbatimpetgred_1000_175_p`|`Verbatim PETG {color_name}`|`Red`|{"source_file": "verbatim.json", "definition_index": 1, "weights": 1, "diameters": 2, "colors": 8, "compiled_records": 16} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_petg_petgred_1000_175_p": "E60000",
    "verbatim_petg_verbatimpetgred_1000_175_p": "ff0000"
  },
  "extruder_temp_range": {
    "verbatim_petg_petgred_1000_175_p": [
      220,
      250
    ],
    "verbatim_petg_verbatimpetgred_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "verbatim_petg_petgred_1000_175_p": [
      70,
      90
    ],
    "verbatim_petg_verbatimpetgred_1000_175_p": [
      60,
      90
    ]
  },
  "codes": {
    "verbatim_petg_petgred_1000_175_p": [
      "55053"
    ],
    "verbatim_petg_verbatimpetgred_1000_175_p": [
      "55053",
      "55061"
    ]
  }
}
```

### VB014: dup-d9942c4308dc20b5523b4a87f65430cd300ff11656654dea518f77e7771e4309

Status: DEFERRED; survivor `verbatim_petg_petgredtransparent_1000_175_p`; Mixed1.75/2.85 identifiers; extra55062 remains on live2.85 same-color row. Exact scoped reconciliation deferred..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_petg_petgredtransparent_1000_175_p`|`PETG {color_name}`|`Red Transparent`|{"source_file": "verbatim.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`verbatim_petg_verbatimpetgredtransparent_1000_175_p`|`Verbatim PETG {color_name}`|`Red Transparent`|{"source_file": "verbatim.json", "definition_index": 1, "weights": 1, "diameters": 2, "colors": 8, "compiled_records": 16} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_petg_petgredtransparent_1000_175_p": "E60000",
    "verbatim_petg_verbatimpetgredtransparent_1000_175_p": "a80000"
  },
  "extruder_temp_range": {
    "verbatim_petg_petgredtransparent_1000_175_p": [
      220,
      250
    ],
    "verbatim_petg_verbatimpetgredtransparent_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "verbatim_petg_petgredtransparent_1000_175_p": [
      70,
      90
    ],
    "verbatim_petg_verbatimpetgredtransparent_1000_175_p": [
      60,
      90
    ]
  },
  "codes": {
    "verbatim_petg_petgredtransparent_1000_175_p": [
      "55054"
    ],
    "verbatim_petg_verbatimpetgredtransparent_1000_175_p": [
      "55054",
      "55062"
    ]
  }
}
```

### VB015: dup-53de259b88029e9882283dc86539173a69bf3d7c4f63d9eede05753b3fbf400a

Status: DEFERRED; survivor `verbatim_petg_petgwhite_1000_175_p`; Mixed1.75/2.85 identifiers; extra55058 remains on live2.85 same-color row. Exact scoped reconciliation deferred..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_petg_petgwhite_1000_175_p`|`PETG {color_name}`|`White`|{"source_file": "verbatim.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`verbatim_petg_verbatimpetgwhite_1000_175_p`|`Verbatim PETG {color_name}`|`White`|{"source_file": "verbatim.json", "definition_index": 1, "weights": 1, "diameters": 2, "colors": 8, "compiled_records": 16} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_petg_petgwhite_1000_175_p": "FFFFFF",
    "verbatim_petg_verbatimpetgwhite_1000_175_p": "ffffff"
  },
  "extruder_temp_range": {
    "verbatim_petg_petgwhite_1000_175_p": [
      220,
      250
    ],
    "verbatim_petg_verbatimpetgwhite_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "verbatim_petg_petgwhite_1000_175_p": [
      70,
      90
    ],
    "verbatim_petg_verbatimpetgwhite_1000_175_p": [
      60,
      90
    ]
  },
  "codes": {
    "verbatim_petg_petgwhite_1000_175_p": [
      "55050"
    ],
    "verbatim_petg_verbatimpetgwhite_1000_175_p": [
      "55050",
      "55058"
    ]
  }
}
```

### VB016: dup-9163fbf93a953d28b3226e092326a189bdaebd32a1da11f6febf357a0e133ac1

Status: DEFERRED; survivor `verbatim_pla_plaaluminiumgrey_1000_175_p`; Mixed1.75/2.85 identifiers; extra55329 remains on live2.85 same-color row. Exact scoped reconciliation deferred..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_pla_plaaluminiumgrey_1000_175_p`|`PLA {color_name}`|`Aluminium Grey`|{"source_file": "verbatim.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`verbatim_pla_verbatimplaaluminiumgrey_1000_175_p`|`Verbatim PLA {color_name}`|`Aluminium Grey`|{"source_file": "verbatim.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 7, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_pla_plaaluminiumgrey_1000_175_p": "9F9F9F",
    "verbatim_pla_verbatimplaaluminiumgrey_1000_175_p": "666666"
  },
  "extruder_temp_range": {
    "verbatim_pla_plaaluminiumgrey_1000_175_p": [
      190,
      230
    ],
    "verbatim_pla_verbatimplaaluminiumgrey_1000_175_p": [
      200,
      220
    ]
  },
  "bed_temp": {
    "verbatim_pla_plaaluminiumgrey_1000_175_p": null,
    "verbatim_pla_verbatimplaaluminiumgrey_1000_175_p": 60
  },
  "bed_temp_range": {
    "verbatim_pla_plaaluminiumgrey_1000_175_p": [
      50,
      70
    ],
    "verbatim_pla_verbatimplaaluminiumgrey_1000_175_p": null
  },
  "codes": {
    "verbatim_pla_plaaluminiumgrey_1000_175_p": [
      "55319"
    ],
    "verbatim_pla_verbatimplaaluminiumgrey_1000_175_p": [
      "55319",
      "55329"
    ]
  }
}
```

### VB017: dup-412449b86e154448d27dd7a18791302edbb0f16c1c8ab245e7e3b19c7442aad9

Status: DEFERRED; survivor `verbatim_pla_plablack_1000_175_p`; Mixed1.75/2.85 identifiers; extra55327 is official2.85 SKU and remains on live2.85 same-color row. Exact scoped reconciliation deferred..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_pla_plablack_1000_175_p`|`PLA {color_name}`|`Black`|{"source_file": "verbatim.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`verbatim_pla_verbatimplablack_1000_175_p`|`Verbatim PLA {color_name}`|`Black`|{"source_file": "verbatim.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 7, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_pla_plablack_1000_175_p": "000000",
    "verbatim_pla_verbatimplablack_1000_175_p": "050505"
  },
  "extruder_temp_range": {
    "verbatim_pla_plablack_1000_175_p": [
      190,
      230
    ],
    "verbatim_pla_verbatimplablack_1000_175_p": [
      200,
      220
    ]
  },
  "bed_temp": {
    "verbatim_pla_plablack_1000_175_p": null,
    "verbatim_pla_verbatimplablack_1000_175_p": 60
  },
  "bed_temp_range": {
    "verbatim_pla_plablack_1000_175_p": [
      50,
      70
    ],
    "verbatim_pla_verbatimplablack_1000_175_p": null
  },
  "codes": {
    "verbatim_pla_plablack_1000_175_p": [
      "55318"
    ],
    "verbatim_pla_verbatimplablack_1000_175_p": [
      "55318",
      "55327"
    ]
  }
}
```

### VB018: dup-1856802471cdc1e19d9b8cca1dfff9de88b08193cb13b7491129daa0bc581f2b

Status: DEFERRED; survivor `verbatim_pla_plablue_1000_175_p`; Mixed1.75/2.85 identifiers; extra55332 remains on live2.85 same-color row. Exact scoped reconciliation deferred..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_pla_plablue_1000_175_p`|`PLA {color_name}`|`Blue`|{"source_file": "verbatim.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`verbatim_pla_verbatimplablue_1000_175_p`|`Verbatim PLA {color_name}`|`Blue`|{"source_file": "verbatim.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 7, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_pla_plablue_1000_175_p": "2C3294",
    "verbatim_pla_verbatimplablue_1000_175_p": "1900ff"
  },
  "extruder_temp_range": {
    "verbatim_pla_plablue_1000_175_p": [
      190,
      230
    ],
    "verbatim_pla_verbatimplablue_1000_175_p": [
      200,
      220
    ]
  },
  "bed_temp": {
    "verbatim_pla_plablue_1000_175_p": null,
    "verbatim_pla_verbatimplablue_1000_175_p": 60
  },
  "bed_temp_range": {
    "verbatim_pla_plablue_1000_175_p": [
      50,
      70
    ],
    "verbatim_pla_verbatimplablue_1000_175_p": null
  },
  "codes": {
    "verbatim_pla_plablue_1000_175_p": [
      "55322"
    ],
    "verbatim_pla_verbatimplablue_1000_175_p": [
      "55322",
      "55332"
    ]
  }
}
```

### VB019: dup-7822572373cbe8760cc16ac5ec1a80a0be346dbff5b467507e4e1f9bfbe0213d

Status: DEFERRED; survivor `verbatim_pla_plagreen_1000_175_p`; Mixed1.75/2.85 identifiers; extra55334 remains on live2.85 same-color row. Exact scoped reconciliation deferred..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_pla_plagreen_1000_175_p`|`PLA {color_name}`|`Green`|{"source_file": "verbatim.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`verbatim_pla_verbatimplagreen_1000_175_p`|`Verbatim PLA {color_name}`|`Green`|{"source_file": "verbatim.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 7, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_pla_plagreen_1000_175_p": "739549",
    "verbatim_pla_verbatimplagreen_1000_175_p": "005900"
  },
  "extruder_temp_range": {
    "verbatim_pla_plagreen_1000_175_p": [
      190,
      230
    ],
    "verbatim_pla_verbatimplagreen_1000_175_p": [
      200,
      220
    ]
  },
  "bed_temp": {
    "verbatim_pla_plagreen_1000_175_p": null,
    "verbatim_pla_verbatimplagreen_1000_175_p": 60
  },
  "bed_temp_range": {
    "verbatim_pla_plagreen_1000_175_p": [
      50,
      70
    ],
    "verbatim_pla_verbatimplagreen_1000_175_p": null
  },
  "codes": {
    "verbatim_pla_plagreen_1000_175_p": [
      "55324"
    ],
    "verbatim_pla_verbatimplagreen_1000_175_p": [
      "55324",
      "55334"
    ]
  }
}
```

### VB020: dup-2dd92bbc8ca2e789e523c9689bfc4725a5b0a8d5727d6749707a4a20daf08e00

Status: APPROVED; survivor `verbatim_pla_planatural/transparent_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_pla_planatural/transparent_1000_175_p`|`PLA {color_name}`|`Natural/Transparent`|{"source_file": "verbatim.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`verbatim_pla_verbatimplanaturaltransparent_1000_175_p`|`Verbatim PLA {color_name}`|`Natural Transparent`|{"source_file": "verbatim.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 7, "compiled_records": 14} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_pla_planatural/transparent_1000_175_p": "DFDFD3",
    "verbatim_pla_verbatimplanaturaltransparent_1000_175_p": "dbfbff"
  },
  "extruder_temp_range": {
    "verbatim_pla_planatural/transparent_1000_175_p": [
      190,
      230
    ],
    "verbatim_pla_verbatimplanaturaltransparent_1000_175_p": [
      200,
      220
    ]
  },
  "bed_temp": {
    "verbatim_pla_planatural/transparent_1000_175_p": null,
    "verbatim_pla_verbatimplanaturaltransparent_1000_175_p": 60
  },
  "bed_temp_range": {
    "verbatim_pla_planatural/transparent_1000_175_p": [
      50,
      70
    ],
    "verbatim_pla_verbatimplanaturaltransparent_1000_175_p": null
  },
  "translucent": {
    "verbatim_pla_planatural/transparent_1000_175_p": false,
    "verbatim_pla_verbatimplanaturaltransparent_1000_175_p": true
  }
}
```

### VB021: dup-79c4cd5b2ab7e35b99eaa45d8ec77988ff90e819454c2b4726acfdc99b8de4a7

Status: DEFERRED; survivor `verbatim_pla_plared_1000_175_p`; Mixed1.75/2.85 identifiers; extra55330 remains on live2.85 same-color row. Exact scoped reconciliation deferred..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_pla_plared_1000_175_p`|`PLA {color_name}`|`Red`|{"source_file": "verbatim.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`verbatim_pla_verbatimplared_1000_175_p`|`Verbatim PLA {color_name}`|`Red`|{"source_file": "verbatim.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 7, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_pla_plared_1000_175_p": "E60000",
    "verbatim_pla_verbatimplared_1000_175_p": "ff0000"
  },
  "extruder_temp_range": {
    "verbatim_pla_plared_1000_175_p": [
      190,
      230
    ],
    "verbatim_pla_verbatimplared_1000_175_p": [
      200,
      220
    ]
  },
  "bed_temp": {
    "verbatim_pla_plared_1000_175_p": null,
    "verbatim_pla_verbatimplared_1000_175_p": 60
  },
  "bed_temp_range": {
    "verbatim_pla_plared_1000_175_p": [
      50,
      70
    ],
    "verbatim_pla_verbatimplared_1000_175_p": null
  },
  "codes": {
    "verbatim_pla_plared_1000_175_p": [
      "55320"
    ],
    "verbatim_pla_verbatimplared_1000_175_p": [
      "55320",
      "55330"
    ]
  }
}
```

### VB022: dup-5d4662bb618df683afb0fc46d9fa20bb83df6bc89c11c3dcc4f29399b097020c

Status: DEFERRED; survivor `verbatim_pla_plawhite_1000_175_p`; Mixed1.75/2.85 identifiers; extra55328 remains on live2.85 same-color row. Exact scoped reconciliation deferred..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`verbatim_pla_plawhite_1000_175_p`|`PLA {color_name}`|`White`|{"source_file": "verbatim.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`verbatim_pla_verbatimplawhite_1000_175_p`|`Verbatim PLA {color_name}`|`White`|{"source_file": "verbatim.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 7, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "verbatim_pla_plawhite_1000_175_p": "FFFFFF",
    "verbatim_pla_verbatimplawhite_1000_175_p": "ffffff"
  },
  "extruder_temp_range": {
    "verbatim_pla_plawhite_1000_175_p": [
      190,
      230
    ],
    "verbatim_pla_verbatimplawhite_1000_175_p": [
      200,
      220
    ]
  },
  "bed_temp": {
    "verbatim_pla_plawhite_1000_175_p": null,
    "verbatim_pla_verbatimplawhite_1000_175_p": 60
  },
  "bed_temp_range": {
    "verbatim_pla_plawhite_1000_175_p": [
      50,
      70
    ],
    "verbatim_pla_verbatimplawhite_1000_175_p": null
  },
  "codes": {
    "verbatim_pla_plawhite_1000_175_p": [
      "55315"
    ],
    "verbatim_pla_verbatimplawhite_1000_175_p": [
      "55315",
      "55328"
    ]
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "verbatim_petg_petgbluetransparent_1000_175_p",
      "values": {
        "extruder_temp_range": [
          225,
          245
        ],
        "bed_temp_range": null,
        "bed_temp": 90
      },
      "source": "https://www.verbatim-europe.com/en/3d/products/verbatim-pet-g-filament-175-mm-black-55052",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "verbatim_pla_planatural/transparent_1000_175_p",
      "values": {
        "extruder_temp_range": [
          200,
          220
        ],
        "bed_temp_range": null,
        "bed_temp": 60
      },
      "source": "https://www.verbatim-europe.com/en/3d/products/verbatim-pla-filament-175mm-1kg-black-55318",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "verbatim_abs_absgreen_1000_175_p",
      "values": {
        "extruder_temp_range": [
          240,
          260
        ],
        "bed_temp_range": null,
        "bed_temp": 90
      },
      "source": "https://www.verbatim-europe.com/en/3d/products/verbatim-abs-filament-175mm-1kg-black-55026",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "verbatim_abs_absblue_1000_175_p",
      "values": {
        "extruder_temp_range": [
          240,
          260
        ],
        "bed_temp_range": null,
        "bed_temp": 90
      },
      "source": "https://www.verbatim-europe.com/en/3d/products/verbatim-abs-filament-175mm-1kg-black-55026",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "verbatim_abs_absred_1000_175_p",
      "values": {
        "extruder_temp_range": [
          240,
          260
        ],
        "bed_temp_range": null,
        "bed_temp": 90
      },
      "source": "https://www.verbatim-europe.com/en/3d/products/verbatim-abs-filament-175mm-1kg-black-55026",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    }
  ],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `verbatim_pla_verbatimplablack_1000_285_p` — Verbatim PLA Black
- `verbatim_pla_verbatimplawhite_1000_285_p` — Verbatim PLA White
- `verbatim_pla_verbatimplanaturaltransparent_1000_285_p` — Verbatim PLA Natural Transparent
- `verbatim_pla_verbatimplared_1000_285_p` — Verbatim PLA Red
- `verbatim_pla_verbatimplagreen_1000_285_p` — Verbatim PLA Green
- `verbatim_pla_verbatimplaaluminiumgrey_1000_285_p` — Verbatim PLA Aluminium Grey
- `verbatim_pla_verbatimplablue_1000_285_p` — Verbatim PLA Blue
- `verbatim_petg_verbatimpetgblack_1000_285_p` — Verbatim PETG Black
- `verbatim_petg_verbatimpetgwhite_1000_285_p` — Verbatim PETG White
- `verbatim_petg_verbatimpetgred_1000_285_p` — Verbatim PETG Red
- `verbatim_petg_verbatimpetgblue_1000_285_p` — Verbatim PETG Blue
- `verbatim_petg_verbatimpetgclear_1000_285_p` — Verbatim PETG Clear
- `verbatim_petg_verbatimpetgredtransparent_1000_285_p` — Verbatim PETG Red Transparent
- `verbatim_petg_verbatimpetgbluetransparent_1000_285_p` — Verbatim PETG Blue Transparent
- `verbatim_petg_verbatimpetggreentransparent_1000_285_p` — Verbatim PETG Green Transparent
- `verbatim_abs_verbatimabsblack_1000_285_p` — Verbatim ABS Black
- `verbatim_abs_verbatimabswhite_1000_285_p` — Verbatim ABS White
- `verbatim_abs_verbatimabsnaturalmilky_1000_285_p` — Verbatim ABS Natural Milky
- `verbatim_abs_verbatimabsred_1000_285_p` — Verbatim ABS Red
- `verbatim_abs_verbatimabsgreen_1000_285_p` — Verbatim ABS Green
- `verbatim_abs_verbatimabsaluminiumgrey_1000_285_p` — Verbatim ABS Aluminium Grey
- `verbatim_abs_verbatimabsblue_1000_285_p` — Verbatim ABS Blue
- `verbatim_bvoh_bvohnatural_1000_175_p` — BVOH Natural
- `verbatim_pp_ppnatural_1000_175_p` — PP Natural
- `verbatim_tpe_tefabloctpeblack_1000_175_p` — Tefabloc TPE Black
- `verbatim_tpe_tefabloctpewhite_1000_175_p` — Tefabloc TPE White
