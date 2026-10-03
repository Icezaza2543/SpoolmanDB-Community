# iboss duplicate migration review

Base `92d6f150ed55b953289f18cada35a3c7e21480aa`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `7aa3a6dfc46d02daac3bd3bcd31ed496e019288f6fcc8f3a18139cc68b866af4`.

## Authorization and result

{"groups": 1, "approved_groups": 0, "retired": 0, "deferred": 1, "hard_stops": 0, "before_count": 51702, "after_count": 51702, "brand_before": 109, "brand_after": 109, "registry_before": 1732, "registry_after": 1732, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Red/Green versusRedGreen tie has differing multicolor representation; no same-SKU proof. Defer; no density/bed guesses or identifier enrichment.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. Future reviewed retirements would not redirect external catalog lookups automatically.

## Current first-party evidence

- {"url": "https://www.iboss-3d.com/IBOSS-3D-Printer-Filament-PLA-Silk-dual-color-material-pd570215268.html", "nozzle": [190, 220], "note": "RedGreen exists; no exactSKU binding between differing source multicolor representations."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### IB001: dup-a4f56d98a88206c53508feaa7d858e2419a0607dde34407de25b9378348c3659

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`iboss_pla+_silkdualred/green_1000_175_p`|`Silk Dual {color_name}`|`Red / Green`|{"source_file": "iboss.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|
|`iboss_pla+_silkdualredgreen_1000_175_p`|`Silk Dual {color_name}`|`Red Green`|{"source_file": "iboss.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "iboss_pla+_silkdualred/green_1000_175_p": null,
    "iboss_pla+_silkdualredgreen_1000_175_p": "66ff8c"
  },
  "color_hexes": {
    "iboss_pla+_silkdualred/green_1000_175_p": [
      "ff0000",
      "008000"
    ],
    "iboss_pla+_silkdualredgreen_1000_175_p": null
  },
  "multi_color_direction": {
    "iboss_pla+_silkdualred/green_1000_175_p": "longitudinal",
    "iboss_pla+_silkdualredgreen_1000_175_p": null
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

- `iboss_petg_glitterdotpurple_1000_175_p` — Glitter Dot Purple
- `iboss_petg_glittermintgreen_1000_175_p` — Glitter Mint Green
- `iboss_petg_glitterpurple_1000_175_p` — Glitter Purple
- `iboss_petg_glitterpurplered_1000_175_p` — Glitter Purple Red
- `iboss_petg_glitterskyblue_1000_175_p` — Glitter Sky Blue
- `iboss_petg_glitterwaterblue_1000_175_p` — Glitter Water Blue
- `iboss_pla+_glittertransparentglitterpurple_1000_175_p` — Glitter Transparent Glitter Purple
- `iboss_pla+_glowwhite_1000_175_p` — Glow White
- `iboss_pla_glowwhitewithblueglow_1000_175_p` — Glow White with Blue Glow
- `iboss_pla_glowwhitewithgreenglow_1000_175_p` — Glow White with Green Glow
- `iboss_pla+_gradientbluewhite_1000_175_p` — Gradient Blue White
- `iboss_pla+_gradientglitterpinkbluegreen_1000_175_p` — Gradient Glitter Pink Blue Green
- `iboss_pla+_gradientglitterrainbow_1000_175_p` — Gradient Glitter Rainbow
- `iboss_pla+_gradientgreenwhite_1000_175_p` — Gradient Green White
- `iboss_pla+_gradientorangewhite_1000_175_p` — Gradient Orange White
- `iboss_pla+_gradientpinkwhite_1000_175_p` — Gradient Pink White
- `iboss_pla+_gradientpurplewhite_1000_175_p` — Gradient Purple White
- `iboss_pla+_gradienttransparentbluegreen_1000_175_p` — Gradient Transparent Blue Green
- `iboss_pla+_gradienttransparentlightorangegreen_1000_175_p` — Gradient Transparent Light Orange Green
- `iboss_pla+_gradienttransparentpurpleblue_1000_175_p` — Gradient Transparent Purple Blue
- `iboss_pla+_gradienttransparentredbluegreen_1000_175_p` — Gradient Transparent Red Blue Green
- `iboss_pla+_gradienttransparentroseredlightblue_1000_175_p` — Gradient Transparent Rose Red Light Blue
- `iboss_pla+_gradienttransparentroseredorange_1000_175_p` — Gradient Transparent Rose Red Orange
- `iboss_pla+_gradientwhitepurpleblue_1000_175_p` — Gradient White Purple Blue
- `iboss_pla+_gradientyellowgreenwhite_1000_175_p` — Gradient Yellow Green White
- `iboss_pla+_gradientyelloworangewhite_1000_175_p` — Gradient Yellow Orange White
- `iboss_pla+_gradientyellowwhite_1000_175_p` — Gradient Yellow White
- `iboss_pla_gradienttransparentpurpleblue_1000_175_p` — Gradient Transparent Purple Blue
- `iboss_pla+_marblemarblegray_1000_175_p` — Marble Marble Gray
- `iboss_pla+_marblemarblewhite_1000_175_p` — Marble Marble White
- `iboss_pla+_mattedualpinkblue_1000_175_p` — Matte Dual Pink Blue
- `iboss_petg_petgblack_1000_175_p` — PETG Black
- `iboss_petg_petgcyan_1000_175_p` — PETG Cyan
- `iboss_petg_petgorange_1000_175_p` — PETG Orange
- `iboss_petg_petgpearlescentgold_1000_175_p` — PETG Pearlescent Gold
- `iboss_petg_petgpink_1000_175_p` — PETG Pink
- `iboss_petg_petgrosepink_1000_175_p` — PETG Rose Pink
- `iboss_petg_petgblack_1194_175_p` — PETG Black
- `iboss_petg_petgcyan_1194_175_p` — PETG Cyan
- `iboss_petg_petgorange_1194_175_p` — PETG Orange
- `iboss_petg_petgpearlescentgold_1194_175_p` — PETG Pearlescent Gold
- `iboss_petg_petgpink_1194_175_p` — PETG Pink
- `iboss_petg_petgrosepink_1194_175_p` — PETG Rose Pink
- `iboss_pla_plasilkblue_1000_175_p` — PLA Silk blue
- `iboss_pla_plasilkgold_1000_175_p` — PLA Silk Gold
- `iboss_pla_plasilktricolorgoldgreenblue_1000_175_p` — PLA Silk Tri Color Gold Green Blue
- `iboss_pla+_pla+mattemattedarkblue_1000_175_p` — PLA+ Matte Matte Dark Blue
- `iboss_pla+_pla+problack_1000_175_p` — PLA+ Pro Black
- `iboss_pla+_pla+problue_1000_175_p` — PLA+ Pro Blue
- `iboss_pla+_pla+silkblue&purpledualcolor_1000_175_p` — PLA+ Silk Blue & Purple Dual Color
- `iboss_pla+_pla+silkcopper_1000_175_p` — PLA+ Silk copper
- `iboss_pla+_pla+silkgold_1000_175_p` — PLA+ Silk Gold
- `iboss_pla+_pla+silkmetalicbluesilverdualcolor_1000_175_p` — PLA+ Silk Metalic Blue Silver Dual Color
- `iboss_pla+_pla+silkpurplesilverdualcolor_1000_175_p` — PLA+ Silk Purple Silver Dual Color
- `iboss_pla+_pla+silkpurplewhitegradient_1000_175_p` — PLA+ Silk Purple White Gradient
- `iboss_pla+_pla+silkredbluedualcolor_1000_175_p` — PLA+ Silk Red Blue Dual Color
- `iboss_pla+_pla+silksapphirebluelinegreendualcolor_1000_175_p` — PLA+ Silk Sapphire Blue Line Green Dual Color
- `iboss_pla+_pla+silksilver_1000_175_p` — PLA+ Silk Silver
- `iboss_pla+_pla+silktricolor(silkblack,red,copper)_1000_175_p` — PLA+ Silk Tri Color (Silk Black, Red, Copper)
- `iboss_pla+_pla+silkviolet_1000_175_p` — PLA+ Silk Violet
- `iboss_pla+_pla+silkwhite_1000_175_p` — PLA+ Silk White
- `iboss_pla+_pla+silkwhitepurplebluegradient_1000_175_p` — PLA+ Silk White Purple Blue Gradient
- `iboss_pla+_pla+silkyellowandgreen_1000_175_p` — PLA+ Silk Yellow and Green
- `iboss_pla+_pla+silkyellowgold_1000_175_p` — PLA+ Silk Yellow Gold
- `iboss_pla+_pla+orange_1000_175_p` — PLA+ orange
- `iboss_pla+_pla+purple_1000_175_p` — PLA+ Purple
- `iboss_pla+_pla+cyan_1000_175_p` — PLA+ Cyan
- `iboss_pla+_pla+ebonywood_1000_175_p` — PLA+ Ebony Wood
- `iboss_pla+_pla+lightblue_1000_175_p` — PLA+ Light Blue
- `iboss_pla+_pla+red_1000_175_p` — PLA+ Red
- `iboss_pla+_pla+skintone_1000_175_p` — PLA+ Skin tone
- `iboss_pla+_pla+white_1000_175_p` — PLA+ White
- `iboss_pla+_pla+yellow_1000_175_p` — PLA+ Yellow
- `iboss_pla+_rainbowcandyrainbow_1000_175_p` — Rainbow Candy Rainbow
- `iboss_pla+_rainbowtransparentrainbow_1000_175_p` — Rainbow transparent Rainbow
- `iboss_pla+_silkdualblack/purple_1000_175_p` — Silk Dual Black / Purple
- `iboss_pla+_silkdualblue/gold_1000_175_p` — Silk Dual Blue / Gold
- `iboss_pla+_silkdualblue/silver_1000_175_p` — Silk Dual Blue / Silver
- `iboss_pla+_silkdualbluegreen_1000_175_p` — Silk Dual Blue Green
- `iboss_pla+_silkdualbluepurple_1000_175_p` — Silk Dual Blue Purple
- `iboss_pla+_silkdualpink/gold_1000_175_p` — Silk Dual Pink / Gold
- `iboss_pla+_silkdualred/black_1000_175_p` — Silk Dual Red / Black
- `iboss_pla+_silkdualred/gold_1000_175_p` — Silk Dual Red / Gold
- `iboss_pla+_silkdualredblack_1000_175_p` — Silk Dual RedBlack
- `iboss_pla+_silkdualredbluegold_1000_175_p` — Silk Dual RedBlueGold
- `iboss_pla+_silkdualyellow/green_1000_175_p` — Silk Dual Yellow / Green
- `iboss_pla+_silkplussilkmacaron_1000_175_p` — Silk Plus SILK MACARON
- `iboss_pla+_silkrainbowrainbowcandy_1000_175_p` — Silk Rainbow Rainbow Candy
- `iboss_pla+_silktriplebluegreenpurple_1000_175_p` — Silk Triple Blue Green Purple
- `iboss_pla+_silktriplegold/green/purple_1000_175_p` — Silk Triple Gold / Green / Purple
- `iboss_pla+_silktriplegoldgreenblue_1000_175_p` — Silk Triple Gold Green Blue
- `iboss_pla+_silktripleredbluegreen_1000_175_p` — Silk Triple Red Blue Green
- `iboss_pla+_silktripleredyellowblue_1000_175_p` — Silk Triple Red Yellow Blue
- `iboss_pla+_silktripletri-colorblack/red/copper_1000_175_p` — Silk Triple Tri-Color Black/Red/Copper
- `iboss_pla+_silktripleyellow/orange/white_1000_175_p` — Silk Triple Yellow/Orange/White
- `iboss_pla+_silktriplebluegreenpurple_1194_175_p` — Silk Triple Blue Green Purple
- `iboss_pla+_silktriplegold/green/purple_1194_175_p` — Silk Triple Gold / Green / Purple
- `iboss_pla+_silktriplegoldgreenblue_1194_175_p` — Silk Triple Gold Green Blue
- `iboss_pla+_silktripleredbluegreen_1194_175_p` — Silk Triple Red Blue Green
- `iboss_pla+_silktripleredyellowblue_1194_175_p` — Silk Triple Red Yellow Blue
- `iboss_pla+_silktripletri-colorblack/red/copper_1194_175_p` — Silk Triple Tri-Color Black/Red/Copper
- `iboss_pla+_silktripleyellow/orange/white_1194_175_p` — Silk Triple Yellow/Orange/White
- `iboss_pla+_toughgreen_1000_175_p` — Tough Green
- `iboss_pla+_translucenttransparentlightorangegreen_1000_175_p` — Translucent Transparent Light Orange Green
- `iboss_pla+_transparentgreen_1000_175_p` — Transparent Green
- `iboss_pla+_transparentpurpleblue_1000_175_p` — Transparent Purple Blue
- `iboss_pla+_transparentviolet_1000_175_p` — Transparent Violet
