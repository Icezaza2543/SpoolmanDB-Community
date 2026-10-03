# americanfilament duplicate migration review

Base `bd94f1d0a6c3fab56b1d50636522ab6c427016c4`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `88dfd3e3db2444a6de4aa610139bd8d028399b1bb23bcd0a6cca27b461390b84`.

## Authorization and result

{"groups": 17, "approved_groups": 13, "retired": 13, "deferred": 4, "hard_stops": 0, "before_count": 51826, "after_count": 51813, "brand_before": 146, "brand_after": 133, "registry_before": 1608, "registry_after": 1621, "metadata_fields_changed": 13, "code_transfers": 13, "new": 0, "changed_identity": 0, "rekeyed": 0}

Thirteen exact1000g1.75mm Silk survivor nozzle ranges corrected to current220–235; existing50–70bed retained. Thirteen explicitly1KG Silk codes preserved on exact target survivors only; no fanout. Silk density1.24 unverified and HEX/finish conflicts retained. Four PCTG groups deferred because mixed-weight identifiers cannot safely be transferred wholesale; current exact PCTG corrections documented but not applied to deferred groups. Packaging/tare unchanged.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://americanfilament.us/products/silky-arctic-white-1-75mm-pla-filament", "nozzle": [220, 235], "bed": [50, 70]}
- {"url": "https://americanfilament.us/products/silky-rose-gold-1-75mm-pla-filament", "nozzle": [220, 235], "bed": [50, 70]}
- {"url": "https://americanfilament.us/collections/silky-af-pla", "note": "current exact Silk line; no exact density document located"}
- {"url": "https://americanfilament.us/products/blizzard-white-af-1-75mm-pctg-filament-made-in-the-usa", "note": "exact current PCTG line, no package-code binding established"}
- {"url": "https://cdn.shopify.com/s/files/1/0560/2741/4702/files/AF_PCTG_Technical_Data_Sheet_-_TDS.pdf?v=1741726850", "density": 1.27, "nozzle": [240, 270], "bed": [70, 100], "scope": "deferred PCTG audit evidence only; no PCTG edits"}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`americanfilament_pla_americanfilamentsilkplaamethystpurple_1000_175_p`|`americanfilament_pla_silkplaamethystpurple_1000_175_p`|`americanfilament.json::American Filament::American Filament Silk PLA {color_name}::American Filament Silk PLA Amethyst Purple::PLA::1000::1.75::plastic::False`|
|`americanfilament_pla_americanfilamentsilkplaarcticwhite_1000_175_p`|`americanfilament_pla_silkplaarcticwhite_1000_175_p`|`americanfilament.json::American Filament::American Filament Silk PLA {color_name}::American Filament Silk PLA Arctic White::PLA::1000::1.75::plastic::False`|
|`americanfilament_pla_americanfilamentsilkplablue_1000_175_p`|`americanfilament_pla_silkplablue_1000_175_p`|`americanfilament.json::American Filament::American Filament Silk PLA {color_name}::American Filament Silk PLA Blue::PLA::1000::1.75::plastic::False`|
|`americanfilament_pla_americanfilamentsilkplaemeraldgreen_1000_175_p`|`americanfilament_pla_silkplaemeraldgreen_1000_175_p`|`americanfilament.json::American Filament::American Filament Silk PLA {color_name}::American Filament Silk PLA Emerald Green::PLA::1000::1.75::plastic::False`|
|`americanfilament_pla_americanfilamentsilkplagraphite_1000_175_p`|`americanfilament_pla_silkplagraphite_1000_175_p`|`americanfilament.json::American Filament::American Filament Silk PLA {color_name}::American Filament Silk PLA Graphite::PLA::1000::1.75::plastic::False`|
|`americanfilament_pla_americanfilamentsilkplaneongreen_1000_175_p`|`americanfilament_pla_silkplaneongreen_1000_175_p`|`americanfilament.json::American Filament::American Filament Silk PLA {color_name}::American Filament Silk PLA Neon Green::PLA::1000::1.75::plastic::False`|
|`americanfilament_pla_americanfilamentsilkplaneonorange_1000_175_p`|`americanfilament_pla_silkplaneonorange_1000_175_p`|`americanfilament.json::American Filament::American Filament Silk PLA {color_name}::American Filament Silk PLA Neon Orange::PLA::1000::1.75::plastic::False`|
|`americanfilament_pla_americanfilamentsilkplaneonpink_1000_175_p`|`americanfilament_pla_silkplaneonpink_1000_175_p`|`americanfilament.json::American Filament::American Filament Silk PLA {color_name}::American Filament Silk PLA Neon Pink::PLA::1000::1.75::plastic::False`|
|`americanfilament_pla_americanfilamentsilkplapurple_1000_175_p`|`americanfilament_pla_silkplapurple_1000_175_p`|`americanfilament.json::American Filament::American Filament Silk PLA {color_name}::American Filament Silk PLA Purple::PLA::1000::1.75::plastic::False`|
|`americanfilament_pla_americanfilamentsilkplared_1000_175_p`|`americanfilament_pla_silkplared_1000_175_p`|`americanfilament.json::American Filament::American Filament Silk PLA {color_name}::American Filament Silk PLA Red::PLA::1000::1.75::plastic::False`|
|`americanfilament_pla_americanfilamentsilkplarosegold_1000_175_p`|`americanfilament_pla_silkplarosegold_1000_175_p`|`americanfilament.json::American Filament::American Filament Silk PLA {color_name}::American Filament Silk PLA Rose Gold::PLA::1000::1.75::plastic::False`|
|`americanfilament_pla_americanfilamentsilkplateal_1000_175_p`|`americanfilament_pla_silkplateal_1000_175_p`|`americanfilament.json::American Filament::American Filament Silk PLA {color_name}::American Filament Silk PLA Teal::PLA::1000::1.75::plastic::False`|
|`americanfilament_pla_americanfilamentsilkplayellow_1000_175_p`|`americanfilament_pla_silkplayellow_1000_175_p`|`americanfilament.json::American Filament::American Filament Silk PLA {color_name}::American Filament Silk PLA Yellow::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### AF001: dup-0cbd82daca2198c43293ed83488990f8ff57d0a83cfe5a4f3176c531b7583dc9

Status: DEFERRED; survivor `americanfilament_pctg_pctgarmygreen_1000_175_p`; PCTG source arrays replicate1KG and4KG codes across weights; live exact SKU binding unavailable. Do not transfer4KG to1000g; retain both records pending exact package-scoped review/tooling..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`americanfilament_pctg_americanfilamentpctgarmygreen_1000_175_p`|`American Filament PCTG {color_name}`|`Army Green`|{"source_file": "americanfilament.json", "definition_index": 3, "weights": 2, "diameters": 1, "colors": 16, "compiled_records": 32} / False|
|`americanfilament_pctg_pctgarmygreen_1000_175_p`|`PCTG {color_name}`|`Army Green`|{"source_file": "americanfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "americanfilament_pctg_americanfilamentpctgarmygreen_1000_175_p": 1.27,
    "americanfilament_pctg_pctgarmygreen_1000_175_p": 1.23
  },
  "spool_weight": {
    "americanfilament_pctg_americanfilamentpctgarmygreen_1000_175_p": 220,
    "americanfilament_pctg_pctgarmygreen_1000_175_p": null
  },
  "color_hex": {
    "americanfilament_pctg_americanfilamentpctgarmygreen_1000_175_p": "36361e",
    "americanfilament_pctg_pctgarmygreen_1000_175_p": "515234"
  },
  "extruder_temp_range": {
    "americanfilament_pctg_americanfilamentpctgarmygreen_1000_175_p": [
      240,
      270
    ],
    "americanfilament_pctg_pctgarmygreen_1000_175_p": [
      230,
      260
    ]
  },
  "bed_temp_range": {
    "americanfilament_pctg_americanfilamentpctgarmygreen_1000_175_p": [
      70,
      100
    ],
    "americanfilament_pctg_pctgarmygreen_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "americanfilament_pctg_americanfilamentpctgarmygreen_1000_175_p": [
      "PCTG_1KG_ARMYG",
      "PCTG_4KG_ARMYG"
    ],
    "americanfilament_pctg_pctgarmygreen_1000_175_p": null
  },
  "sds_url": {
    "americanfilament_pctg_americanfilamentpctgarmygreen_1000_175_p": "https://cdn.shopify.com/s/files/1/0560/2741/4702/files/AF_PCTG_US_Material_Safety_Data_Sheet_-_MSDS.pdf",
    "americanfilament_pctg_pctgarmygreen_1000_175_p": null
  },
  "tds_url": {
    "americanfilament_pctg_americanfilamentpctgarmygreen_1000_175_p": "https://cdn.shopify.com/s/files/1/0560/2741/4702/files/AF_PCTG_Technical_Data_Sheet_-_TDS.pdf",
    "americanfilament_pctg_pctgarmygreen_1000_175_p": null
  }
}
```

### AF002: dup-793c5a66c846857b1437cf6b3e8afdc8207fc302c6f85abf70148c350477a30a

Status: DEFERRED; survivor `americanfilament_pctg_pctgblizzardwhite_1000_175_p`; PCTG source arrays replicate1KG and4KG codes across weights; live exact SKU binding unavailable. Do not transfer4KG to1000g; retain both records pending exact package-scoped review/tooling..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`americanfilament_pctg_americanfilamentpctgblizzardwhite_1000_175_p`|`American Filament PCTG {color_name}`|`Blizzard White`|{"source_file": "americanfilament.json", "definition_index": 3, "weights": 2, "diameters": 1, "colors": 16, "compiled_records": 32} / False|
|`americanfilament_pctg_pctgblizzardwhite_1000_175_p`|`PCTG {color_name}`|`Blizzard White`|{"source_file": "americanfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "americanfilament_pctg_americanfilamentpctgblizzardwhite_1000_175_p": 1.27,
    "americanfilament_pctg_pctgblizzardwhite_1000_175_p": 1.23
  },
  "spool_weight": {
    "americanfilament_pctg_americanfilamentpctgblizzardwhite_1000_175_p": 220,
    "americanfilament_pctg_pctgblizzardwhite_1000_175_p": null
  },
  "color_hex": {
    "americanfilament_pctg_americanfilamentpctgblizzardwhite_1000_175_p": "e8e8e8",
    "americanfilament_pctg_pctgblizzardwhite_1000_175_p": "FFFFFF"
  },
  "extruder_temp_range": {
    "americanfilament_pctg_americanfilamentpctgblizzardwhite_1000_175_p": [
      240,
      270
    ],
    "americanfilament_pctg_pctgblizzardwhite_1000_175_p": [
      230,
      260
    ]
  },
  "bed_temp_range": {
    "americanfilament_pctg_americanfilamentpctgblizzardwhite_1000_175_p": [
      70,
      100
    ],
    "americanfilament_pctg_pctgblizzardwhite_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "americanfilament_pctg_americanfilamentpctgblizzardwhite_1000_175_p": [
      "PCTG_1KG_WHITE",
      "PCTG_4KG_WHITE"
    ],
    "americanfilament_pctg_pctgblizzardwhite_1000_175_p": null
  },
  "sds_url": {
    "americanfilament_pctg_americanfilamentpctgblizzardwhite_1000_175_p": "https://cdn.shopify.com/s/files/1/0560/2741/4702/files/AF_PCTG_US_Material_Safety_Data_Sheet_-_MSDS.pdf",
    "americanfilament_pctg_pctgblizzardwhite_1000_175_p": null
  },
  "tds_url": {
    "americanfilament_pctg_americanfilamentpctgblizzardwhite_1000_175_p": "https://cdn.shopify.com/s/files/1/0560/2741/4702/files/AF_PCTG_Technical_Data_Sheet_-_TDS.pdf",
    "americanfilament_pctg_pctgblizzardwhite_1000_175_p": null
  }
}
```

### AF003: dup-76c5690a3879b598d0b4ecb78333c50a73f26633fed94092d7d2f4fda6d68fbe

Status: DEFERRED; survivor `americanfilament_pctg_pctggunmetalgray_1000_175_p`; PCTG source arrays replicate1KG and4KG codes across weights; live exact SKU binding unavailable. Do not transfer4KG to1000g; retain both records pending exact package-scoped review/tooling..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`americanfilament_pctg_americanfilamentpctggunmetalgray_1000_175_p`|`American Filament PCTG {color_name}`|`Gunmetal Gray`|{"source_file": "americanfilament.json", "definition_index": 3, "weights": 2, "diameters": 1, "colors": 16, "compiled_records": 32} / False|
|`americanfilament_pctg_pctggunmetalgray_1000_175_p`|`PCTG {color_name}`|`Gunmetal Gray`|{"source_file": "americanfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "americanfilament_pctg_americanfilamentpctggunmetalgray_1000_175_p": 1.27,
    "americanfilament_pctg_pctggunmetalgray_1000_175_p": 1.23
  },
  "spool_weight": {
    "americanfilament_pctg_americanfilamentpctggunmetalgray_1000_175_p": 220,
    "americanfilament_pctg_pctggunmetalgray_1000_175_p": null
  },
  "color_hex": {
    "americanfilament_pctg_americanfilamentpctggunmetalgray_1000_175_p": "363636",
    "americanfilament_pctg_pctggunmetalgray_1000_175_p": "6A6C6E"
  },
  "extruder_temp_range": {
    "americanfilament_pctg_americanfilamentpctggunmetalgray_1000_175_p": [
      240,
      270
    ],
    "americanfilament_pctg_pctggunmetalgray_1000_175_p": [
      230,
      260
    ]
  },
  "bed_temp_range": {
    "americanfilament_pctg_americanfilamentpctggunmetalgray_1000_175_p": [
      70,
      100
    ],
    "americanfilament_pctg_pctggunmetalgray_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "americanfilament_pctg_americanfilamentpctggunmetalgray_1000_175_p": [
      "PCTG_1KG_GUNMETAL",
      "PCTG_4KG_GUNMETAL"
    ],
    "americanfilament_pctg_pctggunmetalgray_1000_175_p": null
  },
  "sds_url": {
    "americanfilament_pctg_americanfilamentpctggunmetalgray_1000_175_p": "https://cdn.shopify.com/s/files/1/0560/2741/4702/files/AF_PCTG_US_Material_Safety_Data_Sheet_-_MSDS.pdf",
    "americanfilament_pctg_pctggunmetalgray_1000_175_p": null
  },
  "tds_url": {
    "americanfilament_pctg_americanfilamentpctggunmetalgray_1000_175_p": "https://cdn.shopify.com/s/files/1/0560/2741/4702/files/AF_PCTG_Technical_Data_Sheet_-_TDS.pdf",
    "americanfilament_pctg_pctggunmetalgray_1000_175_p": null
  }
}
```

### AF004: dup-555a43455a3fec10a9a0e419a007527eb4c953aaee9dd9c296af49c72d51d8e7

Status: DEFERRED; survivor `americanfilament_pctg_pctgobsidianblack_1000_175_p`; PCTG source arrays replicate1KG and4KG codes across weights; live exact SKU binding unavailable. Do not transfer4KG to1000g; retain both records pending exact package-scoped review/tooling..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`americanfilament_pctg_americanfilamentpctgobsidianblack_1000_175_p`|`American Filament PCTG {color_name}`|`Obsidian Black`|{"source_file": "americanfilament.json", "definition_index": 3, "weights": 2, "diameters": 1, "colors": 16, "compiled_records": 32} / False|
|`americanfilament_pctg_pctgobsidianblack_1000_175_p`|`PCTG {color_name}`|`Obsidian Black`|{"source_file": "americanfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "americanfilament_pctg_americanfilamentpctgobsidianblack_1000_175_p": 1.27,
    "americanfilament_pctg_pctgobsidianblack_1000_175_p": 1.23
  },
  "spool_weight": {
    "americanfilament_pctg_americanfilamentpctgobsidianblack_1000_175_p": 220,
    "americanfilament_pctg_pctgobsidianblack_1000_175_p": null
  },
  "color_hex": {
    "americanfilament_pctg_americanfilamentpctgobsidianblack_1000_175_p": "2a2a2a",
    "americanfilament_pctg_pctgobsidianblack_1000_175_p": "000000"
  },
  "extruder_temp_range": {
    "americanfilament_pctg_americanfilamentpctgobsidianblack_1000_175_p": [
      240,
      270
    ],
    "americanfilament_pctg_pctgobsidianblack_1000_175_p": [
      230,
      260
    ]
  },
  "bed_temp_range": {
    "americanfilament_pctg_americanfilamentpctgobsidianblack_1000_175_p": [
      70,
      100
    ],
    "americanfilament_pctg_pctgobsidianblack_1000_175_p": [
      70,
      90
    ]
  },
  "codes": {
    "americanfilament_pctg_americanfilamentpctgobsidianblack_1000_175_p": [
      "PCTG_1KG_BLACK",
      "PCTG_4KG_BLACK"
    ],
    "americanfilament_pctg_pctgobsidianblack_1000_175_p": null
  },
  "sds_url": {
    "americanfilament_pctg_americanfilamentpctgobsidianblack_1000_175_p": "https://cdn.shopify.com/s/files/1/0560/2741/4702/files/AF_PCTG_US_Material_Safety_Data_Sheet_-_MSDS.pdf",
    "americanfilament_pctg_pctgobsidianblack_1000_175_p": null
  },
  "tds_url": {
    "americanfilament_pctg_americanfilamentpctgobsidianblack_1000_175_p": "https://cdn.shopify.com/s/files/1/0560/2741/4702/files/AF_PCTG_Technical_Data_Sheet_-_TDS.pdf",
    "americanfilament_pctg_pctgobsidianblack_1000_175_p": null
  }
}
```

### AF005: dup-601bf8a89c00d2c4d53a7e21e0d06e040da40c26df131cfbf0d92b8abc2f648e

Status: APPROVED; survivor `americanfilament_pla_silkplaamethystpurple_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`americanfilament_pla_americanfilamentsilkplaamethystpurple_1000_175_p`|`American Filament Silk PLA {color_name}`|`Amethyst Purple`|{"source_file": "americanfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`americanfilament_pla_silkplaamethystpurple_1000_175_p`|`Silk PLA {color_name}`|`Amethyst Purple`|{"source_file": "americanfilament.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "americanfilament_pla_americanfilamentsilkplaamethystpurple_1000_175_p": 220,
    "americanfilament_pla_silkplaamethystpurple_1000_175_p": null
  },
  "color_hex": {
    "americanfilament_pla_americanfilamentsilkplaamethystpurple_1000_175_p": "ae8ac6",
    "americanfilament_pla_silkplaamethystpurple_1000_175_p": "8D65C7"
  },
  "extruder_temp_range": {
    "americanfilament_pla_americanfilamentsilkplaamethystpurple_1000_175_p": [
      205,
      220
    ],
    "americanfilament_pla_silkplaamethystpurple_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "americanfilament_pla_americanfilamentsilkplaamethystpurple_1000_175_p": [
      45,
      60
    ],
    "americanfilament_pla_silkplaamethystpurple_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "americanfilament_pla_americanfilamentsilkplaamethystpurple_1000_175_p": "glossy",
    "americanfilament_pla_silkplaamethystpurple_1000_175_p": null
  },
  "codes": {
    "americanfilament_pla_americanfilamentsilkplaamethystpurple_1000_175_p": [
      "SILK_1KG_AMETHYST"
    ],
    "americanfilament_pla_silkplaamethystpurple_1000_175_p": null
  }
}
```

### AF006: dup-fe68cd805e1689c11a55172a05ada908796bcdf17c892e73f2e65c2aea461ad1

Status: APPROVED; survivor `americanfilament_pla_silkplaarcticwhite_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`americanfilament_pla_americanfilamentsilkplaarcticwhite_1000_175_p`|`American Filament Silk PLA {color_name}`|`Arctic White`|{"source_file": "americanfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`americanfilament_pla_silkplaarcticwhite_1000_175_p`|`Silk PLA {color_name}`|`Arctic White`|{"source_file": "americanfilament.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "americanfilament_pla_americanfilamentsilkplaarcticwhite_1000_175_p": 220,
    "americanfilament_pla_silkplaarcticwhite_1000_175_p": null
  },
  "color_hex": {
    "americanfilament_pla_americanfilamentsilkplaarcticwhite_1000_175_p": "e8e8e8",
    "americanfilament_pla_silkplaarcticwhite_1000_175_p": "FFFFFF"
  },
  "extruder_temp_range": {
    "americanfilament_pla_americanfilamentsilkplaarcticwhite_1000_175_p": [
      205,
      220
    ],
    "americanfilament_pla_silkplaarcticwhite_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "americanfilament_pla_americanfilamentsilkplaarcticwhite_1000_175_p": [
      45,
      60
    ],
    "americanfilament_pla_silkplaarcticwhite_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "americanfilament_pla_americanfilamentsilkplaarcticwhite_1000_175_p": "glossy",
    "americanfilament_pla_silkplaarcticwhite_1000_175_p": null
  },
  "codes": {
    "americanfilament_pla_americanfilamentsilkplaarcticwhite_1000_175_p": [
      "SILK_1KG_WHITE"
    ],
    "americanfilament_pla_silkplaarcticwhite_1000_175_p": null
  }
}
```

### AF007: dup-7103f6b821a485f066076775dd428f5ef290820e8c17b17147e78004a1a38a1e

Status: APPROVED; survivor `americanfilament_pla_silkplablue_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`americanfilament_pla_americanfilamentsilkplablue_1000_175_p`|`American Filament Silk PLA {color_name}`|`Blue`|{"source_file": "americanfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`americanfilament_pla_silkplablue_1000_175_p`|`Silk PLA {color_name}`|`Blue`|{"source_file": "americanfilament.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "americanfilament_pla_americanfilamentsilkplablue_1000_175_p": 220,
    "americanfilament_pla_silkplablue_1000_175_p": null
  },
  "color_hex": {
    "americanfilament_pla_americanfilamentsilkplablue_1000_175_p": "1565c0",
    "americanfilament_pla_silkplablue_1000_175_p": "0066D9"
  },
  "extruder_temp_range": {
    "americanfilament_pla_americanfilamentsilkplablue_1000_175_p": [
      205,
      220
    ],
    "americanfilament_pla_silkplablue_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "americanfilament_pla_americanfilamentsilkplablue_1000_175_p": [
      45,
      60
    ],
    "americanfilament_pla_silkplablue_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "americanfilament_pla_americanfilamentsilkplablue_1000_175_p": "glossy",
    "americanfilament_pla_silkplablue_1000_175_p": null
  },
  "codes": {
    "americanfilament_pla_americanfilamentsilkplablue_1000_175_p": [
      "SILK_1KG_BLUE"
    ],
    "americanfilament_pla_silkplablue_1000_175_p": null
  }
}
```

### AF008: dup-e950c9242e44da27033661ea97bb898c292173b5e5431cd90bd293bf2ceca1ef

Status: APPROVED; survivor `americanfilament_pla_silkplaemeraldgreen_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`americanfilament_pla_americanfilamentsilkplaemeraldgreen_1000_175_p`|`American Filament Silk PLA {color_name}`|`Emerald Green`|{"source_file": "americanfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`americanfilament_pla_silkplaemeraldgreen_1000_175_p`|`Silk PLA {color_name}`|`Emerald Green`|{"source_file": "americanfilament.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "americanfilament_pla_americanfilamentsilkplaemeraldgreen_1000_175_p": 220,
    "americanfilament_pla_silkplaemeraldgreen_1000_175_p": null
  },
  "color_hex": {
    "americanfilament_pla_americanfilamentsilkplaemeraldgreen_1000_175_p": "06de96",
    "americanfilament_pla_silkplaemeraldgreen_1000_175_p": "0CCF81"
  },
  "extruder_temp_range": {
    "americanfilament_pla_americanfilamentsilkplaemeraldgreen_1000_175_p": [
      205,
      220
    ],
    "americanfilament_pla_silkplaemeraldgreen_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "americanfilament_pla_americanfilamentsilkplaemeraldgreen_1000_175_p": [
      45,
      60
    ],
    "americanfilament_pla_silkplaemeraldgreen_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "americanfilament_pla_americanfilamentsilkplaemeraldgreen_1000_175_p": "glossy",
    "americanfilament_pla_silkplaemeraldgreen_1000_175_p": null
  },
  "codes": {
    "americanfilament_pla_americanfilamentsilkplaemeraldgreen_1000_175_p": [
      "SILK_1KG_EMERALD"
    ],
    "americanfilament_pla_silkplaemeraldgreen_1000_175_p": null
  }
}
```

### AF009: dup-d1c6131d3959c8d78393b68a48d47fc65af8dda46c5d6b8d97432e6f78d5e4d7

Status: APPROVED; survivor `americanfilament_pla_silkplagraphite_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`americanfilament_pla_americanfilamentsilkplagraphite_1000_175_p`|`American Filament Silk PLA {color_name}`|`Graphite`|{"source_file": "americanfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`americanfilament_pla_silkplagraphite_1000_175_p`|`Silk PLA {color_name}`|`Graphite`|{"source_file": "americanfilament.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "americanfilament_pla_americanfilamentsilkplagraphite_1000_175_p": 220,
    "americanfilament_pla_silkplagraphite_1000_175_p": null
  },
  "color_hex": {
    "americanfilament_pla_americanfilamentsilkplagraphite_1000_175_p": "4a4a4a",
    "americanfilament_pla_silkplagraphite_1000_175_p": "000000"
  },
  "extruder_temp_range": {
    "americanfilament_pla_americanfilamentsilkplagraphite_1000_175_p": [
      205,
      220
    ],
    "americanfilament_pla_silkplagraphite_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "americanfilament_pla_americanfilamentsilkplagraphite_1000_175_p": [
      45,
      60
    ],
    "americanfilament_pla_silkplagraphite_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "americanfilament_pla_americanfilamentsilkplagraphite_1000_175_p": "glossy",
    "americanfilament_pla_silkplagraphite_1000_175_p": null
  },
  "codes": {
    "americanfilament_pla_americanfilamentsilkplagraphite_1000_175_p": [
      "SILK_1KG_GRAPHITE"
    ],
    "americanfilament_pla_silkplagraphite_1000_175_p": null
  }
}
```

### AF010: dup-1c16be1d90c399f9c446debebfa636803ae325c1b79dd6a3c19874b051f572bb

Status: APPROVED; survivor `americanfilament_pla_silkplaneongreen_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`americanfilament_pla_americanfilamentsilkplaneongreen_1000_175_p`|`American Filament Silk PLA {color_name}`|`Neon Green`|{"source_file": "americanfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`americanfilament_pla_silkplaneongreen_1000_175_p`|`Silk PLA {color_name}`|`Neon Green`|{"source_file": "americanfilament.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "americanfilament_pla_americanfilamentsilkplaneongreen_1000_175_p": 220,
    "americanfilament_pla_silkplaneongreen_1000_175_p": null
  },
  "color_hex": {
    "americanfilament_pla_americanfilamentsilkplaneongreen_1000_175_p": "7edea2",
    "americanfilament_pla_silkplaneongreen_1000_175_p": "62E480"
  },
  "extruder_temp_range": {
    "americanfilament_pla_americanfilamentsilkplaneongreen_1000_175_p": [
      205,
      220
    ],
    "americanfilament_pla_silkplaneongreen_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "americanfilament_pla_americanfilamentsilkplaneongreen_1000_175_p": [
      45,
      60
    ],
    "americanfilament_pla_silkplaneongreen_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "americanfilament_pla_americanfilamentsilkplaneongreen_1000_175_p": "glossy",
    "americanfilament_pla_silkplaneongreen_1000_175_p": null
  },
  "codes": {
    "americanfilament_pla_americanfilamentsilkplaneongreen_1000_175_p": [
      "SILK_1KG_NGREEN"
    ],
    "americanfilament_pla_silkplaneongreen_1000_175_p": null
  }
}
```

### AF011: dup-024216fc43269e5b8c8a1bf6732fe855c090cf1d070ea7eb731a6866cbc844bf

Status: APPROVED; survivor `americanfilament_pla_silkplaneonorange_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`americanfilament_pla_americanfilamentsilkplaneonorange_1000_175_p`|`American Filament Silk PLA {color_name}`|`Neon Orange`|{"source_file": "americanfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`americanfilament_pla_silkplaneonorange_1000_175_p`|`Silk PLA {color_name}`|`Neon Orange`|{"source_file": "americanfilament.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "americanfilament_pla_americanfilamentsilkplaneonorange_1000_175_p": 220,
    "americanfilament_pla_silkplaneonorange_1000_175_p": null
  },
  "color_hex": {
    "americanfilament_pla_americanfilamentsilkplaneonorange_1000_175_p": "f6ba96",
    "americanfilament_pla_silkplaneonorange_1000_175_p": "F6A25C"
  },
  "extruder_temp_range": {
    "americanfilament_pla_americanfilamentsilkplaneonorange_1000_175_p": [
      205,
      220
    ],
    "americanfilament_pla_silkplaneonorange_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "americanfilament_pla_americanfilamentsilkplaneonorange_1000_175_p": [
      45,
      60
    ],
    "americanfilament_pla_silkplaneonorange_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "americanfilament_pla_americanfilamentsilkplaneonorange_1000_175_p": "glossy",
    "americanfilament_pla_silkplaneonorange_1000_175_p": null
  },
  "codes": {
    "americanfilament_pla_americanfilamentsilkplaneonorange_1000_175_p": [
      "SILK_1KG_NORANGE"
    ],
    "americanfilament_pla_silkplaneonorange_1000_175_p": null
  }
}
```

### AF012: dup-cd7be93f519dfde74e87630b8ce4b4358eddb7e4eb214af2c71928032bede526

Status: APPROVED; survivor `americanfilament_pla_silkplaneonpink_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`americanfilament_pla_americanfilamentsilkplaneonpink_1000_175_p`|`American Filament Silk PLA {color_name}`|`Neon Pink`|{"source_file": "americanfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`americanfilament_pla_silkplaneonpink_1000_175_p`|`Silk PLA {color_name}`|`Neon Pink`|{"source_file": "americanfilament.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "americanfilament_pla_americanfilamentsilkplaneonpink_1000_175_p": 220,
    "americanfilament_pla_silkplaneonpink_1000_175_p": null
  },
  "color_hex": {
    "americanfilament_pla_americanfilamentsilkplaneonpink_1000_175_p": "ff96ba",
    "americanfilament_pla_silkplaneonpink_1000_175_p": "F092B3"
  },
  "extruder_temp_range": {
    "americanfilament_pla_americanfilamentsilkplaneonpink_1000_175_p": [
      205,
      220
    ],
    "americanfilament_pla_silkplaneonpink_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "americanfilament_pla_americanfilamentsilkplaneonpink_1000_175_p": [
      45,
      60
    ],
    "americanfilament_pla_silkplaneonpink_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "americanfilament_pla_americanfilamentsilkplaneonpink_1000_175_p": "glossy",
    "americanfilament_pla_silkplaneonpink_1000_175_p": null
  },
  "codes": {
    "americanfilament_pla_americanfilamentsilkplaneonpink_1000_175_p": [
      "SILK_1KG_NPINK"
    ],
    "americanfilament_pla_silkplaneonpink_1000_175_p": null
  }
}
```

### AF013: dup-2d99c013ccb333def4c800c7ed5f5c35a3a4617687a9064ccb20a715aeb991ea

Status: APPROVED; survivor `americanfilament_pla_silkplapurple_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`americanfilament_pla_americanfilamentsilkplapurple_1000_175_p`|`American Filament Silk PLA {color_name}`|`Purple`|{"source_file": "americanfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`americanfilament_pla_silkplapurple_1000_175_p`|`Silk PLA {color_name}`|`Purple`|{"source_file": "americanfilament.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "americanfilament_pla_americanfilamentsilkplapurple_1000_175_p": 220,
    "americanfilament_pla_silkplapurple_1000_175_p": null
  },
  "color_hex": {
    "americanfilament_pla_americanfilamentsilkplapurple_1000_175_p": "ba72ba",
    "americanfilament_pla_silkplapurple_1000_175_p": "CE92CE"
  },
  "extruder_temp_range": {
    "americanfilament_pla_americanfilamentsilkplapurple_1000_175_p": [
      205,
      220
    ],
    "americanfilament_pla_silkplapurple_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "americanfilament_pla_americanfilamentsilkplapurple_1000_175_p": [
      45,
      60
    ],
    "americanfilament_pla_silkplapurple_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "americanfilament_pla_americanfilamentsilkplapurple_1000_175_p": "glossy",
    "americanfilament_pla_silkplapurple_1000_175_p": null
  },
  "codes": {
    "americanfilament_pla_americanfilamentsilkplapurple_1000_175_p": [
      "SILK_1KG_PURPLE"
    ],
    "americanfilament_pla_silkplapurple_1000_175_p": null
  }
}
```

### AF014: dup-ed1ca0a81bdf46ae86817477fded632c8a7438013d3464c08eaa1148a194298b

Status: APPROVED; survivor `americanfilament_pla_silkplared_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`americanfilament_pla_americanfilamentsilkplared_1000_175_p`|`American Filament Silk PLA {color_name}`|`Red`|{"source_file": "americanfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`americanfilament_pla_silkplared_1000_175_p`|`Silk PLA {color_name}`|`Red`|{"source_file": "americanfilament.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "americanfilament_pla_americanfilamentsilkplared_1000_175_p": 220,
    "americanfilament_pla_silkplared_1000_175_p": null
  },
  "color_hex": {
    "americanfilament_pla_americanfilamentsilkplared_1000_175_p": "de728a",
    "americanfilament_pla_silkplared_1000_175_p": "FC8397"
  },
  "extruder_temp_range": {
    "americanfilament_pla_americanfilamentsilkplared_1000_175_p": [
      205,
      220
    ],
    "americanfilament_pla_silkplared_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "americanfilament_pla_americanfilamentsilkplared_1000_175_p": [
      45,
      60
    ],
    "americanfilament_pla_silkplared_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "americanfilament_pla_americanfilamentsilkplared_1000_175_p": "glossy",
    "americanfilament_pla_silkplared_1000_175_p": null
  },
  "codes": {
    "americanfilament_pla_americanfilamentsilkplared_1000_175_p": [
      "SILK_1KG_RED"
    ],
    "americanfilament_pla_silkplared_1000_175_p": null
  }
}
```

### AF015: dup-3be1a4304b4c49c676bb81f9ff29128348f6af6345429ef838b03f09e97896e2

Status: APPROVED; survivor `americanfilament_pla_silkplarosegold_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`americanfilament_pla_americanfilamentsilkplarosegold_1000_175_p`|`American Filament Silk PLA {color_name}`|`Rose Gold`|{"source_file": "americanfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`americanfilament_pla_silkplarosegold_1000_175_p`|`Silk PLA {color_name}`|`Rose Gold`|{"source_file": "americanfilament.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "americanfilament_pla_americanfilamentsilkplarosegold_1000_175_p": 220,
    "americanfilament_pla_silkplarosegold_1000_175_p": null
  },
  "color_hex": {
    "americanfilament_pla_americanfilamentsilkplarosegold_1000_175_p": "c9877a",
    "americanfilament_pla_silkplarosegold_1000_175_p": "E69E7A"
  },
  "extruder_temp_range": {
    "americanfilament_pla_americanfilamentsilkplarosegold_1000_175_p": [
      205,
      220
    ],
    "americanfilament_pla_silkplarosegold_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "americanfilament_pla_americanfilamentsilkplarosegold_1000_175_p": [
      45,
      60
    ],
    "americanfilament_pla_silkplarosegold_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "americanfilament_pla_americanfilamentsilkplarosegold_1000_175_p": "glossy",
    "americanfilament_pla_silkplarosegold_1000_175_p": null
  },
  "codes": {
    "americanfilament_pla_americanfilamentsilkplarosegold_1000_175_p": [
      "SILK_1KG_ROSE"
    ],
    "americanfilament_pla_silkplarosegold_1000_175_p": null
  }
}
```

### AF016: dup-be0edf74d4598ff26524df051e0382ce577cac7fb1b79fb07368f19fdce79ba6

Status: APPROVED; survivor `americanfilament_pla_silkplateal_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`americanfilament_pla_americanfilamentsilkplateal_1000_175_p`|`American Filament Silk PLA {color_name}`|`Teal`|{"source_file": "americanfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`americanfilament_pla_silkplateal_1000_175_p`|`Silk PLA {color_name}`|`Teal`|{"source_file": "americanfilament.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "americanfilament_pla_americanfilamentsilkplateal_1000_175_p": 220,
    "americanfilament_pla_silkplateal_1000_175_p": null
  },
  "color_hex": {
    "americanfilament_pla_americanfilamentsilkplateal_1000_175_p": "2ad2d2",
    "americanfilament_pla_silkplateal_1000_175_p": "00B4BC"
  },
  "extruder_temp_range": {
    "americanfilament_pla_americanfilamentsilkplateal_1000_175_p": [
      205,
      220
    ],
    "americanfilament_pla_silkplateal_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "americanfilament_pla_americanfilamentsilkplateal_1000_175_p": [
      45,
      60
    ],
    "americanfilament_pla_silkplateal_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "americanfilament_pla_americanfilamentsilkplateal_1000_175_p": "glossy",
    "americanfilament_pla_silkplateal_1000_175_p": null
  },
  "codes": {
    "americanfilament_pla_americanfilamentsilkplateal_1000_175_p": [
      "SILK_1KG_TEAL"
    ],
    "americanfilament_pla_silkplateal_1000_175_p": null
  }
}
```

### AF017: dup-b79bf12547b0c3b8b528d294885ac5415e9ca151f0af86f34a02f77b243ffb10

Status: APPROVED; survivor `americanfilament_pla_silkplayellow_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`americanfilament_pla_americanfilamentsilkplayellow_1000_175_p`|`American Filament Silk PLA {color_name}`|`Yellow`|{"source_file": "americanfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`americanfilament_pla_silkplayellow_1000_175_p`|`Silk PLA {color_name}`|`Yellow`|{"source_file": "americanfilament.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "americanfilament_pla_americanfilamentsilkplayellow_1000_175_p": 220,
    "americanfilament_pla_silkplayellow_1000_175_p": null
  },
  "color_hex": {
    "americanfilament_pla_americanfilamentsilkplayellow_1000_175_p": "ffd700",
    "americanfilament_pla_silkplayellow_1000_175_p": "EFDC4C"
  },
  "extruder_temp_range": {
    "americanfilament_pla_americanfilamentsilkplayellow_1000_175_p": [
      205,
      220
    ],
    "americanfilament_pla_silkplayellow_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp_range": {
    "americanfilament_pla_americanfilamentsilkplayellow_1000_175_p": [
      45,
      60
    ],
    "americanfilament_pla_silkplayellow_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "americanfilament_pla_americanfilamentsilkplayellow_1000_175_p": "glossy",
    "americanfilament_pla_silkplayellow_1000_175_p": null
  },
  "codes": {
    "americanfilament_pla_americanfilamentsilkplayellow_1000_175_p": [
      "SILK_1KG_YELLOW"
    ],
    "americanfilament_pla_silkplayellow_1000_175_p": null
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "americanfilament_pla_silkplaneonorange_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          235
        ],
        "codes": [
          "SILK_1KG_NORANGE"
        ]
      },
      "source": "https://americanfilament.us/products/silky-arctic-white-1-75mm-pla-filament",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true,
      "field_sources": {
        "codes": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
      }
    },
    {
      "id": "americanfilament_pla_silkplaneongreen_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          235
        ],
        "codes": [
          "SILK_1KG_NGREEN"
        ]
      },
      "source": "https://americanfilament.us/products/silky-arctic-white-1-75mm-pla-filament",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true,
      "field_sources": {
        "codes": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
      }
    },
    {
      "id": "americanfilament_pla_silkplapurple_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          235
        ],
        "codes": [
          "SILK_1KG_PURPLE"
        ]
      },
      "source": "https://americanfilament.us/products/silky-arctic-white-1-75mm-pla-filament",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true,
      "field_sources": {
        "codes": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
      }
    },
    {
      "id": "americanfilament_pla_silkplarosegold_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          235
        ],
        "codes": [
          "SILK_1KG_ROSE"
        ]
      },
      "source": "https://americanfilament.us/products/silky-arctic-white-1-75mm-pla-filament",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true,
      "field_sources": {
        "codes": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
      }
    },
    {
      "id": "americanfilament_pla_silkplaamethystpurple_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          235
        ],
        "codes": [
          "SILK_1KG_AMETHYST"
        ]
      },
      "source": "https://americanfilament.us/products/silky-arctic-white-1-75mm-pla-filament",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true,
      "field_sources": {
        "codes": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
      }
    },
    {
      "id": "americanfilament_pla_silkplablue_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          235
        ],
        "codes": [
          "SILK_1KG_BLUE"
        ]
      },
      "source": "https://americanfilament.us/products/silky-arctic-white-1-75mm-pla-filament",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true,
      "field_sources": {
        "codes": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
      }
    },
    {
      "id": "americanfilament_pla_silkplayellow_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          235
        ],
        "codes": [
          "SILK_1KG_YELLOW"
        ]
      },
      "source": "https://americanfilament.us/products/silky-arctic-white-1-75mm-pla-filament",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true,
      "field_sources": {
        "codes": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
      }
    },
    {
      "id": "americanfilament_pla_silkplateal_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          235
        ],
        "codes": [
          "SILK_1KG_TEAL"
        ]
      },
      "source": "https://americanfilament.us/products/silky-arctic-white-1-75mm-pla-filament",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true,
      "field_sources": {
        "codes": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
      }
    },
    {
      "id": "americanfilament_pla_silkplaneonpink_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          235
        ],
        "codes": [
          "SILK_1KG_NPINK"
        ]
      },
      "source": "https://americanfilament.us/products/silky-arctic-white-1-75mm-pla-filament",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true,
      "field_sources": {
        "codes": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
      }
    },
    {
      "id": "americanfilament_pla_silkplagraphite_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          235
        ],
        "codes": [
          "SILK_1KG_GRAPHITE"
        ]
      },
      "source": "https://americanfilament.us/products/silky-arctic-white-1-75mm-pla-filament",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true,
      "field_sources": {
        "codes": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
      }
    },
    {
      "id": "americanfilament_pla_silkplaemeraldgreen_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          235
        ],
        "codes": [
          "SILK_1KG_EMERALD"
        ]
      },
      "source": "https://americanfilament.us/products/silky-arctic-white-1-75mm-pla-filament",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true,
      "field_sources": {
        "codes": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
      }
    },
    {
      "id": "americanfilament_pla_silkplared_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          235
        ],
        "codes": [
          "SILK_1KG_RED"
        ]
      },
      "source": "https://americanfilament.us/products/silky-arctic-white-1-75mm-pla-filament",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true,
      "field_sources": {
        "codes": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
      }
    },
    {
      "id": "americanfilament_pla_silkplaarcticwhite_1000_175_p",
      "values": {
        "extruder_temp_range": [
          220,
          235
        ],
        "codes": [
          "SILK_1KG_WHITE"
        ]
      },
      "source": "https://americanfilament.us/products/silky-arctic-white-1-75mm-pla-filament",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true,
      "field_sources": {
        "codes": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
      }
    }
  ],
  "transfers": [
    {
      "old_id": "americanfilament_pla_americanfilamentsilkplaamethystpurple_1000_175_p",
      "target_id": "americanfilament_pla_silkplaamethystpurple_1000_175_p",
      "field": "codes",
      "values": [
        "SILK_1KG_AMETHYST"
      ],
      "source": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
    },
    {
      "old_id": "americanfilament_pla_americanfilamentsilkplaarcticwhite_1000_175_p",
      "target_id": "americanfilament_pla_silkplaarcticwhite_1000_175_p",
      "field": "codes",
      "values": [
        "SILK_1KG_WHITE"
      ],
      "source": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
    },
    {
      "old_id": "americanfilament_pla_americanfilamentsilkplablue_1000_175_p",
      "target_id": "americanfilament_pla_silkplablue_1000_175_p",
      "field": "codes",
      "values": [
        "SILK_1KG_BLUE"
      ],
      "source": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
    },
    {
      "old_id": "americanfilament_pla_americanfilamentsilkplaemeraldgreen_1000_175_p",
      "target_id": "americanfilament_pla_silkplaemeraldgreen_1000_175_p",
      "field": "codes",
      "values": [
        "SILK_1KG_EMERALD"
      ],
      "source": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
    },
    {
      "old_id": "americanfilament_pla_americanfilamentsilkplagraphite_1000_175_p",
      "target_id": "americanfilament_pla_silkplagraphite_1000_175_p",
      "field": "codes",
      "values": [
        "SILK_1KG_GRAPHITE"
      ],
      "source": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
    },
    {
      "old_id": "americanfilament_pla_americanfilamentsilkplaneongreen_1000_175_p",
      "target_id": "americanfilament_pla_silkplaneongreen_1000_175_p",
      "field": "codes",
      "values": [
        "SILK_1KG_NGREEN"
      ],
      "source": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
    },
    {
      "old_id": "americanfilament_pla_americanfilamentsilkplaneonorange_1000_175_p",
      "target_id": "americanfilament_pla_silkplaneonorange_1000_175_p",
      "field": "codes",
      "values": [
        "SILK_1KG_NORANGE"
      ],
      "source": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
    },
    {
      "old_id": "americanfilament_pla_americanfilamentsilkplaneonpink_1000_175_p",
      "target_id": "americanfilament_pla_silkplaneonpink_1000_175_p",
      "field": "codes",
      "values": [
        "SILK_1KG_NPINK"
      ],
      "source": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
    },
    {
      "old_id": "americanfilament_pla_americanfilamentsilkplapurple_1000_175_p",
      "target_id": "americanfilament_pla_silkplapurple_1000_175_p",
      "field": "codes",
      "values": [
        "SILK_1KG_PURPLE"
      ],
      "source": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
    },
    {
      "old_id": "americanfilament_pla_americanfilamentsilkplared_1000_175_p",
      "target_id": "americanfilament_pla_silkplared_1000_175_p",
      "field": "codes",
      "values": [
        "SILK_1KG_RED"
      ],
      "source": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
    },
    {
      "old_id": "americanfilament_pla_americanfilamentsilkplarosegold_1000_175_p",
      "target_id": "americanfilament_pla_silkplarosegold_1000_175_p",
      "field": "codes",
      "values": [
        "SILK_1KG_ROSE"
      ],
      "source": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
    },
    {
      "old_id": "americanfilament_pla_americanfilamentsilkplateal_1000_175_p",
      "target_id": "americanfilament_pla_silkplateal_1000_175_p",
      "field": "codes",
      "values": [
        "SILK_1KG_TEAL"
      ],
      "source": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
    },
    {
      "old_id": "americanfilament_pla_americanfilamentsilkplayellow_1000_175_p",
      "target_id": "americanfilament_pla_silkplayellow_1000_175_p",
      "field": "codes",
      "values": [
        "SILK_1KG_YELLOW"
      ],
      "source": "bd94f1d0a6c3fab56b1d50636522ab6c427016c4"
    }
  ]
}
```

## Preserved out-of-scope IDs

- `americanfilament_pla+_americanfilamentpla+americanblue_1000_175_p` — American Filament PLA+ American Blue
- `americanfilament_pla+_americanfilamentpla+americanred_1000_175_p` — American Filament PLA+ American Red
- `americanfilament_pla+_americanfilamentpla+amethystpurple_1000_175_p` — American Filament PLA+ Amethyst Purple
- `americanfilament_pla+_americanfilamentpla+armygreen_1000_175_p` — American Filament PLA+ Army Green
- `americanfilament_pla+_americanfilamentpla+bonewhite_1000_175_p` — American Filament PLA+ Bone White
- `americanfilament_pla+_americanfilamentpla+burntorange_1000_175_p` — American Filament PLA+ Burnt Orange
- `americanfilament_pla+_americanfilamentpla+chocolatebrown_1000_175_p` — American Filament PLA+ Chocolate Brown
- `americanfilament_pla+_americanfilamentpla+coyotebrown_1000_175_p` — American Filament PLA+ Coyote Brown
- `americanfilament_pla+_americanfilamentpla+coyotetan_1000_175_p` — American Filament PLA+ Coyote Tan
- `americanfilament_pla+_americanfilamentpla+dandelionyellow_1000_175_p` — American Filament PLA+ Dandelion Yellow
- `americanfilament_pla+_americanfilamentpla+darkgreen_1000_175_p` — American Filament PLA+ Dark Green
- `americanfilament_pla+_americanfilamentpla+deserttan_1000_175_p` — American Filament PLA+ Desert Tan
- `americanfilament_pla+_americanfilamentpla+forestgreen_1000_175_p` — American Filament PLA+ Forest Green
- `americanfilament_pla+_americanfilamentpla+gunmetalgray_1000_175_p` — American Filament PLA+ Gunmetal Gray
- `americanfilament_pla+_americanfilamentpla+honeygold_1000_175_p` — American Filament PLA+ Honey Gold
- `americanfilament_pla+_americanfilamentpla+icewhite_1000_175_p` — American Filament PLA+ Ice White
- `americanfilament_pla+_americanfilamentpla+icyblue_1000_175_p` — American Filament PLA+ Icy Blue
- `americanfilament_pla+_americanfilamentpla+ivorywhite_1000_175_p` — American Filament PLA+ Ivory White
- `americanfilament_pla+_americanfilamentpla+matteblack_1000_175_p` — American Filament PLA+ Matte Black
- `americanfilament_pla+_americanfilamentpla+neongreen_1000_175_p` — American Filament PLA+ Neon Green
- `americanfilament_pla+_americanfilamentpla+neonorange_1000_175_p` — American Filament PLA+ Neon Orange
- `americanfilament_pla+_americanfilamentpla+neonpink_1000_175_p` — American Filament PLA+ Neon Pink
- `americanfilament_pla+_americanfilamentpla+primergray_1000_175_p` — American Filament PLA+ Primer Gray
- `americanfilament_pla+_americanfilamentpla+purple_1000_175_p` — American Filament PLA+ Purple
- `americanfilament_pla+_americanfilamentpla+skyblue_1000_175_p` — American Filament PLA+ Sky Blue
- `americanfilament_pla+_americanfilamentpla+teal_1000_175_p` — American Filament PLA+ Teal
- `americanfilament_pla+_americanfilamenttoughpropla+americanred_1000_175_p` — American Filament Tough Pro PLA+ American Red
- `americanfilament_pla+_americanfilamenttoughpropla+armygreen_1000_175_p` — American Filament Tough Pro PLA+ Army Green
- `americanfilament_pla+_americanfilamenttoughpropla+coyotebrown_1000_175_p` — American Filament Tough Pro PLA+ Coyote Brown
- `americanfilament_pla+_americanfilamenttoughpropla+gunmetalgray_1000_175_p` — American Filament Tough Pro PLA+ Gunmetal Gray
- `americanfilament_pla+_americanfilamenttoughpropla+onyxblack_1000_175_p` — American Filament Tough Pro PLA+ Onyx Black
- `americanfilament_pla+_americanfilamenttoughpropla+safetyorange_1000_175_p` — American Filament Tough Pro PLA+ Safety Orange
- `americanfilament_pla+_americanfilamentregenerativepla+americanblue_1000_175_p` — American Filament Regenerative PLA+ American Blue
- `americanfilament_pla+_americanfilamentregenerativepla+americanred_1000_175_p` — American Filament Regenerative PLA+ American Red
- `americanfilament_pla+_americanfilamentregenerativepla+armygreen_1000_175_p` — American Filament Regenerative PLA+ Army Green
- `americanfilament_pla+_americanfilamentregenerativepla+burntorange_1000_175_p` — American Filament Regenerative PLA+ Burnt Orange
- `americanfilament_pla+_americanfilamentregenerativepla+coyotetan_1000_175_p` — American Filament Regenerative PLA+ Coyote Tan
- `americanfilament_pla+_americanfilamentregenerativepla+forestgreen_1000_175_p` — American Filament Regenerative PLA+ Forest Green
- `americanfilament_pla+_americanfilamentregenerativepla+gunmetalgray_1000_175_p` — American Filament Regenerative PLA+ Gunmetal Gray
- `americanfilament_pla+_americanfilamentregenerativepla+icewhite_1000_175_p` — American Filament Regenerative PLA+ Ice White
- `americanfilament_pla+_americanfilamentregenerativepla+matteblack_1000_175_p` — American Filament Regenerative PLA+ Matte Black
- `americanfilament_pla+_americanfilamentregenerativepla+neonpink_1000_175_p` — American Filament Regenerative PLA+ Neon Pink
- `americanfilament_pctg_americanfilamentpctgcamobrown_1000_175_p` — American Filament PCTG Camo Brown
- `americanfilament_pctg_americanfilamentpctgconstructionorange_1000_175_p` — American Filament PCTG Construction Orange
- `americanfilament_pctg_americanfilamentpctgfireenginered_1000_175_p` — American Filament PCTG Fire Engine Red
- `americanfilament_pctg_americanfilamentpctghi-visyellow_1000_175_p` — American Filament PCTG Hi-Vis Yellow
- `americanfilament_pctg_americanfilamentpctgpoliceblue_1000_175_p` — American Filament PCTG Police Blue
- `americanfilament_pctg_americanfilamentpctgsafetyyellow_1000_175_p` — American Filament PCTG Safety Yellow
- `americanfilament_pctg_americanfilamentpctgtransparentjadegreen_1000_175_p` — American Filament PCTG Transparent Jade Green
- `americanfilament_pctg_americanfilamentpctgtransparentroyalpurple_1000_175_p` — American Filament PCTG Transparent Royal Purple
- `americanfilament_pctg_americanfilamentpctgtransparentrubyred_1000_175_p` — American Filament PCTG Transparent Ruby Red
- `americanfilament_pctg_americanfilamentpctgtransparentsapphireblue_1000_175_p` — American Filament PCTG Transparent Sapphire Blue
- `americanfilament_pctg_americanfilamentpctgtransparentturnsignalorange_1000_175_p` — American Filament PCTG Transparent Turn Signal Orange
- `americanfilament_pctg_americanfilamentpctgturquoise_1000_175_p` — American Filament PCTG Turquoise
- `americanfilament_pctg_americanfilamentpctgarmygreen_4000_175_p` — American Filament PCTG Army Green
- `americanfilament_pctg_americanfilamentpctgblizzardwhite_4000_175_p` — American Filament PCTG Blizzard White
- `americanfilament_pctg_americanfilamentpctgcamobrown_4000_175_p` — American Filament PCTG Camo Brown
- `americanfilament_pctg_americanfilamentpctgconstructionorange_4000_175_p` — American Filament PCTG Construction Orange
- `americanfilament_pctg_americanfilamentpctgfireenginered_4000_175_p` — American Filament PCTG Fire Engine Red
- `americanfilament_pctg_americanfilamentpctggunmetalgray_4000_175_p` — American Filament PCTG Gunmetal Gray
- `americanfilament_pctg_americanfilamentpctghi-visyellow_4000_175_p` — American Filament PCTG Hi-Vis Yellow
- `americanfilament_pctg_americanfilamentpctgobsidianblack_4000_175_p` — American Filament PCTG Obsidian Black
- `americanfilament_pctg_americanfilamentpctgpoliceblue_4000_175_p` — American Filament PCTG Police Blue
- `americanfilament_pctg_americanfilamentpctgsafetyyellow_4000_175_p` — American Filament PCTG Safety Yellow
- `americanfilament_pctg_americanfilamentpctgtransparentjadegreen_4000_175_p` — American Filament PCTG Transparent Jade Green
- `americanfilament_pctg_americanfilamentpctgtransparentroyalpurple_4000_175_p` — American Filament PCTG Transparent Royal Purple
- `americanfilament_pctg_americanfilamentpctgtransparentrubyred_4000_175_p` — American Filament PCTG Transparent Ruby Red
- `americanfilament_pctg_americanfilamentpctgtransparentsapphireblue_4000_175_p` — American Filament PCTG Transparent Sapphire Blue
- `americanfilament_pctg_americanfilamentpctgtransparentturnsignalorange_4000_175_p` — American Filament PCTG Transparent Turn Signal Orange
- `americanfilament_pctg_americanfilamentpctgturquoise_4000_175_p` — American Filament PCTG Turquoise
- `americanfilament_pla_americanfilamentlithophaneplaclassiclithophanewhite_1000_175_p` — American Filament Lithophane PLA Classic Lithophane White
- `americanfilament_pla_americanfilamentlithophaneplacoollithophanegray_1000_175_p` — American Filament Lithophane PLA Cool Lithophane Gray
- `americanfilament_pla_americanfilamentlithophaneplacrisplithophanegray_1000_175_p` — American Filament Lithophane PLA Crisp Lithophane Gray
- `americanfilament_pla_americanfilamentlithophaneplasepialithophane_1000_175_p` — American Filament Lithophane PLA Sepia Lithophane
- `americanfilament_pla_americanfilamentlithophaneplawarmlithophanewhite_1000_175_p` — American Filament Lithophane PLA Warm Lithophane White
- `americanfilament_pla+_americanfilamentcmykpla+cyan_1000_175_p` — American Filament CMYK PLA+ Cyan
- `americanfilament_pla+_americanfilamentcmykpla+magenta_1000_175_p` — American Filament CMYK PLA+ Magenta
- `americanfilament_pla+_americanfilamentcmykpla+yellow_1000_175_p` — American Filament CMYK PLA+ Yellow
- `americanfilament_pla_matteplablack_1000_175_p` — Matte PLA Black
- `americanfilament_pla_plaamericanblue_1000_175_p` — PLA American Blue
- `americanfilament_pla_plaamericanred_1000_175_p` — PLA American Red
- `americanfilament_pla_plaamethystpurple_1000_175_p` — PLA Amethyst Purple
- `americanfilament_pla_plaarmygreen_1000_175_p` — PLA Army Green
- `americanfilament_pla_plachocolatebrown_1000_175_p` — PLA Chocolate Brown
- `americanfilament_pla_placlassiclithophanewhite_1000_175_p` — PLA Classic Lithophane White
- `americanfilament_pla_placoollithophanegray_1000_175_p` — PLA Cool Lithophane Gray
- `americanfilament_pla_placoyotebrown_1000_175_p` — PLA Coyote Brown
- `americanfilament_pla_placoyotetan_1000_175_p` — PLA Coyote Tan
- `americanfilament_pla_placrisplithophanegray_1000_175_p` — PLA Crisp Lithophane Gray
- `americanfilament_pla_placyan_1000_175_p` — PLA Cyan
- `americanfilament_pla_pladandelionyellow_1000_175_p` — PLA Dandelion Yellow
- `americanfilament_pla_pladarkgreen_1000_175_p` — PLA Dark Green
- `americanfilament_pla_pladeserttanfde_1000_175_p` — PLA Desert Tan FDE
- `americanfilament_pla_plaforestgreen_1000_175_p` — PLA Forest Green
- `americanfilament_pla_plagunmetalgray_1000_175_p` — PLA Gunmetal Gray
- `americanfilament_pla_plahoneygold_1000_175_p` — PLA Honey Gold
- `americanfilament_pla_plaicewhite_1000_175_p` — PLA Ice White
- `americanfilament_pla_plaicyblue_1000_175_p` — PLA Icy Blue
- `americanfilament_pla_plaivorywhite_1000_175_p` — PLA Ivory White
- `americanfilament_pla_plamagenta_1000_175_p` — PLA Magenta
- `americanfilament_pla_planeongreen_1000_175_p` — PLA Neon Green
- `americanfilament_pla_planeonorange_1000_175_p` — PLA Neon Orange
- `americanfilament_pla_planeonpink_1000_175_p` — PLA Neon Pink
- `americanfilament_pla_plaonyxblack_1000_175_p` — PLA Onyx Black
- `americanfilament_pla_plaoutdoorgreen_1000_175_p` — PLA Outdoor Green
- `americanfilament_pla_plaprimergray_1000_175_p` — PLA Primer Gray
- `americanfilament_pla_plapurple_1000_175_p` — PLA Purple
- `americanfilament_pla_plasepialithophane_1000_175_p` — PLA Sepia Lithophane
- `americanfilament_pla_plaskyblue_1000_175_p` — PLA Sky Blue
- `americanfilament_pla_plateal_1000_175_p` — PLA Teal
- `americanfilament_pla_plawarmlithophanewhite_1000_175_p` — PLA Warm Lithophane White
- `americanfilament_pla_playellow_1000_175_p` — PLA Yellow
