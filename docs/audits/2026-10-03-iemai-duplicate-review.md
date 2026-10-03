# iemai duplicate migration review

Base `f4a3099ea18f4d6f3284f9f8cd18c3e481e00bcd`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `f9c01db857f46744649f280025804ff2fcb870ee32dc34e9f871fc3cd1c3df90`.

## Authorization and result

{"groups": 3, "approved_groups": 3, "retired": 3, "deferred": 0, "hard_stops": 0, "before_count": 51709, "after_count": 51706, "brand_before": 36, "brand_after": 33, "registry_before": 1725, "registry_after": 1728, "metadata_fields_changed": 3, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Three Rule2 strict duplicates. Correct twoPLA densities1.24→1.17 and onePC1.20→1.19 from current-linked exactmaterialTDS. No current printing manual retrieved; existing temperatures kept unresolved. No identifiers or packaging/tare edits.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://store.iemai3d.com/index.php/product/pla/", "note": "Current product actively links exactPLA TDS."}
- {"url": "https://store.iemai3d.com/wp-content/uploads/2024/01/06_PLA-Filament-TDS.pdf", "density": 1.17}
- {"url": "https://www.iemai3d.com/index.php/download/", "note": "Current manufacturer downloadcentre actively links all-materialTDS."}
- {"url": "https://www.iemai3d.com/wp-content/uploads/2022/11/00_IEMAI_All_Filament_TDS.pdf", "note": "PC sectionp17 density1.19; no printing values stated."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`iemai_pc_iemaipcblack_1000_175_p`|`iemai_pc_pcblack_1000_175_p`|`iemai.json::IEMAI::IEMAI PC {color_name}::IEMAI PC Black::PC::1000::1.75::plastic::False`|
|`iemai_pla_iemaiplablack_1000_175_p`|`iemai_pla_plablack_1000_175_p`|`iemai.json::IEMAI::IEMAI PLA {color_name}::IEMAI PLA Black::PLA::1000::1.75::plastic::False`|
|`iemai_pla_iemaiplawhite_1000_175_p`|`iemai_pla_plawhite_1000_175_p`|`iemai.json::IEMAI::IEMAI PLA {color_name}::IEMAI PLA White::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### IE001: dup-87136a46ecd8954df476b085b8865beafbb92058287f3848ddd82ca7163bacb8

Status: APPROVED; survivor `iemai_pc_pcblack_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`iemai_pc_iemaipcblack_1000_175_p`|`IEMAI PC {color_name}`|`Black`|{"source_file": "iemai.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / False|
|`iemai_pc_pcblack_1000_175_p`|`PC {color_name}`|`Black`|{"source_file": "iemai.json", "definition_index": 12, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "iemai_pc_iemaipcblack_1000_175_p": 200,
    "iemai_pc_pcblack_1000_175_p": 250
  },
  "extruder_temp": {
    "iemai_pc_iemaipcblack_1000_175_p": 260,
    "iemai_pc_pcblack_1000_175_p": null
  },
  "extruder_temp_range": {
    "iemai_pc_iemaipcblack_1000_175_p": null,
    "iemai_pc_pcblack_1000_175_p": [
      250,
      280
    ]
  },
  "bed_temp": {
    "iemai_pc_iemaipcblack_1000_175_p": 100,
    "iemai_pc_pcblack_1000_175_p": null
  },
  "bed_temp_range": {
    "iemai_pc_iemaipcblack_1000_175_p": null,
    "iemai_pc_pcblack_1000_175_p": [
      100,
      110
    ]
  }
}
```

### IE002: dup-82cf2209518965bd62585805c1257e28ca114170e78b848d90d3d972a9aaf9c7

Status: APPROVED; survivor `iemai_pla_plablack_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`iemai_pla_iemaiplablack_1000_175_p`|`IEMAI PLA {color_name}`|`Black`|{"source_file": "iemai.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / False|
|`iemai_pla_plablack_1000_175_p`|`PLA {color_name}`|`Black`|{"source_file": "iemai.json", "definition_index": 20, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "iemai_pla_iemaiplablack_1000_175_p": 200,
    "iemai_pla_plablack_1000_175_p": 250
  },
  "extruder_temp": {
    "iemai_pla_iemaiplablack_1000_175_p": 205,
    "iemai_pla_plablack_1000_175_p": null
  },
  "extruder_temp_range": {
    "iemai_pla_iemaiplablack_1000_175_p": null,
    "iemai_pla_plablack_1000_175_p": [
      190,
      240
    ]
  },
  "bed_temp": {
    "iemai_pla_iemaiplablack_1000_175_p": 55,
    "iemai_pla_plablack_1000_175_p": null
  },
  "bed_temp_range": {
    "iemai_pla_iemaiplablack_1000_175_p": null,
    "iemai_pla_plablack_1000_175_p": [
      45,
      60
    ]
  }
}
```

### IE003: dup-2c36e60d84f446bc5c6899adbf386bc1c23c30036a86d00bb67f706e7b88b226

Status: APPROVED; survivor `iemai_pla_plawhite_1000_175_p`; Rule 2.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`iemai_pla_iemaiplawhite_1000_175_p`|`IEMAI PLA {color_name}`|`White`|{"source_file": "iemai.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / False|
|`iemai_pla_plawhite_1000_175_p`|`PLA {color_name}`|`White`|{"source_file": "iemai.json", "definition_index": 20, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "iemai_pla_iemaiplawhite_1000_175_p": 200,
    "iemai_pla_plawhite_1000_175_p": 250
  },
  "extruder_temp": {
    "iemai_pla_iemaiplawhite_1000_175_p": 205,
    "iemai_pla_plawhite_1000_175_p": null
  },
  "extruder_temp_range": {
    "iemai_pla_iemaiplawhite_1000_175_p": null,
    "iemai_pla_plawhite_1000_175_p": [
      190,
      240
    ]
  },
  "bed_temp": {
    "iemai_pla_iemaiplawhite_1000_175_p": 55,
    "iemai_pla_plawhite_1000_175_p": null
  },
  "bed_temp_range": {
    "iemai_pla_iemaiplawhite_1000_175_p": null,
    "iemai_pla_plawhite_1000_175_p": [
      45,
      60
    ]
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "iemai_pla_plawhite_1000_175_p",
      "values": {
        "density": 1.17
      },
      "source": "https://store.iemai3d.com/wp-content/uploads/2024/01/06_PLA-Filament-TDS.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "iemai_pla_plablack_1000_175_p",
      "values": {
        "density": 1.17
      },
      "source": "https://store.iemai3d.com/wp-content/uploads/2024/01/06_PLA-Filament-TDS.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "iemai_pc_pcblack_1000_175_p",
      "values": {
        "density": 1.19
      },
      "source": "https://www.iemai3d.com/wp-content/uploads/2022/11/00_IEMAI_All_Filament_TDS.pdf",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    }
  ],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `iemai_pla_iemaiplagrey_1000_175_p` — IEMAI PLA Grey
- `iemai_pc_iemaipctransparent_1000_175_p` — IEMAI PC Transparent
- `iemai_abs_absblack_1000_175_p` — ABS Black
- `iemai_abs_abswhite_1000_175_p` — ABS White
- `iemai_abs_cf-absblack_1000_175_p` — CF-ABS Black
- `iemai_abs_esd-absblack_1000_175_p` — ESD-ABS Black
- `iemai_asa_asablack_1000_175_p` — ASA Black
- `iemai_asa_asawhite_1000_175_p` — ASA White
- `iemai_asa_cf-asablack_1000_175_p` — CF-ASA Black
- `iemai_pa12_cf-pa12black_1000_175_p` — CF-PA12 Black
- `iemai_pa12_gf-pa12black_1000_175_p` — GF-PA12 Black
- `iemai_pa12_pa12black_1000_175_p` — PA12 Black
- `iemai_pa12_pa12natural_1000_175_p` — PA12 Natural
- `iemai_pa6_cf-pa6black_1000_175_p` — CF-PA6 Black
- `iemai_pc_cf-pcmatteblack_1000_175_p` — CF-PC Matte Black
- `iemai_pc_pcclear_1000_175_p` — PC Clear
- `iemai_peek_peeknatural_1000_175_p` — PEEK Natural
- `iemai_pei_pei1010natural_1000_175_p` — PEI 1010 Natural
- `iemai_pei_pei9085amber_1000_175_p` — PEI 9085 Amber
- `iemai_pekk_pekknatural_1000_175_p` — PEKK Natural
- `iemai_petg_cf-petgblack_1000_175_p` — CF-PETG Black
- `iemai_petg_petgblack_1000_175_p` — PETG Black
- `iemai_petg_petgclear_1000_175_p` — PETG Clear
- `iemai_petg_petgwhite_1000_175_p` — PETG White
- `iemai_pla_cf-plablack_1000_175_p` — CF-PLA Black
- `iemai_pp_ppnatural_1000_175_p` — PP Natural
- `iemai_pps_cf-ppsblack_1000_175_p` — CF-PPS Black
- `iemai_ppsu_ppsunatural_1000_175_p` — PPSU Natural
- `iemai_tpu_tpublack_1000_175_p` — TPU Black
- `iemai_tpu_tpuwhite_1000_175_p` — TPU White
