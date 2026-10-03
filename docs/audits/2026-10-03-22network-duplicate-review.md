# 22network duplicate migration review

Base `aae57e4eef0952890047740508e16ebdbedee176`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `097a722a4177b127664d75040e8cb4bbe20f7c0e944992a7339e4bbc7bcdf1ef`.

## Authorization and result

{"groups": 15, "approved_groups": 12, "retired": 12, "deferred": 3, "hard_stops": 0, "before_count": 51813, "after_count": 51801, "brand_before": 153, "brand_after": 141, "registry_before": 1621, "registry_after": 1633, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Twelve strict ordinary PLA/Silk groups retain older well-formed families by original Rule4 without Cartesian inflation or tie. Existing identifiers already belong to survivors; no transfers. Current charts corroborate named lines/color codes, but no exact current numeric printing/density document verified: survivor printing values retained unresolved. Three dual-color qualifier split groups deferred by Rule5; no coaxial/HEX feature discarded. Packaging/tare unchanged.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://22-network.com/pla%2Fpla%EF%BC%8B", "note": "official53-colorPLA/PLA+ chart1kg1.75; existing codes on older family preserved"}
- {"url": "https://22-network.com/pla-silk-double", "note": "official21-color dualSilk chart1kg1.75; does not resolve current qualifier/color strict decomposition"}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`22network_pla_plablack_1000_175_p`|`22network_pla_black_1000_175_p`|`22network.json::22 Network::PLA {color_name}::PLA Black::PLA::1000::1.75::plastic::False`|
|`22network_pla_plabrown_1000_175_p`|`22network_pla_brown_1000_175_p`|`22network.json::22 Network::PLA {color_name}::PLA Brown::PLA::1000::1.75::plastic::False`|
|`22network_pla_plagold_1000_175_p`|`22network_pla_gold_1000_175_p`|`22network.json::22 Network::PLA {color_name}::PLA Gold::PLA::1000::1.75::plastic::False`|
|`22network_pla_plagrey_1000_175_p`|`22network_pla_grey_1000_175_p`|`22network.json::22 Network::PLA {color_name}::PLA Grey::PLA::1000::1.75::plastic::False`|
|`22network_pla_plaorange_1000_175_p`|`22network_pla_orange_1000_175_p`|`22network.json::22 Network::PLA {color_name}::PLA Orange::PLA::1000::1.75::plastic::False`|
|`22network_pla_plapink_1000_175_p`|`22network_pla_pink_1000_175_p`|`22network.json::22 Network::PLA {color_name}::PLA Pink::PLA::1000::1.75::plastic::False`|
|`22network_pla_plapurple_1000_175_p`|`22network_pla_purple_1000_175_p`|`22network.json::22 Network::PLA {color_name}::PLA Purple::PLA::1000::1.75::plastic::False`|
|`22network_pla_plared_1000_175_p`|`22network_pla_red_1000_175_p`|`22network.json::22 Network::PLA {color_name}::PLA Red::PLA::1000::1.75::plastic::False`|
|`22network_pla_plasilver_1000_175_p`|`22network_pla_silver_1000_175_p`|`22network.json::22 Network::PLA {color_name}::PLA Silver::PLA::1000::1.75::plastic::False`|
|`22network_pla_playellow_1000_175_p`|`22network_pla_yellow_1000_175_p`|`22network.json::22 Network::PLA {color_name}::PLA Yellow::PLA::1000::1.75::plastic::False`|
|`22network_pla_silkplabronze_1000_175_p`|`22network_pla_silkbronze_1000_175_p`|`22network.json::22 Network::Silk PLA {color_name}::Silk PLA Bronze::PLA::1000::1.75::plastic::False`|
|`22network_pla_silkplasilver_1000_175_p`|`22network_pla_silksilver_1000_175_p`|`22network.json::22 Network::Silk PLA {color_name}::Silk PLA Silver::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### NW001: dup-af6f8ac1479060e3b2f8a1430ac462b639a524d423cdd28aa1c7dfdca0117e1e

Status: APPROVED; survivor `22network_pla_black_1000_175_p`; Rule 4.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`22network_pla_black_1000_175_p`|`{color_name}`|`Black`|{"source_file": "22network.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 53, "compiled_records": 53} / False|
|`22network_pla_plablack_1000_175_p`|`PLA {color_name}`|`Black`|{"source_file": "22network.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "22network_pla_black_1000_175_p": 220,
    "22network_pla_plablack_1000_175_p": null
  },
  "extruder_temp_range": {
    "22network_pla_black_1000_175_p": [
      190,
      220
    ],
    "22network_pla_plablack_1000_175_p": [
      200,
      220
    ]
  },
  "bed_temp_range": {
    "22network_pla_black_1000_175_p": [
      50,
      65
    ],
    "22network_pla_plablack_1000_175_p": [
      22,
      60
    ]
  },
  "codes": {
    "22network_pla_black_1000_175_p": [
      "10101"
    ],
    "22network_pla_plablack_1000_175_p": null
  }
}
```

### NW002: dup-0a6cba846e1b7263e672717570b5bd67b3e4369e042648999f00af4226d0baec

Status: APPROVED; survivor `22network_pla_brown_1000_175_p`; Rule 4.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`22network_pla_brown_1000_175_p`|`{color_name}`|`Brown`|{"source_file": "22network.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 53, "compiled_records": 53} / False|
|`22network_pla_plabrown_1000_175_p`|`PLA {color_name}`|`Brown`|{"source_file": "22network.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "22network_pla_brown_1000_175_p": 220,
    "22network_pla_plabrown_1000_175_p": null
  },
  "extruder_temp_range": {
    "22network_pla_brown_1000_175_p": [
      190,
      220
    ],
    "22network_pla_plabrown_1000_175_p": [
      200,
      220
    ]
  },
  "bed_temp_range": {
    "22network_pla_brown_1000_175_p": [
      50,
      65
    ],
    "22network_pla_plabrown_1000_175_p": [
      22,
      60
    ]
  },
  "codes": {
    "22network_pla_brown_1000_175_p": [
      "10800"
    ],
    "22network_pla_plabrown_1000_175_p": null
  }
}
```

### NW003: dup-d8b9288afab74988689be185d555786153b014ed5e03bcf42b320d1d8e596fde

Status: APPROVED; survivor `22network_pla_gold_1000_175_p`; Rule 4.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`22network_pla_gold_1000_175_p`|`{color_name}`|`Gold`|{"source_file": "22network.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 53, "compiled_records": 53} / False|
|`22network_pla_plagold_1000_175_p`|`PLA {color_name}`|`Gold`|{"source_file": "22network.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "22network_pla_gold_1000_175_p": 220,
    "22network_pla_plagold_1000_175_p": null
  },
  "extruder_temp_range": {
    "22network_pla_gold_1000_175_p": [
      190,
      220
    ],
    "22network_pla_plagold_1000_175_p": [
      200,
      220
    ]
  },
  "bed_temp_range": {
    "22network_pla_gold_1000_175_p": [
      50,
      65
    ],
    "22network_pla_plagold_1000_175_p": [
      22,
      60
    ]
  },
  "codes": {
    "22network_pla_gold_1000_175_p": [
      "10401"
    ],
    "22network_pla_plagold_1000_175_p": null
  }
}
```

### NW004: dup-4c02acbd5c62a83d086b5c960e122f80e190769b157afaf9a8758aa8f468e376

Status: APPROVED; survivor `22network_pla_grey_1000_175_p`; Rule 4.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`22network_pla_grey_1000_175_p`|`{color_name}`|`Grey`|{"source_file": "22network.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 53, "compiled_records": 53} / False|
|`22network_pla_plagrey_1000_175_p`|`PLA {color_name}`|`Grey`|{"source_file": "22network.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "22network_pla_grey_1000_175_p": 220,
    "22network_pla_plagrey_1000_175_p": null
  },
  "extruder_temp_range": {
    "22network_pla_grey_1000_175_p": [
      190,
      220
    ],
    "22network_pla_plagrey_1000_175_p": [
      200,
      220
    ]
  },
  "bed_temp_range": {
    "22network_pla_grey_1000_175_p": [
      50,
      65
    ],
    "22network_pla_plagrey_1000_175_p": [
      22,
      60
    ]
  },
  "codes": {
    "22network_pla_grey_1000_175_p": [
      "10103"
    ],
    "22network_pla_plagrey_1000_175_p": null
  }
}
```

### NW005: dup-0fc699e6504a212a50d8784611cb0b6060bbf8bdb7149f7142d3246662318be8

Status: APPROVED; survivor `22network_pla_orange_1000_175_p`; Rule 4.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`22network_pla_orange_1000_175_p`|`{color_name}`|`Orange`|{"source_file": "22network.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 53, "compiled_records": 53} / False|
|`22network_pla_plaorange_1000_175_p`|`PLA {color_name}`|`Orange`|{"source_file": "22network.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "22network_pla_orange_1000_175_p": 220,
    "22network_pla_plaorange_1000_175_p": null
  },
  "extruder_temp_range": {
    "22network_pla_orange_1000_175_p": [
      190,
      220
    ],
    "22network_pla_plaorange_1000_175_p": [
      200,
      220
    ]
  },
  "bed_temp_range": {
    "22network_pla_orange_1000_175_p": [
      50,
      65
    ],
    "22network_pla_plaorange_1000_175_p": [
      22,
      60
    ]
  },
  "codes": {
    "22network_pla_orange_1000_175_p": [
      "10300"
    ],
    "22network_pla_plaorange_1000_175_p": null
  }
}
```

### NW006: dup-6da9bc57ab106c6264320733d1b27cd0a415011f40bc76c6e021f5150cc968c9

Status: APPROVED; survivor `22network_pla_pink_1000_175_p`; Rule 4.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`22network_pla_pink_1000_175_p`|`{color_name}`|`Pink`|{"source_file": "22network.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 53, "compiled_records": 53} / False|
|`22network_pla_plapink_1000_175_p`|`PLA {color_name}`|`Pink`|{"source_file": "22network.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "22network_pla_pink_1000_175_p": 220,
    "22network_pla_plapink_1000_175_p": null
  },
  "color_hex": {
    "22network_pla_pink_1000_175_p": "FFC0CB",
    "22network_pla_plapink_1000_175_p": "FF69B4"
  },
  "extruder_temp_range": {
    "22network_pla_pink_1000_175_p": [
      190,
      220
    ],
    "22network_pla_plapink_1000_175_p": [
      200,
      220
    ]
  },
  "bed_temp_range": {
    "22network_pla_pink_1000_175_p": [
      50,
      65
    ],
    "22network_pla_plapink_1000_175_p": [
      22,
      60
    ]
  },
  "codes": {
    "22network_pla_pink_1000_175_p": [
      "10203"
    ],
    "22network_pla_plapink_1000_175_p": null
  }
}
```

### NW007: dup-e971099827631eadf2c916f191e048d24cf8d92bf655fe2f363e924b64bff27e

Status: APPROVED; survivor `22network_pla_purple_1000_175_p`; Rule 4.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`22network_pla_plapurple_1000_175_p`|`PLA {color_name}`|`Purple`|{"source_file": "22network.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|
|`22network_pla_purple_1000_175_p`|`{color_name}`|`Purple`|{"source_file": "22network.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 53, "compiled_records": 53} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "22network_pla_plapurple_1000_175_p": null,
    "22network_pla_purple_1000_175_p": 220
  },
  "extruder_temp_range": {
    "22network_pla_plapurple_1000_175_p": [
      200,
      220
    ],
    "22network_pla_purple_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "22network_pla_plapurple_1000_175_p": [
      22,
      60
    ],
    "22network_pla_purple_1000_175_p": [
      50,
      65
    ]
  },
  "codes": {
    "22network_pla_plapurple_1000_175_p": null,
    "22network_pla_purple_1000_175_p": [
      "10700"
    ]
  }
}
```

### NW008: dup-a819da2f2573bc97cd0fec54cefc38abd5a3705901bea27b03034432424f1024

Status: APPROVED; survivor `22network_pla_red_1000_175_p`; Rule 4.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`22network_pla_plared_1000_175_p`|`PLA {color_name}`|`Red`|{"source_file": "22network.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|
|`22network_pla_red_1000_175_p`|`{color_name}`|`Red`|{"source_file": "22network.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 53, "compiled_records": 53} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "22network_pla_plared_1000_175_p": null,
    "22network_pla_red_1000_175_p": 220
  },
  "color_hex": {
    "22network_pla_plared_1000_175_p": "CC0000",
    "22network_pla_red_1000_175_p": "E30613"
  },
  "extruder_temp_range": {
    "22network_pla_plared_1000_175_p": [
      200,
      220
    ],
    "22network_pla_red_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "22network_pla_plared_1000_175_p": [
      22,
      60
    ],
    "22network_pla_red_1000_175_p": [
      50,
      65
    ]
  },
  "codes": {
    "22network_pla_plared_1000_175_p": null,
    "22network_pla_red_1000_175_p": [
      "10200"
    ]
  }
}
```

### NW009: dup-5ebabbc29c4156c0b76ae03a7531612580117122060ea11ed69336c51d51596e

Status: APPROVED; survivor `22network_pla_silver_1000_175_p`; Rule 4.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`22network_pla_plasilver_1000_175_p`|`PLA {color_name}`|`Silver`|{"source_file": "22network.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|
|`22network_pla_silver_1000_175_p`|`{color_name}`|`Silver`|{"source_file": "22network.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 53, "compiled_records": 53} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "22network_pla_plasilver_1000_175_p": null,
    "22network_pla_silver_1000_175_p": 220
  },
  "extruder_temp_range": {
    "22network_pla_plasilver_1000_175_p": [
      200,
      220
    ],
    "22network_pla_silver_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "22network_pla_plasilver_1000_175_p": [
      22,
      60
    ],
    "22network_pla_silver_1000_175_p": [
      50,
      65
    ]
  },
  "codes": {
    "22network_pla_plasilver_1000_175_p": null,
    "22network_pla_silver_1000_175_p": [
      "10102"
    ]
  }
}
```

### NW010: dup-61932a0c80238382aa7cf6321c690248dcf16d51d474e5e08a750ed8aa1035ab

Status: APPROVED; survivor `22network_pla_yellow_1000_175_p`; Rule 4.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`22network_pla_playellow_1000_175_p`|`PLA {color_name}`|`Yellow`|{"source_file": "22network.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 16, "compiled_records": 16} / False|
|`22network_pla_yellow_1000_175_p`|`{color_name}`|`Yellow`|{"source_file": "22network.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 53, "compiled_records": 53} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "22network_pla_playellow_1000_175_p": null,
    "22network_pla_yellow_1000_175_p": 220
  },
  "extruder_temp_range": {
    "22network_pla_playellow_1000_175_p": [
      200,
      220
    ],
    "22network_pla_yellow_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "22network_pla_playellow_1000_175_p": [
      22,
      60
    ],
    "22network_pla_yellow_1000_175_p": [
      50,
      65
    ]
  },
  "codes": {
    "22network_pla_playellow_1000_175_p": null,
    "22network_pla_yellow_1000_175_p": [
      "10400"
    ]
  }
}
```

### NW011: dup-36a3cc83ed67580b023ba5bd8cc832f83dca0b60fecafaa3609cba92e718ce9f

Status: APPROVED; survivor `22network_pla_silkbronze_1000_175_p`; Rule 4.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`22network_pla_silkbronze_1000_175_p`|`Silk {color_name}`|`Bronze`|{"source_file": "22network.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|
|`22network_pla_silkplabronze_1000_175_p`|`Silk PLA {color_name}`|`Bronze`|{"source_file": "22network.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "22network_pla_silkbronze_1000_175_p": 220,
    "22network_pla_silkplabronze_1000_175_p": null
  },
  "extruder_temp_range": {
    "22network_pla_silkbronze_1000_175_p": [
      190,
      220
    ],
    "22network_pla_silkplabronze_1000_175_p": [
      200,
      220
    ]
  },
  "bed_temp_range": {
    "22network_pla_silkbronze_1000_175_p": [
      50,
      65
    ],
    "22network_pla_silkplabronze_1000_175_p": [
      22,
      60
    ]
  },
  "finish": {
    "22network_pla_silkbronze_1000_175_p": "glossy",
    "22network_pla_silkplabronze_1000_175_p": null
  },
  "codes": {
    "22network_pla_silkbronze_1000_175_p": [
      "silk010"
    ],
    "22network_pla_silkplabronze_1000_175_p": null
  }
}
```

### NW012: dup-66560422ca66e39f3865d9bf9b5edf396af2df1bc8384793801a743fe0102985

Status: DEFERRED; survivor `22network_pla_silkdualblue/green_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`22network_pla_silkdualblue/green_1000_175_p`|`Silk Dual {color_name}`|`Blue/Green`|{"source_file": "22network.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|
|`22network_pla_silkpladualbluegreen_1000_175_p`|`Silk PLA {color_name}`|`Dual Blue Green`|{"source_file": "22network.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "22network_pla_silkdualblue/green_1000_175_p": 220,
    "22network_pla_silkpladualbluegreen_1000_175_p": null
  },
  "color_hex": {
    "22network_pla_silkdualblue/green_1000_175_p": null,
    "22network_pla_silkpladualbluegreen_1000_175_p": "0000FF"
  },
  "color_hexes": {
    "22network_pla_silkdualblue/green_1000_175_p": [
      "0000FF",
      "008000"
    ],
    "22network_pla_silkpladualbluegreen_1000_175_p": null
  },
  "extruder_temp_range": {
    "22network_pla_silkdualblue/green_1000_175_p": [
      190,
      220
    ],
    "22network_pla_silkpladualbluegreen_1000_175_p": [
      200,
      220
    ]
  },
  "bed_temp_range": {
    "22network_pla_silkdualblue/green_1000_175_p": [
      50,
      65
    ],
    "22network_pla_silkpladualbluegreen_1000_175_p": [
      22,
      60
    ]
  },
  "finish": {
    "22network_pla_silkdualblue/green_1000_175_p": "glossy",
    "22network_pla_silkpladualbluegreen_1000_175_p": null
  },
  "multi_color_direction": {
    "22network_pla_silkdualblue/green_1000_175_p": "coaxial",
    "22network_pla_silkpladualbluegreen_1000_175_p": null
  },
  "codes": {
    "22network_pla_silkdualblue/green_1000_175_p": [
      "Dual 03"
    ],
    "22network_pla_silkpladualbluegreen_1000_175_p": null
  }
}
```

### NW013: dup-679b8ea7b3e4702b4abfff55f811edd228fdd4154e62a0bc213a0d5285ed9c4a

Status: DEFERRED; survivor `22network_pla_silkdualpurple/gold_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`22network_pla_silkdualpurple/gold_1000_175_p`|`Silk Dual {color_name}`|`Purple/Gold`|{"source_file": "22network.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|
|`22network_pla_silkpladualpurplegold_1000_175_p`|`Silk PLA {color_name}`|`Dual Purple Gold`|{"source_file": "22network.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "22network_pla_silkdualpurple/gold_1000_175_p": 220,
    "22network_pla_silkpladualpurplegold_1000_175_p": null
  },
  "color_hex": {
    "22network_pla_silkdualpurple/gold_1000_175_p": null,
    "22network_pla_silkpladualpurplegold_1000_175_p": "800080"
  },
  "color_hexes": {
    "22network_pla_silkdualpurple/gold_1000_175_p": [
      "800080",
      "FFD700"
    ],
    "22network_pla_silkpladualpurplegold_1000_175_p": null
  },
  "extruder_temp_range": {
    "22network_pla_silkdualpurple/gold_1000_175_p": [
      190,
      220
    ],
    "22network_pla_silkpladualpurplegold_1000_175_p": [
      200,
      220
    ]
  },
  "bed_temp_range": {
    "22network_pla_silkdualpurple/gold_1000_175_p": [
      50,
      65
    ],
    "22network_pla_silkpladualpurplegold_1000_175_p": [
      22,
      60
    ]
  },
  "finish": {
    "22network_pla_silkdualpurple/gold_1000_175_p": "glossy",
    "22network_pla_silkpladualpurplegold_1000_175_p": null
  },
  "multi_color_direction": {
    "22network_pla_silkdualpurple/gold_1000_175_p": "coaxial",
    "22network_pla_silkpladualpurplegold_1000_175_p": null
  },
  "codes": {
    "22network_pla_silkdualpurple/gold_1000_175_p": [
      "Dual 07"
    ],
    "22network_pla_silkpladualpurplegold_1000_175_p": null
  }
}
```

### NW014: dup-a8d5b76081b35eeb925e91403b46c5ccf58887eb5c0dec265e5fd60c29a047a7

Status: DEFERRED; survivor `22network_pla_silkdualred/gold_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`22network_pla_silkdualred/gold_1000_175_p`|`Silk Dual {color_name}`|`Red/Gold`|{"source_file": "22network.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|
|`22network_pla_silkpladualredgold_1000_175_p`|`Silk PLA {color_name}`|`Dual Red Gold`|{"source_file": "22network.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "22network_pla_silkdualred/gold_1000_175_p": 220,
    "22network_pla_silkpladualredgold_1000_175_p": null
  },
  "color_hex": {
    "22network_pla_silkdualred/gold_1000_175_p": null,
    "22network_pla_silkpladualredgold_1000_175_p": "CC0000"
  },
  "color_hexes": {
    "22network_pla_silkdualred/gold_1000_175_p": [
      "E30613",
      "FFD700"
    ],
    "22network_pla_silkpladualredgold_1000_175_p": null
  },
  "extruder_temp_range": {
    "22network_pla_silkdualred/gold_1000_175_p": [
      190,
      220
    ],
    "22network_pla_silkpladualredgold_1000_175_p": [
      200,
      220
    ]
  },
  "bed_temp_range": {
    "22network_pla_silkdualred/gold_1000_175_p": [
      50,
      65
    ],
    "22network_pla_silkpladualredgold_1000_175_p": [
      22,
      60
    ]
  },
  "finish": {
    "22network_pla_silkdualred/gold_1000_175_p": "glossy",
    "22network_pla_silkpladualredgold_1000_175_p": null
  },
  "multi_color_direction": {
    "22network_pla_silkdualred/gold_1000_175_p": "coaxial",
    "22network_pla_silkpladualredgold_1000_175_p": null
  },
  "codes": {
    "22network_pla_silkdualred/gold_1000_175_p": [
      "Dual 04"
    ],
    "22network_pla_silkpladualredgold_1000_175_p": null
  }
}
```

### NW015: dup-8f4907be962758eb72c6a5f466b2d498825b6b4ff9d20ab626d00470a41ea623

Status: APPROVED; survivor `22network_pla_silksilver_1000_175_p`; Rule 4.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`22network_pla_silkplasilver_1000_175_p`|`Silk PLA {color_name}`|`Silver`|{"source_file": "22network.json", "definition_index": 9, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`22network_pla_silksilver_1000_175_p`|`Silk {color_name}`|`Silver`|{"source_file": "22network.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "22network_pla_silkplasilver_1000_175_p": null,
    "22network_pla_silksilver_1000_175_p": 220
  },
  "extruder_temp_range": {
    "22network_pla_silkplasilver_1000_175_p": [
      200,
      220
    ],
    "22network_pla_silksilver_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "22network_pla_silkplasilver_1000_175_p": [
      22,
      60
    ],
    "22network_pla_silksilver_1000_175_p": [
      50,
      65
    ]
  },
  "finish": {
    "22network_pla_silkplasilver_1000_175_p": null,
    "22network_pla_silksilver_1000_175_p": "glossy"
  },
  "codes": {
    "22network_pla_silkplasilver_1000_175_p": null,
    "22network_pla_silksilver_1000_175_p": [
      "silk006"
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

- `22network_pla_coldwhite_1000_175_p` — Cold White
- `22network_pla_warmwhite_1000_175_p` — Warm White
- `22network_pla_lightgrey_1000_175_p` — Light Grey
- `22network_pla_greyblue_1000_175_p` — Grey Blue
- `22network_pla_darkgrey_1000_175_p` — Dark Grey
- `22network_pla_rougered_1000_175_p` — Rouge Red
- `22network_pla_skyblue_1000_175_p` — Sky Blue
- `22network_pla_turquoisegreen_1000_175_p` — Turquoise Green
- `22network_pla_cyan_1000_175_p` — Cyan
- `22network_pla_cobaltblue_1000_175_p` — Cobalt Blue
- `22network_pla_bluegrey_1000_175_p` — Blue Grey
- `22network_pla_darkblue_1000_175_p` — Dark Blue
- `22network_pla_armyblue_1000_175_p` — Army Blue
- `22network_pla_darknightblue_1000_175_p` — Dark Night Blue
- `22network_pla_applegreen_1000_175_p` — Apple Green
- `22network_pla_grassgreen_1000_175_p` — Grass Green
- `22network_pla_bambugreen_1000_175_p` — Bambu Green
- `22network_pla_christmasgreen_1000_175_p` — Christmas Green
- `22network_pla_darknightgreen_1000_175_p` — Dark Night Green
- `22network_pla_lilacpurple_1000_175_p` — Lilac Purple
- `22network_pla_violetpurple_1000_175_p` — Violet Purple
- `22network_pla_pumpkinorange_1000_175_p` — Pumpkin Orange
- `22network_pla_bronze_1000_175_p` — Bronze
- `22network_pla_darknightbrown_1000_175_p` — Dark Night Brown
- `22network_pla_cocobrown_1000_175_p` — Coco Brown
- `22network_pla_darkbrown_1000_175_p` — Dark Brown
- `22network_pla_paleapricot_1000_175_p` — Pale Apricot
- `22network_pla_dessertyellow_1000_175_p` — Dessert Yellow
- `22network_pla_lattebrown_1000_175_p` — Latte Brown
- `22network_pla_warmyellow_1000_175_p` — Warm Yellow
- `22network_pla_cherryblossom_1000_175_p` — Cherry Blossom
- `22network_pla_redpink_1000_175_p` — Red Pink
- `22network_pla_magentared_1000_175_p` — Magenta Red
- `22network_pla_butteryellow_1000_175_p` — Butter Yellow
- `22network_pla_dustypink_1000_175_p` — Dusty Pink
- `22network_pla_azureblue_1000_175_p` — Azure Blue
- `22network_pla_americanyellow_1000_175_p` — American Yellow
- `22network_pla_skin_1000_175_p` — Skin
- `22network_pla_forestgreen_1000_175_p` — Forest Green
- `22network_pla_fluorescentgreen_1000_175_p` — Fluorescent Green
- `22network_pla_fluorescentorange_1000_175_p` — Fluorescent Orange
- `22network_pla_rosered_1000_175_p` — Rose Red
- `22network_pla_fluorescentyellow_1000_175_p` — Fluorescent Yellow
- `22network_pla_luminousgreen_1000_175_p` — Luminous Green
- `22network_pla_luminousblue_1000_175_p` — Luminous Blue
- `22network_pla_silkwhite_1000_175_p` — Silk White
- `22network_pla_silkyellow_1000_175_p` — Silk Yellow
- `22network_pla_silkchinared_1000_175_p` — Silk China Red
- `22network_pla_silkblue_1000_175_p` — Silk Blue
- `22network_pla_silkyellow-gold_1000_175_p` — Silk Yellow-Gold
- `22network_pla_silkpurple_1000_175_p` — Silk Purple
- `22network_pla_silkblack_1000_175_p` — Silk Black
- `22network_pla_silkcopper_1000_175_p` — Silk Copper
- `22network_pla_silkchristmasgreen_1000_175_p` — Silk Christmas Green
- `22network_pla_silkdarkgold_1000_175_p` — Silk Dark Gold
- `22network_pla_silkpink_1000_175_p` — Silk Pink
- `22network_pla_silkcyan_1000_175_p` — Silk Cyan
- `22network_pla_silkdualred/green_1000_175_p` — Silk Dual Red/Green
- `22network_pla_silkdualred/blue_1000_175_p` — Silk Dual Red/Blue
- `22network_pla_silkdualgold/copper_1000_175_p` — Silk Dual Gold/Copper
- `22network_pla_silkdualgold/silver_1000_175_p` — Silk Dual Gold/Silver
- `22network_pla_silkdualyellow/green_1000_175_p` — Silk Dual Yellow/Green
- `22network_pla_silkdualrosered/lightblue_1000_175_p` — Silk Dual Rose Red/Light Blue
- `22network_pla_silkdualrosered/black_1000_175_p` — Silk Dual Rose Red/Black
- `22network_pla_silkdualemeraldgreen/black_1000_175_p` — Silk Dual Emerald Green/Black
- `22network_pla_silkdualblack/gold_1000_175_p` — Silk Dual Black/Gold
- `22network_pla_silkdualblack/purple_1000_175_p` — Silk Dual Black/Purple
- `22network_pla_silkdualblack/red_1000_175_p` — Silk Dual Black/Red
- `22network_pla_silkdualpurple/green_1000_175_p` — Silk Dual Purple/Green
- `22network_pla_silkdualteal/coral_1000_175_p` — Silk Dual Teal/Coral
- `22network_pla_silkdualblue/silver_1000_175_p` — Silk Dual Blue/Silver
- `22network_pla_silkdualblue/gold_1000_175_p` — Silk Dual Blue/Gold
- `22network_pla_silkdualcoral/purple_1000_175_p` — Silk Dual Coral/Purple
- `22network_pla_silkdualblue/purple_1000_175_p` — Silk Dual Blue/Purple
- `22network_pla_silkdualteal/darkviolet_1000_175_p` — Silk Dual Teal/Dark Violet
- `22network_pla_woodclassicbirch_1000_175_p` — Wood Classic Birch
- `22network_pla_woodclaybrown_1000_175_p` — Wood Clay Brown
- `22network_pla_woodblackwalnut_1000_175_p` — Wood Black Walnut
- `22network_pla_woodrosewood_1000_175_p` — Wood Rosewood
- `22network_pla_woodwhiteoak_1000_175_p` — Wood White Oak
- `22network_pla_woodochreyellow_1000_175_p` — Wood Ochre Yellow
- `22network_petg_green_1000_175_p` — Green
- `22network_petg_red_1000_175_p` — Red
- `22network_petg_yellow_1000_175_p` — Yellow
- `22network_petg_warmyellow_1000_175_p` — Warm Yellow
- `22network_petg_black_1000_175_p` — Black
- `22network_petg_grey_1000_175_p` — Grey
- `22network_petg_white_1000_175_p` — White
- `22network_petg_orange_1000_175_p` — Orange
- `22network_petg_darkblue_1000_175_p` — Dark Blue
- `22network_petg_darkgrey_1000_175_p` — Dark Grey
- `22network_petg_lakeblue_1000_175_p` — Lake Blue
- `22network_petg_forestgreen_1000_175_p` — Forest Green
- `22network_petg_lemongreen_1000_175_p` — Lemon Green
- `22network_petg_creamwhite_1000_175_p` — Cream White
- `22network_petg_peanutbrown_1000_175_p` — Peanut Brown
- `22network_petg_transparent_1000_175_p` — Transparent
- `22network_petg_silver_1000_175_p` — Silver
- `22network_petg_transparentblue_1000_175_p` — Transparent Blue
- `22network_petg_transparentyellow_1000_175_p` — Transparent Yellow
- `22network_petg_transparentorange_1000_175_p` — Transparent Orange
- `22network_petg_transparentgreen_1000_175_p` — Transparent Green
- `22network_petg_purple_1000_175_p` — Purple
- `22network_petg_cherryblossom_1000_175_p` — Cherry Blossom
- `22network_petg_pink_1000_175_p` — Pink
- `22network_petg_magenta_1000_175_p` — Magenta
- `22network_petg_brown_1000_175_p` — Brown
- `22network_petg_skyblue_1000_175_p` — Sky Blue
- `22network_pla_glowplaluminousblue_1000_175_p` — Glow PLA Luminous Blue
- `22network_pla_glowplaluminousgreen_1000_175_p` — Glow PLA Luminous Green
- `22network_pla_matteplamattebasicrainbow_1000_175_p` — Matte PLA Matte Basic Rainbow
- `22network_pla_matteplamattemagicrainbow_1000_175_p` — Matte PLA Matte Magic Rainbow
- `22network_pla_plablue_1000_175_p` — PLA Blue
- `22network_pla_placopper_1000_175_p` — PLA Copper
- `22network_pla_plagreen_1000_175_p` — PLA Green
- `22network_pla_plalimegreen_1000_175_p` — PLA Lime Green
- `22network_pla_planavy_1000_175_p` — PLA Navy
- `22network_pla_plawhite_1000_175_p` — PLA White
- `22network_pla_silkplagold_1000_175_p` — Silk PLA Gold
- `22network_pla_silkplarainbow_1000_175_p` — Silk PLA Rainbow
- `22network_pla_silkplatricandyrainbow_1000_175_p` — Silk PLA Tri Candy Rainbow
- `22network_pla_silkplatriroseredlightblue_1000_175_p` — Silk PLA Tri Rose Red Light Blue
- `22network_pla_silkplauniverserainbow_1000_175_p` — Silk PLA Universe Rainbow
