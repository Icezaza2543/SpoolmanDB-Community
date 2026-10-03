# voxelpla duplicate migration review

Base `fd445d7eeff1bec8aac70080ff25f34799a5a517`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `57c1a0a08cf29d17a3cffadf31aaf74711a10c31b5dda5f9d4728e7ed96052e5`.

## Authorization and result

{"groups": 3, "approved_groups": 3, "retired": 3, "deferred": 0, "hard_stops": 0, "before_count": 51706, "after_count": 51703, "brand_before": 35, "brand_after": 32, "registry_before": 1728, "registry_after": 1731, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Three Rule1 strict duplicates. CurrentPlus/PRO sheets not bound to historical genericPLA/PETG; keep survivor values unresolved rather than borrow successor-line formula. No identifiers or packaging/tare edits.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://voxelpla.com/products/voxel-pla-pro-1-75mm-red-filament", "note": "CurrentPLA+HS(PRO), not proven old unqualifiedPLA."}
- {"url": "https://cdn.shopify.com/s/files/1/0632/8614/9338/files/PLA_pro_Technical_Data_Sheet.pdf?v=1661454587", "note": "PLA+PRO only; not applied."}
- {"url": "https://cdn.shopify.com/s/files/1/0632/8614/9338/files/PETG_pro_Technical_Data_Sheet.pdf?v=1705262318", "note": "PETG+PRO only; not applied."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`voxelpla_petg_petgblack_1000_175_p`|`voxelpla_petg_black_1000_175_p`|`voxelpla.json::VOXELPLA::PETG {color_name}::PETG Black::PETG::1000::1.75::plastic::False`|
|`voxelpla_pla_plabrown_1000_175_p`|`voxelpla_pla_brown_1000_175_p`|`voxelpla.json::VOXELPLA::PLA {color_name}::PLA Brown::PLA::1000::1.75::plastic::False`|
|`voxelpla_pla_plafireenginered_1000_175_p`|`voxelpla_pla_fireenginered_1000_175_p`|`voxelpla.json::VOXELPLA::PLA {color_name}::PLA Fire Engine Red::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### VX001: dup-762df267b6a322a9da43484649dbe83e124af298c0a8aeb570896ba1bad845c6

Status: APPROVED; survivor `voxelpla_petg_black_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`voxelpla_petg_black_1000_175_p`|`{color_name}`|`Black`|{"source_file": "voxelpla.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 1, "compiled_records": 1} / True|
|`voxelpla_petg_petgblack_1000_175_p`|`PETG {color_name}`|`Black`|{"source_file": "voxelpla.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "voxelpla_petg_black_1000_175_p": 217,
    "voxelpla_petg_petgblack_1000_175_p": 260
  },
  "color_hex": {
    "voxelpla_petg_black_1000_175_p": "383435",
    "voxelpla_petg_petgblack_1000_175_p": "000000"
  },
  "extruder_temp": {
    "voxelpla_petg_black_1000_175_p": 250,
    "voxelpla_petg_petgblack_1000_175_p": null
  },
  "extruder_temp_range": {
    "voxelpla_petg_black_1000_175_p": null,
    "voxelpla_petg_petgblack_1000_175_p": [
      220,
      250
    ]
  },
  "bed_temp": {
    "voxelpla_petg_black_1000_175_p": 80,
    "voxelpla_petg_petgblack_1000_175_p": null
  },
  "bed_temp_range": {
    "voxelpla_petg_black_1000_175_p": null,
    "voxelpla_petg_petgblack_1000_175_p": [
      70,
      90
    ]
  }
}
```

### VX002: dup-e1a6a0995c77ce5ecd1646b6072299ee7999f8d610ea08c6d7ae05020f019836

Status: APPROVED; survivor `voxelpla_pla_brown_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`voxelpla_pla_brown_1000_175_p`|`{color_name}`|`Brown`|{"source_file": "voxelpla.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / True|
|`voxelpla_pla_plabrown_1000_175_p`|`PLA {color_name}`|`Brown`|{"source_file": "voxelpla.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "voxelpla_pla_brown_1000_175_p": 217,
    "voxelpla_pla_plabrown_1000_175_p": 260
  },
  "color_hex": {
    "voxelpla_pla_brown_1000_175_p": "6A4A34",
    "voxelpla_pla_plabrown_1000_175_p": "935C34"
  },
  "extruder_temp": {
    "voxelpla_pla_brown_1000_175_p": 215,
    "voxelpla_pla_plabrown_1000_175_p": null
  },
  "extruder_temp_range": {
    "voxelpla_pla_brown_1000_175_p": null,
    "voxelpla_pla_plabrown_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "voxelpla_pla_brown_1000_175_p": 60,
    "voxelpla_pla_plabrown_1000_175_p": null
  },
  "bed_temp_range": {
    "voxelpla_pla_brown_1000_175_p": null,
    "voxelpla_pla_plabrown_1000_175_p": [
      50,
      70
    ]
  }
}
```

### VX003: dup-0f6a0c5d265a304a3ab7dbe6743b7259cbbfaa4fddbe237c3d4d776d035edd3a

Status: APPROVED; survivor `voxelpla_pla_fireenginered_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`voxelpla_pla_fireenginered_1000_175_p`|`{color_name}`|`Fire Engine Red`|{"source_file": "voxelpla.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / True|
|`voxelpla_pla_plafireenginered_1000_175_p`|`PLA {color_name}`|`Fire Engine Red`|{"source_file": "voxelpla.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 21, "compiled_records": 21} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "voxelpla_pla_fireenginered_1000_175_p": 217,
    "voxelpla_pla_plafireenginered_1000_175_p": 260
  },
  "color_hex": {
    "voxelpla_pla_fireenginered_1000_175_p": "8D0823",
    "voxelpla_pla_plafireenginered_1000_175_p": "E20010"
  },
  "extruder_temp": {
    "voxelpla_pla_fireenginered_1000_175_p": 215,
    "voxelpla_pla_plafireenginered_1000_175_p": null
  },
  "extruder_temp_range": {
    "voxelpla_pla_fireenginered_1000_175_p": null,
    "voxelpla_pla_plafireenginered_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "voxelpla_pla_fireenginered_1000_175_p": 60,
    "voxelpla_pla_plafireenginered_1000_175_p": null
  },
  "bed_temp_range": {
    "voxelpla_pla_fireenginered_1000_175_p": null,
    "voxelpla_pla_plafireenginered_1000_175_p": [
      50,
      70
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

- `voxelpla_pla_grey_1000_175_p` — Grey
- `voxelpla_petg_petgblue_1000_175_p` — PETG Blue
- `voxelpla_petg_petgcrystalclear_1000_175_p` — PETG Crystal Clear
- `voxelpla_petg_petggreen_1000_175_p` — PETG Green
- `voxelpla_petg_petggrey_1000_175_p` — PETG Grey
- `voxelpla_petg_petgorange_1000_175_p` — PETG Orange
- `voxelpla_petg_petgred_1000_175_p` — PETG Red
- `voxelpla_petg_petgsilver_1000_175_p` — PETG Silver
- `voxelpla_petg_petgwhite_1000_175_p` — PETG White
- `voxelpla_petg_petgyellow_1000_175_p` — PETG Yellow
- `voxelpla_pla_plaarmygreen_1000_175_p` — PLA Army Green
- `voxelpla_pla_placoolwhite_1000_175_p` — PLA Cool White
- `voxelpla_pla_pladarkpurple_1000_175_p` — PLA Dark Purple
- `voxelpla_pla_plafireorange_1000_175_p` — PLA Fire Orange
- `voxelpla_pla_plaforestgreen_1000_175_p` — PLA Forest Green
- `voxelpla_pla_plagold_1000_175_p` — PLA Gold
- `voxelpla_pla_plaiceclear_1000_175_p` — PLA Ice Clear
- `voxelpla_pla_plalavenderpurple_1000_175_p` — PLA Lavender Purple
- `voxelpla_pla_plamagenta_1000_175_p` — PLA Magenta
- `voxelpla_pla_plapink_1000_175_p` — PLA Pink
- `voxelpla_pla_plasilver_1000_175_p` — PLA Silver
- `voxelpla_pla_plaskyblue_1000_175_p` — PLA Sky Blue
- `voxelpla_pla_plavoxelblack_1000_175_p` — PLA Voxel Black
- `voxelpla_pla_plavoxelgrey_1000_175_p` — PLA Voxel Grey
- `voxelpla_pla_plavoxelphantomblue_1000_175_p` — PLA VOXEL Phantom Blue
- `voxelpla_pla_plavoxelroyalblue_1000_175_p` — PLA Voxel Royal Blue
- `voxelpla_pla_plawitchgreen_1000_175_p` — PLA Witch Green
- `voxelpla_pla_plawood_1000_175_p` — PLA Wood
- `voxelpla_pla_playellow_1000_175_p` — PLA Yellow
