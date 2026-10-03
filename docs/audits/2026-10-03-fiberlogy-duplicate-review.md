# fiberlogy duplicate migration review

Base `affb0ec7ac9c008aecf887147afcf7b3e3144808`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `568b4eed28c9f1d5216d30734e0fcaf3707c3137e33d4a6e757fc611342b58a9`.

## Authorization and result

{"groups": 27, "approved_groups": 0, "retired": 0, "deferred": 27, "hard_stops": 0, "before_count": 51889, "after_count": 51889, "brand_before": 595, "brand_after": 595, "registry_before": 1545, "registry_after": 1545, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Audit-only: all27groups deferred.13ASA750g otherwise physical matches cannot transfer identifiers while preserving unrelated1000g bindings under current source semantics. Local regression produced14 duplicateGTIN warnings and202pass/1fail; no compiled key/payload mismatch. Reverted uncommitted source/baseline/registry exactly, no checker/tests change. CurrentASA page confirms retained1.07/260/110 and current matching documents; document corrections are postponed with the retirement. Existing weight bindings remain unresolved. Packaging/tare unchanged.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. Future reviewed retirements would not redirect external catalog lookups automatically.

## Current first-party evidence

- {"url": "https://fiberlogy.com/en/product/asa-filament/", "density": 1.07, "nozzle": [255, 270], "bed": 110, "tds": "https://fiberlogy.com/app/uploads/2026/05/FIBERLOGY_ASA_TDS.pdf", "sds": "https://fiberlogy.com/app/uploads/2026/05/FIBERLOGY_ASA_SDS_EN.pdf", "note": "Exact current page confirms values and actively links current matching documents; old upload/techfiles TDS404. No PDF printing values inferred from failed text extraction."}
- {"url": "https://fiberlogy.com/en/product/abs-plus-filament-s2-4/", "note": "Blocked ABSPLUS exactline density1.05/nozzle250–270/bed100; do not apply because strict qualifier/color decomposition andGray/Grey ambiguity unresolved."}
- {"url": "https://fiberlogy.com/en/product/rpp-filament/", "note": "Blocked rPP exactline1.05/nozzle220–250; strictR line/color decomposition unresolved."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### FL001: dup-07ebcbf93ecf8cc0112817509c8f84c495d4e37a687f7d8c060630dbc0a6af80

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_abs_absgray_850_175_p`|`ABS {color_name}`|`Gray`|{"source_file": "fiberlogy.json", "definition_index": 1, "weights": 2, "diameters": 1, "colors": 27, "compiled_records": 54} / False|
|`fiberlogy_abs_absgrey_850_175_p`|`ABS {color_name}`|`Grey`|{"source_file": "fiberlogy.json", "definition_index": 1, "weights": 2, "diameters": 1, "colors": 27, "compiled_records": 54} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "fiberlogy_abs_absgray_850_175_p": "BBBCBC",
    "fiberlogy_abs_absgrey_850_175_p": "C5C5BF"
  },
  "codes": {
    "fiberlogy_abs_absgray_850_175_p": [
      "ABS-GRAY-175-085"
    ],
    "fiberlogy_abs_absgrey_850_175_p": null
  },
  "eans": {
    "fiberlogy_abs_absgray_850_175_p": [
      "5902560993813"
    ],
    "fiberlogy_abs_absgrey_850_175_p": null
  }
}
```

### FL002: dup-fdeb0e7f48710584747c4bc856e93c89ec3e4f8915f513c6ee0ce5fde2d9ccea

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_abs_absgray_1000_175_p`|`ABS {color_name}`|`Gray`|{"source_file": "fiberlogy.json", "definition_index": 1, "weights": 2, "diameters": 1, "colors": 27, "compiled_records": 54} / False|
|`fiberlogy_abs_absgrey_1000_175_p`|`ABS {color_name}`|`Grey`|{"source_file": "fiberlogy.json", "definition_index": 1, "weights": 2, "diameters": 1, "colors": 27, "compiled_records": 54} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "fiberlogy_abs_absgray_1000_175_p": "BBBCBC",
    "fiberlogy_abs_absgrey_1000_175_p": "C5C5BF"
  },
  "codes": {
    "fiberlogy_abs_absgray_1000_175_p": [
      "ABS-GRAY-175-085"
    ],
    "fiberlogy_abs_absgrey_1000_175_p": null
  },
  "eans": {
    "fiberlogy_abs_absgray_1000_175_p": [
      "5902560993813"
    ],
    "fiberlogy_abs_absgrey_1000_175_p": null
  }
}
```

### FL003: dup-faf9d4c8d3e8cf3eef63254f5190c651bdc4b8d2847ddd57b293fdf0ed5fdba1

Status: DEFERRED; survivor `fiberlogy_abs_absplusgrey_850_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_abs_absplusgray_850_175_p`|`ABS PLUS {color_name}`|`Gray`|{"source_file": "fiberlogy.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`fiberlogy_abs_absplusgrey_850_175_p`|`ABS {color_name}`|`PLUS Grey`|{"source_file": "fiberlogy.json", "definition_index": 1, "weights": 2, "diameters": 1, "colors": 27, "compiled_records": 54} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "fiberlogy_abs_absplusgray_850_175_p": 1.03,
    "fiberlogy_abs_absplusgrey_850_175_p": 1.04
  },
  "color_hex": {
    "fiberlogy_abs_absplusgray_850_175_p": "BBBCBC",
    "fiberlogy_abs_absplusgrey_850_175_p": "C5C5BF"
  },
  "extruder_temp": {
    "fiberlogy_abs_absplusgray_850_175_p": 257,
    "fiberlogy_abs_absplusgrey_850_175_p": null
  },
  "extruder_temp_range": {
    "fiberlogy_abs_absplusgray_850_175_p": null,
    "fiberlogy_abs_absplusgrey_850_175_p": [
      230,
      260
    ]
  },
  "bed_temp": {
    "fiberlogy_abs_absplusgray_850_175_p": 100,
    "fiberlogy_abs_absplusgrey_850_175_p": null
  },
  "bed_temp_range": {
    "fiberlogy_abs_absplusgray_850_175_p": null,
    "fiberlogy_abs_absplusgrey_850_175_p": [
      90,
      110
    ]
  },
  "codes": {
    "fiberlogy_abs_absplusgray_850_175_p": [
      "ABS-PLUS-GRAY-175-085"
    ],
    "fiberlogy_abs_absplusgrey_850_175_p": null
  },
  "eans": {
    "fiberlogy_abs_absplusgray_850_175_p": [
      "5902560994179"
    ],
    "fiberlogy_abs_absplusgrey_850_175_p": null
  },
  "sds_url": {
    "fiberlogy_abs_absplusgray_850_175_p": "https://fiberlogy.com/upload/techfiles/FIBERLOGY_ABSPLUS_SDS_EN.pdf",
    "fiberlogy_abs_absplusgrey_850_175_p": "https://fiberlogy.com/upload/techfiles/FIBERLOGY_ABS_SDS_EN.pdf"
  },
  "tds_url": {
    "fiberlogy_abs_absplusgray_850_175_p": "https://fiberlogy.com/upload/techfiles/FIBERLOGY_ABSPLUS_TDS.pdf",
    "fiberlogy_abs_absplusgrey_850_175_p": "https://fiberlogy.com/upload/techfiles/FIBERLOGY_ABS_TDS.pdf"
  }
}
```

### FL004: dup-1570824e4330210fc75f44de4c427fcc9de83e306fa072458df5f5b35b579e58

Status: DEFERRED; survivor `fiberlogy_asa_black_750_175_p`; Tooling block: exact750g EAN transfer creates source-level duplicate GTIN with untouched1000g definition; changing unrelated bindings or checker is not authorized. Preserve all original records/identifiers pending scoped reconciliation..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_asa_asablack_750_175_p`|`ASA {color_name}`|`Black`|{"source_file": "fiberlogy.json", "definition_index": 8, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|
|`fiberlogy_asa_black_750_175_p`|`{color_name}`|`Black`|{"source_file": "fiberlogy.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "fiberlogy_asa_asablack_750_175_p": null,
    "fiberlogy_asa_black_750_175_p": 260
  },
  "extruder_temp": {
    "fiberlogy_asa_asablack_750_175_p": null,
    "fiberlogy_asa_black_750_175_p": 260
  },
  "extruder_temp_range": {
    "fiberlogy_asa_asablack_750_175_p": [
      235,
      260
    ],
    "fiberlogy_asa_black_750_175_p": null
  },
  "bed_temp": {
    "fiberlogy_asa_asablack_750_175_p": null,
    "fiberlogy_asa_black_750_175_p": 110
  },
  "bed_temp_range": {
    "fiberlogy_asa_asablack_750_175_p": [
      90,
      110
    ],
    "fiberlogy_asa_black_750_175_p": null
  },
  "codes": {
    "fiberlogy_asa_asablack_750_175_p": [
      "ASA-BLACK-175-075"
    ],
    "fiberlogy_asa_black_750_175_p": null
  },
  "eans": {
    "fiberlogy_asa_asablack_750_175_p": [
      "5902560991796"
    ],
    "fiberlogy_asa_black_750_175_p": null
  }
}
```

### FL005: dup-009af81872320f4eb89126a3ec283dd23e1ca4e29624fa0c7b58e984d8b280e6

Status: DEFERRED; survivor `fiberlogy_asa_blue_750_175_p`; Tooling block: exact750g EAN transfer creates source-level duplicate GTIN with untouched1000g definition; changing unrelated bindings or checker is not authorized. Preserve all original records/identifiers pending scoped reconciliation..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_asa_asablue_750_175_p`|`ASA {color_name}`|`Blue`|{"source_file": "fiberlogy.json", "definition_index": 8, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|
|`fiberlogy_asa_blue_750_175_p`|`{color_name}`|`Blue`|{"source_file": "fiberlogy.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "fiberlogy_asa_asablue_750_175_p": null,
    "fiberlogy_asa_blue_750_175_p": 260
  },
  "color_hex": {
    "fiberlogy_asa_asablue_750_175_p": "0092BC",
    "fiberlogy_asa_blue_750_175_p": "0072BB"
  },
  "extruder_temp": {
    "fiberlogy_asa_asablue_750_175_p": null,
    "fiberlogy_asa_blue_750_175_p": 260
  },
  "extruder_temp_range": {
    "fiberlogy_asa_asablue_750_175_p": [
      235,
      260
    ],
    "fiberlogy_asa_blue_750_175_p": null
  },
  "bed_temp": {
    "fiberlogy_asa_asablue_750_175_p": null,
    "fiberlogy_asa_blue_750_175_p": 110
  },
  "bed_temp_range": {
    "fiberlogy_asa_asablue_750_175_p": [
      90,
      110
    ],
    "fiberlogy_asa_blue_750_175_p": null
  },
  "codes": {
    "fiberlogy_asa_asablue_750_175_p": [
      "ASA-BLUE-175-075"
    ],
    "fiberlogy_asa_blue_750_175_p": null
  },
  "eans": {
    "fiberlogy_asa_asablue_750_175_p": [
      "5902560991833"
    ],
    "fiberlogy_asa_blue_750_175_p": null
  }
}
```

### FL006: dup-73a2be73416cf5527b63615887d62cde5412022c6086ce333b50854240f9a348

Status: DEFERRED; survivor `fiberlogy_asa_graphite_750_175_p`; Tooling block: exact750g EAN transfer creates source-level duplicate GTIN with untouched1000g definition; changing unrelated bindings or checker is not authorized. Preserve all original records/identifiers pending scoped reconciliation..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_asa_asagraphite_750_175_p`|`ASA {color_name}`|`Graphite`|{"source_file": "fiberlogy.json", "definition_index": 8, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|
|`fiberlogy_asa_graphite_750_175_p`|`{color_name}`|`Graphite`|{"source_file": "fiberlogy.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "fiberlogy_asa_asagraphite_750_175_p": null,
    "fiberlogy_asa_graphite_750_175_p": 260
  },
  "color_hex": {
    "fiberlogy_asa_asagraphite_750_175_p": "53565A",
    "fiberlogy_asa_graphite_750_175_p": "474A51"
  },
  "extruder_temp": {
    "fiberlogy_asa_asagraphite_750_175_p": null,
    "fiberlogy_asa_graphite_750_175_p": 260
  },
  "extruder_temp_range": {
    "fiberlogy_asa_asagraphite_750_175_p": [
      235,
      260
    ],
    "fiberlogy_asa_graphite_750_175_p": null
  },
  "bed_temp": {
    "fiberlogy_asa_asagraphite_750_175_p": null,
    "fiberlogy_asa_graphite_750_175_p": 110
  },
  "bed_temp_range": {
    "fiberlogy_asa_asagraphite_750_175_p": [
      90,
      110
    ],
    "fiberlogy_asa_graphite_750_175_p": null
  },
  "codes": {
    "fiberlogy_asa_asagraphite_750_175_p": [
      "ASA-GRAPHITE-175-075"
    ],
    "fiberlogy_asa_graphite_750_175_p": null
  },
  "eans": {
    "fiberlogy_asa_asagraphite_750_175_p": [
      "5902560991826"
    ],
    "fiberlogy_asa_graphite_750_175_p": null
  }
}
```

### FL007: dup-c9edf5efd23f20be61f218c4e2cbb5fe01dccd1481ec5b641b89018c1eea47fc

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_asa_asagray_1000_175_p`|`ASA {color_name}`|`Gray`|{"source_file": "fiberlogy.json", "definition_index": 8, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|
|`fiberlogy_asa_asagrey_1000_175_p`|`ASA {color_name}`|`Grey`|{"source_file": "fiberlogy.json", "definition_index": 8, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "fiberlogy_asa_asagray_1000_175_p": "BBBCBC",
    "fiberlogy_asa_asagrey_1000_175_p": "C5C5BF"
  },
  "codes": {
    "fiberlogy_asa_asagray_1000_175_p": [
      "ASA-GRAY-175-075"
    ],
    "fiberlogy_asa_asagrey_1000_175_p": null
  },
  "eans": {
    "fiberlogy_asa_asagray_1000_175_p": [
      "5902560991871"
    ],
    "fiberlogy_asa_asagrey_1000_175_p": null
  }
}
```

### FL008: dup-dd633b62d0e5ce19d985c61299696348d4f395795511a984387ecd1a13b234de

Status: DEFERRED; survivor `fiberlogy_asa_gray_750_175_p`; Three-member ASA750 group contains Gray/Grey intra-template ambiguity, differentHEX and unboundGrey; no same-SKU proof, defer whole group.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_asa_asagray_750_175_p`|`ASA {color_name}`|`Gray`|{"source_file": "fiberlogy.json", "definition_index": 8, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|
|`fiberlogy_asa_asagrey_750_175_p`|`ASA {color_name}`|`Grey`|{"source_file": "fiberlogy.json", "definition_index": 8, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|
|`fiberlogy_asa_gray_750_175_p`|`{color_name}`|`Gray`|{"source_file": "fiberlogy.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "fiberlogy_asa_asagray_750_175_p": null,
    "fiberlogy_asa_asagrey_750_175_p": null,
    "fiberlogy_asa_gray_750_175_p": 260
  },
  "color_hex": {
    "fiberlogy_asa_asagray_750_175_p": "BBBCBC",
    "fiberlogy_asa_asagrey_750_175_p": "C5C5BF",
    "fiberlogy_asa_gray_750_175_p": "808080"
  },
  "extruder_temp": {
    "fiberlogy_asa_asagray_750_175_p": null,
    "fiberlogy_asa_asagrey_750_175_p": null,
    "fiberlogy_asa_gray_750_175_p": 260
  },
  "extruder_temp_range": {
    "fiberlogy_asa_asagray_750_175_p": [
      235,
      260
    ],
    "fiberlogy_asa_asagrey_750_175_p": [
      235,
      260
    ],
    "fiberlogy_asa_gray_750_175_p": null
  },
  "bed_temp": {
    "fiberlogy_asa_asagray_750_175_p": null,
    "fiberlogy_asa_asagrey_750_175_p": null,
    "fiberlogy_asa_gray_750_175_p": 110
  },
  "bed_temp_range": {
    "fiberlogy_asa_asagray_750_175_p": [
      90,
      110
    ],
    "fiberlogy_asa_asagrey_750_175_p": [
      90,
      110
    ],
    "fiberlogy_asa_gray_750_175_p": null
  },
  "codes": {
    "fiberlogy_asa_asagray_750_175_p": [
      "ASA-GRAY-175-075"
    ],
    "fiberlogy_asa_asagrey_750_175_p": null,
    "fiberlogy_asa_gray_750_175_p": null
  },
  "eans": {
    "fiberlogy_asa_asagray_750_175_p": [
      "5902560991871"
    ],
    "fiberlogy_asa_asagrey_750_175_p": null,
    "fiberlogy_asa_gray_750_175_p": null
  }
}
```

### FL009: dup-d090c7d9b8e6f5a24b4b8ac0a201748c315124e3454a06b284397264ea1235da

Status: DEFERRED; survivor `fiberlogy_asa_inox_750_175_p`; Tooling block: exact750g EAN transfer creates source-level duplicate GTIN with untouched1000g definition; changing unrelated bindings or checker is not authorized. Preserve all original records/identifiers pending scoped reconciliation..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_asa_asainox_750_175_p`|`ASA {color_name}`|`Inox`|{"source_file": "fiberlogy.json", "definition_index": 8, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|
|`fiberlogy_asa_inox_750_175_p`|`{color_name}`|`Inox`|{"source_file": "fiberlogy.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "fiberlogy_asa_asainox_750_175_p": null,
    "fiberlogy_asa_inox_750_175_p": 260
  },
  "color_hex": {
    "fiberlogy_asa_asainox_750_175_p": "969AA3",
    "fiberlogy_asa_inox_750_175_p": "C0C0C0"
  },
  "extruder_temp": {
    "fiberlogy_asa_asainox_750_175_p": null,
    "fiberlogy_asa_inox_750_175_p": 260
  },
  "extruder_temp_range": {
    "fiberlogy_asa_asainox_750_175_p": [
      235,
      260
    ],
    "fiberlogy_asa_inox_750_175_p": null
  },
  "bed_temp": {
    "fiberlogy_asa_asainox_750_175_p": null,
    "fiberlogy_asa_inox_750_175_p": 110
  },
  "bed_temp_range": {
    "fiberlogy_asa_asainox_750_175_p": [
      90,
      110
    ],
    "fiberlogy_asa_inox_750_175_p": null
  },
  "codes": {
    "fiberlogy_asa_asainox_750_175_p": [
      "ASA-INOX-175-075"
    ],
    "fiberlogy_asa_inox_750_175_p": null
  },
  "eans": {
    "fiberlogy_asa_asainox_750_175_p": [
      "5902560991765"
    ],
    "fiberlogy_asa_inox_750_175_p": null
  }
}
```

### FL010: dup-cc7ed72794907540cbc2912fe1a2baeefb5177853f7dd88ae42fd77a31c97941

Status: DEFERRED; survivor `fiberlogy_asa_lightgreen_750_175_p`; Tooling block: exact750g EAN transfer creates source-level duplicate GTIN with untouched1000g definition; changing unrelated bindings or checker is not authorized. Preserve all original records/identifiers pending scoped reconciliation..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_asa_asalightgreen_750_175_p`|`ASA {color_name}`|`Light Green`|{"source_file": "fiberlogy.json", "definition_index": 8, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|
|`fiberlogy_asa_lightgreen_750_175_p`|`{color_name}`|`Light Green`|{"source_file": "fiberlogy.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "fiberlogy_asa_asalightgreen_750_175_p": null,
    "fiberlogy_asa_lightgreen_750_175_p": 260
  },
  "color_hex": {
    "fiberlogy_asa_asalightgreen_750_175_p": "A7D500",
    "fiberlogy_asa_lightgreen_750_175_p": "90EE90"
  },
  "extruder_temp": {
    "fiberlogy_asa_asalightgreen_750_175_p": null,
    "fiberlogy_asa_lightgreen_750_175_p": 260
  },
  "extruder_temp_range": {
    "fiberlogy_asa_asalightgreen_750_175_p": [
      235,
      260
    ],
    "fiberlogy_asa_lightgreen_750_175_p": null
  },
  "bed_temp": {
    "fiberlogy_asa_asalightgreen_750_175_p": null,
    "fiberlogy_asa_lightgreen_750_175_p": 110
  },
  "bed_temp_range": {
    "fiberlogy_asa_asalightgreen_750_175_p": [
      90,
      110
    ],
    "fiberlogy_asa_lightgreen_750_175_p": null
  },
  "codes": {
    "fiberlogy_asa_asalightgreen_750_175_p": [
      "ASA-LGREEN-175-075"
    ],
    "fiberlogy_asa_lightgreen_750_175_p": null
  },
  "eans": {
    "fiberlogy_asa_asalightgreen_750_175_p": [
      "5902560991888"
    ],
    "fiberlogy_asa_lightgreen_750_175_p": null
  }
}
```

### FL011: dup-5c0da0ead9cc228563574bbd99c0a8c9f4766fc580c86616c17ab142923d677d

Status: DEFERRED; survivor `fiberlogy_asa_natural_750_175_p`; Tooling block: exact750g EAN transfer creates source-level duplicate GTIN with untouched1000g definition; changing unrelated bindings or checker is not authorized. Preserve all original records/identifiers pending scoped reconciliation..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_asa_asanatural_750_175_p`|`ASA {color_name}`|`Natural`|{"source_file": "fiberlogy.json", "definition_index": 8, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|
|`fiberlogy_asa_natural_750_175_p`|`{color_name}`|`Natural`|{"source_file": "fiberlogy.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "fiberlogy_asa_asanatural_750_175_p": null,
    "fiberlogy_asa_natural_750_175_p": 260
  },
  "color_hex": {
    "fiberlogy_asa_asanatural_750_175_p": "FAF8DF",
    "fiberlogy_asa_natural_750_175_p": "F5F5DC"
  },
  "extruder_temp": {
    "fiberlogy_asa_asanatural_750_175_p": null,
    "fiberlogy_asa_natural_750_175_p": 260
  },
  "extruder_temp_range": {
    "fiberlogy_asa_asanatural_750_175_p": [
      235,
      260
    ],
    "fiberlogy_asa_natural_750_175_p": null
  },
  "bed_temp": {
    "fiberlogy_asa_asanatural_750_175_p": null,
    "fiberlogy_asa_natural_750_175_p": 110
  },
  "bed_temp_range": {
    "fiberlogy_asa_asanatural_750_175_p": [
      90,
      110
    ],
    "fiberlogy_asa_natural_750_175_p": null
  },
  "codes": {
    "fiberlogy_asa_asanatural_750_175_p": [
      "ASA-NATURAL-175-075"
    ],
    "fiberlogy_asa_natural_750_175_p": null
  },
  "eans": {
    "fiberlogy_asa_asanatural_750_175_p": [
      "5902560991857"
    ],
    "fiberlogy_asa_natural_750_175_p": null
  }
}
```

### FL012: dup-0f8e5bf3ed6af6451cb597871140dda249706b5d619d3d47caf0109abb7475fe

Status: DEFERRED; survivor `fiberlogy_asa_olivegreen_750_175_p`; Tooling block: exact750g EAN transfer creates source-level duplicate GTIN with untouched1000g definition; changing unrelated bindings or checker is not authorized. Preserve all original records/identifiers pending scoped reconciliation..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_asa_asaolivegreen_750_175_p`|`ASA {color_name}`|`Olive Green`|{"source_file": "fiberlogy.json", "definition_index": 8, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|
|`fiberlogy_asa_olivegreen_750_175_p`|`{color_name}`|`Olive Green`|{"source_file": "fiberlogy.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "fiberlogy_asa_asaolivegreen_750_175_p": null,
    "fiberlogy_asa_olivegreen_750_175_p": 260
  },
  "color_hex": {
    "fiberlogy_asa_asaolivegreen_750_175_p": "33401C",
    "fiberlogy_asa_olivegreen_750_175_p": "808000"
  },
  "extruder_temp": {
    "fiberlogy_asa_asaolivegreen_750_175_p": null,
    "fiberlogy_asa_olivegreen_750_175_p": 260
  },
  "extruder_temp_range": {
    "fiberlogy_asa_asaolivegreen_750_175_p": [
      235,
      260
    ],
    "fiberlogy_asa_olivegreen_750_175_p": null
  },
  "bed_temp": {
    "fiberlogy_asa_asaolivegreen_750_175_p": null,
    "fiberlogy_asa_olivegreen_750_175_p": 110
  },
  "bed_temp_range": {
    "fiberlogy_asa_asaolivegreen_750_175_p": [
      90,
      110
    ],
    "fiberlogy_asa_olivegreen_750_175_p": null
  },
  "codes": {
    "fiberlogy_asa_asaolivegreen_750_175_p": [
      "ASA-OLIVEGREEN-175-075"
    ],
    "fiberlogy_asa_olivegreen_750_175_p": null
  },
  "eans": {
    "fiberlogy_asa_asaolivegreen_750_175_p": [
      "5902560991741"
    ],
    "fiberlogy_asa_olivegreen_750_175_p": null
  }
}
```

### FL013: dup-9cedeafc62ec5af5f80815326db701e050a69e66574086efd22f1f80156739fd

Status: DEFERRED; survivor `fiberlogy_asa_onyx_750_175_p`; Tooling block: exact750g EAN transfer creates source-level duplicate GTIN with untouched1000g definition; changing unrelated bindings or checker is not authorized. Preserve all original records/identifiers pending scoped reconciliation..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_asa_asaonyx_750_175_p`|`ASA {color_name}`|`Onyx`|{"source_file": "fiberlogy.json", "definition_index": 8, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|
|`fiberlogy_asa_onyx_750_175_p`|`{color_name}`|`Onyx`|{"source_file": "fiberlogy.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "fiberlogy_asa_asaonyx_750_175_p": null,
    "fiberlogy_asa_onyx_750_175_p": 260
  },
  "color_hex": {
    "fiberlogy_asa_asaonyx_750_175_p": "262626",
    "fiberlogy_asa_onyx_750_175_p": "353839"
  },
  "extruder_temp": {
    "fiberlogy_asa_asaonyx_750_175_p": null,
    "fiberlogy_asa_onyx_750_175_p": 260
  },
  "extruder_temp_range": {
    "fiberlogy_asa_asaonyx_750_175_p": [
      235,
      260
    ],
    "fiberlogy_asa_onyx_750_175_p": null
  },
  "bed_temp": {
    "fiberlogy_asa_asaonyx_750_175_p": null,
    "fiberlogy_asa_onyx_750_175_p": 110
  },
  "bed_temp_range": {
    "fiberlogy_asa_asaonyx_750_175_p": [
      90,
      110
    ],
    "fiberlogy_asa_onyx_750_175_p": null
  },
  "codes": {
    "fiberlogy_asa_asaonyx_750_175_p": [
      "ASA-ONYX-175-075"
    ],
    "fiberlogy_asa_onyx_750_175_p": null
  },
  "eans": {
    "fiberlogy_asa_asaonyx_750_175_p": [
      "5902560991789"
    ],
    "fiberlogy_asa_onyx_750_175_p": null
  }
}
```

### FL014: dup-9f84be225dbbd4b5e590170e495468d5a52b4186d51e7ede52e23821b901f089

Status: DEFERRED; survivor `fiberlogy_asa_orange_750_175_p`; Tooling block: exact750g EAN transfer creates source-level duplicate GTIN with untouched1000g definition; changing unrelated bindings or checker is not authorized. Preserve all original records/identifiers pending scoped reconciliation..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_asa_asaorange_750_175_p`|`ASA {color_name}`|`Orange`|{"source_file": "fiberlogy.json", "definition_index": 8, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|
|`fiberlogy_asa_orange_750_175_p`|`{color_name}`|`Orange`|{"source_file": "fiberlogy.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "fiberlogy_asa_asaorange_750_175_p": null,
    "fiberlogy_asa_orange_750_175_p": 260
  },
  "color_hex": {
    "fiberlogy_asa_asaorange_750_175_p": "FF6900",
    "fiberlogy_asa_orange_750_175_p": "FFB200"
  },
  "extruder_temp": {
    "fiberlogy_asa_asaorange_750_175_p": null,
    "fiberlogy_asa_orange_750_175_p": 260
  },
  "extruder_temp_range": {
    "fiberlogy_asa_asaorange_750_175_p": [
      235,
      260
    ],
    "fiberlogy_asa_orange_750_175_p": null
  },
  "bed_temp": {
    "fiberlogy_asa_asaorange_750_175_p": null,
    "fiberlogy_asa_orange_750_175_p": 110
  },
  "bed_temp_range": {
    "fiberlogy_asa_asaorange_750_175_p": [
      90,
      110
    ],
    "fiberlogy_asa_orange_750_175_p": null
  },
  "codes": {
    "fiberlogy_asa_asaorange_750_175_p": [
      "ASA-ORANGE-175-075"
    ],
    "fiberlogy_asa_orange_750_175_p": null
  },
  "eans": {
    "fiberlogy_asa_asaorange_750_175_p": [
      "5902560991840"
    ],
    "fiberlogy_asa_orange_750_175_p": null
  }
}
```

### FL015: dup-21c892a0296946176d3ff02f7bd5269a410291c2a464b0c812895383c6840231

Status: DEFERRED; survivor `fiberlogy_asa_red_750_175_p`; Tooling block: exact750g EAN transfer creates source-level duplicate GTIN with untouched1000g definition; changing unrelated bindings or checker is not authorized. Preserve all original records/identifiers pending scoped reconciliation..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_asa_asared_750_175_p`|`ASA {color_name}`|`Red`|{"source_file": "fiberlogy.json", "definition_index": 8, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|
|`fiberlogy_asa_red_750_175_p`|`{color_name}`|`Red`|{"source_file": "fiberlogy.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "fiberlogy_asa_asared_750_175_p": null,
    "fiberlogy_asa_red_750_175_p": 260
  },
  "color_hex": {
    "fiberlogy_asa_asared_750_175_p": "FF0000",
    "fiberlogy_asa_red_750_175_p": "C41E3A"
  },
  "extruder_temp": {
    "fiberlogy_asa_asared_750_175_p": null,
    "fiberlogy_asa_red_750_175_p": 260
  },
  "extruder_temp_range": {
    "fiberlogy_asa_asared_750_175_p": [
      235,
      260
    ],
    "fiberlogy_asa_red_750_175_p": null
  },
  "bed_temp": {
    "fiberlogy_asa_asared_750_175_p": null,
    "fiberlogy_asa_red_750_175_p": 110
  },
  "bed_temp_range": {
    "fiberlogy_asa_asared_750_175_p": [
      90,
      110
    ],
    "fiberlogy_asa_red_750_175_p": null
  },
  "codes": {
    "fiberlogy_asa_asared_750_175_p": [
      "ASA-RED-175-075"
    ],
    "fiberlogy_asa_red_750_175_p": null
  },
  "eans": {
    "fiberlogy_asa_asared_750_175_p": [
      "5902560991758"
    ],
    "fiberlogy_asa_red_750_175_p": null
  }
}
```

### FL016: dup-1db950ce5c92c34f8c2013db8131c2f85ef3cd119e0f29af67fc6b1517faede7

Status: DEFERRED; survivor `fiberlogy_asa_vertigo_750_175_p`; Tooling block: exact750g EAN transfer creates source-level duplicate GTIN with untouched1000g definition; changing unrelated bindings or checker is not authorized. Preserve all original records/identifiers pending scoped reconciliation..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_asa_asavertigo_750_175_p`|`ASA {color_name}`|`Vertigo`|{"source_file": "fiberlogy.json", "definition_index": 8, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|
|`fiberlogy_asa_vertigo_750_175_p`|`{color_name}`|`Vertigo`|{"source_file": "fiberlogy.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "fiberlogy_asa_asavertigo_750_175_p": null,
    "fiberlogy_asa_vertigo_750_175_p": 260
  },
  "color_hex": {
    "fiberlogy_asa_asavertigo_750_175_p": "282828",
    "fiberlogy_asa_vertigo_750_175_p": "708090"
  },
  "extruder_temp": {
    "fiberlogy_asa_asavertigo_750_175_p": null,
    "fiberlogy_asa_vertigo_750_175_p": 260
  },
  "extruder_temp_range": {
    "fiberlogy_asa_asavertigo_750_175_p": [
      235,
      260
    ],
    "fiberlogy_asa_vertigo_750_175_p": null
  },
  "bed_temp": {
    "fiberlogy_asa_asavertigo_750_175_p": null,
    "fiberlogy_asa_vertigo_750_175_p": 110
  },
  "bed_temp_range": {
    "fiberlogy_asa_asavertigo_750_175_p": [
      90,
      110
    ],
    "fiberlogy_asa_vertigo_750_175_p": null
  },
  "codes": {
    "fiberlogy_asa_asavertigo_750_175_p": [
      "ASA-VERTIGO-175-075"
    ],
    "fiberlogy_asa_vertigo_750_175_p": null
  },
  "eans": {
    "fiberlogy_asa_asavertigo_750_175_p": [
      "5902560991772"
    ],
    "fiberlogy_asa_vertigo_750_175_p": null
  }
}
```

### FL017: dup-c5899608b6029e91a378cb9572d7a55d86d5804bac7e89e045ede6ccc003d35c

Status: DEFERRED; survivor `fiberlogy_asa_white_750_175_p`; Tooling block: exact750g EAN transfer creates source-level duplicate GTIN with untouched1000g definition; changing unrelated bindings or checker is not authorized. Preserve all original records/identifiers pending scoped reconciliation..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_asa_asawhite_750_175_p`|`ASA {color_name}`|`White`|{"source_file": "fiberlogy.json", "definition_index": 8, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|
|`fiberlogy_asa_white_750_175_p`|`{color_name}`|`White`|{"source_file": "fiberlogy.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "fiberlogy_asa_asawhite_750_175_p": null,
    "fiberlogy_asa_white_750_175_p": 260
  },
  "extruder_temp": {
    "fiberlogy_asa_asawhite_750_175_p": null,
    "fiberlogy_asa_white_750_175_p": 260
  },
  "extruder_temp_range": {
    "fiberlogy_asa_asawhite_750_175_p": [
      235,
      260
    ],
    "fiberlogy_asa_white_750_175_p": null
  },
  "bed_temp": {
    "fiberlogy_asa_asawhite_750_175_p": null,
    "fiberlogy_asa_white_750_175_p": 110
  },
  "bed_temp_range": {
    "fiberlogy_asa_asawhite_750_175_p": [
      90,
      110
    ],
    "fiberlogy_asa_white_750_175_p": null
  },
  "codes": {
    "fiberlogy_asa_asawhite_750_175_p": [
      "ASA-WHITE-175-075"
    ],
    "fiberlogy_asa_white_750_175_p": null
  },
  "eans": {
    "fiberlogy_asa_asawhite_750_175_p": [
      "5902560991864"
    ],
    "fiberlogy_asa_white_750_175_p": null
  }
}
```

### FL018: dup-d8dc0d278a89be1767c1fedad23a39803d78c21ff655ef9b1c4b4c77e5d1b20d

Status: DEFERRED; survivor `fiberlogy_asa_yellow_750_175_p`; Tooling block: exact750g EAN transfer creates source-level duplicate GTIN with untouched1000g definition; changing unrelated bindings or checker is not authorized. Preserve all original records/identifiers pending scoped reconciliation..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_asa_asayellow_750_175_p`|`ASA {color_name}`|`Yellow`|{"source_file": "fiberlogy.json", "definition_index": 8, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|
|`fiberlogy_asa_yellow_750_175_p`|`{color_name}`|`Yellow`|{"source_file": "fiberlogy.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 14, "compiled_records": 14} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "fiberlogy_asa_asayellow_750_175_p": null,
    "fiberlogy_asa_yellow_750_175_p": 260
  },
  "extruder_temp": {
    "fiberlogy_asa_asayellow_750_175_p": null,
    "fiberlogy_asa_yellow_750_175_p": 260
  },
  "extruder_temp_range": {
    "fiberlogy_asa_asayellow_750_175_p": [
      235,
      260
    ],
    "fiberlogy_asa_yellow_750_175_p": null
  },
  "bed_temp": {
    "fiberlogy_asa_asayellow_750_175_p": null,
    "fiberlogy_asa_yellow_750_175_p": 110
  },
  "bed_temp_range": {
    "fiberlogy_asa_asayellow_750_175_p": [
      90,
      110
    ],
    "fiberlogy_asa_yellow_750_175_p": null
  },
  "codes": {
    "fiberlogy_asa_asayellow_750_175_p": [
      "ASA-YELLOW-175-075"
    ],
    "fiberlogy_asa_yellow_750_175_p": null
  },
  "eans": {
    "fiberlogy_asa_asayellow_750_175_p": [
      "5902560991895"
    ],
    "fiberlogy_asa_yellow_750_175_p": null
  }
}
```

### FL019: dup-41d47905d6af939a8155f07ce8304f9cf76377ef6748fbed298643b7183ecf0c

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_pctg_pctggray_1000_175_p`|`PCTG {color_name}`|`Gray`|{"source_file": "fiberlogy.json", "definition_index": 25, "weights": 2, "diameters": 1, "colors": 16, "compiled_records": 32} / False|
|`fiberlogy_pctg_pctggrey_1000_175_p`|`PCTG {color_name}`|`Grey`|{"source_file": "fiberlogy.json", "definition_index": 25, "weights": 2, "diameters": 1, "colors": 16, "compiled_records": 32} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "fiberlogy_pctg_pctggray_1000_175_p": "BBBCBC",
    "fiberlogy_pctg_pctggrey_1000_175_p": "C5C5BF"
  },
  "codes": {
    "fiberlogy_pctg_pctggray_1000_175_p": [
      "PCTG-GRAY-175-075"
    ],
    "fiberlogy_pctg_pctggrey_1000_175_p": null
  },
  "eans": {
    "fiberlogy_pctg_pctggray_1000_175_p": [
      "5902560996678"
    ],
    "fiberlogy_pctg_pctggrey_1000_175_p": null
  }
}
```

### FL020: dup-5c1d19df7e34d7f55fef9f35c647c85c49e64e3a5a093a4e45115e90d040fb30

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_pctg_pctggray_750_175_p`|`PCTG {color_name}`|`Gray`|{"source_file": "fiberlogy.json", "definition_index": 25, "weights": 2, "diameters": 1, "colors": 16, "compiled_records": 32} / False|
|`fiberlogy_pctg_pctggrey_750_175_p`|`PCTG {color_name}`|`Grey`|{"source_file": "fiberlogy.json", "definition_index": 25, "weights": 2, "diameters": 1, "colors": 16, "compiled_records": 32} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "fiberlogy_pctg_pctggray_750_175_p": "BBBCBC",
    "fiberlogy_pctg_pctggrey_750_175_p": "C5C5BF"
  },
  "codes": {
    "fiberlogy_pctg_pctggray_750_175_p": [
      "PCTG-GRAY-175-075"
    ],
    "fiberlogy_pctg_pctggrey_750_175_p": null
  },
  "eans": {
    "fiberlogy_pctg_pctggray_750_175_p": [
      "5902560996678"
    ],
    "fiberlogy_pctg_pctggrey_750_175_p": null
  }
}
```

### FL021: dup-839afa98731094aac0bae39da8a86ccdcec48983f3bb3c076d12e2c7379b31af

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_pla_easyplagray_1000_175_p`|`Easy PLA {color_name}`|`Gray`|{"source_file": "fiberlogy.json", "definition_index": 38, "weights": 2, "diameters": 1, "colors": 46, "compiled_records": 92} / False|
|`fiberlogy_pla_easyplagrey_1000_175_p`|`Easy PLA {color_name}`|`Grey`|{"source_file": "fiberlogy.json", "definition_index": 38, "weights": 2, "diameters": 1, "colors": 46, "compiled_records": 92} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "fiberlogy_pla_easyplagray_1000_175_p": "BBBCBC",
    "fiberlogy_pla_easyplagrey_1000_175_p": "C5C5BF"
  },
  "codes": {
    "fiberlogy_pla_easyplagray_1000_175_p": [
      "EASY-GRAY-175-085"
    ],
    "fiberlogy_pla_easyplagrey_1000_175_p": null
  },
  "eans": {
    "fiberlogy_pla_easyplagray_1000_175_p": [
      "5902560994599"
    ],
    "fiberlogy_pla_easyplagrey_1000_175_p": null
  }
}
```

### FL022: dup-ca8d889cabc187e50b216b405f039bc2e204d548a468a49b45e42e0313bb303a

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_pla_easyplagray_850_175_p`|`Easy PLA {color_name}`|`Gray`|{"source_file": "fiberlogy.json", "definition_index": 38, "weights": 2, "diameters": 1, "colors": 46, "compiled_records": 92} / False|
|`fiberlogy_pla_easyplagrey_850_175_p`|`Easy PLA {color_name}`|`Grey`|{"source_file": "fiberlogy.json", "definition_index": 38, "weights": 2, "diameters": 1, "colors": 46, "compiled_records": 92} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "fiberlogy_pla_easyplagray_850_175_p": "BBBCBC",
    "fiberlogy_pla_easyplagrey_850_175_p": "C5C5BF"
  },
  "codes": {
    "fiberlogy_pla_easyplagray_850_175_p": [
      "EASY-GRAY-175-085"
    ],
    "fiberlogy_pla_easyplagrey_850_175_p": null
  },
  "eans": {
    "fiberlogy_pla_easyplagray_850_175_p": [
      "5902560994599"
    ],
    "fiberlogy_pla_easyplagrey_850_175_p": null
  }
}
```

### FL023: dup-2f7273758c5c5b57aae07c653d34311fa6e3e47d65590e5e180df73182bfe734

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_pla_impactplagray_1000_175_p`|`Impact PLA {color_name}`|`Gray`|{"source_file": "fiberlogy.json", "definition_index": 45, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|
|`fiberlogy_pla_impactplagrey_1000_175_p`|`Impact PLA {color_name}`|`Grey`|{"source_file": "fiberlogy.json", "definition_index": 45, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "fiberlogy_pla_impactplagray_1000_175_p": "BBBCBC",
    "fiberlogy_pla_impactplagrey_1000_175_p": "C5C5BF"
  },
  "codes": {
    "fiberlogy_pla_impactplagray_1000_175_p": [
      "PLA-IM-GRAY-175-085"
    ],
    "fiberlogy_pla_impactplagrey_1000_175_p": null
  },
  "eans": {
    "fiberlogy_pla_impactplagray_1000_175_p": [
      "5902560995114"
    ],
    "fiberlogy_pla_impactplagrey_1000_175_p": null
  }
}
```

### FL024: dup-f2cc62d3fb63a2b4518a6946bda162d62ed27aa7406024e786882e0dbf5e8b58

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_pla_impactplagray_850_175_p`|`Impact PLA {color_name}`|`Gray`|{"source_file": "fiberlogy.json", "definition_index": 45, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|
|`fiberlogy_pla_impactplagrey_850_175_p`|`Impact PLA {color_name}`|`Grey`|{"source_file": "fiberlogy.json", "definition_index": 45, "weights": 2, "diameters": 1, "colors": 15, "compiled_records": 30} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "fiberlogy_pla_impactplagray_850_175_p": "BBBCBC",
    "fiberlogy_pla_impactplagrey_850_175_p": "C5C5BF"
  },
  "codes": {
    "fiberlogy_pla_impactplagray_850_175_p": [
      "PLA-IM-GRAY-175-085"
    ],
    "fiberlogy_pla_impactplagrey_850_175_p": null
  },
  "eans": {
    "fiberlogy_pla_impactplagray_850_175_p": [
      "5902560995114"
    ],
    "fiberlogy_pla_impactplagrey_850_175_p": null
  }
}
```

### FL025: dup-8bbbd2473fc7febdcd68b472073e71e4e2ecaa2509b04953e0829de3fc78dec0

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_pp_ppgray_750_175_p`|`PP {color_name}`|`Gray`|{"source_file": "fiberlogy.json", "definition_index": 51, "weights": 2, "diameters": 1, "colors": 12, "compiled_records": 24} / False|
|`fiberlogy_pp_ppgrey_750_175_p`|`PP {color_name}`|`Grey`|{"source_file": "fiberlogy.json", "definition_index": 51, "weights": 2, "diameters": 1, "colors": 12, "compiled_records": 24} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "fiberlogy_pp_ppgray_750_175_p": "BBBCBC",
    "fiberlogy_pp_ppgrey_750_175_p": "C5C5BF"
  },
  "codes": {
    "fiberlogy_pp_ppgray_750_175_p": [
      "PP-GRAY-175-075"
    ],
    "fiberlogy_pp_ppgrey_750_175_p": null
  },
  "eans": {
    "fiberlogy_pp_ppgray_750_175_p": [
      "5902560993424"
    ],
    "fiberlogy_pp_ppgrey_750_175_p": null
  }
}
```

### FL026: dup-8dbfbd48b4b86877dd9c10a2b09fc53c13cc39188c75a52ea0fe87357ca4bfbe

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_pp_ppgray_1000_175_p`|`PP {color_name}`|`Gray`|{"source_file": "fiberlogy.json", "definition_index": 51, "weights": 2, "diameters": 1, "colors": 12, "compiled_records": 24} / False|
|`fiberlogy_pp_ppgrey_1000_175_p`|`PP {color_name}`|`Grey`|{"source_file": "fiberlogy.json", "definition_index": 51, "weights": 2, "diameters": 1, "colors": 12, "compiled_records": 24} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "fiberlogy_pp_ppgray_1000_175_p": "BBBCBC",
    "fiberlogy_pp_ppgrey_1000_175_p": "C5C5BF"
  },
  "codes": {
    "fiberlogy_pp_ppgray_1000_175_p": [
      "PP-GRAY-175-075"
    ],
    "fiberlogy_pp_ppgrey_1000_175_p": null
  },
  "eans": {
    "fiberlogy_pp_ppgray_1000_175_p": [
      "5902560993424"
    ],
    "fiberlogy_pp_ppgrey_1000_175_p": null
  }
}
```

### FL027: dup-a4be2f041b75302871e9dc2a69aaaf15806c963b962b16b5757acec21d7968ee

Status: DEFERRED; survivor `fiberlogy_pp_ppranthracite_750_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`fiberlogy_pp_ppranthracite_750_175_p`|`PP {color_name}`|`R Anthracite`|{"source_file": "fiberlogy.json", "definition_index": 51, "weights": 2, "diameters": 1, "colors": 12, "compiled_records": 24} / False|
|`fiberlogy_pp_rppanthracite_750_175_p`|`R PP {color_name}`|`Anthracite`|{"source_file": "fiberlogy.json", "definition_index": 52, "weights": 1, "diameters": 1, "colors": 1, "compiled_records": 1} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "fiberlogy_pp_ppranthracite_750_175_p": "26272B",
    "fiberlogy_pp_rppanthracite_750_175_p": "0E100D"
  },
  "extruder_temp": {
    "fiberlogy_pp_ppranthracite_750_175_p": null,
    "fiberlogy_pp_rppanthracite_750_175_p": 240
  },
  "extruder_temp_range": {
    "fiberlogy_pp_ppranthracite_750_175_p": [
      210,
      240
    ],
    "fiberlogy_pp_rppanthracite_750_175_p": null
  },
  "bed_temp": {
    "fiberlogy_pp_ppranthracite_750_175_p": null,
    "fiberlogy_pp_rppanthracite_750_175_p": 100
  },
  "bed_temp_range": {
    "fiberlogy_pp_ppranthracite_750_175_p": [
      80,
      100
    ],
    "fiberlogy_pp_rppanthracite_750_175_p": null
  },
  "sds_url": {
    "fiberlogy_pp_ppranthracite_750_175_p": "https://fiberlogy.com/upload/techfiles/FIBERLOGY_PP_SDS_EN.pdf",
    "fiberlogy_pp_rppanthracite_750_175_p": null
  },
  "tds_url": {
    "fiberlogy_pp_ppranthracite_750_175_p": "https://fiberlogy.com/upload/techfiles/FIBERLOGY_PP_TDS.pdf",
    "fiberlogy_pp_rppanthracite_750_175_p": null
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

- `fiberlogy_abs_absbeige_850_175_p` — ABS Beige
- `fiberlogy_abs_absblack_850_175_p` — ABS Black
- `fiberlogy_abs_absblue_850_175_p` — ABS Blue
- `fiberlogy_abs_absburgundy_850_175_p` — ABS Burgundy
- `fiberlogy_abs_abseasybluetransparent_850_175_p` — ABS Easy Blue Transparent
- `fiberlogy_abs_abseasynavybluetransparent_850_175_p` — ABS Easy Navy Blue Transparent
- `fiberlogy_abs_abseasy-puretransparent_850_175_p` — ABS Easy - Pure Transparent
- `fiberlogy_abs_abseasy-transparentburgundy_850_175_p` — ABS Easy - Transparent Burgundy
- `fiberlogy_abs_abseasy-transparentlightgreen_850_175_p` — ABS Easy - Transparent Light Green
- `fiberlogy_abs_abseasy-transparentorange_850_175_p` — ABS Easy - Transparent Orange
- `fiberlogy_abs_absesd_850_175_p` — ABS ESD
- `fiberlogy_abs_absgraphite_850_175_p` — ABS Graphite
- `fiberlogy_abs_absgreen_850_175_p` — ABS Green
- `fiberlogy_abs_absinox_850_175_p` — ABS Inox
- `fiberlogy_abs_absinoxsteel_850_175_p` — ABS Inox Steel
- `fiberlogy_abs_abslightgreen_850_175_p` — ABS Light Green
- `fiberlogy_abs_absnavyblue_850_175_p` — ABS Navy Blue
- `fiberlogy_abs_absonyx_850_175_p` — ABS Onyx
- `fiberlogy_abs_absorange_850_175_p` — ABS Orange
- `fiberlogy_abs_absranthracite_850_175_p` — ABS R Anthracite
- `fiberlogy_abs_absred_850_175_p` — ABS Red
- `fiberlogy_abs_absvertigo_850_175_p` — ABS Vertigo
- `fiberlogy_abs_abswhite_850_175_p` — ABS White
- `fiberlogy_abs_absyellow_850_175_p` — ABS Yellow
- `fiberlogy_abs_absbeige_1000_175_p` — ABS Beige
- `fiberlogy_abs_absblack_1000_175_p` — ABS Black
- `fiberlogy_abs_absblue_1000_175_p` — ABS Blue
- `fiberlogy_abs_absburgundy_1000_175_p` — ABS Burgundy
- `fiberlogy_abs_abseasybluetransparent_1000_175_p` — ABS Easy Blue Transparent
- `fiberlogy_abs_abseasynavybluetransparent_1000_175_p` — ABS Easy Navy Blue Transparent
- `fiberlogy_abs_abseasy-puretransparent_1000_175_p` — ABS Easy - Pure Transparent
- `fiberlogy_abs_abseasy-transparentburgundy_1000_175_p` — ABS Easy - Transparent Burgundy
- `fiberlogy_abs_abseasy-transparentlightgreen_1000_175_p` — ABS Easy - Transparent Light Green
- `fiberlogy_abs_abseasy-transparentorange_1000_175_p` — ABS Easy - Transparent Orange
- `fiberlogy_abs_absesd_1000_175_p` — ABS ESD
- `fiberlogy_abs_absgraphite_1000_175_p` — ABS Graphite
- `fiberlogy_abs_absgreen_1000_175_p` — ABS Green
- `fiberlogy_abs_absinox_1000_175_p` — ABS Inox
- `fiberlogy_abs_absinoxsteel_1000_175_p` — ABS Inox Steel
- `fiberlogy_abs_abslightgreen_1000_175_p` — ABS Light Green
- `fiberlogy_abs_absnavyblue_1000_175_p` — ABS Navy Blue
- `fiberlogy_abs_absonyx_1000_175_p` — ABS Onyx
- `fiberlogy_abs_absorange_1000_175_p` — ABS Orange
- `fiberlogy_abs_absplusgrey_1000_175_p` — ABS PLUS Grey
- `fiberlogy_abs_absranthracite_1000_175_p` — ABS R Anthracite
- `fiberlogy_abs_absred_1000_175_p` — ABS Red
- `fiberlogy_abs_absvertigo_1000_175_p` — ABS Vertigo
- `fiberlogy_abs_abswhite_1000_175_p` — ABS White
- `fiberlogy_abs_absyellow_1000_175_p` — ABS Yellow
- `fiberlogy_abs_absesdblack_500_175_p` — ABS ESD Black
- `fiberlogy_abs_absplusblack_850_175_p` — ABS PLUS Black
- `fiberlogy_abs_absplusblue_850_175_p` — ABS PLUS Blue
- `fiberlogy_abs_absplusgraphite_850_175_p` — ABS PLUS Graphite
- `fiberlogy_abs_absplusred_850_175_p` — ABS PLUS Red
- `fiberlogy_abs_abspluswhite_850_175_p` — ABS PLUS White
- `fiberlogy_abs_absplusyellow_850_175_p` — ABS PLUS Yellow
- `fiberlogy_abs_easyabsbluetransparent_750_175_p` — EASY ABS Blue Transparent
- `fiberlogy_abs_easyabsburgundytransparent_750_175_p` — EASY ABS Burgundy Transparent
- `fiberlogy_abs_easyabslightgreentransparent_750_175_p` — EASY ABS Light Green Transparent
- `fiberlogy_abs_easyabsnavybluetransparent_750_175_p` — EASY ABS Navy Blue Transparent
- `fiberlogy_abs_easyabsorangetransparent_750_175_p` — EASY ABS Orange Transparent
- `fiberlogy_abs_easyabspuretransparent_750_175_p` — EASY ABS Pure Transparent
- `fiberlogy_abs_rabsanthracite_750_175_p` — R ABS Anthracite
- `fiberlogy_abs_refillabsblack_850_175_p` — Refill ABS Black
- `fiberlogy_abs_refillabsgraphite_850_175_p` — Refill ABS Graphite
- `fiberlogy_abs_refillabsgray_850_175_p` — Refill ABS Gray
- `fiberlogy_abs_refillabswhite_850_175_p` — Refill ABS White
- `fiberlogy_abs_refillrabsanthracite_750_175_p` — Refill R ABS Anthracite
- `fiberlogy_asa_asablack_1000_175_p` — ASA Black
- `fiberlogy_asa_asablue_1000_175_p` — ASA Blue
- `fiberlogy_asa_asagraphite_1000_175_p` — ASA Graphite
- `fiberlogy_asa_asainox_1000_175_p` — ASA Inox
- `fiberlogy_asa_asalightgreen_1000_175_p` — ASA Light Green
- `fiberlogy_asa_asanatural_1000_175_p` — ASA Natural
- `fiberlogy_asa_asaolivegreen_1000_175_p` — ASA Olive Green
- `fiberlogy_asa_asaonyx_1000_175_p` — ASA Onyx
- `fiberlogy_asa_asaorange_1000_175_p` — ASA Orange
- `fiberlogy_asa_asared_1000_175_p` — ASA Red
- `fiberlogy_asa_asavertigo_1000_175_p` — ASA Vertigo
- `fiberlogy_asa_asawhite_1000_175_p` — ASA White
- `fiberlogy_asa_asayellow_1000_175_p` — ASA Yellow
- `fiberlogy_asa_matteasablack_1000_175_p` — Matte ASA Black
- `fiberlogy_asa_matteasagraphite_1000_175_p` — Matte ASA Graphite
- `fiberlogy_asa_matteasagrey_1000_175_p` — Matte ASA Grey
- `fiberlogy_asa_matteasanatural_1000_175_p` — Matte ASA Natural
- `fiberlogy_asa_matteasaolivegreen_1000_175_p` — Matte ASA Olive Green
- `fiberlogy_bvoh_bvohnatural_500_175_p` — BVOH Natural
- `fiberlogy_cpe_cpeantibacnatural_1000_175_p` — CPE ANTIBAC Natural
- `fiberlogy_cpe_cpehtblack_1000_175_p` — CPE HT Black
- `fiberlogy_cpe_cpehtpuretransparent_750_175_p` — CPE HT Pure Transparent
- `fiberlogy_hips_hipsblack_850_175_p` — HIPS Black
- `fiberlogy_hips_hipsgraphite_850_175_p` — HIPS Graphite
- `fiberlogy_hips_hipsnatural_850_175_p` — HIPS Natural
- `fiberlogy_hips_hipswhite_850_175_p` — HIPS White
- `fiberlogy_hips_mattehipsblack_1000_175_p` — Matte HIPS Black
- `fiberlogy_hips_mattehipsgraphite_1000_175_p` — Matte HIPS Graphite
- `fiberlogy_hips_mattehipsnatural_1000_175_p` — Matte HIPS Natural
- `fiberlogy_hips_mattehipswhite_1000_175_p` — Matte HIPS White
- `fiberlogy_pa12_pa12cfnylon+cf15black_1000_175_p` — PA12 CF Nylon + CF15 black
- `fiberlogy_pa12_nylongf15gfpa12black_1000_175_p` — Nylon Gf15 GF PA12 Black
- `fiberlogy_pa12_nylongf15gfpa12lightgreen_1000_175_p` — Nylon Gf15 GF PA12 Light Green
- `fiberlogy_pa12_nylongf15gfpa12natural_1000_175_p` — Nylon Gf15 GF PA12 Natural
- `fiberlogy_pa12_nylongf15gfpa12red_1000_175_p` — Nylon Gf15 GF PA12 Red
- `fiberlogy_pa12_nylonpa12black_750_175_p` — Nylon PA12 Black
- `fiberlogy_pa12_nylonpa12blue_750_175_p` — Nylon PA12 Blue
- `fiberlogy_pa12_nylonpa12inox_750_175_p` — Nylon PA12 Inox
- `fiberlogy_pa12_nylonpa12lightgreen_750_175_p` — Nylon PA12 Light Green
- `fiberlogy_pa12_nylonpa12natural_750_175_p` — Nylon PA12 Natural
- `fiberlogy_pa12_nylonpa12orange_750_175_p` — Nylon PA12 Orange
- `fiberlogy_pa12_nylonpa12red_750_175_p` — Nylon PA12 Red
- `fiberlogy_pa12_nylonpa12white_750_175_p` — Nylon PA12 White
- `fiberlogy_pa12_nylonpa12yellow_750_175_p` — Nylon PA12 Yellow
- `fiberlogy_pa12_nylonpa12+cf15black_500_175_p` — Nylon PA12+CF15 Black
- `fiberlogy_pa12_nylonpa12+cf5black_500_175_p` — Nylon PA12+CF5 Black
- `fiberlogy_pa12_nylonpa12+gf15black_500_175_p` — Nylon PA12+GF15 Black
- `fiberlogy_pa12_nylonpa12+gf15natural_500_175_p` — Nylon PA12+GF15 Natural
- `fiberlogy_pa12_pa12nylonblack_1000_175_p` — PA12 Nylon Black
- `fiberlogy_pa12_pa12nylonblue_1000_175_p` — PA12 Nylon blue
- `fiberlogy_pa12_pa12nyloninox_1000_175_p` — PA12 Nylon Inox
- `fiberlogy_pa12_pa12nylonlightgreen_1000_175_p` — PA12 Nylon Light Green
- `fiberlogy_pa12_pa12nylonnatural_1000_175_p` — PA12 Nylon Natural
- `fiberlogy_pa12_pa12nylonorange_1000_175_p` — PA12 Nylon Orange
- `fiberlogy_pa12_pa12nylonred_1000_175_p` — PA12 Nylon Red
- `fiberlogy_pa12_pa12nylonwhite_1000_175_p` — PA12 Nylon White
- `fiberlogy_pa12_pa12nylonyellow_1000_175_p` — PA12 Nylon Yellow
- `fiberlogy_pa12_pa12ranthracite_1000_175_p` — PA12 R Anthracite
- `fiberlogy_pa6_pa6rnylonanthracite_750_175_p` — PA6 R NYLON Anthracite
- `fiberlogy_pc_pcblack_1000_175_p` — PC Black
- `fiberlogy_pc_pcnatural_1000_175_p` — PC Natural
- `fiberlogy_pctg_gf10gfpctgblack_1000_175_p` — Gf10 GF PCTG Black
- `fiberlogy_pctg_gf10gfpctgnatural_1000_175_p` — Gf10 GF PCTG Natural
- `fiberlogy_pctg_pctgblack_750_175_p` — PCTG Black
- `fiberlogy_pctg_pctgblue_750_175_p` — PCTG Blue
- `fiberlogy_pctg_pctgburgundytransparent_750_175_p` — PCTG Burgundy Transparent
- `fiberlogy_pctg_pctggraphite_750_175_p` — PCTG Graphite
- `fiberlogy_pctg_pctginox_750_175_p` — PCTG Inox
- `fiberlogy_pctg_pctglightgreentransparent_750_175_p` — PCTG Light Green Transparent
- `fiberlogy_pctg_pctgnavybluetransparent_750_175_p` — PCTG Navy Blue Transparent
- `fiberlogy_pctg_pctgonyx_750_175_p` — PCTG Onyx
- `fiberlogy_pctg_pctgorange_750_175_p` — PCTG Orange
- `fiberlogy_pctg_pctgorangetransparent_750_175_p` — PCTG Orange Transparent
- `fiberlogy_pctg_pctgpuretransparent_750_175_p` — PCTG Pure Transparent
- `fiberlogy_pctg_pctgred_750_175_p` — PCTG Red
- `fiberlogy_pctg_pctgvertigo_750_175_p` — PCTG Vertigo
- `fiberlogy_pctg_pctgwhite_750_175_p` — PCTG White
- `fiberlogy_pctg_pctgblack_1000_175_p` — PCTG Black
- `fiberlogy_pctg_pctgblue_1000_175_p` — PCTG Blue
- `fiberlogy_pctg_pctgburgundytransparent_1000_175_p` — PCTG Burgundy Transparent
- `fiberlogy_pctg_pctggraphite_1000_175_p` — PCTG Graphite
- `fiberlogy_pctg_pctginox_1000_175_p` — PCTG Inox
- `fiberlogy_pctg_pctglightgreentransparent_1000_175_p` — PCTG Light Green Transparent
- `fiberlogy_pctg_pctgnavybluetransparent_1000_175_p` — PCTG Navy Blue Transparent
- `fiberlogy_pctg_pctgonyx_1000_175_p` — PCTG Onyx
- `fiberlogy_pctg_pctgorange_1000_175_p` — PCTG Orange
- `fiberlogy_pctg_pctgorangetransparent_1000_175_p` — PCTG Orange Transparent
- `fiberlogy_pctg_pctgpuretransparent_1000_175_p` — PCTG Pure Transparent
- `fiberlogy_pctg_pctgred_1000_175_p` — PCTG Red
- `fiberlogy_pctg_pctgvertigo_1000_175_p` — PCTG Vertigo
- `fiberlogy_pctg_pctgwhite_1000_175_p` — PCTG White
- `fiberlogy_pctg_pctgcfblack_1000_175_p` — PCTG CF Black
- `fiberlogy_pctg_refillpctgblack_750_175_p` — Refill PCTG Black
- `fiberlogy_pctg_refillpctggraphite_750_175_p` — Refill PCTG Graphite
- `fiberlogy_pctg_refillpctgpuretransparent_750_175_p` — Refill PCTG Pure Transparent
- `fiberlogy_pctg_refillpctgwhite_750_175_p` — Refill PCTG White
- `fiberlogy_pei_9085peiblack_1000_175_p` — 9085 PEI Black
- `fiberlogy_pei_9085peinatural_1000_175_p` — 9085 PEI Natural
- `fiberlogy_petg_petgcfpet-g+cfblack_1000_175_p` — PETG CF PET-G+CF Black
- `fiberlogy_petg_easypet-gblack_850_175_p` — Easy PET-G Black
- `fiberlogy_petg_easypet-gblue_850_175_p` — Easy PET-G Blue
- `fiberlogy_petg_easypet-gburgundytransparent_850_175_p` — Easy PET-G Burgundy Transparent
- `fiberlogy_petg_easypet-ggraphite_850_175_p` — Easy PET-G Graphite
- `fiberlogy_petg_easypet-ggray_850_175_p` — Easy PET-G Gray
- `fiberlogy_petg_easypet-glightgreentransparent_850_175_p` — Easy PET-G Light Green Transparent
- `fiberlogy_petg_easypet-gnavybluetransparent_850_175_p` — Easy PET-G Navy Blue Transparent
- `fiberlogy_petg_easypet-gonyx_850_175_p` — Easy PET-G Onyx
- `fiberlogy_petg_easypet-gorange_850_175_p` — Easy PET-G Orange
- `fiberlogy_petg_easypet-gorangetransparent_850_175_p` — Easy PET-G Orange Transparent
- `fiberlogy_petg_easypet-gpuretransparent_850_175_p` — Easy PET-G Pure Transparent
- `fiberlogy_petg_easypet-gred_850_175_p` — Easy PET-G Red
- `fiberlogy_petg_easypet-gsilver_850_175_p` — Easy PET-G Silver
- `fiberlogy_petg_easypet-gvertigo_850_175_p` — Easy PET-G Vertigo
- `fiberlogy_petg_easypet-gwhite_850_175_p` — Easy PET-G White
- `fiberlogy_petg_easypet-gyellow_850_175_p` — Easy PET-G Yellow
- `fiberlogy_petg_easypetgblack_1000_175_p` — Easy PETG Black
- `fiberlogy_petg_easypetgblue_1000_175_p` — Easy PETG Blue
- `fiberlogy_petg_easypetgbottlegreentransparent_1000_175_p` — Easy PETG Bottle Green Transparent
- `fiberlogy_petg_easypetggraphite_1000_175_p` — Easy PETG Graphite
- `fiberlogy_petg_easypetggrey_1000_175_p` — Easy PETG Grey
- `fiberlogy_petg_easypetgonyx_1000_175_p` — Easy PETG Onyx
- `fiberlogy_petg_easypetgorange_1000_175_p` — Easy PETG Orange
- `fiberlogy_petg_easypetgpastelblue_1000_175_p` — Easy PETG Pastel Blue
- `fiberlogy_petg_easypetgpastellilac_1000_175_p` — Easy PETG Pastel Lilac
- `fiberlogy_petg_easypetgpastelmint_1000_175_p` — Easy PETG Pastel Mint
- `fiberlogy_petg_easypetgpastelpink_1000_175_p` — Easy PETG Pastel Pink
- `fiberlogy_petg_easypetgpastelyellow_1000_175_p` — Easy PETG Pastel Yellow
- `fiberlogy_petg_easypetgpuretransparent_1000_175_p` — Easy PETG Pure Transparent
- `fiberlogy_petg_easypetgred_1000_175_p` — Easy PETG Red
- `fiberlogy_petg_easypetgscarlet_1000_175_p` — Easy PETG Scarlet
- `fiberlogy_petg_easypetgsilver_1000_175_p` — Easy PETG Silver
- `fiberlogy_petg_easypetgtransparentburgundy_1000_175_p` — Easy PETG Transparent Burgundy
- `fiberlogy_petg_easypetgtransparentlightgreen_1000_175_p` — Easy PETG Transparent Light Green
- `fiberlogy_petg_easypetgtransparentnavyblue_1000_175_p` — Easy PETG Transparent Navy Blue
- `fiberlogy_petg_easypetgtransparentorange_1000_175_p` — Easy PETG Transparent Orange
- `fiberlogy_petg_easypetgvertigo_1000_175_p` — Easy PETG Vertigo
- `fiberlogy_petg_easypetgwhite_1000_175_p` — Easy PETG White
- `fiberlogy_petg_easypetgyellow_1000_175_p` — Easy PETG Yellow
- `fiberlogy_petg_mattpetgmattepetgblack_1000_175_p` — Matt PET G Matte PETG Black
- `fiberlogy_petg_mattpetgmattepetgblue_1000_175_p` — Matt PET G Matte PETG Blue
- `fiberlogy_petg_mattpetgmattepetggraphite_1000_175_p` — Matt PET G Matte PETG Graphite
- `fiberlogy_petg_mattpetgmattepetggrey_1000_175_p` — Matt PET G Matte PETG Grey
- `fiberlogy_petg_mattpetgmattepetgred_1000_175_p` — Matt PET G Matte PETG Red
- `fiberlogy_petg_mattpetgmattepetgwhite_1000_175_p` — Matt PET G Matte PETG White
- `fiberlogy_petg_pet-gblack_850_175_p` — PET-G Black
- `fiberlogy_petg_pet-gblue_850_175_p` — PET-G Blue
- `fiberlogy_petg_pet-gburgundytransparent_850_175_p` — PET-G Burgundy Transparent
- `fiberlogy_petg_pet-ggraphite_850_175_p` — PET-G Graphite
- `fiberlogy_petg_pet-ggray_850_175_p` — PET-G Gray
- `fiberlogy_petg_pet-glightgreentransparent_850_175_p` — PET-G Light Green Transparent
- `fiberlogy_petg_pet-gnavybluetransparent_850_175_p` — PET-G Navy Blue Transparent
- `fiberlogy_petg_pet-gonyx_850_175_p` — PET-G Onyx
- `fiberlogy_petg_pet-gorange_850_175_p` — PET-G Orange
- `fiberlogy_petg_pet-gorangetransparent_850_175_p` — PET-G Orange Transparent
- `fiberlogy_petg_pet-gpuretransparent_850_175_p` — PET-G Pure Transparent
- `fiberlogy_petg_pet-gred_850_175_p` — PET-G Red
- `fiberlogy_petg_pet-gsilver_850_175_p` — PET-G Silver
- `fiberlogy_petg_pet-gvertigo_850_175_p` — PET-G Vertigo
- `fiberlogy_petg_pet-gwhite_850_175_p` — PET-G White
- `fiberlogy_petg_pet-gesdblack_500_175_p` — PET-G ESD Black
- `fiberlogy_petg_pet-gv0petgblack_1000_175_p` — PET-G V0 PETG Black
- `fiberlogy_petg_pet-gv0petggrey_1000_175_p` — PET-G V0 PETG Grey
- `fiberlogy_petg_pet-gv0petgnatural_1000_175_p` — PET-G V0 PETG Natural
- `fiberlogy_petg_petgpet-gesdblack_1000_175_p` — PETG PET-G ESD Black
- `fiberlogy_petg_petgptfenatural_1000_175_p` — PETG PTFE Natural
- `fiberlogy_petg_petgrpet-ganthracite_1000_175_p` — PETG R PET-G Anthracite
- `fiberlogy_petg_refilleasypet-gblack_850_175_p` — Refill Easy PET-G Black
- `fiberlogy_petg_refilleasypet-gburgundytransparent_850_175_p` — Refill Easy PET-G Burgundy Transparent
- `fiberlogy_petg_refilleasypet-ggraphite_850_175_p` — Refill Easy PET-G Graphite
- `fiberlogy_petg_refilleasypet-ggray_850_175_p` — Refill Easy PET-G Gray
- `fiberlogy_petg_refilleasypet-glightgreentransparent_850_175_p` — Refill Easy PET-G Light Green Transparent
- `fiberlogy_petg_refilleasypet-gorangetransparent_850_175_p` — Refill Easy PET-G Orange Transparent
- `fiberlogy_petg_refilleasypet-gpuretransparent_850_175_p` — Refill Easy PET-G Pure Transparent
- `fiberlogy_petg_refilleasypet-gsilver_850_175_p` — Refill Easy PET-G Silver
- `fiberlogy_petg_refilleasypet-gvertigo_850_175_p` — Refill Easy PET-G Vertigo
- `fiberlogy_petg_refilleasypet-gwhite_850_175_p` — Refill Easy PET-G White
- `fiberlogy_pla_easyplaaliengreen_850_175_p` — Easy PLA Alien Green
- `fiberlogy_pla_easyplaaurora_850_175_p` — Easy PLA Aurora
- `fiberlogy_pla_easyplabeige_850_175_p` — Easy PLA Beige
- `fiberlogy_pla_easyplablack_850_175_p` — Easy PLA Black
- `fiberlogy_pla_easyplablue_850_175_p` — Easy PLA Blue
- `fiberlogy_pla_easyplabrick_850_175_p` — Easy PLA Brick
- `fiberlogy_pla_easyplabrown_850_175_p` — Easy PLA Brown
- `fiberlogy_pla_easyplaburgundy_850_175_p` — Easy PLA Burgundy
- `fiberlogy_pla_easyplacandy_850_175_p` — Easy PLA Candy
- `fiberlogy_pla_easyplagraphite_850_175_p` — Easy PLA Graphite
- `fiberlogy_pla_easyplagreen_850_175_p` — Easy PLA Green
- `fiberlogy_pla_easyplainox_850_175_p` — Easy PLA Inox
- `fiberlogy_pla_easyplainoxsteel_850_175_p` — Easy PLA Inox Steel
- `fiberlogy_pla_easyplairishgreen_850_175_p` — Easy PLA Irish Green
- `fiberlogy_pla_easyplalightgreen_850_175_p` — Easy PLA Light Green
- `fiberlogy_pla_easyplamidnightsky_850_175_p` — Easy PLA Midnight Sky
- `fiberlogy_pla_easyplanavyblue_850_175_p` — Easy PLA Navy Blue
- `fiberlogy_pla_easyplaneongreen_850_175_p` — Easy PLA Neon Green
- `fiberlogy_pla_easyplaneonorange_850_175_p` — Easy PLA Neon Orange
- `fiberlogy_pla_easyplaneonyellow_850_175_p` — Easy PLA Neon Yellow
- `fiberlogy_pla_easyplaoldgold_850_175_p` — Easy PLA Old Gold
- `fiberlogy_pla_easyplaonyx_850_175_p` — Easy PLA Onyx
- `fiberlogy_pla_easyplaonyxgold_850_175_p` — Easy PLA Onyx Gold
- `fiberlogy_pla_easyplaorange_850_175_p` — Easy PLA Orange
- `fiberlogy_pla_easyplapastelblue_850_175_p` — Easy PLA Pastel Blue
- `fiberlogy_pla_easyplapastellilac_850_175_p` — Easy PLA Pastel Lilac
- `fiberlogy_pla_easyplapastelmint_850_175_p` — Easy PLA Pastel Mint
- `fiberlogy_pla_easyplapastelpink_850_175_p` — Easy PLA Pastel Pink
- `fiberlogy_pla_easyplapastelyellow_850_175_p` — Easy PLA Pastel Yellow
- `fiberlogy_pla_easyplapink_850_175_p` — Easy PLA Pink
- `fiberlogy_pla_easyplapurple_850_175_p` — Easy PLA Purple
- `fiberlogy_pla_easyplared_850_175_p` — Easy PLA Red
- `fiberlogy_pla_easyplaredorange_850_175_p` — Easy PLA Red Orange
- `fiberlogy_pla_easyplarubyred_850_175_p` — Easy PLA Ruby Red
- `fiberlogy_pla_easyplasandstone_850_175_p` — Easy PLA Sandstone
- `fiberlogy_pla_easyplaskin_850_175_p` — Easy PLA Skin
- `fiberlogy_pla_easyplaskin2_850_175_p` — Easy PLA Skin 2
- `fiberlogy_pla_easyplaskin3_850_175_p` — Easy PLA Skin 3
- `fiberlogy_pla_easyplaspectrablue_850_175_p` — Easy PLA Spectra Blue
- `fiberlogy_pla_easyplatrueblue_850_175_p` — Easy PLA True Blue
- `fiberlogy_pla_easyplatruegold_850_175_p` — Easy PLA True Gold
- `fiberlogy_pla_easyplavertigo_850_175_p` — Easy PLA Vertigo
- `fiberlogy_pla_easyplawhite_850_175_p` — Easy PLA White
- `fiberlogy_pla_easyplayellow_850_175_p` — Easy PLA Yellow
- `fiberlogy_pla_easyplaaliengreen_1000_175_p` — Easy PLA Alien Green
- `fiberlogy_pla_easyplaaurora_1000_175_p` — Easy PLA Aurora
- `fiberlogy_pla_easyplabeige_1000_175_p` — Easy PLA Beige
- `fiberlogy_pla_easyplablack_1000_175_p` — Easy PLA Black
- `fiberlogy_pla_easyplablue_1000_175_p` — Easy PLA Blue
- `fiberlogy_pla_easyplabrick_1000_175_p` — Easy PLA Brick
- `fiberlogy_pla_easyplabrown_1000_175_p` — Easy PLA Brown
- `fiberlogy_pla_easyplaburgundy_1000_175_p` — Easy PLA Burgundy
- `fiberlogy_pla_easyplacandy_1000_175_p` — Easy PLA Candy
- `fiberlogy_pla_easyplagraphite_1000_175_p` — Easy PLA Graphite
- `fiberlogy_pla_easyplagreen_1000_175_p` — Easy PLA Green
- `fiberlogy_pla_easyplainox_1000_175_p` — Easy PLA Inox
- `fiberlogy_pla_easyplainoxsteel_1000_175_p` — Easy PLA Inox Steel
- `fiberlogy_pla_easyplairishgreen_1000_175_p` — Easy PLA Irish Green
- `fiberlogy_pla_easyplalightgreen_1000_175_p` — Easy PLA Light Green
- `fiberlogy_pla_easyplamidnightsky_1000_175_p` — Easy PLA Midnight Sky
- `fiberlogy_pla_easyplanavyblue_1000_175_p` — Easy PLA Navy Blue
- `fiberlogy_pla_easyplaneongreen_1000_175_p` — Easy PLA Neon Green
- `fiberlogy_pla_easyplaneonorange_1000_175_p` — Easy PLA Neon Orange
- `fiberlogy_pla_easyplaneonyellow_1000_175_p` — Easy PLA Neon Yellow
- `fiberlogy_pla_easyplaoldgold_1000_175_p` — Easy PLA Old Gold
- `fiberlogy_pla_easyplaonyx_1000_175_p` — Easy PLA Onyx
- `fiberlogy_pla_easyplaonyxgold_1000_175_p` — Easy PLA Onyx Gold
- `fiberlogy_pla_easyplaorange_1000_175_p` — Easy PLA Orange
- `fiberlogy_pla_easyplapastelblue_1000_175_p` — Easy PLA Pastel Blue
- `fiberlogy_pla_easyplapastellilac_1000_175_p` — Easy PLA Pastel Lilac
- `fiberlogy_pla_easyplapastelmint_1000_175_p` — Easy PLA Pastel Mint
- `fiberlogy_pla_easyplapastelpink_1000_175_p` — Easy PLA Pastel Pink
- `fiberlogy_pla_easyplapastelyellow_1000_175_p` — Easy PLA Pastel Yellow
- `fiberlogy_pla_easyplapink_1000_175_p` — Easy PLA Pink
- `fiberlogy_pla_easyplapurple_1000_175_p` — Easy PLA Purple
- `fiberlogy_pla_easyplared_1000_175_p` — Easy PLA Red
- `fiberlogy_pla_easyplaredorange_1000_175_p` — Easy PLA Red Orange
- `fiberlogy_pla_easyplarubyred_1000_175_p` — Easy PLA Ruby Red
- `fiberlogy_pla_easyplasandstone_1000_175_p` — Easy PLA Sandstone
- `fiberlogy_pla_easyplaskin_1000_175_p` — Easy PLA Skin
- `fiberlogy_pla_easyplaskin2_1000_175_p` — Easy PLA Skin 2
- `fiberlogy_pla_easyplaskin3_1000_175_p` — Easy PLA Skin 3
- `fiberlogy_pla_easyplaspectrablue_1000_175_p` — Easy PLA Spectra Blue
- `fiberlogy_pla_easyplatrueblue_1000_175_p` — Easy PLA True Blue
- `fiberlogy_pla_easyplatruegold_1000_175_p` — Easy PLA True Gold
- `fiberlogy_pla_easyplavertigo_1000_175_p` — Easy PLA Vertigo
- `fiberlogy_pla_easyplawhite_1000_175_p` — Easy PLA White
- `fiberlogy_pla_easyplayellow_1000_175_p` — Easy PLA Yellow
- `fiberlogy_pla_plafibersatinblack_850_175_p` — PLA FiberSatin Black
- `fiberlogy_pla_plafibersatinblue_850_175_p` — PLA FiberSatin Blue
- `fiberlogy_pla_plafibersatingreen_850_175_p` — PLA FiberSatin Green
- `fiberlogy_pla_plafibersatinpearl_850_175_p` — PLA FiberSatin Pearl
- `fiberlogy_pla_plafibersatinpink_850_175_p` — PLA FiberSatin Pink
- `fiberlogy_pla_plafibersatinred_850_175_p` — PLA FiberSatin Red
- `fiberlogy_pla_plafibersatinblack_1000_175_p` — PLA FiberSatin Black
- `fiberlogy_pla_plafibersatinblue_1000_175_p` — PLA FiberSatin Blue
- `fiberlogy_pla_plafibersatingreen_1000_175_p` — PLA FiberSatin Green
- `fiberlogy_pla_plafibersatinpearl_1000_175_p` — PLA FiberSatin Pearl
- `fiberlogy_pla_plafibersatinpink_1000_175_p` — PLA FiberSatin Pink
- `fiberlogy_pla_plafibersatinred_1000_175_p` — PLA FiberSatin Red
- `fiberlogy_pla_plafibersilkanthracite_850_175_p` — PLA FiberSilk Anthracite
- `fiberlogy_pla_plafibersilkblue_850_175_p` — PLA FiberSilk Blue
- `fiberlogy_pla_plafibersilkbrass_850_175_p` — PLA FiberSilk Brass
- `fiberlogy_pla_plafibersilkbronze_850_175_p` — PLA FiberSilk Bronze
- `fiberlogy_pla_plafibersilkburgundy_850_175_p` — PLA FiberSilk Burgundy
- `fiberlogy_pla_plafibersilkcopper_850_175_p` — PLA FiberSilk Copper
- `fiberlogy_pla_plafibersilkgold_850_175_p` — PLA FiberSilk Gold
- `fiberlogy_pla_plafibersilkgreen_850_175_p` — PLA FiberSilk Green
- `fiberlogy_pla_plafibersilkinox_850_175_p` — PLA FiberSilk Inox
- `fiberlogy_pla_plafibersilklightgreen_850_175_p` — PLA FiberSilk Light Green
- `fiberlogy_pla_plafibersilknavyblue_850_175_p` — PLA FiberSilk Navy Blue
- `fiberlogy_pla_plafibersilkorange_850_175_p` — PLA FiberSilk Orange
- `fiberlogy_pla_plafibersilkpearl_850_175_p` — PLA FiberSilk Pearl
- `fiberlogy_pla_plafibersilkpink_850_175_p` — PLA FiberSilk Pink
- `fiberlogy_pla_plafibersilkred_850_175_p` — PLA FiberSilk Red
- `fiberlogy_pla_plafibersilksilver_850_175_p` — PLA FiberSilk Silver
- `fiberlogy_pla_plafibersilkturquoise_850_175_p` — PLA FiberSilk Turquoise
- `fiberlogy_pla_plafibersilkyellow_850_175_p` — PLA FiberSilk Yellow
- `fiberlogy_pla_fibersilkmetallicsilkplabronze_1000_175_p` — Fibersilk Metallic Silk PLA Bronze
- `fiberlogy_pla_fibersilkmetallicsilkplacopper_1000_175_p` — Fibersilk Metallic Silk PLA Copper
- `fiberlogy_pla_fibersilkmetallicsilkplagold_1000_175_p` — Fibersilk Metallic Silk PLA Gold
- `fiberlogy_pla_fibersilkmetallicsilkplainox_1000_175_p` — Fibersilk Metallic Silk PLA Inox
- `fiberlogy_pla_fibersilkmetallicsilkplanavyblue_1000_175_p` — Fibersilk Metallic Silk PLA Navy Blue
- `fiberlogy_pla_fibersilkmetallicsilkplaorange_1000_175_p` — Fibersilk Metallic Silk PLA Orange
- `fiberlogy_pla_fibersilkmetallicsilkplapearl_1000_175_p` — Fibersilk Metallic Silk PLA Pearl
- `fiberlogy_pla_fibersilkmetallicsilkplared_1000_175_p` — Fibersilk Metallic Silk PLA Red
- `fiberlogy_pla_fibersilkmetallicsilkplasilver_1000_175_p` — Fibersilk Metallic Silk PLA Silver
- `fiberlogy_pla_plafiberwoodblack_750_175_p` — PLA FiberWood Black
- `fiberlogy_pla_plafiberwoodbrown_750_175_p` — PLA FiberWood Brown
- `fiberlogy_pla_plafiberwoodcarmine_750_175_p` — PLA FiberWood Carmine
- `fiberlogy_pla_plafiberwoodnatur_750_175_p` — PLA FiberWood Natur
- `fiberlogy_pla_plafiberwoodwhite_750_175_p` — PLA FiberWood White
- `fiberlogy_pla_plafiberwoodblack_1000_175_p` — PLA FiberWood Black
- `fiberlogy_pla_plafiberwoodbrown_1000_175_p` — PLA FiberWood Brown
- `fiberlogy_pla_plafiberwoodcarmine_1000_175_p` — PLA FiberWood Carmine
- `fiberlogy_pla_plafiberwoodnatur_1000_175_p` — PLA FiberWood Natur
- `fiberlogy_pla_plafiberwoodwhite_1000_175_p` — PLA FiberWood White
- `fiberlogy_pla_hdplabeige_850_175_p` — HD PLA Beige
- `fiberlogy_pla_hdplablack_850_175_p` — HD PLA Black
- `fiberlogy_pla_hdplablue_850_175_p` — HD PLA Blue
- `fiberlogy_pla_hdplabrown_850_175_p` — HD PLA Brown
- `fiberlogy_pla_hdplaburgundy_850_175_p` — HD PLA Burgundy
- `fiberlogy_pla_hdplagraphite_850_175_p` — HD PLA Graphite
- `fiberlogy_pla_hdplagray_850_175_p` — HD PLA Gray
- `fiberlogy_pla_hdplagreen_850_175_p` — HD PLA Green
- `fiberlogy_pla_hdplainox_850_175_p` — HD PLA Inox
- `fiberlogy_pla_hdplalightgreen_850_175_p` — HD PLA Light Green
- `fiberlogy_pla_hdplanavyblue_850_175_p` — HD PLA Navy Blue
- `fiberlogy_pla_hdplaorange_850_175_p` — HD PLA Orange
- `fiberlogy_pla_hdplapink_850_175_p` — HD PLA Pink
- `fiberlogy_pla_hdplapurple_850_175_p` — HD PLA Purple
- `fiberlogy_pla_hdplared_850_175_p` — HD PLA Red
- `fiberlogy_pla_hdplavertigo_850_175_p` — HD PLA Vertigo
- `fiberlogy_pla_hdplawhite_850_175_p` — HD PLA White
- `fiberlogy_pla_hdplayellow_850_175_p` — HD PLA Yellow
- `fiberlogy_pla_hsclearhighspeedplablue_1000_175_p` — HS Clear High Speed PLA Blue
- `fiberlogy_pla_hsclearhighspeedplaburgundy_1000_175_p` — HS Clear High Speed PLA Burgundy
- `fiberlogy_pla_hsclearhighspeedplagreen_1000_175_p` — HS Clear High Speed PLA Green
- `fiberlogy_pla_hsclearhighspeedplalightgreen_1000_175_p` — HS Clear High Speed PLA Light Green
- `fiberlogy_pla_hsclearhighspeedplanavyblue_1000_175_p` — HS Clear High Speed PLA Navy Blue
- `fiberlogy_pla_hsclearhighspeedplaorange_1000_175_p` — HS Clear High Speed PLA Orange
- `fiberlogy_pla_hsclearhighspeedplapink_1000_175_p` — HS Clear High Speed PLA Pink
- `fiberlogy_pla_hsclearhighspeedplapuretransparent_1000_175_p` — HS Clear High Speed PLA Pure Transparent
- `fiberlogy_pla_hsclearhighspeedplaturquoise_1000_175_p` — HS Clear High Speed PLA Turquoise
- `fiberlogy_pla_impactplaarmygreen_850_175_p` — Impact PLA Army Green
- `fiberlogy_pla_impactplablack_850_175_p` — Impact PLA Black
- `fiberlogy_pla_impactplablue_850_175_p` — Impact PLA Blue
- `fiberlogy_pla_impactplagraphite_850_175_p` — Impact PLA Graphite
- `fiberlogy_pla_impactplakhaki_850_175_p` — Impact PLA Khaki
- `fiberlogy_pla_impactplalightgreen_850_175_p` — Impact PLA Light Green
- `fiberlogy_pla_impactplaolivegreen_850_175_p` — Impact PLA Olive Green
- `fiberlogy_pla_impactplaonyx_850_175_p` — Impact PLA Onyx
- `fiberlogy_pla_impactplaorange_850_175_p` — Impact PLA Orange
- `fiberlogy_pla_impactplared_850_175_p` — Impact PLA Red
- `fiberlogy_pla_impactplavertigo_850_175_p` — Impact PLA Vertigo
- `fiberlogy_pla_impactplawhite_850_175_p` — Impact PLA White
- `fiberlogy_pla_impactplayellow_850_175_p` — Impact PLA Yellow
- `fiberlogy_pla_impactplaarmygreen_1000_175_p` — Impact PLA Army Green
- `fiberlogy_pla_impactplablack_1000_175_p` — Impact PLA Black
- `fiberlogy_pla_impactplablue_1000_175_p` — Impact PLA Blue
- `fiberlogy_pla_impactplagraphite_1000_175_p` — Impact PLA Graphite
- `fiberlogy_pla_impactplakhaki_1000_175_p` — Impact PLA Khaki
- `fiberlogy_pla_impactplalightgreen_1000_175_p` — Impact PLA Light Green
- `fiberlogy_pla_impactplaolivegreen_1000_175_p` — Impact PLA Olive Green
- `fiberlogy_pla_impactplaonyx_1000_175_p` — Impact PLA Onyx
- `fiberlogy_pla_impactplaorange_1000_175_p` — Impact PLA Orange
- `fiberlogy_pla_impactplared_1000_175_p` — Impact PLA Red
- `fiberlogy_pla_impactplavertigo_1000_175_p` — Impact PLA Vertigo
- `fiberlogy_pla_impactplawhite_1000_175_p` — Impact PLA White
- `fiberlogy_pla_impactplayellow_1000_175_p` — Impact PLA Yellow
- `fiberlogy_pla_plafibersilkmetallicblue_1000_175_p` — PLA FiberSilk Metallic Blue
- `fiberlogy_pla_plaranthracite_1000_175_p` — PLA R Anthracite
- `fiberlogy_pla_plamineralmarble_850_175_p` — PLA Mineral Marble
- `fiberlogy_pla_plamineralnatur_850_175_p` — PLA Mineral Natur
- `fiberlogy_pla_plamineralwhite_850_175_p` — PLA Mineral White
- `fiberlogy_pla_plamineralmarble_1000_175_p` — PLA Mineral Marble
- `fiberlogy_pla_plamineralnatur_1000_175_p` — PLA Mineral Natur
- `fiberlogy_pla_plamineralwhite_1000_175_p` — PLA Mineral White
- `fiberlogy_pla_rplaanthracite_850_175_p` — R PLA Anthracite
- `fiberlogy_pla_refilleasyplablack_850_175_p` — Refill Easy PLA Black
- `fiberlogy_pla_refilleasyplablue_850_175_p` — Refill Easy PLA Blue
- `fiberlogy_pla_refilleasyplagraphite_850_175_p` — Refill Easy PLA Graphite
- `fiberlogy_pla_refilleasyplagray_850_175_p` — Refill Easy PLA Gray
- `fiberlogy_pla_refilleasyplainox_850_175_p` — Refill Easy PLA Inox
- `fiberlogy_pla_refilleasyplalightgreen_850_175_p` — Refill Easy PLA Light Green
- `fiberlogy_pla_refilleasyplaorange_850_175_p` — Refill Easy PLA Orange
- `fiberlogy_pla_refilleasyplavertigo_850_175_p` — Refill Easy PLA Vertigo
- `fiberlogy_pla_refilleasyplawhite_850_175_p` — Refill Easy PLA White
- `fiberlogy_pla_refillrplaanthracite_850_175_p` — Refill R PLA Anthracite
- `fiberlogy_pp_ppblack_750_175_p` — PP Black
- `fiberlogy_pp_ppblue_750_175_p` — PP Blue
- `fiberlogy_pp_ppgraphite_750_175_p` — PP Graphite
- `fiberlogy_pp_pplightgreen_750_175_p` — PP Light Green
- `fiberlogy_pp_ppnatural_750_175_p` — PP Natural
- `fiberlogy_pp_pporange_750_175_p` — PP Orange
- `fiberlogy_pp_ppred_750_175_p` — PP Red
- `fiberlogy_pp_ppwhite_750_175_p` — PP White
- `fiberlogy_pp_ppyellow_750_175_p` — PP Yellow
- `fiberlogy_pp_ppblack_1000_175_p` — PP Black
- `fiberlogy_pp_ppblue_1000_175_p` — PP Blue
- `fiberlogy_pp_ppgraphite_1000_175_p` — PP Graphite
- `fiberlogy_pp_pplightgreen_1000_175_p` — PP Light Green
- `fiberlogy_pp_ppnatural_1000_175_p` — PP Natural
- `fiberlogy_pp_pporange_1000_175_p` — PP Orange
- `fiberlogy_pp_ppranthracite_1000_175_p` — PP R Anthracite
- `fiberlogy_pp_ppred_1000_175_p` — PP Red
- `fiberlogy_pp_ppwhite_1000_175_p` — PP White
- `fiberlogy_pp_ppyellow_1000_175_p` — PP Yellow
- `fiberlogy_pvb_fibersmoothpvbblack_1000_175_p` — Fibersmooth PVB Black
- `fiberlogy_pvb_fibersmoothpvbblue_1000_175_p` — Fibersmooth PVB Blue
- `fiberlogy_pvb_fibersmoothpvbgraphite_1000_175_p` — Fibersmooth PVB Graphite
- `fiberlogy_pvb_fibersmoothpvbgrey_1000_175_p` — Fibersmooth PVB Grey
- `fiberlogy_pvb_fibersmoothpvbred_1000_175_p` — Fibersmooth PVB Red
- `fiberlogy_tpu_tpucffiberflexcfblack_1000_175_p` — TPU CF FiberFlex CF Black
- `fiberlogy_tpu_tpufiberflex30dbeige_850_175_p` — TPU FiberFlex 30D Beige
- `fiberlogy_tpu_tpufiberflex30dblack_850_175_p` — TPU FiberFlex 30D Black
- `fiberlogy_tpu_tpufiberflex30dblue_850_175_p` — TPU FiberFlex 30D Blue
- `fiberlogy_tpu_tpufiberflex30dgraphite_850_175_p` — TPU FiberFlex 30D Graphite
- `fiberlogy_tpu_tpufiberflex30dgray_850_175_p` — TPU FiberFlex 30D Gray
- `fiberlogy_tpu_tpufiberflex30dlightgreen_850_175_p` — TPU FiberFlex 30D Light Green
- `fiberlogy_tpu_tpufiberflex30dorange_850_175_p` — TPU FiberFlex 30D Orange
- `fiberlogy_tpu_tpufiberflex30dpink_850_175_p` — TPU FiberFlex 30D Pink
- `fiberlogy_tpu_tpufiberflex30dred_850_175_p` — TPU FiberFlex 30D Red
- `fiberlogy_tpu_tpufiberflex30dwhite_850_175_p` — TPU FiberFlex 30D White
- `fiberlogy_tpu_tpufiberflex30dyellow_850_175_p` — TPU FiberFlex 30D Yellow
- `fiberlogy_tpu_tpufiberflex30dbeige_1000_175_p` — TPU FiberFlex 30D Beige
- `fiberlogy_tpu_tpufiberflex30dblack_1000_175_p` — TPU FiberFlex 30D Black
- `fiberlogy_tpu_tpufiberflex30dblue_1000_175_p` — TPU FiberFlex 30D Blue
- `fiberlogy_tpu_tpufiberflex30dgraphite_1000_175_p` — TPU FiberFlex 30D Graphite
- `fiberlogy_tpu_tpufiberflex30dgray_1000_175_p` — TPU FiberFlex 30D Gray
- `fiberlogy_tpu_tpufiberflex30dlightgreen_1000_175_p` — TPU FiberFlex 30D Light Green
- `fiberlogy_tpu_tpufiberflex30dorange_1000_175_p` — TPU FiberFlex 30D Orange
- `fiberlogy_tpu_tpufiberflex30dpink_1000_175_p` — TPU FiberFlex 30D Pink
- `fiberlogy_tpu_tpufiberflex30dred_1000_175_p` — TPU FiberFlex 30D Red
- `fiberlogy_tpu_tpufiberflex30dwhite_1000_175_p` — TPU FiberFlex 30D White
- `fiberlogy_tpu_tpufiberflex30dyellow_1000_175_p` — TPU FiberFlex 30D Yellow
- `fiberlogy_tpu_tpufiberflex40dbeige_850_175_p` — TPU FiberFlex 40D Beige
- `fiberlogy_tpu_tpufiberflex40dblack_850_175_p` — TPU FiberFlex 40D Black
- `fiberlogy_tpu_tpufiberflex40dblue_850_175_p` — TPU FiberFlex 40D Blue
- `fiberlogy_tpu_tpufiberflex40dbrown_850_175_p` — TPU FiberFlex 40D Brown
- `fiberlogy_tpu_tpufiberflex40dburgundy_850_175_p` — TPU FiberFlex 40D Burgundy
- `fiberlogy_tpu_tpufiberflex40dgraphite_850_175_p` — TPU FiberFlex 40D Graphite
- `fiberlogy_tpu_tpufiberflex40dgray_850_175_p` — TPU FiberFlex 40D Gray
- `fiberlogy_tpu_tpufiberflex40dgreen_850_175_p` — TPU FiberFlex 40D Green
- `fiberlogy_tpu_tpufiberflex40dlightgreen_850_175_p` — TPU FiberFlex 40D Light Green
- `fiberlogy_tpu_tpufiberflex40dnavyblue_850_175_p` — TPU FiberFlex 40D Navy Blue
- `fiberlogy_tpu_tpufiberflex40dorange_850_175_p` — TPU FiberFlex 40D Orange
- `fiberlogy_tpu_tpufiberflex40dpink_850_175_p` — TPU FiberFlex 40D Pink
- `fiberlogy_tpu_tpufiberflex40dpurple_850_175_p` — TPU FiberFlex 40D Purple
- `fiberlogy_tpu_tpufiberflex40dred_850_175_p` — TPU FiberFlex 40D Red
- `fiberlogy_tpu_tpufiberflex40dvertigo_850_175_p` — TPU FiberFlex 40D Vertigo
- `fiberlogy_tpu_tpufiberflex40dwhite_850_175_p` — TPU FiberFlex 40D White
- `fiberlogy_tpu_tpufiberflex40dyellow_850_175_p` — TPU FiberFlex 40D Yellow
- `fiberlogy_tpu_tpufiberflex40dbeige_1000_175_p` — TPU FiberFlex 40D Beige
- `fiberlogy_tpu_tpufiberflex40dblack_1000_175_p` — TPU FiberFlex 40D Black
- `fiberlogy_tpu_tpufiberflex40dblue_1000_175_p` — TPU FiberFlex 40D Blue
- `fiberlogy_tpu_tpufiberflex40dbrown_1000_175_p` — TPU FiberFlex 40D Brown
- `fiberlogy_tpu_tpufiberflex40dburgundy_1000_175_p` — TPU FiberFlex 40D Burgundy
- `fiberlogy_tpu_tpufiberflex40dgraphite_1000_175_p` — TPU FiberFlex 40D Graphite
- `fiberlogy_tpu_tpufiberflex40dgray_1000_175_p` — TPU FiberFlex 40D Gray
- `fiberlogy_tpu_tpufiberflex40dgreen_1000_175_p` — TPU FiberFlex 40D Green
- `fiberlogy_tpu_tpufiberflex40dlightgreen_1000_175_p` — TPU FiberFlex 40D Light Green
- `fiberlogy_tpu_tpufiberflex40dnavyblue_1000_175_p` — TPU FiberFlex 40D Navy Blue
- `fiberlogy_tpu_tpufiberflex40dorange_1000_175_p` — TPU FiberFlex 40D Orange
- `fiberlogy_tpu_tpufiberflex40dpink_1000_175_p` — TPU FiberFlex 40D Pink
- `fiberlogy_tpu_tpufiberflex40dpurple_1000_175_p` — TPU FiberFlex 40D Purple
- `fiberlogy_tpu_tpufiberflex40dred_1000_175_p` — TPU FiberFlex 40D Red
- `fiberlogy_tpu_tpufiberflex40dvertigo_1000_175_p` — TPU FiberFlex 40D Vertigo
- `fiberlogy_tpu_tpufiberflex40dwhite_1000_175_p` — TPU FiberFlex 40D White
- `fiberlogy_tpu_tpufiberflex40dyellow_1000_175_p` — TPU FiberFlex 40D Yellow
- `fiberlogy_tpu_tpumattflex40dblack_850_175_p` — TPU MattFlex 40D Black
- `fiberlogy_tpu_mattflex40dmattetpublack_1000_175_p` — Mattflex 40D Matte TPU Black
- `fiberlogy_tpu_mattflex40dmattetpublue_1000_175_p` — Mattflex 40D Matte TPU Blue
- `fiberlogy_tpu_mattflex40dmattetpugraphite_1000_175_p` — Mattflex 40D Matte TPU Graphite
- `fiberlogy_tpu_mattflex40dmattetpured_1000_175_p` — Mattflex 40D Matte TPU Red
- `fiberlogy_tpu_mattflex40dmattetpuwhite_1000_175_p` — Mattflex 40D Matte TPU White
