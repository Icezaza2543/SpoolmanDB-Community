# sirayatech duplicate migration review

Base `12e7b92febf7b5da38e9051a99edfc6a9b02c0f5`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `2e76833ef84198903eaf04089838ce09591e6010ccfaf18671296e1ce4cf7500`.

## Authorization and result

{"groups": 1, "approved_groups": 0, "retired": 0, "deferred": 1, "hard_stops": 0, "before_count": 51701, "after_count": 51701, "brand_before": 35, "brand_after": 35, "registry_before": 1733, "registry_after": 1733, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

HF-Black/HFBlack tie unbound exactline/SKU despite bothblack. Defer; currentTDS copyerrors not resolved by borrowingProHF1.3. No identifiers or metadata edits.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. Future reviewed retirements would not redirect external catalog lookups automatically.

## Current first-party evidence

- {"url": "https://siraya.tech/pages/fibreheart-petg-cf-hf-tds-3d-printing-filament", "density": 1.25, "sku": "ST3018", "note": "CurrentHighFlowBlack; pageprintingsection saysPET-CF andspec saysglassfiber despiteCF, so230–250/80 remains copy-error-ambiguous. ProHF/ST3031distinct."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### ST001: dup-e8f507721d490796752bf5cccef4e230205242341cae0ad8b38ffb5871318d98

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`sirayatech_petg-cf_cfhf-black_1000_175_p`|`Cf {color_name}`|`HF - Black`|{"source_file": "sirayatech.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / False|
|`sirayatech_petg-cf_cfhfblack_1000_175_p`|`Cf {color_name}`|`HF Black`|{"source_file": "sirayatech.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 5, "compiled_records": 5} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `sirayatech_tpu_64dblack_1000_175_p` — 64D Black
- `sirayatech_tpu_64dwhite_1000_175_p` — 64D White
- `sirayatech_peba_85ablack_1000_175_p` — 85A Black
- `sirayatech_tpu_85ablack_1000_175_p` — 85A Black
- `sirayatech_tpu_85aclear_1000_175_p` — 85A Clear
- `sirayatech_tpu_85agreen_1000_175_p` — 85A Green
- `sirayatech_tpu_85awhite_1000_175_p` — 85A White
- `sirayatech_tpu_95ablack_1000_175_p` — 95A Black
- `sirayatech_peba_95ablack_800_175_p` — 95A Black
- `sirayatech_peba_airblack_800_175_p` — Air Black
- `sirayatech_tpu_airblack_800_175_p` — Air Black
- `sirayatech_tpu_airgreen_800_175_p` — Air Green
- `sirayatech_tpu_airwhite_800_175_p` — Air White
- `sirayatech_ppa-cf_cfblack_1000_175_p` — Cf Black
- `sirayatech_pet-cf_cfblack_1000_175_p` — Cf Black
- `sirayatech_paht-cf_cfblack_1000_175_p` — Cf Black
- `sirayatech_petg-cf_cfblack-rcf08_1000_175_p` — Cf Black - rCF08
- `sirayatech_petg-cf_cfprohfblack_1000_175_p` — Cf Pro HF Black
- `sirayatech_petg-cf_cfrcf08black_1000_175_p` — Cf rCF08 Black
- `sirayatech_abs-cf_cfcoreblack_1000_175_p` — Cf Core Black
- `sirayatech_asa-gf_gfblack_1000_175_p` — Gf Black
- `sirayatech_asa-gf_gfwhite_1000_175_p` — Gf White
- `sirayatech_ppa-gf_gfblack_1000_175_p` — Gf Black
- `sirayatech_pet-gf_gfblack_1000_175_p` — Gf Black
- `sirayatech_pet-gf_gfflatdarkearth_1000_175_p` — Gf Flat Dark Earth
- `sirayatech_pet-gf_gfodgreen_1000_175_p` — Gf OD Green
- `sirayatech_pet-gf_gfwhite_1000_175_p` — Gf White
- `sirayatech_tpu-gf_gfblack_1000_175_p` — Gf Black
- `sirayatech_abs-gf_gfblack_1000_175_p` — Gf Black
- `sirayatech_abs-gf_gfgrey_1000_175_p` — Gf Grey
- `sirayatech_abs-gf_gfwhite_1000_175_p` — Gf White
- `sirayatech_abs_hthfblack_1000_175_p` — Ht HF Black
- `sirayatech_abs_hthfwhite_1000_175_p` — Ht HF White
