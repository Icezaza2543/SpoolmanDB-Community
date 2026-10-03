# eryone duplicate migration review

Base `c3a2bd82b7c8681a040a42f240865df5fb06bca4`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `d46a057bb2b0003270351f826c31ad01e120c46b7f026d7a5ca98578fa8aefdd`.

## Authorization and result

{"groups": 7, "approved_groups": 2, "retired": 2, "deferred": 5, "hard_stops": 0, "before_count": 51748, "after_count": 51746, "brand_before": 511, "brand_after": 509, "registry_before": 1686, "registry_after": 1688, "metadata_fields_changed": 1, "code_transfers": 1, "new": 0, "changed_identity": 0, "rekeyed": 0}

Two Rule1 strict groups applied: GrayPETG exactoneweightone1.75 incomingB0106003 transferred only to1000g target; current ambiguousPETG printing kept. TripleBlack&Gold&Purple density1.24→1.32 exactcurrentembeddedTDS; valid220/60 nominalpoints retained. Five mixedweightcodegroups defer unchanged. No packaging/tare/HEX changes; no formula borrowed across single/tripleSilk.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://eryone3d.com/products/moq1-pla-silk-triple-color-filament", "density": 1.32, "nozzle": [190, 220], "bed": [55, 70], "color": "Black&Gold&Purple", "note": "TripleSilk only, not Gold/Copper singleSilk."}
- {"url": "https://eryone3d.com/products/petg", "note": "Internally conflicting nozzle230–250 vs215–230 and bed75–80/70–85/80–100; retain survivor1.27/240/80 unresolved."}
- {"url": "https://eryone3d.com/products/moq1-pla-silk-filament", "nozzle": [190, 220], "bed": [55, 70], "note": "SingleSilk Gold/Copper groups deferred; density not verified."}
- {"url": "https://eryone3d.com/products/tpu", "note": "Internal recommendations200–220 vs190–220 and bed0–60 vs55–70; deferredmixedweight group."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`eryone_petg_petggray_1000_175_c`|`eryone_petg_gray_1000_175_c`|`eryone.json::Eryone::PETG {color_name}::PETG Gray::PETG::1000::1.75::cardboard::False`|
|`eryone_pla_plasilkblack&gold&purple_1000_175_c`|`eryone_pla_silkblack&gold&purple_1000_175_c`|`eryone.json::Eryone::PLA Silk {color_name}::PLA Silk Black&Gold&Purple::PLA::1000::1.75::cardboard::False`|

## Per-group decisions and unresolved metadata

### ER001: dup-81420e6dbe3d5d1dfb860145acfef0114f796a223f018bb3bd94460dc5a8ed67

Status: APPROVED; survivor `eryone_petg_gray_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`eryone_petg_gray_1000_175_c`|`{color_name}`|`Gray`|{"source_file": "eryone.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 1, "compiled_records": 1} / True|
|`eryone_petg_petggray_1000_175_c`|`PETG {color_name}`|`Gray`|{"source_file": "eryone.json", "definition_index": 20, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "eryone_petg_gray_1000_175_c": 1.27,
    "eryone_petg_petggray_1000_175_c": 1.25
  },
  "spool_weight": {
    "eryone_petg_gray_1000_175_c": 187.0,
    "eryone_petg_petggray_1000_175_c": 267
  },
  "color_hex": {
    "eryone_petg_gray_1000_175_c": "80817F",
    "eryone_petg_petggray_1000_175_c": "5B605E"
  },
  "extruder_temp": {
    "eryone_petg_gray_1000_175_c": 240,
    "eryone_petg_petggray_1000_175_c": 250
  },
  "bed_temp": {
    "eryone_petg_gray_1000_175_c": 80,
    "eryone_petg_petggray_1000_175_c": 77
  },
  "codes": {
    "eryone_petg_gray_1000_175_c": null,
    "eryone_petg_petggray_1000_175_c": [
      "B0106003"
    ]
  }
}
```

### ER002: dup-4c79fe615e92b5df6c0ceec7f4e29667ae94ac0c518d01fa6cb2d2d74c9b631d

Status: DEFERRED; survivor `eryone_pla_black_1000_175_c`; PLABlackB0101001 replicated across1000/3000g; exactweight binding unavailable; no blindtransfer..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`eryone_pla_black_1000_175_c`|`{color_name}`|`Black`|{"source_file": "eryone.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / True|
|`eryone_pla_plablack_1000_175_c`|`PLA {color_name}`|`Black`|{"source_file": "eryone.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 35, "compiled_records": 70} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "eryone_pla_black_1000_175_c": 187,
    "eryone_pla_plablack_1000_175_c": 267
  },
  "color_hex": {
    "eryone_pla_black_1000_175_c": "000000",
    "eryone_pla_plablack_1000_175_c": "141414"
  },
  "extruder_temp": {
    "eryone_pla_black_1000_175_c": 210,
    "eryone_pla_plablack_1000_175_c": null
  },
  "extruder_temp_range": {
    "eryone_pla_black_1000_175_c": null,
    "eryone_pla_plablack_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "eryone_pla_black_1000_175_c": 50,
    "eryone_pla_plablack_1000_175_c": null
  },
  "bed_temp_range": {
    "eryone_pla_black_1000_175_c": null,
    "eryone_pla_plablack_1000_175_c": [
      50,
      70
    ]
  },
  "codes": {
    "eryone_pla_black_1000_175_c": null,
    "eryone_pla_plablack_1000_175_c": [
      "B0101001"
    ]
  }
}
```

### ER003: dup-f9653d664d8061f77dec98c9c7dbffb6c271e25d47cedcc9c253f491fe0709eb

Status: APPROVED; survivor `eryone_pla_silkblack&gold&purple_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`eryone_pla_plasilkblack&gold&purple_1000_175_c`|`PLA Silk {color_name}`|`Black&Gold&Purple`|{"source_file": "eryone.json", "definition_index": 45, "weights": 3, "diameters": 1, "colors": 46, "compiled_records": 138} / False|
|`eryone_pla_silkblack&gold&purple_1000_175_c`|`Silk {color_name}`|`Black & Gold & Purple`|{"source_file": "eryone.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "eryone_pla_plasilkblack&gold&purple_1000_175_c": 1.32,
    "eryone_pla_silkblack&gold&purple_1000_175_c": 1.24
  },
  "spool_weight": {
    "eryone_pla_plasilkblack&gold&purple_1000_175_c": 267,
    "eryone_pla_silkblack&gold&purple_1000_175_c": 187.0
  },
  "color_hex": {
    "eryone_pla_plasilkblack&gold&purple_1000_175_c": "80550F",
    "eryone_pla_silkblack&gold&purple_1000_175_c": null
  },
  "color_hexes": {
    "eryone_pla_plasilkblack&gold&purple_1000_175_c": null,
    "eryone_pla_silkblack&gold&purple_1000_175_c": [
      "000000",
      "D5983E",
      "5B3378"
    ]
  },
  "extruder_temp": {
    "eryone_pla_plasilkblack&gold&purple_1000_175_c": 205,
    "eryone_pla_silkblack&gold&purple_1000_175_c": 220
  },
  "multi_color_direction": {
    "eryone_pla_plasilkblack&gold&purple_1000_175_c": null,
    "eryone_pla_silkblack&gold&purple_1000_175_c": "coaxial"
  }
}
```

### ER004: dup-6fb3abad4ea3d22f49bd87229853acd0b08ff5b1986400c8d8a16d8bb91156e1

Status: DEFERRED; survivor `eryone_pla_silkcopper_1000_175_c`; CopperB0102003 replicated across250/1000/3000g; live exactweight binding unproven; defer without blindtransfer..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`eryone_pla_plasilkcopper_1000_175_c`|`PLA Silk {color_name}`|`Copper`|{"source_file": "eryone.json", "definition_index": 45, "weights": 3, "diameters": 1, "colors": 46, "compiled_records": 138} / False|
|`eryone_pla_silkcopper_1000_175_c`|`Silk {color_name}`|`Copper`|{"source_file": "eryone.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "eryone_pla_plasilkcopper_1000_175_c": 1.32,
    "eryone_pla_silkcopper_1000_175_c": 1.24
  },
  "spool_weight": {
    "eryone_pla_plasilkcopper_1000_175_c": 267,
    "eryone_pla_silkcopper_1000_175_c": 187.0
  },
  "color_hex": {
    "eryone_pla_plasilkcopper_1000_175_c": "DA7A6F",
    "eryone_pla_silkcopper_1000_175_c": "B36A51"
  },
  "extruder_temp": {
    "eryone_pla_plasilkcopper_1000_175_c": 205,
    "eryone_pla_silkcopper_1000_175_c": 220
  },
  "codes": {
    "eryone_pla_plasilkcopper_1000_175_c": [
      "B0102003"
    ],
    "eryone_pla_silkcopper_1000_175_c": null
  }
}
```

### ER005: dup-1d945c5c6a1e4e0828e9a027594da05e3ce5f765af0b551328ee3ff2f34f6ddc

Status: DEFERRED; survivor `eryone_pla_silkgold_1000_175_c`; GoldB0102001 replicated across250/1000/3000g; live exactweight binding unproven; defer without blindtransfer..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`eryone_pla_plasilkgold_1000_175_c`|`PLA Silk {color_name}`|`Gold`|{"source_file": "eryone.json", "definition_index": 45, "weights": 3, "diameters": 1, "colors": 46, "compiled_records": 138} / False|
|`eryone_pla_silkgold_1000_175_c`|`Silk {color_name}`|`Gold`|{"source_file": "eryone.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "eryone_pla_plasilkgold_1000_175_c": 1.32,
    "eryone_pla_silkgold_1000_175_c": 1.24
  },
  "spool_weight": {
    "eryone_pla_plasilkgold_1000_175_c": 267,
    "eryone_pla_silkgold_1000_175_c": 187.0
  },
  "color_hex": {
    "eryone_pla_plasilkgold_1000_175_c": "F29F43",
    "eryone_pla_silkgold_1000_175_c": "D5983E"
  },
  "extruder_temp": {
    "eryone_pla_plasilkgold_1000_175_c": 205,
    "eryone_pla_silkgold_1000_175_c": 220
  },
  "codes": {
    "eryone_pla_plasilkgold_1000_175_c": [
      "B0102001"
    ],
    "eryone_pla_silkgold_1000_175_c": null
  }
}
```

### ER006: dup-ed95c1be3053cfc50c55b6052beb9b9536bc4e35bf3ae51c8ca266c7b0bf177b

Status: DEFERRED; survivor `eryone_pla_white_1000_175_c`; PLAWhiteB0101002 replicated across1000/3000g; exactweight binding unavailable; no blindtransfer..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`eryone_pla_plawhite_1000_175_c`|`PLA {color_name}`|`White`|{"source_file": "eryone.json", "definition_index": 22, "weights": 2, "diameters": 1, "colors": 35, "compiled_records": 70} / False|
|`eryone_pla_white_1000_175_c`|`{color_name}`|`White`|{"source_file": "eryone.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "eryone_pla_plawhite_1000_175_c": 267,
    "eryone_pla_white_1000_175_c": 187
  },
  "color_hex": {
    "eryone_pla_plawhite_1000_175_c": "E9E9E9",
    "eryone_pla_white_1000_175_c": "FFFFFF"
  },
  "extruder_temp": {
    "eryone_pla_plawhite_1000_175_c": null,
    "eryone_pla_white_1000_175_c": 210
  },
  "extruder_temp_range": {
    "eryone_pla_plawhite_1000_175_c": [
      190,
      230
    ],
    "eryone_pla_white_1000_175_c": null
  },
  "bed_temp": {
    "eryone_pla_plawhite_1000_175_c": null,
    "eryone_pla_white_1000_175_c": 50
  },
  "bed_temp_range": {
    "eryone_pla_plawhite_1000_175_c": [
      50,
      70
    ],
    "eryone_pla_white_1000_175_c": null
  },
  "codes": {
    "eryone_pla_plawhite_1000_175_c": [
      "B0101002"
    ],
    "eryone_pla_white_1000_175_c": null
  }
}
```

### ER007: dup-5db75a39a4bc36500111552096953f46e258439cd4834e1de5dbf828acd2caad

Status: DEFERRED; survivor `eryone_tpu_black_500_175_c`; TPUBlack500g candidate carriesB0107001/B0107015 replicated across500/1000g; no sameSKUweight proof; retainPLA-like density unresolved and both records..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`eryone_tpu_black_500_175_c`|`{color_name}`|`Black`|{"source_file": "eryone.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 1, "compiled_records": 1} / True|
|`eryone_tpu_tpublack_500_175_c`|`TPU {color_name}`|`Black`|{"source_file": "eryone.json", "definition_index": 55, "weights": 2, "diameters": 1, "colors": 6, "compiled_records": 12} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "eryone_tpu_black_500_175_c": 1.24,
    "eryone_tpu_tpublack_500_175_c": 1.21
  },
  "spool_weight": {
    "eryone_tpu_black_500_175_c": 130.0,
    "eryone_tpu_tpublack_500_175_c": 120
  },
  "color_hex": {
    "eryone_tpu_black_500_175_c": "000000",
    "eryone_tpu_tpublack_500_175_c": "414141"
  },
  "extruder_temp": {
    "eryone_tpu_black_500_175_c": 220,
    "eryone_tpu_tpublack_500_175_c": 205
  },
  "bed_temp": {
    "eryone_tpu_black_500_175_c": 60,
    "eryone_tpu_tpublack_500_175_c": 30
  },
  "codes": {
    "eryone_tpu_black_500_175_c": null,
    "eryone_tpu_tpublack_500_175_c": [
      "B0107001",
      "B0107015"
    ]
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "eryone_pla_silkblack&gold&purple_1000_175_c",
      "values": {
        "density": 1.32
      },
      "source": "https://eryone3d.com/products/moq1-pla-silk-triple-color-filament",
      "lot": "current exact triple-color Silk embedded manufacturerTDS; printing evidence only, no packaging inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "eryone_petg_gray_1000_175_c",
      "values": {
        "codes": [
          "B0106003"
        ]
      },
      "source": "c3a2bd82b7c8681a040a42f240865df5fb06bca4",
      "lot": "reviewed historical identifier preservation",
      "same_variant": true,
      "approved": true,
      "field_sources": {
        "codes": "c3a2bd82b7c8681a040a42f240865df5fb06bca4"
      }
    }
  ],
  "transfers": [
    {
      "old_id": "eryone_petg_petggray_1000_175_c",
      "target_id": "eryone_petg_gray_1000_175_c",
      "field": "codes",
      "values": [
        "B0106003"
      ],
      "source": "c3a2bd82b7c8681a040a42f240865df5fb06bca4"
    }
  ]
}
```

## Preserved out-of-scope IDs

- `eryone_pla_silkblack&rosered_1000_175_c` — Silk Black & Rose Red
- `eryone_pla_pink&blue_1000_175_c` — Pink & Blue
- `eryone_pla_dustyblue&mustardyellow_1000_175_c` — Dusty Blue & Mustard Yellow
- `eryone_abs_absblack_1000_175_c` — ABS Black
- `eryone_abs_abswhite_1000_175_c` — ABS White
- `eryone_abs_abs+black_1000_175_c` — ABS+ Black
- `eryone_abs_abs+blue_1000_175_c` — ABS+ Blue
- `eryone_abs_abs+green_1000_175_c` — ABS+ Green
- `eryone_abs_abs+grey_1000_175_c` — ABS+ Grey
- `eryone_abs_abs+red_1000_175_c` — ABS+ Red
- `eryone_abs_abs+white_1000_175_c` — ABS+ White
- `eryone_abs_abs-cfblack_1000_175_c` — ABS-CF Black
- `eryone_abs_abs-gfblack_1000_175_c` — ABS-GF Black
- `eryone_abs_abs-gfwhite_1000_175_c` — ABS-GF White
- `eryone_abs_abshigh-speedblack_1000_175_c` — ABS High-Speed Black
- `eryone_abs_abshigh-speedblue_1000_175_c` — ABS High-Speed Blue
- `eryone_abs_abshigh-speedgray_1000_175_c` — ABS High-Speed Gray
- `eryone_abs_abshigh-speedgreen_1000_175_c` — ABS High-Speed Green
- `eryone_abs_abshigh-speedred_1000_175_c` — ABS High-Speed Red
- `eryone_abs_abshigh-speedwhite_1000_175_c` — ABS High-Speed White
- `eryone_abs_abs-pcwhite_1000_175_c` — ABS-PC White
- `eryone_asa_asablack_1000_175_c` — ASA Black
- `eryone_asa_asawhite_1000_175_c` — ASA White
- `eryone_asa_asa-cfblack_1000_175_c` — ASA-CF Black
- `eryone_asa_asa-cfblue_1000_175_c` — ASA-CF Blue
- `eryone_asa_asa-cfdarkgray_1000_175_c` — ASA-CF Dark gray
- `eryone_asa_asa-cfolivegreen_1000_175_c` — ASA-CF Olive green
- `eryone_asa_asa-cfpurplered_1000_175_c` — ASA-CF Purple red
- `eryone_asa_asa-gfblack_1000_175_c` — ASA-GF Black
- `eryone_asa_asa-gfwhite_1000_175_c` — ASA-GF White
- `eryone_asa_asahigh-speedblack_1000_175_c` — ASA High-Speed Black
- `eryone_asa_asahigh-speedorange_1000_175_c` — ASA High-Speed Orange
- `eryone_asa_asahigh-speedwhite_1000_175_c` — ASA High-Speed White
- `eryone_asa_asalight-weightwhite_1000_175_c` — ASA Light-Weight White
- `eryone_pa12_pa12nylonblack_1000_175_c` — PA12 Nylon Black
- `eryone_pa12_pa12nylontransparent_1000_175_c` — PA12 Nylon Transparent
- `eryone_pa12_pa12nylonwhite_1000_175_c` — PA12 Nylon White
- `eryone_pa12_pa12-cfblack_800_175_c` — PA12-CF Black
- `eryone_pa12_pa12-gfblack_1000_175_c` — PA12-GF Black
- `eryone_pa6_pa6-cfblack_800_175_c` — PA6-CF Black
- `eryone_pa6_pa6-gfblack_1000_175_c` — PA6-GF Black
- `eryone_pa6_pa6-gfwhite_1000_175_c` — PA6-GF White
- `eryone_petg_petgblack_1000_175_c` — PETG Black
- `eryone_petg_petgblue_1000_175_c` — PETG Blue
- `eryone_petg_petgorange_1000_175_c` — PETG Orange
- `eryone_petg_petgred_1000_175_c` — PETG Red
- `eryone_petg_petgtransblue_1000_175_c` — PETG TRANS Blue
- `eryone_petg_petgtransred_1000_175_c` — PETG TRANS Red
- `eryone_petg_petgtransparent_1000_175_c` — PETG Transparent
- `eryone_petg_petgwhite_1000_175_c` — PETG White
- `eryone_petg_petgyellow_1000_175_c` — PETG Yellow
- `eryone_petg_petg-cfblack_1000_175_c` — PETG-CF black
- `eryone_petg_petg-cfblue_1000_175_c` — PETG-CF blue
- `eryone_petg_petg-cfdarkgray_1000_175_c` — PETG-CF dark gray
- `eryone_petg_petg-cfgrassgreen_1000_175_c` — PETG-CF Grass green
- `eryone_petg_petg-cfolivegreen_1000_175_c` — PETG-CF olive green
- `eryone_petg_petg-cforange_1000_175_c` — PETG-CF Orange
- `eryone_petg_petg-cfpurplered_1000_175_c` — PETG-CF Purple red
- `eryone_pla_plaagategray_1000_175_c` — PLA Agate Gray
- `eryone_pla_plaapplegreen_1000_175_c` — PLA Apple Green
- `eryone_pla_plablue_1000_175_c` — PLA Blue
- `eryone_pla_plaburnttitaniumconstellation_1000_175_c` — PLA Burnt Titanium Constellation
- `eryone_pla_plaburnttitaniumgalaxy_1000_175_c` — PLA Burnt Titanium Galaxy
- `eryone_pla_plaburnttitaniuminterstellar_1000_175_c` — PLA Burnt Titanium Interstellar
- `eryone_pla_plaburnttitaniumnebula_1000_175_c` — PLA Burnt Titanium Nebula
- `eryone_pla_plaburnttitaniumwormhole_1000_175_c` — PLA Burnt Titanium Wormhole
- `eryone_pla_placarbonblack_1000_175_c` — PLA Carbon Black
- `eryone_pla_placarbonfibre-black_1000_175_c` — PLA Carbon fibre - black
- `eryone_pla_plachinesered_1000_175_c` — PLA Chinese Red
- `eryone_pla_placoolwhite_1000_175_c` — PLA Cool White
- `eryone_pla_pladarkpurple_1000_175_c` — PLA Dark purple
- `eryone_pla_plaglossyblack_1000_175_c` — PLA Glossy black
- `eryone_pla_plagray_1000_175_c` — PLA Gray
- `eryone_pla_plagreen_1000_175_c` — PLA Green
- `eryone_pla_plaivorywhite_1000_175_c` — PLA Ivory White
- `eryone_pla_plajetblack_1000_175_c` — PLA Jet Black
- `eryone_pla_plalavenderpurple_1000_175_c` — PLA Lavender Purple
- `eryone_pla_plamangoyellow_1000_175_c` — PLA Mango Yellow
- `eryone_pla_plamilitarygreen_1000_175_c` — PLA Military green
- `eryone_pla_plamilkywhite_1000_175_c` — PLA Milky White
- `eryone_pla_planavyblue_1000_175_c` — PLA Navy blue
- `eryone_pla_plaorange_1000_175_c` — PLA Orange
- `eryone_pla_plapearlwhite_1000_175_c` — PLA Pearl white
- `eryone_pla_plared_1000_175_c` — PLA Red
- `eryone_pla_plarosered_1000_175_c` — PLA Rose Red
- `eryone_pla_plasignalgray_1000_175_c` — PLA Signal Gray
- `eryone_pla_plasilver_1000_175_c` — PLA Silver
- `eryone_pla_plaskin_1000_175_c` — PLA Skin
- `eryone_pla_platransparent_1000_175_c` — PLA Transparent
- `eryone_pla_plawhitejade_1000_175_c` — PLA White Jade
- `eryone_pla_playellow_1000_175_c` — PLA Yellow
- `eryone_pla_plaagategray_3000_175_c` — PLA Agate Gray
- `eryone_pla_plaapplegreen_3000_175_c` — PLA Apple Green
- `eryone_pla_plablack_3000_175_c` — PLA Black
- `eryone_pla_plablue_3000_175_c` — PLA Blue
- `eryone_pla_plaburnttitaniumconstellation_3000_175_c` — PLA Burnt Titanium Constellation
- `eryone_pla_plaburnttitaniumgalaxy_3000_175_c` — PLA Burnt Titanium Galaxy
- `eryone_pla_plaburnttitaniuminterstellar_3000_175_c` — PLA Burnt Titanium Interstellar
- `eryone_pla_plaburnttitaniumnebula_3000_175_c` — PLA Burnt Titanium Nebula
- `eryone_pla_plaburnttitaniumwormhole_3000_175_c` — PLA Burnt Titanium Wormhole
- `eryone_pla_placarbonblack_3000_175_c` — PLA Carbon Black
- `eryone_pla_placarbonfibre-black_3000_175_c` — PLA Carbon fibre - black
- `eryone_pla_plachinesered_3000_175_c` — PLA Chinese Red
- `eryone_pla_placoolwhite_3000_175_c` — PLA Cool White
- `eryone_pla_pladarkpurple_3000_175_c` — PLA Dark purple
- `eryone_pla_plaglossyblack_3000_175_c` — PLA Glossy black
- `eryone_pla_plagray_3000_175_c` — PLA Gray
- `eryone_pla_plagreen_3000_175_c` — PLA Green
- `eryone_pla_plaivorywhite_3000_175_c` — PLA Ivory White
- `eryone_pla_plajetblack_3000_175_c` — PLA Jet Black
- `eryone_pla_plalavenderpurple_3000_175_c` — PLA Lavender Purple
- `eryone_pla_plamangoyellow_3000_175_c` — PLA Mango Yellow
- `eryone_pla_plamilitarygreen_3000_175_c` — PLA Military green
- `eryone_pla_plamilkywhite_3000_175_c` — PLA Milky White
- `eryone_pla_planavyblue_3000_175_c` — PLA Navy blue
- `eryone_pla_plaorange_3000_175_c` — PLA Orange
- `eryone_pla_plapearlwhite_3000_175_c` — PLA Pearl white
- `eryone_pla_plared_3000_175_c` — PLA Red
- `eryone_pla_plarosered_3000_175_c` — PLA Rose Red
- `eryone_pla_plasignalgray_3000_175_c` — PLA Signal Gray
- `eryone_pla_plasilver_3000_175_c` — PLA Silver
- `eryone_pla_plaskin_3000_175_c` — PLA Skin
- `eryone_pla_platransparent_3000_175_c` — PLA Transparent
- `eryone_pla_plawhite_3000_175_c` — PLA White
- `eryone_pla_plawhitejade_3000_175_c` — PLA White Jade
- `eryone_pla_playellow_3000_175_c` — PLA Yellow
- `eryone_pla_pla+armygreen_1000_175_c` — PLA+ Army green
- `eryone_pla_pla+black_1000_175_c` — PLA+ Black
- `eryone_pla_pla+blue_1000_175_c` — PLA+ Blue
- `eryone_pla_pla+coolwhite_1000_175_c` — PLA+ Cool white
- `eryone_pla_pla+gray_1000_175_c` — PLA+ Gray
- `eryone_pla_pla+green_1000_175_c` — PLA+ Green
- `eryone_pla_pla+ivorywhite_1000_175_c` — PLA+ Ivory white
- `eryone_pla_pla+olivegreen_1000_175_c` — PLA+ Olive green
- `eryone_pla_pla+orange_1000_175_c` — PLA+ Orange
- `eryone_pla_pla+red_1000_175_c` — PLA+ Red
- `eryone_pla_pla+skin_1000_175_c` — PLA+ Skin
- `eryone_pla_pla+white_1000_175_c` — PLA+ White
- `eryone_pla_pla+yellow_1000_175_c` — PLA+ Yellow
- `eryone_pla_pla+high-speedazureblue_1000_175_c` — PLA+ High-Speed Azure Blue
- `eryone_pla_pla+high-speedblack_1000_175_c` — PLA+ High-Speed Black
- `eryone_pla_pla+high-speedblue_1000_175_c` — PLA+ High-Speed Blue
- `eryone_pla_pla+high-speedbrown_1000_175_c` — PLA+ High-Speed Brown
- `eryone_pla_pla+high-speeddarkbrown_1000_175_c` — PLA+ High-Speed Dark Brown
- `eryone_pla_pla+high-speedgray_1000_175_c` — PLA+ High-Speed Gray
- `eryone_pla_pla+high-speedgreen_1000_175_c` — PLA+ High-Speed Green
- `eryone_pla_pla+high-speedivory_1000_175_c` — PLA+ High-Speed Ivory
- `eryone_pla_pla+high-speedmagenta_1000_175_c` — PLA+ High-Speed Magenta
- `eryone_pla_pla+high-speedmintgreen_1000_175_c` — PLA+ High-Speed Mint Green
- `eryone_pla_pla+high-speedorange_1000_175_c` — PLA+ High-Speed Orange
- `eryone_pla_pla+high-speedpurple_1000_175_c` — PLA+ High-Speed Purple
- `eryone_pla_pla+high-speedred_1000_175_c` — PLA+ High-Speed Red
- `eryone_pla_pla+high-speedstone(brown&khaki&white)_1000_175_c` — PLA+ High-Speed Stone (Brown & Khaki & White)
- `eryone_pla_pla+high-speedviolet_1000_175_c` — PLA+ High-Speed Violet
- `eryone_pla_pla+high-speedwhite_1000_175_c` — PLA+ High-Speed White
- `eryone_pla_pla+high-speedyellow_1000_175_c` — PLA+ High-Speed Yellow
- `eryone_pla_plaburnttitaniumblue_1000_175_c` — PLA Burnt Titanium Blue
- `eryone_pla_plaburnttitaniumbluepurple_1000_175_c` — PLA Burnt Titanium Blue Purple
- `eryone_pla_plaburnttitaniumdarkgold_1000_175_c` — PLA Burnt Titanium Dark Gold
- `eryone_pla_plaburnttitaniumgreen_1000_175_c` — PLA Burnt Titanium Green
- `eryone_pla_plaburnttitaniumred_1000_175_c` — PLA Burnt Titanium Red
- `eryone_pla_plaburnttitaniumtechnologyblue_1000_175_c` — PLA Burnt Titanium Technology Blue
- `eryone_pla_plaburnttitaniumdual-colorblack&blue_1000_175_c` — PLA Burnt Titanium Dual-Color Black & Blue
- `eryone_pla_plaburnttitaniumdual-colorblack&purpleblue_1000_175_c` — PLA Burnt Titanium Dual-Color Black & Purple Blue
- `eryone_pla_plaburnttitaniumdual-colorblack&rosered_1000_175_c` — PLA Burnt Titanium Dual-Color Black & Rose Red
- `eryone_pla_plaburnttitaniumdual-colorblue&rosered_1000_175_c` — PLA Burnt Titanium Dual-Color Blue & Rose Red
- `eryone_pla_plaburnttitaniumdual-colorgreen&blue_1000_175_c` — PLA Burnt Titanium Dual-Color Green & Blue
- `eryone_pla_plaburnttitaniumdual-colorgreen&gold_1000_175_c` — PLA Burnt Titanium Dual-Color Green & Gold
- `eryone_pla_plaburnttitaniumdual-colorgreen&purpleblue_1000_175_c` — PLA Burnt Titanium Dual-Color Green & Purple Blue
- `eryone_pla_plaburnttitaniumdual-colorgreen&rosered_1000_175_c` — PLA Burnt Titanium Dual-Color Green & Rose Red
- `eryone_pla_plaburnttitaniumrainbowconstellation(rosered&flashblack)_1000_175_c` — PLA Burnt Titanium Rainbow Constellation (Rose Red & Flash Black)
- `eryone_pla_plaburnttitaniumrainbowfantasyglaze_1000_175_c` — PLA Burnt Titanium Rainbow Fantasy Glaze
- `eryone_pla_plaburnttitaniumrainbowgalaxy(green&blue&rosered)_1000_175_c` — PLA Burnt Titanium Rainbow Galaxy (Green & Blue & Rose Red)
- `eryone_pla_plaburnttitaniumrainbowinterstellar(blue&flashblack)_1000_175_c` — PLA Burnt Titanium Rainbow Interstellar (Blue & Flash Black)
- `eryone_pla_plaburnttitaniumrainbownebula(darkgold&green&blue-purple)_1000_175_c` — PLA Burnt Titanium Rainbow Nebula (Dark Gold & Green & Blue-Purple)
- `eryone_pla_plaburnttitaniumrainbowwormhole(green&flashingblack)_1000_175_c` — PLA Burnt Titanium Rainbow Wormhole (Green & Flashing Black)
- `eryone_pla_plaburnttitaniumtriplecolorblack&green&rosered_1000_175_c` — PLA Burnt Titanium Triple Color Black & Green & Rose Red
- `eryone_pla_plaburnttitaniumtriplecolorblack&rosered&purpleblue_1000_175_c` — PLA Burnt Titanium Triple Color Black & Rose Red & Purple Blue
- `eryone_pla_plaburnttitaniumtriplecolorblue&black&rosered_1000_175_c` — PLA Burnt Titanium Triple Color Blue & Black & Rose Red
- `eryone_pla_plaburnttitaniumtriplecolorblue&gold&green_1000_175_c` — PLA Burnt Titanium Triple Color Blue & Gold & Green
- `eryone_pla_plaburnttitaniumtriplecolorblue&green&rosered_1000_175_c` — PLA Burnt Titanium Triple Color Blue & Green & Rose Red
- `eryone_pla_plaburnttitaniumtriplecolorgreen&rosered&purpleblue_1000_175_c` — PLA Burnt Titanium Triple Color Green & Rose Red & Purple Blue
- `eryone_pla_plaburnttitaniumtriplecolorpurpleblue&gold&green_1000_175_c` — PLA Burnt Titanium Triple Color Purple Blue & Gold & Green
- `eryone_pla_pla-cfpla-cf_1000_175_c` — PLA-CF PLA-CF
- `eryone_pla_plagalaxybipolarnebula(darkgreen)_1000_175_c` — PLA Galaxy Bipolar Nebula (dark green)
- `eryone_pla_plagalaxyblack_1000_175_c` — PLA Galaxy Black
- `eryone_pla_plagalaxyblue_1000_175_c` — PLA Galaxy Blue
- `eryone_pla_plagalaxyomeganebula(greengold)_1000_175_c` — PLA Galaxy Omega Nebula (Green Gold)
- `eryone_pla_plagalaxyowlnebula(darkpurple)_1000_175_c` — PLA Galaxy Owl Nebula (Dark Purple)
- `eryone_pla_plagalaxypurple_1000_175_c` — PLA Galaxy Purple
- `eryone_pla_plagalaxyred_1000_175_c` — PLA Galaxy Red
- `eryone_pla_plagalaxysilver_1000_175_c` — PLA Galaxy Silver
- `eryone_pla_plagalaxysiriusnebula(darkblue)_1000_175_c` — PLA Galaxy Sirius Nebula (dark blue)
- `eryone_pla_plahigh-speedagategray_1000_175_c` — PLA High-Speed Agate Gray
- `eryone_pla_plahigh-speedblack_1000_175_c` — PLA High-Speed Black
- `eryone_pla_plahigh-speedgray_1000_175_c` — PLA High-Speed Gray
- `eryone_pla_plahigh-speedsignalgray_1000_175_c` — PLA High-Speed Signal Gray
- `eryone_pla_plahigh-speedskincolor_1000_175_c` — PLA High-Speed Skin Color
- `eryone_pla_plahigh-speedwhite_1000_175_c` — PLA High-Speed White
- `eryone_pla_plalightweightblack_1000_175_c` — PLA Light Weight Black
- `eryone_pla_plaluminousblue_1000_175_c` — PLA Luminous Blue
- `eryone_pla_plaluminousfireflygreen_1000_175_c` — PLA Luminous firefly green
- `eryone_pla_plaluminousgreen_1000_175_c` — PLA Luminous Green
- `eryone_pla_plaluminousorange-red_1000_175_c` — PLA Luminous Orange-red
- `eryone_pla_plaluminousorange-yellow_1000_175_c` — PLA Luminous Orange-yellow
- `eryone_pla_plaluminouspurple_1000_175_c` — PLA Luminous Purple
- `eryone_pla_plaluminousrainbow_1000_175_c` — PLA Luminous Rainbow
- `eryone_pla_plamarbleplamarble_1000_175_c` — PLA Marble PLA Marble
- `eryone_pla_plamatteaquablue_1000_175_c` — PLA Matte Aqua Blue
- `eryone_pla_plamattearmygreen_1000_175_c` — PLA Matte Army Green
- `eryone_pla_plamatteblack_1000_175_c` — PLA Matte Black
- `eryone_pla_plamatteblackforestgreen_1000_175_c` — PLA Matte Black forest green
- `eryone_pla_plamattebluelilac_1000_175_c` — PLA Matte Blue Lilac
- `eryone_pla_plamattegray_1000_175_c` — PLA Matte Gray
- `eryone_pla_plamattemintgreen_1000_175_c` — PLA Matte Mint green
- `eryone_pla_plamattenavyblue_1000_175_c` — PLA Matte Navy Blue
- `eryone_pla_plamatteolivegreen_1000_175_c` — PLA Matte Olive Green
- `eryone_pla_plamattepink_1000_175_c` — PLA Matte Pink
- `eryone_pla_plamattepotteryred_1000_175_c` — PLA Matte Pottery Red
- `eryone_pla_plamattered_1000_175_c` — PLA Matte Red
- `eryone_pla_plamatteredwax_1000_175_c` — PLA Matte Red Wax
- `eryone_pla_plamatterubyred_1000_175_c` — PLA Matte Ruby red
- `eryone_pla_plamatteskin_1000_175_c` — PLA Matte Skin
- `eryone_pla_plamattewhite_1000_175_c` — PLA Matte White
- `eryone_pla_plamatteyellow_1000_175_c` — PLA Matte Yellow
- `eryone_pla_plamattedual-colorblack&white_1000_175_c` — PLA Matte Dual-Color Black&White
- `eryone_pla_plamattedual-colorbluegreen&burntorange_1000_175_c` — PLA Matte Dual-Color Blue Green & Burnt Orange
- `eryone_pla_plamattedual-colorblue&purple_1000_175_c` — PLA Matte Dual-Color Blue&Purple
- `eryone_pla_plamattedual-colorblue&white_1000_175_c` — PLA Matte Dual-Color Blue & White
- `eryone_pla_plamattedual-colorblue&yellow_1000_175_c` — PLA Matte Dual-Color Blue&Yellow
- `eryone_pla_plamattedual-colordustyblue&mustardyellow_1000_175_c` — PLA Matte Dual-Color Dusty Blue & Mustard Yellow
- `eryone_pla_plamattedual-colornavyblue&olivegreen_1000_175_c` — PLA Matte Dual-Color Navy Blue&Olive Green
- `eryone_pla_plamattedual-colorpink&blue_1000_175_c` — PLA Matte Dual-Color Pink&Blue
- `eryone_pla_plamattedual-colorpink&mattewhite_1000_175_c` — PLA Matte Dual-Color Pink & Matte White
- `eryone_pla_plamattedual-colorpurple&green_1000_175_c` — PLA Matte Dual-Color Purple&Green
- `eryone_pla_plamattedual-colorredviolet&green_1000_175_c` — PLA Matte Dual-Color Red Violet & Green
- `eryone_pla_plamattedual-colorrosepink&sagegreen_1000_175_c` — PLA Matte Dual-Color Rose Pink & Sage Green
- `eryone_pla_plamattedual-coloryellow&purple_1000_175_c` — PLA Matte Dual-Color Yellow&Purple
- `eryone_pla_plamattegradientbluegreen&purple_1000_175_c` — PLA Matte Gradient Blue Green & Purple
- `eryone_pla_plamattegradientpink&green&blue_1000_175_c` — PLA Matte Gradient Pink & Green & Blue
- `eryone_pla_plamattegradientpink&yellowgreen_1000_175_c` — PLA Matte Gradient Pink & Yellow Green
- `eryone_pla_plamattegradientred&yellow_1000_175_c` — PLA Matte Gradient Red & Yellow
- `eryone_pla_plamattegradientyellow&green_1000_175_c` — PLA Matte Gradient Yellow & Green
- `eryone_pla_plamattegradientyellow&purple_1000_175_c` — PLA Matte Gradient Yellow & Purple
- `eryone_pla_plamattehighspeedblack_1000_175_c` — PLA Matte High Speed Black
- `eryone_pla_plamattehighspeediceblue_1000_175_c` — PLA Matte High Speed Ice Blue
- `eryone_pla_plamattehighspeedlightgray_1000_175_c` — PLA Matte High Speed Light gray
- `eryone_pla_plamattehighspeednavyblue_1000_175_c` — PLA Matte High Speed Navy blue
- `eryone_pla_plamattehighspeedolivegreen_1000_175_c` — PLA Matte High Speed Olive green
- `eryone_pla_plamattehighspeedwhite_1000_175_c` — PLA Matte High Speed White
- `eryone_pla_plamattehighspeedgradientmulti-color(coffee&khaki&white)_1000_175_c` — PLA Matte High Speed Gradient Multi-Color (coffee & khaki & white)
- `eryone_pla_plamattehighspeedgradientmulti-color(darkbrown&yellow&lightbrown)_1000_175_c` — PLA Matte High Speed Gradient Multi-Color (dark brown & yellow & light brown)
- `eryone_pla_plamattehighspeedgradientmulti-colorglacier(blue&white&lightblue)_1000_175_c` — PLA Matte High Speed Gradient Multi-Color Glacier (Blue & White & Light Blue)
- `eryone_pla_plamattehighspeedgradientmulti-color(gold&red)_1000_175_c` — PLA Matte High Speed Gradient Multi-Color (gold & red)
- `eryone_pla_plamattehighspeedgradientmulti-colormarshmallow(blue&pink)_1000_175_c` — PLA Matte High Speed Gradient Multi-Color Marshmallow (Blue & Pink)
- `eryone_pla_plamattehighspeedgradientmulti-colorredvelvet(red&white)_1000_175_c` — PLA Matte High Speed Gradient Multi-Color Red Velvet (Red & White)
- `eryone_pla_plamattehighspeedgradientmulti-colorsnowfield(blue&white)_1000_175_c` — PLA Matte High Speed Gradient Multi-Color Snowfield (Blue & White)
- `eryone_pla_plamattehighspeedrockrainbowarcticblue_1000_175_c` — PLA Matte High Speed Rock Rainbow Arctic Blue
- `eryone_pla_plamattehighspeedrockrainbowfrostmint_1000_175_c` — PLA Matte High Speed Rock Rainbow Frost Mint
- `eryone_pla_plamattehighspeedrockrainbowgrandcanyonred_1000_175_c` — PLA Matte High Speed Rock Rainbow Grand Canyon Red
- `eryone_pla_plamattehighspeedrockrainbowmaplesyrupamber_1000_175_c` — PLA Matte High Speed Rock Rainbow Maple Syrup Amber
- `eryone_pla_plamattehighspeedrockrainbownavajopotteryred_1000_175_c` — PLA Matte High Speed Rock Rainbow Navajo Pottery Red
- `eryone_pla_plamattehighspeedrockrainbowsaltflatveins_1000_175_c` — PLA Matte High Speed Rock Rainbow Salt Flat Veins
- `eryone_pla_plamattehighspeedrockrainbowtotemengraving_1000_175_c` — PLA Matte High Speed Rock Rainbow Totem Engraving
- `eryone_pla_plamattehighspeedrockrainbowzebrastone_1000_175_c` — PLA Matte High Speed Rock Rainbow Zebra Stone
- `eryone_pla_plamattehighspeedtriple-colorblack&red&olivegreen_1000_175_c` — PLA Matte High Speed Triple-Color Black & red & olive green
- `eryone_pla_plamattehighspeedtriple-colorblack&yellow&blue_1000_175_c` — PLA Matte High Speed Triple-Color Black & yellow & blue
- `eryone_pla_plamattehighspeedtriple-colorpink&blue&yellow_1000_175_c` — PLA Matte High Speed Triple-Color Pink & blue & yellow
- `eryone_pla_plamattehighspeedtriple-colorpink&green&blue_1000_175_c` — PLA Matte High Speed Triple-Color Pink & green & blue
- `eryone_pla_plamattehighspeedtriple-colorpurple&yellow&blue_1000_175_c` — PLA Matte High Speed Triple-Color Purple & yellow & blue
- `eryone_pla_plamattehighspeedtriple-colorvibrantgreen&lemonyellow&aquablue_1000_175_c` — PLA Matte High Speed Triple-Color Vibrant green & lemon yellow & aqua blue
- `eryone_pla_plamatterainbowmacarons_1000_175_c` — PLA Matte Rainbow Macarons
- `eryone_pla_plamatterainbowwatercolorfivecolors_1000_175_c` — PLA Matte Rainbow Watercolor five colors
- `eryone_pla_plametalliccopper_1000_175_c` — PLA Metallic Copper
- `eryone_pla_plametalliciron_1000_175_c` — PLA Metallic Iron
- `eryone_pla_plametallicstainlesssteel_1000_175_c` — PLA Metallic Stainless Steel
- `eryone_pla_plametallicwolfram_1000_175_c` — PLA Metallic Wolfram
- `eryone_pla_plarainbowclassical_1000_175_c` — PLA Rainbow Classical
- `eryone_pla_plarainbowlagoon_1000_175_c` — PLA Rainbow Lagoon
- `eryone_pla_plarainbowsteampunk_1000_175_c` — PLA Rainbow Steampunk
- `eryone_pla_plasilkblack&blue&purple_250_175_c` — PLA Silk Black&Blue&Purple
- `eryone_pla_plasilkblack&darkgold_250_175_c` — PLA Silk Black & Dark Gold
- `eryone_pla_plasilkblack&darkgreen_250_175_c` — PLA Silk Black & dark green
- `eryone_pla_plasilkblack&gold&purple_250_175_c` — PLA Silk Black&Gold&Purple
- `eryone_pla_plasilkblack&purple_250_175_c` — PLA Silk Black&Purple
- `eryone_pla_plasilkblack&red_250_175_c` — PLA Silk Black&Red
- `eryone_pla_plasilkblack&red&gold_250_175_c` — PLA Silk Black & Red & Gold
- `eryone_pla_plasilkblack&rose_250_175_c` — PLA Silk Black & Rose
- `eryone_pla_plasilkblue_250_175_c` — PLA Silk Blue
- `eryone_pla_plasilkblue&green_250_175_c` — PLA Silk Blue&Green
- `eryone_pla_plasilkbluegreen&orange_250_175_c` — PLA Silk Blue green & Orange
- `eryone_pla_plasilkblue&purple_250_175_c` — PLA Silk Blue & Purple
- `eryone_pla_plasilkcopper_250_175_c` — PLA Silk Copper
- `eryone_pla_plasilkdarkgreen_250_175_c` — PLA Silk Dark Green
- `eryone_pla_plasilkdarkgreen&midnightblue&black_250_175_c` — PLA Silk Dark Green & Midnight Blue & Black
- `eryone_pla_plasilkdarkgreen&purple&yellow_250_175_c` — PLA Silk Dark green&Purple&Yellow
- `eryone_pla_plasilkgold_250_175_c` — PLA Silk Gold
- `eryone_pla_plasilkgold&blue_250_175_c` — PLA Silk Gold & Blue
- `eryone_pla_plasilkgold&blue&purple_250_175_c` — PLA Silk Gold&Blue&Purple
- `eryone_pla_plasilkgold&copper_250_175_c` — PLA Silk Gold&Copper
- `eryone_pla_plasilkgold&green&purple_250_175_c` — PLA Silk Gold&Green&Purple
- `eryone_pla_plasilkgold&purple_250_175_c` — PLA Silk Gold&Purple
- `eryone_pla_plasilkgold&silver_250_175_c` — PLA Silk Gold&Silver
- `eryone_pla_plasilkgold&silver&copper_250_175_c` — PLA Silk GOLD&SILVER&COPPER
- `eryone_pla_plasilkgreen_250_175_c` — PLA Silk Green
- `eryone_pla_plasilkmidnightblue&black_250_175_c` — PLA Silk Midnight Blue & Black
- `eryone_pla_plasilkmidnightblue&silver_250_175_c` — PLA Silk Midnight Blue & Silver
- `eryone_pla_plasilkorange&blue_250_175_c` — PLA Silk Orange & Blue
- `eryone_pla_plasilkorange&blue&green_250_175_c` — PLA Silk ORANGE&BLUE&GREEN
- `eryone_pla_plasilkpink_250_175_c` — PLA Silk Pink
- `eryone_pla_plasilkpurple&green_250_175_c` — PLA Silk Purple & Green
- `eryone_pla_plasilkpurple&orange_250_175_c` — PLA Silk Purple & Orange
- `eryone_pla_plasilkpurple&teal&burntorange_250_175_c` — PLA Silk Purple & Teal & Burnt Orange
- `eryone_pla_plasilkred&blue_250_175_c` — PLA Silk Red&Blue
- `eryone_pla_plasilkred&blue&green_250_175_c` — PLA Silk Red&Blue&Green
- `eryone_pla_plasilkred&gold_250_175_c` — PLA Silk Red&Gold
- `eryone_pla_plasilkred&gold&blue_250_175_c` — PLA Silk Red&Gold&Blue
- `eryone_pla_plasilkred&gold&purple_250_175_c` — PLA Silk Red&Gold&Purple
- `eryone_pla_plasilkred&green_250_175_c` — PLA Silk Red&Green
- `eryone_pla_plasilkred&purple&green_250_175_c` — PLA Silk Red&Purple&Green
- `eryone_pla_plasilkred&yellow&blue_250_175_c` — PLA Silk Red&Yellow&Blue
- `eryone_pla_plasilkrosered&lightblue_250_175_c` — PLA Silk Rose Red & Light Blue
- `eryone_pla_plasilksapphiregreen&orangered&gold_250_175_c` — PLA Silk Sapphire green & Orange red & Gold
- `eryone_pla_plasilksilver_250_175_c` — PLA Silk Silver
- `eryone_pla_plasilkwhite_250_175_c` — PLA Silk White
- `eryone_pla_plasilkyellow&green_250_175_c` — PLA Silk Yellow&Green
- `eryone_pla_plasilkblack&blue&purple_1000_175_c` — PLA Silk Black&Blue&Purple
- `eryone_pla_plasilkblack&darkgold_1000_175_c` — PLA Silk Black & Dark Gold
- `eryone_pla_plasilkblack&darkgreen_1000_175_c` — PLA Silk Black & dark green
- `eryone_pla_plasilkblack&purple_1000_175_c` — PLA Silk Black&Purple
- `eryone_pla_plasilkblack&red_1000_175_c` — PLA Silk Black&Red
- `eryone_pla_plasilkblack&red&gold_1000_175_c` — PLA Silk Black & Red & Gold
- `eryone_pla_plasilkblack&rose_1000_175_c` — PLA Silk Black & Rose
- `eryone_pla_plasilkblue_1000_175_c` — PLA Silk Blue
- `eryone_pla_plasilkblue&green_1000_175_c` — PLA Silk Blue&Green
- `eryone_pla_plasilkbluegreen&orange_1000_175_c` — PLA Silk Blue green & Orange
- `eryone_pla_plasilkblue&purple_1000_175_c` — PLA Silk Blue & Purple
- `eryone_pla_plasilkdarkgreen_1000_175_c` — PLA Silk Dark Green
- `eryone_pla_plasilkdarkgreen&midnightblue&black_1000_175_c` — PLA Silk Dark Green & Midnight Blue & Black
- `eryone_pla_plasilkdarkgreen&purple&yellow_1000_175_c` — PLA Silk Dark green&Purple&Yellow
- `eryone_pla_plasilkgold&blue_1000_175_c` — PLA Silk Gold & Blue
- `eryone_pla_plasilkgold&blue&purple_1000_175_c` — PLA Silk Gold&Blue&Purple
- `eryone_pla_plasilkgold&copper_1000_175_c` — PLA Silk Gold&Copper
- `eryone_pla_plasilkgold&green&purple_1000_175_c` — PLA Silk Gold&Green&Purple
- `eryone_pla_plasilkgold&purple_1000_175_c` — PLA Silk Gold&Purple
- `eryone_pla_plasilkgold&silver_1000_175_c` — PLA Silk Gold&Silver
- `eryone_pla_plasilkgold&silver&copper_1000_175_c` — PLA Silk GOLD&SILVER&COPPER
- `eryone_pla_plasilkgreen_1000_175_c` — PLA Silk Green
- `eryone_pla_plasilkmidnightblue&black_1000_175_c` — PLA Silk Midnight Blue & Black
- `eryone_pla_plasilkmidnightblue&silver_1000_175_c` — PLA Silk Midnight Blue & Silver
- `eryone_pla_plasilkorange&blue_1000_175_c` — PLA Silk Orange & Blue
- `eryone_pla_plasilkorange&blue&green_1000_175_c` — PLA Silk ORANGE&BLUE&GREEN
- `eryone_pla_plasilkpink_1000_175_c` — PLA Silk Pink
- `eryone_pla_plasilkpurple&green_1000_175_c` — PLA Silk Purple & Green
- `eryone_pla_plasilkpurple&orange_1000_175_c` — PLA Silk Purple & Orange
- `eryone_pla_plasilkpurple&teal&burntorange_1000_175_c` — PLA Silk Purple & Teal & Burnt Orange
- `eryone_pla_plasilkred&blue_1000_175_c` — PLA Silk Red&Blue
- `eryone_pla_plasilkred&blue&green_1000_175_c` — PLA Silk Red&Blue&Green
- `eryone_pla_plasilkred&gold_1000_175_c` — PLA Silk Red&Gold
- `eryone_pla_plasilkred&gold&blue_1000_175_c` — PLA Silk Red&Gold&Blue
- `eryone_pla_plasilkred&gold&purple_1000_175_c` — PLA Silk Red&Gold&Purple
- `eryone_pla_plasilkred&green_1000_175_c` — PLA Silk Red&Green
- `eryone_pla_plasilkred&purple&green_1000_175_c` — PLA Silk Red&Purple&Green
- `eryone_pla_plasilkred&yellow&blue_1000_175_c` — PLA Silk Red&Yellow&Blue
- `eryone_pla_plasilkrosered&lightblue_1000_175_c` — PLA Silk Rose Red & Light Blue
- `eryone_pla_plasilksapphiregreen&orangered&gold_1000_175_c` — PLA Silk Sapphire green & Orange red & Gold
- `eryone_pla_plasilksilver_1000_175_c` — PLA Silk Silver
- `eryone_pla_plasilkwhite_1000_175_c` — PLA Silk White
- `eryone_pla_plasilkyellow&green_1000_175_c` — PLA Silk Yellow&Green
- `eryone_pla_plasilkblack&blue&purple_3000_175_c` — PLA Silk Black&Blue&Purple
- `eryone_pla_plasilkblack&darkgold_3000_175_c` — PLA Silk Black & Dark Gold
- `eryone_pla_plasilkblack&darkgreen_3000_175_c` — PLA Silk Black & dark green
- `eryone_pla_plasilkblack&gold&purple_3000_175_c` — PLA Silk Black&Gold&Purple
- `eryone_pla_plasilkblack&purple_3000_175_c` — PLA Silk Black&Purple
- `eryone_pla_plasilkblack&red_3000_175_c` — PLA Silk Black&Red
- `eryone_pla_plasilkblack&red&gold_3000_175_c` — PLA Silk Black & Red & Gold
- `eryone_pla_plasilkblack&rose_3000_175_c` — PLA Silk Black & Rose
- `eryone_pla_plasilkblue_3000_175_c` — PLA Silk Blue
- `eryone_pla_plasilkblue&green_3000_175_c` — PLA Silk Blue&Green
- `eryone_pla_plasilkbluegreen&orange_3000_175_c` — PLA Silk Blue green & Orange
- `eryone_pla_plasilkblue&purple_3000_175_c` — PLA Silk Blue & Purple
- `eryone_pla_plasilkcopper_3000_175_c` — PLA Silk Copper
- `eryone_pla_plasilkdarkgreen_3000_175_c` — PLA Silk Dark Green
- `eryone_pla_plasilkdarkgreen&midnightblue&black_3000_175_c` — PLA Silk Dark Green & Midnight Blue & Black
- `eryone_pla_plasilkdarkgreen&purple&yellow_3000_175_c` — PLA Silk Dark green&Purple&Yellow
- `eryone_pla_plasilkgold_3000_175_c` — PLA Silk Gold
- `eryone_pla_plasilkgold&blue_3000_175_c` — PLA Silk Gold & Blue
- `eryone_pla_plasilkgold&blue&purple_3000_175_c` — PLA Silk Gold&Blue&Purple
- `eryone_pla_plasilkgold&copper_3000_175_c` — PLA Silk Gold&Copper
- `eryone_pla_plasilkgold&green&purple_3000_175_c` — PLA Silk Gold&Green&Purple
- `eryone_pla_plasilkgold&purple_3000_175_c` — PLA Silk Gold&Purple
- `eryone_pla_plasilkgold&silver_3000_175_c` — PLA Silk Gold&Silver
- `eryone_pla_plasilkgold&silver&copper_3000_175_c` — PLA Silk GOLD&SILVER&COPPER
- `eryone_pla_plasilkgreen_3000_175_c` — PLA Silk Green
- `eryone_pla_plasilkmidnightblue&black_3000_175_c` — PLA Silk Midnight Blue & Black
- `eryone_pla_plasilkmidnightblue&silver_3000_175_c` — PLA Silk Midnight Blue & Silver
- `eryone_pla_plasilkorange&blue_3000_175_c` — PLA Silk Orange & Blue
- `eryone_pla_plasilkorange&blue&green_3000_175_c` — PLA Silk ORANGE&BLUE&GREEN
- `eryone_pla_plasilkpink_3000_175_c` — PLA Silk Pink
- `eryone_pla_plasilkpurple&green_3000_175_c` — PLA Silk Purple & Green
- `eryone_pla_plasilkpurple&orange_3000_175_c` — PLA Silk Purple & Orange
- `eryone_pla_plasilkpurple&teal&burntorange_3000_175_c` — PLA Silk Purple & Teal & Burnt Orange
- `eryone_pla_plasilkred&blue_3000_175_c` — PLA Silk Red&Blue
- `eryone_pla_plasilkred&blue&green_3000_175_c` — PLA Silk Red&Blue&Green
- `eryone_pla_plasilkred&gold_3000_175_c` — PLA Silk Red&Gold
- `eryone_pla_plasilkred&gold&blue_3000_175_c` — PLA Silk Red&Gold&Blue
- `eryone_pla_plasilkred&gold&purple_3000_175_c` — PLA Silk Red&Gold&Purple
- `eryone_pla_plasilkred&green_3000_175_c` — PLA Silk Red&Green
- `eryone_pla_plasilkred&purple&green_3000_175_c` — PLA Silk Red&Purple&Green
- `eryone_pla_plasilkred&yellow&blue_3000_175_c` — PLA Silk Red&Yellow&Blue
- `eryone_pla_plasilkrosered&lightblue_3000_175_c` — PLA Silk Rose Red & Light Blue
- `eryone_pla_plasilksapphiregreen&orangered&gold_3000_175_c` — PLA Silk Sapphire green & Orange red & Gold
- `eryone_pla_plasilksilver_3000_175_c` — PLA Silk Silver
- `eryone_pla_plasilkwhite_3000_175_c` — PLA Silk White
- `eryone_pla_plasilkyellow&green_3000_175_c` — PLA Silk Yellow&Green
- `eryone_pla_plasilkhigh-speeddual-colorblack&red_1000_175_c` — PLA Silk High-Speed Dual-Color Black&Red
- `eryone_pla_plasilkhigh-speeddual-colorblue&green_1000_175_c` — PLA Silk High-Speed Dual-Color Blue&Green
- `eryone_pla_plasilkhigh-speeddual-colorblue&red_1000_175_c` — PLA Silk High-Speed Dual-Color Blue&Red
- `eryone_pla_plasilkhigh-speeddual-colordarkgreen&black_1000_175_c` — PLA Silk High-Speed Dual-Color Dark Green&Black
- `eryone_pla_plasilkhigh-speeddual-colorgold&purple_1000_175_c` — PLA Silk High-Speed Dual-Color Gold&Purple
- `eryone_pla_plasilkhigh-speeddual-colorgreen&yellow_1000_175_c` — PLA Silk High-Speed Dual-Color Green&Yellow
- `eryone_pla_plasilkhigh-speeddual-colormidnightblue&silver_1000_175_c` — PLA Silk High-Speed Dual-Color Midnight Blue&Silver
- `eryone_pla_plasilkhigh-speeddual-colororange&blue_1000_175_c` — PLA Silk High-Speed Dual-Color Orange & Blue
- `eryone_pla_plasilkhigh-speeddual-colorpurple&black_1000_175_c` — PLA Silk High-Speed Dual-Color Purple&Black
- `eryone_pla_plasilkhigh-speeddual-colorred&green_1000_175_c` — PLA Silk High-Speed Dual-Color Red&Green
- `eryone_pla_plasilkhigh-speedquadrupleauroradream_1000_175_c` — PLA Silk High-Speed Quadruple Aurora Dream
- `eryone_pla_plasilkhigh-speedquadruplecoldflamenightattack_1000_175_c` — PLA Silk High-Speed Quadruple Cold Flame Night Attack
- `eryone_pla_plasilkhigh-speedquadrupledarkgreen&midnightblue&black_1000_175_c` — PLA Silk High-Speed Quadruple Dark Green & Midnight Blue & Black
- `eryone_pla_plasilkhigh-speedquadrupleelectricnight_1000_175_c` — PLA Silk High-Speed Quadruple Electric Night
- `eryone_pla_plasilkhigh-speedquadrupleemeraldathens_1000_175_c` — PLA Silk High-Speed Quadruple Emerald Athens
- `eryone_pla_plasilkhigh-speedquadruplegorgeousharmony(black&gold&red&green)_1000_175_c` — PLA Silk High-Speed Quadruple Gorgeous Harmony (Black & Gold & Red & Green)
- `eryone_pla_plasilkhigh-speedquadruplegorgeousquartet(red&yellow&blue&green)_1000_175_c` — PLA Silk High-Speed Quadruple Gorgeous Quartet (Red & Yellow & Blue & Green)
- `eryone_pla_plasilkhigh-speedquadruplemetallicfrenzy_1000_175_c` — PLA Silk High-Speed Quadruple Metallic Frenzy
- `eryone_pla_plasilkhigh-speedquadruplepondoftheunderworld_1000_175_c` — PLA Silk High-Speed Quadruple Pond of the Underworld
- `eryone_pla_plasilkhigh-speedquadrupleroyalessence_1000_175_c` — PLA Silk High-Speed Quadruple Royal Essence
- `eryone_pla_plasilkhigh-speedquadrupletwilightglow(black&red&darkpurple&gold)_1000_175_c` — PLA Silk High-Speed Quadruple Twilight Glow (Black & Red & Dark Purple & Gold)
- `eryone_pla_plasilkhigh-speedtriple-colorblack&blue&purple_1000_175_c` — PLA Silk High-Speed Triple-Color Black & Blue & Purple
- `eryone_pla_plasilkhigh-speedtriple-colorblack&red&gold_1000_175_c` — PLA Silk High-Speed Triple-Color Black & Red & Gold
- `eryone_pla_plasilkhigh-speedtriple-colordarkgreen&midnightblue&black_1000_175_c` — PLA Silk High-Speed Triple-Color Dark Green & Midnight Blue & Black
- `eryone_pla_plasilkhigh-speedtriple-colororange&blue&green_1000_175_c` — PLA Silk High-Speed Triple-Color Orange & Blue & Green
- `eryone_pla_plasilkhigh-speedtriple-colorred&blue&green_1000_175_c` — PLA Silk High-Speed Triple-Color Red & Blue & Green
- `eryone_pla_plasilkhigh-speedtriple-colorred&purple&gold_1000_175_c` — PLA Silk High-Speed Triple-Color Red & Purple & Gold
- `eryone_pla_plasilkhigh-speedtriple-colorred&yellow&blue_1000_175_c` — PLA Silk High-Speed Triple-Color Red & Yellow & Blue
- `eryone_pla_plasilkrainbowcandy_1000_175_c` — PLA Silk Rainbow Candy
- `eryone_pla_plasilkrainbowcolorpaletterainbow_1000_175_c` — PLA Silk Rainbow Color palette rainbow
- `eryone_pla_plasilkrainbowforest_1000_175_c` — PLA Silk Rainbow Forest
- `eryone_pla_plasilkrainbowmacaron_1000_175_c` — PLA Silk Rainbow Macaron
- `eryone_pla_plasilkrainbowminirainbow_1000_175_c` — PLA Silk Rainbow Minirainbow
- `eryone_pla_plasilkrainbowrainbow_1000_175_c` — PLA Silk Rainbow Rainbow
- `eryone_pla_plasilkrainbowrainbowovermountains_1000_175_c` — PLA Silk Rainbow Rainbow over mountains
- `eryone_pla_plasilkrainbowsteampunkrainbow_1000_175_c` — PLA Silk Rainbow Steampunk rainbow
- `eryone_pla_plasilkrainbowsunsetrainbow_1000_175_c` — PLA Silk Rainbow Sunset rainbow
- `eryone_pla_plasilkrainbowuniverse_1000_175_c` — PLA Silk Rainbow Universe
- `eryone_pla_plasilkrainbowvibrantrainbow_1000_175_c` — PLA Silk Rainbow Vibrant rainbow
- `eryone_pla_plasilkrainbowwaterfallrainbow_1000_175_c` — PLA Silk Rainbow Waterfall rainbow
- `eryone_pla_plaultrasilkblack_1000_175_c` — PLA Ultra Silk Black
- `eryone_pla_plaultrasilkbronze_1000_175_c` — PLA Ultra Silk Bronze
- `eryone_pla_plaultrasilkcopper_1000_175_c` — PLA Ultra Silk Copper
- `eryone_pla_plaultrasilkdarkgold_1000_175_c` — PLA Ultra Silk Dark Gold
- `eryone_pla_plaultrasilkgold_1000_175_c` — PLA Ultra Silk Gold
- `eryone_pla_plaultrasilkred_1000_175_c` — PLA Ultra Silk Red
- `eryone_pla_plaultrasilksilver_1000_175_c` — PLA Ultra Silk Silver
- `eryone_pla_plawoodcharcoalash_1000_175_c` — PLA Wood Charcoal ash
- `eryone_pla_plawoodclay_1000_175_c` — PLA Wood Clay
- `eryone_pla_plawooddeep_1000_175_c` — PLA Wood Deep
- `eryone_pla_plawoodlight_1000_175_c` — PLA Wood Light
- `eryone_pla_plawoodpinewood_1000_175_c` — PLA Wood Pine wood
- `eryone_pla_plawoodred_1000_175_c` — PLA Wood Red
- `eryone_pp_ppblack_900_175_c` — PP Black
- `eryone_pp_ppwhite_900_175_c` — PP White
- `eryone_pp_pp-cfblack_900_175_c` — PP-CF Black
- `eryone_pps-cf_pps-cf10black_500_175_c` — PPS-CF10 Black
- `eryone_tpu_tpugray_500_175_c` — TPU Gray
- `eryone_tpu_tputransparent_500_175_c` — TPU Transparent
- `eryone_tpu_tputransparentblue_500_175_c` — TPU Transparent Blue
- `eryone_tpu_tputransparentred_500_175_c` — TPU Transparent Red
- `eryone_tpu_tpuwhite_500_175_c` — TPU White
- `eryone_tpu_tpublack_1000_175_c` — TPU Black
- `eryone_tpu_tpugray_1000_175_c` — TPU Gray
- `eryone_tpu_tputransparent_1000_175_c` — TPU Transparent
- `eryone_tpu_tputransparentblue_1000_175_c` — TPU Transparent Blue
- `eryone_tpu_tputransparentred_1000_175_c` — TPU Transparent Red
- `eryone_tpu_tpuwhite_1000_175_c` — TPU White
- `eryone_tpu_tpu90agray_1000_175_c` — TPU 90A Gray
- `eryone_tpu_tpu90asolidblack_1000_175_c` — TPU 90A Solid black
- `eryone_tpu_tpu90asolidwhite_1000_175_c` — TPU 90A Solid white
- `eryone_tpu_tpu90atransparent_1000_175_c` — TPU 90A Transparent
- `eryone_tpu_tpu90atransparentblue_1000_175_c` — TPU 90A Transparent Blue
- `eryone_tpu_tpu90atransparentred_1000_175_c` — TPU 90A Transparent Red
- `eryone_tpu_tpuhigh-speedsolidblack_1000_175_c` — TPU High-Speed solid black
- `eryone_tpu_tpuhigh-speedsolidgray_1000_175_c` — TPU High-Speed solid gray
- `eryone_tpu_tpuhigh-speedsolidwhite_1000_175_c` — TPU High-Speed solid white
- `eryone_tpu_tpuhigh-speedtransparent_1000_175_c` — TPU High-Speed transparent
- `eryone_tpu_tpuhigh-speedtransparentblue_1000_175_c` — TPU High-Speed transparent blue
- `eryone_tpu_tpuhigh-speedtransparentred_1000_175_c` — TPU High-Speed transparent red
- `eryone_tpu_tpurainbowaurorarainbow_500_175_c` — TPU Rainbow Aurora Rainbow
- `eryone_tpu_tpurainbowseaglassrainbow_500_175_c` — TPU Rainbow Sea Glass Rainbow
