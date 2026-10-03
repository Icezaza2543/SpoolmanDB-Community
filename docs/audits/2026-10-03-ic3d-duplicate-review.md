# ic3d duplicate migration review

Base `f244e2d2fc558cd8e30ab29e45e76b6c8d7ef2ed`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `a0e775acca962133836b42d6054036dcee5f37b5b06097c863a646efc0525a61`.

## Authorization and result

{"groups": 14, "approved_groups": 14, "retired": 14, "deferred": 0, "hard_stops": 0, "before_count": 51801, "after_count": 51787, "brand_before": 157, "brand_after": 143, "registry_before": 1633, "registry_after": 1647, "metadata_fields_changed": 42, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Correct only14 approved ordinary PLA/PETG/ABS survivor variants. Manufacturer approximate nominal bed recommendations stored as their stated nominal points60/70/110, not invented ranges; uncertainty remains documented. Source-cell splits prevent spreading standard-line values onto unique Recycled, UV, PolyHex or Impact Modified variants hidden inside broad generic definitions. Existing densities retained; PLA/PETG corroborated, ABS1.04 remains unverified. HEX/tare conflicts unresolved. Packaging/tare unchanged.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://www.ic3dprinters.com/shop/pla-filaments/", "density": 1.24, "nozzle": [200, 240], "bed": "approximately60C nominal recommendation", "note": "explicit legacy ordinary PLA, not Impact Modified PLA"}
- {"url": "https://www.ic3dprinters.com/shop/petg-filaments/", "nozzle": [240, 270], "bed": "approximately70C nominal recommendation"}
- {"url": "https://www.ic3dprinters.com/shop/abs-filaments/", "nozzle": [220, 260], "bed": "approximately110C nominal recommendation"}
- {"url": "https://www.ic3dprinters.com/ic3d/wp-content/uploads/2020/08/PETG-IC3D-TDS-2020.07.pdf", "density": 1.27}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`ic3d_abs_ic3dabsblack_1000_175_p`|`ic3d_abs_absblack_1000_175_p`|`ic3d.json::IC3D::IC3D ABS {color_name}::IC3D ABS Black::ABS::1000::1.75::plastic::False`|
|`ic3d_abs_ic3dabsblue_1000_175_p`|`ic3d_abs_absblue_1000_175_p`|`ic3d.json::IC3D::IC3D ABS {color_name}::IC3D ABS Blue::ABS::1000::1.75::plastic::False`|
|`ic3d_abs_ic3dabsgray_1000_175_p`|`ic3d_abs_absgrey_1000_175_p`|`ic3d.json::IC3D::IC3D ABS {color_name}::IC3D ABS Gray::ABS::1000::1.75::plastic::False`|
|`ic3d_abs_ic3dabswhite_1000_175_p`|`ic3d_abs_abswhite_1000_175_p`|`ic3d.json::IC3D::IC3D ABS {color_name}::IC3D ABS White::ABS::1000::1.75::plastic::False`|
|`ic3d_petg_ic3dpetgblack_1000_175_p`|`ic3d_petg_petgblack_1000_175_p`|`ic3d.json::IC3D::IC3D PETG {color_name}::IC3D PETG Black::PETG::1000::1.75::plastic::False`|
|`ic3d_petg_ic3dpetgblue_1000_175_p`|`ic3d_petg_petgblue_1000_175_p`|`ic3d.json::IC3D::IC3D PETG {color_name}::IC3D PETG Blue::PETG::1000::1.75::plastic::False`|
|`ic3d_petg_ic3dpetggray_1000_175_p`|`ic3d_petg_petggrey_1000_175_p`|`ic3d.json::IC3D::IC3D PETG {color_name}::IC3D PETG Gray::PETG::1000::1.75::plastic::False`|
|`ic3d_petg_ic3dpetgred_1000_175_p`|`ic3d_petg_petgred_1000_175_p`|`ic3d.json::IC3D::IC3D PETG {color_name}::IC3D PETG Red::PETG::1000::1.75::plastic::False`|
|`ic3d_petg_ic3dpetgwhite_1000_175_p`|`ic3d_petg_petgwhite_1000_175_p`|`ic3d.json::IC3D::IC3D PETG {color_name}::IC3D PETG White::PETG::1000::1.75::plastic::False`|
|`ic3d_pla_ic3dplablack_1000_175_p`|`ic3d_pla_plablack_1000_175_p`|`ic3d.json::IC3D::IC3D PLA {color_name}::IC3D PLA Black::PLA::1000::1.75::plastic::False`|
|`ic3d_pla_ic3dplablue_1000_175_p`|`ic3d_pla_plablue_1000_175_p`|`ic3d.json::IC3D::IC3D PLA {color_name}::IC3D PLA Blue::PLA::1000::1.75::plastic::False`|
|`ic3d_pla_ic3dplagray_1000_175_p`|`ic3d_pla_plagrey_1000_175_p`|`ic3d.json::IC3D::IC3D PLA {color_name}::IC3D PLA Gray::PLA::1000::1.75::plastic::False`|
|`ic3d_pla_ic3dplared_1000_175_p`|`ic3d_pla_plared_1000_175_p`|`ic3d.json::IC3D::IC3D PLA {color_name}::IC3D PLA Red::PLA::1000::1.75::plastic::False`|
|`ic3d_pla_ic3dplawhite_1000_175_p`|`ic3d_pla_plawhite_1000_175_p`|`ic3d.json::IC3D::IC3D PLA {color_name}::IC3D PLA White::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### IC001: dup-d273429b11132ba913348e8bcdba40220762306bc7a8a4a7e5dd97423f1241ec

Status: APPROVED; survivor `ic3d_abs_absblack_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ic3d_abs_absblack_1000_175_p`|`ABS {color_name}`|`Black`|{"source_file": "ic3d.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|
|`ic3d_abs_ic3dabsblack_1000_175_p`|`IC3D ABS {color_name}`|`Black`|{"source_file": "ic3d.json", "definition_index": 2, "weights": 3, "diameters": 2, "colors": 6, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "ic3d_abs_absblack_1000_175_p": null,
    "ic3d_abs_ic3dabsblack_1000_175_p": 250
  },
  "color_hex": {
    "ic3d_abs_absblack_1000_175_p": "000000",
    "ic3d_abs_ic3dabsblack_1000_175_p": "101010"
  },
  "extruder_temp_range": {
    "ic3d_abs_absblack_1000_175_p": [
      230,
      260
    ],
    "ic3d_abs_ic3dabsblack_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "ic3d_abs_absblack_1000_175_p": [
      90,
      110
    ],
    "ic3d_abs_ic3dabsblack_1000_175_p": [
      100,
      110
    ]
  }
}
```

### IC002: dup-2f505b87de399471732fd4ef290119be1ec580c134357cc688a8dbd0906d7608

Status: APPROVED; survivor `ic3d_abs_absblue_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ic3d_abs_absblue_1000_175_p`|`ABS {color_name}`|`Blue`|{"source_file": "ic3d.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|
|`ic3d_abs_ic3dabsblue_1000_175_p`|`IC3D ABS {color_name}`|`Blue`|{"source_file": "ic3d.json", "definition_index": 2, "weights": 3, "diameters": 2, "colors": 6, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "ic3d_abs_absblue_1000_175_p": null,
    "ic3d_abs_ic3dabsblue_1000_175_p": 250
  },
  "color_hex": {
    "ic3d_abs_absblue_1000_175_p": "0022FF",
    "ic3d_abs_ic3dabsblue_1000_175_p": "1010C0"
  },
  "extruder_temp_range": {
    "ic3d_abs_absblue_1000_175_p": [
      230,
      260
    ],
    "ic3d_abs_ic3dabsblue_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "ic3d_abs_absblue_1000_175_p": [
      90,
      110
    ],
    "ic3d_abs_ic3dabsblue_1000_175_p": [
      100,
      110
    ]
  }
}
```

### IC003: dup-ea27d45d81828f7ca0efab2f659c69322ebe4475076d53793f34cc1ab513f83b

Status: APPROVED; survivor `ic3d_abs_absgrey_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ic3d_abs_absgrey_1000_175_p`|`ABS {color_name}`|`Grey`|{"source_file": "ic3d.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|
|`ic3d_abs_ic3dabsgray_1000_175_p`|`IC3D ABS {color_name}`|`Gray`|{"source_file": "ic3d.json", "definition_index": 2, "weights": 3, "diameters": 2, "colors": 6, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "ic3d_abs_absgrey_1000_175_p": null,
    "ic3d_abs_ic3dabsgray_1000_175_p": 250
  },
  "color_hex": {
    "ic3d_abs_absgrey_1000_175_p": "6F727E",
    "ic3d_abs_ic3dabsgray_1000_175_p": "808080"
  },
  "extruder_temp_range": {
    "ic3d_abs_absgrey_1000_175_p": [
      230,
      260
    ],
    "ic3d_abs_ic3dabsgray_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "ic3d_abs_absgrey_1000_175_p": [
      90,
      110
    ],
    "ic3d_abs_ic3dabsgray_1000_175_p": [
      100,
      110
    ]
  }
}
```

### IC004: dup-79212415994325fa043f955a3c31005288ca1391511096f3134cba727c80d15c

Status: APPROVED; survivor `ic3d_abs_abswhite_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ic3d_abs_abswhite_1000_175_p`|`ABS {color_name}`|`White`|{"source_file": "ic3d.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|
|`ic3d_abs_ic3dabswhite_1000_175_p`|`IC3D ABS {color_name}`|`White`|{"source_file": "ic3d.json", "definition_index": 2, "weights": 3, "diameters": 2, "colors": 6, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "ic3d_abs_abswhite_1000_175_p": null,
    "ic3d_abs_ic3dabswhite_1000_175_p": 250
  },
  "color_hex": {
    "ic3d_abs_abswhite_1000_175_p": "FFFFFF",
    "ic3d_abs_ic3dabswhite_1000_175_p": "F2F2F2"
  },
  "extruder_temp_range": {
    "ic3d_abs_abswhite_1000_175_p": [
      230,
      260
    ],
    "ic3d_abs_ic3dabswhite_1000_175_p": [
      220,
      260
    ]
  },
  "bed_temp_range": {
    "ic3d_abs_abswhite_1000_175_p": [
      90,
      110
    ],
    "ic3d_abs_ic3dabswhite_1000_175_p": [
      100,
      110
    ]
  }
}
```

### IC005: dup-5a10240d402efe2ce51842d9cf7e11282cf6a7bc6305a42bad7d49fabb5278f5

Status: APPROVED; survivor `ic3d_petg_petgblack_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ic3d_petg_ic3dpetgblack_1000_175_p`|`IC3D PETG {color_name}`|`Black`|{"source_file": "ic3d.json", "definition_index": 1, "weights": 3, "diameters": 2, "colors": 6, "compiled_records": 36} / False|
|`ic3d_petg_petgblack_1000_175_p`|`PETG {color_name}`|`Black`|{"source_file": "ic3d.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "ic3d_petg_ic3dpetgblack_1000_175_p": 250,
    "ic3d_petg_petgblack_1000_175_p": null
  },
  "color_hex": {
    "ic3d_petg_ic3dpetgblack_1000_175_p": "101010",
    "ic3d_petg_petgblack_1000_175_p": "000000"
  },
  "extruder_temp_range": {
    "ic3d_petg_ic3dpetgblack_1000_175_p": [
      240,
      270
    ],
    "ic3d_petg_petgblack_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "ic3d_petg_ic3dpetgblack_1000_175_p": [
      60,
      80
    ],
    "ic3d_petg_petgblack_1000_175_p": [
      70,
      90
    ]
  }
}
```

### IC006: dup-e0574990662adc348047cdc3671ff438790b1d7e79a78cc1bcaba4f386bf6bf3

Status: APPROVED; survivor `ic3d_petg_petgblue_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ic3d_petg_ic3dpetgblue_1000_175_p`|`IC3D PETG {color_name}`|`Blue`|{"source_file": "ic3d.json", "definition_index": 1, "weights": 3, "diameters": 2, "colors": 6, "compiled_records": 36} / False|
|`ic3d_petg_petgblue_1000_175_p`|`PETG {color_name}`|`Blue`|{"source_file": "ic3d.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "ic3d_petg_ic3dpetgblue_1000_175_p": 250,
    "ic3d_petg_petgblue_1000_175_p": null
  },
  "color_hex": {
    "ic3d_petg_ic3dpetgblue_1000_175_p": "1010C0",
    "ic3d_petg_petgblue_1000_175_p": "0353BA"
  },
  "extruder_temp_range": {
    "ic3d_petg_ic3dpetgblue_1000_175_p": [
      240,
      270
    ],
    "ic3d_petg_petgblue_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "ic3d_petg_ic3dpetgblue_1000_175_p": [
      60,
      80
    ],
    "ic3d_petg_petgblue_1000_175_p": [
      70,
      90
    ]
  }
}
```

### IC007: dup-1aa6a4e834fb13cbba25f27525115985342a5d2a03824607bf9eb8f10f24d92e

Status: APPROVED; survivor `ic3d_petg_petggrey_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ic3d_petg_ic3dpetggray_1000_175_p`|`IC3D PETG {color_name}`|`Gray`|{"source_file": "ic3d.json", "definition_index": 1, "weights": 3, "diameters": 2, "colors": 6, "compiled_records": 36} / False|
|`ic3d_petg_petggrey_1000_175_p`|`PETG {color_name}`|`Grey`|{"source_file": "ic3d.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "ic3d_petg_ic3dpetggray_1000_175_p": 250,
    "ic3d_petg_petggrey_1000_175_p": null
  },
  "color_hex": {
    "ic3d_petg_ic3dpetggray_1000_175_p": "808080",
    "ic3d_petg_petggrey_1000_175_p": "45444A"
  },
  "extruder_temp_range": {
    "ic3d_petg_ic3dpetggray_1000_175_p": [
      240,
      270
    ],
    "ic3d_petg_petggrey_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "ic3d_petg_ic3dpetggray_1000_175_p": [
      60,
      80
    ],
    "ic3d_petg_petggrey_1000_175_p": [
      70,
      90
    ]
  }
}
```

### IC008: dup-475b376a091b999da5a792704811f580a86da09e1522b85d1f6f28ae369afce6

Status: APPROVED; survivor `ic3d_petg_petgred_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ic3d_petg_ic3dpetgred_1000_175_p`|`IC3D PETG {color_name}`|`Red`|{"source_file": "ic3d.json", "definition_index": 1, "weights": 3, "diameters": 2, "colors": 6, "compiled_records": 36} / False|
|`ic3d_petg_petgred_1000_175_p`|`PETG {color_name}`|`Red`|{"source_file": "ic3d.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "ic3d_petg_ic3dpetgred_1000_175_p": 250,
    "ic3d_petg_petgred_1000_175_p": null
  },
  "color_hex": {
    "ic3d_petg_ic3dpetgred_1000_175_p": "C01010",
    "ic3d_petg_petgred_1000_175_p": "E60000"
  },
  "extruder_temp_range": {
    "ic3d_petg_ic3dpetgred_1000_175_p": [
      240,
      270
    ],
    "ic3d_petg_petgred_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "ic3d_petg_ic3dpetgred_1000_175_p": [
      60,
      80
    ],
    "ic3d_petg_petgred_1000_175_p": [
      70,
      90
    ]
  }
}
```

### IC009: dup-bf003b5b866d85befa27ff0ba8b25b45ed890d79e2d280a253cf2a01116fa237

Status: APPROVED; survivor `ic3d_petg_petgwhite_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ic3d_petg_ic3dpetgwhite_1000_175_p`|`IC3D PETG {color_name}`|`White`|{"source_file": "ic3d.json", "definition_index": 1, "weights": 3, "diameters": 2, "colors": 6, "compiled_records": 36} / False|
|`ic3d_petg_petgwhite_1000_175_p`|`PETG {color_name}`|`White`|{"source_file": "ic3d.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "ic3d_petg_ic3dpetgwhite_1000_175_p": 250,
    "ic3d_petg_petgwhite_1000_175_p": null
  },
  "color_hex": {
    "ic3d_petg_ic3dpetgwhite_1000_175_p": "F2F2F2",
    "ic3d_petg_petgwhite_1000_175_p": "FFFFFF"
  },
  "extruder_temp_range": {
    "ic3d_petg_ic3dpetgwhite_1000_175_p": [
      240,
      270
    ],
    "ic3d_petg_petgwhite_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "ic3d_petg_ic3dpetgwhite_1000_175_p": [
      60,
      80
    ],
    "ic3d_petg_petgwhite_1000_175_p": [
      70,
      90
    ]
  }
}
```

### IC010: dup-cbdea5d26e6e19a28d087e759f4075617b0efb314916620d7da2e7629c90b884

Status: APPROVED; survivor `ic3d_pla_plablack_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ic3d_pla_ic3dplablack_1000_175_p`|`IC3D PLA {color_name}`|`Black`|{"source_file": "ic3d.json", "definition_index": 0, "weights": 3, "diameters": 2, "colors": 6, "compiled_records": 36} / False|
|`ic3d_pla_plablack_1000_175_p`|`PLA {color_name}`|`Black`|{"source_file": "ic3d.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "ic3d_pla_ic3dplablack_1000_175_p": 250,
    "ic3d_pla_plablack_1000_175_p": null
  },
  "color_hex": {
    "ic3d_pla_ic3dplablack_1000_175_p": "101010",
    "ic3d_pla_plablack_1000_175_p": "000000"
  },
  "extruder_temp_range": {
    "ic3d_pla_ic3dplablack_1000_175_p": [
      200,
      240
    ],
    "ic3d_pla_plablack_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "ic3d_pla_ic3dplablack_1000_175_p": [
      0,
      60
    ],
    "ic3d_pla_plablack_1000_175_p": [
      50,
      70
    ]
  }
}
```

### IC011: dup-3f07ebe3f7af79db9ded16f86be013a81d42090788d8cea3684e772990aa19a8

Status: APPROVED; survivor `ic3d_pla_plablue_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ic3d_pla_ic3dplablue_1000_175_p`|`IC3D PLA {color_name}`|`Blue`|{"source_file": "ic3d.json", "definition_index": 0, "weights": 3, "diameters": 2, "colors": 6, "compiled_records": 36} / False|
|`ic3d_pla_plablue_1000_175_p`|`PLA {color_name}`|`Blue`|{"source_file": "ic3d.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "ic3d_pla_ic3dplablue_1000_175_p": 250,
    "ic3d_pla_plablue_1000_175_p": null
  },
  "color_hex": {
    "ic3d_pla_ic3dplablue_1000_175_p": "1010C0",
    "ic3d_pla_plablue_1000_175_p": "2E56F1"
  },
  "extruder_temp_range": {
    "ic3d_pla_ic3dplablue_1000_175_p": [
      200,
      240
    ],
    "ic3d_pla_plablue_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "ic3d_pla_ic3dplablue_1000_175_p": [
      0,
      60
    ],
    "ic3d_pla_plablue_1000_175_p": [
      50,
      70
    ]
  }
}
```

### IC012: dup-5e424dd4b1493c755c973abbe400db2d1173638fbd6deb712b4984c91bcc7eba

Status: APPROVED; survivor `ic3d_pla_plagrey_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ic3d_pla_ic3dplagray_1000_175_p`|`IC3D PLA {color_name}`|`Gray`|{"source_file": "ic3d.json", "definition_index": 0, "weights": 3, "diameters": 2, "colors": 6, "compiled_records": 36} / False|
|`ic3d_pla_plagrey_1000_175_p`|`PLA {color_name}`|`Grey`|{"source_file": "ic3d.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "ic3d_pla_ic3dplagray_1000_175_p": 250,
    "ic3d_pla_plagrey_1000_175_p": null
  },
  "color_hex": {
    "ic3d_pla_ic3dplagray_1000_175_p": "808080",
    "ic3d_pla_plagrey_1000_175_p": "737282"
  },
  "extruder_temp_range": {
    "ic3d_pla_ic3dplagray_1000_175_p": [
      200,
      240
    ],
    "ic3d_pla_plagrey_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "ic3d_pla_ic3dplagray_1000_175_p": [
      0,
      60
    ],
    "ic3d_pla_plagrey_1000_175_p": [
      50,
      70
    ]
  }
}
```

### IC013: dup-5d2eccd501831d7913201b2ba1c5aded093ec7ed09d93644b0b3259bf15723de

Status: APPROVED; survivor `ic3d_pla_plared_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ic3d_pla_ic3dplared_1000_175_p`|`IC3D PLA {color_name}`|`Red`|{"source_file": "ic3d.json", "definition_index": 0, "weights": 3, "diameters": 2, "colors": 6, "compiled_records": 36} / False|
|`ic3d_pla_plared_1000_175_p`|`PLA {color_name}`|`Red`|{"source_file": "ic3d.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "ic3d_pla_ic3dplared_1000_175_p": 250,
    "ic3d_pla_plared_1000_175_p": null
  },
  "color_hex": {
    "ic3d_pla_ic3dplared_1000_175_p": "C01010",
    "ic3d_pla_plared_1000_175_p": "E60000"
  },
  "extruder_temp_range": {
    "ic3d_pla_ic3dplared_1000_175_p": [
      200,
      240
    ],
    "ic3d_pla_plared_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "ic3d_pla_ic3dplared_1000_175_p": [
      0,
      60
    ],
    "ic3d_pla_plared_1000_175_p": [
      50,
      70
    ]
  }
}
```

### IC014: dup-601aeae28b390b283e43425f6f0f2f91da710cdc5007e380ef262368e7ca7733

Status: APPROVED; survivor `ic3d_pla_plawhite_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ic3d_pla_ic3dplawhite_1000_175_p`|`IC3D PLA {color_name}`|`White`|{"source_file": "ic3d.json", "definition_index": 0, "weights": 3, "diameters": 2, "colors": 6, "compiled_records": 36} / False|
|`ic3d_pla_plawhite_1000_175_p`|`PLA {color_name}`|`White`|{"source_file": "ic3d.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "ic3d_pla_ic3dplawhite_1000_175_p": 250,
    "ic3d_pla_plawhite_1000_175_p": null
  },
  "color_hex": {
    "ic3d_pla_ic3dplawhite_1000_175_p": "F2F2F2",
    "ic3d_pla_plawhite_1000_175_p": "FFFFFF"
  },
  "extruder_temp_range": {
    "ic3d_pla_ic3dplawhite_1000_175_p": [
      200,
      240
    ],
    "ic3d_pla_plawhite_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "ic3d_pla_ic3dplawhite_1000_175_p": [
      0,
      60
    ],
    "ic3d_pla_plawhite_1000_175_p": [
      50,
      70
    ]
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "ic3d_petg_petggrey_1000_175_p",
      "values": {
        "extruder_temp_range": [
          240,
          270
        ],
        "bed_temp_range": null,
        "bed_temp": 70
      },
      "source": "https://www.ic3dprinters.com/shop/petg-filaments/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "ic3d_abs_absblue_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          260
        ],
        "bed_temp_range": null,
        "bed_temp": 110
      },
      "source": "https://www.ic3dprinters.com/shop/abs-filaments/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "ic3d_pla_plablue_1000_175_p",
      "values": {
        "extruder_temp_range": [
          200,
          240
        ],
        "bed_temp_range": null,
        "bed_temp": 60
      },
      "source": "https://www.ic3dprinters.com/shop/pla-filaments/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "ic3d_petg_petgred_1000_175_p",
      "values": {
        "extruder_temp_range": [
          240,
          270
        ],
        "bed_temp_range": null,
        "bed_temp": 70
      },
      "source": "https://www.ic3dprinters.com/shop/petg-filaments/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "ic3d_petg_petgblack_1000_175_p",
      "values": {
        "extruder_temp_range": [
          240,
          270
        ],
        "bed_temp_range": null,
        "bed_temp": 70
      },
      "source": "https://www.ic3dprinters.com/shop/petg-filaments/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "ic3d_pla_plared_1000_175_p",
      "values": {
        "extruder_temp_range": [
          200,
          240
        ],
        "bed_temp_range": null,
        "bed_temp": 60
      },
      "source": "https://www.ic3dprinters.com/shop/pla-filaments/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "ic3d_pla_plagrey_1000_175_p",
      "values": {
        "extruder_temp_range": [
          200,
          240
        ],
        "bed_temp_range": null,
        "bed_temp": 60
      },
      "source": "https://www.ic3dprinters.com/shop/pla-filaments/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "ic3d_pla_plawhite_1000_175_p",
      "values": {
        "extruder_temp_range": [
          200,
          240
        ],
        "bed_temp_range": null,
        "bed_temp": 60
      },
      "source": "https://www.ic3dprinters.com/shop/pla-filaments/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "ic3d_abs_abswhite_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          260
        ],
        "bed_temp_range": null,
        "bed_temp": 110
      },
      "source": "https://www.ic3dprinters.com/shop/abs-filaments/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "ic3d_petg_petgwhite_1000_175_p",
      "values": {
        "extruder_temp_range": [
          240,
          270
        ],
        "bed_temp_range": null,
        "bed_temp": 70
      },
      "source": "https://www.ic3dprinters.com/shop/petg-filaments/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "ic3d_pla_plablack_1000_175_p",
      "values": {
        "extruder_temp_range": [
          200,
          240
        ],
        "bed_temp_range": null,
        "bed_temp": 60
      },
      "source": "https://www.ic3dprinters.com/shop/pla-filaments/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "ic3d_abs_absblack_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          260
        ],
        "bed_temp_range": null,
        "bed_temp": 110
      },
      "source": "https://www.ic3dprinters.com/shop/abs-filaments/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "ic3d_petg_petgblue_1000_175_p",
      "values": {
        "extruder_temp_range": [
          240,
          270
        ],
        "bed_temp_range": null,
        "bed_temp": 70
      },
      "source": "https://www.ic3dprinters.com/shop/petg-filaments/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "ic3d_abs_absgrey_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          260
        ],
        "bed_temp_range": null,
        "bed_temp": 110
      },
      "source": "https://www.ic3dprinters.com/shop/abs-filaments/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    }
  ],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `ic3d_pla_ic3dplagreen_1000_175_p` — IC3D PLA Green
- `ic3d_pla_ic3dplablack_1000_285_p` — IC3D PLA Black
- `ic3d_pla_ic3dplawhite_1000_285_p` — IC3D PLA White
- `ic3d_pla_ic3dplagray_1000_285_p` — IC3D PLA Gray
- `ic3d_pla_ic3dplared_1000_285_p` — IC3D PLA Red
- `ic3d_pla_ic3dplablue_1000_285_p` — IC3D PLA Blue
- `ic3d_pla_ic3dplagreen_1000_285_p` — IC3D PLA Green
- `ic3d_pla_ic3dplablack_2500_175_p` — IC3D PLA Black
- `ic3d_pla_ic3dplawhite_2500_175_p` — IC3D PLA White
- `ic3d_pla_ic3dplagray_2500_175_p` — IC3D PLA Gray
- `ic3d_pla_ic3dplared_2500_175_p` — IC3D PLA Red
- `ic3d_pla_ic3dplablue_2500_175_p` — IC3D PLA Blue
- `ic3d_pla_ic3dplagreen_2500_175_p` — IC3D PLA Green
- `ic3d_pla_ic3dplablack_2500_285_p` — IC3D PLA Black
- `ic3d_pla_ic3dplawhite_2500_285_p` — IC3D PLA White
- `ic3d_pla_ic3dplagray_2500_285_p` — IC3D PLA Gray
- `ic3d_pla_ic3dplared_2500_285_p` — IC3D PLA Red
- `ic3d_pla_ic3dplablue_2500_285_p` — IC3D PLA Blue
- `ic3d_pla_ic3dplagreen_2500_285_p` — IC3D PLA Green
- `ic3d_pla_ic3dplablack_10000_175_p` — IC3D PLA Black
- `ic3d_pla_ic3dplawhite_10000_175_p` — IC3D PLA White
- `ic3d_pla_ic3dplagray_10000_175_p` — IC3D PLA Gray
- `ic3d_pla_ic3dplared_10000_175_p` — IC3D PLA Red
- `ic3d_pla_ic3dplablue_10000_175_p` — IC3D PLA Blue
- `ic3d_pla_ic3dplagreen_10000_175_p` — IC3D PLA Green
- `ic3d_pla_ic3dplablack_10000_285_p` — IC3D PLA Black
- `ic3d_pla_ic3dplawhite_10000_285_p` — IC3D PLA White
- `ic3d_pla_ic3dplagray_10000_285_p` — IC3D PLA Gray
- `ic3d_pla_ic3dplared_10000_285_p` — IC3D PLA Red
- `ic3d_pla_ic3dplablue_10000_285_p` — IC3D PLA Blue
- `ic3d_pla_ic3dplagreen_10000_285_p` — IC3D PLA Green
- `ic3d_petg_ic3dpetggreen_1000_175_p` — IC3D PETG Green
- `ic3d_petg_ic3dpetgblack_1000_285_p` — IC3D PETG Black
- `ic3d_petg_ic3dpetgwhite_1000_285_p` — IC3D PETG White
- `ic3d_petg_ic3dpetggray_1000_285_p` — IC3D PETG Gray
- `ic3d_petg_ic3dpetgred_1000_285_p` — IC3D PETG Red
- `ic3d_petg_ic3dpetgblue_1000_285_p` — IC3D PETG Blue
- `ic3d_petg_ic3dpetggreen_1000_285_p` — IC3D PETG Green
- `ic3d_petg_ic3dpetgblack_2500_175_p` — IC3D PETG Black
- `ic3d_petg_ic3dpetgwhite_2500_175_p` — IC3D PETG White
- `ic3d_petg_ic3dpetggray_2500_175_p` — IC3D PETG Gray
- `ic3d_petg_ic3dpetgred_2500_175_p` — IC3D PETG Red
- `ic3d_petg_ic3dpetgblue_2500_175_p` — IC3D PETG Blue
- `ic3d_petg_ic3dpetggreen_2500_175_p` — IC3D PETG Green
- `ic3d_petg_ic3dpetgblack_2500_285_p` — IC3D PETG Black
- `ic3d_petg_ic3dpetgwhite_2500_285_p` — IC3D PETG White
- `ic3d_petg_ic3dpetggray_2500_285_p` — IC3D PETG Gray
- `ic3d_petg_ic3dpetgred_2500_285_p` — IC3D PETG Red
- `ic3d_petg_ic3dpetgblue_2500_285_p` — IC3D PETG Blue
- `ic3d_petg_ic3dpetggreen_2500_285_p` — IC3D PETG Green
- `ic3d_petg_ic3dpetgblack_10000_175_p` — IC3D PETG Black
- `ic3d_petg_ic3dpetgwhite_10000_175_p` — IC3D PETG White
- `ic3d_petg_ic3dpetggray_10000_175_p` — IC3D PETG Gray
- `ic3d_petg_ic3dpetgred_10000_175_p` — IC3D PETG Red
- `ic3d_petg_ic3dpetgblue_10000_175_p` — IC3D PETG Blue
- `ic3d_petg_ic3dpetggreen_10000_175_p` — IC3D PETG Green
- `ic3d_petg_ic3dpetgblack_10000_285_p` — IC3D PETG Black
- `ic3d_petg_ic3dpetgwhite_10000_285_p` — IC3D PETG White
- `ic3d_petg_ic3dpetggray_10000_285_p` — IC3D PETG Gray
- `ic3d_petg_ic3dpetgred_10000_285_p` — IC3D PETG Red
- `ic3d_petg_ic3dpetgblue_10000_285_p` — IC3D PETG Blue
- `ic3d_petg_ic3dpetggreen_10000_285_p` — IC3D PETG Green
- `ic3d_abs_ic3dabsred_1000_175_p` — IC3D ABS Red
- `ic3d_abs_ic3dabsgreen_1000_175_p` — IC3D ABS Green
- `ic3d_abs_ic3dabsblack_1000_285_p` — IC3D ABS Black
- `ic3d_abs_ic3dabswhite_1000_285_p` — IC3D ABS White
- `ic3d_abs_ic3dabsgray_1000_285_p` — IC3D ABS Gray
- `ic3d_abs_ic3dabsred_1000_285_p` — IC3D ABS Red
- `ic3d_abs_ic3dabsblue_1000_285_p` — IC3D ABS Blue
- `ic3d_abs_ic3dabsgreen_1000_285_p` — IC3D ABS Green
- `ic3d_abs_ic3dabsblack_2500_175_p` — IC3D ABS Black
- `ic3d_abs_ic3dabswhite_2500_175_p` — IC3D ABS White
- `ic3d_abs_ic3dabsgray_2500_175_p` — IC3D ABS Gray
- `ic3d_abs_ic3dabsred_2500_175_p` — IC3D ABS Red
- `ic3d_abs_ic3dabsblue_2500_175_p` — IC3D ABS Blue
- `ic3d_abs_ic3dabsgreen_2500_175_p` — IC3D ABS Green
- `ic3d_abs_ic3dabsblack_2500_285_p` — IC3D ABS Black
- `ic3d_abs_ic3dabswhite_2500_285_p` — IC3D ABS White
- `ic3d_abs_ic3dabsgray_2500_285_p` — IC3D ABS Gray
- `ic3d_abs_ic3dabsred_2500_285_p` — IC3D ABS Red
- `ic3d_abs_ic3dabsblue_2500_285_p` — IC3D ABS Blue
- `ic3d_abs_ic3dabsgreen_2500_285_p` — IC3D ABS Green
- `ic3d_abs_ic3dabsblack_10000_175_p` — IC3D ABS Black
- `ic3d_abs_ic3dabswhite_10000_175_p` — IC3D ABS White
- `ic3d_abs_ic3dabsgray_10000_175_p` — IC3D ABS Gray
- `ic3d_abs_ic3dabsred_10000_175_p` — IC3D ABS Red
- `ic3d_abs_ic3dabsblue_10000_175_p` — IC3D ABS Blue
- `ic3d_abs_ic3dabsgreen_10000_175_p` — IC3D ABS Green
- `ic3d_abs_ic3dabsblack_10000_285_p` — IC3D ABS Black
- `ic3d_abs_ic3dabswhite_10000_285_p` — IC3D ABS White
- `ic3d_abs_ic3dabsgray_10000_285_p` — IC3D ABS Gray
- `ic3d_abs_ic3dabsred_10000_285_p` — IC3D ABS Red
- `ic3d_abs_ic3dabsblue_10000_285_p` — IC3D ABS Blue
- `ic3d_abs_ic3dabsgreen_10000_285_p` — IC3D ABS Green
- `ic3d_abs_absnatural_1000_175_p` — ABS Natural
- `ic3d_abs_absyellow_1000_175_p` — ABS Yellow
- `ic3d_petg_petgcfblack_1000_175_p` — PETG CF Black
- `ic3d_petg_petggreen(bright)_1000_175_p` — PETG Green (Bright)
- `ic3d_petg_petgnatural(clear)_1000_175_p` — PETG Natural (Clear)
- `ic3d_petg_petgpolyhex(hi-temp)black_1000_175_p` — PETG PolyHex™ (Hi-Temp ) Black
- `ic3d_petg_petgrecycledblack_1000_175_p` — PETG Recycled Black
- `ic3d_petg_petgrecyclednatural(clear)_1000_175_p` — PETG Recycled Natural (Clear)
- `ic3d_petg_petgrecycledred_1000_175_p` — PETG Recycled Red
- `ic3d_petg_petgrecycledtranslucentbluerazz_1000_175_p` — PETG Recycled Translucent Blue Razz
- `ic3d_petg_petgrecycledtranslucentcherry_1000_175_p` — PETG Recycled Translucent Cherry
- `ic3d_petg_petgrecycledtranslucentgrape_1000_175_p` — PETG Recycled Translucent Grape
- `ic3d_petg_petgrecycledtranslucenthoney_1000_175_p` — PETG Recycled Translucent Honey
- `ic3d_petg_petgrecycledtranslucentwatermelon_1000_175_p` — PETG Recycled Translucent Watermelon
- `ic3d_petg_petgrecycledwhite_1000_175_p` — PETG Recycled White
- `ic3d_petg_petguv-black_1000_175_p` — PETG UV- Black
- `ic3d_petg_petguv-charcoal_1000_175_p` — PETG UV- Charcoal
- `ic3d_petg_petguv-natural(clear)_1000_175_p` — PETG UV- Natural (Clear)
- `ic3d_petg_petguv-white_1000_175_p` — PETG UV- White
- `ic3d_petg_petgyellow_1000_175_p` — PETG Yellow
- `ic3d_petg_recycledmattepetgbalancedbeige_1000_175_p` — Recycled Matte PETG Balanced Beige
- `ic3d_petg_recycledmattepetgblack_1000_175_p` — Recycled Matte PETG Black
- `ic3d_petg_recycledmattepetgdriftingfog_1000_175_p` — Recycled Matte PETG Drifting Fog
- `ic3d_petg_recycledmattepetggraphitegrey_1000_175_p` — Recycled Matte PETG Graphite Grey
- `ic3d_petg_recycledmattepetgwhite_1000_175_p` — Recycled Matte PETG White
- `ic3d_pla_matteplaimpactmodifiedmossgreen_1000_175_p` — Matte PLA Impact Modified Moss Green
- `ic3d_pla_plaimpactmodifiedblack_1000_175_p` — PLA Impact Modified Black
- `ic3d_pla_plaimpactmodifiedblue_1000_175_p` — PLA Impact Modified Blue
- `ic3d_pla_plaimpactmodifiedgrey_1000_175_p` — PLA Impact Modified Grey
- `ic3d_pla_plaimpactmodifiednatural_1000_175_p` — PLA Impact Modified Natural
- `ic3d_pla_plaimpactmodifiedred_1000_175_p` — PLA Impact Modified Red
- `ic3d_pla_plaimpactmodifiedwhite_1000_175_p` — PLA Impact Modified White
- `ic3d_pla_planatural_1000_175_p` — PLA Natural
- `ic3d_pla_plaorange_1000_175_p` — PLA Orange
- `ic3d_pla_playellow_1000_175_p` — PLA Yellow
