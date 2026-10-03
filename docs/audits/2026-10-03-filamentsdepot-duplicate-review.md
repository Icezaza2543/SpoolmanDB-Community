# filamentsdepot duplicate migration review

Base `91f2f515d4f1c723e5ebc0b5ca146b2f61f8a9bd`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `7aa3a6dfc46d02daac3bd3bcd31ed496e019288f6fcc8f3a18139cc68b866af4`.

## Authorization and result

{"groups": 1, "approved_groups": 0, "retired": 0, "deferred": 1, "hard_stops": 0, "before_count": 51702, "after_count": 51702, "brand_before": 20, "brand_after": 20, "registry_before": 1732, "registry_after": 1732, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

StoneGray/Grey visibly differing HEXc9bba0/5c5e61 cannot be bound sameSKU; defer. StandardGray page is not proof for Stone. Both records remain unchanged.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. Future reviewed retirements would not redirect external catalog lookups automatically.

## Current first-party evidence

- {"url": "https://www.filamentsdepot.com/products/filaments-depot-gray-petg", "density": "1.23–1.27", "nozzle": [235, 250], "bed": [80, 90], "note": "StandardGray, not proven StoneGray identity."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### FD001: dup-16506851842feae0bb209ddb6736636a144ea00105cb6cd27b8e75e137c475e1

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filamentsdepot_petg_petgstonegray_1000_175_p`|`PETG {color_name}`|`Stone Gray`|{"source_file": "filamentsdepot.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|
|`filamentsdepot_petg_petgstonegrey_1000_175_p`|`PETG {color_name}`|`Stone Grey`|{"source_file": "filamentsdepot.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filamentsdepot_petg_petgstonegray_1000_175_p": "c9bba0",
    "filamentsdepot_petg_petgstonegrey_1000_175_p": "5c5e61"
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

- `filamentsdepot_pla_galaxyburnttitanium_1000_175_p` — Galaxy Burnt Titanium
- `filamentsdepot_pla_gradientcamouflage_1000_175_p` — Gradient Camouflage
- `filamentsdepot_pctg_pctgclear_1000_175_p` — PCTG Clear
- `filamentsdepot_pctg_pctgwhite_1000_175_p` — PCTG White
- `filamentsdepot_petg_petgalmond_1000_175_p` — PETG Almond
- `filamentsdepot_petg_petgblack_1000_175_p` — PETG Black
- `filamentsdepot_petg_petgcharcoal_1000_175_p` — PETG Charcoal
- `filamentsdepot_petg_petggray_1000_175_p` — PETG Gray
- `filamentsdepot_petg_petgteal_1000_175_p` — PETG Teal
- `filamentsdepot_petg+plus_petg+pluswhite_1000_175_p` — PETG+PLUS White
- `filamentsdepot_pla_plamysterywhite_1000_175_p` — PLA Mystery White
- `filamentsdepot_pla_planatural_1000_175_p` — PLA Natural
- `filamentsdepot_pla_recycledgrey/black(inconsistent)_1000_175_p` — Recycled Grey/Black (inconsistent)
- `filamentsdepot_petg_recycledgrey/black(inconsistent)_1000_175_p` — Recycled Grey/Black (inconsistent)
- `filamentsdepot_pla_silkdualflame(gold-red)_1000_175_p` — Silk Dual Flame (Gold-Red)
- `filamentsdepot_pla_toughgrey_1000_175_p` — Tough Grey
- `filamentsdepot_pla_toughyellow_1000_175_p` — Tough Yellow
- `filamentsdepot_petg_toughwhite_1000_175_p` — Tough White
