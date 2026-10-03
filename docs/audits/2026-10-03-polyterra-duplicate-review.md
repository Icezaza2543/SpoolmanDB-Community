# polyterra duplicate migration review

Base `eaaa485c71e500dfa5bec68b6fc4d31aa1f05d6e`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `7aa3a6dfc46d02daac3bd3bcd31ed496e019288f6fcc8f3a18139cc68b866af4`.

## Authorization and result

{"groups": 1, "approved_groups": 1, "retired": 1, "deferred": 0, "hard_stops": 0, "before_count": 51702, "after_count": 51701, "brand_before": 33, "brand_after": 32, "registry_before": 1732, "registry_after": 1733, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

OneRule2 strictSapphireBlue duplicate, survivorPLA family. Legacy density1.24/bed25-only looksPLA-default-like. Reopened exact current first-party page: current CA04038 and legacy PM70828 are simultaneously sold as separate variant selectors, despite formerlyPolyTerra branding. Page1.37 and unavailable exactoldPolyTerra sheet indexed1.31 are not unambiguously bound to this legacy record. Keep survivor printing unresolved; current-line printing evidence needs no lot binding, but separate current product/SKU choices cannot be conflated. No guessed formula, identifier transfer, cross-brand rename or packaging/tare change.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://eu-wholesale.polymaker.com/products/panchroma-matte-pla", "note": "Current page says formerlyPolyTerraPLA but simultaneously lists1.75mm/1kg/SapphireBlue as CA04038 and a separate1.75mm(PolyTerra)/1kg/SapphireBlue as PM70828. The current page density1.37 is not explicitly SKU-bound to the legacy PM variant; no blind formula substitution."}
- {"url": "https://polymaker.com/wp-content/uploads/lana-downloads/PolyTerra-PLA_TDS_EN_V5.4-1.pdf", "note": "Officialsearchindexed exactoldPolyTerraPLA sheet gives1.31, but document fetchfailed; conflicts with current successor1.37. No density substitution."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`polyterra_pla_polyterrasapphireblue_1000_175_c`|`polyterra_pla_plasapphireblue_1000_175_c`|`polyterra.json::PolyTerra::Polyterra {color_name}::Polyterra Sapphire Blue::PLA::1000::1.75::cardboard::False`|

## Per-group decisions and unresolved metadata

### PT001: dup-643e41a9f3be4cea39248970f96718a463a653fad2b3525a3015bb5633a5a895

Status: APPROVED; survivor `polyterra_pla_plasapphireblue_1000_175_c`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`polyterra_pla_plasapphireblue_1000_175_c`|`PLA {color_name}`|`Sapphire Blue`|{"source_file": "polyterra.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 17, "compiled_records": 17} / False|
|`polyterra_pla_polyterrasapphireblue_1000_175_c`|`Polyterra {color_name}`|`Sapphire Blue`|{"source_file": "polyterra.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "polyterra_pla_plasapphireblue_1000_175_c": "2191db",
    "polyterra_pla_polyterrasapphireblue_1000_175_c": "808080"
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

- `polyterra_pla_multicolormulticolorfoggyorange(grey-orange)_1000_175_c` — Multicolor Multicolor Foggy Orange (Grey-Orange)
- `polyterra_pla_plamattearcticteal_1000_175_c` — PLA Matte Arctic Teal
- `polyterra_pla_plamattearticteal_1000_175_c` — PLA Matte Artic Teal
- `polyterra_pla_plamattecharcoalblack_1000_175_c` — PLA Matte Charcoal black
- `polyterra_pla_plamattecharcoalblack(noircharbon)_1000_175_c` — PLA Matte Charcoal Black (noir charbon)
- `polyterra_pla_plamatteforestgreen_1000_175_c` — PLA Matte Forest Green
- `polyterra_pla_plamattelavenderpurple_1000_175_c` — PLA Matte Lavender Purple
- `polyterra_pla_plamattemutedwhite_1000_175_c` — PLA Matte Muted White
- `polyterra_pla_plamattepastelice_1000_175_c` — PLA Matte Pastel Ice
- `polyterra_pla_plamattesavannahyellow_1000_175_c` — PLA Matte Savannah Yellow
- `polyterra_pla_plamattesunriseorange_1000_175_c` — PLA Matte Sunrise Orange
- `polyterra_pla_plamattewhite_1000_175_c` — PLA Matte white
- `polyterra_pla_plasilksilver_1000_175_c` — PLA Silk Silver
- `polyterra_pla_plaarmybeige_1000_175_c` — PLA Army Beige
- `polyterra_pla_plaarmybrown_1000_175_c` — PLA Army Brown
- `polyterra_pla_plaarmydarkgreen_1000_175_c` — PLA Army Dark Green
- `polyterra_pla_placharcoalblack_1000_175_c` — PLA Charcoal Black
- `polyterra_pla_placottonwhite_1000_175_c` — PLA Cotton white
- `polyterra_pla_plaearthbrown_1000_175_c` — PLA Earth Brown
- `polyterra_pla_plaforestgreen_1000_175_c` — PLA Forest Green
- `polyterra_pla_plalavared_1000_175_c` — PLA Lava Red
- `polyterra_pla_plamarbleslategrey_1000_175_c` — PLA Marble Slate Grey
- `polyterra_pla_plamarblewhite_1000_175_c` — PLA Marble White
- `polyterra_pla_plamutedblue_1000_175_c` — PLA Muted Blue
- `polyterra_pla_plamutedgreen_1000_175_c` — PLA Muted Green
- `polyterra_pla_plamutedpurple_1000_175_c` — PLA Muted Purple
- `polyterra_pla_plapeanut_1000_175_c` — PLA Peanut
- `polyterra_pla_plasakurapink_1000_175_c` — PLA Sakura Pink
- `polyterra_pla_plawoodbrown_1000_175_c` — PLA Wood Brown
- `polyterra_pla_polyterrafossilgray_1000_175_c` — Polyterra Fossil Gray
- `polyterra_pla_woodwoodbrown_1000_175_c` — Wood Wood Brown
