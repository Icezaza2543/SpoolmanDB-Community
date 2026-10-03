# splice3d duplicate migration review

Base `ab87807148374ab7e905376cb78ef4c3e26a36bd`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `2e76833ef84198903eaf04089838ce09591e6010ccfaf18671296e1ce4cf7500`.

## Authorization and result

{"groups": 1, "approved_groups": 0, "retired": 0, "deferred": 1, "hard_stops": 0, "before_count": 51701, "after_count": 51701, "brand_before": 27, "brand_after": 27, "registry_before": 1733, "registry_after": 1733, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

IndustrialGray/Grey visibly differentHEX tie, no sameSKU proof; defer. Currentbedrange30–60 versusexisting25/30-only held in audit; no edits to deferredrecords.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. Future reviewed retirements would not redirect external catalog lookups automatically.

## Current first-party evidence

- {"url": "https://splice3d.com/products/workday-pla?variant=42268611346572", "nozzle": [190, 220], "bed": [30, 60], "note": "IndustrialGray exists, not proof that sourceGray/GreyHEXbdb7b9/5a5955 are sameSKU."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### SL001: dup-eb862602306fe656b8f581804b1cf96273a4503a63d4a60f44c9a794874885b1

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`splice3d_pla_plaindustrialgray_1000_175_p`|`PLA {color_name}`|`Industrial Gray`|{"source_file": "splice3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 23, "compiled_records": 23} / False|
|`splice3d_pla_plaindustrialgrey_1000_175_p`|`PLA {color_name}`|`Industrial Grey`|{"source_file": "splice3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 23, "compiled_records": 23} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "splice3d_pla_plaindustrialgray_1000_175_p": "bdb7b9",
    "splice3d_pla_plaindustrialgrey_1000_175_p": "5a5955"
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

- `splice3d_petg_hfblack_1000_175_p` — Hf Black
- `splice3d_petg_hfmidnightblue_1000_175_p` — Hf Midnight Blue
- `splice3d_petg_hfspringgreen_1000_175_p` — Hf Spring Green
- `splice3d_petg_hfwhite_1000_175_p` — Hf White
- `splice3d_pla_plaaquamarineblue_1000_175_p` — PLA Aquamarine Blue
- `splice3d_pla_plaautumnorange_1000_175_p` — PLA Autumn Orange
- `splice3d_pla_plablack_1000_175_p` — PLA Black
- `splice3d_pla_plabluelilac_1000_175_p` — PLA Blue Lilac
- `splice3d_pla_plabubblegumpink_1000_175_p` — PLA Bubblegum Pink
- `splice3d_pla_placaribbeanblue_1000_175_p` — PLA Caribbean Blue
- `splice3d_pla_placharcoalgray_1000_175_p` — PLA Charcoal Gray
- `splice3d_pla_plachocolatebrown_1000_175_p` — PLA Chocolate Brown
- `splice3d_pla_placopper_1000_175_p` — PLA Copper
- `splice3d_pla_plafluorescentorange_1000_175_p` — PLA Fluorescent Orange
- `splice3d_pla_plahotmagenta_1000_175_p` — PLA Hot Magenta
- `splice3d_pla_plajunglegreen_1000_175_p` — PLA Jungle Green
- `splice3d_pla_plalivelyyellow_1000_175_p` — PLA Lively Yellow
- `splice3d_pla_plamidnightblue_1000_175_p` — PLA Midnight Blue
- `splice3d_pla_planuttybrown_1000_175_p` — PLA Nutty Brown
- `splice3d_pla_plapoppyred_1000_175_p` — PLA Poppy Red
- `splice3d_pla_plaryobytegreen_1000_175_p` — PLA Ryobyte Green
- `splice3d_pla_plaskyblue_1000_175_p` — PLA Sky Blue
- `splice3d_pla_plaspringgreen_1000_175_p` — PLA Spring Green
- `splice3d_pla_plawhite_1000_175_p` — PLA White
- `splice3d_pla_plazincyellow_1000_175_p` — PLA Zinc Yellow
