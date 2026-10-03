# 3de duplicate migration review

Base `f55246de37ab0e9381169a03ee4c9f03127a8525`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `c37ae75d49e0a8d936fbcaaa6b8bef6fe29d2cbe666ffe0b46ecb0e11f11fc78`.

## Authorization and result

{"groups": 3, "approved_groups": 3, "retired": 3, "deferred": 0, "hard_stops": 0, "before_count": 51715, "after_count": 51712, "brand_before": 1071, "brand_after": 1068, "registry_before": 1719, "registry_after": 1722, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Three candidates resolved by Rule3 before Rule4; no Cartesian-based decision. Printing/density conflicts internal to current pages remain unresolved, survivor values kept. Existing generic correct documentation collection retained. SurvivorWhite codes already mix2007021kg1.75/2507021kg2.85/2007912kg1.75 plusunbound200796; no new transfer/coverage claim. Packaging/tare unchanged.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://3deksperten.dk/products/flame-orange-3de-premium-pla-1-75mm", "note": "Official familyname; page conflicts1.24/190–210/45–60 vs1.23/190–220/35–60."}
- {"url": "https://3deksperten.dk/products/solid-white-3de-premium-petg-1-75mm", "note": "Official familyname; page conflicts density1.17–1.24 vs1.29 and bed60–80 vs40–70."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`3de_petg_premiumsolidblue_1000_175_p`|`3de_petg_premiumpetgsolidblue_1000_175_p`|`3de.json::3DE::Premium {color_name}::Premium Solid Blue::PETG::1000::1.75::plastic::False`|
|`3de_petg_premiumsolidwhite_1000_175_p`|`3de_petg_premiumpetgsolidwhite_1000_175_p`|`3de.json::3DE::Premium {color_name}::Premium Solid White::PETG::1000::1.75::plastic::False`|
|`3de_pla_premiumflameorange_1000_175_p`|`3de_pla_premiumplaflameorange_1000_175_p`|`3de.json::3DE::Premium {color_name}::Premium Flame Orange::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### DE001: dup-3bb6585802cd9b3d67467455561988dd69980b028bf2101eb2db05079f0619ec

Status: APPROVED; survivor `3de_petg_premiumpetgsolidblue_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3de_petg_premiumpetgsolidblue_1000_175_p`|`Premium PETG {color_name}`|`Solid Blue`|{"source_file": "3de.json", "definition_index": 12, "weights": 3, "diameters": 2, "colors": 36, "compiled_records": 216} / False|
|`3de_petg_premiumsolidblue_1000_175_p`|`Premium {color_name}`|`Solid Blue`|{"source_file": "3de.json", "definition_index": 39, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "3de_petg_premiumpetgsolidblue_1000_175_p": 1.17,
    "3de_petg_premiumsolidblue_1000_175_p": 1.24
  },
  "spool_weight": {
    "3de_petg_premiumpetgsolidblue_1000_175_p": 200,
    "3de_petg_premiumsolidblue_1000_175_p": null
  },
  "color_hex": {
    "3de_petg_premiumpetgsolidblue_1000_175_p": "005eb8",
    "3de_petg_premiumsolidblue_1000_175_p": "1B5FAA"
  },
  "extruder_temp_range": {
    "3de_petg_premiumpetgsolidblue_1000_175_p": [
      230,
      255
    ],
    "3de_petg_premiumsolidblue_1000_175_p": [
      220,
      240
    ]
  },
  "bed_temp_range": {
    "3de_petg_premiumpetgsolidblue_1000_175_p": [
      60,
      80
    ],
    "3de_petg_premiumsolidblue_1000_175_p": [
      40,
      70
    ]
  },
  "codes": {
    "3de_petg_premiumpetgsolidblue_1000_175_p": [
      "200713"
    ],
    "3de_petg_premiumsolidblue_1000_175_p": null
  }
}
```

### DE002: dup-86fe2c815f6ad055ce25c6956658d14aaa445006e7edd57d20b4348c0a7ef1ee

Status: APPROVED; survivor `3de_petg_premiumpetgsolidwhite_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3de_petg_premiumpetgsolidwhite_1000_175_p`|`Premium PETG {color_name}`|`Solid White`|{"source_file": "3de.json", "definition_index": 12, "weights": 3, "diameters": 2, "colors": 36, "compiled_records": 216} / False|
|`3de_petg_premiumsolidwhite_1000_175_p`|`Premium {color_name}`|`Solid White`|{"source_file": "3de.json", "definition_index": 39, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "3de_petg_premiumpetgsolidwhite_1000_175_p": 1.17,
    "3de_petg_premiumsolidwhite_1000_175_p": 1.24
  },
  "spool_weight": {
    "3de_petg_premiumpetgsolidwhite_1000_175_p": 200,
    "3de_petg_premiumsolidwhite_1000_175_p": null
  },
  "color_hex": {
    "3de_petg_premiumpetgsolidwhite_1000_175_p": "ffffff",
    "3de_petg_premiumsolidwhite_1000_175_p": "F2F0EB"
  },
  "extruder_temp_range": {
    "3de_petg_premiumpetgsolidwhite_1000_175_p": [
      230,
      255
    ],
    "3de_petg_premiumsolidwhite_1000_175_p": [
      220,
      240
    ]
  },
  "bed_temp_range": {
    "3de_petg_premiumpetgsolidwhite_1000_175_p": [
      60,
      80
    ],
    "3de_petg_premiumsolidwhite_1000_175_p": [
      40,
      70
    ]
  },
  "codes": {
    "3de_petg_premiumpetgsolidwhite_1000_175_p": [
      "250702",
      "200796",
      "200702",
      "200791"
    ],
    "3de_petg_premiumsolidwhite_1000_175_p": null
  }
}
```

### DE003: dup-d08c2256450e432b2d1251f6ed71c6094185ef2e95871edacbc40ccb3ea4a8ca

Status: APPROVED; survivor `3de_pla_premiumplaflameorange_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`3de_pla_premiumflameorange_1000_175_p`|`Premium {color_name}`|`Flame Orange`|{"source_file": "3de.json", "definition_index": 30, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / False|
|`3de_pla_premiumplaflameorange_1000_175_p`|`Premium PLA {color_name}`|`Flame Orange`|{"source_file": "3de.json", "definition_index": 23, "weights": 3, "diameters": 2, "colors": 41, "compiled_records": 246} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "3de_pla_premiumflameorange_1000_175_p": "FC8A17",
    "3de_pla_premiumplaflameorange_1000_175_p": "ff6900"
  },
  "extruder_temp_range": {
    "3de_pla_premiumflameorange_1000_175_p": [
      190,
      220
    ],
    "3de_pla_premiumplaflameorange_1000_175_p": [
      190,
      210
    ]
  },
  "bed_temp_range": {
    "3de_pla_premiumflameorange_1000_175_p": [
      35,
      60
    ],
    "3de_pla_premiumplaflameorange_1000_175_p": [
      45,
      60
    ]
  },
  "codes": {
    "3de_pla_premiumflameorange_1000_175_p": null,
    "3de_pla_premiumplaflameorange_1000_175_p": [
      "200030"
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

- `3de_abs_premiumabschoclatebrown_1000_175_p` — Premium ABS Choclate Brown
- `3de_abs_premiumabsdarkblue_1000_175_p` — Premium ABS Dark Blue
- `3de_abs_premiumabsemeraldgreen_1000_175_p` — Premium ABS Emerald Green
- `3de_abs_premiumabsflameorange_1000_175_p` — Premium ABS Flame Orange
- `3de_abs_premiumabsgeckogreen_1000_175_p` — Premium ABS Gecko Green
- `3de_abs_premiumabsleafgreen_1000_175_p` — Premium ABS Leaf Green
- `3de_abs_premiumabsleatherbrown_1000_175_p` — Premium ABS Leather Brown
- `3de_abs_premiumabsmailboxred_1000_175_p` — Premium ABS Mailbox Red
- `3de_abs_premiumabsnature_1000_175_p` — Premium ABS Nature
- `3de_abs_premiumabsnormalblue_1000_175_p` — Premium ABS Normal Blue
- `3de_abs_premiumabspirateblack_1000_175_p` — Premium ABS Pirate Black
- `3de_abs_premiumabssignalyellow_1000_175_p` — Premium ABS Signal Yellow
- `3de_abs_premiumabsslategrey_1000_175_p` — Premium ABS Slate Grey
- `3de_abs_premiumabssnowwhite_1000_175_p` — Premium ABS Snow White
- `3de_abs_premiumabsterminatorgrey_1000_175_p` — Premium ABS Terminator Grey
- `3de_abs_premiumabstransparent_1000_175_p` — Premium ABS Transparent
- `3de_abs_premiumabschoclatebrown_1000_285_p` — Premium ABS Choclate Brown
- `3de_abs_premiumabsdarkblue_1000_285_p` — Premium ABS Dark Blue
- `3de_abs_premiumabsemeraldgreen_1000_285_p` — Premium ABS Emerald Green
- `3de_abs_premiumabsflameorange_1000_285_p` — Premium ABS Flame Orange
- `3de_abs_premiumabsgeckogreen_1000_285_p` — Premium ABS Gecko Green
- `3de_abs_premiumabsleafgreen_1000_285_p` — Premium ABS Leaf Green
- `3de_abs_premiumabsleatherbrown_1000_285_p` — Premium ABS Leather Brown
- `3de_abs_premiumabsmailboxred_1000_285_p` — Premium ABS Mailbox Red
- `3de_abs_premiumabsnature_1000_285_p` — Premium ABS Nature
- `3de_abs_premiumabsnormalblue_1000_285_p` — Premium ABS Normal Blue
- `3de_abs_premiumabspirateblack_1000_285_p` — Premium ABS Pirate Black
- `3de_abs_premiumabssignalyellow_1000_285_p` — Premium ABS Signal Yellow
- `3de_abs_premiumabsslategrey_1000_285_p` — Premium ABS Slate Grey
- `3de_abs_premiumabssnowwhite_1000_285_p` — Premium ABS Snow White
- `3de_abs_premiumabsterminatorgrey_1000_285_p` — Premium ABS Terminator Grey
- `3de_abs_premiumabstransparent_1000_285_p` — Premium ABS Transparent
- `3de_asa_premiumasablack_1000_175_p` — Premium ASA Black
- `3de_asa_premiumasagrey_1000_175_p` — Premium ASA Grey
- `3de_asa_premiumasaslategrey_1000_175_p` — Premium ASA Slate Grey
- `3de_asa_premiumasawhite_1000_175_p` — Premium ASA White
- `3de_asa_premiumasablack_1000_285_p` — Premium ASA Black
- `3de_asa_premiumasagrey_1000_285_p` — Premium ASA Grey
- `3de_asa_premiumasaslategrey_1000_285_p` — Premium ASA Slate Grey
- `3de_asa_premiumasawhite_1000_285_p` — Premium ASA White
- `3de_nylon_premiumnylonblack_1000_175_p` — Premium NYLON Black
- `3de_nylon_premiumnylonwhite_1000_175_p` — Premium NYLON White
- `3de_nylon_premiumnylonblack_1000_285_p` — Premium NYLON Black
- `3de_nylon_premiumnylonwhite_1000_285_p` — Premium NYLON White
- `3de_pbt_premiumpbtavocadogreen_1000_175_p` — Premium PBT Avocado Green
- `3de_pbt_premiumpbtbluefish_1000_175_p` — Premium PBT Blue Fish
- `3de_pbt_premiumpbtcarbonblack_1000_175_p` — Premium PBT Carbon Black
- `3de_pbt_premiumpbtcyberyellow_1000_175_p` — Premium PBT Cyber Yellow
- `3de_pbt_premiumpbtgrey_1000_175_p` — Premium PBT Grey
- `3de_pbt_premiumpbthotred_1000_175_p` — Premium PBT Hot Red
- `3de_pbt_premiumpbtpirateblack_1000_175_p` — Premium PBT Pirate Black
- `3de_pbt_premiumpbtsnowwhite_1000_175_p` — Premium PBT Snow White
- `3de_pbt_premiumpbtwhite_1000_175_p` — Premium PBT White
- `3de_pbt_premiumpbtavocadogreen_1000_285_p` — Premium PBT Avocado Green
- `3de_pbt_premiumpbtbluefish_1000_285_p` — Premium PBT Blue Fish
- `3de_pbt_premiumpbtcarbonblack_1000_285_p` — Premium PBT Carbon Black
- `3de_pbt_premiumpbtcyberyellow_1000_285_p` — Premium PBT Cyber Yellow
- `3de_pbt_premiumpbtgrey_1000_285_p` — Premium PBT Grey
- `3de_pbt_premiumpbthotred_1000_285_p` — Premium PBT Hot Red
- `3de_pbt_premiumpbtpirateblack_1000_285_p` — Premium PBT Pirate Black
- `3de_pbt_premiumpbtsnowwhite_1000_285_p` — Premium PBT Snow White
- `3de_pbt_premiumpbtwhite_1000_285_p` — Premium PBT White
- `3de_pbt_premiumpbtavocadogreen_2000_175_p` — Premium PBT Avocado Green
- `3de_pbt_premiumpbtbluefish_2000_175_p` — Premium PBT Blue Fish
- `3de_pbt_premiumpbtcarbonblack_2000_175_p` — Premium PBT Carbon Black
- `3de_pbt_premiumpbtcyberyellow_2000_175_p` — Premium PBT Cyber Yellow
- `3de_pbt_premiumpbtgrey_2000_175_p` — Premium PBT Grey
- `3de_pbt_premiumpbthotred_2000_175_p` — Premium PBT Hot Red
- `3de_pbt_premiumpbtpirateblack_2000_175_p` — Premium PBT Pirate Black
- `3de_pbt_premiumpbtsnowwhite_2000_175_p` — Premium PBT Snow White
- `3de_pbt_premiumpbtwhite_2000_175_p` — Premium PBT White
- `3de_pbt_premiumpbtavocadogreen_2000_285_p` — Premium PBT Avocado Green
- `3de_pbt_premiumpbtbluefish_2000_285_p` — Premium PBT Blue Fish
- `3de_pbt_premiumpbtcarbonblack_2000_285_p` — Premium PBT Carbon Black
- `3de_pbt_premiumpbtcyberyellow_2000_285_p` — Premium PBT Cyber Yellow
- `3de_pbt_premiumpbtgrey_2000_285_p` — Premium PBT Grey
- `3de_pbt_premiumpbthotred_2000_285_p` — Premium PBT Hot Red
- `3de_pbt_premiumpbtpirateblack_2000_285_p` — Premium PBT Pirate Black
- `3de_pbt_premiumpbtsnowwhite_2000_285_p` — Premium PBT Snow White
- `3de_pbt_premiumpbtwhite_2000_285_p` — Premium PBT White
- `3de_pbt_premiumpbtavocadogreen_5000_175_p` — Premium PBT Avocado Green
- `3de_pbt_premiumpbtbluefish_5000_175_p` — Premium PBT Blue Fish
- `3de_pbt_premiumpbtcarbonblack_5000_175_p` — Premium PBT Carbon Black
- `3de_pbt_premiumpbtcyberyellow_5000_175_p` — Premium PBT Cyber Yellow
- `3de_pbt_premiumpbtgrey_5000_175_p` — Premium PBT Grey
- `3de_pbt_premiumpbthotred_5000_175_p` — Premium PBT Hot Red
- `3de_pbt_premiumpbtpirateblack_5000_175_p` — Premium PBT Pirate Black
- `3de_pbt_premiumpbtsnowwhite_5000_175_p` — Premium PBT Snow White
- `3de_pbt_premiumpbtwhite_5000_175_p` — Premium PBT White
- `3de_pbt_premiumpbtavocadogreen_5000_285_p` — Premium PBT Avocado Green
- `3de_pbt_premiumpbtbluefish_5000_285_p` — Premium PBT Blue Fish
- `3de_pbt_premiumpbtcarbonblack_5000_285_p` — Premium PBT Carbon Black
- `3de_pbt_premiumpbtcyberyellow_5000_285_p` — Premium PBT Cyber Yellow
- `3de_pbt_premiumpbtgrey_5000_285_p` — Premium PBT Grey
- `3de_pbt_premiumpbthotred_5000_285_p` — Premium PBT Hot Red
- `3de_pbt_premiumpbtpirateblack_5000_285_p` — Premium PBT Pirate Black
- `3de_pbt_premiumpbtsnowwhite_5000_285_p` — Premium PBT Snow White
- `3de_pbt_premiumpbtwhite_5000_285_p` — Premium PBT White
- `3de_pbt_premiumtoughpbtblack_1000_175_p` — Premium Tough PBT Black
- `3de_pc_premiumpbtpc-pbt-black_1000_175_p` — Premium PBT PC-PBT - Black
- `3de_pc_premiumpbtpc-pbt-white_1000_175_p` — Premium PBT PC-PBT - White
- `3de_pc_premiumpcblack_1000_175_p` — Premium PC Black
- `3de_pc_premiumpctransparent_1000_175_p` — Premium PC Transparent
- `3de_pc_premiumpcwhite_1000_175_p` — Premium PC White
- `3de_pc_premiumpcblack_1000_285_p` — Premium PC Black
- `3de_pc_premiumpctransparent_1000_285_p` — Premium PC Transparent
- `3de_pc_premiumpcwhite_1000_285_p` — Premium PC White
- `3de_pctg_premiumpctgfullyblack_1000_175_p` — Premium PCTG Fully Black
- `3de_pctg_premiumpctgfullywhite_1000_175_p` — Premium PCTG Fully White
- `3de_pet_premiumpethighspeedpet-blackdiamond_1000_175_c` — Premium PET High Speed PET - Black Diamond
- `3de_pet_premiumpethighspeedpet-whiteagat_1000_175_c` — Premium PET High Speed PET - White Agat
- `3de_petg_premiumcarbonfiberpetgcarbonfiberblack_1000_175_p` — Premium Carbon Fiber PETG Carbon Fiber Black
- `3de_petg_premiumcarbonfiberpetgcarbonfiberindigoblue_1000_175_p` — Premium Carbon Fiber PETG Carbon Fiber Indigo Blue
- `3de_petg_premiumglowplagreen_1000_175_p` — Premium Glow PLA Green
- `3de_petg_premiumopaquepetgblack_1000_175_p` — Premium Opaque PETG Black
- `3de_petg_premiumpetgaliengreen_1000_175_p` — Premium PETG Alien Green
- `3de_petg_premiumpetgblackinblue_1000_175_p` — Premium PETG Black in Blue
- `3de_petg_premiumpetgbudgetblack_1000_175_p` — Premium PETG Budget Black
- `3de_petg_premiumpetgbudgetwhite_1000_175_p` — Premium PETG Budget White
- `3de_petg_premiumpetgdarkgreen_1000_175_p` — Premium PETG Dark Green
- `3de_petg_premiumpetgdarkgrey_1000_175_p` — Premium PETG Dark Grey
- `3de_petg_premiumpetgfluorescentgreen-semi-transparent_1000_175_p` — Premium PETG Fluorescent Green - Semi-transparent
- `3de_petg_premiumpetgfluorescentorange-semi-transparent_1000_175_p` — Premium PETG Fluorescent Orange - Semi-transparent
- `3de_petg_premiumpetgfluorescentyellow-semi-transparent_1000_175_p` — Premium PETG Fluorescent Yellow - Semi-transparent
- `3de_petg_premiumpetgfluorescentyellow-solidcolor_1000_175_p` — Premium PETG Fluorescent Yellow - Solid Color
- `3de_petg_premiumpetghighspeedpetg-black_1000_175_p` — Premium PETG High Speed PETG - Black
- `3de_petg_premiumpetghighspeedpetg-blue_1000_175_p` — Premium PETG High Speed PETG - Blue
- `3de_petg_premiumpetghighspeedpetg-darkgrey_1000_175_p` — Premium PETG High Speed PETG - Dark Grey
- `3de_petg_premiumpetghighspeedpetg-green_1000_175_p` — Premium PETG High Speed PETG - Green
- `3de_petg_premiumpetghighspeedpetg-lightgrey_1000_175_p` — Premium PETG High Speed PETG - Light Grey
- `3de_petg_premiumpetghighspeedpetg-orange_1000_175_p` — Premium PETG High Speed PETG - Orange
- `3de_petg_premiumpetghighspeedpetg-red_1000_175_p` — Premium PETG High Speed PETG - Red
- `3de_petg_premiumpetghighspeedpetg-white_1000_175_p` — Premium PETG High Speed PETG - White
- `3de_petg_premiumpetghighspeedpetg-yellow_1000_175_p` — Premium PETG High Speed PETG - Yellow
- `3de_petg_premiumpetgpetgmagic-blue,greenandgold_1000_175_p` — Premium PETG PETG Magic - Blue, Green and Gold
- `3de_petg_premiumpetgpetgmagic-gold,redandpurple_1000_175_p` — Premium PETG PETG Magic - Gold, Red and Purple
- `3de_petg_premiumpetgpetgmagic-red,purpleandblue_1000_175_p` — Premium PETG PETG Magic - Red, Purple and Blue
- `3de_petg_premiumpetgpurple_1000_175_p` — Premium PETG Purple
- `3de_petg_premiumpetgsolidblack_1000_175_p` — Premium PETG Solid Black
- `3de_petg_premiumpetgsolidgreen_1000_175_p` — Premium PETG Solid Green
- `3de_petg_premiumpetgsolidorange_1000_175_p` — Premium PETG Solid Orange
- `3de_petg_premiumpetgsolidred_1000_175_p` — Premium PETG Solid Red
- `3de_petg_premiumpetgsolidtoolgreen_1000_175_p` — Premium PETG Solid Tool Green
- `3de_petg_premiumpetgsolidwarmyellow_1000_175_p` — Premium PETG Solid Warm Yellow
- `3de_petg_premiumpetgsolidwaterblue_1000_175_p` — Premium PETG Solid Water Blue
- `3de_petg_premiumpetgsolidyellow_1000_175_p` — Premium PETG Solid Yellow
- `3de_petg_premiumpetgsort_1000_175_p` — Premium PETG Sort
- `3de_petg_premiumpetgtransparent_1000_175_p` — Premium PETG Transparent
- `3de_petg_premiumpetgwhite_1000_175_p` — Premium PETG White
- `3de_petg_premiumpetgaliengreen_1000_285_p` — Premium PETG Alien Green
- `3de_petg_premiumpetgblackinblue_1000_285_p` — Premium PETG Black in Blue
- `3de_petg_premiumpetgbudgetblack_1000_285_p` — Premium PETG Budget Black
- `3de_petg_premiumpetgbudgetwhite_1000_285_p` — Premium PETG Budget White
- `3de_petg_premiumpetgdarkgreen_1000_285_p` — Premium PETG Dark Green
- `3de_petg_premiumpetgdarkgrey_1000_285_p` — Premium PETG Dark Grey
- `3de_petg_premiumpetgfluorescentgreen-semi-transparent_1000_285_p` — Premium PETG Fluorescent Green - Semi-transparent
- `3de_petg_premiumpetgfluorescentorange-semi-transparent_1000_285_p` — Premium PETG Fluorescent Orange - Semi-transparent
- `3de_petg_premiumpetgfluorescentyellow-semi-transparent_1000_285_p` — Premium PETG Fluorescent Yellow - Semi-transparent
- `3de_petg_premiumpetgfluorescentyellow-solidcolor_1000_285_p` — Premium PETG Fluorescent Yellow - Solid Color
- `3de_petg_premiumpetghighspeedpetg-black_1000_285_p` — Premium PETG High Speed PETG - Black
- `3de_petg_premiumpetghighspeedpetg-blue_1000_285_p` — Premium PETG High Speed PETG - Blue
- `3de_petg_premiumpetghighspeedpetg-darkgrey_1000_285_p` — Premium PETG High Speed PETG - Dark Grey
- `3de_petg_premiumpetghighspeedpetg-green_1000_285_p` — Premium PETG High Speed PETG - Green
- `3de_petg_premiumpetghighspeedpetg-lightgrey_1000_285_p` — Premium PETG High Speed PETG - Light Grey
- `3de_petg_premiumpetghighspeedpetg-orange_1000_285_p` — Premium PETG High Speed PETG - Orange
- `3de_petg_premiumpetghighspeedpetg-red_1000_285_p` — Premium PETG High Speed PETG - Red
- `3de_petg_premiumpetghighspeedpetg-white_1000_285_p` — Premium PETG High Speed PETG - White
- `3de_petg_premiumpetghighspeedpetg-yellow_1000_285_p` — Premium PETG High Speed PETG - Yellow
- `3de_petg_premiumpetgpetgmagic-blue,greenandgold_1000_285_p` — Premium PETG PETG Magic - Blue, Green and Gold
- `3de_petg_premiumpetgpetgmagic-gold,redandpurple_1000_285_p` — Premium PETG PETG Magic - Gold, Red and Purple
- `3de_petg_premiumpetgpetgmagic-red,purpleandblue_1000_285_p` — Premium PETG PETG Magic - Red, Purple and Blue
- `3de_petg_premiumpetgpurple_1000_285_p` — Premium PETG Purple
- `3de_petg_premiumpetgsolidblack_1000_285_p` — Premium PETG Solid Black
- `3de_petg_premiumpetgsolidblue_1000_285_p` — Premium PETG Solid Blue
- `3de_petg_premiumpetgsolidgreen_1000_285_p` — Premium PETG Solid Green
- `3de_petg_premiumpetgsolidorange_1000_285_p` — Premium PETG Solid Orange
- `3de_petg_premiumpetgsolidred_1000_285_p` — Premium PETG Solid Red
- `3de_petg_premiumpetgsolidtoolgreen_1000_285_p` — Premium PETG Solid Tool Green
- `3de_petg_premiumpetgsolidwarmyellow_1000_285_p` — Premium PETG Solid Warm Yellow
- `3de_petg_premiumpetgsolidwaterblue_1000_285_p` — Premium PETG Solid Water Blue
- `3de_petg_premiumpetgsolidwhite_1000_285_p` — Premium PETG Solid White
- `3de_petg_premiumpetgsolidyellow_1000_285_p` — Premium PETG Solid Yellow
- `3de_petg_premiumpetgsort_1000_285_p` — Premium PETG Sort
- `3de_petg_premiumpetgtransparent_1000_285_p` — Premium PETG Transparent
- `3de_petg_premiumpetgwhite_1000_285_p` — Premium PETG White
- `3de_petg_premiumpetgaliengreen_2000_175_p` — Premium PETG Alien Green
- `3de_petg_premiumpetgblackinblue_2000_175_p` — Premium PETG Black in Blue
- `3de_petg_premiumpetgbudgetblack_2000_175_p` — Premium PETG Budget Black
- `3de_petg_premiumpetgbudgetwhite_2000_175_p` — Premium PETG Budget White
- `3de_petg_premiumpetgdarkgreen_2000_175_p` — Premium PETG Dark Green
- `3de_petg_premiumpetgdarkgrey_2000_175_p` — Premium PETG Dark Grey
- `3de_petg_premiumpetgfluorescentgreen-semi-transparent_2000_175_p` — Premium PETG Fluorescent Green - Semi-transparent
- `3de_petg_premiumpetgfluorescentorange-semi-transparent_2000_175_p` — Premium PETG Fluorescent Orange - Semi-transparent
- `3de_petg_premiumpetgfluorescentyellow-semi-transparent_2000_175_p` — Premium PETG Fluorescent Yellow - Semi-transparent
- `3de_petg_premiumpetgfluorescentyellow-solidcolor_2000_175_p` — Premium PETG Fluorescent Yellow - Solid Color
- `3de_petg_premiumpetghighspeedpetg-black_2000_175_p` — Premium PETG High Speed PETG - Black
- `3de_petg_premiumpetghighspeedpetg-blue_2000_175_p` — Premium PETG High Speed PETG - Blue
- `3de_petg_premiumpetghighspeedpetg-darkgrey_2000_175_p` — Premium PETG High Speed PETG - Dark Grey
- `3de_petg_premiumpetghighspeedpetg-green_2000_175_p` — Premium PETG High Speed PETG - Green
- `3de_petg_premiumpetghighspeedpetg-lightgrey_2000_175_p` — Premium PETG High Speed PETG - Light Grey
- `3de_petg_premiumpetghighspeedpetg-orange_2000_175_p` — Premium PETG High Speed PETG - Orange
- `3de_petg_premiumpetghighspeedpetg-red_2000_175_p` — Premium PETG High Speed PETG - Red
- `3de_petg_premiumpetghighspeedpetg-white_2000_175_p` — Premium PETG High Speed PETG - White
- `3de_petg_premiumpetghighspeedpetg-yellow_2000_175_p` — Premium PETG High Speed PETG - Yellow
- `3de_petg_premiumpetgpetgmagic-blue,greenandgold_2000_175_p` — Premium PETG PETG Magic - Blue, Green and Gold
- `3de_petg_premiumpetgpetgmagic-gold,redandpurple_2000_175_p` — Premium PETG PETG Magic - Gold, Red and Purple
- `3de_petg_premiumpetgpetgmagic-red,purpleandblue_2000_175_p` — Premium PETG PETG Magic - Red, Purple and Blue
- `3de_petg_premiumpetgpurple_2000_175_p` — Premium PETG Purple
- `3de_petg_premiumpetgsolidblack_2000_175_p` — Premium PETG Solid Black
- `3de_petg_premiumpetgsolidblue_2000_175_p` — Premium PETG Solid Blue
- `3de_petg_premiumpetgsolidgreen_2000_175_p` — Premium PETG Solid Green
- `3de_petg_premiumpetgsolidorange_2000_175_p` — Premium PETG Solid Orange
- `3de_petg_premiumpetgsolidred_2000_175_p` — Premium PETG Solid Red
- `3de_petg_premiumpetgsolidtoolgreen_2000_175_p` — Premium PETG Solid Tool Green
- `3de_petg_premiumpetgsolidwarmyellow_2000_175_p` — Premium PETG Solid Warm Yellow
- `3de_petg_premiumpetgsolidwaterblue_2000_175_p` — Premium PETG Solid Water Blue
- `3de_petg_premiumpetgsolidwhite_2000_175_p` — Premium PETG Solid White
- `3de_petg_premiumpetgsolidyellow_2000_175_p` — Premium PETG Solid Yellow
- `3de_petg_premiumpetgsort_2000_175_p` — Premium PETG Sort
- `3de_petg_premiumpetgtransparent_2000_175_p` — Premium PETG Transparent
- `3de_petg_premiumpetgwhite_2000_175_p` — Premium PETG White
- `3de_petg_premiumpetgaliengreen_2000_285_p` — Premium PETG Alien Green
- `3de_petg_premiumpetgblackinblue_2000_285_p` — Premium PETG Black in Blue
- `3de_petg_premiumpetgbudgetblack_2000_285_p` — Premium PETG Budget Black
- `3de_petg_premiumpetgbudgetwhite_2000_285_p` — Premium PETG Budget White
- `3de_petg_premiumpetgdarkgreen_2000_285_p` — Premium PETG Dark Green
- `3de_petg_premiumpetgdarkgrey_2000_285_p` — Premium PETG Dark Grey
- `3de_petg_premiumpetgfluorescentgreen-semi-transparent_2000_285_p` — Premium PETG Fluorescent Green - Semi-transparent
- `3de_petg_premiumpetgfluorescentorange-semi-transparent_2000_285_p` — Premium PETG Fluorescent Orange - Semi-transparent
- `3de_petg_premiumpetgfluorescentyellow-semi-transparent_2000_285_p` — Premium PETG Fluorescent Yellow - Semi-transparent
- `3de_petg_premiumpetgfluorescentyellow-solidcolor_2000_285_p` — Premium PETG Fluorescent Yellow - Solid Color
- `3de_petg_premiumpetghighspeedpetg-black_2000_285_p` — Premium PETG High Speed PETG - Black
- `3de_petg_premiumpetghighspeedpetg-blue_2000_285_p` — Premium PETG High Speed PETG - Blue
- `3de_petg_premiumpetghighspeedpetg-darkgrey_2000_285_p` — Premium PETG High Speed PETG - Dark Grey
- `3de_petg_premiumpetghighspeedpetg-green_2000_285_p` — Premium PETG High Speed PETG - Green
- `3de_petg_premiumpetghighspeedpetg-lightgrey_2000_285_p` — Premium PETG High Speed PETG - Light Grey
- `3de_petg_premiumpetghighspeedpetg-orange_2000_285_p` — Premium PETG High Speed PETG - Orange
- `3de_petg_premiumpetghighspeedpetg-red_2000_285_p` — Premium PETG High Speed PETG - Red
- `3de_petg_premiumpetghighspeedpetg-white_2000_285_p` — Premium PETG High Speed PETG - White
- `3de_petg_premiumpetghighspeedpetg-yellow_2000_285_p` — Premium PETG High Speed PETG - Yellow
- `3de_petg_premiumpetgpetgmagic-blue,greenandgold_2000_285_p` — Premium PETG PETG Magic - Blue, Green and Gold
- `3de_petg_premiumpetgpetgmagic-gold,redandpurple_2000_285_p` — Premium PETG PETG Magic - Gold, Red and Purple
- `3de_petg_premiumpetgpetgmagic-red,purpleandblue_2000_285_p` — Premium PETG PETG Magic - Red, Purple and Blue
- `3de_petg_premiumpetgpurple_2000_285_p` — Premium PETG Purple
- `3de_petg_premiumpetgsolidblack_2000_285_p` — Premium PETG Solid Black
- `3de_petg_premiumpetgsolidblue_2000_285_p` — Premium PETG Solid Blue
- `3de_petg_premiumpetgsolidgreen_2000_285_p` — Premium PETG Solid Green
- `3de_petg_premiumpetgsolidorange_2000_285_p` — Premium PETG Solid Orange
- `3de_petg_premiumpetgsolidred_2000_285_p` — Premium PETG Solid Red
- `3de_petg_premiumpetgsolidtoolgreen_2000_285_p` — Premium PETG Solid Tool Green
- `3de_petg_premiumpetgsolidwarmyellow_2000_285_p` — Premium PETG Solid Warm Yellow
- `3de_petg_premiumpetgsolidwaterblue_2000_285_p` — Premium PETG Solid Water Blue
- `3de_petg_premiumpetgsolidwhite_2000_285_p` — Premium PETG Solid White
- `3de_petg_premiumpetgsolidyellow_2000_285_p` — Premium PETG Solid Yellow
- `3de_petg_premiumpetgsort_2000_285_p` — Premium PETG Sort
- `3de_petg_premiumpetgtransparent_2000_285_p` — Premium PETG Transparent
- `3de_petg_premiumpetgwhite_2000_285_p` — Premium PETG White
- `3de_petg_premiumpetgaliengreen_5000_175_p` — Premium PETG Alien Green
- `3de_petg_premiumpetgblackinblue_5000_175_p` — Premium PETG Black in Blue
- `3de_petg_premiumpetgbudgetblack_5000_175_p` — Premium PETG Budget Black
- `3de_petg_premiumpetgbudgetwhite_5000_175_p` — Premium PETG Budget White
- `3de_petg_premiumpetgdarkgreen_5000_175_p` — Premium PETG Dark Green
- `3de_petg_premiumpetgdarkgrey_5000_175_p` — Premium PETG Dark Grey
- `3de_petg_premiumpetgfluorescentgreen-semi-transparent_5000_175_p` — Premium PETG Fluorescent Green - Semi-transparent
- `3de_petg_premiumpetgfluorescentorange-semi-transparent_5000_175_p` — Premium PETG Fluorescent Orange - Semi-transparent
- `3de_petg_premiumpetgfluorescentyellow-semi-transparent_5000_175_p` — Premium PETG Fluorescent Yellow - Semi-transparent
- `3de_petg_premiumpetgfluorescentyellow-solidcolor_5000_175_p` — Premium PETG Fluorescent Yellow - Solid Color
- `3de_petg_premiumpetghighspeedpetg-black_5000_175_p` — Premium PETG High Speed PETG - Black
- `3de_petg_premiumpetghighspeedpetg-blue_5000_175_p` — Premium PETG High Speed PETG - Blue
- `3de_petg_premiumpetghighspeedpetg-darkgrey_5000_175_p` — Premium PETG High Speed PETG - Dark Grey
- `3de_petg_premiumpetghighspeedpetg-green_5000_175_p` — Premium PETG High Speed PETG - Green
- `3de_petg_premiumpetghighspeedpetg-lightgrey_5000_175_p` — Premium PETG High Speed PETG - Light Grey
- `3de_petg_premiumpetghighspeedpetg-orange_5000_175_p` — Premium PETG High Speed PETG - Orange
- `3de_petg_premiumpetghighspeedpetg-red_5000_175_p` — Premium PETG High Speed PETG - Red
- `3de_petg_premiumpetghighspeedpetg-white_5000_175_p` — Premium PETG High Speed PETG - White
- `3de_petg_premiumpetghighspeedpetg-yellow_5000_175_p` — Premium PETG High Speed PETG - Yellow
- `3de_petg_premiumpetgpetgmagic-blue,greenandgold_5000_175_p` — Premium PETG PETG Magic - Blue, Green and Gold
- `3de_petg_premiumpetgpetgmagic-gold,redandpurple_5000_175_p` — Premium PETG PETG Magic - Gold, Red and Purple
- `3de_petg_premiumpetgpetgmagic-red,purpleandblue_5000_175_p` — Premium PETG PETG Magic - Red, Purple and Blue
- `3de_petg_premiumpetgpurple_5000_175_p` — Premium PETG Purple
- `3de_petg_premiumpetgsolidblack_5000_175_p` — Premium PETG Solid Black
- `3de_petg_premiumpetgsolidblue_5000_175_p` — Premium PETG Solid Blue
- `3de_petg_premiumpetgsolidgreen_5000_175_p` — Premium PETG Solid Green
- `3de_petg_premiumpetgsolidorange_5000_175_p` — Premium PETG Solid Orange
- `3de_petg_premiumpetgsolidred_5000_175_p` — Premium PETG Solid Red
- `3de_petg_premiumpetgsolidtoolgreen_5000_175_p` — Premium PETG Solid Tool Green
- `3de_petg_premiumpetgsolidwarmyellow_5000_175_p` — Premium PETG Solid Warm Yellow
- `3de_petg_premiumpetgsolidwaterblue_5000_175_p` — Premium PETG Solid Water Blue
- `3de_petg_premiumpetgsolidwhite_5000_175_p` — Premium PETG Solid White
- `3de_petg_premiumpetgsolidyellow_5000_175_p` — Premium PETG Solid Yellow
- `3de_petg_premiumpetgsort_5000_175_p` — Premium PETG Sort
- `3de_petg_premiumpetgtransparent_5000_175_p` — Premium PETG Transparent
- `3de_petg_premiumpetgwhite_5000_175_p` — Premium PETG White
- `3de_petg_premiumpetgaliengreen_5000_285_p` — Premium PETG Alien Green
- `3de_petg_premiumpetgblackinblue_5000_285_p` — Premium PETG Black in Blue
- `3de_petg_premiumpetgbudgetblack_5000_285_p` — Premium PETG Budget Black
- `3de_petg_premiumpetgbudgetwhite_5000_285_p` — Premium PETG Budget White
- `3de_petg_premiumpetgdarkgreen_5000_285_p` — Premium PETG Dark Green
- `3de_petg_premiumpetgdarkgrey_5000_285_p` — Premium PETG Dark Grey
- `3de_petg_premiumpetgfluorescentgreen-semi-transparent_5000_285_p` — Premium PETG Fluorescent Green - Semi-transparent
- `3de_petg_premiumpetgfluorescentorange-semi-transparent_5000_285_p` — Premium PETG Fluorescent Orange - Semi-transparent
- `3de_petg_premiumpetgfluorescentyellow-semi-transparent_5000_285_p` — Premium PETG Fluorescent Yellow - Semi-transparent
- `3de_petg_premiumpetgfluorescentyellow-solidcolor_5000_285_p` — Premium PETG Fluorescent Yellow - Solid Color
- `3de_petg_premiumpetghighspeedpetg-black_5000_285_p` — Premium PETG High Speed PETG - Black
- `3de_petg_premiumpetghighspeedpetg-blue_5000_285_p` — Premium PETG High Speed PETG - Blue
- `3de_petg_premiumpetghighspeedpetg-darkgrey_5000_285_p` — Premium PETG High Speed PETG - Dark Grey
- `3de_petg_premiumpetghighspeedpetg-green_5000_285_p` — Premium PETG High Speed PETG - Green
- `3de_petg_premiumpetghighspeedpetg-lightgrey_5000_285_p` — Premium PETG High Speed PETG - Light Grey
- `3de_petg_premiumpetghighspeedpetg-orange_5000_285_p` — Premium PETG High Speed PETG - Orange
- `3de_petg_premiumpetghighspeedpetg-red_5000_285_p` — Premium PETG High Speed PETG - Red
- `3de_petg_premiumpetghighspeedpetg-white_5000_285_p` — Premium PETG High Speed PETG - White
- `3de_petg_premiumpetghighspeedpetg-yellow_5000_285_p` — Premium PETG High Speed PETG - Yellow
- `3de_petg_premiumpetgpetgmagic-blue,greenandgold_5000_285_p` — Premium PETG PETG Magic - Blue, Green and Gold
- `3de_petg_premiumpetgpetgmagic-gold,redandpurple_5000_285_p` — Premium PETG PETG Magic - Gold, Red and Purple
- `3de_petg_premiumpetgpetgmagic-red,purpleandblue_5000_285_p` — Premium PETG PETG Magic - Red, Purple and Blue
- `3de_petg_premiumpetgpurple_5000_285_p` — Premium PETG Purple
- `3de_petg_premiumpetgsolidblack_5000_285_p` — Premium PETG Solid Black
- `3de_petg_premiumpetgsolidblue_5000_285_p` — Premium PETG Solid Blue
- `3de_petg_premiumpetgsolidgreen_5000_285_p` — Premium PETG Solid Green
- `3de_petg_premiumpetgsolidorange_5000_285_p` — Premium PETG Solid Orange
- `3de_petg_premiumpetgsolidred_5000_285_p` — Premium PETG Solid Red
- `3de_petg_premiumpetgsolidtoolgreen_5000_285_p` — Premium PETG Solid Tool Green
- `3de_petg_premiumpetgsolidwarmyellow_5000_285_p` — Premium PETG Solid Warm Yellow
- `3de_petg_premiumpetgsolidwaterblue_5000_285_p` — Premium PETG Solid Water Blue
- `3de_petg_premiumpetgsolidwhite_5000_285_p` — Premium PETG Solid White
- `3de_petg_premiumpetgsolidyellow_5000_285_p` — Premium PETG Solid Yellow
- `3de_petg_premiumpetgsort_5000_285_p` — Premium PETG Sort
- `3de_petg_premiumpetgtransparent_5000_285_p` — Premium PETG Transparent
- `3de_petg_premiumpetgwhite_5000_285_p` — Premium PETG White
- `3de_petg_premiumpropetgblack_1000_175_p` — Premium PRO PETG Black
- `3de_petg_premiumpropetggrey_1000_175_p` — Premium PRO PETG Grey
- `3de_petg_premiumpropetgwhite_1000_175_p` — Premium PRO PETG White
- `3de_petg_premiumpropetgblack_2000_175_p` — Premium PRO PETG Black
- `3de_petg_premiumpropetggrey_2000_175_p` — Premium PRO PETG Grey
- `3de_petg_premiumpropetgwhite_2000_175_p` — Premium PRO PETG White
- `3de_pla_maxplabarbadoscherry_1000_175_p` — MAX PLA Barbados Cherry
- `3de_pla_maxplablack_1000_175_p` — MAX PLA Black
- `3de_pla_maxplablue_1000_175_p` — MAX PLA Blue
- `3de_pla_maxplabone_1000_175_p` — MAX PLA Bone
- `3de_pla_maxplacappucino_1000_175_p` — MAX PLA Cappucino
- `3de_pla_maxplachilired_1000_175_p` — MAX PLA Chili Red
- `3de_pla_maxplacoffeebrown_1000_175_p` — MAX PLA Coffee Brown
- `3de_pla_maxplacoldwhite_1000_175_p` — MAX PLA Cold White
- `3de_pla_maxpladarkgrey_1000_175_p` — MAX PLA Dark Grey
- `3de_pla_maxpladesertbeige_1000_175_p` — MAX PLA Desert Beige
- `3de_pla_maxpladustyrose_1000_175_p` — MAX PLA Dusty Rose
- `3de_pla_maxplaeveningsand_1000_175_p` — MAX PLA Evening Sand
- `3de_pla_maxplafluorescentgreen_1000_175_p` — MAX PLA Fluorescent Green
- `3de_pla_maxplafluorescentorange_1000_175_p` — MAX PLA Fluorescent Orange
- `3de_pla_maxplafluorescentyellow_1000_175_p` — MAX PLA Fluorescent Yellow
- `3de_pla_maxplagrassgreen_1000_175_p` — MAX PLA Grass Green
- `3de_pla_maxplagreen_1000_175_p` — MAX PLA Green
- `3de_pla_maxplagreenginfruit_1000_175_p` — MAX PLA Green Gin Fruit
- `3de_pla_maxplagreen-blueslate_1000_175_p` — MAX PLA Green-Blue Slate
- `3de_pla_maxplagreige_1000_175_p` — MAX PLA Greige
- `3de_pla_maxplagunmetal_1000_175_p` — MAX PLA Gun Metal
- `3de_pla_maxplajadegreen_1000_175_p` — MAX PLA Jade Green
- `3de_pla_maxplalemonyellow_1000_175_p` — MAX PLA Lemon Yellow
- `3de_pla_maxplalightgrey_1000_175_p` — MAX PLA Light Grey
- `3de_pla_maxplaoceanblue_1000_175_p` — MAX PLA Ocean Blue
- `3de_pla_maxplaolivegreen_1000_175_p` — MAX PLA Olive Green
- `3de_pla_maxplaorange_1000_175_p` — MAX PLA Orange
- `3de_pla_maxplapacificturquoise_1000_175_p` — MAX PLA Pacific Turquoise
- `3de_pla_maxplapopulargreen_1000_175_p` — MAX PLA Popular Green
- `3de_pla_maxplapureblack_1000_175_p` — MAX PLA Pure Black
- `3de_pla_maxplapuregold_1000_175_p` — MAX PLA Pure Gold
- `3de_pla_maxplapurewhite_1000_175_p` — MAX PLA Pure White
- `3de_pla_maxplared_1000_175_p` — MAX PLA Red
- `3de_pla_maxplaroyalblue_1000_175_p` — MAX PLA Royal Blue
- `3de_pla_maxplashadowgrey_1000_175_p` — MAX PLA Shadow Grey
- `3de_pla_maxplaskyblue_1000_175_p` — MAX PLA Sky Blue
- `3de_pla_maxplasoliddeeppurple_1000_175_p` — MAX PLA Solid Deep Purple
- `3de_pla_maxplasummerskyblue_1000_175_p` — MAX PLA Summer Sky Blue
- `3de_pla_maxplathundergrey_1000_175_p` — MAX PLA Thunder Grey
- `3de_pla_maxplatrueorange_1000_175_p` — MAX PLA True Orange
- `3de_pla_maxplawalnutbrown_1000_175_p` — MAX PLA Walnut Brown
- `3de_pla_maxplawarmwhite_1000_175_p` — MAX PLA Warm White
- `3de_pla_maxplawarmyellow_1000_175_p` — MAX PLA Warm Yellow
- `3de_pla_maxplawhite_1000_175_p` — MAX PLA White
- `3de_pla_maxplayellow_1000_175_p` — MAX PLA Yellow
- `3de_pla_maxplabarbadoscherry_1000_285_p` — MAX PLA Barbados Cherry
- `3de_pla_maxplablack_1000_285_p` — MAX PLA Black
- `3de_pla_maxplablue_1000_285_p` — MAX PLA Blue
- `3de_pla_maxplabone_1000_285_p` — MAX PLA Bone
- `3de_pla_maxplacappucino_1000_285_p` — MAX PLA Cappucino
- `3de_pla_maxplachilired_1000_285_p` — MAX PLA Chili Red
- `3de_pla_maxplacoffeebrown_1000_285_p` — MAX PLA Coffee Brown
- `3de_pla_maxplacoldwhite_1000_285_p` — MAX PLA Cold White
- `3de_pla_maxpladarkgrey_1000_285_p` — MAX PLA Dark Grey
- `3de_pla_maxpladesertbeige_1000_285_p` — MAX PLA Desert Beige
- `3de_pla_maxpladustyrose_1000_285_p` — MAX PLA Dusty Rose
- `3de_pla_maxplaeveningsand_1000_285_p` — MAX PLA Evening Sand
- `3de_pla_maxplafluorescentgreen_1000_285_p` — MAX PLA Fluorescent Green
- `3de_pla_maxplafluorescentorange_1000_285_p` — MAX PLA Fluorescent Orange
- `3de_pla_maxplafluorescentyellow_1000_285_p` — MAX PLA Fluorescent Yellow
- `3de_pla_maxplagrassgreen_1000_285_p` — MAX PLA Grass Green
- `3de_pla_maxplagreen_1000_285_p` — MAX PLA Green
- `3de_pla_maxplagreenginfruit_1000_285_p` — MAX PLA Green Gin Fruit
- `3de_pla_maxplagreen-blueslate_1000_285_p` — MAX PLA Green-Blue Slate
- `3de_pla_maxplagreige_1000_285_p` — MAX PLA Greige
- `3de_pla_maxplagunmetal_1000_285_p` — MAX PLA Gun Metal
- `3de_pla_maxplajadegreen_1000_285_p` — MAX PLA Jade Green
- `3de_pla_maxplalemonyellow_1000_285_p` — MAX PLA Lemon Yellow
- `3de_pla_maxplalightgrey_1000_285_p` — MAX PLA Light Grey
- `3de_pla_maxplaoceanblue_1000_285_p` — MAX PLA Ocean Blue
- `3de_pla_maxplaolivegreen_1000_285_p` — MAX PLA Olive Green
- `3de_pla_maxplaorange_1000_285_p` — MAX PLA Orange
- `3de_pla_maxplapacificturquoise_1000_285_p` — MAX PLA Pacific Turquoise
- `3de_pla_maxplapopulargreen_1000_285_p` — MAX PLA Popular Green
- `3de_pla_maxplapureblack_1000_285_p` — MAX PLA Pure Black
- `3de_pla_maxplapuregold_1000_285_p` — MAX PLA Pure Gold
- `3de_pla_maxplapurewhite_1000_285_p` — MAX PLA Pure White
- `3de_pla_maxplared_1000_285_p` — MAX PLA Red
- `3de_pla_maxplaroyalblue_1000_285_p` — MAX PLA Royal Blue
- `3de_pla_maxplashadowgrey_1000_285_p` — MAX PLA Shadow Grey
- `3de_pla_maxplaskyblue_1000_285_p` — MAX PLA Sky Blue
- `3de_pla_maxplasoliddeeppurple_1000_285_p` — MAX PLA Solid Deep Purple
- `3de_pla_maxplasummerskyblue_1000_285_p` — MAX PLA Summer Sky Blue
- `3de_pla_maxplathundergrey_1000_285_p` — MAX PLA Thunder Grey
- `3de_pla_maxplatrueorange_1000_285_p` — MAX PLA True Orange
- `3de_pla_maxplawalnutbrown_1000_285_p` — MAX PLA Walnut Brown
- `3de_pla_maxplawarmwhite_1000_285_p` — MAX PLA Warm White
- `3de_pla_maxplawarmyellow_1000_285_p` — MAX PLA Warm Yellow
- `3de_pla_maxplawhite_1000_285_p` — MAX PLA White
- `3de_pla_maxplayellow_1000_285_p` — MAX PLA Yellow
- `3de_pla_maxplabarbadoscherry_2000_175_p` — MAX PLA Barbados Cherry
- `3de_pla_maxplablack_2000_175_p` — MAX PLA Black
- `3de_pla_maxplablue_2000_175_p` — MAX PLA Blue
- `3de_pla_maxplabone_2000_175_p` — MAX PLA Bone
- `3de_pla_maxplacappucino_2000_175_p` — MAX PLA Cappucino
- `3de_pla_maxplachilired_2000_175_p` — MAX PLA Chili Red
- `3de_pla_maxplacoffeebrown_2000_175_p` — MAX PLA Coffee Brown
- `3de_pla_maxplacoldwhite_2000_175_p` — MAX PLA Cold White
- `3de_pla_maxpladarkgrey_2000_175_p` — MAX PLA Dark Grey
- `3de_pla_maxpladesertbeige_2000_175_p` — MAX PLA Desert Beige
- `3de_pla_maxpladustyrose_2000_175_p` — MAX PLA Dusty Rose
- `3de_pla_maxplaeveningsand_2000_175_p` — MAX PLA Evening Sand
- `3de_pla_maxplafluorescentgreen_2000_175_p` — MAX PLA Fluorescent Green
- `3de_pla_maxplafluorescentorange_2000_175_p` — MAX PLA Fluorescent Orange
- `3de_pla_maxplafluorescentyellow_2000_175_p` — MAX PLA Fluorescent Yellow
- `3de_pla_maxplagrassgreen_2000_175_p` — MAX PLA Grass Green
- `3de_pla_maxplagreen_2000_175_p` — MAX PLA Green
- `3de_pla_maxplagreenginfruit_2000_175_p` — MAX PLA Green Gin Fruit
- `3de_pla_maxplagreen-blueslate_2000_175_p` — MAX PLA Green-Blue Slate
- `3de_pla_maxplagreige_2000_175_p` — MAX PLA Greige
- `3de_pla_maxplagunmetal_2000_175_p` — MAX PLA Gun Metal
- `3de_pla_maxplajadegreen_2000_175_p` — MAX PLA Jade Green
- `3de_pla_maxplalemonyellow_2000_175_p` — MAX PLA Lemon Yellow
- `3de_pla_maxplalightgrey_2000_175_p` — MAX PLA Light Grey
- `3de_pla_maxplaoceanblue_2000_175_p` — MAX PLA Ocean Blue
- `3de_pla_maxplaolivegreen_2000_175_p` — MAX PLA Olive Green
- `3de_pla_maxplaorange_2000_175_p` — MAX PLA Orange
- `3de_pla_maxplapacificturquoise_2000_175_p` — MAX PLA Pacific Turquoise
- `3de_pla_maxplapopulargreen_2000_175_p` — MAX PLA Popular Green
- `3de_pla_maxplapureblack_2000_175_p` — MAX PLA Pure Black
- `3de_pla_maxplapuregold_2000_175_p` — MAX PLA Pure Gold
- `3de_pla_maxplapurewhite_2000_175_p` — MAX PLA Pure White
- `3de_pla_maxplared_2000_175_p` — MAX PLA Red
- `3de_pla_maxplaroyalblue_2000_175_p` — MAX PLA Royal Blue
- `3de_pla_maxplashadowgrey_2000_175_p` — MAX PLA Shadow Grey
- `3de_pla_maxplaskyblue_2000_175_p` — MAX PLA Sky Blue
- `3de_pla_maxplasoliddeeppurple_2000_175_p` — MAX PLA Solid Deep Purple
- `3de_pla_maxplasummerskyblue_2000_175_p` — MAX PLA Summer Sky Blue
- `3de_pla_maxplathundergrey_2000_175_p` — MAX PLA Thunder Grey
- `3de_pla_maxplatrueorange_2000_175_p` — MAX PLA True Orange
- `3de_pla_maxplawalnutbrown_2000_175_p` — MAX PLA Walnut Brown
- `3de_pla_maxplawarmwhite_2000_175_p` — MAX PLA Warm White
- `3de_pla_maxplawarmyellow_2000_175_p` — MAX PLA Warm Yellow
- `3de_pla_maxplawhite_2000_175_p` — MAX PLA White
- `3de_pla_maxplayellow_2000_175_p` — MAX PLA Yellow
- `3de_pla_maxplabarbadoscherry_2000_285_p` — MAX PLA Barbados Cherry
- `3de_pla_maxplablack_2000_285_p` — MAX PLA Black
- `3de_pla_maxplablue_2000_285_p` — MAX PLA Blue
- `3de_pla_maxplabone_2000_285_p` — MAX PLA Bone
- `3de_pla_maxplacappucino_2000_285_p` — MAX PLA Cappucino
- `3de_pla_maxplachilired_2000_285_p` — MAX PLA Chili Red
- `3de_pla_maxplacoffeebrown_2000_285_p` — MAX PLA Coffee Brown
- `3de_pla_maxplacoldwhite_2000_285_p` — MAX PLA Cold White
- `3de_pla_maxpladarkgrey_2000_285_p` — MAX PLA Dark Grey
- `3de_pla_maxpladesertbeige_2000_285_p` — MAX PLA Desert Beige
- `3de_pla_maxpladustyrose_2000_285_p` — MAX PLA Dusty Rose
- `3de_pla_maxplaeveningsand_2000_285_p` — MAX PLA Evening Sand
- `3de_pla_maxplafluorescentgreen_2000_285_p` — MAX PLA Fluorescent Green
- `3de_pla_maxplafluorescentorange_2000_285_p` — MAX PLA Fluorescent Orange
- `3de_pla_maxplafluorescentyellow_2000_285_p` — MAX PLA Fluorescent Yellow
- `3de_pla_maxplagrassgreen_2000_285_p` — MAX PLA Grass Green
- `3de_pla_maxplagreen_2000_285_p` — MAX PLA Green
- `3de_pla_maxplagreenginfruit_2000_285_p` — MAX PLA Green Gin Fruit
- `3de_pla_maxplagreen-blueslate_2000_285_p` — MAX PLA Green-Blue Slate
- `3de_pla_maxplagreige_2000_285_p` — MAX PLA Greige
- `3de_pla_maxplagunmetal_2000_285_p` — MAX PLA Gun Metal
- `3de_pla_maxplajadegreen_2000_285_p` — MAX PLA Jade Green
- `3de_pla_maxplalemonyellow_2000_285_p` — MAX PLA Lemon Yellow
- `3de_pla_maxplalightgrey_2000_285_p` — MAX PLA Light Grey
- `3de_pla_maxplaoceanblue_2000_285_p` — MAX PLA Ocean Blue
- `3de_pla_maxplaolivegreen_2000_285_p` — MAX PLA Olive Green
- `3de_pla_maxplaorange_2000_285_p` — MAX PLA Orange
- `3de_pla_maxplapacificturquoise_2000_285_p` — MAX PLA Pacific Turquoise
- `3de_pla_maxplapopulargreen_2000_285_p` — MAX PLA Popular Green
- `3de_pla_maxplapureblack_2000_285_p` — MAX PLA Pure Black
- `3de_pla_maxplapuregold_2000_285_p` — MAX PLA Pure Gold
- `3de_pla_maxplapurewhite_2000_285_p` — MAX PLA Pure White
- `3de_pla_maxplared_2000_285_p` — MAX PLA Red
- `3de_pla_maxplaroyalblue_2000_285_p` — MAX PLA Royal Blue
- `3de_pla_maxplashadowgrey_2000_285_p` — MAX PLA Shadow Grey
- `3de_pla_maxplaskyblue_2000_285_p` — MAX PLA Sky Blue
- `3de_pla_maxplasoliddeeppurple_2000_285_p` — MAX PLA Solid Deep Purple
- `3de_pla_maxplasummerskyblue_2000_285_p` — MAX PLA Summer Sky Blue
- `3de_pla_maxplathundergrey_2000_285_p` — MAX PLA Thunder Grey
- `3de_pla_maxplatrueorange_2000_285_p` — MAX PLA True Orange
- `3de_pla_maxplawalnutbrown_2000_285_p` — MAX PLA Walnut Brown
- `3de_pla_maxplawarmwhite_2000_285_p` — MAX PLA Warm White
- `3de_pla_maxplawarmyellow_2000_285_p` — MAX PLA Warm Yellow
- `3de_pla_maxplawhite_2000_285_p` — MAX PLA White
- `3de_pla_maxplayellow_2000_285_p` — MAX PLA Yellow
- `3de_pla_maxplabarbadoscherry_5000_175_p` — MAX PLA Barbados Cherry
- `3de_pla_maxplablack_5000_175_p` — MAX PLA Black
- `3de_pla_maxplablue_5000_175_p` — MAX PLA Blue
- `3de_pla_maxplabone_5000_175_p` — MAX PLA Bone
- `3de_pla_maxplacappucino_5000_175_p` — MAX PLA Cappucino
- `3de_pla_maxplachilired_5000_175_p` — MAX PLA Chili Red
- `3de_pla_maxplacoffeebrown_5000_175_p` — MAX PLA Coffee Brown
- `3de_pla_maxplacoldwhite_5000_175_p` — MAX PLA Cold White
- `3de_pla_maxpladarkgrey_5000_175_p` — MAX PLA Dark Grey
- `3de_pla_maxpladesertbeige_5000_175_p` — MAX PLA Desert Beige
- `3de_pla_maxpladustyrose_5000_175_p` — MAX PLA Dusty Rose
- `3de_pla_maxplaeveningsand_5000_175_p` — MAX PLA Evening Sand
- `3de_pla_maxplafluorescentgreen_5000_175_p` — MAX PLA Fluorescent Green
- `3de_pla_maxplafluorescentorange_5000_175_p` — MAX PLA Fluorescent Orange
- `3de_pla_maxplafluorescentyellow_5000_175_p` — MAX PLA Fluorescent Yellow
- `3de_pla_maxplagrassgreen_5000_175_p` — MAX PLA Grass Green
- `3de_pla_maxplagreen_5000_175_p` — MAX PLA Green
- `3de_pla_maxplagreenginfruit_5000_175_p` — MAX PLA Green Gin Fruit
- `3de_pla_maxplagreen-blueslate_5000_175_p` — MAX PLA Green-Blue Slate
- `3de_pla_maxplagreige_5000_175_p` — MAX PLA Greige
- `3de_pla_maxplagunmetal_5000_175_p` — MAX PLA Gun Metal
- `3de_pla_maxplajadegreen_5000_175_p` — MAX PLA Jade Green
- `3de_pla_maxplalemonyellow_5000_175_p` — MAX PLA Lemon Yellow
- `3de_pla_maxplalightgrey_5000_175_p` — MAX PLA Light Grey
- `3de_pla_maxplaoceanblue_5000_175_p` — MAX PLA Ocean Blue
- `3de_pla_maxplaolivegreen_5000_175_p` — MAX PLA Olive Green
- `3de_pla_maxplaorange_5000_175_p` — MAX PLA Orange
- `3de_pla_maxplapacificturquoise_5000_175_p` — MAX PLA Pacific Turquoise
- `3de_pla_maxplapopulargreen_5000_175_p` — MAX PLA Popular Green
- `3de_pla_maxplapureblack_5000_175_p` — MAX PLA Pure Black
- `3de_pla_maxplapuregold_5000_175_p` — MAX PLA Pure Gold
- `3de_pla_maxplapurewhite_5000_175_p` — MAX PLA Pure White
- `3de_pla_maxplared_5000_175_p` — MAX PLA Red
- `3de_pla_maxplaroyalblue_5000_175_p` — MAX PLA Royal Blue
- `3de_pla_maxplashadowgrey_5000_175_p` — MAX PLA Shadow Grey
- `3de_pla_maxplaskyblue_5000_175_p` — MAX PLA Sky Blue
- `3de_pla_maxplasoliddeeppurple_5000_175_p` — MAX PLA Solid Deep Purple
- `3de_pla_maxplasummerskyblue_5000_175_p` — MAX PLA Summer Sky Blue
- `3de_pla_maxplathundergrey_5000_175_p` — MAX PLA Thunder Grey
- `3de_pla_maxplatrueorange_5000_175_p` — MAX PLA True Orange
- `3de_pla_maxplawalnutbrown_5000_175_p` — MAX PLA Walnut Brown
- `3de_pla_maxplawarmwhite_5000_175_p` — MAX PLA Warm White
- `3de_pla_maxplawarmyellow_5000_175_p` — MAX PLA Warm Yellow
- `3de_pla_maxplawhite_5000_175_p` — MAX PLA White
- `3de_pla_maxplayellow_5000_175_p` — MAX PLA Yellow
- `3de_pla_maxplabarbadoscherry_5000_285_p` — MAX PLA Barbados Cherry
- `3de_pla_maxplablack_5000_285_p` — MAX PLA Black
- `3de_pla_maxplablue_5000_285_p` — MAX PLA Blue
- `3de_pla_maxplabone_5000_285_p` — MAX PLA Bone
- `3de_pla_maxplacappucino_5000_285_p` — MAX PLA Cappucino
- `3de_pla_maxplachilired_5000_285_p` — MAX PLA Chili Red
- `3de_pla_maxplacoffeebrown_5000_285_p` — MAX PLA Coffee Brown
- `3de_pla_maxplacoldwhite_5000_285_p` — MAX PLA Cold White
- `3de_pla_maxpladarkgrey_5000_285_p` — MAX PLA Dark Grey
- `3de_pla_maxpladesertbeige_5000_285_p` — MAX PLA Desert Beige
- `3de_pla_maxpladustyrose_5000_285_p` — MAX PLA Dusty Rose
- `3de_pla_maxplaeveningsand_5000_285_p` — MAX PLA Evening Sand
- `3de_pla_maxplafluorescentgreen_5000_285_p` — MAX PLA Fluorescent Green
- `3de_pla_maxplafluorescentorange_5000_285_p` — MAX PLA Fluorescent Orange
- `3de_pla_maxplafluorescentyellow_5000_285_p` — MAX PLA Fluorescent Yellow
- `3de_pla_maxplagrassgreen_5000_285_p` — MAX PLA Grass Green
- `3de_pla_maxplagreen_5000_285_p` — MAX PLA Green
- `3de_pla_maxplagreenginfruit_5000_285_p` — MAX PLA Green Gin Fruit
- `3de_pla_maxplagreen-blueslate_5000_285_p` — MAX PLA Green-Blue Slate
- `3de_pla_maxplagreige_5000_285_p` — MAX PLA Greige
- `3de_pla_maxplagunmetal_5000_285_p` — MAX PLA Gun Metal
- `3de_pla_maxplajadegreen_5000_285_p` — MAX PLA Jade Green
- `3de_pla_maxplalemonyellow_5000_285_p` — MAX PLA Lemon Yellow
- `3de_pla_maxplalightgrey_5000_285_p` — MAX PLA Light Grey
- `3de_pla_maxplaoceanblue_5000_285_p` — MAX PLA Ocean Blue
- `3de_pla_maxplaolivegreen_5000_285_p` — MAX PLA Olive Green
- `3de_pla_maxplaorange_5000_285_p` — MAX PLA Orange
- `3de_pla_maxplapacificturquoise_5000_285_p` — MAX PLA Pacific Turquoise
- `3de_pla_maxplapopulargreen_5000_285_p` — MAX PLA Popular Green
- `3de_pla_maxplapureblack_5000_285_p` — MAX PLA Pure Black
- `3de_pla_maxplapuregold_5000_285_p` — MAX PLA Pure Gold
- `3de_pla_maxplapurewhite_5000_285_p` — MAX PLA Pure White
- `3de_pla_maxplared_5000_285_p` — MAX PLA Red
- `3de_pla_maxplaroyalblue_5000_285_p` — MAX PLA Royal Blue
- `3de_pla_maxplashadowgrey_5000_285_p` — MAX PLA Shadow Grey
- `3de_pla_maxplaskyblue_5000_285_p` — MAX PLA Sky Blue
- `3de_pla_maxplasoliddeeppurple_5000_285_p` — MAX PLA Solid Deep Purple
- `3de_pla_maxplasummerskyblue_5000_285_p` — MAX PLA Summer Sky Blue
- `3de_pla_maxplathundergrey_5000_285_p` — MAX PLA Thunder Grey
- `3de_pla_maxplatrueorange_5000_285_p` — MAX PLA True Orange
- `3de_pla_maxplawalnutbrown_5000_285_p` — MAX PLA Walnut Brown
- `3de_pla_maxplawarmwhite_5000_285_p` — MAX PLA Warm White
- `3de_pla_maxplawarmyellow_5000_285_p` — MAX PLA Warm Yellow
- `3de_pla_maxplawhite_5000_285_p` — MAX PLA White
- `3de_pla_maxplayellow_5000_285_p` — MAX PLA Yellow
- `3de_pla_premiumcarbonfiberplacarbonfiberblack_1000_175_p` — Premium Carbon Fiber PLA Carbon Fiber Black
- `3de_pla_premiumflexiblepla54d-allblack_1000_175_p` — Premium Flexible PLA 54D - All Black
- `3de_pla_premiumflexiblepla54d-allblue_1000_175_p` — Premium Flexible PLA 54D - All Blue
- `3de_pla_premiumflexiblepla54d-allwhite_1000_175_p` — Premium Flexible PLA 54D - All White
- `3de_pla_premiumfluorescentplaneonyellow-fluorescent_1000_175_p` — Premium Fluorescent PLA Neon Yellow - Fluorescent
- `3de_pla_premiumfluorescentplanucleargreen_1000_175_p` — Premium Fluorescent PLA Nuclear Green
- `3de_pla_premiumfluorescentplasafetyorange_1000_175_p` — Premium Fluorescent PLA Safety Orange
- `3de_pla_premiumfluorescentplaneonyellow-fluorescent_1000_285_p` — Premium Fluorescent PLA Neon Yellow - Fluorescent
- `3de_pla_premiumfluorescentplanucleargreen_1000_285_p` — Premium Fluorescent PLA Nuclear Green
- `3de_pla_premiumfluorescentplasafetyorange_1000_285_p` — Premium Fluorescent PLA Safety Orange
- `3de_pla_premiumglowplaglow'n'glitterblue_1000_175_p` — Premium Glow PLA Glow'n'Glitter Blue
- `3de_pla_premiumglowplaglow'n'glittergreen_1000_175_p` — Premium Glow PLA Glow'n'Glitter Green
- `3de_pla_premiumglowplaglowingblue_1000_175_p` — Premium Glow PLA Glowing Blue
- `3de_pla_premiumglowplaglowingbluepurple_1000_175_p` — Premium Glow PLA Glowing BluePurple
- `3de_pla_premiumglowplaglowinggreen_1000_175_p` — Premium Glow PLA Glowing Green
- `3de_pla_premiumglowplaglowingorange_1000_175_p` — Premium Glow PLA Glowing Orange
- `3de_pla_premiumglowplaglowingrainbow_1000_175_p` — Premium Glow PLA Glowing Rainbow
- `3de_pla_premiumglowplaglowingred_1000_175_p` — Premium Glow PLA Glowing Red
- `3de_pla_premiumglowplaglowingwhite_1000_175_p` — Premium Glow PLA Glowing White
- `3de_pla_premiumglowplaglowingyellow_1000_175_p` — Premium Glow PLA Glowing Yellow
- `3de_pla_premiumglowplagreen_1000_175_p` — Premium Glow PLA Green
- `3de_pla_premiumglowplagreen-purple_1000_175_p` — Premium Glow PLA Green-Purple
- `3de_pla_premiumglowplamultiglowrainbow_1000_175_p` — Premium Glow PLA Multi Glow Rainbow
- `3de_pla_premiumhighspeedplasilkybronze_1000_175_p` — Premium High Speed PLA Silky Bronze
- `3de_pla_premiummattplacoolgrey_1000_175_p` — Premium Matt PLA Cool Grey
- `3de_pla_premiummattplaghostwhite_1000_175_p` — Premium Matt PLA Ghost White
- `3de_pla_premiummattplamarineblue_1000_175_p` — Premium Matt PLA Marine Blue
- `3de_pla_premiummattplamatterainbowmacaron_1000_175_p` — Premium Matt PLA Matte Rainbow Macaron
- `3de_pla_premiummattplamatterainbowoceanwave_1000_175_p` — Premium Matt PLA Matte Rainbow Ocean Wave
- `3de_pla_premiummattplamatterainbowpaddyfields_1000_175_p` — Premium Matt PLA Matte Rainbow Paddy Fields
- `3de_pla_premiummattplamatterainbowpurplerain_1000_175_p` — Premium Matt PLA Matte Rainbow Purple Rain
- `3de_pla_premiummattplamatterainbowsunrise_1000_175_p` — Premium Matt PLA Matte Rainbow Sunrise
- `3de_pla_premiummattplamidnightblack_1000_175_p` — Premium Matt PLA Midnight Black
- `3de_pla_premiummattplamossgreen_1000_175_p` — Premium Matt PLA Moss Green
- `3de_pla_premiummattplarubyred_1000_175_p` — Premium Matt PLA Ruby Red
- `3de_pla_premiummattplasunyellow_1000_175_p` — Premium Matt PLA Sun Yellow
- `3de_pla_premiumopaquepetgwhite_1000_285_p` — Premium Opaque PETG White
- `3de_pla_premiumopaqueplablack_1000_175_p` — Premium Opaque PLA Black
- `3de_pla_premiumopaqueplaoffwhite_1000_175_p` — Premium Opaque PLA Off White
- `3de_pla_premiumplaaquablue_1000_175_p` — Premium PLA Aqua Blue
- `3de_pla_premiumplaarmygreen_1000_175_p` — Premium PLA Army Green
- `3de_pla_premiumplaarmygreencamouflage_1000_175_p` — Premium PLA Army Green Camouflage
- `3de_pla_premiumplablackinblue_1000_175_p` — Premium PLA Black in Blue
- `3de_pla_premiumplacamelbeige_1000_175_p` — Premium PLA Camel Beige
- `3de_pla_premiumplachameleonblue_1000_175_p` — Premium PLA Chameleon Blue
- `3de_pla_premiumplachameleonpurple_1000_175_p` — Premium PLA Chameleon Purple
- `3de_pla_premiumplacherryred_1000_175_p` — Premium PLA Cherry Red
- `3de_pla_premiumplachocolatebrown_1000_175_p` — Premium PLA Chocolate Brown
- `3de_pla_premiumpladarkblue_1000_175_p` — Premium PLA Dark Blue
- `3de_pla_premiumpladarkstone_1000_175_p` — Premium PLA Dark Stone
- `3de_pla_premiumplaemeraldgreen_1000_175_p` — Premium PLA Emerald Green
- `3de_pla_premiumplaflourishrainbow_1000_175_p` — Premium PLA Flourish Rainbow
- `3de_pla_premiumplafrostedbronze_1000_175_p` — Premium PLA Frosted Bronze
- `3de_pla_premiumplageckogreen_1000_175_p` — Premium PLA Gecko Green
- `3de_pla_premiumplahotpink_1000_175_p` — Premium PLA Hot Pink
- `3de_pla_premiumplaiceblue_1000_175_p` — Premium PLA Ice Blue
- `3de_pla_premiumplakakicamouflage_1000_175_p` — Premium PLA Kaki Camouflage
- `3de_pla_premiumplaleafgreen_1000_175_p` — Premium PLA Leaf Green
- `3de_pla_premiumplaleatherbrown_1000_175_p` — Premium PLA Leather Brown
- `3de_pla_premiumplalightstone_1000_175_p` — Premium PLA Light Stone
- `3de_pla_premiumplamagenta_1000_175_p` — Premium PLA Magenta
- `3de_pla_premiumplamagicgreenforest_1000_175_p` — Premium PLA Magic Green Forest
- `3de_pla_premiumplamailboxred_1000_175_p` — Premium PLA Mailbox Red
- `3de_pla_premiumplamysticblue_1000_175_p` — Premium PLA Mystic Blue
- `3de_pla_premiumplanormalblue_1000_175_p` — Premium PLA Normal Blue
- `3de_pla_premiumplanudecolor_1000_175_p` — Premium PLA Nude Color
- `3de_pla_premiumplapearlcopper_1000_175_p` — Premium PLA Pearl Copper
- `3de_pla_premiumplapearlnature_1000_175_p` — Premium PLA Pearl Nature
- `3de_pla_premiumplapearlpurplishred_1000_175_p` — Premium PLA Pearl Purplish Red
- `3de_pla_premiumplapearlredbrown_1000_175_p` — Premium PLA Pearl Red Brown
- `3de_pla_premiumplapirateblack_1000_175_p` — Premium PLA Pirate Black
- `3de_pla_premiumplapurple_1000_175_p` — Premium PLA Purple
- `3de_pla_premiumplarainbow_1000_175_p` — Premium PLA Rainbow
- `3de_pla_premiumplasignalyellow_1000_175_p` — Premium PLA Signal Yellow
- `3de_pla_premiumplasilkrainbowuniverse_1000_175_p` — Premium PLA Silk Rainbow Universe
- `3de_pla_premiumplaslategrey_1000_175_p` — Premium PLA Slate Grey
- `3de_pla_premiumplasnowwhite_1000_175_p` — Premium PLA Snow White
- `3de_pla_premiumplaterminatorgrey_1000_175_p` — Premium PLA Terminator Grey
- `3de_pla_premiumplawaterblue_1000_175_p` — Premium PLA Water Blue
- `3de_pla_premiumplaaquablue_1000_285_p` — Premium PLA Aqua Blue
- `3de_pla_premiumplaarmygreen_1000_285_p` — Premium PLA Army Green
- `3de_pla_premiumplaarmygreencamouflage_1000_285_p` — Premium PLA Army Green Camouflage
- `3de_pla_premiumplablackinblue_1000_285_p` — Premium PLA Black in Blue
- `3de_pla_premiumplacamelbeige_1000_285_p` — Premium PLA Camel Beige
- `3de_pla_premiumplachameleonblue_1000_285_p` — Premium PLA Chameleon Blue
- `3de_pla_premiumplachameleonpurple_1000_285_p` — Premium PLA Chameleon Purple
- `3de_pla_premiumplacherryred_1000_285_p` — Premium PLA Cherry Red
- `3de_pla_premiumplachocolatebrown_1000_285_p` — Premium PLA Chocolate Brown
- `3de_pla_premiumpladarkblue_1000_285_p` — Premium PLA Dark Blue
- `3de_pla_premiumpladarkstone_1000_285_p` — Premium PLA Dark Stone
- `3de_pla_premiumplaemeraldgreen_1000_285_p` — Premium PLA Emerald Green
- `3de_pla_premiumplaflameorange_1000_285_p` — Premium PLA Flame Orange
- `3de_pla_premiumplaflourishrainbow_1000_285_p` — Premium PLA Flourish Rainbow
- `3de_pla_premiumplafrostedbronze_1000_285_p` — Premium PLA Frosted Bronze
- `3de_pla_premiumplageckogreen_1000_285_p` — Premium PLA Gecko Green
- `3de_pla_premiumplahotpink_1000_285_p` — Premium PLA Hot Pink
- `3de_pla_premiumplaiceblue_1000_285_p` — Premium PLA Ice Blue
- `3de_pla_premiumplakakicamouflage_1000_285_p` — Premium PLA Kaki Camouflage
- `3de_pla_premiumplaleafgreen_1000_285_p` — Premium PLA Leaf Green
- `3de_pla_premiumplaleatherbrown_1000_285_p` — Premium PLA Leather Brown
- `3de_pla_premiumplalightstone_1000_285_p` — Premium PLA Light Stone
- `3de_pla_premiumplamagenta_1000_285_p` — Premium PLA Magenta
- `3de_pla_premiumplamagicgreenforest_1000_285_p` — Premium PLA Magic Green Forest
- `3de_pla_premiumplamailboxred_1000_285_p` — Premium PLA Mailbox Red
- `3de_pla_premiumplamysticblue_1000_285_p` — Premium PLA Mystic Blue
- `3de_pla_premiumplanormalblue_1000_285_p` — Premium PLA Normal Blue
- `3de_pla_premiumplanudecolor_1000_285_p` — Premium PLA Nude Color
- `3de_pla_premiumplapearlcopper_1000_285_p` — Premium PLA Pearl Copper
- `3de_pla_premiumplapearlnature_1000_285_p` — Premium PLA Pearl Nature
- `3de_pla_premiumplapearlpurplishred_1000_285_p` — Premium PLA Pearl Purplish Red
- `3de_pla_premiumplapearlredbrown_1000_285_p` — Premium PLA Pearl Red Brown
- `3de_pla_premiumplapirateblack_1000_285_p` — Premium PLA Pirate Black
- `3de_pla_premiumplapurple_1000_285_p` — Premium PLA Purple
- `3de_pla_premiumplarainbow_1000_285_p` — Premium PLA Rainbow
- `3de_pla_premiumplasignalyellow_1000_285_p` — Premium PLA Signal Yellow
- `3de_pla_premiumplasilkrainbowuniverse_1000_285_p` — Premium PLA Silk Rainbow Universe
- `3de_pla_premiumplaslategrey_1000_285_p` — Premium PLA Slate Grey
- `3de_pla_premiumplasnowwhite_1000_285_p` — Premium PLA Snow White
- `3de_pla_premiumplaterminatorgrey_1000_285_p` — Premium PLA Terminator Grey
- `3de_pla_premiumplawaterblue_1000_285_p` — Premium PLA Water Blue
- `3de_pla_premiumplaaquablue_2000_175_p` — Premium PLA Aqua Blue
- `3de_pla_premiumplaarmygreen_2000_175_p` — Premium PLA Army Green
- `3de_pla_premiumplaarmygreencamouflage_2000_175_p` — Premium PLA Army Green Camouflage
- `3de_pla_premiumplablackinblue_2000_175_p` — Premium PLA Black in Blue
- `3de_pla_premiumplacamelbeige_2000_175_p` — Premium PLA Camel Beige
- `3de_pla_premiumplachameleonblue_2000_175_p` — Premium PLA Chameleon Blue
- `3de_pla_premiumplachameleonpurple_2000_175_p` — Premium PLA Chameleon Purple
- `3de_pla_premiumplacherryred_2000_175_p` — Premium PLA Cherry Red
- `3de_pla_premiumplachocolatebrown_2000_175_p` — Premium PLA Chocolate Brown
- `3de_pla_premiumpladarkblue_2000_175_p` — Premium PLA Dark Blue
- `3de_pla_premiumpladarkstone_2000_175_p` — Premium PLA Dark Stone
- `3de_pla_premiumplaemeraldgreen_2000_175_p` — Premium PLA Emerald Green
- `3de_pla_premiumplaflameorange_2000_175_p` — Premium PLA Flame Orange
- `3de_pla_premiumplaflourishrainbow_2000_175_p` — Premium PLA Flourish Rainbow
- `3de_pla_premiumplafrostedbronze_2000_175_p` — Premium PLA Frosted Bronze
- `3de_pla_premiumplageckogreen_2000_175_p` — Premium PLA Gecko Green
- `3de_pla_premiumplahotpink_2000_175_p` — Premium PLA Hot Pink
- `3de_pla_premiumplaiceblue_2000_175_p` — Premium PLA Ice Blue
- `3de_pla_premiumplakakicamouflage_2000_175_p` — Premium PLA Kaki Camouflage
- `3de_pla_premiumplaleafgreen_2000_175_p` — Premium PLA Leaf Green
- `3de_pla_premiumplaleatherbrown_2000_175_p` — Premium PLA Leather Brown
- `3de_pla_premiumplalightstone_2000_175_p` — Premium PLA Light Stone
- `3de_pla_premiumplamagenta_2000_175_p` — Premium PLA Magenta
- `3de_pla_premiumplamagicgreenforest_2000_175_p` — Premium PLA Magic Green Forest
- `3de_pla_premiumplamailboxred_2000_175_p` — Premium PLA Mailbox Red
- `3de_pla_premiumplamysticblue_2000_175_p` — Premium PLA Mystic Blue
- `3de_pla_premiumplanormalblue_2000_175_p` — Premium PLA Normal Blue
- `3de_pla_premiumplanudecolor_2000_175_p` — Premium PLA Nude Color
- `3de_pla_premiumplapearlcopper_2000_175_p` — Premium PLA Pearl Copper
- `3de_pla_premiumplapearlnature_2000_175_p` — Premium PLA Pearl Nature
- `3de_pla_premiumplapearlpurplishred_2000_175_p` — Premium PLA Pearl Purplish Red
- `3de_pla_premiumplapearlredbrown_2000_175_p` — Premium PLA Pearl Red Brown
- `3de_pla_premiumplapirateblack_2000_175_p` — Premium PLA Pirate Black
- `3de_pla_premiumplapurple_2000_175_p` — Premium PLA Purple
- `3de_pla_premiumplarainbow_2000_175_p` — Premium PLA Rainbow
- `3de_pla_premiumplasignalyellow_2000_175_p` — Premium PLA Signal Yellow
- `3de_pla_premiumplasilkrainbowuniverse_2000_175_p` — Premium PLA Silk Rainbow Universe
- `3de_pla_premiumplaslategrey_2000_175_p` — Premium PLA Slate Grey
- `3de_pla_premiumplasnowwhite_2000_175_p` — Premium PLA Snow White
- `3de_pla_premiumplaterminatorgrey_2000_175_p` — Premium PLA Terminator Grey
- `3de_pla_premiumplawaterblue_2000_175_p` — Premium PLA Water Blue
- `3de_pla_premiumplaaquablue_2000_285_p` — Premium PLA Aqua Blue
- `3de_pla_premiumplaarmygreen_2000_285_p` — Premium PLA Army Green
- `3de_pla_premiumplaarmygreencamouflage_2000_285_p` — Premium PLA Army Green Camouflage
- `3de_pla_premiumplablackinblue_2000_285_p` — Premium PLA Black in Blue
- `3de_pla_premiumplacamelbeige_2000_285_p` — Premium PLA Camel Beige
- `3de_pla_premiumplachameleonblue_2000_285_p` — Premium PLA Chameleon Blue
- `3de_pla_premiumplachameleonpurple_2000_285_p` — Premium PLA Chameleon Purple
- `3de_pla_premiumplacherryred_2000_285_p` — Premium PLA Cherry Red
- `3de_pla_premiumplachocolatebrown_2000_285_p` — Premium PLA Chocolate Brown
- `3de_pla_premiumpladarkblue_2000_285_p` — Premium PLA Dark Blue
- `3de_pla_premiumpladarkstone_2000_285_p` — Premium PLA Dark Stone
- `3de_pla_premiumplaemeraldgreen_2000_285_p` — Premium PLA Emerald Green
- `3de_pla_premiumplaflameorange_2000_285_p` — Premium PLA Flame Orange
- `3de_pla_premiumplaflourishrainbow_2000_285_p` — Premium PLA Flourish Rainbow
- `3de_pla_premiumplafrostedbronze_2000_285_p` — Premium PLA Frosted Bronze
- `3de_pla_premiumplageckogreen_2000_285_p` — Premium PLA Gecko Green
- `3de_pla_premiumplahotpink_2000_285_p` — Premium PLA Hot Pink
- `3de_pla_premiumplaiceblue_2000_285_p` — Premium PLA Ice Blue
- `3de_pla_premiumplakakicamouflage_2000_285_p` — Premium PLA Kaki Camouflage
- `3de_pla_premiumplaleafgreen_2000_285_p` — Premium PLA Leaf Green
- `3de_pla_premiumplaleatherbrown_2000_285_p` — Premium PLA Leather Brown
- `3de_pla_premiumplalightstone_2000_285_p` — Premium PLA Light Stone
- `3de_pla_premiumplamagenta_2000_285_p` — Premium PLA Magenta
- `3de_pla_premiumplamagicgreenforest_2000_285_p` — Premium PLA Magic Green Forest
- `3de_pla_premiumplamailboxred_2000_285_p` — Premium PLA Mailbox Red
- `3de_pla_premiumplamysticblue_2000_285_p` — Premium PLA Mystic Blue
- `3de_pla_premiumplanormalblue_2000_285_p` — Premium PLA Normal Blue
- `3de_pla_premiumplanudecolor_2000_285_p` — Premium PLA Nude Color
- `3de_pla_premiumplapearlcopper_2000_285_p` — Premium PLA Pearl Copper
- `3de_pla_premiumplapearlnature_2000_285_p` — Premium PLA Pearl Nature
- `3de_pla_premiumplapearlpurplishred_2000_285_p` — Premium PLA Pearl Purplish Red
- `3de_pla_premiumplapearlredbrown_2000_285_p` — Premium PLA Pearl Red Brown
- `3de_pla_premiumplapirateblack_2000_285_p` — Premium PLA Pirate Black
- `3de_pla_premiumplapurple_2000_285_p` — Premium PLA Purple
- `3de_pla_premiumplarainbow_2000_285_p` — Premium PLA Rainbow
- `3de_pla_premiumplasignalyellow_2000_285_p` — Premium PLA Signal Yellow
- `3de_pla_premiumplasilkrainbowuniverse_2000_285_p` — Premium PLA Silk Rainbow Universe
- `3de_pla_premiumplaslategrey_2000_285_p` — Premium PLA Slate Grey
- `3de_pla_premiumplasnowwhite_2000_285_p` — Premium PLA Snow White
- `3de_pla_premiumplaterminatorgrey_2000_285_p` — Premium PLA Terminator Grey
- `3de_pla_premiumplawaterblue_2000_285_p` — Premium PLA Water Blue
- `3de_pla_premiumplaaquablue_5000_175_p` — Premium PLA Aqua Blue
- `3de_pla_premiumplaarmygreen_5000_175_p` — Premium PLA Army Green
- `3de_pla_premiumplaarmygreencamouflage_5000_175_p` — Premium PLA Army Green Camouflage
- `3de_pla_premiumplablackinblue_5000_175_p` — Premium PLA Black in Blue
- `3de_pla_premiumplacamelbeige_5000_175_p` — Premium PLA Camel Beige
- `3de_pla_premiumplachameleonblue_5000_175_p` — Premium PLA Chameleon Blue
- `3de_pla_premiumplachameleonpurple_5000_175_p` — Premium PLA Chameleon Purple
- `3de_pla_premiumplacherryred_5000_175_p` — Premium PLA Cherry Red
- `3de_pla_premiumplachocolatebrown_5000_175_p` — Premium PLA Chocolate Brown
- `3de_pla_premiumpladarkblue_5000_175_p` — Premium PLA Dark Blue
- `3de_pla_premiumpladarkstone_5000_175_p` — Premium PLA Dark Stone
- `3de_pla_premiumplaemeraldgreen_5000_175_p` — Premium PLA Emerald Green
- `3de_pla_premiumplaflameorange_5000_175_p` — Premium PLA Flame Orange
- `3de_pla_premiumplaflourishrainbow_5000_175_p` — Premium PLA Flourish Rainbow
- `3de_pla_premiumplafrostedbronze_5000_175_p` — Premium PLA Frosted Bronze
- `3de_pla_premiumplageckogreen_5000_175_p` — Premium PLA Gecko Green
- `3de_pla_premiumplahotpink_5000_175_p` — Premium PLA Hot Pink
- `3de_pla_premiumplaiceblue_5000_175_p` — Premium PLA Ice Blue
- `3de_pla_premiumplakakicamouflage_5000_175_p` — Premium PLA Kaki Camouflage
- `3de_pla_premiumplaleafgreen_5000_175_p` — Premium PLA Leaf Green
- `3de_pla_premiumplaleatherbrown_5000_175_p` — Premium PLA Leather Brown
- `3de_pla_premiumplalightstone_5000_175_p` — Premium PLA Light Stone
- `3de_pla_premiumplamagenta_5000_175_p` — Premium PLA Magenta
- `3de_pla_premiumplamagicgreenforest_5000_175_p` — Premium PLA Magic Green Forest
- `3de_pla_premiumplamailboxred_5000_175_p` — Premium PLA Mailbox Red
- `3de_pla_premiumplamysticblue_5000_175_p` — Premium PLA Mystic Blue
- `3de_pla_premiumplanormalblue_5000_175_p` — Premium PLA Normal Blue
- `3de_pla_premiumplanudecolor_5000_175_p` — Premium PLA Nude Color
- `3de_pla_premiumplapearlcopper_5000_175_p` — Premium PLA Pearl Copper
- `3de_pla_premiumplapearlnature_5000_175_p` — Premium PLA Pearl Nature
- `3de_pla_premiumplapearlpurplishred_5000_175_p` — Premium PLA Pearl Purplish Red
- `3de_pla_premiumplapearlredbrown_5000_175_p` — Premium PLA Pearl Red Brown
- `3de_pla_premiumplapirateblack_5000_175_p` — Premium PLA Pirate Black
- `3de_pla_premiumplapurple_5000_175_p` — Premium PLA Purple
- `3de_pla_premiumplarainbow_5000_175_p` — Premium PLA Rainbow
- `3de_pla_premiumplasignalyellow_5000_175_p` — Premium PLA Signal Yellow
- `3de_pla_premiumplasilkrainbowuniverse_5000_175_p` — Premium PLA Silk Rainbow Universe
- `3de_pla_premiumplaslategrey_5000_175_p` — Premium PLA Slate Grey
- `3de_pla_premiumplasnowwhite_5000_175_p` — Premium PLA Snow White
- `3de_pla_premiumplaterminatorgrey_5000_175_p` — Premium PLA Terminator Grey
- `3de_pla_premiumplawaterblue_5000_175_p` — Premium PLA Water Blue
- `3de_pla_premiumplaaquablue_5000_285_p` — Premium PLA Aqua Blue
- `3de_pla_premiumplaarmygreen_5000_285_p` — Premium PLA Army Green
- `3de_pla_premiumplaarmygreencamouflage_5000_285_p` — Premium PLA Army Green Camouflage
- `3de_pla_premiumplablackinblue_5000_285_p` — Premium PLA Black in Blue
- `3de_pla_premiumplacamelbeige_5000_285_p` — Premium PLA Camel Beige
- `3de_pla_premiumplachameleonblue_5000_285_p` — Premium PLA Chameleon Blue
- `3de_pla_premiumplachameleonpurple_5000_285_p` — Premium PLA Chameleon Purple
- `3de_pla_premiumplacherryred_5000_285_p` — Premium PLA Cherry Red
- `3de_pla_premiumplachocolatebrown_5000_285_p` — Premium PLA Chocolate Brown
- `3de_pla_premiumpladarkblue_5000_285_p` — Premium PLA Dark Blue
- `3de_pla_premiumpladarkstone_5000_285_p` — Premium PLA Dark Stone
- `3de_pla_premiumplaemeraldgreen_5000_285_p` — Premium PLA Emerald Green
- `3de_pla_premiumplaflameorange_5000_285_p` — Premium PLA Flame Orange
- `3de_pla_premiumplaflourishrainbow_5000_285_p` — Premium PLA Flourish Rainbow
- `3de_pla_premiumplafrostedbronze_5000_285_p` — Premium PLA Frosted Bronze
- `3de_pla_premiumplageckogreen_5000_285_p` — Premium PLA Gecko Green
- `3de_pla_premiumplahotpink_5000_285_p` — Premium PLA Hot Pink
- `3de_pla_premiumplaiceblue_5000_285_p` — Premium PLA Ice Blue
- `3de_pla_premiumplakakicamouflage_5000_285_p` — Premium PLA Kaki Camouflage
- `3de_pla_premiumplaleafgreen_5000_285_p` — Premium PLA Leaf Green
- `3de_pla_premiumplaleatherbrown_5000_285_p` — Premium PLA Leather Brown
- `3de_pla_premiumplalightstone_5000_285_p` — Premium PLA Light Stone
- `3de_pla_premiumplamagenta_5000_285_p` — Premium PLA Magenta
- `3de_pla_premiumplamagicgreenforest_5000_285_p` — Premium PLA Magic Green Forest
- `3de_pla_premiumplamailboxred_5000_285_p` — Premium PLA Mailbox Red
- `3de_pla_premiumplamysticblue_5000_285_p` — Premium PLA Mystic Blue
- `3de_pla_premiumplanormalblue_5000_285_p` — Premium PLA Normal Blue
- `3de_pla_premiumplanudecolor_5000_285_p` — Premium PLA Nude Color
- `3de_pla_premiumplapearlcopper_5000_285_p` — Premium PLA Pearl Copper
- `3de_pla_premiumplapearlnature_5000_285_p` — Premium PLA Pearl Nature
- `3de_pla_premiumplapearlpurplishred_5000_285_p` — Premium PLA Pearl Purplish Red
- `3de_pla_premiumplapearlredbrown_5000_285_p` — Premium PLA Pearl Red Brown
- `3de_pla_premiumplapirateblack_5000_285_p` — Premium PLA Pirate Black
- `3de_pla_premiumplapurple_5000_285_p` — Premium PLA Purple
- `3de_pla_premiumplarainbow_5000_285_p` — Premium PLA Rainbow
- `3de_pla_premiumplasignalyellow_5000_285_p` — Premium PLA Signal Yellow
- `3de_pla_premiumplasilkrainbowuniverse_5000_285_p` — Premium PLA Silk Rainbow Universe
- `3de_pla_premiumplaslategrey_5000_285_p` — Premium PLA Slate Grey
- `3de_pla_premiumplasnowwhite_5000_285_p` — Premium PLA Snow White
- `3de_pla_premiumplaterminatorgrey_5000_285_p` — Premium PLA Terminator Grey
- `3de_pla_premiumplawaterblue_5000_285_p` — Premium PLA Water Blue
- `3de_pla_premiumpastelpladinogreen_1000_175_p` — Premium Pastel PLA Dino Green
- `3de_pla_premiumpastelplalavenderpurple-pastel_1000_175_p` — Premium Pastel PLA Lavender Purple - Pastel
- `3de_pla_premiumpastelplasteelblue-pastel_1000_175_p` — Premium Pastel PLA Steel Blue - Pastel
- `3de_pla_premiumpastelplasunriseyellow-pastel_1000_175_p` — Premium Pastel PLA Sunrise Yellow - Pastel
- `3de_pla_premiumpastelplaunicornpink-pastel_1000_175_p` — Premium Pastel PLA Unicorn Pink - Pastel
- `3de_pla_premiumshimmerplablack_1000_175_p` — Premium Shimmer PLA Black
- `3de_pla_premiumshimmerpladarkblue_1000_175_p` — Premium Shimmer PLA Dark Blue
- `3de_pla_premiumshimmerpladarkgreen_1000_175_p` — Premium Shimmer PLA Dark Green
- `3de_pla_premiumshimmerplagold_1000_175_p` — Premium Shimmer PLA Gold
- `3de_pla_premiumshimmerplagrey_1000_175_p` — Premium Shimmer PLA Grey
- `3de_pla_premiumshimmerplared_1000_175_p` — Premium Shimmer PLA Red
- `3de_pla_premiumshimmerplasilver_1000_175_p` — Premium Shimmer PLA Silver
- `3de_pla_premiumshimmerplatransparentred_1000_175_p` — Premium Shimmer PLA Transparent Red
- `3de_pla_premiumsilkyplabicolor-yellow&blue_1000_175_p` — Premium Silky PLA BiColor - Yellow&Blue
- `3de_pla_premiumsilkyplablack_1000_175_p` — Premium Silky PLA Black
- `3de_pla_premiumsilkyplablack&gold_1000_175_p` — Premium Silky PLA Black & Gold
- `3de_pla_premiumsilkyplablack&green_1000_175_p` — Premium Silky PLA Black & Green
- `3de_pla_premiumsilkyplablue_1000_175_p` — Premium Silky PLA Blue
- `3de_pla_premiumsilkyplablue&green_1000_175_p` — Premium Silky PLA Blue & Green
- `3de_pla_premiumsilkyplabluepurple_1000_175_p` — Premium Silky PLA Blue Purple
- `3de_pla_premiumsilkyplabronze_1000_175_p` — Premium Silky PLA Bronze
- `3de_pla_premiumsilkyplacandypink_1000_175_p` — Premium Silky PLA Candy Pink
- `3de_pla_premiumsilkyplacopper_1000_175_p` — Premium Silky PLA Copper
- `3de_pla_premiumsilkypladarkblue_1000_175_p` — Premium Silky PLA Dark Blue
- `3de_pla_premiumsilkypladarkblue&gold_1000_175_p` — Premium Silky PLA Dark Blue & Gold
- `3de_pla_premiumsilkypladeepcyan_1000_175_p` — Premium Silky PLA Deep Cyan
- `3de_pla_premiumsilkyplaelixirblue_1000_175_p` — Premium Silky PLA Elixir Blue
- `3de_pla_premiumsilkyplageckogreen_1000_175_p` — Premium Silky PLA Gecko Green
- `3de_pla_premiumsilkyplagold_1000_175_p` — Premium Silky PLA Gold
- `3de_pla_premiumsilkyplagoldenyellow_1000_175_p` — Premium Silky PLA Golden Yellow
- `3de_pla_premiumsilkyplagoldfishorange_1000_175_p` — Premium Silky PLA Goldfish Orange
- `3de_pla_premiumsilkyplagreen_1000_175_p` — Premium Silky PLA Green
- `3de_pla_premiumsilkyplagreen&yellow_1000_175_p` — Premium Silky PLA Green & Yellow
- `3de_pla_premiumsilkyplairongrey_1000_175_p` — Premium Silky PLA Iron Grey
- `3de_pla_premiumsilkyplalagoonblue_1000_175_p` — Premium Silky PLA Lagoon Blue
- `3de_pla_premiumsilkyplamixred-sapphireblue_1000_175_p` — Premium Silky PLA Mix Red-Sapphire Blue
- `3de_pla_premiumsilkyplamochabrown_1000_175_p` — Premium Silky PLA Mocha Brown
- `3de_pla_premiumsilkyplapink&gold_1000_175_p` — Premium Silky PLA Pink & Gold
- `3de_pla_premiumsilkyplapurple_1000_175_p` — Premium Silky PLA Purple
- `3de_pla_premiumsilkyplarainbow_1000_175_p` — Premium Silky PLA Rainbow
- `3de_pla_premiumsilkyplared_1000_175_p` — Premium Silky PLA Red
- `3de_pla_premiumsilkyplared&black_1000_175_p` — Premium Silky PLA Red & Black
- `3de_pla_premiumsilkyplared&blue_1000_175_p` — Premium Silky PLA Red & Blue
- `3de_pla_premiumsilkyplared&gold_1000_175_p` — Premium Silky PLA Red & Gold
- `3de_pla_premiumsilkyplared&lightgreen_1000_175_p` — Premium Silky PLA Red & Light Green
- `3de_pla_premiumsilkyplaredcopper_1000_175_p` — Premium Silky PLA Red Copper
- `3de_pla_premiumsilkyplarosegold_1000_175_p` — Premium Silky PLA Rose Gold
- `3de_pla_premiumsilkyplasagegreen_1000_175_p` — Premium Silky PLA Sage Green
- `3de_pla_premiumsilkyplasilkyrainbowblueviolet_1000_175_p` — Premium Silky PLA Silky Rainbow Blue Violet
- `3de_pla_premiumsilkyplasilkyrainbowcandy_1000_175_p` — Premium Silky PLA Silky Rainbow Candy
- `3de_pla_premiumsilkyplasilkyrainbowflower_1000_175_p` — Premium Silky PLA Silky Rainbow Flower
- `3de_pla_premiumsilkyplasilkyrainbowforest_1000_175_p` — Premium Silky PLA Silky Rainbow Forest
- `3de_pla_premiumsilkyplasilkyrainbowmacaron_1000_175_p` — Premium Silky PLA Silky Rainbow Macaron
- `3de_pla_premiumsilkyplasilkyrainbowpastel_1000_175_p` — Premium Silky PLA Silky Rainbow Pastel
- `3de_pla_premiumsilkyplasilver_1000_175_p` — Premium Silky PLA Silver
- `3de_pla_premiumsilkyplasparklyrainbow_1000_175_p` — Premium Silky PLA Sparkly Rainbow
- `3de_pla_premiumsilkyplatricolorgold,blueandfuchsia_1000_175_p` — Premium Silky PLA Tricolor Gold, Blue and Fuchsia
- `3de_pla_premiumsilkyplatricolorgold,blueandred_1000_175_p` — Premium Silky PLA Tricolor Gold, Blue and Red
- `3de_pla_premiumsilkyplatricolorgold,fuchsiaandblack_1000_175_p` — Premium Silky PLA Tricolor Gold, Fuchsia and Black
- `3de_pla_premiumsilkyplatricolorgold,greenandblue_1000_175_p` — Premium Silky PLA Tricolor Gold, Green and Blue
- `3de_pla_premiumsilkyplatricolorgold,greenandfuchsia_1000_175_p` — Premium Silky PLA Tricolor Gold, Green and Fuchsia
- `3de_pla_premiumsilkyplatricolorgold,greenandpinkish_1000_175_p` — Premium Silky PLA Tricolor Gold, Green and Pinkish
- `3de_pla_premiumsilkyplatricolorgold,greenandpurple_1000_175_p` — Premium Silky PLA Tricolor Gold, Green and Purple
- `3de_pla_premiumsilkyplatricolorgold,greenandred_1000_175_p` — Premium Silky PLA Tricolor Gold, Green and Red
- `3de_pla_premiumsilkyplatricolorgold,redandblack_1000_175_p` — Premium Silky PLA Tricolor Gold, Red and Black
- `3de_pla_premiumsilkyplatricolorgold,silverandcopper_1000_175_p` — Premium Silky PLA Tricolor Gold, Silver and Copper
- `3de_pla_premiumsilkyplatricolorred,greenandblue_1000_175_p` — Premium Silky PLA Tricolor Red, Green and Blue
- `3de_pla_premiumsilkyplawhite_1000_175_p` — Premium Silky PLA White
- `3de_pla_premiumsilkyplayellow_1000_175_p` — Premium Silky PLA Yellow
- `3de_pla_premiumsilkyplabicolor-yellow&blue_1000_285_p` — Premium Silky PLA BiColor - Yellow&Blue
- `3de_pla_premiumsilkyplablack_1000_285_p` — Premium Silky PLA Black
- `3de_pla_premiumsilkyplablack&gold_1000_285_p` — Premium Silky PLA Black & Gold
- `3de_pla_premiumsilkyplablack&green_1000_285_p` — Premium Silky PLA Black & Green
- `3de_pla_premiumsilkyplablue_1000_285_p` — Premium Silky PLA Blue
- `3de_pla_premiumsilkyplablue&green_1000_285_p` — Premium Silky PLA Blue & Green
- `3de_pla_premiumsilkyplabluepurple_1000_285_p` — Premium Silky PLA Blue Purple
- `3de_pla_premiumsilkyplabronze_1000_285_p` — Premium Silky PLA Bronze
- `3de_pla_premiumsilkyplacandypink_1000_285_p` — Premium Silky PLA Candy Pink
- `3de_pla_premiumsilkyplacopper_1000_285_p` — Premium Silky PLA Copper
- `3de_pla_premiumsilkypladarkblue_1000_285_p` — Premium Silky PLA Dark Blue
- `3de_pla_premiumsilkypladarkblue&gold_1000_285_p` — Premium Silky PLA Dark Blue & Gold
- `3de_pla_premiumsilkypladeepcyan_1000_285_p` — Premium Silky PLA Deep Cyan
- `3de_pla_premiumsilkyplaelixirblue_1000_285_p` — Premium Silky PLA Elixir Blue
- `3de_pla_premiumsilkyplageckogreen_1000_285_p` — Premium Silky PLA Gecko Green
- `3de_pla_premiumsilkyplagold_1000_285_p` — Premium Silky PLA Gold
- `3de_pla_premiumsilkyplagoldenyellow_1000_285_p` — Premium Silky PLA Golden Yellow
- `3de_pla_premiumsilkyplagoldfishorange_1000_285_p` — Premium Silky PLA Goldfish Orange
- `3de_pla_premiumsilkyplagreen_1000_285_p` — Premium Silky PLA Green
- `3de_pla_premiumsilkyplagreen&yellow_1000_285_p` — Premium Silky PLA Green & Yellow
- `3de_pla_premiumsilkyplairongrey_1000_285_p` — Premium Silky PLA Iron Grey
- `3de_pla_premiumsilkyplalagoonblue_1000_285_p` — Premium Silky PLA Lagoon Blue
- `3de_pla_premiumsilkyplamixred-sapphireblue_1000_285_p` — Premium Silky PLA Mix Red-Sapphire Blue
- `3de_pla_premiumsilkyplamochabrown_1000_285_p` — Premium Silky PLA Mocha Brown
- `3de_pla_premiumsilkyplapink&gold_1000_285_p` — Premium Silky PLA Pink & Gold
- `3de_pla_premiumsilkyplapurple_1000_285_p` — Premium Silky PLA Purple
- `3de_pla_premiumsilkyplarainbow_1000_285_p` — Premium Silky PLA Rainbow
- `3de_pla_premiumsilkyplared_1000_285_p` — Premium Silky PLA Red
- `3de_pla_premiumsilkyplared&black_1000_285_p` — Premium Silky PLA Red & Black
- `3de_pla_premiumsilkyplared&blue_1000_285_p` — Premium Silky PLA Red & Blue
- `3de_pla_premiumsilkyplared&gold_1000_285_p` — Premium Silky PLA Red & Gold
- `3de_pla_premiumsilkyplared&lightgreen_1000_285_p` — Premium Silky PLA Red & Light Green
- `3de_pla_premiumsilkyplaredcopper_1000_285_p` — Premium Silky PLA Red Copper
- `3de_pla_premiumsilkyplarosegold_1000_285_p` — Premium Silky PLA Rose Gold
- `3de_pla_premiumsilkyplasagegreen_1000_285_p` — Premium Silky PLA Sage Green
- `3de_pla_premiumsilkyplasilkyrainbowblueviolet_1000_285_p` — Premium Silky PLA Silky Rainbow Blue Violet
- `3de_pla_premiumsilkyplasilkyrainbowcandy_1000_285_p` — Premium Silky PLA Silky Rainbow Candy
- `3de_pla_premiumsilkyplasilkyrainbowflower_1000_285_p` — Premium Silky PLA Silky Rainbow Flower
- `3de_pla_premiumsilkyplasilkyrainbowforest_1000_285_p` — Premium Silky PLA Silky Rainbow Forest
- `3de_pla_premiumsilkyplasilkyrainbowmacaron_1000_285_p` — Premium Silky PLA Silky Rainbow Macaron
- `3de_pla_premiumsilkyplasilkyrainbowpastel_1000_285_p` — Premium Silky PLA Silky Rainbow Pastel
- `3de_pla_premiumsilkyplasilver_1000_285_p` — Premium Silky PLA Silver
- `3de_pla_premiumsilkyplasparklyrainbow_1000_285_p` — Premium Silky PLA Sparkly Rainbow
- `3de_pla_premiumsilkyplatricolorgold,blueandfuchsia_1000_285_p` — Premium Silky PLA Tricolor Gold, Blue and Fuchsia
- `3de_pla_premiumsilkyplatricolorgold,blueandred_1000_285_p` — Premium Silky PLA Tricolor Gold, Blue and Red
- `3de_pla_premiumsilkyplatricolorgold,fuchsiaandblack_1000_285_p` — Premium Silky PLA Tricolor Gold, Fuchsia and Black
- `3de_pla_premiumsilkyplatricolorgold,greenandblue_1000_285_p` — Premium Silky PLA Tricolor Gold, Green and Blue
- `3de_pla_premiumsilkyplatricolorgold,greenandfuchsia_1000_285_p` — Premium Silky PLA Tricolor Gold, Green and Fuchsia
- `3de_pla_premiumsilkyplatricolorgold,greenandpinkish_1000_285_p` — Premium Silky PLA Tricolor Gold, Green and Pinkish
- `3de_pla_premiumsilkyplatricolorgold,greenandpurple_1000_285_p` — Premium Silky PLA Tricolor Gold, Green and Purple
- `3de_pla_premiumsilkyplatricolorgold,greenandred_1000_285_p` — Premium Silky PLA Tricolor Gold, Green and Red
- `3de_pla_premiumsilkyplatricolorgold,redandblack_1000_285_p` — Premium Silky PLA Tricolor Gold, Red and Black
- `3de_pla_premiumsilkyplatricolorgold,silverandcopper_1000_285_p` — Premium Silky PLA Tricolor Gold, Silver and Copper
- `3de_pla_premiumsilkyplatricolorred,greenandblue_1000_285_p` — Premium Silky PLA Tricolor Red, Green and Blue
- `3de_pla_premiumsilkyplawhite_1000_285_p` — Premium Silky PLA White
- `3de_pla_premiumsilkyplayellow_1000_285_p` — Premium Silky PLA Yellow
- `3de_pla_premiumtransparentplablack_1000_175_p` — Premium Transparent PLA Black
- `3de_pla_premiumtransparentplablue_1000_175_p` — Premium Transparent PLA Blue
- `3de_pla_premiumtransparentplagreen_1000_175_p` — Premium Transparent PLA Green
- `3de_pla_premiumtransparentplalightgrey_1000_175_p` — Premium Transparent PLA Light Grey
- `3de_pla_premiumtransparentplaorange_1000_175_p` — Premium Transparent PLA Orange
- `3de_pla_premiumtransparentplaplatransparentrainbow-glacierblue_1000_175_p` — Premium Transparent PLA PLA Transparent Rainbow - Glacier Blue
- `3de_pla_premiumtransparentplaplatransparentrainbow-lotuspink_1000_175_p` — Premium Transparent PLA PLA Transparent Rainbow - Lotus Pink
- `3de_pla_premiumtransparentplaplatransparentrainbow-mintgreen_1000_175_p` — Premium Transparent PLA PLA Transparent Rainbow - Mint Green
- `3de_pla_premiumtransparentplaplatransparentrainbow-phantomblue_1000_175_p` — Premium Transparent PLA PLA Transparent Rainbow - Phantom Blue
- `3de_pla_premiumtransparentplared_1000_175_p` — Premium Transparent PLA Red
- `3de_pla_premiumtransparentplatransparent_1000_175_p` — Premium Transparent PLA Transparent
- `3de_pla_premiumtransparentplayellow_1000_175_p` — Premium Transparent PLA Yellow
- `3de_pla_premiumtransparentplablack_2000_175_p` — Premium Transparent PLA Black
- `3de_pla_premiumtransparentplablue_2000_175_p` — Premium Transparent PLA Blue
- `3de_pla_premiumtransparentplagreen_2000_175_p` — Premium Transparent PLA Green
- `3de_pla_premiumtransparentplalightgrey_2000_175_p` — Premium Transparent PLA Light Grey
- `3de_pla_premiumtransparentplaorange_2000_175_p` — Premium Transparent PLA Orange
- `3de_pla_premiumtransparentplaplatransparentrainbow-glacierblue_2000_175_p` — Premium Transparent PLA PLA Transparent Rainbow - Glacier Blue
- `3de_pla_premiumtransparentplaplatransparentrainbow-lotuspink_2000_175_p` — Premium Transparent PLA PLA Transparent Rainbow - Lotus Pink
- `3de_pla_premiumtransparentplaplatransparentrainbow-mintgreen_2000_175_p` — Premium Transparent PLA PLA Transparent Rainbow - Mint Green
- `3de_pla_premiumtransparentplaplatransparentrainbow-phantomblue_2000_175_p` — Premium Transparent PLA PLA Transparent Rainbow - Phantom Blue
- `3de_pla_premiumtransparentplared_2000_175_p` — Premium Transparent PLA Red
- `3de_pla_premiumtransparentplatransparent_2000_175_p` — Premium Transparent PLA Transparent
- `3de_pla_premiumtransparentplayellow_2000_175_p` — Premium Transparent PLA Yellow
- `3de_pla_premiumwoodfillpladarkwood_1000_175_p` — Premium Woodfill PLA Dark Wood
- `3de_pla_premiumwoodfillplalightwood_1000_175_p` — Premium Woodfill PLA Light Wood
- `3de_pla_premiumwoodfillplawood_1000_175_p` — Premium Woodfill PLA Wood
- `3de_pla_premiumx-strongplablack_1000_175_p` — Premium X-Strong PLA Black
- `3de_pla_premiumx-strongplagrey_1000_175_p` — Premium X-Strong PLA Grey
- `3de_pla_premiumx-strongplawhite_1000_175_p` — Premium X-Strong PLA White
- `3de_pla_premiumblack_1000_175_p` — Premium Black
- `3de_pla_premium4dplanature_1000_175_p` — Premium 4D PLA Nature
- `3de_pla_premiumantibacterialplawhite_1000_175_p` — Premium Antibacterial PLA White
- `3de_pla_premiumantistaticplablack_1000_175_p` — Premium Antistatic PLA Black
- `3de_plahightemp_premiumhightempplablack_1000_175_p` — Premium High Temp PLA Black
- `3de_plahightemp_premiumhightempplagrey_1000_175_p` — Premium High Temp PLA Grey
- `3de_plahightemp_premiumhightempplawhite_1000_175_p` — Premium High Temp PLA White
- `3de_plahightemp_premiumhightempplablack_1000_285_p` — Premium High Temp PLA Black
- `3de_plahightemp_premiumhightempplagrey_1000_285_p` — Premium High Temp PLA Grey
- `3de_plahightemp_premiumhightempplawhite_1000_285_p` — Premium High Temp PLA White
- `3de_plamagic_premiummagicplablue_1000_175_p` — Premium Magic PLA Blue
- `3de_plamagic_premiummagicplagold_1000_175_p` — Premium Magic PLA Gold
- `3de_plamagic_premiummagicplagreen_1000_175_p` — Premium Magic PLA Green
- `3de_plamagic_premiummagicplapurple_1000_175_p` — Premium Magic PLA Purple
- `3de_plaseaweed_premiumseaweedplayellow/green_1000_175_p` — Premium Seaweed PLA Yellow/Green
- `3de_pp_premiumppblack_1000_175_p` — Premium PP Black
- `3de_pp_premiumppblack_1000_285_p` — Premium PP Black
- `3de_pvb_premiumceramicjadenature_500_175_p` — Premium Ceramic Jade Nature
- `3de_pvb_premiumceramicsnowwhite_500_175_p` — Premium Ceramic Snow White
- `3de_pla_premiumsilkmixred-sapphireblue_1000_175_p` — Premium Silk Mix Red-Sapphire Blue
- `3de_pla_premiumsilktricolorgoldgreenpinkish_1000_175_p` — Premium Silk Tricolor Gold Green Pinkish
