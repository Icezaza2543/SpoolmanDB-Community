# l3d duplicate migration review

Base `8078820142cbab5165eac2a3457020c807e57593`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `7aa3a6dfc46d02daac3bd3bcd31ed496e019288f6fcc8f3a18139cc68b866af4`.

## Authorization and result

{"groups": 1, "approved_groups": 0, "retired": 0, "deferred": 1, "hard_stops": 0, "before_count": 51702, "after_count": 51702, "brand_before": 62, "brand_after": 62, "registry_before": 1732, "registry_after": 1732, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

One3kgGray/Grey tie HEX808080/A3A3A3 and unbound sameSKU; preserve source code/EAN exact placement. No transfer to current1kg products; both historicalrecords unchanged.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. Future reviewed retirements would not redirect external catalog lookups automatically.

## Current first-party evidence

- {"url": "https://shop.lab3d.dk/collections/lab3d-filament-petg", "note": "CurrentlyGrey1kg, not proof for3kgPETG-GREY-03/EAN5744006030696."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### LD001: dup-377dfee5243440f2c3d930ca9e3d9e5ead5a2d4fabfada1965a1d1eb79a9c284

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`l3d_petg_petggray_3000_175_c`|`PETG {color_name}`|`Gray`|{"source_file": "l3d.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`l3d_petg_petggrey_3000_175_c`|`PETG {color_name}`|`Grey`|{"source_file": "l3d.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "l3d_petg_petggray_3000_175_c": "808080",
    "l3d_petg_petggrey_3000_175_c": "A3A3A3"
  },
  "codes": {
    "l3d_petg_petggray_3000_175_c": [
      "PETG-GREY-03"
    ],
    "l3d_petg_petggrey_3000_175_c": null
  },
  "eans": {
    "l3d_petg_petggray_3000_175_c": [
      "5744006030696"
    ],
    "l3d_petg_petggrey_3000_175_c": null
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

- `l3d_pla_glitterplablack_1000_175_c` — Glitter PLA Black
- `l3d_pla_glitterplasilver_1000_175_c` — Glitter PLA Silver
- `l3d_petg_mattepetgblack_3000_175_c` — Matte PETG Black
- `l3d_pla_matteplablack_1000_175_c` — Matte PLA Black
- `l3d_petg_petgblack_1000_175_c` — PETG Black
- `l3d_petg_petgdarkgreen_1000_175_c` — PETG Dark Green
- `l3d_petg_petggray_1000_175_c` — PETG Gray
- `l3d_petg_petgorange_1000_175_c` — PETG Orange
- `l3d_petg_petgred_1000_175_c` — PETG Red
- `l3d_petg_petgwhite_1000_175_c` — PETG White
- `l3d_petg_petgyellow_1000_175_c` — PETG Yellow
- `l3d_petg_petgblack_3000_175_c` — PETG Black
- `l3d_petg_petgwhite_3000_175_c` — PETG White
- `l3d_petg_petgmattblack_3000_175_c` — PETG Matt Black
- `l3d_petg_petgmattwhite_3000_175_c` — PETG Matt White
- `l3d_petg_petgorange_3000_175_c` — PETG Orange
- `l3d_petg_petgyellow_3000_175_c` — PETG Yellow
- `l3d_pla_plablack_1000_175_c` — PLA Black
- `l3d_pla_plablue_1000_175_c` — PLA Blue
- `l3d_pla_plabrown_1000_175_c` — PLA Brown
- `l3d_pla_placyan_1000_175_c` — PLA Cyan
- `l3d_pla_plagold_1000_175_c` — PLA Gold
- `l3d_pla_plagray_1000_175_c` — PLA Gray
- `l3d_pla_plagreen_1000_175_c` — PLA Green
- `l3d_pla_plakhaki_1000_175_c` — PLA Khaki
- `l3d_pla_plalightwood_1000_175_c` — PLA Light Wood
- `l3d_pla_plamagenta_1000_175_c` — PLA Magenta
- `l3d_pla_plared_1000_175_c` — PLA Red
- `l3d_pla_plawhite_1000_175_c` — PLA White
- `l3d_pla_playellow_1000_175_c` — PLA Yellow
- `l3d_pla_plawhite_3000_175_c` — PLA White
- `l3d_pla_silkplaarmygreen_1000_175_c` — Silk PLA Army Green
- `l3d_pla_silkplacopper_1000_175_c` — Silk PLA Copper
- `l3d_pla_silkplagold_1000_175_c` — Silk PLA Gold
- `l3d_pla_silkplalightblue_1000_175_c` — Silk PLA Light Blue
- `l3d_pla_silkplalightgreen_1000_175_c` — Silk PLA Light Green
- `l3d_pla_silkplalightlilac_1000_175_c` — Silk PLA Light Lilac
- `l3d_pla_silkplared_1000_175_c` — Silk PLA Red
- `l3d_pla_silkplarose_1000_175_c` — Silk PLA Rose
- `l3d_pla_silkplasilver_1000_175_c` — Silk PLA Silver
- `l3d_pla_silkplawhite_1000_175_c` — Silk PLA White
- `l3d_pla_plabasicblue_1000_175_p` — PLA Basic Blue
- `l3d_pla_plabasiccyan_1000_175_p` — PLA Basic Cyan
- `l3d_pla_plabasicdarkgray_1000_175_p` — PLA Basic Dark Gray
- `l3d_pla_plabasicgold_1000_175_p` — PLA Basic Gold
- `l3d_pla_plabasicgreen_1000_175_p` — PLA Basic Green
- `l3d_pla_plabasicmagenta_1000_175_p` — PLA Basic Magenta
- `l3d_pla_plabasicred_1000_175_p` — PLA Basic Red
- `l3d_pla_plabasicwhite_1000_175_p` — PLA Basic White
- `l3d_pla_plabasicyellow_1000_175_p` — PLA Basic Yellow
- `l3d_pla_plasilkarmygreen_1000_175_p` — PLA Silk Army green
- `l3d_pla_plasilkcopper_1000_175_p` — PLA Silk Copper
- `l3d_pla_plasilkgold_1000_175_p` — PLA Silk Gold
- `l3d_pla_plasilklightblue_1000_175_p` — PLA Silk Light Blue
- `l3d_pla_plasilklightgreen_1000_175_p` — PLA Silk Light Green
- `l3d_pla_plasilklightlilla_1000_175_p` — PLA Silk Light Lilla
- `l3d_pla_plasilkred_1000_175_p` — PLA Silk Red
- `l3d_pla_plasilkrose_1000_175_p` — PLA Silk Rose
- `l3d_pla_plasilksilver_1000_175_p` — PLA Silk Silver
- `l3d_pla_plasilkwhite_1000_175_p` — PLA Silk White
