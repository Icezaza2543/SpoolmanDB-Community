# nobufil duplicate migration review

Base `8d68c8f08374181a45a4092c1918ed32b477e667`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `b3d37bc43c696cb19bddc4b718b9462614cbb1adf04d9bbc0b4819c5efe266bb`.

## Authorization and result

{"groups": 5, "approved_groups": 5, "retired": 5, "deferred": 0, "hard_stops": 0, "before_count": 51724, "after_count": 51719, "brand_before": 119, "brand_after": 114, "registry_before": 1710, "registry_after": 1715, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Five Rule1 strict ordinary PETG duplicates. Existing density1.27/nozzle235/bed75 corroborated by exact current-linked TDS; keep valid points. CurrentBlue code is not imported or fanned out. No identifiers on retiring records; packaging/tare untouched.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://www.nobufil.com/product-page/petg-filament-blue", "note": "Ordinary plain PETG, not Industrial or Candy."}
- {"url": "https://www.nobufil.com/_files/ugd/c9047f_bfc04fd990cb4d21a3805af1e1a2dd78.pdf", "density": 1.27, "nozzle": [225, 245], "bed": [65, 85], "version": "23.12"}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`nobufil_petg_petgblack_1000_175_c`|`nobufil_petg_black_1000_175_c`|`nobufil.json::Nobufil::PETG {color_name}::PETG Black::PETG::1000::1.75::cardboard::False`|
|`nobufil_petg_petgblue_1000_175_c`|`nobufil_petg_blue_1000_175_c`|`nobufil.json::Nobufil::PETG {color_name}::PETG Blue::PETG::1000::1.75::cardboard::False`|
|`nobufil_petg_petggreen_1000_175_c`|`nobufil_petg_green_1000_175_c`|`nobufil.json::Nobufil::PETG {color_name}::PETG Green::PETG::1000::1.75::cardboard::False`|
|`nobufil_petg_petgwhite_1000_175_c`|`nobufil_petg_white_1000_175_c`|`nobufil.json::Nobufil::PETG {color_name}::PETG White::PETG::1000::1.75::cardboard::False`|
|`nobufil_petg_petgyellow_1000_175_c`|`nobufil_petg_yellow_1000_175_c`|`nobufil.json::Nobufil::PETG {color_name}::PETG Yellow::PETG::1000::1.75::cardboard::False`|

## Per-group decisions and unresolved metadata

### NO001: dup-ba3dd034d5f54e1b822d12621658f34e78168656056fdd57341781afa816dd0b

Status: APPROVED; survivor `nobufil_petg_black_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`nobufil_petg_black_1000_175_c`|`{color_name}`|`Black`|{"source_file": "nobufil.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|
|`nobufil_petg_petgblack_1000_175_c`|`PETG {color_name}`|`Black`|{"source_file": "nobufil.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "nobufil_petg_black_1000_175_c": 234,
    "nobufil_petg_petgblack_1000_175_c": null
  },
  "extruder_temp": {
    "nobufil_petg_black_1000_175_c": 235,
    "nobufil_petg_petgblack_1000_175_c": null
  },
  "extruder_temp_range": {
    "nobufil_petg_black_1000_175_c": null,
    "nobufil_petg_petgblack_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "nobufil_petg_black_1000_175_c": 75,
    "nobufil_petg_petgblack_1000_175_c": null
  },
  "bed_temp_range": {
    "nobufil_petg_black_1000_175_c": null,
    "nobufil_petg_petgblack_1000_175_c": [
      70,
      90
    ]
  }
}
```

### NO002: dup-672236bda1ee7a0623899698847a47ae707acb7755618a9738a4ca403bbcf89b

Status: APPROVED; survivor `nobufil_petg_blue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`nobufil_petg_blue_1000_175_c`|`{color_name}`|`Blue`|{"source_file": "nobufil.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|
|`nobufil_petg_petgblue_1000_175_c`|`PETG {color_name}`|`Blue`|{"source_file": "nobufil.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "nobufil_petg_blue_1000_175_c": 234,
    "nobufil_petg_petgblue_1000_175_c": null
  },
  "color_hex": {
    "nobufil_petg_blue_1000_175_c": "0000FF",
    "nobufil_petg_petgblue_1000_175_c": "0078BF"
  },
  "extruder_temp": {
    "nobufil_petg_blue_1000_175_c": 235,
    "nobufil_petg_petgblue_1000_175_c": null
  },
  "extruder_temp_range": {
    "nobufil_petg_blue_1000_175_c": null,
    "nobufil_petg_petgblue_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "nobufil_petg_blue_1000_175_c": 75,
    "nobufil_petg_petgblue_1000_175_c": null
  },
  "bed_temp_range": {
    "nobufil_petg_blue_1000_175_c": null,
    "nobufil_petg_petgblue_1000_175_c": [
      70,
      90
    ]
  }
}
```

### NO003: dup-c8f74587ebecd77cd3f0d2e4c2dd4a2990d68593d8faccd78e9fb524f1e3cf59

Status: APPROVED; survivor `nobufil_petg_green_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`nobufil_petg_green_1000_175_c`|`{color_name}`|`Green`|{"source_file": "nobufil.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|
|`nobufil_petg_petggreen_1000_175_c`|`PETG {color_name}`|`Green`|{"source_file": "nobufil.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "nobufil_petg_green_1000_175_c": 234,
    "nobufil_petg_petggreen_1000_175_c": null
  },
  "color_hex": {
    "nobufil_petg_green_1000_175_c": "00FF00",
    "nobufil_petg_petggreen_1000_175_c": "317C2E"
  },
  "extruder_temp": {
    "nobufil_petg_green_1000_175_c": 235,
    "nobufil_petg_petggreen_1000_175_c": null
  },
  "extruder_temp_range": {
    "nobufil_petg_green_1000_175_c": null,
    "nobufil_petg_petggreen_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "nobufil_petg_green_1000_175_c": 75,
    "nobufil_petg_petggreen_1000_175_c": null
  },
  "bed_temp_range": {
    "nobufil_petg_green_1000_175_c": null,
    "nobufil_petg_petggreen_1000_175_c": [
      70,
      90
    ]
  }
}
```

### NO004: dup-c67dc3ef6c5d97645383ecfa743b66955ad26e6d6454a8775af8f36d1e6665ed

Status: APPROVED; survivor `nobufil_petg_white_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`nobufil_petg_petgwhite_1000_175_c`|`PETG {color_name}`|`White`|{"source_file": "nobufil.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|
|`nobufil_petg_white_1000_175_c`|`{color_name}`|`White`|{"source_file": "nobufil.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "nobufil_petg_petgwhite_1000_175_c": null,
    "nobufil_petg_white_1000_175_c": 234
  },
  "extruder_temp": {
    "nobufil_petg_petgwhite_1000_175_c": null,
    "nobufil_petg_white_1000_175_c": 235
  },
  "extruder_temp_range": {
    "nobufil_petg_petgwhite_1000_175_c": [
      220,
      250
    ],
    "nobufil_petg_white_1000_175_c": null
  },
  "bed_temp": {
    "nobufil_petg_petgwhite_1000_175_c": null,
    "nobufil_petg_white_1000_175_c": 75
  },
  "bed_temp_range": {
    "nobufil_petg_petgwhite_1000_175_c": [
      70,
      90
    ],
    "nobufil_petg_white_1000_175_c": null
  }
}
```

### NO005: dup-aa881cd4191f5146d5ef3155ef569e043a7bfd604aa9eb9757a08c96edbc7dd3

Status: APPROVED; survivor `nobufil_petg_yellow_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`nobufil_petg_petgyellow_1000_175_c`|`PETG {color_name}`|`Yellow`|{"source_file": "nobufil.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|
|`nobufil_petg_yellow_1000_175_c`|`{color_name}`|`Yellow`|{"source_file": "nobufil.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "nobufil_petg_petgyellow_1000_175_c": null,
    "nobufil_petg_yellow_1000_175_c": 234
  },
  "color_hex": {
    "nobufil_petg_petgyellow_1000_175_c": "FFD342",
    "nobufil_petg_yellow_1000_175_c": "FFFF00"
  },
  "extruder_temp": {
    "nobufil_petg_petgyellow_1000_175_c": null,
    "nobufil_petg_yellow_1000_175_c": 235
  },
  "extruder_temp_range": {
    "nobufil_petg_petgyellow_1000_175_c": [
      220,
      250
    ],
    "nobufil_petg_yellow_1000_175_c": null
  },
  "bed_temp": {
    "nobufil_petg_petgyellow_1000_175_c": null,
    "nobufil_petg_yellow_1000_175_c": 75
  },
  "bed_temp_range": {
    "nobufil_petg_petgyellow_1000_175_c": [
      70,
      90
    ],
    "nobufil_petg_yellow_1000_175_c": null
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

- `nobufil_petg_brown_1000_175_c` — Brown
- `nobufil_petg_classicgrey_1000_175_c` — Classic Grey
- `nobufil_petg_industrialdarkgrey_1000_175_c` — Industrial Dark Grey
- `nobufil_plax_mattewhite_1000_175_c` — Matte White
- `nobufil_plax_matteblack_1000_175_c` — Matte Black
- `nobufil_plax_matteartistgrey_1000_175_c` — Matte Artist Grey
- `nobufil_petg_matteblack_1000_175_c` — Matte Black
- `nobufil_pla-cf_black_1000_175_c` — Black
- `nobufil_abs_absxaluminumgray_1000_175_c` — ABS x Aluminum Gray
- `nobufil_abs_absxarcticwhite_1000_175_c` — ABS x Arctic White
- `nobufil_abs_absxblack_1000_175_c` — ABS x Black
- `nobufil_abs_absxbrightmagenta_1000_175_c` — ABS x Bright Magenta
- `nobufil_abs_absxbronze_1000_175_c` — ABS x Bronze
- `nobufil_abs_absxcopper_1000_175_c` — ABS x Copper
- `nobufil_abs_absxdarkpurple_1000_175_c` — ABS x Dark Purple
- `nobufil_abs_absxlimegreen_1000_175_c` — ABS x Lime Green
- `nobufil_abs_absxmarblewhite_1000_175_c` — ABS x Marble White
- `nobufil_abs_absxorchidpurple_1000_175_c` — ABS x Orchid Purple
- `nobufil_abs_absxpearlwhite_1000_175_c` — ABS x Pearl White
- `nobufil_abs_absxsilver_1000_175_c` — ABS x Silver
- `nobufil_abs_absxstainlesssteel_1000_175_c` — ABS x Stainless Steel
- `nobufil_abs_absxwhite_1000_175_c` — ABS x White
- `nobufil_abs_glowabsblue_1000_175_c` — Glow ABS Blue
- `nobufil_abs_glowabsgreen_1000_175_c` — Glow ABS Green
- `nobufil_abs_xastroabsblack_1000_175_c` — X Astro ABS Black
- `nobufil_abs_xastroabsblue_1000_175_c` — X Astro ABS Blue
- `nobufil_abs_xastroabsgray_1000_175_c` — X Astro ABS Gray
- `nobufil_abs_xastroabsgreen_1000_175_c` — X Astro ABS Green
- `nobufil_abs_xastroabspurple_1000_175_c` — X Astro ABS Purple
- `nobufil_abs_xastroabsred_1000_175_c` — X Astro ABS Red
- `nobufil_abs_xcandyabsblue_1000_175_c` — X Candy ABS Blue
- `nobufil_abs_xcandyabsgreen_1000_175_c` — X Candy ABS Green
- `nobufil_abs_xcandyabsiceblue_1000_175_c` — X Candy ABS Ice Blue
- `nobufil_abs_xcandyabsneongreen_1000_175_c` — X Candy ABS Neon Green
- `nobufil_abs_xcandyabsred_1000_175_c` — X Candy ABS Red
- `nobufil_abs_xcandyabssmokegrey_1000_175_c` — X Candy ABS Smoke Grey
- `nobufil_abs_xindustrialabsbeige_1000_175_c` — X Industrial ABS Beige
- `nobufil_abs_xindustrialabsblue_1000_175_c` — X Industrial ABS Blue
- `nobufil_abs_xindustrialabsbrown_1000_175_c` — X Industrial ABS Brown
- `nobufil_abs_xindustrialabsdarkgrey_1000_175_c` — X Industrial ABS Dark Grey
- `nobufil_abs_xindustrialabsgreen_1000_175_c` — X Industrial ABS Green
- `nobufil_abs_xindustrialabslightgreen_1000_175_c` — X Industrial ABS Light Green
- `nobufil_abs_xindustrialabslightgrey_1000_175_c` — X Industrial ABS Light Grey
- `nobufil_abs_xindustrialabsorange_1000_175_c` — X Industrial ABS Orange
- `nobufil_abs_xindustrialabsred_1000_175_c` — X Industrial ABS Red
- `nobufil_abs_xindustrialabsteal_1000_175_c` — X Industrial ABS Teal
- `nobufil_abs_xindustrialabsturquoise_1000_175_c` — X Industrial ABS Turquoise
- `nobufil_abs_xindustrialabsyellow_1000_175_c` — X Industrial ABS Yellow
- `nobufil_abs_xmattmatteabsblack_1000_175_c` — X Matt Matte ABS Black
- `nobufil_abs_xmattmatteabsdesertsand_1000_175_c` — X Matt Matte ABS Desert Sand
- `nobufil_abs_xmattmatteabsnavyblue_1000_175_c` — X Matt Matte ABS Navy Blue
- `nobufil_abs_xmattmatteabsolivegreen_1000_175_c` — X Matt Matte ABS Olive Green
- `nobufil_abs_xmattmatteabsstonegrey_1000_175_c` — X Matt Matte ABS Stone Grey
- `nobufil_abs_xneonabsorange_1000_175_c` — X Neon ABS Orange
- `nobufil_abs_xneonabspink_1000_175_c` — X Neon ABS Pink
- `nobufil_abs_xneonabsyellow_1000_175_c` — X Neon ABS Yellow
- `nobufil_asa_asablack_1000_175_c` — ASA Black
- `nobufil_asa_xcfcfasaanthracite_1000_175_c` — X CF CF ASA Anthracite
- `nobufil_asa_xcfcfasablack_1000_175_c` — X CF CF ASA Black
- `nobufil_pctg_pctgaluminumgray_1000_175_c` — PCTG Aluminum Gray
- `nobufil_pctg_pctgblack_1000_175_c` — PCTG Black
- `nobufil_pctg_pctgcandyblue_1000_175_c` — PCTG Candy Blue
- `nobufil_pctg_pctgcandygreen_1000_175_c` — PCTG Candy Green
- `nobufil_pctg_pctgcandyred_1000_175_c` — PCTG Candy Red
- `nobufil_pctg_pctgindustrialblue_1000_175_c` — PCTG Industrial Blue
- `nobufil_pctg_pctgindustriallightgreen_1000_175_c` — PCTG Industrial Light Green
- `nobufil_pctg_pctgindustrialneonyellow_1000_175_c` — PCTG Industrial Neon Yellow
- `nobufil_pctg_pctgindustrialorange_1000_175_c` — PCTG Industrial Orange
- `nobufil_pctg_pctgindustrialteal_1000_175_c` — PCTG Industrial Teal
- `nobufil_pctg_pctgindustrialturquoise_1000_175_c` — PCTG Industrial Turquoise
- `nobufil_pctg_pctglimegreen_1000_175_c` — PCTG Lime Green
- `nobufil_pctg_pctgneonorange_1000_175_c` — PCTG Neon Orange
- `nobufil_pctg_pctgstainlesssteel_1000_175_c` — PCTG Stainless Steel
- `nobufil_pctg_pctgwhite_1000_175_c` — PCTG White
- `nobufil_pctg_pctgcfblack_1000_175_c` — PCTG CF Black
- `nobufil_petg_glowpetgblue_1000_175_c` — Glow PETG Blue
- `nobufil_petg_glowpetggreen_1000_175_c` — Glow PETG Green
- `nobufil_petg_mattepetgmattblack_1000_175_c` — Matte PETG Matt Black
- `nobufil_petg_petgalugrey_1000_175_c` — PETG Alu Grey
- `nobufil_petg_petgastroblack_1000_175_c` — PETG Astro Black
- `nobufil_petg_petgastrogray_1000_175_c` — PETG Astro Gray
- `nobufil_petg_petgbrightmagenta_1000_175_c` — PETG Bright Magenta
- `nobufil_petg_petgcandyblue_1000_175_c` — PETG Candy Blue
- `nobufil_petg_petgcandygreen_1000_175_c` — PETG Candy Green
- `nobufil_petg_petgcandyred_1000_175_c` — PETG Candy Red
- `nobufil_petg_petgclear_1000_175_c` — PETG Clear
- `nobufil_petg_petgdarkpurple_1000_175_c` — PETG Dark Purple
- `nobufil_petg_petgindustrialblue_1000_175_c` — PETG Industrial Blue
- `nobufil_petg_petgindustrialbrown_1000_175_c` — PETG Industrial Brown
- `nobufil_petg_petgindustriallightgreen_1000_175_c` — PETG Industrial Light Green
- `nobufil_petg_petgindustrialorange_1000_175_c` — PETG Industrial Orange
- `nobufil_petg_petgindustrialteal_1000_175_c` — PETG Industrial Teal
- `nobufil_petg_petgindustrialturquoise_1000_175_c` — PETG Industrial Turquoise
- `nobufil_petg_petglimegreen_1000_175_c` — PETG Lime Green
- `nobufil_petg_petgmarblewhite_1000_175_c` — PETG Marble White
- `nobufil_petg_petgneonorange_1000_175_c` — PETG Neon Orange
- `nobufil_petg_petgneonpink_1000_175_c` — PETG Neon Pink
- `nobufil_petg_petgneonyellow_1000_175_c` — PETG Neon Yellow
- `nobufil_petg_petgorange_1000_175_c` — PETG Orange
- `nobufil_petg_petgpearlwhite_1000_175_c` — PETG Pearl White
- `nobufil_petg_petgred_1000_175_c` — PETG Red
- `nobufil_petg_petgsilver_1000_175_c` — PETG Silver
- `nobufil_petg_petgstainlesssteel_1000_175_c` — PETG Stainless Steel
- `nobufil_petg_petgcfblack_1000_175_c` — PETG CF Black
- `nobufil_petg_petgcfdarkblue_1000_175_c` — PETG CF Dark Blue
- `nobufil_petg_petgcfdarkburgundy_1000_175_c` — PETG CF Dark Burgundy
- `nobufil_petg_petgcfdarkgreen_1000_175_c` — PETG CF Dark Green
- `nobufil_petg_petgcfdarkgrey_1000_175_c` — PETG CF Dark Grey
- `nobufil_pla_placfxcfblack_1000_175_c` — PLA CF x CF Black
