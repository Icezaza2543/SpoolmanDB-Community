# filamentworld duplicate migration review

Base `6e22eeab4c4ff692216cc2fd41ee5caeec96aaea`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `7aa3a6dfc46d02daac3bd3bcd31ed496e019288f6fcc8f3a18139cc68b866af4`.

## Authorization and result

{"groups": 1, "approved_groups": 0, "retired": 0, "deferred": 1, "hard_stops": 0, "before_count": 51702, "after_count": 51702, "brand_before": 143, "brand_after": 143, "registry_before": 1732, "registry_after": 1732, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

One strict line/color and Cartesian warning candidate deferred; older well-formed family is not authorization to retire an unproven weightvariant. Existing1000g SKU/750g current-page mismatch explicitly unresolved. No identifier transfers or metadata edits.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. Future reviewed retirements would not redirect external catalog lookups automatically.

## Current first-party evidence

- {"url": "https://filamentworld.de/shop/pla-filament-3d-drucker/pla-basic-filament/filamentworld-basic-pla-filament-dunkelgruen-1-75-mm/?switch_shop=b2c", "sku": "PLAXBASX175XDGR", "weight": 750, "diameter": 1.75}
- {"url": "https://filamentworld.de/fact-sheets/Filamentworld_PLA_Datenblatt.pdf", "note": "GenericPLA1.24/190–210/40–50, unheatedbed allowed; exactBasicline unverified."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### FW001: dup-461266fe7f1d4169145c930b68114c01ac4cc9c936b98588d382fd7e4a051a25

Status: DEFERRED; survivor `filamentworld_pla_plabasic-darkgreen_1000_175_p`; Strict line/color mismatch and Cartesian/malformed alternative; existingPLAXBASX175XDGR officially binds750g1.75, not source1000g. Defer all retirement/transfer pending exact weight identity review..

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filamentworld_pla_plabasic-darkgreen_1000_175_p`|`PLA {color_name}`|`Basic- Dark Green`|{"source_file": "filamentworld.json", "definition_index": 3, "weights": 2, "diameters": 1, "colors": 34, "compiled_records": 68} / False|
|`filamentworld_pla_plabasicdarkgreen_1000_175_p`|`PLA Basic {color_name}`|`Dark Green`|{"source_file": "filamentworld.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 8, "compiled_records": 8} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filamentworld_pla_plabasic-darkgreen_1000_175_p": "04A584",
    "filamentworld_pla_plabasicdarkgreen_1000_175_p": "006400"
  },
  "extruder_temp_range": {
    "filamentworld_pla_plabasic-darkgreen_1000_175_p": [
      180,
      210
    ],
    "filamentworld_pla_plabasicdarkgreen_1000_175_p": [
      190,
      230
    ]
  },
  "codes": {
    "filamentworld_pla_plabasic-darkgreen_1000_175_p": null,
    "filamentworld_pla_plabasicdarkgreen_1000_175_p": [
      "PLAXBASX175XDGR"
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

- `filamentworld_abs_absblack_1000_175_p` — ABS Black
- `filamentworld_abs_absblue_1000_175_p` — ABS Blue
- `filamentworld_abs_absdarkbrown_1000_175_p` — ABS Dark Brown
- `filamentworld_abs_absfirered_1000_175_p` — ABS Fire Red
- `filamentworld_abs_absgold_1000_175_p` — ABS Gold
- `filamentworld_abs_absgray_1000_175_p` — ABS Gray
- `filamentworld_abs_absgreen_1000_175_p` — ABS Green
- `filamentworld_abs_absmagenta_1000_175_p` — ABS Magenta
- `filamentworld_abs_absneonorange_1000_175_p` — ABS Neon Orange
- `filamentworld_abs_absneonyellow_1000_175_p` — ABS Neon Yellow
- `filamentworld_abs_absorange_1000_175_p` — ABS Orange
- `filamentworld_abs_abssilver_1000_175_p` — ABS Silver
- `filamentworld_abs_abstransparent_1000_175_p` — ABS Transparent
- `filamentworld_abs_abswhite_1000_175_p` — ABS White
- `filamentworld_abs_absyellow_1000_175_p` — ABS Yellow
- `filamentworld_abs_absdefault_1000_175_p` — ABS Default
- `filamentworld_abs_absgrassgreen_1000_175_p` — ABS Grass Green
- `filamentworld_abs_absneongreen_1000_175_p` — ABS Neon Green
- `filamentworld_abs_absskyblue_1000_175_p` — ABS Sky Blue
- `filamentworld_abs_abssnowwhite_1000_175_p` — ABS Snow White
- `filamentworld_abs_abssunyellow_1000_175_p` — ABS Sun Yellow
- `filamentworld_pla_matteplablack_1000_175_p` — Matte PLA Black
- `filamentworld_pla_matteplablue_1000_175_p` — Matte PLA Blue
- `filamentworld_pla_matteplagray_1000_175_p` — Matte PLA Gray
- `filamentworld_pla_matteplared_1000_175_p` — Matte PLA Red
- `filamentworld_pla_matteplawhite_1000_175_p` — Matte PLA White
- `filamentworld_petg_petgblack_1000_175_p` — PETG Black
- `filamentworld_petg_petgblue_1000_175_p` — PETG Blue
- `filamentworld_petg_petgbronze_1000_175_p` — PETG Bronze
- `filamentworld_petg_petgfirered_1000_175_p` — PETG Fire Red
- `filamentworld_petg_petggray_1000_175_p` — PETG Gray
- `filamentworld_petg_petggreen_1000_175_p` — PETG Green
- `filamentworld_petg_petgorange_1000_175_p` — PETG Orange
- `filamentworld_petg_petgsilver_1000_175_p` — PETG Silver
- `filamentworld_petg_petgtransparentclear_1000_175_p` — PETG Transparent Clear
- `filamentworld_petg_petgwhite_1000_175_p` — PETG White
- `filamentworld_petg_petgyellow_1000_175_p` — PETG Yellow
- `filamentworld_petg_petgcrystalclear_1000_175_p` — PETG Crystal Clear
- `filamentworld_petg_petggrassgreen_1000_175_p` — PETG Grass Green
- `filamentworld_petg_petgskyblue_1000_175_p` — PETG Sky Blue
- `filamentworld_petg_petgsnowwhite_1000_175_p` — PETG Snow White
- `filamentworld_pla_plaanthracite_750_175_p` — PLA Anthracite
- `filamentworld_pla_plablack_750_175_p` — PLA Black
- `filamentworld_pla_plablue_750_175_p` — PLA Blue
- `filamentworld_pla_pladarkbrown_750_175_p` — PLA Dark Brown
- `filamentworld_pla_plafirered_750_175_p` — PLA Fire Red
- `filamentworld_pla_plagold_750_175_p` — PLA Gold
- `filamentworld_pla_plagray_750_175_p` — PLA Gray
- `filamentworld_pla_plagreen_750_175_p` — PLA Green
- `filamentworld_pla_plamagenta_750_175_p` — PLA Magenta
- `filamentworld_pla_planatural_750_175_p` — PLA Natural
- `filamentworld_pla_planeonorange_750_175_p` — PLA Neon Orange
- `filamentworld_pla_planeonyellow_750_175_p` — PLA Neon Yellow
- `filamentworld_pla_plaorange_750_175_p` — PLA Orange
- `filamentworld_pla_plasilver_750_175_p` — PLA Silver
- `filamentworld_pla_platransparent_750_175_p` — PLA Transparent
- `filamentworld_pla_plaviolet_750_175_p` — PLA Violet
- `filamentworld_pla_plawhite_750_175_p` — PLA White
- `filamentworld_pla_playellow_750_175_p` — PLA Yellow
- `filamentworld_pla_plaanthracitegray_750_175_p` — PLA anthracite gray
- `filamentworld_pla_plabasic-darkgreen_750_175_p` — PLA Basic- Dark Green
- `filamentworld_pla_plagrassgreen_750_175_p` — PLA Grass Green
- `filamentworld_pla_plalightgray_750_175_p` — PLA ​​Light Gray
- `filamentworld_pla_planavyblue/navy_750_175_p` — PLA Navy Blue / Navy
- `filamentworld_pla_planeongreen_750_175_p` — PLA Neon Green
- `filamentworld_pla_plaplusblack_750_175_p` — PLA PLUS Black
- `filamentworld_pla_plaplusblue_750_175_p` — PLA PLUS Blue
- `filamentworld_pla_plaplusgray_750_175_p` — PLA PLUS Gray
- `filamentworld_pla_plaplusgreen_750_175_p` — PLA PLUS Green
- `filamentworld_pla_plaplusnatural_750_175_p` — PLA PLUS Natural
- `filamentworld_pla_plaplusred_750_175_p` — PLA PLUS Red
- `filamentworld_pla_plapluswhite_750_175_p` — PLA PLUS White
- `filamentworld_pla_plaskyblue_750_175_p` — PLA Sky Blue
- `filamentworld_pla_plasnowwhite_750_175_p` — PLA Snow White
- `filamentworld_pla_plasunyellow_750_175_p` — PLA Sun Yellow
- `filamentworld_pla_plaanthracite_1000_175_p` — PLA Anthracite
- `filamentworld_pla_plablack_1000_175_p` — PLA Black
- `filamentworld_pla_plablue_1000_175_p` — PLA Blue
- `filamentworld_pla_pladarkbrown_1000_175_p` — PLA Dark Brown
- `filamentworld_pla_plafirered_1000_175_p` — PLA Fire Red
- `filamentworld_pla_plagold_1000_175_p` — PLA Gold
- `filamentworld_pla_plagray_1000_175_p` — PLA Gray
- `filamentworld_pla_plagreen_1000_175_p` — PLA Green
- `filamentworld_pla_plamagenta_1000_175_p` — PLA Magenta
- `filamentworld_pla_planatural_1000_175_p` — PLA Natural
- `filamentworld_pla_planeonorange_1000_175_p` — PLA Neon Orange
- `filamentworld_pla_planeonyellow_1000_175_p` — PLA Neon Yellow
- `filamentworld_pla_plaorange_1000_175_p` — PLA Orange
- `filamentworld_pla_plasilver_1000_175_p` — PLA Silver
- `filamentworld_pla_platransparent_1000_175_p` — PLA Transparent
- `filamentworld_pla_plaviolet_1000_175_p` — PLA Violet
- `filamentworld_pla_plawhite_1000_175_p` — PLA White
- `filamentworld_pla_playellow_1000_175_p` — PLA Yellow
- `filamentworld_pla_plaanthracitegray_1000_175_p` — PLA anthracite gray
- `filamentworld_pla_plagrassgreen_1000_175_p` — PLA Grass Green
- `filamentworld_pla_plalightgray_1000_175_p` — PLA ​​Light Gray
- `filamentworld_pla_planavyblue/navy_1000_175_p` — PLA Navy Blue / Navy
- `filamentworld_pla_planeongreen_1000_175_p` — PLA Neon Green
- `filamentworld_pla_plaplusblack_1000_175_p` — PLA PLUS Black
- `filamentworld_pla_plaplusblue_1000_175_p` — PLA PLUS Blue
- `filamentworld_pla_plaplusgray_1000_175_p` — PLA PLUS Gray
- `filamentworld_pla_plaplusgreen_1000_175_p` — PLA PLUS Green
- `filamentworld_pla_plaplusnatural_1000_175_p` — PLA PLUS Natural
- `filamentworld_pla_plaplusred_1000_175_p` — PLA PLUS Red
- `filamentworld_pla_plapluswhite_1000_175_p` — PLA PLUS White
- `filamentworld_pla_plaskyblue_1000_175_p` — PLA Sky Blue
- `filamentworld_pla_plasnowwhite_1000_175_p` — PLA Snow White
- `filamentworld_pla_plasunyellow_1000_175_p` — PLA Sun Yellow
- `filamentworld_pla_plabasicdarkblue_1000_175_p` — PLA Basic Dark Blue
- `filamentworld_pla_plabasicgold_1000_175_p` — PLA Basic Gold
- `filamentworld_pla_plabasicorange_1000_175_p` — PLA Basic Orange
- `filamentworld_pla_plabasicpink_1000_175_p` — PLA Basic Pink
- `filamentworld_pla_plabasicsilver_1000_175_p` — PLA Basic Silver
- `filamentworld_pla_plabasicwintershinewhite_1000_175_p` — PLA Basic Wintershine White
- `filamentworld_pla_plabasicwondrouswhite_1000_175_p` — PLA Basic Wondrous White
- `filamentworld_pla+_plaplusblack_1000_175_p` — PLA Plus Black
- `filamentworld_pla+_plaplusblue_1000_175_p` — PLA Plus Blue
- `filamentworld_pla+_plaplusgray_1000_175_p` — PLA Plus Gray
- `filamentworld_pla+_plaplusgreen_1000_175_p` — PLA Plus Green
- `filamentworld_pla+_plaplusnatural_1000_175_p` — PLA Plus Natural
- `filamentworld_pla+_plaplusred_1000_175_p` — PLA Plus Red
- `filamentworld_pla+_plapluswhite_1000_175_p` — PLA Plus White
- `filamentworld_pla_silkplablack_1000_175_p` — Silk PLA Black
- `filamentworld_pla_silkplacopper_1000_175_p` — Silk PLA Copper
- `filamentworld_pla_silkpladarkblue_1000_175_p` — Silk PLA Dark Blue
- `filamentworld_pla_silkplagold_1000_175_p` — Silk PLA Gold
- `filamentworld_pla_silkplared_1000_175_p` — Silk PLA Red
- `filamentworld_pla_silkplasilver_1000_175_p` — Silk PLA Silver
- `filamentworld_pla_silkplaviolet_1000_175_p` — Silk PLA Violet
- `filamentworld_pla_silkplawhite_1000_175_p` — Silk PLA White
- `filamentworld_pla_silkplamagicblue-green_1000_175_p` — Silk PLA Magic Blue-Green
- `filamentworld_pla_silkplamagicblue-yellow_1000_175_p` — Silk PLA Magic Blue-Yellow
- `filamentworld_pla_silkplamagicgold-violet_1000_175_p` — Silk PLA Magic ​​Gold-Violet
- `filamentworld_pla_silkplamagicredgold_1000_175_p` — Silk PLA Magic Red Gold
- `filamentworld_pla_silkplamagicred-green_1000_175_p` — Silk PLA Magic Red-Green
- `filamentworld_pla_silkplapurple_1000_175_p` — Silk PLA Purple
- `filamentworld_pla_silkplasilvergrey_1000_175_p` — Silk PLA Silver Grey
- `filamentworld_petg_metallicsilkpetgblue_1000_175_p` — Metallic Silk PETG Blue
- `filamentworld_petg_metallicsilkpetgbronze_1000_175_p` — Metallic Silk PETG Bronze
- `filamentworld_petg_metallicsilkpetggreen_1000_175_p` — Metallic Silk PETG Green
- `filamentworld_petg_metallicsilkpetgsilver_1000_175_p` — Metallic Silk PETG Silver
