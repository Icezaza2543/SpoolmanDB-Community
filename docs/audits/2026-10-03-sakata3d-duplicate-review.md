# sakata3d duplicate migration review

Base `509259caecaf10d71be91d067bc5f895419f0ee0`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `d73d2a45171b342429eb04af491ce37382c703582c54eb836fecb7ef5c81aa69`.

## Authorization and result

{"groups": 41, "approved_groups": 28, "retired": 28, "deferred": 13, "hard_stops": 0, "before_count": 52141, "after_count": 52113, "brand_before": 799, "brand_after": 771, "registry_before": 1293, "registry_after": 1321, "metadata_fields_changed": 10, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Older well-formed PLA GO&PRINT, PLA HR-870 and PLA WOOD names agree with current official names; Rule3 must precede size/Cartesian selection. Only approved HR-870 targets change bed50–70 to40–60; other survivor values retained. ABS-E versus ABS E color-label decomposition is Rule5 backlog. Current color/packaging/weight matrix not inferred; historical unique broad variants preserved. WOOD printing/density evidence unresolved. Packaging/tare/HEX unchanged.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://sakata3d.com/en/content/34-pla-goprint", "name": "PLA GO&PRINT", "nozzle": [185, 205], "bed": [40, 60], "note": "Current exact product-line name and printing values; no current all-color/diameter sales inference."}
- {"url": "https://sakata3d.com/en/content/36-pla-hr-870", "name": "PLA HR-870", "nozzle": [210, 230], "bed": [40, 60], "note": "Exact current line recommendations. Its official navigation also names PLA WOOD; the separate WOOD technical page could not be retrieved, so no WOOD printing changes are made."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`sakata3d_pla_go&printplablack_1000_175_c`|`sakata3d_pla_plago&printblack_1000_175_c`|`sakata3d.json::Sakata 3D::Go&Print PLA {color_name}::Go&Print PLA Black::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_go&printplablue_1000_175_c`|`sakata3d_pla_plago&printblue_1000_175_c`|`sakata3d.json::Sakata 3D::Go&Print PLA {color_name}::Go&Print PLA Blue::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_go&printplachocolate_1000_175_c`|`sakata3d_pla_plago&printchocolate_1000_175_c`|`sakata3d.json::Sakata 3D::Go&Print PLA {color_name}::Go&Print PLA Chocolate::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_go&printplafuchsia_1000_175_c`|`sakata3d_pla_plago&printfuchsia_1000_175_c`|`sakata3d.json::Sakata 3D::Go&Print PLA {color_name}::Go&Print PLA Fuchsia::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_go&printplagreen_1000_175_c`|`sakata3d_pla_plago&printgreen_1000_175_c`|`sakata3d.json::Sakata 3D::Go&Print PLA {color_name}::Go&Print PLA Green::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_go&printplagrey_1000_175_c`|`sakata3d_pla_plago&printgrey_1000_175_c`|`sakata3d.json::Sakata 3D::Go&Print PLA {color_name}::Go&Print PLA Grey::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_go&printplaorange_1000_175_c`|`sakata3d_pla_plago&printorange_1000_175_c`|`sakata3d.json::Sakata 3D::Go&Print PLA {color_name}::Go&Print PLA Orange::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_go&printplapastelpink_1000_175_c`|`sakata3d_pla_plago&printpastelpink_1000_175_c`|`sakata3d.json::Sakata 3D::Go&Print PLA {color_name}::Go&Print PLA Pastel Pink::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_go&printplapastelyellow_1000_175_c`|`sakata3d_pla_plago&printpastelyellow_1000_175_c`|`sakata3d.json::Sakata 3D::Go&Print PLA {color_name}::Go&Print PLA Pastel Yellow::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_go&printplapink_1000_175_c`|`sakata3d_pla_plago&printpink_1000_175_c`|`sakata3d.json::Sakata 3D::Go&Print PLA {color_name}::Go&Print PLA Pink::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_go&printplapurple_1000_175_c`|`sakata3d_pla_plago&printpurple_1000_175_c`|`sakata3d.json::Sakata 3D::Go&Print PLA {color_name}::Go&Print PLA Purple::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_go&printplared_1000_175_c`|`sakata3d_pla_plago&printred_1000_175_c`|`sakata3d.json::Sakata 3D::Go&Print PLA {color_name}::Go&Print PLA Red::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_go&printplasilver_1000_175_c`|`sakata3d_pla_plago&printsilver_1000_175_c`|`sakata3d.json::Sakata 3D::Go&Print PLA {color_name}::Go&Print PLA Silver::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_go&printplawhite_1000_175_c`|`sakata3d_pla_plago&printwhite_1000_175_c`|`sakata3d.json::Sakata 3D::Go&Print PLA {color_name}::Go&Print PLA White::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_go&printplayellow_1000_175_c`|`sakata3d_pla_plago&printyellow_1000_175_c`|`sakata3d.json::Sakata 3D::Go&Print PLA {color_name}::Go&Print PLA Yellow::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_hr-870plablack_1000_175_c`|`sakata3d_pla_plahr-870black_1000_175_c`|`sakata3d.json::Sakata 3D::HR-870 PLA {color_name}::HR-870 PLA Black::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_hr-870plablue_1000_175_c`|`sakata3d_pla_plahr-870blue_1000_175_c`|`sakata3d.json::Sakata 3D::HR-870 PLA {color_name}::HR-870 PLA Blue::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_hr-870plagreen_1000_175_c`|`sakata3d_pla_plahr-870green_1000_175_c`|`sakata3d.json::Sakata 3D::HR-870 PLA {color_name}::HR-870 PLA Green::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_hr-870plagrey_1000_175_c`|`sakata3d_pla_plahr-870grey_1000_175_c`|`sakata3d.json::Sakata 3D::HR-870 PLA {color_name}::HR-870 PLA Grey::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_hr-870planatural_1000_175_c`|`sakata3d_pla_plahr-870natural_1000_175_c`|`sakata3d.json::Sakata 3D::HR-870 PLA {color_name}::HR-870 PLA Natural::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_hr-870plaorange_1000_175_c`|`sakata3d_pla_plahr-870orange_1000_175_c`|`sakata3d.json::Sakata 3D::HR-870 PLA {color_name}::HR-870 PLA Orange::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_hr-870plared_1000_175_c`|`sakata3d_pla_plahr-870red_1000_175_c`|`sakata3d.json::Sakata 3D::HR-870 PLA {color_name}::HR-870 PLA Red::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_hr-870plasilver_1000_175_c`|`sakata3d_pla_plahr-870silver_1000_175_c`|`sakata3d.json::Sakata 3D::HR-870 PLA {color_name}::HR-870 PLA Silver::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_hr-870plawhite_1000_175_c`|`sakata3d_pla_plahr-870white_1000_175_c`|`sakata3d.json::Sakata 3D::HR-870 PLA {color_name}::HR-870 PLA White::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_hr-870playellow_1000_175_c`|`sakata3d_pla_plahr-870yellow_1000_175_c`|`sakata3d.json::Sakata 3D::HR-870 PLA {color_name}::HR-870 PLA Yellow::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_woodplaarce_1000_175_c`|`sakata3d_pla_plawoodarce_1000_175_c`|`sakata3d.json::Sakata 3D::Wood PLA {color_name}::Wood PLA Arce::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_woodplaoak_1000_175_c`|`sakata3d_pla_plawoodoak_1000_175_c`|`sakata3d.json::Sakata 3D::Wood PLA {color_name}::Wood PLA Oak::PLA::1000::1.75::cardboard::False`|
|`sakata3d_pla_woodplawhite_1000_175_c`|`sakata3d_pla_plawoodwhite_1000_175_c`|`sakata3d.json::Sakata 3D::Wood PLA {color_name}::Wood PLA White::PLA::1000::1.75::cardboard::False`|

## Per-group decisions and unresolved metadata

### SA001: dup-fc0339dfdc4fea9711ba7cc7c0e4ff95b9ed7adbfc2b9ab610839e2ce4e1742e

Status: DEFERRED; survivor `sakata3d_abs_abs-eblack_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_abs_abs-eblack_1000_175_c`|`ABS-E {color_name}`|`Black`|{"source_file": "sakata3d.json", "definition_index": 0, "weights": 4, "diameters": 2, "colors": 14, "compiled_records": 112} / False|
|`sakata3d_abs_abseblack_1000_175_c`|`ABS {color_name}`|`E Black`|{"source_file": "sakata3d.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_abs_abs-eblack_1000_175_c": "211F20",
    "sakata3d_abs_abseblack_1000_175_c": "000000"
  },
  "extruder_temp_range": {
    "sakata3d_abs_abs-eblack_1000_175_c": [
      235,
      250
    ],
    "sakata3d_abs_abseblack_1000_175_c": [
      230,
      260
    ]
  },
  "bed_temp_range": {
    "sakata3d_abs_abs-eblack_1000_175_c": [
      60,
      100
    ],
    "sakata3d_abs_abseblack_1000_175_c": [
      90,
      110
    ]
  }
}
```

### SA002: dup-8c2b47395e9d4e376b3c7e514ef512c6f953bf630b93b0a755561d8bedae6071

Status: DEFERRED; survivor `sakata3d_abs_abs-eblue_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_abs_abs-eblue_1000_175_c`|`ABS-E {color_name}`|`Blue`|{"source_file": "sakata3d.json", "definition_index": 0, "weights": 4, "diameters": 2, "colors": 14, "compiled_records": 112} / False|
|`sakata3d_abs_abseblue_1000_175_c`|`ABS {color_name}`|`E Blue`|{"source_file": "sakata3d.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_abs_abs-eblue_1000_175_c": "1E2460",
    "sakata3d_abs_abseblue_1000_175_c": "2E56F1"
  },
  "extruder_temp_range": {
    "sakata3d_abs_abs-eblue_1000_175_c": [
      235,
      250
    ],
    "sakata3d_abs_abseblue_1000_175_c": [
      230,
      260
    ]
  },
  "bed_temp_range": {
    "sakata3d_abs_abs-eblue_1000_175_c": [
      60,
      100
    ],
    "sakata3d_abs_abseblue_1000_175_c": [
      90,
      110
    ]
  }
}
```

### SA003: dup-e338b02fc883b592f88c3004adcc18297e4da9b96a64fabee9be415f09bfe29b

Status: DEFERRED; survivor `sakata3d_abs_abs-ecaramel_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_abs_abs-ecaramel_1000_175_c`|`ABS-E {color_name}`|`Caramel`|{"source_file": "sakata3d.json", "definition_index": 0, "weights": 4, "diameters": 2, "colors": 14, "compiled_records": 112} / False|
|`sakata3d_abs_absecaramel_1000_175_c`|`ABS {color_name}`|`E Caramel`|{"source_file": "sakata3d.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_abs_abs-ecaramel_1000_175_c": "755847",
    "sakata3d_abs_absecaramel_1000_175_c": "D8BA64"
  },
  "extruder_temp_range": {
    "sakata3d_abs_abs-ecaramel_1000_175_c": [
      235,
      250
    ],
    "sakata3d_abs_absecaramel_1000_175_c": [
      230,
      260
    ]
  },
  "bed_temp_range": {
    "sakata3d_abs_abs-ecaramel_1000_175_c": [
      60,
      100
    ],
    "sakata3d_abs_absecaramel_1000_175_c": [
      90,
      110
    ]
  }
}
```

### SA004: dup-ad6dc53f226b326b8726e6293c8bdc5c3f9fc633dee27009c07d6cc4e33b7696

Status: DEFERRED; survivor `sakata3d_abs_abs-egreen_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_abs_abs-egreen_1000_175_c`|`ABS-E {color_name}`|`Green`|{"source_file": "sakata3d.json", "definition_index": 0, "weights": 4, "diameters": 2, "colors": 14, "compiled_records": 112} / False|
|`sakata3d_abs_absegreen_1000_175_c`|`ABS {color_name}`|`E Green`|{"source_file": "sakata3d.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_abs_abs-egreen_1000_175_c": "57A639",
    "sakata3d_abs_absegreen_1000_175_c": "41A840"
  },
  "extruder_temp_range": {
    "sakata3d_abs_abs-egreen_1000_175_c": [
      235,
      250
    ],
    "sakata3d_abs_absegreen_1000_175_c": [
      230,
      260
    ]
  },
  "bed_temp_range": {
    "sakata3d_abs_abs-egreen_1000_175_c": [
      60,
      100
    ],
    "sakata3d_abs_absegreen_1000_175_c": [
      90,
      110
    ]
  }
}
```

### SA005: dup-6156c03e20684109601c47033543a83ea17ece85647e0a3cc4cf2ff89eddcbbc

Status: DEFERRED; survivor `sakata3d_abs_abs-egrey_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_abs_abs-egrey_1000_175_c`|`ABS-E {color_name}`|`Grey`|{"source_file": "sakata3d.json", "definition_index": 0, "weights": 4, "diameters": 2, "colors": 14, "compiled_records": 112} / False|
|`sakata3d_abs_absegrey_1000_175_c`|`ABS {color_name}`|`E Grey`|{"source_file": "sakata3d.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_abs_abs-egrey_1000_175_c": "9DA3A6",
    "sakata3d_abs_absegrey_1000_175_c": "B8BAB8"
  },
  "extruder_temp_range": {
    "sakata3d_abs_abs-egrey_1000_175_c": [
      235,
      250
    ],
    "sakata3d_abs_absegrey_1000_175_c": [
      230,
      260
    ]
  },
  "bed_temp_range": {
    "sakata3d_abs_abs-egrey_1000_175_c": [
      60,
      100
    ],
    "sakata3d_abs_absegrey_1000_175_c": [
      90,
      110
    ]
  }
}
```

### SA006: dup-1e6880a9890c17ea19e61f60d8f6b8d71a3e5f2325062ca8973a2d24ae0947b8

Status: DEFERRED; survivor `sakata3d_abs_abs-elightblue_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_abs_abs-elightblue_1000_175_c`|`ABS-E {color_name}`|`Light Blue`|{"source_file": "sakata3d.json", "definition_index": 0, "weights": 4, "diameters": 2, "colors": 14, "compiled_records": 112} / False|
|`sakata3d_abs_abselightblue_1000_175_c`|`ABS {color_name}`|`E Light Blue`|{"source_file": "sakata3d.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_abs_abs-elightblue_1000_175_c": "6A93B0",
    "sakata3d_abs_abselightblue_1000_175_c": "40B6E4"
  },
  "extruder_temp_range": {
    "sakata3d_abs_abs-elightblue_1000_175_c": [
      235,
      250
    ],
    "sakata3d_abs_abselightblue_1000_175_c": [
      230,
      260
    ]
  },
  "bed_temp_range": {
    "sakata3d_abs_abs-elightblue_1000_175_c": [
      60,
      100
    ],
    "sakata3d_abs_abselightblue_1000_175_c": [
      90,
      110
    ]
  }
}
```

### SA007: dup-05443d0d02ce51a5d96edec7cbc0574b87f664af0df49c97dcc8e77fbd0bb846

Status: DEFERRED; survivor `sakata3d_abs_abs-enatural_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_abs_abs-enatural_1000_175_c`|`ABS-E {color_name}`|`Natural`|{"source_file": "sakata3d.json", "definition_index": 0, "weights": 4, "diameters": 2, "colors": 14, "compiled_records": 112} / False|
|`sakata3d_abs_absenatural_1000_175_c`|`ABS {color_name}`|`E Natural`|{"source_file": "sakata3d.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_abs_abs-enatural_1000_175_c": "F1F0EA",
    "sakata3d_abs_absenatural_1000_175_c": "F2EFE9"
  },
  "extruder_temp_range": {
    "sakata3d_abs_abs-enatural_1000_175_c": [
      235,
      250
    ],
    "sakata3d_abs_absenatural_1000_175_c": [
      230,
      260
    ]
  },
  "bed_temp_range": {
    "sakata3d_abs_abs-enatural_1000_175_c": [
      60,
      100
    ],
    "sakata3d_abs_absenatural_1000_175_c": [
      90,
      110
    ]
  },
  "translucent": {
    "sakata3d_abs_abs-enatural_1000_175_c": true,
    "sakata3d_abs_absenatural_1000_175_c": false
  }
}
```

### SA008: dup-6d6952a9caa39476ad71098dd1cf84e3e7510b3f3447493695403d41c1b33d86

Status: DEFERRED; survivor `sakata3d_abs_abs-epurple_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_abs_abs-epurple_1000_175_c`|`ABS-E {color_name}`|`Purple`|{"source_file": "sakata3d.json", "definition_index": 0, "weights": 4, "diameters": 2, "colors": 14, "compiled_records": 112} / False|
|`sakata3d_abs_absepurple_1000_175_c`|`ABS {color_name}`|`E Purple`|{"source_file": "sakata3d.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_abs_abs-epurple_1000_175_c": "6D6680",
    "sakata3d_abs_absepurple_1000_175_c": "A67DFF"
  },
  "extruder_temp_range": {
    "sakata3d_abs_abs-epurple_1000_175_c": [
      235,
      250
    ],
    "sakata3d_abs_absepurple_1000_175_c": [
      230,
      260
    ]
  },
  "bed_temp_range": {
    "sakata3d_abs_abs-epurple_1000_175_c": [
      60,
      100
    ],
    "sakata3d_abs_absepurple_1000_175_c": [
      90,
      110
    ]
  }
}
```

### SA009: dup-1703e283b23ad6ea45bd62af65ffa465248daad5a245c25567bed4ab08fb6a5b

Status: DEFERRED; survivor `sakata3d_abs_abs-ered_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_abs_abs-ered_1000_175_c`|`ABS-E {color_name}`|`Red`|{"source_file": "sakata3d.json", "definition_index": 0, "weights": 4, "diameters": 2, "colors": 14, "compiled_records": 112} / False|
|`sakata3d_abs_absered_1000_175_c`|`ABS {color_name}`|`E Red`|{"source_file": "sakata3d.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_abs_abs-ered_1000_175_c": "CB2821",
    "sakata3d_abs_absered_1000_175_c": "E72F1D"
  },
  "extruder_temp_range": {
    "sakata3d_abs_abs-ered_1000_175_c": [
      235,
      250
    ],
    "sakata3d_abs_absered_1000_175_c": [
      230,
      260
    ]
  },
  "bed_temp_range": {
    "sakata3d_abs_abs-ered_1000_175_c": [
      60,
      100
    ],
    "sakata3d_abs_absered_1000_175_c": [
      90,
      110
    ]
  }
}
```

### SA010: dup-2c6751ea05416fdb6ea31d960150d50efadb8b29e0879fc6d549e7f9c3ee5488

Status: DEFERRED; survivor `sakata3d_abs_abs-esilver_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_abs_abs-esilver_1000_175_c`|`ABS-E {color_name}`|`Silver`|{"source_file": "sakata3d.json", "definition_index": 0, "weights": 4, "diameters": 2, "colors": 14, "compiled_records": 112} / False|
|`sakata3d_abs_absesilver_1000_175_c`|`ABS {color_name}`|`E Silver`|{"source_file": "sakata3d.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_abs_abs-esilver_1000_175_c": "8C9196",
    "sakata3d_abs_absesilver_1000_175_c": "CACACA"
  },
  "extruder_temp_range": {
    "sakata3d_abs_abs-esilver_1000_175_c": [
      235,
      250
    ],
    "sakata3d_abs_absesilver_1000_175_c": [
      230,
      260
    ]
  },
  "bed_temp_range": {
    "sakata3d_abs_abs-esilver_1000_175_c": [
      60,
      100
    ],
    "sakata3d_abs_absesilver_1000_175_c": [
      90,
      110
    ]
  }
}
```

### SA011: dup-ab103ad2d96af760cf58cc67aa99a7af37943c6ceefb97459adef7dc6574076a

Status: DEFERRED; survivor `sakata3d_abs_abs-etile_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_abs_abs-etile_1000_175_c`|`ABS-E {color_name}`|`Tile`|{"source_file": "sakata3d.json", "definition_index": 0, "weights": 4, "diameters": 2, "colors": 14, "compiled_records": 112} / False|
|`sakata3d_abs_absetile_1000_175_c`|`ABS {color_name}`|`E TILE`|{"source_file": "sakata3d.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_abs_abs-etile_1000_175_c": "D05D28",
    "sakata3d_abs_absetile_1000_175_c": "A54830"
  },
  "extruder_temp_range": {
    "sakata3d_abs_abs-etile_1000_175_c": [
      235,
      250
    ],
    "sakata3d_abs_absetile_1000_175_c": [
      230,
      260
    ]
  },
  "bed_temp_range": {
    "sakata3d_abs_abs-etile_1000_175_c": [
      60,
      100
    ],
    "sakata3d_abs_absetile_1000_175_c": [
      90,
      110
    ]
  }
}
```

### SA012: dup-c42ec7b0355cd6016c3ded390785e1b7e782c3e57ffb9cbc56bd6722899d9024

Status: DEFERRED; survivor `sakata3d_abs_abs-ewhite_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_abs_abs-ewhite_1000_175_c`|`ABS-E {color_name}`|`White`|{"source_file": "sakata3d.json", "definition_index": 0, "weights": 4, "diameters": 2, "colors": 14, "compiled_records": 112} / False|
|`sakata3d_abs_absewhite_1000_175_c`|`ABS {color_name}`|`E White`|{"source_file": "sakata3d.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_abs_abs-ewhite_1000_175_c": "F6F6F6",
    "sakata3d_abs_absewhite_1000_175_c": "FFFFFF"
  },
  "extruder_temp_range": {
    "sakata3d_abs_abs-ewhite_1000_175_c": [
      235,
      250
    ],
    "sakata3d_abs_absewhite_1000_175_c": [
      230,
      260
    ]
  },
  "bed_temp_range": {
    "sakata3d_abs_abs-ewhite_1000_175_c": [
      60,
      100
    ],
    "sakata3d_abs_absewhite_1000_175_c": [
      90,
      110
    ]
  }
}
```

### SA013: dup-716e61f2979a854d7d7d4040bb7de7e1eaedccb207c207f67ac517ac39cfc5b3

Status: DEFERRED; survivor `sakata3d_abs_abs-eyellow_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_abs_abs-eyellow_1000_175_c`|`ABS-E {color_name}`|`Yellow`|{"source_file": "sakata3d.json", "definition_index": 0, "weights": 4, "diameters": 2, "colors": 14, "compiled_records": 112} / False|
|`sakata3d_abs_abseyellow_1000_175_c`|`ABS {color_name}`|`E Yellow`|{"source_file": "sakata3d.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_abs_abs-eyellow_1000_175_c": "FAD201",
    "sakata3d_abs_abseyellow_1000_175_c": "FBE200"
  },
  "extruder_temp_range": {
    "sakata3d_abs_abs-eyellow_1000_175_c": [
      235,
      250
    ],
    "sakata3d_abs_abseyellow_1000_175_c": [
      230,
      260
    ]
  },
  "bed_temp_range": {
    "sakata3d_abs_abs-eyellow_1000_175_c": [
      60,
      100
    ],
    "sakata3d_abs_abseyellow_1000_175_c": [
      90,
      110
    ]
  }
}
```

### SA014: dup-8d122dc3c1bf4e66a9708a91cc8eb7c66e9435903b312fe4d40f32d2f14c4e3b

Status: APPROVED; survivor `sakata3d_pla_plago&printblack_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_go&printplablack_1000_175_c`|`Go&Print PLA {color_name}`|`Black`|{"source_file": "sakata3d.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 23, "compiled_records": 23} / False|
|`sakata3d_pla_plago&printblack_1000_175_c`|`PLA GO&PRINT {color_name}`|`Black`|{"source_file": "sakata3d.json", "definition_index": 12, "weights": 1, "diameters": 2, "colors": 16, "compiled_records": 32} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_go&printplablack_1000_175_c": "000000",
    "sakata3d_pla_plago&printblack_1000_175_c": "211F20"
  },
  "extruder_temp_range": {
    "sakata3d_pla_go&printplablack_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plago&printblack_1000_175_c": [
      185,
      205
    ]
  },
  "bed_temp_range": {
    "sakata3d_pla_go&printplablack_1000_175_c": [
      50,
      70
    ],
    "sakata3d_pla_plago&printblack_1000_175_c": [
      40,
      60
    ]
  }
}
```

### SA015: dup-aedb065b5eeb44c14d666942db6f7d03c2d43f5a12512a3678b4a33f6d93d3a3

Status: APPROVED; survivor `sakata3d_pla_plago&printblue_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_go&printplablue_1000_175_c`|`Go&Print PLA {color_name}`|`Blue`|{"source_file": "sakata3d.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 23, "compiled_records": 23} / False|
|`sakata3d_pla_plago&printblue_1000_175_c`|`PLA GO&PRINT {color_name}`|`Blue`|{"source_file": "sakata3d.json", "definition_index": 12, "weights": 1, "diameters": 2, "colors": 16, "compiled_records": 32} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_go&printplablue_1000_175_c": "2E56F1",
    "sakata3d_pla_plago&printblue_1000_175_c": "1E2460"
  },
  "extruder_temp_range": {
    "sakata3d_pla_go&printplablue_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plago&printblue_1000_175_c": [
      185,
      205
    ]
  },
  "bed_temp_range": {
    "sakata3d_pla_go&printplablue_1000_175_c": [
      50,
      70
    ],
    "sakata3d_pla_plago&printblue_1000_175_c": [
      40,
      60
    ]
  }
}
```

### SA016: dup-4a77b0299ea0c224c788eaff5594a82d935c315330de518eb72c106f929caf30

Status: APPROVED; survivor `sakata3d_pla_plago&printchocolate_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_go&printplachocolate_1000_175_c`|`Go&Print PLA {color_name}`|`Chocolate`|{"source_file": "sakata3d.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 23, "compiled_records": 23} / False|
|`sakata3d_pla_plago&printchocolate_1000_175_c`|`PLA GO&PRINT {color_name}`|`Chocolate`|{"source_file": "sakata3d.json", "definition_index": 12, "weights": 1, "diameters": 2, "colors": 16, "compiled_records": 32} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_go&printplachocolate_1000_175_c": "6E4325",
    "sakata3d_pla_plago&printchocolate_1000_175_c": "755847"
  },
  "extruder_temp_range": {
    "sakata3d_pla_go&printplachocolate_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plago&printchocolate_1000_175_c": [
      185,
      205
    ]
  },
  "bed_temp_range": {
    "sakata3d_pla_go&printplachocolate_1000_175_c": [
      50,
      70
    ],
    "sakata3d_pla_plago&printchocolate_1000_175_c": [
      40,
      60
    ]
  }
}
```

### SA017: dup-4e83c9a04ecbf0c64f5c4d3aac2363a172191a731b082f69e73e6462dd3a576e

Status: APPROVED; survivor `sakata3d_pla_plago&printfuchsia_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_go&printplafuchsia_1000_175_c`|`Go&Print PLA {color_name}`|`Fuchsia`|{"source_file": "sakata3d.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 23, "compiled_records": 23} / False|
|`sakata3d_pla_plago&printfuchsia_1000_175_c`|`PLA GO&PRINT {color_name}`|`Fuchsia`|{"source_file": "sakata3d.json", "definition_index": 12, "weights": 1, "diameters": 2, "colors": 16, "compiled_records": 32} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_go&printplafuchsia_1000_175_c": "FF72B6",
    "sakata3d_pla_plago&printfuchsia_1000_175_c": "6A5D7B"
  },
  "extruder_temp_range": {
    "sakata3d_pla_go&printplafuchsia_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plago&printfuchsia_1000_175_c": [
      185,
      205
    ]
  },
  "bed_temp_range": {
    "sakata3d_pla_go&printplafuchsia_1000_175_c": [
      50,
      70
    ],
    "sakata3d_pla_plago&printfuchsia_1000_175_c": [
      40,
      60
    ]
  }
}
```

### SA018: dup-a8f83273b422689a699b222081fb25bba5d63975a5e046473cad391b8c99d375

Status: APPROVED; survivor `sakata3d_pla_plago&printgreen_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_go&printplagreen_1000_175_c`|`Go&Print PLA {color_name}`|`Green`|{"source_file": "sakata3d.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 23, "compiled_records": 23} / False|
|`sakata3d_pla_plago&printgreen_1000_175_c`|`PLA GO&PRINT {color_name}`|`Green`|{"source_file": "sakata3d.json", "definition_index": 12, "weights": 1, "diameters": 2, "colors": 16, "compiled_records": 32} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_go&printplagreen_1000_175_c": "7FE200",
    "sakata3d_pla_plago&printgreen_1000_175_c": "57A639"
  },
  "extruder_temp_range": {
    "sakata3d_pla_go&printplagreen_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plago&printgreen_1000_175_c": [
      185,
      205
    ]
  },
  "bed_temp_range": {
    "sakata3d_pla_go&printplagreen_1000_175_c": [
      50,
      70
    ],
    "sakata3d_pla_plago&printgreen_1000_175_c": [
      40,
      60
    ]
  }
}
```

### SA019: dup-25e14f05e8a99d92c3d233030ecf519dfe2ad95be88f482d4bba473a367dd9df

Status: APPROVED; survivor `sakata3d_pla_plago&printgrey_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_go&printplagrey_1000_175_c`|`Go&Print PLA {color_name}`|`Grey`|{"source_file": "sakata3d.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 23, "compiled_records": 23} / False|
|`sakata3d_pla_plago&printgrey_1000_175_c`|`PLA GO&PRINT {color_name}`|`Grey`|{"source_file": "sakata3d.json", "definition_index": 12, "weights": 1, "diameters": 2, "colors": 16, "compiled_records": 32} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_go&printplagrey_1000_175_c": "B6B9BD",
    "sakata3d_pla_plago&printgrey_1000_175_c": "9DA3A6"
  },
  "extruder_temp_range": {
    "sakata3d_pla_go&printplagrey_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plago&printgrey_1000_175_c": [
      185,
      205
    ]
  },
  "bed_temp_range": {
    "sakata3d_pla_go&printplagrey_1000_175_c": [
      50,
      70
    ],
    "sakata3d_pla_plago&printgrey_1000_175_c": [
      40,
      60
    ]
  }
}
```

### SA020: dup-bea6103474eb12869748e2f675ebfa8093b812526a757d982e861f321e9339d0

Status: APPROVED; survivor `sakata3d_pla_plago&printorange_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_go&printplaorange_1000_175_c`|`Go&Print PLA {color_name}`|`Orange`|{"source_file": "sakata3d.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 23, "compiled_records": 23} / False|
|`sakata3d_pla_plago&printorange_1000_175_c`|`PLA GO&PRINT {color_name}`|`Orange`|{"source_file": "sakata3d.json", "definition_index": 12, "weights": 1, "diameters": 2, "colors": 16, "compiled_records": 32} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_go&printplaorange_1000_175_c": "FFB031",
    "sakata3d_pla_plago&printorange_1000_175_c": "D05D28"
  },
  "extruder_temp_range": {
    "sakata3d_pla_go&printplaorange_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plago&printorange_1000_175_c": [
      185,
      205
    ]
  },
  "bed_temp_range": {
    "sakata3d_pla_go&printplaorange_1000_175_c": [
      50,
      70
    ],
    "sakata3d_pla_plago&printorange_1000_175_c": [
      40,
      60
    ]
  }
}
```

### SA021: dup-9e28b41e41422bf1590664484c92b145e79c9c9e5222bcbc762ac5baecaaec34

Status: APPROVED; survivor `sakata3d_pla_plago&printpastelpink_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_go&printplapastelpink_1000_175_c`|`Go&Print PLA {color_name}`|`Pastel Pink`|{"source_file": "sakata3d.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 23, "compiled_records": 23} / False|
|`sakata3d_pla_plago&printpastelpink_1000_175_c`|`PLA GO&PRINT {color_name}`|`Pastel Pink`|{"source_file": "sakata3d.json", "definition_index": 12, "weights": 1, "diameters": 2, "colors": 16, "compiled_records": 32} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_go&printplapastelpink_1000_175_c": "FFC8C9",
    "sakata3d_pla_plago&printpastelpink_1000_175_c": "CB8D73"
  },
  "extruder_temp_range": {
    "sakata3d_pla_go&printplapastelpink_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plago&printpastelpink_1000_175_c": [
      185,
      205
    ]
  },
  "bed_temp_range": {
    "sakata3d_pla_go&printplapastelpink_1000_175_c": [
      50,
      70
    ],
    "sakata3d_pla_plago&printpastelpink_1000_175_c": [
      40,
      60
    ]
  }
}
```

### SA022: dup-920fac56c8ebcdab01722c796672cbf799f2772cb0b73bba025ed4d89ea3f534

Status: APPROVED; survivor `sakata3d_pla_plago&printpastelyellow_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_go&printplapastelyellow_1000_175_c`|`Go&Print PLA {color_name}`|`Pastel Yellow`|{"source_file": "sakata3d.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 23, "compiled_records": 23} / False|
|`sakata3d_pla_plago&printpastelyellow_1000_175_c`|`PLA GO&PRINT {color_name}`|`Pastel Yellow`|{"source_file": "sakata3d.json", "definition_index": 12, "weights": 1, "diameters": 2, "colors": 16, "compiled_records": 32} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_go&printplapastelyellow_1000_175_c": "FCE575",
    "sakata3d_pla_plago&printpastelyellow_1000_175_c": "FAD201"
  },
  "extruder_temp_range": {
    "sakata3d_pla_go&printplapastelyellow_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plago&printpastelyellow_1000_175_c": [
      185,
      205
    ]
  },
  "bed_temp_range": {
    "sakata3d_pla_go&printplapastelyellow_1000_175_c": [
      50,
      70
    ],
    "sakata3d_pla_plago&printpastelyellow_1000_175_c": [
      40,
      60
    ]
  }
}
```

### SA023: dup-b46e2b829a91bf1c7fae7bda35b6a0f80a7a89e8f802ae415c06989c84c17feb

Status: APPROVED; survivor `sakata3d_pla_plago&printpink_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_go&printplapink_1000_175_c`|`Go&Print PLA {color_name}`|`Pink`|{"source_file": "sakata3d.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 23, "compiled_records": 23} / False|
|`sakata3d_pla_plago&printpink_1000_175_c`|`PLA GO&PRINT {color_name}`|`Pink`|{"source_file": "sakata3d.json", "definition_index": 12, "weights": 1, "diameters": 2, "colors": 16, "compiled_records": 32} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_go&printplapink_1000_175_c": "FB637E",
    "sakata3d_pla_plago&printpink_1000_175_c": "CB8D73"
  },
  "extruder_temp_range": {
    "sakata3d_pla_go&printplapink_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plago&printpink_1000_175_c": [
      185,
      205
    ]
  },
  "bed_temp_range": {
    "sakata3d_pla_go&printplapink_1000_175_c": [
      50,
      70
    ],
    "sakata3d_pla_plago&printpink_1000_175_c": [
      40,
      60
    ]
  }
}
```

### SA024: dup-1d92a8dde3cdcd1b81d23dde2c5aef4ec60776e4caec1bc5dcf4b4298434b136

Status: APPROVED; survivor `sakata3d_pla_plago&printpurple_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_go&printplapurple_1000_175_c`|`Go&Print PLA {color_name}`|`Purple`|{"source_file": "sakata3d.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 23, "compiled_records": 23} / False|
|`sakata3d_pla_plago&printpurple_1000_175_c`|`PLA GO&PRINT {color_name}`|`Purple`|{"source_file": "sakata3d.json", "definition_index": 12, "weights": 1, "diameters": 2, "colors": 16, "compiled_records": 32} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_go&printplapurple_1000_175_c": "AE00FF",
    "sakata3d_pla_plago&printpurple_1000_175_c": "6D6680"
  },
  "extruder_temp_range": {
    "sakata3d_pla_go&printplapurple_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plago&printpurple_1000_175_c": [
      185,
      205
    ]
  },
  "bed_temp_range": {
    "sakata3d_pla_go&printplapurple_1000_175_c": [
      50,
      70
    ],
    "sakata3d_pla_plago&printpurple_1000_175_c": [
      40,
      60
    ]
  }
}
```

### SA025: dup-0ea227a40b1379480d09b147d66e52368843ae9df15034c8d2001adeb7ec8223

Status: APPROVED; survivor `sakata3d_pla_plago&printred_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_go&printplared_1000_175_c`|`Go&Print PLA {color_name}`|`Red`|{"source_file": "sakata3d.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 23, "compiled_records": 23} / False|
|`sakata3d_pla_plago&printred_1000_175_c`|`PLA GO&PRINT {color_name}`|`Red`|{"source_file": "sakata3d.json", "definition_index": 12, "weights": 1, "diameters": 2, "colors": 16, "compiled_records": 32} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_go&printplared_1000_175_c": "E20010",
    "sakata3d_pla_plago&printred_1000_175_c": "CB2821"
  },
  "extruder_temp_range": {
    "sakata3d_pla_go&printplared_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plago&printred_1000_175_c": [
      185,
      205
    ]
  },
  "bed_temp_range": {
    "sakata3d_pla_go&printplared_1000_175_c": [
      50,
      70
    ],
    "sakata3d_pla_plago&printred_1000_175_c": [
      40,
      60
    ]
  }
}
```

### SA026: dup-5923321893b7e9d5a90edacae47567536d348b3c5db0bcbd99b16128975cae8c

Status: APPROVED; survivor `sakata3d_pla_plago&printsilver_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_go&printplasilver_1000_175_c`|`Go&Print PLA {color_name}`|`Silver`|{"source_file": "sakata3d.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 23, "compiled_records": 23} / False|
|`sakata3d_pla_plago&printsilver_1000_175_c`|`PLA GO&PRINT {color_name}`|`Silver`|{"source_file": "sakata3d.json", "definition_index": 12, "weights": 1, "diameters": 2, "colors": 16, "compiled_records": 32} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_go&printplasilver_1000_175_c": "ABACB0",
    "sakata3d_pla_plago&printsilver_1000_175_c": "8C9196"
  },
  "extruder_temp_range": {
    "sakata3d_pla_go&printplasilver_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plago&printsilver_1000_175_c": [
      185,
      205
    ]
  },
  "bed_temp_range": {
    "sakata3d_pla_go&printplasilver_1000_175_c": [
      50,
      70
    ],
    "sakata3d_pla_plago&printsilver_1000_175_c": [
      40,
      60
    ]
  }
}
```

### SA027: dup-498e37c940342128b30e50c3165438eb1b3525b9e8fc3a05e5773f4af84d6e60

Status: APPROVED; survivor `sakata3d_pla_plago&printwhite_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_go&printplawhite_1000_175_c`|`Go&Print PLA {color_name}`|`White`|{"source_file": "sakata3d.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 23, "compiled_records": 23} / False|
|`sakata3d_pla_plago&printwhite_1000_175_c`|`PLA GO&PRINT {color_name}`|`White`|{"source_file": "sakata3d.json", "definition_index": 12, "weights": 1, "diameters": 2, "colors": 16, "compiled_records": 32} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_go&printplawhite_1000_175_c": "FFFFFF",
    "sakata3d_pla_plago&printwhite_1000_175_c": "F6F6F6"
  },
  "extruder_temp_range": {
    "sakata3d_pla_go&printplawhite_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plago&printwhite_1000_175_c": [
      185,
      205
    ]
  },
  "bed_temp_range": {
    "sakata3d_pla_go&printplawhite_1000_175_c": [
      50,
      70
    ],
    "sakata3d_pla_plago&printwhite_1000_175_c": [
      40,
      60
    ]
  }
}
```

### SA028: dup-730ed3699fe54b80f11bb246dbe053a89d4975276ee90d8ba809c47f36ee720e

Status: APPROVED; survivor `sakata3d_pla_plago&printyellow_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_go&printplayellow_1000_175_c`|`Go&Print PLA {color_name}`|`Yellow`|{"source_file": "sakata3d.json", "definition_index": 19, "weights": 1, "diameters": 1, "colors": 23, "compiled_records": 23} / False|
|`sakata3d_pla_plago&printyellow_1000_175_c`|`PLA GO&PRINT {color_name}`|`Yellow`|{"source_file": "sakata3d.json", "definition_index": 12, "weights": 1, "diameters": 2, "colors": 16, "compiled_records": 32} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_go&printplayellow_1000_175_c": "F3C102",
    "sakata3d_pla_plago&printyellow_1000_175_c": "FAD201"
  },
  "extruder_temp_range": {
    "sakata3d_pla_go&printplayellow_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plago&printyellow_1000_175_c": [
      185,
      205
    ]
  },
  "bed_temp_range": {
    "sakata3d_pla_go&printplayellow_1000_175_c": [
      50,
      70
    ],
    "sakata3d_pla_plago&printyellow_1000_175_c": [
      40,
      60
    ]
  }
}
```

### SA029: dup-5438af9f3c8f149d405b68bdc835ed460c2a526466fb8b8ac681ac8866802f08

Status: APPROVED; survivor `sakata3d_pla_plahr-870black_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_hr-870plablack_1000_175_c`|`HR-870 PLA {color_name}`|`Black`|{"source_file": "sakata3d.json", "definition_index": 21, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`sakata3d_pla_plahr-870black_1000_175_c`|`PLA HR-870 {color_name}`|`Black`|{"source_file": "sakata3d.json", "definition_index": 13, "weights": 1, "diameters": 2, "colors": 10, "compiled_records": 20} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_hr-870plablack_1000_175_c": "000000",
    "sakata3d_pla_plahr-870black_1000_175_c": "211F20"
  },
  "extruder_temp_range": {
    "sakata3d_pla_hr-870plablack_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plahr-870black_1000_175_c": [
      210,
      230
    ]
  }
}
```

### SA030: dup-f5a7a72acf1c9e4e5222e61458ee73c589ba3e5f2d2808c2bd7fcd846fa64829

Status: APPROVED; survivor `sakata3d_pla_plahr-870blue_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_hr-870plablue_1000_175_c`|`HR-870 PLA {color_name}`|`Blue`|{"source_file": "sakata3d.json", "definition_index": 21, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`sakata3d_pla_plahr-870blue_1000_175_c`|`PLA HR-870 {color_name}`|`Blue`|{"source_file": "sakata3d.json", "definition_index": 13, "weights": 1, "diameters": 2, "colors": 10, "compiled_records": 20} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_hr-870plablue_1000_175_c": "2E56F1",
    "sakata3d_pla_plahr-870blue_1000_175_c": "1E2460"
  },
  "extruder_temp_range": {
    "sakata3d_pla_hr-870plablue_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plahr-870blue_1000_175_c": [
      210,
      230
    ]
  }
}
```

### SA031: dup-3dc5844527dc435a5066f90fa10302870828e3a5f7fb828615a40d8056175317

Status: APPROVED; survivor `sakata3d_pla_plahr-870green_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_hr-870plagreen_1000_175_c`|`HR-870 PLA {color_name}`|`Green`|{"source_file": "sakata3d.json", "definition_index": 21, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`sakata3d_pla_plahr-870green_1000_175_c`|`PLA HR-870 {color_name}`|`Green`|{"source_file": "sakata3d.json", "definition_index": 13, "weights": 1, "diameters": 2, "colors": 10, "compiled_records": 20} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_hr-870plagreen_1000_175_c": "58C91B",
    "sakata3d_pla_plahr-870green_1000_175_c": "57A639"
  },
  "extruder_temp_range": {
    "sakata3d_pla_hr-870plagreen_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plahr-870green_1000_175_c": [
      210,
      230
    ]
  }
}
```

### SA032: dup-e7242abf1890a4d28f1a6d36c502533547e48c6a1feecbfda3a99d34a7b2f314

Status: APPROVED; survivor `sakata3d_pla_plahr-870grey_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_hr-870plagrey_1000_175_c`|`HR-870 PLA {color_name}`|`Grey`|{"source_file": "sakata3d.json", "definition_index": 21, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`sakata3d_pla_plahr-870grey_1000_175_c`|`PLA HR-870 {color_name}`|`Grey`|{"source_file": "sakata3d.json", "definition_index": 13, "weights": 1, "diameters": 2, "colors": 10, "compiled_records": 20} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_hr-870plagrey_1000_175_c": "B8BAB8",
    "sakata3d_pla_plahr-870grey_1000_175_c": "9DA3A6"
  },
  "extruder_temp_range": {
    "sakata3d_pla_hr-870plagrey_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plahr-870grey_1000_175_c": [
      210,
      230
    ]
  }
}
```

### SA033: dup-ed5f47890c9cc00c05b474d1cd75873ff01c7a304de34d09fa3215002959abb9

Status: APPROVED; survivor `sakata3d_pla_plahr-870natural_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_hr-870planatural_1000_175_c`|`HR-870 PLA {color_name}`|`Natural`|{"source_file": "sakata3d.json", "definition_index": 21, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`sakata3d_pla_plahr-870natural_1000_175_c`|`PLA HR-870 {color_name}`|`Natural`|{"source_file": "sakata3d.json", "definition_index": 13, "weights": 1, "diameters": 2, "colors": 10, "compiled_records": 20} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_hr-870planatural_1000_175_c": "F2EFE9",
    "sakata3d_pla_plahr-870natural_1000_175_c": "F1F0EA"
  },
  "extruder_temp_range": {
    "sakata3d_pla_hr-870planatural_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plahr-870natural_1000_175_c": [
      210,
      230
    ]
  },
  "translucent": {
    "sakata3d_pla_hr-870planatural_1000_175_c": false,
    "sakata3d_pla_plahr-870natural_1000_175_c": true
  }
}
```

### SA034: dup-80808d519258cab1a74bda6bf3987787815f1b16a3dae67df78b33cc56a7a543

Status: APPROVED; survivor `sakata3d_pla_plahr-870orange_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_hr-870plaorange_1000_175_c`|`HR-870 PLA {color_name}`|`Orange`|{"source_file": "sakata3d.json", "definition_index": 21, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`sakata3d_pla_plahr-870orange_1000_175_c`|`PLA HR-870 {color_name}`|`Orange`|{"source_file": "sakata3d.json", "definition_index": 13, "weights": 1, "diameters": 2, "colors": 10, "compiled_records": 20} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_hr-870plaorange_1000_175_c": "FF9A14",
    "sakata3d_pla_plahr-870orange_1000_175_c": "D05D28"
  },
  "extruder_temp_range": {
    "sakata3d_pla_hr-870plaorange_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plahr-870orange_1000_175_c": [
      210,
      230
    ]
  }
}
```

### SA035: dup-9558fec26ad3a035e5e133ca4e40ca467397020d6c50ce9478de259ca4e7d4d7

Status: APPROVED; survivor `sakata3d_pla_plahr-870red_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_hr-870plared_1000_175_c`|`HR-870 PLA {color_name}`|`Red`|{"source_file": "sakata3d.json", "definition_index": 21, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`sakata3d_pla_plahr-870red_1000_175_c`|`PLA HR-870 {color_name}`|`Red`|{"source_file": "sakata3d.json", "definition_index": 13, "weights": 1, "diameters": 2, "colors": 10, "compiled_records": 20} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_hr-870plared_1000_175_c": "E20010",
    "sakata3d_pla_plahr-870red_1000_175_c": "CB2821"
  },
  "extruder_temp_range": {
    "sakata3d_pla_hr-870plared_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plahr-870red_1000_175_c": [
      210,
      230
    ]
  }
}
```

### SA036: dup-7d6debdc15885c1d1ffdb0b76f7ab9e5a59f82506518eaf36658f215c542bf1a

Status: APPROVED; survivor `sakata3d_pla_plahr-870silver_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_hr-870plasilver_1000_175_c`|`HR-870 PLA {color_name}`|`Silver`|{"source_file": "sakata3d.json", "definition_index": 21, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`sakata3d_pla_plahr-870silver_1000_175_c`|`PLA HR-870 {color_name}`|`Silver`|{"source_file": "sakata3d.json", "definition_index": 13, "weights": 1, "diameters": 2, "colors": 10, "compiled_records": 20} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_hr-870plasilver_1000_175_c": "ABACB0",
    "sakata3d_pla_plahr-870silver_1000_175_c": "8C9196"
  },
  "extruder_temp_range": {
    "sakata3d_pla_hr-870plasilver_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plahr-870silver_1000_175_c": [
      210,
      230
    ]
  }
}
```

### SA037: dup-f1294cd316ea41c7e34eba8f3e540bd35c61eda213bb5cb27fca7b145a321faf

Status: APPROVED; survivor `sakata3d_pla_plahr-870white_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_hr-870plawhite_1000_175_c`|`HR-870 PLA {color_name}`|`White`|{"source_file": "sakata3d.json", "definition_index": 21, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`sakata3d_pla_plahr-870white_1000_175_c`|`PLA HR-870 {color_name}`|`White`|{"source_file": "sakata3d.json", "definition_index": 13, "weights": 1, "diameters": 2, "colors": 10, "compiled_records": 20} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_hr-870plawhite_1000_175_c": "FFFFFF",
    "sakata3d_pla_plahr-870white_1000_175_c": "F6F6F6"
  },
  "extruder_temp_range": {
    "sakata3d_pla_hr-870plawhite_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plahr-870white_1000_175_c": [
      210,
      230
    ]
  }
}
```

### SA038: dup-4152bd3eca59a27e23b7fc8d2919b01930cf72011c2d1865492fc48abeeca666

Status: APPROVED; survivor `sakata3d_pla_plahr-870yellow_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_hr-870playellow_1000_175_c`|`HR-870 PLA {color_name}`|`Yellow`|{"source_file": "sakata3d.json", "definition_index": 21, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`sakata3d_pla_plahr-870yellow_1000_175_c`|`PLA HR-870 {color_name}`|`Yellow`|{"source_file": "sakata3d.json", "definition_index": 13, "weights": 1, "diameters": 2, "colors": 10, "compiled_records": 20} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_hr-870playellow_1000_175_c": "FBE200",
    "sakata3d_pla_plahr-870yellow_1000_175_c": "FAD201"
  },
  "extruder_temp_range": {
    "sakata3d_pla_hr-870playellow_1000_175_c": [
      190,
      230
    ],
    "sakata3d_pla_plahr-870yellow_1000_175_c": [
      210,
      230
    ]
  }
}
```

### SA039: dup-5330048a943bf7eedd4d09a1edc60ae3a08b1415291f8ab2d466587fab047e6f

Status: APPROVED; survivor `sakata3d_pla_plawoodarce_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_plawoodarce_1000_175_c`|`PLA WOOD {color_name}`|`Arce`|{"source_file": "sakata3d.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|
|`sakata3d_pla_woodplaarce_1000_175_c`|`Wood PLA {color_name}`|`Arce`|{"source_file": "sakata3d.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_plawoodarce_1000_175_c": "755847",
    "sakata3d_pla_woodplaarce_1000_175_c": "EAD7B8"
  },
  "extruder_temp_range": {
    "sakata3d_pla_plawoodarce_1000_175_c": [
      200,
      255
    ],
    "sakata3d_pla_woodplaarce_1000_175_c": [
      190,
      230
    ]
  },
  "fill": {
    "sakata3d_pla_plawoodarce_1000_175_c": "wood",
    "sakata3d_pla_woodplaarce_1000_175_c": null
  },
  "pattern": {
    "sakata3d_pla_plawoodarce_1000_175_c": "marble",
    "sakata3d_pla_woodplaarce_1000_175_c": null
  }
}
```

### SA040: dup-1b37c6f139a6350a943c3d3e2f52a9cf387c05cd789a87fe4f0a78f454749e07

Status: APPROVED; survivor `sakata3d_pla_plawoodoak_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_plawoodoak_1000_175_c`|`PLA WOOD {color_name}`|`Oak`|{"source_file": "sakata3d.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|
|`sakata3d_pla_woodplaoak_1000_175_c`|`Wood PLA {color_name}`|`Oak`|{"source_file": "sakata3d.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_plawoodoak_1000_175_c": "755847",
    "sakata3d_pla_woodplaoak_1000_175_c": "C69581"
  },
  "extruder_temp_range": {
    "sakata3d_pla_plawoodoak_1000_175_c": [
      200,
      255
    ],
    "sakata3d_pla_woodplaoak_1000_175_c": [
      190,
      230
    ]
  },
  "fill": {
    "sakata3d_pla_plawoodoak_1000_175_c": "wood",
    "sakata3d_pla_woodplaoak_1000_175_c": null
  },
  "pattern": {
    "sakata3d_pla_plawoodoak_1000_175_c": "marble",
    "sakata3d_pla_woodplaoak_1000_175_c": null
  }
}
```

### SA041: dup-8199be3b17d219f969473a2c5358e0a6bb7dc719ee8da8da8e88b9c33e631936

Status: APPROVED; survivor `sakata3d_pla_plawoodwhite_1000_175_c`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sakata3d_pla_plawoodwhite_1000_175_c`|`PLA WOOD {color_name}`|`White`|{"source_file": "sakata3d.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|
|`sakata3d_pla_woodplawhite_1000_175_c`|`Wood PLA {color_name}`|`White`|{"source_file": "sakata3d.json", "definition_index": 24, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "sakata3d_pla_plawoodwhite_1000_175_c": "F6F6F6",
    "sakata3d_pla_woodplawhite_1000_175_c": "E6DDDB"
  },
  "extruder_temp_range": {
    "sakata3d_pla_plawoodwhite_1000_175_c": [
      200,
      255
    ],
    "sakata3d_pla_woodplawhite_1000_175_c": [
      190,
      230
    ]
  },
  "fill": {
    "sakata3d_pla_plawoodwhite_1000_175_c": "wood",
    "sakata3d_pla_woodplawhite_1000_175_c": null
  },
  "pattern": {
    "sakata3d_pla_plawoodwhite_1000_175_c": "marble",
    "sakata3d_pla_woodplawhite_1000_175_c": null
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "sakata3d_pla_plahr-870green_1000_175_c",
      "values": {
        "bed_temp_range": [
          40,
          60
        ]
      },
      "source": "https://sakata3d.com/en/content/36-pla-hr-870",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "sakata3d_pla_plahr-870yellow_1000_175_c",
      "values": {
        "bed_temp_range": [
          40,
          60
        ]
      },
      "source": "https://sakata3d.com/en/content/36-pla-hr-870",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "sakata3d_pla_plahr-870black_1000_175_c",
      "values": {
        "bed_temp_range": [
          40,
          60
        ]
      },
      "source": "https://sakata3d.com/en/content/36-pla-hr-870",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "sakata3d_pla_plahr-870silver_1000_175_c",
      "values": {
        "bed_temp_range": [
          40,
          60
        ]
      },
      "source": "https://sakata3d.com/en/content/36-pla-hr-870",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "sakata3d_pla_plahr-870orange_1000_175_c",
      "values": {
        "bed_temp_range": [
          40,
          60
        ]
      },
      "source": "https://sakata3d.com/en/content/36-pla-hr-870",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "sakata3d_pla_plahr-870red_1000_175_c",
      "values": {
        "bed_temp_range": [
          40,
          60
        ]
      },
      "source": "https://sakata3d.com/en/content/36-pla-hr-870",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "sakata3d_pla_plahr-870grey_1000_175_c",
      "values": {
        "bed_temp_range": [
          40,
          60
        ]
      },
      "source": "https://sakata3d.com/en/content/36-pla-hr-870",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "sakata3d_pla_plahr-870natural_1000_175_c",
      "values": {
        "bed_temp_range": [
          40,
          60
        ]
      },
      "source": "https://sakata3d.com/en/content/36-pla-hr-870",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "sakata3d_pla_plahr-870white_1000_175_c",
      "values": {
        "bed_temp_range": [
          40,
          60
        ]
      },
      "source": "https://sakata3d.com/en/content/36-pla-hr-870",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "sakata3d_pla_plahr-870blue_1000_175_c",
      "values": {
        "bed_temp_range": [
          40,
          60
        ]
      },
      "source": "https://sakata3d.com/en/content/36-pla-hr-870",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    }
  ],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `sakata3d_abs_abs-eblack_850_175_c` — ABS-E Black
- `sakata3d_abs_abs-eblue_850_175_c` — ABS-E Blue
- `sakata3d_abs_abs-ecaramel_850_175_c` — ABS-E Caramel
- `sakata3d_abs_abs-egreen_850_175_c` — ABS-E Green
- `sakata3d_abs_abs-egrey_850_175_c` — ABS-E Grey
- `sakata3d_abs_abs-elightblue_850_175_c` — ABS-E Light Blue
- `sakata3d_abs_abs-enatural_850_175_c` — ABS-E Natural
- `sakata3d_abs_abs-eorange_850_175_c` — ABS-E Orange
- `sakata3d_abs_abs-epurple_850_175_c` — ABS-E Purple
- `sakata3d_abs_abs-ered_850_175_c` — ABS-E Red
- `sakata3d_abs_abs-esilver_850_175_c` — ABS-E Silver
- `sakata3d_abs_abs-etile_850_175_c` — ABS-E Tile
- `sakata3d_abs_abs-ewhite_850_175_c` — ABS-E White
- `sakata3d_abs_abs-eyellow_850_175_c` — ABS-E Yellow
- `sakata3d_abs_abs-eblack_850_285_c` — ABS-E Black
- `sakata3d_abs_abs-eblue_850_285_c` — ABS-E Blue
- `sakata3d_abs_abs-ecaramel_850_285_c` — ABS-E Caramel
- `sakata3d_abs_abs-egreen_850_285_c` — ABS-E Green
- `sakata3d_abs_abs-egrey_850_285_c` — ABS-E Grey
- `sakata3d_abs_abs-elightblue_850_285_c` — ABS-E Light Blue
- `sakata3d_abs_abs-enatural_850_285_c` — ABS-E Natural
- `sakata3d_abs_abs-eorange_850_285_c` — ABS-E Orange
- `sakata3d_abs_abs-epurple_850_285_c` — ABS-E Purple
- `sakata3d_abs_abs-ered_850_285_c` — ABS-E Red
- `sakata3d_abs_abs-esilver_850_285_c` — ABS-E Silver
- `sakata3d_abs_abs-etile_850_285_c` — ABS-E Tile
- `sakata3d_abs_abs-ewhite_850_285_c` — ABS-E White
- `sakata3d_abs_abs-eyellow_850_285_c` — ABS-E Yellow
- `sakata3d_abs_abs-eorange_1000_175_c` — ABS-E Orange
- `sakata3d_abs_abs-eblack_1000_285_c` — ABS-E Black
- `sakata3d_abs_abs-eblue_1000_285_c` — ABS-E Blue
- `sakata3d_abs_abs-ecaramel_1000_285_c` — ABS-E Caramel
- `sakata3d_abs_abs-egreen_1000_285_c` — ABS-E Green
- `sakata3d_abs_abs-egrey_1000_285_c` — ABS-E Grey
- `sakata3d_abs_abs-elightblue_1000_285_c` — ABS-E Light Blue
- `sakata3d_abs_abs-enatural_1000_285_c` — ABS-E Natural
- `sakata3d_abs_abs-eorange_1000_285_c` — ABS-E Orange
- `sakata3d_abs_abs-epurple_1000_285_c` — ABS-E Purple
- `sakata3d_abs_abs-ered_1000_285_c` — ABS-E Red
- `sakata3d_abs_abs-esilver_1000_285_c` — ABS-E Silver
- `sakata3d_abs_abs-etile_1000_285_c` — ABS-E Tile
- `sakata3d_abs_abs-ewhite_1000_285_c` — ABS-E White
- `sakata3d_abs_abs-eyellow_1000_285_c` — ABS-E Yellow
- `sakata3d_abs_abs-eblack_2500_175_c` — ABS-E Black
- `sakata3d_abs_abs-eblue_2500_175_c` — ABS-E Blue
- `sakata3d_abs_abs-ecaramel_2500_175_c` — ABS-E Caramel
- `sakata3d_abs_abs-egreen_2500_175_c` — ABS-E Green
- `sakata3d_abs_abs-egrey_2500_175_c` — ABS-E Grey
- `sakata3d_abs_abs-elightblue_2500_175_c` — ABS-E Light Blue
- `sakata3d_abs_abs-enatural_2500_175_c` — ABS-E Natural
- `sakata3d_abs_abs-eorange_2500_175_c` — ABS-E Orange
- `sakata3d_abs_abs-epurple_2500_175_c` — ABS-E Purple
- `sakata3d_abs_abs-ered_2500_175_c` — ABS-E Red
- `sakata3d_abs_abs-esilver_2500_175_c` — ABS-E Silver
- `sakata3d_abs_abs-etile_2500_175_c` — ABS-E Tile
- `sakata3d_abs_abs-ewhite_2500_175_c` — ABS-E White
- `sakata3d_abs_abs-eyellow_2500_175_c` — ABS-E Yellow
- `sakata3d_abs_abs-eblack_2500_285_c` — ABS-E Black
- `sakata3d_abs_abs-eblue_2500_285_c` — ABS-E Blue
- `sakata3d_abs_abs-ecaramel_2500_285_c` — ABS-E Caramel
- `sakata3d_abs_abs-egreen_2500_285_c` — ABS-E Green
- `sakata3d_abs_abs-egrey_2500_285_c` — ABS-E Grey
- `sakata3d_abs_abs-elightblue_2500_285_c` — ABS-E Light Blue
- `sakata3d_abs_abs-enatural_2500_285_c` — ABS-E Natural
- `sakata3d_abs_abs-eorange_2500_285_c` — ABS-E Orange
- `sakata3d_abs_abs-epurple_2500_285_c` — ABS-E Purple
- `sakata3d_abs_abs-ered_2500_285_c` — ABS-E Red
- `sakata3d_abs_abs-esilver_2500_285_c` — ABS-E Silver
- `sakata3d_abs_abs-etile_2500_285_c` — ABS-E Tile
- `sakata3d_abs_abs-ewhite_2500_285_c` — ABS-E White
- `sakata3d_abs_abs-eyellow_2500_285_c` — ABS-E Yellow
- `sakata3d_abs_abs-eblack_5000_175_c` — ABS-E Black
- `sakata3d_abs_abs-eblue_5000_175_c` — ABS-E Blue
- `sakata3d_abs_abs-ecaramel_5000_175_c` — ABS-E Caramel
- `sakata3d_abs_abs-egreen_5000_175_c` — ABS-E Green
- `sakata3d_abs_abs-egrey_5000_175_c` — ABS-E Grey
- `sakata3d_abs_abs-elightblue_5000_175_c` — ABS-E Light Blue
- `sakata3d_abs_abs-enatural_5000_175_c` — ABS-E Natural
- `sakata3d_abs_abs-eorange_5000_175_c` — ABS-E Orange
- `sakata3d_abs_abs-epurple_5000_175_c` — ABS-E Purple
- `sakata3d_abs_abs-ered_5000_175_c` — ABS-E Red
- `sakata3d_abs_abs-esilver_5000_175_c` — ABS-E Silver
- `sakata3d_abs_abs-etile_5000_175_c` — ABS-E Tile
- `sakata3d_abs_abs-ewhite_5000_175_c` — ABS-E White
- `sakata3d_abs_abs-eyellow_5000_175_c` — ABS-E Yellow
- `sakata3d_abs_abs-eblack_5000_285_c` — ABS-E Black
- `sakata3d_abs_abs-eblue_5000_285_c` — ABS-E Blue
- `sakata3d_abs_abs-ecaramel_5000_285_c` — ABS-E Caramel
- `sakata3d_abs_abs-egreen_5000_285_c` — ABS-E Green
- `sakata3d_abs_abs-egrey_5000_285_c` — ABS-E Grey
- `sakata3d_abs_abs-elightblue_5000_285_c` — ABS-E Light Blue
- `sakata3d_abs_abs-enatural_5000_285_c` — ABS-E Natural
- `sakata3d_abs_abs-eorange_5000_285_c` — ABS-E Orange
- `sakata3d_abs_abs-epurple_5000_285_c` — ABS-E Purple
- `sakata3d_abs_abs-ered_5000_285_c` — ABS-E Red
- `sakata3d_abs_abs-esilver_5000_285_c` — ABS-E Silver
- `sakata3d_abs_abs-etile_5000_285_c` — ABS-E Tile
- `sakata3d_abs_abs-ewhite_5000_285_c` — ABS-E White
- `sakata3d_abs_abs-eyellow_5000_285_c` — ABS-E Yellow
- `sakata3d_asa_asablack_850_175_c` — ASA Black
- `sakata3d_asa_asanatural_850_175_c` — ASA Natural
- `sakata3d_asa_asablack_850_285_c` — ASA Black
- `sakata3d_asa_asanatural_850_285_c` — ASA Natural
- `sakata3d_asa_asablack_1000_175_c` — ASA Black
- `sakata3d_asa_asanatural_1000_175_c` — ASA Natural
- `sakata3d_asa_asablack_1000_285_c` — ASA Black
- `sakata3d_asa_asanatural_1000_285_c` — ASA Natural
- `sakata3d_tpu_flex-920black_1000_175_c` — FleX-920 Black
- `sakata3d_tpu_flex-920blue_1000_175_c` — FleX-920 Blue
- `sakata3d_tpu_flex-920camel_1000_175_c` — FleX-920 Camel
- `sakata3d_tpu_flex-920chocolate_1000_175_c` — FleX-920 Chocolate
- `sakata3d_tpu_flex-920fluorlime_1000_175_c` — FleX-920 Fluor Lime
- `sakata3d_tpu_flex-920fuchsia_1000_175_c` — FleX-920 Fuchsia
- `sakata3d_tpu_flex-920green_1000_175_c` — FleX-920 Green
- `sakata3d_tpu_flex-920grey_1000_175_c` — FleX-920 Grey
- `sakata3d_tpu_flex-920orange_1000_175_c` — FleX-920 Orange
- `sakata3d_tpu_flex-920orangefresh_1000_175_c` — FleX-920 Orange Fresh
- `sakata3d_tpu_flex-920red_1000_175_c` — FleX-920 Red
- `sakata3d_tpu_flex-920skintone1_1000_175_c` — FleX-920 Skin Tone 1
- `sakata3d_tpu_flex-920surfgreen_1000_175_c` — FleX-920 Surf Green
- `sakata3d_tpu_flex-920white_1000_175_c` — FleX-920 White
- `sakata3d_tpu_flex-920yellow_1000_175_c` — FleX-920 Yellow
- `sakata3d_hips_hipsblack_1000_175_c` — HIPS Black
- `sakata3d_hips_hipsnaturalwhite_1000_175_c` — HIPS Natural white
- `sakata3d_hips_hipsblack_1000_285_c` — HIPS Black
- `sakata3d_hips_hipsnaturalwhite_1000_285_c` — HIPS Natural white
- `sakata3d_petg_pet-gambar_1000_175_c` — PET-G Ambar
- `sakata3d_petg_pet-ganthracitegrey_1000_175_c` — PET-G Anthracite Grey
- `sakata3d_petg_pet-gblack_1000_175_c` — PET-G Black
- `sakata3d_petg_pet-gblue_1000_175_c` — PET-G Blue
- `sakata3d_petg_pet-gemerald_1000_175_c` — PET-G Emerald
- `sakata3d_petg_pet-gfuchsia_1000_175_c` — PET-G Fuchsia
- `sakata3d_petg_pet-ggreen_1000_175_c` — PET-G Green
- `sakata3d_petg_pet-ggrey_1000_175_c` — PET-G Grey
- `sakata3d_petg_pet-gnatural_1000_175_c` — PET-G Natural
- `sakata3d_petg_pet-gorange_1000_175_c` — PET-G Orange
- `sakata3d_petg_pet-gred_1000_175_c` — PET-G Red
- `sakata3d_petg_pet-gruby_1000_175_c` — PET-G Ruby
- `sakata3d_petg_pet-gwhite_1000_175_c` — PET-G White
- `sakata3d_petg_pet-gyellow_1000_175_c` — PET-G Yellow
- `sakata3d_petg_pet-gzaphire_1000_175_c` — PET-G Zaphire
- `sakata3d_petg_pet-gambar(translucid)_1000_175_c` — PET-G Ambar (translucid)
- `sakata3d_petg_pet-gemerald(translucid)_1000_175_c` — PET-G Emerald (translucid)
- `sakata3d_petg_pet-gruby(translucid)_1000_175_c` — PET-G Ruby (translucid)
- `sakata3d_petg_pet-gzaphire(translucid)_1000_175_c` — PET-G Zaphire (translucid)
- `sakata3d_petg_pet-gambar_1000_285_c` — PET-G Ambar
- `sakata3d_petg_pet-ganthracitegrey_1000_285_c` — PET-G Anthracite Grey
- `sakata3d_petg_pet-gblack_1000_285_c` — PET-G Black
- `sakata3d_petg_pet-gblue_1000_285_c` — PET-G Blue
- `sakata3d_petg_pet-gemerald_1000_285_c` — PET-G Emerald
- `sakata3d_petg_pet-gfuchsia_1000_285_c` — PET-G Fuchsia
- `sakata3d_petg_pet-ggreen_1000_285_c` — PET-G Green
- `sakata3d_petg_pet-ggrey_1000_285_c` — PET-G Grey
- `sakata3d_petg_pet-gnatural_1000_285_c` — PET-G Natural
- `sakata3d_petg_pet-gorange_1000_285_c` — PET-G Orange
- `sakata3d_petg_pet-gred_1000_285_c` — PET-G Red
- `sakata3d_petg_pet-gruby_1000_285_c` — PET-G Ruby
- `sakata3d_petg_pet-gwhite_1000_285_c` — PET-G White
- `sakata3d_petg_pet-gyellow_1000_285_c` — PET-G Yellow
- `sakata3d_petg_pet-gzaphire_1000_285_c` — PET-G Zaphire
- `sakata3d_petg_pet-gambar(translucid)_1000_285_c` — PET-G Ambar (translucid)
- `sakata3d_petg_pet-gemerald(translucid)_1000_285_c` — PET-G Emerald (translucid)
- `sakata3d_petg_pet-gruby(translucid)_1000_285_c` — PET-G Ruby (translucid)
- `sakata3d_petg_pet-gzaphire(translucid)_1000_285_c` — PET-G Zaphire (translucid)
- `sakata3d_petg_pet-gambar_2500_175_c` — PET-G Ambar
- `sakata3d_petg_pet-ganthracitegrey_2500_175_c` — PET-G Anthracite Grey
- `sakata3d_petg_pet-gblack_2500_175_c` — PET-G Black
- `sakata3d_petg_pet-gblue_2500_175_c` — PET-G Blue
- `sakata3d_petg_pet-gemerald_2500_175_c` — PET-G Emerald
- `sakata3d_petg_pet-gfuchsia_2500_175_c` — PET-G Fuchsia
- `sakata3d_petg_pet-ggreen_2500_175_c` — PET-G Green
- `sakata3d_petg_pet-ggrey_2500_175_c` — PET-G Grey
- `sakata3d_petg_pet-gnatural_2500_175_c` — PET-G Natural
- `sakata3d_petg_pet-gorange_2500_175_c` — PET-G Orange
- `sakata3d_petg_pet-gred_2500_175_c` — PET-G Red
- `sakata3d_petg_pet-gruby_2500_175_c` — PET-G Ruby
- `sakata3d_petg_pet-gwhite_2500_175_c` — PET-G White
- `sakata3d_petg_pet-gyellow_2500_175_c` — PET-G Yellow
- `sakata3d_petg_pet-gzaphire_2500_175_c` — PET-G Zaphire
- `sakata3d_petg_pet-gambar(translucid)_2500_175_c` — PET-G Ambar (translucid)
- `sakata3d_petg_pet-gemerald(translucid)_2500_175_c` — PET-G Emerald (translucid)
- `sakata3d_petg_pet-gruby(translucid)_2500_175_c` — PET-G Ruby (translucid)
- `sakata3d_petg_pet-gzaphire(translucid)_2500_175_c` — PET-G Zaphire (translucid)
- `sakata3d_petg_pet-gambar_2500_285_c` — PET-G Ambar
- `sakata3d_petg_pet-ganthracitegrey_2500_285_c` — PET-G Anthracite Grey
- `sakata3d_petg_pet-gblack_2500_285_c` — PET-G Black
- `sakata3d_petg_pet-gblue_2500_285_c` — PET-G Blue
- `sakata3d_petg_pet-gemerald_2500_285_c` — PET-G Emerald
- `sakata3d_petg_pet-gfuchsia_2500_285_c` — PET-G Fuchsia
- `sakata3d_petg_pet-ggreen_2500_285_c` — PET-G Green
- `sakata3d_petg_pet-ggrey_2500_285_c` — PET-G Grey
- `sakata3d_petg_pet-gnatural_2500_285_c` — PET-G Natural
- `sakata3d_petg_pet-gorange_2500_285_c` — PET-G Orange
- `sakata3d_petg_pet-gred_2500_285_c` — PET-G Red
- `sakata3d_petg_pet-gruby_2500_285_c` — PET-G Ruby
- `sakata3d_petg_pet-gwhite_2500_285_c` — PET-G White
- `sakata3d_petg_pet-gyellow_2500_285_c` — PET-G Yellow
- `sakata3d_petg_pet-gzaphire_2500_285_c` — PET-G Zaphire
- `sakata3d_petg_pet-gambar(translucid)_2500_285_c` — PET-G Ambar (translucid)
- `sakata3d_petg_pet-gemerald(translucid)_2500_285_c` — PET-G Emerald (translucid)
- `sakata3d_petg_pet-gruby(translucid)_2500_285_c` — PET-G Ruby (translucid)
- `sakata3d_petg_pet-gzaphire(translucid)_2500_285_c` — PET-G Zaphire (translucid)
- `sakata3d_petg_pet-gambar_5000_175_c` — PET-G Ambar
- `sakata3d_petg_pet-ganthracitegrey_5000_175_c` — PET-G Anthracite Grey
- `sakata3d_petg_pet-gblack_5000_175_c` — PET-G Black
- `sakata3d_petg_pet-gblue_5000_175_c` — PET-G Blue
- `sakata3d_petg_pet-gemerald_5000_175_c` — PET-G Emerald
- `sakata3d_petg_pet-gfuchsia_5000_175_c` — PET-G Fuchsia
- `sakata3d_petg_pet-ggreen_5000_175_c` — PET-G Green
- `sakata3d_petg_pet-ggrey_5000_175_c` — PET-G Grey
- `sakata3d_petg_pet-gnatural_5000_175_c` — PET-G Natural
- `sakata3d_petg_pet-gorange_5000_175_c` — PET-G Orange
- `sakata3d_petg_pet-gred_5000_175_c` — PET-G Red
- `sakata3d_petg_pet-gruby_5000_175_c` — PET-G Ruby
- `sakata3d_petg_pet-gwhite_5000_175_c` — PET-G White
- `sakata3d_petg_pet-gyellow_5000_175_c` — PET-G Yellow
- `sakata3d_petg_pet-gzaphire_5000_175_c` — PET-G Zaphire
- `sakata3d_petg_pet-gambar(translucid)_5000_175_c` — PET-G Ambar (translucid)
- `sakata3d_petg_pet-gemerald(translucid)_5000_175_c` — PET-G Emerald (translucid)
- `sakata3d_petg_pet-gruby(translucid)_5000_175_c` — PET-G Ruby (translucid)
- `sakata3d_petg_pet-gzaphire(translucid)_5000_175_c` — PET-G Zaphire (translucid)
- `sakata3d_petg_pet-gambar_5000_285_c` — PET-G Ambar
- `sakata3d_petg_pet-ganthracitegrey_5000_285_c` — PET-G Anthracite Grey
- `sakata3d_petg_pet-gblack_5000_285_c` — PET-G Black
- `sakata3d_petg_pet-gblue_5000_285_c` — PET-G Blue
- `sakata3d_petg_pet-gemerald_5000_285_c` — PET-G Emerald
- `sakata3d_petg_pet-gfuchsia_5000_285_c` — PET-G Fuchsia
- `sakata3d_petg_pet-ggreen_5000_285_c` — PET-G Green
- `sakata3d_petg_pet-ggrey_5000_285_c` — PET-G Grey
- `sakata3d_petg_pet-gnatural_5000_285_c` — PET-G Natural
- `sakata3d_petg_pet-gorange_5000_285_c` — PET-G Orange
- `sakata3d_petg_pet-gred_5000_285_c` — PET-G Red
- `sakata3d_petg_pet-gruby_5000_285_c` — PET-G Ruby
- `sakata3d_petg_pet-gwhite_5000_285_c` — PET-G White
- `sakata3d_petg_pet-gyellow_5000_285_c` — PET-G Yellow
- `sakata3d_petg_pet-gzaphire_5000_285_c` — PET-G Zaphire
- `sakata3d_petg_pet-gambar(translucid)_5000_285_c` — PET-G Ambar (translucid)
- `sakata3d_petg_pet-gemerald(translucid)_5000_285_c` — PET-G Emerald (translucid)
- `sakata3d_petg_pet-gruby(translucid)_5000_285_c` — PET-G Ruby (translucid)
- `sakata3d_petg_pet-gzaphire(translucid)_5000_285_c` — PET-G Zaphire (translucid)
- `sakata3d_petg-cf15_pet-gcf15black_1000_175_c` — PET-G CF15 Black
- `sakata3d_petg_pet-gv0black_1000_175_c` — PET-G V0 Black
- `sakata3d_petg_pet-gv0natural_1000_175_c` — PET-G V0 Natural
- `sakata3d_pla_pla700black_2500_175_c` — PLA 700 Black
- `sakata3d_pla_pla700grey_2500_175_c` — PLA 700 Grey
- `sakata3d_pla_pla700white_2500_175_c` — PLA 700 White
- `sakata3d_pla_pla700black_2500_285_c` — PLA 700 Black
- `sakata3d_pla_pla700grey_2500_285_c` — PLA 700 Grey
- `sakata3d_pla_pla700white_2500_285_c` — PLA 700 White
- `sakata3d_pla_pla700black_5000_175_c` — PLA 700 Black
- `sakata3d_pla_pla700grey_5000_175_c` — PLA 700 Grey
- `sakata3d_pla_pla700white_5000_175_c` — PLA 700 White
- `sakata3d_pla_pla700black_5000_285_c` — PLA 700 Black
- `sakata3d_pla_pla700grey_5000_285_c` — PLA 700 Grey
- `sakata3d_pla_pla700white_5000_285_c` — PLA 700 White
- `sakata3d_pla_pla850glassblue_1000_175_c` — PLA 850 Glass Blue
- `sakata3d_pla_pla850glassgreen_1000_175_c` — PLA 850 Glass Green
- `sakata3d_pla_pla850glassorange_1000_175_c` — PLA 850 Glass Orange
- `sakata3d_pla_pla850glassred_1000_175_c` — PLA 850 Glass Red
- `sakata3d_pla_pla850glassviolet_1000_175_c` — PLA 850 Glass Violet
- `sakata3d_pla_pla850glassyellow_1000_175_c` — PLA 850 Glass Yellow
- `sakata3d_pla_pla850glassblue_1000_285_c` — PLA 850 Glass Blue
- `sakata3d_pla_pla850glassgreen_1000_285_c` — PLA 850 Glass Green
- `sakata3d_pla_pla850glassorange_1000_285_c` — PLA 850 Glass Orange
- `sakata3d_pla_pla850glassred_1000_285_c` — PLA 850 Glass Red
- `sakata3d_pla_pla850glassviolet_1000_285_c` — PLA 850 Glass Violet
- `sakata3d_pla_pla850glassyellow_1000_285_c` — PLA 850 Glass Yellow
- `sakata3d_pla_pla850glassblue_2500_175_c` — PLA 850 Glass Blue
- `sakata3d_pla_pla850glassgreen_2500_175_c` — PLA 850 Glass Green
- `sakata3d_pla_pla850glassorange_2500_175_c` — PLA 850 Glass Orange
- `sakata3d_pla_pla850glassred_2500_175_c` — PLA 850 Glass Red
- `sakata3d_pla_pla850glassviolet_2500_175_c` — PLA 850 Glass Violet
- `sakata3d_pla_pla850glassyellow_2500_175_c` — PLA 850 Glass Yellow
- `sakata3d_pla_pla850glassblue_2500_285_c` — PLA 850 Glass Blue
- `sakata3d_pla_pla850glassgreen_2500_285_c` — PLA 850 Glass Green
- `sakata3d_pla_pla850glassorange_2500_285_c` — PLA 850 Glass Orange
- `sakata3d_pla_pla850glassred_2500_285_c` — PLA 850 Glass Red
- `sakata3d_pla_pla850glassviolet_2500_285_c` — PLA 850 Glass Violet
- `sakata3d_pla_pla850glassyellow_2500_285_c` — PLA 850 Glass Yellow
- `sakata3d_pla_pla850glassblue_5000_175_c` — PLA 850 Glass Blue
- `sakata3d_pla_pla850glassgreen_5000_175_c` — PLA 850 Glass Green
- `sakata3d_pla_pla850glassorange_5000_175_c` — PLA 850 Glass Orange
- `sakata3d_pla_pla850glassred_5000_175_c` — PLA 850 Glass Red
- `sakata3d_pla_pla850glassviolet_5000_175_c` — PLA 850 Glass Violet
- `sakata3d_pla_pla850glassyellow_5000_175_c` — PLA 850 Glass Yellow
- `sakata3d_pla_pla850glassblue_5000_285_c` — PLA 850 Glass Blue
- `sakata3d_pla_pla850glassgreen_5000_285_c` — PLA 850 Glass Green
- `sakata3d_pla_pla850glassorange_5000_285_c` — PLA 850 Glass Orange
- `sakata3d_pla_pla850glassred_5000_285_c` — PLA 850 Glass Red
- `sakata3d_pla_pla850glassviolet_5000_285_c` — PLA 850 Glass Violet
- `sakata3d_pla_pla850glassyellow_5000_285_c` — PLA 850 Glass Yellow
- `sakata3d_pla_pla850magiccoal_1000_175_c` — PLA 850 Magic Coal
- `sakata3d_pla_pla850magicnavyblue_1000_175_c` — PLA 850 Magic Navy Blue
- `sakata3d_pla_pla850magicplusblue_1000_175_c` — PLA 850 Magic Plus Blue
- `sakata3d_pla_pla850magicpluscoal_1000_175_c` — PLA 850 Magic Plus Coal
- `sakata3d_pla_pla850magicplusred_1000_175_c` — PLA 850 Magic Plus Red
- `sakata3d_pla_pla850magicplussilver_1000_175_c` — PLA 850 Magic Plus Silver
- `sakata3d_pla_pla850magicpurple_1000_175_c` — PLA 850 Magic Purple
- `sakata3d_pla_pla850magicsilver_1000_175_c` — PLA 850 Magic Silver
- `sakata3d_pla_pla850magicstargold_1000_175_c` — PLA 850 Magic Star Gold
- `sakata3d_pla_pla850magiccoal_1000_285_c` — PLA 850 Magic Coal
- `sakata3d_pla_pla850magicnavyblue_1000_285_c` — PLA 850 Magic Navy Blue
- `sakata3d_pla_pla850magicplusblue_1000_285_c` — PLA 850 Magic Plus Blue
- `sakata3d_pla_pla850magicpluscoal_1000_285_c` — PLA 850 Magic Plus Coal
- `sakata3d_pla_pla850magicplusred_1000_285_c` — PLA 850 Magic Plus Red
- `sakata3d_pla_pla850magicplussilver_1000_285_c` — PLA 850 Magic Plus Silver
- `sakata3d_pla_pla850magicpurple_1000_285_c` — PLA 850 Magic Purple
- `sakata3d_pla_pla850magicsilver_1000_285_c` — PLA 850 Magic Silver
- `sakata3d_pla_pla850magicstargold_1000_285_c` — PLA 850 Magic Star Gold
- `sakata3d_pla_pla850magiccoal_2500_175_c` — PLA 850 Magic Coal
- `sakata3d_pla_pla850magicnavyblue_2500_175_c` — PLA 850 Magic Navy Blue
- `sakata3d_pla_pla850magicplusblue_2500_175_c` — PLA 850 Magic Plus Blue
- `sakata3d_pla_pla850magicpluscoal_2500_175_c` — PLA 850 Magic Plus Coal
- `sakata3d_pla_pla850magicplusred_2500_175_c` — PLA 850 Magic Plus Red
- `sakata3d_pla_pla850magicplussilver_2500_175_c` — PLA 850 Magic Plus Silver
- `sakata3d_pla_pla850magicpurple_2500_175_c` — PLA 850 Magic Purple
- `sakata3d_pla_pla850magicsilver_2500_175_c` — PLA 850 Magic Silver
- `sakata3d_pla_pla850magicstargold_2500_175_c` — PLA 850 Magic Star Gold
- `sakata3d_pla_pla850magiccoal_2500_285_c` — PLA 850 Magic Coal
- `sakata3d_pla_pla850magicnavyblue_2500_285_c` — PLA 850 Magic Navy Blue
- `sakata3d_pla_pla850magicplusblue_2500_285_c` — PLA 850 Magic Plus Blue
- `sakata3d_pla_pla850magicpluscoal_2500_285_c` — PLA 850 Magic Plus Coal
- `sakata3d_pla_pla850magicplusred_2500_285_c` — PLA 850 Magic Plus Red
- `sakata3d_pla_pla850magicplussilver_2500_285_c` — PLA 850 Magic Plus Silver
- `sakata3d_pla_pla850magicpurple_2500_285_c` — PLA 850 Magic Purple
- `sakata3d_pla_pla850magicsilver_2500_285_c` — PLA 850 Magic Silver
- `sakata3d_pla_pla850magicstargold_2500_285_c` — PLA 850 Magic Star Gold
- `sakata3d_pla_pla850magiccoal_5000_175_c` — PLA 850 Magic Coal
- `sakata3d_pla_pla850magicnavyblue_5000_175_c` — PLA 850 Magic Navy Blue
- `sakata3d_pla_pla850magicplusblue_5000_175_c` — PLA 850 Magic Plus Blue
- `sakata3d_pla_pla850magicpluscoal_5000_175_c` — PLA 850 Magic Plus Coal
- `sakata3d_pla_pla850magicplusred_5000_175_c` — PLA 850 Magic Plus Red
- `sakata3d_pla_pla850magicplussilver_5000_175_c` — PLA 850 Magic Plus Silver
- `sakata3d_pla_pla850magicpurple_5000_175_c` — PLA 850 Magic Purple
- `sakata3d_pla_pla850magicsilver_5000_175_c` — PLA 850 Magic Silver
- `sakata3d_pla_pla850magicstargold_5000_175_c` — PLA 850 Magic Star Gold
- `sakata3d_pla_pla850magiccoal_5000_285_c` — PLA 850 Magic Coal
- `sakata3d_pla_pla850magicnavyblue_5000_285_c` — PLA 850 Magic Navy Blue
- `sakata3d_pla_pla850magicplusblue_5000_285_c` — PLA 850 Magic Plus Blue
- `sakata3d_pla_pla850magicpluscoal_5000_285_c` — PLA 850 Magic Plus Coal
- `sakata3d_pla_pla850magicplusred_5000_285_c` — PLA 850 Magic Plus Red
- `sakata3d_pla_pla850magicplussilver_5000_285_c` — PLA 850 Magic Plus Silver
- `sakata3d_pla_pla850magicpurple_5000_285_c` — PLA 850 Magic Purple
- `sakata3d_pla_pla850magicsilver_5000_285_c` — PLA 850 Magic Silver
- `sakata3d_pla_pla850magicstargold_5000_285_c` — PLA 850 Magic Star Gold
- `sakata3d_pla_pla850silkarctic_1000_175_c` — PLA 850 Silk Arctic
- `sakata3d_pla_pla850silkaubergine_1000_175_c` — PLA 850 Silk Aubergine
- `sakata3d_pla_pla850silkclover_1000_175_c` — PLA 850 Silk Clover
- `sakata3d_pla_pla850silkfirgreen_1000_175_c` — PLA 850 Silk Fir Green
- `sakata3d_pla_pla850silkgold_1000_175_c` — PLA 850 Silk Gold
- `sakata3d_pla_pla850silkmidnight_1000_175_c` — PLA 850 Silk Midnight
- `sakata3d_pla_pla850silkocean_1000_175_c` — PLA 850 Silk Ocean
- `sakata3d_pla_pla850silksnow_1000_175_c` — PLA 850 Silk Snow
- `sakata3d_pla_pla850silksunset_1000_175_c` — PLA 850 Silk Sunset
- `sakata3d_pla_pla850silkwine_1000_175_c` — PLA 850 Silk Wine
- `sakata3d_pla_pla850silkarctic_1000_285_c` — PLA 850 Silk Arctic
- `sakata3d_pla_pla850silkaubergine_1000_285_c` — PLA 850 Silk Aubergine
- `sakata3d_pla_pla850silkclover_1000_285_c` — PLA 850 Silk Clover
- `sakata3d_pla_pla850silkfirgreen_1000_285_c` — PLA 850 Silk Fir Green
- `sakata3d_pla_pla850silkgold_1000_285_c` — PLA 850 Silk Gold
- `sakata3d_pla_pla850silkmidnight_1000_285_c` — PLA 850 Silk Midnight
- `sakata3d_pla_pla850silkocean_1000_285_c` — PLA 850 Silk Ocean
- `sakata3d_pla_pla850silksnow_1000_285_c` — PLA 850 Silk Snow
- `sakata3d_pla_pla850silksunset_1000_285_c` — PLA 850 Silk Sunset
- `sakata3d_pla_pla850silkwine_1000_285_c` — PLA 850 Silk Wine
- `sakata3d_pla_pla850silkarctic_2500_175_c` — PLA 850 Silk Arctic
- `sakata3d_pla_pla850silkaubergine_2500_175_c` — PLA 850 Silk Aubergine
- `sakata3d_pla_pla850silkclover_2500_175_c` — PLA 850 Silk Clover
- `sakata3d_pla_pla850silkfirgreen_2500_175_c` — PLA 850 Silk Fir Green
- `sakata3d_pla_pla850silkgold_2500_175_c` — PLA 850 Silk Gold
- `sakata3d_pla_pla850silkmidnight_2500_175_c` — PLA 850 Silk Midnight
- `sakata3d_pla_pla850silkocean_2500_175_c` — PLA 850 Silk Ocean
- `sakata3d_pla_pla850silksnow_2500_175_c` — PLA 850 Silk Snow
- `sakata3d_pla_pla850silksunset_2500_175_c` — PLA 850 Silk Sunset
- `sakata3d_pla_pla850silkwine_2500_175_c` — PLA 850 Silk Wine
- `sakata3d_pla_pla850silkarctic_2500_285_c` — PLA 850 Silk Arctic
- `sakata3d_pla_pla850silkaubergine_2500_285_c` — PLA 850 Silk Aubergine
- `sakata3d_pla_pla850silkclover_2500_285_c` — PLA 850 Silk Clover
- `sakata3d_pla_pla850silkfirgreen_2500_285_c` — PLA 850 Silk Fir Green
- `sakata3d_pla_pla850silkgold_2500_285_c` — PLA 850 Silk Gold
- `sakata3d_pla_pla850silkmidnight_2500_285_c` — PLA 850 Silk Midnight
- `sakata3d_pla_pla850silkocean_2500_285_c` — PLA 850 Silk Ocean
- `sakata3d_pla_pla850silksnow_2500_285_c` — PLA 850 Silk Snow
- `sakata3d_pla_pla850silksunset_2500_285_c` — PLA 850 Silk Sunset
- `sakata3d_pla_pla850silkwine_2500_285_c` — PLA 850 Silk Wine
- `sakata3d_pla_pla850silkarctic_5000_175_c` — PLA 850 Silk Arctic
- `sakata3d_pla_pla850silkaubergine_5000_175_c` — PLA 850 Silk Aubergine
- `sakata3d_pla_pla850silkclover_5000_175_c` — PLA 850 Silk Clover
- `sakata3d_pla_pla850silkfirgreen_5000_175_c` — PLA 850 Silk Fir Green
- `sakata3d_pla_pla850silkgold_5000_175_c` — PLA 850 Silk Gold
- `sakata3d_pla_pla850silkmidnight_5000_175_c` — PLA 850 Silk Midnight
- `sakata3d_pla_pla850silkocean_5000_175_c` — PLA 850 Silk Ocean
- `sakata3d_pla_pla850silksnow_5000_175_c` — PLA 850 Silk Snow
- `sakata3d_pla_pla850silksunset_5000_175_c` — PLA 850 Silk Sunset
- `sakata3d_pla_pla850silkwine_5000_175_c` — PLA 850 Silk Wine
- `sakata3d_pla_pla850silkarctic_5000_285_c` — PLA 850 Silk Arctic
- `sakata3d_pla_pla850silkaubergine_5000_285_c` — PLA 850 Silk Aubergine
- `sakata3d_pla_pla850silkclover_5000_285_c` — PLA 850 Silk Clover
- `sakata3d_pla_pla850silkfirgreen_5000_285_c` — PLA 850 Silk Fir Green
- `sakata3d_pla_pla850silkgold_5000_285_c` — PLA 850 Silk Gold
- `sakata3d_pla_pla850silkmidnight_5000_285_c` — PLA 850 Silk Midnight
- `sakata3d_pla_pla850silkocean_5000_285_c` — PLA 850 Silk Ocean
- `sakata3d_pla_pla850silksnow_5000_285_c` — PLA 850 Silk Snow
- `sakata3d_pla_pla850silksunset_5000_285_c` — PLA 850 Silk Sunset
- `sakata3d_pla_pla850silkwine_5000_285_c` — PLA 850 Silk Wine
- `sakata3d_pla_pla850andaluciagreen_1000_175_c` — PLA 850 Andalucia Green
- `sakata3d_pla_pla850anthracitegray_1000_175_c` — PLA 850 Anthracite Gray
- `sakata3d_pla_pla850black_1000_175_c` — PLA 850 Black
- `sakata3d_pla_pla850blue_1000_175_c` — PLA 850 Blue
- `sakata3d_pla_pla850carminered_1000_175_c` — PLA 850 Carmine Red
- `sakata3d_pla_pla850chocolate_1000_175_c` — PLA 850 Chocolate
- `sakata3d_pla_pla850clay_1000_175_c` — PLA 850 Clay
- `sakata3d_pla_pla850fluorlightgreen_1000_175_c` — PLA 850 Fluor Light Green
- `sakata3d_pla_pla850fluorlime_1000_175_c` — PLA 850 Fluor Lime
- `sakata3d_pla_pla850fluororange_1000_175_c` — PLA 850 Fluor Orange
- `sakata3d_pla_pla850fluororangefresh_1000_175_c` — PLA 850 Fluor Orange Fresh
- `sakata3d_pla_pla850fluoryellow_1000_175_c` — PLA 850 Fluor Yellow
- `sakata3d_pla_pla850fucsia_1000_175_c` — PLA 850 Fucsia
- `sakata3d_pla_pla850gold_1000_175_c` — PLA 850 Gold
- `sakata3d_pla_pla850granite_1000_175_c` — PLA 850 Granite
- `sakata3d_pla_pla850green_1000_175_c` — PLA 850 Green
- `sakata3d_pla_pla850grey_1000_175_c` — PLA 850 Grey
- `sakata3d_pla_pla850ivory_1000_175_c` — PLA 850 Ivory
- `sakata3d_pla_pla850militartone1gc_1000_175_c` — PLA 850 Militar Tone 1 Gc
- `sakata3d_pla_pla850militartone2_1000_175_c` — PLA 850 Militar Tone 2
- `sakata3d_pla_pla850natural_1000_175_c` — PLA 850 Natural
- `sakata3d_pla_pla850orange_1000_175_c` — PLA 850 Orange
- `sakata3d_pla_pla850pastelbabypink_1000_175_c` — PLA 850 Pastel Baby Pink
- `sakata3d_pla_pla850pastelgreen_1000_175_c` — PLA 850 Pastel Green
- `sakata3d_pla_pla850pastellilac_1000_175_c` — PLA 850 Pastel Lilac
- `sakata3d_pla_pla850pastelmangoyellow_1000_175_c` — PLA 850 Pastel Mango Yellow
- `sakata3d_pla_pla850pink_1000_175_c` — PLA 850 Pink
- `sakata3d_pla_pla850purple_1000_175_c` — PLA 850 Purple
- `sakata3d_pla_pla850red_1000_175_c` — PLA 850 Red
- `sakata3d_pla_pla850silver_1000_175_c` — PLA 850 Silver
- `sakata3d_pla_pla850skintone1_1000_175_c` — PLA 850 Skin Tone 1
- `sakata3d_pla_pla850skintone2_1000_175_c` — PLA 850 Skin Tone 2
- `sakata3d_pla_pla850skyblue_1000_175_c` — PLA 850 Sky Blue
- `sakata3d_pla_pla850solidary_1000_175_c` — PLA 850 Solidary
- `sakata3d_pla_pla850surfgreen_1000_175_c` — PLA 850 Surf Green
- `sakata3d_pla_pla850white_1000_175_c` — PLA 850 White
- `sakata3d_pla_pla850yellow_1000_175_c` — PLA 850 Yellow
- `sakata3d_pla_pla850fuchsia_1000_175_c` — PLA 850 Fuchsia
- `sakata3d_pla_pla850andaluciagreen_1000_285_c` — PLA 850 Andalucia Green
- `sakata3d_pla_pla850anthracitegray_1000_285_c` — PLA 850 Anthracite Gray
- `sakata3d_pla_pla850black_1000_285_c` — PLA 850 Black
- `sakata3d_pla_pla850blue_1000_285_c` — PLA 850 Blue
- `sakata3d_pla_pla850carminered_1000_285_c` — PLA 850 Carmine Red
- `sakata3d_pla_pla850chocolate_1000_285_c` — PLA 850 Chocolate
- `sakata3d_pla_pla850clay_1000_285_c` — PLA 850 Clay
- `sakata3d_pla_pla850fluorlightgreen_1000_285_c` — PLA 850 Fluor Light Green
- `sakata3d_pla_pla850fluorlime_1000_285_c` — PLA 850 Fluor Lime
- `sakata3d_pla_pla850fluororange_1000_285_c` — PLA 850 Fluor Orange
- `sakata3d_pla_pla850fluororangefresh_1000_285_c` — PLA 850 Fluor Orange Fresh
- `sakata3d_pla_pla850fluoryellow_1000_285_c` — PLA 850 Fluor Yellow
- `sakata3d_pla_pla850fucsia_1000_285_c` — PLA 850 Fucsia
- `sakata3d_pla_pla850gold_1000_285_c` — PLA 850 Gold
- `sakata3d_pla_pla850granite_1000_285_c` — PLA 850 Granite
- `sakata3d_pla_pla850green_1000_285_c` — PLA 850 Green
- `sakata3d_pla_pla850grey_1000_285_c` — PLA 850 Grey
- `sakata3d_pla_pla850ivory_1000_285_c` — PLA 850 Ivory
- `sakata3d_pla_pla850militartone1gc_1000_285_c` — PLA 850 Militar Tone 1 Gc
- `sakata3d_pla_pla850militartone2_1000_285_c` — PLA 850 Militar Tone 2
- `sakata3d_pla_pla850natural_1000_285_c` — PLA 850 Natural
- `sakata3d_pla_pla850orange_1000_285_c` — PLA 850 Orange
- `sakata3d_pla_pla850pastelbabypink_1000_285_c` — PLA 850 Pastel Baby Pink
- `sakata3d_pla_pla850pastelgreen_1000_285_c` — PLA 850 Pastel Green
- `sakata3d_pla_pla850pastellilac_1000_285_c` — PLA 850 Pastel Lilac
- `sakata3d_pla_pla850pastelmangoyellow_1000_285_c` — PLA 850 Pastel Mango Yellow
- `sakata3d_pla_pla850pink_1000_285_c` — PLA 850 Pink
- `sakata3d_pla_pla850purple_1000_285_c` — PLA 850 Purple
- `sakata3d_pla_pla850red_1000_285_c` — PLA 850 Red
- `sakata3d_pla_pla850silver_1000_285_c` — PLA 850 Silver
- `sakata3d_pla_pla850skintone1_1000_285_c` — PLA 850 Skin Tone 1
- `sakata3d_pla_pla850skintone2_1000_285_c` — PLA 850 Skin Tone 2
- `sakata3d_pla_pla850skyblue_1000_285_c` — PLA 850 Sky Blue
- `sakata3d_pla_pla850solidary_1000_285_c` — PLA 850 Solidary
- `sakata3d_pla_pla850surfgreen_1000_285_c` — PLA 850 Surf Green
- `sakata3d_pla_pla850white_1000_285_c` — PLA 850 White
- `sakata3d_pla_pla850yellow_1000_285_c` — PLA 850 Yellow
- `sakata3d_pla_pla850fuchsia_1000_285_c` — PLA 850 Fuchsia
- `sakata3d_pla_pla850andaluciagreen_2500_175_c` — PLA 850 Andalucia Green
- `sakata3d_pla_pla850anthracitegray_2500_175_c` — PLA 850 Anthracite Gray
- `sakata3d_pla_pla850black_2500_175_c` — PLA 850 Black
- `sakata3d_pla_pla850blue_2500_175_c` — PLA 850 Blue
- `sakata3d_pla_pla850carminered_2500_175_c` — PLA 850 Carmine Red
- `sakata3d_pla_pla850chocolate_2500_175_c` — PLA 850 Chocolate
- `sakata3d_pla_pla850clay_2500_175_c` — PLA 850 Clay
- `sakata3d_pla_pla850fluorlightgreen_2500_175_c` — PLA 850 Fluor Light Green
- `sakata3d_pla_pla850fluorlime_2500_175_c` — PLA 850 Fluor Lime
- `sakata3d_pla_pla850fluororange_2500_175_c` — PLA 850 Fluor Orange
- `sakata3d_pla_pla850fluororangefresh_2500_175_c` — PLA 850 Fluor Orange Fresh
- `sakata3d_pla_pla850fluoryellow_2500_175_c` — PLA 850 Fluor Yellow
- `sakata3d_pla_pla850fucsia_2500_175_c` — PLA 850 Fucsia
- `sakata3d_pla_pla850gold_2500_175_c` — PLA 850 Gold
- `sakata3d_pla_pla850granite_2500_175_c` — PLA 850 Granite
- `sakata3d_pla_pla850green_2500_175_c` — PLA 850 Green
- `sakata3d_pla_pla850grey_2500_175_c` — PLA 850 Grey
- `sakata3d_pla_pla850ivory_2500_175_c` — PLA 850 Ivory
- `sakata3d_pla_pla850militartone1gc_2500_175_c` — PLA 850 Militar Tone 1 Gc
- `sakata3d_pla_pla850militartone2_2500_175_c` — PLA 850 Militar Tone 2
- `sakata3d_pla_pla850natural_2500_175_c` — PLA 850 Natural
- `sakata3d_pla_pla850orange_2500_175_c` — PLA 850 Orange
- `sakata3d_pla_pla850pastelbabypink_2500_175_c` — PLA 850 Pastel Baby Pink
- `sakata3d_pla_pla850pastelgreen_2500_175_c` — PLA 850 Pastel Green
- `sakata3d_pla_pla850pastellilac_2500_175_c` — PLA 850 Pastel Lilac
- `sakata3d_pla_pla850pastelmangoyellow_2500_175_c` — PLA 850 Pastel Mango Yellow
- `sakata3d_pla_pla850pink_2500_175_c` — PLA 850 Pink
- `sakata3d_pla_pla850purple_2500_175_c` — PLA 850 Purple
- `sakata3d_pla_pla850red_2500_175_c` — PLA 850 Red
- `sakata3d_pla_pla850silver_2500_175_c` — PLA 850 Silver
- `sakata3d_pla_pla850skintone1_2500_175_c` — PLA 850 Skin Tone 1
- `sakata3d_pla_pla850skintone2_2500_175_c` — PLA 850 Skin Tone 2
- `sakata3d_pla_pla850skyblue_2500_175_c` — PLA 850 Sky Blue
- `sakata3d_pla_pla850solidary_2500_175_c` — PLA 850 Solidary
- `sakata3d_pla_pla850surfgreen_2500_175_c` — PLA 850 Surf Green
- `sakata3d_pla_pla850white_2500_175_c` — PLA 850 White
- `sakata3d_pla_pla850yellow_2500_175_c` — PLA 850 Yellow
- `sakata3d_pla_pla850fuchsia_2500_175_c` — PLA 850 Fuchsia
- `sakata3d_pla_pla850andaluciagreen_2500_285_c` — PLA 850 Andalucia Green
- `sakata3d_pla_pla850anthracitegray_2500_285_c` — PLA 850 Anthracite Gray
- `sakata3d_pla_pla850black_2500_285_c` — PLA 850 Black
- `sakata3d_pla_pla850blue_2500_285_c` — PLA 850 Blue
- `sakata3d_pla_pla850carminered_2500_285_c` — PLA 850 Carmine Red
- `sakata3d_pla_pla850chocolate_2500_285_c` — PLA 850 Chocolate
- `sakata3d_pla_pla850clay_2500_285_c` — PLA 850 Clay
- `sakata3d_pla_pla850fluorlightgreen_2500_285_c` — PLA 850 Fluor Light Green
- `sakata3d_pla_pla850fluorlime_2500_285_c` — PLA 850 Fluor Lime
- `sakata3d_pla_pla850fluororange_2500_285_c` — PLA 850 Fluor Orange
- `sakata3d_pla_pla850fluororangefresh_2500_285_c` — PLA 850 Fluor Orange Fresh
- `sakata3d_pla_pla850fluoryellow_2500_285_c` — PLA 850 Fluor Yellow
- `sakata3d_pla_pla850fucsia_2500_285_c` — PLA 850 Fucsia
- `sakata3d_pla_pla850gold_2500_285_c` — PLA 850 Gold
- `sakata3d_pla_pla850granite_2500_285_c` — PLA 850 Granite
- `sakata3d_pla_pla850green_2500_285_c` — PLA 850 Green
- `sakata3d_pla_pla850grey_2500_285_c` — PLA 850 Grey
- `sakata3d_pla_pla850ivory_2500_285_c` — PLA 850 Ivory
- `sakata3d_pla_pla850militartone1gc_2500_285_c` — PLA 850 Militar Tone 1 Gc
- `sakata3d_pla_pla850militartone2_2500_285_c` — PLA 850 Militar Tone 2
- `sakata3d_pla_pla850natural_2500_285_c` — PLA 850 Natural
- `sakata3d_pla_pla850orange_2500_285_c` — PLA 850 Orange
- `sakata3d_pla_pla850pastelbabypink_2500_285_c` — PLA 850 Pastel Baby Pink
- `sakata3d_pla_pla850pastelgreen_2500_285_c` — PLA 850 Pastel Green
- `sakata3d_pla_pla850pastellilac_2500_285_c` — PLA 850 Pastel Lilac
- `sakata3d_pla_pla850pastelmangoyellow_2500_285_c` — PLA 850 Pastel Mango Yellow
- `sakata3d_pla_pla850pink_2500_285_c` — PLA 850 Pink
- `sakata3d_pla_pla850purple_2500_285_c` — PLA 850 Purple
- `sakata3d_pla_pla850red_2500_285_c` — PLA 850 Red
- `sakata3d_pla_pla850silver_2500_285_c` — PLA 850 Silver
- `sakata3d_pla_pla850skintone1_2500_285_c` — PLA 850 Skin Tone 1
- `sakata3d_pla_pla850skintone2_2500_285_c` — PLA 850 Skin Tone 2
- `sakata3d_pla_pla850skyblue_2500_285_c` — PLA 850 Sky Blue
- `sakata3d_pla_pla850solidary_2500_285_c` — PLA 850 Solidary
- `sakata3d_pla_pla850surfgreen_2500_285_c` — PLA 850 Surf Green
- `sakata3d_pla_pla850white_2500_285_c` — PLA 850 White
- `sakata3d_pla_pla850yellow_2500_285_c` — PLA 850 Yellow
- `sakata3d_pla_pla850fuchsia_2500_285_c` — PLA 850 Fuchsia
- `sakata3d_pla_pla850andaluciagreen_5000_175_c` — PLA 850 Andalucia Green
- `sakata3d_pla_pla850anthracitegray_5000_175_c` — PLA 850 Anthracite Gray
- `sakata3d_pla_pla850black_5000_175_c` — PLA 850 Black
- `sakata3d_pla_pla850blue_5000_175_c` — PLA 850 Blue
- `sakata3d_pla_pla850carminered_5000_175_c` — PLA 850 Carmine Red
- `sakata3d_pla_pla850chocolate_5000_175_c` — PLA 850 Chocolate
- `sakata3d_pla_pla850clay_5000_175_c` — PLA 850 Clay
- `sakata3d_pla_pla850fluorlightgreen_5000_175_c` — PLA 850 Fluor Light Green
- `sakata3d_pla_pla850fluorlime_5000_175_c` — PLA 850 Fluor Lime
- `sakata3d_pla_pla850fluororange_5000_175_c` — PLA 850 Fluor Orange
- `sakata3d_pla_pla850fluororangefresh_5000_175_c` — PLA 850 Fluor Orange Fresh
- `sakata3d_pla_pla850fluoryellow_5000_175_c` — PLA 850 Fluor Yellow
- `sakata3d_pla_pla850fucsia_5000_175_c` — PLA 850 Fucsia
- `sakata3d_pla_pla850gold_5000_175_c` — PLA 850 Gold
- `sakata3d_pla_pla850granite_5000_175_c` — PLA 850 Granite
- `sakata3d_pla_pla850green_5000_175_c` — PLA 850 Green
- `sakata3d_pla_pla850grey_5000_175_c` — PLA 850 Grey
- `sakata3d_pla_pla850ivory_5000_175_c` — PLA 850 Ivory
- `sakata3d_pla_pla850militartone1gc_5000_175_c` — PLA 850 Militar Tone 1 Gc
- `sakata3d_pla_pla850militartone2_5000_175_c` — PLA 850 Militar Tone 2
- `sakata3d_pla_pla850natural_5000_175_c` — PLA 850 Natural
- `sakata3d_pla_pla850orange_5000_175_c` — PLA 850 Orange
- `sakata3d_pla_pla850pastelbabypink_5000_175_c` — PLA 850 Pastel Baby Pink
- `sakata3d_pla_pla850pastelgreen_5000_175_c` — PLA 850 Pastel Green
- `sakata3d_pla_pla850pastellilac_5000_175_c` — PLA 850 Pastel Lilac
- `sakata3d_pla_pla850pastelmangoyellow_5000_175_c` — PLA 850 Pastel Mango Yellow
- `sakata3d_pla_pla850pink_5000_175_c` — PLA 850 Pink
- `sakata3d_pla_pla850purple_5000_175_c` — PLA 850 Purple
- `sakata3d_pla_pla850red_5000_175_c` — PLA 850 Red
- `sakata3d_pla_pla850silver_5000_175_c` — PLA 850 Silver
- `sakata3d_pla_pla850skintone1_5000_175_c` — PLA 850 Skin Tone 1
- `sakata3d_pla_pla850skintone2_5000_175_c` — PLA 850 Skin Tone 2
- `sakata3d_pla_pla850skyblue_5000_175_c` — PLA 850 Sky Blue
- `sakata3d_pla_pla850solidary_5000_175_c` — PLA 850 Solidary
- `sakata3d_pla_pla850surfgreen_5000_175_c` — PLA 850 Surf Green
- `sakata3d_pla_pla850white_5000_175_c` — PLA 850 White
- `sakata3d_pla_pla850yellow_5000_175_c` — PLA 850 Yellow
- `sakata3d_pla_pla850fuchsia_5000_175_c` — PLA 850 Fuchsia
- `sakata3d_pla_pla850andaluciagreen_5000_285_c` — PLA 850 Andalucia Green
- `sakata3d_pla_pla850anthracitegray_5000_285_c` — PLA 850 Anthracite Gray
- `sakata3d_pla_pla850black_5000_285_c` — PLA 850 Black
- `sakata3d_pla_pla850blue_5000_285_c` — PLA 850 Blue
- `sakata3d_pla_pla850carminered_5000_285_c` — PLA 850 Carmine Red
- `sakata3d_pla_pla850chocolate_5000_285_c` — PLA 850 Chocolate
- `sakata3d_pla_pla850clay_5000_285_c` — PLA 850 Clay
- `sakata3d_pla_pla850fluorlightgreen_5000_285_c` — PLA 850 Fluor Light Green
- `sakata3d_pla_pla850fluorlime_5000_285_c` — PLA 850 Fluor Lime
- `sakata3d_pla_pla850fluororange_5000_285_c` — PLA 850 Fluor Orange
- `sakata3d_pla_pla850fluororangefresh_5000_285_c` — PLA 850 Fluor Orange Fresh
- `sakata3d_pla_pla850fluoryellow_5000_285_c` — PLA 850 Fluor Yellow
- `sakata3d_pla_pla850fucsia_5000_285_c` — PLA 850 Fucsia
- `sakata3d_pla_pla850gold_5000_285_c` — PLA 850 Gold
- `sakata3d_pla_pla850granite_5000_285_c` — PLA 850 Granite
- `sakata3d_pla_pla850green_5000_285_c` — PLA 850 Green
- `sakata3d_pla_pla850grey_5000_285_c` — PLA 850 Grey
- `sakata3d_pla_pla850ivory_5000_285_c` — PLA 850 Ivory
- `sakata3d_pla_pla850militartone1gc_5000_285_c` — PLA 850 Militar Tone 1 Gc
- `sakata3d_pla_pla850militartone2_5000_285_c` — PLA 850 Militar Tone 2
- `sakata3d_pla_pla850natural_5000_285_c` — PLA 850 Natural
- `sakata3d_pla_pla850orange_5000_285_c` — PLA 850 Orange
- `sakata3d_pla_pla850pastelbabypink_5000_285_c` — PLA 850 Pastel Baby Pink
- `sakata3d_pla_pla850pastelgreen_5000_285_c` — PLA 850 Pastel Green
- `sakata3d_pla_pla850pastellilac_5000_285_c` — PLA 850 Pastel Lilac
- `sakata3d_pla_pla850pastelmangoyellow_5000_285_c` — PLA 850 Pastel Mango Yellow
- `sakata3d_pla_pla850pink_5000_285_c` — PLA 850 Pink
- `sakata3d_pla_pla850purple_5000_285_c` — PLA 850 Purple
- `sakata3d_pla_pla850red_5000_285_c` — PLA 850 Red
- `sakata3d_pla_pla850silver_5000_285_c` — PLA 850 Silver
- `sakata3d_pla_pla850skintone1_5000_285_c` — PLA 850 Skin Tone 1
- `sakata3d_pla_pla850skintone2_5000_285_c` — PLA 850 Skin Tone 2
- `sakata3d_pla_pla850skyblue_5000_285_c` — PLA 850 Sky Blue
- `sakata3d_pla_pla850solidary_5000_285_c` — PLA 850 Solidary
- `sakata3d_pla_pla850surfgreen_5000_285_c` — PLA 850 Surf Green
- `sakata3d_pla_pla850white_5000_285_c` — PLA 850 White
- `sakata3d_pla_pla850yellow_5000_285_c` — PLA 850 Yellow
- `sakata3d_pla_pla850fuchsia_5000_285_c` — PLA 850 Fuchsia
- `sakata3d_pla_plago&printpasteltorquoise_1000_175_c` — PLA GO&PRINT Pastel Torquoise
- `sakata3d_pla_plago&printblack_1000_285_c` — PLA GO&PRINT Black
- `sakata3d_pla_plago&printblue_1000_285_c` — PLA GO&PRINT Blue
- `sakata3d_pla_plago&printchocolate_1000_285_c` — PLA GO&PRINT Chocolate
- `sakata3d_pla_plago&printfuchsia_1000_285_c` — PLA GO&PRINT Fuchsia
- `sakata3d_pla_plago&printgreen_1000_285_c` — PLA GO&PRINT Green
- `sakata3d_pla_plago&printgrey_1000_285_c` — PLA GO&PRINT Grey
- `sakata3d_pla_plago&printorange_1000_285_c` — PLA GO&PRINT Orange
- `sakata3d_pla_plago&printpastelpink_1000_285_c` — PLA GO&PRINT Pastel Pink
- `sakata3d_pla_plago&printpasteltorquoise_1000_285_c` — PLA GO&PRINT Pastel Torquoise
- `sakata3d_pla_plago&printpastelyellow_1000_285_c` — PLA GO&PRINT Pastel Yellow
- `sakata3d_pla_plago&printpink_1000_285_c` — PLA GO&PRINT Pink
- `sakata3d_pla_plago&printpurple_1000_285_c` — PLA GO&PRINT Purple
- `sakata3d_pla_plago&printred_1000_285_c` — PLA GO&PRINT Red
- `sakata3d_pla_plago&printsilver_1000_285_c` — PLA GO&PRINT Silver
- `sakata3d_pla_plago&printwhite_1000_285_c` — PLA GO&PRINT White
- `sakata3d_pla_plago&printyellow_1000_285_c` — PLA GO&PRINT Yellow
- `sakata3d_pla_plahr-870black_1000_285_c` — PLA HR-870 Black
- `sakata3d_pla_plahr-870blue_1000_285_c` — PLA HR-870 Blue
- `sakata3d_pla_plahr-870green_1000_285_c` — PLA HR-870 Green
- `sakata3d_pla_plahr-870grey_1000_285_c` — PLA HR-870 Grey
- `sakata3d_pla_plahr-870natural_1000_285_c` — PLA HR-870 Natural
- `sakata3d_pla_plahr-870orange_1000_285_c` — PLA HR-870 Orange
- `sakata3d_pla_plahr-870red_1000_285_c` — PLA HR-870 Red
- `sakata3d_pla_plahr-870silver_1000_285_c` — PLA HR-870 Silver
- `sakata3d_pla_plahr-870white_1000_285_c` — PLA HR-870 White
- `sakata3d_pla_plahr-870yellow_1000_285_c` — PLA HR-870 Yellow
- `sakata3d_pla_plahshighspeedproblack_1000_175_c` — PLA HS High Speed PRO Black
- `sakata3d_pla_plahshighspeedproblue_1000_175_c` — PLA HS High Speed PRO Blue
- `sakata3d_pla_plahshighspeedprofluorlightblue_1000_175_c` — PLA HS High Speed PRO Fluor Light Blue
- `sakata3d_pla_plahshighspeedprofluorlightgreen_1000_175_c` — PLA HS High Speed PRO Fluor Light Green
- `sakata3d_pla_plahshighspeedprofluorpurple_1000_175_c` — PLA HS High Speed PRO Fluor Purple
- `sakata3d_pla_plahshighspeedprogreen_1000_175_c` — PLA HS High Speed PRO Green
- `sakata3d_pla_plahshighspeedprogrey_1000_175_c` — PLA HS High Speed PRO Grey
- `sakata3d_pla_plahshighspeedproivory_1000_175_c` — PLA HS High Speed PRO Ivory
- `sakata3d_pla_plahshighspeedpromilitar2_1000_175_c` — PLA HS High Speed PRO Militar 2
- `sakata3d_pla_plahshighspeedprored_1000_175_c` — PLA HS High Speed PRO Red
- `sakata3d_pla_plahshighspeedprowhite_1000_175_c` — PLA HS High Speed PRO White
- `sakata3d_pla_plahshighspeedproyellow_1000_175_c` — PLA HS High Speed PRO Yellow
- `sakata3d_pla_plawoodolivegreen_1000_175_c` — PLA WOOD Olive Green
- `sakata3d_pla_pla-mblack_1000_175_c` — PLA-M Black
- `sakata3d_pla_pla-mblue_1000_175_c` — PLA-M Blue
- `sakata3d_pla_pla-mgrey_1000_175_c` — PLA-M Grey
- `sakata3d_pla_pla-mred_1000_175_c` — PLA-M Red
- `sakata3d_pla_pla-mwhite_1000_175_c` — PLA-M White
- `sakata3d_pla_pla-myellow_1000_175_c` — PLA-M Yellow
- `sakata3d_pla_pla-mblack_1000_285_c` — PLA-M Black
- `sakata3d_pla_pla-mblue_1000_285_c` — PLA-M Blue
- `sakata3d_pla_pla-mgrey_1000_285_c` — PLA-M Grey
- `sakata3d_pla_pla-mred_1000_285_c` — PLA-M Red
- `sakata3d_pla_pla-mwhite_1000_285_c` — PLA-M White
- `sakata3d_pla_pla-myellow_1000_285_c` — PLA-M Yellow
- `sakata3d_abs_absesurfgreen_1000_175_c` — ABS E Surf Green
- `sakata3d_petg_petgcfpet-gcf15_1000_175_c` — PETG CF PET-G CF15
- `sakata3d_pla_go&printplagold_1000_175_c` — Go&Print PLA Gold
- `sakata3d_pla_go&printplalightblue_1000_175_c` — Go&Print PLA Light Blue
- `sakata3d_pla_go&printplamagicstargold_1000_175_c` — Go&Print PLA Magic Star Gold
- `sakata3d_pla_go&printplamilitar1gc_1000_175_c` — Go&Print PLA Militar 1 GC
- `sakata3d_pla_go&printplapastelgreen_1000_175_c` — Go&Print PLA Pastel Green
- `sakata3d_pla_go&printplapastelturquoise_1000_175_c` — Go&Print PLA Pastel Turquoise
- `sakata3d_pla_go&printplaskintone2_1000_175_c` — Go&Print PLA Skin Tone 2
- `sakata3d_pla_go&printplasurfgreen_1000_175_c` — Go&Print PLA Surf Green
- `sakata3d_pla_highspeedplablack_1000_175_c` — High Speed PLA Black
- `sakata3d_pla_highspeedplablue_1000_175_c` — High Speed PLA Blue
- `sakata3d_pla_highspeedplagreen_1000_175_c` — High Speed PLA Green
- `sakata3d_pla_highspeedplagrey_1000_175_c` — High Speed PLA Grey
- `sakata3d_pla_highspeedplared_1000_175_c` — High Speed PLA Red
- `sakata3d_pla_highspeedplawhite_1000_175_c` — High Speed PLA White
- `sakata3d_pla_highspeedplayellow_1000_175_c` — High Speed PLA Yellow
- `sakata3d_pla_matteplamblack_1000_175_c` — Matte PLA M Black
- `sakata3d_pla_matteplamblue_1000_175_c` — Matte PLA M Blue
- `sakata3d_pla_matteplamgrey_1000_175_c` — Matte PLA M Grey
- `sakata3d_pla_matteplamred_1000_175_c` — Matte PLA M Red
- `sakata3d_pla_matteplamwhite_1000_175_c` — Matte PLA M White
- `sakata3d_pla_matteplamyellow_1000_175_c` — Matte PLA M Yellow
- `sakata3d_pla_plasilk850arctic_1000_175_c` — PLA Silk 850 Arctic
- `sakata3d_pla_plasilk850clover_1000_175_c` — PLA Silk 850 Clover
- `sakata3d_pla_plasilk850firgreen_1000_175_c` — PLA Silk 850 Fir Green
- `sakata3d_pla_plasilk850gold_1000_175_c` — PLA Silk 850 Gold
- `sakata3d_pla_plasilk850midnight_1000_175_c` — PLA Silk 850 Midnight
- `sakata3d_pla_plasilk850ocean_1000_175_c` — PLA Silk 850 Ocean
- `sakata3d_pla_plasilk850snow_1000_175_c` — PLA Silk 850 Snow
- `sakata3d_pla_plasilk850sunset_1000_175_c` — PLA Silk 850 Sunset
- `sakata3d_pla_plasilk850wine_1000_175_c` — PLA Silk 850 Wine
