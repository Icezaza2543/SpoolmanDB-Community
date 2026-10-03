# aceaddity duplicate migration review

Base `68c532fc88c0253ae1222bae6d651d3f3e4231d6`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `0760b6ec051c841b160ba155f14d4042b99d343b5b5bff3c69dd3cf94c0a5fe0`.

## Authorization and result

{"groups": 5, "approved_groups": 4, "retired": 4, "deferred": 1, "hard_stops": 0, "before_count": 51728, "after_count": 51724, "brand_before": 71, "brand_after": 67, "registry_before": 1706, "registry_after": 1710, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Four Rule4 strict Matte groups retain larger well-formed family without Cartesian warning; identifiers already on survivors and no transfers. Marble tie is unbound with differing HEX/pattern; defer. Existing B0D97... values retained historically, not asserted newly verified manufacturer SKUs. No exact current numeric first-party evidence found; printing/density retained unresolved.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence


## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`aceaddity_pla_matteplagooseyellow_1000_175_p`|`aceaddity_pla_mattegooseyellow_1000_175_p`|`aceaddity.json::Aceaddity::Matte PLA {color_name}::Matte PLA Goose Yellow::PLA::1000::1.75::plastic::False`|
|`aceaddity_pla_matteplalightpink_1000_175_p`|`aceaddity_pla_mattelightpink_1000_175_p`|`aceaddity.json::Aceaddity::Matte PLA {color_name}::Matte PLA Light Pink::PLA::1000::1.75::plastic::False`|
|`aceaddity_pla_matteplapinkblue_1000_175_p`|`aceaddity_pla_mattepinkblue_1000_175_p`|`aceaddity.json::Aceaddity::Matte PLA {color_name}::Matte PLA Pink Blue::PLA::1000::1.75::plastic::False`|
|`aceaddity_pla_matteplawatergreen_1000_175_p`|`aceaddity_pla_mattewatergreen_1000_175_p`|`aceaddity.json::Aceaddity::Matte PLA {color_name}::Matte PLA Water Green::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### AC001: dup-215b581197e595d71341f5362d3d64aec29209bdbcedc619a130894a51ebb220

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aceaddity_pla_marblemarble_1000_175_p`|`Marble {color_name}`|`Marble`|{"source_file": "aceaddity.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 1, "compiled_records": 1} / False|
|`aceaddity_pla_marbleplamarble_1000_175_p`|`Marble PLA {color_name}`|`Marble`|{"source_file": "aceaddity.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 1, "compiled_records": 1} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "aceaddity_pla_marblemarble_1000_175_p": "C2C0BA",
    "aceaddity_pla_marbleplamarble_1000_175_p": "ADB4B9"
  },
  "pattern": {
    "aceaddity_pla_marblemarble_1000_175_p": "marble",
    "aceaddity_pla_marbleplamarble_1000_175_p": null
  },
  "codes": {
    "aceaddity_pla_marblemarble_1000_175_p": [
      "B0D97QFJLM"
    ],
    "aceaddity_pla_marbleplamarble_1000_175_p": null
  }
}
```

### AC002: dup-3f653d51ee1683239cb29de5661b97ee68b946eb8cb201be43f71c4c485fd994

Status: APPROVED; survivor `aceaddity_pla_mattegooseyellow_1000_175_p`; Rule 4.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aceaddity_pla_mattegooseyellow_1000_175_p`|`Matte {color_name}`|`Goose Yellow`|{"source_file": "aceaddity.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|
|`aceaddity_pla_matteplagooseyellow_1000_175_p`|`Matte PLA {color_name}`|`Goose Yellow`|{"source_file": "aceaddity.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "aceaddity_pla_mattegooseyellow_1000_175_p": "F5E868",
    "aceaddity_pla_matteplagooseyellow_1000_175_p": "F0C75E"
  },
  "codes": {
    "aceaddity_pla_mattegooseyellow_1000_175_p": [
      "B0D97MSJCT"
    ],
    "aceaddity_pla_matteplagooseyellow_1000_175_p": null
  }
}
```

### AC003: dup-da53a942cfcbd1dda0b5b828eae63c2db13293d0461a79298c1544bf08088534

Status: APPROVED; survivor `aceaddity_pla_mattelightpink_1000_175_p`; Rule 4.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aceaddity_pla_mattelightpink_1000_175_p`|`Matte {color_name}`|`Light Pink`|{"source_file": "aceaddity.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|
|`aceaddity_pla_matteplalightpink_1000_175_p`|`Matte PLA {color_name}`|`Light Pink`|{"source_file": "aceaddity.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "aceaddity_pla_mattelightpink_1000_175_p": "E5A6B7",
    "aceaddity_pla_matteplalightpink_1000_175_p": "FFB6C1"
  },
  "codes": {
    "aceaddity_pla_mattelightpink_1000_175_p": [
      "B0D97MP4Q6"
    ],
    "aceaddity_pla_matteplalightpink_1000_175_p": null
  }
}
```

### AC004: dup-dfae5b4b37f267f8fad0897269af0ca620fbf2876d9e6999a8f3d3f1d60b071f

Status: APPROVED; survivor `aceaddity_pla_mattepinkblue_1000_175_p`; Rule 4.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aceaddity_pla_mattepinkblue_1000_175_p`|`Matte {color_name}`|`Pink Blue`|{"source_file": "aceaddity.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|
|`aceaddity_pla_matteplapinkblue_1000_175_p`|`Matte PLA {color_name}`|`Pink Blue`|{"source_file": "aceaddity.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "aceaddity_pla_mattepinkblue_1000_175_p": "9B8EC4",
    "aceaddity_pla_matteplapinkblue_1000_175_p": "DDA0DD"
  },
  "codes": {
    "aceaddity_pla_mattepinkblue_1000_175_p": [
      "B0D97ML822"
    ],
    "aceaddity_pla_matteplapinkblue_1000_175_p": null
  }
}
```

### AC005: dup-d9bac021289c29363010ccbebb02bfec2b7f9e81aff38130a7634417c1a81b4c

Status: APPROVED; survivor `aceaddity_pla_mattewatergreen_1000_175_p`; Rule 4.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`aceaddity_pla_matteplawatergreen_1000_175_p`|`Matte PLA {color_name}`|`Water Green`|{"source_file": "aceaddity.json", "definition_index": 11, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|
|`aceaddity_pla_mattewatergreen_1000_175_p`|`Matte {color_name}`|`Water Green`|{"source_file": "aceaddity.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "aceaddity_pla_matteplawatergreen_1000_175_p": "7FFFD4",
    "aceaddity_pla_mattewatergreen_1000_175_p": "8FD4B4"
  },
  "codes": {
    "aceaddity_pla_matteplawatergreen_1000_175_p": null,
    "aceaddity_pla_mattewatergreen_1000_175_p": [
      "B0D97N8J7Q"
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

- `aceaddity_pla+_pla+black_1000_175_p` — PLA+ Black
- `aceaddity_pla+_pla+yellow_1000_175_p` — PLA+ Yellow
- `aceaddity_pla+_pla+red_1000_175_p` — PLA+ Red
- `aceaddity_pla+_pla+blue_1000_175_p` — PLA+ Blue
- `aceaddity_pla+_flashpla+black_1000_175_c` — Flash PLA+ Black
- `aceaddity_pla+_flashpla+white_1000_175_c` — Flash PLA+ White
- `aceaddity_pla+_flashpla+grey_1000_175_c` — Flash PLA+ Grey
- `aceaddity_pla+_flashpla+yellow_1000_175_c` — Flash PLA+ Yellow
- `aceaddity_pla+_flashpla+blue_1000_175_c` — Flash PLA+ Blue
- `aceaddity_pla+_flashpla+red_1000_175_c` — Flash PLA+ Red
- `aceaddity_petg_petgblack_1000_175_p` — PETG Black
- `aceaddity_petg_petgwhite_1000_175_p` — PETG White
- `aceaddity_petg_petggrey_1000_175_p` — PETG Grey
- `aceaddity_petg_petgspacegrey_1000_175_p` — PETG Space Grey
- `aceaddity_petg_petgred_1000_175_p` — PETG Red
- `aceaddity_petg_petgblue_1000_175_p` — PETG Blue
- `aceaddity_petg_petgclear_1000_175_p` — PETG Clear
- `aceaddity_pla_mattewhite_1000_175_p` — Matte White
- `aceaddity_pla_matteblack_1000_175_p` — Matte Black
- `aceaddity_pla_silkmagicdualblue&rosered_1000_175_c` — Silk Magic Dual Blue & Rose Red
- `aceaddity_pla_silkmagicdualpurple&yellow_1000_175_c` — Silk Magic Dual Purple & Yellow
- `aceaddity_pla_silkmagicdualgold&red_1000_175_c` — Silk Magic Dual Gold & Red
- `aceaddity_pla_silkmagicdualsilver&darkblue_1000_175_c` — Silk Magic Dual Silver & Dark Blue
- `aceaddity_pla_silkmagicdualblue&green_1000_175_c` — Silk Magic Dual Blue & Green
- `aceaddity_pla_silkmagicdualgold&rosered_1000_175_c` — Silk Magic Dual Gold & Rose Red
- `aceaddity_pla_silkmagictriblue-red-green_1000_175_c` — Silk Magic Tri Blue-Red-Green
- `aceaddity_pla_silkmagictriblue-purple-yellow_1000_175_c` — Silk Magic Tri Blue-Purple-Yellow
- `aceaddity_pla_silkmagictriblue-green-orange_1000_175_c` — Silk Magic Tri Blue-Green-Orange
- `aceaddity_pla_silkmagictrigold-copper-black_1000_175_c` — Silk Magic Tri Gold-Copper-Black
- `aceaddity_pla_silkmagictrigold-silver-copper_1000_175_c` — Silk Magic Tri Gold-Silver-Copper
- `aceaddity_pla_rainbowcosmic_1000_175_c` — Rainbow Cosmic
- `aceaddity_pla_rainbowcandy_1000_175_c` — Rainbow Candy
- `aceaddity_pla_rainbowforest_1000_175_c` — Rainbow Forest
- `aceaddity_pla_rainbowmacaron_1000_175_c` — Rainbow Macaron
- `aceaddity_pla_woodplabeige_1000_175_p` — Wood PLA Beige
- `aceaddity_pla_woodplawood_1000_175_p` — Wood PLA Wood
- `aceaddity_pla_flashpla+(highspeed600mm/s)black_1000_175_p` — Flash PLA+ (High Speed 600mm/s) Black
- `aceaddity_pla_flashpla+(highspeed600mm/s)blue_1000_175_p` — Flash PLA+ (High Speed 600mm/s) Blue
- `aceaddity_pla_flashpla+(highspeed600mm/s)brown_1000_175_p` — Flash PLA+ (High Speed 600mm/s) Brown
- `aceaddity_pla_flashpla+(highspeed600mm/s)gray_1000_175_p` — Flash PLA+ (High Speed 600mm/s) Gray
- `aceaddity_pla_flashpla+(highspeed600mm/s)green_1000_175_p` — Flash PLA+ (High Speed 600mm/s) Green
- `aceaddity_pla_flashpla+(highspeed600mm/s)orange_1000_175_p` — Flash PLA+ (High Speed 600mm/s) Orange
- `aceaddity_pla_flashpla+(highspeed600mm/s)pink_1000_175_p` — Flash PLA+ (High Speed 600mm/s) Pink
- `aceaddity_pla_flashpla+(highspeed600mm/s)purple_1000_175_p` — Flash PLA+ (High Speed 600mm/s) Purple
- `aceaddity_pla_flashpla+(highspeed600mm/s)red_1000_175_p` — Flash PLA+ (High Speed 600mm/s) Red
- `aceaddity_pla_flashpla+(highspeed600mm/s)white_1000_175_p` — Flash PLA+ (High Speed 600mm/s) White
- `aceaddity_pla_flashpla+(highspeed600mm/s)yellow_1000_175_p` — Flash PLA+ (High Speed 600mm/s) Yellow
- `aceaddity_pla_pla+black_1000_175_p` — PLA+ Black
- `aceaddity_pla_pla+blue_1000_175_p` — PLA+ Blue
- `aceaddity_pla_pla+brown_1000_175_p` — PLA+ Brown
- `aceaddity_pla_pla+gray_1000_175_p` — PLA+ Gray
- `aceaddity_pla_pla+green_1000_175_p` — PLA+ Green
- `aceaddity_pla_pla+orange_1000_175_p` — PLA+ Orange
- `aceaddity_pla_pla+pink_1000_175_p` — PLA+ Pink
- `aceaddity_pla_pla+purple_1000_175_p` — PLA+ Purple
- `aceaddity_pla_pla+red_1000_175_p` — PLA+ Red
- `aceaddity_pla_pla+white_1000_175_p` — PLA+ White
- `aceaddity_pla_pla+yellow_1000_175_p` — PLA+ Yellow
- `aceaddity_pla_silkmagicplabluerosered_1000_175_p` — Silk Magic PLA Blue Rose Red
- `aceaddity_pla_silkmagicplagoldcopperblack_1000_175_p` — Silk Magic PLA Gold Copper Black
- `aceaddity_pla_silkmagicplagoldrosered_1000_175_p` — Silk Magic PLA Gold Rose Red
