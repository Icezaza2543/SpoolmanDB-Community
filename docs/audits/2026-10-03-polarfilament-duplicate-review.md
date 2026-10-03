# polarfilament duplicate migration review

Base `f302ca0f0bfd35243a07df52624c2c0a42e96d8e`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `4d25c2e83a92240c03c3ffc5becd098d0da2b9a7d946cf35cf7f5c007ee86cca`.

## Authorization and result

{"groups": 40, "approved_groups": 40, "retired": 40, "deferred": 0, "hard_stops": 0, "before_count": 52113, "after_count": 52073, "brand_before": 99, "brand_after": 59, "registry_before": 1321, "registry_after": 1361, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

All40 Rule1 normalized identity matches approved; survivor HEX/translucency/sparkle/tare retained, including Natural, LemonDrop,Seafoam,MarineBlue,Bloopiter. No identifiers to transfer. PETG bed55–65 repeats PLA and is flagged as suspicious; no exact official current printing evidence found for historical generic product, so retain unresolved, not replace with unverified newer-source70–90. EngineeringGrade density not used to assume oldformula identity. Packaging/tare untouched.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://cdn.shopify.com/s/files/1/0529/9965/1523/files/Polar_Filament_PLA_TDS_Rev1.1.pdf?v=1771348596", "density": 1.24, "note": "Current linked PLA TDS Rev1.1 February2026; defers printing temperatures to specific listings."}
- {"url": "https://cdn.shopify.com/s/files/1/0529/9965/1523/files/Polar_Filament_PETG_Engineering_Grade_TDS_Rev1.0.pdf?v=1771348596", "density": 1.27, "note": "Current Engineering Grade, not automatic evidence for Old PETG Formula. No printing ranges in sheet."}
- {"url": "https://polarfilament.com/products/petg-partial-old-petg-formula", "note": "Official catalog separates oldformula; no inferred current lot metadata."}
- {"url": "https://polarfilament.com/products/open-beta-experimental-black-petg-1kg-1-75mm", "note": "Current listing inspected; no numerical print recommendations found."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`polarfilament_petg_petgcandyred_1000_175_c`|`polarfilament_petg_candyred_1000_175_c`|`polarfilament.json::Polar Filament::PETG {color_name}::PETG Candy Red::PETG::1000::1.75::cardboard::False`|
|`polarfilament_petg_petgclassicblack_1000_175_c`|`polarfilament_petg_classicblack_1000_175_c`|`polarfilament.json::Polar Filament::PETG {color_name}::PETG Classic Black::PETG::1000::1.75::cardboard::False`|
|`polarfilament_petg_petgnatural(clear)_1000_175_c`|`polarfilament_petg_natural(clear)_1000_175_c`|`polarfilament.json::Polar Filament::PETG {color_name}::PETG Natural (Clear)::PETG::1000::1.75::cardboard::False`|
|`polarfilament_petg_petgpolarwhite_1000_175_c`|`polarfilament_petg_polarwhite_1000_175_c`|`polarfilament.json::Polar Filament::PETG {color_name}::PETG Polar White::PETG::1000::1.75::cardboard::False`|
|`polarfilament_petg_petgpurplex_1000_175_c`|`polarfilament_petg_purplex_1000_175_c`|`polarfilament.json::Polar Filament::PETG {color_name}::PETG Purplex::PETG::1000::1.75::cardboard::False`|
|`polarfilament_petg_petgregulationgray_1000_175_c`|`polarfilament_petg_regulationgray_1000_175_c`|`polarfilament.json::Polar Filament::PETG {color_name}::PETG Regulation Gray::PETG::1000::1.75::cardboard::False`|
|`polarfilament_petg_petgroyalblue_1000_175_c`|`polarfilament_petg_royalblue_1000_175_c`|`polarfilament.json::Polar Filament::PETG {color_name}::PETG Royal Blue::PETG::1000::1.75::cardboard::False`|
|`polarfilament_petg_petgsunshineyellow_1000_175_c`|`polarfilament_petg_sunshineyellow_1000_175_c`|`polarfilament.json::Polar Filament::PETG {color_name}::PETG Sunshine Yellow::PETG::1000::1.75::cardboard::False`|
|`polarfilament_petg_petgvividorange_1000_175_c`|`polarfilament_petg_vividorange_1000_175_c`|`polarfilament.json::Polar Filament::PETG {color_name}::PETG Vivid Orange::PETG::1000::1.75::cardboard::False`|
|`polarfilament_pla_plaaliengreen_1000_175_c`|`polarfilament_pla_aliengreen_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Alien Green::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plabananasplit_1000_175_c`|`polarfilament_pla_bananasplit_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Banana Split::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plablazeorange_1000_175_c`|`polarfilament_pla_blazeorange_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Blaze Orange::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plabloopiter_1000_175_c`|`polarfilament_pla_bloopiter_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Bloopiter::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plabubblegum_1000_175_c`|`polarfilament_pla_bubblegum_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Bubblegum::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_placandyred_1000_175_c`|`polarfilament_pla_candyred_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Candy Red::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plachestnut_1000_175_c`|`polarfilament_pla_chestnut_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Chestnut::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_placlassicblack_1000_175_c`|`polarfilament_pla_classicblack_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Classic Black::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_placoral_1000_175_c`|`polarfilament_pla_coral_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Coral::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_placornflowerblue_1000_175_c`|`polarfilament_pla_cornflowerblue_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Cornflower Blue::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_placreamsicle_1000_175_c`|`polarfilament_pla_creamsicle_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Creamsicle::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_pladeepspace_1000_175_c`|`polarfilament_pla_deepspace_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Deep Space::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plalemondrop_1000_175_c`|`polarfilament_pla_lemondrop_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Lemon Drop::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plalightblue_1000_175_c`|`polarfilament_pla_lightblue_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Light Blue::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plamagenta_1000_175_c`|`polarfilament_pla_magenta_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Magenta::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plamarineblue_1000_175_c`|`polarfilament_pla_marineblue_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Marine Blue::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plamerlot_1000_175_c`|`polarfilament_pla_merlot_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Merlot::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plamocha_1000_175_c`|`polarfilament_pla_mocha_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Mocha::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_planatural_1000_175_c`|`polarfilament_pla_natural_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Natural::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plapink_1000_175_c`|`polarfilament_pla_pink_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Pink::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plapolarwhite_1000_175_c`|`polarfilament_pla_polarwhite_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Polar White::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plapurplex_1000_175_c`|`polarfilament_pla_purplex_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Purplex::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plaregulationgray_1000_175_c`|`polarfilament_pla_regulationgray_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Regulation Gray::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plarocketred_1000_175_c`|`polarfilament_pla_rocketred_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Rocket Red::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plaroyalblue_1000_175_c`|`polarfilament_pla_royalblue_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Royal Blue::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plasapphire_1000_175_c`|`polarfilament_pla_sapphire_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Sapphire::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plaseafoam_1000_175_c`|`polarfilament_pla_seafoam_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Seafoam::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plashamrock_1000_175_c`|`polarfilament_pla_shamrock_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Shamrock::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plasquid_1000_175_c`|`polarfilament_pla_squid_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Squid::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plasunshineyellow_1000_175_c`|`polarfilament_pla_sunshineyellow_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Sunshine Yellow::PLA::1000::1.75::cardboard::False`|
|`polarfilament_pla_plavividorange_1000_175_c`|`polarfilament_pla_vividorange_1000_175_c`|`polarfilament.json::Polar Filament::PLA {color_name}::PLA Vivid Orange::PLA::1000::1.75::cardboard::False`|

## Per-group decisions and unresolved metadata

### PO001: dup-5b5ec59d4baac64c791f1445450a1be59dc0b248e3f00631ed7fd4c10d3a143e

Status: APPROVED; survivor `polarfilament_petg_candyred_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_petg_candyred_1000_175_c`|`{color_name}`|`Candy Red`|{"source_file": "polarfilament.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|
|`polarfilament_petg_petgcandyred_1000_175_c`|`PETG {color_name}`|`Candy Red`|{"source_file": "polarfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_petg_candyred_1000_175_c": 190.0,
    "polarfilament_petg_petgcandyred_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_petg_candyred_1000_175_c": "C10006",
    "polarfilament_petg_petgcandyred_1000_175_c": "DE1619"
  },
  "extruder_temp_range": {
    "polarfilament_petg_candyred_1000_175_c": [
      230,
      250
    ],
    "polarfilament_petg_petgcandyred_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "polarfilament_petg_candyred_1000_175_c": [
      55,
      65
    ],
    "polarfilament_petg_petgcandyred_1000_175_c": [
      70,
      90
    ]
  }
}
```

### PO002: dup-3fc53bb1dd225f3f389f453c66af5d2b357fa78dcfed1971bd6364e32583770c

Status: APPROVED; survivor `polarfilament_petg_classicblack_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_petg_classicblack_1000_175_c`|`{color_name}`|`Classic Black`|{"source_file": "polarfilament.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|
|`polarfilament_petg_petgclassicblack_1000_175_c`|`PETG {color_name}`|`Classic Black`|{"source_file": "polarfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_petg_classicblack_1000_175_c": 190.0,
    "polarfilament_petg_petgclassicblack_1000_175_c": null
  },
  "extruder_temp_range": {
    "polarfilament_petg_classicblack_1000_175_c": [
      230,
      250
    ],
    "polarfilament_petg_petgclassicblack_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "polarfilament_petg_classicblack_1000_175_c": [
      55,
      65
    ],
    "polarfilament_petg_petgclassicblack_1000_175_c": [
      70,
      90
    ]
  }
}
```

### PO003: dup-911b3c1c49b411ce2fd63933cb719fbc5a8f22bcedfe57295a8b8bacaaa6ae12

Status: APPROVED; survivor `polarfilament_petg_natural(clear)_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_petg_natural(clear)_1000_175_c`|`{color_name}`|`Natural (Clear)`|{"source_file": "polarfilament.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|
|`polarfilament_petg_petgnatural(clear)_1000_175_c`|`PETG {color_name}`|`Natural (Clear)`|{"source_file": "polarfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_petg_natural(clear)_1000_175_c": 190.0,
    "polarfilament_petg_petgnatural(clear)_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_petg_natural(clear)_1000_175_c": "C6C695",
    "polarfilament_petg_petgnatural(clear)_1000_175_c": "E4E7E5"
  },
  "extruder_temp_range": {
    "polarfilament_petg_natural(clear)_1000_175_c": [
      230,
      250
    ],
    "polarfilament_petg_petgnatural(clear)_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp_range": {
    "polarfilament_petg_natural(clear)_1000_175_c": [
      55,
      65
    ],
    "polarfilament_petg_petgnatural(clear)_1000_175_c": [
      70,
      90
    ]
  }
}
```

### PO004: dup-34bbe814203050c561f2d82cc52ee845e4292153589ac14cd6f055713ed14d53

Status: APPROVED; survivor `polarfilament_petg_polarwhite_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_petg_petgpolarwhite_1000_175_c`|`PETG {color_name}`|`Polar White`|{"source_file": "polarfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|
|`polarfilament_petg_polarwhite_1000_175_c`|`{color_name}`|`Polar White`|{"source_file": "polarfilament.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_petg_petgpolarwhite_1000_175_c": null,
    "polarfilament_petg_polarwhite_1000_175_c": 190.0
  },
  "color_hex": {
    "polarfilament_petg_petgpolarwhite_1000_175_c": "F0EBE5",
    "polarfilament_petg_polarwhite_1000_175_c": "BABAB0"
  },
  "extruder_temp_range": {
    "polarfilament_petg_petgpolarwhite_1000_175_c": [
      220,
      250
    ],
    "polarfilament_petg_polarwhite_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "polarfilament_petg_petgpolarwhite_1000_175_c": [
      70,
      90
    ],
    "polarfilament_petg_polarwhite_1000_175_c": [
      55,
      65
    ]
  }
}
```

### PO005: dup-d623f456539e02298c79ceb372b69d14c65614785b09d4bc828d6a2edb14d707

Status: APPROVED; survivor `polarfilament_petg_purplex_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_petg_petgpurplex_1000_175_c`|`PETG {color_name}`|`Purplex`|{"source_file": "polarfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|
|`polarfilament_petg_purplex_1000_175_c`|`{color_name}`|`Purplex`|{"source_file": "polarfilament.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_petg_petgpurplex_1000_175_c": null,
    "polarfilament_petg_purplex_1000_175_c": 190.0
  },
  "color_hex": {
    "polarfilament_petg_petgpurplex_1000_175_c": "6C47B2",
    "polarfilament_petg_purplex_1000_175_c": "5a2d91"
  },
  "extruder_temp_range": {
    "polarfilament_petg_petgpurplex_1000_175_c": [
      220,
      250
    ],
    "polarfilament_petg_purplex_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "polarfilament_petg_petgpurplex_1000_175_c": [
      70,
      90
    ],
    "polarfilament_petg_purplex_1000_175_c": [
      55,
      65
    ]
  }
}
```

### PO006: dup-96559ebd4bcca01352ceab72b7203f0ff3e3f543a42b714735c475fc82862071

Status: APPROVED; survivor `polarfilament_petg_regulationgray_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_petg_petgregulationgray_1000_175_c`|`PETG {color_name}`|`Regulation Gray`|{"source_file": "polarfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|
|`polarfilament_petg_regulationgray_1000_175_c`|`{color_name}`|`Regulation Gray`|{"source_file": "polarfilament.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_petg_petgregulationgray_1000_175_c": null,
    "polarfilament_petg_regulationgray_1000_175_c": 190.0
  },
  "color_hex": {
    "polarfilament_petg_petgregulationgray_1000_175_c": "91A0B6",
    "polarfilament_petg_regulationgray_1000_175_c": "6d6d6d"
  },
  "extruder_temp_range": {
    "polarfilament_petg_petgregulationgray_1000_175_c": [
      220,
      250
    ],
    "polarfilament_petg_regulationgray_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "polarfilament_petg_petgregulationgray_1000_175_c": [
      70,
      90
    ],
    "polarfilament_petg_regulationgray_1000_175_c": [
      55,
      65
    ]
  }
}
```

### PO007: dup-a1539c5532fb916baf8a7cf28803f9a925350c461fee34294b7b96fc2a02bb86

Status: APPROVED; survivor `polarfilament_petg_royalblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_petg_petgroyalblue_1000_175_c`|`PETG {color_name}`|`Royal Blue`|{"source_file": "polarfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|
|`polarfilament_petg_royalblue_1000_175_c`|`{color_name}`|`Royal Blue`|{"source_file": "polarfilament.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_petg_petgroyalblue_1000_175_c": null,
    "polarfilament_petg_royalblue_1000_175_c": 190.0
  },
  "color_hex": {
    "polarfilament_petg_petgroyalblue_1000_175_c": "436176",
    "polarfilament_petg_royalblue_1000_175_c": "0130AF"
  },
  "extruder_temp_range": {
    "polarfilament_petg_petgroyalblue_1000_175_c": [
      220,
      250
    ],
    "polarfilament_petg_royalblue_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "polarfilament_petg_petgroyalblue_1000_175_c": [
      70,
      90
    ],
    "polarfilament_petg_royalblue_1000_175_c": [
      55,
      65
    ]
  }
}
```

### PO008: dup-c69b16e9db26fae2363b673b28a3dcfce6464ed7dbf85ab45cbab387884a457c

Status: APPROVED; survivor `polarfilament_petg_sunshineyellow_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_petg_petgsunshineyellow_1000_175_c`|`PETG {color_name}`|`Sunshine Yellow`|{"source_file": "polarfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|
|`polarfilament_petg_sunshineyellow_1000_175_c`|`{color_name}`|`Sunshine Yellow`|{"source_file": "polarfilament.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_petg_petgsunshineyellow_1000_175_c": null,
    "polarfilament_petg_sunshineyellow_1000_175_c": 190.0
  },
  "color_hex": {
    "polarfilament_petg_petgsunshineyellow_1000_175_c": "EFDC4C",
    "polarfilament_petg_sunshineyellow_1000_175_c": "F9E20C"
  },
  "extruder_temp_range": {
    "polarfilament_petg_petgsunshineyellow_1000_175_c": [
      220,
      250
    ],
    "polarfilament_petg_sunshineyellow_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "polarfilament_petg_petgsunshineyellow_1000_175_c": [
      70,
      90
    ],
    "polarfilament_petg_sunshineyellow_1000_175_c": [
      55,
      65
    ]
  }
}
```

### PO009: dup-cd9038c6c77c8679d1d53d29e24ebd12d4a03e4a882b72c435133113aa99ef45

Status: APPROVED; survivor `polarfilament_petg_vividorange_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_petg_petgvividorange_1000_175_c`|`PETG {color_name}`|`Vivid Orange`|{"source_file": "polarfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|
|`polarfilament_petg_vividorange_1000_175_c`|`{color_name}`|`Vivid Orange`|{"source_file": "polarfilament.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_petg_petgvividorange_1000_175_c": null,
    "polarfilament_petg_vividorange_1000_175_c": 190.0
  },
  "color_hex": {
    "polarfilament_petg_petgvividorange_1000_175_c": "FF5F2E",
    "polarfilament_petg_vividorange_1000_175_c": "C62A03"
  },
  "extruder_temp_range": {
    "polarfilament_petg_petgvividorange_1000_175_c": [
      220,
      250
    ],
    "polarfilament_petg_vividorange_1000_175_c": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "polarfilament_petg_petgvividorange_1000_175_c": [
      70,
      90
    ],
    "polarfilament_petg_vividorange_1000_175_c": [
      55,
      65
    ]
  }
}
```

### PO010: dup-a9c55d39adf9ec21c0c1369110e2fe65c7505c66420781955962f4c97257c5d3

Status: APPROVED; survivor `polarfilament_pla_aliengreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_aliengreen_1000_175_c`|`{color_name}`|`Alien Green`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_plaaliengreen_1000_175_c`|`PLA {color_name}`|`Alien Green`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_aliengreen_1000_175_c": 190.0,
    "polarfilament_pla_plaaliengreen_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_aliengreen_1000_175_c": "0a5e0a",
    "polarfilament_pla_plaaliengreen_1000_175_c": "26A648"
  },
  "extruder_temp_range": {
    "polarfilament_pla_aliengreen_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_plaaliengreen_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_aliengreen_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_plaaliengreen_1000_175_c": [
      50,
      70
    ]
  }
}
```

### PO011: dup-a29d0167a7c6b1ba45812da4aa2ba04bbe11331e02088a242c4ed4e24cd79903

Status: APPROVED; survivor `polarfilament_pla_bananasplit_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_bananasplit_1000_175_c`|`{color_name}`|`Banana Split`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_plabananasplit_1000_175_c`|`PLA {color_name}`|`Banana Split`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_bananasplit_1000_175_c": 190.0,
    "polarfilament_pla_plabananasplit_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_bananasplit_1000_175_c": "abba3b",
    "polarfilament_pla_plabananasplit_1000_175_c": "EEEA44"
  },
  "extruder_temp_range": {
    "polarfilament_pla_bananasplit_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_plabananasplit_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_bananasplit_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_plabananasplit_1000_175_c": [
      50,
      70
    ]
  }
}
```

### PO012: dup-273948fb4ba038002baae5998c6a1c1e5c0effd61840b2b0385a1755443cae35

Status: APPROVED; survivor `polarfilament_pla_blazeorange_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_blazeorange_1000_175_c`|`{color_name}`|`Blaze Orange`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_plablazeorange_1000_175_c`|`PLA {color_name}`|`Blaze Orange`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_blazeorange_1000_175_c": 190.0,
    "polarfilament_pla_plablazeorange_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_blazeorange_1000_175_c": "F91D09",
    "polarfilament_pla_plablazeorange_1000_175_c": "E03F26"
  },
  "extruder_temp_range": {
    "polarfilament_pla_blazeorange_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_plablazeorange_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_blazeorange_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_plablazeorange_1000_175_c": [
      50,
      70
    ]
  }
}
```

### PO013: dup-b0ab1cbf53e95450d3d199f5eb7458a1965e73fa0c683a6959b12a0d0a9ff2d7

Status: APPROVED; survivor `polarfilament_pla_bloopiter_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_bloopiter_1000_175_c`|`{color_name}`|`Bloopiter`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_plabloopiter_1000_175_c`|`PLA {color_name}`|`Bloopiter`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_bloopiter_1000_175_c": 190.0,
    "polarfilament_pla_plabloopiter_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_bloopiter_1000_175_c": "3b3149",
    "polarfilament_pla_plabloopiter_1000_175_c": "584E6A"
  },
  "extruder_temp_range": {
    "polarfilament_pla_bloopiter_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_plabloopiter_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_bloopiter_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_plabloopiter_1000_175_c": [
      50,
      70
    ]
  },
  "pattern": {
    "polarfilament_pla_bloopiter_1000_175_c": "sparkle",
    "polarfilament_pla_plabloopiter_1000_175_c": null
  }
}
```

### PO014: dup-64c1b7939dd0b4f8b067b6a47c5077a8045cd1275ac305365246c03caa9bd229

Status: APPROVED; survivor `polarfilament_pla_bubblegum_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_bubblegum_1000_175_c`|`{color_name}`|`Bubblegum`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_plabubblegum_1000_175_c`|`PLA {color_name}`|`Bubblegum`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_bubblegum_1000_175_c": 190.0,
    "polarfilament_pla_plabubblegum_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_bubblegum_1000_175_c": "D62285",
    "polarfilament_pla_plabubblegum_1000_175_c": "F300EA"
  },
  "extruder_temp_range": {
    "polarfilament_pla_bubblegum_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_plabubblegum_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_bubblegum_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_plabubblegum_1000_175_c": [
      50,
      70
    ]
  }
}
```

### PO015: dup-acb8dc789df801d9934d6fa2c0dcd6b6671994e8e2cf42b21601704dbfcb5e26

Status: APPROVED; survivor `polarfilament_pla_candyred_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_candyred_1000_175_c`|`{color_name}`|`Candy Red`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_placandyred_1000_175_c`|`PLA {color_name}`|`Candy Red`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_candyred_1000_175_c": 190.0,
    "polarfilament_pla_placandyred_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_candyred_1000_175_c": "C10006",
    "polarfilament_pla_placandyred_1000_175_c": "AA0101"
  },
  "extruder_temp_range": {
    "polarfilament_pla_candyred_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_placandyred_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_candyred_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_placandyred_1000_175_c": [
      50,
      70
    ]
  }
}
```

### PO016: dup-3576a7ef219b0aaf55ae29b4fd35d2396fc20d5acb694191bca169b65515d38d

Status: APPROVED; survivor `polarfilament_pla_chestnut_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_chestnut_1000_175_c`|`{color_name}`|`Chestnut`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_plachestnut_1000_175_c`|`PLA {color_name}`|`Chestnut`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_chestnut_1000_175_c": 190.0,
    "polarfilament_pla_plachestnut_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_chestnut_1000_175_c": "873232",
    "polarfilament_pla_plachestnut_1000_175_c": "98282F"
  },
  "extruder_temp_range": {
    "polarfilament_pla_chestnut_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_plachestnut_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_chestnut_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_plachestnut_1000_175_c": [
      50,
      70
    ]
  }
}
```

### PO017: dup-9e1cd70e16503b8dfd8508f4c73fd2afd3d36d09158455fb3f1afa6ae23fbb54

Status: APPROVED; survivor `polarfilament_pla_classicblack_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_classicblack_1000_175_c`|`{color_name}`|`Classic Black`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_placlassicblack_1000_175_c`|`PLA {color_name}`|`Classic Black`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_classicblack_1000_175_c": 190.0,
    "polarfilament_pla_placlassicblack_1000_175_c": null
  },
  "extruder_temp_range": {
    "polarfilament_pla_classicblack_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_placlassicblack_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_classicblack_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_placlassicblack_1000_175_c": [
      50,
      70
    ]
  }
}
```

### PO018: dup-2abf4a7eaa7398f1095187a0814f0cc94690cf850c6a3d38f4e38fa37871442a

Status: APPROVED; survivor `polarfilament_pla_coral_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_coral_1000_175_c`|`{color_name}`|`Coral`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_placoral_1000_175_c`|`PLA {color_name}`|`Coral`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_coral_1000_175_c": 190.0,
    "polarfilament_pla_placoral_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_coral_1000_175_c": "d12b4a",
    "polarfilament_pla_placoral_1000_175_c": "FB637E"
  },
  "extruder_temp_range": {
    "polarfilament_pla_coral_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_placoral_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_coral_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_placoral_1000_175_c": [
      50,
      70
    ]
  }
}
```

### PO019: dup-9d08478f615272a7564026a9b03560cefff939d615e14ec523debe36af4b3ee7

Status: APPROVED; survivor `polarfilament_pla_cornflowerblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_cornflowerblue_1000_175_c`|`{color_name}`|`Cornflower Blue`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_placornflowerblue_1000_175_c`|`PLA {color_name}`|`Cornflower Blue`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_cornflowerblue_1000_175_c": 190.0,
    "polarfilament_pla_placornflowerblue_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_cornflowerblue_1000_175_c": "5065af",
    "polarfilament_pla_placornflowerblue_1000_175_c": "4F7BBB"
  },
  "extruder_temp_range": {
    "polarfilament_pla_cornflowerblue_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_placornflowerblue_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_cornflowerblue_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_placornflowerblue_1000_175_c": [
      50,
      70
    ]
  }
}
```

### PO020: dup-41628ceb6696d764fa85004a66e8b832a8e57987f720c58e474167bd64923d66

Status: APPROVED; survivor `polarfilament_pla_creamsicle_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_creamsicle_1000_175_c`|`{color_name}`|`Creamsicle`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_placreamsicle_1000_175_c`|`PLA {color_name}`|`Creamsicle`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_creamsicle_1000_175_c": 190.0,
    "polarfilament_pla_placreamsicle_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_creamsicle_1000_175_c": "D65A3B",
    "polarfilament_pla_placreamsicle_1000_175_c": "FF8B47"
  },
  "extruder_temp_range": {
    "polarfilament_pla_creamsicle_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_placreamsicle_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_creamsicle_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_placreamsicle_1000_175_c": [
      50,
      70
    ]
  }
}
```

### PO021: dup-8fb03171adb6870fe46d566ab2ccc9c8dfa268dc9a0333e25dc8888f2a6377db

Status: APPROVED; survivor `polarfilament_pla_deepspace_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_deepspace_1000_175_c`|`{color_name}`|`Deep Space`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_pladeepspace_1000_175_c`|`PLA {color_name}`|`Deep Space`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_deepspace_1000_175_c": 190.0,
    "polarfilament_pla_pladeepspace_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_deepspace_1000_175_c": "1d3154",
    "polarfilament_pla_pladeepspace_1000_175_c": "253F56"
  },
  "extruder_temp_range": {
    "polarfilament_pla_deepspace_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_pladeepspace_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_deepspace_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_pladeepspace_1000_175_c": [
      50,
      70
    ]
  }
}
```

### PO022: dup-8cadeefe9e46c6b900148cc73474289945a5237a4477fc74d881cd1cedac19c9

Status: APPROVED; survivor `polarfilament_pla_lemondrop_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_lemondrop_1000_175_c`|`{color_name}`|`Lemon Drop`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_plalemondrop_1000_175_c`|`PLA {color_name}`|`Lemon Drop`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_lemondrop_1000_175_c": 190.0,
    "polarfilament_pla_plalemondrop_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_lemondrop_1000_175_c": "B8C109",
    "polarfilament_pla_plalemondrop_1000_175_c": "EEEA44"
  },
  "extruder_temp_range": {
    "polarfilament_pla_lemondrop_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_plalemondrop_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_lemondrop_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_plalemondrop_1000_175_c": [
      50,
      70
    ]
  },
  "translucent": {
    "polarfilament_pla_lemondrop_1000_175_c": false,
    "polarfilament_pla_plalemondrop_1000_175_c": true
  }
}
```

### PO023: dup-0fe7b7fe8e0afac10667f3276518f7cad2933bf14addb2f034ddaa6119ddb0cf

Status: APPROVED; survivor `polarfilament_pla_lightblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_lightblue_1000_175_c`|`{color_name}`|`Light Blue`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_plalightblue_1000_175_c`|`PLA {color_name}`|`Light Blue`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_lightblue_1000_175_c": 190.0,
    "polarfilament_pla_plalightblue_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_lightblue_1000_175_c": "0a15af",
    "polarfilament_pla_plalightblue_1000_175_c": "0099E6"
  },
  "extruder_temp_range": {
    "polarfilament_pla_lightblue_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_plalightblue_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_lightblue_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_plalightblue_1000_175_c": [
      50,
      70
    ]
  }
}
```

### PO024: dup-11e4beb897cca43041b5424884645e9b842d02ca9503f9dc10092d2e70bc5385

Status: APPROVED; survivor `polarfilament_pla_magenta_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_magenta_1000_175_c`|`{color_name}`|`Magenta`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_plamagenta_1000_175_c`|`PLA {color_name}`|`Magenta`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_magenta_1000_175_c": 190.0,
    "polarfilament_pla_plamagenta_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_magenta_1000_175_c": "C1004A",
    "polarfilament_pla_plamagenta_1000_175_c": "F2306E"
  },
  "extruder_temp_range": {
    "polarfilament_pla_magenta_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_plamagenta_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_magenta_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_plamagenta_1000_175_c": [
      50,
      70
    ]
  }
}
```

### PO025: dup-6178814b193514134769060e4875831f37ee3c477a8025d031f131649faf6e79

Status: APPROVED; survivor `polarfilament_pla_marineblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_marineblue_1000_175_c`|`{color_name}`|`Marine Blue`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_plamarineblue_1000_175_c`|`PLA {color_name}`|`Marine Blue`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_marineblue_1000_175_c": 190.0,
    "polarfilament_pla_plamarineblue_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_marineblue_1000_175_c": "043591",
    "polarfilament_pla_plamarineblue_1000_175_c": "0353BA"
  },
  "extruder_temp_range": {
    "polarfilament_pla_marineblue_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_plamarineblue_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_marineblue_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_plamarineblue_1000_175_c": [
      50,
      70
    ]
  },
  "pattern": {
    "polarfilament_pla_marineblue_1000_175_c": "sparkle",
    "polarfilament_pla_plamarineblue_1000_175_c": null
  }
}
```

### PO026: dup-5aa245a0b99ea12b929d18d70b0c169d984b8e1b29c244e99001a89de9c0e5b1

Status: APPROVED; survivor `polarfilament_pla_merlot_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_merlot_1000_175_c`|`{color_name}`|`Merlot`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_plamerlot_1000_175_c`|`PLA {color_name}`|`Merlot`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_merlot_1000_175_c": 190.0,
    "polarfilament_pla_plamerlot_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_merlot_1000_175_c": "68364a",
    "polarfilament_pla_plamerlot_1000_175_c": "915672"
  },
  "extruder_temp_range": {
    "polarfilament_pla_merlot_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_plamerlot_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_merlot_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_plamerlot_1000_175_c": [
      50,
      70
    ]
  }
}
```

### PO027: dup-f98517b24bdbec51ac9c790c2a46e288c198d93be5720ebeb109d2bd06faf5fc

Status: APPROVED; survivor `polarfilament_pla_mocha_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_mocha_1000_175_c`|`{color_name}`|`Mocha`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_plamocha_1000_175_c`|`PLA {color_name}`|`Mocha`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_mocha_1000_175_c": 190.0,
    "polarfilament_pla_plamocha_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_mocha_1000_175_c": "5e4a3b",
    "polarfilament_pla_plamocha_1000_175_c": "724E3D"
  },
  "extruder_temp_range": {
    "polarfilament_pla_mocha_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_plamocha_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_mocha_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_plamocha_1000_175_c": [
      50,
      70
    ]
  }
}
```

### PO028: dup-024a84da873bb26ed3484763731768ed90d974a1c8117b0dc6a26d338f34e0ab

Status: APPROVED; survivor `polarfilament_pla_natural_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_natural_1000_175_c`|`{color_name}`|`Natural`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_planatural_1000_175_c`|`PLA {color_name}`|`Natural`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_natural_1000_175_c": 190.0,
    "polarfilament_pla_planatural_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_natural_1000_175_c": "C6C695",
    "polarfilament_pla_planatural_1000_175_c": "DFDFD3"
  },
  "extruder_temp_range": {
    "polarfilament_pla_natural_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_planatural_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_natural_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_planatural_1000_175_c": [
      50,
      70
    ]
  },
  "translucent": {
    "polarfilament_pla_natural_1000_175_c": true,
    "polarfilament_pla_planatural_1000_175_c": false
  }
}
```

### PO029: dup-6706efc3f57a91fb94f89e22672a100c318556688d45eee3753760f9612c864c

Status: APPROVED; survivor `polarfilament_pla_pink_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_pink_1000_175_c`|`{color_name}`|`Pink`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|
|`polarfilament_pla_plapink_1000_175_c`|`PLA {color_name}`|`Pink`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_pink_1000_175_c": 190.0,
    "polarfilament_pla_plapink_1000_175_c": null
  },
  "color_hex": {
    "polarfilament_pla_pink_1000_175_c": "af5f5f",
    "polarfilament_pla_plapink_1000_175_c": "F4A0B1"
  },
  "extruder_temp_range": {
    "polarfilament_pla_pink_1000_175_c": [
      205,
      225
    ],
    "polarfilament_pla_plapink_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_pink_1000_175_c": [
      55,
      65
    ],
    "polarfilament_pla_plapink_1000_175_c": [
      50,
      70
    ]
  }
}
```

### PO030: dup-53822589a86ea3c74231318c902b2283f29ba50a36c0c211641a183dcfb175cc

Status: APPROVED; survivor `polarfilament_pla_polarwhite_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_plapolarwhite_1000_175_c`|`PLA {color_name}`|`Polar White`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|
|`polarfilament_pla_polarwhite_1000_175_c`|`{color_name}`|`Polar White`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_plapolarwhite_1000_175_c": null,
    "polarfilament_pla_polarwhite_1000_175_c": 190.0
  },
  "color_hex": {
    "polarfilament_pla_plapolarwhite_1000_175_c": "E3E0D3",
    "polarfilament_pla_polarwhite_1000_175_c": "BABAB0"
  },
  "extruder_temp_range": {
    "polarfilament_pla_plapolarwhite_1000_175_c": [
      190,
      230
    ],
    "polarfilament_pla_polarwhite_1000_175_c": [
      205,
      225
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_plapolarwhite_1000_175_c": [
      50,
      70
    ],
    "polarfilament_pla_polarwhite_1000_175_c": [
      55,
      65
    ]
  }
}
```

### PO031: dup-c4c4c1a98ef7f92e3d81179a4df5662462cfa04de30fe690dafcc0624b444954

Status: APPROVED; survivor `polarfilament_pla_purplex_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_plapurplex_1000_175_c`|`PLA {color_name}`|`Purplex`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|
|`polarfilament_pla_purplex_1000_175_c`|`{color_name}`|`Purplex`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_plapurplex_1000_175_c": null,
    "polarfilament_pla_purplex_1000_175_c": 190.0
  },
  "color_hex": {
    "polarfilament_pla_plapurplex_1000_175_c": "6C47B2",
    "polarfilament_pla_purplex_1000_175_c": "5a2d91"
  },
  "extruder_temp_range": {
    "polarfilament_pla_plapurplex_1000_175_c": [
      190,
      230
    ],
    "polarfilament_pla_purplex_1000_175_c": [
      205,
      225
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_plapurplex_1000_175_c": [
      50,
      70
    ],
    "polarfilament_pla_purplex_1000_175_c": [
      55,
      65
    ]
  }
}
```

### PO032: dup-144d790222bc75cf1307426ce96d32b78c30b68730b5cdede42883687bde4606

Status: APPROVED; survivor `polarfilament_pla_regulationgray_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_plaregulationgray_1000_175_c`|`PLA {color_name}`|`Regulation Gray`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|
|`polarfilament_pla_regulationgray_1000_175_c`|`{color_name}`|`Regulation Gray`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_plaregulationgray_1000_175_c": null,
    "polarfilament_pla_regulationgray_1000_175_c": 190.0
  },
  "color_hex": {
    "polarfilament_pla_plaregulationgray_1000_175_c": "949A9E",
    "polarfilament_pla_regulationgray_1000_175_c": "6d6d6d"
  },
  "extruder_temp_range": {
    "polarfilament_pla_plaregulationgray_1000_175_c": [
      190,
      230
    ],
    "polarfilament_pla_regulationgray_1000_175_c": [
      205,
      225
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_plaregulationgray_1000_175_c": [
      50,
      70
    ],
    "polarfilament_pla_regulationgray_1000_175_c": [
      55,
      65
    ]
  }
}
```

### PO033: dup-dd8945d50ea5974f673b451e3007326a14045372e4fe30b4a3ee368bfee9bce5

Status: APPROVED; survivor `polarfilament_pla_rocketred_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_plarocketred_1000_175_c`|`PLA {color_name}`|`Rocket Red`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|
|`polarfilament_pla_rocketred_1000_175_c`|`{color_name}`|`Rocket Red`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_plarocketred_1000_175_c": null,
    "polarfilament_pla_rocketred_1000_175_c": 190.0
  },
  "color_hex": {
    "polarfilament_pla_plarocketred_1000_175_c": "E60000",
    "polarfilament_pla_rocketred_1000_175_c": "C60003"
  },
  "extruder_temp_range": {
    "polarfilament_pla_plarocketred_1000_175_c": [
      190,
      230
    ],
    "polarfilament_pla_rocketred_1000_175_c": [
      205,
      225
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_plarocketred_1000_175_c": [
      50,
      70
    ],
    "polarfilament_pla_rocketred_1000_175_c": [
      55,
      65
    ]
  }
}
```

### PO034: dup-13ae681586e801e88bb721f6beea8bf560eb0b4c59a552005aeab1c57f364cb6

Status: APPROVED; survivor `polarfilament_pla_royalblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_plaroyalblue_1000_175_c`|`PLA {color_name}`|`Royal Blue`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|
|`polarfilament_pla_royalblue_1000_175_c`|`{color_name}`|`Royal Blue`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_plaroyalblue_1000_175_c": null,
    "polarfilament_pla_royalblue_1000_175_c": 190.0
  },
  "color_hex": {
    "polarfilament_pla_plaroyalblue_1000_175_c": "0353BA",
    "polarfilament_pla_royalblue_1000_175_c": "0130AF"
  },
  "extruder_temp_range": {
    "polarfilament_pla_plaroyalblue_1000_175_c": [
      190,
      230
    ],
    "polarfilament_pla_royalblue_1000_175_c": [
      205,
      225
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_plaroyalblue_1000_175_c": [
      50,
      70
    ],
    "polarfilament_pla_royalblue_1000_175_c": [
      55,
      65
    ]
  }
}
```

### PO035: dup-046b7209be0e9659a74ccf410ebaed4de5f05ef9cc2505c327f98cb8841d8da3

Status: APPROVED; survivor `polarfilament_pla_sapphire_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_plasapphire_1000_175_c`|`PLA {color_name}`|`Sapphire`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|
|`polarfilament_pla_sapphire_1000_175_c`|`{color_name}`|`Sapphire`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_plasapphire_1000_175_c": null,
    "polarfilament_pla_sapphire_1000_175_c": 190.0
  },
  "color_hex": {
    "polarfilament_pla_plasapphire_1000_175_c": "0353BA",
    "polarfilament_pla_sapphire_1000_175_c": "043591"
  },
  "extruder_temp_range": {
    "polarfilament_pla_plasapphire_1000_175_c": [
      190,
      230
    ],
    "polarfilament_pla_sapphire_1000_175_c": [
      205,
      225
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_plasapphire_1000_175_c": [
      50,
      70
    ],
    "polarfilament_pla_sapphire_1000_175_c": [
      55,
      65
    ]
  }
}
```

### PO036: dup-2f1767baba4643f29f09aa415ad37c76e5358c6cfae3f07702eae21134bf9755

Status: APPROVED; survivor `polarfilament_pla_seafoam_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_plaseafoam_1000_175_c`|`PLA {color_name}`|`Seafoam`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|
|`polarfilament_pla_seafoam_1000_175_c`|`{color_name}`|`Seafoam`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_plaseafoam_1000_175_c": null,
    "polarfilament_pla_seafoam_1000_175_c": 190.0
  },
  "color_hex": {
    "polarfilament_pla_plaseafoam_1000_175_c": "00B4BC",
    "polarfilament_pla_seafoam_1000_175_c": "0a5e5e"
  },
  "extruder_temp_range": {
    "polarfilament_pla_plaseafoam_1000_175_c": [
      190,
      230
    ],
    "polarfilament_pla_seafoam_1000_175_c": [
      205,
      225
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_plaseafoam_1000_175_c": [
      50,
      70
    ],
    "polarfilament_pla_seafoam_1000_175_c": [
      55,
      65
    ]
  },
  "pattern": {
    "polarfilament_pla_plaseafoam_1000_175_c": null,
    "polarfilament_pla_seafoam_1000_175_c": "sparkle"
  }
}
```

### PO037: dup-fc523feaa42fdff22a4fe95b21c26f17cbac995335b1168d770cdcc0f4775e38

Status: APPROVED; survivor `polarfilament_pla_shamrock_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_plashamrock_1000_175_c`|`PLA {color_name}`|`Shamrock`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|
|`polarfilament_pla_shamrock_1000_175_c`|`{color_name}`|`Shamrock`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_plashamrock_1000_175_c": null,
    "polarfilament_pla_shamrock_1000_175_c": 190.0
  },
  "color_hex": {
    "polarfilament_pla_plashamrock_1000_175_c": "018E63",
    "polarfilament_pla_shamrock_1000_175_c": "148714"
  },
  "extruder_temp_range": {
    "polarfilament_pla_plashamrock_1000_175_c": [
      190,
      230
    ],
    "polarfilament_pla_shamrock_1000_175_c": [
      205,
      225
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_plashamrock_1000_175_c": [
      50,
      70
    ],
    "polarfilament_pla_shamrock_1000_175_c": [
      55,
      65
    ]
  }
}
```

### PO038: dup-4e8ba11c891c497b69005a6b073826432174d6d5a210355f7b770b1b55c46567

Status: APPROVED; survivor `polarfilament_pla_squid_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_plasquid_1000_175_c`|`PLA {color_name}`|`Squid`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|
|`polarfilament_pla_squid_1000_175_c`|`{color_name}`|`Squid`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_plasquid_1000_175_c": null,
    "polarfilament_pla_squid_1000_175_c": 190.0
  },
  "color_hex": {
    "polarfilament_pla_plasquid_1000_175_c": "00B4BC",
    "polarfilament_pla_squid_1000_175_c": "139677"
  },
  "extruder_temp_range": {
    "polarfilament_pla_plasquid_1000_175_c": [
      190,
      230
    ],
    "polarfilament_pla_squid_1000_175_c": [
      205,
      225
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_plasquid_1000_175_c": [
      50,
      70
    ],
    "polarfilament_pla_squid_1000_175_c": [
      55,
      65
    ]
  }
}
```

### PO039: dup-41c5a379b8c5a22db970e48c4df74bbe771e61fef114db465e3c1c0170adf68d

Status: APPROVED; survivor `polarfilament_pla_sunshineyellow_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_plasunshineyellow_1000_175_c`|`PLA {color_name}`|`Sunshine Yellow`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|
|`polarfilament_pla_sunshineyellow_1000_175_c`|`{color_name}`|`Sunshine Yellow`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_plasunshineyellow_1000_175_c": null,
    "polarfilament_pla_sunshineyellow_1000_175_c": 190.0
  },
  "color_hex": {
    "polarfilament_pla_plasunshineyellow_1000_175_c": "EFDC4C",
    "polarfilament_pla_sunshineyellow_1000_175_c": "F9E20C"
  },
  "extruder_temp_range": {
    "polarfilament_pla_plasunshineyellow_1000_175_c": [
      190,
      230
    ],
    "polarfilament_pla_sunshineyellow_1000_175_c": [
      205,
      225
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_plasunshineyellow_1000_175_c": [
      50,
      70
    ],
    "polarfilament_pla_sunshineyellow_1000_175_c": [
      55,
      65
    ]
  }
}
```

### PO040: dup-ee0e14444ac9efdcf3f47374f042a85f1fc356f7e6fe8e827310b52e46648e88

Status: APPROVED; survivor `polarfilament_pla_vividorange_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polarfilament_pla_plavividorange_1000_175_c`|`PLA {color_name}`|`Vivid Orange`|{"source_file": "polarfilament.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 36, "compiled_records": 36} / False|
|`polarfilament_pla_vividorange_1000_175_c`|`{color_name}`|`Vivid Orange`|{"source_file": "polarfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 33, "compiled_records": 33} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "polarfilament_pla_plavividorange_1000_175_c": null,
    "polarfilament_pla_vividorange_1000_175_c": 190.0
  },
  "color_hex": {
    "polarfilament_pla_plavividorange_1000_175_c": "FF5F2E",
    "polarfilament_pla_vividorange_1000_175_c": "C62A03"
  },
  "extruder_temp_range": {
    "polarfilament_pla_plavividorange_1000_175_c": [
      190,
      230
    ],
    "polarfilament_pla_vividorange_1000_175_c": [
      205,
      225
    ]
  },
  "bed_temp_range": {
    "polarfilament_pla_plavividorange_1000_175_c": [
      50,
      70
    ],
    "polarfilament_pla_vividorange_1000_175_c": [
      55,
      65
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

- `polarfilament_pla_opulentgold_1000_175_c` — Opulent Gold
- `polarfilament_pla_spaceship_1000_175_c` — Spaceship
- `polarfilament_asa_asagray_1000_175_c` — ASA Gray
- `polarfilament_pa12_pa12naturalnylon_1000_175_c` — PA12 Natural Nylon
- `polarfilament_pha_biodegradablephablack_1000_175_c` — Biodegradable Pha Black
- `polarfilament_pha_biodegradablephanatural_1000_175_c` — Biodegradable Pha Natural
- `polarfilament_pla_placolorchangingblue_1000_175_c` — PLA Color Changing Blue
- `polarfilament_pla_pladijonyellow_1000_175_c` — PLA Dijon Yellow
- `polarfilament_pla_plalavender_1000_175_c` — PLA Lavender
- `polarfilament_pla_planucleargreen_1000_175_c` — PLA Nuclear Green
- `polarfilament_pla_plaspaceshipsteel_1000_175_c` — PLA Spaceship Steel
- `polarfilament_tpu_biodegradableflexible95asofttpublack_1000_175_c` — Biodegradable Flexible 95A Soft TPU Black
- `polarfilament_tpu_biodegradableflexible95asofttpunatural_1000_175_c` — Biodegradable Flexible 95A Soft TPU Natural
- `polarfilament_tpu_tpucandyredflexible-60d_1000_175_c` — TPU Candy Red Flexible -60D
- `polarfilament_tpu_tpuclassicblackflexible-60d_1000_175_c` — TPU Classic Black Flexible -60D
- `polarfilament_tpu_tpulightblueflexible-60d_1000_175_c` — TPU Light Blue Flexible -60D
- `polarfilament_tpu_tpunaturalflexible-60d_1000_175_c` — TPU Natural Flexible -60D
- `polarfilament_tpu_tpushamrockflexible-60d_1000_175_c` — TPU Shamrock Flexible -60D
- `polarfilament_tpu_tpuvividorangeflexible-60d_1000_175_c` — TPU Vivid Orange Flexible -60D
