# inland duplicate migration review

Base `c3700f57eb0492d469f26230cc9041cf6c547774`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `7aa3a6dfc46d02daac3bd3bcd31ed496e019288f6fcc8f3a18139cc68b866af4`.

## Authorization and result

{"groups": 1, "approved_groups": 0, "retired": 0, "deferred": 1, "hard_stops": 0, "before_count": 51702, "after_count": 51702, "brand_before": 196, "brand_after": 196, "registry_before": 1732, "registry_after": 1732, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

OnePLA BasicGray/Grey visibly differentHEX and unbound sameSKU; defer. CurrentUPC/SKU not imported onto uncertain historicalcolors. No metadata changes.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. Future reviewed retirements would not redirect external catalog lookups automatically.

## Current first-party evidence

- {"url": "https://www.microcenter.com/product/692937/inland-175mm-pla-basic-3d-printer-filament-1kg-(22lbs)-cardboard-spool-gray", "sku": "MCPLABASICH1", "upc": "618996783663", "nozzle": [210, 230], "bed": [35, 60], "note": "Exact currentGray does not bind both HEX808080/585B69 source colors; no packaging inference."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### IN001: dup-0bc49e98c8e449298a280432faa4f1b9cac9de925498a7791e96354ecb7dc6d5

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`inland_pla_plabasicgray_1000_175_c`|`PLA Basic {color_name}`|`Gray`|{"source_file": "inland.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`inland_pla_plabasicgrey_1000_175_c`|`PLA Basic {color_name}`|`Grey`|{"source_file": "inland.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "inland_pla_plabasicgray_1000_175_c": "808080",
    "inland_pla_plabasicgrey_1000_175_c": "585B69"
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

- `inland_pla_plabasicblack_1000_175_c` — PLA Basic Black
- `inland_pla_plabasicwhite_1000_175_c` — PLA Basic White
- `inland_pla_plabasictruered_1000_175_c` — PLA Basic True Red
- `inland_pla_plabasicblue_1000_175_c` — PLA Basic Blue
- `inland_pla_plabasicgreen_1000_175_c` — PLA Basic Green
- `inland_pla_plabasictruegreen_1000_175_c` — PLA Basic True Green
- `inland_pla_plabasicyellow_1000_175_c` — PLA Basic Yellow
- `inland_pla_plabasicorange_1000_175_c` — PLA Basic Orange
- `inland_pla_plabasicpurple_1000_175_c` — PLA Basic Purple
- `inland_pla_plabasicbrown_1000_175_c` — PLA Basic Brown
- `inland_pla_plabasicgold_1000_175_c` — PLA Basic Gold
- `inland_pla_plabasicsilver_1000_175_c` — PLA Basic Silver
- `inland_pla_plabasicpink_1000_175_c` — PLA Basic Pink
- `inland_pla_plabasicneongreen_1000_175_c` — PLA Basic Neon Green
- `inland_pla_plabasicneonorange_1000_175_c` — PLA Basic Neon Orange
- `inland_pla_plabasicneonyellow_1000_175_c` — PLA Basic Neon Yellow
- `inland_pla+_pla+black_1000_175_p` — PLA+ Black
- `inland_pla+_pla+white_1000_175_p` — PLA+ White
- `inland_pla+_pla+gray_1000_175_p` — PLA+ Gray
- `inland_pla+_pla+truered_1000_175_p` — PLA+ True Red
- `inland_pla+_pla+blue_1000_175_p` — PLA+ Blue
- `inland_pla+_pla+brown_1000_175_p` — PLA+ Brown
- `inland_pla+_pla+green_1000_175_p` — PLA+ Green
- `inland_pla+_pla+yellow_1000_175_p` — PLA+ Yellow
- `inland_pla+_pla+orange_1000_175_p` — PLA+ Orange
- `inland_pla+_pla+purple_1000_175_p` — PLA+ Purple
- `inland_pla+_pla+neongreen_1000_175_p` — PLA+ Neon Green
- `inland_pla+_pla+spoolessblack_1000_175_c` — PLA+ Spooless Black
- `inland_pla+_pla+spoolesswhite_1000_175_c` — PLA+ Spooless White
- `inland_pla+_pla+spoolesstruered_1000_175_c` — PLA+ Spooless True Red
- `inland_pla+_pla+spoolessbrown_1000_175_c` — PLA+ Spooless Brown
- `inland_pla+_pla+spoolessyellow_1000_175_c` — PLA+ Spooless Yellow
- `inland_pla_plamatteblack_1000_175_c` — PLA Matte Black
- `inland_pla_plamattewoodbrown_1000_175_c` — PLA Matte Wood Brown
- `inland_pla_plamattewhite_1000_175_c` — PLA Matte White
- `inland_pla_plamatteashgray_1000_175_c` — PLA Matte Ash Gray
- `inland_pla_plamattepink_1000_175_c` — PLA Matte Pink
- `inland_pla_platoughblack_1000_175_c` — PLA Tough Black
- `inland_pla_platoughblue_1000_175_c` — PLA Tough Blue
- `inland_pla_platoughlightgray_1000_175_c` — PLA Tough Light Gray
- `inland_pla_platoughorange_1000_175_c` — PLA Tough Orange
- `inland_pla_platoughred_1000_175_c` — PLA Tough Red
- `inland_pla_platoughwhite_1000_175_c` — PLA Tough White
- `inland_pla_platoughyellow_1000_175_c` — PLA Tough Yellow
- `inland_pla_plaglowindarkrainbow_1000_175_p` — PLA Glow in Dark Rainbow
- `inland_pla_plasilksilksilver_1000_175_p` — PLA Silk Silk Silver
- `inland_pla_plasilksilkgold_1000_175_p` — PLA Silk Silk Gold
- `inland_pla_pladualcolorsilkblue-green_1000_175_c` — PLA Dual Color Silk Blue-Green
- `inland_pla_pladualcolormatteblack-white_1000_175_p` — PLA Dual Color Matte Black-White
- `inland_pla_pladualcolormatteblue-lightblue_1000_175_p` — PLA Dual Color Matte Blue-Light Blue
- `inland_pla_pladualcolormatteblue-red_1000_175_p` — PLA Dual Color Matte Blue-Red
- `inland_pla_pladualcolormattepink-red_1000_175_p` — PLA Dual Color Matte Pink-Red
- `inland_petg_petg+black_1000_175_p` — PETG+ Black
- `inland_petg_petg+clear_1000_175_p` — PETG+ Clear
- `inland_petg_petg+translucentblue_1000_175_p` — PETG+ Translucent Blue
- `inland_petg_petg+translucentpurple_1000_175_p` — PETG+ Translucent Purple
- `inland_petg_petg+gray_1000_175_p` — PETG+ Gray
- `inland_petg_petg+silver_1000_175_p` — PETG+ Silver
- `inland_petg_petg+yellow_1000_175_p` — PETG+ Yellow
- `inland_petg_petg+green_1000_175_p` — PETG+ Green
- `inland_petg_petg+blue_1000_175_p` — PETG+ Blue
- `inland_petg_petg+red_1000_175_p` — PETG+ Red
- `inland_petg_petgblack_1000_175_c` — PETG Black
- `inland_petg_petgwhite_1000_175_c` — PETG White
- `inland_petg_petgblue_1000_175_c` — PETG Blue
- `inland_petg_petggreen_1000_175_c` — PETG Green
- `inland_petg_petgpurple_1000_175_c` — PETG Purple
- `inland_petg_petgred_1000_175_c` — PETG Red
- `inland_petg_petgyellow_1000_175_c` — PETG Yellow
- `inland_petg_petggray_1000_175_c` — PETG Gray
- `inland_petg_petgdarkgray_1000_175_c` — PETG Dark Gray
- `inland_petg_petgtransparent_1000_175_c` — PETG Transparent
- `inland_petg_petgclear_1000_175_c` — PETG Clear
- `inland_petg_petghighspeedblack_1000_175_c` — PETG High Speed Black
- `inland_petg_petghighspeedred_1000_175_c` — PETG High Speed Red
- `inland_petg-cf_petg-cfblack_1000_175_p` — PETG-CF Black
- `inland_petg-cf_petg-cfantiquebrass_1000_175_p` — PETG-CF Antique Brass
- `inland_petg-cf_petg-cfblackishgreen_1000_175_p` — PETG-CF Blackish Green
- `inland_petg-cf_petg-cfblackishred_1000_175_p` — PETG-CF Blackish Red
- `inland_asa_polyliteasablack_1000_175_p` — PolyLite ASA Black
- `inland_tpu_tpuredcolorchange_1000_175_p` — TPU Red Color Change
- `inland_tpu_tpublack_1000_175_p` — TPU Black
- `inland_tpu_tputranslucentyellow_1000_175_p` — TPU Translucent Yellow
- `inland_pa-cf_nyloncarbonfiberblack_500_175_p` — Nylon Carbon Fiber Black
- `inland_pla_platwinklinggold_1000_175_p` — PLA Twinkling Gold
- `inland_pla_platoughmetallicbronze_1000_175_p` — PLA Tough Metallic Bronze
- `inland_pla_plablack-red_1000_175_p` — PLA Black-Red
- `inland_pla_plablack_1000_175_p` — PLA Black
- `inland_pla_plablue_1000_175_p` — PLA Blue
- `inland_pla_plabluemarble_1000_175_p` — PLA Blue Marble
- `inland_pla_plabonewhite_1000_175_p` — PLA Bone White
- `inland_pla_plabrown_1000_175_p` — PLA Brown
- `inland_pla_placoolwhite_1000_175_p` — PLA Cool White
- `inland_pla_placoral_1000_175_p` — PLA Coral
- `inland_pla_placornflowerblue_1000_175_p` — PLA Cornflower Blue
- `inland_pla_pladarkblue_1000_175_p` — PLA Dark Blue
- `inland_pla_pladarkgrey-green_1000_175_p` — PLA Dark Grey-Green
- `inland_pla_plaegyptianblue_1000_175_p` — PLA Egyptian Blue
- `inland_pla_plaglitterblack_1000_175_p` — PLA Glitter Black
- `inland_pla_plaglitterpink_1000_175_p` — PLA Glitter Pink
- `inland_pla_plaglitterpurple_1000_175_p` — PLA Glitter Purple
- `inland_pla_plaglittersilver_1000_175_p` — PLA Glitter Silver
- `inland_pla_plagold_1000_175_p` — PLA Gold
- `inland_pla_plagray_1000_175_p` — PLA Gray
- `inland_pla_plagreen_1000_175_p` — PLA Green
- `inland_pla_plainlandblue_1000_175_p` — PLA Inland Blue
- `inland_pla_plakhaki_1000_175_p` — PLA Khaki
- `inland_pla_plalightblue_1000_175_p` — PLA Light Blue
- `inland_pla_plalightbrown_1000_175_p` — PLA Light Brown
- `inland_pla_plalightolive_1000_175_p` — PLA Light Olive
- `inland_pla_plamagenta_1000_175_p` — PLA Magenta
- `inland_pla_plamarble_1000_175_p` — PLA Marble
- `inland_pla_plamilitarybrown_1000_175_p` — PLA Military Brown
- `inland_pla_plamilitarygreen_1000_175_p` — PLA Military Green
- `inland_pla_planatural_1000_175_p` — PLA Natural
- `inland_pla_planeongreen_1000_175_p` — PLA Neon Green
- `inland_pla_plaolivebrown_1000_175_p` — PLA Olive Brown
- `inland_pla_plaolivegreen_1000_175_p` — PLA Olive Green
- `inland_pla_plaorange_1000_175_p` — PLA Orange
- `inland_pla_plapink_1000_175_p` — PLA Pink
- `inland_pla_plapurple_1000_175_p` — PLA Purple
- `inland_pla_plaraspberryred_1000_175_p` — PLA Raspberry Red
- `inland_pla_plared_1000_175_p` — PLA Red
- `inland_pla_plasand_1000_175_p` — PLA Sand
- `inland_pla_plasilver_1000_175_p` — PLA Silver
- `inland_pla_platruegreen_1000_175_p` — PLA True Green
- `inland_pla_platurquoise_1000_175_p` — PLA Turquoise
- `inland_pla_plawhite_1000_175_p` — PLA White
- `inland_pla_plawhitemarble_1000_175_p` — PLA White Marble
- `inland_pla_plawood_1000_175_p` — PLA Wood
- `inland_pla_playellow_1000_175_p` — PLA Yellow
- `inland_pla_playellowmarble_1000_175_p` — PLA Yellow Marble
- `inland_pla_pladarkgray_1000_175_p` — PLA Dark Gray
- `inland_pla_plaluminousblue_1000_175_p` — PLA Luminous Blue
- `inland_pla_plaluminousgreen_1000_175_p` — PLA Luminous Green
- `inland_pla_platruered_1000_175_p` — PLA True Red
- `inland_abs_absblack_1000_175_c` — ABS Black
- `inland_abs_absblue_1000_175_c` — ABS Blue
- `inland_abs_absgray_1000_175_c` — ABS Gray
- `inland_abs_absgreen_1000_175_c` — ABS Green
- `inland_abs_absnatural_1000_175_c` — ABS Natural
- `inland_abs_absneonorange_1000_175_c` — ABS Neon Orange
- `inland_abs_absneonred_1000_175_c` — ABS Neon Red
- `inland_abs_absneonwhite_1000_175_c` — ABS Neon White
- `inland_abs_absneonyellow_1000_175_c` — ABS Neon Yellow
- `inland_abs_absorange_1000_175_c` — ABS Orange
- `inland_abs_abssilver_1000_175_c` — ABS Silver
- `inland_abs_abswhite_1000_175_c` — ABS White
- `inland_abs_absyellow_1000_175_c` — ABS Yellow
- `inland_abs_glowabsinthedark_1000_175_c` — Glow ABS In the Dark
- `inland_pla_highspeedpla+beige_1000_175_c` — High Speed PLA+ Beige
- `inland_pla_highspeedpla+black_1000_175_c` — High Speed PLA+ Black
- `inland_pla_highspeedpla+blue_1000_175_c` — High Speed PLA+ Blue
- `inland_pla_highspeedpla+bonewhite_1000_175_c` — High Speed PLA+ Bone White
- `inland_pla_highspeedpla+brown_1000_175_c` — High Speed PLA+ Brown
- `inland_pla_highspeedpla+darkblue_1000_175_c` — High Speed PLA+ Dark Blue
- `inland_pla_highspeedpla+forestgreen_1000_175_c` — High Speed PLA+ Forest Green
- `inland_pla_highspeedpla+gray_1000_175_c` — High Speed PLA+ Gray
- `inland_pla_highspeedpla+lightblue_1000_175_c` — High Speed PLA+ Light Blue
- `inland_pla_highspeedpla+lightbrown_1000_175_c` — High Speed PLA+ Light Brown
- `inland_pla_highspeedpla+magenta_1000_175_c` — High Speed PLA+ Magenta
- `inland_pla_highspeedpla+milkwhite_1000_175_c` — High Speed PLA+ Milk White
- `inland_pla_highspeedpla+neongreen_1000_175_c` — High Speed PLA+ Neon Green
- `inland_pla_highspeedpla+olivegreen_1000_175_c` — High Speed PLA+ Olive Green
- `inland_pla_highspeedpla+orange_1000_175_c` — High Speed PLA+ Orange
- `inland_pla_highspeedpla+periwinkleblue_1000_175_c` — High Speed PLA+ Periwinkle Blue
- `inland_pla_highspeedpla+pink_1000_175_c` — High Speed PLA+ Pink
- `inland_pla_highspeedpla+purple_1000_175_c` — High Speed PLA+ Purple
- `inland_pla_highspeedpla+red_1000_175_c` — High Speed PLA+ Red
- `inland_pla_highspeedpla+silver_1000_175_c` — High Speed PLA+ Silver
- `inland_pla_highspeedpla+spaceblue_1000_175_c` — High Speed PLA+ Space Blue
- `inland_pla_highspeedpla+truered_1000_175_c` — High Speed PLA+ True Red
- `inland_pla_highspeedpla+white_1000_175_c` — High Speed PLA+ White
- `inland_pla_highspeedpla+yellow_1000_175_c` — High Speed PLA+ Yellow
- `inland_pla_plachameleongray_1000_175_c` — PLA Chameleon Gray
- `inland_pla_plaglitterrainbowpurple,yellow,green_1000_175_c` — Pla Glitter Rainbow Purple, Yellow, Green
- `inland_pla_plaglitterrainbowred_1000_175_c` — Pla Glitter Rainbow Red
- `inland_pla_plamysticsilkgoldgreenblack_1000_175_c` — PLA Mystic Silk Gold Green Black
- `inland_pla_plasilkrainbowbronze_1000_175_c` — Pla Silk Rainbow Bronze
- `inland_pla_plasilkrainbowteal,yellow_1000_175_c` — Pla Silk Rainbow Teal, Yellow
- `inland_pla_silkplablue_1000_175_c` — Silk PLA Blue
- `inland_pla_silkplacopper_1000_175_c` — Silk PLA Copper
- `inland_pla_silkplacyanblue_1000_175_c` — Silk PLA Cyan Blue
- `inland_pla_silkpladualcolorlimegreentomagenta_1000_175_c` — Silk PLA Dual Color Lime Green to Magenta
- `inland_pla_silkplagold_1000_175_c` — Silk PLA Gold
- `inland_pla_silkplagray_1000_175_c` — Silk PLA Gray
- `inland_pla_silkplamysticblack-gold-green_1000_175_c` — Silk PLA Mystic Black-gold-green
- `inland_pla_silkplamysticcopper-purple-green_1000_175_c` — Silk PLA Mystic Copper-purple-green
- `inland_pla_silkplamysticgoldredgreen_1000_175_c` — Silk PLA Mystic Gold Red Green
- `inland_pla_silkplamysticorangebluegreen_1000_175_c` — Silk PLA Mystic Orange Blue Green
- `inland_pla_silkplapurple_1000_175_c` — Silk PLA Purple
- `inland_pla_silkplared_1000_175_c` — Silk PLA Red
- `inland_pla_silkplasilver_1000_175_c` — Silk PLA Silver
- `inland_pla_silkplawhite_1000_175_c` — Silk PLA White
