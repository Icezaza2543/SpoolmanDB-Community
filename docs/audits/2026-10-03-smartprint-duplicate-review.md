# smartprint duplicate migration review

Base `fd47548ead0e74b8373dfa39f9ea7b73835c9a4d`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `2e76833ef84198903eaf04089838ce09591e6010ccfaf18671296e1ce4cf7500`.

## Authorization and result

{"groups": 1, "approved_groups": 0, "retired": 0, "deferred": 1, "hard_stops": 0, "before_count": 51701, "after_count": 51701, "brand_before": 175, "brand_after": 175, "registry_before": 1733, "registry_after": 1733, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

TPUGray/Grey tieHEX7A7A7A/808080 not bound sameSKU; defer. No resellerEAN, density guess or packaging/tare change.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. Future reviewed retirements would not redirect external catalog lookups automatically.

## Current first-party evidence

- {"url": "https://b2b.smartprint24.com/produkty/filaments?page=16&perpage=15&so=Code", "note": "CataloglinksGrayFG-S124-E1 but exactpage unavailable."}
- {"url": "https://b2b.smartprint24.com/products/filaments/tpu/fg-s125-e1-fg-s125-e1-tpu-yellow-_-smart-print.html", "nozzle": [200, 230], "bed": [50, 60], "note": "ExactTPU95A familyYellow, not bothGray/GreySKU proof."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### SP001: dup-30bb854d9240b3a016777f8b6dfa75b16c0f1bf737f94d6e1f5362eb72b3c299

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`smartprint_tpu_tpugray_1000_175_p`|`TPU {color_name}`|`Gray`|{"source_file": "smartprint.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|
|`smartprint_tpu_tpugrey_1000_175_p`|`TPU {color_name}`|`Grey`|{"source_file": "smartprint.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "smartprint_tpu_tpugray_1000_175_p": "7A7A7A",
    "smartprint_tpu_tpugrey_1000_175_p": "808080"
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

- `smartprint_pla+_plaplusblack_1000_175_p` — PLA Plus Black
- `smartprint_pla+_plapluswhite_1000_175_p` — PLA Plus White
- `smartprint_pla+_plaplusgrey_1000_175_p` — PLA Plus Grey
- `smartprint_pla+_plaplusblue_1000_175_p` — PLA Plus Blue
- `smartprint_pla+_plaplusred_1000_175_p` — PLA Plus Red
- `smartprint_pla+_plaplusyellow_1000_175_p` — PLA Plus Yellow
- `smartprint_pla+_plaplusorange_1000_175_p` — PLA Plus Orange
- `smartprint_pla+_plaplusgreen_1000_175_p` — PLA Plus Green
- `smartprint_pla+_plaplusnatural_1000_175_p` — PLA Plus Natural
- `smartprint_pla+_plapluspink_1000_175_p` — PLA Plus Pink
- `smartprint_petg_petgblack_1000_175_p` — PETG Black
- `smartprint_petg_petgwhite_1000_175_p` — PETG White
- `smartprint_petg_petgnatural_1000_175_p` — PETG Natural
- `smartprint_petg_petgblue_1000_175_p` — PETG Blue
- `smartprint_petg_petgred_1000_175_p` — PETG Red
- `smartprint_petg_petgbrown_1000_175_p` — PETG Brown
- `smartprint_petg_petgcyan_1000_175_p` — PETG Cyan
- `smartprint_petg_petggreen_1000_175_p` — PETG Green
- `smartprint_petg_petgoak_1000_175_p` — PETG Oak
- `smartprint_petg_petgolivegreen_1000_175_p` — PETG Olive Green
- `smartprint_abs_absplusblack_1000_175_p` — ABS Plus Black
- `smartprint_abs_abspluswhite_1000_175_p` — ABS Plus White
- `smartprint_abs_absplusblue_1000_175_p` — ABS Plus Blue
- `smartprint_abs_absplusred_1000_175_p` — ABS Plus Red
- `smartprint_abs_absplusyellow_1000_175_p` — ABS Plus Yellow
- `smartprint_abs_absplusbrown_1000_175_p` — ABS Plus Brown
- `smartprint_abs_absplusorange_1000_175_p` — ABS Plus Orange
- `smartprint_tpu_tpublack_1000_175_p` — TPU Black
- `smartprint_tpu_tpuwhite_1000_175_p` — TPU White
- `smartprint_tpu_tpured_1000_175_p` — TPU Red
- `smartprint_tpu_tpublue_1000_175_p` — TPU Blue
- `smartprint_tpu_tpugreen_1000_175_p` — TPU Green
- `smartprint_tpu_tpuorange_1000_175_p` — TPU Orange
- `smartprint_tpu_tputransparent_1000_175_p` — TPU Transparent
- `smartprint_abs_absblack_1000_175_p` — ABS Black
- `smartprint_abs_absblue_1000_175_p` — ABS Blue
- `smartprint_abs_absbrown_1000_175_p` — ABS Brown
- `smartprint_asa_asablack_1000_175_p` — ASA Black
- `smartprint_asa_asablue_1000_175_p` — ASA Blue
- `smartprint_asa_asaglassfiberblack_1000_175_p` — ASA glass fiber black
- `smartprint_asa_asagray_1000_175_p` — ASA Gray
- `smartprint_asa_asagreen_1000_175_p` — ASA Green
- `smartprint_asa_asared_1000_175_p` — ASA Red
- `smartprint_asa_asasilver_1000_175_p` — ASA Silver
- `smartprint_asa_asawhite_1000_175_p` — ASA White
- `smartprint_pa12_pa12-cf15black_1000_175_p` — PA12-CF15 Black
- `smartprint_petg_petgtransparentblue_1000_175_p` — PETG Transparent Blue
- `smartprint_petg_petgtransparentclear_1000_175_p` — PETG Transparent Clear
- `smartprint_petg_petgtransparentgreen_1000_175_p` — PETG Transparent Green
- `smartprint_petg_petgtransparentred_1000_175_p` — PETG Transparent Red
- `smartprint_petg_petgtransparentyellow_1000_175_p` — PETG Transparent yellow
- `smartprint_pla_hs-plablack_1000_175_p` — HS-PLA Black
- `smartprint_pla_hs-plablue_1000_175_p` — HS-PLA Blue
- `smartprint_pla_hs-plagray_1000_175_p` — HS-PLA Gray
- `smartprint_pla_hs-plagreen_1000_175_p` — HS-PLA Green
- `smartprint_pla_hs-plaorange_1000_175_p` — HS-PLA Orange
- `smartprint_pla_hs-plared_1000_175_p` — HS-PLA Red
- `smartprint_pla_hs-platransparent_1000_175_p` — HS-PLA Transparent
- `smartprint_pla_hs-plawhite_1000_175_p` — HS-PLA White
- `smartprint_pla_hs-playellow_1000_175_p` — HS-PLA Yellow
- `smartprint_pla_plaapplegreen_1000_175_p` — PLA Apple Green
- `smartprint_pla_plablack_1000_175_p` — PLA Black
- `smartprint_pla_plablue_1000_175_p` — PLA Blue
- `smartprint_pla_plabrown_1000_175_p` — PLA Brown
- `smartprint_pla_plachocolate_1000_175_p` — PLA Chocolate
- `smartprint_pla_placlaret_1000_175_p` — PLA Claret
- `smartprint_pla_placyan_1000_175_p` — PLA Cyan
- `smartprint_pla_plagradient_1000_175_p` — PLA Gradient
- `smartprint_pla_plagrassgreen_1000_175_p` — PLA Grass Green
- `smartprint_pla_plagray_1000_175_p` — PLA Gray
- `smartprint_pla_plagreen_1000_175_p` — PLA Green
- `smartprint_pla_plalightbrown_1000_175_p` — PLA Light brown
- `smartprint_pla_plamagenta_1000_175_p` — PLA Magenta
- `smartprint_pla_planavyblue_1000_175_p` — PLA Navy Blue
- `smartprint_pla_planewpink_1000_175_p` — PLA New Pink
- `smartprint_pla_plaolivegreen_1000_175_p` — PLA Olive Green
- `smartprint_pla_plaorange_1000_175_p` — PLA Orange
- `smartprint_pla_plapastelblue_1000_175_p` — PLA Pastel blue
- `smartprint_pla_plaplum_1000_175_p` — PLA Plum
- `smartprint_pla_plapurple_1000_175_p` — PLA Purple
- `smartprint_pla_plaraspberry_1000_175_p` — PLA Raspberry
- `smartprint_pla_plared_1000_175_p` — PLA Red
- `smartprint_pla_plasilver_1000_175_p` — PLA Silver
- `smartprint_pla_plaskin_1000_175_p` — PLA Skin
- `smartprint_pla_platransparent_1000_175_p` — PLA Transparent
- `smartprint_pla_plawhite_1000_175_p` — PLA White
- `smartprint_pla_playellow_1000_175_p` — PLA Yellow
- `smartprint_pla_pla+black_1000_175_p` — PLA+ Black
- `smartprint_pla_pla+blue_1000_175_p` — PLA+ Blue
- `smartprint_pla_pla+brown_1000_175_p` — PLA+ Brown
- `smartprint_pla_pla+gray_1000_175_p` — PLA+ Gray
- `smartprint_pla_pla+green_1000_175_p` — PLA+ Green
- `smartprint_pla_pla+newpink_1000_175_p` — PLA+ New Pink
- `smartprint_pla_pla+orange_1000_175_p` — PLA+ Orange
- `smartprint_pla_pla+purple_1000_175_p` — PLA+ Purple
- `smartprint_pla_pla+red_1000_175_p` — PLA+ Red
- `smartprint_pla_pla+sandgold_1000_175_p` — PLA+ Sand Gold
- `smartprint_pla_pla+silver_1000_175_p` — PLA+ Silver
- `smartprint_pla_pla+transparent_1000_175_p` — PLA+ Transparent
- `smartprint_pla_pla+white_1000_175_p` — PLA+ White
- `smartprint_pla_pla+yellow_1000_175_p` — PLA+ Yellow
- `smartprint_pla_pla+black_5000_175_p` — PLA+ Black
- `smartprint_pla_pla+blue_5000_175_p` — PLA+ Blue
- `smartprint_pla_pla+brown_5000_175_p` — PLA+ Brown
- `smartprint_pla_pla+gray_5000_175_p` — PLA+ Gray
- `smartprint_pla_pla+green_5000_175_p` — PLA+ Green
- `smartprint_pla_pla+newpink_5000_175_p` — PLA+ New Pink
- `smartprint_pla_pla+orange_5000_175_p` — PLA+ Orange
- `smartprint_pla_pla+purple_5000_175_p` — PLA+ Purple
- `smartprint_pla_pla+red_5000_175_p` — PLA+ Red
- `smartprint_pla_pla+sandgold_5000_175_p` — PLA+ Sand Gold
- `smartprint_pla_pla+silver_5000_175_p` — PLA+ Silver
- `smartprint_pla_pla+transparent_5000_175_p` — PLA+ Transparent
- `smartprint_pla_pla+white_5000_175_p` — PLA+ White
- `smartprint_pla_pla+yellow_5000_175_p` — PLA+ Yellow
- `smartprint_pla_pla-cfblack_1000_175_p` — PLA-CF Black
- `smartprint_pla_pla-cfblue_1000_175_p` — PLA-CF Blue
- `smartprint_pla_pla-cfgray_1000_175_p` — PLA-CF Gray
- `smartprint_pla_pla-cfred_1000_175_p` — PLA-CF Red
- `smartprint_pla_plagalaxyblack_1000_175_p` — PLA Galaxy Black
- `smartprint_pla_plagalaxyblue_1000_175_p` — PLA Galaxy Blue
- `smartprint_pla_plaglowblue_1000_175_p` — PLA Glow Blue
- `smartprint_pla_plaglowgreen_1000_175_p` — PLA Glow Green
- `smartprint_pla_plaglowyellow_1000_175_p` — PLA Glow Yellow
- `smartprint_pla_plamarblebrickred_1000_175_p` — PLA Marble Brick Red
- `smartprint_pla_plamarbleconcrete_1000_175_p` — PLA Marble Concrete
- `smartprint_pla_plamarblemarble_1000_175_p` — PLA Marble Marble
- `smartprint_pla_plamatteblack_1000_175_p` — PLA Matte Black
- `smartprint_pla_plamatteblue_1000_175_p` — PLA Matte Blue
- `smartprint_pla_plamattegray_1000_175_p` — PLA Matte Gray
- `smartprint_pla_plamattered_1000_175_p` — PLA Matte Red
- `smartprint_pla_plamattewhite_1000_175_p` — PLA Matte White
- `smartprint_pla_plametablack_1000_175_p` — PLA Meta Black
- `smartprint_pla_plametablue_1000_175_p` — PLA Meta Blue
- `smartprint_pla_plametagray_1000_175_p` — PLA Meta Gray
- `smartprint_pla_plametagreen_1000_175_p` — PLA Meta Green
- `smartprint_pla_plametared_1000_175_p` — PLA Meta Red
- `smartprint_pla_plametawhite_1000_175_p` — PLA Meta White
- `smartprint_pla_plametayellow_1000_175_p` — PLA Meta Yellow
- `smartprint_pla_plasilkblack_1000_175_p` — PLA Silk Black
- `smartprint_pla_plasilkbrass_1000_175_p` — PLA Silk Brass
- `smartprint_pla_plasilkcopper_1000_175_p` — PLA Silk Copper
- `smartprint_pla_plasilkglamour_1000_175_p` — PLA Silk Glamour
- `smartprint_pla_plasilkgold_1000_175_p` — PLA Silk Gold
- `smartprint_pla_plasilkgreen_1000_175_p` — PLA Silk Green
- `smartprint_pla_plasilkpurple_1000_175_p` — PLA Silk Purple
- `smartprint_pla_plasilkrainbow_1000_175_p` — PLA Silk Rainbow
- `smartprint_pla_plasilksilver_1000_175_p` — PLA Silk Silver
- `smartprint_pla_plasilktransparent_1000_175_p` — PLA Silk Transparent
- `smartprint_pla_plasilkwhite_1000_175_p` — PLA Silk White
- `smartprint_pla_plasilkyellow_1000_175_p` — PLA Silk Yellow
- `smartprint_pla_plasilkdualblackblue_1000_175_p` — PLA Silk Dual Black Blue
- `smartprint_pla_plasilkdualblackgold_1000_175_p` — PLA Silk Dual Black Gold
- `smartprint_pla_plasilkdualblackgreen_1000_175_p` — PLA Silk Dual Black Green
- `smartprint_pla_plasilkdualblackpurple_1000_175_p` — PLA Silk Dual Black Purple
- `smartprint_pla_plasilkdualoceansembrace_1000_175_p` — PLA Silk Dual Oceans Embrace
- `smartprint_pla_plasilkdualpinkgold_1000_175_p` — PLA Silk Dual Pink Gold
- `smartprint_pla_plasilkdualredblue_1000_175_p` — PLA Silk Dual Red Blue
- `smartprint_pla_plasilkdualredgold_1000_175_p` — PLA Silk Dual Red Gold
- `smartprint_pla_plasilkdualtwilightserenity_1000_175_p` — PLA Silk Dual Twilight Serenity
- `smartprint_pla_plasilktriarmy_1000_175_p` — PLA Silk Tri Army
- `smartprint_pla_plasilktriblackgoldpurple_1000_175_p` — PLA Silk Tri Black Gold Purple
- `smartprint_pla_plasilktribluegreenpurple_1000_175_p` — PLA Silk Tri Blue Green Purple
- `smartprint_pla_plasilktribluepurpleblack_1000_175_p` — PLA Silk Tri Blue Purple Black
- `smartprint_pla_plasilktriorangebluegreen_1000_175_p` — PLA Silk Tri Orange Blue Green
- `smartprint_pla_plasilktriredbluegreen_1000_175_p` — PLA Silk Tri Red Blue Green
- `smartprint_pla_plasilktriredyellowgreen_1000_175_p` — PLA Silk Tri Red Yellow Green
- `smartprint_pla_plasilktriroyalblossom_1000_175_p` — PLA Silk Tri Royal Blossom
- `smartprint_pla_plasilktristormswhisper_1000_175_p` — PLA Silk Tri Storms Whisper
- `smartprint_pla_plasilktrisunsethorizon_1000_175_p` — PLA Silk Tri Sunset Horizon
- `smartprint_pla_plawoodblackwalnut_1000_175_p` — PLA Wood Black Walnut
- `smartprint_pla_plawoodmaple_1000_175_p` — PLA Wood Maple
- `smartprint_pla_plawoodwood_1000_175_p` — PLA Wood Wood
