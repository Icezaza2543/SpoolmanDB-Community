# alzament duplicate migration review

Base `8c6d362f86366c41fa6d7e5c81849390f173d3c9`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `416101170c086e7e0b2ad06a5bf96185d80524409709758a661d707e74dc418a`.

## Authorization and result

{"groups": 2, "approved_groups": 1, "retired": 1, "deferred": 1, "hard_stops": 0, "before_count": 51703, "after_count": 51702, "brand_before": 139, "brand_after": 138, "registry_before": 1731, "registry_after": 1732, "metadata_fields_changed": 2, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

One strictRule4 SilkGold duplicate retains well-formed larger family, no Cartesian warning; correct exacttarget nozzle/bed. Density1.19 unverified retained. ABSGray/Grey visibly differentHEX unbound, deferred. No identifiers/packaging/tare changes.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://www.alza.cz/alzament-pla-silk-1-kg-gold-d12869930.htm", "nozzle": [210, 230], "bed": [45, 60], "note": "Alza own brand exactSilkGold1kg1.75."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`alzament_pla_silkplagold_1000_175_p`|`alzament_pla_plasilkgold_1000_175_p`|`alzament.json::Alzament::Silk PLA {color_name}::Silk PLA Gold::PLA::1000.0::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### AL001: dup-ab2600f560ca16e859bf5f55b7bd2c9375df2cc151a853b699ca6075e2d34c3c

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`alzament_abs_absgray_1000_175_p`|`ABS {color_name}`|`Gray`|{"source_file": "alzament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|
|`alzament_abs_absgrey_1000_175_p`|`ABS {color_name}`|`Grey`|{"source_file": "alzament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "alzament_abs_absgray_1000_175_p": "939392",
    "alzament_abs_absgrey_1000_175_p": "808080"
  }
}
```

### AL002: dup-b693686d4895234867c5e1ed8557b2c43415d7031fbf6f19b6bb772176b123e7

Status: APPROVED; survivor `alzament_pla_plasilkgold_1000_175_p`; Rule 4.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`alzament_pla_plasilkgold_1000_175_p`|`PLA Silk {color_name}`|`Gold`|{"source_file": "alzament.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 45, "compiled_records": 45} / False|
|`alzament_pla_silkplagold_1000_175_p`|`Silk PLA {color_name}`|`Gold`|{"source_file": "alzament.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "alzament_pla_plasilkgold_1000_175_p": 1.19,
    "alzament_pla_silkplagold_1000_175_p": 1.24
  },
  "color_hex": {
    "alzament_pla_plasilkgold_1000_175_p": "E4C33F",
    "alzament_pla_silkplagold_1000_175_p": "d4af37"
  },
  "extruder_temp_range": {
    "alzament_pla_plasilkgold_1000_175_p": [
      190,
      230
    ],
    "alzament_pla_silkplagold_1000_175_p": [
      210,
      230
    ]
  },
  "bed_temp_range": {
    "alzament_pla_plasilkgold_1000_175_p": [
      50,
      70
    ],
    "alzament_pla_silkplagold_1000_175_p": [
      45,
      60
    ]
  },
  "finish": {
    "alzament_pla_plasilkgold_1000_175_p": null,
    "alzament_pla_silkplagold_1000_175_p": "glossy"
  },
  "country_of_origin": {
    "alzament_pla_plasilkgold_1000_175_p": "CZ",
    "alzament_pla_silkplagold_1000_175_p": "ES"
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "alzament_pla_plasilkgold_1000_175_p",
      "values": {
        "extruder_temp_range": [
          210,
          230
        ],
        "bed_temp_range": [
          45,
          60
        ]
      },
      "source": "https://www.alza.cz/alzament-pla-silk-1-kg-gold-d12869930.htm",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    }
  ],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `alzament_pla+_pla+black_1000_175_p` — PLA+ Black
- `alzament_pla+_pla+white_1000_175_p` — PLA+ White
- `alzament_pla+_pla+yellow_1000_175_p` — PLA+ Yellow
- `alzament_pla+_pla+blue_1000_175_p` — PLA+ Blue
- `alzament_pla+_pla+lavared_1000_175_p` — PLA+ Lava Red
- `alzament_pla+_pla+gold_1000_175_p` — PLA+ Gold
- `alzament_pla+_pla+silver_1000_175_p` — PLA+ Silver
- `alzament_pla+_pla+grey_1000_175_p` — PLA+ Grey
- `alzament_pla+_pla+pink_1000_175_p` — PLA+ Pink
- `alzament_pla+_pla+orange_1000_175_p` — PLA+ Orange
- `alzament_pla+_pla+green_1000_175_p` — PLA+ Green
- `alzament_pla+_pla+brown_1000_175_p` — PLA+ Brown
- `alzament_pla+_pla+beige_1000_175_p` — PLA+ Beige
- `alzament_petg_petgblack_1000_175_p` — PETG Black
- `alzament_petg_petgwhite_1000_175_p` — PETG White
- `alzament_petg_petgblue_1000_175_p` — PETG Blue
- `alzament_petg_petgred_1000_175_p` — PETG Red
- `alzament_petg_petgsilver_1000_175_p` — PETG Silver
- `alzament_petg_petgorange_1000_175_p` — PETG Orange
- `alzament_petg_petggreen_1000_175_p` — PETG Green
- `alzament_petg_petgtransparent_1000_175_p` — PETG Transparent
- `alzament_petg_petggold_1000_175_p` — PETG Gold
- `alzament_abs_absblack_1000_175_p` — ABS Black
- `alzament_abs_abswhite_1000_175_p` — ABS White
- `alzament_abs_absred_1000_175_p` — ABS Red
- `alzament_abs_absblue_1000_175_p` — ABS Blue
- `alzament_abs_absgold_1000_175_p` — ABS Gold
- `alzament_abs_abssilver_1000_175_p` — ABS Silver
- `alzament_pla_silkplasilver_1000_175_p` — Silk PLA Silver
- `alzament_pla_silkplacopper_1000_175_p` — Silk PLA Copper
- `alzament_pla_silkpladualblue-pink_1000_175_p` — Silk PLA Dual Blue-Pink
- `alzament_pla_silkpladualblack-gold_1000_175_p` — Silk PLA Dual Black-Gold
- `alzament_pla_silkplatrired-green-blue_1000_175_p` — Silk PLA Tri Red-Green-Blue
- `alzament_pla_silkplatrigold-silver-copper_1000_175_p` — Silk PLA Tri Gold-Silver-Copper
- `alzament_asa_asablack_1000_175_p` — ASA Black
- `alzament_asa_asablue_1000_175_p` — ASA Blue
- `alzament_asa_asagray_1000_175_p` — ASA Gray
- `alzament_asa_asagreen_1000_175_p` — ASA Green
- `alzament_asa_asared_1000_175_p` — ASA Red
- `alzament_asa_asawhite_1000_175_p` — ASA White
- `alzament_petg_petg-cfblack_1000_175_p` — PETG-CF Black
- `alzament_petg_petghyperblack_1000_175_p` — PETG Hyper Black
- `alzament_petg_petghyperblue_1000_175_p` — PETG Hyper Blue
- `alzament_petg_petghypergold_1000_175_p` — PETG Hyper Gold
- `alzament_petg_petghyperred_1000_175_p` — PETG Hyper Red
- `alzament_petg_petghypersilver_1000_175_p` — PETG Hyper Silver
- `alzament_petg_petghyperwhite_1000_175_p` — PETG Hyper White
- `alzament_pla_hyperpla+black_1000_175_p` — Hyper PLA+ Black
- `alzament_pla_hyperpla+blue_1000_175_p` — Hyper PLA+ Blue
- `alzament_pla_hyperpla+red_1000_175_p` — Hyper PLA+ Red
- `alzament_pla_hyperpla+white_1000_175_p` — Hyper PLA+ White
- `alzament_pla_hyperpla+yellow_1000_175_p` — Hyper PLA+ Yellow
- `alzament_pla_pla+black_1000_175_p` — PLA+ Black
- `alzament_pla_pla+blue_1000_175_p` — PLA+ Blue
- `alzament_pla_pla+red_1000_175_p` — PLA+ Red
- `alzament_pla_pla+white_1000_175_p` — PLA+ White
- `alzament_pla_pla+yellow_1000_175_p` — PLA+ Yellow
- `alzament_pla_plabasicbeige_1000_175_p` — PLA Basic Beige
- `alzament_pla_plabasicblack_1000_175_p` — PLA Basic Black
- `alzament_pla_plabasicblue_1000_175_p` — PLA Basic Blue
- `alzament_pla_plabasicfireenginered_1000_175_p` — PLA Basic Fire Engine Red
- `alzament_pla_plabasicgold_1000_175_p` — PLA Basic Gold
- `alzament_pla_plabasicgray_1000_175_p` — PLA Basic Gray
- `alzament_pla_plabasicgreen_1000_175_p` — PLA Basic Green
- `alzament_pla_plabasicmintgreen_1000_175_p` — PLA Basic Mint Green
- `alzament_pla_plabasicpurple_1000_175_p` — PLA Basic Purple
- `alzament_pla_plabasicred_1000_175_p` — PLA Basic Red
- `alzament_pla_plabasicrose_1000_175_p` — PLA Basic Rose
- `alzament_pla_plabasicsilver_1000_175_p` — PLA Basic Silver
- `alzament_pla_plabasicskyblue_1000_175_p` — PLA Basic Sky Blue
- `alzament_pla_plabasictransparent_1000_175_p` — PLA Basic Transparent
- `alzament_pla_plabasicwhite_1000_175_p` — PLA Basic White
- `alzament_pla_plabasicyellow_1000_175_p` — PLA Basic Yellow
- `alzament_pla_pla-cfblack_1000_175_p` — PLA-CF Black
- `alzament_pla_plachameleonburningtitanium_1000_175_p` — PLA Chameleon Burning Titanium
- `alzament_pla_plachameleonnebulapurple_1000_175_p` — PLA Chameleon Nebula Purple
- `alzament_pla_plamatteblack_1000_175_p` — PLA Matte Black
- `alzament_pla_plamatteblue_1000_175_p` — PLA Matte Blue
- `alzament_pla_plamattegreen_1000_175_p` — PLA Matte Green
- `alzament_pla_plamatteorange_1000_175_p` — PLA Matte Orange
- `alzament_pla_plamattepink_1000_175_p` — PLA Matte Pink
- `alzament_pla_plamattered_1000_175_p` — PLA Matte Red
- `alzament_pla_plamattewhite_1000_175_p` — PLA Matte White
- `alzament_pla_plamatteyellow_1000_175_p` — PLA Matte Yellow
- `alzament_pla_plasilkblack_1000_175_p` — PLA Silk Black
- `alzament_pla_plasilkblue_1000_175_p` — PLA Silk Blue
- `alzament_pla_plasilkcandyblack-silver_1000_175_p` — PLA Silk Candy Black-Silver
- `alzament_pla_plasilkcandyblue-green_1000_175_p` — PLA Silk Candy Blue-Green
- `alzament_pla_plasilkcandyblue-silver_1000_175_p` — PLA Silk Candy Blue-Silver
- `alzament_pla_plasilkcandygold-blue-green_1000_175_p` — PLA Silk Candy Gold-Blue-Green
- `alzament_pla_plasilkcandygold-red_1000_175_p` — PLA Silk Candy Gold-Red
- `alzament_pla_plasilkcandyred-gold-blue_1000_175_p` — PLA Silk Candy Red-Gold-Blue
- `alzament_pla_plasilkdualcolorblack-gold_1000_175_p` — PLA Silk Dual Color Black-Gold
- `alzament_pla_plasilkdualcolorblack-purple_1000_175_p` — PLA Silk Dual Color Black-Purple
- `alzament_pla_plasilkdualcolorblack-rosered_1000_175_p` — PLA Silk Dual Color Black-Rose Red
- `alzament_pla_plasilkdualcolorblue-green_1000_175_p` — PLA Silk Dual Color Blue-Green
- `alzament_pla_plasilkdualcolorblue-pink_1000_175_p` — PLA Silk Dual Color Blue-Pink
- `alzament_pla_plasilkdualcolorred-gold_1000_175_p` — PLA Silk Dual Color Red-Gold
- `alzament_pla_plasilkdualcolorred-green_1000_175_p` — PLA Silk Dual Color Red-Green
- `alzament_pla_plasilkdualcolourblack-gold_1000_175_p` — PLA Silk Dual colour Black-Gold
- `alzament_pla_plasilkdualcolourblack-purple_1000_175_p` — PLA Silk Dual colour Black-Purple
- `alzament_pla_plasilkdualcolourblack-rosered_1000_175_p` — PLA Silk Dual colour Black-Rose Red
- `alzament_pla_plasilkdualcolourblue-pink_1000_175_p` — PLA Silk Dual colour Blue-Pink
- `alzament_pla_plasilkdualcolourred-gold_1000_175_p` — PLA Silk Dual colour Red-Gold
- `alzament_pla_plasilkdualcolourred-green_1000_175_p` — PLA Silk Dual colour Red-Green
- `alzament_pla_plasilkgray_1000_175_p` — PLA Silk Gray
- `alzament_pla_plasilkpink_1000_175_p` — PLA Silk Pink
- `alzament_pla_plasilkrainbow_1000_175_p` — PLA Silk Rainbow
- `alzament_pla_plasilkrainbowdragonpalace_1000_175_p` — PLA Silk Rainbow Dragon Palace
- `alzament_pla_plasilkrainbowflamemountain_1000_175_p` — PLA Silk Rainbow Flame Mountain
- `alzament_pla_plasilkrainbowhuaguomountain_1000_175_p` — PLA Silk Rainbow Huaguo Mountain
- `alzament_pla_plasilkrainbowjadepool_1000_175_p` — PLA Silk Rainbow Jade Pool
- `alzament_pla_plasilkrainbowmoonpalace_1000_175_p` — PLA Silk Rainbow Moon Palace
- `alzament_pla_plasilkred_1000_175_p` — PLA Silk Red
- `alzament_pla_plasilkredcopper_1000_175_p` — PLA Silk Red Copper
- `alzament_pla_plasilkroyalblue_1000_175_p` — PLA Silk Royal Blue
- `alzament_pla_plasilkskyblue_1000_175_p` — PLA Silk Sky Blue
- `alzament_pla_plasilktricolorgold-green-black_1000_175_p` — PLA Silk Tri Color Gold-Green-Black
- `alzament_pla_plasilktricolorgold-green-rose_1000_175_p` — PLA Silk Tri Color Gold-Green-Rose
- `alzament_pla_plasilktricolorgold-silver-copper_1000_175_p` — PLA Silk Tri Color Gold-Silver-Copper
- `alzament_pla_plasilktricolorred-green-blue_1000_175_p` — PLA Silk Tri Color Red-Green-Blue
- `alzament_pla_plasilktricoloryellow-blue-green_1000_175_p` — PLA Silk Tri Color Yellow-Blue-Green
- `alzament_pla_plasilktricolourgold-green-black_1000_175_p` — PLA Silk Tri colour Gold-Green-Black
- `alzament_pla_plasilktricolourgold-green-rosered_1000_175_p` — PLA Silk Tri colour Gold-Green-Rose Red
- `alzament_pla_plasilktricolourgold-silver-copper_1000_175_p` — PLA Silk Tri colour Gold-Silver-Copper
- `alzament_pla_plasilktricolourred-green-blue_1000_175_p` — PLA Silk Tri colour Red-Green-Blue
- `alzament_pla_plasilktricolouryellow-blue-green_1000_175_p` — PLA Silk Tri colour Yellow-Blue-Green
- `alzament_pla_plasilkwhite_1000_175_p` — PLA Silk White
- `alzament_tpu_tpu95ablack_1000_175_p` — TPU 95A Black
- `alzament_tpu_tpu95ablue_1000_175_p` — TPU 95A Blue
- `alzament_tpu_tpu95agray_1000_175_p` — TPU 95A Gray
- `alzament_tpu_tpu95agreen_1000_175_p` — TPU 95A Green
- `alzament_tpu_tpu95ared_1000_175_p` — TPU 95A Red
- `alzament_tpu_tpu95atranslucent_1000_175_p` — TPU 95A Translucent
- `alzament_tpu_tpu95awhite_1000_175_p` — TPU 95A White
