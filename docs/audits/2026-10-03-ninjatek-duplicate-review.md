# ninjatek duplicate migration review

Base `bf20f42c24871e22aeabca0c99579be9bcf5837a`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `3f06c6aad7454ee7775bf81d767c80b0448e16bac0667b639ccbfa0d584cfc2e`.

## Authorization and result

{"groups": 20, "approved_groups": 20, "retired": 20, "deferred": 0, "hard_stops": 0, "before_count": 51861, "after_count": 51841, "brand_before": 197, "brand_after": 177, "registry_before": 1573, "registry_after": 1593, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Current exact official names select NinjaFlex/Cheetah by Rule 3 before Cartesian family size. Current nozzle and exact-line densities agree with survivor values. Qualitative ambient-to-50 bed recommendation is not converted to zero or an invented lower bound. HEX/translucency conflicts remain unresolved; survivor values retained. Packaging/tare unchanged.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://ninjatek.com/shop/ninjaflex/", "name": "NinjaFlex", "nozzle": [225, 250], "bed": "room temperature to 50 C; qualitative lower bound not encoded"}
- {"url": "https://ninjatek.com/shop/cheetah/", "name": "Cheetah", "nozzle": [225, 250], "bed": "room temperature to 50 C; qualitative lower bound not encoded"}
- {"url": "https://ninjatek.com/wp-content/uploads/NinjaFlex-TDS.pdf", "density": 1.19}
- {"url": "https://ninjatek.com/wp-content/uploads/Cheetah-TDS.pdf", "density": 1.22}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`ninjatek_tpu_cheetahtpufirered_1000_175_p`|`ninjatek_tpu_cheetahfirered_1000_175_p`|`ninjatek.json::NinjaTek::Cheetah TPU {color_name}::Cheetah TPU Fire Red::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_cheetahtpuflamingopink_1000_175_p`|`ninjatek_tpu_cheetahflamingopink_1000_175_p`|`ninjatek.json::NinjaTek::Cheetah TPU {color_name}::Cheetah TPU Flamingo Pink::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_cheetahtpugrassgreen_1000_175_p`|`ninjatek_tpu_cheetahgrassgreen_1000_175_p`|`ninjatek.json::NinjaTek::Cheetah TPU {color_name}::Cheetah TPU Grass Green::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_cheetahtpulavaorange_1000_175_p`|`ninjatek_tpu_cheetahlavaorange_1000_175_p`|`ninjatek.json::NinjaTek::Cheetah TPU {color_name}::Cheetah TPU Lava Orange::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_cheetahtpumidnightblack_1000_175_p`|`ninjatek_tpu_cheetahmidnightblack_1000_175_p`|`ninjatek.json::NinjaTek::Cheetah TPU {color_name}::Cheetah TPU Midnight Black::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_cheetahtpusapphireblue_1000_175_p`|`ninjatek_tpu_cheetahsapphireblue_1000_175_p`|`ninjatek.json::NinjaTek::Cheetah TPU {color_name}::Cheetah TPU Sapphire Blue::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_cheetahtpusnowwhite_1000_175_p`|`ninjatek_tpu_cheetahsnowwhite_1000_175_p`|`ninjatek.json::NinjaTek::Cheetah TPU {color_name}::Cheetah TPU Snow White::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_cheetahtpusteelgray_1000_175_p`|`ninjatek_tpu_cheetahsteelgray_1000_175_p`|`ninjatek.json::NinjaTek::Cheetah TPU {color_name}::Cheetah TPU Steel Gray::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_cheetahtpusunyellow_1000_175_p`|`ninjatek_tpu_cheetahsunyellow_1000_175_p`|`ninjatek.json::NinjaTek::Cheetah TPU {color_name}::Cheetah TPU Sun Yellow::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_cheetahtpuwatertranslucent_1000_175_p`|`ninjatek_tpu_cheetahwatertranslucent_1000_175_p`|`ninjatek.json::NinjaTek::Cheetah TPU {color_name}::Cheetah TPU Water Translucent::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_ninjaflextpufirered_1000_175_p`|`ninjatek_tpu_ninjaflexfirered_1000_175_p`|`ninjatek.json::NinjaTek::NinjaFlex TPU {color_name}::NinjaFlex TPU Fire Red::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_ninjaflextpuflamingopink_1000_175_p`|`ninjatek_tpu_ninjaflexflamingopink_1000_175_p`|`ninjatek.json::NinjaTek::NinjaFlex TPU {color_name}::NinjaFlex TPU Flamingo Pink::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_ninjaflextpugrassgreen_1000_175_p`|`ninjatek_tpu_ninjaflexgrassgreen_1000_175_p`|`ninjatek.json::NinjaTek::NinjaFlex TPU {color_name}::NinjaFlex TPU Grass Green::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_ninjaflextpulavaorange_1000_175_p`|`ninjatek_tpu_ninjaflexlavaorange_1000_175_p`|`ninjatek.json::NinjaTek::NinjaFlex TPU {color_name}::NinjaFlex TPU Lava Orange::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_ninjaflextpumidnightblack_1000_175_p`|`ninjatek_tpu_ninjaflexmidnightblack_1000_175_p`|`ninjatek.json::NinjaTek::NinjaFlex TPU {color_name}::NinjaFlex TPU Midnight Black::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_ninjaflextpusapphireblue_1000_175_p`|`ninjatek_tpu_ninjaflexsapphireblue_1000_175_p`|`ninjatek.json::NinjaTek::NinjaFlex TPU {color_name}::NinjaFlex TPU Sapphire Blue::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_ninjaflextpusnowwhite_1000_175_p`|`ninjatek_tpu_ninjaflexsnowwhite_1000_175_p`|`ninjatek.json::NinjaTek::NinjaFlex TPU {color_name}::NinjaFlex TPU Snow White::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_ninjaflextpusteelgray_1000_175_p`|`ninjatek_tpu_ninjaflexsteelgray_1000_175_p`|`ninjatek.json::NinjaTek::NinjaFlex TPU {color_name}::NinjaFlex TPU Steel Gray::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_ninjaflextpusunyellow_1000_175_p`|`ninjatek_tpu_ninjaflexsunyellow_1000_175_p`|`ninjatek.json::NinjaTek::NinjaFlex TPU {color_name}::NinjaFlex TPU Sun Yellow::TPU::1000::1.75::plastic::False`|
|`ninjatek_tpu_ninjaflextpuwatertranslucent_1000_175_p`|`ninjatek_tpu_ninjaflexwatertranslucent_1000_175_p`|`ninjatek.json::NinjaTek::NinjaFlex TPU {color_name}::NinjaFlex TPU Water Translucent::TPU::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### NT001: dup-62d7b96e1dc9de37d9500be25d5f01368a7c2b3ac850634275ea5d2c723c6af9

Status: APPROVED; survivor `ninjatek_tpu_cheetahfirered_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_cheetahfirered_1000_175_p`|`Cheetah {color_name}`|`Fire Red`|{"source_file": "ninjatek.json", "definition_index": 1, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|
|`ninjatek_tpu_cheetahtpufirered_1000_175_p`|`Cheetah TPU {color_name}`|`Fire Red`|{"source_file": "ninjatek.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_cheetahfirered_1000_175_p": "e13326",
    "ninjatek_tpu_cheetahtpufirered_1000_175_p": "C00000"
  }
}
```

### NT002: dup-33fd3b69786f89117983e25e8a9b30b8b73e7526fde6154b704413308f80f6b6

Status: APPROVED; survivor `ninjatek_tpu_cheetahflamingopink_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_cheetahflamingopink_1000_175_p`|`Cheetah {color_name}`|`Flamingo Pink`|{"source_file": "ninjatek.json", "definition_index": 1, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|
|`ninjatek_tpu_cheetahtpuflamingopink_1000_175_p`|`Cheetah TPU {color_name}`|`Flamingo Pink`|{"source_file": "ninjatek.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_cheetahflamingopink_1000_175_p": "fc8eac",
    "ninjatek_tpu_cheetahtpuflamingopink_1000_175_p": "F06E92"
  }
}
```

### NT003: dup-d23adf539e6fced7640fa67bcaa8bb3abdddd7955267d9142686ac7a5f40f1aa

Status: APPROVED; survivor `ninjatek_tpu_cheetahgrassgreen_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_cheetahgrassgreen_1000_175_p`|`Cheetah {color_name}`|`Grass Green`|{"source_file": "ninjatek.json", "definition_index": 1, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|
|`ninjatek_tpu_cheetahtpugrassgreen_1000_175_p`|`Cheetah TPU {color_name}`|`Grass Green`|{"source_file": "ninjatek.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_cheetahgrassgreen_1000_175_p": "8bd25a",
    "ninjatek_tpu_cheetahtpugrassgreen_1000_175_p": "41A840"
  }
}
```

### NT004: dup-18a2b46dcc45b9b9622fb8809057019ad1862cb5e9f085626e31d172ceb59bd7

Status: APPROVED; survivor `ninjatek_tpu_cheetahlavaorange_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_cheetahlavaorange_1000_175_p`|`Cheetah {color_name}`|`Lava Orange`|{"source_file": "ninjatek.json", "definition_index": 1, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|
|`ninjatek_tpu_cheetahtpulavaorange_1000_175_p`|`Cheetah TPU {color_name}`|`Lava Orange`|{"source_file": "ninjatek.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_cheetahlavaorange_1000_175_p": "f85a22",
    "ninjatek_tpu_cheetahtpulavaorange_1000_175_p": "FF5F2E"
  }
}
```

### NT005: dup-081474535f145be2ca837d5ab12492de5236b181066e95d9b3e288c2724a0515

Status: APPROVED; survivor `ninjatek_tpu_cheetahmidnightblack_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_cheetahmidnightblack_1000_175_p`|`Cheetah {color_name}`|`Midnight Black`|{"source_file": "ninjatek.json", "definition_index": 1, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|
|`ninjatek_tpu_cheetahtpumidnightblack_1000_175_p`|`Cheetah TPU {color_name}`|`Midnight Black`|{"source_file": "ninjatek.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_cheetahmidnightblack_1000_175_p": "323239",
    "ninjatek_tpu_cheetahtpumidnightblack_1000_175_p": "000000"
  }
}
```

### NT006: dup-9530da7f148d865ae08afe4d803c2d55b36553ce5870e350c03f81b7dd82755a

Status: APPROVED; survivor `ninjatek_tpu_cheetahsapphireblue_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_cheetahsapphireblue_1000_175_p`|`Cheetah {color_name}`|`Sapphire Blue`|{"source_file": "ninjatek.json", "definition_index": 1, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|
|`ninjatek_tpu_cheetahtpusapphireblue_1000_175_p`|`Cheetah TPU {color_name}`|`Sapphire Blue`|{"source_file": "ninjatek.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_cheetahsapphireblue_1000_175_p": "1746a1",
    "ninjatek_tpu_cheetahtpusapphireblue_1000_175_p": "0022FF"
  }
}
```

### NT007: dup-a6e226011e26ef6f33db64b57851a3d3fbba32d675d8185788f0d916ae92c61e

Status: APPROVED; survivor `ninjatek_tpu_cheetahsnowwhite_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_cheetahsnowwhite_1000_175_p`|`Cheetah {color_name}`|`Snow White`|{"source_file": "ninjatek.json", "definition_index": 1, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|
|`ninjatek_tpu_cheetahtpusnowwhite_1000_175_p`|`Cheetah TPU {color_name}`|`Snow White`|{"source_file": "ninjatek.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_cheetahsnowwhite_1000_175_p": "f2f5f8",
    "ninjatek_tpu_cheetahtpusnowwhite_1000_175_p": "FFFFFF"
  }
}
```

### NT008: dup-129d3bc53c75e719026b60c3e8148a840b843a6f7b3793e06d85b8a6cb0b4e44

Status: APPROVED; survivor `ninjatek_tpu_cheetahsteelgray_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_cheetahsteelgray_1000_175_p`|`Cheetah {color_name}`|`Steel Gray`|{"source_file": "ninjatek.json", "definition_index": 1, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|
|`ninjatek_tpu_cheetahtpusteelgray_1000_175_p`|`Cheetah TPU {color_name}`|`Steel Gray`|{"source_file": "ninjatek.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_cheetahsteelgray_1000_175_p": "b7bab4",
    "ninjatek_tpu_cheetahtpusteelgray_1000_175_p": "AFAEAB"
  }
}
```

### NT009: dup-e552cdda2d25fb060924bdcbd5d7b80bad303d27b24e57b2861107bb0e01e28f

Status: APPROVED; survivor `ninjatek_tpu_cheetahsunyellow_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_cheetahsunyellow_1000_175_p`|`Cheetah {color_name}`|`Sun Yellow`|{"source_file": "ninjatek.json", "definition_index": 1, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|
|`ninjatek_tpu_cheetahtpusunyellow_1000_175_p`|`Cheetah TPU {color_name}`|`Sun Yellow`|{"source_file": "ninjatek.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_cheetahsunyellow_1000_175_p": "fbca18",
    "ninjatek_tpu_cheetahtpusunyellow_1000_175_p": "FFE15B"
  }
}
```

### NT010: dup-7417d291e21e5ab14a9ba8dbdf4b479189195c5db434616f9bb08de7eb7d7206

Status: APPROVED; survivor `ninjatek_tpu_cheetahwatertranslucent_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_cheetahtpuwatertranslucent_1000_175_p`|`Cheetah TPU {color_name}`|`Water Translucent`|{"source_file": "ninjatek.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`ninjatek_tpu_cheetahwatertranslucent_1000_175_p`|`Cheetah {color_name}`|`Water Translucent`|{"source_file": "ninjatek.json", "definition_index": 1, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_cheetahtpuwatertranslucent_1000_175_p": "F2EFE9",
    "ninjatek_tpu_cheetahwatertranslucent_1000_175_p": "eaeaea"
  },
  "translucent": {
    "ninjatek_tpu_cheetahtpuwatertranslucent_1000_175_p": false,
    "ninjatek_tpu_cheetahwatertranslucent_1000_175_p": true
  }
}
```

### NT011: dup-7f45145c6010da73480d75973edc55353b7713d86890cf50cb28c293efb21007

Status: APPROVED; survivor `ninjatek_tpu_ninjaflexfirered_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_ninjaflexfirered_1000_175_p`|`NinjaFlex {color_name}`|`Fire Red`|{"source_file": "ninjatek.json", "definition_index": 0, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|
|`ninjatek_tpu_ninjaflextpufirered_1000_175_p`|`NinjaFlex TPU {color_name}`|`Fire Red`|{"source_file": "ninjatek.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_ninjaflexfirered_1000_175_p": "e13326",
    "ninjatek_tpu_ninjaflextpufirered_1000_175_p": "D33D3D"
  }
}
```

### NT012: dup-348c33ed01be3ce1ea82e3a36c4b1a89e3c93664255d3ab6c9007201b24ea241

Status: APPROVED; survivor `ninjatek_tpu_ninjaflexflamingopink_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_ninjaflexflamingopink_1000_175_p`|`NinjaFlex {color_name}`|`Flamingo Pink`|{"source_file": "ninjatek.json", "definition_index": 0, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|
|`ninjatek_tpu_ninjaflextpuflamingopink_1000_175_p`|`NinjaFlex TPU {color_name}`|`Flamingo Pink`|{"source_file": "ninjatek.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_ninjaflexflamingopink_1000_175_p": "fc8eac",
    "ninjatek_tpu_ninjaflextpuflamingopink_1000_175_p": "F06E92"
  }
}
```

### NT013: dup-c43ca44cb795157849827db88298c0d45d8e1e8a891d397aaddab6f3bba2578d

Status: APPROVED; survivor `ninjatek_tpu_ninjaflexgrassgreen_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_ninjaflexgrassgreen_1000_175_p`|`NinjaFlex {color_name}`|`Grass Green`|{"source_file": "ninjatek.json", "definition_index": 0, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|
|`ninjatek_tpu_ninjaflextpugrassgreen_1000_175_p`|`NinjaFlex TPU {color_name}`|`Grass Green`|{"source_file": "ninjatek.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_ninjaflexgrassgreen_1000_175_p": "8bd25a",
    "ninjatek_tpu_ninjaflextpugrassgreen_1000_175_p": "41A840"
  }
}
```

### NT014: dup-87e58e8c598cc6da8c83153084c854d36817361974e069574875ac5949cb1fa0

Status: APPROVED; survivor `ninjatek_tpu_ninjaflexlavaorange_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_ninjaflexlavaorange_1000_175_p`|`NinjaFlex {color_name}`|`Lava Orange`|{"source_file": "ninjatek.json", "definition_index": 0, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|
|`ninjatek_tpu_ninjaflextpulavaorange_1000_175_p`|`NinjaFlex TPU {color_name}`|`Lava Orange`|{"source_file": "ninjatek.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_ninjaflexlavaorange_1000_175_p": "f85a22",
    "ninjatek_tpu_ninjaflextpulavaorange_1000_175_p": "FF7A33"
  }
}
```

### NT015: dup-c8ec2111f99a57de968d8a63bce125dcc108ac09ba1881264b7d1fce3e3e5e53

Status: APPROVED; survivor `ninjatek_tpu_ninjaflexmidnightblack_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_ninjaflexmidnightblack_1000_175_p`|`NinjaFlex {color_name}`|`Midnight Black`|{"source_file": "ninjatek.json", "definition_index": 0, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|
|`ninjatek_tpu_ninjaflextpumidnightblack_1000_175_p`|`NinjaFlex TPU {color_name}`|`Midnight Black`|{"source_file": "ninjatek.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_ninjaflexmidnightblack_1000_175_p": "323239",
    "ninjatek_tpu_ninjaflextpumidnightblack_1000_175_p": "000000"
  }
}
```

### NT016: dup-3a8315e10c8e381f53776b07fa69c66b80aa109eea59c3e934c4479e029c0bac

Status: APPROVED; survivor `ninjatek_tpu_ninjaflexsapphireblue_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_ninjaflexsapphireblue_1000_175_p`|`NinjaFlex {color_name}`|`Sapphire Blue`|{"source_file": "ninjatek.json", "definition_index": 0, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|
|`ninjatek_tpu_ninjaflextpusapphireblue_1000_175_p`|`NinjaFlex TPU {color_name}`|`Sapphire Blue`|{"source_file": "ninjatek.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_ninjaflexsapphireblue_1000_175_p": "1746a1",
    "ninjatek_tpu_ninjaflextpusapphireblue_1000_175_p": "0022FF"
  }
}
```

### NT017: dup-08011fa1c01d9c443748deae17c985caa1731ae69796444517119a76db0b09c1

Status: APPROVED; survivor `ninjatek_tpu_ninjaflexsnowwhite_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_ninjaflexsnowwhite_1000_175_p`|`NinjaFlex {color_name}`|`Snow White`|{"source_file": "ninjatek.json", "definition_index": 0, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|
|`ninjatek_tpu_ninjaflextpusnowwhite_1000_175_p`|`NinjaFlex TPU {color_name}`|`Snow White`|{"source_file": "ninjatek.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_ninjaflexsnowwhite_1000_175_p": "f2f5f8",
    "ninjatek_tpu_ninjaflextpusnowwhite_1000_175_p": "FFFFFF"
  }
}
```

### NT018: dup-ca53ec22af4a1e10b2ddb52aa0ffe363d732a7aa9ed9bbf2fff5ad501cf9e36b

Status: APPROVED; survivor `ninjatek_tpu_ninjaflexsteelgray_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_ninjaflexsteelgray_1000_175_p`|`NinjaFlex {color_name}`|`Steel Gray`|{"source_file": "ninjatek.json", "definition_index": 0, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|
|`ninjatek_tpu_ninjaflextpusteelgray_1000_175_p`|`NinjaFlex TPU {color_name}`|`Steel Gray`|{"source_file": "ninjatek.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_ninjaflexsteelgray_1000_175_p": "b7bab4",
    "ninjatek_tpu_ninjaflextpusteelgray_1000_175_p": "AFAEAB"
  }
}
```

### NT019: dup-61d06ec9e13079fc226c29662b49cdd836e93f5ef14f7a91ce261a791ee73564

Status: APPROVED; survivor `ninjatek_tpu_ninjaflexsunyellow_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_ninjaflexsunyellow_1000_175_p`|`NinjaFlex {color_name}`|`Sun Yellow`|{"source_file": "ninjatek.json", "definition_index": 0, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|
|`ninjatek_tpu_ninjaflextpusunyellow_1000_175_p`|`NinjaFlex TPU {color_name}`|`Sun Yellow`|{"source_file": "ninjatek.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_ninjaflexsunyellow_1000_175_p": "fbca18",
    "ninjatek_tpu_ninjaflextpusunyellow_1000_175_p": "FFE15B"
  }
}
```

### NT020: dup-2fc2e8971a5c3bbc5dd04e7917b16d440e5075c79bc1e31bdc99900eb02e24a5

Status: APPROVED; survivor `ninjatek_tpu_ninjaflexwatertranslucent_1000_175_p`; Rule 3.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`ninjatek_tpu_ninjaflextpuwatertranslucent_1000_175_p`|`NinjaFlex TPU {color_name}`|`Water Translucent`|{"source_file": "ninjatek.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 10, "compiled_records": 10} / False|
|`ninjatek_tpu_ninjaflexwatertranslucent_1000_175_p`|`NinjaFlex {color_name}`|`Water Translucent`|{"source_file": "ninjatek.json", "definition_index": 0, "weights": 3, "diameters": 2, "colors": 11, "compiled_records": 66} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "ninjatek_tpu_ninjaflextpuwatertranslucent_1000_175_p": "F2EFE9",
    "ninjatek_tpu_ninjaflexwatertranslucent_1000_175_p": "eaeaea"
  },
  "translucent": {
    "ninjatek_tpu_ninjaflextpuwatertranslucent_1000_175_p": false,
    "ninjatek_tpu_ninjaflexwatertranslucent_1000_175_p": true
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

- `ninjatek_tpu_ninjaflexmidnightblack_500_175_p` — NinjaFlex Midnight Black
- `ninjatek_tpu_ninjaflexsnowwhite_500_175_p` — NinjaFlex Snow White
- `ninjatek_tpu_ninjaflexsteelgray_500_175_p` — NinjaFlex Steel Gray
- `ninjatek_tpu_ninjaflexfirered_500_175_p` — NinjaFlex Fire Red
- `ninjatek_tpu_ninjaflexlavaorange_500_175_p` — NinjaFlex Lava Orange
- `ninjatek_tpu_ninjaflexsapphireblue_500_175_p` — NinjaFlex Sapphire Blue
- `ninjatek_tpu_ninjaflexgrassgreen_500_175_p` — NinjaFlex Grass Green
- `ninjatek_tpu_ninjaflexsunyellow_500_175_p` — NinjaFlex Sun Yellow
- `ninjatek_tpu_ninjaflexwatertranslucent_500_175_p` — NinjaFlex Water Translucent
- `ninjatek_tpu_ninjaflexflamingopink_500_175_p` — NinjaFlex Flamingo Pink
- `ninjatek_tpu_ninjaflexneonglow_500_175_p` — NinjaFlex Neon Glow
- `ninjatek_tpu_ninjaflexmidnightblack_500_285_p` — NinjaFlex Midnight Black
- `ninjatek_tpu_ninjaflexsnowwhite_500_285_p` — NinjaFlex Snow White
- `ninjatek_tpu_ninjaflexsteelgray_500_285_p` — NinjaFlex Steel Gray
- `ninjatek_tpu_ninjaflexfirered_500_285_p` — NinjaFlex Fire Red
- `ninjatek_tpu_ninjaflexlavaorange_500_285_p` — NinjaFlex Lava Orange
- `ninjatek_tpu_ninjaflexsapphireblue_500_285_p` — NinjaFlex Sapphire Blue
- `ninjatek_tpu_ninjaflexgrassgreen_500_285_p` — NinjaFlex Grass Green
- `ninjatek_tpu_ninjaflexsunyellow_500_285_p` — NinjaFlex Sun Yellow
- `ninjatek_tpu_ninjaflexwatertranslucent_500_285_p` — NinjaFlex Water Translucent
- `ninjatek_tpu_ninjaflexflamingopink_500_285_p` — NinjaFlex Flamingo Pink
- `ninjatek_tpu_ninjaflexneonglow_500_285_p` — NinjaFlex Neon Glow
- `ninjatek_tpu_ninjaflexneonglow_1000_175_p` — NinjaFlex Neon Glow
- `ninjatek_tpu_ninjaflexmidnightblack_1000_285_p` — NinjaFlex Midnight Black
- `ninjatek_tpu_ninjaflexsnowwhite_1000_285_p` — NinjaFlex Snow White
- `ninjatek_tpu_ninjaflexsteelgray_1000_285_p` — NinjaFlex Steel Gray
- `ninjatek_tpu_ninjaflexfirered_1000_285_p` — NinjaFlex Fire Red
- `ninjatek_tpu_ninjaflexlavaorange_1000_285_p` — NinjaFlex Lava Orange
- `ninjatek_tpu_ninjaflexsapphireblue_1000_285_p` — NinjaFlex Sapphire Blue
- `ninjatek_tpu_ninjaflexgrassgreen_1000_285_p` — NinjaFlex Grass Green
- `ninjatek_tpu_ninjaflexsunyellow_1000_285_p` — NinjaFlex Sun Yellow
- `ninjatek_tpu_ninjaflexwatertranslucent_1000_285_p` — NinjaFlex Water Translucent
- `ninjatek_tpu_ninjaflexflamingopink_1000_285_p` — NinjaFlex Flamingo Pink
- `ninjatek_tpu_ninjaflexneonglow_1000_285_p` — NinjaFlex Neon Glow
- `ninjatek_tpu_ninjaflexmidnightblack_2000_175_p` — NinjaFlex Midnight Black
- `ninjatek_tpu_ninjaflexsnowwhite_2000_175_p` — NinjaFlex Snow White
- `ninjatek_tpu_ninjaflexsteelgray_2000_175_p` — NinjaFlex Steel Gray
- `ninjatek_tpu_ninjaflexfirered_2000_175_p` — NinjaFlex Fire Red
- `ninjatek_tpu_ninjaflexlavaorange_2000_175_p` — NinjaFlex Lava Orange
- `ninjatek_tpu_ninjaflexsapphireblue_2000_175_p` — NinjaFlex Sapphire Blue
- `ninjatek_tpu_ninjaflexgrassgreen_2000_175_p` — NinjaFlex Grass Green
- `ninjatek_tpu_ninjaflexsunyellow_2000_175_p` — NinjaFlex Sun Yellow
- `ninjatek_tpu_ninjaflexwatertranslucent_2000_175_p` — NinjaFlex Water Translucent
- `ninjatek_tpu_ninjaflexflamingopink_2000_175_p` — NinjaFlex Flamingo Pink
- `ninjatek_tpu_ninjaflexneonglow_2000_175_p` — NinjaFlex Neon Glow
- `ninjatek_tpu_ninjaflexmidnightblack_2000_285_p` — NinjaFlex Midnight Black
- `ninjatek_tpu_ninjaflexsnowwhite_2000_285_p` — NinjaFlex Snow White
- `ninjatek_tpu_ninjaflexsteelgray_2000_285_p` — NinjaFlex Steel Gray
- `ninjatek_tpu_ninjaflexfirered_2000_285_p` — NinjaFlex Fire Red
- `ninjatek_tpu_ninjaflexlavaorange_2000_285_p` — NinjaFlex Lava Orange
- `ninjatek_tpu_ninjaflexsapphireblue_2000_285_p` — NinjaFlex Sapphire Blue
- `ninjatek_tpu_ninjaflexgrassgreen_2000_285_p` — NinjaFlex Grass Green
- `ninjatek_tpu_ninjaflexsunyellow_2000_285_p` — NinjaFlex Sun Yellow
- `ninjatek_tpu_ninjaflexwatertranslucent_2000_285_p` — NinjaFlex Water Translucent
- `ninjatek_tpu_ninjaflexflamingopink_2000_285_p` — NinjaFlex Flamingo Pink
- `ninjatek_tpu_ninjaflexneonglow_2000_285_p` — NinjaFlex Neon Glow
- `ninjatek_tpu_cheetahmidnightblack_500_175_p` — Cheetah Midnight Black
- `ninjatek_tpu_cheetahsnowwhite_500_175_p` — Cheetah Snow White
- `ninjatek_tpu_cheetahsteelgray_500_175_p` — Cheetah Steel Gray
- `ninjatek_tpu_cheetahfirered_500_175_p` — Cheetah Fire Red
- `ninjatek_tpu_cheetahlavaorange_500_175_p` — Cheetah Lava Orange
- `ninjatek_tpu_cheetahsapphireblue_500_175_p` — Cheetah Sapphire Blue
- `ninjatek_tpu_cheetahgrassgreen_500_175_p` — Cheetah Grass Green
- `ninjatek_tpu_cheetahsunyellow_500_175_p` — Cheetah Sun Yellow
- `ninjatek_tpu_cheetahwatertranslucent_500_175_p` — Cheetah Water Translucent
- `ninjatek_tpu_cheetahflamingopink_500_175_p` — Cheetah Flamingo Pink
- `ninjatek_tpu_cheetahneonglow_500_175_p` — Cheetah Neon Glow
- `ninjatek_tpu_cheetahmidnightblack_500_285_p` — Cheetah Midnight Black
- `ninjatek_tpu_cheetahsnowwhite_500_285_p` — Cheetah Snow White
- `ninjatek_tpu_cheetahsteelgray_500_285_p` — Cheetah Steel Gray
- `ninjatek_tpu_cheetahfirered_500_285_p` — Cheetah Fire Red
- `ninjatek_tpu_cheetahlavaorange_500_285_p` — Cheetah Lava Orange
- `ninjatek_tpu_cheetahsapphireblue_500_285_p` — Cheetah Sapphire Blue
- `ninjatek_tpu_cheetahgrassgreen_500_285_p` — Cheetah Grass Green
- `ninjatek_tpu_cheetahsunyellow_500_285_p` — Cheetah Sun Yellow
- `ninjatek_tpu_cheetahwatertranslucent_500_285_p` — Cheetah Water Translucent
- `ninjatek_tpu_cheetahflamingopink_500_285_p` — Cheetah Flamingo Pink
- `ninjatek_tpu_cheetahneonglow_500_285_p` — Cheetah Neon Glow
- `ninjatek_tpu_cheetahmidnightblack_750_175_p` — Cheetah Midnight Black
- `ninjatek_tpu_cheetahsnowwhite_750_175_p` — Cheetah Snow White
- `ninjatek_tpu_cheetahsteelgray_750_175_p` — Cheetah Steel Gray
- `ninjatek_tpu_cheetahfirered_750_175_p` — Cheetah Fire Red
- `ninjatek_tpu_cheetahlavaorange_750_175_p` — Cheetah Lava Orange
- `ninjatek_tpu_cheetahsapphireblue_750_175_p` — Cheetah Sapphire Blue
- `ninjatek_tpu_cheetahgrassgreen_750_175_p` — Cheetah Grass Green
- `ninjatek_tpu_cheetahsunyellow_750_175_p` — Cheetah Sun Yellow
- `ninjatek_tpu_cheetahwatertranslucent_750_175_p` — Cheetah Water Translucent
- `ninjatek_tpu_cheetahflamingopink_750_175_p` — Cheetah Flamingo Pink
- `ninjatek_tpu_cheetahneonglow_750_175_p` — Cheetah Neon Glow
- `ninjatek_tpu_cheetahmidnightblack_750_285_p` — Cheetah Midnight Black
- `ninjatek_tpu_cheetahsnowwhite_750_285_p` — Cheetah Snow White
- `ninjatek_tpu_cheetahsteelgray_750_285_p` — Cheetah Steel Gray
- `ninjatek_tpu_cheetahfirered_750_285_p` — Cheetah Fire Red
- `ninjatek_tpu_cheetahlavaorange_750_285_p` — Cheetah Lava Orange
- `ninjatek_tpu_cheetahsapphireblue_750_285_p` — Cheetah Sapphire Blue
- `ninjatek_tpu_cheetahgrassgreen_750_285_p` — Cheetah Grass Green
- `ninjatek_tpu_cheetahsunyellow_750_285_p` — Cheetah Sun Yellow
- `ninjatek_tpu_cheetahwatertranslucent_750_285_p` — Cheetah Water Translucent
- `ninjatek_tpu_cheetahflamingopink_750_285_p` — Cheetah Flamingo Pink
- `ninjatek_tpu_cheetahneonglow_750_285_p` — Cheetah Neon Glow
- `ninjatek_tpu_cheetahneonglow_1000_175_p` — Cheetah Neon Glow
- `ninjatek_tpu_cheetahmidnightblack_1000_285_p` — Cheetah Midnight Black
- `ninjatek_tpu_cheetahsnowwhite_1000_285_p` — Cheetah Snow White
- `ninjatek_tpu_cheetahsteelgray_1000_285_p` — Cheetah Steel Gray
- `ninjatek_tpu_cheetahfirered_1000_285_p` — Cheetah Fire Red
- `ninjatek_tpu_cheetahlavaorange_1000_285_p` — Cheetah Lava Orange
- `ninjatek_tpu_cheetahsapphireblue_1000_285_p` — Cheetah Sapphire Blue
- `ninjatek_tpu_cheetahgrassgreen_1000_285_p` — Cheetah Grass Green
- `ninjatek_tpu_cheetahsunyellow_1000_285_p` — Cheetah Sun Yellow
- `ninjatek_tpu_cheetahwatertranslucent_1000_285_p` — Cheetah Water Translucent
- `ninjatek_tpu_cheetahflamingopink_1000_285_p` — Cheetah Flamingo Pink
- `ninjatek_tpu_cheetahneonglow_1000_285_p` — Cheetah Neon Glow
- `ninjatek_tpu_armadillomidnightblack_500_175_p` — Armadillo Midnight Black
- `ninjatek_tpu_armadillosnowwhite_500_175_p` — Armadillo Snow White
- `ninjatek_tpu_armadillosteelgray_500_175_p` — Armadillo Steel Gray
- `ninjatek_tpu_armadillofirered_500_175_p` — Armadillo Fire Red
- `ninjatek_tpu_armadillolavaorange_500_175_p` — Armadillo Lava Orange
- `ninjatek_tpu_armadillosapphireblue_500_175_p` — Armadillo Sapphire Blue
- `ninjatek_tpu_armadillograssgreen_500_175_p` — Armadillo Grass Green
- `ninjatek_tpu_armadillosunyellow_500_175_p` — Armadillo Sun Yellow
- `ninjatek_tpu_armadillowatertranslucent_500_175_p` — Armadillo Water Translucent
- `ninjatek_tpu_armadillomidnightblack_500_285_p` — Armadillo Midnight Black
- `ninjatek_tpu_armadillosnowwhite_500_285_p` — Armadillo Snow White
- `ninjatek_tpu_armadillosteelgray_500_285_p` — Armadillo Steel Gray
- `ninjatek_tpu_armadillofirered_500_285_p` — Armadillo Fire Red
- `ninjatek_tpu_armadillolavaorange_500_285_p` — Armadillo Lava Orange
- `ninjatek_tpu_armadillosapphireblue_500_285_p` — Armadillo Sapphire Blue
- `ninjatek_tpu_armadillograssgreen_500_285_p` — Armadillo Grass Green
- `ninjatek_tpu_armadillosunyellow_500_285_p` — Armadillo Sun Yellow
- `ninjatek_tpu_armadillowatertranslucent_500_285_p` — Armadillo Water Translucent
- `ninjatek_tpu_armadillomidnightblack_750_175_p` — Armadillo Midnight Black
- `ninjatek_tpu_armadillosnowwhite_750_175_p` — Armadillo Snow White
- `ninjatek_tpu_armadillosteelgray_750_175_p` — Armadillo Steel Gray
- `ninjatek_tpu_armadillofirered_750_175_p` — Armadillo Fire Red
- `ninjatek_tpu_armadillolavaorange_750_175_p` — Armadillo Lava Orange
- `ninjatek_tpu_armadillosapphireblue_750_175_p` — Armadillo Sapphire Blue
- `ninjatek_tpu_armadillograssgreen_750_175_p` — Armadillo Grass Green
- `ninjatek_tpu_armadillosunyellow_750_175_p` — Armadillo Sun Yellow
- `ninjatek_tpu_armadillowatertranslucent_750_175_p` — Armadillo Water Translucent
- `ninjatek_tpu_armadillomidnightblack_750_285_p` — Armadillo Midnight Black
- `ninjatek_tpu_armadillosnowwhite_750_285_p` — Armadillo Snow White
- `ninjatek_tpu_armadillosteelgray_750_285_p` — Armadillo Steel Gray
- `ninjatek_tpu_armadillofirered_750_285_p` — Armadillo Fire Red
- `ninjatek_tpu_armadillolavaorange_750_285_p` — Armadillo Lava Orange
- `ninjatek_tpu_armadillosapphireblue_750_285_p` — Armadillo Sapphire Blue
- `ninjatek_tpu_armadillograssgreen_750_285_p` — Armadillo Grass Green
- `ninjatek_tpu_armadillosunyellow_750_285_p` — Armadillo Sun Yellow
- `ninjatek_tpu_armadillowatertranslucent_750_285_p` — Armadillo Water Translucent
- `ninjatek_tpu_chinchillatpumidnightblack_1000_175_p` — Chinchilla TPU Midnight Black
- `ninjatek_tpu_chinchillatpuskyblue_1000_175_p` — Chinchilla TPU Sky Blue
- `ninjatek_tpu_chinchillatpusnowwhite_1000_175_p` — Chinchilla TPU Snow White
- `ninjatek_tpu_chinchillatpusteelgray_1000_175_p` — Chinchilla TPU Steel Gray
- `ninjatek_tpu_edgetpumidnightblack_1000_175_p` — Edge TPU Midnight Black
- `ninjatek_tpu_edgetpusnowwhite_1000_175_p` — Edge TPU Snow White
- `ninjatek_tpu_glowtpucheetah-neonglow_1000_175_p` — Glow TPU Cheetah - Neon Glow
- `ninjatek_tpu_glowtpuninjaflex-neonglow_1000_175_p` — Glow TPU NinjaFlex - Neon Glow
- `ninjatek_tpu_tpuninjatekeel-midnightblack_1000_175_p` — TPU NinjaTek Eel - Midnight Black
