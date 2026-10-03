# r3d duplicate migration review

Base `956c5b79b71726c62166df1ef4904da1d7eb88cc`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `8f529c8189786635f2ca5371e14885f3c7fadac4606b63b080ef14f86bf8e5ca`.

## Authorization and result

{"groups": 2, "approved_groups": 0, "retired": 0, "deferred": 2, "hard_stops": 0, "before_count": 51702, "after_count": 51702, "brand_before": 366, "brand_after": 366, "registry_before": 1732, "registry_after": 1732, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Two PETGGray/Grey ties plastic/cardboard, HEXE7EAF2 versus808080. Defer without same-SKU/lot binding. Survivor unspecified; both fullpayloads and doclinks preserved.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. Future reviewed retirements would not redirect external catalog lookups automatically.

## Current first-party evidence

- {"url": "https://cdn.shopify.com/s/files/1/0717/3308/4411/files/PETG.pdf?v=1782966025", "note": "Existing exactPETG PDF unavailable in this audit; no current numeric claim."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### RD001: dup-034167fdd92059eb1d45ce02a412601a506e428663ee171e1c9bc957ccdd1678

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`r3d_petg_petggray_1000_175_c`|`PETG {color_name}`|`Gray`|{"source_file": "r3d.json", "definition_index": 10, "weights": 2, "diameters": 1, "colors": 34, "compiled_records": 68} / False|
|`r3d_petg_petggrey_1000_175_c`|`PETG {color_name}`|`Grey`|{"source_file": "r3d.json", "definition_index": 10, "weights": 2, "diameters": 1, "colors": 34, "compiled_records": 68} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "r3d_petg_petggray_1000_175_c": "E7EAF2",
    "r3d_petg_petggrey_1000_175_c": "808080"
  }
}
```

### RD002: dup-2aeaee15e70fe5dcad05e0feb9216866dee6a061fa5d0d02b96f78a8217ffa87

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`r3d_petg_petggray_1000_175_p`|`PETG {color_name}`|`Gray`|{"source_file": "r3d.json", "definition_index": 10, "weights": 2, "diameters": 1, "colors": 34, "compiled_records": 68} / False|
|`r3d_petg_petggrey_1000_175_p`|`PETG {color_name}`|`Grey`|{"source_file": "r3d.json", "definition_index": 10, "weights": 2, "diameters": 1, "colors": 34, "compiled_records": 68} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "r3d_petg_petggray_1000_175_p": "E7EAF2",
    "r3d_petg_petggrey_1000_175_p": "808080"
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

- `r3d_abs_absgrey_1000_175_p` — ABS Grey
- `r3d_abs_absgrey_1000_175_c` — ABS Grey
- `r3d_abs_highspeedabsblack_1000_175_p` — High Speed ABS Black
- `r3d_abs_highspeedabsblack_1000_175_c` — High Speed ABS Black
- `r3d_abs-cf_abs-cfblack_1000_175_p` — ABS-CF Black
- `r3d_abs-cf_abs-cfblack_1000_175_c` — ABS-CF Black
- `r3d_asa_asaashgray_1000_175_p` — ASA Ash Gray
- `r3d_asa_asaashgray_1000_175_c` — ASA Ash Gray
- `r3d_pa_nylonblack_1000_175_p` — Nylon Black
- `r3d_pa_nylonblack_1000_175_c` — Nylon Black
- `r3d_peba_pebalemongreen_1000_175_p` — PEBA Lemon green
- `r3d_peba_pebamatchabrown_1000_175_p` — PEBA Matcha brown
- `r3d_peba_pebalemongreen_1000_175_c` — PEBA Lemon green
- `r3d_peba_pebamatchabrown_1000_175_c` — PEBA Matcha brown
- `r3d_petg_fluorescentpetgfluorescentgreen_1000_175_p` — Fluorescent PETG Fluorescent Green
- `r3d_petg_fluorescentpetgfluorescentgreen_1000_175_c` — Fluorescent PETG Fluorescent Green
- `r3d_petg_highspeedpetgblack_1000_175_p` — High Speed PETG Black
- `r3d_petg_highspeedpetgred_1000_175_p` — High Speed PETG RED
- `r3d_petg_highspeedpetgwhite_1000_175_p` — High Speed PETG White
- `r3d_petg_highspeedpetgblack_1000_175_c` — High Speed PETG Black
- `r3d_petg_highspeedpetgred_1000_175_c` — High Speed PETG RED
- `r3d_petg_highspeedpetgwhite_1000_175_c` — High Speed PETG White
- `r3d_petg_marblepetggranite_1000_175_p` — Marble PETG Granite
- `r3d_petg_marblepetglightblue_1000_175_p` — Marble PETG Light Blue
- `r3d_petg_marblepetglightgreen_1000_175_p` — Marble PETG Light Green
- `r3d_petg_marblepetglightpurple_1000_175_p` — Marble PETG Light Purple
- `r3d_petg_marblepetgmilkcoffee_1000_175_p` — Marble PETG Milk Coffee
- `r3d_petg_marblepetggranite_1000_175_c` — Marble PETG Granite
- `r3d_petg_marblepetglightblue_1000_175_c` — Marble PETG Light Blue
- `r3d_petg_marblepetglightgreen_1000_175_c` — Marble PETG Light Green
- `r3d_petg_marblepetglightpurple_1000_175_c` — Marble PETG Light Purple
- `r3d_petg_marblepetgmilkcoffee_1000_175_c` — Marble PETG Milk Coffee
- `r3d_petg_mattepetgapricotpollen_1000_175_p` — Matte PETG Apricot Pollen
- `r3d_petg_mattepetgblack_1000_175_p` — Matte PETG Black
- `r3d_petg_mattepetgbronzegold_1000_175_p` — Matte PETG Bronze Gold
- `r3d_petg_mattepetgbrown_1000_175_p` — Matte PETG Brown
- `r3d_petg_mattepetgchinesered_1000_175_p` — Matte PETG Chinese Red
- `r3d_petg_mattepetgdarknavyblue_1000_175_p` — Matte PETG Dark Navy Blue
- `r3d_petg_mattepetgfreshgreen_1000_175_p` — Matte PETG Fresh Green
- `r3d_petg_mattepetgglacierblue_1000_175_p` — Matte PETG Glacier Blue
- `r3d_petg_mattepetggungray_1000_175_p` — Matte PETG Gun Gray
- `r3d_petg_mattepetghazeblue_1000_175_p` — Matte PETG Haze Blue
- `r3d_petg_mattepetgkhaki_1000_175_p` — Matte PETG Khaki
- `r3d_petg_mattepetglightgray_1000_175_p` — Matte PETG Light Gray
- `r3d_petg_mattepetglightpurple_1000_175_p` — Matte PETG Light Purple
- `r3d_petg_mattepetglightskyblue_1000_175_p` — Matte PETG Light Sky Blue
- `r3d_petg_mattepetgmilitarygreen_1000_175_p` — Matte PETG Military Green
- `r3d_petg_mattepetgmilkyapricotyellow_1000_175_p` — Matte PETG Milky Apricot Yellow
- `r3d_petg_mattepetgoatmealwhite_1000_175_p` — Matte PETG Oatmeal White
- `r3d_petg_mattepetgolivegreen_1000_175_p` — Matte PETG Olive Green
- `r3d_petg_mattepetgredwine_1000_175_p` — Matte PETG Red Wine
- `r3d_petg_mattepetgskyblue_1000_175_p` — Matte PETG Sky Blue
- `r3d_petg_mattepetgsnowwaxyskin_1000_175_p` — Matte PETG Snow Waxy Skin
- `r3d_petg_mattepetgsoftskin_1000_175_p` — Matte PETG Soft Skin
- `r3d_petg_mattepetgwarmgray_1000_175_p` — Matte PETG Warm Gray
- `r3d_petg_mattepetgwhite_1000_175_p` — Matte PETG White
- `r3d_petg_mattepetgwhitegreen_1000_175_p` — Matte PETG White Green
- `r3d_petg_mattepetgyellow_1000_175_p` — Matte PETG Yellow
- `r3d_petg_mattepetgyelloworange_1000_175_p` — Matte PETG Yellow Orange
- `r3d_petg_mattepetgzincyellow_1000_175_p` — Matte PETG Zinc Yellow
- `r3d_petg_mattepetgapricotpollen_1000_175_c` — Matte PETG Apricot Pollen
- `r3d_petg_mattepetgblack_1000_175_c` — Matte PETG Black
- `r3d_petg_mattepetgbronzegold_1000_175_c` — Matte PETG Bronze Gold
- `r3d_petg_mattepetgbrown_1000_175_c` — Matte PETG Brown
- `r3d_petg_mattepetgchinesered_1000_175_c` — Matte PETG Chinese Red
- `r3d_petg_mattepetgdarknavyblue_1000_175_c` — Matte PETG Dark Navy Blue
- `r3d_petg_mattepetgfreshgreen_1000_175_c` — Matte PETG Fresh Green
- `r3d_petg_mattepetgglacierblue_1000_175_c` — Matte PETG Glacier Blue
- `r3d_petg_mattepetggungray_1000_175_c` — Matte PETG Gun Gray
- `r3d_petg_mattepetghazeblue_1000_175_c` — Matte PETG Haze Blue
- `r3d_petg_mattepetgkhaki_1000_175_c` — Matte PETG Khaki
- `r3d_petg_mattepetglightgray_1000_175_c` — Matte PETG Light Gray
- `r3d_petg_mattepetglightpurple_1000_175_c` — Matte PETG Light Purple
- `r3d_petg_mattepetglightskyblue_1000_175_c` — Matte PETG Light Sky Blue
- `r3d_petg_mattepetgmilitarygreen_1000_175_c` — Matte PETG Military Green
- `r3d_petg_mattepetgmilkyapricotyellow_1000_175_c` — Matte PETG Milky Apricot Yellow
- `r3d_petg_mattepetgoatmealwhite_1000_175_c` — Matte PETG Oatmeal White
- `r3d_petg_mattepetgolivegreen_1000_175_c` — Matte PETG Olive Green
- `r3d_petg_mattepetgredwine_1000_175_c` — Matte PETG Red Wine
- `r3d_petg_mattepetgskyblue_1000_175_c` — Matte PETG Sky Blue
- `r3d_petg_mattepetgsnowwaxyskin_1000_175_c` — Matte PETG Snow Waxy Skin
- `r3d_petg_mattepetgsoftskin_1000_175_c` — Matte PETG Soft Skin
- `r3d_petg_mattepetgwarmgray_1000_175_c` — Matte PETG Warm Gray
- `r3d_petg_mattepetgwhite_1000_175_c` — Matte PETG White
- `r3d_petg_mattepetgwhitegreen_1000_175_c` — Matte PETG White Green
- `r3d_petg_mattepetgyellow_1000_175_c` — Matte PETG Yellow
- `r3d_petg_mattepetgyelloworange_1000_175_c` — Matte PETG Yellow Orange
- `r3d_petg_mattepetgzincyellow_1000_175_c` — Matte PETG Zinc Yellow
- `r3d_petg_petgbambugreen_1000_175_p` — PETG Bambu Green
- `r3d_petg_petgblack_1000_175_p` — PETG Black
- `r3d_petg_petgchinared_1000_175_p` — PETG China Red
- `r3d_petg_petgchinesered_1000_175_p` — PETG Chinese Red
- `r3d_petg_petgcoffeebrown_1000_175_p` — PETG Coffee Brown
- `r3d_petg_petgdarkgreen_1000_175_p` — PETG Dark Green
- `r3d_petg_petgdarkblue_1000_175_p` — PETG DarkBlue
- `r3d_petg_petgemerald_1000_175_p` — PETG Emerald
- `r3d_petg_petgfishbellywhite_1000_175_p` — PETG Fish Belly White
- `r3d_petg_petggildedgold_1000_175_p` — PETG Gilded Gold
- `r3d_petg_petgiris_1000_175_p` — PETG Iris
- `r3d_petg_petgjustpurple_1000_175_p` — PETG Just Purple
- `r3d_petg_petglatte_1000_175_p` — PETG Latte
- `r3d_petg_petglightblue_1000_175_p` — PETG Light Blue
- `r3d_petg_petglightpurple_1000_175_p` — PETG Light Purple
- `r3d_petg_petgmibaowhite_1000_175_p` — PETG Mibao White
- `r3d_petg_petgmintgreen_1000_175_p` — PETG Mint Green
- `r3d_petg_petgocher_1000_175_p` — PETG Ocher
- `r3d_petg_petgorange_1000_175_p` — PETG Orange
- `r3d_petg_petgpastelviolet_1000_175_p` — PETG Pastel Violet
- `r3d_petg_petgpeach_1000_175_p` — PETG Peach
- `r3d_petg_petgpink_1000_175_p` — PETG Pink
- `r3d_petg_petgpurple_1000_175_p` — PETG Purple
- `r3d_petg_petgred_1000_175_p` — PETG Red
- `r3d_petg_petgroyalblue_1000_175_p` — PETG Royal Blue
- `r3d_petg_petgsilver_1000_175_p` — PETG Silver
- `r3d_petg_petgskin_1000_175_p` — PETG Skin
- `r3d_petg_petgsnowwhiteskin_1000_175_p` — PETG Snow White Skin
- `r3d_petg_petgtangerine_1000_175_p` — PETG Tangerine
- `r3d_petg_petgwhite_1000_175_p` — PETG White
- `r3d_petg_petgwood_1000_175_p` — PETG Wood
- `r3d_petg_petgyellow_1000_175_p` — PETG Yellow
- `r3d_petg_petgbambugreen_1000_175_c` — PETG Bambu Green
- `r3d_petg_petgblack_1000_175_c` — PETG Black
- `r3d_petg_petgchinared_1000_175_c` — PETG China Red
- `r3d_petg_petgchinesered_1000_175_c` — PETG Chinese Red
- `r3d_petg_petgcoffeebrown_1000_175_c` — PETG Coffee Brown
- `r3d_petg_petgdarkgreen_1000_175_c` — PETG Dark Green
- `r3d_petg_petgdarkblue_1000_175_c` — PETG DarkBlue
- `r3d_petg_petgemerald_1000_175_c` — PETG Emerald
- `r3d_petg_petgfishbellywhite_1000_175_c` — PETG Fish Belly White
- `r3d_petg_petggildedgold_1000_175_c` — PETG Gilded Gold
- `r3d_petg_petgiris_1000_175_c` — PETG Iris
- `r3d_petg_petgjustpurple_1000_175_c` — PETG Just Purple
- `r3d_petg_petglatte_1000_175_c` — PETG Latte
- `r3d_petg_petglightblue_1000_175_c` — PETG Light Blue
- `r3d_petg_petglightpurple_1000_175_c` — PETG Light Purple
- `r3d_petg_petgmibaowhite_1000_175_c` — PETG Mibao White
- `r3d_petg_petgmintgreen_1000_175_c` — PETG Mint Green
- `r3d_petg_petgocher_1000_175_c` — PETG Ocher
- `r3d_petg_petgorange_1000_175_c` — PETG Orange
- `r3d_petg_petgpastelviolet_1000_175_c` — PETG Pastel Violet
- `r3d_petg_petgpeach_1000_175_c` — PETG Peach
- `r3d_petg_petgpink_1000_175_c` — PETG Pink
- `r3d_petg_petgpurple_1000_175_c` — PETG Purple
- `r3d_petg_petgred_1000_175_c` — PETG Red
- `r3d_petg_petgroyalblue_1000_175_c` — PETG Royal Blue
- `r3d_petg_petgsilver_1000_175_c` — PETG Silver
- `r3d_petg_petgskin_1000_175_c` — PETG Skin
- `r3d_petg_petgsnowwhiteskin_1000_175_c` — PETG Snow White Skin
- `r3d_petg_petgtangerine_1000_175_c` — PETG Tangerine
- `r3d_petg_petgwhite_1000_175_c` — PETG White
- `r3d_petg_petgwood_1000_175_c` — PETG Wood
- `r3d_petg_petgyellow_1000_175_c` — PETG Yellow
- `r3d_petg_sparklepetgsparklepink_1000_175_p` — Sparkle PETG Sparkle Pink
- `r3d_petg_sparklepetgsparklepink_1000_175_c` — Sparkle PETG Sparkle Pink
- `r3d_petg_translucentpetgbluecost-effective_1000_175_p` — Translucent PETG Blue Cost-Effective
- `r3d_petg_translucentpetgclear_1000_175_p` — Translucent PETG Clear
- `r3d_petg_translucentpetgclear(cost-effective)_1000_175_p` — Translucent PETG Clear (Cost-Effective)
- `r3d_petg_translucentpetgcleargrey_1000_175_p` — Translucent PETG Clear Grey
- `r3d_petg_translucentpetgbluecost-effective_1000_175_c` — Translucent PETG Blue Cost-Effective
- `r3d_petg_translucentpetgclear_1000_175_c` — Translucent PETG Clear
- `r3d_petg_translucentpetgclear(cost-effective)_1000_175_c` — Translucent PETG Clear (Cost-Effective)
- `r3d_petg_translucentpetgcleargrey_1000_175_c` — Translucent PETG Clear Grey
- `r3d_pla_colorchangeplapurpletored_1000_175_p` — Color Change PLA Purple to Red
- `r3d_pla_colorchangeplapurpletored_1000_175_c` — Color Change PLA Purple to Red
- `r3d_pla_fluorescentplagreen_1000_175_p` — Fluorescent PLA Green
- `r3d_pla_fluorescentplayellow_1000_175_p` — Fluorescent PLA Yellow
- `r3d_pla_fluorescentplagreen_1000_175_c` — Fluorescent PLA Green
- `r3d_pla_fluorescentplayellow_1000_175_c` — Fluorescent PLA Yellow
- `r3d_pla_glowplaneongreen_1000_175_p` — Glow PLA Neon Green
- `r3d_pla_glowplaturquoise_1000_175_p` — Glow PLA Turquoise
- `r3d_pla_glowplaneongreen_1000_175_c` — Glow PLA Neon Green
- `r3d_pla_glowplaturquoise_1000_175_c` — Glow PLA Turquoise
- `r3d_pla_highspeedmarbleplamarblewhite_1000_175_p` — High Speed Marble PLA Marble White
- `r3d_pla_highspeedmarbleplamarblewhite_1000_175_c` — High Speed Marble PLA Marble White
- `r3d_pla_highspeedmattepladarkblue_1000_175_p` — High Speed Matte PLA Dark blue
- `r3d_pla_highspeedmatteplamattenavyblue_1000_175_p` — High Speed Matte PLA MAtte Navy Blue
- `r3d_pla_highspeedmattepladarkblue_1000_175_c` — High Speed Matte PLA Dark blue
- `r3d_pla_highspeedmatteplamattenavyblue_1000_175_c` — High Speed Matte PLA MAtte Navy Blue
- `r3d_pla_magicplablack-red_1000_175_p` — Magic PLA Black-Red
- `r3d_pla_magicplasilverlavender_1000_175_p` — Magic PLA Silver Lavender
- `r3d_pla_magicplablack-red_1000_175_c` — Magic PLA Black-Red
- `r3d_pla_magicplasilverlavender_1000_175_c` — Magic PLA Silver Lavender
- `r3d_pla_marbleplablue-grey_1000_175_p` — Marble PLA Blue-grey
- `r3d_pla_marbleplablue-grey_1000_175_c` — Marble PLA Blue-grey
- `r3d_pla_matteplaarmygreen_1000_175_p` — Matte PLA Army Green
- `r3d_pla_matteplaashgrey_1000_175_p` — Matte PLA Ash Grey
- `r3d_pla_matteplaavocadogreen_1000_175_p` — Matte PLA Avocado Green
- `r3d_pla_matteplablack_1000_175_p` — Matte PLA Black
- `r3d_pla_matteplablack(refill)_1000_175_p` — Matte PLA Black (Refill)
- `r3d_pla_matteplacreamyellow_1000_175_p` — Matte PLA Cream Yellow
- `r3d_pla_mattepladarkgrey_1000_175_p` — Matte PLA Dark Grey
- `r3d_pla_matteplaglacierblue_1000_175_p` — Matte PLA Glacier Blue
- `r3d_pla_matteplagrey_1000_175_p` — Matte PLA Grey
- `r3d_pla_matteplaiceblue_1000_175_p` — Matte PLA Ice Blue
- `r3d_pla_matteplalemonyellow_1000_175_p` — Matte PLA Lemon Yellow
- `r3d_pla_matteplalightpink_1000_175_p` — Matte PLA Light Pink
- `r3d_pla_matteplalotuspink_1000_175_p` — Matte PLA Lotus Pink
- `r3d_pla_matteplamattewhite_1000_175_p` — Matte PLA Matte White
- `r3d_pla_matteplaoats_1000_175_p` — Matte PLA Oats
- `r3d_pla_matteplaolivegreen(a1ea21h)_1000_175_p` — Matte PLA Olive Green (A1EA21H)
- `r3d_pla_matteplaorange_1000_175_p` — Matte PLA Orange
- `r3d_pla_matteplapinegreen_1000_175_p` — Matte PLA Pine Green
- `r3d_pla_matteplared_1000_175_p` — Matte PLA Red
- `r3d_pla_matteplasageblue_1000_175_p` — Matte PLA Sage Blue
- `r3d_pla_matteplascalliongreen_1000_175_p` — Matte PLA Scallion Green
- `r3d_pla_matteplaseagreen_1000_175_p` — Matte PLA Sea Green
- `r3d_pla_matteplaterracotta_1000_175_p` — Matte PLA Terra Cotta
- `r3d_pla_matteplawhite_1000_175_p` — Matte PLA White
- `r3d_pla_matteplawhite(refill)_1000_175_p` — Matte PLA White (Refill)
- `r3d_pla_matteplaarmygreen_1000_175_c` — Matte PLA Army Green
- `r3d_pla_matteplaashgrey_1000_175_c` — Matte PLA Ash Grey
- `r3d_pla_matteplaavocadogreen_1000_175_c` — Matte PLA Avocado Green
- `r3d_pla_matteplablack_1000_175_c` — Matte PLA Black
- `r3d_pla_matteplablack(refill)_1000_175_c` — Matte PLA Black (Refill)
- `r3d_pla_matteplacreamyellow_1000_175_c` — Matte PLA Cream Yellow
- `r3d_pla_mattepladarkgrey_1000_175_c` — Matte PLA Dark Grey
- `r3d_pla_matteplaglacierblue_1000_175_c` — Matte PLA Glacier Blue
- `r3d_pla_matteplagrey_1000_175_c` — Matte PLA Grey
- `r3d_pla_matteplaiceblue_1000_175_c` — Matte PLA Ice Blue
- `r3d_pla_matteplalemonyellow_1000_175_c` — Matte PLA Lemon Yellow
- `r3d_pla_matteplalightpink_1000_175_c` — Matte PLA Light Pink
- `r3d_pla_matteplalotuspink_1000_175_c` — Matte PLA Lotus Pink
- `r3d_pla_matteplamattewhite_1000_175_c` — Matte PLA Matte White
- `r3d_pla_matteplaoats_1000_175_c` — Matte PLA Oats
- `r3d_pla_matteplaolivegreen(a1ea21h)_1000_175_c` — Matte PLA Olive Green (A1EA21H)
- `r3d_pla_matteplaorange_1000_175_c` — Matte PLA Orange
- `r3d_pla_matteplapinegreen_1000_175_c` — Matte PLA Pine Green
- `r3d_pla_matteplared_1000_175_c` — Matte PLA Red
- `r3d_pla_matteplasageblue_1000_175_c` — Matte PLA Sage Blue
- `r3d_pla_matteplascalliongreen_1000_175_c` — Matte PLA Scallion Green
- `r3d_pla_matteplaseagreen_1000_175_c` — Matte PLA Sea Green
- `r3d_pla_matteplaterracotta_1000_175_c` — Matte PLA Terra Cotta
- `r3d_pla_matteplawhite_1000_175_c` — Matte PLA White
- `r3d_pla_matteplawhite(refill)_1000_175_c` — Matte PLA White (Refill)
- `r3d_pla_plabasicblack_1000_175_p` — PLA Basic Black
- `r3d_pla_plabasicbrown_1000_175_p` — PLA Basic Brown
- `r3d_pla_plabasicdarkskin_1000_175_p` — PLA Basic Dark Skin
- `r3d_pla_plabasicdarkyellow_1000_175_p` — PLA Basic Dark Yellow
- `r3d_pla_plabasicgrey_1000_175_p` — PLA Basic Grey
- `r3d_pla_plabasiclimegreen_1000_175_p` — PLA Basic Lime Green
- `r3d_pla_plabasicmarble_1000_175_p` — PLA Basic Marble
- `r3d_pla_plabasicmintgreen_1000_175_p` — PLA Basic Mint Green
- `r3d_pla_plabasicnightglowblue_1000_175_p` — PLA Basic Nightglow Blue
- `r3d_pla_plabasicoats_1000_175_p` — PLA Basic Oats
- `r3d_pla_plabasicorange_1000_175_p` — PLA Basic Orange
- `r3d_pla_plabasicpersimmonyellow_1000_175_p` — PLA Basic Persimmon Yellow
- `r3d_pla_plabasicpurple_1000_175_p` — PLA Basic Purple
- `r3d_pla_plabasicred_1000_175_p` — PLA Basic Red
- `r3d_pla_plabasictransparent_1000_175_p` — PLA Basic Transparent
- `r3d_pla_plabasicwhite_1000_175_p` — PLA Basic White
- `r3d_pla_plabasicblack_1000_175_c` — PLA Basic Black
- `r3d_pla_plabasicbrown_1000_175_c` — PLA Basic Brown
- `r3d_pla_plabasicdarkskin_1000_175_c` — PLA Basic Dark Skin
- `r3d_pla_plabasicdarkyellow_1000_175_c` — PLA Basic Dark Yellow
- `r3d_pla_plabasicgrey_1000_175_c` — PLA Basic Grey
- `r3d_pla_plabasiclimegreen_1000_175_c` — PLA Basic Lime Green
- `r3d_pla_plabasicmarble_1000_175_c` — PLA Basic Marble
- `r3d_pla_plabasicmintgreen_1000_175_c` — PLA Basic Mint Green
- `r3d_pla_plabasicnightglowblue_1000_175_c` — PLA Basic Nightglow Blue
- `r3d_pla_plabasicoats_1000_175_c` — PLA Basic Oats
- `r3d_pla_plabasicorange_1000_175_c` — PLA Basic Orange
- `r3d_pla_plabasicpersimmonyellow_1000_175_c` — PLA Basic Persimmon Yellow
- `r3d_pla_plabasicpurple_1000_175_c` — PLA Basic Purple
- `r3d_pla_plabasicred_1000_175_c` — PLA Basic Red
- `r3d_pla_plabasictransparent_1000_175_c` — PLA Basic Transparent
- `r3d_pla_plabasicwhite_1000_175_c` — PLA Basic White
- `r3d_pla_rainbowplarainbowone_1000_175_p` — Rainbow PLA Rainbow one
- `r3d_pla_rainbowplarainbowone_1000_175_c` — Rainbow PLA Rainbow one
- `r3d_pla_silkdual-colorplaautumn_1000_175_p` — Silk Dual-Color PLA Autumn
- `r3d_pla_silkdual-colorplablack-blue_1000_175_p` — Silk Dual-Color PLA Black-Blue
- `r3d_pla_silkdual-colorplablack-red_1000_175_p` — Silk Dual-Color PLA Black-red
- `r3d_pla_silkdual-colorplablueorange_1000_175_p` — Silk Dual-Color PLA Blue Orange
- `r3d_pla_silkdual-colorplablue-green_1000_175_p` — Silk Dual-Color PLA Blue-green
- `r3d_pla_silkdual-colorplagreen-orange_1000_175_p` — Silk Dual-Color PLA Green-Orange
- `r3d_pla_silkdual-colorplaorange-bronze_1000_175_p` — Silk Dual-Color PLA Orange-Bronze
- `r3d_pla_silkdual-colorplarosered-gold_1000_175_p` — Silk Dual-Color PLA Rose Red-Gold
- `r3d_pla_silkdual-colorplasilkblack-green_1000_175_p` — Silk Dual-Color PLA Silk Black-Green
- `r3d_pla_silkdual-colorplasilkblack-purple_1000_175_p` — Silk Dual-Color PLA Silk Black-Purple
- `r3d_pla_silkdual-colorplaautumn_1000_175_c` — Silk Dual-Color PLA Autumn
- `r3d_pla_silkdual-colorplablack-blue_1000_175_c` — Silk Dual-Color PLA Black-Blue
- `r3d_pla_silkdual-colorplablack-red_1000_175_c` — Silk Dual-Color PLA Black-red
- `r3d_pla_silkdual-colorplablueorange_1000_175_c` — Silk Dual-Color PLA Blue Orange
- `r3d_pla_silkdual-colorplablue-green_1000_175_c` — Silk Dual-Color PLA Blue-green
- `r3d_pla_silkdual-colorplagreen-orange_1000_175_c` — Silk Dual-Color PLA Green-Orange
- `r3d_pla_silkdual-colorplaorange-bronze_1000_175_c` — Silk Dual-Color PLA Orange-Bronze
- `r3d_pla_silkdual-colorplarosered-gold_1000_175_c` — Silk Dual-Color PLA Rose Red-Gold
- `r3d_pla_silkdual-colorplasilkblack-green_1000_175_c` — Silk Dual-Color PLA Silk Black-Green
- `r3d_pla_silkdual-colorplasilkblack-purple_1000_175_c` — Silk Dual-Color PLA Silk Black-Purple
- `r3d_pla_silkplacherryblossoms_1000_175_p` — Silk PLA Cherry Blossoms
- `r3d_pla_silkplacopper_1000_175_p` — Silk PLA Copper
- `r3d_pla_silkplagold_1000_175_p` — Silk PLA Gold
- `r3d_pla_silkplagreen_1000_175_p` — Silk PLA Green
- `r3d_pla_silkplalemonyellow_1000_175_p` — Silk PLA Lemon Yellow
- `r3d_pla_silkplaorange_1000_175_p` — Silk PLA Orange
- `r3d_pla_silkplapink_1000_175_p` — Silk PLA Pink
- `r3d_pla_silkplarainbowtwo_1000_175_p` — Silk PLA Rainbow Two
- `r3d_pla_silkplasilkblue_1000_175_p` — Silk PLA Silk Blue
- `r3d_pla_silkplasilkbronze_1000_175_p` — Silk PLA Silk Bronze
- `r3d_pla_silkplasilkred_1000_175_p` — Silk PLA Silk Red
- `r3d_pla_silkplasilksilver_1000_175_p` — Silk PLA Silk Silver
- `r3d_pla_silkplawhite_1000_175_p` — Silk PLA White
- `r3d_pla_silkplacherryblossoms_1000_175_c` — Silk PLA Cherry Blossoms
- `r3d_pla_silkplacopper_1000_175_c` — Silk PLA Copper
- `r3d_pla_silkplagold_1000_175_c` — Silk PLA Gold
- `r3d_pla_silkplagreen_1000_175_c` — Silk PLA Green
- `r3d_pla_silkplalemonyellow_1000_175_c` — Silk PLA Lemon Yellow
- `r3d_pla_silkplaorange_1000_175_c` — Silk PLA Orange
- `r3d_pla_silkplapink_1000_175_c` — Silk PLA Pink
- `r3d_pla_silkplarainbowtwo_1000_175_c` — Silk PLA Rainbow Two
- `r3d_pla_silkplasilkblue_1000_175_c` — Silk PLA Silk Blue
- `r3d_pla_silkplasilkbronze_1000_175_c` — Silk PLA Silk Bronze
- `r3d_pla_silkplasilkred_1000_175_c` — Silk PLA Silk Red
- `r3d_pla_silkplasilksilver_1000_175_c` — Silk PLA Silk Silver
- `r3d_pla_silkplawhite_1000_175_c` — Silk PLA White
- `r3d_pla_silktri-colorplablue-purple-black_1000_175_p` — Silk Tri-Color PLA Blue-Purple-Black
- `r3d_pla_silktri-colorplagreenpurplecopper_1000_175_p` — Silk Tri-Color PLA Green Purple Copper
- `r3d_pla_silktri-colorplared-gold-black_1000_175_p` — Silk Tri-Color PLA Red-gold-black
- `r3d_pla_silktri-colorplarosered-purple-silver_1000_175_p` — Silk Tri-Color PLA Rose Red-Purple-Silver
- `r3d_pla_silktri-colorplablue-purple-black_1000_175_c` — Silk Tri-Color PLA Blue-Purple-Black
- `r3d_pla_silktri-colorplagreenpurplecopper_1000_175_c` — Silk Tri-Color PLA Green Purple Copper
- `r3d_pla_silktri-colorplared-gold-black_1000_175_c` — Silk Tri-Color PLA Red-gold-black
- `r3d_pla_silktri-colorplarosered-purple-silver_1000_175_c` — Silk Tri-Color PLA Rose Red-Purple-Silver
- `r3d_pla_sparkleplatwinklingred_1000_175_p` — Sparkle PLA Twinkling Red
- `r3d_pla_sparkleplatwinklingred_1000_175_c` — Sparkle PLA Twinkling Red
- `r3d_pla_translucentplablue_1000_175_p` — Translucent PLA Blue
- `r3d_pla_translucentplared_1000_175_p` — Translucent PLA Red
- `r3d_pla_translucentplablue_1000_175_c` — Translucent PLA Blue
- `r3d_pla_translucentplared_1000_175_c` — Translucent PLA Red
- `r3d_pla_uvcolorchangeplabluetopink_1000_175_p` — UV Color Change PLA Blue to Pink
- `r3d_pla_uvcolorchangeplabluetopink_1000_175_c` — UV Color Change PLA Blue to Pink
- `r3d_pla+_plaprohighspeedmatteavacadogreen_1000_175_p` — PLA Pro High Speed Matte Avacado Green
- `r3d_pla+_plaprohighspeedmattebeige_1000_175_p` — PLA Pro High Speed Matte Beige
- `r3d_pla+_plaprohighspeedmatteterracotta_1000_175_p` — PLA Pro High Speed Matte Terracotta
- `r3d_pla+_plaprohighspeedmatteavacadogreen_1000_175_c` — PLA Pro High Speed Matte Avacado Green
- `r3d_pla+_plaprohighspeedmattebeige_1000_175_c` — PLA Pro High Speed Matte Beige
- `r3d_pla+_plaprohighspeedmatteterracotta_1000_175_c` — PLA Pro High Speed Matte Terracotta
- `r3d_pla+_plaprohighspeedblack_1000_175_p` — PLA Pro High Speed Black
- `r3d_pla+_plaprohighspeedcoffee_1000_175_p` — PLA Pro High Speed Coffee
- `r3d_pla+_plaprohighspeedemerald_1000_175_p` — PLA Pro High Speed Emerald
- `r3d_pla+_plaprohighspeednavy_1000_175_p` — PLA Pro High Speed Navy
- `r3d_pla+_plaprohighspeedred_1000_175_p` — PLA Pro High Speed Red
- `r3d_pla+_plaprohighspeedskin_1000_175_p` — PLA Pro High Speed Skin
- `r3d_pla+_plaprohighspeedwhite_1000_175_p` — PLA Pro High Speed White
- `r3d_pla+_plaprohighspeedblack_1000_175_c` — PLA Pro High Speed Black
- `r3d_pla+_plaprohighspeedcoffee_1000_175_c` — PLA Pro High Speed Coffee
- `r3d_pla+_plaprohighspeedemerald_1000_175_c` — PLA Pro High Speed Emerald
- `r3d_pla+_plaprohighspeednavy_1000_175_c` — PLA Pro High Speed Navy
- `r3d_pla+_plaprohighspeedred_1000_175_c` — PLA Pro High Speed Red
- `r3d_pla+_plaprohighspeedskin_1000_175_c` — PLA Pro High Speed Skin
- `r3d_pla+_plaprohighspeedwhite_1000_175_c` — PLA Pro High Speed White
- `r3d_pla+_plapromatteashgrey_1000_175_p` — PLA Pro Matte Ash Grey
- `r3d_pla+_plapromatteashgrey_1000_175_c` — PLA Pro Matte Ash Grey
- `r3d_pla+_plaprolatte_1000_175_p` — PLA Pro Latte
- `r3d_pla+_plaprored_1000_175_p` — PLA Pro Red
- `r3d_pla+_plaprolatte_1000_175_c` — PLA Pro Latte
- `r3d_pla+_plaprored_1000_175_c` — PLA Pro Red
- `r3d_tpu_tpublack_1000_175_p` — TPU Black
- `r3d_tpu_tpuwhite_1000_175_p` — TPU White
- `r3d_tpu_tpublack_1000_175_c` — TPU Black
- `r3d_tpu_tpuwhite_1000_175_c` — TPU White
- `r3d_petg-gf_petg-gfassortedcolors(shopeelisting)_1000_175_u` — PETG-GF Assorted Colors (Shopee listing)
- `r3d_tpu-95a_tpu95aassortedcolors(shopeelisting)_1000_175_u` — TPU 95A Assorted Colors (Shopee listing)
