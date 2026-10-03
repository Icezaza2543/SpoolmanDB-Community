# extrudr duplicate migration review

Base `fc58e8a03c627357fa6b2f7ec985681966df4b87`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `b9bfb65b2d5ee0b6da1c420aacdb34355edda1db7602b5e39fc34509dee2720f`.

## Authorization and result

{"groups": 29, "approved_groups": 29, "retired": 29, "deferred": 0, "hard_stops": 0, "before_count": 51974, "after_count": 51945, "brand_before": 1155, "brand_after": 1126, "registry_before": 1460, "registry_after": 1489, "metadata_fields_changed": 32, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

29 Rule1 survivors retained. Eight Basic250/110 values are incompatible with exact official PLA Basic; replace invalid points with200–230/20–60 ranges, not invented midpoints. NX2 density1.3/matte/nozzle230/bed60 agree with exact TDS; keep, not imported genericPLA1.24. Existing documentlinks are matching. All non-target variants, HEX/tare/packaging untouched.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://s3.extrudr.com/extrudr-media/datasheets/tds/tds-en/pla-basic-TDS-en.pdf", "date": "2025-07-16", "density": 1.24, "nozzle": [200, 230], "bed": [20, 60]}
- {"url": "https://s3.extrudr.com/extrudr-media/datasheets/tds/tds-en/pla-basic-cmyk-TDS-en.pdf", "density": 1.24, "nozzle": [200, 230], "bed": [20, 60], "note": "Exact CMYKline same settings; no packaging inference."}
- {"url": "https://s3.extrudr.com/extrudr-media/datasheets/tds/tds-en/pla-nx2-matt-TDS-en.pdf", "date": "2025-07-16", "density": 1.3, "nozzle": [200, 230], "bed": [20, 60]}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`extrudr_pla_basicplablack_1000_175_p`|`extrudr_pla_basic-black_1000_175_p`|`extrudr.json::Extrudr::Basic PLA {color_name}::Basic PLA Black::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_basicplacmyklithocyan_1000_175_p`|`extrudr_pla_basic-cmyklithocyan_1000_175_p`|`extrudr.json::Extrudr::Basic PLA {color_name}::Basic PLA CMYK Lithocyan::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_basicplacmyklithomagenta_1000_175_p`|`extrudr_pla_basic-cmyklithomagenta_1000_175_p`|`extrudr.json::Extrudr::Basic PLA {color_name}::Basic PLA CMYK Lithomagenta::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_basicplacmyklithowhite_1000_175_p`|`extrudr_pla_basic-cmyklithowhite_1000_175_p`|`extrudr.json::Extrudr::Basic PLA {color_name}::Basic PLA CMYK Lithowhite::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_basicplacmyklithoyellow_1000_175_p`|`extrudr_pla_basic-cmyklithoyellow_1000_175_p`|`extrudr.json::Extrudr::Basic PLA {color_name}::Basic PLA CMYK Lithoyellow::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_basicplagold_1000_175_p`|`extrudr_pla_basic-gold_1000_175_p`|`extrudr.json::Extrudr::Basic PLA {color_name}::Basic PLA Gold::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_basicplatransparent_1000_175_p`|`extrudr_pla_basic-transparent_1000_175_p`|`extrudr.json::Extrudr::Basic PLA {color_name}::Basic PLA Transparent::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_basicplawhite_1000_175_p`|`extrudr_pla_basic-white_1000_175_p`|`extrudr.json::Extrudr::Basic PLA {color_name}::Basic PLA White::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattanthracite_1000_175_p`|`extrudr_pla_nx2-matt-anthracite_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Anthracite::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattblack_1000_175_p`|`extrudr_pla_nx2-matt-black_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Black::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattbluesteel_1000_175_p`|`extrudr_pla_nx2-matt-bluesteel_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Blue Steel::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattbrown_1000_175_p`|`extrudr_pla_nx2-matt-brown_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Brown::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattemeraldgreen_1000_175_p`|`extrudr_pla_nx2-matt-emeraldgreen_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Emerald Green::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattepicpurple_1000_175_p`|`extrudr_pla_nx2-matt-epicpurple_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Epic Purple::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattgrey_1000_175_p`|`extrudr_pla_nx2-matt-grey_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Grey::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2matthellfirered_1000_175_p`|`extrudr_pla_nx2-matt-hellfirered_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Hellfire Red::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattlightblue_1000_175_p`|`extrudr_pla_nx2-matt-lightblue_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Light Blue::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattmetallicgrey_1000_175_p`|`extrudr_pla_nx2-matt-metallicgrey_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Metallic Grey::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattmilitarybeige_1000_175_p`|`extrudr_pla_nx2-matt-militarybeige_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Military Beige::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattmilitarygreen_1000_175_p`|`extrudr_pla_nx2-matt-militarygreen_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Military Green::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattnavyblue_1000_175_p`|`extrudr_pla_nx2-matt-navyblue_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Navy Blue::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattneonorange_1000_175_p`|`extrudr_pla_nx2-matt-neonorange_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Neon Orange::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattorange_1000_175_p`|`extrudr_pla_nx2-matt-orange_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Orange::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattpurple_1000_175_p`|`extrudr_pla_nx2-matt-purple_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Purple::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattsignalgreen_1000_175_p`|`extrudr_pla_nx2-matt-signalgreen_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Signal Green::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattsilver_1000_175_p`|`extrudr_pla_nx2-matt-silver_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Silver::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattturquoise_1000_175_p`|`extrudr_pla_nx2-matt-turquoise_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Turquoise::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattwhite_1000_175_p`|`extrudr_pla_nx2-matt-white_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt White::PLA::1000::1.75::plastic::False`|
|`extrudr_pla_planx2mattyellow_1000_175_p`|`extrudr_pla_nx2-matt-yellow_1000_175_p`|`extrudr.json::Extrudr::PLA NX2 Matt {color_name}::PLA NX2 Matt Yellow::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### EX001: dup-96ea24a1564dd3d998c58dc6f6bae9013078dceacf499408469f74541a9d6d00

Status: APPROVED; survivor `extrudr_pla_basic-black_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_basic-black_1000_175_p`|`Basic - {color_name}`|`Black `|{"source_file": "extrudr.json", "definition_index": 16, "weights": 4, "diameters": 2, "colors": 8, "compiled_records": 64} / True|
|`extrudr_pla_basicplablack_1000_175_p`|`Basic PLA {color_name}`|`Black`|{"source_file": "extrudr.json", "definition_index": 37, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "extrudr_pla_basic-black_1000_175_p": 260.0,
    "extrudr_pla_basicplablack_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_basic-black_1000_175_p": "1E1E1E",
    "extrudr_pla_basicplablack_1000_175_p": "000000"
  },
  "extruder_temp": {
    "extrudr_pla_basic-black_1000_175_p": 250,
    "extrudr_pla_basicplablack_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_basic-black_1000_175_p": null,
    "extrudr_pla_basicplablack_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_basic-black_1000_175_p": 110,
    "extrudr_pla_basicplablack_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_basic-black_1000_175_p": null,
    "extrudr_pla_basicplablack_1000_175_p": [
      50,
      70
    ]
  }
}
```

### EX002: dup-0c98173fd6f0320bdb65c3d677dfc25aaa526e4f15dc91a42a34142de52c1c6d

Status: APPROVED; survivor `extrudr_pla_basic-cmyklithocyan_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_basic-cmyklithocyan_1000_175_p`|`Basic - {color_name}`|`CMYK Lithocyan`|{"source_file": "extrudr.json", "definition_index": 16, "weights": 4, "diameters": 2, "colors": 8, "compiled_records": 64} / True|
|`extrudr_pla_basicplacmyklithocyan_1000_175_p`|`Basic PLA {color_name}`|`CMYK Lithocyan`|{"source_file": "extrudr.json", "definition_index": 37, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "extrudr_pla_basic-cmyklithocyan_1000_175_p": 260.0,
    "extrudr_pla_basicplacmyklithocyan_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_basic-cmyklithocyan_1000_175_p": "84C3BE",
    "extrudr_pla_basicplacmyklithocyan_1000_175_p": "0099E6"
  },
  "extruder_temp": {
    "extrudr_pla_basic-cmyklithocyan_1000_175_p": 250,
    "extrudr_pla_basicplacmyklithocyan_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_basic-cmyklithocyan_1000_175_p": null,
    "extrudr_pla_basicplacmyklithocyan_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_basic-cmyklithocyan_1000_175_p": 110,
    "extrudr_pla_basicplacmyklithocyan_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_basic-cmyklithocyan_1000_175_p": null,
    "extrudr_pla_basicplacmyklithocyan_1000_175_p": [
      50,
      70
    ]
  }
}
```

### EX003: dup-90d97d1c2c28fa73adbe7c6f3620956d0676fb56723ccbcd5c5a893f9206e381

Status: APPROVED; survivor `extrudr_pla_basic-cmyklithomagenta_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_basic-cmyklithomagenta_1000_175_p`|`Basic - {color_name}`|`CMYK Lithomagenta`|{"source_file": "extrudr.json", "definition_index": 16, "weights": 4, "diameters": 2, "colors": 8, "compiled_records": 64} / True|
|`extrudr_pla_basicplacmyklithomagenta_1000_175_p`|`Basic PLA {color_name}`|`CMYK Lithomagenta`|{"source_file": "extrudr.json", "definition_index": 37, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "extrudr_pla_basic-cmyklithomagenta_1000_175_p": 260.0,
    "extrudr_pla_basicplacmyklithomagenta_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_basic-cmyklithomagenta_1000_175_p": "CF3476",
    "extrudr_pla_basicplacmyklithomagenta_1000_175_p": "C75072"
  },
  "extruder_temp": {
    "extrudr_pla_basic-cmyklithomagenta_1000_175_p": 250,
    "extrudr_pla_basicplacmyklithomagenta_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_basic-cmyklithomagenta_1000_175_p": null,
    "extrudr_pla_basicplacmyklithomagenta_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_basic-cmyklithomagenta_1000_175_p": 110,
    "extrudr_pla_basicplacmyklithomagenta_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_basic-cmyklithomagenta_1000_175_p": null,
    "extrudr_pla_basicplacmyklithomagenta_1000_175_p": [
      50,
      70
    ]
  }
}
```

### EX004: dup-9df15196a492a95114fab1ef29cad1a9c2a26f103b4b1c4a18f8e98e4686bc8f

Status: APPROVED; survivor `extrudr_pla_basic-cmyklithowhite_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_basic-cmyklithowhite_1000_175_p`|`Basic - {color_name}`|`CMYK Lithowhite`|{"source_file": "extrudr.json", "definition_index": 16, "weights": 4, "diameters": 2, "colors": 8, "compiled_records": 64} / True|
|`extrudr_pla_basicplacmyklithowhite_1000_175_p`|`Basic PLA {color_name}`|`CMYK Lithowhite`|{"source_file": "extrudr.json", "definition_index": 37, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "extrudr_pla_basic-cmyklithowhite_1000_175_p": 260.0,
    "extrudr_pla_basicplacmyklithowhite_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_basic-cmyklithowhite_1000_175_p": "F4F4F4",
    "extrudr_pla_basicplacmyklithowhite_1000_175_p": "FFFFFF"
  },
  "extruder_temp": {
    "extrudr_pla_basic-cmyklithowhite_1000_175_p": 250,
    "extrudr_pla_basicplacmyklithowhite_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_basic-cmyklithowhite_1000_175_p": null,
    "extrudr_pla_basicplacmyklithowhite_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_basic-cmyklithowhite_1000_175_p": 110,
    "extrudr_pla_basicplacmyklithowhite_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_basic-cmyklithowhite_1000_175_p": null,
    "extrudr_pla_basicplacmyklithowhite_1000_175_p": [
      50,
      70
    ]
  }
}
```

### EX005: dup-a659503fb70c4da6b9a22769d1315533a28ed2085b0046a86751fc7638ff36e0

Status: APPROVED; survivor `extrudr_pla_basic-cmyklithoyellow_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_basic-cmyklithoyellow_1000_175_p`|`Basic - {color_name}`|`CMYK Lithoyellow`|{"source_file": "extrudr.json", "definition_index": 16, "weights": 4, "diameters": 2, "colors": 8, "compiled_records": 64} / True|
|`extrudr_pla_basicplacmyklithoyellow_1000_175_p`|`Basic PLA {color_name}`|`CMYK Lithoyellow`|{"source_file": "extrudr.json", "definition_index": 37, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "extrudr_pla_basic-cmyklithoyellow_1000_175_p": 260.0,
    "extrudr_pla_basicplacmyklithoyellow_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_basic-cmyklithoyellow_1000_175_p": "FFFF00",
    "extrudr_pla_basicplacmyklithoyellow_1000_175_p": "FAD61B"
  },
  "extruder_temp": {
    "extrudr_pla_basic-cmyklithoyellow_1000_175_p": 250,
    "extrudr_pla_basicplacmyklithoyellow_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_basic-cmyklithoyellow_1000_175_p": null,
    "extrudr_pla_basicplacmyklithoyellow_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_basic-cmyklithoyellow_1000_175_p": 110,
    "extrudr_pla_basicplacmyklithoyellow_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_basic-cmyklithoyellow_1000_175_p": null,
    "extrudr_pla_basicplacmyklithoyellow_1000_175_p": [
      50,
      70
    ]
  }
}
```

### EX006: dup-4ad642a5ea7a483401c86bf99e4960ca7f346eb5ec13090f11c4a1eef3237fb8

Status: APPROVED; survivor `extrudr_pla_basic-gold_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_basic-gold_1000_175_p`|`Basic - {color_name}`|`Gold`|{"source_file": "extrudr.json", "definition_index": 16, "weights": 4, "diameters": 2, "colors": 8, "compiled_records": 64} / True|
|`extrudr_pla_basicplagold_1000_175_p`|`Basic PLA {color_name}`|`Gold`|{"source_file": "extrudr.json", "definition_index": 37, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "extrudr_pla_basic-gold_1000_175_p": 260.0,
    "extrudr_pla_basicplagold_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_basic-gold_1000_175_p": "705335",
    "extrudr_pla_basicplagold_1000_175_p": "E3B145"
  },
  "extruder_temp": {
    "extrudr_pla_basic-gold_1000_175_p": 250,
    "extrudr_pla_basicplagold_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_basic-gold_1000_175_p": null,
    "extrudr_pla_basicplagold_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_basic-gold_1000_175_p": 110,
    "extrudr_pla_basicplagold_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_basic-gold_1000_175_p": null,
    "extrudr_pla_basicplagold_1000_175_p": [
      50,
      70
    ]
  }
}
```

### EX007: dup-824a095866db70fa080b83dd28f663ec4b1dcdd55db4a549a8bdec4ad746a830

Status: APPROVED; survivor `extrudr_pla_basic-transparent_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_basic-transparent_1000_175_p`|`Basic - {color_name}`|`Transparent `|{"source_file": "extrudr.json", "definition_index": 16, "weights": 4, "diameters": 2, "colors": 8, "compiled_records": 64} / True|
|`extrudr_pla_basicplatransparent_1000_175_p`|`Basic PLA {color_name}`|`Transparent`|{"source_file": "extrudr.json", "definition_index": 37, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "extrudr_pla_basic-transparent_1000_175_p": 260.0,
    "extrudr_pla_basicplatransparent_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_basic-transparent_1000_175_p": "FFFFFF",
    "extrudr_pla_basicplatransparent_1000_175_p": "EFE8D8"
  },
  "extruder_temp": {
    "extrudr_pla_basic-transparent_1000_175_p": 250,
    "extrudr_pla_basicplatransparent_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_basic-transparent_1000_175_p": null,
    "extrudr_pla_basicplatransparent_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_basic-transparent_1000_175_p": 110,
    "extrudr_pla_basicplatransparent_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_basic-transparent_1000_175_p": null,
    "extrudr_pla_basicplatransparent_1000_175_p": [
      50,
      70
    ]
  }
}
```

### EX008: dup-1f652ab82e8a22c2c0cce64fade422b6c318cc13b5a8a9e8b7cd9f7c6baa7386

Status: APPROVED; survivor `extrudr_pla_basic-white_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_basic-white_1000_175_p`|`Basic - {color_name}`|`White`|{"source_file": "extrudr.json", "definition_index": 16, "weights": 4, "diameters": 2, "colors": 8, "compiled_records": 64} / True|
|`extrudr_pla_basicplawhite_1000_175_p`|`Basic PLA {color_name}`|`White`|{"source_file": "extrudr.json", "definition_index": 37, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "extrudr_pla_basic-white_1000_175_p": 260.0,
    "extrudr_pla_basicplawhite_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_basic-white_1000_175_p": "F4F4F4",
    "extrudr_pla_basicplawhite_1000_175_p": "FFFFFF"
  },
  "extruder_temp": {
    "extrudr_pla_basic-white_1000_175_p": 250,
    "extrudr_pla_basicplawhite_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_basic-white_1000_175_p": null,
    "extrudr_pla_basicplawhite_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_basic-white_1000_175_p": 110,
    "extrudr_pla_basicplawhite_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_basic-white_1000_175_p": null,
    "extrudr_pla_basicplawhite_1000_175_p": [
      50,
      70
    ]
  }
}
```

### EX009: dup-64df1a390e3cc804b4781da1ac509160f357d7f371edd1f18dab8703fcc95e66

Status: APPROVED; survivor `extrudr_pla_nx2-matt-anthracite_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-anthracite_1000_175_p`|`NX2-MATT - {color_name}`|`Anthracite`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattanthracite_1000_175_p`|`PLA NX2 Matt {color_name}`|`Anthracite`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-anthracite_1000_175_p": 1.3,
    "extrudr_pla_planx2mattanthracite_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-anthracite_1000_175_p": 260.0,
    "extrudr_pla_planx2mattanthracite_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-anthracite_1000_175_p": "293133",
    "extrudr_pla_planx2mattanthracite_1000_175_p": "697272"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-anthracite_1000_175_p": 230,
    "extrudr_pla_planx2mattanthracite_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-anthracite_1000_175_p": null,
    "extrudr_pla_planx2mattanthracite_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-anthracite_1000_175_p": 60,
    "extrudr_pla_planx2mattanthracite_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-anthracite_1000_175_p": null,
    "extrudr_pla_planx2mattanthracite_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-anthracite_1000_175_p": "matte",
    "extrudr_pla_planx2mattanthracite_1000_175_p": null
  }
}
```

### EX010: dup-4f5a751c3e2706e5a69441b58e6b7330f511ae462298333c4f93c494e295546c

Status: APPROVED; survivor `extrudr_pla_nx2-matt-black_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-black_1000_175_p`|`NX2-MATT - {color_name}`|`Black`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattblack_1000_175_p`|`PLA NX2 Matt {color_name}`|`Black`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-black_1000_175_p": 1.3,
    "extrudr_pla_planx2mattblack_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-black_1000_175_p": 260.0,
    "extrudr_pla_planx2mattblack_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-black_1000_175_p": "1E1E1E",
    "extrudr_pla_planx2mattblack_1000_175_p": "000000"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-black_1000_175_p": 230,
    "extrudr_pla_planx2mattblack_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-black_1000_175_p": null,
    "extrudr_pla_planx2mattblack_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-black_1000_175_p": 60,
    "extrudr_pla_planx2mattblack_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-black_1000_175_p": null,
    "extrudr_pla_planx2mattblack_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-black_1000_175_p": "matte",
    "extrudr_pla_planx2mattblack_1000_175_p": null
  }
}
```

### EX011: dup-67fd33730b3ba111bb61917699abfda143b1c34b6c8953ac155e34da76fb9098

Status: APPROVED; survivor `extrudr_pla_nx2-matt-bluesteel_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-bluesteel_1000_175_p`|`NX2-MATT - {color_name}`|`Blue Steel`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattbluesteel_1000_175_p`|`PLA NX2 Matt {color_name}`|`Blue Steel`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-bluesteel_1000_175_p": 1.3,
    "extrudr_pla_planx2mattbluesteel_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-bluesteel_1000_175_p": 260.0,
    "extrudr_pla_planx2mattbluesteel_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-bluesteel_1000_175_p": "1E213D",
    "extrudr_pla_planx2mattbluesteel_1000_175_p": "033877"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-bluesteel_1000_175_p": 230,
    "extrudr_pla_planx2mattbluesteel_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-bluesteel_1000_175_p": null,
    "extrudr_pla_planx2mattbluesteel_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-bluesteel_1000_175_p": 60,
    "extrudr_pla_planx2mattbluesteel_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-bluesteel_1000_175_p": null,
    "extrudr_pla_planx2mattbluesteel_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-bluesteel_1000_175_p": "matte",
    "extrudr_pla_planx2mattbluesteel_1000_175_p": null
  }
}
```

### EX012: dup-79bf5a2d77f0ca64225b561eab9f05bcab3d081638101b1b0cbf4b175bd675e5

Status: APPROVED; survivor `extrudr_pla_nx2-matt-brown_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-brown_1000_175_p`|`NX2-MATT - {color_name}`|`Brown`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattbrown_1000_175_p`|`PLA NX2 Matt {color_name}`|`Brown`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-brown_1000_175_p": 1.3,
    "extrudr_pla_planx2mattbrown_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-brown_1000_175_p": 260.0,
    "extrudr_pla_planx2mattbrown_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-brown_1000_175_p": "59351F",
    "extrudr_pla_planx2mattbrown_1000_175_p": "A47C48"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-brown_1000_175_p": 230,
    "extrudr_pla_planx2mattbrown_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-brown_1000_175_p": null,
    "extrudr_pla_planx2mattbrown_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-brown_1000_175_p": 60,
    "extrudr_pla_planx2mattbrown_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-brown_1000_175_p": null,
    "extrudr_pla_planx2mattbrown_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-brown_1000_175_p": "matte",
    "extrudr_pla_planx2mattbrown_1000_175_p": null
  }
}
```

### EX013: dup-9219074096fe47ef09ea1301fc3bc629dcdbc2945c2bf3e03e22e265d6000138

Status: APPROVED; survivor `extrudr_pla_nx2-matt-emeraldgreen_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-emeraldgreen_1000_175_p`|`NX2-MATT - {color_name}`|`Emerald Green`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattemeraldgreen_1000_175_p`|`PLA NX2 Matt {color_name}`|`Emerald Green`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-emeraldgreen_1000_175_p": 1.3,
    "extrudr_pla_planx2mattemeraldgreen_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-emeraldgreen_1000_175_p": 260.0,
    "extrudr_pla_planx2mattemeraldgreen_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-emeraldgreen_1000_175_p": "287233",
    "extrudr_pla_planx2mattemeraldgreen_1000_175_p": "41A840"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-emeraldgreen_1000_175_p": 230,
    "extrudr_pla_planx2mattemeraldgreen_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-emeraldgreen_1000_175_p": null,
    "extrudr_pla_planx2mattemeraldgreen_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-emeraldgreen_1000_175_p": 60,
    "extrudr_pla_planx2mattemeraldgreen_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-emeraldgreen_1000_175_p": null,
    "extrudr_pla_planx2mattemeraldgreen_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-emeraldgreen_1000_175_p": "matte",
    "extrudr_pla_planx2mattemeraldgreen_1000_175_p": null
  }
}
```

### EX014: dup-2133052d5f2fa537240858ba144f6a73c1af6e9cd23d04bc04578490a7cbff92

Status: APPROVED; survivor `extrudr_pla_nx2-matt-epicpurple_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-epicpurple_1000_175_p`|`NX2-MATT - {color_name}`|`Epic Purple`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattepicpurple_1000_175_p`|`PLA NX2 Matt {color_name}`|`Epic Purple`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-epicpurple_1000_175_p": 1.3,
    "extrudr_pla_planx2mattepicpurple_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-epicpurple_1000_175_p": 260.0,
    "extrudr_pla_planx2mattepicpurple_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-epicpurple_1000_175_p": "4A192C",
    "extrudr_pla_planx2mattepicpurple_1000_175_p": "7142A3"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-epicpurple_1000_175_p": 230,
    "extrudr_pla_planx2mattepicpurple_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-epicpurple_1000_175_p": null,
    "extrudr_pla_planx2mattepicpurple_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-epicpurple_1000_175_p": 60,
    "extrudr_pla_planx2mattepicpurple_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-epicpurple_1000_175_p": null,
    "extrudr_pla_planx2mattepicpurple_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-epicpurple_1000_175_p": "matte",
    "extrudr_pla_planx2mattepicpurple_1000_175_p": null
  }
}
```

### EX015: dup-f0619328661144d989396651bf8c35f10564f34b0f7801f566cfb0b342dd72a8

Status: APPROVED; survivor `extrudr_pla_nx2-matt-grey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-grey_1000_175_p`|`NX2-MATT - {color_name}`|`Grey`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattgrey_1000_175_p`|`PLA NX2 Matt {color_name}`|`Grey`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-grey_1000_175_p": 1.3,
    "extrudr_pla_planx2mattgrey_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-grey_1000_175_p": 260.0,
    "extrudr_pla_planx2mattgrey_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-grey_1000_175_p": "CAC4B0",
    "extrudr_pla_planx2mattgrey_1000_175_p": "C5C5BF"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-grey_1000_175_p": 230,
    "extrudr_pla_planx2mattgrey_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-grey_1000_175_p": null,
    "extrudr_pla_planx2mattgrey_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-grey_1000_175_p": 60,
    "extrudr_pla_planx2mattgrey_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-grey_1000_175_p": null,
    "extrudr_pla_planx2mattgrey_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-grey_1000_175_p": "matte",
    "extrudr_pla_planx2mattgrey_1000_175_p": null
  }
}
```

### EX016: dup-ebdea006e9074aa0fdd44dc88ec555a1446e76354262e25ecc463f1d00c995d6

Status: APPROVED; survivor `extrudr_pla_nx2-matt-hellfirered_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-hellfirered_1000_175_p`|`NX2-MATT - {color_name}`|`Hellfire Red `|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2matthellfirered_1000_175_p`|`PLA NX2 Matt {color_name}`|`Hellfire Red`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-hellfirered_1000_175_p": 1.3,
    "extrudr_pla_planx2matthellfirered_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-hellfirered_1000_175_p": 260.0,
    "extrudr_pla_planx2matthellfirered_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-hellfirered_1000_175_p": "F80000",
    "extrudr_pla_planx2matthellfirered_1000_175_p": "000000"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-hellfirered_1000_175_p": 230,
    "extrudr_pla_planx2matthellfirered_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-hellfirered_1000_175_p": null,
    "extrudr_pla_planx2matthellfirered_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-hellfirered_1000_175_p": 60,
    "extrudr_pla_planx2matthellfirered_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-hellfirered_1000_175_p": null,
    "extrudr_pla_planx2matthellfirered_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-hellfirered_1000_175_p": "matte",
    "extrudr_pla_planx2matthellfirered_1000_175_p": null
  }
}
```

### EX017: dup-f51d19677ce6462eff749e53c0b531c417d15741ec38f8b6e15de96e62e0d969

Status: APPROVED; survivor `extrudr_pla_nx2-matt-lightblue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-lightblue_1000_175_p`|`NX2-MATT - {color_name}`|`Light Blue`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattlightblue_1000_175_p`|`PLA NX2 Matt {color_name}`|`Light Blue`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-lightblue_1000_175_p": 1.3,
    "extrudr_pla_planx2mattlightblue_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-lightblue_1000_175_p": 260.0,
    "extrudr_pla_planx2mattlightblue_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-lightblue_1000_175_p": "3B83BD",
    "extrudr_pla_planx2mattlightblue_1000_175_p": "0099E6"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-lightblue_1000_175_p": 230,
    "extrudr_pla_planx2mattlightblue_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-lightblue_1000_175_p": null,
    "extrudr_pla_planx2mattlightblue_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-lightblue_1000_175_p": 60,
    "extrudr_pla_planx2mattlightblue_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-lightblue_1000_175_p": null,
    "extrudr_pla_planx2mattlightblue_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-lightblue_1000_175_p": "matte",
    "extrudr_pla_planx2mattlightblue_1000_175_p": null
  }
}
```

### EX018: dup-82d1065d659063e54c0b6e8df5f1dbe09f4567f1cee4cc31d1c49aaa354ecbd6

Status: APPROVED; survivor `extrudr_pla_nx2-matt-metallicgrey_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-metallicgrey_1000_175_p`|`NX2-MATT - {color_name}`|`Metallic Grey`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattmetallicgrey_1000_175_p`|`PLA NX2 Matt {color_name}`|`Metallic Grey`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-metallicgrey_1000_175_p": 1.3,
    "extrudr_pla_planx2mattmetallicgrey_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-metallicgrey_1000_175_p": 260.0,
    "extrudr_pla_planx2mattmetallicgrey_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-metallicgrey_1000_175_p": "828282",
    "extrudr_pla_planx2mattmetallicgrey_1000_175_p": "6A6C6E"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-metallicgrey_1000_175_p": 230,
    "extrudr_pla_planx2mattmetallicgrey_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-metallicgrey_1000_175_p": null,
    "extrudr_pla_planx2mattmetallicgrey_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-metallicgrey_1000_175_p": 60,
    "extrudr_pla_planx2mattmetallicgrey_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-metallicgrey_1000_175_p": null,
    "extrudr_pla_planx2mattmetallicgrey_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-metallicgrey_1000_175_p": "matte",
    "extrudr_pla_planx2mattmetallicgrey_1000_175_p": null
  }
}
```

### EX019: dup-d468e7db07d39657a3ae5208d83742088127f868fd7606c05e22ca8ec5376e3b

Status: APPROVED; survivor `extrudr_pla_nx2-matt-militarybeige_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-militarybeige_1000_175_p`|`NX2-MATT - {color_name}`|`Military Beige`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattmilitarybeige_1000_175_p`|`PLA NX2 Matt {color_name}`|`Military Beige`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-militarybeige_1000_175_p": 1.3,
    "extrudr_pla_planx2mattmilitarybeige_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-militarybeige_1000_175_p": 260.0,
    "extrudr_pla_planx2mattmilitarybeige_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-militarybeige_1000_175_p": "C2B078",
    "extrudr_pla_planx2mattmilitarybeige_1000_175_p": "D4B6A3"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-militarybeige_1000_175_p": 230,
    "extrudr_pla_planx2mattmilitarybeige_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-militarybeige_1000_175_p": null,
    "extrudr_pla_planx2mattmilitarybeige_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-militarybeige_1000_175_p": 60,
    "extrudr_pla_planx2mattmilitarybeige_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-militarybeige_1000_175_p": null,
    "extrudr_pla_planx2mattmilitarybeige_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-militarybeige_1000_175_p": "matte",
    "extrudr_pla_planx2mattmilitarybeige_1000_175_p": null
  }
}
```

### EX020: dup-a516cea111cff939247501ff7b437ec336d222c1b6986ed83915994341bedbf2

Status: APPROVED; survivor `extrudr_pla_nx2-matt-militarygreen_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-militarygreen_1000_175_p`|`NX2-MATT - {color_name}`|`Military Green`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattmilitarygreen_1000_175_p`|`PLA NX2 Matt {color_name}`|`Military Green`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-militarygreen_1000_175_p": 1.3,
    "extrudr_pla_planx2mattmilitarygreen_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-militarygreen_1000_175_p": 260.0,
    "extrudr_pla_planx2mattmilitarygreen_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-militarygreen_1000_175_p": "424632",
    "extrudr_pla_planx2mattmilitarygreen_1000_175_p": "4C645B"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-militarygreen_1000_175_p": 230,
    "extrudr_pla_planx2mattmilitarygreen_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-militarygreen_1000_175_p": null,
    "extrudr_pla_planx2mattmilitarygreen_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-militarygreen_1000_175_p": 60,
    "extrudr_pla_planx2mattmilitarygreen_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-militarygreen_1000_175_p": null,
    "extrudr_pla_planx2mattmilitarygreen_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-militarygreen_1000_175_p": "matte",
    "extrudr_pla_planx2mattmilitarygreen_1000_175_p": null
  }
}
```

### EX021: dup-13cbb683c5535b20e58e0f764829a1ebf6d7a2016c87be578b71ad282eb23671

Status: APPROVED; survivor `extrudr_pla_nx2-matt-navyblue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-navyblue_1000_175_p`|`NX2-MATT - {color_name}`|`Navy Blue`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattnavyblue_1000_175_p`|`PLA NX2 Matt {color_name}`|`Navy Blue`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-navyblue_1000_175_p": 1.3,
    "extrudr_pla_planx2mattnavyblue_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-navyblue_1000_175_p": 260.0,
    "extrudr_pla_planx2mattnavyblue_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-navyblue_1000_175_p": "1D1E33",
    "extrudr_pla_planx2mattnavyblue_1000_175_p": "2E56F1"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-navyblue_1000_175_p": 230,
    "extrudr_pla_planx2mattnavyblue_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-navyblue_1000_175_p": null,
    "extrudr_pla_planx2mattnavyblue_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-navyblue_1000_175_p": 60,
    "extrudr_pla_planx2mattnavyblue_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-navyblue_1000_175_p": null,
    "extrudr_pla_planx2mattnavyblue_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-navyblue_1000_175_p": "matte",
    "extrudr_pla_planx2mattnavyblue_1000_175_p": null
  }
}
```

### EX022: dup-09bb474fb8dd17bed035a54828589da49d5abedd240080299648b59430a27e2f

Status: APPROVED; survivor `extrudr_pla_nx2-matt-neonorange_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-neonorange_1000_175_p`|`NX2-MATT - {color_name}`|`Neon Orange`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattneonorange_1000_175_p`|`PLA NX2 Matt {color_name}`|`Neon Orange`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-neonorange_1000_175_p": 1.3,
    "extrudr_pla_planx2mattneonorange_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-neonorange_1000_175_p": 260.0,
    "extrudr_pla_planx2mattneonorange_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-neonorange_1000_175_p": "FF2301",
    "extrudr_pla_planx2mattneonorange_1000_175_p": "F67405"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-neonorange_1000_175_p": 230,
    "extrudr_pla_planx2mattneonorange_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-neonorange_1000_175_p": null,
    "extrudr_pla_planx2mattneonorange_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-neonorange_1000_175_p": 60,
    "extrudr_pla_planx2mattneonorange_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-neonorange_1000_175_p": null,
    "extrudr_pla_planx2mattneonorange_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-neonorange_1000_175_p": "matte",
    "extrudr_pla_planx2mattneonorange_1000_175_p": null
  }
}
```

### EX023: dup-6ba12c193863f4d2a2c42c47a2dac2e2abf93a47db8837ee1cc0ee9a4b04d22c

Status: APPROVED; survivor `extrudr_pla_nx2-matt-orange_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-orange_1000_175_p`|`NX2-MATT - {color_name}`|`Orange`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattorange_1000_175_p`|`PLA NX2 Matt {color_name}`|`Orange`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-orange_1000_175_p": 1.3,
    "extrudr_pla_planx2mattorange_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-orange_1000_175_p": 260.0,
    "extrudr_pla_planx2mattorange_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-orange_1000_175_p": "F54021",
    "extrudr_pla_planx2mattorange_1000_175_p": "FF9A14"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-orange_1000_175_p": 230,
    "extrudr_pla_planx2mattorange_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-orange_1000_175_p": null,
    "extrudr_pla_planx2mattorange_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-orange_1000_175_p": 60,
    "extrudr_pla_planx2mattorange_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-orange_1000_175_p": null,
    "extrudr_pla_planx2mattorange_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-orange_1000_175_p": "matte",
    "extrudr_pla_planx2mattorange_1000_175_p": null
  }
}
```

### EX024: dup-40224f817761a31688311c4f7039b3bc9e63be556422a7371372493c06b6d043

Status: APPROVED; survivor `extrudr_pla_nx2-matt-purple_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-purple_1000_175_p`|`NX2-MATT - {color_name}`|`Purple`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattpurple_1000_175_p`|`PLA NX2 Matt {color_name}`|`Purple`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-purple_1000_175_p": 1.3,
    "extrudr_pla_planx2mattpurple_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-purple_1000_175_p": 260.0,
    "extrudr_pla_planx2mattpurple_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-purple_1000_175_p": "924E7D",
    "extrudr_pla_planx2mattpurple_1000_175_p": "C63DBA"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-purple_1000_175_p": 230,
    "extrudr_pla_planx2mattpurple_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-purple_1000_175_p": null,
    "extrudr_pla_planx2mattpurple_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-purple_1000_175_p": 60,
    "extrudr_pla_planx2mattpurple_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-purple_1000_175_p": null,
    "extrudr_pla_planx2mattpurple_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-purple_1000_175_p": "matte",
    "extrudr_pla_planx2mattpurple_1000_175_p": null
  }
}
```

### EX025: dup-07d8db56d31c9bc9264284bd28ca709fc8a46a5dfcd15015555c918cdf39a329

Status: APPROVED; survivor `extrudr_pla_nx2-matt-signalgreen_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-signalgreen_1000_175_p`|`NX2-MATT - {color_name}`|`Signal Green`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattsignalgreen_1000_175_p`|`PLA NX2 Matt {color_name}`|`Signal Green`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-signalgreen_1000_175_p": 1.3,
    "extrudr_pla_planx2mattsignalgreen_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-signalgreen_1000_175_p": 260.0,
    "extrudr_pla_planx2mattsignalgreen_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-signalgreen_1000_175_p": "008F39",
    "extrudr_pla_planx2mattsignalgreen_1000_175_p": "7CEF83"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-signalgreen_1000_175_p": 230,
    "extrudr_pla_planx2mattsignalgreen_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-signalgreen_1000_175_p": null,
    "extrudr_pla_planx2mattsignalgreen_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-signalgreen_1000_175_p": 60,
    "extrudr_pla_planx2mattsignalgreen_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-signalgreen_1000_175_p": null,
    "extrudr_pla_planx2mattsignalgreen_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-signalgreen_1000_175_p": "matte",
    "extrudr_pla_planx2mattsignalgreen_1000_175_p": null
  }
}
```

### EX026: dup-dfcdd6aa320eb50fa418d11e2d664ed77a7f5f551b83d4a6ea6170cf09344681

Status: APPROVED; survivor `extrudr_pla_nx2-matt-silver_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-silver_1000_175_p`|`NX2-MATT - {color_name}`|`Silver`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattsilver_1000_175_p`|`PLA NX2 Matt {color_name}`|`Silver`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-silver_1000_175_p": 1.3,
    "extrudr_pla_planx2mattsilver_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-silver_1000_175_p": 260.0,
    "extrudr_pla_planx2mattsilver_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-silver_1000_175_p": "A5A5A5",
    "extrudr_pla_planx2mattsilver_1000_175_p": "A8B0BD"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-silver_1000_175_p": 230,
    "extrudr_pla_planx2mattsilver_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-silver_1000_175_p": null,
    "extrudr_pla_planx2mattsilver_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-silver_1000_175_p": 60,
    "extrudr_pla_planx2mattsilver_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-silver_1000_175_p": null,
    "extrudr_pla_planx2mattsilver_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-silver_1000_175_p": "matte",
    "extrudr_pla_planx2mattsilver_1000_175_p": null
  }
}
```

### EX027: dup-8a5fb67d209983c4982a1643f61c379c3021a62879f9df46f157be9a7e21b2ec

Status: APPROVED; survivor `extrudr_pla_nx2-matt-turquoise_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-turquoise_1000_175_p`|`NX2-MATT - {color_name}`|`Turquoise`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattturquoise_1000_175_p`|`PLA NX2 Matt {color_name}`|`Turquoise`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-turquoise_1000_175_p": 1.3,
    "extrudr_pla_planx2mattturquoise_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-turquoise_1000_175_p": 260.0,
    "extrudr_pla_planx2mattturquoise_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-turquoise_1000_175_p": "3F888F",
    "extrudr_pla_planx2mattturquoise_1000_175_p": "6AC4CD"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-turquoise_1000_175_p": 230,
    "extrudr_pla_planx2mattturquoise_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-turquoise_1000_175_p": null,
    "extrudr_pla_planx2mattturquoise_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-turquoise_1000_175_p": 60,
    "extrudr_pla_planx2mattturquoise_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-turquoise_1000_175_p": null,
    "extrudr_pla_planx2mattturquoise_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-turquoise_1000_175_p": "matte",
    "extrudr_pla_planx2mattturquoise_1000_175_p": null
  }
}
```

### EX028: dup-2d071c1a2fee6033dfd51284367bcf0b842f6d505b602088cfb6e930f3c44d7d

Status: APPROVED; survivor `extrudr_pla_nx2-matt-white_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-white_1000_175_p`|`NX2-MATT - {color_name}`|`White`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattwhite_1000_175_p`|`PLA NX2 Matt {color_name}`|`White`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-white_1000_175_p": 1.3,
    "extrudr_pla_planx2mattwhite_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-white_1000_175_p": 260.0,
    "extrudr_pla_planx2mattwhite_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-white_1000_175_p": "F4F4F4",
    "extrudr_pla_planx2mattwhite_1000_175_p": "FFFFFF"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-white_1000_175_p": 230,
    "extrudr_pla_planx2mattwhite_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-white_1000_175_p": null,
    "extrudr_pla_planx2mattwhite_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-white_1000_175_p": 60,
    "extrudr_pla_planx2mattwhite_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-white_1000_175_p": null,
    "extrudr_pla_planx2mattwhite_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-white_1000_175_p": "matte",
    "extrudr_pla_planx2mattwhite_1000_175_p": null
  }
}
```

### EX029: dup-74c06c74712dff62dccc9e5e3e23eb873065a03bfc408e427369f1bcc5ae7b47

Status: APPROVED; survivor `extrudr_pla_nx2-matt-yellow_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`extrudr_pla_nx2-matt-yellow_1000_175_p`|`NX2-MATT - {color_name}`|`Yellow`|{"source_file": "extrudr.json", "definition_index": 17, "weights": 4, "diameters": 2, "colors": 22, "compiled_records": 176} / True|
|`extrudr_pla_planx2mattyellow_1000_175_p`|`PLA NX2 Matt {color_name}`|`Yellow`|{"source_file": "extrudr.json", "definition_index": 43, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "extrudr_pla_nx2-matt-yellow_1000_175_p": 1.3,
    "extrudr_pla_planx2mattyellow_1000_175_p": 1.24
  },
  "spool_weight": {
    "extrudr_pla_nx2-matt-yellow_1000_175_p": 260.0,
    "extrudr_pla_planx2mattyellow_1000_175_p": 250
  },
  "color_hex": {
    "extrudr_pla_nx2-matt-yellow_1000_175_p": "FAD201",
    "extrudr_pla_planx2mattyellow_1000_175_p": "E4FF33"
  },
  "extruder_temp": {
    "extrudr_pla_nx2-matt-yellow_1000_175_p": 230,
    "extrudr_pla_planx2mattyellow_1000_175_p": null
  },
  "extruder_temp_range": {
    "extrudr_pla_nx2-matt-yellow_1000_175_p": null,
    "extrudr_pla_planx2mattyellow_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "extrudr_pla_nx2-matt-yellow_1000_175_p": 60,
    "extrudr_pla_planx2mattyellow_1000_175_p": null
  },
  "bed_temp_range": {
    "extrudr_pla_nx2-matt-yellow_1000_175_p": null,
    "extrudr_pla_planx2mattyellow_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "extrudr_pla_nx2-matt-yellow_1000_175_p": "matte",
    "extrudr_pla_planx2mattyellow_1000_175_p": null
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "extrudr_pla_basic-cmyklithocyan_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          20,
          60
        ]
      },
      "source": "https://s3.extrudr.com/extrudr-media/datasheets/tds/tds-en/pla-basic-TDS-en.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "extrudr_pla_basic-white_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          20,
          60
        ]
      },
      "source": "https://s3.extrudr.com/extrudr-media/datasheets/tds/tds-en/pla-basic-TDS-en.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "extrudr_pla_basic-gold_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          20,
          60
        ]
      },
      "source": "https://s3.extrudr.com/extrudr-media/datasheets/tds/tds-en/pla-basic-TDS-en.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "extrudr_pla_basic-transparent_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          20,
          60
        ]
      },
      "source": "https://s3.extrudr.com/extrudr-media/datasheets/tds/tds-en/pla-basic-TDS-en.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "extrudr_pla_basic-cmyklithomagenta_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          20,
          60
        ]
      },
      "source": "https://s3.extrudr.com/extrudr-media/datasheets/tds/tds-en/pla-basic-TDS-en.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "extrudr_pla_basic-black_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          20,
          60
        ]
      },
      "source": "https://s3.extrudr.com/extrudr-media/datasheets/tds/tds-en/pla-basic-TDS-en.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "extrudr_pla_basic-cmyklithowhite_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          20,
          60
        ]
      },
      "source": "https://s3.extrudr.com/extrudr-media/datasheets/tds/tds-en/pla-basic-TDS-en.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "extrudr_pla_basic-cmyklithoyellow_1000_175_p",
      "values": {
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          20,
          60
        ]
      },
      "source": "https://s3.extrudr.com/extrudr-media/datasheets/tds/tds-en/pla-basic-TDS-en.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    }
  ],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `extrudr_biofusion_arcticwhite_800_175_p` — Arctic White
- `extrudr_biofusion_jetblack_800_175_p` — Jet Black 
- `extrudr_biofusion_metallicgrey_800_175_p` — Metallic Grey
- `extrudr_biofusion_quicksilver_800_175_p` — Quicksilver
- `extrudr_biofusion_reptilegreen_800_175_p` — Reptile Green
- `extrudr_biofusion_venomgreen_800_175_p` — Venom Green
- `extrudr_biofusion_bluefire_800_175_p` — Blue Fire
- `extrudr_biofusion_epicpurple_800_175_p` — Epic Purple
- `extrudr_biofusion_cherryred_800_175_p` — Cherry Red
- `extrudr_biofusion_steampunkcopper_800_175_p` — Steampunk Copper
- `extrudr_biofusion_incagold_800_175_p` — Inca Gold
- `extrudr_biofusion_arcticwhite_800_285_p` — Arctic White
- `extrudr_biofusion_jetblack_800_285_p` — Jet Black 
- `extrudr_biofusion_metallicgrey_800_285_p` — Metallic Grey
- `extrudr_biofusion_quicksilver_800_285_p` — Quicksilver
- `extrudr_biofusion_reptilegreen_800_285_p` — Reptile Green
- `extrudr_biofusion_venomgreen_800_285_p` — Venom Green
- `extrudr_biofusion_bluefire_800_285_p` — Blue Fire
- `extrudr_biofusion_epicpurple_800_285_p` — Epic Purple
- `extrudr_biofusion_cherryred_800_285_p` — Cherry Red
- `extrudr_biofusion_steampunkcopper_800_285_p` — Steampunk Copper
- `extrudr_biofusion_incagold_800_285_p` — Inca Gold
- `extrudr_abs_durapro-white_750_175_p` — DuraPro - White
- `extrudr_abs_durapro-black_750_175_p` — DuraPro - Black 
- `extrudr_abs_durapro-anthracite_750_175_p` — DuraPro - Anthracite
- `extrudr_abs_durapro-metallic_750_175_p` — DuraPro - Metallic
- `extrudr_abs_durapro-silver_750_175_p` — DuraPro - Silver
- `extrudr_abs_durapro-grey_750_175_p` — DuraPro - Grey
- `extrudr_abs_durapro-blue_750_175_p` — DuraPro - Blue
- `extrudr_abs_durapro-red_750_175_p` — DuraPro - Red
- `extrudr_abs_durapro-nature_750_175_p` — DuraPro - Nature
- `extrudr_abs_durapro-white_750_285_p` — DuraPro - White
- `extrudr_abs_durapro-black_750_285_p` — DuraPro - Black 
- `extrudr_abs_durapro-anthracite_750_285_p` — DuraPro - Anthracite
- `extrudr_abs_durapro-metallic_750_285_p` — DuraPro - Metallic
- `extrudr_abs_durapro-silver_750_285_p` — DuraPro - Silver
- `extrudr_abs_durapro-grey_750_285_p` — DuraPro - Grey
- `extrudr_abs_durapro-blue_750_285_p` — DuraPro - Blue
- `extrudr_abs_durapro-red_750_285_p` — DuraPro - Red
- `extrudr_abs_durapro-nature_750_285_p` — DuraPro - Nature
- `extrudr_abs_durapro-white_2000_175_p` — DuraPro - White
- `extrudr_abs_durapro-black_2000_175_p` — DuraPro - Black 
- `extrudr_abs_durapro-anthracite_2000_175_p` — DuraPro - Anthracite
- `extrudr_abs_durapro-metallic_2000_175_p` — DuraPro - Metallic
- `extrudr_abs_durapro-silver_2000_175_p` — DuraPro - Silver
- `extrudr_abs_durapro-grey_2000_175_p` — DuraPro - Grey
- `extrudr_abs_durapro-blue_2000_175_p` — DuraPro - Blue
- `extrudr_abs_durapro-red_2000_175_p` — DuraPro - Red
- `extrudr_abs_durapro-nature_2000_175_p` — DuraPro - Nature
- `extrudr_abs_durapro-white_2000_285_p` — DuraPro - White
- `extrudr_abs_durapro-black_2000_285_p` — DuraPro - Black 
- `extrudr_abs_durapro-anthracite_2000_285_p` — DuraPro - Anthracite
- `extrudr_abs_durapro-metallic_2000_285_p` — DuraPro - Metallic
- `extrudr_abs_durapro-silver_2000_285_p` — DuraPro - Silver
- `extrudr_abs_durapro-grey_2000_285_p` — DuraPro - Grey
- `extrudr_abs_durapro-blue_2000_285_p` — DuraPro - Blue
- `extrudr_abs_durapro-red_2000_285_p` — DuraPro - Red
- `extrudr_abs_durapro-nature_2000_285_p` — DuraPro - Nature
- `extrudr_abs_durapro-white_10000_175_p` — DuraPro - White
- `extrudr_abs_durapro-black_10000_175_p` — DuraPro - Black 
- `extrudr_abs_durapro-anthracite_10000_175_p` — DuraPro - Anthracite
- `extrudr_abs_durapro-metallic_10000_175_p` — DuraPro - Metallic
- `extrudr_abs_durapro-silver_10000_175_p` — DuraPro - Silver
- `extrudr_abs_durapro-grey_10000_175_p` — DuraPro - Grey
- `extrudr_abs_durapro-blue_10000_175_p` — DuraPro - Blue
- `extrudr_abs_durapro-red_10000_175_p` — DuraPro - Red
- `extrudr_abs_durapro-nature_10000_175_p` — DuraPro - Nature
- `extrudr_abs_durapro-white_10000_285_p` — DuraPro - White
- `extrudr_abs_durapro-black_10000_285_p` — DuraPro - Black 
- `extrudr_abs_durapro-anthracite_10000_285_p` — DuraPro - Anthracite
- `extrudr_abs_durapro-metallic_10000_285_p` — DuraPro - Metallic
- `extrudr_abs_durapro-silver_10000_285_p` — DuraPro - Silver
- `extrudr_abs_durapro-grey_10000_285_p` — DuraPro - Grey
- `extrudr_abs_durapro-blue_10000_285_p` — DuraPro - Blue
- `extrudr_abs_durapro-red_10000_285_p` — DuraPro - Red
- `extrudr_abs_durapro-nature_10000_285_p` — DuraPro - Nature
- `extrudr_asa_durapro-black_750_175_p` — DuraPro - Black 
- `extrudr_asa_durapro-anthracite_750_175_p` — DuraPro - Anthracite
- `extrudr_asa_durapro-metallic_750_175_p` — DuraPro - Metallic
- `extrudr_asa_durapro-darksilver_750_175_p` — DuraPro - Dark Silver
- `extrudr_asa_durapro-grey_750_175_p` — DuraPro - Grey
- `extrudr_asa_durapro-emeraldgreen_750_175_p` — DuraPro - Emerald Green
- `extrudr_asa_durapro-neongreen_750_175_p` — DuraPro - Neon Green
- `extrudr_asa_durapro-blue_750_175_p` — DuraPro - Blue
- `extrudr_asa_durapro-red_750_175_p` — DuraPro - Red
- `extrudr_asa_durapro-neonorange_750_175_p` — DuraPro - Neon Orange
- `extrudr_asa_durapro-yellow_750_175_p` — DuraPro - Yellow
- `extrudr_asa_durapro-neonyellow_750_175_p` — DuraPro - Neon Yellow
- `extrudr_asa_durapro-nature_750_175_p` — DuraPro - Nature
- `extrudr_asa_durapro-white_750_175_p` — DuraPro - White
- `extrudr_asa_durapro-orange_750_175_p` — DuraPro - Orange
- `extrudr_asa_durapro-black_750_285_p` — DuraPro - Black 
- `extrudr_asa_durapro-anthracite_750_285_p` — DuraPro - Anthracite
- `extrudr_asa_durapro-metallic_750_285_p` — DuraPro - Metallic
- `extrudr_asa_durapro-darksilver_750_285_p` — DuraPro - Dark Silver
- `extrudr_asa_durapro-grey_750_285_p` — DuraPro - Grey
- `extrudr_asa_durapro-emeraldgreen_750_285_p` — DuraPro - Emerald Green
- `extrudr_asa_durapro-neongreen_750_285_p` — DuraPro - Neon Green
- `extrudr_asa_durapro-blue_750_285_p` — DuraPro - Blue
- `extrudr_asa_durapro-red_750_285_p` — DuraPro - Red
- `extrudr_asa_durapro-neonorange_750_285_p` — DuraPro - Neon Orange
- `extrudr_asa_durapro-yellow_750_285_p` — DuraPro - Yellow
- `extrudr_asa_durapro-neonyellow_750_285_p` — DuraPro - Neon Yellow
- `extrudr_asa_durapro-nature_750_285_p` — DuraPro - Nature
- `extrudr_asa_durapro-white_750_285_p` — DuraPro - White
- `extrudr_asa_durapro-orange_750_285_p` — DuraPro - Orange
- `extrudr_asa_durapro-black_2000_175_p` — DuraPro - Black 
- `extrudr_asa_durapro-anthracite_2000_175_p` — DuraPro - Anthracite
- `extrudr_asa_durapro-metallic_2000_175_p` — DuraPro - Metallic
- `extrudr_asa_durapro-darksilver_2000_175_p` — DuraPro - Dark Silver
- `extrudr_asa_durapro-grey_2000_175_p` — DuraPro - Grey
- `extrudr_asa_durapro-emeraldgreen_2000_175_p` — DuraPro - Emerald Green
- `extrudr_asa_durapro-neongreen_2000_175_p` — DuraPro - Neon Green
- `extrudr_asa_durapro-blue_2000_175_p` — DuraPro - Blue
- `extrudr_asa_durapro-red_2000_175_p` — DuraPro - Red
- `extrudr_asa_durapro-neonorange_2000_175_p` — DuraPro - Neon Orange
- `extrudr_asa_durapro-yellow_2000_175_p` — DuraPro - Yellow
- `extrudr_asa_durapro-neonyellow_2000_175_p` — DuraPro - Neon Yellow
- `extrudr_asa_durapro-nature_2000_175_p` — DuraPro - Nature
- `extrudr_asa_durapro-white_2000_175_p` — DuraPro - White
- `extrudr_asa_durapro-orange_2000_175_p` — DuraPro - Orange
- `extrudr_asa_durapro-black_2000_285_p` — DuraPro - Black 
- `extrudr_asa_durapro-anthracite_2000_285_p` — DuraPro - Anthracite
- `extrudr_asa_durapro-metallic_2000_285_p` — DuraPro - Metallic
- `extrudr_asa_durapro-darksilver_2000_285_p` — DuraPro - Dark Silver
- `extrudr_asa_durapro-grey_2000_285_p` — DuraPro - Grey
- `extrudr_asa_durapro-emeraldgreen_2000_285_p` — DuraPro - Emerald Green
- `extrudr_asa_durapro-neongreen_2000_285_p` — DuraPro - Neon Green
- `extrudr_asa_durapro-blue_2000_285_p` — DuraPro - Blue
- `extrudr_asa_durapro-red_2000_285_p` — DuraPro - Red
- `extrudr_asa_durapro-neonorange_2000_285_p` — DuraPro - Neon Orange
- `extrudr_asa_durapro-yellow_2000_285_p` — DuraPro - Yellow
- `extrudr_asa_durapro-neonyellow_2000_285_p` — DuraPro - Neon Yellow
- `extrudr_asa_durapro-nature_2000_285_p` — DuraPro - Nature
- `extrudr_asa_durapro-white_2000_285_p` — DuraPro - White
- `extrudr_asa_durapro-orange_2000_285_p` — DuraPro - Orange
- `extrudr_asa_durapro-black_5000_175_p` — DuraPro - Black 
- `extrudr_asa_durapro-anthracite_5000_175_p` — DuraPro - Anthracite
- `extrudr_asa_durapro-metallic_5000_175_p` — DuraPro - Metallic
- `extrudr_asa_durapro-darksilver_5000_175_p` — DuraPro - Dark Silver
- `extrudr_asa_durapro-grey_5000_175_p` — DuraPro - Grey
- `extrudr_asa_durapro-emeraldgreen_5000_175_p` — DuraPro - Emerald Green
- `extrudr_asa_durapro-neongreen_5000_175_p` — DuraPro - Neon Green
- `extrudr_asa_durapro-blue_5000_175_p` — DuraPro - Blue
- `extrudr_asa_durapro-red_5000_175_p` — DuraPro - Red
- `extrudr_asa_durapro-neonorange_5000_175_p` — DuraPro - Neon Orange
- `extrudr_asa_durapro-yellow_5000_175_p` — DuraPro - Yellow
- `extrudr_asa_durapro-neonyellow_5000_175_p` — DuraPro - Neon Yellow
- `extrudr_asa_durapro-nature_5000_175_p` — DuraPro - Nature
- `extrudr_asa_durapro-white_5000_175_p` — DuraPro - White
- `extrudr_asa_durapro-orange_5000_175_p` — DuraPro - Orange
- `extrudr_asa_durapro-black_5000_285_p` — DuraPro - Black 
- `extrudr_asa_durapro-anthracite_5000_285_p` — DuraPro - Anthracite
- `extrudr_asa_durapro-metallic_5000_285_p` — DuraPro - Metallic
- `extrudr_asa_durapro-darksilver_5000_285_p` — DuraPro - Dark Silver
- `extrudr_asa_durapro-grey_5000_285_p` — DuraPro - Grey
- `extrudr_asa_durapro-emeraldgreen_5000_285_p` — DuraPro - Emerald Green
- `extrudr_asa_durapro-neongreen_5000_285_p` — DuraPro - Neon Green
- `extrudr_asa_durapro-blue_5000_285_p` — DuraPro - Blue
- `extrudr_asa_durapro-red_5000_285_p` — DuraPro - Red
- `extrudr_asa_durapro-neonorange_5000_285_p` — DuraPro - Neon Orange
- `extrudr_asa_durapro-yellow_5000_285_p` — DuraPro - Yellow
- `extrudr_asa_durapro-neonyellow_5000_285_p` — DuraPro - Neon Yellow
- `extrudr_asa_durapro-nature_5000_285_p` — DuraPro - Nature
- `extrudr_asa_durapro-white_5000_285_p` — DuraPro - White
- `extrudr_asa_durapro-orange_5000_285_p` — DuraPro - Orange
- `extrudr_asa_durapro-black_10000_175_p` — DuraPro - Black 
- `extrudr_asa_durapro-anthracite_10000_175_p` — DuraPro - Anthracite
- `extrudr_asa_durapro-metallic_10000_175_p` — DuraPro - Metallic
- `extrudr_asa_durapro-darksilver_10000_175_p` — DuraPro - Dark Silver
- `extrudr_asa_durapro-grey_10000_175_p` — DuraPro - Grey
- `extrudr_asa_durapro-emeraldgreen_10000_175_p` — DuraPro - Emerald Green
- `extrudr_asa_durapro-neongreen_10000_175_p` — DuraPro - Neon Green
- `extrudr_asa_durapro-blue_10000_175_p` — DuraPro - Blue
- `extrudr_asa_durapro-red_10000_175_p` — DuraPro - Red
- `extrudr_asa_durapro-neonorange_10000_175_p` — DuraPro - Neon Orange
- `extrudr_asa_durapro-yellow_10000_175_p` — DuraPro - Yellow
- `extrudr_asa_durapro-neonyellow_10000_175_p` — DuraPro - Neon Yellow
- `extrudr_asa_durapro-nature_10000_175_p` — DuraPro - Nature
- `extrudr_asa_durapro-white_10000_175_p` — DuraPro - White
- `extrudr_asa_durapro-orange_10000_175_p` — DuraPro - Orange
- `extrudr_asa_durapro-black_10000_285_p` — DuraPro - Black 
- `extrudr_asa_durapro-anthracite_10000_285_p` — DuraPro - Anthracite
- `extrudr_asa_durapro-metallic_10000_285_p` — DuraPro - Metallic
- `extrudr_asa_durapro-darksilver_10000_285_p` — DuraPro - Dark Silver
- `extrudr_asa_durapro-grey_10000_285_p` — DuraPro - Grey
- `extrudr_asa_durapro-emeraldgreen_10000_285_p` — DuraPro - Emerald Green
- `extrudr_asa_durapro-neongreen_10000_285_p` — DuraPro - Neon Green
- `extrudr_asa_durapro-blue_10000_285_p` — DuraPro - Blue
- `extrudr_asa_durapro-red_10000_285_p` — DuraPro - Red
- `extrudr_asa_durapro-neonorange_10000_285_p` — DuraPro - Neon Orange
- `extrudr_asa_durapro-yellow_10000_285_p` — DuraPro - Yellow
- `extrudr_asa_durapro-neonyellow_10000_285_p` — DuraPro - Neon Yellow
- `extrudr_asa_durapro-nature_10000_285_p` — DuraPro - Nature
- `extrudr_asa_durapro-white_10000_285_p` — DuraPro - White
- `extrudr_asa_durapro-orange_10000_285_p` — DuraPro - Orange
- `extrudr_asa-cf_durapro-black_750_175_p` — DuraPro - Black
- `extrudr_asa-cf_durapro-black_2000_175_p` — DuraPro - Black
- `extrudr_asa-gf_durapro-nature_750_175_p` — DuraPro - Nature
- `extrudr_pa12_durapro-black_750_175_p` — DuraPro - Black
- `extrudr_pa12_durapro-black_2000_175_p` — DuraPro - Black
- `extrudr_pa12-cf_durapro-black_500_175_p` — DuraPro - Black
- `extrudr_pa12-cf_durapro-black_2000_175_p` — DuraPro - Black
- `extrudr_pcpbt_durapro-white_750_175_p` — DuraPro - White
- `extrudr_pcpbt_durapro-black_750_175_p` — DuraPro - Black
- `extrudr_pcpbt_durapro-white_2000_175_p` — DuraPro - White
- `extrudr_pcpbt_durapro-black_2000_175_p` — DuraPro - Black
- `extrudr_pcpbt-cf_durapro-black_700_175_p` — DuraPro - Black
- `extrudr_pctg_transparent_800_175_p` — Transparent
- `extrudr_pctg_anthracite_800_175_p` — Anthracite
- `extrudr_pctg_metallic_800_175_p` — Metallic
- `extrudr_pctg_silver_800_175_p` — Silver
- `extrudr_pctg_navyblue_800_175_p` — Navy Blue
- `extrudr_pctg_white_800_175_p` — White
- `extrudr_pctg_black_800_175_p` — Black
- `extrudr_pctg_red_800_175_p` — Red
- `extrudr_pctg_transparent_2500_175_p` — Transparent
- `extrudr_pctg_anthracite_2500_175_p` — Anthracite
- `extrudr_pctg_metallic_2500_175_p` — Metallic
- `extrudr_pctg_silver_2500_175_p` — Silver
- `extrudr_pctg_navyblue_2500_175_p` — Navy Blue
- `extrudr_pctg_white_2500_175_p` — White
- `extrudr_pctg_black_2500_175_p` — Black
- `extrudr_pctg_red_2500_175_p` — Red
- `extrudr_flax_nature_1100_175_p` — Nature
- `extrudr_flax_nature_1100_285_p` — Nature
- `extrudr_flax_nature_2500_175_p` — Nature
- `extrudr_flax_nature_2500_285_p` — Nature
- `extrudr_flax_nature_10000_175_p` — Nature
- `extrudr_flax_nature_10000_285_p` — Nature
- `extrudr_greentec_white_1100_175_p` — White
- `extrudr_greentec_black_1100_175_p` — Black 
- `extrudr_greentec_anthracite_1100_175_p` — Anthracite
- `extrudr_greentec_silver_1100_175_p` — Silver
- `extrudr_greentec_navyblue_1100_175_p` — Navy Blue
- `extrudr_greentec_red_1100_175_p` — Red
- `extrudr_greentec_nature_1100_175_p` — Nature
- `extrudr_greentec_white_1100_285_p` — White
- `extrudr_greentec_black_1100_285_p` — Black 
- `extrudr_greentec_anthracite_1100_285_p` — Anthracite
- `extrudr_greentec_silver_1100_285_p` — Silver
- `extrudr_greentec_navyblue_1100_285_p` — Navy Blue
- `extrudr_greentec_red_1100_285_p` — Red
- `extrudr_greentec_nature_1100_285_p` — Nature
- `extrudr_greentec_white_2500_175_p` — White
- `extrudr_greentec_black_2500_175_p` — Black 
- `extrudr_greentec_anthracite_2500_175_p` — Anthracite
- `extrudr_greentec_silver_2500_175_p` — Silver
- `extrudr_greentec_navyblue_2500_175_p` — Navy Blue
- `extrudr_greentec_red_2500_175_p` — Red
- `extrudr_greentec_nature_2500_175_p` — Nature
- `extrudr_greentec_white_2500_285_p` — White
- `extrudr_greentec_black_2500_285_p` — Black 
- `extrudr_greentec_anthracite_2500_285_p` — Anthracite
- `extrudr_greentec_silver_2500_285_p` — Silver
- `extrudr_greentec_navyblue_2500_285_p` — Navy Blue
- `extrudr_greentec_red_2500_285_p` — Red
- `extrudr_greentec_nature_2500_285_p` — Nature
- `extrudr_greentec_white_5000_175_p` — White
- `extrudr_greentec_black_5000_175_p` — Black 
- `extrudr_greentec_anthracite_5000_175_p` — Anthracite
- `extrudr_greentec_silver_5000_175_p` — Silver
- `extrudr_greentec_navyblue_5000_175_p` — Navy Blue
- `extrudr_greentec_red_5000_175_p` — Red
- `extrudr_greentec_nature_5000_175_p` — Nature
- `extrudr_greentec_white_5000_285_p` — White
- `extrudr_greentec_black_5000_285_p` — Black 
- `extrudr_greentec_anthracite_5000_285_p` — Anthracite
- `extrudr_greentec_silver_5000_285_p` — Silver
- `extrudr_greentec_navyblue_5000_285_p` — Navy Blue
- `extrudr_greentec_red_5000_285_p` — Red
- `extrudr_greentec_nature_5000_285_p` — Nature
- `extrudr_greentec_white_10000_175_p` — White
- `extrudr_greentec_black_10000_175_p` — Black 
- `extrudr_greentec_anthracite_10000_175_p` — Anthracite
- `extrudr_greentec_silver_10000_175_p` — Silver
- `extrudr_greentec_navyblue_10000_175_p` — Navy Blue
- `extrudr_greentec_red_10000_175_p` — Red
- `extrudr_greentec_nature_10000_175_p` — Nature
- `extrudr_greentec_white_10000_285_p` — White
- `extrudr_greentec_black_10000_285_p` — Black 
- `extrudr_greentec_anthracite_10000_285_p` — Anthracite
- `extrudr_greentec_silver_10000_285_p` — Silver
- `extrudr_greentec_navyblue_10000_285_p` — Navy Blue
- `extrudr_greentec_red_10000_285_p` — Red
- `extrudr_greentec_nature_10000_285_p` — Nature
- `extrudr_greentec_problack_800_175_p` — Pro Black 
- `extrudr_greentec_proanthracite_800_175_p` — Pro Anthracite
- `extrudr_greentec_prohellfirered_800_175_p` — Pro Hellfire Red
- `extrudr_greentec_prowhite_800_175_p` — Pro White
- `extrudr_greentec_pronature_800_175_p` — Pro Nature
- `extrudr_greentec_prosilver_800_175_p` — Pro Silver
- `extrudr_greentec_pronavyblue_800_175_p` — Pro Navy Blue
- `extrudr_greentec_problack_800_285_p` — Pro Black 
- `extrudr_greentec_proanthracite_800_285_p` — Pro Anthracite
- `extrudr_greentec_prohellfirered_800_285_p` — Pro Hellfire Red
- `extrudr_greentec_prowhite_800_285_p` — Pro White
- `extrudr_greentec_pronature_800_285_p` — Pro Nature
- `extrudr_greentec_prosilver_800_285_p` — Pro Silver
- `extrudr_greentec_pronavyblue_800_285_p` — Pro Navy Blue
- `extrudr_greentec_problack_2500_175_p` — Pro Black 
- `extrudr_greentec_proanthracite_2500_175_p` — Pro Anthracite
- `extrudr_greentec_prohellfirered_2500_175_p` — Pro Hellfire Red
- `extrudr_greentec_prowhite_2500_175_p` — Pro White
- `extrudr_greentec_pronature_2500_175_p` — Pro Nature
- `extrudr_greentec_prosilver_2500_175_p` — Pro Silver
- `extrudr_greentec_pronavyblue_2500_175_p` — Pro Navy Blue
- `extrudr_greentec_problack_2500_285_p` — Pro Black 
- `extrudr_greentec_proanthracite_2500_285_p` — Pro Anthracite
- `extrudr_greentec_prohellfirered_2500_285_p` — Pro Hellfire Red
- `extrudr_greentec_prowhite_2500_285_p` — Pro White
- `extrudr_greentec_pronature_2500_285_p` — Pro Nature
- `extrudr_greentec_prosilver_2500_285_p` — Pro Silver
- `extrudr_greentec_pronavyblue_2500_285_p` — Pro Navy Blue
- `extrudr_greentec_problack_5000_175_p` — Pro Black 
- `extrudr_greentec_proanthracite_5000_175_p` — Pro Anthracite
- `extrudr_greentec_prohellfirered_5000_175_p` — Pro Hellfire Red
- `extrudr_greentec_prowhite_5000_175_p` — Pro White
- `extrudr_greentec_pronature_5000_175_p` — Pro Nature
- `extrudr_greentec_prosilver_5000_175_p` — Pro Silver
- `extrudr_greentec_pronavyblue_5000_175_p` — Pro Navy Blue
- `extrudr_greentec_problack_5000_285_p` — Pro Black 
- `extrudr_greentec_proanthracite_5000_285_p` — Pro Anthracite
- `extrudr_greentec_prohellfirered_5000_285_p` — Pro Hellfire Red
- `extrudr_greentec_prowhite_5000_285_p` — Pro White
- `extrudr_greentec_pronature_5000_285_p` — Pro Nature
- `extrudr_greentec_prosilver_5000_285_p` — Pro Silver
- `extrudr_greentec_pronavyblue_5000_285_p` — Pro Navy Blue
- `extrudr_greentec_problack_10000_175_p` — Pro Black 
- `extrudr_greentec_proanthracite_10000_175_p` — Pro Anthracite
- `extrudr_greentec_prohellfirered_10000_175_p` — Pro Hellfire Red
- `extrudr_greentec_prowhite_10000_175_p` — Pro White
- `extrudr_greentec_pronature_10000_175_p` — Pro Nature
- `extrudr_greentec_prosilver_10000_175_p` — Pro Silver
- `extrudr_greentec_pronavyblue_10000_175_p` — Pro Navy Blue
- `extrudr_greentec_problack_10000_285_p` — Pro Black 
- `extrudr_greentec_proanthracite_10000_285_p` — Pro Anthracite
- `extrudr_greentec_prohellfirered_10000_285_p` — Pro Hellfire Red
- `extrudr_greentec_prowhite_10000_285_p` — Pro White
- `extrudr_greentec_pronature_10000_285_p` — Pro Nature
- `extrudr_greentec_prosilver_10000_285_p` — Pro Silver
- `extrudr_greentec_pronavyblue_10000_285_p` — Pro Navy Blue
- `extrudr_greentec-cf_problack_800_175_p` — Pro Black
- `extrudr_greentec-cf_problack_800_285_p` — Pro Black
- `extrudr_greentec-cf_problack_2500_175_p` — Pro Black
- `extrudr_greentec-cf_problack_2500_285_p` — Pro Black
- `extrudr_greentec-cf_problack_5000_175_p` — Pro Black
- `extrudr_greentec-cf_problack_5000_285_p` — Pro Black
- `extrudr_greentec-cf_problack_10000_175_p` — Pro Black
- `extrudr_greentec-cf_problack_10000_285_p` — Pro Black
- `extrudr_pearl_nature_1100_175_p` — Nature
- `extrudr_pearl_nature_1100_285_p` — Nature
- `extrudr_pearl_nature_2500_175_p` — Nature
- `extrudr_pearl_nature_2500_285_p` — Nature
- `extrudr_pearl_nature_10000_175_p` — Nature
- `extrudr_pearl_nature_10000_285_p` — Nature
- `extrudr_wood_darkwood_800_175_p` — Dark Wood
- `extrudr_wood_nature_800_175_p` — Nature
- `extrudr_wood_darkwood_800_285_p` — Dark Wood
- `extrudr_wood_nature_800_285_p` — Nature
- `extrudr_wood_darkwood_2000_175_p` — Dark Wood
- `extrudr_wood_nature_2000_175_p` — Nature
- `extrudr_wood_darkwood_2000_285_p` — Dark Wood
- `extrudr_wood_nature_2000_285_p` — Nature
- `extrudr_wood_darkwood_10000_175_p` — Dark Wood
- `extrudr_wood_nature_10000_175_p` — Nature
- `extrudr_wood_darkwood_10000_285_p` — Dark Wood
- `extrudr_wood_nature_10000_285_p` — Nature
- `extrudr_pla_basic-white_1000_285_p` — Basic - White
- `extrudr_pla_basic-transparent_1000_285_p` — Basic - Transparent 
- `extrudr_pla_basic-black_1000_285_p` — Basic - Black 
- `extrudr_pla_basic-gold_1000_285_p` — Basic - Gold
- `extrudr_pla_basic-cmyklithowhite_1000_285_p` — Basic - CMYK Lithowhite
- `extrudr_pla_basic-cmyklithomagenta_1000_285_p` — Basic - CMYK Lithomagenta
- `extrudr_pla_basic-cmyklithoyellow_1000_285_p` — Basic - CMYK Lithoyellow
- `extrudr_pla_basic-cmyklithocyan_1000_285_p` — Basic - CMYK Lithocyan
- `extrudr_pla_basic-white_2500_175_p` — Basic - White
- `extrudr_pla_basic-transparent_2500_175_p` — Basic - Transparent 
- `extrudr_pla_basic-black_2500_175_p` — Basic - Black 
- `extrudr_pla_basic-gold_2500_175_p` — Basic - Gold
- `extrudr_pla_basic-cmyklithowhite_2500_175_p` — Basic - CMYK Lithowhite
- `extrudr_pla_basic-cmyklithomagenta_2500_175_p` — Basic - CMYK Lithomagenta
- `extrudr_pla_basic-cmyklithoyellow_2500_175_p` — Basic - CMYK Lithoyellow
- `extrudr_pla_basic-cmyklithocyan_2500_175_p` — Basic - CMYK Lithocyan
- `extrudr_pla_basic-white_2500_285_p` — Basic - White
- `extrudr_pla_basic-transparent_2500_285_p` — Basic - Transparent 
- `extrudr_pla_basic-black_2500_285_p` — Basic - Black 
- `extrudr_pla_basic-gold_2500_285_p` — Basic - Gold
- `extrudr_pla_basic-cmyklithowhite_2500_285_p` — Basic - CMYK Lithowhite
- `extrudr_pla_basic-cmyklithomagenta_2500_285_p` — Basic - CMYK Lithomagenta
- `extrudr_pla_basic-cmyklithoyellow_2500_285_p` — Basic - CMYK Lithoyellow
- `extrudr_pla_basic-cmyklithocyan_2500_285_p` — Basic - CMYK Lithocyan
- `extrudr_pla_basic-white_5000_175_p` — Basic - White
- `extrudr_pla_basic-transparent_5000_175_p` — Basic - Transparent 
- `extrudr_pla_basic-black_5000_175_p` — Basic - Black 
- `extrudr_pla_basic-gold_5000_175_p` — Basic - Gold
- `extrudr_pla_basic-cmyklithowhite_5000_175_p` — Basic - CMYK Lithowhite
- `extrudr_pla_basic-cmyklithomagenta_5000_175_p` — Basic - CMYK Lithomagenta
- `extrudr_pla_basic-cmyklithoyellow_5000_175_p` — Basic - CMYK Lithoyellow
- `extrudr_pla_basic-cmyklithocyan_5000_175_p` — Basic - CMYK Lithocyan
- `extrudr_pla_basic-white_5000_285_p` — Basic - White
- `extrudr_pla_basic-transparent_5000_285_p` — Basic - Transparent 
- `extrudr_pla_basic-black_5000_285_p` — Basic - Black 
- `extrudr_pla_basic-gold_5000_285_p` — Basic - Gold
- `extrudr_pla_basic-cmyklithowhite_5000_285_p` — Basic - CMYK Lithowhite
- `extrudr_pla_basic-cmyklithomagenta_5000_285_p` — Basic - CMYK Lithomagenta
- `extrudr_pla_basic-cmyklithoyellow_5000_285_p` — Basic - CMYK Lithoyellow
- `extrudr_pla_basic-cmyklithocyan_5000_285_p` — Basic - CMYK Lithocyan
- `extrudr_pla_basic-white_10000_175_p` — Basic - White
- `extrudr_pla_basic-transparent_10000_175_p` — Basic - Transparent 
- `extrudr_pla_basic-black_10000_175_p` — Basic - Black 
- `extrudr_pla_basic-gold_10000_175_p` — Basic - Gold
- `extrudr_pla_basic-cmyklithowhite_10000_175_p` — Basic - CMYK Lithowhite
- `extrudr_pla_basic-cmyklithomagenta_10000_175_p` — Basic - CMYK Lithomagenta
- `extrudr_pla_basic-cmyklithoyellow_10000_175_p` — Basic - CMYK Lithoyellow
- `extrudr_pla_basic-cmyklithocyan_10000_175_p` — Basic - CMYK Lithocyan
- `extrudr_pla_basic-white_10000_285_p` — Basic - White
- `extrudr_pla_basic-transparent_10000_285_p` — Basic - Transparent 
- `extrudr_pla_basic-black_10000_285_p` — Basic - Black 
- `extrudr_pla_basic-gold_10000_285_p` — Basic - Gold
- `extrudr_pla_basic-cmyklithowhite_10000_285_p` — Basic - CMYK Lithowhite
- `extrudr_pla_basic-cmyklithomagenta_10000_285_p` — Basic - CMYK Lithomagenta
- `extrudr_pla_basic-cmyklithoyellow_10000_285_p` — Basic - CMYK Lithoyellow
- `extrudr_pla_basic-cmyklithocyan_10000_285_p` — Basic - CMYK Lithocyan
- `extrudr_pla_nx2-matt-neonyellow_1000_175_p` — NX2-MATT - Neon Yellow
- `extrudr_pla_nx2-matt-black_1000_285_p` — NX2-MATT - Black
- `extrudr_pla_nx2-matt-anthracite_1000_285_p` — NX2-MATT - Anthracite
- `extrudr_pla_nx2-matt-metallicgrey_1000_285_p` — NX2-MATT - Metallic Grey
- `extrudr_pla_nx2-matt-silver_1000_285_p` — NX2-MATT - Silver
- `extrudr_pla_nx2-matt-grey_1000_285_p` — NX2-MATT - Grey
- `extrudr_pla_nx2-matt-militarygreen_1000_285_p` — NX2-MATT - Military Green
- `extrudr_pla_nx2-matt-emeraldgreen_1000_285_p` — NX2-MATT - Emerald Green
- `extrudr_pla_nx2-matt-signalgreen_1000_285_p` — NX2-MATT - Signal Green
- `extrudr_pla_nx2-matt-turquoise_1000_285_p` — NX2-MATT - Turquoise
- `extrudr_pla_nx2-matt-bluesteel_1000_285_p` — NX2-MATT - Blue Steel
- `extrudr_pla_nx2-matt-navyblue_1000_285_p` — NX2-MATT - Navy Blue
- `extrudr_pla_nx2-matt-lightblue_1000_285_p` — NX2-MATT - Light Blue
- `extrudr_pla_nx2-matt-epicpurple_1000_285_p` — NX2-MATT - Epic Purple
- `extrudr_pla_nx2-matt-purple_1000_285_p` — NX2-MATT - Purple
- `extrudr_pla_nx2-matt-hellfirered_1000_285_p` — NX2-MATT - Hellfire Red 
- `extrudr_pla_nx2-matt-neonorange_1000_285_p` — NX2-MATT - Neon Orange
- `extrudr_pla_nx2-matt-orange_1000_285_p` — NX2-MATT - Orange
- `extrudr_pla_nx2-matt-yellow_1000_285_p` — NX2-MATT - Yellow
- `extrudr_pla_nx2-matt-neonyellow_1000_285_p` — NX2-MATT - Neon Yellow
- `extrudr_pla_nx2-matt-brown_1000_285_p` — NX2-MATT - Brown
- `extrudr_pla_nx2-matt-militarybeige_1000_285_p` — NX2-MATT - Military Beige
- `extrudr_pla_nx2-matt-white_1000_285_p` — NX2-MATT - White
- `extrudr_pla_nx2-matt-black_2500_175_p` — NX2-MATT - Black
- `extrudr_pla_nx2-matt-anthracite_2500_175_p` — NX2-MATT - Anthracite
- `extrudr_pla_nx2-matt-metallicgrey_2500_175_p` — NX2-MATT - Metallic Grey
- `extrudr_pla_nx2-matt-silver_2500_175_p` — NX2-MATT - Silver
- `extrudr_pla_nx2-matt-grey_2500_175_p` — NX2-MATT - Grey
- `extrudr_pla_nx2-matt-militarygreen_2500_175_p` — NX2-MATT - Military Green
- `extrudr_pla_nx2-matt-emeraldgreen_2500_175_p` — NX2-MATT - Emerald Green
- `extrudr_pla_nx2-matt-signalgreen_2500_175_p` — NX2-MATT - Signal Green
- `extrudr_pla_nx2-matt-turquoise_2500_175_p` — NX2-MATT - Turquoise
- `extrudr_pla_nx2-matt-bluesteel_2500_175_p` — NX2-MATT - Blue Steel
- `extrudr_pla_nx2-matt-navyblue_2500_175_p` — NX2-MATT - Navy Blue
- `extrudr_pla_nx2-matt-lightblue_2500_175_p` — NX2-MATT - Light Blue
- `extrudr_pla_nx2-matt-epicpurple_2500_175_p` — NX2-MATT - Epic Purple
- `extrudr_pla_nx2-matt-purple_2500_175_p` — NX2-MATT - Purple
- `extrudr_pla_nx2-matt-hellfirered_2500_175_p` — NX2-MATT - Hellfire Red 
- `extrudr_pla_nx2-matt-neonorange_2500_175_p` — NX2-MATT - Neon Orange
- `extrudr_pla_nx2-matt-orange_2500_175_p` — NX2-MATT - Orange
- `extrudr_pla_nx2-matt-yellow_2500_175_p` — NX2-MATT - Yellow
- `extrudr_pla_nx2-matt-neonyellow_2500_175_p` — NX2-MATT - Neon Yellow
- `extrudr_pla_nx2-matt-brown_2500_175_p` — NX2-MATT - Brown
- `extrudr_pla_nx2-matt-militarybeige_2500_175_p` — NX2-MATT - Military Beige
- `extrudr_pla_nx2-matt-white_2500_175_p` — NX2-MATT - White
- `extrudr_pla_nx2-matt-black_2500_285_p` — NX2-MATT - Black
- `extrudr_pla_nx2-matt-anthracite_2500_285_p` — NX2-MATT - Anthracite
- `extrudr_pla_nx2-matt-metallicgrey_2500_285_p` — NX2-MATT - Metallic Grey
- `extrudr_pla_nx2-matt-silver_2500_285_p` — NX2-MATT - Silver
- `extrudr_pla_nx2-matt-grey_2500_285_p` — NX2-MATT - Grey
- `extrudr_pla_nx2-matt-militarygreen_2500_285_p` — NX2-MATT - Military Green
- `extrudr_pla_nx2-matt-emeraldgreen_2500_285_p` — NX2-MATT - Emerald Green
- `extrudr_pla_nx2-matt-signalgreen_2500_285_p` — NX2-MATT - Signal Green
- `extrudr_pla_nx2-matt-turquoise_2500_285_p` — NX2-MATT - Turquoise
- `extrudr_pla_nx2-matt-bluesteel_2500_285_p` — NX2-MATT - Blue Steel
- `extrudr_pla_nx2-matt-navyblue_2500_285_p` — NX2-MATT - Navy Blue
- `extrudr_pla_nx2-matt-lightblue_2500_285_p` — NX2-MATT - Light Blue
- `extrudr_pla_nx2-matt-epicpurple_2500_285_p` — NX2-MATT - Epic Purple
- `extrudr_pla_nx2-matt-purple_2500_285_p` — NX2-MATT - Purple
- `extrudr_pla_nx2-matt-hellfirered_2500_285_p` — NX2-MATT - Hellfire Red 
- `extrudr_pla_nx2-matt-neonorange_2500_285_p` — NX2-MATT - Neon Orange
- `extrudr_pla_nx2-matt-orange_2500_285_p` — NX2-MATT - Orange
- `extrudr_pla_nx2-matt-yellow_2500_285_p` — NX2-MATT - Yellow
- `extrudr_pla_nx2-matt-neonyellow_2500_285_p` — NX2-MATT - Neon Yellow
- `extrudr_pla_nx2-matt-brown_2500_285_p` — NX2-MATT - Brown
- `extrudr_pla_nx2-matt-militarybeige_2500_285_p` — NX2-MATT - Military Beige
- `extrudr_pla_nx2-matt-white_2500_285_p` — NX2-MATT - White
- `extrudr_pla_nx2-matt-black_5000_175_p` — NX2-MATT - Black
- `extrudr_pla_nx2-matt-anthracite_5000_175_p` — NX2-MATT - Anthracite
- `extrudr_pla_nx2-matt-metallicgrey_5000_175_p` — NX2-MATT - Metallic Grey
- `extrudr_pla_nx2-matt-silver_5000_175_p` — NX2-MATT - Silver
- `extrudr_pla_nx2-matt-grey_5000_175_p` — NX2-MATT - Grey
- `extrudr_pla_nx2-matt-militarygreen_5000_175_p` — NX2-MATT - Military Green
- `extrudr_pla_nx2-matt-emeraldgreen_5000_175_p` — NX2-MATT - Emerald Green
- `extrudr_pla_nx2-matt-signalgreen_5000_175_p` — NX2-MATT - Signal Green
- `extrudr_pla_nx2-matt-turquoise_5000_175_p` — NX2-MATT - Turquoise
- `extrudr_pla_nx2-matt-bluesteel_5000_175_p` — NX2-MATT - Blue Steel
- `extrudr_pla_nx2-matt-navyblue_5000_175_p` — NX2-MATT - Navy Blue
- `extrudr_pla_nx2-matt-lightblue_5000_175_p` — NX2-MATT - Light Blue
- `extrudr_pla_nx2-matt-epicpurple_5000_175_p` — NX2-MATT - Epic Purple
- `extrudr_pla_nx2-matt-purple_5000_175_p` — NX2-MATT - Purple
- `extrudr_pla_nx2-matt-hellfirered_5000_175_p` — NX2-MATT - Hellfire Red 
- `extrudr_pla_nx2-matt-neonorange_5000_175_p` — NX2-MATT - Neon Orange
- `extrudr_pla_nx2-matt-orange_5000_175_p` — NX2-MATT - Orange
- `extrudr_pla_nx2-matt-yellow_5000_175_p` — NX2-MATT - Yellow
- `extrudr_pla_nx2-matt-neonyellow_5000_175_p` — NX2-MATT - Neon Yellow
- `extrudr_pla_nx2-matt-brown_5000_175_p` — NX2-MATT - Brown
- `extrudr_pla_nx2-matt-militarybeige_5000_175_p` — NX2-MATT - Military Beige
- `extrudr_pla_nx2-matt-white_5000_175_p` — NX2-MATT - White
- `extrudr_pla_nx2-matt-black_5000_285_p` — NX2-MATT - Black
- `extrudr_pla_nx2-matt-anthracite_5000_285_p` — NX2-MATT - Anthracite
- `extrudr_pla_nx2-matt-metallicgrey_5000_285_p` — NX2-MATT - Metallic Grey
- `extrudr_pla_nx2-matt-silver_5000_285_p` — NX2-MATT - Silver
- `extrudr_pla_nx2-matt-grey_5000_285_p` — NX2-MATT - Grey
- `extrudr_pla_nx2-matt-militarygreen_5000_285_p` — NX2-MATT - Military Green
- `extrudr_pla_nx2-matt-emeraldgreen_5000_285_p` — NX2-MATT - Emerald Green
- `extrudr_pla_nx2-matt-signalgreen_5000_285_p` — NX2-MATT - Signal Green
- `extrudr_pla_nx2-matt-turquoise_5000_285_p` — NX2-MATT - Turquoise
- `extrudr_pla_nx2-matt-bluesteel_5000_285_p` — NX2-MATT - Blue Steel
- `extrudr_pla_nx2-matt-navyblue_5000_285_p` — NX2-MATT - Navy Blue
- `extrudr_pla_nx2-matt-lightblue_5000_285_p` — NX2-MATT - Light Blue
- `extrudr_pla_nx2-matt-epicpurple_5000_285_p` — NX2-MATT - Epic Purple
- `extrudr_pla_nx2-matt-purple_5000_285_p` — NX2-MATT - Purple
- `extrudr_pla_nx2-matt-hellfirered_5000_285_p` — NX2-MATT - Hellfire Red 
- `extrudr_pla_nx2-matt-neonorange_5000_285_p` — NX2-MATT - Neon Orange
- `extrudr_pla_nx2-matt-orange_5000_285_p` — NX2-MATT - Orange
- `extrudr_pla_nx2-matt-yellow_5000_285_p` — NX2-MATT - Yellow
- `extrudr_pla_nx2-matt-neonyellow_5000_285_p` — NX2-MATT - Neon Yellow
- `extrudr_pla_nx2-matt-brown_5000_285_p` — NX2-MATT - Brown
- `extrudr_pla_nx2-matt-militarybeige_5000_285_p` — NX2-MATT - Military Beige
- `extrudr_pla_nx2-matt-white_5000_285_p` — NX2-MATT - White
- `extrudr_pla_nx2-matt-black_10000_175_p` — NX2-MATT - Black
- `extrudr_pla_nx2-matt-anthracite_10000_175_p` — NX2-MATT - Anthracite
- `extrudr_pla_nx2-matt-metallicgrey_10000_175_p` — NX2-MATT - Metallic Grey
- `extrudr_pla_nx2-matt-silver_10000_175_p` — NX2-MATT - Silver
- `extrudr_pla_nx2-matt-grey_10000_175_p` — NX2-MATT - Grey
- `extrudr_pla_nx2-matt-militarygreen_10000_175_p` — NX2-MATT - Military Green
- `extrudr_pla_nx2-matt-emeraldgreen_10000_175_p` — NX2-MATT - Emerald Green
- `extrudr_pla_nx2-matt-signalgreen_10000_175_p` — NX2-MATT - Signal Green
- `extrudr_pla_nx2-matt-turquoise_10000_175_p` — NX2-MATT - Turquoise
- `extrudr_pla_nx2-matt-bluesteel_10000_175_p` — NX2-MATT - Blue Steel
- `extrudr_pla_nx2-matt-navyblue_10000_175_p` — NX2-MATT - Navy Blue
- `extrudr_pla_nx2-matt-lightblue_10000_175_p` — NX2-MATT - Light Blue
- `extrudr_pla_nx2-matt-epicpurple_10000_175_p` — NX2-MATT - Epic Purple
- `extrudr_pla_nx2-matt-purple_10000_175_p` — NX2-MATT - Purple
- `extrudr_pla_nx2-matt-hellfirered_10000_175_p` — NX2-MATT - Hellfire Red 
- `extrudr_pla_nx2-matt-neonorange_10000_175_p` — NX2-MATT - Neon Orange
- `extrudr_pla_nx2-matt-orange_10000_175_p` — NX2-MATT - Orange
- `extrudr_pla_nx2-matt-yellow_10000_175_p` — NX2-MATT - Yellow
- `extrudr_pla_nx2-matt-neonyellow_10000_175_p` — NX2-MATT - Neon Yellow
- `extrudr_pla_nx2-matt-brown_10000_175_p` — NX2-MATT - Brown
- `extrudr_pla_nx2-matt-militarybeige_10000_175_p` — NX2-MATT - Military Beige
- `extrudr_pla_nx2-matt-white_10000_175_p` — NX2-MATT - White
- `extrudr_pla_nx2-matt-black_10000_285_p` — NX2-MATT - Black
- `extrudr_pla_nx2-matt-anthracite_10000_285_p` — NX2-MATT - Anthracite
- `extrudr_pla_nx2-matt-metallicgrey_10000_285_p` — NX2-MATT - Metallic Grey
- `extrudr_pla_nx2-matt-silver_10000_285_p` — NX2-MATT - Silver
- `extrudr_pla_nx2-matt-grey_10000_285_p` — NX2-MATT - Grey
- `extrudr_pla_nx2-matt-militarygreen_10000_285_p` — NX2-MATT - Military Green
- `extrudr_pla_nx2-matt-emeraldgreen_10000_285_p` — NX2-MATT - Emerald Green
- `extrudr_pla_nx2-matt-signalgreen_10000_285_p` — NX2-MATT - Signal Green
- `extrudr_pla_nx2-matt-turquoise_10000_285_p` — NX2-MATT - Turquoise
- `extrudr_pla_nx2-matt-bluesteel_10000_285_p` — NX2-MATT - Blue Steel
- `extrudr_pla_nx2-matt-navyblue_10000_285_p` — NX2-MATT - Navy Blue
- `extrudr_pla_nx2-matt-lightblue_10000_285_p` — NX2-MATT - Light Blue
- `extrudr_pla_nx2-matt-epicpurple_10000_285_p` — NX2-MATT - Epic Purple
- `extrudr_pla_nx2-matt-purple_10000_285_p` — NX2-MATT - Purple
- `extrudr_pla_nx2-matt-hellfirered_10000_285_p` — NX2-MATT - Hellfire Red 
- `extrudr_pla_nx2-matt-neonorange_10000_285_p` — NX2-MATT - Neon Orange
- `extrudr_pla_nx2-matt-orange_10000_285_p` — NX2-MATT - Orange
- `extrudr_pla_nx2-matt-yellow_10000_285_p` — NX2-MATT - Yellow
- `extrudr_pla_nx2-matt-neonyellow_10000_285_p` — NX2-MATT - Neon Yellow
- `extrudr_pla_nx2-matt-brown_10000_285_p` — NX2-MATT - Brown
- `extrudr_pla_nx2-matt-militarybeige_10000_285_p` — NX2-MATT - Military Beige
- `extrudr_pla_nx2-matt-white_10000_285_p` — NX2-MATT - White
- `extrudr_petg_transparent_1100_175_p` — Transparent
- `extrudr_petg_black_1100_175_p` — Black
- `extrudr_petg_anthracite_1100_175_p` — Anthracite
- `extrudr_petg_metallic_1100_175_p` — Metallic
- `extrudr_petg_silver_1100_175_p` — Silver
- `extrudr_petg_grey_1100_175_p` — Grey
- `extrudr_petg_militarygreen_1100_175_p` — Military Green
- `extrudr_petg_transparentgreen_1100_175_p` — Transparent Green
- `extrudr_petg_emeraldgreen_1100_175_p` — Emerald Green
- `extrudr_petg_signalgreen_1100_175_p` — Signal Green
- `extrudr_petg_neongreen_1100_175_p` — Neon Green
- `extrudr_petg_white_1100_175_p` — White
- `extrudr_petg_turquoise_1100_175_p` — Turquoise
- `extrudr_petg_transparentblue_1100_175_p` — Transparent Blue
- `extrudr_petg_navyblue_1100_175_p` — Navy Blue
- `extrudr_petg_lightblue_1100_175_p` — Light Blue
- `extrudr_petg_purple_1100_175_p` — Purple
- `extrudr_petg_magenta_1100_175_p` — Magenta
- `extrudr_petg_transparentred_1100_175_p` — Transparent Red
- `extrudr_petg_red_1100_175_p` — Red
- `extrudr_petg_neonred_1100_175_p` — Neon Red
- `extrudr_petg_hellfirered_1100_175_p` — Hellfire Red 
- `extrudr_petg_copper_1100_175_p` — Copper
- `extrudr_petg_bronze_1100_175_p` — Bronze
- `extrudr_petg_transparentorange_1100_175_p` — Transparent Orange
- `extrudr_petg_neonorange_1100_175_p` — Neon Orange
- `extrudr_petg_orange_1100_175_p` — Orange
- `extrudr_petg_transparentyellow_1100_175_p` — Transparent Yellow
- `extrudr_petg_gold_1100_175_p` — Gold
- `extrudr_petg_yellow_1100_175_p` — Yellow
- `extrudr_petg_neonyellow_1100_175_p` — Neon Yellow
- `extrudr_petg_transparent_1100_285_p` — Transparent
- `extrudr_petg_black_1100_285_p` — Black
- `extrudr_petg_anthracite_1100_285_p` — Anthracite
- `extrudr_petg_metallic_1100_285_p` — Metallic
- `extrudr_petg_silver_1100_285_p` — Silver
- `extrudr_petg_grey_1100_285_p` — Grey
- `extrudr_petg_militarygreen_1100_285_p` — Military Green
- `extrudr_petg_transparentgreen_1100_285_p` — Transparent Green
- `extrudr_petg_emeraldgreen_1100_285_p` — Emerald Green
- `extrudr_petg_signalgreen_1100_285_p` — Signal Green
- `extrudr_petg_neongreen_1100_285_p` — Neon Green
- `extrudr_petg_white_1100_285_p` — White
- `extrudr_petg_turquoise_1100_285_p` — Turquoise
- `extrudr_petg_transparentblue_1100_285_p` — Transparent Blue
- `extrudr_petg_navyblue_1100_285_p` — Navy Blue
- `extrudr_petg_lightblue_1100_285_p` — Light Blue
- `extrudr_petg_purple_1100_285_p` — Purple
- `extrudr_petg_magenta_1100_285_p` — Magenta
- `extrudr_petg_transparentred_1100_285_p` — Transparent Red
- `extrudr_petg_red_1100_285_p` — Red
- `extrudr_petg_neonred_1100_285_p` — Neon Red
- `extrudr_petg_hellfirered_1100_285_p` — Hellfire Red 
- `extrudr_petg_copper_1100_285_p` — Copper
- `extrudr_petg_bronze_1100_285_p` — Bronze
- `extrudr_petg_transparentorange_1100_285_p` — Transparent Orange
- `extrudr_petg_neonorange_1100_285_p` — Neon Orange
- `extrudr_petg_orange_1100_285_p` — Orange
- `extrudr_petg_transparentyellow_1100_285_p` — Transparent Yellow
- `extrudr_petg_gold_1100_285_p` — Gold
- `extrudr_petg_yellow_1100_285_p` — Yellow
- `extrudr_petg_neonyellow_1100_285_p` — Neon Yellow
- `extrudr_petg_transparent_2500_175_p` — Transparent
- `extrudr_petg_black_2500_175_p` — Black
- `extrudr_petg_anthracite_2500_175_p` — Anthracite
- `extrudr_petg_metallic_2500_175_p` — Metallic
- `extrudr_petg_silver_2500_175_p` — Silver
- `extrudr_petg_grey_2500_175_p` — Grey
- `extrudr_petg_militarygreen_2500_175_p` — Military Green
- `extrudr_petg_transparentgreen_2500_175_p` — Transparent Green
- `extrudr_petg_emeraldgreen_2500_175_p` — Emerald Green
- `extrudr_petg_signalgreen_2500_175_p` — Signal Green
- `extrudr_petg_neongreen_2500_175_p` — Neon Green
- `extrudr_petg_white_2500_175_p` — White
- `extrudr_petg_turquoise_2500_175_p` — Turquoise
- `extrudr_petg_transparentblue_2500_175_p` — Transparent Blue
- `extrudr_petg_navyblue_2500_175_p` — Navy Blue
- `extrudr_petg_lightblue_2500_175_p` — Light Blue
- `extrudr_petg_purple_2500_175_p` — Purple
- `extrudr_petg_magenta_2500_175_p` — Magenta
- `extrudr_petg_transparentred_2500_175_p` — Transparent Red
- `extrudr_petg_red_2500_175_p` — Red
- `extrudr_petg_neonred_2500_175_p` — Neon Red
- `extrudr_petg_hellfirered_2500_175_p` — Hellfire Red 
- `extrudr_petg_copper_2500_175_p` — Copper
- `extrudr_petg_bronze_2500_175_p` — Bronze
- `extrudr_petg_transparentorange_2500_175_p` — Transparent Orange
- `extrudr_petg_neonorange_2500_175_p` — Neon Orange
- `extrudr_petg_orange_2500_175_p` — Orange
- `extrudr_petg_transparentyellow_2500_175_p` — Transparent Yellow
- `extrudr_petg_gold_2500_175_p` — Gold
- `extrudr_petg_yellow_2500_175_p` — Yellow
- `extrudr_petg_neonyellow_2500_175_p` — Neon Yellow
- `extrudr_petg_transparent_2500_285_p` — Transparent
- `extrudr_petg_black_2500_285_p` — Black
- `extrudr_petg_anthracite_2500_285_p` — Anthracite
- `extrudr_petg_metallic_2500_285_p` — Metallic
- `extrudr_petg_silver_2500_285_p` — Silver
- `extrudr_petg_grey_2500_285_p` — Grey
- `extrudr_petg_militarygreen_2500_285_p` — Military Green
- `extrudr_petg_transparentgreen_2500_285_p` — Transparent Green
- `extrudr_petg_emeraldgreen_2500_285_p` — Emerald Green
- `extrudr_petg_signalgreen_2500_285_p` — Signal Green
- `extrudr_petg_neongreen_2500_285_p` — Neon Green
- `extrudr_petg_white_2500_285_p` — White
- `extrudr_petg_turquoise_2500_285_p` — Turquoise
- `extrudr_petg_transparentblue_2500_285_p` — Transparent Blue
- `extrudr_petg_navyblue_2500_285_p` — Navy Blue
- `extrudr_petg_lightblue_2500_285_p` — Light Blue
- `extrudr_petg_purple_2500_285_p` — Purple
- `extrudr_petg_magenta_2500_285_p` — Magenta
- `extrudr_petg_transparentred_2500_285_p` — Transparent Red
- `extrudr_petg_red_2500_285_p` — Red
- `extrudr_petg_neonred_2500_285_p` — Neon Red
- `extrudr_petg_hellfirered_2500_285_p` — Hellfire Red 
- `extrudr_petg_copper_2500_285_p` — Copper
- `extrudr_petg_bronze_2500_285_p` — Bronze
- `extrudr_petg_transparentorange_2500_285_p` — Transparent Orange
- `extrudr_petg_neonorange_2500_285_p` — Neon Orange
- `extrudr_petg_orange_2500_285_p` — Orange
- `extrudr_petg_transparentyellow_2500_285_p` — Transparent Yellow
- `extrudr_petg_gold_2500_285_p` — Gold
- `extrudr_petg_yellow_2500_285_p` — Yellow
- `extrudr_petg_neonyellow_2500_285_p` — Neon Yellow
- `extrudr_petg_transparent_5000_175_p` — Transparent
- `extrudr_petg_black_5000_175_p` — Black
- `extrudr_petg_anthracite_5000_175_p` — Anthracite
- `extrudr_petg_metallic_5000_175_p` — Metallic
- `extrudr_petg_silver_5000_175_p` — Silver
- `extrudr_petg_grey_5000_175_p` — Grey
- `extrudr_petg_militarygreen_5000_175_p` — Military Green
- `extrudr_petg_transparentgreen_5000_175_p` — Transparent Green
- `extrudr_petg_emeraldgreen_5000_175_p` — Emerald Green
- `extrudr_petg_signalgreen_5000_175_p` — Signal Green
- `extrudr_petg_neongreen_5000_175_p` — Neon Green
- `extrudr_petg_white_5000_175_p` — White
- `extrudr_petg_turquoise_5000_175_p` — Turquoise
- `extrudr_petg_transparentblue_5000_175_p` — Transparent Blue
- `extrudr_petg_navyblue_5000_175_p` — Navy Blue
- `extrudr_petg_lightblue_5000_175_p` — Light Blue
- `extrudr_petg_purple_5000_175_p` — Purple
- `extrudr_petg_magenta_5000_175_p` — Magenta
- `extrudr_petg_transparentred_5000_175_p` — Transparent Red
- `extrudr_petg_red_5000_175_p` — Red
- `extrudr_petg_neonred_5000_175_p` — Neon Red
- `extrudr_petg_hellfirered_5000_175_p` — Hellfire Red 
- `extrudr_petg_copper_5000_175_p` — Copper
- `extrudr_petg_bronze_5000_175_p` — Bronze
- `extrudr_petg_transparentorange_5000_175_p` — Transparent Orange
- `extrudr_petg_neonorange_5000_175_p` — Neon Orange
- `extrudr_petg_orange_5000_175_p` — Orange
- `extrudr_petg_transparentyellow_5000_175_p` — Transparent Yellow
- `extrudr_petg_gold_5000_175_p` — Gold
- `extrudr_petg_yellow_5000_175_p` — Yellow
- `extrudr_petg_neonyellow_5000_175_p` — Neon Yellow
- `extrudr_petg_transparent_5000_285_p` — Transparent
- `extrudr_petg_black_5000_285_p` — Black
- `extrudr_petg_anthracite_5000_285_p` — Anthracite
- `extrudr_petg_metallic_5000_285_p` — Metallic
- `extrudr_petg_silver_5000_285_p` — Silver
- `extrudr_petg_grey_5000_285_p` — Grey
- `extrudr_petg_militarygreen_5000_285_p` — Military Green
- `extrudr_petg_transparentgreen_5000_285_p` — Transparent Green
- `extrudr_petg_emeraldgreen_5000_285_p` — Emerald Green
- `extrudr_petg_signalgreen_5000_285_p` — Signal Green
- `extrudr_petg_neongreen_5000_285_p` — Neon Green
- `extrudr_petg_white_5000_285_p` — White
- `extrudr_petg_turquoise_5000_285_p` — Turquoise
- `extrudr_petg_transparentblue_5000_285_p` — Transparent Blue
- `extrudr_petg_navyblue_5000_285_p` — Navy Blue
- `extrudr_petg_lightblue_5000_285_p` — Light Blue
- `extrudr_petg_purple_5000_285_p` — Purple
- `extrudr_petg_magenta_5000_285_p` — Magenta
- `extrudr_petg_transparentred_5000_285_p` — Transparent Red
- `extrudr_petg_red_5000_285_p` — Red
- `extrudr_petg_neonred_5000_285_p` — Neon Red
- `extrudr_petg_hellfirered_5000_285_p` — Hellfire Red 
- `extrudr_petg_copper_5000_285_p` — Copper
- `extrudr_petg_bronze_5000_285_p` — Bronze
- `extrudr_petg_transparentorange_5000_285_p` — Transparent Orange
- `extrudr_petg_neonorange_5000_285_p` — Neon Orange
- `extrudr_petg_orange_5000_285_p` — Orange
- `extrudr_petg_transparentyellow_5000_285_p` — Transparent Yellow
- `extrudr_petg_gold_5000_285_p` — Gold
- `extrudr_petg_yellow_5000_285_p` — Yellow
- `extrudr_petg_neonyellow_5000_285_p` — Neon Yellow
- `extrudr_petg_transparent_10000_175_p` — Transparent
- `extrudr_petg_black_10000_175_p` — Black
- `extrudr_petg_anthracite_10000_175_p` — Anthracite
- `extrudr_petg_metallic_10000_175_p` — Metallic
- `extrudr_petg_silver_10000_175_p` — Silver
- `extrudr_petg_grey_10000_175_p` — Grey
- `extrudr_petg_militarygreen_10000_175_p` — Military Green
- `extrudr_petg_transparentgreen_10000_175_p` — Transparent Green
- `extrudr_petg_emeraldgreen_10000_175_p` — Emerald Green
- `extrudr_petg_signalgreen_10000_175_p` — Signal Green
- `extrudr_petg_neongreen_10000_175_p` — Neon Green
- `extrudr_petg_white_10000_175_p` — White
- `extrudr_petg_turquoise_10000_175_p` — Turquoise
- `extrudr_petg_transparentblue_10000_175_p` — Transparent Blue
- `extrudr_petg_navyblue_10000_175_p` — Navy Blue
- `extrudr_petg_lightblue_10000_175_p` — Light Blue
- `extrudr_petg_purple_10000_175_p` — Purple
- `extrudr_petg_magenta_10000_175_p` — Magenta
- `extrudr_petg_transparentred_10000_175_p` — Transparent Red
- `extrudr_petg_red_10000_175_p` — Red
- `extrudr_petg_neonred_10000_175_p` — Neon Red
- `extrudr_petg_hellfirered_10000_175_p` — Hellfire Red 
- `extrudr_petg_copper_10000_175_p` — Copper
- `extrudr_petg_bronze_10000_175_p` — Bronze
- `extrudr_petg_transparentorange_10000_175_p` — Transparent Orange
- `extrudr_petg_neonorange_10000_175_p` — Neon Orange
- `extrudr_petg_orange_10000_175_p` — Orange
- `extrudr_petg_transparentyellow_10000_175_p` — Transparent Yellow
- `extrudr_petg_gold_10000_175_p` — Gold
- `extrudr_petg_yellow_10000_175_p` — Yellow
- `extrudr_petg_neonyellow_10000_175_p` — Neon Yellow
- `extrudr_petg_transparent_10000_285_p` — Transparent
- `extrudr_petg_black_10000_285_p` — Black
- `extrudr_petg_anthracite_10000_285_p` — Anthracite
- `extrudr_petg_metallic_10000_285_p` — Metallic
- `extrudr_petg_silver_10000_285_p` — Silver
- `extrudr_petg_grey_10000_285_p` — Grey
- `extrudr_petg_militarygreen_10000_285_p` — Military Green
- `extrudr_petg_transparentgreen_10000_285_p` — Transparent Green
- `extrudr_petg_emeraldgreen_10000_285_p` — Emerald Green
- `extrudr_petg_signalgreen_10000_285_p` — Signal Green
- `extrudr_petg_neongreen_10000_285_p` — Neon Green
- `extrudr_petg_white_10000_285_p` — White
- `extrudr_petg_turquoise_10000_285_p` — Turquoise
- `extrudr_petg_transparentblue_10000_285_p` — Transparent Blue
- `extrudr_petg_navyblue_10000_285_p` — Navy Blue
- `extrudr_petg_lightblue_10000_285_p` — Light Blue
- `extrudr_petg_purple_10000_285_p` — Purple
- `extrudr_petg_magenta_10000_285_p` — Magenta
- `extrudr_petg_transparentred_10000_285_p` — Transparent Red
- `extrudr_petg_red_10000_285_p` — Red
- `extrudr_petg_neonred_10000_285_p` — Neon Red
- `extrudr_petg_hellfirered_10000_285_p` — Hellfire Red 
- `extrudr_petg_copper_10000_285_p` — Copper
- `extrudr_petg_bronze_10000_285_p` — Bronze
- `extrudr_petg_transparentorange_10000_285_p` — Transparent Orange
- `extrudr_petg_neonorange_10000_285_p` — Neon Orange
- `extrudr_petg_orange_10000_285_p` — Orange
- `extrudr_petg_transparentyellow_10000_285_p` — Transparent Yellow
- `extrudr_petg_gold_10000_285_p` — Gold
- `extrudr_petg_yellow_10000_285_p` — Yellow
- `extrudr_petg_neonyellow_10000_285_p` — Neon Yellow
- `extrudr_petg_glowex_800_175_p` — glowEx
- `extrudr_petg_glowex_800_285_p` — glowEx
- `extrudr_petg_glowex_2500_175_p` — glowEx
- `extrudr_petg_glowex_2500_285_p` — glowEx
- `extrudr_petg-cf_x-black_800_175_p` — X - Black
- `extrudr_petg-cf_x-black_800_285_p` — X - Black
- `extrudr_petg-cf_x-black_2500_175_p` — X - Black
- `extrudr_petg-cf_x-black_2500_285_p` — X - Black
- `extrudr_petg-cf_x-black_5000_175_p` — X - Black
- `extrudr_petg-cf_x-black_5000_285_p` — X - Black
- `extrudr_petg-cf_x-black_10000_175_p` — X - Black
- `extrudr_petg-cf_x-black_10000_285_p` — X - Black
- `extrudr_petg_matt-black_1000_175_p` — MATT - Black
- `extrudr_petg_matt-anthracite_1000_175_p` — MATT - Anthracite
- `extrudr_petg_matt-militarygreen_1000_175_p` — MATT - Military Green
- `extrudr_petg_matt-blue_1000_175_p` — MATT - Blue
- `extrudr_petg_matt-red_1000_175_p` — MATT - Red
- `extrudr_petg_matt-transparent_1000_175_p` — MATT - Transparent
- `extrudr_petg_matt-black_1000_285_p` — MATT - Black
- `extrudr_petg_matt-anthracite_1000_285_p` — MATT - Anthracite
- `extrudr_petg_matt-militarygreen_1000_285_p` — MATT - Military Green
- `extrudr_petg_matt-blue_1000_285_p` — MATT - Blue
- `extrudr_petg_matt-red_1000_285_p` — MATT - Red
- `extrudr_petg_matt-transparent_1000_285_p` — MATT - Transparent
- `extrudr_petg_matt-black_2500_175_p` — MATT - Black
- `extrudr_petg_matt-anthracite_2500_175_p` — MATT - Anthracite
- `extrudr_petg_matt-militarygreen_2500_175_p` — MATT - Military Green
- `extrudr_petg_matt-blue_2500_175_p` — MATT - Blue
- `extrudr_petg_matt-red_2500_175_p` — MATT - Red
- `extrudr_petg_matt-transparent_2500_175_p` — MATT - Transparent
- `extrudr_petg_matt-black_2500_285_p` — MATT - Black
- `extrudr_petg_matt-anthracite_2500_285_p` — MATT - Anthracite
- `extrudr_petg_matt-militarygreen_2500_285_p` — MATT - Military Green
- `extrudr_petg_matt-blue_2500_285_p` — MATT - Blue
- `extrudr_petg_matt-red_2500_285_p` — MATT - Red
- `extrudr_petg_matt-transparent_2500_285_p` — MATT - Transparent
- `extrudr_petg_x-whiterec_1000_175_c` — X - White REC
- `extrudr_petg_x-transparentrec_1000_175_c` — X - Transparent REC
- `extrudr_petg_x-blackrec_1000_175_c` — X - Black REC
- `extrudr_petg_x-whiterec_10000_175_c` — X - White REC
- `extrudr_petg_x-transparentrec_10000_175_c` — X - Transparent REC
- `extrudr_petg_x-blackrec_10000_175_c` — X - Black REC
- `extrudr_tpu_flex-whitehard_750_175_p` — FLEX - White Hard
- `extrudr_tpu_flex-transparenthard_750_175_p` — FLEX - Transparent Hard
- `extrudr_tpu_flex-blackhard_750_175_p` — FLEX - Black Hard
- `extrudr_tpu_flex-whitehard_750_285_p` — FLEX - White Hard
- `extrudr_tpu_flex-transparenthard_750_285_p` — FLEX - Transparent Hard
- `extrudr_tpu_flex-blackhard_750_285_p` — FLEX - Black Hard
- `extrudr_tpu_flex-whitehard_2000_175_p` — FLEX - White Hard
- `extrudr_tpu_flex-transparenthard_2000_175_p` — FLEX - Transparent Hard
- `extrudr_tpu_flex-blackhard_2000_175_p` — FLEX - Black Hard
- `extrudr_tpu_flex-whitehard_2000_285_p` — FLEX - White Hard
- `extrudr_tpu_flex-transparenthard_2000_285_p` — FLEX - Transparent Hard
- `extrudr_tpu_flex-blackhard_2000_285_p` — FLEX - Black Hard
- `extrudr_tpu-cf_flex-black-hard_500_175_p` — FLEX - Black - Hard
- `extrudr_tpu-cf_flex-black-hard_2000_175_p` — FLEX - Black - Hard
- `extrudr_tpu_flex-transparent-medium_750_175_p` — FLEX - Transparent - Medium
- `extrudr_tpu_flex-neongreen-medium_750_175_p` — FLEX - Neon Green - Medium
- `extrudr_tpu_flex-navyblue-medium_750_175_p` — FLEX - Navy Blue - Medium
- `extrudr_tpu_flex-white-medium_750_175_p` — FLEX - White - Medium
- `extrudr_tpu_flex-black-medium_750_175_p` — FLEX - Black - Medium
- `extrudr_tpu_flex-anthracite-medium_750_175_p` — FLEX - Anthracite - Medium
- `extrudr_tpu_flex-neonred-medium_750_175_p` — FLEX - Neon Red - Medium
- `extrudr_tpu_flex-hellfirered-medium_750_175_p` — FLEX - Hellfire Red  - Medium
- `extrudr_tpu_flex-neonorange-medium_750_175_p` — FLEX - Neon Orange - Medium
- `extrudr_tpu_flex-neonyellow-medium_750_175_p` — FLEX - Neon Yellow - Medium
- `extrudr_tpu_flex-transparent-medium_750_285_p` — FLEX - Transparent - Medium
- `extrudr_tpu_flex-neongreen-medium_750_285_p` — FLEX - Neon Green - Medium
- `extrudr_tpu_flex-navyblue-medium_750_285_p` — FLEX - Navy Blue - Medium
- `extrudr_tpu_flex-white-medium_750_285_p` — FLEX - White - Medium
- `extrudr_tpu_flex-black-medium_750_285_p` — FLEX - Black - Medium
- `extrudr_tpu_flex-anthracite-medium_750_285_p` — FLEX - Anthracite - Medium
- `extrudr_tpu_flex-neonred-medium_750_285_p` — FLEX - Neon Red - Medium
- `extrudr_tpu_flex-hellfirered-medium_750_285_p` — FLEX - Hellfire Red  - Medium
- `extrudr_tpu_flex-neonorange-medium_750_285_p` — FLEX - Neon Orange - Medium
- `extrudr_tpu_flex-neonyellow-medium_750_285_p` — FLEX - Neon Yellow - Medium
- `extrudr_tpu_flex-transparent-medium_2000_175_p` — FLEX - Transparent - Medium
- `extrudr_tpu_flex-neongreen-medium_2000_175_p` — FLEX - Neon Green - Medium
- `extrudr_tpu_flex-navyblue-medium_2000_175_p` — FLEX - Navy Blue - Medium
- `extrudr_tpu_flex-white-medium_2000_175_p` — FLEX - White - Medium
- `extrudr_tpu_flex-black-medium_2000_175_p` — FLEX - Black - Medium
- `extrudr_tpu_flex-anthracite-medium_2000_175_p` — FLEX - Anthracite - Medium
- `extrudr_tpu_flex-neonred-medium_2000_175_p` — FLEX - Neon Red - Medium
- `extrudr_tpu_flex-hellfirered-medium_2000_175_p` — FLEX - Hellfire Red  - Medium
- `extrudr_tpu_flex-neonorange-medium_2000_175_p` — FLEX - Neon Orange - Medium
- `extrudr_tpu_flex-neonyellow-medium_2000_175_p` — FLEX - Neon Yellow - Medium
- `extrudr_tpu_flex-transparent-medium_2000_285_p` — FLEX - Transparent - Medium
- `extrudr_tpu_flex-neongreen-medium_2000_285_p` — FLEX - Neon Green - Medium
- `extrudr_tpu_flex-navyblue-medium_2000_285_p` — FLEX - Navy Blue - Medium
- `extrudr_tpu_flex-white-medium_2000_285_p` — FLEX - White - Medium
- `extrudr_tpu_flex-black-medium_2000_285_p` — FLEX - Black - Medium
- `extrudr_tpu_flex-anthracite-medium_2000_285_p` — FLEX - Anthracite - Medium
- `extrudr_tpu_flex-neonred-medium_2000_285_p` — FLEX - Neon Red - Medium
- `extrudr_tpu_flex-hellfirered-medium_2000_285_p` — FLEX - Hellfire Red  - Medium
- `extrudr_tpu_flex-neonorange-medium_2000_285_p` — FLEX - Neon Orange - Medium
- `extrudr_tpu_flex-neonyellow-medium_2000_285_p` — FLEX - Neon Yellow - Medium
- `extrudr_tpu_flex-transparent-medium_5000_175_p` — FLEX - Transparent - Medium
- `extrudr_tpu_flex-neongreen-medium_5000_175_p` — FLEX - Neon Green - Medium
- `extrudr_tpu_flex-navyblue-medium_5000_175_p` — FLEX - Navy Blue - Medium
- `extrudr_tpu_flex-white-medium_5000_175_p` — FLEX - White - Medium
- `extrudr_tpu_flex-black-medium_5000_175_p` — FLEX - Black - Medium
- `extrudr_tpu_flex-anthracite-medium_5000_175_p` — FLEX - Anthracite - Medium
- `extrudr_tpu_flex-neonred-medium_5000_175_p` — FLEX - Neon Red - Medium
- `extrudr_tpu_flex-hellfirered-medium_5000_175_p` — FLEX - Hellfire Red  - Medium
- `extrudr_tpu_flex-neonorange-medium_5000_175_p` — FLEX - Neon Orange - Medium
- `extrudr_tpu_flex-neonyellow-medium_5000_175_p` — FLEX - Neon Yellow - Medium
- `extrudr_tpu_flex-transparent-medium_5000_285_p` — FLEX - Transparent - Medium
- `extrudr_tpu_flex-neongreen-medium_5000_285_p` — FLEX - Neon Green - Medium
- `extrudr_tpu_flex-navyblue-medium_5000_285_p` — FLEX - Navy Blue - Medium
- `extrudr_tpu_flex-white-medium_5000_285_p` — FLEX - White - Medium
- `extrudr_tpu_flex-black-medium_5000_285_p` — FLEX - Black - Medium
- `extrudr_tpu_flex-anthracite-medium_5000_285_p` — FLEX - Anthracite - Medium
- `extrudr_tpu_flex-neonred-medium_5000_285_p` — FLEX - Neon Red - Medium
- `extrudr_tpu_flex-hellfirered-medium_5000_285_p` — FLEX - Hellfire Red  - Medium
- `extrudr_tpu_flex-neonorange-medium_5000_285_p` — FLEX - Neon Orange - Medium
- `extrudr_tpu_flex-neonyellow-medium_5000_285_p` — FLEX - Neon Yellow - Medium
- `extrudr_tpu_flex-black-medium-esd_500_175_p` — FLEX - Black - Medium-ESD
- `extrudr_tpu_flex-black-medium-esd_2000_175_p` — FLEX - Black - Medium-ESD
- `extrudr_tpu_flex-transparent-semisoft_750_175_p` — FLEX - Transparent - Semisoft
- `extrudr_tpu_flex-black-semisoft_750_175_p` — FLEX - Black - Semisoft
- `extrudr_tpu_flex-white-semisoft_750_175_p` — FLEX - White - Semisoft
- `extrudr_tpu_flex-transparent-semisoft_750_285_p` — FLEX - Transparent - Semisoft
- `extrudr_tpu_flex-black-semisoft_750_285_p` — FLEX - Black - Semisoft
- `extrudr_tpu_flex-white-semisoft_750_285_p` — FLEX - White - Semisoft
- `extrudr_tpu_flex-transparent-semisoft_2000_175_p` — FLEX - Transparent - Semisoft
- `extrudr_tpu_flex-black-semisoft_2000_175_p` — FLEX - Black - Semisoft
- `extrudr_tpu_flex-white-semisoft_2000_175_p` — FLEX - White - Semisoft
- `extrudr_tpu_flex-transparent-semisoft_2000_285_p` — FLEX - Transparent - Semisoft
- `extrudr_tpu_flex-black-semisoft_2000_285_p` — FLEX - Black - Semisoft
- `extrudr_tpu_flex-white-semisoft_2000_285_p` — FLEX - White - Semisoft
- `extrudr_abs_duraproabsanthracite_1000_175_p` — DuraPro ABS Anthracite
- `extrudr_abs_duraproabsblack_1000_175_p` — DuraPro ABS Black
- `extrudr_abs_duraproabsblue_1000_175_p` — DuraPro ABS Blue
- `extrudr_abs_duraproabsgrey_1000_175_p` — DuraPro ABS Grey
- `extrudr_abs_duraproabsmetallic_1000_175_p` — DuraPro ABS Metallic
- `extrudr_abs_duraproabsnature_1000_175_p` — DuraPro ABS Nature
- `extrudr_abs_duraproabsred_1000_175_p` — DuraPro ABS Red
- `extrudr_abs_duraproabssilver_1000_175_p` — DuraPro ABS Silver
- `extrudr_abs_duraproabswhite_1000_175_p` — DuraPro ABS White
- `extrudr_asa_duraproasaanthracite_1000_175_p` — DuraPro ASA Anthracite
- `extrudr_asa_duraproasablue_1000_175_p` — DuraPro ASA Blue
- `extrudr_asa_duraproasadarksilver_1000_175_p` — DuraPro ASA Dark Silver
- `extrudr_asa_duraproasaemeraldgreen_1000_175_p` — DuraPro ASA Emerald Green
- `extrudr_asa_duraproasametallic_1000_175_p` — DuraPro ASA Metallic
- `extrudr_asa_duraproasanature_1000_175_p` — DuraPro ASA Nature
- `extrudr_asa_duraproasaneongreen_1000_175_p` — DuraPro ASA Neon Green
- `extrudr_asa_duraproasaneonorange_1000_175_p` — DuraPro ASA Neon Orange
- `extrudr_asa_duraproasaneonyellow_1000_175_p` — DuraPro ASA Neon Yellow
- `extrudr_asa_duraproasared_1000_175_p` — DuraPro ASA Red
- `extrudr_asa_duraproasawhite_1000_175_p` — DuraPro ASA White
- `extrudr_asa_duraproasayellow_1000_175_p` — DuraPro ASA Yellow
- `extrudr_asa_durapromatteasablack_1000_175_p` — DuraPro Matte ASA Black
- `extrudr_asa_durapromatteasagrey_1000_175_p` — DuraPro Matte ASA Grey
- `extrudr_pa12_duraprocfpa12black_1000_175_p` — DuraPro CF PA12 Black
- `extrudr_pa12_durapropa12black_1000_175_p` — DuraPro PA12 Black
- `extrudr_pa12_durapropa12transparent_1000_175_p` — DuraPro PA12 Transparent
- `extrudr_pa12_durapropa12white_1000_175_p` — DuraPro PA12 White
- `extrudr_pc_durapropbtpcblack_1000_175_p` — DuraPro PBT PC Black
- `extrudr_pc_durapropbtpcwhite_1000_175_p` — DuraPro PBT PC White
- `extrudr_pctg_pctganthracite_1000_175_p` — PCTG Anthracite
- `extrudr_pctg_pctgblack_1000_175_p` — PCTG Black
- `extrudr_pctg_pctghellfirered_1000_175_p` — PCTG Hellfire Red
- `extrudr_pctg_pctgmetallic_1000_175_p` — PCTG Metallic
- `extrudr_pctg_pctgnavyblue_1000_175_p` — PCTG Navy Blue
- `extrudr_pctg_pctgred_1000_175_p` — PCTG Red
- `extrudr_pctg_pctgsilver_1000_175_p` — PCTG Silver
- `extrudr_pctg_pctgtransparent_1000_175_p` — PCTG transparent
- `extrudr_pctg_pctgwhite_1000_175_p` — PCTG White
- `extrudr_petg_glowpetgglowex_1000_175_p` — Glow PETG Glowex
- `extrudr_petg_petganthracite_1000_175_p` — PETG Anthracite
- `extrudr_petg_petgblack_1000_175_p` — PETG Black
- `extrudr_petg_petgbronze_1000_175_p` — PETG Bronze
- `extrudr_petg_petgcopper_1000_175_p` — PETG Copper
- `extrudr_petg_petgemeraldgreen_1000_175_p` — PETG Emerald Green
- `extrudr_petg_petggold_1000_175_p` — PETG Gold
- `extrudr_petg_petggrey_1000_175_p` — PETG Grey
- `extrudr_petg_petghellfirered_1000_175_p` — PETG Hellfire Red
- `extrudr_petg_petglightblue_1000_175_p` — PETG Light Blue
- `extrudr_petg_petgmagenta_1000_175_p` — PETG Magenta
- `extrudr_petg_petgmetallic_1000_175_p` — PETG Metallic
- `extrudr_petg_petgmilitarygreen_1000_175_p` — PETG Military Green
- `extrudr_petg_petgnavyblue_1000_175_p` — PETG Navy Blue
- `extrudr_petg_petgneongreen_1000_175_p` — PETG Neon Green
- `extrudr_petg_petgneonorange_1000_175_p` — PETG Neon Orange
- `extrudr_petg_petgneonred_1000_175_p` — PETG Neon Red
- `extrudr_petg_petgneonyellow_1000_175_p` — PETG Neon Yellow
- `extrudr_petg_petgorange_1000_175_p` — PETG Orange
- `extrudr_petg_petgpurple_1000_175_p` — PETG Purple
- `extrudr_petg_petgred_1000_175_p` — PETG Red
- `extrudr_petg_petgsignalgreen_1000_175_p` — PETG Signal Green
- `extrudr_petg_petgsilver_1000_175_p` — PETG Silver
- `extrudr_petg_petgtransparent_1000_175_p` — PETG transparent
- `extrudr_petg_petgtransparentblue_1000_175_p` — PETG Transparent Blue
- `extrudr_petg_petgtransparentgreen_1000_175_p` — PETG Transparent Green
- `extrudr_petg_petgtransparentorange_1000_175_p` — PETG Transparent Orange
- `extrudr_petg_petgtransparentred_1000_175_p` — PETG Transparent Red
- `extrudr_petg_petgtransparentyellow_1000_175_p` — PETG Transparent Yellow
- `extrudr_petg_petgturquoise_1000_175_p` — PETG Turquoise
- `extrudr_petg_petgwhite_1000_175_p` — PETG White
- `extrudr_petg_petgyellow_1000_175_p` — PETG Yellow
- `extrudr_pla_biofusionplabluefire_1000_175_p` — BioFusion PLA Blue Fire
- `extrudr_pla_biofusionplacherryred_1000_175_p` — BioFusion PLA Cherry Red
- `extrudr_pla_biofusionplajetblack_1000_175_p` — BioFusion PLA Jet Black
- `extrudr_pla_biofusionplametallicgrey_1000_175_p` — BioFusion PLA Metallic Grey
- `extrudr_pla_biofusionplareptilegreen_1000_175_p` — BioFusion PLA Reptile Green
- `extrudr_pla_biofusionsilkplaarcticwhite_1000_175_p` — BioFusion Silk PLA Arctic White
- `extrudr_pla_biofusionsilkplaepicpurple_1000_175_p` — BioFusion Silk PLA Epic Purple
- `extrudr_pla_biofusionsilkplaincagold_1000_175_p` — BioFusion Silk PLA Inca Gold
- `extrudr_pla_biofusionsilkplaquicksilver_1000_175_p` — BioFusion Silk PLA Quicksilver
- `extrudr_pla_biofusionsilkplasteampunkcopper_1000_175_p` — BioFusion Silk PLA Steampunk Copper
- `extrudr_pla_biofusionsilkplavenomgreen_1000_175_p` — BioFusion Silk PLA Venom Green
- `extrudr_pla_flaxplanature_1000_175_p` — Flax PLA Nature
- `extrudr_pla_greentecmatteplaanthracite_1000_175_p` — GreenTEC Matte PLA Anthracite
- `extrudr_pla_greentecmatteplablack_1000_175_p` — GreenTEC Matte PLA Black
- `extrudr_pla_greentecmatteplanature_1000_175_p` — GreenTEC Matte PLA Nature
- `extrudr_pla_greentecmatteplanavyblue_1000_175_p` — GreenTEC Matte PLA Navy Blue
- `extrudr_pla_greentecmatteplared_1000_175_p` — GreenTEC Matte PLA Red
- `extrudr_pla_greentecmatteplasilver_1000_175_p` — GreenTEC Matte PLA Silver
- `extrudr_pla_greentecmatteplawhite_1000_175_p` — GreenTEC Matte PLA White
- `extrudr_pla_greentecplaanthracite_1000_175_p` — GreenTEC PLA Anthracite
- `extrudr_pla_greentecplablack_1000_175_p` — GreenTEC PLA Black
- `extrudr_pla_greentecplahellfirered_1000_175_p` — GreenTEC PLA Hellfire Red
- `extrudr_pla_greentecplanature_1000_175_p` — GreenTEC PLA Nature
- `extrudr_pla_greentecplanavyblue_1000_175_p` — GreenTEC PLA Navy Blue
- `extrudr_pla_greentecplasilver_1000_175_p` — GreenTEC PLA Silver
- `extrudr_pla_greentecplawhite_1000_175_p` — GreenTEC PLA White
- `extrudr_pla_planx2matttrafficyellow_1000_175_p` — PLA NX2 Matt Traffic Yellow
- `extrudr_pla_pearlplanature_1000_175_p` — Pearl PLA Nature
- `extrudr_pla_woodpladarkwood_1000_175_p` — Wood PLA Dark Wood
- `extrudr_pla_woodplanature_1000_175_p` — Wood PLA Nature
- `extrudr_tpu_flexhardcftpublack_1000_175_p` — FLEX Hard CF TPU Black
- `extrudr_tpu_flexhardtpublack_1000_175_p` — FLEX Hard TPU Black
- `extrudr_tpu_flexhardtputransparent_1000_175_p` — FLEX Hard TPU Transparent
- `extrudr_tpu_flexhardtpuwhite_1000_175_p` — FLEX Hard TPU White
- `extrudr_tpu_flexmediumtpuanthracite_1000_175_p` — FLEX Medium TPU Anthracite
- `extrudr_tpu_flexmediumtpublack_1000_175_p` — FLEX Medium TPU Black
- `extrudr_tpu_flexmediumtpuesdblack_1000_175_p` — FLEX Medium TPU ESD Black
- `extrudr_tpu_flexmediumtpuhellfirered_1000_175_p` — FLEX Medium TPU Hellfire Red
- `extrudr_tpu_flexmediumtpunavyblue_1000_175_p` — FLEX Medium TPU Navy Blue
- `extrudr_tpu_flexmediumtpuneongreen_1000_175_p` — FLEX Medium TPU Neon Green
- `extrudr_tpu_flexmediumtpuneonorange_1000_175_p` — FLEX Medium TPU Neon Orange
- `extrudr_tpu_flexmediumtpuneonred_1000_175_p` — FLEX Medium TPU Neon Red
- `extrudr_tpu_flexmediumtpuneonyellow_1000_175_p` — FLEX Medium TPU Neon Yellow
- `extrudr_tpu_flexmediumtputransparent_1000_175_p` — FLEX Medium TPU Transparent
- `extrudr_tpu_flexmediumtpuwhite_1000_175_p` — FLEX Medium TPU White
- `extrudr_tpu_flexsemisofttpublack_1000_175_p` — FLEX Semisoft TPU Black
- `extrudr_tpu_flexsemisofttputransparent_1000_175_p` — FLEX Semisoft TPU Transparent
- `extrudr_tpu_flexsemisofttpuwhite_1000_175_p` — FLEX Semisoft TPU White
- `extrudr_pla_plahsblack_1000_175_p` — PLA HS Black
- `extrudr_pla_plahswhite_1000_175_p` — PLA HS White
- `extrudr_pla_plahsneongreen_1000_175_p` — PLA HS Neon Green
- `extrudr_pla_plahsneonorange_1000_175_p` — PLA HS Neon Orange
- `extrudr_pla_plahsneonyellow_1000_175_p` — PLA HS Neon Yellow
- `extrudr_pla_plahshellfirered_1000_175_p` — PLA HS Hellfire Red
- `extrudr_pla_plahsnavyblue_1000_175_p` — PLA HS Navy Blue
- `extrudr_pla_plahsanthracite_1000_175_p` — PLA HS Anthracite
- `extrudr_pla_plahsmetallic_1000_175_p` — PLA HS Metallic
- `extrudr_pla_plahssilver_1000_175_p` — PLA HS Silver
- `extrudr_pla_plahsgrey_1000_175_p` — PLA HS Grey
- `extrudr_pla_plahsmilitarybeige_1000_175_p` — PLA HS Military Beige
- `extrudr_pla_plahsyellow_1000_175_p` — PLA HS Yellow
- `extrudr_pla_plahsorange_1000_175_p` — PLA HS Orange
- `extrudr_pla_plahsred_1000_175_p` — PLA HS Red
- `extrudr_pla_plahslightblue_1000_175_p` — PLA HS Light Blue
- `extrudr_pla_plahsturquoise_1000_175_p` — PLA HS Turquoise
- `extrudr_pla_plahsmilitarygreen_1000_175_p` — PLA HS Military Green
- `extrudr_pla_plahsmilitarydarkgreen_1000_175_p` — PLA HS Military Dark Green
- `extrudr_pla_plahsbrown_1000_175_p` — PLA HS Brown
- `extrudr_pla_plahspastelgreen_1000_175_p` — PLA HS Pastel Green
- `extrudr_pla_plahspastelblue_1000_175_p` — PLA HS Pastel Blue
