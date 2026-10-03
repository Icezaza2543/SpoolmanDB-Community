# ldo duplicate migration review

Base `72ea8083ccfc1930ad2e331d21c79497c693091d`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `38b1e3cdc65ac470e070cbf0b6a599ba80f314867858bdeff6beeccd31aabbd8`.

## Authorization and result

{"groups": 11, "approved_groups": 11, "retired": 11, "deferred": 0, "hard_stops": 0, "before_count": 51775, "after_count": 51764, "brand_before": 26, "brand_after": 15, "registry_before": 1659, "registry_after": 1670, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Eleven strict Rule1 groups retain survivor values. Current exact ABS matches1.06/260/90–110. Existing ASA260/90–110 lies within current recommendation; density1.08 retained unresolved because official density unit is malformed. No identifiers/doc links transferred. HEX conflicts unresolved. Packaging/tare unchanged.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://store.ldomotion.com/products/abs-filaments", "density": 1.06, "nozzle": 260, "bed": [90, 110]}
- {"url": "https://ldomotion.com/products/16607023627068828", "nozzle": [230, 260], "bed": [90, 110], "note": "ASA density unit is malformed1.14g/m3; not silently converted to g/cm3"}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`ldo_abs_absblack_1000_175_p`|`ldo_abs_black_1000_175_p`|`ldo.json::LDO::ABS {color_name}::ABS Black::ABS::1000::1.75::plastic::False`|
|`ldo_abs_absdarkteal_1000_175_p`|`ldo_abs_darkteal_1000_175_p`|`ldo.json::LDO::ABS {color_name}::ABS Dark Teal::ABS::1000::1.75::plastic::False`|
|`ldo_abs_abslemonlime_1000_175_p`|`ldo_abs_lemonlime_1000_175_p`|`ldo.json::LDO::ABS {color_name}::ABS Lemon Lime::ABS::1000::1.75::plastic::False`|
|`ldo_abs_abslightblue_1000_175_p`|`ldo_abs_lightblue_1000_175_p`|`ldo.json::LDO::ABS {color_name}::ABS Light Blue::ABS::1000::1.75::plastic::False`|
|`ldo_abs_abspurple_1000_175_p`|`ldo_abs_purple_1000_175_p`|`ldo.json::LDO::ABS {color_name}::ABS Purple::ABS::1000::1.75::plastic::False`|
|`ldo_abs_absred_1000_175_p`|`ldo_abs_red_1000_175_p`|`ldo.json::LDO::ABS {color_name}::ABS Red::ABS::1000::1.75::plastic::False`|
|`ldo_abs_abssmokegray_1000_175_p`|`ldo_abs_smokegray_1000_175_p`|`ldo.json::LDO::ABS {color_name}::ABS Smoke Gray::ABS::1000::1.75::plastic::False`|
|`ldo_abs_absstardustgray_1000_175_p`|`ldo_abs_stardustgray_1000_175_p`|`ldo.json::LDO::ABS {color_name}::ABS Stardust Gray::ABS::1000::1.75::plastic::False`|
|`ldo_abs_abswhite_1000_175_p`|`ldo_abs_white_1000_175_p`|`ldo.json::LDO::ABS {color_name}::ABS White::ABS::1000::1.75::plastic::False`|
|`ldo_asa_asaolivegreen_1000_175_p`|`ldo_asa_olivegreen_1000_175_p`|`ldo.json::LDO::ASA {color_name}::ASA Olive Green::ASA::1000::1.75::plastic::False`|
|`ldo_asa_asaorange_1000_175_p`|`ldo_asa_orange_1000_175_p`|`ldo.json::LDO::ASA {color_name}::ASA Orange::ASA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### LD001: dup-827f8022c1d5ffccb66a63424964c760c0bbd918de7f9848270e76b0e35e20a2

Status: APPROVED; survivor `ldo_abs_black_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ldo_abs_absblack_1000_175_p`|`ABS {color_name}`|`Black`|{"source_file": "ldo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`ldo_abs_black_1000_175_p`|`{color_name}`|`Black`|{"source_file": "ldo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "ldo_abs_absblack_1000_175_p": null,
    "ldo_abs_black_1000_175_p": 260
  },
  "extruder_temp_range": {
    "ldo_abs_absblack_1000_175_p": [
      250,
      270
    ],
    "ldo_abs_black_1000_175_p": null
  }
}
```

### LD002: dup-f84eb04a7797291ccfc42d69dfc6a241e24576abdb0f2cc632f457b01a704416

Status: APPROVED; survivor `ldo_abs_darkteal_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ldo_abs_absdarkteal_1000_175_p`|`ABS {color_name}`|`Dark Teal`|{"source_file": "ldo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`ldo_abs_darkteal_1000_175_p`|`{color_name}`|`Dark Teal`|{"source_file": "ldo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ldo_abs_absdarkteal_1000_175_p": "00677F",
    "ldo_abs_darkteal_1000_175_p": "00677f"
  },
  "extruder_temp": {
    "ldo_abs_absdarkteal_1000_175_p": null,
    "ldo_abs_darkteal_1000_175_p": 260
  },
  "extruder_temp_range": {
    "ldo_abs_absdarkteal_1000_175_p": [
      250,
      270
    ],
    "ldo_abs_darkteal_1000_175_p": null
  }
}
```

### LD003: dup-c1ad6773c2aad0143a4b54b24aeb81957a514170f444f2eaec455c50ea5ce225

Status: APPROVED; survivor `ldo_abs_lemonlime_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ldo_abs_abslemonlime_1000_175_p`|`ABS {color_name}`|`Lemon Lime`|{"source_file": "ldo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`ldo_abs_lemonlime_1000_175_p`|`{color_name}`|`Lemon Lime`|{"source_file": "ldo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ldo_abs_abslemonlime_1000_175_p": "D6E865",
    "ldo_abs_lemonlime_1000_175_p": "d6e865"
  },
  "extruder_temp": {
    "ldo_abs_abslemonlime_1000_175_p": null,
    "ldo_abs_lemonlime_1000_175_p": 260
  },
  "extruder_temp_range": {
    "ldo_abs_abslemonlime_1000_175_p": [
      250,
      270
    ],
    "ldo_abs_lemonlime_1000_175_p": null
  }
}
```

### LD004: dup-dea24d188286341303f8aadabe8422983a2718214eb901ec575cabe36f96bec7

Status: APPROVED; survivor `ldo_abs_lightblue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ldo_abs_abslightblue_1000_175_p`|`ABS {color_name}`|`Light Blue`|{"source_file": "ldo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`ldo_abs_lightblue_1000_175_p`|`{color_name}`|`Light Blue`|{"source_file": "ldo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ldo_abs_abslightblue_1000_175_p": "6AD1E3",
    "ldo_abs_lightblue_1000_175_p": "6ad1e3"
  },
  "extruder_temp": {
    "ldo_abs_abslightblue_1000_175_p": null,
    "ldo_abs_lightblue_1000_175_p": 260
  },
  "extruder_temp_range": {
    "ldo_abs_abslightblue_1000_175_p": [
      250,
      270
    ],
    "ldo_abs_lightblue_1000_175_p": null
  }
}
```

### LD005: dup-b68efc289063eb5c4701c10c3455a546892ede5c66d9da4205217e5a242f706e

Status: APPROVED; survivor `ldo_abs_purple_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ldo_abs_abspurple_1000_175_p`|`ABS {color_name}`|`Purple`|{"source_file": "ldo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`ldo_abs_purple_1000_175_p`|`{color_name}`|`Purple`|{"source_file": "ldo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "ldo_abs_abspurple_1000_175_p": null,
    "ldo_abs_purple_1000_175_p": 260
  },
  "extruder_temp_range": {
    "ldo_abs_abspurple_1000_175_p": [
      250,
      270
    ],
    "ldo_abs_purple_1000_175_p": null
  }
}
```

### LD006: dup-cc6389f9d5c70774a678b8538a63ab07f49c472c220d116108497bb851b94cbe

Status: APPROVED; survivor `ldo_abs_red_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ldo_abs_absred_1000_175_p`|`ABS {color_name}`|`Red`|{"source_file": "ldo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`ldo_abs_red_1000_175_p`|`{color_name}`|`Red`|{"source_file": "ldo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "ldo_abs_absred_1000_175_p": null,
    "ldo_abs_red_1000_175_p": 260
  },
  "extruder_temp_range": {
    "ldo_abs_absred_1000_175_p": [
      250,
      270
    ],
    "ldo_abs_red_1000_175_p": null
  }
}
```

### LD007: dup-9344c4d3bd9715ca70181ac5f4a9270bea0a647bb31f4d74d1c483b3630440ca

Status: APPROVED; survivor `ldo_abs_smokegray_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ldo_abs_abssmokegray_1000_175_p`|`ABS {color_name}`|`Smoke Gray`|{"source_file": "ldo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`ldo_abs_smokegray_1000_175_p`|`{color_name}`|`Smoke Gray`|{"source_file": "ldo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "ldo_abs_abssmokegray_1000_175_p": null,
    "ldo_abs_smokegray_1000_175_p": 260
  },
  "extruder_temp_range": {
    "ldo_abs_abssmokegray_1000_175_p": [
      250,
      270
    ],
    "ldo_abs_smokegray_1000_175_p": null
  }
}
```

### LD008: dup-5a3adfcbcc859aa86fceee3dfcf6b309ebc62934b0607139521af0da55b2f833

Status: APPROVED; survivor `ldo_abs_stardustgray_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ldo_abs_absstardustgray_1000_175_p`|`ABS {color_name}`|`Stardust Gray`|{"source_file": "ldo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`ldo_abs_stardustgray_1000_175_p`|`{color_name}`|`Stardust Gray`|{"source_file": "ldo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "ldo_abs_absstardustgray_1000_175_p": null,
    "ldo_abs_stardustgray_1000_175_p": 260
  },
  "extruder_temp_range": {
    "ldo_abs_absstardustgray_1000_175_p": [
      250,
      270
    ],
    "ldo_abs_stardustgray_1000_175_p": null
  }
}
```

### LD009: dup-2c46cd79ecef4ac2a8fb87beed1c133ecbf7026fcb91b613577835f646aba2a9

Status: APPROVED; survivor `ldo_abs_white_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ldo_abs_abswhite_1000_175_p`|`ABS {color_name}`|`White`|{"source_file": "ldo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`ldo_abs_white_1000_175_p`|`{color_name}`|`White`|{"source_file": "ldo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ldo_abs_abswhite_1000_175_p": "F7F9EF",
    "ldo_abs_white_1000_175_p": "f7f9ef"
  },
  "extruder_temp": {
    "ldo_abs_abswhite_1000_175_p": null,
    "ldo_abs_white_1000_175_p": 260
  },
  "extruder_temp_range": {
    "ldo_abs_abswhite_1000_175_p": [
      250,
      270
    ],
    "ldo_abs_white_1000_175_p": null
  }
}
```

### LD010: dup-4ec62482fef0011792099e05ef03a3e7b6426a2b7e5b005b9c00a7653162d2fa

Status: APPROVED; survivor `ldo_asa_olivegreen_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ldo_asa_asaolivegreen_1000_175_p`|`ASA {color_name}`|`Olive Green`|{"source_file": "ldo.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / False|
|`ldo_asa_olivegreen_1000_175_p`|`{color_name}`|`Olive Green`|{"source_file": "ldo.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ldo_asa_asaolivegreen_1000_175_p": "4B5E23",
    "ldo_asa_olivegreen_1000_175_p": "4b5e23"
  },
  "extruder_temp": {
    "ldo_asa_asaolivegreen_1000_175_p": null,
    "ldo_asa_olivegreen_1000_175_p": 260
  },
  "extruder_temp_range": {
    "ldo_asa_asaolivegreen_1000_175_p": [
      250,
      270
    ],
    "ldo_asa_olivegreen_1000_175_p": null
  }
}
```

### LD011: dup-426c00ce18ad360368ab18d8669727dcf3b4823ab70f436dfca3bef111d7014e

Status: APPROVED; survivor `ldo_asa_orange_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ldo_asa_asaorange_1000_175_p`|`ASA {color_name}`|`Orange`|{"source_file": "ldo.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / False|
|`ldo_asa_orange_1000_175_p`|`{color_name}`|`Orange`|{"source_file": "ldo.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ldo_asa_asaorange_1000_175_p": "F93822",
    "ldo_asa_orange_1000_175_p": "f93822"
  },
  "extruder_temp": {
    "ldo_asa_asaorange_1000_175_p": null,
    "ldo_asa_orange_1000_175_p": 260
  },
  "extruder_temp_range": {
    "ldo_asa_asaorange_1000_175_p": [
      250,
      270
    ],
    "ldo_asa_orange_1000_175_p": null
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

- `ldo_abs_ldoblue_1000_175_p` — LDO Blue
- `ldo_asa-cf_black_1000_175_p` — Black
- `ldo_abs_absldoblue_1000_175_p` — ABS LDO Blue
- `ldo_asa_asa-cfblack_1000_175_p` — ASA-CF Black
