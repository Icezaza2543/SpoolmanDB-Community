# conjure duplicate migration review

Base `e4e8923ef7407b9f9fd923bee237f67d378cbc58`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `7aa3a6dfc46d02daac3bd3bcd31ed496e019288f6fcc8f3a18139cc68b866af4`.

## Authorization and result

{"groups": 1, "approved_groups": 0, "retired": 0, "deferred": 1, "hard_stops": 0, "before_count": 51702, "after_count": 51702, "brand_before": 32, "brand_after": 32, "registry_before": 1732, "registry_after": 1732, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

One PLA Silk/DualBlackRed versusSilkDual/BlackRed strict decomposition mismatch; defer. No invented qualifier binding, no packaging/tare/metadata edits.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. Future reviewed retirements would not redirect external catalog lookups automatically.

## Current first-party evidence

- {"url": "https://www.chitusystems.com/products/conjure-silk-dual-color-pla-filament", "note": "BlackRed1/2kg options; does not resolve source line/color decomposition; no verified density or printing table."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### CJ001: dup-8b57502205f1098c2b42cfc16287a836f54b49b8278d3dfe3d9f75be12a0ee48

Status: DEFERRED; survivor `conjure_pla_silkdualblackred_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`conjure_pla_plasilkdualblackred_1000_175_p`|`PLA Silk {color_name}`|`Dual Black Red`|{"source_file": "conjure.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 1, "compiled_records": 1} / False|
|`conjure_pla_silkdualblackred_1000_175_p`|`Silk Dual {color_name}`|`Black Red`|{"source_file": "conjure.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `conjure_pla_chameleonburnttitaniumgreen_1000_175_p` — Chameleon Burnt Titanium Green
- `conjure_pla_chameleonpurpleblue_1000_175_p` — Chameleon Purple Blue
- `conjure_pla_glowrainbow_1000_175_p` — Glow Rainbow
- `conjure_pla_glowrainbow2_1000_175_p` — Glow Rainbow 2
- `conjure_pla_glowrainbowtoglowmulticolor_1000_175_p` — Glow RAINBOW TO GLOW MULTICOLOR
- `conjure_pla_marblewhite_1000_175_p` — Marble White
- `conjure_petg_petgrainbow_1000_175_p` — PETG Rainbow
- `conjure_pla_plamatterainbow_1000_175_p` — PLA Matte Rainbow
- `conjure_pla+_pla+green_1000_175_p` — PLA+ Green
- `conjure_pla+_pla+grey_1000_175_p` — PLA+ Grey
- `conjure_pla+_pla+white_1000_175_p` — PLA+ White
- `conjure_pla_rainbowrainbow_1000_175_p` — Rainbow Rainbow
- `conjure_pla_silkdualblack/darkgreen_1000_175_p` — Silk Dual Black / Dark Green
- `conjure_pla_silkdualblue/red_1000_175_p` — Silk Dual Blue / Red
- `conjure_pla_silkdualdualblackpurple_1000_175_p` — Silk Dual Dual Black Purple
- `conjure_pla_silkdualdualbluegreen_1000_175_p` — Silk Dual Dual Blue Green
- `conjure_pla_silkdualdualredgold_1000_175_p` — Silk Dual Dual Red Gold
- `conjure_pla_silkdualgold/black_1000_175_p` — Silk Dual Gold / Black
- `conjure_pla+_silkdualhotpink/blue_1000_175_p` — Silk Dual hotpink/blue
- `conjure_pla_silkrainbowno.1_1000_175_p` — Silk Rainbow No. 1
- `conjure_pla_silktripleblackpurpleblue_1000_175_p` — Silk Triple Black Purple Blue
- `conjure_pla_silktriplegreen/gold/orange_1000_175_p` — Silk Triple Green/Gold/Orange
- `conjure_pla_silktriplepurple-orange-blue_1000_175_p` — Silk Triple Purple-Orange-Blue
- `conjure_pla_silktripleredbluegreentri-color_1000_175_p` — Silk Triple Red Blue Green Tri-Color
- `conjure_pla_silktripleredyellowblue_1000_175_p` — Silk Triple Red Yellow Blue
- `conjure_pla_silktriplered/gold/blue_1000_175_p` — Silk Triple Red/Gold/Blue
- `conjure_pla_silktriplered/gold/purple_1000_175_p` — Silk Triple Red/Gold/Purple
- `conjure_pla_woodrose_1000_175_p` — Wood Rose
- `conjure_pla_woodwalnut_1000_175_p` — Wood Walnut
- `conjure_pla_woodwhiteoak_1000_175_p` — Wood White Oak
