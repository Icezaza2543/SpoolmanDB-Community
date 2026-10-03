# AmazonBasics duplicate migration review

Base `f5272390dae8954626e59c03d13e74c09886b6f9`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `72a3c2eab55874a6c18295a34ab83845abbf5573be9b9f2e38236dc4e91d1ca6`.

## Authorization and result

{"groups": 3, "approved_groups": 3, "retired": 3, "deferred": 0, "hard_stops": 0, "before_count": 51712, "after_count": 51709, "brand_before": 43, "brand_after": 40, "registry_before": 1722, "registry_after": 1725, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Three Rule1 strict SilkPLA duplicates. No readable current exact first-party printing evidence found; retain density1.25/nozzle220/bed60 unresolved. No identifiers or packaging/tare change.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence


## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`amazonbasics_pla_silkplablue_1000_175_p`|`amazonbasics_pla_silkblue_1000_175_p`|`AmazonBasics.json::AmazonBasics::Silk PLA {color_name}::Silk PLA Blue::PLA::1000::1.75::plastic::False`|
|`amazonbasics_pla_silkplagold_1000_175_p`|`amazonbasics_pla_silkgold_1000_175_p`|`AmazonBasics.json::AmazonBasics::Silk PLA {color_name}::Silk PLA Gold::PLA::1000::1.75::plastic::False`|
|`amazonbasics_pla_silkplasilver_1000_175_p`|`amazonbasics_pla_silksilver_1000_175_p`|`AmazonBasics.json::AmazonBasics::Silk PLA {color_name}::Silk PLA Silver::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### AB001: dup-ddacf0339a9c2c332a2aacbdc87536e441adda8f73d9a685d77b4ccd2492383e

Status: APPROVED; survivor `amazonbasics_pla_silkblue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`amazonbasics_pla_silkblue_1000_175_p`|`Silk {color_name}`|`Blue`|{"source_file": "AmazonBasics.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / True|
|`amazonbasics_pla_silkplablue_1000_175_p`|`Silk PLA {color_name}`|`Blue`|{"source_file": "AmazonBasics.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "amazonbasics_pla_silkblue_1000_175_p": 1.25,
    "amazonbasics_pla_silkplablue_1000_175_p": 1.24
  },
  "spool_weight": {
    "amazonbasics_pla_silkblue_1000_175_p": 266,
    "amazonbasics_pla_silkplablue_1000_175_p": null
  },
  "color_hex": {
    "amazonbasics_pla_silkblue_1000_175_p": "1E90EC",
    "amazonbasics_pla_silkplablue_1000_175_p": "0099E6"
  },
  "extruder_temp": {
    "amazonbasics_pla_silkblue_1000_175_p": 220,
    "amazonbasics_pla_silkplablue_1000_175_p": null
  },
  "extruder_temp_range": {
    "amazonbasics_pla_silkblue_1000_175_p": null,
    "amazonbasics_pla_silkplablue_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "amazonbasics_pla_silkblue_1000_175_p": 60,
    "amazonbasics_pla_silkplablue_1000_175_p": null
  },
  "bed_temp_range": {
    "amazonbasics_pla_silkblue_1000_175_p": null,
    "amazonbasics_pla_silkplablue_1000_175_p": [
      50,
      70
    ]
  }
}
```

### AB002: dup-02258db08d09a1fbd1bfba61facb2bd57a36e28e04c5e4c3f56a8300d46d919f

Status: APPROVED; survivor `amazonbasics_pla_silkgold_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`amazonbasics_pla_silkgold_1000_175_p`|`Silk {color_name}`|`Gold`|{"source_file": "AmazonBasics.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / True|
|`amazonbasics_pla_silkplagold_1000_175_p`|`Silk PLA {color_name}`|`Gold`|{"source_file": "AmazonBasics.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "amazonbasics_pla_silkgold_1000_175_p": 1.25,
    "amazonbasics_pla_silkplagold_1000_175_p": 1.24
  },
  "spool_weight": {
    "amazonbasics_pla_silkgold_1000_175_p": 266,
    "amazonbasics_pla_silkplagold_1000_175_p": null
  },
  "color_hex": {
    "amazonbasics_pla_silkgold_1000_175_p": "F8CC6D",
    "amazonbasics_pla_silkplagold_1000_175_p": "DDB95D"
  },
  "extruder_temp": {
    "amazonbasics_pla_silkgold_1000_175_p": 220,
    "amazonbasics_pla_silkplagold_1000_175_p": null
  },
  "extruder_temp_range": {
    "amazonbasics_pla_silkgold_1000_175_p": null,
    "amazonbasics_pla_silkplagold_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "amazonbasics_pla_silkgold_1000_175_p": 60,
    "amazonbasics_pla_silkplagold_1000_175_p": null
  },
  "bed_temp_range": {
    "amazonbasics_pla_silkgold_1000_175_p": null,
    "amazonbasics_pla_silkplagold_1000_175_p": [
      50,
      70
    ]
  }
}
```

### AB003: dup-3f087b12e2537f07eb7c73814f0ebc10a085ebb738ebaf1ef2e0e90d5a0cad94

Status: APPROVED; survivor `amazonbasics_pla_silksilver_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`amazonbasics_pla_silkplasilver_1000_175_p`|`Silk PLA {color_name}`|`Silver`|{"source_file": "AmazonBasics.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|
|`amazonbasics_pla_silksilver_1000_175_p`|`Silk {color_name}`|`Silver`|{"source_file": "AmazonBasics.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "amazonbasics_pla_silkplasilver_1000_175_p": 1.24,
    "amazonbasics_pla_silksilver_1000_175_p": 1.25
  },
  "spool_weight": {
    "amazonbasics_pla_silkplasilver_1000_175_p": null,
    "amazonbasics_pla_silksilver_1000_175_p": 266
  },
  "color_hex": {
    "amazonbasics_pla_silkplasilver_1000_175_p": "C9D0D4",
    "amazonbasics_pla_silksilver_1000_175_p": "A0AAB1"
  },
  "extruder_temp": {
    "amazonbasics_pla_silkplasilver_1000_175_p": null,
    "amazonbasics_pla_silksilver_1000_175_p": 220
  },
  "extruder_temp_range": {
    "amazonbasics_pla_silkplasilver_1000_175_p": [
      190,
      230
    ],
    "amazonbasics_pla_silksilver_1000_175_p": null
  },
  "bed_temp": {
    "amazonbasics_pla_silkplasilver_1000_175_p": null,
    "amazonbasics_pla_silksilver_1000_175_p": 60
  },
  "bed_temp_range": {
    "amazonbasics_pla_silkplasilver_1000_175_p": [
      50,
      70
    ],
    "amazonbasics_pla_silksilver_1000_175_p": null
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

- `amazonbasics_pla_blue_1000_175_p` — Blue
- `amazonbasics_pla_brown_1000_175_p` — Brown
- `amazonbasics_pla_darkblue_1000_175_p` — Dark Blue
- `amazonbasics_pla_darkgray_1000_175_p` — Dark Gray
- `amazonbasics_pla_translucent_1000_175_p` — Translucent
- `amazonbasics_pla_translucentred_1000_175_p` — Translucent Red
- `amazonbasics_pla_yellow_1000_175_p` — Yellow
- `amazonbasics_pla_gold_1000_175_p` — Gold
- `amazonbasics_pla_lightgrey_1000_175_p` — Light Grey
- `amazonbasics_pla_brightgreen_1000_175_p` — Bright Green
- `amazonbasics_pla_luminous_1000_175_p` — Luminous
- `amazonbasics_pla_neongreen_1000_175_p` — Neon Green
- `amazonbasics_pla_neonorange_1000_175_p` — Neon Orange
- `amazonbasics_pla_orange_1000_175_p` — Orange
- `amazonbasics_pla_pearlwhite_1000_175_p` — Pearl White
- `amazonbasics_pla_pink_1000_175_p` — Pink
- `amazonbasics_pla_red_1000_175_p` — Red
- `amazonbasics_pla_black_1000_175_p` — Black
- `amazonbasics_pla_silver_1000_175_p` — Silver
- `amazonbasics_pla_purple_1000_175_p` — Purple
- `amazonbasics_pla_white_1000_175_p` — White
- `amazonbasics_abs_white_1000_175_p` — White
- `amazonbasics_abs_black_1000_175_p` — Black
- `amazonbasics_abs_darkgray_1000_175_p` — Dark Gray
- `amazonbasics_abs_blue_1000_175_p` — Blue
- `amazonbasics_abs_red_1000_175_p` — Red
- `amazonbasics_pla_silkcopper_1000_175_p` — Silk Copper
- `amazonbasics_pla_silkcream_1000_175_p` — Silk Cream
- `amazonbasics_petg_white_1000_175_p` — White
- `amazonbasics_petg_black_1000_175_p` — Black
- `amazonbasics_petg_orange_1000_175_p` — Orange
- `amazonbasics_petg_blue_1000_175_p` — Blue
- `amazonbasics_petg_red_1000_175_p` — Red
- `amazonbasics_petg_gray_1000_175_p` — Gray
- `amazonbasics_petg_yellow_1000_175_p` — Yellow
- `amazonbasics_petg_translucent_1000_175_p` — Translucent
- `amazonbasics_pla_silkplaoffwhite_1000_175_p` — Silk PLA Off White
