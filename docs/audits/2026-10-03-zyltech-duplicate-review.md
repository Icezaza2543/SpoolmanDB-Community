# zyltech duplicate migration review

Base `2e3b44fe6b59d75b01b7fd3d33e8545ffd4eaa99`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `f2973166db885c50a2007e0988192ac5d91cba03ba74c11af293ebb648612513`.

## Authorization and result

{"groups": 6, "approved_groups": 6, "retired": 6, "deferred": 0, "hard_stops": 0, "before_count": 51734, "after_count": 51728, "brand_before": 137, "brand_after": 131, "registry_before": 1700, "registry_after": 1706, "metadata_fields_changed": 10, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Six Rule2 strict duplicates. Correct only exact target PLA density/nozzle and PETG bed. PLA bed and PETG nozzle internal conflicts stay unresolved; no COO, packaging or tare change. No identifier transfers.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://www.zyltech.com/pla-3d-printer-filament-1-75mm-1-kg-2-2-lbs/", "density": 1.27, "nozzle": [200, 220], "note": "Bed optional without numeric range; old bed preserved unresolved."}
- {"url": "https://www.zyltech.com/petg-3d-printer-filament-1-75mm-1-kg-2-2-lbs/", "bed": "75±10", "note": "Nozzle internally conflicts230–270 versus235±10; retain existing nozzle unresolved. Standard PETG, not HighSpeed."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`zyltech_petg_zyltechpetgblack_1000_175_p`|`zyltech_petg_petgblack_1000_175_p`|`zyltech.json::Zyltech::Zyltech PETG {color_name}::Zyltech PETG Black::PETG::1000::1.75::plastic::False`|
|`zyltech_petg_zyltechpetgwhite_1000_175_p`|`zyltech_petg_petgwhite_1000_175_p`|`zyltech.json::Zyltech::Zyltech PETG {color_name}::Zyltech PETG White::PETG::1000::1.75::plastic::False`|
|`zyltech_pla_zyltechplagreen_1000_175_p`|`zyltech_pla_plagreen_1000_175_p`|`zyltech.json::Zyltech::Zyltech PLA {color_name}::Zyltech PLA Green::PLA::1000::1.75::plastic::False`|
|`zyltech_pla_zyltechplagrey_1000_175_p`|`zyltech_pla_plagray_1000_175_p`|`zyltech.json::Zyltech::Zyltech PLA {color_name}::Zyltech PLA Grey::PLA::1000::1.75::plastic::False`|
|`zyltech_pla_zyltechplaorange_1000_175_p`|`zyltech_pla_plaorange_1000_175_p`|`zyltech.json::Zyltech::Zyltech PLA {color_name}::Zyltech PLA Orange::PLA::1000::1.75::plastic::False`|
|`zyltech_pla_zyltechplayellow_1000_175_p`|`zyltech_pla_playellow_1000_175_p`|`zyltech.json::Zyltech::Zyltech PLA {color_name}::Zyltech PLA Yellow::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### ZY001: dup-c515a69e5d73e6db877fd524d4403c4b5f25c41852f5d9929e88cb5098f52fec

Status: APPROVED; survivor `zyltech_petg_petgblack_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`zyltech_petg_petgblack_1000_175_p`|`PETG {color_name}`|`Black`|{"source_file": "zyltech.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / False|
|`zyltech_petg_zyltechpetgblack_1000_175_p`|`Zyltech PETG {color_name}`|`Black`|{"source_file": "zyltech.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "zyltech_petg_petgblack_1000_175_p": "000000",
    "zyltech_petg_zyltechpetgblack_1000_175_p": "1a1a1a"
  },
  "extruder_temp_range": {
    "zyltech_petg_petgblack_1000_175_p": [
      220,
      250
    ],
    "zyltech_petg_zyltechpetgblack_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "zyltech_petg_petgblack_1000_175_p": [
      70,
      90
    ],
    "zyltech_petg_zyltechpetgblack_1000_175_p": [
      70,
      85
    ]
  }
}
```

### ZY002: dup-ae6b00e5e63daa414db2505e72e82f741c9212624076343de52c444d58894084

Status: APPROVED; survivor `zyltech_petg_petgwhite_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`zyltech_petg_petgwhite_1000_175_p`|`PETG {color_name}`|`White`|{"source_file": "zyltech.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / False|
|`zyltech_petg_zyltechpetgwhite_1000_175_p`|`Zyltech PETG {color_name}`|`White`|{"source_file": "zyltech.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "zyltech_petg_petgwhite_1000_175_p": "FFFFFF",
    "zyltech_petg_zyltechpetgwhite_1000_175_p": "f5f5f5"
  },
  "extruder_temp_range": {
    "zyltech_petg_petgwhite_1000_175_p": [
      220,
      250
    ],
    "zyltech_petg_zyltechpetgwhite_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp_range": {
    "zyltech_petg_petgwhite_1000_175_p": [
      70,
      90
    ],
    "zyltech_petg_zyltechpetgwhite_1000_175_p": [
      70,
      85
    ]
  }
}
```

### ZY003: dup-3bb100a2b53380440ffdfccd5b2348c4137af3cadb1559f7a74194d265bf7c4e

Status: APPROVED; survivor `zyltech_pla_plagray_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`zyltech_pla_plagray_1000_175_p`|`PLA {color_name}`|`Gray`|{"source_file": "zyltech.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`zyltech_pla_zyltechplagrey_1000_175_p`|`Zyltech PLA {color_name}`|`Grey`|{"source_file": "zyltech.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "zyltech_pla_plagray_1000_175_p": "949A9E",
    "zyltech_pla_zyltechplagrey_1000_175_p": "808080"
  },
  "extruder_temp_range": {
    "zyltech_pla_plagray_1000_175_p": [
      190,
      230
    ],
    "zyltech_pla_zyltechplagrey_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "zyltech_pla_plagray_1000_175_p": [
      50,
      70
    ],
    "zyltech_pla_zyltechplagrey_1000_175_p": [
      50,
      60
    ]
  }
}
```

### ZY004: dup-f7feb13c87b9a2a9d011fda54d3278b952384962acd9befd25493b206799011d

Status: APPROVED; survivor `zyltech_pla_plagreen_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`zyltech_pla_plagreen_1000_175_p`|`PLA {color_name}`|`Green`|{"source_file": "zyltech.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`zyltech_pla_zyltechplagreen_1000_175_p`|`Zyltech PLA {color_name}`|`Green`|{"source_file": "zyltech.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "zyltech_pla_plagreen_1000_175_p": "70FA00",
    "zyltech_pla_zyltechplagreen_1000_175_p": "2e7d32"
  },
  "extruder_temp_range": {
    "zyltech_pla_plagreen_1000_175_p": [
      190,
      230
    ],
    "zyltech_pla_zyltechplagreen_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "zyltech_pla_plagreen_1000_175_p": [
      50,
      70
    ],
    "zyltech_pla_zyltechplagreen_1000_175_p": [
      50,
      60
    ]
  }
}
```

### ZY005: dup-3d9f172d01d22edf19595b47fbfbbdbf442b952d4e40cc43dac26750ffdda947

Status: APPROVED; survivor `zyltech_pla_plaorange_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`zyltech_pla_plaorange_1000_175_p`|`PLA {color_name}`|`Orange`|{"source_file": "zyltech.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`zyltech_pla_zyltechplaorange_1000_175_p`|`Zyltech PLA {color_name}`|`Orange`|{"source_file": "zyltech.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "zyltech_pla_plaorange_1000_175_p": "FF8E24",
    "zyltech_pla_zyltechplaorange_1000_175_p": "f57c00"
  },
  "extruder_temp_range": {
    "zyltech_pla_plaorange_1000_175_p": [
      190,
      230
    ],
    "zyltech_pla_zyltechplaorange_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "zyltech_pla_plaorange_1000_175_p": [
      50,
      70
    ],
    "zyltech_pla_zyltechplaorange_1000_175_p": [
      50,
      60
    ]
  }
}
```

### ZY006: dup-589ae1c39b6611f00b3fcade8d674a0c94a8b4c048225afccb6886698be080db

Status: APPROVED; survivor `zyltech_pla_playellow_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`zyltech_pla_playellow_1000_175_p`|`PLA {color_name}`|`Yellow`|{"source_file": "zyltech.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`zyltech_pla_zyltechplayellow_1000_175_p`|`Zyltech PLA {color_name}`|`Yellow`|{"source_file": "zyltech.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "zyltech_pla_playellow_1000_175_p": "FFFB00",
    "zyltech_pla_zyltechplayellow_1000_175_p": "fdd835"
  },
  "extruder_temp_range": {
    "zyltech_pla_playellow_1000_175_p": [
      190,
      230
    ],
    "zyltech_pla_zyltechplayellow_1000_175_p": [
      190,
      220
    ]
  },
  "bed_temp_range": {
    "zyltech_pla_playellow_1000_175_p": [
      50,
      70
    ],
    "zyltech_pla_zyltechplayellow_1000_175_p": [
      50,
      60
    ]
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "zyltech_pla_plagray_1000_175_p",
      "values": {
        "density": 1.27,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://www.zyltech.com/pla-3d-printer-filament-1-75mm-1-kg-2-2-lbs/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "zyltech_pla_plaorange_1000_175_p",
      "values": {
        "density": 1.27,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://www.zyltech.com/pla-3d-printer-filament-1-75mm-1-kg-2-2-lbs/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "zyltech_pla_playellow_1000_175_p",
      "values": {
        "density": 1.27,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://www.zyltech.com/pla-3d-printer-filament-1-75mm-1-kg-2-2-lbs/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "zyltech_petg_petgwhite_1000_175_p",
      "values": {
        "bed_temp_range": [
          65,
          85
        ]
      },
      "source": "https://www.zyltech.com/petg-3d-printer-filament-1-75mm-1-kg-2-2-lbs/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "zyltech_petg_petgblack_1000_175_p",
      "values": {
        "bed_temp_range": [
          65,
          85
        ]
      },
      "source": "https://www.zyltech.com/petg-3d-printer-filament-1-75mm-1-kg-2-2-lbs/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "zyltech_pla_plagreen_1000_175_p",
      "values": {
        "density": 1.27,
        "extruder_temp_range": [
          200,
          220
        ]
      },
      "source": "https://www.zyltech.com/pla-3d-printer-filament-1-75mm-1-kg-2-2-lbs/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    }
  ],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `zyltech_pla_zyltechplablack_1000_175_p` — Zyltech PLA Black
- `zyltech_pla_zyltechplawhite_1000_175_p` — Zyltech PLA White
- `zyltech_pla_zyltechplared_1000_175_p` — Zyltech PLA Red
- `zyltech_pla_zyltechplablue_1000_175_p` — Zyltech PLA Blue
- `zyltech_pla_zyltechplapurple_1000_175_p` — Zyltech PLA Purple
- `zyltech_pla_zyltechplanatural_1000_175_p` — Zyltech PLA Natural
- `zyltech_petg_zyltechpetgblue_1000_175_p` — Zyltech PETG Blue
- `zyltech_petg_zyltechpetgclear_1000_175_p` — Zyltech PETG Clear
- `zyltech_asa_asablack_1000_175_p` — ASA Black
- `zyltech_asa_asagray_1000_175_p` — ASA Gray
- `zyltech_asa_matteasaeggshell_1000_175_p` — Matte ASA Eggshell
- `zyltech_asa_matteasagray_1000_175_p` — Matte ASA Gray
- `zyltech_asa_matteasagreen_1000_175_p` — Matte ASA Green
- `zyltech_asa_matteasared_1000_175_p` — Matte ASA Red
- `zyltech_petg_petgarmygreen_1000_175_p` — PETG Army Green
- `zyltech_petg_petgblacktexassizespool_1000_175_p` — PETG Black Texas Size Spool
- `zyltech_petg_petgbrightgreen_1000_175_p` — PETG Bright Green
- `zyltech_petg_petgbrown_1000_175_p` — PETG Brown
- `zyltech_petg_petgbrowntexassizespool_1000_175_p` — PETG Brown Texas Size Spool
- `zyltech_petg_petgcleartexassizespool_1000_175_p` — PETG Clear Texas Size Spool
- `zyltech_petg_petgdeepblue_1000_175_p` — PETG Deep Blue
- `zyltech_petg_petgdeepbluetexassizespool_1000_175_p` — PETG Deep Blue Texas Size Spool
- `zyltech_petg_petggray_1000_175_p` — PETG Gray
- `zyltech_petg_petggraytexassizespool_1000_175_p` — PETG Gray Texas Size Spool
- `zyltech_petg_petggreen_1000_175_p` — PETG Green
- `zyltech_petg_petggunmetalsilvertexassizespool_1000_175_p` — PETG Gun Metal Silver Texas Size Spool
- `zyltech_petg_petgmaroon_1000_175_p` — PETG Maroon
- `zyltech_petg_petgmaroontexassizespool_1000_175_p` — PETG Maroon Texas Size Spool
- `zyltech_petg_petgorange_1000_175_p` — PETG Orange
- `zyltech_petg_petgorangetexassizespool_1000_175_p` — PETG Orange Texas Size Spool
- `zyltech_petg_petgpurple_1000_175_p` — PETG Purple
- `zyltech_petg_petgpurpletexassizespool_1000_175_p` — PETG Purple Texas Size Spool
- `zyltech_petg_petgred_1000_175_p` — PETG Red
- `zyltech_petg_petgredtexassizespool_1000_175_p` — PETG Red Texas Size Spool
- `zyltech_petg_petgtransparent_1000_175_p` — PETG Transparent
- `zyltech_petg_petgunclejessy'sgunmetalsilver_1000_175_p` — PETG Uncle Jessy's Gun Metal Silver
- `zyltech_petg_petgwhitetexassizespool_1000_175_p` — PETG White Texas Size Spool
- `zyltech_petg_petgyellow_1000_175_p` — PETG Yellow
- `zyltech_petg_petgyellowtexassizespool_1000_175_p` — PETG Yellow Texas Size Spool
- `zyltech_pla_placfcomposite_1000_175_p` — PLA CF Composite
- `zyltech_pla_glowplahauntedemborglowindarkluminous_1000_175_p` — Glow PLA Haunted Embor Glow in Dark Luminous
- `zyltech_pla_glowplarainbowgalaxyglowindarkluminous_1000_175_p` — Glow PLA Rainbow Galaxy Glow in Dark Luminous
- `zyltech_pla_glowplastardustglowglowindarkluminous_1000_175_p` — Glow PLA Stardust Glow Glow in Dark Luminous
- `zyltech_pla_matteplablack_1000_175_p` — Matte PLA Black
- `zyltech_pla_matteplakingscakedualcolor_1000_175_p` — Matte PLA Kings Cake Dual Color
- `zyltech_pla_plaarmygreen_1000_175_p` — PLA Army Green
- `zyltech_pla_plabahamablue_1000_175_p` — PLA Bahama Blue
- `zyltech_pla_placeramicwhite_1000_175_p` — PLA Ceramic White
- `zyltech_pla_placlear/natural_1000_175_p` — PLA Clear/Natural
- `zyltech_pla_placobaltbluemetallic_1000_175_p` — PLA Cobalt Blue Metallic
- `zyltech_pla_placocoabrown_1000_175_p` — PLA Cocoa Brown
- `zyltech_pla_placookielovepink_1000_175_p` — PLA Cookie Love Pink
- `zyltech_pla_placosmicsparkle(clearw/glitterflakes)_1000_175_p` — PLA Cosmic Sparkle (Clear w/ Glitter Flakes)
- `zyltech_pla_pladarkgreen_1000_175_p` — PLA Dark Green
- `zyltech_pla_pladeepblue_1000_175_p` — PLA Deep Blue
- `zyltech_pla_plafluorescentblue_1000_175_p` — PLA Fluorescent Blue
- `zyltech_pla_plafluorescentred/hotpink_1000_175_p` — PLA Fluorescent Red/Hot Pink
- `zyltech_pla_plafortressgray_1000_175_p` — PLA Fortress Gray
- `zyltech_pla_plagreentexassizespool_1000_175_p` — PLA Green Texas Size Spool
- `zyltech_pla_plahighlighterfluorescentgreen_1000_175_p` — PLA Highlighter Fluorescent Green
- `zyltech_pla_plalightblue_1000_175_p` — PLA Light Blue
- `zyltech_pla_plalipstickred_1000_175_p` — PLA Lipstick Red
- `zyltech_pla_plamajesticpurple_1000_175_p` — PLA Majestic Purple
- `zyltech_pla_plamaroon_1000_175_p` — PLA Maroon
- `zyltech_pla_plamilkywhite_1000_175_p` — PLA Milky White
- `zyltech_pla_plapanhandlekhaki_1000_175_p` — PLA Panhandle Khaki
- `zyltech_pla_plapink_1000_175_p` — PLA Pink
- `zyltech_pla_plapumpkinspice_1000_175_p` — PLA Pumpkin Spice
- `zyltech_pla_plaseaglassteal_1000_175_p` — PLA Sea Glass Teal
- `zyltech_pla_plataropurple_1000_175_p` — PLA Taro Purple
- `zyltech_pla_plaunclejessy'sgunmetalsilver_1000_175_p` — PLA Uncle Jessy's Gun Metal Silver
- `zyltech_pla_plawood+composite_1000_175_p` — PLA Wood+ Composite
- `zyltech_pla_silkplaamberoxidetri-color_1000_175_p` — Silk PLA Amber Oxide Tri-Color
- `zyltech_pla_silkplaaquaserenitydualcolor_1000_175_p` — Silk PLA Aqua Serenity Dual Color
- `zyltech_pla_silkplablacknewmadeinusapremiumcomposite_1000_175_p` — Silk PLA Black New Made In USA Premium Composite
- `zyltech_pla_silkplabluenewmadeinusapremiumcomposite_1000_175_p` — Silk PLA Blue New Made In USA Premium Composite
- `zyltech_pla_silkplabronzemetallic_1000_175_p` — Silk PLA Bronze Metallic
- `zyltech_pla_silkplaburnishedbrilliancedualcolor_1000_175_p` — Silk PLA Burnished Brilliance Dual Color
- `zyltech_pla_silkplacandyskies2024rainbowseries_1000_175_p` — Silk PLA Candy Skies 2024 Rainbow Series
- `zyltech_pla_silkplacelestialcascade2024rainbowseries_1000_175_p` — Silk PLA Celestial Cascade 2024 Rainbow Series
- `zyltech_pla_silkplacoinagemetalstri-color_1000_175_p` — Silk PLA Coinage Metals Tri-Color
- `zyltech_pla_silkplacoraldreamdualgradient_1000_175_p` — Silk PLA Coral Dream Dual Gradient
- `zyltech_pla_silkplacrimsonnoirdualcolor_1000_175_p` — Silk PLA Crimson Noir Dual Color
- `zyltech_pla_silkplaelectricdreamtri-color_1000_175_p` — Silk PLA Electric Dream Tri-Color
- `zyltech_pla_silkplaemeraldwaterdualcolor_1000_175_p` — Silk PLA Emerald Water Dual Color
- `zyltech_pla_silkplaexoticorchiddualcolor_1000_175_p` — Silk PLA Exotic Orchid Dual Color
- `zyltech_pla_silkplaforestpalette2024rainbowseries_1000_175_p` — Silk PLA Forest Palette 2024 Rainbow Series
- `zyltech_pla_silkplaglossyblack_1000_175_p` — Silk PLA Glossy Black
- `zyltech_pla_silkplagoldnewmadeinusapremiumcomposite_1000_175_p` — Silk PLA Gold New Made In USA Premium Composite
- `zyltech_pla_silkplagoldenhalodualcolor_1000_175_p` — Silk PLA Golden Halo Dual Color
- `zyltech_pla_silkplagreennewmadeinusapremiumcomposite_1000_175_p` — Silk PLA Green New Made In USA Premium Composite
- `zyltech_pla_silkplakaleidoscopetri-color_1000_175_p` — Silk PLA Kaleidoscope Tri-Color
- `zyltech_pla_silkplalemonadebreezedualcolor_1000_175_p` — Silk PLA Lemonade Breeze Dual Color
- `zyltech_pla_silkplaluckyclovertri-color_1000_175_p` — Silk PLA Lucky Clover Tri-Color
- `zyltech_pla_silkplamacaronmedley2024rainbowseries_1000_175_p` — Silk PLA Macaron Medley 2024 Rainbow Series
- `zyltech_pla_silkplamidnightplumdualgradient_1000_175_p` — Silk PLA Midnight Plum Dual Gradient
- `zyltech_pla_silkplanewrainbow2024rainbowseries_1000_175_p` — Silk PLA New Rainbow 2024 Rainbow Series
- `zyltech_pla_silkplanikko'shotrodrednewmadeinusapremiumcomposite_1000_175_p` — Silk PLA Nikko's Hot Rod Red New Made In USA Premium Composite
- `zyltech_pla_silkplapinknewmadeinusapremiumcomposite_1000_175_p` — Silk PLA Pink New Made In USA Premium Composite
- `zyltech_pla_silkplapsychedelic2024rainbowseries_1000_175_p` — Silk PLA Psychedelic 2024 Rainbow Series
- `zyltech_pla_silkplapurplenewmadeinusapremiumcomposite_1000_175_p` — Silk PLA Purple New Made In USA Premium Composite
- `zyltech_pla_silkplarainbowradiance2024rainbowseries_1000_175_p` — Silk PLA Rainbow Radiance 2024 Rainbow Series
- `zyltech_pla_silkplaregalvineyardtri-color_1000_175_p` — Silk PLA Regal Vineyard Tri-Color
- `zyltech_pla_silkplashadowbladedualcolor_1000_175_p` — Silk PLA Shadow Blade Dual Color
- `zyltech_pla_silkplasilverskydualcolor_1000_175_p` — Silk PLA Silver Sky Dual Color
- `zyltech_pla_silkplastellarflaredualgradient_1000_175_p` — Silk PLA Stellar Flare Dual Gradient
- `zyltech_pla_silkplasunnyindigotri-color_1000_175_p` — Silk PLA Sunny Indigo Tri-Color
- `zyltech_pla_silkplasunsetserenadedualcolor_1000_175_p` — Silk PLA Sunset Serenade Dual Color
- `zyltech_pla_silkplatechnicolortwist2024rainbowseries_1000_175_p` — Silk PLA Technicolor Twist 2024 Rainbow Series
- `zyltech_pla_silkplatexasskydualcolor_1000_175_p` — Silk PLA Texas Sky Dual Color
- `zyltech_pla_silkplatiger'seyedualgradient_1000_175_p` — Silk PLA Tiger's Eye Dual Gradient
- `zyltech_pla_silkplatropicalbreezetri-color_1000_175_p` — Silk PLA Tropical Breeze Tri-Color
- `zyltech_pla_silkplaunclejessy'sgunmetalsilvermetallic_1000_175_p` — Silk PLA Uncle Jessy's Gun Metal Silver Metallic
- `zyltech_pla_silkplavibranttreasurestri-color_1000_175_p` — Silk PLA Vibrant Treasures Tri-Color
- `zyltech_pla_silkplavividfusion2024rainbowseries_1000_175_p` — Silk PLA Vivid Fusion 2024 Rainbow Series
- `zyltech_pla_silkplawhitenewmadeinusapremiumcomposite_1000_175_p` — Silk PLA White New Made In USA Premium Composite
- `zyltech_pla_texastwisterseriesmulticolormatteplamidnightmarble_1000_175_p` — Texas Twister Series Multi Color Matte PLA Midnight Marble
- `zyltech_pla_texastwisterseriesmulticolorplaevergladeessence_1000_175_p` — Texas Twister Series Multi Color PLA Everglade Essence
- `zyltech_pla_texastwisterseriesmulticolorsilkplalimeripple_1000_175_p` — Texas Twister Series Multi Color Silk PLA Lime Ripple
- `zyltech_pla_texastwisterseriesmulticolorsilkplasapphiremoon_1000_175_p` — Texas Twister Series Multi Color Silk PLA Sapphire Moon
- `zyltech_pla_texastwisterseriesmulticolorsilkplasterlingwave_1000_175_p` — Texas Twister Series Multi Color Silk PLA Sterling Wave
- `zyltech_pla_texastwisterseriesmulticolorsilkplatwistedcarnival_1000_175_p` — Texas Twister Series Multi Color Silk PLA Twisted Carnival
- `zyltech_tpu_tpublack_1000_175_p` — TPU Black
- `zyltech_tpu_tpublue_1000_175_p` — TPU Blue
- `zyltech_tpu_tpured_1000_175_p` — TPU Red
