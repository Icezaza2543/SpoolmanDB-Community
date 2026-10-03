# printwithsmile duplicate migration review

Base `2e3d8e021bce22be73f2f7690a3b97ba9a55c20f`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `3e2acf1ffec0328a130273a7c8557c0693f7a581db31044d1036c54b4b017258`.

## Authorization and result

{"groups": 68, "approved_groups": 0, "retired": 0, "deferred": 68, "hard_stops": 0, "before_count": 52294, "after_count": 52294, "brand_before": 759, "brand_after": 759, "registry_before": 1140, "registry_after": 1140, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

All 68 candidates are retained: source-color material-token duplication/line-color decomposition or unresolved tie. No current same-SKU binding is established for the Cartesian broad variants. The previously cited HIS PLA product URL returns 404 on final review; its technical values and SKU/EAN binding are not treated as current verified evidence. No data edits, identifiers or packaging changes.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. If a later reviewed migration retires records, existing Spoolman spools retain local data, but retired external catalog lookups will not redirect automatically.

## Current first-party evidence

- {"url": "https://printwithsmile.cz/gb/his-pla/188-his-pla-175-mm-natural-500-g-8594196455154.html", "name": "HIS PLA natural", "sku": "515", "ean": "8594196455154", "note": "Historical candidate URL returns 404 on final review; current product, technical values and SKU/EAN binding remain unverified. Source-color decomposition differs from broad OFD PLA/HIS natural; defer without inventing binding."}
- {"url": "https://pws.3dfilaments.cz/gb/", "note": "Manufacturer catalog distinguishes SATIN PLA and HIS PLA product lines. Duplicated material words inside color labels cannot be removed by the immutable-key Rule5 checker; retained for tooling review."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### PWS001: dup-0bb798e93831020ac6acdc40df7935de7e1d3294bfda758d9f68f9614a9494bf

Status: DEFERRED; survivor `printwithsmile_pla_plahisnatural_500_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_hisplanatural_500_175_c`|`HIS PLA {color_name}`|`natural`|{"source_file": "printwithsmile.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 1, "compiled_records": 1} / False|
|`printwithsmile_pla_plahisnatural_500_175_c`|`PLA {color_name}`|`HIS natural`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_hisplanatural_500_175_c": "f5e6c8",
    "printwithsmile_pla_plahisnatural_500_175_c": "DFDFD3"
  },
  "extruder_temp_range": {
    "printwithsmile_pla_hisplanatural_500_175_c": [
      210,
      250
    ],
    "printwithsmile_pla_plahisnatural_500_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "printwithsmile_pla_hisplanatural_500_175_c": [
      40,
      60
    ],
    "printwithsmile_pla_plahisnatural_500_175_c": [
      60,
      65
    ]
  },
  "finish": {
    "printwithsmile_pla_hisplanatural_500_175_c": null,
    "printwithsmile_pla_plahisnatural_500_175_c": "glossy"
  },
  "codes": {
    "printwithsmile_pla_hisplanatural_500_175_c": [
      "515"
    ],
    "printwithsmile_pla_plahisnatural_500_175_c": null
  },
  "eans": {
    "printwithsmile_pla_hisplanatural_500_175_c": [
      "8594196455154"
    ],
    "printwithsmile_pla_plahisnatural_500_175_c": null
  }
}
```

### PWS002: dup-13198a5311933b736ef6580ef9711d25b146b6739d38690ab5c23842a9dd1cdd

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plabicolormetallicgreenbrown_500_175_c`|`PLA {color_name}`|`BICOLOR METALLIC GREEN BROWN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plabicolormetallicplagreenbrown_500_175_c`|`PLA {color_name}`|`BICOLOR METALLIC PLA GREEN BROWN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plabicolormetallicgreenbrown_500_175_c": "BA8960",
    "printwithsmile_pla_plabicolormetallicplagreenbrown_500_175_c": "8b4513"
  },
  "codes": {
    "printwithsmile_pla_plabicolormetallicgreenbrown_500_175_c": null,
    "printwithsmile_pla_plabicolormetallicplagreenbrown_500_175_c": [
      "094"
    ]
  },
  "eans": {
    "printwithsmile_pla_plabicolormetallicgreenbrown_500_175_c": null,
    "printwithsmile_pla_plabicolormetallicplagreenbrown_500_175_c": [
      "8594196450944"
    ]
  }
}
```

### PWS003: dup-521f14897f868689de04c82e6b4a6d5291a493cb4a54e8456ae1a3ee481c18fd

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plabicolormetallicgreenbrown_2500_175_c`|`PLA {color_name}`|`BICOLOR METALLIC GREEN BROWN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plabicolormetallicplagreenbrown_2500_175_c`|`PLA {color_name}`|`BICOLOR METALLIC PLA GREEN BROWN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plabicolormetallicgreenbrown_2500_175_c": "BA8960",
    "printwithsmile_pla_plabicolormetallicplagreenbrown_2500_175_c": "8b4513"
  },
  "codes": {
    "printwithsmile_pla_plabicolormetallicgreenbrown_2500_175_c": null,
    "printwithsmile_pla_plabicolormetallicplagreenbrown_2500_175_c": [
      "094"
    ]
  },
  "eans": {
    "printwithsmile_pla_plabicolormetallicgreenbrown_2500_175_c": null,
    "printwithsmile_pla_plabicolormetallicplagreenbrown_2500_175_c": [
      "8594196450944"
    ]
  }
}
```

### PWS004: dup-5f4c234e91562e65141b5b1ddf845817ce85eba16a52c77cfeb4e159ff0c1178

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plabicolormetallicgreenbrown_750_175_c`|`PLA {color_name}`|`BICOLOR METALLIC GREEN BROWN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plabicolormetallicplagreenbrown_750_175_c`|`PLA {color_name}`|`BICOLOR METALLIC PLA GREEN BROWN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plabicolormetallicgreenbrown_750_175_c": "BA8960",
    "printwithsmile_pla_plabicolormetallicplagreenbrown_750_175_c": "8b4513"
  },
  "codes": {
    "printwithsmile_pla_plabicolormetallicgreenbrown_750_175_c": null,
    "printwithsmile_pla_plabicolormetallicplagreenbrown_750_175_c": [
      "094"
    ]
  },
  "eans": {
    "printwithsmile_pla_plabicolormetallicgreenbrown_750_175_c": null,
    "printwithsmile_pla_plabicolormetallicplagreenbrown_750_175_c": [
      "8594196450944"
    ]
  }
}
```

### PWS005: dup-bb5e5e64ce1084109d6722997c6dc24c4976276b4bbd59a63cee4064431326c6

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plabicolormetallicgreenbrown_1000_175_c`|`PLA {color_name}`|`BICOLOR METALLIC GREEN BROWN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plabicolormetallicplagreenbrown_1000_175_c`|`PLA {color_name}`|`BICOLOR METALLIC PLA GREEN BROWN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plabicolormetallicgreenbrown_1000_175_c": "BA8960",
    "printwithsmile_pla_plabicolormetallicplagreenbrown_1000_175_c": "8b4513"
  },
  "codes": {
    "printwithsmile_pla_plabicolormetallicgreenbrown_1000_175_c": null,
    "printwithsmile_pla_plabicolormetallicplagreenbrown_1000_175_c": [
      "094"
    ]
  },
  "eans": {
    "printwithsmile_pla_plabicolormetallicgreenbrown_1000_175_c": null,
    "printwithsmile_pla_plabicolormetallicplagreenbrown_1000_175_c": [
      "8594196450944"
    ]
  }
}
```

### PWS006: dup-e1d548a1048014b18fcbd09bf4505b61883bfbc53d5c1f80808b3e9fbbddbd0d

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plabicolormetallicgreenbrown_2000_175_c`|`PLA {color_name}`|`BICOLOR METALLIC GREEN BROWN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plabicolormetallicplagreenbrown_2000_175_c`|`PLA {color_name}`|`BICOLOR METALLIC PLA GREEN BROWN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plabicolormetallicgreenbrown_2000_175_c": "BA8960",
    "printwithsmile_pla_plabicolormetallicplagreenbrown_2000_175_c": "8b4513"
  },
  "codes": {
    "printwithsmile_pla_plabicolormetallicgreenbrown_2000_175_c": null,
    "printwithsmile_pla_plabicolormetallicplagreenbrown_2000_175_c": [
      "094"
    ]
  },
  "eans": {
    "printwithsmile_pla_plabicolormetallicgreenbrown_2000_175_c": null,
    "printwithsmile_pla_plabicolormetallicplagreenbrown_2000_175_c": [
      "8594196450944"
    ]
  }
}
```

### PWS007: dup-e58fc5cd7ee15c26bc32cf97120dc914f7b5c26826b2facef588417d289c952a

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plabicolormetallicgreenbrown_5000_175_c`|`PLA {color_name}`|`BICOLOR METALLIC GREEN BROWN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plabicolormetallicplagreenbrown_5000_175_c`|`PLA {color_name}`|`BICOLOR METALLIC PLA GREEN BROWN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plabicolormetallicgreenbrown_5000_175_c": "BA8960",
    "printwithsmile_pla_plabicolormetallicplagreenbrown_5000_175_c": "8b4513"
  },
  "codes": {
    "printwithsmile_pla_plabicolormetallicgreenbrown_5000_175_c": null,
    "printwithsmile_pla_plabicolormetallicplagreenbrown_5000_175_c": [
      "094"
    ]
  },
  "eans": {
    "printwithsmile_pla_plabicolormetallicgreenbrown_5000_175_c": null,
    "printwithsmile_pla_plabicolormetallicplagreenbrown_5000_175_c": [
      "8594196450944"
    ]
  }
}
```

### PWS008: dup-4263fee74b19fe680627aeea9802e7a6598c9ad8deb54b1db55ae1745f4f830b

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plabicolormetallicplavioletsilver_5000_175_c`|`PLA {color_name}`|`BICOLOR METALLIC PLA VIOLET SILVER`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plabicolormetallicvioletsilver_5000_175_c`|`PLA {color_name}`|`BICOLOR METALLIC VIOLET SILVER`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plabicolormetallicplavioletsilver_5000_175_c": "c0c0c0",
    "printwithsmile_pla_plabicolormetallicvioletsilver_5000_175_c": "583061"
  },
  "codes": {
    "printwithsmile_pla_plabicolormetallicplavioletsilver_5000_175_c": [
      "093"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsilver_5000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plabicolormetallicplavioletsilver_5000_175_c": [
      "8594196450937"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsilver_5000_175_c": null
  }
}
```

### PWS009: dup-75691292d8ea5d85a91ff2794c16cf72f58e79782aa368cb66c7397c339cb808

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plabicolormetallicplavioletsilver_750_175_c`|`PLA {color_name}`|`BICOLOR METALLIC PLA VIOLET SILVER`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plabicolormetallicvioletsilver_750_175_c`|`PLA {color_name}`|`BICOLOR METALLIC VIOLET SILVER`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plabicolormetallicplavioletsilver_750_175_c": "c0c0c0",
    "printwithsmile_pla_plabicolormetallicvioletsilver_750_175_c": "583061"
  },
  "codes": {
    "printwithsmile_pla_plabicolormetallicplavioletsilver_750_175_c": [
      "093"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsilver_750_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plabicolormetallicplavioletsilver_750_175_c": [
      "8594196450937"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsilver_750_175_c": null
  }
}
```

### PWS010: dup-8e1e5eb757017a05a1d345710b994f0c42b4a22cc2c3714ce6b12943e54f5740

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plabicolormetallicplavioletsilver_1000_175_c`|`PLA {color_name}`|`BICOLOR METALLIC PLA VIOLET SILVER`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plabicolormetallicvioletsilver_1000_175_c`|`PLA {color_name}`|`BICOLOR METALLIC VIOLET SILVER`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plabicolormetallicplavioletsilver_1000_175_c": "c0c0c0",
    "printwithsmile_pla_plabicolormetallicvioletsilver_1000_175_c": "583061"
  },
  "codes": {
    "printwithsmile_pla_plabicolormetallicplavioletsilver_1000_175_c": [
      "093"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsilver_1000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plabicolormetallicplavioletsilver_1000_175_c": [
      "8594196450937"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsilver_1000_175_c": null
  }
}
```

### PWS011: dup-948d5defd59ca737fddb2923f5858929729c2b9abd73eb6d135f688ba4a452c9

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plabicolormetallicplavioletsilver_2500_175_c`|`PLA {color_name}`|`BICOLOR METALLIC PLA VIOLET SILVER`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plabicolormetallicvioletsilver_2500_175_c`|`PLA {color_name}`|`BICOLOR METALLIC VIOLET SILVER`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plabicolormetallicplavioletsilver_2500_175_c": "c0c0c0",
    "printwithsmile_pla_plabicolormetallicvioletsilver_2500_175_c": "583061"
  },
  "codes": {
    "printwithsmile_pla_plabicolormetallicplavioletsilver_2500_175_c": [
      "093"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsilver_2500_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plabicolormetallicplavioletsilver_2500_175_c": [
      "8594196450937"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsilver_2500_175_c": null
  }
}
```

### PWS012: dup-a7779644a344f5fce85f74b8c330b104fea739742322be4a910523be25479e8e

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plabicolormetallicplavioletsilver_2000_175_c`|`PLA {color_name}`|`BICOLOR METALLIC PLA VIOLET SILVER`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plabicolormetallicvioletsilver_2000_175_c`|`PLA {color_name}`|`BICOLOR METALLIC VIOLET SILVER`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plabicolormetallicplavioletsilver_2000_175_c": "c0c0c0",
    "printwithsmile_pla_plabicolormetallicvioletsilver_2000_175_c": "583061"
  },
  "codes": {
    "printwithsmile_pla_plabicolormetallicplavioletsilver_2000_175_c": [
      "093"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsilver_2000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plabicolormetallicplavioletsilver_2000_175_c": [
      "8594196450937"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsilver_2000_175_c": null
  }
}
```

### PWS013: dup-f803743e61379025c17ea79b9e229ec94215ea1313bcec590a153b8323d18802

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plabicolormetallicplavioletsilver_500_175_c`|`PLA {color_name}`|`BICOLOR METALLIC PLA VIOLET SILVER`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plabicolormetallicvioletsilver_500_175_c`|`PLA {color_name}`|`BICOLOR METALLIC VIOLET SILVER`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plabicolormetallicplavioletsilver_500_175_c": "c0c0c0",
    "printwithsmile_pla_plabicolormetallicvioletsilver_500_175_c": "583061"
  },
  "codes": {
    "printwithsmile_pla_plabicolormetallicplavioletsilver_500_175_c": [
      "093"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsilver_500_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plabicolormetallicplavioletsilver_500_175_c": [
      "8594196450937"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsilver_500_175_c": null
  }
}
```

### PWS014: dup-03e887a192d0924353f7fa1a80ad4cca2557d9aaabe64979b3a8cdb3bf9727c7

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plabicolormetallicplavioletsparkle_1000_175_c`|`PLA {color_name}`|`BICOLOR METALLIC PLA VIOLET SPARKLE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plabicolormetallicvioletsparkle_1000_175_c`|`PLA {color_name}`|`BICOLOR METALLIC VIOLET SPARKLE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plabicolormetallicplavioletsparkle_1000_175_c": "8a2be2",
    "printwithsmile_pla_plabicolormetallicvioletsparkle_1000_175_c": "583061"
  },
  "codes": {
    "printwithsmile_pla_plabicolormetallicplavioletsparkle_1000_175_c": [
      "092"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsparkle_1000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plabicolormetallicplavioletsparkle_1000_175_c": [
      "8594196450920"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsparkle_1000_175_c": null
  }
}
```

### PWS015: dup-5d0673ef6d88573f5a97967bdc5464798a246b5fa9f4a6a669ea08c725a350dd

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plabicolormetallicplavioletsparkle_5000_175_c`|`PLA {color_name}`|`BICOLOR METALLIC PLA VIOLET SPARKLE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plabicolormetallicvioletsparkle_5000_175_c`|`PLA {color_name}`|`BICOLOR METALLIC VIOLET SPARKLE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plabicolormetallicplavioletsparkle_5000_175_c": "8a2be2",
    "printwithsmile_pla_plabicolormetallicvioletsparkle_5000_175_c": "583061"
  },
  "codes": {
    "printwithsmile_pla_plabicolormetallicplavioletsparkle_5000_175_c": [
      "092"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsparkle_5000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plabicolormetallicplavioletsparkle_5000_175_c": [
      "8594196450920"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsparkle_5000_175_c": null
  }
}
```

### PWS016: dup-7016597dbd930380e81d47e5a724dc5ee39516bdc26bee6efc998d9ce3ecfb0e

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plabicolormetallicplavioletsparkle_2500_175_c`|`PLA {color_name}`|`BICOLOR METALLIC PLA VIOLET SPARKLE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plabicolormetallicvioletsparkle_2500_175_c`|`PLA {color_name}`|`BICOLOR METALLIC VIOLET SPARKLE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plabicolormetallicplavioletsparkle_2500_175_c": "8a2be2",
    "printwithsmile_pla_plabicolormetallicvioletsparkle_2500_175_c": "583061"
  },
  "codes": {
    "printwithsmile_pla_plabicolormetallicplavioletsparkle_2500_175_c": [
      "092"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsparkle_2500_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plabicolormetallicplavioletsparkle_2500_175_c": [
      "8594196450920"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsparkle_2500_175_c": null
  }
}
```

### PWS017: dup-9042a107317c1eee9be047b386eb387c7955c7f9647b9011c0417036f5e4e619

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plabicolormetallicplavioletsparkle_750_175_c`|`PLA {color_name}`|`BICOLOR METALLIC PLA VIOLET SPARKLE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plabicolormetallicvioletsparkle_750_175_c`|`PLA {color_name}`|`BICOLOR METALLIC VIOLET SPARKLE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plabicolormetallicplavioletsparkle_750_175_c": "8a2be2",
    "printwithsmile_pla_plabicolormetallicvioletsparkle_750_175_c": "583061"
  },
  "codes": {
    "printwithsmile_pla_plabicolormetallicplavioletsparkle_750_175_c": [
      "092"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsparkle_750_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plabicolormetallicplavioletsparkle_750_175_c": [
      "8594196450920"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsparkle_750_175_c": null
  }
}
```

### PWS018: dup-951e6d5666b80e50295fed9761024fc543963b252ba1b67b20a83df15493f71a

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plabicolormetallicplavioletsparkle_2000_175_c`|`PLA {color_name}`|`BICOLOR METALLIC PLA VIOLET SPARKLE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plabicolormetallicvioletsparkle_2000_175_c`|`PLA {color_name}`|`BICOLOR METALLIC VIOLET SPARKLE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plabicolormetallicplavioletsparkle_2000_175_c": "8a2be2",
    "printwithsmile_pla_plabicolormetallicvioletsparkle_2000_175_c": "583061"
  },
  "codes": {
    "printwithsmile_pla_plabicolormetallicplavioletsparkle_2000_175_c": [
      "092"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsparkle_2000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plabicolormetallicplavioletsparkle_2000_175_c": [
      "8594196450920"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsparkle_2000_175_c": null
  }
}
```

### PWS019: dup-97df22fd7b72e894f34a1d6446701a36b6ee25ee22d8263a824437a034d3171b

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plabicolormetallicplavioletsparkle_500_175_c`|`PLA {color_name}`|`BICOLOR METALLIC PLA VIOLET SPARKLE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plabicolormetallicvioletsparkle_500_175_c`|`PLA {color_name}`|`BICOLOR METALLIC VIOLET SPARKLE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plabicolormetallicplavioletsparkle_500_175_c": "8a2be2",
    "printwithsmile_pla_plabicolormetallicvioletsparkle_500_175_c": "583061"
  },
  "codes": {
    "printwithsmile_pla_plabicolormetallicplavioletsparkle_500_175_c": [
      "092"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsparkle_500_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plabicolormetallicplavioletsparkle_500_175_c": [
      "8594196450920"
    ],
    "printwithsmile_pla_plabicolormetallicvioletsparkle_500_175_c": null
  }
}
```

### PWS020: dup-159228f070a45244be0cf37bd92df96af8d2a9a68616231d5e988d134e34b244

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinpeachred_2000_175_c`|`PLA {color_name}`|`SATIN Peach RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinplapeachred_2000_175_c`|`PLA {color_name}`|`SATIN PLA Peach RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinpeachred_2000_175_c": "FC496D",
    "printwithsmile_pla_plasatinplapeachred_2000_175_c": "cc0000"
  },
  "codes": {
    "printwithsmile_pla_plasatinpeachred_2000_175_c": null,
    "printwithsmile_pla_plasatinplapeachred_2000_175_c": [
      "066",
      "056"
    ]
  },
  "eans": {
    "printwithsmile_pla_plasatinpeachred_2000_175_c": null,
    "printwithsmile_pla_plasatinplapeachred_2000_175_c": [
      "8594196450661",
      "8594196450562"
    ]
  }
}
```

### PWS021: dup-25e50e79ce497fe280ecc03e0870ea51282e73a3f3349bd04bcd2b34d55b5c69

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinpeachred_750_175_c`|`PLA {color_name}`|`SATIN Peach RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinplapeachred_750_175_c`|`PLA {color_name}`|`SATIN PLA Peach RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinpeachred_750_175_c": "FC496D",
    "printwithsmile_pla_plasatinplapeachred_750_175_c": "cc0000"
  },
  "codes": {
    "printwithsmile_pla_plasatinpeachred_750_175_c": null,
    "printwithsmile_pla_plasatinplapeachred_750_175_c": [
      "066",
      "056"
    ]
  },
  "eans": {
    "printwithsmile_pla_plasatinpeachred_750_175_c": null,
    "printwithsmile_pla_plasatinplapeachred_750_175_c": [
      "8594196450661",
      "8594196450562"
    ]
  }
}
```

### PWS022: dup-7dd65f5e2c435c49e36d94a12c0caa8ccf05ee7de9305936c8a96ffdc8997b23

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinpeachred_500_175_c`|`PLA {color_name}`|`SATIN Peach RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinplapeachred_500_175_c`|`PLA {color_name}`|`SATIN PLA Peach RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinpeachred_500_175_c": "FC496D",
    "printwithsmile_pla_plasatinplapeachred_500_175_c": "cc0000"
  },
  "codes": {
    "printwithsmile_pla_plasatinpeachred_500_175_c": null,
    "printwithsmile_pla_plasatinplapeachred_500_175_c": [
      "066",
      "056"
    ]
  },
  "eans": {
    "printwithsmile_pla_plasatinpeachred_500_175_c": null,
    "printwithsmile_pla_plasatinplapeachred_500_175_c": [
      "8594196450661",
      "8594196450562"
    ]
  }
}
```

### PWS023: dup-86e315258338876a211e4f8f3a54c85517c739d64ba3789c09dd4073a5561853

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinpeachred_5000_175_c`|`PLA {color_name}`|`SATIN Peach RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinplapeachred_5000_175_c`|`PLA {color_name}`|`SATIN PLA Peach RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinpeachred_5000_175_c": "FC496D",
    "printwithsmile_pla_plasatinplapeachred_5000_175_c": "cc0000"
  },
  "codes": {
    "printwithsmile_pla_plasatinpeachred_5000_175_c": null,
    "printwithsmile_pla_plasatinplapeachred_5000_175_c": [
      "066",
      "056"
    ]
  },
  "eans": {
    "printwithsmile_pla_plasatinpeachred_5000_175_c": null,
    "printwithsmile_pla_plasatinplapeachred_5000_175_c": [
      "8594196450661",
      "8594196450562"
    ]
  }
}
```

### PWS024: dup-9f50efab50e6bc8ae7c358ec89ee2a403c95054c9c4fbbf73c64f7eb20ba9c77

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinpeachred_1000_175_c`|`PLA {color_name}`|`SATIN Peach RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinplapeachred_1000_175_c`|`PLA {color_name}`|`SATIN PLA Peach RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinpeachred_1000_175_c": "FC496D",
    "printwithsmile_pla_plasatinplapeachred_1000_175_c": "cc0000"
  },
  "codes": {
    "printwithsmile_pla_plasatinpeachred_1000_175_c": null,
    "printwithsmile_pla_plasatinplapeachred_1000_175_c": [
      "066",
      "056"
    ]
  },
  "eans": {
    "printwithsmile_pla_plasatinpeachred_1000_175_c": null,
    "printwithsmile_pla_plasatinplapeachred_1000_175_c": [
      "8594196450661",
      "8594196450562"
    ]
  }
}
```

### PWS025: dup-c331a30c09eca28ced3dce308140931af035500a9d7d618cdcd35e2ebf271d02

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinpeachred_2500_175_c`|`PLA {color_name}`|`SATIN Peach RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinplapeachred_2500_175_c`|`PLA {color_name}`|`SATIN PLA Peach RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinpeachred_2500_175_c": "FC496D",
    "printwithsmile_pla_plasatinplapeachred_2500_175_c": "cc0000"
  },
  "codes": {
    "printwithsmile_pla_plasatinpeachred_2500_175_c": null,
    "printwithsmile_pla_plasatinplapeachred_2500_175_c": [
      "066",
      "056"
    ]
  },
  "eans": {
    "printwithsmile_pla_plasatinpeachred_2500_175_c": null,
    "printwithsmile_pla_plasatinplapeachred_2500_175_c": [
      "8594196450661",
      "8594196450562"
    ]
  }
}
```

### PWS026: dup-1c8cc71ac91f2a7799dcd95ce1e8ef11e410339cfe313fef82ed5e5ef3af481a

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaprincesspink_500_175_c`|`PLA {color_name}`|`SATIN PLA Princess PINK`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinprincesspink_500_175_c`|`PLA {color_name}`|`SATIN Princess PINK`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaprincesspink_500_175_c": "ff69b4",
    "printwithsmile_pla_plasatinprincesspink_500_175_c": "FF67F5"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaprincesspink_500_175_c": [
      "057"
    ],
    "printwithsmile_pla_plasatinprincesspink_500_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaprincesspink_500_175_c": [
      "8594196450579"
    ],
    "printwithsmile_pla_plasatinprincesspink_500_175_c": null
  }
}
```

### PWS027: dup-33565435c5e49b6e104b0055d1b06ce1ffa015b348911d86c40b3841c962df3b

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaprincesspink_2500_175_c`|`PLA {color_name}`|`SATIN PLA Princess PINK`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinprincesspink_2500_175_c`|`PLA {color_name}`|`SATIN Princess PINK`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaprincesspink_2500_175_c": "ff69b4",
    "printwithsmile_pla_plasatinprincesspink_2500_175_c": "FF67F5"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaprincesspink_2500_175_c": [
      "057"
    ],
    "printwithsmile_pla_plasatinprincesspink_2500_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaprincesspink_2500_175_c": [
      "8594196450579"
    ],
    "printwithsmile_pla_plasatinprincesspink_2500_175_c": null
  }
}
```

### PWS028: dup-9bf143cb4176e47737ec0cd73a907038fa431a5a9f526f72d24b0d6f984e872d

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaprincesspink_1000_175_c`|`PLA {color_name}`|`SATIN PLA Princess PINK`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinprincesspink_1000_175_c`|`PLA {color_name}`|`SATIN Princess PINK`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaprincesspink_1000_175_c": "ff69b4",
    "printwithsmile_pla_plasatinprincesspink_1000_175_c": "FF67F5"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaprincesspink_1000_175_c": [
      "057"
    ],
    "printwithsmile_pla_plasatinprincesspink_1000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaprincesspink_1000_175_c": [
      "8594196450579"
    ],
    "printwithsmile_pla_plasatinprincesspink_1000_175_c": null
  }
}
```

### PWS029: dup-a5996db3ebaba10aea0fb797baf81a52673ec42c49f560fea345902f3f6dd9f4

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaprincesspink_750_175_c`|`PLA {color_name}`|`SATIN PLA Princess PINK`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinprincesspink_750_175_c`|`PLA {color_name}`|`SATIN Princess PINK`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaprincesspink_750_175_c": "ff69b4",
    "printwithsmile_pla_plasatinprincesspink_750_175_c": "FF67F5"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaprincesspink_750_175_c": [
      "057"
    ],
    "printwithsmile_pla_plasatinprincesspink_750_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaprincesspink_750_175_c": [
      "8594196450579"
    ],
    "printwithsmile_pla_plasatinprincesspink_750_175_c": null
  }
}
```

### PWS030: dup-be8bbfa592d86de48d8aa0c9647fd0d9188ac8776f3357b9dabc9dc2ba568c97

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaprincesspink_5000_175_c`|`PLA {color_name}`|`SATIN PLA Princess PINK`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinprincesspink_5000_175_c`|`PLA {color_name}`|`SATIN Princess PINK`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaprincesspink_5000_175_c": "ff69b4",
    "printwithsmile_pla_plasatinprincesspink_5000_175_c": "FF67F5"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaprincesspink_5000_175_c": [
      "057"
    ],
    "printwithsmile_pla_plasatinprincesspink_5000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaprincesspink_5000_175_c": [
      "8594196450579"
    ],
    "printwithsmile_pla_plasatinprincesspink_5000_175_c": null
  }
}
```

### PWS031: dup-fc345bc1f2972dfd0be261160834da673b967bebe1d2e5e69844b1ec3c1abfe3

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaprincesspink_2000_175_c`|`PLA {color_name}`|`SATIN PLA Princess PINK`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinprincesspink_2000_175_c`|`PLA {color_name}`|`SATIN Princess PINK`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaprincesspink_2000_175_c": "ff69b4",
    "printwithsmile_pla_plasatinprincesspink_2000_175_c": "FF67F5"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaprincesspink_2000_175_c": [
      "057"
    ],
    "printwithsmile_pla_plasatinprincesspink_2000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaprincesspink_2000_175_c": [
      "8594196450579"
    ],
    "printwithsmile_pla_plasatinprincesspink_2000_175_c": null
  }
}
```

### PWS032: dup-35e3ed8349f7c36022c59a09fb5a91ef169461f5f718bd0f7888e234bfceb039

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaskyblue_500_175_c`|`PLA {color_name}`|`SATIN PLA Sky BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinskyblue_500_175_c`|`PLA {color_name}`|`SATIN Sky BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaskyblue_500_175_c": "0066cc",
    "printwithsmile_pla_plasatinskyblue_500_175_c": "0099E6"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaskyblue_500_175_c": [
      "068",
      "058"
    ],
    "printwithsmile_pla_plasatinskyblue_500_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaskyblue_500_175_c": [
      "8594196450685",
      "8594196450586"
    ],
    "printwithsmile_pla_plasatinskyblue_500_175_c": null
  }
}
```

### PWS033: dup-8e4e26d14f4c3a9f77f2d00be0710ca4253a63ec662a94e42b5bb1e5e4ae2195

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaskyblue_1000_175_c`|`PLA {color_name}`|`SATIN PLA Sky BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinskyblue_1000_175_c`|`PLA {color_name}`|`SATIN Sky BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaskyblue_1000_175_c": "0066cc",
    "printwithsmile_pla_plasatinskyblue_1000_175_c": "0099E6"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaskyblue_1000_175_c": [
      "068",
      "058"
    ],
    "printwithsmile_pla_plasatinskyblue_1000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaskyblue_1000_175_c": [
      "8594196450685",
      "8594196450586"
    ],
    "printwithsmile_pla_plasatinskyblue_1000_175_c": null
  }
}
```

### PWS034: dup-91921c61b2585207c5b61ac5670a867b43821b244ea23553753da30028218cb0

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaskyblue_2500_175_c`|`PLA {color_name}`|`SATIN PLA Sky BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinskyblue_2500_175_c`|`PLA {color_name}`|`SATIN Sky BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaskyblue_2500_175_c": "0066cc",
    "printwithsmile_pla_plasatinskyblue_2500_175_c": "0099E6"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaskyblue_2500_175_c": [
      "068",
      "058"
    ],
    "printwithsmile_pla_plasatinskyblue_2500_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaskyblue_2500_175_c": [
      "8594196450685",
      "8594196450586"
    ],
    "printwithsmile_pla_plasatinskyblue_2500_175_c": null
  }
}
```

### PWS035: dup-92836721b8435f0de68fdd50f0ee5e570af854259ad70d8a5b4fa831bf8333d6

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaskyblue_2000_175_c`|`PLA {color_name}`|`SATIN PLA Sky BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinskyblue_2000_175_c`|`PLA {color_name}`|`SATIN Sky BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaskyblue_2000_175_c": "0066cc",
    "printwithsmile_pla_plasatinskyblue_2000_175_c": "0099E6"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaskyblue_2000_175_c": [
      "068",
      "058"
    ],
    "printwithsmile_pla_plasatinskyblue_2000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaskyblue_2000_175_c": [
      "8594196450685",
      "8594196450586"
    ],
    "printwithsmile_pla_plasatinskyblue_2000_175_c": null
  }
}
```

### PWS036: dup-93717e2c7f36398ddf715020c1fe273205d7469b4b8edce0240ed1803f3191e5

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaskyblue_5000_175_c`|`PLA {color_name}`|`SATIN PLA Sky BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinskyblue_5000_175_c`|`PLA {color_name}`|`SATIN Sky BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaskyblue_5000_175_c": "0066cc",
    "printwithsmile_pla_plasatinskyblue_5000_175_c": "0099E6"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaskyblue_5000_175_c": [
      "068",
      "058"
    ],
    "printwithsmile_pla_plasatinskyblue_5000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaskyblue_5000_175_c": [
      "8594196450685",
      "8594196450586"
    ],
    "printwithsmile_pla_plasatinskyblue_5000_175_c": null
  }
}
```

### PWS037: dup-b2195f9239e20069cb9e5c7ecf12e77fb546728d4ecfb6c88d1df464e3e45102

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaskyblue_750_175_c`|`PLA {color_name}`|`SATIN PLA Sky BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinskyblue_750_175_c`|`PLA {color_name}`|`SATIN Sky BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaskyblue_750_175_c": "0066cc",
    "printwithsmile_pla_plasatinskyblue_750_175_c": "0099E6"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaskyblue_750_175_c": [
      "068",
      "058"
    ],
    "printwithsmile_pla_plasatinskyblue_750_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaskyblue_750_175_c": [
      "8594196450685",
      "8594196450586"
    ],
    "printwithsmile_pla_plasatinskyblue_750_175_c": null
  }
}
```

### PWS038: dup-1b2f5ae402ec9bbdd644a54465d3937a7bd24f69e7075b6df1704702efcff47b

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaspringgreen_2000_175_c`|`PLA {color_name}`|`SATIN PLA Spring GREEN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinspringgreen_2000_175_c`|`PLA {color_name}`|`SATIN Spring GREEN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaspringgreen_2000_175_c": "228b22",
    "printwithsmile_pla_plasatinspringgreen_2000_175_c": "26A648"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaspringgreen_2000_175_c": [
      "069",
      "059"
    ],
    "printwithsmile_pla_plasatinspringgreen_2000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaspringgreen_2000_175_c": [
      "8594196450692",
      "8594196450593"
    ],
    "printwithsmile_pla_plasatinspringgreen_2000_175_c": null
  }
}
```

### PWS039: dup-4cd6e8e9cc21b9d279211af016ac560402f1820efefbeb10251f370b7ddf24fa

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaspringgreen_500_175_c`|`PLA {color_name}`|`SATIN PLA Spring GREEN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinspringgreen_500_175_c`|`PLA {color_name}`|`SATIN Spring GREEN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaspringgreen_500_175_c": "228b22",
    "printwithsmile_pla_plasatinspringgreen_500_175_c": "26A648"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaspringgreen_500_175_c": [
      "069",
      "059"
    ],
    "printwithsmile_pla_plasatinspringgreen_500_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaspringgreen_500_175_c": [
      "8594196450692",
      "8594196450593"
    ],
    "printwithsmile_pla_plasatinspringgreen_500_175_c": null
  }
}
```

### PWS040: dup-55c990ffcb762b5f90cc06495cbe55818d1a7be42b576e61c973379e2ef540f3

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaspringgreen_2500_175_c`|`PLA {color_name}`|`SATIN PLA Spring GREEN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinspringgreen_2500_175_c`|`PLA {color_name}`|`SATIN Spring GREEN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaspringgreen_2500_175_c": "228b22",
    "printwithsmile_pla_plasatinspringgreen_2500_175_c": "26A648"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaspringgreen_2500_175_c": [
      "069",
      "059"
    ],
    "printwithsmile_pla_plasatinspringgreen_2500_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaspringgreen_2500_175_c": [
      "8594196450692",
      "8594196450593"
    ],
    "printwithsmile_pla_plasatinspringgreen_2500_175_c": null
  }
}
```

### PWS041: dup-70cb8b01e9c519c6386ffba2eb948f78ee40aef7e36053c38f95de2a47e366d9

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaspringgreen_750_175_c`|`PLA {color_name}`|`SATIN PLA Spring GREEN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinspringgreen_750_175_c`|`PLA {color_name}`|`SATIN Spring GREEN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaspringgreen_750_175_c": "228b22",
    "printwithsmile_pla_plasatinspringgreen_750_175_c": "26A648"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaspringgreen_750_175_c": [
      "069",
      "059"
    ],
    "printwithsmile_pla_plasatinspringgreen_750_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaspringgreen_750_175_c": [
      "8594196450692",
      "8594196450593"
    ],
    "printwithsmile_pla_plasatinspringgreen_750_175_c": null
  }
}
```

### PWS042: dup-f3f005f10b62a4670e438e0f87932e7023eb3a9b4d76c1e6ade3931c377f510f

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaspringgreen_1000_175_c`|`PLA {color_name}`|`SATIN PLA Spring GREEN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinspringgreen_1000_175_c`|`PLA {color_name}`|`SATIN Spring GREEN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaspringgreen_1000_175_c": "228b22",
    "printwithsmile_pla_plasatinspringgreen_1000_175_c": "26A648"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaspringgreen_1000_175_c": [
      "069",
      "059"
    ],
    "printwithsmile_pla_plasatinspringgreen_1000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaspringgreen_1000_175_c": [
      "8594196450692",
      "8594196450593"
    ],
    "printwithsmile_pla_plasatinspringgreen_1000_175_c": null
  }
}
```

### PWS043: dup-f9569743e81d08025ccd64c4bffb058d22060e0482c99a70b71f3a628844e41c

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaspringgreen_5000_175_c`|`PLA {color_name}`|`SATIN PLA Spring GREEN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinspringgreen_5000_175_c`|`PLA {color_name}`|`SATIN Spring GREEN`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaspringgreen_5000_175_c": "228b22",
    "printwithsmile_pla_plasatinspringgreen_5000_175_c": "26A648"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaspringgreen_5000_175_c": [
      "069",
      "059"
    ],
    "printwithsmile_pla_plasatinspringgreen_5000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaspringgreen_5000_175_c": [
      "8594196450692",
      "8594196450593"
    ],
    "printwithsmile_pla_plasatinspringgreen_5000_175_c": null
  }
}
```

### PWS044: dup-03fcee97772e32cee4df5a627c4b66e103ed8d3d0de5641d8fdaeee95c1bfdfe

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaviolet_2000_175_c`|`PLA {color_name}`|`SATIN PLA Violet`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinviolet_2000_175_c`|`PLA {color_name}`|`SATIN Violet`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaviolet_2000_175_c": "8a2be2",
    "printwithsmile_pla_plasatinviolet_2000_175_c": "0353BA"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaviolet_2000_175_c": [
      "070",
      "060"
    ],
    "printwithsmile_pla_plasatinviolet_2000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaviolet_2000_175_c": [
      "8594196450708",
      "8594196450609"
    ],
    "printwithsmile_pla_plasatinviolet_2000_175_c": null
  }
}
```

### PWS045: dup-04b4ee517eb2aab5697d9b5d08de5a2e4615da68ad0e7449f6443d5231a708bb

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaviolet_1000_175_c`|`PLA {color_name}`|`SATIN PLA Violet`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinviolet_1000_175_c`|`PLA {color_name}`|`SATIN Violet`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaviolet_1000_175_c": "8a2be2",
    "printwithsmile_pla_plasatinviolet_1000_175_c": "0353BA"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaviolet_1000_175_c": [
      "070",
      "060"
    ],
    "printwithsmile_pla_plasatinviolet_1000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaviolet_1000_175_c": [
      "8594196450708",
      "8594196450609"
    ],
    "printwithsmile_pla_plasatinviolet_1000_175_c": null
  }
}
```

### PWS046: dup-40ccca3bdbf80131426d6e5cd9fee91606f0c4561f9535e723c4107448b9648d

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaviolet_750_175_c`|`PLA {color_name}`|`SATIN PLA Violet`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinviolet_750_175_c`|`PLA {color_name}`|`SATIN Violet`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaviolet_750_175_c": "8a2be2",
    "printwithsmile_pla_plasatinviolet_750_175_c": "0353BA"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaviolet_750_175_c": [
      "070",
      "060"
    ],
    "printwithsmile_pla_plasatinviolet_750_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaviolet_750_175_c": [
      "8594196450708",
      "8594196450609"
    ],
    "printwithsmile_pla_plasatinviolet_750_175_c": null
  }
}
```

### PWS047: dup-67d461ac778007605ceb4a6505e552da86371aff2db47c03724f8801ed9deaef

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaviolet_2500_175_c`|`PLA {color_name}`|`SATIN PLA Violet`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinviolet_2500_175_c`|`PLA {color_name}`|`SATIN Violet`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaviolet_2500_175_c": "8a2be2",
    "printwithsmile_pla_plasatinviolet_2500_175_c": "0353BA"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaviolet_2500_175_c": [
      "070",
      "060"
    ],
    "printwithsmile_pla_plasatinviolet_2500_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaviolet_2500_175_c": [
      "8594196450708",
      "8594196450609"
    ],
    "printwithsmile_pla_plasatinviolet_2500_175_c": null
  }
}
```

### PWS048: dup-d2a0d445e49d7d4948a1fff23e3ecb0cc7f2724ad1b44a52562914003960ddf6

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaviolet_500_175_c`|`PLA {color_name}`|`SATIN PLA Violet`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinviolet_500_175_c`|`PLA {color_name}`|`SATIN Violet`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaviolet_500_175_c": "8a2be2",
    "printwithsmile_pla_plasatinviolet_500_175_c": "0353BA"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaviolet_500_175_c": [
      "070",
      "060"
    ],
    "printwithsmile_pla_plasatinviolet_500_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaviolet_500_175_c": [
      "8594196450708",
      "8594196450609"
    ],
    "printwithsmile_pla_plasatinviolet_500_175_c": null
  }
}
```

### PWS049: dup-db992bf8f9ba43139ab101fdd40ce38a5987ecfae471ead25b643179820459e5

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplaviolet_5000_175_c`|`PLA {color_name}`|`SATIN PLA Violet`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinviolet_5000_175_c`|`PLA {color_name}`|`SATIN Violet`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplaviolet_5000_175_c": "8a2be2",
    "printwithsmile_pla_plasatinviolet_5000_175_c": "0353BA"
  },
  "codes": {
    "printwithsmile_pla_plasatinplaviolet_5000_175_c": [
      "070",
      "060"
    ],
    "printwithsmile_pla_plasatinviolet_5000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplaviolet_5000_175_c": [
      "8594196450708",
      "8594196450609"
    ],
    "printwithsmile_pla_plasatinviolet_5000_175_c": null
  }
}
```

### PWS050: dup-15efe28114b105cf07b5eba292f50810f54109f4ed7262cb2011f982601ac56e

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplayellow_2000_175_c`|`PLA {color_name}`|`SATIN PLA Yellow`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinyellow_2000_175_c`|`PLA {color_name}`|`SATIN Yellow`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplayellow_2000_175_c": "ffff00",
    "printwithsmile_pla_plasatinyellow_2000_175_c": "F3B400"
  },
  "codes": {
    "printwithsmile_pla_plasatinplayellow_2000_175_c": [
      "071",
      "055"
    ],
    "printwithsmile_pla_plasatinyellow_2000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplayellow_2000_175_c": [
      "8594196450715",
      "8594196450555"
    ],
    "printwithsmile_pla_plasatinyellow_2000_175_c": null
  }
}
```

### PWS051: dup-4d6e52fe7fef35f850a4b548792cbef3ea59d18bd8b1e0c2b2975d773bf126a5

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplayellow_2500_175_c`|`PLA {color_name}`|`SATIN PLA Yellow`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinyellow_2500_175_c`|`PLA {color_name}`|`SATIN Yellow`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplayellow_2500_175_c": "ffff00",
    "printwithsmile_pla_plasatinyellow_2500_175_c": "F3B400"
  },
  "codes": {
    "printwithsmile_pla_plasatinplayellow_2500_175_c": [
      "071",
      "055"
    ],
    "printwithsmile_pla_plasatinyellow_2500_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplayellow_2500_175_c": [
      "8594196450715",
      "8594196450555"
    ],
    "printwithsmile_pla_plasatinyellow_2500_175_c": null
  }
}
```

### PWS052: dup-c59cceb2527eaf8d7c4eeeb39c4decd729fa72732c4b1825e53d70c7fb7cbdbb

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplayellow_1000_175_c`|`PLA {color_name}`|`SATIN PLA Yellow`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinyellow_1000_175_c`|`PLA {color_name}`|`SATIN Yellow`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplayellow_1000_175_c": "ffff00",
    "printwithsmile_pla_plasatinyellow_1000_175_c": "F3B400"
  },
  "codes": {
    "printwithsmile_pla_plasatinplayellow_1000_175_c": [
      "071",
      "055"
    ],
    "printwithsmile_pla_plasatinyellow_1000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplayellow_1000_175_c": [
      "8594196450715",
      "8594196450555"
    ],
    "printwithsmile_pla_plasatinyellow_1000_175_c": null
  }
}
```

### PWS053: dup-dbf1f7144a1a3fe30b42574f8d868ae219179d1c2013a8dab5c1917daf9ddd90

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplayellow_5000_175_c`|`PLA {color_name}`|`SATIN PLA Yellow`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinyellow_5000_175_c`|`PLA {color_name}`|`SATIN Yellow`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplayellow_5000_175_c": "ffff00",
    "printwithsmile_pla_plasatinyellow_5000_175_c": "F3B400"
  },
  "codes": {
    "printwithsmile_pla_plasatinplayellow_5000_175_c": [
      "071",
      "055"
    ],
    "printwithsmile_pla_plasatinyellow_5000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplayellow_5000_175_c": [
      "8594196450715",
      "8594196450555"
    ],
    "printwithsmile_pla_plasatinyellow_5000_175_c": null
  }
}
```

### PWS054: dup-ef478e28207619bcbc0c07843d39870c3b895b36a264f1a8e2beede4cc034ab8

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplayellow_500_175_c`|`PLA {color_name}`|`SATIN PLA Yellow`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinyellow_500_175_c`|`PLA {color_name}`|`SATIN Yellow`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplayellow_500_175_c": "ffff00",
    "printwithsmile_pla_plasatinyellow_500_175_c": "F3B400"
  },
  "codes": {
    "printwithsmile_pla_plasatinplayellow_500_175_c": [
      "071",
      "055"
    ],
    "printwithsmile_pla_plasatinyellow_500_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplayellow_500_175_c": [
      "8594196450715",
      "8594196450555"
    ],
    "printwithsmile_pla_plasatinyellow_500_175_c": null
  }
}
```

### PWS055: dup-f0aad06a2696405087a1014896c29e2b5fafbeb6bf5b31e27f6360a670843853

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasatinplayellow_750_175_c`|`PLA {color_name}`|`SATIN PLA Yellow`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plasatinyellow_750_175_c`|`PLA {color_name}`|`SATIN Yellow`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasatinplayellow_750_175_c": "ffff00",
    "printwithsmile_pla_plasatinyellow_750_175_c": "F3B400"
  },
  "codes": {
    "printwithsmile_pla_plasatinplayellow_750_175_c": [
      "071",
      "055"
    ],
    "printwithsmile_pla_plasatinyellow_750_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasatinplayellow_750_175_c": [
      "8594196450715",
      "8594196450555"
    ],
    "printwithsmile_pla_plasatinyellow_750_175_c": null
  }
}
```

### PWS056: dup-263165a0a50b23fc657d60c448551645f5806784acd27ce1602a35fe9ce91830

Status: DEFERRED; survivor `printwithsmile_pla_plasilkplaoldgold_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plasilkplaoldgold_1000_175_c`|`PLA {color_name}`|`SILK PLA OLD GOLD`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_silkplaoldgold_1000_175_c`|`Silk PLA {color_name}`|`OLD GOLD`|{"source_file": "printwithsmile.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plasilkplaoldgold_1000_175_c": "daa520",
    "printwithsmile_pla_silkplaoldgold_1000_175_c": "D0BD93"
  },
  "bed_temp_range": {
    "printwithsmile_pla_plasilkplaoldgold_1000_175_c": [
      60,
      65
    ],
    "printwithsmile_pla_silkplaoldgold_1000_175_c": [
      50,
      70
    ]
  },
  "finish": {
    "printwithsmile_pla_plasilkplaoldgold_1000_175_c": "glossy",
    "printwithsmile_pla_silkplaoldgold_1000_175_c": null
  },
  "codes": {
    "printwithsmile_pla_plasilkplaoldgold_1000_175_c": [
      "582"
    ],
    "printwithsmile_pla_silkplaoldgold_1000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plasilkplaoldgold_1000_175_c": [
      "8594196455826"
    ],
    "printwithsmile_pla_silkplaoldgold_1000_175_c": null
  }
}
```

### PWS057: dup-2e98eea115144310a1b222eb2c6cd4ad742a9b33a4b7494e6a0dc4440bac729b

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plathermblue_1000_175_c`|`PLA {color_name}`|`THERM BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plathermplablue_1000_175_c`|`PLA {color_name}`|`THERM PLA BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plathermblue_1000_175_c": "DFDFD3",
    "printwithsmile_pla_plathermplablue_1000_175_c": "0066cc"
  },
  "codes": {
    "printwithsmile_pla_plathermblue_1000_175_c": null,
    "printwithsmile_pla_plathermplablue_1000_175_c": [
      "545"
    ]
  },
  "eans": {
    "printwithsmile_pla_plathermblue_1000_175_c": null,
    "printwithsmile_pla_plathermplablue_1000_175_c": [
      "8594196455451"
    ]
  }
}
```

### PWS058: dup-8d53cd4c2fd2750950fa61ebfd5809fa5660e5e9c9240242f944d800b3e44a07

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plathermblue_500_175_c`|`PLA {color_name}`|`THERM BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plathermplablue_500_175_c`|`PLA {color_name}`|`THERM PLA BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plathermblue_500_175_c": "DFDFD3",
    "printwithsmile_pla_plathermplablue_500_175_c": "0066cc"
  },
  "codes": {
    "printwithsmile_pla_plathermblue_500_175_c": null,
    "printwithsmile_pla_plathermplablue_500_175_c": [
      "545"
    ]
  },
  "eans": {
    "printwithsmile_pla_plathermblue_500_175_c": null,
    "printwithsmile_pla_plathermplablue_500_175_c": [
      "8594196455451"
    ]
  }
}
```

### PWS059: dup-9ffbd27aa746d5e0d7c7c661a692db5fb46bf6660664bcea90fc0fb53e36680c

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plathermblue_2500_175_c`|`PLA {color_name}`|`THERM BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plathermplablue_2500_175_c`|`PLA {color_name}`|`THERM PLA BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plathermblue_2500_175_c": "DFDFD3",
    "printwithsmile_pla_plathermplablue_2500_175_c": "0066cc"
  },
  "codes": {
    "printwithsmile_pla_plathermblue_2500_175_c": null,
    "printwithsmile_pla_plathermplablue_2500_175_c": [
      "545"
    ]
  },
  "eans": {
    "printwithsmile_pla_plathermblue_2500_175_c": null,
    "printwithsmile_pla_plathermplablue_2500_175_c": [
      "8594196455451"
    ]
  }
}
```

### PWS060: dup-a458db49a6c00515a1a20b17638dcf15dc6907c012df29bcf9c6bfa9a7d1dd30

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plathermblue_5000_175_c`|`PLA {color_name}`|`THERM BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plathermplablue_5000_175_c`|`PLA {color_name}`|`THERM PLA BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plathermblue_5000_175_c": "DFDFD3",
    "printwithsmile_pla_plathermplablue_5000_175_c": "0066cc"
  },
  "codes": {
    "printwithsmile_pla_plathermblue_5000_175_c": null,
    "printwithsmile_pla_plathermplablue_5000_175_c": [
      "545"
    ]
  },
  "eans": {
    "printwithsmile_pla_plathermblue_5000_175_c": null,
    "printwithsmile_pla_plathermplablue_5000_175_c": [
      "8594196455451"
    ]
  }
}
```

### PWS061: dup-cf4b9064da557ab75d3598f13c9b86f780b49e153e84c76896acc9ad16213b04

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plathermblue_750_175_c`|`PLA {color_name}`|`THERM BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plathermplablue_750_175_c`|`PLA {color_name}`|`THERM PLA BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plathermblue_750_175_c": "DFDFD3",
    "printwithsmile_pla_plathermplablue_750_175_c": "0066cc"
  },
  "codes": {
    "printwithsmile_pla_plathermblue_750_175_c": null,
    "printwithsmile_pla_plathermplablue_750_175_c": [
      "545"
    ]
  },
  "eans": {
    "printwithsmile_pla_plathermblue_750_175_c": null,
    "printwithsmile_pla_plathermplablue_750_175_c": [
      "8594196455451"
    ]
  }
}
```

### PWS062: dup-e01e39fd81a829456179c45b1c54057f6392174346808ad30465db27d6ec343f

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plathermblue_2000_175_c`|`PLA {color_name}`|`THERM BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plathermplablue_2000_175_c`|`PLA {color_name}`|`THERM PLA BLUE`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plathermblue_2000_175_c": "DFDFD3",
    "printwithsmile_pla_plathermplablue_2000_175_c": "0066cc"
  },
  "codes": {
    "printwithsmile_pla_plathermblue_2000_175_c": null,
    "printwithsmile_pla_plathermplablue_2000_175_c": [
      "545"
    ]
  },
  "eans": {
    "printwithsmile_pla_plathermblue_2000_175_c": null,
    "printwithsmile_pla_plathermplablue_2000_175_c": [
      "8594196455451"
    ]
  }
}
```

### PWS063: dup-0712b9748bef089ec815273a8c4ad88e99c75410754543b193854610fa0e95c0

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plathermplared_2500_175_c`|`PLA {color_name}`|`THERM PLA RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plathermred_2500_175_c`|`PLA {color_name}`|`THERM RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plathermplared_2500_175_c": "cc0000",
    "printwithsmile_pla_plathermred_2500_175_c": "FF7D7A"
  },
  "codes": {
    "printwithsmile_pla_plathermplared_2500_175_c": [
      "546"
    ],
    "printwithsmile_pla_plathermred_2500_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plathermplared_2500_175_c": [
      "8594196455468"
    ],
    "printwithsmile_pla_plathermred_2500_175_c": null
  }
}
```

### PWS064: dup-1a64c16956846a4f48b33f223b583a8cfa69a35ea4a57c4d6ae5e78064cd835a

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plathermplared_500_175_c`|`PLA {color_name}`|`THERM PLA RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plathermred_500_175_c`|`PLA {color_name}`|`THERM RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plathermplared_500_175_c": "cc0000",
    "printwithsmile_pla_plathermred_500_175_c": "FF7D7A"
  },
  "codes": {
    "printwithsmile_pla_plathermplared_500_175_c": [
      "546"
    ],
    "printwithsmile_pla_plathermred_500_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plathermplared_500_175_c": [
      "8594196455468"
    ],
    "printwithsmile_pla_plathermred_500_175_c": null
  }
}
```

### PWS065: dup-215c9c3d3ed30a04e7b946e2e4b1c29a473a22e80f4225b9700b83e22112204d

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plathermplared_750_175_c`|`PLA {color_name}`|`THERM PLA RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plathermred_750_175_c`|`PLA {color_name}`|`THERM RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plathermplared_750_175_c": "cc0000",
    "printwithsmile_pla_plathermred_750_175_c": "FF7D7A"
  },
  "codes": {
    "printwithsmile_pla_plathermplared_750_175_c": [
      "546"
    ],
    "printwithsmile_pla_plathermred_750_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plathermplared_750_175_c": [
      "8594196455468"
    ],
    "printwithsmile_pla_plathermred_750_175_c": null
  }
}
```

### PWS066: dup-580b82aca212365f386ddfddcaca92a3b2e48ad2b73b1f4bc82733cc3e59c92d

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plathermplared_2000_175_c`|`PLA {color_name}`|`THERM PLA RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plathermred_2000_175_c`|`PLA {color_name}`|`THERM RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plathermplared_2000_175_c": "cc0000",
    "printwithsmile_pla_plathermred_2000_175_c": "FF7D7A"
  },
  "codes": {
    "printwithsmile_pla_plathermplared_2000_175_c": [
      "546"
    ],
    "printwithsmile_pla_plathermred_2000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plathermplared_2000_175_c": [
      "8594196455468"
    ],
    "printwithsmile_pla_plathermred_2000_175_c": null
  }
}
```

### PWS067: dup-8544cc0421cadcff6e5af66c5ae9d8652651e7b3e7c170d70726975346661665

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plathermplared_5000_175_c`|`PLA {color_name}`|`THERM PLA RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plathermred_5000_175_c`|`PLA {color_name}`|`THERM RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plathermplared_5000_175_c": "cc0000",
    "printwithsmile_pla_plathermred_5000_175_c": "FF7D7A"
  },
  "codes": {
    "printwithsmile_pla_plathermplared_5000_175_c": [
      "546"
    ],
    "printwithsmile_pla_plathermred_5000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plathermplared_5000_175_c": [
      "8594196455468"
    ],
    "printwithsmile_pla_plathermred_5000_175_c": null
  }
}
```

### PWS068: dup-b88a471aa42c43937b4f240ff3b03f9b150ac3d8ef988c44c342a9e6f665da59

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`printwithsmile_pla_plathermplared_1000_175_c`|`PLA {color_name}`|`THERM PLA RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|
|`printwithsmile_pla_plathermred_1000_175_c`|`PLA {color_name}`|`THERM RED`|{"source_file": "printwithsmile.json", "definition_index": 8, "weights": 6, "diameters": 1, "colors": 87, "compiled_records": 522} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "printwithsmile_pla_plathermplared_1000_175_c": "cc0000",
    "printwithsmile_pla_plathermred_1000_175_c": "FF7D7A"
  },
  "codes": {
    "printwithsmile_pla_plathermplared_1000_175_c": [
      "546"
    ],
    "printwithsmile_pla_plathermred_1000_175_c": null
  },
  "eans": {
    "printwithsmile_pla_plathermplared_1000_175_c": [
      "8594196455468"
    ],
    "printwithsmile_pla_plathermred_1000_175_c": null
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

- `printwithsmile_abs_abscherryred_500_175_c` — ABS Cherry RED
- `printwithsmile_abs_abscobaltblue/modr_500_175_c` — ABS Cobalt BLUE/modrá
- `printwithsmile_abs_absgreen_500_175_c` — ABS GREEN
- `printwithsmile_abs_abslemondrop_500_175_c` — ABS Lemon DROP
- `printwithsmile_abs_abslightgreen_500_175_c` — ABS Light GREEN
- `printwithsmile_abs_absnaturalivory_500_175_c` — ABS NATURAL Ivory
- `printwithsmile_abs_abssatineblack_500_175_c` — ABS Satine Black
- `printwithsmile_abs_abssatinewhite_500_175_c` — ABS Satine White
- `printwithsmile_abs_abssilvershine_500_175_c` — ABS SILVER Shine
- `printwithsmile_abs_absskyblue_500_175_c` — ABS Sky BLUE
- `printwithsmile_abs_absyellow_500_175_c` — ABS YELLOW
- `printwithsmile_abs_absm-black_500_175_c` — ABS M- Black
- `printwithsmile_asa_asablackvolkano_850_175_c` — ASA BLACK volkano
- `printwithsmile_asa_asacherryred_850_175_c` — ASA CHERRY RED
- `printwithsmile_asa_asadarkblue_850_175_c` — ASA DARK BLUE
- `printwithsmile_asa_asadarkgrey_850_175_c` — ASA Dark GREY
- `printwithsmile_asa_asanatural_850_175_c` — ASA NATURAL
- `printwithsmile_asa_asaorange_850_175_c` — ASA ORANGE
- `printwithsmile_asa_asasivershine_850_175_c` — ASA SIVER SHINE
- `printwithsmile_asa_asawhite_850_175_c` — ASA WHITE
- `printwithsmile_asa_asaxxlblackvolkano_850_175_c` — ASA XXL BLACK Volkano
- `printwithsmile_asa_asayellow_850_175_c` — ASA YELLOW
- `printwithsmile_asa_asayellowgreen_850_175_c` — ASA Yellow GREEN
- `printwithsmile_asa_asakevlarblack_850_175_c` — ASA KEVLAR BLACK
- `printwithsmile_asa_asablackvolkano_2500_175_c` — ASA BLACK volkano
- `printwithsmile_asa_asacherryred_2500_175_c` — ASA CHERRY RED
- `printwithsmile_asa_asadarkblue_2500_175_c` — ASA DARK BLUE
- `printwithsmile_asa_asadarkgrey_2500_175_c` — ASA Dark GREY
- `printwithsmile_asa_asanatural_2500_175_c` — ASA NATURAL
- `printwithsmile_asa_asaorange_2500_175_c` — ASA ORANGE
- `printwithsmile_asa_asasivershine_2500_175_c` — ASA SIVER SHINE
- `printwithsmile_asa_asawhite_2500_175_c` — ASA WHITE
- `printwithsmile_asa_asaxxlblackvolkano_2500_175_c` — ASA XXL BLACK Volkano
- `printwithsmile_asa_asayellow_2500_175_c` — ASA YELLOW
- `printwithsmile_asa_asayellowgreen_2500_175_c` — ASA Yellow GREEN
- `printwithsmile_asa_asakevlarblack_2500_175_c` — ASA KEVLAR BLACK
- `printwithsmile_pla_biofilmattwhite_500_175_c` — BIOFIL Matt WHITE
- `printwithsmile_pla_biofilwood_500_175_c` — BIOFIL WOOD
- `printwithsmile_asa_compositeasakevlarblack_850_175_c` — COMPOSITE ASA KEVLAR BLACK
- `printwithsmile_pla_compositepa12cf15_500_175_c` — COMPOSITE PA12 CF15
- `printwithsmile_pla_compositeplauvhtc15_500_175_c` — COMPOSITE PLA UVHT C15
- `printwithsmile_pla_multicolordualsilkplablack/red_1000_175_c` — MULTICOLOR DUAL SILK PLA BLACK/RED
- `printwithsmile_pla_multicolordualsilkplablue/green_1000_175_c` — MULTICOLOR DUAL SILK PLA BLUE/GREEN
- `printwithsmile_pla_multicolordualsilkplablue/orange_1000_175_c` — MULTICOLOR DUAL SILK PLA BLUE/ORANGE
- `printwithsmile_pla_multicolordualsilkplablue/yellow_1000_175_c` — MULTICOLOR DUAL SILK PLA BLUE/YELLOW
- `printwithsmile_pla_multicolordualsilkplapurple/blue_1000_175_c` — MULTICOLOR DUAL SILK PLA PURPLE/BLUE
- `printwithsmile_pla_multicolordualsilkplarose/jade_1000_175_c` — MULTICOLOR DUAL SILK PLA ROSE/JADE
- `printwithsmile_pla_multicolordualsilkplawinter_1000_175_c` — MULTICOLOR DUAL SILK PLA WINTER
- `printwithsmile_pla_multicolorrainbowmatte_1000_175_c` — MULTICOLOR RAINBOW MATTE
- `printwithsmile_pla_multicolorsilkplapastelrainbow_1000_175_c` — MULTICOLOR SILK PLA PASTEL RAINBOW
- `printwithsmile_pla_multicolorsilkplarainbow_1000_175_c` — MULTICOLOR SILK PLA RAINBOW
- `printwithsmile_pla_multicolortriplesilkplablue/purple/yellow_1000_175_c` — MULTICOLOR TRIPLE SILK PLA BLUE/PURPLE/YELLOW
- `printwithsmile_pla_multicolortriplesilkplagold/green/black_1000_175_c` — MULTICOLOR TRIPLE SILK PLA GOLD/GREEN/BLACK
- `printwithsmile_pla_multicolortriplesilkplagold/green/fuchsia_1000_175_c` — MULTICOLOR TRIPLE SILK PLA GOLD/GREEN/FUCHSIA
- `printwithsmile_pla_multicolortriplesilkplared/gold/purple_1000_175_c` — MULTICOLOR TRIPLE SILK PLA RED/GOLD/PURPLE
- `printwithsmile_pla_multicolortriplesilkplarosered/green/blue_1000_175_c` — MULTICOLOR TRIPLE SILK PLA ROSE RED/GREEN/BLUE
- `printwithsmile_petg_petgbicolormetallicpetggreenbrown_750_175_c` — PETG BICOLOR METALLIC PET G GREEN BROWN
- `printwithsmile_petg_petgbicolormetallicpetgvioletsilver_750_175_c` — PETG BICOLOR METALLIC PET G VIOLET SILVER
- `printwithsmile_petg_petgbicolormetallicpetgvioletsparkle_750_175_c` — PETG BICOLOR METALLIC PET G VIOLET SPARKLE
- `printwithsmile_petg_petgpetgcolorchange_750_175_c` — PETG PET G COLOR CHANGE
- `printwithsmile_petg_petgrecpetgcolorchange_750_175_c` — PETG REC PET G COLOR CHANGE
- `printwithsmile_petg_petgxxlsatineblack_750_175_c` — PETG XXL Satine BLACK
- `printwithsmile_petg_petgxxlsatinewhite_750_175_c` — PETG XXL Satine WHITE
- `printwithsmile_petg_petganthracite_750_175_c` — PETG Anthracite
- `printwithsmile_petg_petgbluelagoon_750_175_c` — PETG Blue Lagoon
- `printwithsmile_petg_petgbrightorange_750_175_c` — PETG Bright Orange
- `printwithsmile_petg_petgchocoladebrown_750_175_c` — PETG Chocolade BROWN
- `printwithsmile_petg_petgcobaltblue_750_175_c` — PETG Cobalt BLUE
- `printwithsmile_petg_petgcyanblue_750_175_c` — PETG CYAN Blue
- `printwithsmile_petg_petggoldshine_750_175_c` — PETG GOLD Shine
- `printwithsmile_petg_petggreen_750_175_c` — PETG GREEN
- `printwithsmile_petg_petggreenbottle_750_175_c` — PETG GREEN Bottle
- `printwithsmile_petg_petggreenfield_750_175_c` — PETG GREEN Field
- `printwithsmile_petg_petggrey_750_175_c` — PETG GREY
- `printwithsmile_petg_petglightgrey_750_175_c` — PETG Light Grey
- `printwithsmile_petg_petgmarble_750_175_c` — PETG MARBLE
- `printwithsmile_petg_petgmetallicblue_750_175_c` — PETG Metallic BLUE
- `printwithsmile_petg_petgnatural_750_175_c` — PETG Natural
- `printwithsmile_petg_petgneonred_750_175_c` — PETG Neon RED
- `printwithsmile_petg_petgneonyellow_750_175_c` — PETG Neon YELLOW
- `printwithsmile_petg_petgorange_750_175_c` — PETG Orange
- `printwithsmile_petg_petgorangeglass_750_175_c` — PETG Orange Glass
- `printwithsmile_petg_petgraspberrypink_750_175_c` — PETG Raspberry PINK
- `printwithsmile_petg_petgred_750_175_c` — PETG RED
- `printwithsmile_petg_petgrubinred_750_175_c` — PETG Rubin RED
- `printwithsmile_petg_petgsatineblack_750_175_c` — PETG Satine Black
- `printwithsmile_petg_petgsatinewhite_750_175_c` — PETG Satine white
- `printwithsmile_petg_petgsilvershine_750_175_c` — PETG Silver Shine
- `printwithsmile_petg_petgv0white_750_175_c` — PETG V0 WHITE
- `printwithsmile_petg_petgvioletglass_750_175_c` — PETG Violet Glass
- `printwithsmile_petg_petgyellow_750_175_c` — PETG Yellow
- `printwithsmile_petg_petgyellowglass_750_175_c` — PETG Yellow Glass
- `printwithsmile_petg_petgbicolormetallicpetggreenbrown_1000_175_c` — PETG BICOLOR METALLIC PET G GREEN BROWN
- `printwithsmile_petg_petgbicolormetallicpetgvioletsilver_1000_175_c` — PETG BICOLOR METALLIC PET G VIOLET SILVER
- `printwithsmile_petg_petgbicolormetallicpetgvioletsparkle_1000_175_c` — PETG BICOLOR METALLIC PET G VIOLET SPARKLE
- `printwithsmile_petg_petgpetgcolorchange_1000_175_c` — PETG PET G COLOR CHANGE
- `printwithsmile_petg_petgrecpetgcolorchange_1000_175_c` — PETG REC PET G COLOR CHANGE
- `printwithsmile_petg_petgxxlsatineblack_1000_175_c` — PETG XXL Satine BLACK
- `printwithsmile_petg_petgxxlsatinewhite_1000_175_c` — PETG XXL Satine WHITE
- `printwithsmile_petg_petganthracite_1000_175_c` — PETG Anthracite
- `printwithsmile_petg_petgbluelagoon_1000_175_c` — PETG Blue Lagoon
- `printwithsmile_petg_petgbrightorange_1000_175_c` — PETG Bright Orange
- `printwithsmile_petg_petgchocoladebrown_1000_175_c` — PETG Chocolade BROWN
- `printwithsmile_petg_petgcobaltblue_1000_175_c` — PETG Cobalt BLUE
- `printwithsmile_petg_petgcyanblue_1000_175_c` — PETG CYAN Blue
- `printwithsmile_petg_petggoldshine_1000_175_c` — PETG GOLD Shine
- `printwithsmile_petg_petggreen_1000_175_c` — PETG GREEN
- `printwithsmile_petg_petggreenbottle_1000_175_c` — PETG GREEN Bottle
- `printwithsmile_petg_petggreenfield_1000_175_c` — PETG GREEN Field
- `printwithsmile_petg_petggrey_1000_175_c` — PETG GREY
- `printwithsmile_petg_petglightgrey_1000_175_c` — PETG Light Grey
- `printwithsmile_petg_petgmarble_1000_175_c` — PETG MARBLE
- `printwithsmile_petg_petgmetallicblue_1000_175_c` — PETG Metallic BLUE
- `printwithsmile_petg_petgnatural_1000_175_c` — PETG Natural
- `printwithsmile_petg_petgneonred_1000_175_c` — PETG Neon RED
- `printwithsmile_petg_petgneonyellow_1000_175_c` — PETG Neon YELLOW
- `printwithsmile_petg_petgorange_1000_175_c` — PETG Orange
- `printwithsmile_petg_petgorangeglass_1000_175_c` — PETG Orange Glass
- `printwithsmile_petg_petgraspberrypink_1000_175_c` — PETG Raspberry PINK
- `printwithsmile_petg_petgred_1000_175_c` — PETG RED
- `printwithsmile_petg_petgrubinred_1000_175_c` — PETG Rubin RED
- `printwithsmile_petg_petgsatineblack_1000_175_c` — PETG Satine Black
- `printwithsmile_petg_petgsatinewhite_1000_175_c` — PETG Satine white
- `printwithsmile_petg_petgsilvershine_1000_175_c` — PETG Silver Shine
- `printwithsmile_petg_petgv0white_1000_175_c` — PETG V0 WHITE
- `printwithsmile_petg_petgvioletglass_1000_175_c` — PETG Violet Glass
- `printwithsmile_petg_petgyellow_1000_175_c` — PETG Yellow
- `printwithsmile_petg_petgyellowglass_1000_175_c` — PETG Yellow Glass
- `printwithsmile_petg_petgbicolormetallicpetggreenbrown_2500_175_c` — PETG BICOLOR METALLIC PET G GREEN BROWN
- `printwithsmile_petg_petgbicolormetallicpetgvioletsilver_2500_175_c` — PETG BICOLOR METALLIC PET G VIOLET SILVER
- `printwithsmile_petg_petgbicolormetallicpetgvioletsparkle_2500_175_c` — PETG BICOLOR METALLIC PET G VIOLET SPARKLE
- `printwithsmile_petg_petgpetgcolorchange_2500_175_c` — PETG PET G COLOR CHANGE
- `printwithsmile_petg_petgrecpetgcolorchange_2500_175_c` — PETG REC PET G COLOR CHANGE
- `printwithsmile_petg_petgxxlsatineblack_2500_175_c` — PETG XXL Satine BLACK
- `printwithsmile_petg_petgxxlsatinewhite_2500_175_c` — PETG XXL Satine WHITE
- `printwithsmile_petg_petganthracite_2500_175_c` — PETG Anthracite
- `printwithsmile_petg_petgbluelagoon_2500_175_c` — PETG Blue Lagoon
- `printwithsmile_petg_petgbrightorange_2500_175_c` — PETG Bright Orange
- `printwithsmile_petg_petgchocoladebrown_2500_175_c` — PETG Chocolade BROWN
- `printwithsmile_petg_petgcobaltblue_2500_175_c` — PETG Cobalt BLUE
- `printwithsmile_petg_petgcyanblue_2500_175_c` — PETG CYAN Blue
- `printwithsmile_petg_petggoldshine_2500_175_c` — PETG GOLD Shine
- `printwithsmile_petg_petggreen_2500_175_c` — PETG GREEN
- `printwithsmile_petg_petggreenbottle_2500_175_c` — PETG GREEN Bottle
- `printwithsmile_petg_petggreenfield_2500_175_c` — PETG GREEN Field
- `printwithsmile_petg_petggrey_2500_175_c` — PETG GREY
- `printwithsmile_petg_petglightgrey_2500_175_c` — PETG Light Grey
- `printwithsmile_petg_petgmarble_2500_175_c` — PETG MARBLE
- `printwithsmile_petg_petgmetallicblue_2500_175_c` — PETG Metallic BLUE
- `printwithsmile_petg_petgnatural_2500_175_c` — PETG Natural
- `printwithsmile_petg_petgneonred_2500_175_c` — PETG Neon RED
- `printwithsmile_petg_petgneonyellow_2500_175_c` — PETG Neon YELLOW
- `printwithsmile_petg_petgorange_2500_175_c` — PETG Orange
- `printwithsmile_petg_petgorangeglass_2500_175_c` — PETG Orange Glass
- `printwithsmile_petg_petgraspberrypink_2500_175_c` — PETG Raspberry PINK
- `printwithsmile_petg_petgred_2500_175_c` — PETG RED
- `printwithsmile_petg_petgrubinred_2500_175_c` — PETG Rubin RED
- `printwithsmile_petg_petgsatineblack_2500_175_c` — PETG Satine Black
- `printwithsmile_petg_petgsatinewhite_2500_175_c` — PETG Satine white
- `printwithsmile_petg_petgsilvershine_2500_175_c` — PETG Silver Shine
- `printwithsmile_petg_petgv0white_2500_175_c` — PETG V0 WHITE
- `printwithsmile_petg_petgvioletglass_2500_175_c` — PETG Violet Glass
- `printwithsmile_petg_petgyellow_2500_175_c` — PETG Yellow
- `printwithsmile_petg_petgyellowglass_2500_175_c` — PETG Yellow Glass
- `printwithsmile_petg_petgbicolormetallicpetggreenbrown_3000_175_c` — PETG BICOLOR METALLIC PET G GREEN BROWN
- `printwithsmile_petg_petgbicolormetallicpetgvioletsilver_3000_175_c` — PETG BICOLOR METALLIC PET G VIOLET SILVER
- `printwithsmile_petg_petgbicolormetallicpetgvioletsparkle_3000_175_c` — PETG BICOLOR METALLIC PET G VIOLET SPARKLE
- `printwithsmile_petg_petgpetgcolorchange_3000_175_c` — PETG PET G COLOR CHANGE
- `printwithsmile_petg_petgrecpetgcolorchange_3000_175_c` — PETG REC PET G COLOR CHANGE
- `printwithsmile_petg_petgxxlsatineblack_3000_175_c` — PETG XXL Satine BLACK
- `printwithsmile_petg_petgxxlsatinewhite_3000_175_c` — PETG XXL Satine WHITE
- `printwithsmile_petg_petganthracite_3000_175_c` — PETG Anthracite
- `printwithsmile_petg_petgbluelagoon_3000_175_c` — PETG Blue Lagoon
- `printwithsmile_petg_petgbrightorange_3000_175_c` — PETG Bright Orange
- `printwithsmile_petg_petgchocoladebrown_3000_175_c` — PETG Chocolade BROWN
- `printwithsmile_petg_petgcobaltblue_3000_175_c` — PETG Cobalt BLUE
- `printwithsmile_petg_petgcyanblue_3000_175_c` — PETG CYAN Blue
- `printwithsmile_petg_petggoldshine_3000_175_c` — PETG GOLD Shine
- `printwithsmile_petg_petggreen_3000_175_c` — PETG GREEN
- `printwithsmile_petg_petggreenbottle_3000_175_c` — PETG GREEN Bottle
- `printwithsmile_petg_petggreenfield_3000_175_c` — PETG GREEN Field
- `printwithsmile_petg_petggrey_3000_175_c` — PETG GREY
- `printwithsmile_petg_petglightgrey_3000_175_c` — PETG Light Grey
- `printwithsmile_petg_petgmarble_3000_175_c` — PETG MARBLE
- `printwithsmile_petg_petgmetallicblue_3000_175_c` — PETG Metallic BLUE
- `printwithsmile_petg_petgnatural_3000_175_c` — PETG Natural
- `printwithsmile_petg_petgneonred_3000_175_c` — PETG Neon RED
- `printwithsmile_petg_petgneonyellow_3000_175_c` — PETG Neon YELLOW
- `printwithsmile_petg_petgorange_3000_175_c` — PETG Orange
- `printwithsmile_petg_petgorangeglass_3000_175_c` — PETG Orange Glass
- `printwithsmile_petg_petgraspberrypink_3000_175_c` — PETG Raspberry PINK
- `printwithsmile_petg_petgred_3000_175_c` — PETG RED
- `printwithsmile_petg_petgrubinred_3000_175_c` — PETG Rubin RED
- `printwithsmile_petg_petgsatineblack_3000_175_c` — PETG Satine Black
- `printwithsmile_petg_petgsatinewhite_3000_175_c` — PETG Satine white
- `printwithsmile_petg_petgsilvershine_3000_175_c` — PETG Silver Shine
- `printwithsmile_petg_petgv0white_3000_175_c` — PETG V0 WHITE
- `printwithsmile_petg_petgvioletglass_3000_175_c` — PETG Violet Glass
- `printwithsmile_petg_petgyellow_3000_175_c` — PETG Yellow
- `printwithsmile_petg_petgyellowglass_3000_175_c` — PETG Yellow Glass
- `printwithsmile_pla_pla5xlblack_500_175_c` — PLA 5XL BLACK
- `printwithsmile_pla_pla5xlwhite_500_175_c` — PLA 5XL WHITE
- `printwithsmile_pla_plablack_500_175_c` — PLA Black
- `printwithsmile_pla_plablackstar_500_175_c` — PLA BLACK STAR
- `printwithsmile_pla_plachocoladeshine_500_175_c` — PLA Chocolade Shine
- `printwithsmile_pla_placloudygrey_500_175_c` — PLA Cloudy Grey
- `printwithsmile_pla_placobaltblue_500_175_c` — PLA Cobalt BLUE
- `printwithsmile_pla_placopperbrown_500_175_c` — PLA Copper BROWN
- `printwithsmile_pla_placoralpink_500_175_c` — PLA Coral PINK
- `printwithsmile_pla_placreamy_500_175_c` — PLA Creamy
- `printwithsmile_pla_pladarkgreen_500_175_c` — PLA Dark GREEN
- `printwithsmile_pla_plaecotyrkys_500_175_c` — PLA Eco TYRKYS
- `printwithsmile_pla_plafreshmint_500_175_c` — PLA Fresh MINT
- `printwithsmile_pla_plagreen_500_175_c` — PLA GREEN
- `printwithsmile_pla_plagreenapple_500_175_c` — PLA GREEN Apple
- `printwithsmile_pla_plagrey_500_175_c` — PLA Grey
- `printwithsmile_pla_plajustblue_500_175_c` — PLA Just BLUE
- `printwithsmile_pla_plajustbrown_500_175_c` — PLA Just BROWN
- `printwithsmile_pla_plajustgrey_500_175_c` — PLA Just GREY
- `printwithsmile_pla_plajustred_500_175_c` — PLA Just RED
- `printwithsmile_pla_plajustyellow_500_175_c` — PLA Just YELLOW
- `printwithsmile_pla_plalemondrop_500_175_c` — PLA Lemon Drop
- `printwithsmile_pla_plalightgreen_500_175_c` — PLA Light GREEN
- `printwithsmile_pla_plalowgrey_500_175_c` — PLA Low GREY
- `printwithsmile_pla_plamarblebright_500_175_c` — PLA MARBLE Bright
- `printwithsmile_pla_plamaygreen_500_175_c` — PLA May GREEN
- `printwithsmile_pla_plamayablue_500_175_c` — PLA Maya BLUE
- `printwithsmile_pla_plametallicblue_500_175_c` — PLA Metallic BLUE
- `printwithsmile_pla_plametallicgreen_500_175_c` — PLA Metallic GREEN
- `printwithsmile_pla_planatural_500_175_c` — PLA Natural
- `printwithsmile_pla_plaorange_500_175_c` — PLA Orange
- `printwithsmile_pla_plapastelblue_500_175_c` — PLA Pastel BLUE
- `printwithsmile_pla_plapumkinorange_500_175_c` — PLA Pumkin ORANGE
- `printwithsmile_pla_plapurple_500_175_c` — PLA Purple
- `printwithsmile_pla_plarubinred_500_175_c` — PLA Rubin RED
- `printwithsmile_pla_plasilkplacopper_500_175_c` — PLA SILK PLA COPPER
- `printwithsmile_pla_plasilkplaoldgold_500_175_c` — PLA SILK PLA OLD GOLD
- `printwithsmile_pla_plasilver_500_175_c` — PLA Silver
- `printwithsmile_pla_plasunsetgold_500_175_c` — PLA Sunset GOLD
- `printwithsmile_pla_platurquoiseblue_500_175_c` — PLA Turquoise BLUE
- `printwithsmile_pla_plawhite_500_175_c` — PLA White
- `printwithsmile_pla_plaxxlblack_500_175_c` — PLA XXL BLACK
- `printwithsmile_pla_plaxxljustblack_500_175_c` — PLA XXL Just BLACK
- `printwithsmile_pla_plaxxljustwhite_500_175_c` — PLA XXL Just WHITE
- `printwithsmile_pla_plaxxlwhite_500_175_c` — PLA XXL WHITE
- `printwithsmile_pla_playellow_500_175_c` — PLA Yellow
- `printwithsmile_pla_plaebenwood_500_175_c` — PLA EBEN Wood
- `printwithsmile_pla_plamahagonwood_500_175_c` — PLA MAHAGON Wood
- `printwithsmile_pla_plarec-ecotyrkys_500_175_c` — PLA REC- Eco TYRKYS
- `printwithsmile_pla_plarec-huntergreen_500_175_c` — PLA REC- Hunter GREEN
- `printwithsmile_pla_plarec-justblack_500_175_c` — PLA REC- Just BLACK
- `printwithsmile_pla_plarec-justblue_500_175_c` — PLA REC- Just BLUE
- `printwithsmile_pla_plarec-justbrown_500_175_c` — PLA REC- Just BROWN
- `printwithsmile_pla_plarec-justgrey_500_175_c` — PLA REC- Just GREY
- `printwithsmile_pla_plarec-justpurple_500_175_c` — PLA REC- Just PURPLE
- `printwithsmile_pla_plarec-justred_500_175_c` — PLA REC- Just RED
- `printwithsmile_pla_plarec-justwhite_500_175_c` — PLA REC- Just WHITE
- `printwithsmile_pla_plarec-justyellow_500_175_c` — PLA REC- Just YELLOW
- `printwithsmile_pla_plarec-lowgrey_500_175_c` — PLA REC- Low GREY
- `printwithsmile_pla_plarec-maygreen_500_175_c` — PLA REC- May GREEN
- `printwithsmile_pla_plarec-mayablue_500_175_c` — PLA REC- Maya BLUE
- `printwithsmile_pla_plarec-pumkinorange_500_175_c` — PLA REC- Pumkin ORANGE
- `printwithsmile_pla_plawhitewood_500_175_c` — PLA White Wood
- `printwithsmile_pla_plawood_500_175_c` — PLA Wood
- `printwithsmile_pla_pla5xlblack_750_175_c` — PLA 5XL BLACK
- `printwithsmile_pla_pla5xlwhite_750_175_c` — PLA 5XL WHITE
- `printwithsmile_pla_plablack_750_175_c` — PLA Black
- `printwithsmile_pla_plablackstar_750_175_c` — PLA BLACK STAR
- `printwithsmile_pla_plachocoladeshine_750_175_c` — PLA Chocolade Shine
- `printwithsmile_pla_placloudygrey_750_175_c` — PLA Cloudy Grey
- `printwithsmile_pla_placobaltblue_750_175_c` — PLA Cobalt BLUE
- `printwithsmile_pla_placopperbrown_750_175_c` — PLA Copper BROWN
- `printwithsmile_pla_placoralpink_750_175_c` — PLA Coral PINK
- `printwithsmile_pla_placreamy_750_175_c` — PLA Creamy
- `printwithsmile_pla_pladarkgreen_750_175_c` — PLA Dark GREEN
- `printwithsmile_pla_plaecotyrkys_750_175_c` — PLA Eco TYRKYS
- `printwithsmile_pla_plafreshmint_750_175_c` — PLA Fresh MINT
- `printwithsmile_pla_plagreen_750_175_c` — PLA GREEN
- `printwithsmile_pla_plagreenapple_750_175_c` — PLA GREEN Apple
- `printwithsmile_pla_plagrey_750_175_c` — PLA Grey
- `printwithsmile_pla_plajustblue_750_175_c` — PLA Just BLUE
- `printwithsmile_pla_plajustbrown_750_175_c` — PLA Just BROWN
- `printwithsmile_pla_plajustgrey_750_175_c` — PLA Just GREY
- `printwithsmile_pla_plajustred_750_175_c` — PLA Just RED
- `printwithsmile_pla_plajustyellow_750_175_c` — PLA Just YELLOW
- `printwithsmile_pla_plalemondrop_750_175_c` — PLA Lemon Drop
- `printwithsmile_pla_plalightgreen_750_175_c` — PLA Light GREEN
- `printwithsmile_pla_plalowgrey_750_175_c` — PLA Low GREY
- `printwithsmile_pla_plamarblebright_750_175_c` — PLA MARBLE Bright
- `printwithsmile_pla_plamaygreen_750_175_c` — PLA May GREEN
- `printwithsmile_pla_plamayablue_750_175_c` — PLA Maya BLUE
- `printwithsmile_pla_plametallicblue_750_175_c` — PLA Metallic BLUE
- `printwithsmile_pla_plametallicgreen_750_175_c` — PLA Metallic GREEN
- `printwithsmile_pla_planatural_750_175_c` — PLA Natural
- `printwithsmile_pla_plaorange_750_175_c` — PLA Orange
- `printwithsmile_pla_plapastelblue_750_175_c` — PLA Pastel BLUE
- `printwithsmile_pla_plapumkinorange_750_175_c` — PLA Pumkin ORANGE
- `printwithsmile_pla_plapurple_750_175_c` — PLA Purple
- `printwithsmile_pla_plarubinred_750_175_c` — PLA Rubin RED
- `printwithsmile_pla_plasilkplacopper_750_175_c` — PLA SILK PLA COPPER
- `printwithsmile_pla_plasilkplaoldgold_750_175_c` — PLA SILK PLA OLD GOLD
- `printwithsmile_pla_plasilver_750_175_c` — PLA Silver
- `printwithsmile_pla_plasunsetgold_750_175_c` — PLA Sunset GOLD
- `printwithsmile_pla_platurquoiseblue_750_175_c` — PLA Turquoise BLUE
- `printwithsmile_pla_plawhite_750_175_c` — PLA White
- `printwithsmile_pla_plaxxlblack_750_175_c` — PLA XXL BLACK
- `printwithsmile_pla_plaxxljustblack_750_175_c` — PLA XXL Just BLACK
- `printwithsmile_pla_plaxxljustwhite_750_175_c` — PLA XXL Just WHITE
- `printwithsmile_pla_plaxxlwhite_750_175_c` — PLA XXL WHITE
- `printwithsmile_pla_playellow_750_175_c` — PLA Yellow
- `printwithsmile_pla_plaebenwood_750_175_c` — PLA EBEN Wood
- `printwithsmile_pla_plahisnatural_750_175_c` — PLA HIS natural
- `printwithsmile_pla_plamahagonwood_750_175_c` — PLA MAHAGON Wood
- `printwithsmile_pla_plarec-ecotyrkys_750_175_c` — PLA REC- Eco TYRKYS
- `printwithsmile_pla_plarec-huntergreen_750_175_c` — PLA REC- Hunter GREEN
- `printwithsmile_pla_plarec-justblack_750_175_c` — PLA REC- Just BLACK
- `printwithsmile_pla_plarec-justblue_750_175_c` — PLA REC- Just BLUE
- `printwithsmile_pla_plarec-justbrown_750_175_c` — PLA REC- Just BROWN
- `printwithsmile_pla_plarec-justgrey_750_175_c` — PLA REC- Just GREY
- `printwithsmile_pla_plarec-justpurple_750_175_c` — PLA REC- Just PURPLE
- `printwithsmile_pla_plarec-justred_750_175_c` — PLA REC- Just RED
- `printwithsmile_pla_plarec-justwhite_750_175_c` — PLA REC- Just WHITE
- `printwithsmile_pla_plarec-justyellow_750_175_c` — PLA REC- Just YELLOW
- `printwithsmile_pla_plarec-lowgrey_750_175_c` — PLA REC- Low GREY
- `printwithsmile_pla_plarec-maygreen_750_175_c` — PLA REC- May GREEN
- `printwithsmile_pla_plarec-mayablue_750_175_c` — PLA REC- Maya BLUE
- `printwithsmile_pla_plarec-pumkinorange_750_175_c` — PLA REC- Pumkin ORANGE
- `printwithsmile_pla_plawhitewood_750_175_c` — PLA White Wood
- `printwithsmile_pla_plawood_750_175_c` — PLA Wood
- `printwithsmile_pla_pla5xlblack_1000_175_c` — PLA 5XL BLACK
- `printwithsmile_pla_pla5xlwhite_1000_175_c` — PLA 5XL WHITE
- `printwithsmile_pla_plablack_1000_175_c` — PLA Black
- `printwithsmile_pla_plablackstar_1000_175_c` — PLA BLACK STAR
- `printwithsmile_pla_plachocoladeshine_1000_175_c` — PLA Chocolade Shine
- `printwithsmile_pla_placloudygrey_1000_175_c` — PLA Cloudy Grey
- `printwithsmile_pla_placobaltblue_1000_175_c` — PLA Cobalt BLUE
- `printwithsmile_pla_placopperbrown_1000_175_c` — PLA Copper BROWN
- `printwithsmile_pla_placoralpink_1000_175_c` — PLA Coral PINK
- `printwithsmile_pla_placreamy_1000_175_c` — PLA Creamy
- `printwithsmile_pla_pladarkgreen_1000_175_c` — PLA Dark GREEN
- `printwithsmile_pla_plaecotyrkys_1000_175_c` — PLA Eco TYRKYS
- `printwithsmile_pla_plafreshmint_1000_175_c` — PLA Fresh MINT
- `printwithsmile_pla_plagreen_1000_175_c` — PLA GREEN
- `printwithsmile_pla_plagreenapple_1000_175_c` — PLA GREEN Apple
- `printwithsmile_pla_plagrey_1000_175_c` — PLA Grey
- `printwithsmile_pla_plajustblue_1000_175_c` — PLA Just BLUE
- `printwithsmile_pla_plajustbrown_1000_175_c` — PLA Just BROWN
- `printwithsmile_pla_plajustgrey_1000_175_c` — PLA Just GREY
- `printwithsmile_pla_plajustred_1000_175_c` — PLA Just RED
- `printwithsmile_pla_plajustyellow_1000_175_c` — PLA Just YELLOW
- `printwithsmile_pla_plalemondrop_1000_175_c` — PLA Lemon Drop
- `printwithsmile_pla_plalightgreen_1000_175_c` — PLA Light GREEN
- `printwithsmile_pla_plalowgrey_1000_175_c` — PLA Low GREY
- `printwithsmile_pla_plamarblebright_1000_175_c` — PLA MARBLE Bright
- `printwithsmile_pla_plamaygreen_1000_175_c` — PLA May GREEN
- `printwithsmile_pla_plamayablue_1000_175_c` — PLA Maya BLUE
- `printwithsmile_pla_plametallicblue_1000_175_c` — PLA Metallic BLUE
- `printwithsmile_pla_plametallicgreen_1000_175_c` — PLA Metallic GREEN
- `printwithsmile_pla_planatural_1000_175_c` — PLA Natural
- `printwithsmile_pla_plaorange_1000_175_c` — PLA Orange
- `printwithsmile_pla_plapastelblue_1000_175_c` — PLA Pastel BLUE
- `printwithsmile_pla_plapumkinorange_1000_175_c` — PLA Pumkin ORANGE
- `printwithsmile_pla_plapurple_1000_175_c` — PLA Purple
- `printwithsmile_pla_plarubinred_1000_175_c` — PLA Rubin RED
- `printwithsmile_pla_plasilkplacopper_1000_175_c` — PLA SILK PLA COPPER
- `printwithsmile_pla_plasilver_1000_175_c` — PLA Silver
- `printwithsmile_pla_plasunsetgold_1000_175_c` — PLA Sunset GOLD
- `printwithsmile_pla_platurquoiseblue_1000_175_c` — PLA Turquoise BLUE
- `printwithsmile_pla_plawhite_1000_175_c` — PLA White
- `printwithsmile_pla_plaxxlblack_1000_175_c` — PLA XXL BLACK
- `printwithsmile_pla_plaxxljustblack_1000_175_c` — PLA XXL Just BLACK
- `printwithsmile_pla_plaxxljustwhite_1000_175_c` — PLA XXL Just WHITE
- `printwithsmile_pla_plaxxlwhite_1000_175_c` — PLA XXL WHITE
- `printwithsmile_pla_playellow_1000_175_c` — PLA Yellow
- `printwithsmile_pla_plaebenwood_1000_175_c` — PLA EBEN Wood
- `printwithsmile_pla_plahisnatural_1000_175_c` — PLA HIS natural
- `printwithsmile_pla_plamahagonwood_1000_175_c` — PLA MAHAGON Wood
- `printwithsmile_pla_plarec-ecotyrkys_1000_175_c` — PLA REC- Eco TYRKYS
- `printwithsmile_pla_plarec-huntergreen_1000_175_c` — PLA REC- Hunter GREEN
- `printwithsmile_pla_plarec-justblack_1000_175_c` — PLA REC- Just BLACK
- `printwithsmile_pla_plarec-justblue_1000_175_c` — PLA REC- Just BLUE
- `printwithsmile_pla_plarec-justbrown_1000_175_c` — PLA REC- Just BROWN
- `printwithsmile_pla_plarec-justgrey_1000_175_c` — PLA REC- Just GREY
- `printwithsmile_pla_plarec-justpurple_1000_175_c` — PLA REC- Just PURPLE
- `printwithsmile_pla_plarec-justred_1000_175_c` — PLA REC- Just RED
- `printwithsmile_pla_plarec-justwhite_1000_175_c` — PLA REC- Just WHITE
- `printwithsmile_pla_plarec-justyellow_1000_175_c` — PLA REC- Just YELLOW
- `printwithsmile_pla_plarec-lowgrey_1000_175_c` — PLA REC- Low GREY
- `printwithsmile_pla_plarec-maygreen_1000_175_c` — PLA REC- May GREEN
- `printwithsmile_pla_plarec-mayablue_1000_175_c` — PLA REC- Maya BLUE
- `printwithsmile_pla_plarec-pumkinorange_1000_175_c` — PLA REC- Pumkin ORANGE
- `printwithsmile_pla_plawhitewood_1000_175_c` — PLA White Wood
- `printwithsmile_pla_plawood_1000_175_c` — PLA Wood
- `printwithsmile_pla_pla5xlblack_2000_175_c` — PLA 5XL BLACK
- `printwithsmile_pla_pla5xlwhite_2000_175_c` — PLA 5XL WHITE
- `printwithsmile_pla_plablack_2000_175_c` — PLA Black
- `printwithsmile_pla_plablackstar_2000_175_c` — PLA BLACK STAR
- `printwithsmile_pla_plachocoladeshine_2000_175_c` — PLA Chocolade Shine
- `printwithsmile_pla_placloudygrey_2000_175_c` — PLA Cloudy Grey
- `printwithsmile_pla_placobaltblue_2000_175_c` — PLA Cobalt BLUE
- `printwithsmile_pla_placopperbrown_2000_175_c` — PLA Copper BROWN
- `printwithsmile_pla_placoralpink_2000_175_c` — PLA Coral PINK
- `printwithsmile_pla_placreamy_2000_175_c` — PLA Creamy
- `printwithsmile_pla_pladarkgreen_2000_175_c` — PLA Dark GREEN
- `printwithsmile_pla_plaecotyrkys_2000_175_c` — PLA Eco TYRKYS
- `printwithsmile_pla_plafreshmint_2000_175_c` — PLA Fresh MINT
- `printwithsmile_pla_plagreen_2000_175_c` — PLA GREEN
- `printwithsmile_pla_plagreenapple_2000_175_c` — PLA GREEN Apple
- `printwithsmile_pla_plagrey_2000_175_c` — PLA Grey
- `printwithsmile_pla_plajustblue_2000_175_c` — PLA Just BLUE
- `printwithsmile_pla_plajustbrown_2000_175_c` — PLA Just BROWN
- `printwithsmile_pla_plajustgrey_2000_175_c` — PLA Just GREY
- `printwithsmile_pla_plajustred_2000_175_c` — PLA Just RED
- `printwithsmile_pla_plajustyellow_2000_175_c` — PLA Just YELLOW
- `printwithsmile_pla_plalemondrop_2000_175_c` — PLA Lemon Drop
- `printwithsmile_pla_plalightgreen_2000_175_c` — PLA Light GREEN
- `printwithsmile_pla_plalowgrey_2000_175_c` — PLA Low GREY
- `printwithsmile_pla_plamarblebright_2000_175_c` — PLA MARBLE Bright
- `printwithsmile_pla_plamaygreen_2000_175_c` — PLA May GREEN
- `printwithsmile_pla_plamayablue_2000_175_c` — PLA Maya BLUE
- `printwithsmile_pla_plametallicblue_2000_175_c` — PLA Metallic BLUE
- `printwithsmile_pla_plametallicgreen_2000_175_c` — PLA Metallic GREEN
- `printwithsmile_pla_planatural_2000_175_c` — PLA Natural
- `printwithsmile_pla_plaorange_2000_175_c` — PLA Orange
- `printwithsmile_pla_plapastelblue_2000_175_c` — PLA Pastel BLUE
- `printwithsmile_pla_plapumkinorange_2000_175_c` — PLA Pumkin ORANGE
- `printwithsmile_pla_plapurple_2000_175_c` — PLA Purple
- `printwithsmile_pla_plarubinred_2000_175_c` — PLA Rubin RED
- `printwithsmile_pla_plasilkplacopper_2000_175_c` — PLA SILK PLA COPPER
- `printwithsmile_pla_plasilkplaoldgold_2000_175_c` — PLA SILK PLA OLD GOLD
- `printwithsmile_pla_plasilver_2000_175_c` — PLA Silver
- `printwithsmile_pla_plasunsetgold_2000_175_c` — PLA Sunset GOLD
- `printwithsmile_pla_platurquoiseblue_2000_175_c` — PLA Turquoise BLUE
- `printwithsmile_pla_plawhite_2000_175_c` — PLA White
- `printwithsmile_pla_plaxxlblack_2000_175_c` — PLA XXL BLACK
- `printwithsmile_pla_plaxxljustblack_2000_175_c` — PLA XXL Just BLACK
- `printwithsmile_pla_plaxxljustwhite_2000_175_c` — PLA XXL Just WHITE
- `printwithsmile_pla_plaxxlwhite_2000_175_c` — PLA XXL WHITE
- `printwithsmile_pla_playellow_2000_175_c` — PLA Yellow
- `printwithsmile_pla_plaebenwood_2000_175_c` — PLA EBEN Wood
- `printwithsmile_pla_plahisnatural_2000_175_c` — PLA HIS natural
- `printwithsmile_pla_plamahagonwood_2000_175_c` — PLA MAHAGON Wood
- `printwithsmile_pla_plarec-ecotyrkys_2000_175_c` — PLA REC- Eco TYRKYS
- `printwithsmile_pla_plarec-huntergreen_2000_175_c` — PLA REC- Hunter GREEN
- `printwithsmile_pla_plarec-justblack_2000_175_c` — PLA REC- Just BLACK
- `printwithsmile_pla_plarec-justblue_2000_175_c` — PLA REC- Just BLUE
- `printwithsmile_pla_plarec-justbrown_2000_175_c` — PLA REC- Just BROWN
- `printwithsmile_pla_plarec-justgrey_2000_175_c` — PLA REC- Just GREY
- `printwithsmile_pla_plarec-justpurple_2000_175_c` — PLA REC- Just PURPLE
- `printwithsmile_pla_plarec-justred_2000_175_c` — PLA REC- Just RED
- `printwithsmile_pla_plarec-justwhite_2000_175_c` — PLA REC- Just WHITE
- `printwithsmile_pla_plarec-justyellow_2000_175_c` — PLA REC- Just YELLOW
- `printwithsmile_pla_plarec-lowgrey_2000_175_c` — PLA REC- Low GREY
- `printwithsmile_pla_plarec-maygreen_2000_175_c` — PLA REC- May GREEN
- `printwithsmile_pla_plarec-mayablue_2000_175_c` — PLA REC- Maya BLUE
- `printwithsmile_pla_plarec-pumkinorange_2000_175_c` — PLA REC- Pumkin ORANGE
- `printwithsmile_pla_plawhitewood_2000_175_c` — PLA White Wood
- `printwithsmile_pla_plawood_2000_175_c` — PLA Wood
- `printwithsmile_pla_pla5xlblack_2500_175_c` — PLA 5XL BLACK
- `printwithsmile_pla_pla5xlwhite_2500_175_c` — PLA 5XL WHITE
- `printwithsmile_pla_plablack_2500_175_c` — PLA Black
- `printwithsmile_pla_plablackstar_2500_175_c` — PLA BLACK STAR
- `printwithsmile_pla_plachocoladeshine_2500_175_c` — PLA Chocolade Shine
- `printwithsmile_pla_placloudygrey_2500_175_c` — PLA Cloudy Grey
- `printwithsmile_pla_placobaltblue_2500_175_c` — PLA Cobalt BLUE
- `printwithsmile_pla_placopperbrown_2500_175_c` — PLA Copper BROWN
- `printwithsmile_pla_placoralpink_2500_175_c` — PLA Coral PINK
- `printwithsmile_pla_placreamy_2500_175_c` — PLA Creamy
- `printwithsmile_pla_pladarkgreen_2500_175_c` — PLA Dark GREEN
- `printwithsmile_pla_plaecotyrkys_2500_175_c` — PLA Eco TYRKYS
- `printwithsmile_pla_plafreshmint_2500_175_c` — PLA Fresh MINT
- `printwithsmile_pla_plagreen_2500_175_c` — PLA GREEN
- `printwithsmile_pla_plagreenapple_2500_175_c` — PLA GREEN Apple
- `printwithsmile_pla_plagrey_2500_175_c` — PLA Grey
- `printwithsmile_pla_plajustblue_2500_175_c` — PLA Just BLUE
- `printwithsmile_pla_plajustbrown_2500_175_c` — PLA Just BROWN
- `printwithsmile_pla_plajustgrey_2500_175_c` — PLA Just GREY
- `printwithsmile_pla_plajustred_2500_175_c` — PLA Just RED
- `printwithsmile_pla_plajustyellow_2500_175_c` — PLA Just YELLOW
- `printwithsmile_pla_plalemondrop_2500_175_c` — PLA Lemon Drop
- `printwithsmile_pla_plalightgreen_2500_175_c` — PLA Light GREEN
- `printwithsmile_pla_plalowgrey_2500_175_c` — PLA Low GREY
- `printwithsmile_pla_plamarblebright_2500_175_c` — PLA MARBLE Bright
- `printwithsmile_pla_plamaygreen_2500_175_c` — PLA May GREEN
- `printwithsmile_pla_plamayablue_2500_175_c` — PLA Maya BLUE
- `printwithsmile_pla_plametallicblue_2500_175_c` — PLA Metallic BLUE
- `printwithsmile_pla_plametallicgreen_2500_175_c` — PLA Metallic GREEN
- `printwithsmile_pla_planatural_2500_175_c` — PLA Natural
- `printwithsmile_pla_plaorange_2500_175_c` — PLA Orange
- `printwithsmile_pla_plapastelblue_2500_175_c` — PLA Pastel BLUE
- `printwithsmile_pla_plapumkinorange_2500_175_c` — PLA Pumkin ORANGE
- `printwithsmile_pla_plapurple_2500_175_c` — PLA Purple
- `printwithsmile_pla_plarubinred_2500_175_c` — PLA Rubin RED
- `printwithsmile_pla_plasilkplacopper_2500_175_c` — PLA SILK PLA COPPER
- `printwithsmile_pla_plasilkplaoldgold_2500_175_c` — PLA SILK PLA OLD GOLD
- `printwithsmile_pla_plasilver_2500_175_c` — PLA Silver
- `printwithsmile_pla_plasunsetgold_2500_175_c` — PLA Sunset GOLD
- `printwithsmile_pla_platurquoiseblue_2500_175_c` — PLA Turquoise BLUE
- `printwithsmile_pla_plawhite_2500_175_c` — PLA White
- `printwithsmile_pla_plaxxlblack_2500_175_c` — PLA XXL BLACK
- `printwithsmile_pla_plaxxljustblack_2500_175_c` — PLA XXL Just BLACK
- `printwithsmile_pla_plaxxljustwhite_2500_175_c` — PLA XXL Just WHITE
- `printwithsmile_pla_plaxxlwhite_2500_175_c` — PLA XXL WHITE
- `printwithsmile_pla_playellow_2500_175_c` — PLA Yellow
- `printwithsmile_pla_plaebenwood_2500_175_c` — PLA EBEN Wood
- `printwithsmile_pla_plahisnatural_2500_175_c` — PLA HIS natural
- `printwithsmile_pla_plamahagonwood_2500_175_c` — PLA MAHAGON Wood
- `printwithsmile_pla_plarec-ecotyrkys_2500_175_c` — PLA REC- Eco TYRKYS
- `printwithsmile_pla_plarec-huntergreen_2500_175_c` — PLA REC- Hunter GREEN
- `printwithsmile_pla_plarec-justblack_2500_175_c` — PLA REC- Just BLACK
- `printwithsmile_pla_plarec-justblue_2500_175_c` — PLA REC- Just BLUE
- `printwithsmile_pla_plarec-justbrown_2500_175_c` — PLA REC- Just BROWN
- `printwithsmile_pla_plarec-justgrey_2500_175_c` — PLA REC- Just GREY
- `printwithsmile_pla_plarec-justpurple_2500_175_c` — PLA REC- Just PURPLE
- `printwithsmile_pla_plarec-justred_2500_175_c` — PLA REC- Just RED
- `printwithsmile_pla_plarec-justwhite_2500_175_c` — PLA REC- Just WHITE
- `printwithsmile_pla_plarec-justyellow_2500_175_c` — PLA REC- Just YELLOW
- `printwithsmile_pla_plarec-lowgrey_2500_175_c` — PLA REC- Low GREY
- `printwithsmile_pla_plarec-maygreen_2500_175_c` — PLA REC- May GREEN
- `printwithsmile_pla_plarec-mayablue_2500_175_c` — PLA REC- Maya BLUE
- `printwithsmile_pla_plarec-pumkinorange_2500_175_c` — PLA REC- Pumkin ORANGE
- `printwithsmile_pla_plawhitewood_2500_175_c` — PLA White Wood
- `printwithsmile_pla_plawood_2500_175_c` — PLA Wood
- `printwithsmile_pla_pla5xlblack_5000_175_c` — PLA 5XL BLACK
- `printwithsmile_pla_pla5xlwhite_5000_175_c` — PLA 5XL WHITE
- `printwithsmile_pla_plablack_5000_175_c` — PLA Black
- `printwithsmile_pla_plablackstar_5000_175_c` — PLA BLACK STAR
- `printwithsmile_pla_plachocoladeshine_5000_175_c` — PLA Chocolade Shine
- `printwithsmile_pla_placloudygrey_5000_175_c` — PLA Cloudy Grey
- `printwithsmile_pla_placobaltblue_5000_175_c` — PLA Cobalt BLUE
- `printwithsmile_pla_placopperbrown_5000_175_c` — PLA Copper BROWN
- `printwithsmile_pla_placoralpink_5000_175_c` — PLA Coral PINK
- `printwithsmile_pla_placreamy_5000_175_c` — PLA Creamy
- `printwithsmile_pla_pladarkgreen_5000_175_c` — PLA Dark GREEN
- `printwithsmile_pla_plaecotyrkys_5000_175_c` — PLA Eco TYRKYS
- `printwithsmile_pla_plafreshmint_5000_175_c` — PLA Fresh MINT
- `printwithsmile_pla_plagreen_5000_175_c` — PLA GREEN
- `printwithsmile_pla_plagreenapple_5000_175_c` — PLA GREEN Apple
- `printwithsmile_pla_plagrey_5000_175_c` — PLA Grey
- `printwithsmile_pla_plajustblue_5000_175_c` — PLA Just BLUE
- `printwithsmile_pla_plajustbrown_5000_175_c` — PLA Just BROWN
- `printwithsmile_pla_plajustgrey_5000_175_c` — PLA Just GREY
- `printwithsmile_pla_plajustred_5000_175_c` — PLA Just RED
- `printwithsmile_pla_plajustyellow_5000_175_c` — PLA Just YELLOW
- `printwithsmile_pla_plalemondrop_5000_175_c` — PLA Lemon Drop
- `printwithsmile_pla_plalightgreen_5000_175_c` — PLA Light GREEN
- `printwithsmile_pla_plalowgrey_5000_175_c` — PLA Low GREY
- `printwithsmile_pla_plamarblebright_5000_175_c` — PLA MARBLE Bright
- `printwithsmile_pla_plamaygreen_5000_175_c` — PLA May GREEN
- `printwithsmile_pla_plamayablue_5000_175_c` — PLA Maya BLUE
- `printwithsmile_pla_plametallicblue_5000_175_c` — PLA Metallic BLUE
- `printwithsmile_pla_plametallicgreen_5000_175_c` — PLA Metallic GREEN
- `printwithsmile_pla_planatural_5000_175_c` — PLA Natural
- `printwithsmile_pla_plaorange_5000_175_c` — PLA Orange
- `printwithsmile_pla_plapastelblue_5000_175_c` — PLA Pastel BLUE
- `printwithsmile_pla_plapumkinorange_5000_175_c` — PLA Pumkin ORANGE
- `printwithsmile_pla_plapurple_5000_175_c` — PLA Purple
- `printwithsmile_pla_plarubinred_5000_175_c` — PLA Rubin RED
- `printwithsmile_pla_plasilkplacopper_5000_175_c` — PLA SILK PLA COPPER
- `printwithsmile_pla_plasilkplaoldgold_5000_175_c` — PLA SILK PLA OLD GOLD
- `printwithsmile_pla_plasilver_5000_175_c` — PLA Silver
- `printwithsmile_pla_plasunsetgold_5000_175_c` — PLA Sunset GOLD
- `printwithsmile_pla_platurquoiseblue_5000_175_c` — PLA Turquoise BLUE
- `printwithsmile_pla_plawhite_5000_175_c` — PLA White
- `printwithsmile_pla_plaxxlblack_5000_175_c` — PLA XXL BLACK
- `printwithsmile_pla_plaxxljustblack_5000_175_c` — PLA XXL Just BLACK
- `printwithsmile_pla_plaxxljustwhite_5000_175_c` — PLA XXL Just WHITE
- `printwithsmile_pla_plaxxlwhite_5000_175_c` — PLA XXL WHITE
- `printwithsmile_pla_playellow_5000_175_c` — PLA Yellow
- `printwithsmile_pla_plaebenwood_5000_175_c` — PLA EBEN Wood
- `printwithsmile_pla_plahisnatural_5000_175_c` — PLA HIS natural
- `printwithsmile_pla_plamahagonwood_5000_175_c` — PLA MAHAGON Wood
- `printwithsmile_pla_plarec-ecotyrkys_5000_175_c` — PLA REC- Eco TYRKYS
- `printwithsmile_pla_plarec-huntergreen_5000_175_c` — PLA REC- Hunter GREEN
- `printwithsmile_pla_plarec-justblack_5000_175_c` — PLA REC- Just BLACK
- `printwithsmile_pla_plarec-justblue_5000_175_c` — PLA REC- Just BLUE
- `printwithsmile_pla_plarec-justbrown_5000_175_c` — PLA REC- Just BROWN
- `printwithsmile_pla_plarec-justgrey_5000_175_c` — PLA REC- Just GREY
- `printwithsmile_pla_plarec-justpurple_5000_175_c` — PLA REC- Just PURPLE
- `printwithsmile_pla_plarec-justred_5000_175_c` — PLA REC- Just RED
- `printwithsmile_pla_plarec-justwhite_5000_175_c` — PLA REC- Just WHITE
- `printwithsmile_pla_plarec-justyellow_5000_175_c` — PLA REC- Just YELLOW
- `printwithsmile_pla_plarec-lowgrey_5000_175_c` — PLA REC- Low GREY
- `printwithsmile_pla_plarec-maygreen_5000_175_c` — PLA REC- May GREEN
- `printwithsmile_pla_plarec-mayablue_5000_175_c` — PLA REC- Maya BLUE
- `printwithsmile_pla_plarec-pumkinorange_5000_175_c` — PLA REC- Pumkin ORANGE
- `printwithsmile_pla_plawhitewood_5000_175_c` — PLA White Wood
- `printwithsmile_pla_plawood_5000_175_c` — PLA Wood
- `printwithsmile_pla_planaturalfibersplaebenwood450g_450_175_c` — PLA Natural Fibers PLA EBEN Wood 450 g
- `printwithsmile_pla_planaturalfibersplamahagonwood450g_450_175_c` — PLA Natural Fibers PLA MAHAGON Wood 450 g
- `printwithsmile_pla_planaturalfibersplawhitewood450g_450_175_c` — PLA Natural Fibers PLA White Wood 450 g
- `printwithsmile_pla_planaturalfibersplawood450g_450_175_c` — PLA Natural Fibers PLA Wood 450 g
- `printwithsmile_pla_refillplablackvolkano_850_175_c` — REFILL PLA BLACK Volkano
- `printwithsmile_pla_refillpladarkgrey_850_175_c` — REFILL PLA Dark GREY
- `printwithsmile_pla_refillplawhite_850_175_c` — REFILL PLA WHITE
- `printwithsmile_tpu_tpuprintwsflexblue96a_500_175_c` — TPU PRINT WS FLEX BLUE 96A
- `printwithsmile_tpu_tpuprintwsflexdarkgrey96a_500_175_c` — TPU PRINT WS FLEX DARK GREY 96A
- `printwithsmile_tpu_tpuprintwsflexgreen96a_500_175_c` — TPU PRINT WS FLEX GREEN 96A
- `printwithsmile_tpu_tpuprintwsflexred96a_500_175_c` — TPU PRINT WS FLEX RED 96A
- `printwithsmile_tpu_tpuprintwsflexwhite96a_500_175_c` — TPU PRINT WS FLEX WHITE 96A
- `printwithsmile_pa12_pa12cfcf15_1000_175_c` — PA12 CF CF15
- `printwithsmile_petg_bicolormetallicpetggreenbrown_1000_175_c` — Bicolor Metallic PETG GREEN BROWN
- `printwithsmile_petg_bicolormetallicpetgvioletsilver_1000_175_c` — Bicolor Metallic PETG VIOLET SILVER
- `printwithsmile_petg_bicolormetallicpetgvioletsparkle_1000_175_c` — Bicolor Metallic PETG VIOLET SPARKLE
- `printwithsmile_petg_petgcfpet-g-carbonfiber-black_1000_175_c` — PETG CF PET-G - CARBON Fiber - BLACK
- `printwithsmile_petg_repetgarmygreen_1000_175_c` — RE PETG Army GREEN
- `printwithsmile_petg_repetgcanaryyellow_1000_175_c` — RE PETG Canary YELLOW
- `printwithsmile_petg_repetgcoralneonred_1000_175_c` — RE PETG Coral NEON RED
- `printwithsmile_petg_repetgmetalgrey_1000_175_c` — RE PETG Metal GREY
- `printwithsmile_petg_repetgpersianblue_1000_175_c` — RE PETG Persian BLUE
- `printwithsmile_petg_repetgpetrolblue_1000_175_c` — RE PETG Petrol BLUE
- `printwithsmile_petg_repetgpetrolgreen_1000_175_c` — RE PETG Petrol GREEN
- `printwithsmile_petg_repetgpureblack_1000_175_c` — RE PETG Pure BLACK
- `printwithsmile_petg_repetgroyalblue_1000_175_c` — RE PETG Royal BLUE
- `printwithsmile_petg_repetgscarletred_1000_175_c` — RE PETG Scarlet RED
- `printwithsmile_petg_repetgsilver_1000_175_c` — RE PETG SILVER
- `printwithsmile_petg_repetgsmaragdgreen_1000_175_c` — RE PETG Smaragd GREEN
- `printwithsmile_petg_repetgsugarpink_1000_175_c` — RE PETG Sugar PINK
- `printwithsmile_pla_placfuvht-c15_1000_175_c` — PLA CF UVHT-C15
- `printwithsmile_pla_silkplagold_1000_175_c` — Silk PLA GOLD
- `printwithsmile_pla_silkplametallicblue_1000_175_c` — Silk PLA Metallic BLUE
- `printwithsmile_pla_silkplametallicgreen_1000_175_c` — Silk PLA Metallic GREEN
- `printwithsmile_pla_silkplasilver_1000_175_c` — Silk PLA SILVER
