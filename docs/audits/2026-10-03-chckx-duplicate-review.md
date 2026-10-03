# chckx duplicate migration review

Base `87406189a515e133519bc74f05508fe760fe7269`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `7aa3a6dfc46d02daac3bd3bcd31ed496e019288f6fcc8f3a18139cc68b866af4`.

## Authorization and result

{"groups": 1, "approved_groups": 0, "retired": 0, "deferred": 1, "hard_stops": 0, "before_count": 51702, "after_count": 51702, "brand_before": 78, "brand_after": 78, "registry_before": 1732, "registry_after": 1732, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

CrystalPurple candidate blocked by strict product-line/color decomposition. Source website self-identifies as conceptdemo; no numeric substitution or identity inference. Preserve both records.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. Future reviewed retirements would not redirect external catalog lookups automatically.

## Current first-party evidence

- {"url": "https://chckx.net/", "note": "Explicit concept-demonstration site; representative figures are not manufacturer-specification evidence."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### CH001: dup-299c93ce44bdb22707f2e67bae927a012f826cf8664dbc679df4a75da5965d98

Status: DEFERRED; survivor `chckx_petg_petgcrystalpurple_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`chckx_petg_crystalpurple_1000_175_p`|`Crystal {color_name}`|`Purple`|{"source_file": "chckx.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / False|
|`chckx_petg_petgcrystalpurple_1000_175_p`|`PETG {color_name}`|`Crystal Purple`|{"source_file": "chckx.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 19, "compiled_records": 19} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp_range": {
    "chckx_petg_crystalpurple_1000_175_p": [
      230,
      250
    ],
    "chckx_petg_petgcrystalpurple_1000_175_p": [
      240,
      260
    ]
  },
  "bed_temp_range": {
    "chckx_petg_crystalpurple_1000_175_p": [
      70,
      85
    ],
    "chckx_petg_petgcrystalpurple_1000_175_p": [
      70,
      70
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

- `chckx_petg_crystalblue_1000_175_p` — Crystal Blue
- `chckx_petg-gf_gfblack_1000_175_p` — Gf Black
- `chckx_petg-gf_gfgray_1000_175_p` — Gf Gray
- `chckx_petg-gf_gfwhite_1000_175_p` — Gf White
- `chckx_pla_mattedualredandyellow_1000_175_p` — Matte Dual Red and Yellow
- `chckx_pla_mattedualyellow-green_1000_175_p` — Matte Dual Yellow-Green
- `chckx_pla_mattedualyellow-pink_1000_175_p` — Matte Dual Yellow-Pink
- `chckx_pla_matterainbowcandy_1000_175_p` — Matte Rainbow Candy
- `chckx_pla_matterainbowcandy2_1000_175_p` — Matte Rainbow Candy 2
- `chckx_pla_matterainbowcandy3_1000_175_p` — Matte Rainbow Candy 3
- `chckx_pla_mattetricolorblack,red,andorange_1000_175_p` — Matte Tri Color Black, Red, and Orange
- `chckx_pla_mattetricolorblue,green,andpurple_1000_175_p` — Matte Tri Color Blue, Green, and Purple
- `chckx_pla_mattetricolorblue,green,andyellow_1000_175_p` — Matte Tri Color Blue, Green, and Yellow
- `chckx_pla_mattetricolorblue,yellow,andpink_1000_175_p` — Matte Tri Color Blue, Yellow, and Pink
- `chckx_pla_mattetricolorchckx_1000_175_p` — Matte Tri Color CHCKX
- `chckx_petg_multicolormulticolorglassaurora1_1000_175_p` — Multicolor Multicolor Glass Aurora 1
- `chckx_petg_multicolormulticolorglassblue-purple_1000_175_p` — Multicolor Multicolor Glass Blue-Purple
- `chckx_petg_multicolormulticolorglasscandycolors_1000_175_p` — Multicolor Multicolor Glass Candy Colors
- `chckx_petg_multicolormulticolorglassicecream_1000_175_p` — Multicolor Multicolor Glass Ice Cream
- `chckx_petg_multicolormulticolorglassmacarons_1000_175_p` — Multicolor Multicolor Glass Macarons
- `chckx_petg_multicolormulticolorglassstarrysea_1000_175_p` — Multicolor Multicolor Glass Starry Sea
- `chckx_petg_petgmatteblue_1000_175_p` — PETG Matte Blue
- `chckx_petg_petgmattegrey_1000_175_p` — PETG Matte Grey
- `chckx_petg_petgmattematteblack_1000_175_p` — PETG Matte Matte Black
- `chckx_petg_petgmattemattewhite_1000_175_p` — PETG Matte Matte White
- `chckx_petg_petgmattepink_1000_175_p` — PETG Matte Pink
- `chckx_petg_petgmattered_1000_175_p` — PETG Matte Red
- `chckx_petg_petgmatteskincolor_1000_175_p` — PETG Matte SKIN Color
- `chckx_petg_petgblack_1000_175_p` — PETG Black
- `chckx_petg_petgblue_1000_175_p` — PETG Blue
- `chckx_petg_petgbrown_1000_175_p` — PETG Brown
- `chckx_petg_petgcolor_1000_175_p` — PETG Color
- `chckx_petg_petgflashblue_1000_175_p` — PETG Flash Blue
- `chckx_petg_petggreen_1000_175_p` — PETG Green
- `chckx_petg_petggrey_1000_175_p` — PETG Grey
- `chckx_petg_petgmetalliccoffeebrown_1000_175_p` — PETG Metallic Coffee Brown
- `chckx_petg_petgmetallicorange_1000_175_p` — PETG Metallic Orange
- `chckx_petg_petgmetallicrosegold_1000_175_p` — PETG Metallic Rose Gold
- `chckx_petg_petgmetallicteal(greeneye)_1000_175_p` — PETG Metallic Teal (Green Eye)
- `chckx_petg_petgorange_1000_175_p` — PETG Orange
- `chckx_petg_petgorange-light_1000_175_p` — PETG Orange-Light
- `chckx_petg_petgpurple_1000_175_p` — PETG Purple
- `chckx_petg_petgred_1000_175_p` — PETG Red
- `chckx_petg_petgsilver_1000_175_p` — PETG Silver
- `chckx_petg_petgwhite_1000_175_p` — PETG White
- `chckx_petg_petgyellow_1000_175_p` — PETG Yellow
- `chckx_pla_plamattefourseasonsofautumn_1000_175_p` — PLA Matte Four Seasons of Autumn
- `chckx_pla_plamattefourseasonsofspring_1000_175_p` — PLA Matte Four Seasons of Spring
- `chckx_pla_plamattefourseasonsofsummer_1000_175_p` — PLA Matte Four Seasons of Summer
- `chckx_pla_plamattefourseasonsofwinter_1000_175_p` — PLA Matte Four Seasons of Winter
- `chckx_pla_plamattepowderblue_1000_175_p` — PLA Matte Powder Blue
- `chckx_pla_plabamboogreen_1000_175_p` — PLA Bamboo Green
- `chckx_pla_plablack_1000_175_p` — PLA Black
- `chckx_pla_plaenergeticorange_1000_175_p` — PLA Energetic Orange
- `chckx_pla_plagray_1000_175_p` — PLA Gray
- `chckx_pla_plalightyellow_1000_175_p` — PLA Light Yellow
- `chckx_pla_plaorange_1000_175_p` — PLA Orange
- `chckx_pla_plapeachpink_1000_175_p` — PLA Peach Pink
- `chckx_pla_plapink_1000_175_p` — PLA Pink
- `chckx_pla_plapurple_1000_175_p` — PLA Purple
- `chckx_pla_plasilver_1000_175_p` — PLA Silver
- `chckx_pla_plaskin-color_1000_175_p` — PLA Skin-Color
- `chckx_pla_plastarryblue_1000_175_p` — PLA Starry Blue
- `chckx_pla_plawhite_1000_175_p` — PLA White
- `chckx_pla_silkdualblackandred_1000_175_p` — Silk Dual Black and Red
- `chckx_pla_silkdualbluegreen_1000_175_p` — Silk Dual Blue Green
- `chckx_pla_silkdualred/pink/purple_1000_175_p` — Silk Dual Red/Pink/Purple
- `chckx_pla_silktripleblack/blue/purple_1000_175_p` — Silk Triple Black/Blue/Purple
- `chckx_pla_silktripleblue,black,andpurple_1000_175_p` — Silk Triple Blue, Black, and Purple
- `chckx_pla_silktriplegreen/purple/copper_1000_175_p` — Silk Triple Green/Purple/Copper
- `chckx_pla_silktripleredyellowblue_1000_175_p` — Silk Triple Red Yellow Blue
- `chckx_pla_silktriplered/blue/green_1000_175_p` — Silk Triple Red/Blue/Green
- `chckx_pla_silktriplered/gold/green_1000_175_p` — Silk Triple Red/Gold/Green
- `chckx_pla_silktriplewhite/blue/green_1000_175_p` — Silk Triple White/Blue/Green
- `chckx_pla_silktriplewhite/gold/green_1000_175_p` — Silk Triple White/Gold/Green
- `chckx_pla_silktripleyellow/blue/purple_1000_175_p` — Silk Triple Yellow/Blue/Purple
