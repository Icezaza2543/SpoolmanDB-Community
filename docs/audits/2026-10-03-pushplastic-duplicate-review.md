# pushplastic duplicate migration review

Base `f7a3b6bf3e6c3b515aa238da89c661a35f5a27e6`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `812cc99f3a70de1453f01a2c7b4e2d9ecee31d39489eaa215ce20d58f8108354`.

## Authorization and result

{"groups": 29, "approved_groups": 29, "retired": 29, "deferred": 0, "hard_stops": 0, "before_count": 51945, "after_count": 51916, "brand_before": 280, "brand_after": 251, "registry_before": 1489, "registry_after": 1518, "metadata_fields_changed": 34, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

29 Rule2 survivors;17ABS exact current ranges230–260/90–110 corrected to220–250/100–120, preserving valid density1.03 and matching doclink.12PETG density1.27/nozzle235–250/bed90 already agree with exact standard manufacturer settings; keep. No code/EAN transfers. Cartesian source shape does not decide survivor. HEX/tare conflicts unresolved; all uniqueweights/colors and packaging/tare untouched.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://www.pushplastic.com/pages/print-settings", "note": "Manufacturer standard settings distinct from Bambu profiles."}
- {"url": "https://cdn.shopify.com/s/files/1/0260/7421/files/ABS_print_settings.pdf?v=1683905833", "nozzle": [220, 250], "bed": [100, 120], "preferred": [230, 110]}
- {"url": "https://cdn.shopify.com/s/files/1/0260/7421/files/PETG_print_settings.pdf?v=1683905833", "nozzle": [235, 250], "bed": [80, 100], "preferred": [240, 90]}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`pushplastic_abs_pushplasticabsblack_1000_175_p`|`pushplastic_abs_absblack_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic ABS {color_name}::Push Plastic ABS Black::ABS::1000::1.75::plastic::False`|
|`pushplastic_abs_pushplasticabsbronzemetallic_1000_175_p`|`pushplastic_abs_absbronzemetallic_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic ABS {color_name}::Push Plastic ABS Bronze Metallic::ABS::1000::1.75::plastic::False`|
|`pushplastic_abs_pushplasticabsbrown_1000_175_p`|`pushplastic_abs_absbrown_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic ABS {color_name}::Push Plastic ABS Brown::ABS::1000::1.75::plastic::False`|
|`pushplastic_abs_pushplasticabsdarkgrey_1000_175_p`|`pushplastic_abs_absdarkgrey_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic ABS {color_name}::Push Plastic ABS Dark Grey::ABS::1000::1.75::plastic::False`|
|`pushplastic_abs_pushplasticabsflatdarkearth_1000_175_p`|`pushplastic_abs_absflatdarkearth_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic ABS {color_name}::Push Plastic ABS Flat Dark Earth::ABS::1000::1.75::plastic::False`|
|`pushplastic_abs_pushplasticabsgoldmetallic_1000_175_p`|`pushplastic_abs_absgoldmetallic_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic ABS {color_name}::Push Plastic ABS Gold Metallic::ABS::1000::1.75::plastic::False`|
|`pushplastic_abs_pushplasticabsgreen_1000_175_p`|`pushplastic_abs_absgreen_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic ABS {color_name}::Push Plastic ABS Green::ABS::1000::1.75::plastic::False`|
|`pushplastic_abs_pushplasticabslightgrey_1000_175_p`|`pushplastic_abs_abslightgrey_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic ABS {color_name}::Push Plastic ABS Light Grey::ABS::1000::1.75::plastic::False`|
|`pushplastic_abs_pushplasticabsnatural_1000_175_p`|`pushplastic_abs_absnatural_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic ABS {color_name}::Push Plastic ABS Natural::ABS::1000::1.75::plastic::False`|
|`pushplastic_abs_pushplasticabsoceanblue_1000_175_p`|`pushplastic_abs_absoceanblue_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic ABS {color_name}::Push Plastic ABS Ocean Blue::ABS::1000::1.75::plastic::False`|
|`pushplastic_abs_pushplasticabsorange_1000_175_p`|`pushplastic_abs_absorange_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic ABS {color_name}::Push Plastic ABS Orange::ABS::1000::1.75::plastic::False`|
|`pushplastic_abs_pushplasticabspink_1000_175_p`|`pushplastic_abs_abspink_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic ABS {color_name}::Push Plastic ABS Pink::ABS::1000::1.75::plastic::False`|
|`pushplastic_abs_pushplasticabspurple_1000_175_p`|`pushplastic_abs_abspurple_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic ABS {color_name}::Push Plastic ABS Purple::ABS::1000::1.75::plastic::False`|
|`pushplastic_abs_pushplasticabssilvermetallic_1000_175_p`|`pushplastic_abs_abssilvermetallic_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic ABS {color_name}::Push Plastic ABS Silver Metallic::ABS::1000::1.75::plastic::False`|
|`pushplastic_abs_pushplasticabsultrablue_1000_175_p`|`pushplastic_abs_absultrablue_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic ABS {color_name}::Push Plastic ABS Ultra Blue::ABS::1000::1.75::plastic::False`|
|`pushplastic_abs_pushplasticabswhite_1000_175_p`|`pushplastic_abs_abswhite_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic ABS {color_name}::Push Plastic ABS White::ABS::1000::1.75::plastic::False`|
|`pushplastic_abs_pushplasticabsyellow_1000_175_p`|`pushplastic_abs_absyellow_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic ABS {color_name}::Push Plastic ABS Yellow::ABS::1000::1.75::plastic::False`|
|`pushplastic_petg_pushplasticpetgblack_1000_175_p`|`pushplastic_petg_petgblack_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic PETG {color_name}::Push Plastic PETG Black::PETG::1000::1.75::plastic::False`|
|`pushplastic_petg_pushplasticpetggreen_1000_175_p`|`pushplastic_petg_petggreen_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic PETG {color_name}::Push Plastic PETG Green::PETG::1000::1.75::plastic::False`|
|`pushplastic_petg_pushplasticpetglightgrey_1000_175_p`|`pushplastic_petg_petglightgrey_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic PETG {color_name}::Push Plastic PETG Light Grey::PETG::1000::1.75::plastic::False`|
|`pushplastic_petg_pushplasticpetgorange_1000_175_p`|`pushplastic_petg_petgorange_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic PETG {color_name}::Push Plastic PETG Orange::PETG::1000::1.75::plastic::False`|
|`pushplastic_petg_pushplasticpetgred_1000_175_p`|`pushplastic_petg_petgred_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic PETG {color_name}::Push Plastic PETG Red::PETG::1000::1.75::plastic::False`|
|`pushplastic_petg_pushplasticpetgrust_1000_175_p`|`pushplastic_petg_petgrust_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic PETG {color_name}::Push Plastic PETG Rust::PETG::1000::1.75::plastic::False`|
|`pushplastic_petg_pushplasticpetgsilvermetallic_1000_175_p`|`pushplastic_petg_petgsilvermetallic_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic PETG {color_name}::Push Plastic PETG Silver Metallic::PETG::1000::1.75::plastic::False`|
|`pushplastic_petg_pushplasticpetgtranslucentamber_1000_175_p`|`pushplastic_petg_petgtranslucentamber_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic PETG {color_name}::Push Plastic PETG Translucent Amber::PETG::1000::1.75::plastic::False`|
|`pushplastic_petg_pushplasticpetgtranslucentblue_1000_175_p`|`pushplastic_petg_petgtranslucentblue_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic PETG {color_name}::Push Plastic PETG Translucent Blue::PETG::1000::1.75::plastic::False`|
|`pushplastic_petg_pushplasticpetgtranslucentgreen_1000_175_p`|`pushplastic_petg_petgtranslucentgreen_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic PETG {color_name}::Push Plastic PETG Translucent Green::PETG::1000::1.75::plastic::False`|
|`pushplastic_petg_pushplasticpetgultrablue_1000_175_p`|`pushplastic_petg_petgultrablue_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic PETG {color_name}::Push Plastic PETG Ultra Blue::PETG::1000::1.75::plastic::False`|
|`pushplastic_petg_pushplasticpetgwhite_1000_175_p`|`pushplastic_petg_petgwhite_1000_175_p`|`pushplastic.json::Push Plastic::Push Plastic PETG {color_name}::Push Plastic PETG White::PETG::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### PP001: dup-981d9d1bea05169fc683eb2b771701112bda66f502763f7d7ff4d13879f5d4ae

Status: APPROVED; survivor `pushplastic_abs_absblack_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_abs_absblack_1000_175_p`|`ABS {color_name}`|`Black`|{"source_file": "pushplastic.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / False|
|`pushplastic_abs_pushplasticabsblack_1000_175_p`|`Push Plastic ABS {color_name}`|`Black`|{"source_file": "pushplastic.json", "definition_index": 2, "weights": 3, "diameters": 1, "colors": 20, "compiled_records": 60} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_abs_absblack_1000_175_p": "000000",
    "pushplastic_abs_pushplasticabsblack_1000_175_p": "1a1a1a"
  },
  "extruder_temp_range": {
    "pushplastic_abs_absblack_1000_175_p": [
      230,
      260
    ],
    "pushplastic_abs_pushplasticabsblack_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "pushplastic_abs_absblack_1000_175_p": [
      90,
      110
    ],
    "pushplastic_abs_pushplasticabsblack_1000_175_p": [
      100,
      120
    ]
  }
}
```

### PP002: dup-074ff541f4983ee7330c3261622fdc8cd1105ba4992ff88a5d0ee4a066091b75

Status: APPROVED; survivor `pushplastic_abs_absbronzemetallic_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_abs_absbronzemetallic_1000_175_p`|`ABS {color_name}`|`Bronze Metallic`|{"source_file": "pushplastic.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / False|
|`pushplastic_abs_pushplasticabsbronzemetallic_1000_175_p`|`Push Plastic ABS {color_name}`|`Bronze Metallic`|{"source_file": "pushplastic.json", "definition_index": 2, "weights": 3, "diameters": 1, "colors": 20, "compiled_records": 60} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_abs_absbronzemetallic_1000_175_p": "805F3C",
    "pushplastic_abs_pushplasticabsbronzemetallic_1000_175_p": "8c6239"
  },
  "extruder_temp_range": {
    "pushplastic_abs_absbronzemetallic_1000_175_p": [
      230,
      260
    ],
    "pushplastic_abs_pushplasticabsbronzemetallic_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "pushplastic_abs_absbronzemetallic_1000_175_p": [
      90,
      110
    ],
    "pushplastic_abs_pushplasticabsbronzemetallic_1000_175_p": [
      100,
      120
    ]
  }
}
```

### PP003: dup-bb17be9f0b9a5ab29a57d61d95be65d2e902bdb102895091c46e3565454ffe29

Status: APPROVED; survivor `pushplastic_abs_absbrown_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_abs_absbrown_1000_175_p`|`ABS {color_name}`|`Brown`|{"source_file": "pushplastic.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / False|
|`pushplastic_abs_pushplasticabsbrown_1000_175_p`|`Push Plastic ABS {color_name}`|`Brown`|{"source_file": "pushplastic.json", "definition_index": 2, "weights": 3, "diameters": 1, "colors": 20, "compiled_records": 60} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_abs_absbrown_1000_175_p": "694D3F",
    "pushplastic_abs_pushplasticabsbrown_1000_175_p": "6b3e2e"
  },
  "extruder_temp_range": {
    "pushplastic_abs_absbrown_1000_175_p": [
      230,
      260
    ],
    "pushplastic_abs_pushplasticabsbrown_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "pushplastic_abs_absbrown_1000_175_p": [
      90,
      110
    ],
    "pushplastic_abs_pushplasticabsbrown_1000_175_p": [
      100,
      120
    ]
  }
}
```

### PP004: dup-9361844e46c74da350805f24e793b19ab704e4acd597c55af2ab77e8db12b920

Status: APPROVED; survivor `pushplastic_abs_absdarkgrey_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_abs_absdarkgrey_1000_175_p`|`ABS {color_name}`|`Dark Grey`|{"source_file": "pushplastic.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / False|
|`pushplastic_abs_pushplasticabsdarkgrey_1000_175_p`|`Push Plastic ABS {color_name}`|`Dark Grey`|{"source_file": "pushplastic.json", "definition_index": 2, "weights": 3, "diameters": 1, "colors": 20, "compiled_records": 60} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_abs_absdarkgrey_1000_175_p": "6A6C6E",
    "pushplastic_abs_pushplasticabsdarkgrey_1000_175_p": "4a4a4a"
  },
  "extruder_temp_range": {
    "pushplastic_abs_absdarkgrey_1000_175_p": [
      230,
      260
    ],
    "pushplastic_abs_pushplasticabsdarkgrey_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "pushplastic_abs_absdarkgrey_1000_175_p": [
      90,
      110
    ],
    "pushplastic_abs_pushplasticabsdarkgrey_1000_175_p": [
      100,
      120
    ]
  }
}
```

### PP005: dup-ab780c46aa70ee6c4a834bb09dc3588201c0988f4099360ec88d2f1ff7fd6fc2

Status: APPROVED; survivor `pushplastic_abs_absflatdarkearth_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_abs_absflatdarkearth_1000_175_p`|`ABS {color_name}`|`Flat Dark Earth`|{"source_file": "pushplastic.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / False|
|`pushplastic_abs_pushplasticabsflatdarkearth_1000_175_p`|`Push Plastic ABS {color_name}`|`Flat Dark Earth`|{"source_file": "pushplastic.json", "definition_index": 2, "weights": 3, "diameters": 1, "colors": 20, "compiled_records": 60} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_abs_absflatdarkearth_1000_175_p": "90785E",
    "pushplastic_abs_pushplasticabsflatdarkearth_1000_175_p": "8b7355"
  },
  "extruder_temp_range": {
    "pushplastic_abs_absflatdarkearth_1000_175_p": [
      230,
      260
    ],
    "pushplastic_abs_pushplasticabsflatdarkearth_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "pushplastic_abs_absflatdarkearth_1000_175_p": [
      90,
      110
    ],
    "pushplastic_abs_pushplasticabsflatdarkearth_1000_175_p": [
      100,
      120
    ]
  }
}
```

### PP006: dup-335beb93386e3e6f3feea974b462f15af193c9626adea537bfd7d684b15016da

Status: APPROVED; survivor `pushplastic_abs_absgoldmetallic_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_abs_absgoldmetallic_1000_175_p`|`ABS {color_name}`|`Gold Metallic`|{"source_file": "pushplastic.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / False|
|`pushplastic_abs_pushplasticabsgoldmetallic_1000_175_p`|`Push Plastic ABS {color_name}`|`Gold Metallic`|{"source_file": "pushplastic.json", "definition_index": 2, "weights": 3, "diameters": 1, "colors": 20, "compiled_records": 60} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_abs_absgoldmetallic_1000_175_p": "6E5E2F",
    "pushplastic_abs_pushplasticabsgoldmetallic_1000_175_p": "c9a227"
  },
  "extruder_temp_range": {
    "pushplastic_abs_absgoldmetallic_1000_175_p": [
      230,
      260
    ],
    "pushplastic_abs_pushplasticabsgoldmetallic_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "pushplastic_abs_absgoldmetallic_1000_175_p": [
      90,
      110
    ],
    "pushplastic_abs_pushplasticabsgoldmetallic_1000_175_p": [
      100,
      120
    ]
  }
}
```

### PP007: dup-81a128ec78d3771fd91702c845c489da108e0f886181527a6de2508d5d0c0322

Status: APPROVED; survivor `pushplastic_abs_absgreen_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_abs_absgreen_1000_175_p`|`ABS {color_name}`|`Green`|{"source_file": "pushplastic.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / False|
|`pushplastic_abs_pushplasticabsgreen_1000_175_p`|`Push Plastic ABS {color_name}`|`Green`|{"source_file": "pushplastic.json", "definition_index": 2, "weights": 3, "diameters": 1, "colors": 20, "compiled_records": 60} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_abs_absgreen_1000_175_p": "26A648",
    "pushplastic_abs_pushplasticabsgreen_1000_175_p": "2e7d32"
  },
  "extruder_temp_range": {
    "pushplastic_abs_absgreen_1000_175_p": [
      230,
      260
    ],
    "pushplastic_abs_pushplasticabsgreen_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "pushplastic_abs_absgreen_1000_175_p": [
      90,
      110
    ],
    "pushplastic_abs_pushplasticabsgreen_1000_175_p": [
      100,
      120
    ]
  }
}
```

### PP008: dup-27bc6de6bac6c1f79f15052a3689bace21170f94453363fdd2a47a4b7bf95a3b

Status: APPROVED; survivor `pushplastic_abs_abslightgrey_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_abs_abslightgrey_1000_175_p`|`ABS {color_name}`|`Light Grey`|{"source_file": "pushplastic.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / False|
|`pushplastic_abs_pushplasticabslightgrey_1000_175_p`|`Push Plastic ABS {color_name}`|`Light Grey`|{"source_file": "pushplastic.json", "definition_index": 2, "weights": 3, "diameters": 1, "colors": 20, "compiled_records": 60} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_abs_abslightgrey_1000_175_p": "C5C5BF",
    "pushplastic_abs_pushplasticabslightgrey_1000_175_p": "a0a0a0"
  },
  "extruder_temp_range": {
    "pushplastic_abs_abslightgrey_1000_175_p": [
      230,
      260
    ],
    "pushplastic_abs_pushplasticabslightgrey_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "pushplastic_abs_abslightgrey_1000_175_p": [
      90,
      110
    ],
    "pushplastic_abs_pushplasticabslightgrey_1000_175_p": [
      100,
      120
    ]
  }
}
```

### PP009: dup-64a2765a9693869d0e2297c641f5ef30218acfcd85d9f108bcf8837c98771340

Status: APPROVED; survivor `pushplastic_abs_absnatural_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_abs_absnatural_1000_175_p`|`ABS {color_name}`|`Natural`|{"source_file": "pushplastic.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / False|
|`pushplastic_abs_pushplasticabsnatural_1000_175_p`|`Push Plastic ABS {color_name}`|`Natural`|{"source_file": "pushplastic.json", "definition_index": 2, "weights": 3, "diameters": 1, "colors": 20, "compiled_records": 60} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_abs_absnatural_1000_175_p": "DFDFD3",
    "pushplastic_abs_pushplasticabsnatural_1000_175_p": "e8e0d0"
  },
  "extruder_temp_range": {
    "pushplastic_abs_absnatural_1000_175_p": [
      230,
      260
    ],
    "pushplastic_abs_pushplasticabsnatural_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "pushplastic_abs_absnatural_1000_175_p": [
      90,
      110
    ],
    "pushplastic_abs_pushplasticabsnatural_1000_175_p": [
      100,
      120
    ]
  }
}
```

### PP010: dup-7a804c543d83de8b3b02c30d4c3c638f738f586d8cc83a4b511af23797db9f05

Status: APPROVED; survivor `pushplastic_abs_absoceanblue_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_abs_absoceanblue_1000_175_p`|`ABS {color_name}`|`Ocean Blue`|{"source_file": "pushplastic.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / False|
|`pushplastic_abs_pushplasticabsoceanblue_1000_175_p`|`Push Plastic ABS {color_name}`|`Ocean Blue`|{"source_file": "pushplastic.json", "definition_index": 2, "weights": 3, "diameters": 1, "colors": 20, "compiled_records": 60} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_abs_absoceanblue_1000_175_p": "40B6E4",
    "pushplastic_abs_pushplasticabsoceanblue_1000_175_p": "1b6b8a"
  },
  "extruder_temp_range": {
    "pushplastic_abs_absoceanblue_1000_175_p": [
      230,
      260
    ],
    "pushplastic_abs_pushplasticabsoceanblue_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "pushplastic_abs_absoceanblue_1000_175_p": [
      90,
      110
    ],
    "pushplastic_abs_pushplasticabsoceanblue_1000_175_p": [
      100,
      120
    ]
  }
}
```

### PP011: dup-c59cd553591c1d439bf39475ba23e0d970d6b938da1080d75d06ca83623e3c26

Status: APPROVED; survivor `pushplastic_abs_absorange_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_abs_absorange_1000_175_p`|`ABS {color_name}`|`Orange`|{"source_file": "pushplastic.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / False|
|`pushplastic_abs_pushplasticabsorange_1000_175_p`|`Push Plastic ABS {color_name}`|`Orange`|{"source_file": "pushplastic.json", "definition_index": 2, "weights": 3, "diameters": 1, "colors": 20, "compiled_records": 60} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_abs_absorange_1000_175_p": "FF5F2E",
    "pushplastic_abs_pushplasticabsorange_1000_175_p": "f57c00"
  },
  "extruder_temp_range": {
    "pushplastic_abs_absorange_1000_175_p": [
      230,
      260
    ],
    "pushplastic_abs_pushplasticabsorange_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "pushplastic_abs_absorange_1000_175_p": [
      90,
      110
    ],
    "pushplastic_abs_pushplasticabsorange_1000_175_p": [
      100,
      120
    ]
  }
}
```

### PP012: dup-6567f0506813ddb2dcfa687282225ea9b7039e66a7c54c6222e2ef34bcb02ea2

Status: APPROVED; survivor `pushplastic_abs_abspink_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_abs_abspink_1000_175_p`|`ABS {color_name}`|`Pink`|{"source_file": "pushplastic.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / False|
|`pushplastic_abs_pushplasticabspink_1000_175_p`|`Push Plastic ABS {color_name}`|`Pink`|{"source_file": "pushplastic.json", "definition_index": 2, "weights": 3, "diameters": 1, "colors": 20, "compiled_records": 60} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_abs_abspink_1000_175_p": "FF72B6",
    "pushplastic_abs_pushplasticabspink_1000_175_p": "e873a5"
  },
  "extruder_temp_range": {
    "pushplastic_abs_abspink_1000_175_p": [
      230,
      260
    ],
    "pushplastic_abs_pushplasticabspink_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "pushplastic_abs_abspink_1000_175_p": [
      90,
      110
    ],
    "pushplastic_abs_pushplasticabspink_1000_175_p": [
      100,
      120
    ]
  }
}
```

### PP013: dup-a59d344a5ad11ae6eb443d3decc61852d6584a3ba76e4cc02c57021e2748d055

Status: APPROVED; survivor `pushplastic_abs_abspurple_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_abs_abspurple_1000_175_p`|`ABS {color_name}`|`Purple`|{"source_file": "pushplastic.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / False|
|`pushplastic_abs_pushplasticabspurple_1000_175_p`|`Push Plastic ABS {color_name}`|`Purple`|{"source_file": "pushplastic.json", "definition_index": 2, "weights": 3, "diameters": 1, "colors": 20, "compiled_records": 60} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_abs_abspurple_1000_175_p": "AE00FF",
    "pushplastic_abs_pushplasticabspurple_1000_175_p": "6a1b9a"
  },
  "extruder_temp_range": {
    "pushplastic_abs_abspurple_1000_175_p": [
      230,
      260
    ],
    "pushplastic_abs_pushplasticabspurple_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "pushplastic_abs_abspurple_1000_175_p": [
      90,
      110
    ],
    "pushplastic_abs_pushplasticabspurple_1000_175_p": [
      100,
      120
    ]
  }
}
```

### PP014: dup-68965106718346c11a9ed9d837c09c76a72a68ee715aa3c5901f9bfb3ccdf042

Status: APPROVED; survivor `pushplastic_abs_abssilvermetallic_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_abs_abssilvermetallic_1000_175_p`|`ABS {color_name}`|`Silver Metallic`|{"source_file": "pushplastic.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / False|
|`pushplastic_abs_pushplasticabssilvermetallic_1000_175_p`|`Push Plastic ABS {color_name}`|`Silver Metallic`|{"source_file": "pushplastic.json", "definition_index": 2, "weights": 3, "diameters": 1, "colors": 20, "compiled_records": 60} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_abs_abssilvermetallic_1000_175_p": "848484",
    "pushplastic_abs_pushplasticabssilvermetallic_1000_175_p": "b0b0b0"
  },
  "extruder_temp_range": {
    "pushplastic_abs_abssilvermetallic_1000_175_p": [
      230,
      260
    ],
    "pushplastic_abs_pushplasticabssilvermetallic_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "pushplastic_abs_abssilvermetallic_1000_175_p": [
      90,
      110
    ],
    "pushplastic_abs_pushplasticabssilvermetallic_1000_175_p": [
      100,
      120
    ]
  }
}
```

### PP015: dup-218f59fd29f75613e1511e3c7eeff3b2346585a43958c35ebf470e3d7e66c2b7

Status: APPROVED; survivor `pushplastic_abs_absultrablue_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_abs_absultrablue_1000_175_p`|`ABS {color_name}`|`Ultra Blue`|{"source_file": "pushplastic.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / False|
|`pushplastic_abs_pushplasticabsultrablue_1000_175_p`|`Push Plastic ABS {color_name}`|`Ultra Blue`|{"source_file": "pushplastic.json", "definition_index": 2, "weights": 3, "diameters": 1, "colors": 20, "compiled_records": 60} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_abs_absultrablue_1000_175_p": "0022FF",
    "pushplastic_abs_pushplasticabsultrablue_1000_175_p": "005fe8"
  },
  "extruder_temp_range": {
    "pushplastic_abs_absultrablue_1000_175_p": [
      230,
      260
    ],
    "pushplastic_abs_pushplasticabsultrablue_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "pushplastic_abs_absultrablue_1000_175_p": [
      90,
      110
    ],
    "pushplastic_abs_pushplasticabsultrablue_1000_175_p": [
      100,
      120
    ]
  }
}
```

### PP016: dup-c2f4bc7fd94bd29a1e85a8756662e006709de4e6f8b2be44f485187a430fb5ac

Status: APPROVED; survivor `pushplastic_abs_abswhite_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_abs_abswhite_1000_175_p`|`ABS {color_name}`|`White`|{"source_file": "pushplastic.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / False|
|`pushplastic_abs_pushplasticabswhite_1000_175_p`|`Push Plastic ABS {color_name}`|`White`|{"source_file": "pushplastic.json", "definition_index": 2, "weights": 3, "diameters": 1, "colors": 20, "compiled_records": 60} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_abs_abswhite_1000_175_p": "FFFFFF",
    "pushplastic_abs_pushplasticabswhite_1000_175_p": "f5f5f5"
  },
  "extruder_temp_range": {
    "pushplastic_abs_abswhite_1000_175_p": [
      230,
      260
    ],
    "pushplastic_abs_pushplasticabswhite_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "pushplastic_abs_abswhite_1000_175_p": [
      90,
      110
    ],
    "pushplastic_abs_pushplasticabswhite_1000_175_p": [
      100,
      120
    ]
  }
}
```

### PP017: dup-b95650f5b2a285c228a0615368e1e4229499d9e51e6cdb28e3fa799b79112aea

Status: APPROVED; survivor `pushplastic_abs_absyellow_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_abs_absyellow_1000_175_p`|`ABS {color_name}`|`Yellow`|{"source_file": "pushplastic.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 24, "compiled_records": 24} / False|
|`pushplastic_abs_pushplasticabsyellow_1000_175_p`|`Push Plastic ABS {color_name}`|`Yellow`|{"source_file": "pushplastic.json", "definition_index": 2, "weights": 3, "diameters": 1, "colors": 20, "compiled_records": 60} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_abs_absyellow_1000_175_p": "F2DE00",
    "pushplastic_abs_pushplasticabsyellow_1000_175_p": "fdd835"
  },
  "extruder_temp_range": {
    "pushplastic_abs_absyellow_1000_175_p": [
      230,
      260
    ],
    "pushplastic_abs_pushplasticabsyellow_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "pushplastic_abs_absyellow_1000_175_p": [
      90,
      110
    ],
    "pushplastic_abs_pushplasticabsyellow_1000_175_p": [
      100,
      120
    ]
  }
}
```

### PP018: dup-a836e96a9703cfd3ded3a125f7554cde7e8aa7793530ab6551c388b4f72dc6a9

Status: APPROVED; survivor `pushplastic_petg_petgblack_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_petg_petgblack_1000_175_p`|`PETG {color_name}`|`Black`|{"source_file": "pushplastic.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`pushplastic_petg_pushplasticpetgblack_1000_175_p`|`Push Plastic PETG {color_name}`|`Black`|{"source_file": "pushplastic.json", "definition_index": 1, "weights": 3, "diameters": 1, "colors": 17, "compiled_records": 51} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_petg_petgblack_1000_175_p": "000000",
    "pushplastic_petg_pushplasticpetgblack_1000_175_p": "1a1a1a"
  }
}
```

### PP019: dup-b81db3991312fab1761dff24a069bfa2d064fc4a6ea8fe2ecbe31a5bb9f0caa6

Status: APPROVED; survivor `pushplastic_petg_petggreen_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_petg_petggreen_1000_175_p`|`PETG {color_name}`|`Green`|{"source_file": "pushplastic.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`pushplastic_petg_pushplasticpetggreen_1000_175_p`|`Push Plastic PETG {color_name}`|`Green`|{"source_file": "pushplastic.json", "definition_index": 1, "weights": 3, "diameters": 1, "colors": 17, "compiled_records": 51} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_petg_petggreen_1000_175_p": "089A45",
    "pushplastic_petg_pushplasticpetggreen_1000_175_p": "2e7d32"
  }
}
```

### PP020: dup-f4a4346fbd292250a29cbf235eb2fcb7389ab445952290e8cc5e8193019de901

Status: APPROVED; survivor `pushplastic_petg_petglightgrey_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_petg_petglightgrey_1000_175_p`|`PETG {color_name}`|`Light Grey`|{"source_file": "pushplastic.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`pushplastic_petg_pushplasticpetglightgrey_1000_175_p`|`Push Plastic PETG {color_name}`|`Light Grey`|{"source_file": "pushplastic.json", "definition_index": 1, "weights": 3, "diameters": 1, "colors": 17, "compiled_records": 51} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_petg_petglightgrey_1000_175_p": "C5C5BF",
    "pushplastic_petg_pushplasticpetglightgrey_1000_175_p": "a0a0a0"
  }
}
```

### PP021: dup-bab67e933aa3d638c2ab9b89cc3e9be9bcf381837243055b034afe92c4c1ad3f

Status: APPROVED; survivor `pushplastic_petg_petgorange_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_petg_petgorange_1000_175_p`|`PETG {color_name}`|`Orange`|{"source_file": "pushplastic.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`pushplastic_petg_pushplasticpetgorange_1000_175_p`|`Push Plastic PETG {color_name}`|`Orange`|{"source_file": "pushplastic.json", "definition_index": 1, "weights": 3, "diameters": 1, "colors": 17, "compiled_records": 51} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_petg_petgorange_1000_175_p": "FF5F2E",
    "pushplastic_petg_pushplasticpetgorange_1000_175_p": "f57c00"
  }
}
```

### PP022: dup-2bcc8969d9ed34c679cb655747d7ee27332ed2222f89a928182b46d01af4914d

Status: APPROVED; survivor `pushplastic_petg_petgred_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_petg_petgred_1000_175_p`|`PETG {color_name}`|`Red`|{"source_file": "pushplastic.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`pushplastic_petg_pushplasticpetgred_1000_175_p`|`Push Plastic PETG {color_name}`|`Red`|{"source_file": "pushplastic.json", "definition_index": 1, "weights": 3, "diameters": 1, "colors": 17, "compiled_records": 51} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_petg_petgred_1000_175_p": "E60000",
    "pushplastic_petg_pushplasticpetgred_1000_175_p": "c41e2a"
  }
}
```

### PP023: dup-97e40cd6b0cd53578cef4bd949bb1e50b9ab64f967687113fd11548dbfe32018

Status: APPROVED; survivor `pushplastic_petg_petgrust_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_petg_petgrust_1000_175_p`|`PETG {color_name}`|`Rust`|{"source_file": "pushplastic.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`pushplastic_petg_pushplasticpetgrust_1000_175_p`|`Push Plastic PETG {color_name}`|`Rust`|{"source_file": "pushplastic.json", "definition_index": 1, "weights": 3, "diameters": 1, "colors": 17, "compiled_records": 51} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_petg_petgrust_1000_175_p": "A54830",
    "pushplastic_petg_pushplasticpetgrust_1000_175_p": "b5523a"
  }
}
```

### PP024: dup-4b18c782bd4efc23cf1aab37c416ca0386ef48dbc57b16ea1dd501ae8e0c4658

Status: APPROVED; survivor `pushplastic_petg_petgsilvermetallic_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_petg_petgsilvermetallic_1000_175_p`|`PETG {color_name}`|`Silver Metallic`|{"source_file": "pushplastic.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`pushplastic_petg_pushplasticpetgsilvermetallic_1000_175_p`|`Push Plastic PETG {color_name}`|`Silver Metallic`|{"source_file": "pushplastic.json", "definition_index": 1, "weights": 3, "diameters": 1, "colors": 17, "compiled_records": 51} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_petg_petgsilvermetallic_1000_175_p": "949597",
    "pushplastic_petg_pushplasticpetgsilvermetallic_1000_175_p": "b0b0b0"
  }
}
```

### PP025: dup-4eccf4fd69fcad7a62fde98ef233e15202dc4065a58c5e7092499e1d3c54ce5b

Status: APPROVED; survivor `pushplastic_petg_petgtranslucentamber_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_petg_petgtranslucentamber_1000_175_p`|`PETG {color_name}`|`Translucent Amber`|{"source_file": "pushplastic.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`pushplastic_petg_pushplasticpetgtranslucentamber_1000_175_p`|`Push Plastic PETG {color_name}`|`Translucent Amber`|{"source_file": "pushplastic.json", "definition_index": 1, "weights": 3, "diameters": 1, "colors": 17, "compiled_records": 51} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_petg_petgtranslucentamber_1000_175_p": "FF9A14",
    "pushplastic_petg_pushplasticpetgtranslucentamber_1000_175_p": "e6a23c"
  }
}
```

### PP026: dup-857b39ba0737ee31b2f1174262db0ed27d00280bcd1723466f5c1e6c0e1eff20

Status: APPROVED; survivor `pushplastic_petg_petgtranslucentblue_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_petg_petgtranslucentblue_1000_175_p`|`PETG {color_name}`|`Translucent Blue`|{"source_file": "pushplastic.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`pushplastic_petg_pushplasticpetgtranslucentblue_1000_175_p`|`Push Plastic PETG {color_name}`|`Translucent Blue`|{"source_file": "pushplastic.json", "definition_index": 1, "weights": 3, "diameters": 1, "colors": 17, "compiled_records": 51} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_petg_petgtranslucentblue_1000_175_p": "0353BA",
    "pushplastic_petg_pushplasticpetgtranslucentblue_1000_175_p": "4da6d9"
  }
}
```

### PP027: dup-7845734fe1eb581b8a688046975412aace683e708e3e5b36ca3e2c03f3aef9d9

Status: APPROVED; survivor `pushplastic_petg_petgtranslucentgreen_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_petg_petgtranslucentgreen_1000_175_p`|`PETG {color_name}`|`Translucent Green`|{"source_file": "pushplastic.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`pushplastic_petg_pushplasticpetgtranslucentgreen_1000_175_p`|`Push Plastic PETG {color_name}`|`Translucent Green`|{"source_file": "pushplastic.json", "definition_index": 1, "weights": 3, "diameters": 1, "colors": 17, "compiled_records": 51} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_petg_petgtranslucentgreen_1000_175_p": "00A594",
    "pushplastic_petg_pushplasticpetgtranslucentgreen_1000_175_p": "5cb85c"
  }
}
```

### PP028: dup-7038eb4dc0d0b8260edd3b30d886be28ead67ce962d3ce9f2ab4ff11dc4e79dc

Status: APPROVED; survivor `pushplastic_petg_petgultrablue_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_petg_petgultrablue_1000_175_p`|`PETG {color_name}`|`Ultra Blue`|{"source_file": "pushplastic.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`pushplastic_petg_pushplasticpetgultrablue_1000_175_p`|`Push Plastic PETG {color_name}`|`Ultra Blue`|{"source_file": "pushplastic.json", "definition_index": 1, "weights": 3, "diameters": 1, "colors": 17, "compiled_records": 51} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_petg_petgultrablue_1000_175_p": "0022FF",
    "pushplastic_petg_pushplasticpetgultrablue_1000_175_p": "005fe8"
  }
}
```

### PP029: dup-a798ec550d2465ccc05be19012ed16d6575f462219f42425c37cbe0840d56842

Status: APPROVED; survivor `pushplastic_petg_petgwhite_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`pushplastic_petg_petgwhite_1000_175_p`|`PETG {color_name}`|`White`|{"source_file": "pushplastic.json", "definition_index": 14, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`pushplastic_petg_pushplasticpetgwhite_1000_175_p`|`Push Plastic PETG {color_name}`|`White`|{"source_file": "pushplastic.json", "definition_index": 1, "weights": 3, "diameters": 1, "colors": 17, "compiled_records": 51} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "pushplastic_petg_petgwhite_1000_175_p": "FFFFFF",
    "pushplastic_petg_pushplasticpetgwhite_1000_175_p": "f5f5f5"
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "pushplastic_abs_absbronzemetallic_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          250
        ],
        "bed_temp_range": [
          100,
          120
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0260/7421/files/ABS_print_settings.pdf?v=1683905833",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "pushplastic_abs_absultrablue_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          250
        ],
        "bed_temp_range": [
          100,
          120
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0260/7421/files/ABS_print_settings.pdf?v=1683905833",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "pushplastic_abs_abslightgrey_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          250
        ],
        "bed_temp_range": [
          100,
          120
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0260/7421/files/ABS_print_settings.pdf?v=1683905833",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "pushplastic_abs_absgoldmetallic_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          250
        ],
        "bed_temp_range": [
          100,
          120
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0260/7421/files/ABS_print_settings.pdf?v=1683905833",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "pushplastic_abs_absnatural_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          250
        ],
        "bed_temp_range": [
          100,
          120
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0260/7421/files/ABS_print_settings.pdf?v=1683905833",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "pushplastic_abs_abspink_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          250
        ],
        "bed_temp_range": [
          100,
          120
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0260/7421/files/ABS_print_settings.pdf?v=1683905833",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "pushplastic_abs_abssilvermetallic_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          250
        ],
        "bed_temp_range": [
          100,
          120
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0260/7421/files/ABS_print_settings.pdf?v=1683905833",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "pushplastic_abs_absoceanblue_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          250
        ],
        "bed_temp_range": [
          100,
          120
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0260/7421/files/ABS_print_settings.pdf?v=1683905833",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "pushplastic_abs_absgreen_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          250
        ],
        "bed_temp_range": [
          100,
          120
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0260/7421/files/ABS_print_settings.pdf?v=1683905833",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "pushplastic_abs_absdarkgrey_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          250
        ],
        "bed_temp_range": [
          100,
          120
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0260/7421/files/ABS_print_settings.pdf?v=1683905833",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "pushplastic_abs_absblack_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          250
        ],
        "bed_temp_range": [
          100,
          120
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0260/7421/files/ABS_print_settings.pdf?v=1683905833",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "pushplastic_abs_abspurple_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          250
        ],
        "bed_temp_range": [
          100,
          120
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0260/7421/files/ABS_print_settings.pdf?v=1683905833",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "pushplastic_abs_absflatdarkearth_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          250
        ],
        "bed_temp_range": [
          100,
          120
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0260/7421/files/ABS_print_settings.pdf?v=1683905833",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "pushplastic_abs_absyellow_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          250
        ],
        "bed_temp_range": [
          100,
          120
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0260/7421/files/ABS_print_settings.pdf?v=1683905833",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "pushplastic_abs_absbrown_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          250
        ],
        "bed_temp_range": [
          100,
          120
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0260/7421/files/ABS_print_settings.pdf?v=1683905833",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "pushplastic_abs_abswhite_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          250
        ],
        "bed_temp_range": [
          100,
          120
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0260/7421/files/ABS_print_settings.pdf?v=1683905833",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "pushplastic_abs_absorange_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          250
        ],
        "bed_temp_range": [
          100,
          120
        ]
      },
      "source": "https://cdn.shopify.com/s/files/1/0260/7421/files/ABS_print_settings.pdf?v=1683905833",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    }
  ],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `pushplastic_pla_pushplasticplablack_1000_175_p` — Push Plastic PLA Black
- `pushplastic_pla_pushplasticplawhite_1000_175_p` — Push Plastic PLA White
- `pushplastic_pla_pushplasticplared_1000_175_p` — Push Plastic PLA Red
- `pushplastic_pla_pushplasticplagreen_1000_175_p` — Push Plastic PLA Green
- `pushplastic_pla_pushplasticplayellow_1000_175_p` — Push Plastic PLA Yellow
- `pushplastic_pla_pushplasticplaorange_1000_175_p` — Push Plastic PLA Orange
- `pushplastic_pla_pushplasticplapurple_1000_175_p` — Push Plastic PLA Purple
- `pushplastic_pla_pushplasticplapink_1000_175_p` — Push Plastic PLA Pink
- `pushplastic_pla_pushplasticplanatural_1000_175_p` — Push Plastic PLA Natural
- `pushplastic_pla_pushplasticplabeige_1000_175_p` — Push Plastic PLA Beige
- `pushplastic_pla_pushplasticplalightgrey_1000_175_p` — Push Plastic PLA Light Grey
- `pushplastic_pla_pushplasticpladarkgrey_1000_175_p` — Push Plastic PLA Dark Grey
- `pushplastic_pla_pushplasticplanavyblue_1000_175_p` — Push Plastic PLA Navy Blue
- `pushplastic_pla_pushplasticplaultrablue_1000_175_p` — Push Plastic PLA Ultra Blue
- `pushplastic_pla_pushplasticplaoceanblue_1000_175_p` — Push Plastic PLA Ocean Blue
- `pushplastic_pla_pushplasticplablack_1000_285_p` — Push Plastic PLA Black
- `pushplastic_pla_pushplasticplawhite_1000_285_p` — Push Plastic PLA White
- `pushplastic_pla_pushplasticplared_1000_285_p` — Push Plastic PLA Red
- `pushplastic_pla_pushplasticplagreen_1000_285_p` — Push Plastic PLA Green
- `pushplastic_pla_pushplasticplayellow_1000_285_p` — Push Plastic PLA Yellow
- `pushplastic_pla_pushplasticplaorange_1000_285_p` — Push Plastic PLA Orange
- `pushplastic_pla_pushplasticplapurple_1000_285_p` — Push Plastic PLA Purple
- `pushplastic_pla_pushplasticplapink_1000_285_p` — Push Plastic PLA Pink
- `pushplastic_pla_pushplasticplanatural_1000_285_p` — Push Plastic PLA Natural
- `pushplastic_pla_pushplasticplabeige_1000_285_p` — Push Plastic PLA Beige
- `pushplastic_pla_pushplasticplalightgrey_1000_285_p` — Push Plastic PLA Light Grey
- `pushplastic_pla_pushplasticpladarkgrey_1000_285_p` — Push Plastic PLA Dark Grey
- `pushplastic_pla_pushplasticplanavyblue_1000_285_p` — Push Plastic PLA Navy Blue
- `pushplastic_pla_pushplasticplaultrablue_1000_285_p` — Push Plastic PLA Ultra Blue
- `pushplastic_pla_pushplasticplaoceanblue_1000_285_p` — Push Plastic PLA Ocean Blue
- `pushplastic_pla_pushplasticplablack_3000_175_p` — Push Plastic PLA Black
- `pushplastic_pla_pushplasticplawhite_3000_175_p` — Push Plastic PLA White
- `pushplastic_pla_pushplasticplared_3000_175_p` — Push Plastic PLA Red
- `pushplastic_pla_pushplasticplagreen_3000_175_p` — Push Plastic PLA Green
- `pushplastic_pla_pushplasticplayellow_3000_175_p` — Push Plastic PLA Yellow
- `pushplastic_pla_pushplasticplaorange_3000_175_p` — Push Plastic PLA Orange
- `pushplastic_pla_pushplasticplapurple_3000_175_p` — Push Plastic PLA Purple
- `pushplastic_pla_pushplasticplapink_3000_175_p` — Push Plastic PLA Pink
- `pushplastic_pla_pushplasticplanatural_3000_175_p` — Push Plastic PLA Natural
- `pushplastic_pla_pushplasticplabeige_3000_175_p` — Push Plastic PLA Beige
- `pushplastic_pla_pushplasticplalightgrey_3000_175_p` — Push Plastic PLA Light Grey
- `pushplastic_pla_pushplasticpladarkgrey_3000_175_p` — Push Plastic PLA Dark Grey
- `pushplastic_pla_pushplasticplanavyblue_3000_175_p` — Push Plastic PLA Navy Blue
- `pushplastic_pla_pushplasticplaultrablue_3000_175_p` — Push Plastic PLA Ultra Blue
- `pushplastic_pla_pushplasticplaoceanblue_3000_175_p` — Push Plastic PLA Ocean Blue
- `pushplastic_pla_pushplasticplablack_3000_285_p` — Push Plastic PLA Black
- `pushplastic_pla_pushplasticplawhite_3000_285_p` — Push Plastic PLA White
- `pushplastic_pla_pushplasticplared_3000_285_p` — Push Plastic PLA Red
- `pushplastic_pla_pushplasticplagreen_3000_285_p` — Push Plastic PLA Green
- `pushplastic_pla_pushplasticplayellow_3000_285_p` — Push Plastic PLA Yellow
- `pushplastic_pla_pushplasticplaorange_3000_285_p` — Push Plastic PLA Orange
- `pushplastic_pla_pushplasticplapurple_3000_285_p` — Push Plastic PLA Purple
- `pushplastic_pla_pushplasticplapink_3000_285_p` — Push Plastic PLA Pink
- `pushplastic_pla_pushplasticplanatural_3000_285_p` — Push Plastic PLA Natural
- `pushplastic_pla_pushplasticplabeige_3000_285_p` — Push Plastic PLA Beige
- `pushplastic_pla_pushplasticplalightgrey_3000_285_p` — Push Plastic PLA Light Grey
- `pushplastic_pla_pushplasticpladarkgrey_3000_285_p` — Push Plastic PLA Dark Grey
- `pushplastic_pla_pushplasticplanavyblue_3000_285_p` — Push Plastic PLA Navy Blue
- `pushplastic_pla_pushplasticplaultrablue_3000_285_p` — Push Plastic PLA Ultra Blue
- `pushplastic_pla_pushplasticplaoceanblue_3000_285_p` — Push Plastic PLA Ocean Blue
- `pushplastic_pla_pushplasticplablack_10000_175_p` — Push Plastic PLA Black
- `pushplastic_pla_pushplasticplawhite_10000_175_p` — Push Plastic PLA White
- `pushplastic_pla_pushplasticplared_10000_175_p` — Push Plastic PLA Red
- `pushplastic_pla_pushplasticplagreen_10000_175_p` — Push Plastic PLA Green
- `pushplastic_pla_pushplasticplayellow_10000_175_p` — Push Plastic PLA Yellow
- `pushplastic_pla_pushplasticplaorange_10000_175_p` — Push Plastic PLA Orange
- `pushplastic_pla_pushplasticplapurple_10000_175_p` — Push Plastic PLA Purple
- `pushplastic_pla_pushplasticplapink_10000_175_p` — Push Plastic PLA Pink
- `pushplastic_pla_pushplasticplanatural_10000_175_p` — Push Plastic PLA Natural
- `pushplastic_pla_pushplasticplabeige_10000_175_p` — Push Plastic PLA Beige
- `pushplastic_pla_pushplasticplalightgrey_10000_175_p` — Push Plastic PLA Light Grey
- `pushplastic_pla_pushplasticpladarkgrey_10000_175_p` — Push Plastic PLA Dark Grey
- `pushplastic_pla_pushplasticplanavyblue_10000_175_p` — Push Plastic PLA Navy Blue
- `pushplastic_pla_pushplasticplaultrablue_10000_175_p` — Push Plastic PLA Ultra Blue
- `pushplastic_pla_pushplasticplaoceanblue_10000_175_p` — Push Plastic PLA Ocean Blue
- `pushplastic_pla_pushplasticplablack_10000_285_p` — Push Plastic PLA Black
- `pushplastic_pla_pushplasticplawhite_10000_285_p` — Push Plastic PLA White
- `pushplastic_pla_pushplasticplared_10000_285_p` — Push Plastic PLA Red
- `pushplastic_pla_pushplasticplagreen_10000_285_p` — Push Plastic PLA Green
- `pushplastic_pla_pushplasticplayellow_10000_285_p` — Push Plastic PLA Yellow
- `pushplastic_pla_pushplasticplaorange_10000_285_p` — Push Plastic PLA Orange
- `pushplastic_pla_pushplasticplapurple_10000_285_p` — Push Plastic PLA Purple
- `pushplastic_pla_pushplasticplapink_10000_285_p` — Push Plastic PLA Pink
- `pushplastic_pla_pushplasticplanatural_10000_285_p` — Push Plastic PLA Natural
- `pushplastic_pla_pushplasticplabeige_10000_285_p` — Push Plastic PLA Beige
- `pushplastic_pla_pushplasticplalightgrey_10000_285_p` — Push Plastic PLA Light Grey
- `pushplastic_pla_pushplasticpladarkgrey_10000_285_p` — Push Plastic PLA Dark Grey
- `pushplastic_pla_pushplasticplanavyblue_10000_285_p` — Push Plastic PLA Navy Blue
- `pushplastic_pla_pushplasticplaultrablue_10000_285_p` — Push Plastic PLA Ultra Blue
- `pushplastic_pla_pushplasticplaoceanblue_10000_285_p` — Push Plastic PLA Ocean Blue
- `pushplastic_petg_pushplasticpetgpurple_1000_175_p` — Push Plastic PETG Purple
- `pushplastic_petg_pushplasticpetgdarkgrey_1000_175_p` — Push Plastic PETG Dark Grey
- `pushplastic_petg_pushplasticpetgnavyblue_1000_175_p` — Push Plastic PETG Navy Blue
- `pushplastic_petg_pushplasticpetgelectricblue_1000_175_p` — Push Plastic PETG Electric Blue
- `pushplastic_petg_pushplasticpetglightteal_1000_175_p` — Push Plastic PETG Light Teal
- `pushplastic_petg_pushplasticpetgblack_3000_175_p` — Push Plastic PETG Black
- `pushplastic_petg_pushplasticpetgwhite_3000_175_p` — Push Plastic PETG White
- `pushplastic_petg_pushplasticpetgred_3000_175_p` — Push Plastic PETG Red
- `pushplastic_petg_pushplasticpetggreen_3000_175_p` — Push Plastic PETG Green
- `pushplastic_petg_pushplasticpetgorange_3000_175_p` — Push Plastic PETG Orange
- `pushplastic_petg_pushplasticpetgpurple_3000_175_p` — Push Plastic PETG Purple
- `pushplastic_petg_pushplasticpetglightgrey_3000_175_p` — Push Plastic PETG Light Grey
- `pushplastic_petg_pushplasticpetgdarkgrey_3000_175_p` — Push Plastic PETG Dark Grey
- `pushplastic_petg_pushplasticpetgnavyblue_3000_175_p` — Push Plastic PETG Navy Blue
- `pushplastic_petg_pushplasticpetgultrablue_3000_175_p` — Push Plastic PETG Ultra Blue
- `pushplastic_petg_pushplasticpetgelectricblue_3000_175_p` — Push Plastic PETG Electric Blue
- `pushplastic_petg_pushplasticpetglightteal_3000_175_p` — Push Plastic PETG Light Teal
- `pushplastic_petg_pushplasticpetgrust_3000_175_p` — Push Plastic PETG Rust
- `pushplastic_petg_pushplasticpetgsilvermetallic_3000_175_p` — Push Plastic PETG Silver Metallic
- `pushplastic_petg_pushplasticpetgtranslucentblue_3000_175_p` — Push Plastic PETG Translucent Blue
- `pushplastic_petg_pushplasticpetgtranslucentgreen_3000_175_p` — Push Plastic PETG Translucent Green
- `pushplastic_petg_pushplasticpetgtranslucentamber_3000_175_p` — Push Plastic PETG Translucent Amber
- `pushplastic_petg_pushplasticpetgblack_10000_175_p` — Push Plastic PETG Black
- `pushplastic_petg_pushplasticpetgwhite_10000_175_p` — Push Plastic PETG White
- `pushplastic_petg_pushplasticpetgred_10000_175_p` — Push Plastic PETG Red
- `pushplastic_petg_pushplasticpetggreen_10000_175_p` — Push Plastic PETG Green
- `pushplastic_petg_pushplasticpetgorange_10000_175_p` — Push Plastic PETG Orange
- `pushplastic_petg_pushplasticpetgpurple_10000_175_p` — Push Plastic PETG Purple
- `pushplastic_petg_pushplasticpetglightgrey_10000_175_p` — Push Plastic PETG Light Grey
- `pushplastic_petg_pushplasticpetgdarkgrey_10000_175_p` — Push Plastic PETG Dark Grey
- `pushplastic_petg_pushplasticpetgnavyblue_10000_175_p` — Push Plastic PETG Navy Blue
- `pushplastic_petg_pushplasticpetgultrablue_10000_175_p` — Push Plastic PETG Ultra Blue
- `pushplastic_petg_pushplasticpetgelectricblue_10000_175_p` — Push Plastic PETG Electric Blue
- `pushplastic_petg_pushplasticpetglightteal_10000_175_p` — Push Plastic PETG Light Teal
- `pushplastic_petg_pushplasticpetgrust_10000_175_p` — Push Plastic PETG Rust
- `pushplastic_petg_pushplasticpetgsilvermetallic_10000_175_p` — Push Plastic PETG Silver Metallic
- `pushplastic_petg_pushplasticpetgtranslucentblue_10000_175_p` — Push Plastic PETG Translucent Blue
- `pushplastic_petg_pushplasticpetgtranslucentgreen_10000_175_p` — Push Plastic PETG Translucent Green
- `pushplastic_petg_pushplasticpetgtranslucentamber_10000_175_p` — Push Plastic PETG Translucent Amber
- `pushplastic_abs_pushplasticabsbeige_1000_175_p` — Push Plastic ABS Beige
- `pushplastic_abs_pushplasticabsmagenta_1000_175_p` — Push Plastic ABS Magenta
- `pushplastic_abs_pushplasticabsdeserttan_1000_175_p` — Push Plastic ABS Desert Tan
- `pushplastic_abs_pushplasticabsblack_3000_175_p` — Push Plastic ABS Black
- `pushplastic_abs_pushplasticabswhite_3000_175_p` — Push Plastic ABS White
- `pushplastic_abs_pushplasticabsgreen_3000_175_p` — Push Plastic ABS Green
- `pushplastic_abs_pushplasticabsyellow_3000_175_p` — Push Plastic ABS Yellow
- `pushplastic_abs_pushplasticabsorange_3000_175_p` — Push Plastic ABS Orange
- `pushplastic_abs_pushplasticabspink_3000_175_p` — Push Plastic ABS Pink
- `pushplastic_abs_pushplasticabspurple_3000_175_p` — Push Plastic ABS Purple
- `pushplastic_abs_pushplasticabsnatural_3000_175_p` — Push Plastic ABS Natural
- `pushplastic_abs_pushplasticabsbeige_3000_175_p` — Push Plastic ABS Beige
- `pushplastic_abs_pushplasticabsbrown_3000_175_p` — Push Plastic ABS Brown
- `pushplastic_abs_pushplasticabslightgrey_3000_175_p` — Push Plastic ABS Light Grey
- `pushplastic_abs_pushplasticabsdarkgrey_3000_175_p` — Push Plastic ABS Dark Grey
- `pushplastic_abs_pushplasticabsmagenta_3000_175_p` — Push Plastic ABS Magenta
- `pushplastic_abs_pushplasticabsultrablue_3000_175_p` — Push Plastic ABS Ultra Blue
- `pushplastic_abs_pushplasticabsoceanblue_3000_175_p` — Push Plastic ABS Ocean Blue
- `pushplastic_abs_pushplasticabsdeserttan_3000_175_p` — Push Plastic ABS Desert Tan
- `pushplastic_abs_pushplasticabsflatdarkearth_3000_175_p` — Push Plastic ABS Flat Dark Earth
- `pushplastic_abs_pushplasticabssilvermetallic_3000_175_p` — Push Plastic ABS Silver Metallic
- `pushplastic_abs_pushplasticabsgoldmetallic_3000_175_p` — Push Plastic ABS Gold Metallic
- `pushplastic_abs_pushplasticabsbronzemetallic_3000_175_p` — Push Plastic ABS Bronze Metallic
- `pushplastic_abs_pushplasticabsblack_10000_175_p` — Push Plastic ABS Black
- `pushplastic_abs_pushplasticabswhite_10000_175_p` — Push Plastic ABS White
- `pushplastic_abs_pushplasticabsgreen_10000_175_p` — Push Plastic ABS Green
- `pushplastic_abs_pushplasticabsyellow_10000_175_p` — Push Plastic ABS Yellow
- `pushplastic_abs_pushplasticabsorange_10000_175_p` — Push Plastic ABS Orange
- `pushplastic_abs_pushplasticabspink_10000_175_p` — Push Plastic ABS Pink
- `pushplastic_abs_pushplasticabspurple_10000_175_p` — Push Plastic ABS Purple
- `pushplastic_abs_pushplasticabsnatural_10000_175_p` — Push Plastic ABS Natural
- `pushplastic_abs_pushplasticabsbeige_10000_175_p` — Push Plastic ABS Beige
- `pushplastic_abs_pushplasticabsbrown_10000_175_p` — Push Plastic ABS Brown
- `pushplastic_abs_pushplasticabslightgrey_10000_175_p` — Push Plastic ABS Light Grey
- `pushplastic_abs_pushplasticabsdarkgrey_10000_175_p` — Push Plastic ABS Dark Grey
- `pushplastic_abs_pushplasticabsmagenta_10000_175_p` — Push Plastic ABS Magenta
- `pushplastic_abs_pushplasticabsultrablue_10000_175_p` — Push Plastic ABS Ultra Blue
- `pushplastic_abs_pushplasticabsoceanblue_10000_175_p` — Push Plastic ABS Ocean Blue
- `pushplastic_abs_pushplasticabsdeserttan_10000_175_p` — Push Plastic ABS Desert Tan
- `pushplastic_abs_pushplasticabsflatdarkearth_10000_175_p` — Push Plastic ABS Flat Dark Earth
- `pushplastic_abs_pushplasticabssilvermetallic_10000_175_p` — Push Plastic ABS Silver Metallic
- `pushplastic_abs_pushplasticabsgoldmetallic_10000_175_p` — Push Plastic ABS Gold Metallic
- `pushplastic_abs_pushplasticabsbronzemetallic_10000_175_p` — Push Plastic ABS Bronze Metallic
- `pushplastic_abs_absarmygreen_1000_175_p` — ABS Army Green
- `pushplastic_abs_abslavender_1000_175_p` — ABS Lavender
- `pushplastic_abs_abslightteal_1000_175_p` — ABS Light Teal
- `pushplastic_abs_abslimegreen_1000_175_p` — ABS Lime Green
- `pushplastic_abs_absmaroon_1000_175_p` — ABS Maroon
- `pushplastic_abs_abspc/natural_1000_175_p` — ABS PC/ Natural
- `pushplastic_abs_absred_1000_175_p` — ABS Red
- `pushplastic_abs_cfabsblack_1000_175_p` — CF ABS Black
- `pushplastic_abs_matteabsblack_1000_175_p` — Matte ABS Black
- `pushplastic_abs_matteabsdarkgrey_1000_175_p` — Matte ABS Dark Grey
- `pushplastic_abs_matteabslightgrey_1000_175_p` — Matte ABS Light Grey
- `pushplastic_abs_matteabsnatural_1000_175_p` — Matte ABS Natural
- `pushplastic_abs_matteabswhite_1000_175_p` — Matte ABS White
- `pushplastic_asa_asablack_1000_175_p` — ASA Black
- `pushplastic_asa_asanatural_1000_175_p` — ASA Natural
- `pushplastic_asa_asasilvermetallic_1000_175_p` — ASA Silver Metallic
- `pushplastic_asa_asawhite_1000_175_p` — ASA White
- `pushplastic_hips_hipsnatural_1000_175_p` — HIPS Natural
- `pushplastic_pbt_pcpbtnatural_1000_175_p` — PC PBT Natural
- `pushplastic_pbt_pcpbtorange_1000_175_p` — PC PBT Orange
- `pushplastic_pbt_pcpbtultrablue_1000_175_p` — PC PBT Ultra Blue
- `pushplastic_pc_pccfpbtblack_1000_175_p` — PC CF PBT Black
- `pushplastic_pc_pcblack_1000_175_p` — PC Black
- `pushplastic_pc_pcpbtblack_1000_175_p` — PC PBT Black
- `pushplastic_pc_pcpbtred_1000_175_p` — PC PBT Red
- `pushplastic_pc_pcpbtsilvermetallic_1000_175_p` — PC PBT Silver Metallic
- `pushplastic_pc_pcpbtwhite_1000_175_p` — PC PBT White
- `pushplastic_pc_pcpolycarbonateblack_1000_175_p` — PC Polycarbonate Black
- `pushplastic_pc_pcpolycarbonatenatural_1000_175_p` — PC Polycarbonate Natural
- `pushplastic_pc_pcpolycarbonatewhite_1000_175_p` — PC Polycarbonate White
- `pushplastic_pc_pcsiblack_1000_175_p` — PC Si Black
- `pushplastic_pctg_pctgblack_1000_175_p` — PCTG Black
- `pushplastic_pctg_pctgnatural_1000_175_p` — PCTG Natural
- `pushplastic_pctg_pctgwhite_1000_175_p` — PCTG White
- `pushplastic_pei_pei1010natural_1000_175_p` — PEI 1010 Natural
- `pushplastic_petg_petgcfcarbonfiber_1000_175_p` — PETG CF Carbon Fiber
- `pushplastic_petg_petgdeserttan_1000_175_p` — PETG Desert Tan
- `pushplastic_petg_petgnatural_1000_175_p` — PETG Natural
- `pushplastic_petg_petgpuschgreen_1000_175_p` — PETG PUSCH Green
- `pushplastic_petg_petgpwaltyellow_1000_175_p` — PETG PWalt Yellow
- `pushplastic_petg_petgsafetyyellow_1000_175_p` — PETG Safety Yellow
- `pushplastic_petg_petgtranslucentred_1000_175_p` — PETG Translucent Red
- `pushplastic_pla_highheatplablack_1000_175_p` — High Heat PLA Black
- `pushplastic_pla_highheatplanatural_1000_175_p` — High Heat PLA Natural
- `pushplastic_pla_highheatplared_1000_175_p` — High Heat PLA Red
- `pushplastic_pla_highheatplasilvermetallic_1000_175_p` — High Heat PLA Silver Metallic
- `pushplastic_pla_highheatplaultrablue_1000_175_p` — High Heat PLA Ultra Blue
- `pushplastic_pla_highheatplawhite_1000_175_p` — High Heat PLA White
- `pushplastic_pmma_pmmafilament_1000_175_p` — PMMA Filament
- `pushplastic_tpu_tpu100a_1000_175_p` — TPU 100A
