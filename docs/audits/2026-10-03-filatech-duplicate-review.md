# filatech duplicate migration review

Base `6b14472c4a877c4d34627271ed7bf3088a801fe7`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `568b4eed28c9f1d5216d30734e0fcaf3707c3137e33d4a6e757fc611342b58a9`.

## Authorization and result

{"groups": 24, "approved_groups": 0, "retired": 0, "deferred": 24, "hard_stops": 0, "before_count": 51889, "after_count": 51889, "brand_before": 228, "brand_after": 228, "registry_before": 1545, "registry_after": 1545, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

All24 groups deferred:16Rule5 Hyper qualifier-in-color mismatches and8spelling/punctuation ties without same-SKU proof. Older well-formed Hyper families conceptually preferable, but strict line/color keys prevent authorized retirement now; originalpayloads and HB/HL codes unchanged. Hyper printing values carry plain-grade defaults and HyperPLA wrong plainPLA TDS link; exactcurrentgrade evidence recorded for later tooling/evidence work, no speculativeHyper density or changes to deferred records. Packaging/tare unchanged.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. Future reviewed retirements would not redirect external catalog lookups automatically.

## Current first-party evidence

- {"url": "https://fila-tech.store/product/pla-filament/", "note": "Current generic selector SKU N/A; no same-SKU spelling bindings."}
- {"url": "https://fila-tech.store/product/abs-filament/", "note": "Current page links exact grade configuration PDF."}
- {"url": "https://fila-tech.store/wp-content/uploads/2025/04/Recommended-Printer-Configuration.pdf", "note": "HyperPLA nozzle220 all layers,bed60first/55others;HyperABS nozzle265–270,bed100first/90others. Layer settings not generic min/max inferred ranges."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### FT001: dup-6c56df589bf051654df05f13b0d3e8e14b33f9c085a32f10cd10bef427f48d3f

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_abs_absdarkblue(luminous)_500_175_p`|`ABS {color_name}`|`Dark Blue (Luminous)`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|
|`filatech_abs_absdarkblueluminous_500_175_p`|`ABS {color_name}`|`Dark Blue Luminous`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_abs_absdarkblue(luminous)_500_175_p": "0066D9",
    "filatech_abs_absdarkblueluminous_500_175_p": "1e90ff"
  },
  "glow": {
    "filatech_abs_absdarkblue(luminous)_500_175_p": false,
    "filatech_abs_absdarkblueluminous_500_175_p": true
  },
  "codes": {
    "filatech_abs_absdarkblue(luminous)_500_175_p": null,
    "filatech_abs_absdarkblueluminous_500_175_p": [
      "AB110502",
      "AB120502"
    ]
  }
}
```

### FT002: dup-712f04936664f7ee38212fe8a5d35796b69e4d12af8b6c34bddc9831782ca725

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_abs_absdarkblue(luminous)_1000_175_p`|`ABS {color_name}`|`Dark Blue (Luminous)`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|
|`filatech_abs_absdarkblueluminous_1000_175_p`|`ABS {color_name}`|`Dark Blue Luminous`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_abs_absdarkblue(luminous)_1000_175_p": "0066D9",
    "filatech_abs_absdarkblueluminous_1000_175_p": "1e90ff"
  },
  "glow": {
    "filatech_abs_absdarkblue(luminous)_1000_175_p": false,
    "filatech_abs_absdarkblueluminous_1000_175_p": true
  },
  "codes": {
    "filatech_abs_absdarkblue(luminous)_1000_175_p": null,
    "filatech_abs_absdarkblueluminous_1000_175_p": [
      "AB110502",
      "AB120502"
    ]
  }
}
```

### FT003: dup-5bd771be0ff91ae7264ea796f6c516f4d707b45f4b153ee4a46dbc53b1265693

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_abs_absdarkgreen(luminous)_1000_175_p`|`ABS {color_name}`|`Dark Green (Luminous)`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|
|`filatech_abs_absdarkgreenluminous_1000_175_p`|`ABS {color_name}`|`Dark Green Luminous`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_abs_absdarkgreen(luminous)_1000_175_p": "06B100",
    "filatech_abs_absdarkgreenluminous_1000_175_p": "39ff14"
  },
  "glow": {
    "filatech_abs_absdarkgreen(luminous)_1000_175_p": false,
    "filatech_abs_absdarkgreenluminous_1000_175_p": true
  },
  "codes": {
    "filatech_abs_absdarkgreen(luminous)_1000_175_p": null,
    "filatech_abs_absdarkgreenluminous_1000_175_p": [
      "AB110602",
      "AB120602"
    ]
  }
}
```

### FT004: dup-d68408ed2ead82cc133675a2956ed4f5b8a895932f480b4b2ada703d937a55f9

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_abs_absdarkgreen(luminous)_500_175_p`|`ABS {color_name}`|`Dark Green (Luminous)`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|
|`filatech_abs_absdarkgreenluminous_500_175_p`|`ABS {color_name}`|`Dark Green Luminous`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_abs_absdarkgreen(luminous)_500_175_p": "06B100",
    "filatech_abs_absdarkgreenluminous_500_175_p": "39ff14"
  },
  "glow": {
    "filatech_abs_absdarkgreen(luminous)_500_175_p": false,
    "filatech_abs_absdarkgreenluminous_500_175_p": true
  },
  "codes": {
    "filatech_abs_absdarkgreen(luminous)_500_175_p": null,
    "filatech_abs_absdarkgreenluminous_500_175_p": [
      "AB110602",
      "AB120602"
    ]
  }
}
```

### FT005: dup-634ea9765d5f9567bb812e6558071365a0fc6043a645cf3d4d7f75a0a9dc433f

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_abs_absdarkyellow(luminous)_1000_175_p`|`ABS {color_name}`|`Dark Yellow (Luminous)`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|
|`filatech_abs_absdarkyellowluminous_1000_175_p`|`ABS {color_name}`|`Dark Yellow Luminous`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_abs_absdarkyellow(luminous)_1000_175_p": "FADB24",
    "filatech_abs_absdarkyellowluminous_1000_175_p": "ffff33"
  },
  "glow": {
    "filatech_abs_absdarkyellow(luminous)_1000_175_p": false,
    "filatech_abs_absdarkyellowluminous_1000_175_p": true
  },
  "codes": {
    "filatech_abs_absdarkyellow(luminous)_1000_175_p": null,
    "filatech_abs_absdarkyellowluminous_1000_175_p": [
      "AB120402"
    ]
  }
}
```

### FT006: dup-d95756313225bf388b2a834b404bcb8ab3d2fe0a4eb661bbe9b2a0ce22035e24

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_abs_absdarkyellow(luminous)_500_175_p`|`ABS {color_name}`|`Dark Yellow (Luminous)`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|
|`filatech_abs_absdarkyellowluminous_500_175_p`|`ABS {color_name}`|`Dark Yellow Luminous`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_abs_absdarkyellow(luminous)_500_175_p": "FADB24",
    "filatech_abs_absdarkyellowluminous_500_175_p": "ffff33"
  },
  "glow": {
    "filatech_abs_absdarkyellow(luminous)_500_175_p": false,
    "filatech_abs_absdarkyellowluminous_500_175_p": true
  },
  "codes": {
    "filatech_abs_absdarkyellow(luminous)_500_175_p": null,
    "filatech_abs_absdarkyellowluminous_500_175_p": [
      "AB120402"
    ]
  }
}
```

### FT007: dup-cf5b2db6d7b6ba52e0c1ef2c27c33973cc26f659d7ec3b44804a9c27ca315d7e

Status: DEFERRED; survivor `filatech_abs_abshyperblack_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_abs_abshyperblack_1000_175_p`|`ABS {color_name}`|`Hyper Black`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|
|`filatech_abs_hyperabsblack_1000_175_p`|`Hyper ABS {color_name}`|`Black`|{"source_file": "filatech.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "codes": {
    "filatech_abs_abshyperblack_1000_175_p": null,
    "filatech_abs_hyperabsblack_1000_175_p": [
      "HB120200"
    ]
  }
}
```

### FT008: dup-a1c85f7cb7aca011a6a0f934a1d18494b71da070b36cd9f5b196d85bbc46e5fd

Status: DEFERRED; survivor `filatech_abs_abshyperdarkorange(luminous)_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_abs_abshyperdarkorange(luminous)_1000_175_p`|`ABS {color_name}`|`Hyper Dark Orange (Luminous)`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|
|`filatech_abs_hyperabsdarkorange(luminous)_1000_175_p`|`Hyper ABS {color_name}`|`Dark Orange (Luminous)`|{"source_file": "filatech.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_abs_abshyperdarkorange(luminous)_1000_175_p": "FF8E24",
    "filatech_abs_hyperabsdarkorange(luminous)_1000_175_p": "ff4500"
  },
  "glow": {
    "filatech_abs_abshyperdarkorange(luminous)_1000_175_p": false,
    "filatech_abs_hyperabsdarkorange(luminous)_1000_175_p": true
  },
  "codes": {
    "filatech_abs_abshyperdarkorange(luminous)_1000_175_p": null,
    "filatech_abs_hyperabsdarkorange(luminous)_1000_175_p": [
      "HB120702"
    ]
  }
}
```

### FT009: dup-dba388be555618db438aba8750fd2a98b9dadd667967bfded4d9cf50603e17c9

Status: DEFERRED; survivor `filatech_abs_abshyperdarkyellow(luminous)_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_abs_abshyperdarkyellow(luminous)_1000_175_p`|`ABS {color_name}`|`Hyper Dark Yellow (Luminous)`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|
|`filatech_abs_hyperabsdarkyellowluminous_1000_175_p`|`Hyper ABS {color_name}`|`Dark Yellow Luminous`|{"source_file": "filatech.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_abs_abshyperdarkyellow(luminous)_1000_175_p": "FADB24",
    "filatech_abs_hyperabsdarkyellowluminous_1000_175_p": "ffff33"
  },
  "glow": {
    "filatech_abs_abshyperdarkyellow(luminous)_1000_175_p": false,
    "filatech_abs_hyperabsdarkyellowluminous_1000_175_p": true
  },
  "codes": {
    "filatech_abs_abshyperdarkyellow(luminous)_1000_175_p": null,
    "filatech_abs_hyperabsdarkyellowluminous_1000_175_p": [
      "HB120402"
    ]
  }
}
```

### FT010: dup-1e34301c14aedc73f8141f5bbcb0eb5cf8a0768ddacad1b3882762e26c67445b

Status: DEFERRED; survivor `filatech_abs_abshypernaturalwhite_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_abs_abshypernaturalwhite_1000_175_p`|`ABS {color_name}`|`Hyper Natural White`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|
|`filatech_abs_hyperabsnaturalwhite_1000_175_p`|`Hyper ABS {color_name}`|`Natural White`|{"source_file": "filatech.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_abs_abshypernaturalwhite_1000_175_p": "EFEFEF",
    "filatech_abs_hyperabsnaturalwhite_1000_175_p": "f5f5dc"
  },
  "codes": {
    "filatech_abs_abshypernaturalwhite_1000_175_p": null,
    "filatech_abs_hyperabsnaturalwhite_1000_175_p": [
      "HB120000"
    ]
  }
}
```

### FT011: dup-7ec7d469b10bb426231f84125c3ccd1b29c60b996660034ed40f336dc2a51349

Status: DEFERRED; survivor `filatech_abs_abshyperravenblack_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_abs_abshyperravenblack_1000_175_p`|`ABS {color_name}`|`Hyper Raven Black`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|
|`filatech_abs_hyperabsravenblack_1000_175_p`|`Hyper ABS {color_name}`|`Raven Black`|{"source_file": "filatech.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_abs_abshyperravenblack_1000_175_p": "000000",
    "filatech_abs_hyperabsravenblack_1000_175_p": "808080"
  },
  "codes": {
    "filatech_abs_abshyperravenblack_1000_175_p": null,
    "filatech_abs_hyperabsravenblack_1000_175_p": [
      "HB120201"
    ]
  }
}
```

### FT012: dup-d9a9001a832bb323d88f80d15ac10d925b4283b4691f5dbebfb5123f7cd53df1

Status: DEFERRED; survivor `filatech_abs_abshyperred(luminous)_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_abs_abshyperred(luminous)_1000_175_p`|`ABS {color_name}`|`Hyper Red (Luminous)`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|
|`filatech_abs_hyperabsred(luminous)_1000_175_p`|`Hyper ABS {color_name}`|`Red (Luminous)`|{"source_file": "filatech.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_abs_abshyperred(luminous)_1000_175_p": "E03F26",
    "filatech_abs_hyperabsred(luminous)_1000_175_p": "ff1744"
  },
  "glow": {
    "filatech_abs_abshyperred(luminous)_1000_175_p": false,
    "filatech_abs_hyperabsred(luminous)_1000_175_p": true
  },
  "codes": {
    "filatech_abs_abshyperred(luminous)_1000_175_p": null,
    "filatech_abs_hyperabsred(luminous)_1000_175_p": [
      "HB120301"
    ]
  }
}
```

### FT013: dup-eaacaa880c7c6aa9cfbd40eae48a5c04a37d997c7a930579d893c28bfdd1cbca

Status: DEFERRED; survivor `filatech_abs_abshyperwhite_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_abs_abshyperwhite_1000_175_p`|`ABS {color_name}`|`Hyper White`|{"source_file": "filatech.json", "definition_index": 0, "weights": 2, "diameters": 1, "colors": 19, "compiled_records": 38} / False|
|`filatech_abs_hyperabswhite_1000_175_p`|`Hyper ABS {color_name}`|`White`|{"source_file": "filatech.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 7, "compiled_records": 7} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_abs_abshyperwhite_1000_175_p": "FFFFFF",
    "filatech_abs_hyperabswhite_1000_175_p": "ffffff"
  },
  "codes": {
    "filatech_abs_abshyperwhite_1000_175_p": null,
    "filatech_abs_hyperabswhite_1000_175_p": [
      "HB120100"
    ]
  }
}
```

### FT014: dup-4a1dbec764a062106be642ada78a35e78476fa71628f8b1f1180e043bb5f7dac

Status: DEFERRED; survivor `filatech_pla_plahyperblack_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_pla_hyperplablack_1000_175_p`|`Hyper PLA {color_name}`|`Black`|{"source_file": "filatech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|
|`filatech_pla_plahyperblack_1000_175_p`|`PLA {color_name}`|`Hyper Black`|{"source_file": "filatech.json", "definition_index": 11, "weights": 2, "diameters": 1, "colors": 33, "compiled_records": 66} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "codes": {
    "filatech_pla_hyperplablack_1000_175_p": [
      "HL120200"
    ],
    "filatech_pla_plahyperblack_1000_175_p": null
  }
}
```

### FT015: dup-3801b628f4b4ccf0c59dd7b734f791358d0868d9e5ea26411907bf4517c66549

Status: DEFERRED; survivor `filatech_pla_plahyperbronzegold_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_pla_hyperplabronzegold_1000_175_p`|`Hyper PLA {color_name}`|`Bronze Gold`|{"source_file": "filatech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|
|`filatech_pla_plahyperbronzegold_1000_175_p`|`PLA {color_name}`|`Hyper Bronze Gold`|{"source_file": "filatech.json", "definition_index": 11, "weights": 2, "diameters": 1, "colors": 33, "compiled_records": 66} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_pla_hyperplabronzegold_1000_175_p": "cd7f32",
    "filatech_pla_plahyperbronzegold_1000_175_p": "6D6E4A"
  },
  "codes": {
    "filatech_pla_hyperplabronzegold_1000_175_p": [
      "HL121104"
    ],
    "filatech_pla_plahyperbronzegold_1000_175_p": null
  }
}
```

### FT016: dup-e76071ff72acd89df9776c6dbe8f9aa4c9fce150c6bb6750abfc1767536d8c26

Status: DEFERRED; survivor `filatech_pla_plahyperdarkyellow_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_pla_hyperpladarkyellow_1000_175_p`|`Hyper PLA {color_name}`|`Dark Yellow`|{"source_file": "filatech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|
|`filatech_pla_plahyperdarkyellow_1000_175_p`|`PLA {color_name}`|`Hyper Dark Yellow`|{"source_file": "filatech.json", "definition_index": 11, "weights": 2, "diameters": 1, "colors": 33, "compiled_records": 66} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_pla_hyperpladarkyellow_1000_175_p": "cccc00",
    "filatech_pla_plahyperdarkyellow_1000_175_p": "FADB24"
  },
  "codes": {
    "filatech_pla_hyperpladarkyellow_1000_175_p": [
      "HL120403"
    ],
    "filatech_pla_plahyperdarkyellow_1000_175_p": null
  }
}
```

### FT017: dup-318cfa9ee6bca5870faedc4839a8cc9f706194918175697f3766a0acada85060

Status: DEFERRED; survivor `filatech_pla_plahypergrey_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_pla_hyperplagray_1000_175_p`|`Hyper PLA {color_name}`|`Gray`|{"source_file": "filatech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|
|`filatech_pla_plahypergrey_1000_175_p`|`PLA {color_name}`|`Hyper Grey`|{"source_file": "filatech.json", "definition_index": 11, "weights": 2, "diameters": 1, "colors": 33, "compiled_records": 66} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_pla_hyperplagray_1000_175_p": "808080",
    "filatech_pla_plahypergrey_1000_175_p": "D6D7D8"
  },
  "codes": {
    "filatech_pla_hyperplagray_1000_175_p": [
      "HL120800"
    ],
    "filatech_pla_plahypergrey_1000_175_p": null
  }
}
```

### FT018: dup-c43d41ce1aa17399f0d446529eced651bd133c322282f93693b4d99163c42fa8

Status: DEFERRED; survivor `filatech_pla_plahypernaturaltransparent_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_pla_hyperplanaturaltransparent_1000_175_p`|`Hyper PLA {color_name}`|`Natural Transparent`|{"source_file": "filatech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|
|`filatech_pla_plahypernaturaltransparent_1000_175_p`|`PLA {color_name}`|`Hyper Natural Transparent`|{"source_file": "filatech.json", "definition_index": 11, "weights": 2, "diameters": 1, "colors": 33, "compiled_records": 66} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_pla_hyperplanaturaltransparent_1000_175_p": "ffffff80",
    "filatech_pla_plahypernaturaltransparent_1000_175_p": "DFDFD3"
  },
  "translucent": {
    "filatech_pla_hyperplanaturaltransparent_1000_175_p": true,
    "filatech_pla_plahypernaturaltransparent_1000_175_p": false
  },
  "codes": {
    "filatech_pla_hyperplanaturaltransparent_1000_175_p": [
      "HL120001"
    ],
    "filatech_pla_plahypernaturaltransparent_1000_175_p": null
  }
}
```

### FT019: dup-20382129ba87bd406c7e6dab0cd7d94d0cdb0d1ab720fb84e901d3257780a03c

Status: DEFERRED; survivor `filatech_pla_plahypernaturalwhite_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_pla_hyperplanaturalwhite_1000_175_p`|`Hyper PLA {color_name}`|`Natural White`|{"source_file": "filatech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|
|`filatech_pla_plahypernaturalwhite_1000_175_p`|`PLA {color_name}`|`Hyper Natural White`|{"source_file": "filatech.json", "definition_index": 11, "weights": 2, "diameters": 1, "colors": 33, "compiled_records": 66} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_pla_hyperplanaturalwhite_1000_175_p": "f5f5dc",
    "filatech_pla_plahypernaturalwhite_1000_175_p": "F2EFE9"
  },
  "codes": {
    "filatech_pla_hyperplanaturalwhite_1000_175_p": [
      "HL120000"
    ],
    "filatech_pla_plahypernaturalwhite_1000_175_p": null
  }
}
```

### FT020: dup-bb9b106ad390ddb1a8cf909ff5a4f71937daab07384b05ff6754ae476580cad9

Status: DEFERRED; survivor `filatech_pla_plahypersnowwhite_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_pla_hyperplasnowwhite_1000_175_p`|`Hyper PLA {color_name}`|`Snow White`|{"source_file": "filatech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|
|`filatech_pla_plahypersnowwhite_1000_175_p`|`PLA {color_name}`|`Hyper Snow White`|{"source_file": "filatech.json", "definition_index": 11, "weights": 2, "diameters": 1, "colors": 33, "compiled_records": 66} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_pla_hyperplasnowwhite_1000_175_p": "fffafa",
    "filatech_pla_plahypersnowwhite_1000_175_p": "EFEFEF"
  },
  "codes": {
    "filatech_pla_hyperplasnowwhite_1000_175_p": [
      "HL120103"
    ],
    "filatech_pla_plahypersnowwhite_1000_175_p": null
  }
}
```

### FT021: dup-81d4d4f64e642f94cc8c1eba0c442cce0ae7d59eb18fd5d3b92ff8e2884dee6d

Status: DEFERRED; survivor `filatech_pla_plahyperyellow_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_pla_hyperplayellow_1000_175_p`|`Hyper PLA {color_name}`|`Yellow`|{"source_file": "filatech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|
|`filatech_pla_plahyperyellow_1000_175_p`|`PLA {color_name}`|`Hyper Yellow`|{"source_file": "filatech.json", "definition_index": 11, "weights": 2, "diameters": 1, "colors": 33, "compiled_records": 66} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_pla_hyperplayellow_1000_175_p": "ffd700",
    "filatech_pla_plahyperyellow_1000_175_p": "FFE15B"
  },
  "codes": {
    "filatech_pla_hyperplayellow_1000_175_p": [
      "HL120400"
    ],
    "filatech_pla_plahyperyellow_1000_175_p": null
  }
}
```

### FT022: dup-38416cb3510b7379825613a5267e2271dce43a2df8563c385aa1de2adb21c757

Status: DEFERRED; survivor `filatech_pla_plahyperyellow(luminous)_1000_175_p`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_pla_hyperplayellow(luminous)_1000_175_p`|`Hyper PLA {color_name}`|`Yellow (Luminous)`|{"source_file": "filatech.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 9, "compiled_records": 9} / False|
|`filatech_pla_plahyperyellow(luminous)_1000_175_p`|`PLA {color_name}`|`Hyper Yellow (Luminous)`|{"source_file": "filatech.json", "definition_index": 11, "weights": 2, "diameters": 1, "colors": 33, "compiled_records": 66} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_pla_hyperplayellow(luminous)_1000_175_p": "ffff33",
    "filatech_pla_plahyperyellow(luminous)_1000_175_p": "FBF942"
  },
  "glow": {
    "filatech_pla_hyperplayellow(luminous)_1000_175_p": true,
    "filatech_pla_plahyperyellow(luminous)_1000_175_p": false
  },
  "codes": {
    "filatech_pla_hyperplayellow(luminous)_1000_175_p": [
      "HL120401"
    ],
    "filatech_pla_plahyperyellow(luminous)_1000_175_p": null
  }
}
```

### FT023: dup-5b9afff239a6b3407013723a5e5d1d13a8f01cae8152544c84faececefc0f30f

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_pla_plagray_1000_175_p`|`PLA {color_name}`|`Gray`|{"source_file": "filatech.json", "definition_index": 11, "weights": 2, "diameters": 1, "colors": 33, "compiled_records": 66} / False|
|`filatech_pla_plagrey_1000_175_p`|`PLA {color_name}`|`Grey`|{"source_file": "filatech.json", "definition_index": 11, "weights": 2, "diameters": 1, "colors": 33, "compiled_records": 66} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_pla_plagray_1000_175_p": "808080",
    "filatech_pla_plagrey_1000_175_p": "D6D7D8"
  },
  "codes": {
    "filatech_pla_plagray_1000_175_p": [
      "PL120800"
    ],
    "filatech_pla_plagrey_1000_175_p": null
  }
}
```

### FT024: dup-7086b82ad1ee36839787d3e062e55c184e577a6f2ba1b30528d0fc9195d5c5dd

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`filatech_pla_plagray_6000_175_p`|`PLA {color_name}`|`Gray`|{"source_file": "filatech.json", "definition_index": 11, "weights": 2, "diameters": 1, "colors": 33, "compiled_records": 66} / False|
|`filatech_pla_plagrey_6000_175_p`|`PLA {color_name}`|`Grey`|{"source_file": "filatech.json", "definition_index": 11, "weights": 2, "diameters": 1, "colors": 33, "compiled_records": 66} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "filatech_pla_plagray_6000_175_p": "808080",
    "filatech_pla_plagrey_6000_175_p": "D6D7D8"
  },
  "codes": {
    "filatech_pla_plagray_6000_175_p": [
      "PL120800"
    ],
    "filatech_pla_plagrey_6000_175_p": null
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

- `filatech_abs_absblack_500_175_p` — ABS Black
- `filatech_abs_absdarkorange(luminous)_500_175_p` — ABS Dark Orange (Luminous)
- `filatech_abs_absnaturalwhite_500_175_p` — ABS Natural White
- `filatech_abs_absravenblack_500_175_p` — ABS Raven Black
- `filatech_abs_absred(luminous)_500_175_p` — ABS Red (Luminous)
- `filatech_abs_abswhite_500_175_p` — ABS White
- `filatech_abs_abshyperblack_500_175_p` — ABS Hyper Black
- `filatech_abs_abshyperdarkorange(luminous)_500_175_p` — ABS Hyper Dark Orange (Luminous)
- `filatech_abs_abshyperdarkyellow(luminous)_500_175_p` — ABS Hyper Dark Yellow (Luminous)
- `filatech_abs_abshypernaturalwhite_500_175_p` — ABS Hyper Natural White
- `filatech_abs_abshyperravenblack_500_175_p` — ABS Hyper Raven Black
- `filatech_abs_abshyperred(luminous)_500_175_p` — ABS Hyper Red (Luminous)
- `filatech_abs_abshyperwhite_500_175_p` — ABS Hyper White
- `filatech_abs_absblack_1000_175_p` — ABS Black
- `filatech_abs_absdarkorange(luminous)_1000_175_p` — ABS Dark Orange (Luminous)
- `filatech_abs_absnaturalwhite_1000_175_p` — ABS Natural White
- `filatech_abs_absravenblack_1000_175_p` — ABS Raven Black
- `filatech_abs_absred(luminous)_1000_175_p` — ABS Red (Luminous)
- `filatech_abs_abswhite_1000_175_p` — ABS White
- `filatech_pla-cf_filacarbonblack_500_175_p` — FilaCarbon Black
- `filatech_pla-cf_filacarbonblack_1000_175_p` — FilaCarbon Black
- `filatech_pla_filaplablack_1000_175_p` — FilaPLA Black
- `filatech_pla_filaplagreen_1000_175_p` — FilaPLA Green
- `filatech_pla_filaplalightbrown_1000_175_p` — FilaPLA Light Brown
- `filatech_pla_filaplanaturalwhite_1000_175_p` — FilaPLA Natural White
- `filatech_pla_filaplasilver_1000_175_p` — FilaPLA Silver
- `filatech_pla_filaplawhite_1000_175_p` — FilaPLA White
- `filatech_pla_filaplayellow_1000_175_p` — FilaPLA Yellow
- `filatech_petg_filatoughnaturalwhite_500_175_p` — FilaTough Natural White
- `filatech_petg_filatoughyellow(luminous)_500_175_p` — FilaTough Yellow (Luminous)
- `filatech_petg_filatoughnaturalwhite_1000_175_p` — FilaTough Natural White
- `filatech_petg_filatoughyellow(luminous)_1000_175_p` — FilaTough Yellow (Luminous)
- `filatech_hips_hipsblack_500_175_p` — HIPS Black
- `filatech_hips_hipsdarkgreenluminous_500_175_p` — HIPS Dark Green Luminous
- `filatech_hips_hipsdarkorange(luminous)_500_175_p` — HIPS Dark Orange (Luminous)
- `filatech_hips_hipsdarkredluminous_500_175_p` — HIPS Dark Red Luminous
- `filatech_hips_hipsdarkyellowluminous_500_175_p` — HIPS Dark Yellow Luminous
- `filatech_hips_hipsnatural_500_175_p` — HIPS Natural
- `filatech_hips_hipswhite_500_175_p` — HIPS White
- `filatech_hips_hipsblack_1000_175_p` — HIPS Black
- `filatech_hips_hipsdarkgreenluminous_1000_175_p` — HIPS Dark Green Luminous
- `filatech_hips_hipsdarkorange(luminous)_1000_175_p` — HIPS Dark Orange (Luminous)
- `filatech_hips_hipsdarkredluminous_1000_175_p` — HIPS Dark Red Luminous
- `filatech_hips_hipsdarkyellowluminous_1000_175_p` — HIPS Dark Yellow Luminous
- `filatech_hips_hipsnatural_1000_175_p` — HIPS Natural
- `filatech_hips_hipswhite_1000_175_p` — HIPS White
- `filatech_petg_hyperpetgblack_1000_175_p` — Hyper PETG Black
- `filatech_petg_hyperpetgnaturalclear_1000_175_p` — Hyper PETG Natural Clear
- `filatech_petg_hyperpetgwhite_1000_175_p` — Hyper PETG White
- `filatech_nylon_pablack_500_175_p` — PA Black
- `filatech_nylon_panatural_500_175_p` — PA Natural
- `filatech_nylon_pared(luminous)_500_175_p` — PA Red (Luminous)
- `filatech_nylon_pawhite_500_175_p` — PA White
- `filatech_nylon_payellow(luminous)_500_175_p` — PA Yellow (Luminous)
- `filatech_nylon_pablack_1000_175_p` — PA Black
- `filatech_nylon_panatural_1000_175_p` — PA Natural
- `filatech_nylon_pared(luminous)_1000_175_p` — PA Red (Luminous)
- `filatech_nylon_pawhite_1000_175_p` — PA White
- `filatech_nylon_payellow(luminous)_1000_175_p` — PA Yellow (Luminous)
- `filatech_pc_pcblack_500_175_p` — PC Black
- `filatech_pc_pcnaturalclear_500_175_p` — PC Natural Clear
- `filatech_pc_pcred_500_175_p` — PC Red
- `filatech_pc_pcwhite_500_175_p` — PC White
- `filatech_pc_pcyellow_500_175_p` — PC Yellow
- `filatech_pc_pcblack_1000_175_p` — PC Black
- `filatech_pc_pcnaturalclear_1000_175_p` — PC Natural Clear
- `filatech_pc_pcred_1000_175_p` — PC Red
- `filatech_pc_pcwhite_1000_175_p` — PC White
- `filatech_pc_pcyellow_1000_175_p` — PC Yellow
- `filatech_petg_petgblack_500_175_p` — PETG Black
- `filatech_petg_petgchocobrown_500_175_p` — PETG Choco Brown
- `filatech_petg_petgdarkblue_500_175_p` — PETG Dark Blue
- `filatech_petg_petgdarkmetallicgrey_500_175_p` — PETG Dark Metallic Grey
- `filatech_petg_petgdarkorange(luminous)_500_175_p` — PETG Dark Orange (Luminous)
- `filatech_petg_petgdarkredluminous_500_175_p` — PETG Dark Red Luminous
- `filatech_petg_petgdarkyellowluminous_500_175_p` — PETG Dark Yellow Luminous
- `filatech_petg_petggold_500_175_p` — PETG Gold
- `filatech_petg_petgnaturalclear_500_175_p` — PETG Natural Clear
- `filatech_petg_petgsilver_500_175_p` — PETG Silver
- `filatech_petg_petgwhite_500_175_p` — PETG White
- `filatech_petg_petgyellow_500_175_p` — PETG Yellow
- `filatech_petg_petgblack_1000_175_p` — PETG Black
- `filatech_petg_petgchocobrown_1000_175_p` — PETG Choco Brown
- `filatech_petg_petgdarkblue_1000_175_p` — PETG Dark Blue
- `filatech_petg_petgdarkmetallicgrey_1000_175_p` — PETG Dark Metallic Grey
- `filatech_petg_petgdarkorange(luminous)_1000_175_p` — PETG Dark Orange (Luminous)
- `filatech_petg_petgdarkredluminous_1000_175_p` — PETG Dark Red Luminous
- `filatech_petg_petgdarkyellowluminous_1000_175_p` — PETG Dark Yellow Luminous
- `filatech_petg_petggold_1000_175_p` — PETG Gold
- `filatech_petg_petgnaturalclear_1000_175_p` — PETG Natural Clear
- `filatech_petg_petgsilver_1000_175_p` — PETG Silver
- `filatech_petg_petgwhite_1000_175_p` — PETG White
- `filatech_petg_petgyellow_1000_175_p` — PETG Yellow
- `filatech_pla_plablack_1000_175_p` — PLA Black
- `filatech_pla_plablue_1000_175_p` — PLA Blue
- `filatech_pla_plachocobrown_1000_175_p` — PLA Choco Brown
- `filatech_pla_pladarkgreen_1000_175_p` — PLA Dark Green
- `filatech_pla_pladarkmetallicgrey_1000_175_p` — PLA Dark Metallic Grey
- `filatech_pla_pladarkorange(luminous)_1000_175_p` — PLA Dark Orange (Luminous)
- `filatech_pla_pladarkskyblue_1000_175_p` — PLA Dark Sky Blue
- `filatech_pla_pladarkyellow_1000_175_p` — PLA Dark Yellow
- `filatech_pla_plagreen(luminous)_1000_175_p` — PLA Green (Luminous)
- `filatech_pla_plahotpink_1000_175_p` — PLA Hot Pink
- `filatech_pla_planaturalwhite_1000_175_p` — PLA Natural White
- `filatech_pla_plaolivegold_1000_175_p` — PLA Olive Gold
- `filatech_pla_plapink_1000_175_p` — PLA Pink
- `filatech_pla_plared(luminous)_1000_175_p` — PLA Red (Luminous)
- `filatech_pla_plasilver_1000_175_p` — PLA Silver
- `filatech_pla_plasnowwhite_1000_175_p` — PLA Snow White
- `filatech_pla_platerracottabrown_1000_175_p` — PLA Terracotta Brown
- `filatech_pla_playellow_1000_175_p` — PLA Yellow
- `filatech_pla_playellow(fluorescent)_1000_175_p` — PLA Yellow (Fluorescent)
- `filatech_pla_playellow(luminous)_1000_175_p` — PLA Yellow (Luminous)
- `filatech_pla_plaorange(luminous)_1000_175_p` — PLA Orange (Luminous)
- `filatech_pla_plawhite_1000_175_p` — PLA White
- `filatech_pla_plablack_6000_175_p` — PLA Black
- `filatech_pla_plablue_6000_175_p` — PLA Blue
- `filatech_pla_plachocobrown_6000_175_p` — PLA Choco Brown
- `filatech_pla_pladarkgreen_6000_175_p` — PLA Dark Green
- `filatech_pla_pladarkmetallicgrey_6000_175_p` — PLA Dark Metallic Grey
- `filatech_pla_pladarkorange(luminous)_6000_175_p` — PLA Dark Orange (Luminous)
- `filatech_pla_pladarkskyblue_6000_175_p` — PLA Dark Sky Blue
- `filatech_pla_pladarkyellow_6000_175_p` — PLA Dark Yellow
- `filatech_pla_plagreen(luminous)_6000_175_p` — PLA Green (Luminous)
- `filatech_pla_plahotpink_6000_175_p` — PLA Hot Pink
- `filatech_pla_planaturalwhite_6000_175_p` — PLA Natural White
- `filatech_pla_plaolivegold_6000_175_p` — PLA Olive Gold
- `filatech_pla_plapink_6000_175_p` — PLA Pink
- `filatech_pla_plared(luminous)_6000_175_p` — PLA Red (Luminous)
- `filatech_pla_plasilver_6000_175_p` — PLA Silver
- `filatech_pla_plasnowwhite_6000_175_p` — PLA Snow White
- `filatech_pla_platerracottabrown_6000_175_p` — PLA Terracotta Brown
- `filatech_pla_playellow_6000_175_p` — PLA Yellow
- `filatech_pla_playellow(fluorescent)_6000_175_p` — PLA Yellow (Fluorescent)
- `filatech_pla_playellow(luminous)_6000_175_p` — PLA Yellow (Luminous)
- `filatech_pla_plahyperblack_6000_175_p` — PLA Hyper Black
- `filatech_pla_plahyperbronzegold_6000_175_p` — PLA Hyper Bronze Gold
- `filatech_pla_plahyperdarkyellow_6000_175_p` — PLA Hyper Dark Yellow
- `filatech_pla_plahypergrey_6000_175_p` — PLA Hyper Grey
- `filatech_pla_plahypernaturaltransparent_6000_175_p` — PLA Hyper Natural Transparent
- `filatech_pla_plahypernaturalwhite_6000_175_p` — PLA Hyper Natural White
- `filatech_pla_plahypersnowwhite_6000_175_p` — PLA Hyper Snow White
- `filatech_pla_plahyperyellow_6000_175_p` — PLA Hyper Yellow
- `filatech_pla_plahyperyellow(luminous)_6000_175_p` — PLA Hyper Yellow (Luminous)
- `filatech_pla_plaorange(luminous)_6000_175_p` — PLA Orange (Luminous)
- `filatech_pla_plawhite_6000_175_p` — PLA White
- `filatech_pla+_pla+black_500_175_p` — PLA+ Black
- `filatech_pla+_pla+blue_500_175_p` — PLA+ Blue
- `filatech_pla+_pla+orange(luminous)_500_175_p` — PLA+ Orange (Luminous)
- `filatech_pla+_pla+silver_500_175_p` — PLA+ Silver
- `filatech_pla+_pla+white_500_175_p` — PLA+ White
- `filatech_pla+_pla+yellow_500_175_p` — PLA+ Yellow
- `filatech_pla+_pla+black_1000_175_p` — PLA+ Black
- `filatech_pla+_pla+blue_1000_175_p` — PLA+ Blue
- `filatech_pla+_pla+orange(luminous)_1000_175_p` — PLA+ Orange (Luminous)
- `filatech_pla+_pla+silver_1000_175_p` — PLA+ Silver
- `filatech_pla+_pla+white_1000_175_p` — PLA+ White
- `filatech_pla+_pla+yellow_1000_175_p` — PLA+ Yellow
- `filatech_tpe_tpegray_500_175_p` — TPE Gray
- `filatech_tpe_tpeorange_500_175_p` — TPE Orange
- `filatech_tpe_tpered_500_175_p` — TPE Red
- `filatech_tpe_tpesilver_500_175_p` — TPE Silver
- `filatech_tpe_tpeyellow_500_175_p` — TPE Yellow
- `filatech_tpu_tpublack_500_175_p` — TPU Black
- `filatech_tpu_tpuorange_500_175_p` — TPU Orange
- `filatech_tpu_tpured_500_175_p` — TPU Red
- `filatech_tpu_tpuwhite_500_175_p` — TPU White
- `filatech_tpu_tpuyellow_500_175_p` — TPU Yellow
- `filatech_tpu_tpu2black_500_175_p` — TPU 2 Black
- `filatech_tpu_tpu2white_500_175_p` — TPU 2 White
- `filatech_tpu_tpu2yellow(luminous)_500_175_p` — TPU 2 Yellow (Luminous)
- `filatech_tpu_tpu2black_1000_175_p` — TPU 2 Black
- `filatech_tpu_tpu2white_1000_175_p` — TPU 2 White
- `filatech_tpu_tpu2yellow(luminous)_1000_175_p` — TPU 2 Yellow (Luminous)
- `filatech_pla+wood_woodpladarkash_500_175_p` — Wood PLA Dark Ash
- `filatech_pla+wood_woodplamahogany_500_175_p` — Wood PLA Mahogany
- `filatech_pla+wood_woodplanaturalwood_500_175_p` — Wood PLA Natural Wood
- `filatech_pla+wood_woodpladarkash_1000_175_p` — Wood PLA Dark Ash
- `filatech_pla+wood_woodplamahogany_1000_175_p` — Wood PLA Mahogany
- `filatech_pla+wood_woodplanaturalwood_1000_175_p` — Wood PLA Natural Wood
