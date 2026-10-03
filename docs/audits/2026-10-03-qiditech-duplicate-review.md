# qiditech duplicate migration review

Base `d089dffe307c1f17f572b2649888269ec1b21b8b`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `7ec29c4983ce5c045e8f04482e0aa27c0a625b06c0ad0d3951d0877b5d2b2144`.

## Authorization and result

{"groups": 8, "approved_groups": 8, "retired": 8, "deferred": 0, "hard_stops": 0, "before_count": 51756, "after_count": 51748, "brand_before": 156, "brand_after": 148, "registry_before": 1678, "registry_after": 1686, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Eight Rule1 strict ASA duplicates; both source families carry identical density1.07/nozzle240–280/bed100–110. Keep survivor metadata; tare conflicts remain unresolved and unchanged. No identifiers or transfers.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://us.qidi3d.com/products/qidi-asa-filament", "note": "Exact ordinary ASA line; not ASA-Aero or ASA-CF. Printing image not visually verified in this audit."}
- {"url": "https://cdn.shopify.com/s/files/1/0587/5282/7532/files/ASA_-6.jpg?v=1696937719", "note": "Image-only technical evidence; not claimed visually verified."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`qiditech_asa_asablack_1000_175_p`|`qiditech_asa_black_1000_175_p`|`qiditech.json::QIDI Tech::ASA {color_name}::ASA Black::ASA::1000::1.75::plastic::False`|
|`qiditech_asa_asablue_1000_175_p`|`qiditech_asa_blue_1000_175_p`|`qiditech.json::QIDI Tech::ASA {color_name}::ASA Blue::ASA::1000::1.75::plastic::False`|
|`qiditech_asa_asabrown_1000_175_p`|`qiditech_asa_brown_1000_175_p`|`qiditech.json::QIDI Tech::ASA {color_name}::ASA Brown::ASA::1000::1.75::plastic::False`|
|`qiditech_asa_asagray_1000_175_p`|`qiditech_asa_gray_1000_175_p`|`qiditech.json::QIDI Tech::ASA {color_name}::ASA Gray::ASA::1000::1.75::plastic::False`|
|`qiditech_asa_asagreen_1000_175_p`|`qiditech_asa_green_1000_175_p`|`qiditech.json::QIDI Tech::ASA {color_name}::ASA Green::ASA::1000::1.75::plastic::False`|
|`qiditech_asa_asared_1000_175_p`|`qiditech_asa_red_1000_175_p`|`qiditech.json::QIDI Tech::ASA {color_name}::ASA Red::ASA::1000::1.75::plastic::False`|
|`qiditech_asa_asawhite_1000_175_p`|`qiditech_asa_white_1000_175_p`|`qiditech.json::QIDI Tech::ASA {color_name}::ASA White::ASA::1000::1.75::plastic::False`|
|`qiditech_asa_asayellow_1000_175_p`|`qiditech_asa_yellow_1000_175_p`|`qiditech.json::QIDI Tech::ASA {color_name}::ASA Yellow::ASA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### QI001: dup-c96b7338ab3614b724770a4d78f9fbfa78d8d8761a0eb543ea757fb6e66eee55

Status: APPROVED; survivor `qiditech_asa_black_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`qiditech_asa_asablack_1000_175_p`|`ASA {color_name}`|`Black`|{"source_file": "qiditech.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`qiditech_asa_black_1000_175_p`|`{color_name}`|`Black`|{"source_file": "qiditech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "qiditech_asa_asablack_1000_175_p": 235,
    "qiditech_asa_black_1000_175_p": 245.0
  }
}
```

### QI002: dup-ea172a16c5de1b271f56105efef0d13643a49782c903dd0afe370cf9107bc29f

Status: APPROVED; survivor `qiditech_asa_blue_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`qiditech_asa_asablue_1000_175_p`|`ASA {color_name}`|`Blue`|{"source_file": "qiditech.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`qiditech_asa_blue_1000_175_p`|`{color_name}`|`Blue`|{"source_file": "qiditech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "qiditech_asa_asablue_1000_175_p": 235,
    "qiditech_asa_blue_1000_175_p": 245.0
  }
}
```

### QI003: dup-0203053f0160a3f7f2c50da20b9bcf36949548cc4b86168ba0cca1a4c7b78110

Status: APPROVED; survivor `qiditech_asa_brown_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`qiditech_asa_asabrown_1000_175_p`|`ASA {color_name}`|`Brown`|{"source_file": "qiditech.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`qiditech_asa_brown_1000_175_p`|`{color_name}`|`Brown`|{"source_file": "qiditech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "qiditech_asa_asabrown_1000_175_p": 235,
    "qiditech_asa_brown_1000_175_p": 245.0
  }
}
```

### QI004: dup-aa991f36c3e76b791bed5074c89c2304433f44b7baf5e30c5fa57deb3ebacc50

Status: APPROVED; survivor `qiditech_asa_gray_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`qiditech_asa_asagray_1000_175_p`|`ASA {color_name}`|`Gray`|{"source_file": "qiditech.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`qiditech_asa_gray_1000_175_p`|`{color_name}`|`Gray`|{"source_file": "qiditech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "qiditech_asa_asagray_1000_175_p": 235,
    "qiditech_asa_gray_1000_175_p": 245.0
  }
}
```

### QI005: dup-074b878aef7ab003c40158ec4d034f4ce4f89b98bc125284516e70f2385db97d

Status: APPROVED; survivor `qiditech_asa_green_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`qiditech_asa_asagreen_1000_175_p`|`ASA {color_name}`|`Green`|{"source_file": "qiditech.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`qiditech_asa_green_1000_175_p`|`{color_name}`|`Green`|{"source_file": "qiditech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "qiditech_asa_asagreen_1000_175_p": 235,
    "qiditech_asa_green_1000_175_p": 245.0
  }
}
```

### QI006: dup-6a01d7c775fc9844f84242427bf9bddb5c1c6e6f360f2b9529c334b923156b14

Status: APPROVED; survivor `qiditech_asa_red_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`qiditech_asa_asared_1000_175_p`|`ASA {color_name}`|`Red`|{"source_file": "qiditech.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`qiditech_asa_red_1000_175_p`|`{color_name}`|`Red`|{"source_file": "qiditech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "qiditech_asa_asared_1000_175_p": 235,
    "qiditech_asa_red_1000_175_p": 245.0
  }
}
```

### QI007: dup-92606cd17d62bace5dbf84df4bbc1cfc8c3b056c048dc1fa33bd6a20a1f08397

Status: APPROVED; survivor `qiditech_asa_white_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`qiditech_asa_asawhite_1000_175_p`|`ASA {color_name}`|`White`|{"source_file": "qiditech.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`qiditech_asa_white_1000_175_p`|`{color_name}`|`White`|{"source_file": "qiditech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "qiditech_asa_asawhite_1000_175_p": 235,
    "qiditech_asa_white_1000_175_p": 245.0
  }
}
```

### QI008: dup-6539683dc8bc19a9d99079b53a68c0de671d474c32676b1a2f9d42e0317770d1

Status: APPROVED; survivor `qiditech_asa_yellow_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`qiditech_asa_asayellow_1000_175_p`|`ASA {color_name}`|`Yellow`|{"source_file": "qiditech.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`qiditech_asa_yellow_1000_175_p`|`{color_name}`|`Yellow`|{"source_file": "qiditech.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "qiditech_asa_asayellow_1000_175_p": 235,
    "qiditech_asa_yellow_1000_175_p": 245.0
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

- `qiditech_pps-cf_black_750_175_p` — Black
- `qiditech_paht-cf_black_1000_175_p` — Black
- `qiditech_pa12-cf_black_1000_175_p` — Black
- `qiditech_petg_petg-toughblack_1000_175_p` — PETG-Tough Black
- `qiditech_petg_petg-toughwhite_1000_175_p` — PETG-Tough White
- `qiditech_petg_petg-toughred_1000_175_p` — PETG-Tough Red
- `qiditech_petg_petg-toughorange_1000_175_p` — PETG-Tough Orange
- `qiditech_petg_petg-toughblue_1000_175_p` — PETG-Tough Blue
- `qiditech_petg_petg-toughgreen_1000_175_p` — PETG-Tough Green
- `qiditech_petg_petg-toughyellow_1000_175_p` — PETG-Tough Yellow
- `qiditech_abs_abs-gf25black_500_175_p` — ABS-GF25 Black
- `qiditech_abs_abs-gf25green_500_175_p` — ABS-GF25 Green
- `qiditech_abs_abs-gf25purple_500_175_p` — ABS-GF25 Purple
- `qiditech_abs_abs-gf25red_500_175_p` — ABS-GF25 Red
- `qiditech_abs_abs-gf25black_1000_175_p` — ABS-GF25 Black
- `qiditech_abs_abs-gf25green_1000_175_p` — ABS-GF25 Green
- `qiditech_abs_abs-gf25purple_1000_175_p` — ABS-GF25 Purple
- `qiditech_abs_abs-gf25red_1000_175_p` — ABS-GF25 Red
- `qiditech_abs_absmetalrapidochampagnegold_1000_175_p` — ABS Metal Rapido Champagne Gold
- `qiditech_abs_absmetalrapidomidnightgreen_1000_175_p` — ABS Metal Rapido Midnight Green
- `qiditech_abs_absmetalrapidosilver_1000_175_p` — ABS Metal Rapido Silver
- `qiditech_abs_odorlessabsrapidoblack_1000_175_p` — Odorless ABS Rapido Black
- `qiditech_abs_odorlessabsrapidoblue_1000_175_p` — Odorless ABS Rapido Blue
- `qiditech_abs_odorlessabsrapidogray_1000_175_p` — Odorless ABS Rapido Gray
- `qiditech_abs_odorlessabsrapidogreen_1000_175_p` — Odorless ABS Rapido Green
- `qiditech_abs_odorlessabsrapidopurple_1000_175_p` — Odorless ABS Rapido Purple
- `qiditech_abs_odorlessabsrapidored_1000_175_p` — Odorless ABS Rapido Red
- `qiditech_abs_odorlessabsrapidosilver_1000_175_p` — Odorless ABS Rapido Silver
- `qiditech_abs_odorlessabsrapidowhite_1000_175_p` — Odorless ABS Rapido White
- `qiditech_abs_odorlessabsrapidoyellow_1000_175_p` — Odorless ABS Rapido Yellow
- `qiditech_abs_absrapidoblack_1000_175_p` — ABS Rapido Black
- `qiditech_abs_absrapidoblue_1000_175_p` — ABS Rapido Blue
- `qiditech_abs_absrapidogray_1000_175_p` — ABS Rapido Gray
- `qiditech_abs_absrapidogreen_1000_175_p` — ABS Rapido Green
- `qiditech_abs_absrapidored_1000_175_p` — ABS Rapido Red
- `qiditech_abs_absrapidowhite_1000_175_p` — ABS Rapido White
- `qiditech_abs_absrapidoyellow_1000_175_p` — ABS Rapido Yellow
- `qiditech_asa_asa-aeroblack_1000_175_p` — ASA-Aero Black
- `qiditech_asa_asa-aeronatural_1000_175_p` — ASA-Aero Natural
- `qiditech_pa12_pa12-cfblack_1000_175_p` — PA12-CF Black
- `qiditech_pa12_pa12s-whitesupportwhite_1000_175_p` — PA12 S-White Support White
- `qiditech_pc_pc/abs-frblack_1000_175_p` — PC/ABS-FR Black
- `qiditech_peba_peba95ablack_1000_175_p` — PEBA 95A Black
- `qiditech_pet_pet-cfblack_1000_175_p` — PET-CF Black
- `qiditech_pet_pet-gfblack_1000_175_p` — PET-GF Black
- `qiditech_pet_pet-gfbrown_1000_175_p` — PET-GF Brown
- `qiditech_pet_pet-gfred_1000_175_p` — PET-GF Red
- `qiditech_petg_petgbasicbeige_1000_175_p` — PETG Basic Beige
- `qiditech_petg_petgbasicblack_1000_175_p` — PETG Basic Black
- `qiditech_petg_petgbasiccyan_1000_175_p` — PETG Basic Cyan
- `qiditech_petg_petgbasicgreen_1000_175_p` — PETG Basic Green
- `qiditech_petg_petgbasickleinblue_1000_175_p` — PETG Basic Klein Blue
- `qiditech_petg_petgbasiclightgray_1000_175_p` — PETG Basic Light Gray
- `qiditech_petg_petgbasicred_1000_175_p` — PETG Basic Red
- `qiditech_petg_petgbasicskin_1000_175_p` — PETG Basic Skin
- `qiditech_petg_petgbasicwhite_1000_175_p` — PETG Basic White
- `qiditech_petg_petgbasicyellow_1000_175_p` — PETG Basic Yellow
- `qiditech_petg_petg-cfblack_1000_175_p` — PETG-CF Black
- `qiditech_petg_petg-gfblack_1000_175_p` — PETG-GF Black
- `qiditech_petg_petg-gfmacchiatobrown_1000_175_p` — PETG-GF Macchiato Brown
- `qiditech_petg_petg-gfskylightblue_1000_175_p` — PETG-GF Skylight Blue
- `qiditech_petg_petg-gfwhite_1000_175_p` — PETG-GF White
- `qiditech_petg_petgrapidoblack_1000_175_p` — PETG Rapido Black
- `qiditech_petg_petgrapidoblue_1000_175_p` — PETG Rapido Blue
- `qiditech_petg_petgrapidocopper_1000_175_p` — PETG Rapido Copper
- `qiditech_petg_petgrapidodiffuseclearwhite_1000_175_p` — PETG Rapido Diffuse Clear White
- `qiditech_petg_petgrapidograssgreen_1000_175_p` — PETG Rapido Grass Green
- `qiditech_petg_petgrapidogray_1000_175_p` — PETG Rapido Gray
- `qiditech_petg_petgrapidored_1000_175_p` — PETG Rapido Red
- `qiditech_petg_petgrapidowhite_1000_175_p` — PETG Rapido White
- `qiditech_petg_petgrapidoyellow_1000_175_p` — PETG Rapido Yellow
- `qiditech_petg_petgtranslucentblack_1000_175_p` — PETG Translucent Black
- `qiditech_petg_petgtranslucentblue_1000_175_p` — PETG Translucent Blue
- `qiditech_petg_petgtranslucentclear_1000_175_p` — PETG Translucent Clear
- `qiditech_petg_petgtranslucentpurple_1000_175_p` — PETG Translucent Purple
- `qiditech_petg_petgtranslucentred_1000_175_p` — PETG Translucent Red
- `qiditech_petg_petgtranslucentyellow_1000_175_p` — PETG Translucent Yellow
- `qiditech_pla_plabasicblack_1000_175_p` — PLA Basic Black
- `qiditech_pla_plabasicblue_1000_175_p` — PLA Basic Blue
- `qiditech_pla_plabasicbrown_1000_175_p` — PLA Basic Brown
- `qiditech_pla_plabasicdarkgreen_1000_175_p` — PLA Basic Dark Green
- `qiditech_pla_plabasicgray_1000_175_p` — PLA Basic Gray
- `qiditech_pla_plabasicred_1000_175_p` — PLA Basic Red
- `qiditech_pla_plabasicskin_1000_175_p` — PLA Basic Skin
- `qiditech_pla_plabasicskyblue_1000_175_p` — PLA Basic Sky Blue
- `qiditech_pla_plabasicwhite_1000_175_p` — PLA Basic White
- `qiditech_pla_plabasicyellow_1000_175_p` — PLA Basic Yellow
- `qiditech_pla_pla-cfblack_1000_175_p` — PLA-CF Black
- `qiditech_pla_pla-cfdarkred_1000_175_p` — PLA-CF Dark Red
- `qiditech_pla_pla-cflavenderpurple_1000_175_p` — PLA-CF Lavender Purple
- `qiditech_pla_pla-cfmidnightblue_1000_175_p` — PLA-CF Midnight Blue
- `qiditech_pla_pla-cfolivegreen_1000_175_p` — PLA-CF Olive Green
- `qiditech_pla_plamattebasiccoconutwhite_1000_175_p` — PLA Matte Basic Coconut White
- `qiditech_pla_plamattebasiclattebrown_1000_175_p` — PLA Matte Basic Latte Brown
- `qiditech_pla_plamattebasicmaltgreen_1000_175_p` — PLA Matte Basic Malt Green
- `qiditech_pla_plamattebasicmilkygreen_1000_175_p` — PLA Matte Basic Milky Green
- `qiditech_pla_plamattebasicmintblue_1000_175_p` — PLA Matte Basic Mint Blue
- `qiditech_pla_plamattebasicpeachpink_1000_175_p` — PLA Matte Basic Peach Pink
- `qiditech_pla_plamattebasicsesameblack_1000_175_p` — PLA Matte Basic Sesame Black
- `qiditech_pla_plamattebasicwatermelonred_1000_175_p` — PLA Matte Basic Watermelon Red
- `qiditech_pla_plamatterapidoashgray_1000_175_p` — PLA Matte Rapido Ash Gray
- `qiditech_pla_plamatterapidoblack_1000_175_p` — PLA Matte Rapido Black
- `qiditech_pla_plamatterapidokraft_1000_175_p` — PLA Matte Rapido Kraft
- `qiditech_pla_plamatterapidomaltclay_1000_175_p` — PLA Matte Rapido Malt Clay
- `qiditech_pla_plamatterapidonavyblue_1000_175_p` — PLA Matte Rapido Navy Blue
- `qiditech_pla_plamatterapidoolivegreen_1000_175_p` — PLA Matte Rapido Olive Green
- `qiditech_pla_plamatterapidotechgray_1000_175_p` — PLA Matte Rapido Tech Gray
- `qiditech_pla_plamatterapidowarmgray_1000_175_p` — PLA Matte Rapido Warm Gray
- `qiditech_pla_plamatterapidowhite_1000_175_p` — PLA Matte Rapido White
- `qiditech_pla_plametalrapidoblue_1000_175_p` — PLA Metal Rapido Blue
- `qiditech_pla_plametalrapidocoffeegold_1000_175_p` — PLA Metal Rapido Coffee Gold
- `qiditech_pla_plametalrapidomidnightgreen_1000_175_p` — PLA Metal Rapido Midnight Green
- `qiditech_pla_plametalrapidosilver_1000_175_p` — PLA Metal Rapido Silver
- `qiditech_pla_plarapidoblack_1000_175_p` — PLA Rapido Black
- `qiditech_pla_plarapidoblue_1000_175_p` — PLA Rapido Blue
- `qiditech_pla_plarapidogray_1000_175_p` — PLA Rapido Gray
- `qiditech_pla_plarapidogreen_1000_175_p` — PLA Rapido Green
- `qiditech_pla_plarapidoorange_1000_175_p` — PLA Rapido Orange
- `qiditech_pla_plarapidopink_1000_175_p` — PLA Rapido Pink
- `qiditech_pla_plarapidopurple_1000_175_p` — PLA Rapido Purple
- `qiditech_pla_plarapidored_1000_175_p` — PLA Rapido Red
- `qiditech_pla_plarapidowhite_1000_175_p` — PLA Rapido White
- `qiditech_pla_plarapidoyellow_1000_175_p` — PLA Rapido Yellow
- `qiditech_pla_plasilkrapidobronze_1000_175_p` — PLA Silk Rapido Bronze
- `qiditech_pla_plasilkrapidogreen_1000_175_p` — PLA Silk Rapido Green
- `qiditech_pla_plasilkrapidorosered_1000_175_p` — PLA Silk Rapido Rose Red
- `qiditech_pla_plasilkrapidoskin_1000_175_p` — PLA Silk Rapido Skin
- `qiditech_pla_plawoodcedarbrown_1000_175_p` — PLA Wood Cedar Brown
- `qiditech_pla_plawoodyellow_1000_175_p` — PLA Wood Yellow
- `qiditech_ppa_paht-cfblack_1000_175_p` — PAHT-CF Black
- `qiditech_ppa_ultrapa-cf25black_1000_175_p` — UltraPA-CF25 Black
- `qiditech_ppa_paht-gfblue_1000_175_p` — PAHT-GF Blue
- `qiditech_ppa_paht-gfgray_1000_175_p` — PAHT-GF Gray
- `qiditech_ppa_ultrapanatural_1000_175_p` — UltraPA Natural
- `qiditech_pps_pps-cfblack_750_175_p` — PPS-CF Black
- `qiditech_pps_pps-gf20gray_750_175_p` — PPS-GF20 Gray
- `qiditech_tpu_tpu95ahfblack_1000_175_p` — TPU 95A HF Black
- `qiditech_tpu_tpu95ahfwhite_1000_175_p` — TPU 95A HF White
- `qiditech_tpu_tpu-aeroblack_1000_175_p` — TPU-Aero Black
- `qiditech_tpu_tpu-aerowhite_1000_175_p` — TPU-Aero White
