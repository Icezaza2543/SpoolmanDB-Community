# buddy3d duplicate migration review

Base `b9e056a00ad9a63850552c5afedbfe7a19b33f07`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `d91ea30c2edc0aaa15e2727cfbe7dd84e67cc7eb1b16f1478d55bdf4a44d67e1`.

## Authorization and result

{"groups": 37, "approved_groups": 36, "retired": 36, "deferred": 1, "hard_stops": 0, "before_count": 52073, "after_count": 52037, "brand_before": 137, "brand_after": 101, "registry_before": 1361, "registry_after": 1397, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

PLA/PETG R4 Cartesian choices replaced by older well-formed narrower one-weight families under owner-pattern override; all unique other weights/colors unchanged. Silk official name PLA Silk selects older line byRule3. ABS current official ABS name selects ABS template byRule3, not size; ESD Black unique out-of-scope record untouched. Existing printing values agree with current exact pages; no metadata changes. PETG density1.27 vs1.28 unresolved because current official-host TDS could not be read; no nonofficial mirror used. HEX/tare conflicts retained. Packaging/tare unchanged.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://www.prusa3d.com/product/buddy3d-pla-black-1kg/", "nozzle": 215, "bed": [50, 60]}
- {"url": "https://www.prusa3d.com/product/buddy3d-pla-silk-dark-gold-1kg/", "name": "PLA Silk", "nozzle": 215, "bed": [50, 60]}
- {"url": "https://www.prusa3d.com/product/buddy3d-petg-black-1kg/", "nozzle": [240, 260], "bed": [70, 90]}
- {"url": "https://www.prusa3d.com/product/buddy3d-abs-filament/", "name": "ABS", "nozzle": 255, "bed": 100, "bed_adjustable": [80, 110]}
- {"url": "https://www.prusa3d.com/product/buddy3d-pla-glitter-black-gold-1kg/", "note": "Current spelling does not resolve strict line/color decomposition; Glitter pair remains backlog."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`buddy3d_abs_black_750_175_p`|`buddy3d_abs_absblack_750_175_p`|`buddy3d.json::Buddy3D::{color_name}::Black::ABS::750.0::1.75::None::False`|
|`buddy3d_abs_green_750_175_p`|`buddy3d_abs_absgreen_750_175_p`|`buddy3d.json::Buddy3D::{color_name}::Green::ABS::750.0::1.75::None::False`|
|`buddy3d_abs_natural_750_175_p`|`buddy3d_abs_absnatural_750_175_p`|`buddy3d.json::Buddy3D::{color_name}::Natural::ABS::750.0::1.75::None::False`|
|`buddy3d_abs_white_750_175_p`|`buddy3d_abs_abswhite_750_175_p`|`buddy3d.json::Buddy3D::{color_name}::White::ABS::750.0::1.75::None::False`|
|`buddy3d_petg_petgblack_1000_175_p`|`buddy3d_petg_black_1000_175_p`|`buddy3d.json::Buddy3D::PETG {color_name}::PETG Black::PETG::1000::1.75::None::False`|
|`buddy3d_petg_petgblue_1000_175_p`|`buddy3d_petg_blue_1000_175_p`|`buddy3d.json::Buddy3D::PETG {color_name}::PETG Blue::PETG::1000::1.75::None::False`|
|`buddy3d_petg_petgbrown_1000_175_p`|`buddy3d_petg_brown_1000_175_p`|`buddy3d.json::Buddy3D::PETG {color_name}::PETG Brown::PETG::1000::1.75::None::False`|
|`buddy3d_petg_petggreen_1000_175_p`|`buddy3d_petg_green_1000_175_p`|`buddy3d.json::Buddy3D::PETG {color_name}::PETG Green::PETG::1000::1.75::None::False`|
|`buddy3d_petg_petggrey_1000_175_p`|`buddy3d_petg_grey_1000_175_p`|`buddy3d.json::Buddy3D::PETG {color_name}::PETG Grey::PETG::1000::1.75::None::False`|
|`buddy3d_petg_petglila_1000_175_p`|`buddy3d_petg_lila_1000_175_p`|`buddy3d.json::Buddy3D::PETG {color_name}::PETG Lila::PETG::1000::1.75::None::False`|
|`buddy3d_petg_petgred_1000_175_p`|`buddy3d_petg_red_1000_175_p`|`buddy3d.json::Buddy3D::PETG {color_name}::PETG Red::PETG::1000::1.75::None::False`|
|`buddy3d_petg_petgsilver_1000_175_p`|`buddy3d_petg_silver_1000_175_p`|`buddy3d.json::Buddy3D::PETG {color_name}::PETG Silver::PETG::1000::1.75::None::False`|
|`buddy3d_petg_petgwhite_1000_175_p`|`buddy3d_petg_white_1000_175_p`|`buddy3d.json::Buddy3D::PETG {color_name}::PETG White::PETG::1000::1.75::None::False`|
|`buddy3d_petg_petgyellow_1000_175_p`|`buddy3d_petg_yellow_1000_175_p`|`buddy3d.json::Buddy3D::PETG {color_name}::PETG Yellow::PETG::1000::1.75::None::False`|
|`buddy3d_pla_plablack_1000_175_p`|`buddy3d_pla_black_1000_175_p`|`buddy3d.json::Buddy3D::PLA {color_name}::PLA Black::PLA::1000::1.75::None::False`|
|`buddy3d_pla_plablue_1000_175_p`|`buddy3d_pla_blue_1000_175_p`|`buddy3d.json::Buddy3D::PLA {color_name}::PLA Blue::PLA::1000::1.75::None::False`|
|`buddy3d_pla_plabrown_1000_175_p`|`buddy3d_pla_brown_1000_175_p`|`buddy3d.json::Buddy3D::PLA {color_name}::PLA Brown::PLA::1000::1.75::None::False`|
|`buddy3d_pla_plagreen_1000_175_p`|`buddy3d_pla_green_1000_175_p`|`buddy3d.json::Buddy3D::PLA {color_name}::PLA Green::PLA::1000::1.75::None::False`|
|`buddy3d_pla_plagrey_1000_175_p`|`buddy3d_pla_grey_1000_175_p`|`buddy3d.json::Buddy3D::PLA {color_name}::PLA Grey::PLA::1000::1.75::None::False`|
|`buddy3d_pla_plalila_1000_175_p`|`buddy3d_pla_lila_1000_175_p`|`buddy3d.json::Buddy3D::PLA {color_name}::PLA Lila::PLA::1000::1.75::None::False`|
|`buddy3d_pla_plapink_1000_175_p`|`buddy3d_pla_pink_1000_175_p`|`buddy3d.json::Buddy3D::PLA {color_name}::PLA Pink::PLA::1000::1.75::None::False`|
|`buddy3d_pla_plared_1000_175_p`|`buddy3d_pla_red_1000_175_p`|`buddy3d.json::Buddy3D::PLA {color_name}::PLA Red::PLA::1000::1.75::None::False`|
|`buddy3d_pla_plasilver_1000_175_p`|`buddy3d_pla_silver_1000_175_p`|`buddy3d.json::Buddy3D::PLA {color_name}::PLA Silver::PLA::1000::1.75::None::False`|
|`buddy3d_pla_plawhite_1000_175_p`|`buddy3d_pla_white_1000_175_p`|`buddy3d.json::Buddy3D::PLA {color_name}::PLA White::PLA::1000::1.75::None::False`|
|`buddy3d_pla_playellow_1000_175_p`|`buddy3d_pla_yellow_1000_175_p`|`buddy3d.json::Buddy3D::PLA {color_name}::PLA Yellow::PLA::1000::1.75::None::False`|
|`buddy3d_pla_silkplablue_1000_175_p`|`buddy3d_pla_plasilkblue_1000_175_p`|`buddy3d.json::Buddy3D::Silk PLA {color_name}::Silk PLA Blue::PLA::1000::1.75::None::False`|
|`buddy3d_pla_silkplabronze_1000_175_p`|`buddy3d_pla_plasilkbronze_1000_175_p`|`buddy3d.json::Buddy3D::Silk PLA {color_name}::Silk PLA Bronze::PLA::1000::1.75::None::False`|
|`buddy3d_pla_silkplacopper_1000_175_p`|`buddy3d_pla_plasilkcopper_1000_175_p`|`buddy3d.json::Buddy3D::Silk PLA {color_name}::Silk PLA Copper::PLA::1000::1.75::None::False`|
|`buddy3d_pla_silkpladarkgold_1000_175_p`|`buddy3d_pla_plasilkdarkgold_1000_175_p`|`buddy3d.json::Buddy3D::Silk PLA {color_name}::Silk PLA Dark gold::PLA::1000::1.75::None::False`|
|`buddy3d_pla_silkplagold_1000_175_p`|`buddy3d_pla_plasilkgold_1000_175_p`|`buddy3d.json::Buddy3D::Silk PLA {color_name}::Silk PLA Gold::PLA::1000::1.75::None::False`|
|`buddy3d_pla_silkplaiceblue_1000_175_p`|`buddy3d_pla_plasilkiceblue_1000_175_p`|`buddy3d.json::Buddy3D::Silk PLA {color_name}::Silk PLA Ice Blue::PLA::1000::1.75::None::False`|
|`buddy3d_pla_silkplapink_1000_175_p`|`buddy3d_pla_plasilkpink_1000_175_p`|`buddy3d.json::Buddy3D::Silk PLA {color_name}::Silk PLA Pink::PLA::1000::1.75::None::False`|
|`buddy3d_pla_silkplared_1000_175_p`|`buddy3d_pla_plasilkred_1000_175_p`|`buddy3d.json::Buddy3D::Silk PLA {color_name}::Silk PLA Red::PLA::1000::1.75::None::False`|
|`buddy3d_pla_silkplarose_1000_175_p`|`buddy3d_pla_plasilkrose_1000_175_p`|`buddy3d.json::Buddy3D::Silk PLA {color_name}::Silk PLA Rose::PLA::1000::1.75::None::False`|
|`buddy3d_pla_silkplaultraviolet_1000_175_p`|`buddy3d_pla_plasilkultraviolet_1000_175_p`|`buddy3d.json::Buddy3D::Silk PLA {color_name}::Silk PLA Ultra Violet::PLA::1000::1.75::None::False`|
|`buddy3d_pla_silkplawhite_1000_175_p`|`buddy3d_pla_plasilkwhite_1000_175_p`|`buddy3d.json::Buddy3D::Silk PLA {color_name}::Silk PLA White::PLA::1000::1.75::None::False`|

## Per-group decisions and unresolved metadata

### BD001: dup-4748252bfbf64672fd8d03115d8199b687f5e3be386d163727cf82612b8df85b

Status: APPROVED; survivor `buddy3d_abs_absblack_750_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_abs_absblack_750_175_p`|`ABS {color_name}`|`Black`|{"source_file": "buddy3d.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / False|
|`buddy3d_abs_black_750_175_p`|`{color_name}`|`Black`|{"source_file": "buddy3d.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_abs_absblack_750_175_p": "000000",
    "buddy3d_abs_black_750_175_p": "080808"
  }
}
```

### BD002: dup-daa9236fd5cae8331a0197af6cecf3254d8090a433001f7aef9fa6bf34e9cb5f

Status: APPROVED; survivor `buddy3d_abs_absgreen_750_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_abs_absgreen_750_175_p`|`ABS {color_name}`|`Green`|{"source_file": "buddy3d.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / False|
|`buddy3d_abs_green_750_175_p`|`{color_name}`|`Green`|{"source_file": "buddy3d.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_abs_absgreen_750_175_p": "089A45",
    "buddy3d_abs_green_750_175_p": "22D133"
  }
}
```

### BD003: dup-d28296e50c2304ce61c461aa340d0770f5284a06257602611e0603418db03463

Status: APPROVED; survivor `buddy3d_abs_absnatural_750_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_abs_absnatural_750_175_p`|`ABS {color_name}`|`Natural`|{"source_file": "buddy3d.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / False|
|`buddy3d_abs_natural_750_175_p`|`{color_name}`|`Natural`|{"source_file": "buddy3d.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_abs_absnatural_750_175_p": "DFDFD3",
    "buddy3d_abs_natural_750_175_p": "EBEDDA"
  },
  "translucent": {
    "buddy3d_abs_absnatural_750_175_p": false,
    "buddy3d_abs_natural_750_175_p": true
  }
}
```

### BD004: dup-abe9ddca798e53453453aaf7f81fbaafd299e8fc29b7d26616f174689c81b4f9

Status: APPROVED; survivor `buddy3d_abs_abswhite_750_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_abs_abswhite_750_175_p`|`ABS {color_name}`|`White`|{"source_file": "buddy3d.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / False|
|`buddy3d_abs_white_750_175_p`|`{color_name}`|`White`|{"source_file": "buddy3d.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{}
```

### BD005: dup-0c2054875885c9d9803dfd16f2a677bdb34b02899076d24e5d0b73ee15ddd9b7

Status: APPROVED; survivor `buddy3d_petg_black_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_petg_black_1000_175_p`|`{color_name}`|`Black`|{"source_file": "buddy3d.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`buddy3d_petg_petgblack_1000_175_p`|`PETG {color_name}`|`Black`|{"source_file": "buddy3d.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 13, "compiled_records": 26} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "buddy3d_petg_black_1000_175_p": 1.27,
    "buddy3d_petg_petgblack_1000_175_p": 1.28
  },
  "extruder_temp": {
    "buddy3d_petg_black_1000_175_p": 250,
    "buddy3d_petg_petgblack_1000_175_p": null
  },
  "bed_temp": {
    "buddy3d_petg_black_1000_175_p": 80,
    "buddy3d_petg_petgblack_1000_175_p": null
  }
}
```

### BD006: dup-0e51d27705a7794fe8866af75426ae8e258c9ab55276e025d31d849798aa787c

Status: APPROVED; survivor `buddy3d_petg_blue_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_petg_blue_1000_175_p`|`{color_name}`|`Blue`|{"source_file": "buddy3d.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`buddy3d_petg_petgblue_1000_175_p`|`PETG {color_name}`|`Blue`|{"source_file": "buddy3d.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 13, "compiled_records": 26} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "buddy3d_petg_blue_1000_175_p": 1.27,
    "buddy3d_petg_petgblue_1000_175_p": 1.28
  },
  "color_hex": {
    "buddy3d_petg_blue_1000_175_p": "288AE0",
    "buddy3d_petg_petgblue_1000_175_p": "0099E6"
  },
  "extruder_temp": {
    "buddy3d_petg_blue_1000_175_p": 250,
    "buddy3d_petg_petgblue_1000_175_p": null
  },
  "bed_temp": {
    "buddy3d_petg_blue_1000_175_p": 80,
    "buddy3d_petg_petgblue_1000_175_p": null
  }
}
```

### BD007: dup-f1aebfabcd7f6dd1960debc9b862cdfb337613daf845b62dd8f340d7819a487a

Status: APPROVED; survivor `buddy3d_petg_brown_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_petg_brown_1000_175_p`|`{color_name}`|`Brown`|{"source_file": "buddy3d.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`buddy3d_petg_petgbrown_1000_175_p`|`PETG {color_name}`|`Brown`|{"source_file": "buddy3d.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 13, "compiled_records": 26} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "buddy3d_petg_brown_1000_175_p": 1.27,
    "buddy3d_petg_petgbrown_1000_175_p": 1.28
  },
  "color_hex": {
    "buddy3d_petg_brown_1000_175_p": "613500",
    "buddy3d_petg_petgbrown_1000_175_p": "694D3F"
  },
  "extruder_temp": {
    "buddy3d_petg_brown_1000_175_p": 250,
    "buddy3d_petg_petgbrown_1000_175_p": null
  },
  "bed_temp": {
    "buddy3d_petg_brown_1000_175_p": 80,
    "buddy3d_petg_petgbrown_1000_175_p": null
  }
}
```

### BD008: dup-d6db104096bf35da9fd6e09daa476e5d6ce67b376ed96df4e57e98edac2fc038

Status: APPROVED; survivor `buddy3d_petg_green_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_petg_green_1000_175_p`|`{color_name}`|`Green`|{"source_file": "buddy3d.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`buddy3d_petg_petggreen_1000_175_p`|`PETG {color_name}`|`Green`|{"source_file": "buddy3d.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 13, "compiled_records": 26} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "buddy3d_petg_green_1000_175_p": 1.27,
    "buddy3d_petg_petggreen_1000_175_p": 1.28
  },
  "color_hex": {
    "buddy3d_petg_green_1000_175_p": "6ACF85",
    "buddy3d_petg_petggreen_1000_175_p": "089A45"
  },
  "extruder_temp": {
    "buddy3d_petg_green_1000_175_p": 250,
    "buddy3d_petg_petggreen_1000_175_p": null
  },
  "bed_temp": {
    "buddy3d_petg_green_1000_175_p": 80,
    "buddy3d_petg_petggreen_1000_175_p": null
  }
}
```

### BD009: dup-343823fc436a8d5647009bad037334bcee6dcb5935feb9338e683bb648598f05

Status: APPROVED; survivor `buddy3d_petg_grey_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_petg_grey_1000_175_p`|`{color_name}`|`Grey`|{"source_file": "buddy3d.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`buddy3d_petg_petggrey_1000_175_p`|`PETG {color_name}`|`Grey`|{"source_file": "buddy3d.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 13, "compiled_records": 26} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "buddy3d_petg_grey_1000_175_p": 1.27,
    "buddy3d_petg_petggrey_1000_175_p": 1.28
  },
  "color_hex": {
    "buddy3d_petg_grey_1000_175_p": "878787",
    "buddy3d_petg_petggrey_1000_175_p": "727376"
  },
  "extruder_temp": {
    "buddy3d_petg_grey_1000_175_p": 250,
    "buddy3d_petg_petggrey_1000_175_p": null
  },
  "bed_temp": {
    "buddy3d_petg_grey_1000_175_p": 80,
    "buddy3d_petg_petggrey_1000_175_p": null
  }
}
```

### BD010: dup-42d0442c9792e4bdbe7f104a12dbefef0f9649b774bdd278af1c026ea632deed

Status: APPROVED; survivor `buddy3d_petg_lila_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_petg_lila_1000_175_p`|`{color_name}`|`Lila`|{"source_file": "buddy3d.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`buddy3d_petg_petglila_1000_175_p`|`PETG {color_name}`|`Lila`|{"source_file": "buddy3d.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 13, "compiled_records": 26} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "buddy3d_petg_lila_1000_175_p": 1.27,
    "buddy3d_petg_petglila_1000_175_p": 1.28
  },
  "color_hex": {
    "buddy3d_petg_lila_1000_175_p": "7634AD",
    "buddy3d_petg_petglila_1000_175_p": "8D65C7"
  },
  "extruder_temp": {
    "buddy3d_petg_lila_1000_175_p": 250,
    "buddy3d_petg_petglila_1000_175_p": null
  },
  "bed_temp": {
    "buddy3d_petg_lila_1000_175_p": 80,
    "buddy3d_petg_petglila_1000_175_p": null
  }
}
```

### BD011: dup-f82ce3276723102accf0bc4fd7c6d634220a0c674ca6e899bbd4c68713e97fef

Status: APPROVED; survivor `buddy3d_petg_red_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_petg_petgred_1000_175_p`|`PETG {color_name}`|`Red`|{"source_file": "buddy3d.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 13, "compiled_records": 26} / False|
|`buddy3d_petg_red_1000_175_p`|`{color_name}`|`Red`|{"source_file": "buddy3d.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "buddy3d_petg_petgred_1000_175_p": 1.28,
    "buddy3d_petg_red_1000_175_p": 1.27
  },
  "color_hex": {
    "buddy3d_petg_petgred_1000_175_p": "FF0505",
    "buddy3d_petg_red_1000_175_p": "FC3714"
  },
  "extruder_temp": {
    "buddy3d_petg_petgred_1000_175_p": null,
    "buddy3d_petg_red_1000_175_p": 250
  },
  "bed_temp": {
    "buddy3d_petg_petgred_1000_175_p": null,
    "buddy3d_petg_red_1000_175_p": 80
  }
}
```

### BD012: dup-5daa47e9caa6c912a9dcb0b57e909265d0104d874dd77d1ced3046ffea645993

Status: APPROVED; survivor `buddy3d_petg_silver_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_petg_petgsilver_1000_175_p`|`PETG {color_name}`|`Silver`|{"source_file": "buddy3d.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 13, "compiled_records": 26} / False|
|`buddy3d_petg_silver_1000_175_p`|`{color_name}`|`Silver`|{"source_file": "buddy3d.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "buddy3d_petg_petgsilver_1000_175_p": 1.28,
    "buddy3d_petg_silver_1000_175_p": 1.27
  },
  "color_hex": {
    "buddy3d_petg_petgsilver_1000_175_p": "A8B0BD",
    "buddy3d_petg_silver_1000_175_p": "B0B0B0"
  },
  "extruder_temp": {
    "buddy3d_petg_petgsilver_1000_175_p": null,
    "buddy3d_petg_silver_1000_175_p": 250
  },
  "bed_temp": {
    "buddy3d_petg_petgsilver_1000_175_p": null,
    "buddy3d_petg_silver_1000_175_p": 80
  }
}
```

### BD013: dup-881666db7c9941e52f2cac8f8d49993a72bbb4cfd4dcfdabaa45c0285dd46aac

Status: APPROVED; survivor `buddy3d_petg_white_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_petg_petgwhite_1000_175_p`|`PETG {color_name}`|`White`|{"source_file": "buddy3d.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 13, "compiled_records": 26} / False|
|`buddy3d_petg_white_1000_175_p`|`{color_name}`|`White`|{"source_file": "buddy3d.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "buddy3d_petg_petgwhite_1000_175_p": 1.28,
    "buddy3d_petg_white_1000_175_p": 1.27
  },
  "extruder_temp": {
    "buddy3d_petg_petgwhite_1000_175_p": null,
    "buddy3d_petg_white_1000_175_p": 250
  },
  "bed_temp": {
    "buddy3d_petg_petgwhite_1000_175_p": null,
    "buddy3d_petg_white_1000_175_p": 80
  }
}
```

### BD014: dup-458863684b8f287b432d2a83231bcabb259601ddbc555628a68b7197b8b7a9af

Status: APPROVED; survivor `buddy3d_petg_yellow_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_petg_petgyellow_1000_175_p`|`PETG {color_name}`|`Yellow`|{"source_file": "buddy3d.json", "definition_index": 15, "weights": 2, "diameters": 1, "colors": 13, "compiled_records": 26} / False|
|`buddy3d_petg_yellow_1000_175_p`|`{color_name}`|`Yellow`|{"source_file": "buddy3d.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "buddy3d_petg_petgyellow_1000_175_p": 1.28,
    "buddy3d_petg_yellow_1000_175_p": 1.27
  },
  "color_hex": {
    "buddy3d_petg_petgyellow_1000_175_p": "F2DE00",
    "buddy3d_petg_yellow_1000_175_p": "FFF645"
  },
  "extruder_temp": {
    "buddy3d_petg_petgyellow_1000_175_p": null,
    "buddy3d_petg_yellow_1000_175_p": 250
  },
  "bed_temp": {
    "buddy3d_petg_petgyellow_1000_175_p": null,
    "buddy3d_petg_yellow_1000_175_p": 80
  }
}
```

### BD015: dup-25f3b8cfe79d2fe5bfc22f87ea2314eaf5bcb7212ea3632e1e28e62b053bf18c

Status: APPROVED; survivor `buddy3d_pla_black_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_black_1000_175_p`|`{color_name}`|`Black`|{"source_file": "buddy3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|
|`buddy3d_pla_plablack_1000_175_p`|`PLA {color_name}`|`Black`|{"source_file": "buddy3d.json", "definition_index": 17, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{}
```

### BD016: dup-9982c733170a5ecf1ef76608d9954bf123c235da1d0422aacdfe76ec47ab9a3e

Status: APPROVED; survivor `buddy3d_pla_blue_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_blue_1000_175_p`|`{color_name}`|`Blue`|{"source_file": "buddy3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|
|`buddy3d_pla_plablue_1000_175_p`|`PLA {color_name}`|`Blue`|{"source_file": "buddy3d.json", "definition_index": 17, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_blue_1000_175_p": "2187ED",
    "buddy3d_pla_plablue_1000_175_p": "0099E6"
  }
}
```

### BD017: dup-e4051bb4b91d74deef55198100ad4209bc457217f83e27d69bbed495480bce66

Status: APPROVED; survivor `buddy3d_pla_brown_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_brown_1000_175_p`|`{color_name}`|`Brown`|{"source_file": "buddy3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|
|`buddy3d_pla_plabrown_1000_175_p`|`PLA {color_name}`|`Brown`|{"source_file": "buddy3d.json", "definition_index": 17, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_brown_1000_175_p": "732C00",
    "buddy3d_pla_plabrown_1000_175_p": "875117"
  }
}
```

### BD018: dup-54050d39ff67f940d164cf7e08a3a515adcf45ad8d03bf8d27872c81b5cc4c44

Status: APPROVED; survivor `buddy3d_pla_green_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_green_1000_175_p`|`{color_name}`|`Green`|{"source_file": "buddy3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|
|`buddy3d_pla_plagreen_1000_175_p`|`PLA {color_name}`|`Green`|{"source_file": "buddy3d.json", "definition_index": 17, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_green_1000_175_p": "40ED60",
    "buddy3d_pla_plagreen_1000_175_p": "26A648"
  }
}
```

### BD019: dup-d327a40836cf3114f32d83cd6e12160953455e4058f23f4897b242cae6ba293b

Status: APPROVED; survivor `buddy3d_pla_grey_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_grey_1000_175_p`|`{color_name}`|`Grey`|{"source_file": "buddy3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|
|`buddy3d_pla_plagrey_1000_175_p`|`PLA {color_name}`|`Grey`|{"source_file": "buddy3d.json", "definition_index": 17, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_grey_1000_175_p": "B8B7AB",
    "buddy3d_pla_plagrey_1000_175_p": "B8BAB8"
  }
}
```

### BD020: dup-7bc82b811b55f652822896af406d7bf173c103d2be8d25dcdd7af71e04386445

Status: APPROVED; survivor `buddy3d_pla_lila_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_lila_1000_175_p`|`{color_name}`|`Lila`|{"source_file": "buddy3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|
|`buddy3d_pla_plalila_1000_175_p`|`PLA {color_name}`|`Lila`|{"source_file": "buddy3d.json", "definition_index": 17, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_lila_1000_175_p": "985AE8",
    "buddy3d_pla_plalila_1000_175_p": "7142A3"
  }
}
```

### BD021: dup-7fc0edbaed63d84e60fa7d3e32e33affa0b7b52fca68aa1f69f6701dfaeec8d2

Status: APPROVED; survivor `buddy3d_pla_pink_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_pink_1000_175_p`|`{color_name}`|`Pink`|{"source_file": "buddy3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|
|`buddy3d_pla_plapink_1000_175_p`|`PLA {color_name}`|`Pink`|{"source_file": "buddy3d.json", "definition_index": 17, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_pink_1000_175_p": "FC7ED6",
    "buddy3d_pla_plapink_1000_175_p": "F6ABD7"
  }
}
```

### BD022: dup-8954032c26a801fd9a434ce249e827dccf1228b1497651401adc263078454d27

Status: DEFERRED; survivor `buddy3d_pla_plaglitterblack/gold_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_plaglitterblack/gold_1000_175_p`|`PLA {color_name}`|`Glitter Black/Gold`|{"source_file": "buddy3d.json", "definition_index": 17, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|
|`buddy3d_pla_plaglitterblackgold_1000_175_p`|`PLA Glitter {color_name}`|`Black Gold`|{"source_file": "buddy3d.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_plaglitterblack/gold_1000_175_p": "000000",
    "buddy3d_pla_plaglitterblackgold_1000_175_p": "141413"
  },
  "pattern": {
    "buddy3d_pla_plaglitterblack/gold_1000_175_p": null,
    "buddy3d_pla_plaglitterblackgold_1000_175_p": "sparkle"
  }
}
```

### BD023: dup-9e825df822229d47b54a27b94ea9c561396c671e66aa75d60f16e6efa2c919e0

Status: APPROVED; survivor `buddy3d_pla_red_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_plared_1000_175_p`|`PLA {color_name}`|`Red`|{"source_file": "buddy3d.json", "definition_index": 17, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|
|`buddy3d_pla_red_1000_175_p`|`{color_name}`|`Red`|{"source_file": "buddy3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_plared_1000_175_p": "FF0505",
    "buddy3d_pla_red_1000_175_p": "FF423B"
  }
}
```

### BD024: dup-de95376ef5eef3ed3c89a429f5d3c91e7e46bf9d773dabecc9610e721b2858b0

Status: APPROVED; survivor `buddy3d_pla_plasilkblue_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_plasilkblue_1000_175_p`|`PLA Silk {color_name}`|`Blue`|{"source_file": "buddy3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|
|`buddy3d_pla_silkplablue_1000_175_p`|`Silk PLA {color_name}`|`Blue`|{"source_file": "buddy3d.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_plasilkblue_1000_175_p": "1D95E0",
    "buddy3d_pla_silkplablue_1000_175_p": "0099E6"
  }
}
```

### BD025: dup-b3ee8dbfeddd15a15b3b23f43d7f1aeec0b8f6c901b0383460343cd8f9ea719f

Status: APPROVED; survivor `buddy3d_pla_plasilkbronze_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_plasilkbronze_1000_175_p`|`PLA Silk {color_name}`|`Bronze`|{"source_file": "buddy3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|
|`buddy3d_pla_silkplabronze_1000_175_p`|`Silk PLA {color_name}`|`Bronze`|{"source_file": "buddy3d.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_plasilkbronze_1000_175_p": "C99A60",
    "buddy3d_pla_silkplabronze_1000_175_p": "8C7354"
  }
}
```

### BD026: dup-e8a4dee64e3237a4ec8c504dd068ebdd3209c83f3c67d35422dd99762b6123e0

Status: APPROVED; survivor `buddy3d_pla_plasilkcopper_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_plasilkcopper_1000_175_p`|`PLA Silk {color_name}`|`Copper`|{"source_file": "buddy3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|
|`buddy3d_pla_silkplacopper_1000_175_p`|`Silk PLA {color_name}`|`Copper`|{"source_file": "buddy3d.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_plasilkcopper_1000_175_p": "E89C74",
    "buddy3d_pla_silkplacopper_1000_175_p": "863938"
  }
}
```

### BD027: dup-c6e3fb682b1d4d5817a3edb90336eb8db61a0cf7c221bd7d00728c9660ba10f4

Status: APPROVED; survivor `buddy3d_pla_plasilkdarkgold_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_plasilkdarkgold_1000_175_p`|`PLA Silk {color_name}`|`Dark Gold`|{"source_file": "buddy3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|
|`buddy3d_pla_silkpladarkgold_1000_175_p`|`Silk PLA {color_name}`|`Dark gold`|{"source_file": "buddy3d.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_plasilkdarkgold_1000_175_p": "DBC63D",
    "buddy3d_pla_silkpladarkgold_1000_175_p": "F3B400"
  }
}
```

### BD028: dup-1d695ae3fb2e109b44275a3154b07cf3327ecf76d7e56e14d263487bdeebac5b

Status: APPROVED; survivor `buddy3d_pla_plasilkgold_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_plasilkgold_1000_175_p`|`PLA Silk {color_name}`|`Gold`|{"source_file": "buddy3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|
|`buddy3d_pla_silkplagold_1000_175_p`|`Silk PLA {color_name}`|`Gold`|{"source_file": "buddy3d.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_plasilkgold_1000_175_p": "FFD500",
    "buddy3d_pla_silkplagold_1000_175_p": "F6C500"
  }
}
```

### BD029: dup-0f18a252a1001416dd96fa71e33c5612858f70e0e8c09dcff0e34e708893e698

Status: APPROVED; survivor `buddy3d_pla_plasilkiceblue_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_plasilkiceblue_1000_175_p`|`PLA Silk {color_name}`|`Ice Blue`|{"source_file": "buddy3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|
|`buddy3d_pla_silkplaiceblue_1000_175_p`|`Silk PLA {color_name}`|`Ice Blue`|{"source_file": "buddy3d.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_plasilkiceblue_1000_175_p": "96DEFF",
    "buddy3d_pla_silkplaiceblue_1000_175_p": "39B9DB"
  }
}
```

### BD030: dup-143150af6b39d39357a1b2290d7b91e3628c934bcc2654cf5f12714cbda87486

Status: APPROVED; survivor `buddy3d_pla_plasilkpink_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_plasilkpink_1000_175_p`|`PLA Silk {color_name}`|`Pink`|{"source_file": "buddy3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|
|`buddy3d_pla_silkplapink_1000_175_p`|`Silk PLA {color_name}`|`Pink`|{"source_file": "buddy3d.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_plasilkpink_1000_175_p": "FC62B9",
    "buddy3d_pla_silkplapink_1000_175_p": "FC6D8E"
  }
}
```

### BD031: dup-4f3adb189d4a4a1e452d3a8ce71b74df0a0b185044f8f14561d36f6324394c8a

Status: APPROVED; survivor `buddy3d_pla_plasilkred_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_plasilkred_1000_175_p`|`PLA Silk {color_name}`|`Red`|{"source_file": "buddy3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|
|`buddy3d_pla_silkplared_1000_175_p`|`Silk PLA {color_name}`|`Red`|{"source_file": "buddy3d.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_plasilkred_1000_175_p": "F55858",
    "buddy3d_pla_silkplared_1000_175_p": "FF0505"
  }
}
```

### BD032: dup-d64ed03f678d8809c79a9fa2f5a32b3b5fe7d435a137807fbb88ab33a0891028

Status: APPROVED; survivor `buddy3d_pla_plasilkrose_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_plasilkrose_1000_175_p`|`PLA Silk {color_name}`|`Rose`|{"source_file": "buddy3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|
|`buddy3d_pla_silkplarose_1000_175_p`|`Silk PLA {color_name}`|`Rose`|{"source_file": "buddy3d.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_plasilkrose_1000_175_p": "F08BC9",
    "buddy3d_pla_silkplarose_1000_175_p": "D93382"
  }
}
```

### BD033: dup-d33b97878e4a5893edb37fc80b3b810701f9c1c722866c5dc3489ab644e8305c

Status: APPROVED; survivor `buddy3d_pla_plasilkultraviolet_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_plasilkultraviolet_1000_175_p`|`PLA Silk {color_name}`|`Ultra Violet`|{"source_file": "buddy3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|
|`buddy3d_pla_silkplaultraviolet_1000_175_p`|`Silk PLA {color_name}`|`Ultra Violet`|{"source_file": "buddy3d.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_plasilkultraviolet_1000_175_p": "A328D4",
    "buddy3d_pla_silkplaultraviolet_1000_175_p": "7769BC"
  }
}
```

### BD034: dup-1033b8adb083c1dc1ecef4c839a3d7b40a33aa45c5fb2b63188f87955e3a8c77

Status: APPROVED; survivor `buddy3d_pla_plasilkwhite_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_plasilkwhite_1000_175_p`|`PLA Silk {color_name}`|`White`|{"source_file": "buddy3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|
|`buddy3d_pla_silkplawhite_1000_175_p`|`Silk PLA {color_name}`|`White`|{"source_file": "buddy3d.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_plasilkwhite_1000_175_p": "F5F5F5",
    "buddy3d_pla_silkplawhite_1000_175_p": "FFFFFF"
  }
}
```

### BD035: dup-d346b91f0f65b0bed75f78dff96f9ae2bfc8048888b88149186601e1166fa4a8

Status: APPROVED; survivor `buddy3d_pla_silver_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_plasilver_1000_175_p`|`PLA {color_name}`|`Silver`|{"source_file": "buddy3d.json", "definition_index": 17, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|
|`buddy3d_pla_silver_1000_175_p`|`{color_name}`|`Silver`|{"source_file": "buddy3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_plasilver_1000_175_p": "A8B0BD",
    "buddy3d_pla_silver_1000_175_p": "A6A6A6"
  }
}
```

### BD036: dup-3c3c678fd843b618109dd61543425585a230a4164ea26ea9d1d061e869305648

Status: APPROVED; survivor `buddy3d_pla_white_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_plawhite_1000_175_p`|`PLA {color_name}`|`White`|{"source_file": "buddy3d.json", "definition_index": 17, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|
|`buddy3d_pla_white_1000_175_p`|`{color_name}`|`White`|{"source_file": "buddy3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_plawhite_1000_175_p": "FFFFFF",
    "buddy3d_pla_white_1000_175_p": "FAFAFA"
  }
}
```

### BD037: dup-d69bc6c043968758da773be54e9eb102a5a84e84d9c8560a18f078549722de35

Status: APPROVED; survivor `buddy3d_pla_yellow_1000_175_p`; owner-pattern override.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`buddy3d_pla_playellow_1000_175_p`|`PLA {color_name}`|`Yellow`|{"source_file": "buddy3d.json", "definition_index": 17, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|
|`buddy3d_pla_yellow_1000_175_p`|`{color_name}`|`Yellow`|{"source_file": "buddy3d.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 11, "compiled_records": 11} / False|

owner-pattern override: older well-formed one-weight family retained over R4 Cartesian weight x color expansion; no unique variants changed

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "buddy3d_pla_playellow_1000_175_p": "F2DE00",
    "buddy3d_pla_yellow_1000_175_p": "F7EC13"
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

- `buddy3d_pla_plaglitterdarkgreen_1000_175_p` — PLA Glitter Dark Green
- `buddy3d_pla_plaglittergreen_1000_175_p` — PLA Glitter Green
- `buddy3d_pla_plaglitterred_1000_175_p` — PLA Glitter Red
- `buddy3d_pla_plapearlblue_1000_175_p` — PLA Pearl Blue
- `buddy3d_pla_plapearlgreen_1000_175_p` — PLA Pearl Green
- `buddy3d_pla_plastonemarblegrey_1000_175_p` — PLA Stone Marble Grey
- `buddy3d_pla+_pla+skintone477c_1000_175_p` — PLA+ Skin tone 477C
- `buddy3d_pla+_pla+skintone478c_1000_175_p` — PLA+ Skin tone 478C
- `buddy3d_pla+_pla+skintone479c_1000_175_p` — PLA+ Skin tone 479C
- `buddy3d_pla+_pla+skintone480c_1000_175_p` — PLA+ Skin tone 480C
- `buddy3d_pla+_pla+lithophane_1000_175_p` — PLA+ Lithophane
- `buddy3d_petg_petgmattblack_1000_175_p` — PETG Matt Black
- `buddy3d_petg_petgmattwhite_1000_175_p` — PETG Matt White
- `buddy3d_asa_asanatural_750_175_p` — ASA Natural
- `buddy3d_asa_asalightblue_750_175_p` — ASA Light Blue
- `buddy3d_asa_asalightgreen_750_175_p` — ASA Light Green
- `buddy3d_asa_asared_750_175_p` — ASA Red
- `buddy3d_asa_asayellow_750_175_p` — ASA Yellow
- `buddy3d_abs+fr_absfrblack_750_175_p` — ABS FR Black
- `buddy3d_abs+fr_absfrnatural_750_175_p` — ABS FR Natural
- `buddy3d_abs+esd_absesdblack_750_175_p` — ABS ESD Black
- `buddy3d_abs_absesdblack_750_175_p` — ABS ESD Black
- `buddy3d_abs_matteabsmattblack_750_175_p` — Matte ABS Matt BLACK
- `buddy3d_petg_petgpink_1000_175_p` — PETG Pink
- `buddy3d_petg_petgradioactivegreen_1000_175_p` — PETG Radioactive Green
- `buddy3d_petg_petgviolettransparent_1000_175_p` — PETG Violet Transparent
- `buddy3d_petg_petgblack_5000_175_p` — PETG Black
- `buddy3d_petg_petgblue_5000_175_p` — PETG Blue
- `buddy3d_petg_petgbrown_5000_175_p` — PETG Brown
- `buddy3d_petg_petggreen_5000_175_p` — PETG Green
- `buddy3d_petg_petggrey_5000_175_p` — PETG Grey
- `buddy3d_petg_petglila_5000_175_p` — PETG Lila
- `buddy3d_petg_petgpink_5000_175_p` — PETG Pink
- `buddy3d_petg_petgradioactivegreen_5000_175_p` — PETG Radioactive Green
- `buddy3d_petg_petgred_5000_175_p` — PETG Red
- `buddy3d_petg_petgsilver_5000_175_p` — PETG Silver
- `buddy3d_petg_petgviolettransparent_5000_175_p` — PETG Violet Transparent
- `buddy3d_petg_petgwhite_5000_175_p` — PETG White
- `buddy3d_petg_petgyellow_5000_175_p` — PETG Yellow
- `buddy3d_pla_glowplainthedark_1000_175_p` — Glow PLA In the dark
- `buddy3d_pla_plabeige_1000_175_p` — PLA Beige
- `buddy3d_pla_plachewigumpink_1000_175_p` — PLA Chewi gum Pink
- `buddy3d_pla_plaglitterblue_1000_175_p` — PLA Glitter Blue
- `buddy3d_pla_plastonesandstone_1000_175_p` — PLA Stone Sandstone
- `buddy3d_pla_platransparent_1000_175_p` — PLA Transparent
- `buddy3d_pla_plabeige_5000_175_p` — PLA Beige
- `buddy3d_pla_plablack_5000_175_p` — PLA Black
- `buddy3d_pla_plablue_5000_175_p` — PLA Blue
- `buddy3d_pla_plabrown_5000_175_p` — PLA Brown
- `buddy3d_pla_plachewigumpink_5000_175_p` — PLA Chewi gum Pink
- `buddy3d_pla_plaglitterblack/gold_5000_175_p` — PLA Glitter Black/Gold
- `buddy3d_pla_plaglitterblue_5000_175_p` — PLA Glitter Blue
- `buddy3d_pla_plagreen_5000_175_p` — PLA Green
- `buddy3d_pla_plagrey_5000_175_p` — PLA Grey
- `buddy3d_pla_plalila_5000_175_p` — PLA Lila
- `buddy3d_pla_plapink_5000_175_p` — PLA Pink
- `buddy3d_pla_plared_5000_175_p` — PLA Red
- `buddy3d_pla_plasilver_5000_175_p` — PLA Silver
- `buddy3d_pla_plastonesandstone_5000_175_p` — PLA Stone Sandstone
- `buddy3d_pla_platransparent_5000_175_p` — PLA Transparent
- `buddy3d_pla_plawhite_5000_175_p` — PLA White
- `buddy3d_pla_playellow_5000_175_p` — PLA Yellow
- `buddy3d_pla_silkplablack_1000_175_p` — Silk PLA Black
