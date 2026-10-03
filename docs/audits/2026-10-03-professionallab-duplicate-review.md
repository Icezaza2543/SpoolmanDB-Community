# professionallab duplicate migration review

Base `9666e3186385f4d12bf4dca788a8799128455b0c`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `f578932a3f10c66c1a5efb4a207b202e61286199f416f201fe22bf27e49a96d3`.

## Authorization and result

{"groups": 1, "approved_groups": 0, "retired": 0, "deferred": 1, "hard_stops": 0, "before_count": 51701, "after_count": 51701, "brand_before": 152, "brand_after": 152, "registry_before": 1733, "registry_after": 1733, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Gray/Grey tieHEXAAAAAA/808080, no sameSKU; defer. StandardSilver evidence not bound to Gray; PLA+/MatteGray distinct, not imported.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. Future reviewed retirements would not redirect external catalog lookups automatically.

## Current first-party evidence

- {"url": "https://b2b.smartprint24.com/products/filaments/pla/pla-standard/fg-p67-e1-fg-p67-e1-pla-silver-_-prof-lab.html", "nozzle": [185, 215], "bed": [25, 60], "note": "StandardPLA Silver, not proven GraySKU."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### PL001: dup-f19051aa2dcd18ae24e90b53dd45e7af7ab84c0d9c04e662c3b8d46c0443e2aa

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`professionallab_pla_plagray_1000_175_p`|`PLA {color_name}`|`Gray`|{"source_file": "professionallab.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|
|`professionallab_pla_plagrey_1000_175_p`|`PLA {color_name}`|`Grey`|{"source_file": "professionallab.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "professionallab_pla_plagray_1000_175_p": "AAAAAA",
    "professionallab_pla_plagrey_1000_175_p": "808080"
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

- `professionallab_pla_plablack_1000_175_p` — PLA Black
- `professionallab_pla_plawhite_1000_175_p` — PLA White
- `professionallab_pla_plablue_1000_175_p` — PLA Blue
- `professionallab_pla_plared_1000_175_p` — PLA Red
- `professionallab_pla_playellow_1000_175_p` — PLA Yellow
- `professionallab_pla_plawaterblue_1000_175_p` — PLA Water Blue
- `professionallab_pla_plasilver_1000_175_p` — PLA Silver
- `professionallab_pla_plagreen_1000_175_p` — PLA Green
- `professionallab_pla_plaapplegreen_1000_175_p` — PLA Apple Green
- `professionallab_pla_plabrown_1000_175_p` — PLA Brown
- `professionallab_pla_plachocolate_1000_175_p` — PLA Chocolate
- `professionallab_pla_placlaret_1000_175_p` — PLA Claret
- `professionallab_pla_placyan_1000_175_p` — PLA Cyan
- `professionallab_pla_plagradient_1000_175_p` — PLA Gradient
- `professionallab_pla_plagrassgreen_1000_175_p` — PLA Grass Green
- `professionallab_pla_plalightbrown_1000_175_p` — PLA Light brown
- `professionallab_pla_plamagenta_1000_175_p` — PLA Magenta
- `professionallab_pla_planavyblue_1000_175_p` — PLA Navy Blue
- `professionallab_pla_planewpink_1000_175_p` — PLA New Pink
- `professionallab_pla_plaolivegreen_1000_175_p` — PLA Olive Green
- `professionallab_pla_plaorange_1000_175_p` — PLA Orange
- `professionallab_pla_plalightpastelblue_1000_175_p` — PLA Light Pastel Blue
- `professionallab_pla_plaplum_1000_175_p` — PLA Plum
- `professionallab_pla_plapurple_1000_175_p` — PLA Purple
- `professionallab_pla_plaraspberry_1000_175_p` — PLA Raspberry
- `professionallab_pla_plaskin_1000_175_p` — PLA Skin
- `professionallab_pla_platransparent_1000_175_p` — PLA Transparent
- `professionallab_pla_plasandgold_1000_175_p` — PLA Sand Gold
- `professionallab_petg_petgblack_1000_175_p` — PETG Black
- `professionallab_petg_petgwhite_1000_175_p` — PETG White
- `professionallab_petg_petgblue_1000_175_p` — PETG Blue
- `professionallab_petg_petgred_1000_175_p` — PETG Red
- `professionallab_petg_petggrey_1000_175_p` — PETG Grey
- `professionallab_petg_petgtransparent_1000_175_p` — PETG Transparent
- `professionallab_petg_petgbrown_1000_175_p` — PETG Brown
- `professionallab_petg_petggreen_1000_175_p` — PETG Green
- `professionallab_petg_petgpink_1000_175_p` — PETG Pink
- `professionallab_petg_petgyellow_1000_175_p` — PETG Yellow
- `professionallab_abs_absblack_1000_175_p` — ABS Black
- `professionallab_abs_absblue_1000_175_p` — ABS Blue
- `professionallab_abs_absbrown_1000_175_p` — ABS Brown
- `professionallab_asa_asablack_1000_175_p` — ASA Black
- `professionallab_asa_asablue_1000_175_p` — ASA Blue
- `professionallab_asa_asaglassfiberblack_1000_175_p` — ASA glass fiber black
- `professionallab_asa_asagray_1000_175_p` — ASA Gray
- `professionallab_asa_asagreen_1000_175_p` — ASA Green
- `professionallab_asa_asared_1000_175_p` — ASA Red
- `professionallab_asa_asasilver_1000_175_p` — ASA Silver
- `professionallab_asa_asawhite_1000_175_p` — ASA White
- `professionallab_pa12_pa12-cf15black_1000_175_p` — PA12-CF15 Black
- `professionallab_petg_petg-cfblack_1000_175_p` — PETG-CF Black
- `professionallab_petg_petg-cfblue_1000_175_p` — PETG-CF Blue
- `professionallab_petg_petg-cfgreen_1000_175_p` — PETG-CF Green
- `professionallab_petg_petg-cfgrey_1000_175_p` — PETG-CF Grey
- `professionallab_petg_petgmattebeige_1000_175_p` — PETG Matte Beige
- `professionallab_petg_petgmatteblack_1000_175_p` — PETG Matte Black
- `professionallab_petg_petgmatteblue_1000_175_p` — PETG Matte Blue
- `professionallab_petg_petgmattebrown_1000_175_p` — PETG Matte Brown
- `professionallab_petg_petgmattedarkgreen_1000_175_p` — PETG Matte Dark Green
- `professionallab_petg_petgmattegreen_1000_175_p` — PETG Matte Green
- `professionallab_petg_petgmattered_1000_175_p` — PETG Matte Red
- `professionallab_petg_petgmatteyellow_1000_175_p` — PETG Matte Yellow
- `professionallab_petg_petgtransparentblue_1000_175_p` — PETG Transparent Blue
- `professionallab_petg_petgtransparentclear_1000_175_p` — PETG Transparent Clear
- `professionallab_petg_petgtransparentgreen_1000_175_p` — PETG Transparent Green
- `professionallab_petg_petgtransparentred_1000_175_p` — PETG Transparent Red
- `professionallab_petg_petgtransparentyellow_1000_175_p` — PETG Transparent yellow
- `professionallab_pla_hs-plablack_1000_175_p` — HS-PLA Black
- `professionallab_pla_hs-plablue_1000_175_p` — HS-PLA Blue
- `professionallab_pla_hs-plagray_1000_175_p` — HS-PLA Gray
- `professionallab_pla_hs-plagreen_1000_175_p` — HS-PLA Green
- `professionallab_pla_hs-plaorange_1000_175_p` — HS-PLA Orange
- `professionallab_pla_hs-plared_1000_175_p` — HS-PLA Red
- `professionallab_pla_hs-platransparent_1000_175_p` — HS-PLA Transparent
- `professionallab_pla_hs-plawhite_1000_175_p` — HS-PLA White
- `professionallab_pla_hs-playellow_1000_175_p` — HS-PLA Yellow
- `professionallab_pla_pla-cfblack_1000_175_p` — PLA-CF Black
- `professionallab_pla_pla-cfblue_1000_175_p` — PLA-CF Blue
- `professionallab_pla_pla-cfgray_1000_175_p` — PLA-CF Gray
- `professionallab_pla_pla-cfgreen_1000_175_p` — PLA-CF Green
- `professionallab_pla_pla-cfred_1000_175_p` — PLA-CF Red
- `professionallab_pla_plagalaxyblack_1000_175_p` — PLA Galaxy Black
- `professionallab_pla_plagalaxyblue_1000_175_p` — PLA Galaxy Blue
- `professionallab_pla_plaglowblue_1000_175_p` — PLA Glow Blue
- `professionallab_pla_plaglowgreen_1000_175_p` — PLA Glow Green
- `professionallab_pla_plaglowyellow_1000_175_p` — PLA Glow Yellow
- `professionallab_pla_plamarblebrickred_1000_175_p` — PLA Marble Brick Red
- `professionallab_pla_plamarbleconcrete_1000_175_p` — PLA Marble Concrete
- `professionallab_pla_plamarblemarble_1000_175_p` — PLA Marble Marble
- `professionallab_pla_plamatteblack_1000_175_p` — PLA Matte Black
- `professionallab_pla_plamatteblue_1000_175_p` — PLA Matte Blue
- `professionallab_pla_plamattegray_1000_175_p` — PLA Matte Gray
- `professionallab_pla_plamattered_1000_175_p` — PLA Matte Red
- `professionallab_pla_plamattewhite_1000_175_p` — PLA Matte White
- `professionallab_pla_plametablack_1000_175_p` — PLA Meta Black
- `professionallab_pla_plametablue_1000_175_p` — PLA Meta Blue
- `professionallab_pla_plametagray_1000_175_p` — PLA Meta Gray
- `professionallab_pla_plametagreen_1000_175_p` — PLA Meta Green
- `professionallab_pla_plametared_1000_175_p` — PLA Meta Red
- `professionallab_pla_plametawhite_1000_175_p` — PLA Meta White
- `professionallab_pla_plametayellow_1000_175_p` — PLA Meta Yellow
- `professionallab_pla_plapastelblue_1000_175_p` — PLA Pastel Blue
- `professionallab_pla_plapastelgreen_1000_175_p` — PLA Pastel Green
- `professionallab_pla_plapastelorange_1000_175_p` — PLA Pastel Orange
- `professionallab_pla_plapastelpink_1000_175_p` — PLA Pastel Pink
- `professionallab_pla_plapastelpurple_1000_175_p` — PLA Pastel Purple
- `professionallab_pla_plapastelraspberry_1000_175_p` — PLA Pastel Raspberry
- `professionallab_pla_plapastelyellow_1000_175_p` — PLA Pastel Yellow
- `professionallab_pla_plasilkblack_1000_175_p` — PLA Silk Black
- `professionallab_pla_plasilkbrass_1000_175_p` — PLA Silk Brass
- `professionallab_pla_plasilkcopper_1000_175_p` — PLA Silk Copper
- `professionallab_pla_plasilkglamour_1000_175_p` — PLA Silk Glamour
- `professionallab_pla_plasilkgold_1000_175_p` — PLA Silk Gold
- `professionallab_pla_plasilkgreen_1000_175_p` — PLA Silk Green
- `professionallab_pla_plasilkpurple_1000_175_p` — PLA Silk Purple
- `professionallab_pla_plasilkrainbow_1000_175_p` — PLA Silk Rainbow
- `professionallab_pla_plasilksilver_1000_175_p` — PLA Silk Silver
- `professionallab_pla_plasilktransparent_1000_175_p` — PLA Silk Transparent
- `professionallab_pla_plasilkwhite_1000_175_p` — PLA Silk White
- `professionallab_pla_plasilkyellow_1000_175_p` — PLA Silk Yellow
- `professionallab_pla_plasilkdualblackblue_1000_175_p` — PLA Silk Dual Black Blue
- `professionallab_pla_plasilkdualblackgold_1000_175_p` — PLA Silk Dual Black Gold
- `professionallab_pla_plasilkdualblackgreen_1000_175_p` — PLA Silk Dual Black Green
- `professionallab_pla_plasilkdualblackpurple_1000_175_p` — PLA Silk Dual Black Purple
- `professionallab_pla_plasilkdualoceansembrace_1000_175_p` — PLA Silk Dual Oceans Embrace
- `professionallab_pla_plasilkdualpinkgold_1000_175_p` — PLA Silk Dual Pink Gold
- `professionallab_pla_plasilkdualredblue_1000_175_p` — PLA Silk Dual Red Blue
- `professionallab_pla_plasilkdualredgold_1000_175_p` — PLA Silk Dual Red Gold
- `professionallab_pla_plasilkdualtwilightserenity_1000_175_p` — PLA Silk Dual Twilight Serenity
- `professionallab_pla_plasilktriarmy_1000_175_p` — PLA Silk Tri Army
- `professionallab_pla_plasilktriblackgoldpurple_1000_175_p` — PLA Silk Tri Black Gold Purple
- `professionallab_pla_plasilktribluegreenpurple_1000_175_p` — PLA Silk Tri Blue Green Purple
- `professionallab_pla_plasilktribluepurpleblack_1000_175_p` — PLA Silk Tri Blue Purple Black
- `professionallab_pla_plasilktriorangebluegreen_1000_175_p` — PLA Silk Tri Orange Blue Green
- `professionallab_pla_plasilktriredbluegreen_1000_175_p` — PLA Silk Tri Red Blue Green
- `professionallab_pla_plasilktriredyellowgreen_1000_175_p` — PLA Silk Tri Red Yellow Green
- `professionallab_pla_plasilktriroyalblossom_1000_175_p` — PLA Silk Tri Royal Blossom
- `professionallab_pla_plasilktristormswhisper_1000_175_p` — PLA Silk Tri Storms Whisper
- `professionallab_pla_plasilktrisunsethorizon_1000_175_p` — PLA Silk Tri Sunset Horizon
- `professionallab_pla_plawoodblackwalnut_1000_175_p` — PLA Wood Black Walnut
- `professionallab_pla_plawoodmaple_1000_175_p` — PLA Wood Maple
- `professionallab_pla_plawoodwood_1000_175_p` — PLA Wood Wood
- `professionallab_tpu_tpublack_1000_175_p` — TPU Black
- `professionallab_tpu_tpublue_1000_175_p` — TPU Blue
- `professionallab_tpu_tpugray_1000_175_p` — TPU Gray
- `professionallab_tpu_tpugreen_1000_175_p` — TPU Green
- `professionallab_tpu_tpuorange_1000_175_p` — TPU Orange
- `professionallab_tpu_tpured_1000_175_p` — TPU Red
- `professionallab_tpu_tputransparent_1000_175_p` — TPU Transparent
- `professionallab_tpu_tpuwhite_1000_175_p` — TPU White
