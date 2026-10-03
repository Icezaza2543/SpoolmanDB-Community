# aurapol duplicate migration review

Base `adb7d3aa95e48f68d5a2c7d7fbb10afea7423e3e`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `67d4750cdbb32e1295ef7969e60418a2fb6029d47d7593ed86d04b6aafb914e7`.

## Authorization and result

{"groups": 18, "approved_groups": 15, "retired": 15, "deferred": 3, "hard_stops": 0, "before_count": 51841, "after_count": 51826, "brand_before": 142, "brand_after": 127, "registry_before": 1593, "registry_after": 1608, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Current exact ordinary PLA/PET-G printing ranges match survivors; existing densities1.223/1.259 retained unresolved, no generic replacements. Metallic Brick and L-EGO Red/Yellow qualifier line/color splits deferred by strict Rule5. Ordinary cross-template HEX/translucency conflicts kept unresolved. Packaging/tare unchanged.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://www.aurapol.com/p/aurapol-pla-3d-filament-black-1-kg-1-75-mm", "nozzle": [210, 240], "bed": [40, 60]}
- {"url": "https://www.aurapol.com/p/aurapol-pet-g-filament-graphite-black-1-kg-1-75-mm", "nozzle": [245, 255], "bed": [85, 95]}
- {"url": "https://drive.google.com/file/d/1lMZzndGU3eidKYi9jWhx-IDMQcEBbeH1/view?usp=sharing", "status": "linked current PLA TDS; contents inaccessible, density unverified"}
- {"url": "https://drive.google.com/file/d/1eYryaiw7-c5AxGmrCDw6SFeDG9_S2wsp/view?usp=sharing", "status": "linked current PET-G TDS; contents inaccessible, density unverified"}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`aurapol_petg_petggraphiteblack_1000_175_p`|`aurapol_petg_graphiteblack_1000_175_p`|`aurapol.json::AURAPOL::PETG {color_name}::PETG Graphite black::PETG::1000::1.75::plastic::False`|
|`aurapol_petg_petggreenmint_1000_175_p`|`aurapol_petg_greenmint_1000_175_p`|`aurapol.json::AURAPOL::PETG {color_name}::PETG Green Mint::PETG::1000::1.75::plastic::False`|
|`aurapol_petg_petgnaturaltransparent_1000_175_p`|`aurapol_petg_naturaltransparent_1000_175_p`|`aurapol.json::AURAPOL::PETG {color_name}::PETG Natural transparent::PETG::1000::1.75::plastic::False`|
|`aurapol_petg_petgsignalblue_1000_175_p`|`aurapol_petg_signalblue_1000_175_p`|`aurapol.json::AURAPOL::PETG {color_name}::PETG Signal Blue::PETG::1000::1.75::plastic::False`|
|`aurapol_petg_petgsignalgrey_1000_175_p`|`aurapol_petg_signalgrey_1000_175_p`|`aurapol.json::AURAPOL::PETG {color_name}::PETG Signal Grey::PETG::1000::1.75::plastic::False`|
|`aurapol_petg_petgsulfuryellow_1000_175_p`|`aurapol_petg_sulfuryellow_1000_175_p`|`aurapol.json::AURAPOL::PETG {color_name}::PETG Sulfur Yellow::PETG::1000::1.75::plastic::False`|
|`aurapol_petg_petgtrafficred_1000_175_p`|`aurapol_petg_trafficred_1000_175_p`|`aurapol.json::AURAPOL::PETG {color_name}::PETG Traffic Red::PETG::1000::1.75::plastic::False`|
|`aurapol_petg_petgwhite_1000_175_p`|`aurapol_petg_white_1000_175_p`|`aurapol.json::AURAPOL::PETG {color_name}::PETG White::PETG::1000::1.75::plastic::False`|
|`aurapol_pla_plablack_1000_175_p`|`aurapol_pla_black_1000_175_p`|`aurapol.json::AURAPOL::PLA {color_name}::PLA Black::PLA::1000::1.75::plastic::False`|
|`aurapol_pla_plagrey_1000_175_p`|`aurapol_pla_grey_1000_175_p`|`aurapol.json::AURAPOL::PLA {color_name}::PLA Grey::PLA::1000::1.75::plastic::False`|
|`aurapol_pla_plaleafgreen_1000_175_p`|`aurapol_pla_leafgreen_1000_175_p`|`aurapol.json::AURAPOL::PLA {color_name}::PLA leaf green::PLA::1000::1.75::plastic::False`|
|`aurapol_pla_planatural_1000_175_p`|`aurapol_pla_natural_1000_175_p`|`aurapol.json::AURAPOL::PLA {color_name}::PLA Natural::PLA::1000::1.75::plastic::False`|
|`aurapol_pla_plaraspberrypartiallytransparent_1000_175_p`|`aurapol_pla_raspberrypartiallytransparent_1000_175_p`|`aurapol.json::AURAPOL::PLA {color_name}::PLA Raspberry partially transparent::PLA::1000::1.75::plastic::False`|
|`aurapol_pla_plawhite_1000_175_p`|`aurapol_pla_white_1000_175_p`|`aurapol.json::AURAPOL::PLA {color_name}::PLA White::PLA::1000::1.75::plastic::False`|
|`aurapol_pla_playellowgreen_1000_175_p`|`aurapol_pla_yellowgreen_1000_175_p`|`aurapol.json::AURAPOL::PLA {color_name}::PLA Yellow Green::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### AU001: dup-084366e96bb70abbfbaf69c4be2dc8c3591e2db37fcad1f1850115c28ffd62f8

Status: APPROVED; survivor `aurapol_petg_graphiteblack_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aurapol_petg_graphiteblack_1000_175_p`|`{color_name}`|`Graphite black`|{"source_file": "aurapol.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|
|`aurapol_petg_petggraphiteblack_1000_175_p`|`PETG {color_name}`|`Graphite black`|{"source_file": "aurapol.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "aurapol_petg_graphiteblack_1000_175_p": 1.259,
    "aurapol_petg_petggraphiteblack_1000_175_p": 1.27
  },
  "spool_weight": {
    "aurapol_petg_graphiteblack_1000_175_p": 250.0,
    "aurapol_petg_petggraphiteblack_1000_175_p": null
  },
  "color_hex": {
    "aurapol_petg_graphiteblack_1000_175_p": "101010",
    "aurapol_petg_petggraphiteblack_1000_175_p": "1D1D1D"
  },
  "extruder_temp_range": {
    "aurapol_petg_graphiteblack_1000_175_p": [
      245,
      255
    ],
    "aurapol_petg_petggraphiteblack_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "aurapol_petg_graphiteblack_1000_175_p": [
      85,
      95
    ],
    "aurapol_petg_petggraphiteblack_1000_175_p": [
      70,
      90
    ]
  }
}
```

### AU002: dup-0c732bc93afb7527ef279c09a45e180f22f8077a7534f153a251377b2a6d0b60

Status: APPROVED; survivor `aurapol_petg_greenmint_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aurapol_petg_greenmint_1000_175_p`|`{color_name}`|`Green Mint`|{"source_file": "aurapol.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|
|`aurapol_petg_petggreenmint_1000_175_p`|`PETG {color_name}`|`Green Mint`|{"source_file": "aurapol.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "aurapol_petg_greenmint_1000_175_p": 1.259,
    "aurapol_petg_petggreenmint_1000_175_p": 1.27
  },
  "spool_weight": {
    "aurapol_petg_greenmint_1000_175_p": 250.0,
    "aurapol_petg_petggreenmint_1000_175_p": null
  },
  "color_hex": {
    "aurapol_petg_greenmint_1000_175_p": "00ff00",
    "aurapol_petg_petggreenmint_1000_175_p": "26A648"
  },
  "extruder_temp_range": {
    "aurapol_petg_greenmint_1000_175_p": [
      245,
      255
    ],
    "aurapol_petg_petggreenmint_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "aurapol_petg_greenmint_1000_175_p": [
      85,
      95
    ],
    "aurapol_petg_petggreenmint_1000_175_p": [
      70,
      90
    ]
  }
}
```

### AU003: dup-d8019ddd62b2dd66f66bbe6bd72ecd60675d45c6b5735e5e25d56e057159eadd

Status: APPROVED; survivor `aurapol_petg_naturaltransparent_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aurapol_petg_naturaltransparent_1000_175_p`|`{color_name}`|`Natural transparent`|{"source_file": "aurapol.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|
|`aurapol_petg_petgnaturaltransparent_1000_175_p`|`PETG {color_name}`|`Natural transparent`|{"source_file": "aurapol.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "aurapol_petg_naturaltransparent_1000_175_p": 1.259,
    "aurapol_petg_petgnaturaltransparent_1000_175_p": 1.27
  },
  "spool_weight": {
    "aurapol_petg_naturaltransparent_1000_175_p": 250.0,
    "aurapol_petg_petgnaturaltransparent_1000_175_p": null
  },
  "color_hex": {
    "aurapol_petg_naturaltransparent_1000_175_p": "ffffff",
    "aurapol_petg_petgnaturaltransparent_1000_175_p": "DEE2DA"
  },
  "extruder_temp_range": {
    "aurapol_petg_naturaltransparent_1000_175_p": [
      245,
      255
    ],
    "aurapol_petg_petgnaturaltransparent_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "aurapol_petg_naturaltransparent_1000_175_p": [
      85,
      95
    ],
    "aurapol_petg_petgnaturaltransparent_1000_175_p": [
      70,
      90
    ]
  }
}
```

### AU004: dup-eac54a11c33362d1019355d8ef50b1460de6077a878c71a9805d32ccd11c2d8b

Status: APPROVED; survivor `aurapol_petg_signalblue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aurapol_petg_petgsignalblue_1000_175_p`|`PETG {color_name}`|`Signal Blue`|{"source_file": "aurapol.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|
|`aurapol_petg_signalblue_1000_175_p`|`{color_name}`|`Signal blue`|{"source_file": "aurapol.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "aurapol_petg_petgsignalblue_1000_175_p": 1.27,
    "aurapol_petg_signalblue_1000_175_p": 1.259
  },
  "spool_weight": {
    "aurapol_petg_petgsignalblue_1000_175_p": null,
    "aurapol_petg_signalblue_1000_175_p": 250.0
  },
  "color_hex": {
    "aurapol_petg_petgsignalblue_1000_175_p": "346CE3",
    "aurapol_petg_signalblue_1000_175_p": "0000ff"
  },
  "extruder_temp_range": {
    "aurapol_petg_petgsignalblue_1000_175_p": [
      220,
      250
    ],
    "aurapol_petg_signalblue_1000_175_p": [
      245,
      255
    ]
  },
  "bed_temp_range": {
    "aurapol_petg_petgsignalblue_1000_175_p": [
      70,
      90
    ],
    "aurapol_petg_signalblue_1000_175_p": [
      85,
      95
    ]
  }
}
```

### AU005: dup-59feb361ff85bfab4d6537d8e6a63e64b4aef7d627afb734c92d6b9438bc258a

Status: APPROVED; survivor `aurapol_petg_signalgrey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aurapol_petg_petgsignalgrey_1000_175_p`|`PETG {color_name}`|`Signal Grey`|{"source_file": "aurapol.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|
|`aurapol_petg_signalgrey_1000_175_p`|`{color_name}`|`Signal Grey`|{"source_file": "aurapol.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "aurapol_petg_petgsignalgrey_1000_175_p": 1.27,
    "aurapol_petg_signalgrey_1000_175_p": 1.259
  },
  "spool_weight": {
    "aurapol_petg_petgsignalgrey_1000_175_p": null,
    "aurapol_petg_signalgrey_1000_175_p": 250.0
  },
  "color_hex": {
    "aurapol_petg_petgsignalgrey_1000_175_p": "DED9D4",
    "aurapol_petg_signalgrey_1000_175_p": "7f7f7f"
  },
  "extruder_temp_range": {
    "aurapol_petg_petgsignalgrey_1000_175_p": [
      220,
      250
    ],
    "aurapol_petg_signalgrey_1000_175_p": [
      245,
      255
    ]
  },
  "bed_temp_range": {
    "aurapol_petg_petgsignalgrey_1000_175_p": [
      70,
      90
    ],
    "aurapol_petg_signalgrey_1000_175_p": [
      85,
      95
    ]
  }
}
```

### AU006: dup-a24374fbd21a7cc4ca2726af34b3943ad45f0b117d76833ea9211f79a3d08d8d

Status: APPROVED; survivor `aurapol_petg_sulfuryellow_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aurapol_petg_petgsulfuryellow_1000_175_p`|`PETG {color_name}`|`Sulfur Yellow`|{"source_file": "aurapol.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|
|`aurapol_petg_sulfuryellow_1000_175_p`|`{color_name}`|`Sulfur Yellow`|{"source_file": "aurapol.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "aurapol_petg_petgsulfuryellow_1000_175_p": 1.27,
    "aurapol_petg_sulfuryellow_1000_175_p": 1.259
  },
  "spool_weight": {
    "aurapol_petg_petgsulfuryellow_1000_175_p": null,
    "aurapol_petg_sulfuryellow_1000_175_p": 250.0
  },
  "color_hex": {
    "aurapol_petg_petgsulfuryellow_1000_175_p": "E4FF33",
    "aurapol_petg_sulfuryellow_1000_175_p": "ffff00"
  },
  "extruder_temp_range": {
    "aurapol_petg_petgsulfuryellow_1000_175_p": [
      220,
      250
    ],
    "aurapol_petg_sulfuryellow_1000_175_p": [
      245,
      255
    ]
  },
  "bed_temp_range": {
    "aurapol_petg_petgsulfuryellow_1000_175_p": [
      70,
      90
    ],
    "aurapol_petg_sulfuryellow_1000_175_p": [
      85,
      95
    ]
  }
}
```

### AU007: dup-d52393c2698a4dc56e3af3811e5cdd8b4ce07243e6a9f47dca529992f42a6fb3

Status: APPROVED; survivor `aurapol_petg_trafficred_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aurapol_petg_petgtrafficred_1000_175_p`|`PETG {color_name}`|`Traffic Red`|{"source_file": "aurapol.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|
|`aurapol_petg_trafficred_1000_175_p`|`{color_name}`|`Traffic Red`|{"source_file": "aurapol.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "aurapol_petg_petgtrafficred_1000_175_p": 1.27,
    "aurapol_petg_trafficred_1000_175_p": 1.259
  },
  "spool_weight": {
    "aurapol_petg_petgtrafficred_1000_175_p": null,
    "aurapol_petg_trafficred_1000_175_p": 250.0
  },
  "color_hex": {
    "aurapol_petg_petgtrafficred_1000_175_p": "E03F26",
    "aurapol_petg_trafficred_1000_175_p": "ff0000"
  },
  "extruder_temp_range": {
    "aurapol_petg_petgtrafficred_1000_175_p": [
      220,
      250
    ],
    "aurapol_petg_trafficred_1000_175_p": [
      245,
      255
    ]
  },
  "bed_temp_range": {
    "aurapol_petg_petgtrafficred_1000_175_p": [
      70,
      90
    ],
    "aurapol_petg_trafficred_1000_175_p": [
      85,
      95
    ]
  }
}
```

### AU008: dup-b328b866dd20ade9ffe8ab884d5698fd9962cd0a5241a5fff8a1c253d741ca6c

Status: APPROVED; survivor `aurapol_petg_white_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aurapol_petg_petgwhite_1000_175_p`|`PETG {color_name}`|`White`|{"source_file": "aurapol.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / False|
|`aurapol_petg_white_1000_175_p`|`{color_name}`|`White`|{"source_file": "aurapol.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "aurapol_petg_petgwhite_1000_175_p": 1.27,
    "aurapol_petg_white_1000_175_p": 1.259
  },
  "spool_weight": {
    "aurapol_petg_petgwhite_1000_175_p": null,
    "aurapol_petg_white_1000_175_p": 250.0
  },
  "color_hex": {
    "aurapol_petg_petgwhite_1000_175_p": "EFEFEF",
    "aurapol_petg_white_1000_175_p": "ffffff"
  },
  "extruder_temp_range": {
    "aurapol_petg_petgwhite_1000_175_p": [
      220,
      250
    ],
    "aurapol_petg_white_1000_175_p": [
      245,
      255
    ]
  },
  "bed_temp_range": {
    "aurapol_petg_petgwhite_1000_175_p": [
      70,
      90
    ],
    "aurapol_petg_white_1000_175_p": [
      85,
      95
    ]
  }
}
```

### AU009: dup-e3611d9f6a953e2ac8d0475c006a832433218dd5f9c37e2bdb88fd87f0f342b8

Status: APPROVED; survivor `aurapol_pla_black_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aurapol_pla_black_1000_175_p`|`{color_name}`|`Black`|{"source_file": "aurapol.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|
|`aurapol_pla_plablack_1000_175_p`|`PLA {color_name}`|`Black`|{"source_file": "aurapol.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 52, "compiled_records": 52} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "aurapol_pla_black_1000_175_p": 1.223,
    "aurapol_pla_plablack_1000_175_p": 1.24
  },
  "spool_weight": {
    "aurapol_pla_black_1000_175_p": 250.0,
    "aurapol_pla_plablack_1000_175_p": null
  },
  "extruder_temp_range": {
    "aurapol_pla_black_1000_175_p": [
      210,
      240
    ],
    "aurapol_pla_plablack_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "aurapol_pla_black_1000_175_p": [
      40,
      60
    ],
    "aurapol_pla_plablack_1000_175_p": [
      50,
      70
    ]
  }
}
```

### AU010: dup-6132edef8148d7606ed621750aeb8c4ab19352e7bbb8d9d81ca235f3223baebf

Status: APPROVED; survivor `aurapol_pla_grey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aurapol_pla_grey_1000_175_p`|`{color_name}`|`Grey`|{"source_file": "aurapol.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|
|`aurapol_pla_plagrey_1000_175_p`|`PLA {color_name}`|`Grey`|{"source_file": "aurapol.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 52, "compiled_records": 52} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "aurapol_pla_grey_1000_175_p": 1.223,
    "aurapol_pla_plagrey_1000_175_p": 1.24
  },
  "spool_weight": {
    "aurapol_pla_grey_1000_175_p": 250.0,
    "aurapol_pla_plagrey_1000_175_p": null
  },
  "color_hex": {
    "aurapol_pla_grey_1000_175_p": "7f7f7f",
    "aurapol_pla_plagrey_1000_175_p": "C5C7C4"
  },
  "extruder_temp_range": {
    "aurapol_pla_grey_1000_175_p": [
      210,
      240
    ],
    "aurapol_pla_plagrey_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "aurapol_pla_grey_1000_175_p": [
      40,
      60
    ],
    "aurapol_pla_plagrey_1000_175_p": [
      50,
      70
    ]
  }
}
```

### AU011: dup-7f4f5cdbeb4d3f3dda13bb1df31d31ac91cc54ebdd56600d702b3fcc1077fba5

Status: DEFERRED; survivor `aurapol_pla_l-egored_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aurapol_pla_l-egoplared_1000_175_p`|`L-EGO PLA {color_name}`|`Red`|{"source_file": "aurapol.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`aurapol_pla_l-egored_1000_175_p`|`{color_name}`|`L-EGO red`|{"source_file": "aurapol.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "aurapol_pla_l-egoplared_1000_175_p": 1.24,
    "aurapol_pla_l-egored_1000_175_p": 1.223
  },
  "spool_weight": {
    "aurapol_pla_l-egoplared_1000_175_p": null,
    "aurapol_pla_l-egored_1000_175_p": 250.0
  },
  "color_hex": {
    "aurapol_pla_l-egoplared_1000_175_p": "E72F1D",
    "aurapol_pla_l-egored_1000_175_p": "ff0000"
  },
  "extruder_temp_range": {
    "aurapol_pla_l-egoplared_1000_175_p": [
      190,
      230
    ],
    "aurapol_pla_l-egored_1000_175_p": [
      210,
      240
    ]
  },
  "bed_temp_range": {
    "aurapol_pla_l-egoplared_1000_175_p": [
      50,
      70
    ],
    "aurapol_pla_l-egored_1000_175_p": [
      40,
      60
    ]
  }
}
```

### AU012: dup-97d4093cd5eeb5abae12521b13d5af41ff7e37eb0ba23bc6af862e543e513044

Status: DEFERRED; survivor `aurapol_pla_l-egoyellow_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aurapol_pla_l-egoplayellow_1000_175_p`|`L-EGO PLA {color_name}`|`Yellow`|{"source_file": "aurapol.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`aurapol_pla_l-egoyellow_1000_175_p`|`{color_name}`|`L-EGO yellow`|{"source_file": "aurapol.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "aurapol_pla_l-egoplayellow_1000_175_p": 1.24,
    "aurapol_pla_l-egoyellow_1000_175_p": 1.223
  },
  "spool_weight": {
    "aurapol_pla_l-egoplayellow_1000_175_p": null,
    "aurapol_pla_l-egoyellow_1000_175_p": 250.0
  },
  "color_hex": {
    "aurapol_pla_l-egoplayellow_1000_175_p": "FFFC25",
    "aurapol_pla_l-egoyellow_1000_175_p": "ffff00"
  },
  "extruder_temp_range": {
    "aurapol_pla_l-egoplayellow_1000_175_p": [
      190,
      230
    ],
    "aurapol_pla_l-egoyellow_1000_175_p": [
      210,
      240
    ]
  },
  "bed_temp_range": {
    "aurapol_pla_l-egoplayellow_1000_175_p": [
      50,
      70
    ],
    "aurapol_pla_l-egoyellow_1000_175_p": [
      40,
      60
    ]
  }
}
```

### AU013: dup-334c1a0b8083207c5070015eca76a411b8bdb8664eb584603dc3f1aea40e151c

Status: APPROVED; survivor `aurapol_pla_leafgreen_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aurapol_pla_leafgreen_1000_175_p`|`{color_name}`|`leaf green`|{"source_file": "aurapol.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|
|`aurapol_pla_plaleafgreen_1000_175_p`|`PLA {color_name}`|`leaf green`|{"source_file": "aurapol.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 52, "compiled_records": 52} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "aurapol_pla_leafgreen_1000_175_p": 1.223,
    "aurapol_pla_plaleafgreen_1000_175_p": 1.24
  },
  "spool_weight": {
    "aurapol_pla_leafgreen_1000_175_p": 250.0,
    "aurapol_pla_plaleafgreen_1000_175_p": null
  },
  "color_hex": {
    "aurapol_pla_leafgreen_1000_175_p": "00a000",
    "aurapol_pla_plaleafgreen_1000_175_p": "446B20"
  },
  "extruder_temp_range": {
    "aurapol_pla_leafgreen_1000_175_p": [
      210,
      240
    ],
    "aurapol_pla_plaleafgreen_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "aurapol_pla_leafgreen_1000_175_p": [
      40,
      60
    ],
    "aurapol_pla_plaleafgreen_1000_175_p": [
      50,
      70
    ]
  }
}
```

### AU014: dup-382b48f7726f9762bebd8fbb9b3023c247357d6b0d7a60fa62125f6598a6f33a

Status: DEFERRED; survivor `aurapol_pla_metallicbrick_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aurapol_pla_metallicbrick_1000_175_p`|`{color_name}`|`Metallic Brick`|{"source_file": "aurapol.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|
|`aurapol_pla_metallicplabrick_1000_175_p`|`Metallic PLA {color_name}`|`Brick`|{"source_file": "aurapol.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "aurapol_pla_metallicbrick_1000_175_p": 1.223,
    "aurapol_pla_metallicplabrick_1000_175_p": 1.24
  },
  "spool_weight": {
    "aurapol_pla_metallicbrick_1000_175_p": 250.0,
    "aurapol_pla_metallicplabrick_1000_175_p": null
  },
  "color_hex": {
    "aurapol_pla_metallicbrick_1000_175_p": "ff4010",
    "aurapol_pla_metallicplabrick_1000_175_p": "C65E0A"
  },
  "extruder_temp_range": {
    "aurapol_pla_metallicbrick_1000_175_p": [
      210,
      240
    ],
    "aurapol_pla_metallicplabrick_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "aurapol_pla_metallicbrick_1000_175_p": [
      40,
      60
    ],
    "aurapol_pla_metallicplabrick_1000_175_p": [
      50,
      70
    ]
  }
}
```

### AU015: dup-f82563083cc2e26f8cc9b21feacb3cb18b25bfa206b763b70a1f558b7f9cac2f

Status: APPROVED; survivor `aurapol_pla_natural_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aurapol_pla_natural_1000_175_p`|`{color_name}`|`Natural`|{"source_file": "aurapol.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|
|`aurapol_pla_planatural_1000_175_p`|`PLA {color_name}`|`Natural`|{"source_file": "aurapol.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 52, "compiled_records": 52} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "aurapol_pla_natural_1000_175_p": 1.223,
    "aurapol_pla_planatural_1000_175_p": 1.24
  },
  "spool_weight": {
    "aurapol_pla_natural_1000_175_p": 250.0,
    "aurapol_pla_planatural_1000_175_p": null
  },
  "color_hex": {
    "aurapol_pla_natural_1000_175_p": "ffffff",
    "aurapol_pla_planatural_1000_175_p": "DFDFD3"
  },
  "extruder_temp_range": {
    "aurapol_pla_natural_1000_175_p": [
      210,
      240
    ],
    "aurapol_pla_planatural_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "aurapol_pla_natural_1000_175_p": [
      40,
      60
    ],
    "aurapol_pla_planatural_1000_175_p": [
      50,
      70
    ]
  }
}
```

### AU016: dup-d024f25d942e012c15446ee54d04a7b4cfa2cfcff9dd4a7c6c7fcd60e9f9bff2

Status: APPROVED; survivor `aurapol_pla_raspberrypartiallytransparent_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aurapol_pla_plaraspberrypartiallytransparent_1000_175_p`|`PLA {color_name}`|`Raspberry partially transparent`|{"source_file": "aurapol.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 52, "compiled_records": 52} / False|
|`aurapol_pla_raspberrypartiallytransparent_1000_175_p`|`{color_name}`|`Raspberry partially transparent`|{"source_file": "aurapol.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "aurapol_pla_plaraspberrypartiallytransparent_1000_175_p": 1.24,
    "aurapol_pla_raspberrypartiallytransparent_1000_175_p": 1.223
  },
  "spool_weight": {
    "aurapol_pla_plaraspberrypartiallytransparent_1000_175_p": null,
    "aurapol_pla_raspberrypartiallytransparent_1000_175_p": 250.0
  },
  "color_hex": {
    "aurapol_pla_plaraspberrypartiallytransparent_1000_175_p": "B13566",
    "aurapol_pla_raspberrypartiallytransparent_1000_175_p": "ff2060"
  },
  "extruder_temp_range": {
    "aurapol_pla_plaraspberrypartiallytransparent_1000_175_p": [
      190,
      230
    ],
    "aurapol_pla_raspberrypartiallytransparent_1000_175_p": [
      210,
      240
    ]
  },
  "bed_temp_range": {
    "aurapol_pla_plaraspberrypartiallytransparent_1000_175_p": [
      50,
      70
    ],
    "aurapol_pla_raspberrypartiallytransparent_1000_175_p": [
      40,
      60
    ]
  },
  "translucent": {
    "aurapol_pla_plaraspberrypartiallytransparent_1000_175_p": true,
    "aurapol_pla_raspberrypartiallytransparent_1000_175_p": false
  }
}
```

### AU017: dup-58050b66413045e4b14d7a167fff69641499787c20c5f30c1d1cbeffd7804aa4

Status: APPROVED; survivor `aurapol_pla_white_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aurapol_pla_plawhite_1000_175_p`|`PLA {color_name}`|`White`|{"source_file": "aurapol.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 52, "compiled_records": 52} / False|
|`aurapol_pla_white_1000_175_p`|`{color_name}`|`White`|{"source_file": "aurapol.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "aurapol_pla_plawhite_1000_175_p": 1.24,
    "aurapol_pla_white_1000_175_p": 1.223
  },
  "spool_weight": {
    "aurapol_pla_plawhite_1000_175_p": null,
    "aurapol_pla_white_1000_175_p": 250.0
  },
  "color_hex": {
    "aurapol_pla_plawhite_1000_175_p": "F5F5F5",
    "aurapol_pla_white_1000_175_p": "ffffff"
  },
  "extruder_temp_range": {
    "aurapol_pla_plawhite_1000_175_p": [
      190,
      230
    ],
    "aurapol_pla_white_1000_175_p": [
      210,
      240
    ]
  },
  "bed_temp_range": {
    "aurapol_pla_plawhite_1000_175_p": [
      50,
      70
    ],
    "aurapol_pla_white_1000_175_p": [
      40,
      60
    ]
  }
}
```

### AU018: dup-bad12e48817de88ee94250a021e0d714980b35e5023094d19b82671b6c18255a

Status: APPROVED; survivor `aurapol_pla_yellowgreen_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aurapol_pla_playellowgreen_1000_175_p`|`PLA {color_name}`|`Yellow Green`|{"source_file": "aurapol.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 52, "compiled_records": 52} / False|
|`aurapol_pla_yellowgreen_1000_175_p`|`{color_name}`|`Yellow Green`|{"source_file": "aurapol.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "aurapol_pla_playellowgreen_1000_175_p": 1.24,
    "aurapol_pla_yellowgreen_1000_175_p": 1.223
  },
  "spool_weight": {
    "aurapol_pla_playellowgreen_1000_175_p": null,
    "aurapol_pla_yellowgreen_1000_175_p": 250.0
  },
  "color_hex": {
    "aurapol_pla_playellowgreen_1000_175_p": "00CC00",
    "aurapol_pla_yellowgreen_1000_175_p": "80ff00"
  },
  "extruder_temp_range": {
    "aurapol_pla_playellowgreen_1000_175_p": [
      190,
      230
    ],
    "aurapol_pla_yellowgreen_1000_175_p": [
      210,
      240
    ]
  },
  "bed_temp_range": {
    "aurapol_pla_playellowgreen_1000_175_p": [
      50,
      70
    ],
    "aurapol_pla_yellowgreen_1000_175_p": [
      40,
      60
    ]
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

- `aurapol_pla_l-egogreen_1000_175_p` — L-EGO green
- `aurapol_pla_l-egoblue_1000_175_p` — L-EGO blue
- `aurapol_asa_graphiteblack_850_175_p` — Graphite black
- `aurapol_asa_signalwhite_850_175_p` — Signal White
- `aurapol_asa_natural_850_175_p` — Natural
- `aurapol_asa_lightgrey_850_175_p` — Light Grey
- `aurapol_asa_signalorange_850_175_p` — Signal Orange
- `aurapol_asa_skyblue_850_175_p` — Sky Blue
- `aurapol_asa_greengrass_850_175_p` — Green Grass
- `aurapol_asa_slategray_850_175_p` — Slate Gray
- `aurapol_abs_absblack_1000_175_p` — ABS Black
- `aurapol_abs_absnatural_1000_175_p` — ABS Natural
- `aurapol_abs_absslategrey_1000_175_p` — ABS Slate Grey
- `aurapol_asa_asaaluminiumgray_1000_175_p` — ASA Aluminium Gray
- `aurapol_asa_asabrownkhaki_1000_175_p` — ASA Brown Khaki
- `aurapol_asa_asadarkbrass_1000_175_p` — ASA Dark Brass
- `aurapol_asa_asadarkbronze_1000_175_p` — ASA Dark Bronze
- `aurapol_asa_asadarkturquoise_1000_175_p` — ASA Dark Turquoise
- `aurapol_asa_asagraphiteblack_1000_175_p` — ASA Graphite Black
- `aurapol_asa_asagreengrass_1000_175_p` — ASA Green Grass
- `aurapol_asa_asalightgrey_1000_175_p` — ASA Light Grey
- `aurapol_asa_asanatural_1000_175_p` — ASA Natural
- `aurapol_asa_asasignalorange_1000_175_p` — ASA Signal Orange
- `aurapol_asa_asasignalwhite_1000_175_p` — ASA Signal White
- `aurapol_asa_asaskyblue_1000_175_p` — ASA Sky Blue
- `aurapol_asa_asaslategrey_1000_175_p` — ASA Slate Grey
- `aurapol_petg_armypetgdesertstorm_1000_175_p` — ARMY PETG Desert Storm
- `aurapol_petg_armypetghighlandgreen_1000_175_p` — ARMY PETG Highland green
- `aurapol_petg_armypetgpanzergrau_1000_175_p` — ARMY PETG Panzer Grau
- `aurapol_petg_armypetgsandstorm_1000_175_p` — ARMY PETG Sand Storm
- `aurapol_petg_armypetgsurvivalgrey_1000_175_p` — ARMY PETG Survival Grey
- `aurapol_petg_petgbrightorange_1000_175_p` — PETG Bright Orange
- `aurapol_petg_petgcopperbrown_1000_175_p` — PETG Copper brown
- `aurapol_petg_petgmachineblue_1000_175_p` — PETG Machine Blue
- `aurapol_petg_petgnuclearorange_1000_175_p` — PETG Nuclear Orange
- `aurapol_petg_petgpark-side_1000_175_p` — PETG PARK-SIDE
- `aurapol_petg_petgsilver_1000_175_p` — PETG Silver
- `aurapol_petg_petgultramarinebluetransparent_1000_175_p` — PETG Ultramarine Blue Transparent
- `aurapol_pla_plaht110black_1000_175_p` — PLA HT110 Black
- `aurapol_pla_plaht110blue_1000_175_p` — PLA HT110 Blue
- `aurapol_pla_plaht110bodycolor_1000_175_p` — PLA HT110 Body Color
- `aurapol_pla_plaht110brown_1000_175_p` — PLA HT110 Brown
- `aurapol_pla_plaht110green_1000_175_p` — PLA HT110 Green
- `aurapol_pla_plaht110machineblue_1000_175_p` — PLA HT110 Machine Blue
- `aurapol_pla_plaht110red_1000_175_p` — PLA HT110 Red
- `aurapol_pla_plaht110white_1000_175_p` — PLA HT110 White
- `aurapol_pla_plaht110yellow_1000_175_p` — PLA HT110 Yellow
- `aurapol_pla_l-egoplababyblue_1000_175_p` — L-EGO PLA Baby Blue
- `aurapol_pla_l-egoplacloudnine_1000_175_p` — L-EGO PLA Cloud Nine
- `aurapol_pla_l-egopladesertdune_1000_175_p` — L-EGO PLA Desert Dune
- `aurapol_pla_l-egoplamildmoss_1000_175_p` — L-EGO PLA Mild Moss
- `aurapol_pla_l-egoplanudecolor_1000_175_p` — L-EGO PLA Nude Color
- `aurapol_pla_l-egoplasourmustard_1000_175_p` — L-EGO PLA Sour Mustard
- `aurapol_pla_metallicplablue_1000_175_p` — Metallic PLA Blue
- `aurapol_pla_metallicplagreen_1000_175_p` — Metallic PLA Green
- `aurapol_pla_metallicplapurple_1000_175_p` — Metallic PLA Purple
- `aurapol_pla_metallicplared_1000_175_p` — Metallic PLA Red
- `aurapol_pla_metallicplaturquoise_1000_175_p` — Metallic PLA Turquoise
- `aurapol_pla_plaaquadreampartiallytransparent_1000_175_p` — PLA Aqua dream partially transparent
- `aurapol_pla_plaarmyhighlandgreen_1000_175_p` — PLA ARMY Highland GREEN
- `aurapol_pla_plabananapeel_1000_175_p` — PLA Banana peel
- `aurapol_pla_plablack-grey_1000_175_p` — PLA Black-grey
- `aurapol_pla_plabluel-ego_1000_175_p` — PLA Blue L-EGO
- `aurapol_pla_plabodycolor_1000_175_p` — PLA Body color
- `aurapol_pla_plabondibeach_1000_175_p` — PLA BONDI BEACH
- `aurapol_pla_plabrightorange_1000_175_p` — PLA Bright Orange
- `aurapol_pla_plabrownl-ego_1000_175_p` — PLA Brown L-EGO
- `aurapol_pla_placaramelchampagne_1000_175_p` — PLA Caramel Champagne
- `aurapol_pla_placrazymauve_1000_175_p` — PLA CRAZY MAUVE
- `aurapol_pla_placyberballerina_1000_175_p` — PLA CYBER BALLERINA
- `aurapol_pla_pladarkgoldpowder_1000_175_p` — PLA Dark Gold Powder
- `aurapol_pla_plafuchsiadreampartiallytransparent_1000_175_p` — PLA Fuchsia dream partially transparent
- `aurapol_pla_plagalaxyblack_1000_175_p` — PLA Galaxy Black
- `aurapol_pla_plagrandmagray_1000_175_p` — PLA GRANDMA GRAY
- `aurapol_pla_plagreenl-ego_1000_175_p` — PLA Green L-EGO
- `aurapol_pla_plagreenpearl_1000_175_p` — PLA Green pearl
- `aurapol_pla_plahoneypartiallytransparent_1000_175_p` — PLA Honey partially transparent
- `aurapol_pla_plalavenderfieldpartiallytransparent_1000_175_p` — PLA Lavender field partially transparent
- `aurapol_pla_plalightblush_1000_175_p` — PLA Light Blush
- `aurapol_pla_plalilaclily_1000_175_p` — PLA LILAC LILY
- `aurapol_pla_plalilacmistpartiallytransparent_1000_175_p` — PLA Lilac mist partially transparent
- `aurapol_pla_plamachineblue_1000_175_p` — PLA Machine Blue
- `aurapol_pla_plamangotango_1000_175_p` — PLA MANGO TANGO
- `aurapol_pla_plamarble_1000_175_p` — PLA MARBLE
- `aurapol_pla_plamintbreezepartiallytransparent_1000_175_p` — PLA Mint breeze partially transparent
- `aurapol_pla_plamustardfield_1000_175_p` — PLA Mustard Field
- `aurapol_pla_plamysticclearuv_1000_175_p` — PLA MYSTIC CLEAR UV
- `aurapol_pla_planeoncoralpartiallytransparent_1000_175_p` — PLA Neon coral partially transparent
- `aurapol_pla_planordicblue_1000_175_p` — PLA Nordic Blue
- `aurapol_pla_plaolivepowder_1000_175_p` — PLA Olive Powder
- `aurapol_pla_plapark-side_1000_175_p` — PLA PARK-SIDE
- `aurapol_pla_plapeachflamepartiallytransparent_1000_175_p` — PLA Peach flame partially transparent
- `aurapol_pla_plapickyourpoison_1000_175_p` — PLA PICK YOUR POISON
- `aurapol_pla_plapinkpowder_1000_175_p` — PLA Pink Powder
- `aurapol_pla_plapurplepearl_1000_175_p` — PLA Purple pearl
- `aurapol_pla_plaroyalred_1000_175_p` — PLA Royal Red
- `aurapol_pla_plasandyblush_1000_175_p` — PLA Sandy Blush
- `aurapol_pla_plasilver_1000_175_p` — PLA Silver
- `aurapol_pla_plasoftlinen_1000_175_p` — PLA Soft Linen
- `aurapol_pla_plasummersky_1000_175_p` — PLA SUMMER SKY
- `aurapol_pla_plawildsage_1000_175_p` — PLA Wild Sage
- `aurapol_pla_plawisteriawinds_1000_175_p` — PLA WISTERIA WINDS
- `aurapol_pla_playellowmarble_1000_175_p` — PLA YELLOW MARBLE
- `aurapol_pla_woodplabamboo_1000_175_p` — Wood PLA BAMBOO
- `aurapol_pla_woodplacork_1000_175_p` — Wood PLA CORK
- `aurapol_pla_woodplapine_1000_175_p` — Wood PLA PINE
