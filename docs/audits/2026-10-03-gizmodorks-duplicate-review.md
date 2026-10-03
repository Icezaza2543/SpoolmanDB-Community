# gizmodorks duplicate migration review

Base `35a494b676f206b8e749667d4eb1cdeeffce2fe7`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `3e2acf1ffec0328a130273a7c8557c0693f7a581db31044d1036c54b4b017258`.

## Authorization and result

{"groups": 65, "approved_groups": 55, "retired": 55, "deferred": 10, "hard_stops": 0, "before_count": 52294, "after_count": 52239, "brand_before": 294, "brand_after": 239, "registry_before": 1140, "registry_after": 1195, "metadata_fields_changed": 165, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Apply current exact 1kg PLA/ABS/PETG product-line nozzle and explicitly recommended bed values to safe survivor IDs only. Density stays unchanged without current exact density proof. Fluorescent/Glow line-color decompositions defer; no guessed color binding. All HEX and packaging/tare conflicts retained unchanged.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://gizmodorks.com/abs-3d-printer-filament/", "package": "1kg product line", "nozzle": [230, 250], "bed": 110, "note": "Not the distinct Low Odor ABS or200g product, which list225–250/80–110."}
- {"url": "https://gizmodorks.com/pla-3d-printer-filament/", "package": "1kg product line", "nozzle": [190, 225], "bed": 60}
- {"url": "https://gizmodorks.com/petg-3d-printer-filament/", "package": "1kg product line", "nozzle": [230, 260], "bed": 80}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`gizmodorks_abs_gizmodorksabsbeige_1000_175_p`|`gizmodorks_abs_absbeige_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Beige::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabsblack_1000_175_p`|`gizmodorks_abs_absblack_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Black::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabsblue_1000_175_p`|`gizmodorks_abs_absblue_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Blue::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabsbrown_1000_175_p`|`gizmodorks_abs_absbrown_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Brown::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabsconductiveblack_1000_175_p`|`gizmodorks_abs_absconductiveblack_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Conductive Black::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabsdarkblue_1000_175_p`|`gizmodorks_abs_absdarkblue_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Dark Blue::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabsdarkpurple_1000_175_p`|`gizmodorks_abs_absdarkpurple_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Dark Purple::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabsgold_1000_175_p`|`gizmodorks_abs_absgold_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Gold::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabsgrassgreen_1000_175_p`|`gizmodorks_abs_absgrassgreen_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Grass Green::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabsgreen_1000_175_p`|`gizmodorks_abs_absgreen_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Green::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabsgrey_1000_175_p`|`gizmodorks_abs_absgrey_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Grey::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabsorange_1000_175_p`|`gizmodorks_abs_absorange_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Orange::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabspink_1000_175_p`|`gizmodorks_abs_abspink_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Pink::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabspinkrose_1000_175_p`|`gizmodorks_abs_abspinkrose_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Pink Rose::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabspurple_1000_175_p`|`gizmodorks_abs_abspurple_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Purple::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabsred_1000_175_p`|`gizmodorks_abs_absred_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Red::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabsredlava_1000_175_p`|`gizmodorks_abs_absredlava_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Red Lava::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabssilver_1000_175_p`|`gizmodorks_abs_abssilver_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Silver::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabstransparent_1000_175_p`|`gizmodorks_abs_abstransparent_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Transparent::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabsviolet_1000_175_p`|`gizmodorks_abs_absviolet_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Violet::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabswhite_1000_175_p`|`gizmodorks_abs_abswhite_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS White::ABS::1000::1.75::plastic::False`|
|`gizmodorks_abs_gizmodorksabsyellow_1000_175_p`|`gizmodorks_abs_absyellow_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks ABS {color_name}::Gizmo Dorks ABS Yellow::ABS::1000::1.75::plastic::False`|
|`gizmodorks_petg_gizmodorkspetgblack_1000_175_p`|`gizmodorks_petg_petgblack_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PETG {color_name}::Gizmo Dorks PETG Black::PETG::1000::1.75::plastic::False`|
|`gizmodorks_petg_gizmodorkspetgtranslucentblue_1000_175_p`|`gizmodorks_petg_petgtranslucentblue_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PETG {color_name}::Gizmo Dorks PETG Translucent Blue::PETG::1000::1.75::plastic::False`|
|`gizmodorks_petg_gizmodorkspetgtranslucentgreen_1000_175_p`|`gizmodorks_petg_petgtranslucentgreen_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PETG {color_name}::Gizmo Dorks PETG Translucent Green::PETG::1000::1.75::plastic::False`|
|`gizmodorks_petg_gizmodorkspetgtranslucentred_1000_175_p`|`gizmodorks_petg_petgtranslucentred_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PETG {color_name}::Gizmo Dorks PETG Translucent Red::PETG::1000::1.75::plastic::False`|
|`gizmodorks_petg_gizmodorkspetgtransparent_1000_175_p`|`gizmodorks_petg_petgtransparent_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PETG {color_name}::Gizmo Dorks PETG Transparent::PETG::1000::1.75::plastic::False`|
|`gizmodorks_petg_gizmodorkspetgwhite_1000_175_p`|`gizmodorks_petg_petgwhite_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PETG {color_name}::Gizmo Dorks PETG White::PETG::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplabeige_1000_175_p`|`gizmodorks_pla_plabeige_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Beige::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplablack_1000_175_p`|`gizmodorks_pla_plablack_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Black::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplablue_1000_175_p`|`gizmodorks_pla_plablue_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Blue::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplabrown_1000_175_p`|`gizmodorks_pla_plabrown_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Brown::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorkspladarkblue_1000_175_p`|`gizmodorks_pla_pladarkblue_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Dark Blue::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorkspladarkbrown_1000_175_p`|`gizmodorks_pla_pladarkbrown_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Dark Brown::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplagold_1000_175_p`|`gizmodorks_pla_plagold_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Gold::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplagrassgreen_1000_175_p`|`gizmodorks_pla_plagrassgreen_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Grass Green::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplagreen(translucent)_1000_175_p`|`gizmodorks_pla_plagreen(translucent)_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Green (Translucent)::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplagreen_1000_175_p`|`gizmodorks_pla_plagreen_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Green::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplagrey_1000_175_p`|`gizmodorks_pla_plagrey_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Grey::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplalightyellow_1000_175_p`|`gizmodorks_pla_plalightyellow_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Light Yellow::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplaorange(translucent)_1000_175_p`|`gizmodorks_pla_plaorange(translucent)_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Orange (Translucent)::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplaorange_1000_175_p`|`gizmodorks_pla_plaorange_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Orange::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplapink(translucent)_1000_175_p`|`gizmodorks_pla_plapink(translucent)_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Pink (Translucent)::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplapink_1000_175_p`|`gizmodorks_pla_plapink_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Pink::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplapinkrose_1000_175_p`|`gizmodorks_pla_plapinkrose_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Pink Rose::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplapurple(translucent)_1000_175_p`|`gizmodorks_pla_plapurple(translucent)_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Purple (Translucent)::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplapurple_1000_175_p`|`gizmodorks_pla_plapurple_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Purple::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplared(translucent)_1000_175_p`|`gizmodorks_pla_plared(translucent)_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Red (Translucent)::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplared_1000_175_p`|`gizmodorks_pla_plared_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Red::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplaredlava_1000_175_p`|`gizmodorks_pla_plaredlava_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Red Lava::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplasilver_1000_175_p`|`gizmodorks_pla_plasilver_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Silver::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplatransparent_1000_175_p`|`gizmodorks_pla_platransparent_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Transparent::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplaviolet_1000_175_p`|`gizmodorks_pla_plaviolet_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Violet::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplawhite_1000_175_p`|`gizmodorks_pla_plawhite_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA White::PLA::1000::1.75::plastic::False`|
|`gizmodorks_pla_gizmodorksplayellow_1000_175_p`|`gizmodorks_pla_playellow_1000_175_p`|`gizmodorks.json::Gizmo Dorks::Gizmo Dorks PLA {color_name}::Gizmo Dorks PLA Yellow::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### GD001: dup-b46474fa7aa3df1191642faccf3ed439be20a0b53636e05392e3011ef1005b13

Status: APPROVED; survivor `gizmodorks_abs_absbeige_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_absbeige_1000_175_p`|`ABS {color_name}`|`Beige`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabsbeige_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Beige`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_absbeige_1000_175_p": "E2C077",
    "gizmodorks_abs_gizmodorksabsbeige_1000_175_p": "f5f5dc"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_absbeige_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsbeige_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_absbeige_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsbeige_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_absbeige_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsbeige_1000_175_p": null
  }
}
```

### GD002: dup-c422c2dbfe98405ff34f9e79201237aef599e05bc1b78b963842bdf0a59e3749

Status: APPROVED; survivor `gizmodorks_abs_absblack_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_absblack_1000_175_p`|`ABS {color_name}`|`Black`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabsblack_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Black`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp_range": {
    "gizmodorks_abs_absblack_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsblack_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_absblack_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsblack_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_absblack_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsblack_1000_175_p": null
  }
}
```

### GD003: dup-03ebe5a528be4adfb28d965732e9f9f7abbb931df5396e26741505e18338e512

Status: APPROVED; survivor `gizmodorks_abs_absblue_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_absblue_1000_175_p`|`ABS {color_name}`|`Blue`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabsblue_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Blue`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_absblue_1000_175_p": "2E56F1",
    "gizmodorks_abs_gizmodorksabsblue_1000_175_p": "0066cc"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_absblue_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsblue_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_absblue_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsblue_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_absblue_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsblue_1000_175_p": null
  }
}
```

### GD004: dup-d81bf1ec74e8afe32db3d293a1e38bcc6dc2ecde0cb41fe36db361afe909cdfe

Status: APPROVED; survivor `gizmodorks_abs_absbrown_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_absbrown_1000_175_p`|`ABS {color_name}`|`Brown`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabsbrown_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Brown`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_absbrown_1000_175_p": "A45B27",
    "gizmodorks_abs_gizmodorksabsbrown_1000_175_p": "8b4513"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_absbrown_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsbrown_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_absbrown_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsbrown_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_absbrown_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsbrown_1000_175_p": null
  }
}
```

### GD005: dup-dd98796bdca9f5286a878a729952ad855a5aecadb2ac61056aee4a182a10a798

Status: APPROVED; survivor `gizmodorks_abs_absconductiveblack_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_absconductiveblack_1000_175_p`|`ABS {color_name}`|`Conductive Black`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabsconductiveblack_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Conductive Black`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_absconductiveblack_1000_175_p": "000000",
    "gizmodorks_abs_gizmodorksabsconductiveblack_1000_175_p": "1a1a1a"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_absconductiveblack_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsconductiveblack_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_absconductiveblack_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsconductiveblack_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_absconductiveblack_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsconductiveblack_1000_175_p": null
  }
}
```

### GD006: dup-0c4490d266d52a2a084dd76d5d092c5a1852b39207bcc393027126c85b7e2baf

Status: APPROVED; survivor `gizmodorks_abs_absdarkblue_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_absdarkblue_1000_175_p`|`ABS {color_name}`|`Dark Blue`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabsdarkblue_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Dark Blue`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_absdarkblue_1000_175_p": "003287",
    "gizmodorks_abs_gizmodorksabsdarkblue_1000_175_p": "00008b"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_absdarkblue_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsdarkblue_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_absdarkblue_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsdarkblue_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_absdarkblue_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsdarkblue_1000_175_p": null
  }
}
```

### GD007: dup-395054c79027dbac8a17047e0f60e32a24acdbefa031944a67266666fe647d52

Status: APPROVED; survivor `gizmodorks_abs_absdarkpurple_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_absdarkpurple_1000_175_p`|`ABS {color_name}`|`Dark Purple`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabsdarkpurple_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Dark Purple`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_absdarkpurple_1000_175_p": "663D7E",
    "gizmodorks_abs_gizmodorksabsdarkpurple_1000_175_p": "4b0082"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_absdarkpurple_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsdarkpurple_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_absdarkpurple_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsdarkpurple_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_absdarkpurple_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsdarkpurple_1000_175_p": null
  }
}
```

### GD008: dup-fd1d74601ba3a2c30f331085701b36e2bbe3d7828439ec486ba057a85072423a

Status: APPROVED; survivor `gizmodorks_abs_absgold_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_absgold_1000_175_p`|`ABS {color_name}`|`Gold`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabsgold_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Gold`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_absgold_1000_175_p": "E3B145",
    "gizmodorks_abs_gizmodorksabsgold_1000_175_p": "d4af37"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_absgold_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsgold_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_absgold_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsgold_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_absgold_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsgold_1000_175_p": null
  }
}
```

### GD009: dup-a65a7ed7f70dcb1ef859857cdc5ae772bb3e3abc28063c22df5647052420cec6

Status: APPROVED; survivor `gizmodorks_abs_absgrassgreen_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_absgrassgreen_1000_175_p`|`ABS {color_name}`|`Grass Green`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabsgrassgreen_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Grass Green`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_absgrassgreen_1000_175_p": "26A648",
    "gizmodorks_abs_gizmodorksabsgrassgreen_1000_175_p": "7cba3c"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_absgrassgreen_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsgrassgreen_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_absgrassgreen_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsgrassgreen_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_absgrassgreen_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsgrassgreen_1000_175_p": null
  }
}
```

### GD010: dup-4b78d597474b21d7fa74c6142b7b4c207d9969255524270f7ac75962063744ca

Status: APPROVED; survivor `gizmodorks_abs_absgreen_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_absgreen_1000_175_p`|`ABS {color_name}`|`Green`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabsgreen_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Green`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_absgreen_1000_175_p": "83E665",
    "gizmodorks_abs_gizmodorksabsgreen_1000_175_p": "228b22"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_absgreen_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsgreen_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_absgreen_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsgreen_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_absgreen_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsgreen_1000_175_p": null
  }
}
```

### GD011: dup-ae2f75baed19340bb01049f7f1bdb396decd04ca28efc214fe3cef2c9f1eca0f

Status: APPROVED; survivor `gizmodorks_abs_absgrey_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_absgrey_1000_175_p`|`ABS {color_name}`|`Grey`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabsgrey_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Grey`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_absgrey_1000_175_p": "55555E",
    "gizmodorks_abs_gizmodorksabsgrey_1000_175_p": "808080"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_absgrey_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsgrey_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_absgrey_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsgrey_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_absgrey_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsgrey_1000_175_p": null
  }
}
```

### GD012: dup-fdb59a8dbe88286f1a60f80e33f77b5369d209448f4d9771fb6fe77e5c47d0bd

Status: APPROVED; survivor `gizmodorks_abs_absorange_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_absorange_1000_175_p`|`ABS {color_name}`|`Orange`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabsorange_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Orange`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_absorange_1000_175_p": "FD9106",
    "gizmodorks_abs_gizmodorksabsorange_1000_175_p": "ff8c00"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_absorange_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsorange_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_absorange_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsorange_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_absorange_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsorange_1000_175_p": null
  }
}
```

### GD013: dup-52a30746939c715e0c121562d87ad00979d58492439e051cf2027812d9c34b8d

Status: APPROVED; survivor `gizmodorks_abs_abspink_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_abspink_1000_175_p`|`ABS {color_name}`|`Pink`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabspink_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Pink`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_abspink_1000_175_p": "E23288",
    "gizmodorks_abs_gizmodorksabspink_1000_175_p": "ff69b4"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_abspink_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabspink_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_abspink_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabspink_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_abspink_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabspink_1000_175_p": null
  }
}
```

### GD014: dup-dfecd54a875feafc987c7560aa387b8473a86a5c9de6d0fd40ed7cceff6a02a5

Status: APPROVED; survivor `gizmodorks_abs_abspinkrose_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_abspinkrose_1000_175_p`|`ABS {color_name}`|`Pink Rose`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabspinkrose_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Pink Rose`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_abspinkrose_1000_175_p": "C90D6E",
    "gizmodorks_abs_gizmodorksabspinkrose_1000_175_p": "e75480"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_abspinkrose_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabspinkrose_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_abspinkrose_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabspinkrose_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_abspinkrose_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabspinkrose_1000_175_p": null
  }
}
```

### GD015: dup-06f5cfdf4a7ab50b3a15d68597ae5f7ca8dbedb12814b780c580ec6b509d265b

Status: APPROVED; survivor `gizmodorks_abs_abspurple_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_abspurple_1000_175_p`|`ABS {color_name}`|`Purple`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabspurple_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Purple`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_abspurple_1000_175_p": "963877",
    "gizmodorks_abs_gizmodorksabspurple_1000_175_p": "800080"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_abspurple_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabspurple_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_abspurple_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabspurple_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_abspurple_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabspurple_1000_175_p": null
  }
}
```

### GD016: dup-8bb3b684ecf99f635ff1ce6ebf1564e99cbe1e2abef5fd187631f36de4864ad9

Status: APPROVED; survivor `gizmodorks_abs_absred_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_absred_1000_175_p`|`ABS {color_name}`|`Red`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabsred_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Red`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_absred_1000_175_p": "E03F26",
    "gizmodorks_abs_gizmodorksabsred_1000_175_p": "cc0000"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_absred_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsred_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_absred_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsred_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_absred_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsred_1000_175_p": null
  }
}
```

### GD017: dup-37bd60a791ed1adbec632c750acd723d777b554bb92d806aed9d7cd4db4f4695

Status: APPROVED; survivor `gizmodorks_abs_absredlava_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_absredlava_1000_175_p`|`ABS {color_name}`|`Red Lava`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabsredlava_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Red Lava`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_absredlava_1000_175_p": "DF3303",
    "gizmodorks_abs_gizmodorksabsredlava_1000_175_p": "b22222"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_absredlava_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsredlava_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_absredlava_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsredlava_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_absredlava_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsredlava_1000_175_p": null
  }
}
```

### GD018: dup-2dd077d1e1882d852d2909e0583b575187d5f4536f1520b50db7890075d870aa

Status: APPROVED; survivor `gizmodorks_abs_abssilver_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_abssilver_1000_175_p`|`ABS {color_name}`|`Silver`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabssilver_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Silver`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_abssilver_1000_175_p": "949A9E",
    "gizmodorks_abs_gizmodorksabssilver_1000_175_p": "c0c0c0"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_abssilver_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabssilver_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_abssilver_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabssilver_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_abssilver_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabssilver_1000_175_p": null
  }
}
```

### GD019: dup-7c6f6558f588dc00924ecb5de3b09f88e3b8db2f23d5bf790e1b685b7de0f869

Status: APPROVED; survivor `gizmodorks_abs_abstransparent_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_abstransparent_1000_175_p`|`ABS {color_name}`|`Transparent`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabstransparent_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Transparent`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_abstransparent_1000_175_p": "E4E7E5",
    "gizmodorks_abs_gizmodorksabstransparent_1000_175_p": "f0f8ff"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_abstransparent_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabstransparent_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_abstransparent_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabstransparent_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_abstransparent_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabstransparent_1000_175_p": null
  }
}
```

### GD020: dup-ec032eaea8cbcd7a60494dbd479105d51a8fd209549ca13524efce2e99664b62

Status: APPROVED; survivor `gizmodorks_abs_absviolet_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_absviolet_1000_175_p`|`ABS {color_name}`|`Violet`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabsviolet_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Violet`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_absviolet_1000_175_p": "D6ABFF",
    "gizmodorks_abs_gizmodorksabsviolet_1000_175_p": "8f00ff"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_absviolet_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsviolet_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_absviolet_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsviolet_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_absviolet_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsviolet_1000_175_p": null
  }
}
```

### GD021: dup-763c31e31f79b1b043a0400491ca4d245381098d6c841cf9f818fd36fbfff96d

Status: APPROVED; survivor `gizmodorks_abs_abswhite_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_abswhite_1000_175_p`|`ABS {color_name}`|`White`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabswhite_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`White`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_abswhite_1000_175_p": "EFE8D8",
    "gizmodorks_abs_gizmodorksabswhite_1000_175_p": "ffffff"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_abswhite_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabswhite_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_abswhite_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabswhite_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_abswhite_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabswhite_1000_175_p": null
  }
}
```

### GD022: dup-413d3385ef8182364a7e7846b9d8fb1f85d0f5414953c2c2ca35dfacdf79ada8

Status: APPROVED; survivor `gizmodorks_abs_absyellow_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_absyellow_1000_175_p`|`ABS {color_name}`|`Yellow`|{"source_file": "gizmodorks.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 22, "compiled_records": 22} / False|
|`gizmodorks_abs_gizmodorksabsyellow_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Yellow`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_absyellow_1000_175_p": "FFD342",
    "gizmodorks_abs_gizmodorksabsyellow_1000_175_p": "ffd700"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_absyellow_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsyellow_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_absyellow_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsyellow_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_absyellow_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsyellow_1000_175_p": null
  }
}
```

### GD023: dup-b26446dff2b7b8d0cdbf50080a4c0cb013c224c3146571f5ffee32f17340d194

Status: DEFERRED; survivor `gizmodorks_abs_fluorescentabsgreen(blacklightreactive)_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_fluorescentabsgreen(blacklightreactive)_1000_175_p`|`Fluorescent ABS {color_name}`|`Green (Black Light Reactive)`|{"source_file": "gizmodorks.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|
|`gizmodorks_abs_gizmodorksabsfluorescentgreen(blacklightreactive)_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Fluorescent Green (Black Light Reactive)`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_fluorescentabsgreen(blacklightreactive)_1000_175_p": "9FEC41",
    "gizmodorks_abs_gizmodorksabsfluorescentgreen(blacklightreactive)_1000_175_p": "39ff14"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_fluorescentabsgreen(blacklightreactive)_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsfluorescentgreen(blacklightreactive)_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_fluorescentabsgreen(blacklightreactive)_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsfluorescentgreen(blacklightreactive)_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_fluorescentabsgreen(blacklightreactive)_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsfluorescentgreen(blacklightreactive)_1000_175_p": null
  }
}
```

### GD024: dup-f815d2c1c0e5156990e48ca806a882ee9f3a8061593623718e0c77f73156f8e8

Status: DEFERRED; survivor `gizmodorks_abs_fluorescentabsorange(blacklightreactive)_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_fluorescentabsorange(blacklightreactive)_1000_175_p`|`Fluorescent ABS {color_name}`|`Orange (Black Light Reactive)`|{"source_file": "gizmodorks.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|
|`gizmodorks_abs_gizmodorksabsfluorescentorange(blacklightreactive)_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Fluorescent Orange (Black Light Reactive)`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_fluorescentabsorange(blacklightreactive)_1000_175_p": "FF5F2E",
    "gizmodorks_abs_gizmodorksabsfluorescentorange(blacklightreactive)_1000_175_p": "ff6600"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_fluorescentabsorange(blacklightreactive)_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsfluorescentorange(blacklightreactive)_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_fluorescentabsorange(blacklightreactive)_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsfluorescentorange(blacklightreactive)_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_fluorescentabsorange(blacklightreactive)_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsfluorescentorange(blacklightreactive)_1000_175_p": null
  }
}
```

### GD025: dup-950926a18e44b4aafbbcd276945bd21074c31790528ae8c7905c34ff1ebc7c5b

Status: DEFERRED; survivor `gizmodorks_abs_fluorescentabsyellow(blacklightreactive)_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_fluorescentabsyellow(blacklightreactive)_1000_175_p`|`Fluorescent ABS {color_name}`|`Yellow (Black Light Reactive)`|{"source_file": "gizmodorks.json", "definition_index": 6, "weights": 1, "diameters": 1, "colors": 4, "compiled_records": 4} / False|
|`gizmodorks_abs_gizmodorksabsfluorescentyellow(blacklightreactive)_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Fluorescent Yellow (Black Light Reactive)`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_fluorescentabsyellow(blacklightreactive)_1000_175_p": "FFFB00",
    "gizmodorks_abs_gizmodorksabsfluorescentyellow(blacklightreactive)_1000_175_p": "ccff00"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_fluorescentabsyellow(blacklightreactive)_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_abs_gizmodorksabsfluorescentyellow(blacklightreactive)_1000_175_p": [
      230,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_fluorescentabsyellow(blacklightreactive)_1000_175_p": null,
    "gizmodorks_abs_gizmodorksabsfluorescentyellow(blacklightreactive)_1000_175_p": 110
  },
  "bed_temp_range": {
    "gizmodorks_abs_fluorescentabsyellow(blacklightreactive)_1000_175_p": [
      90,
      110
    ],
    "gizmodorks_abs_gizmodorksabsfluorescentyellow(blacklightreactive)_1000_175_p": null
  }
}
```

### GD026: dup-90e32272af6acda9913f6cc08222b2845871e741c85056fc8abc498a12b0078d

Status: DEFERRED; survivor `gizmodorks_abs_glowabsinthedark_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_abs_gizmodorksabsglowinthedark_1000_175_p`|`Gizmo Dorks ABS {color_name}`|`Glow in the Dark`|{"source_file": "gizmodorks.json", "definition_index": 2, "weights": 1, "diameters": 2, "colors": 33, "compiled_records": 66} / False|
|`gizmodorks_abs_glowabsinthedark_1000_175_p`|`Glow ABS {color_name}`|`In the Dark`|{"source_file": "gizmodorks.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_abs_gizmodorksabsglowinthedark_1000_175_p": "c8e6c9",
    "gizmodorks_abs_glowabsinthedark_1000_175_p": "58C91B"
  },
  "extruder_temp_range": {
    "gizmodorks_abs_gizmodorksabsglowinthedark_1000_175_p": [
      230,
      250
    ],
    "gizmodorks_abs_glowabsinthedark_1000_175_p": [
      230,
      260
    ]
  },
  "bed_temp": {
    "gizmodorks_abs_gizmodorksabsglowinthedark_1000_175_p": 110,
    "gizmodorks_abs_glowabsinthedark_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_abs_gizmodorksabsglowinthedark_1000_175_p": null,
    "gizmodorks_abs_glowabsinthedark_1000_175_p": [
      90,
      110
    ]
  }
}
```

### GD027: dup-2577e31a89947e87dba5a55c4e655cf5bb0c4d28b267ed06470860b615231045

Status: APPROVED; survivor `gizmodorks_petg_petgblack_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_petg_gizmodorkspetgblack_1000_175_p`|`Gizmo Dorks PETG {color_name}`|`Black`|{"source_file": "gizmodorks.json", "definition_index": 1, "weights": 1, "diameters": 2, "colors": 6, "compiled_records": 12} / False|
|`gizmodorks_petg_petgblack_1000_175_p`|`PETG {color_name}`|`Black`|{"source_file": "gizmodorks.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp_range": {
    "gizmodorks_petg_gizmodorkspetgblack_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_petg_petgblack_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_petg_gizmodorkspetgblack_1000_175_p": 80,
    "gizmodorks_petg_petgblack_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_petg_gizmodorkspetgblack_1000_175_p": null,
    "gizmodorks_petg_petgblack_1000_175_p": [
      70,
      90
    ]
  }
}
```

### GD028: dup-32b67fa200a87749e60c94ce37dadee4a4a773cb3098e17ad73f51ef9d362d11

Status: APPROVED; survivor `gizmodorks_petg_petgtranslucentblue_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_petg_gizmodorkspetgtranslucentblue_1000_175_p`|`Gizmo Dorks PETG {color_name}`|`Translucent Blue`|{"source_file": "gizmodorks.json", "definition_index": 1, "weights": 1, "diameters": 2, "colors": 6, "compiled_records": 12} / False|
|`gizmodorks_petg_petgtranslucentblue_1000_175_p`|`PETG {color_name}`|`Translucent Blue`|{"source_file": "gizmodorks.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_petg_gizmodorkspetgtranslucentblue_1000_175_p": "3399ff",
    "gizmodorks_petg_petgtranslucentblue_1000_175_p": "2E56F1"
  },
  "extruder_temp_range": {
    "gizmodorks_petg_gizmodorkspetgtranslucentblue_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_petg_petgtranslucentblue_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_petg_gizmodorkspetgtranslucentblue_1000_175_p": 80,
    "gizmodorks_petg_petgtranslucentblue_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_petg_gizmodorkspetgtranslucentblue_1000_175_p": null,
    "gizmodorks_petg_petgtranslucentblue_1000_175_p": [
      70,
      90
    ]
  }
}
```

### GD029: dup-9d044db6f8f82ef20cf6a27850937c77e10212a9ad9fe3141441a389daebf88f

Status: APPROVED; survivor `gizmodorks_petg_petgtranslucentgreen_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_petg_gizmodorkspetgtranslucentgreen_1000_175_p`|`Gizmo Dorks PETG {color_name}`|`Translucent Green`|{"source_file": "gizmodorks.json", "definition_index": 1, "weights": 1, "diameters": 2, "colors": 6, "compiled_records": 12} / False|
|`gizmodorks_petg_petgtranslucentgreen_1000_175_p`|`PETG {color_name}`|`Translucent Green`|{"source_file": "gizmodorks.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_petg_gizmodorkspetgtranslucentgreen_1000_175_p": "66cc66",
    "gizmodorks_petg_petgtranslucentgreen_1000_175_p": "58C91B"
  },
  "extruder_temp_range": {
    "gizmodorks_petg_gizmodorkspetgtranslucentgreen_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_petg_petgtranslucentgreen_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_petg_gizmodorkspetgtranslucentgreen_1000_175_p": 80,
    "gizmodorks_petg_petgtranslucentgreen_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_petg_gizmodorkspetgtranslucentgreen_1000_175_p": null,
    "gizmodorks_petg_petgtranslucentgreen_1000_175_p": [
      70,
      90
    ]
  }
}
```

### GD030: dup-c59e3c0e72ce797ac958f273d1dd574cdf7af95fec7afbe724dffb8b97509273

Status: APPROVED; survivor `gizmodorks_petg_petgtranslucentred_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_petg_gizmodorkspetgtranslucentred_1000_175_p`|`Gizmo Dorks PETG {color_name}`|`Translucent Red`|{"source_file": "gizmodorks.json", "definition_index": 1, "weights": 1, "diameters": 2, "colors": 6, "compiled_records": 12} / False|
|`gizmodorks_petg_petgtranslucentred_1000_175_p`|`PETG {color_name}`|`Translucent Red`|{"source_file": "gizmodorks.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_petg_gizmodorkspetgtranslucentred_1000_175_p": "ff4444",
    "gizmodorks_petg_petgtranslucentred_1000_175_p": "E20010"
  },
  "extruder_temp_range": {
    "gizmodorks_petg_gizmodorkspetgtranslucentred_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_petg_petgtranslucentred_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_petg_gizmodorkspetgtranslucentred_1000_175_p": 80,
    "gizmodorks_petg_petgtranslucentred_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_petg_gizmodorkspetgtranslucentred_1000_175_p": null,
    "gizmodorks_petg_petgtranslucentred_1000_175_p": [
      70,
      90
    ]
  }
}
```

### GD031: dup-2744d9d91e438a4a436ecb77ed34819cbe367e0d15be91744da5e2b6a5232452

Status: APPROVED; survivor `gizmodorks_petg_petgtransparent_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_petg_gizmodorkspetgtransparent_1000_175_p`|`Gizmo Dorks PETG {color_name}`|`Transparent`|{"source_file": "gizmodorks.json", "definition_index": 1, "weights": 1, "diameters": 2, "colors": 6, "compiled_records": 12} / False|
|`gizmodorks_petg_petgtransparent_1000_175_p`|`PETG {color_name}`|`Transparent`|{"source_file": "gizmodorks.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_petg_gizmodorkspetgtransparent_1000_175_p": "f0f8ff",
    "gizmodorks_petg_petgtransparent_1000_175_p": "E4E7E5"
  },
  "extruder_temp_range": {
    "gizmodorks_petg_gizmodorkspetgtransparent_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_petg_petgtransparent_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_petg_gizmodorkspetgtransparent_1000_175_p": 80,
    "gizmodorks_petg_petgtransparent_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_petg_gizmodorkspetgtransparent_1000_175_p": null,
    "gizmodorks_petg_petgtransparent_1000_175_p": [
      70,
      90
    ]
  }
}
```

### GD032: dup-abc22455a9d585865fd1c487aee6b42a27afb63364dc2e9a80b6f2488b4f57fc

Status: APPROVED; survivor `gizmodorks_petg_petgwhite_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_petg_gizmodorkspetgwhite_1000_175_p`|`Gizmo Dorks PETG {color_name}`|`White`|{"source_file": "gizmodorks.json", "definition_index": 1, "weights": 1, "diameters": 2, "colors": 6, "compiled_records": 12} / False|
|`gizmodorks_petg_petgwhite_1000_175_p`|`PETG {color_name}`|`White`|{"source_file": "gizmodorks.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_petg_gizmodorkspetgwhite_1000_175_p": "ffffff",
    "gizmodorks_petg_petgwhite_1000_175_p": "FFFFFF"
  },
  "extruder_temp_range": {
    "gizmodorks_petg_gizmodorkspetgwhite_1000_175_p": [
      230,
      260
    ],
    "gizmodorks_petg_petgwhite_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp": {
    "gizmodorks_petg_gizmodorkspetgwhite_1000_175_p": 80,
    "gizmodorks_petg_petgwhite_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_petg_gizmodorkspetgwhite_1000_175_p": null,
    "gizmodorks_petg_petgwhite_1000_175_p": [
      70,
      90
    ]
  }
}
```

### GD033: dup-2beac9799787121b9b2e33c1207826c8a5b6b60cc4c1cd2b15526709f8245ae8

Status: DEFERRED; survivor `gizmodorks_pla_fluorescentplablue(blacklightreactive)_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_fluorescentplablue(blacklightreactive)_1000_175_p`|`Fluorescent PLA {color_name}`|`Blue (Black Light Reactive)`|{"source_file": "gizmodorks.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / False|
|`gizmodorks_pla_gizmodorksplafluorescentblue(blacklightreactive)_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Fluorescent Blue (Black Light Reactive)`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_fluorescentplablue(blacklightreactive)_1000_175_p": "2E56F1",
    "gizmodorks_pla_gizmodorksplafluorescentblue(blacklightreactive)_1000_175_p": "00bfff"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_fluorescentplablue(blacklightreactive)_1000_175_p": [
      190,
      230
    ],
    "gizmodorks_pla_gizmodorksplafluorescentblue(blacklightreactive)_1000_175_p": [
      190,
      225
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_fluorescentplablue(blacklightreactive)_1000_175_p": null,
    "gizmodorks_pla_gizmodorksplafluorescentblue(blacklightreactive)_1000_175_p": 60
  },
  "bed_temp_range": {
    "gizmodorks_pla_fluorescentplablue(blacklightreactive)_1000_175_p": [
      50,
      70
    ],
    "gizmodorks_pla_gizmodorksplafluorescentblue(blacklightreactive)_1000_175_p": null
  }
}
```

### GD034: dup-1282374799cf2e46a791e2ad7a68b7c6010881f86d1a2530375ece05b5ab3918

Status: DEFERRED; survivor `gizmodorks_pla_fluorescentplagreen(blacklightreactive)_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_fluorescentplagreen(blacklightreactive)_1000_175_p`|`Fluorescent PLA {color_name}`|`Green (Black Light Reactive)`|{"source_file": "gizmodorks.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / False|
|`gizmodorks_pla_gizmodorksplafluorescentgreen(blacklightreactive)_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Fluorescent Green (Black Light Reactive)`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_fluorescentplagreen(blacklightreactive)_1000_175_p": "9AEE6C",
    "gizmodorks_pla_gizmodorksplafluorescentgreen(blacklightreactive)_1000_175_p": "39ff14"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_fluorescentplagreen(blacklightreactive)_1000_175_p": [
      190,
      230
    ],
    "gizmodorks_pla_gizmodorksplafluorescentgreen(blacklightreactive)_1000_175_p": [
      190,
      225
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_fluorescentplagreen(blacklightreactive)_1000_175_p": null,
    "gizmodorks_pla_gizmodorksplafluorescentgreen(blacklightreactive)_1000_175_p": 60
  },
  "bed_temp_range": {
    "gizmodorks_pla_fluorescentplagreen(blacklightreactive)_1000_175_p": [
      50,
      70
    ],
    "gizmodorks_pla_gizmodorksplafluorescentgreen(blacklightreactive)_1000_175_p": null
  }
}
```

### GD035: dup-da8b0dbecfe80018fb25bc999346bb7b29ed391e654e04fbf19893bbfda778e8

Status: DEFERRED; survivor `gizmodorks_pla_fluorescentplaorange(blacklightreactive)_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_fluorescentplaorange(blacklightreactive)_1000_175_p`|`Fluorescent PLA {color_name}`|`Orange (Black Light Reactive)`|{"source_file": "gizmodorks.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / False|
|`gizmodorks_pla_gizmodorksplafluorescentorange(blacklightreactive)_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Fluorescent Orange (Black Light Reactive)`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_fluorescentplaorange(blacklightreactive)_1000_175_p": "FF5F2E",
    "gizmodorks_pla_gizmodorksplafluorescentorange(blacklightreactive)_1000_175_p": "ff6600"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_fluorescentplaorange(blacklightreactive)_1000_175_p": [
      190,
      230
    ],
    "gizmodorks_pla_gizmodorksplafluorescentorange(blacklightreactive)_1000_175_p": [
      190,
      225
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_fluorescentplaorange(blacklightreactive)_1000_175_p": null,
    "gizmodorks_pla_gizmodorksplafluorescentorange(blacklightreactive)_1000_175_p": 60
  },
  "bed_temp_range": {
    "gizmodorks_pla_fluorescentplaorange(blacklightreactive)_1000_175_p": [
      50,
      70
    ],
    "gizmodorks_pla_gizmodorksplafluorescentorange(blacklightreactive)_1000_175_p": null
  }
}
```

### GD036: dup-4a4f965dbc53320de66d5fec3eceeb6cb6afe91b2073b9a28f5308fc88010148

Status: DEFERRED; survivor `gizmodorks_pla_fluorescentplared(blacklightreactive)_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_fluorescentplared(blacklightreactive)_1000_175_p`|`Fluorescent PLA {color_name}`|`Red (Black Light Reactive)`|{"source_file": "gizmodorks.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / False|
|`gizmodorks_pla_gizmodorksplafluorescentred(blacklightreactive)_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Fluorescent Red (Black Light Reactive)`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_fluorescentplared(blacklightreactive)_1000_175_p": "ED1536",
    "gizmodorks_pla_gizmodorksplafluorescentred(blacklightreactive)_1000_175_p": "ff0040"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_fluorescentplared(blacklightreactive)_1000_175_p": [
      190,
      230
    ],
    "gizmodorks_pla_gizmodorksplafluorescentred(blacklightreactive)_1000_175_p": [
      190,
      225
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_fluorescentplared(blacklightreactive)_1000_175_p": null,
    "gizmodorks_pla_gizmodorksplafluorescentred(blacklightreactive)_1000_175_p": 60
  },
  "bed_temp_range": {
    "gizmodorks_pla_fluorescentplared(blacklightreactive)_1000_175_p": [
      50,
      70
    ],
    "gizmodorks_pla_gizmodorksplafluorescentred(blacklightreactive)_1000_175_p": null
  }
}
```

### GD037: dup-d76262008266fef6f3fcf5ece68f29a6b2623e23e2918240c4d45bfd31cafd35

Status: DEFERRED; survivor `gizmodorks_pla_fluorescentplayellow(blacklightreactive)_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_fluorescentplayellow(blacklightreactive)_1000_175_p`|`Fluorescent PLA {color_name}`|`Yellow (Black Light Reactive)`|{"source_file": "gizmodorks.json", "definition_index": 15, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / False|
|`gizmodorks_pla_gizmodorksplafluorescentyellow(blacklightreactive)_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Fluorescent Yellow (Black Light Reactive)`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_fluorescentplayellow(blacklightreactive)_1000_175_p": "FFFB00",
    "gizmodorks_pla_gizmodorksplafluorescentyellow(blacklightreactive)_1000_175_p": "ccff00"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_fluorescentplayellow(blacklightreactive)_1000_175_p": [
      190,
      230
    ],
    "gizmodorks_pla_gizmodorksplafluorescentyellow(blacklightreactive)_1000_175_p": [
      190,
      225
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_fluorescentplayellow(blacklightreactive)_1000_175_p": null,
    "gizmodorks_pla_gizmodorksplafluorescentyellow(blacklightreactive)_1000_175_p": 60
  },
  "bed_temp_range": {
    "gizmodorks_pla_fluorescentplayellow(blacklightreactive)_1000_175_p": [
      50,
      70
    ],
    "gizmodorks_pla_gizmodorksplafluorescentyellow(blacklightreactive)_1000_175_p": null
  }
}
```

### GD038: dup-dd2825410e90f355cc89338c7ceced8e6126b878d29a12ecad951726f7708804

Status: APPROVED; survivor `gizmodorks_pla_plabeige_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplabeige_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Beige`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plabeige_1000_175_p`|`PLA {color_name}`|`Beige`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplabeige_1000_175_p": "f5f5dc",
    "gizmodorks_pla_plabeige_1000_175_p": "E2C077"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplabeige_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plabeige_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplabeige_1000_175_p": 60,
    "gizmodorks_pla_plabeige_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplabeige_1000_175_p": null,
    "gizmodorks_pla_plabeige_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD039: dup-b6754caef5d17a704c48508ac5a5639ed0d9f7476292b2f18710ce645cb5faf9

Status: APPROVED; survivor `gizmodorks_pla_plablack_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplablack_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Black`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plablack_1000_175_p`|`PLA {color_name}`|`Black`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplablack_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plablack_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplablack_1000_175_p": 60,
    "gizmodorks_pla_plablack_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplablack_1000_175_p": null,
    "gizmodorks_pla_plablack_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD040: dup-8988a751e0ee1a84617248c65f5784f6d2b774619018b2518fc7e8756193bfa1

Status: APPROVED; survivor `gizmodorks_pla_plablue_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplablue_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Blue`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plablue_1000_175_p`|`PLA {color_name}`|`Blue`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplablue_1000_175_p": "0066cc",
    "gizmodorks_pla_plablue_1000_175_p": "2E56F1"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplablue_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plablue_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplablue_1000_175_p": 60,
    "gizmodorks_pla_plablue_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplablue_1000_175_p": null,
    "gizmodorks_pla_plablue_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD041: dup-b1f5114eb7ad152a3b4d780d5613c89be13ed51d492d8119c1c732278939c7be

Status: APPROVED; survivor `gizmodorks_pla_plabrown_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplabrown_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Brown`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plabrown_1000_175_p`|`PLA {color_name}`|`Brown`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplabrown_1000_175_p": "8b4513",
    "gizmodorks_pla_plabrown_1000_175_p": "A6662E"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplabrown_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plabrown_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplabrown_1000_175_p": 60,
    "gizmodorks_pla_plabrown_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplabrown_1000_175_p": null,
    "gizmodorks_pla_plabrown_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD042: dup-a4bc9af947619b5e8eff2c31b0d69c377066f0cd3be80eee1b0cb745620960ac

Status: APPROVED; survivor `gizmodorks_pla_pladarkblue_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorkspladarkblue_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Dark Blue`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_pladarkblue_1000_175_p`|`PLA {color_name}`|`Dark Blue`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorkspladarkblue_1000_175_p": "00008b",
    "gizmodorks_pla_pladarkblue_1000_175_p": "2C3294"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorkspladarkblue_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_pladarkblue_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorkspladarkblue_1000_175_p": 60,
    "gizmodorks_pla_pladarkblue_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorkspladarkblue_1000_175_p": null,
    "gizmodorks_pla_pladarkblue_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD043: dup-bba970675585e537dc4a5ae9d104f4da87613f81f799c99aeab5a00455afaab1

Status: APPROVED; survivor `gizmodorks_pla_pladarkbrown_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorkspladarkbrown_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Dark Brown`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_pladarkbrown_1000_175_p`|`PLA {color_name}`|`Dark Brown`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorkspladarkbrown_1000_175_p": "654321",
    "gizmodorks_pla_pladarkbrown_1000_175_p": "503529"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorkspladarkbrown_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_pladarkbrown_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorkspladarkbrown_1000_175_p": 60,
    "gizmodorks_pla_pladarkbrown_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorkspladarkbrown_1000_175_p": null,
    "gizmodorks_pla_pladarkbrown_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD044: dup-bc266db6c2f4272061a60cad0b8d05ec5e814e1c4d200ccc24ca0fb9ed44fbfc

Status: DEFERRED; survivor `gizmodorks_pla_glowplainthedark_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplaglowinthedark_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Glow in the Dark`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_glowplainthedark_1000_175_p`|`Glow PLA {color_name}`|`In the Dark`|{"source_file": "gizmodorks.json", "definition_index": 17, "weights": 1, "diameters": 1, "colors": 1, "compiled_records": 1} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplaglowinthedark_1000_175_p": "c8e6c9",
    "gizmodorks_pla_glowplainthedark_1000_175_p": "F1E6B2"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplaglowinthedark_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_glowplainthedark_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplaglowinthedark_1000_175_p": 60,
    "gizmodorks_pla_glowplainthedark_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplaglowinthedark_1000_175_p": null,
    "gizmodorks_pla_glowplainthedark_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD045: dup-0ba9d3fc1402870563a34a71dee894f729cafeb65ab2f9cb71bd96f9acda98f7

Status: APPROVED; survivor `gizmodorks_pla_plagold_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplagold_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Gold`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plagold_1000_175_p`|`PLA {color_name}`|`Gold`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplagold_1000_175_p": "d4af37",
    "gizmodorks_pla_plagold_1000_175_p": "E3B145"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplagold_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plagold_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplagold_1000_175_p": 60,
    "gizmodorks_pla_plagold_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplagold_1000_175_p": null,
    "gizmodorks_pla_plagold_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD046: dup-e8111c3605522c02dee8b6745f67b00cf98bbd78263e2e859c9cf550a88ce1be

Status: APPROVED; survivor `gizmodorks_pla_plagrassgreen_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplagrassgreen_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Grass Green`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plagrassgreen_1000_175_p`|`PLA {color_name}`|`Grass Green`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplagrassgreen_1000_175_p": "7cba3c",
    "gizmodorks_pla_plagrassgreen_1000_175_p": "26A648"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplagrassgreen_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plagrassgreen_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplagrassgreen_1000_175_p": 60,
    "gizmodorks_pla_plagrassgreen_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplagrassgreen_1000_175_p": null,
    "gizmodorks_pla_plagrassgreen_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD047: dup-bbdfb94554688cf47e81b3984e24a718a02f16913078b09bad11e6b76896819c

Status: APPROVED; survivor `gizmodorks_pla_plagreen_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplagreen_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Green`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plagreen_1000_175_p`|`PLA {color_name}`|`Green`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplagreen_1000_175_p": "228b22",
    "gizmodorks_pla_plagreen_1000_175_p": "58C91B"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplagreen_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plagreen_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplagreen_1000_175_p": 60,
    "gizmodorks_pla_plagreen_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplagreen_1000_175_p": null,
    "gizmodorks_pla_plagreen_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD048: dup-7744c4bff8fa0de34cb1666130b04d827cca121183edfefdb5d8e39975720be6

Status: APPROVED; survivor `gizmodorks_pla_plagreen(translucent)_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplagreen(translucent)_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Green (Translucent)`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plagreen(translucent)_1000_175_p`|`PLA {color_name}`|`Green (Translucent)`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplagreen(translucent)_1000_175_p": "66cc66",
    "gizmodorks_pla_plagreen(translucent)_1000_175_p": "58C91B"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplagreen(translucent)_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plagreen(translucent)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplagreen(translucent)_1000_175_p": 60,
    "gizmodorks_pla_plagreen(translucent)_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplagreen(translucent)_1000_175_p": null,
    "gizmodorks_pla_plagreen(translucent)_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD049: dup-a10fced8c9c1304300236cfd2ace54113798e5430c7f049abf68ae1f67d9afb5

Status: APPROVED; survivor `gizmodorks_pla_plagrey_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplagrey_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Grey`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plagrey_1000_175_p`|`PLA {color_name}`|`Grey`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplagrey_1000_175_p": "808080",
    "gizmodorks_pla_plagrey_1000_175_p": "6A6C6E"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplagrey_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plagrey_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplagrey_1000_175_p": 60,
    "gizmodorks_pla_plagrey_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplagrey_1000_175_p": null,
    "gizmodorks_pla_plagrey_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD050: dup-e47f289e6d183d471f1bab957db90bccc7fe98b1b657bea1c7fe2aa5f7eeaa82

Status: APPROVED; survivor `gizmodorks_pla_plalightyellow_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplalightyellow_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Light Yellow`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plalightyellow_1000_175_p`|`PLA {color_name}`|`Light Yellow`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplalightyellow_1000_175_p": "fffacd",
    "gizmodorks_pla_plalightyellow_1000_175_p": "E4FF33"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplalightyellow_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plalightyellow_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplalightyellow_1000_175_p": 60,
    "gizmodorks_pla_plalightyellow_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplalightyellow_1000_175_p": null,
    "gizmodorks_pla_plalightyellow_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD051: dup-5020ba55dd964a9335e15499872210edd6a9845628f629b5c657f4d9d1fe0870

Status: APPROVED; survivor `gizmodorks_pla_plaorange_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplaorange_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Orange`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plaorange_1000_175_p`|`PLA {color_name}`|`Orange`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplaorange_1000_175_p": "ff8c00",
    "gizmodorks_pla_plaorange_1000_175_p": "FD9106"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplaorange_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plaorange_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplaorange_1000_175_p": 60,
    "gizmodorks_pla_plaorange_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplaorange_1000_175_p": null,
    "gizmodorks_pla_plaorange_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD052: dup-f0b6d16e791b67dd717510a2fcda76b30b3eaca1a9526e258aa146d2d4f4f8a3

Status: APPROVED; survivor `gizmodorks_pla_plaorange(translucent)_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplaorange(translucent)_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Orange (Translucent)`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plaorange(translucent)_1000_175_p`|`PLA {color_name}`|`Orange (Translucent)`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplaorange(translucent)_1000_175_p": "ffaa55",
    "gizmodorks_pla_plaorange(translucent)_1000_175_p": "F67405"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplaorange(translucent)_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plaorange(translucent)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplaorange(translucent)_1000_175_p": 60,
    "gizmodorks_pla_plaorange(translucent)_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplaorange(translucent)_1000_175_p": null,
    "gizmodorks_pla_plaorange(translucent)_1000_175_p": [
      50,
      70
    ]
  },
  "translucent": {
    "gizmodorks_pla_gizmodorksplaorange(translucent)_1000_175_p": true,
    "gizmodorks_pla_plaorange(translucent)_1000_175_p": false
  }
}
```

### GD053: dup-ca192d550ae6782c65ac5e13864b19f92a98b1428b21f7641f23d0b52a2b0313

Status: APPROVED; survivor `gizmodorks_pla_plapink_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplapink_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Pink`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plapink_1000_175_p`|`PLA {color_name}`|`Pink`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplapink_1000_175_p": "ff69b4",
    "gizmodorks_pla_plapink_1000_175_p": "FFC8C9"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplapink_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plapink_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplapink_1000_175_p": 60,
    "gizmodorks_pla_plapink_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplapink_1000_175_p": null,
    "gizmodorks_pla_plapink_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD054: dup-86af20c001b9a67a5e201cd9a8b81f00e3ed513ed2152dea08bd86344e5c0055

Status: APPROVED; survivor `gizmodorks_pla_plapink(translucent)_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplapink(translucent)_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Pink (Translucent)`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plapink(translucent)_1000_175_p`|`PLA {color_name}`|`Pink (Translucent)`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplapink(translucent)_1000_175_p": "ff99cc",
    "gizmodorks_pla_plapink(translucent)_1000_175_p": "FF72B6"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplapink(translucent)_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plapink(translucent)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplapink(translucent)_1000_175_p": 60,
    "gizmodorks_pla_plapink(translucent)_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplapink(translucent)_1000_175_p": null,
    "gizmodorks_pla_plapink(translucent)_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD055: dup-b64e3e8c5311267a3eb4fce139cbc0e02c6538f1f239215fc56b772fe8753793

Status: APPROVED; survivor `gizmodorks_pla_plapinkrose_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplapinkrose_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Pink Rose`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plapinkrose_1000_175_p`|`PLA {color_name}`|`Pink Rose`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplapinkrose_1000_175_p": "e75480",
    "gizmodorks_pla_plapinkrose_1000_175_p": "C90D6E"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplapinkrose_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plapinkrose_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplapinkrose_1000_175_p": 60,
    "gizmodorks_pla_plapinkrose_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplapinkrose_1000_175_p": null,
    "gizmodorks_pla_plapinkrose_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD056: dup-fc89a1250500888de5022362c604c9b76993869a8693b148ea582af87e68de77

Status: APPROVED; survivor `gizmodorks_pla_plapurple_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplapurple_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Purple`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plapurple_1000_175_p`|`PLA {color_name}`|`Purple`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplapurple_1000_175_p": "800080",
    "gizmodorks_pla_plapurple_1000_175_p": "963877"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplapurple_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plapurple_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplapurple_1000_175_p": 60,
    "gizmodorks_pla_plapurple_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplapurple_1000_175_p": null,
    "gizmodorks_pla_plapurple_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD057: dup-63b6e763a0be7c85db08459c887ca86bdbdbab8616fda3bd2ecf663b78930b07

Status: APPROVED; survivor `gizmodorks_pla_plapurple(translucent)_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplapurple(translucent)_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Purple (Translucent)`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plapurple(translucent)_1000_175_p`|`PLA {color_name}`|`Purple (Translucent)`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplapurple(translucent)_1000_175_p": "bb66bb",
    "gizmodorks_pla_plapurple(translucent)_1000_175_p": "C80181"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplapurple(translucent)_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plapurple(translucent)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplapurple(translucent)_1000_175_p": 60,
    "gizmodorks_pla_plapurple(translucent)_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplapurple(translucent)_1000_175_p": null,
    "gizmodorks_pla_plapurple(translucent)_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD058: dup-948af0fcc687d867ea9084d1828022355a19ba4048f0e83cdc8e8984520ffe72

Status: APPROVED; survivor `gizmodorks_pla_plared_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplared_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Red`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plared_1000_175_p`|`PLA {color_name}`|`Red`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplared_1000_175_p": "cc0000",
    "gizmodorks_pla_plared_1000_175_p": "E20010"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplared_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plared_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplared_1000_175_p": 60,
    "gizmodorks_pla_plared_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplared_1000_175_p": null,
    "gizmodorks_pla_plared_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD059: dup-fd7fca972757867d4792b32c7c8b0a6ee35a3b0c880c8f3be97066e68342e732

Status: APPROVED; survivor `gizmodorks_pla_plared(translucent)_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplared(translucent)_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Red (Translucent)`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plared(translucent)_1000_175_p`|`PLA {color_name}`|`Red (Translucent)`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplared(translucent)_1000_175_p": "ff4444",
    "gizmodorks_pla_plared(translucent)_1000_175_p": "C01616"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplared(translucent)_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plared(translucent)_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplared(translucent)_1000_175_p": 60,
    "gizmodorks_pla_plared(translucent)_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplared(translucent)_1000_175_p": null,
    "gizmodorks_pla_plared(translucent)_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD060: dup-584d7d32a72bbbc2af575c477b58f20062ce79e69878642df8fa96f316035080

Status: APPROVED; survivor `gizmodorks_pla_plaredlava_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplaredlava_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Red Lava`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plaredlava_1000_175_p`|`PLA {color_name}`|`Red Lava`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplaredlava_1000_175_p": "b22222",
    "gizmodorks_pla_plaredlava_1000_175_p": "DF3303"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplaredlava_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plaredlava_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplaredlava_1000_175_p": 60,
    "gizmodorks_pla_plaredlava_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplaredlava_1000_175_p": null,
    "gizmodorks_pla_plaredlava_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD061: dup-ae7d17a35105056f8d53b53d1d5cf2a93d2d43af79b0592b2212a36916e384de

Status: APPROVED; survivor `gizmodorks_pla_plasilver_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplasilver_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Silver`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plasilver_1000_175_p`|`PLA {color_name}`|`Silver`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplasilver_1000_175_p": "c0c0c0",
    "gizmodorks_pla_plasilver_1000_175_p": "818184"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplasilver_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plasilver_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplasilver_1000_175_p": 60,
    "gizmodorks_pla_plasilver_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplasilver_1000_175_p": null,
    "gizmodorks_pla_plasilver_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD062: dup-c9820ec81a687f8da6a14127ac845af1e42eb29b709ad1638cf23053f09f6b15

Status: APPROVED; survivor `gizmodorks_pla_platransparent_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplatransparent_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Transparent`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_platransparent_1000_175_p`|`PLA {color_name}`|`Transparent`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplatransparent_1000_175_p": "f0f8ff",
    "gizmodorks_pla_platransparent_1000_175_p": "E4E7E5"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplatransparent_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_platransparent_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplatransparent_1000_175_p": 60,
    "gizmodorks_pla_platransparent_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplatransparent_1000_175_p": null,
    "gizmodorks_pla_platransparent_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD063: dup-2f8558eb56960d7bc46686eef3fcd9b0f752f0819a446bd87e1950370c2b9626

Status: APPROVED; survivor `gizmodorks_pla_plaviolet_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplaviolet_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Violet`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plaviolet_1000_175_p`|`PLA {color_name}`|`Violet`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplaviolet_1000_175_p": "8f00ff",
    "gizmodorks_pla_plaviolet_1000_175_p": "D6ABFF"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplaviolet_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plaviolet_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplaviolet_1000_175_p": 60,
    "gizmodorks_pla_plaviolet_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplaviolet_1000_175_p": null,
    "gizmodorks_pla_plaviolet_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD064: dup-35c78b749c282415e3afeb051bce30df214c32c3e21477223637bae33e61d236

Status: APPROVED; survivor `gizmodorks_pla_plawhite_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplawhite_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`White`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_plawhite_1000_175_p`|`PLA {color_name}`|`White`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplawhite_1000_175_p": "ffffff",
    "gizmodorks_pla_plawhite_1000_175_p": "EFE8D8"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplawhite_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_plawhite_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplawhite_1000_175_p": 60,
    "gizmodorks_pla_plawhite_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplawhite_1000_175_p": null,
    "gizmodorks_pla_plawhite_1000_175_p": [
      50,
      70
    ]
  }
}
```

### GD065: dup-50a42af30b335b253ddd4ea93fb4bb15ad6b3a7ed6e1df777646f1b1bbc65381

Status: APPROVED; survivor `gizmodorks_pla_playellow_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gizmodorks_pla_gizmodorksplayellow_1000_175_p`|`Gizmo Dorks PLA {color_name}`|`Yellow`|{"source_file": "gizmodorks.json", "definition_index": 0, "weights": 1, "diameters": 2, "colors": 41, "compiled_records": 82} / False|
|`gizmodorks_pla_playellow_1000_175_p`|`PLA {color_name}`|`Yellow`|{"source_file": "gizmodorks.json", "definition_index": 18, "weights": 1, "diameters": 1, "colors": 34, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "gizmodorks_pla_gizmodorksplayellow_1000_175_p": "ffd700",
    "gizmodorks_pla_playellow_1000_175_p": "FBE200"
  },
  "extruder_temp_range": {
    "gizmodorks_pla_gizmodorksplayellow_1000_175_p": [
      190,
      225
    ],
    "gizmodorks_pla_playellow_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "gizmodorks_pla_gizmodorksplayellow_1000_175_p": 60,
    "gizmodorks_pla_playellow_1000_175_p": null
  },
  "bed_temp_range": {
    "gizmodorks_pla_gizmodorksplayellow_1000_175_p": null,
    "gizmodorks_pla_playellow_1000_175_p": [
      50,
      70
    ]
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "gizmodorks_abs_absblue_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_abspurple_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plagold_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_absdarkblue_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_petg_petgblack_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          260
        ],
        "bed_temp": 80,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/petg-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_petg_petgtransparent_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          260
        ],
        "bed_temp": 80,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/petg-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_abssilver_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plaviolet_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_petg_petgtranslucentblue_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          260
        ],
        "bed_temp": 80,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/petg-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plawhite_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_absredlava_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_absdarkpurple_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_absyellow_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_absgreen_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plaorange_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_playellow_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_abspink_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plaredlava_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plapurple(translucent)_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_abswhite_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plagreen(translucent)_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_abstransparent_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plapink(translucent)_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plablue_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_absred_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plared_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_petg_petgtranslucentgreen_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          260
        ],
        "bed_temp": 80,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/petg-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plagrey_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_pladarkblue_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_absgrassgreen_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_petg_petgwhite_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          260
        ],
        "bed_temp": 80,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/petg-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_absgrey_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plasilver_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plabrown_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_absbeige_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plapinkrose_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plablack_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_pladarkbrown_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plagreen_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_absblack_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_petg_petgtranslucentred_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          260
        ],
        "bed_temp": 80,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/petg-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_platransparent_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plapink_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_absbrown_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plabeige_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_absconductiveblack_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_abspinkrose_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plalightyellow_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plagrassgreen_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_absviolet_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plaorange(translucent)_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plapurple_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_absgold_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_pla_plared(translucent)_1000_175_p",
      "values": {
        "extruder_temp_range": [
          190,
          225
        ],
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/pla-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gizmodorks_abs_absorange_1000_175_p",
      "values": {
        "extruder_temp_range": [
          230,
          250
        ],
        "bed_temp": 110,
        "bed_temp_range": null
      },
      "source": "https://gizmodorks.com/abs-3d-printer-filament/",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    }
  ],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `gizmodorks_pla_gizmodorksplablue(translucent)_1000_175_p` — Gizmo Dorks PLA Blue (Translucent)
- `gizmodorks_pla_gizmodorksplacolorchangebluetowhite(heatactivated)_1000_175_p` — Gizmo Dorks PLA Color Change Blue to White (Heat Activated)
- `gizmodorks_pla_gizmodorksplacolorchangegreentoyellow(heatactivated)_1000_175_p` — Gizmo Dorks PLA Color Change Green to Yellow (Heat Activated)
- `gizmodorks_pla_gizmodorksplacolorchangegreytowhite(heatactivated)_1000_175_p` — Gizmo Dorks PLA Color Change Grey to White (Heat Activated)
- `gizmodorks_pla_gizmodorksplacolorchangepurpletopink(heatactivated)_1000_175_p` — Gizmo Dorks PLA Color Change Purple to Pink (Heat Activated)
- `gizmodorks_pla_gizmodorksplagradientrainbow_1000_175_p` — Gizmo Dorks PLA Gradient Rainbow
- `gizmodorks_pla_gizmodorkspladarkpurple_1000_175_p` — Gizmo Dorks PLA Dark Purple
- `gizmodorks_pla_gizmodorksplalightyellow(translucent)_1000_175_p` — Gizmo Dorks PLA Light Yellow (Translucent)
- `gizmodorks_pla_gizmodorksplabeige_1000_285_p` — Gizmo Dorks PLA Beige
- `gizmodorks_pla_gizmodorksplablack_1000_285_p` — Gizmo Dorks PLA Black
- `gizmodorks_pla_gizmodorksplablue_1000_285_p` — Gizmo Dorks PLA Blue
- `gizmodorks_pla_gizmodorksplablue(translucent)_1000_285_p` — Gizmo Dorks PLA Blue (Translucent)
- `gizmodorks_pla_gizmodorkspladarkblue_1000_285_p` — Gizmo Dorks PLA Dark Blue
- `gizmodorks_pla_gizmodorksplabrown_1000_285_p` — Gizmo Dorks PLA Brown
- `gizmodorks_pla_gizmodorkspladarkbrown_1000_285_p` — Gizmo Dorks PLA Dark Brown
- `gizmodorks_pla_gizmodorksplacolorchangebluetowhite(heatactivated)_1000_285_p` — Gizmo Dorks PLA Color Change Blue to White (Heat Activated)
- `gizmodorks_pla_gizmodorksplacolorchangegreentoyellow(heatactivated)_1000_285_p` — Gizmo Dorks PLA Color Change Green to Yellow (Heat Activated)
- `gizmodorks_pla_gizmodorksplacolorchangegreytowhite(heatactivated)_1000_285_p` — Gizmo Dorks PLA Color Change Grey to White (Heat Activated)
- `gizmodorks_pla_gizmodorksplacolorchangepurpletopink(heatactivated)_1000_285_p` — Gizmo Dorks PLA Color Change Purple to Pink (Heat Activated)
- `gizmodorks_pla_gizmodorksplafluorescentblue(blacklightreactive)_1000_285_p` — Gizmo Dorks PLA Fluorescent Blue (Black Light Reactive)
- `gizmodorks_pla_gizmodorksplafluorescentgreen(blacklightreactive)_1000_285_p` — Gizmo Dorks PLA Fluorescent Green (Black Light Reactive)
- `gizmodorks_pla_gizmodorksplafluorescentorange(blacklightreactive)_1000_285_p` — Gizmo Dorks PLA Fluorescent Orange (Black Light Reactive)
- `gizmodorks_pla_gizmodorksplafluorescentred(blacklightreactive)_1000_285_p` — Gizmo Dorks PLA Fluorescent Red (Black Light Reactive)
- `gizmodorks_pla_gizmodorksplafluorescentyellow(blacklightreactive)_1000_285_p` — Gizmo Dorks PLA Fluorescent Yellow (Black Light Reactive)
- `gizmodorks_pla_gizmodorksplaglowinthedark_1000_285_p` — Gizmo Dorks PLA Glow in the Dark
- `gizmodorks_pla_gizmodorksplagold_1000_285_p` — Gizmo Dorks PLA Gold
- `gizmodorks_pla_gizmodorksplagradientrainbow_1000_285_p` — Gizmo Dorks PLA Gradient Rainbow
- `gizmodorks_pla_gizmodorksplagrassgreen_1000_285_p` — Gizmo Dorks PLA Grass Green
- `gizmodorks_pla_gizmodorksplagreen_1000_285_p` — Gizmo Dorks PLA Green
- `gizmodorks_pla_gizmodorksplagreen(translucent)_1000_285_p` — Gizmo Dorks PLA Green (Translucent)
- `gizmodorks_pla_gizmodorksplagrey_1000_285_p` — Gizmo Dorks PLA Grey
- `gizmodorks_pla_gizmodorksplaorange_1000_285_p` — Gizmo Dorks PLA Orange
- `gizmodorks_pla_gizmodorksplaorange(translucent)_1000_285_p` — Gizmo Dorks PLA Orange (Translucent)
- `gizmodorks_pla_gizmodorksplapink_1000_285_p` — Gizmo Dorks PLA Pink
- `gizmodorks_pla_gizmodorksplapink(translucent)_1000_285_p` — Gizmo Dorks PLA Pink (Translucent)
- `gizmodorks_pla_gizmodorksplapinkrose_1000_285_p` — Gizmo Dorks PLA Pink Rose
- `gizmodorks_pla_gizmodorksplapurple_1000_285_p` — Gizmo Dorks PLA Purple
- `gizmodorks_pla_gizmodorksplapurple(translucent)_1000_285_p` — Gizmo Dorks PLA Purple (Translucent)
- `gizmodorks_pla_gizmodorkspladarkpurple_1000_285_p` — Gizmo Dorks PLA Dark Purple
- `gizmodorks_pla_gizmodorksplared_1000_285_p` — Gizmo Dorks PLA Red
- `gizmodorks_pla_gizmodorksplared(translucent)_1000_285_p` — Gizmo Dorks PLA Red (Translucent)
- `gizmodorks_pla_gizmodorksplaredlava_1000_285_p` — Gizmo Dorks PLA Red Lava
- `gizmodorks_pla_gizmodorksplasilver_1000_285_p` — Gizmo Dorks PLA Silver
- `gizmodorks_pla_gizmodorksplatransparent_1000_285_p` — Gizmo Dorks PLA Transparent
- `gizmodorks_pla_gizmodorksplaviolet_1000_285_p` — Gizmo Dorks PLA Violet
- `gizmodorks_pla_gizmodorksplawhite_1000_285_p` — Gizmo Dorks PLA White
- `gizmodorks_pla_gizmodorksplalightyellow_1000_285_p` — Gizmo Dorks PLA Light Yellow
- `gizmodorks_pla_gizmodorksplalightyellow(translucent)_1000_285_p` — Gizmo Dorks PLA Light Yellow (Translucent)
- `gizmodorks_pla_gizmodorksplayellow_1000_285_p` — Gizmo Dorks PLA Yellow
- `gizmodorks_petg_gizmodorkspetgblack_1000_285_p` — Gizmo Dorks PETG Black
- `gizmodorks_petg_gizmodorkspetgtranslucentblue_1000_285_p` — Gizmo Dorks PETG Translucent Blue
- `gizmodorks_petg_gizmodorkspetgtranslucentgreen_1000_285_p` — Gizmo Dorks PETG Translucent Green
- `gizmodorks_petg_gizmodorkspetgtranslucentred_1000_285_p` — Gizmo Dorks PETG Translucent Red
- `gizmodorks_petg_gizmodorkspetgtransparent_1000_285_p` — Gizmo Dorks PETG Transparent
- `gizmodorks_petg_gizmodorkspetgwhite_1000_285_p` — Gizmo Dorks PETG White
- `gizmodorks_abs_gizmodorksabscolorchangebluetowhite(heatactivated)_1000_175_p` — Gizmo Dorks ABS Color Change Blue to White (Heat Activated)
- `gizmodorks_abs_gizmodorksabscolorchangegreentoyellow(heatactivated)_1000_175_p` — Gizmo Dorks ABS Color Change Green to Yellow (Heat Activated)
- `gizmodorks_abs_gizmodorksabscolorchangegreytowhite(heatactivated)_1000_175_p` — Gizmo Dorks ABS Color Change Grey to White (Heat Activated)
- `gizmodorks_abs_gizmodorksabscolorchangepurpletopink(heatactivated)_1000_175_p` — Gizmo Dorks ABS Color Change Purple to Pink (Heat Activated)
- `gizmodorks_abs_gizmodorksabsfluorescentblue(blacklightreactive)_1000_175_p` — Gizmo Dorks ABS Fluorescent Blue (Black Light Reactive)
- `gizmodorks_abs_gizmodorksabsfluorescenthotpink(blacklightreactive)_1000_175_p` — Gizmo Dorks ABS Fluorescent Hot Pink (Black Light Reactive)
- `gizmodorks_abs_gizmodorksabslightyellow_1000_175_p` — Gizmo Dorks ABS Light Yellow
- `gizmodorks_abs_gizmodorksabsbeige_1000_285_p` — Gizmo Dorks ABS Beige
- `gizmodorks_abs_gizmodorksabsblack_1000_285_p` — Gizmo Dorks ABS Black
- `gizmodorks_abs_gizmodorksabsblue_1000_285_p` — Gizmo Dorks ABS Blue
- `gizmodorks_abs_gizmodorksabsbrown_1000_285_p` — Gizmo Dorks ABS Brown
- `gizmodorks_abs_gizmodorksabscolorchangebluetowhite(heatactivated)_1000_285_p` — Gizmo Dorks ABS Color Change Blue to White (Heat Activated)
- `gizmodorks_abs_gizmodorksabscolorchangegreentoyellow(heatactivated)_1000_285_p` — Gizmo Dorks ABS Color Change Green to Yellow (Heat Activated)
- `gizmodorks_abs_gizmodorksabscolorchangegreytowhite(heatactivated)_1000_285_p` — Gizmo Dorks ABS Color Change Grey to White (Heat Activated)
- `gizmodorks_abs_gizmodorksabscolorchangepurpletopink(heatactivated)_1000_285_p` — Gizmo Dorks ABS Color Change Purple to Pink (Heat Activated)
- `gizmodorks_abs_gizmodorksabsconductiveblack_1000_285_p` — Gizmo Dorks ABS Conductive Black
- `gizmodorks_abs_gizmodorksabsdarkblue_1000_285_p` — Gizmo Dorks ABS Dark Blue
- `gizmodorks_abs_gizmodorksabsdarkpurple_1000_285_p` — Gizmo Dorks ABS Dark Purple
- `gizmodorks_abs_gizmodorksabsfluorescentblue(blacklightreactive)_1000_285_p` — Gizmo Dorks ABS Fluorescent Blue (Black Light Reactive)
- `gizmodorks_abs_gizmodorksabsfluorescentgreen(blacklightreactive)_1000_285_p` — Gizmo Dorks ABS Fluorescent Green (Black Light Reactive)
- `gizmodorks_abs_gizmodorksabsfluorescenthotpink(blacklightreactive)_1000_285_p` — Gizmo Dorks ABS Fluorescent Hot Pink (Black Light Reactive)
- `gizmodorks_abs_gizmodorksabsfluorescentorange(blacklightreactive)_1000_285_p` — Gizmo Dorks ABS Fluorescent Orange (Black Light Reactive)
- `gizmodorks_abs_gizmodorksabsfluorescentyellow(blacklightreactive)_1000_285_p` — Gizmo Dorks ABS Fluorescent Yellow (Black Light Reactive)
- `gizmodorks_abs_gizmodorksabsglowinthedark_1000_285_p` — Gizmo Dorks ABS Glow in the Dark
- `gizmodorks_abs_gizmodorksabsgold_1000_285_p` — Gizmo Dorks ABS Gold
- `gizmodorks_abs_gizmodorksabsgreen_1000_285_p` — Gizmo Dorks ABS Green
- `gizmodorks_abs_gizmodorksabsgrey_1000_285_p` — Gizmo Dorks ABS Grey
- `gizmodorks_abs_gizmodorksabsgrassgreen_1000_285_p` — Gizmo Dorks ABS Grass Green
- `gizmodorks_abs_gizmodorksabsorange_1000_285_p` — Gizmo Dorks ABS Orange
- `gizmodorks_abs_gizmodorksabspink_1000_285_p` — Gizmo Dorks ABS Pink
- `gizmodorks_abs_gizmodorksabspinkrose_1000_285_p` — Gizmo Dorks ABS Pink Rose
- `gizmodorks_abs_gizmodorksabspurple_1000_285_p` — Gizmo Dorks ABS Purple
- `gizmodorks_abs_gizmodorksabsred_1000_285_p` — Gizmo Dorks ABS Red
- `gizmodorks_abs_gizmodorksabsredlava_1000_285_p` — Gizmo Dorks ABS Red Lava
- `gizmodorks_abs_gizmodorksabssilver_1000_285_p` — Gizmo Dorks ABS Silver
- `gizmodorks_abs_gizmodorksabstransparent_1000_285_p` — Gizmo Dorks ABS Transparent
- `gizmodorks_abs_gizmodorksabsviolet_1000_285_p` — Gizmo Dorks ABS Violet
- `gizmodorks_abs_gizmodorksabswhite_1000_285_p` — Gizmo Dorks ABS White
- `gizmodorks_abs_gizmodorksabsyellow_1000_285_p` — Gizmo Dorks ABS Yellow
- `gizmodorks_abs_gizmodorksabslightyellow_1000_285_p` — Gizmo Dorks ABS Light Yellow
- `gizmodorks_abs_abscffilament_1000_175_p` — ABS CF Filament
- `gizmodorks_abs_colorchangeabsbluetowhite_1000_175_p` — Color Change ABS Blue to White
- `gizmodorks_abs_colorchangeabsgreentoyellow_1000_175_p` — Color Change ABS Green to Yellow
- `gizmodorks_abs_colorchangeabsgreytowhite_1000_175_p` — Color Change ABS Grey to White
- `gizmodorks_abs_colorchangeabspurpletopink_1000_175_p` — Color Change ABS Purple to Pink
- `gizmodorks_abs_fluorescentabshotpink_1000_175_p` — Fluorescent ABS Hot Pink
- `gizmodorks_abs_glowabslowodorglowinthedark(blue)_1000_175_p` — Glow ABS Low Odor Glow in the Dark (Blue)
- `gizmodorks_abs_lowodorabsblack_1000_175_p` — Low Odor ABS Black
- `gizmodorks_abs_lowodorabsgray_1000_175_p` — Low Odor ABS Gray
- `gizmodorks_abs_lowodorabsorange_1000_175_p` — Low Odor ABS Orange
- `gizmodorks_abs_lowodorabspink_1000_175_p` — Low Odor ABS Pink
- `gizmodorks_abs_lowodorabspurple_1000_175_p` — Low Odor ABS Purple
- `gizmodorks_abs_lowodorabsred_1000_175_p` — Low Odor ABS Red
- `gizmodorks_abs_lowodorabsskyblue_1000_175_p` — Low Odor ABS Sky Blue
- `gizmodorks_abs_lowodorabsteal_1000_175_p` — Low Odor ABS Teal
- `gizmodorks_abs_lowodorabswhite_1000_175_p` — Low Odor ABS White
- `gizmodorks_abs_thermochromicabsbluetowhite_1000_175_p` — Thermochromic ABS Blue to White
- `gizmodorks_abs_thermochromicabsgraytowhite_1000_175_p` — Thermochromic ABS Gray to White
- `gizmodorks_abs_thermochromicabsgreentoyellow_1000_175_p` — Thermochromic ABS Green to Yellow
- `gizmodorks_abs_thermochromicabspurpletopink_1000_175_p` — Thermochromic ABS Purple to Pink
- `gizmodorks_hips_glowhipsinthedark_1000_175_p` — Glow HIPS In the Dark
- `gizmodorks_hips_hipsblack_1000_175_p` — HIPS Black
- `gizmodorks_hips_hipsblue_1000_175_p` — HIPS Blue
- `gizmodorks_hips_hipsbrown_1000_175_p` — HIPS Brown
- `gizmodorks_hips_hipsgreen_1000_175_p` — HIPS Green
- `gizmodorks_hips_hipsgrey_1000_175_p` — HIPS Grey
- `gizmodorks_hips_hipsorange_1000_175_p` — HIPS Orange
- `gizmodorks_hips_hipspink_1000_175_p` — HIPS Pink
- `gizmodorks_hips_hipspurple_1000_175_p` — HIPS Purple
- `gizmodorks_hips_hipsred_1000_175_p` — HIPS Red
- `gizmodorks_hips_hipswhite_1000_175_p` — HIPS White
- `gizmodorks_hips_hipsyellow_1000_175_p` — HIPS Yellow
- `gizmodorks_pc_pcblack_1000_175_p` — PC Black
- `gizmodorks_pc_pcblue_1000_175_p` — PC Blue
- `gizmodorks_pc_pctransparent_1000_175_p` — PC Transparent
- `gizmodorks_pla_colorchangeplabluetowhite_1000_175_p` — Color Change PLA Blue to White
- `gizmodorks_pla_colorchangeplagreentoyellow_1000_175_p` — Color Change PLA Green to Yellow
- `gizmodorks_pla_colorchangeplagreytowhite_1000_175_p` — Color Change PLA Grey to White
- `gizmodorks_pla_colorchangeplapurpletopink_1000_175_p` — Color Change PLA Purple to Pink
- `gizmodorks_pla_glittersparkleplablack_1000_175_p` — Glitter Sparkle PLA Black
- `gizmodorks_pla_glittersparkleplablue_1000_175_p` — Glitter Sparkle PLA Blue
- `gizmodorks_pla_glittersparkleplagray_1000_175_p` — Glitter Sparkle PLA Gray
- `gizmodorks_pla_glittersparkleplagreen_1000_175_p` — Glitter Sparkle PLA Green
- `gizmodorks_pla_glittersparkleplapurple_1000_175_p` — Glitter Sparkle PLA Purple
- `gizmodorks_pla_glittersparkleplared_1000_175_p` — Glitter Sparkle PLA Red
- `gizmodorks_pla_plablue(transparent)_1000_175_p` — PLA Blue (Transparent)
- `gizmodorks_pla_pladefault_1000_175_p` — PLA Default
- `gizmodorks_pla_plametalfilledbronze_1000_175_p` — PLA Metal Filled Bronze
- `gizmodorks_pla_plaplusengineeringgrade_1000_175_p` — PLA Plus Engineering Grade
- `gizmodorks_pla_plaplusfilamentengineeringgrade_1000_175_p` — PLA Plus Filament Engineering Grade
- `gizmodorks_pla_plawoodfilament_1000_175_p` — PLA Wood Filament
- `gizmodorks_pla_plawoodfilled_1000_175_p` — PLA Wood Filled
- `gizmodorks_pla_silkplametalfilledcopper_1000_175_p` — Silk PLA Metal Filled Copper
- `gizmodorks_pla_silkplaoceanblue_1000_175_p` — Silk PLA Ocean Blue
- `gizmodorks_pla_silkplaredpink_1000_175_p` — Silk PLA Red Pink
- `gizmodorks_pla_silkplateal_1000_175_p` — Silk PLA Teal
- `gizmodorks_pla_silkplayellowgold_1000_175_p` — Silk PLA Yellow Gold
- `gizmodorks_pla_thermochromicplabluetowhite_1000_175_p` — Thermochromic PLA Blue to White
- `gizmodorks_pla_thermochromicplagraytowhite_1000_175_p` — Thermochromic PLA Gray to White
- `gizmodorks_pla_thermochromicplagreentoyellow_1000_175_p` — Thermochromic PLA Green to Yellow
- `gizmodorks_pla_thermochromicplapurpletopink_1000_175_p` — Thermochromic PLA Purple to Pink
- `gizmodorks_pom_acetalpomblack_1000_175_p` — Acetal POM Black
- `gizmodorks_pom_acetalpomwhite_1000_175_p` — Acetal POM White
- `gizmodorks_pva_pvafilament_1000_175_p` — PVA Filament
- `gizmodorks_tpu_tpublack_1000_175_p` — TPU Black
- `gizmodorks_tpu_tpublue_1000_175_p` — TPU Blue
- `gizmodorks_tpu_tpured_1000_175_p` — TPU Red
- `gizmodorks_tpu_tpuwhite_1000_175_p` — TPU White
- `gizmodorks_tpu_tpuyellow_1000_175_p` — TPU Yellow
