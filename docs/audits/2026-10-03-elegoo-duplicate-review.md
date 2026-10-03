# elegoo duplicate migration review

Base `8317ee58093af0347cf299ec7f02f092c1cc422e`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `af77b68f8f977afecd3206d0c8428c59cd72931431b89651b3cdae5724903ebd`.

## Authorization and result

{"groups": 86, "approved_groups": 49, "retired": 49, "deferred": 37, "hard_stops": 0, "before_count": 52498, "after_count": 52449, "brand_before": 494, "brand_after": 445, "registry_before": 936, "registry_after": 985, "metadata_fields_changed": 160, "code_transfers": 10, "new": 0, "changed_identity": 0, "rekeyed": 0}

Current manufacturer exact-line pages applied to approved matching PLA/Matte/RapidPETG/ASA survivor IDs only; no PLA defaults applied to ASA/PETG. PLA1.26→1.20; Matte1.26→1.31; ASA1.09→1.10 per current main official page (regional UK historical1.09 retained as conflict). RapidPETG density1.26 retained. Silk numerical evidence in search results was not sufficiently reverified on the live exact product page; retain survivor values and flag unresolved. Qualifier-in-color RapidPLAPlus groups are Rule5-deferred with all their existing SKU bindings intact. No packaging/tare changes; target-only transfers preserve already enrolled identifier values. Final review correction: Wood Filled is not Wood Color/ordinary PLA; use exact PLA Wood density1.21,nozzle200–240,bed35–65 with no inferred scalar. Bronze Filled and Marble keep all original survivor printing values unresolved: generic PLA table does not explicitly bind filled technical specifications. Wood Color is the current named ordinary PLA option and retains ordinary PLA evidence.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://www.elegoo.com/products/pla-filament-1-75mm-colored-1kg", "material": "PLA", "template": "{color_name}", "values": {"density": 1.2, "extruder_temp": 205, "extruder_temp_range": [190, 220], "bed_temp": null, "bed_temp_range": [50, 65]}, "verified_fragments": ["1.20g/cm", "190~220", "50-65"], "retrieved_at": "2026-10-03T16:29:52.975508+00:00", "sha256": "da4dcc20cf752d9c56a597fb7725deb956a5c8e827fc66b3870d40115bc3def5", "scope": "Exact product line current printing values, not packaging/tare"}
- {"url": "https://www.elegoo.com/products/pla-matte-filament-1-75mm-colored-1kg", "material": "PLA", "template": "Matte {color_name}", "values": {"density": 1.31, "extruder_temp": 220, "extruder_temp_range": [190, 230], "bed_temp": null, "bed_temp_range": [50, 65]}, "verified_fragments": ["1.31g/cm", "190~230", "50-65"], "retrieved_at": "2026-10-03T16:29:54.046521+00:00", "sha256": "dd046b7334f48d355a38c26d8c81551f875b340c6d2652ab2d7ef3d0beb0727d", "scope": "Exact product line current printing values, not packaging/tare"}
- {"url": "https://www.elegoo.com/products/rapid-petg-filament-1-75mm-colored-1kg", "material": "PETG", "template": "RAPID PETG {color_name}", "values": {"extruder_temp": 230, "extruder_temp_range": [220, 250], "bed_temp": null, "bed_temp_range": [75, 90]}, "verified_fragments": ["1.26g/cm", "220~250", "75-90"], "retrieved_at": "2026-10-03T16:29:55.070686+00:00", "sha256": "8cbe0625b06e10c53844e2d108ace618fcde501e617c1d9470b564a3a825cfd0", "scope": "Exact product line current printing values, not packaging/tare"}
- {"url": "https://www.elegoo.com/products/asa-filament-1-75mm-colored-1kg", "material": "ASA", "template": "{color_name}", "values": {"density": 1.1, "extruder_temp": null, "extruder_temp_range": [240, 270], "bed_temp": null, "bed_temp_range": [90, 100]}, "verified_fragments": ["1.1g/cm", "240 - 270", "90 - 100"], "retrieved_at": "2026-10-03T16:29:56.277453+00:00", "sha256": "d7a0c4bf6e270fa8e28855bc4de47d2ef2733a0719a998555dca790065f691fe", "scope": "Exact product line current printing values, not packaging/tare"}
- {"url": "https://www.elegoo.com/en-gb/collections/materials/products/pla-wood", "material": "PLA", "physical_product_line": "PLA Wood", "source_color": "Wood filled", "target_id": "elegoo_pla_woodfilled_1000_175_c", "values": {"density": 1.21, "extruder_temp": null, "extruder_temp_range": [200, 240], "bed_temp": null, "bed_temp_range": [35, 65]}, "verified_fragments": ["Visible current variant: Wood filled", "Structured specification Density = 1.21 g/cm³", "Structured Nozzle Temperature = 200 - 240 °C", "Structured Bed Temperature = 35 - 65 °C"], "retrieved_at": "2026-10-03T16:42:52.537694+00:00", "sha256": "8ab60b8168ca694e62354f78cad85cd212f424cf17d2f52cb02da046663a4130", "scope": "Exact Wood Filled option of PLA Wood line; no packaging/tare changes"}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`elegoo_asa_asablack_1000_175_c`|`elegoo_asa_black_1000_175_c`|`elegoo.json::ELEGOO::ASA {color_name}::ASA Black::ASA::1000::1.75::cardboard::False`|
|`elegoo_asa_asawhite_1000_175_c`|`elegoo_asa_white_1000_175_c`|`elegoo.json::ELEGOO::ASA {color_name}::ASA White::ASA::1000::1.75::cardboard::False`|
|`elegoo_pla_plabeige_1000_175_c`|`elegoo_pla_beige_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Beige::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plablack_1000_175_c`|`elegoo_pla_black_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Black::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plabronzefilled_1000_175_c`|`elegoo_pla_bronzefilled_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Bronze filled::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plabrown_1000_175_c`|`elegoo_pla_brown_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Brown::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_pladarkblue_1000_175_c`|`elegoo_pla_darkblue_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Dark Blue::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plagrey_1000_175_c`|`elegoo_pla_grey_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Grey::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plamarble_1000_175_c`|`elegoo_pla_marble_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Marble::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plamattebeige_1000_175_c`|`elegoo_pla_mattebeige_1000_175_c`|`elegoo.json::ELEGOO::PLA MATTE {color_name}::PLA MATTE Beige::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plamatteblack_1000_175_c`|`elegoo_pla_matteblack_1000_175_c`|`elegoo.json::ELEGOO::PLA MATTE {color_name}::PLA MATTE Black::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plamatteiceblue_1000_175_c`|`elegoo_pla_matteiceblue_1000_175_c`|`elegoo.json::ELEGOO::PLA MATTE {color_name}::PLA MATTE Ice Blue::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plamattelavenderpurple_1000_175_c`|`elegoo_pla_mattelavenderpurple_1000_175_c`|`elegoo.json::ELEGOO::PLA MATTE {color_name}::PLA MATTE Lavender Purple::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plamattemintgreen_1000_175_c`|`elegoo_pla_mattemintgreen_1000_175_c`|`elegoo.json::ELEGOO::PLA MATTE {color_name}::PLA MATTE Mint Green::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plamattenavyblue_1000_175_c`|`elegoo_pla_mattenavyblue_1000_175_c`|`elegoo.json::ELEGOO::PLA MATTE {color_name}::PLA MATTE Navy Blue::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plamatterubyred_1000_175_c`|`elegoo_pla_matterubyred_1000_175_c`|`elegoo.json::ELEGOO::PLA MATTE {color_name}::PLA MATTE Ruby Red::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plamattesakurapink_1000_175_c`|`elegoo_pla_mattesakurapink_1000_175_c`|`elegoo.json::ELEGOO::PLA MATTE {color_name}::PLA MATTE Sakura Pink::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plamatteslategrey_1000_175_c`|`elegoo_pla_matteslategrey_1000_175_c`|`elegoo.json::ELEGOO::PLA MATTE {color_name}::PLA MATTE Slate Grey::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plamattesunshineyellow_1000_175_c`|`elegoo_pla_mattesunshineyellow_1000_175_c`|`elegoo.json::ELEGOO::PLA MATTE {color_name}::PLA MATTE Sunshine Yellow::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plamattetealgreen_1000_175_c`|`elegoo_pla_mattetealgreen_1000_175_c`|`elegoo.json::ELEGOO::PLA MATTE {color_name}::PLA MATTE Teal Green::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plamattewhite_1000_175_c`|`elegoo_pla_mattewhite_1000_175_c`|`elegoo.json::ELEGOO::PLA MATTE {color_name}::PLA MATTE White::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_planeongreen_1000_175_c`|`elegoo_pla_neongreen_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Neon Green::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plaorange_1000_175_c`|`elegoo_pla_orange_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Orange::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plapink_1000_175_c`|`elegoo_pla_pink_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Pink::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plapurple_1000_175_c`|`elegoo_pla_purple_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Purple::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plared_1000_175_c`|`elegoo_pla_red_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Red::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plaseagreen_1000_175_c`|`elegoo_pla_seagreen_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Sea Green::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plaskyblue_1000_175_c`|`elegoo_pla_skyblue_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Sky Blue::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plaspacegrey_1000_175_c`|`elegoo_pla_spacegrey_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Space Grey::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_platranslucent_1000_175_c`|`elegoo_pla_translucent_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Translucent::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plawhite_1000_175_c`|`elegoo_pla_white_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA White::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plawoodcolor_1000_175_c`|`elegoo_pla_woodcolor_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Wood Color::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_plawoodfilled_1000_175_c`|`elegoo_pla_woodfilled_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Wood filled::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_playellow_1000_175_c`|`elegoo_pla_yellow_1000_175_c`|`elegoo.json::ELEGOO::PLA {color_name}::PLA Yellow::PLA::1000::1.75::cardboard::False`|
|`elegoo_pla_silkplablackpurple_1000_175_p`|`elegoo_pla_silkblackpurple_1000_175_p`|`elegoo.json::ELEGOO::Silk PLA {color_name}::Silk PLA Black Purple::PLA::1000::1.75::plastic::False`|
|`elegoo_pla_silkplablackred_1000_175_p`|`elegoo_pla_silkblackred_1000_175_p`|`elegoo.json::ELEGOO::Silk PLA {color_name}::Silk PLA Black Red::PLA::1000::1.75::plastic::False`|
|`elegoo_pla_silkplabluegreen_1000_175_p`|`elegoo_pla_silkbluegreen_1000_175_p`|`elegoo.json::ELEGOO::Silk PLA {color_name}::Silk PLA Blue Green::PLA::1000::1.75::plastic::False`|
|`elegoo_pla_silkplabluegreenorange_1000_175_p`|`elegoo_pla_silkbluegreenorange_1000_175_p`|`elegoo.json::ELEGOO::Silk PLA {color_name}::Silk PLA Blue Green Orange::PLA::1000::1.75::plastic::False`|
|`elegoo_pla_silkplabluemagenta_1000_175_p`|`elegoo_pla_silkbluemagenta_1000_175_p`|`elegoo.json::ELEGOO::Silk PLA {color_name}::Silk PLA Blue Magenta::PLA::1000::1.75::plastic::False`|
|`elegoo_pla_silkplabluepurpleblack_1000_175_p`|`elegoo_pla_silkbluepurpleblack_1000_175_p`|`elegoo.json::ELEGOO::Silk PLA {color_name}::Silk PLA Blue Purple Black::PLA::1000::1.75::plastic::False`|
|`elegoo_pla_silkplabronze_1000_175_p`|`elegoo_pla_silkbronze_1000_175_p`|`elegoo.json::ELEGOO::Silk PLA {color_name}::Silk PLA Bronze::PLA::1000::1.75::plastic::False`|
|`elegoo_pla_silkplacoralpink_1000_175_p`|`elegoo_pla_silkcoralpink_1000_175_p`|`elegoo.json::ELEGOO::Silk PLA {color_name}::Silk PLA Coral Pink::PLA::1000::1.75::plastic::False`|
|`elegoo_pla_silkplagold_1000_175_p`|`elegoo_pla_silkgold_1000_175_p`|`elegoo.json::ELEGOO::Silk PLA {color_name}::Silk PLA Gold::PLA::1000::1.75::plastic::False`|
|`elegoo_pla_silkplagreenred_1000_175_p`|`elegoo_pla_silkgreenred_1000_175_p`|`elegoo.json::ELEGOO::Silk PLA {color_name}::Silk PLA Green Red::PLA::1000::1.75::plastic::False`|
|`elegoo_pla_silkplahollygreen_1000_175_p`|`elegoo_pla_silkhollygreen_1000_175_p`|`elegoo.json::ELEGOO::Silk PLA {color_name}::Silk PLA Holly Green::PLA::1000::1.75::plastic::False`|
|`elegoo_pla_silkplamintgreen_1000_175_p`|`elegoo_pla_silkmintgreen_1000_175_p`|`elegoo.json::ELEGOO::Silk PLA {color_name}::Silk PLA Mint Green::PLA::1000::1.75::plastic::False`|
|`elegoo_pla_silkplared_1000_175_p`|`elegoo_pla_silkred_1000_175_p`|`elegoo.json::ELEGOO::Silk PLA {color_name}::Silk PLA Red::PLA::1000::1.75::plastic::False`|
|`elegoo_pla_silkplasilver_1000_175_p`|`elegoo_pla_silksilver_1000_175_p`|`elegoo.json::ELEGOO::Silk PLA {color_name}::Silk PLA Silver::PLA::1000::1.75::plastic::False`|
|`elegoo_pla_silkplawhite_1000_175_p`|`elegoo_pla_silkwhite_1000_175_p`|`elegoo.json::ELEGOO::Silk PLA {color_name}::Silk PLA White::PLA::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### EL001: dup-cb5e93ad870dfaa547d704f5dcf1d5d3e7e1215396f492ea507d2d8fc06472f9

Status: APPROVED; survivor `elegoo_asa_black_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_asa_asablack_1000_175_c`|`ASA {color_name}`|`Black`|{"source_file": "elegoo.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|
|`elegoo_asa_black_1000_175_c`|`{color_name}`|`Black`|{"source_file": "elegoo.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "elegoo_asa_asablack_1000_175_c": null,
    "elegoo_asa_black_1000_175_c": 265
  },
  "extruder_temp_range": {
    "elegoo_asa_asablack_1000_175_c": [
      235,
      260
    ],
    "elegoo_asa_black_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_asa_asablack_1000_175_c": null,
    "elegoo_asa_black_1000_175_c": 95
  },
  "bed_temp_range": {
    "elegoo_asa_asablack_1000_175_c": [
      90,
      110
    ],
    "elegoo_asa_black_1000_175_c": null
  }
}
```

### EL002: dup-7c4b6b330652bf7159e495c774ad04520fd7642200ff160c27958f0f719a52db

Status: APPROVED; survivor `elegoo_asa_white_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_asa_asawhite_1000_175_c`|`ASA {color_name}`|`White`|{"source_file": "elegoo.json", "definition_index": 10, "weights": 1, "diameters": 1, "colors": 6, "compiled_records": 6} / False|
|`elegoo_asa_white_1000_175_c`|`{color_name}`|`White`|{"source_file": "elegoo.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_asa_asawhite_1000_175_c": "FFFFFF",
    "elegoo_asa_white_1000_175_c": "ffffff"
  },
  "extruder_temp": {
    "elegoo_asa_asawhite_1000_175_c": null,
    "elegoo_asa_white_1000_175_c": 265
  },
  "extruder_temp_range": {
    "elegoo_asa_asawhite_1000_175_c": [
      235,
      260
    ],
    "elegoo_asa_white_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_asa_asawhite_1000_175_c": null,
    "elegoo_asa_white_1000_175_c": 95
  },
  "bed_temp_range": {
    "elegoo_asa_asawhite_1000_175_c": [
      90,
      110
    ],
    "elegoo_asa_white_1000_175_c": null
  }
}
```

### EL003: dup-9f178f0c086e451fc6bae2d454c9ad9b83a515efc4fc2a6948083c1ef05bc151

Status: DEFERRED; survivor `elegoo_petg_rapidpetgbeige_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_petg_petgrapidbeige_1000_175_c`|`PETG {color_name}`|`RAPID Beige`|{"source_file": "elegoo.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / False|
|`elegoo_petg_rapidpetgbeige_1000_175_c`|`RAPID PETG {color_name}`|`Beige`|{"source_file": "elegoo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_petg_petgrapidbeige_1000_175_c": 1.29,
    "elegoo_petg_rapidpetgbeige_1000_175_c": 1.26
  },
  "color_hex": {
    "elegoo_petg_petgrapidbeige_1000_175_c": "EADAC2",
    "elegoo_petg_rapidpetgbeige_1000_175_c": "EDE8D0"
  },
  "extruder_temp": {
    "elegoo_petg_petgrapidbeige_1000_175_c": null,
    "elegoo_petg_rapidpetgbeige_1000_175_c": 245
  },
  "extruder_temp_range": {
    "elegoo_petg_petgrapidbeige_1000_175_c": [
      220,
      250
    ],
    "elegoo_petg_rapidpetgbeige_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_petg_petgrapidbeige_1000_175_c": null,
    "elegoo_petg_rapidpetgbeige_1000_175_c": 80
  },
  "bed_temp_range": {
    "elegoo_petg_petgrapidbeige_1000_175_c": [
      70,
      90
    ],
    "elegoo_petg_rapidpetgbeige_1000_175_c": null
  },
  "codes": {
    "elegoo_petg_petgrapidbeige_1000_175_c": null,
    "elegoo_petg_rapidpetgbeige_1000_175_c": [
      "SPUK-EL-PTG-112"
    ]
  }
}
```

### EL004: dup-4c26830e18586b64b6850250392a2751955ed9b4df12c7b2ed5c6debae6fc59a

Status: DEFERRED; survivor `elegoo_petg_rapidpetgblack_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_petg_petgrapidblack_1000_175_c`|`PETG {color_name}`|`RAPID Black`|{"source_file": "elegoo.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / False|
|`elegoo_petg_rapidpetgblack_1000_175_c`|`RAPID PETG {color_name}`|`Black`|{"source_file": "elegoo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_petg_petgrapidblack_1000_175_c": 1.29,
    "elegoo_petg_rapidpetgblack_1000_175_c": 1.26
  },
  "extruder_temp": {
    "elegoo_petg_petgrapidblack_1000_175_c": null,
    "elegoo_petg_rapidpetgblack_1000_175_c": 245
  },
  "extruder_temp_range": {
    "elegoo_petg_petgrapidblack_1000_175_c": [
      220,
      250
    ],
    "elegoo_petg_rapidpetgblack_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_petg_petgrapidblack_1000_175_c": null,
    "elegoo_petg_rapidpetgblack_1000_175_c": 80
  },
  "bed_temp_range": {
    "elegoo_petg_petgrapidblack_1000_175_c": [
      70,
      90
    ],
    "elegoo_petg_rapidpetgblack_1000_175_c": null
  },
  "codes": {
    "elegoo_petg_petgrapidblack_1000_175_c": null,
    "elegoo_petg_rapidpetgblack_1000_175_c": [
      "SPUK-EL-PTG-101"
    ]
  }
}
```

### EL005: dup-33c23ff58ffb5ec8fefb89a77645f2fa0323f3364cc70291a1a2c68008908281

Status: DEFERRED; survivor `elegoo_petg_rapidpetgblue_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_petg_petgrapidblue_1000_175_c`|`PETG {color_name}`|`RAPID Blue`|{"source_file": "elegoo.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / False|
|`elegoo_petg_rapidpetgblue_1000_175_c`|`RAPID PETG {color_name}`|`Blue`|{"source_file": "elegoo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_petg_petgrapidblue_1000_175_c": 1.29,
    "elegoo_petg_rapidpetgblue_1000_175_c": 1.26
  },
  "color_hex": {
    "elegoo_petg_petgrapidblue_1000_175_c": "2E56F1",
    "elegoo_petg_rapidpetgblue_1000_175_c": "0000FF"
  },
  "extruder_temp": {
    "elegoo_petg_petgrapidblue_1000_175_c": null,
    "elegoo_petg_rapidpetgblue_1000_175_c": 245
  },
  "extruder_temp_range": {
    "elegoo_petg_petgrapidblue_1000_175_c": [
      220,
      250
    ],
    "elegoo_petg_rapidpetgblue_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_petg_petgrapidblue_1000_175_c": null,
    "elegoo_petg_rapidpetgblue_1000_175_c": 80
  },
  "bed_temp_range": {
    "elegoo_petg_petgrapidblue_1000_175_c": [
      70,
      90
    ],
    "elegoo_petg_rapidpetgblue_1000_175_c": null
  },
  "codes": {
    "elegoo_petg_petgrapidblue_1000_175_c": null,
    "elegoo_petg_rapidpetgblue_1000_175_c": [
      "SPUK-EL-PTG-104"
    ]
  }
}
```

### EL006: dup-c8f7b6fcb1218e8e9ecf341e538bdf4e5038e1940af9add64d9295fe4c1dd6f6

Status: DEFERRED; survivor `elegoo_petg_rapidpetgbrown_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_petg_petgrapidbrown_1000_175_c`|`PETG {color_name}`|`RAPID Brown`|{"source_file": "elegoo.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / False|
|`elegoo_petg_rapidpetgbrown_1000_175_c`|`RAPID PETG {color_name}`|`Brown`|{"source_file": "elegoo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_petg_petgrapidbrown_1000_175_c": 1.29,
    "elegoo_petg_rapidpetgbrown_1000_175_c": 1.26
  },
  "color_hex": {
    "elegoo_petg_petgrapidbrown_1000_175_c": "9F563E",
    "elegoo_petg_rapidpetgbrown_1000_175_c": "743824"
  },
  "extruder_temp": {
    "elegoo_petg_petgrapidbrown_1000_175_c": null,
    "elegoo_petg_rapidpetgbrown_1000_175_c": 245
  },
  "extruder_temp_range": {
    "elegoo_petg_petgrapidbrown_1000_175_c": [
      220,
      250
    ],
    "elegoo_petg_rapidpetgbrown_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_petg_petgrapidbrown_1000_175_c": null,
    "elegoo_petg_rapidpetgbrown_1000_175_c": 80
  },
  "bed_temp_range": {
    "elegoo_petg_petgrapidbrown_1000_175_c": [
      70,
      90
    ],
    "elegoo_petg_rapidpetgbrown_1000_175_c": null
  },
  "codes": {
    "elegoo_petg_petgrapidbrown_1000_175_c": null,
    "elegoo_petg_rapidpetgbrown_1000_175_c": [
      "SPUK-EL-PTG-110"
    ]
  }
}
```

### EL007: dup-3f7587aef6db249a96963f5d778c0001981d5069ebb95621f1d4fa93f6e0277d

Status: DEFERRED; survivor `elegoo_petg_rapidpetggreen_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_petg_petgrapidgreen_1000_175_c`|`PETG {color_name}`|`RAPID Green`|{"source_file": "elegoo.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / False|
|`elegoo_petg_rapidpetggreen_1000_175_c`|`RAPID PETG {color_name}`|`Green`|{"source_file": "elegoo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_petg_petgrapidgreen_1000_175_c": 1.29,
    "elegoo_petg_rapidpetggreen_1000_175_c": 1.26
  },
  "color_hex": {
    "elegoo_petg_petgrapidgreen_1000_175_c": "26A648",
    "elegoo_petg_rapidpetggreen_1000_175_c": "2B9A84"
  },
  "extruder_temp": {
    "elegoo_petg_petgrapidgreen_1000_175_c": null,
    "elegoo_petg_rapidpetggreen_1000_175_c": 245
  },
  "extruder_temp_range": {
    "elegoo_petg_petgrapidgreen_1000_175_c": [
      220,
      250
    ],
    "elegoo_petg_rapidpetggreen_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_petg_petgrapidgreen_1000_175_c": null,
    "elegoo_petg_rapidpetggreen_1000_175_c": 80
  },
  "bed_temp_range": {
    "elegoo_petg_petgrapidgreen_1000_175_c": [
      70,
      90
    ],
    "elegoo_petg_rapidpetggreen_1000_175_c": null
  },
  "codes": {
    "elegoo_petg_petgrapidgreen_1000_175_c": null,
    "elegoo_petg_rapidpetggreen_1000_175_c": [
      "SPUK-EL-PTG-105"
    ]
  }
}
```

### EL008: dup-11ab096208f05b11e8ed3e484437cc82be986a6c94d971f36c149a4421bd9944

Status: DEFERRED; survivor `elegoo_petg_rapidpetggrey_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_petg_petgrapidgrey_1000_175_c`|`PETG {color_name}`|`RAPID Grey`|{"source_file": "elegoo.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / False|
|`elegoo_petg_rapidpetggrey_1000_175_c`|`RAPID PETG {color_name}`|`Grey`|{"source_file": "elegoo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_petg_petgrapidgrey_1000_175_c": 1.29,
    "elegoo_petg_rapidpetggrey_1000_175_c": 1.26
  },
  "color_hex": {
    "elegoo_petg_petgrapidgrey_1000_175_c": "C5C5BF",
    "elegoo_petg_rapidpetggrey_1000_175_c": "828282"
  },
  "extruder_temp": {
    "elegoo_petg_petgrapidgrey_1000_175_c": null,
    "elegoo_petg_rapidpetggrey_1000_175_c": 245
  },
  "extruder_temp_range": {
    "elegoo_petg_petgrapidgrey_1000_175_c": [
      220,
      250
    ],
    "elegoo_petg_rapidpetggrey_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_petg_petgrapidgrey_1000_175_c": null,
    "elegoo_petg_rapidpetggrey_1000_175_c": 80
  },
  "bed_temp_range": {
    "elegoo_petg_petgrapidgrey_1000_175_c": [
      70,
      90
    ],
    "elegoo_petg_rapidpetggrey_1000_175_c": null
  },
  "codes": {
    "elegoo_petg_petgrapidgrey_1000_175_c": null,
    "elegoo_petg_rapidpetggrey_1000_175_c": [
      "SPUK-EL-PTG-107"
    ]
  }
}
```

### EL009: dup-a904e4ab648d9a40cfc746469b1f15e94f3f6d41b3c962545afc1ab28552b2a1

Status: DEFERRED; survivor `elegoo_petg_rapidpetgorange_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_petg_petgrapidorange_1000_175_c`|`PETG {color_name}`|`RAPID Orange`|{"source_file": "elegoo.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / False|
|`elegoo_petg_rapidpetgorange_1000_175_c`|`RAPID PETG {color_name}`|`Orange`|{"source_file": "elegoo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_petg_petgrapidorange_1000_175_c": 1.29,
    "elegoo_petg_rapidpetgorange_1000_175_c": 1.26
  },
  "color_hex": {
    "elegoo_petg_petgrapidorange_1000_175_c": "FF8E24",
    "elegoo_petg_rapidpetgorange_1000_175_c": "D0864C"
  },
  "extruder_temp": {
    "elegoo_petg_petgrapidorange_1000_175_c": null,
    "elegoo_petg_rapidpetgorange_1000_175_c": 245
  },
  "extruder_temp_range": {
    "elegoo_petg_petgrapidorange_1000_175_c": [
      220,
      250
    ],
    "elegoo_petg_rapidpetgorange_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_petg_petgrapidorange_1000_175_c": null,
    "elegoo_petg_rapidpetgorange_1000_175_c": 80
  },
  "bed_temp_range": {
    "elegoo_petg_petgrapidorange_1000_175_c": [
      70,
      90
    ],
    "elegoo_petg_rapidpetgorange_1000_175_c": null
  },
  "codes": {
    "elegoo_petg_petgrapidorange_1000_175_c": null,
    "elegoo_petg_rapidpetgorange_1000_175_c": [
      "SPUK-EL-PTG-108"
    ]
  }
}
```

### EL010: dup-ca605f92aa4123261cdc49dc5d046b827c25f5452691745f3bf4924f97dfc42f

Status: DEFERRED; survivor `elegoo_petg_rapidpetgred_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_petg_petgrapidred_1000_175_c`|`PETG {color_name}`|`RAPID Red`|{"source_file": "elegoo.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / False|
|`elegoo_petg_rapidpetgred_1000_175_c`|`RAPID PETG {color_name}`|`Red`|{"source_file": "elegoo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_petg_petgrapidred_1000_175_c": 1.29,
    "elegoo_petg_rapidpetgred_1000_175_c": 1.26
  },
  "color_hex": {
    "elegoo_petg_petgrapidred_1000_175_c": "E72F1D",
    "elegoo_petg_rapidpetgred_1000_175_c": "FF0000"
  },
  "extruder_temp": {
    "elegoo_petg_petgrapidred_1000_175_c": null,
    "elegoo_petg_rapidpetgred_1000_175_c": 245
  },
  "extruder_temp_range": {
    "elegoo_petg_petgrapidred_1000_175_c": [
      220,
      250
    ],
    "elegoo_petg_rapidpetgred_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_petg_petgrapidred_1000_175_c": null,
    "elegoo_petg_rapidpetgred_1000_175_c": 80
  },
  "bed_temp_range": {
    "elegoo_petg_petgrapidred_1000_175_c": [
      70,
      90
    ],
    "elegoo_petg_rapidpetgred_1000_175_c": null
  },
  "codes": {
    "elegoo_petg_petgrapidred_1000_175_c": null,
    "elegoo_petg_rapidpetgred_1000_175_c": [
      "SPUK-EL-PTG-103"
    ]
  }
}
```

### EL011: dup-bb4974d0f1e9735e3c28f2abb5b9d829e390de447d8111c96b8b9476b5eb556b

Status: DEFERRED; survivor `elegoo_petg_rapidpetgspacegrey_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_petg_petgrapidspacegrey_1000_175_c`|`PETG {color_name}`|`RAPID Space Grey`|{"source_file": "elegoo.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / False|
|`elegoo_petg_rapidpetgspacegrey_1000_175_c`|`RAPID PETG {color_name}`|`Space Grey`|{"source_file": "elegoo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_petg_petgrapidspacegrey_1000_175_c": 1.29,
    "elegoo_petg_rapidpetgspacegrey_1000_175_c": 1.26
  },
  "color_hex": {
    "elegoo_petg_petgrapidspacegrey_1000_175_c": "6A6C6E",
    "elegoo_petg_rapidpetgspacegrey_1000_175_c": "7E7E7E"
  },
  "extruder_temp": {
    "elegoo_petg_petgrapidspacegrey_1000_175_c": null,
    "elegoo_petg_rapidpetgspacegrey_1000_175_c": 245
  },
  "extruder_temp_range": {
    "elegoo_petg_petgrapidspacegrey_1000_175_c": [
      220,
      250
    ],
    "elegoo_petg_rapidpetgspacegrey_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_petg_petgrapidspacegrey_1000_175_c": null,
    "elegoo_petg_rapidpetgspacegrey_1000_175_c": 80
  },
  "bed_temp_range": {
    "elegoo_petg_petgrapidspacegrey_1000_175_c": [
      70,
      90
    ],
    "elegoo_petg_rapidpetgspacegrey_1000_175_c": null
  },
  "codes": {
    "elegoo_petg_petgrapidspacegrey_1000_175_c": null,
    "elegoo_petg_rapidpetgspacegrey_1000_175_c": [
      "SPUK-EL-PTG-113"
    ]
  }
}
```

### EL012: dup-02c7f12b96545080f13ef8a3c73f9edc3a897c00538a5324ede37c2a3138b63c

Status: DEFERRED; survivor `elegoo_petg_rapidpetgtransparent_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_petg_petgrapidtransparent_1000_175_c`|`PETG {color_name}`|`RAPID Transparent`|{"source_file": "elegoo.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / False|
|`elegoo_petg_rapidpetgtransparent_1000_175_c`|`RAPID PETG {color_name}`|`Transparent`|{"source_file": "elegoo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_petg_petgrapidtransparent_1000_175_c": 1.29,
    "elegoo_petg_rapidpetgtransparent_1000_175_c": 1.26
  },
  "color_hex": {
    "elegoo_petg_petgrapidtransparent_1000_175_c": "E4E7E5",
    "elegoo_petg_rapidpetgtransparent_1000_175_c": "00FFFFFF"
  },
  "extruder_temp": {
    "elegoo_petg_petgrapidtransparent_1000_175_c": null,
    "elegoo_petg_rapidpetgtransparent_1000_175_c": 245
  },
  "extruder_temp_range": {
    "elegoo_petg_petgrapidtransparent_1000_175_c": [
      220,
      250
    ],
    "elegoo_petg_rapidpetgtransparent_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_petg_petgrapidtransparent_1000_175_c": null,
    "elegoo_petg_rapidpetgtransparent_1000_175_c": 80
  },
  "bed_temp_range": {
    "elegoo_petg_petgrapidtransparent_1000_175_c": [
      70,
      90
    ],
    "elegoo_petg_rapidpetgtransparent_1000_175_c": null
  },
  "codes": {
    "elegoo_petg_petgrapidtransparent_1000_175_c": null,
    "elegoo_petg_rapidpetgtransparent_1000_175_c": [
      "SPUK-EL-PTG-111"
    ]
  }
}
```

### EL013: dup-a7a4ebded53278f36902617e33dc2c1a6d07cad3f44d2c2cb901b2401dbd23ac

Status: DEFERRED; survivor `elegoo_petg_rapidpetgwhite_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_petg_petgrapidwhite_1000_175_c`|`PETG {color_name}`|`RAPID White`|{"source_file": "elegoo.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / False|
|`elegoo_petg_rapidpetgwhite_1000_175_c`|`RAPID PETG {color_name}`|`White`|{"source_file": "elegoo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_petg_petgrapidwhite_1000_175_c": 1.29,
    "elegoo_petg_rapidpetgwhite_1000_175_c": 1.26
  },
  "extruder_temp": {
    "elegoo_petg_petgrapidwhite_1000_175_c": null,
    "elegoo_petg_rapidpetgwhite_1000_175_c": 245
  },
  "extruder_temp_range": {
    "elegoo_petg_petgrapidwhite_1000_175_c": [
      220,
      250
    ],
    "elegoo_petg_rapidpetgwhite_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_petg_petgrapidwhite_1000_175_c": null,
    "elegoo_petg_rapidpetgwhite_1000_175_c": 80
  },
  "bed_temp_range": {
    "elegoo_petg_petgrapidwhite_1000_175_c": [
      70,
      90
    ],
    "elegoo_petg_rapidpetgwhite_1000_175_c": null
  },
  "codes": {
    "elegoo_petg_petgrapidwhite_1000_175_c": null,
    "elegoo_petg_rapidpetgwhite_1000_175_c": [
      "SPUK-EL-PTG-102"
    ]
  }
}
```

### EL014: dup-a64a238e12beb1950c65eab98c0eab60c578f02b3a4c01720e5c148dce3a06a1

Status: DEFERRED; survivor `elegoo_petg_rapidpetgyellow_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_petg_petgrapidyellow_1000_175_c`|`PETG {color_name}`|`RAPID Yellow`|{"source_file": "elegoo.json", "definition_index": 13, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / False|
|`elegoo_petg_rapidpetgyellow_1000_175_c`|`RAPID PETG {color_name}`|`Yellow`|{"source_file": "elegoo.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 13, "compiled_records": 13} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_petg_petgrapidyellow_1000_175_c": 1.29,
    "elegoo_petg_rapidpetgyellow_1000_175_c": 1.26
  },
  "color_hex": {
    "elegoo_petg_petgrapidyellow_1000_175_c": "FBE200",
    "elegoo_petg_rapidpetgyellow_1000_175_c": "DBFF80"
  },
  "extruder_temp": {
    "elegoo_petg_petgrapidyellow_1000_175_c": null,
    "elegoo_petg_rapidpetgyellow_1000_175_c": 245
  },
  "extruder_temp_range": {
    "elegoo_petg_petgrapidyellow_1000_175_c": [
      220,
      250
    ],
    "elegoo_petg_rapidpetgyellow_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_petg_petgrapidyellow_1000_175_c": null,
    "elegoo_petg_rapidpetgyellow_1000_175_c": 80
  },
  "bed_temp_range": {
    "elegoo_petg_petgrapidyellow_1000_175_c": [
      70,
      90
    ],
    "elegoo_petg_rapidpetgyellow_1000_175_c": null
  },
  "codes": {
    "elegoo_petg_petgrapidyellow_1000_175_c": null,
    "elegoo_petg_rapidpetgyellow_1000_175_c": [
      "SPUK-EL-PTG-106"
    ]
  }
}
```

### EL015: dup-9305cff398168af4ebfb5e793b365540bc3249196257212c5f2eca7bd71153cf

Status: APPROVED; survivor `elegoo_pla_beige_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_beige_1000_175_c`|`{color_name}`|`Beige`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`elegoo_pla_plabeige_1000_175_c`|`PLA {color_name}`|`Beige`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_pla_beige_1000_175_c": "fee7bf",
    "elegoo_pla_plabeige_1000_175_c": "F4E0B8"
  },
  "extruder_temp": {
    "elegoo_pla_beige_1000_175_c": 210,
    "elegoo_pla_plabeige_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_beige_1000_175_c": null,
    "elegoo_pla_plabeige_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_beige_1000_175_c": 60,
    "elegoo_pla_plabeige_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_beige_1000_175_c": null,
    "elegoo_pla_plabeige_1000_175_c": [
      50,
      70
    ]
  }
}
```

### EL016: dup-c7629404d97bb25a7e110a87e61a1294e46233d661e5db87ad70b16cf0e37a23

Status: APPROVED; survivor `elegoo_pla_black_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_black_1000_175_c`|`{color_name}`|`Black`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`elegoo_pla_plablack_1000_175_c`|`PLA {color_name}`|`Black`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "elegoo_pla_black_1000_175_c": 210,
    "elegoo_pla_plablack_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_black_1000_175_c": null,
    "elegoo_pla_plablack_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_black_1000_175_c": 60,
    "elegoo_pla_plablack_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_black_1000_175_c": null,
    "elegoo_pla_plablack_1000_175_c": [
      50,
      70
    ]
  }
}
```

### EL017: dup-26674680ac47d32621be8fc9617f2be1bec8260257d47fc919e3582914408628

Status: APPROVED; survivor `elegoo_pla_bronzefilled_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_bronzefilled_1000_175_c`|`{color_name}`|`Bronze Filled`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`elegoo_pla_plabronzefilled_1000_175_c`|`PLA {color_name}`|`Bronze filled`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "extruder_temp": {
    "elegoo_pla_bronzefilled_1000_175_c": 210,
    "elegoo_pla_plabronzefilled_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_bronzefilled_1000_175_c": null,
    "elegoo_pla_plabronzefilled_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_bronzefilled_1000_175_c": 60,
    "elegoo_pla_plabronzefilled_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_bronzefilled_1000_175_c": null,
    "elegoo_pla_plabronzefilled_1000_175_c": [
      50,
      70
    ]
  }
}
```

### EL018: dup-ce0bca03e4ace01b4346a2d8bdc47ea6b32c490ff2911d88c4e0fdcb71c511c8

Status: APPROVED; survivor `elegoo_pla_brown_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_brown_1000_175_c`|`{color_name}`|`Brown`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`elegoo_pla_plabrown_1000_175_c`|`PLA {color_name}`|`Brown`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_pla_brown_1000_175_c": "9e6a4b",
    "elegoo_pla_plabrown_1000_175_c": "9E6A4B"
  },
  "extruder_temp": {
    "elegoo_pla_brown_1000_175_c": 210,
    "elegoo_pla_plabrown_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_brown_1000_175_c": null,
    "elegoo_pla_plabrown_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_brown_1000_175_c": 60,
    "elegoo_pla_plabrown_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_brown_1000_175_c": null,
    "elegoo_pla_plabrown_1000_175_c": [
      50,
      70
    ]
  }
}
```

### EL019: dup-426ab70f7426ed641827734fe33cc024524f9bbac577461125ddf8b933b2004b

Status: APPROVED; survivor `elegoo_pla_darkblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_darkblue_1000_175_c`|`{color_name}`|`Dark Blue`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`elegoo_pla_pladarkblue_1000_175_c`|`PLA {color_name}`|`Dark Blue`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_pla_darkblue_1000_175_c": "2240af",
    "elegoo_pla_pladarkblue_1000_175_c": "2240AF"
  },
  "extruder_temp": {
    "elegoo_pla_darkblue_1000_175_c": 210,
    "elegoo_pla_pladarkblue_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_darkblue_1000_175_c": null,
    "elegoo_pla_pladarkblue_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_darkblue_1000_175_c": 60,
    "elegoo_pla_pladarkblue_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_darkblue_1000_175_c": null,
    "elegoo_pla_pladarkblue_1000_175_c": [
      50,
      70
    ]
  }
}
```

### EL020: dup-9e48e48b81f51d542902f2607c884b96e240637f24f0f2e57c4e03ecb4a18117

Status: DEFERRED; survivor `elegoo_pla_plagalaxyblack_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_galaxyplablack_1000_175_c`|`Galaxy PLA {color_name}`|`Black`|{"source_file": "elegoo.json", "definition_index": 16, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / False|
|`elegoo_pla_plagalaxyblack_1000_175_c`|`PLA {color_name}`|`Galaxy Black`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_galaxyplablack_1000_175_c": 1.21,
    "elegoo_pla_plagalaxyblack_1000_175_c": 1.26
  },
  "color_hex": {
    "elegoo_pla_galaxyplablack_1000_175_c": "0D162C",
    "elegoo_pla_plagalaxyblack_1000_175_c": "000000"
  },
  "extruder_temp": {
    "elegoo_pla_galaxyplablack_1000_175_c": 205,
    "elegoo_pla_plagalaxyblack_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_galaxyplablack_1000_175_c": null,
    "elegoo_pla_plagalaxyblack_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_galaxyplablack_1000_175_c": 60,
    "elegoo_pla_plagalaxyblack_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_galaxyplablack_1000_175_c": null,
    "elegoo_pla_plagalaxyblack_1000_175_c": [
      50,
      70
    ]
  },
  "codes": {
    "elegoo_pla_galaxyplablack_1000_175_c": [
      "EL-PLA-108"
    ],
    "elegoo_pla_plagalaxyblack_1000_175_c": null
  }
}
```

### EL021: dup-2b6bc1cbdf95c53d6dc6ac63726db47a651d5b15c0d48c8ae9a276a90908ba92

Status: DEFERRED; survivor `elegoo_pla_plagalaxypeacockblue_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_galaxyplapeacockblue_1000_175_c`|`Galaxy PLA {color_name}`|`Peacock Blue`|{"source_file": "elegoo.json", "definition_index": 16, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / False|
|`elegoo_pla_plagalaxypeacockblue_1000_175_c`|`PLA {color_name}`|`Galaxy Peacock Blue`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_galaxyplapeacockblue_1000_175_c": 1.21,
    "elegoo_pla_plagalaxypeacockblue_1000_175_c": 1.26
  },
  "color_hex": {
    "elegoo_pla_galaxyplapeacockblue_1000_175_c": "1C506D",
    "elegoo_pla_plagalaxypeacockblue_1000_175_c": "375680"
  },
  "extruder_temp": {
    "elegoo_pla_galaxyplapeacockblue_1000_175_c": 205,
    "elegoo_pla_plagalaxypeacockblue_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_galaxyplapeacockblue_1000_175_c": null,
    "elegoo_pla_plagalaxypeacockblue_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_galaxyplapeacockblue_1000_175_c": 60,
    "elegoo_pla_plagalaxypeacockblue_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_galaxyplapeacockblue_1000_175_c": null,
    "elegoo_pla_plagalaxypeacockblue_1000_175_c": [
      50,
      70
    ]
  }
}
```

### EL022: dup-dc916bc3d2ee0fc732d00eb781f32cee9ef327790088f0820574330166e371e3

Status: DEFERRED; survivor `elegoo_pla_plagalaxypurple_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_galaxyplapurple_1000_175_c`|`Galaxy PLA {color_name}`|`Purple`|{"source_file": "elegoo.json", "definition_index": 16, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / False|
|`elegoo_pla_plagalaxypurple_1000_175_c`|`PLA {color_name}`|`Galaxy Purple`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_galaxyplapurple_1000_175_c": 1.21,
    "elegoo_pla_plagalaxypurple_1000_175_c": 1.26
  },
  "color_hex": {
    "elegoo_pla_galaxyplapurple_1000_175_c": "34276E",
    "elegoo_pla_plagalaxypurple_1000_175_c": "3A0A8C"
  },
  "extruder_temp": {
    "elegoo_pla_galaxyplapurple_1000_175_c": 205,
    "elegoo_pla_plagalaxypurple_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_galaxyplapurple_1000_175_c": null,
    "elegoo_pla_plagalaxypurple_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_galaxyplapurple_1000_175_c": 60,
    "elegoo_pla_plagalaxypurple_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_galaxyplapurple_1000_175_c": null,
    "elegoo_pla_plagalaxypurple_1000_175_c": [
      50,
      70
    ]
  }
}
```

### EL023: dup-66a02e399cc0e123a2d16ab3ebf0a54b03ea6b591395f632dcbed7d096cca414

Status: APPROVED; survivor `elegoo_pla_grey_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_grey_1000_175_c`|`{color_name}`|`Grey`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`elegoo_pla_plagrey_1000_175_c`|`PLA {color_name}`|`Grey`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_pla_grey_1000_175_c": "8f949b",
    "elegoo_pla_plagrey_1000_175_c": "8F949B"
  },
  "extruder_temp": {
    "elegoo_pla_grey_1000_175_c": 210,
    "elegoo_pla_plagrey_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_grey_1000_175_c": null,
    "elegoo_pla_plagrey_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_grey_1000_175_c": 60,
    "elegoo_pla_plagrey_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_grey_1000_175_c": null,
    "elegoo_pla_plagrey_1000_175_c": [
      50,
      70
    ]
  }
}
```

### EL024: dup-ccdfba9ac818ff688c30dd1f05f941953ba1b9ed3f97e1aa378fbb4f2246eb0e

Status: APPROVED; survivor `elegoo_pla_marble_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_marble_1000_175_c`|`{color_name}`|`Marble`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`elegoo_pla_plamarble_1000_175_c`|`PLA {color_name}`|`Marble`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_pla_marble_1000_175_c": "B1B6B6",
    "elegoo_pla_plamarble_1000_175_c": "ACB1B1"
  },
  "extruder_temp": {
    "elegoo_pla_marble_1000_175_c": 210,
    "elegoo_pla_plamarble_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_marble_1000_175_c": null,
    "elegoo_pla_plamarble_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_marble_1000_175_c": 60,
    "elegoo_pla_plamarble_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_marble_1000_175_c": null,
    "elegoo_pla_plamarble_1000_175_c": [
      50,
      70
    ]
  }
}
```

### EL025: dup-b67b8b23c2f63828bd67e91b5f646dfffff62890a64a6076f5b5a6db2a0d56de

Status: APPROVED; survivor `elegoo_pla_mattebeige_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_mattebeige_1000_175_c`|`Matte {color_name}`|`Beige`|{"source_file": "elegoo.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|
|`elegoo_pla_plamattebeige_1000_175_c`|`PLA MATTE {color_name}`|`Beige`|{"source_file": "elegoo.json", "definition_index": 20, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_mattebeige_1000_175_c": 1.26,
    "elegoo_pla_plamattebeige_1000_175_c": 1.31
  },
  "color_hex": {
    "elegoo_pla_mattebeige_1000_175_c": "f4e0b8",
    "elegoo_pla_plamattebeige_1000_175_c": "F4E0B8"
  },
  "extruder_temp": {
    "elegoo_pla_mattebeige_1000_175_c": 210,
    "elegoo_pla_plamattebeige_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_mattebeige_1000_175_c": null,
    "elegoo_pla_plamattebeige_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_mattebeige_1000_175_c": 60,
    "elegoo_pla_plamattebeige_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_mattebeige_1000_175_c": null,
    "elegoo_pla_plamattebeige_1000_175_c": [
      50,
      70
    ]
  },
  "codes": {
    "elegoo_pla_mattebeige_1000_175_c": null,
    "elegoo_pla_plamattebeige_1000_175_c": [
      "SPUK-EL-MAT-111"
    ]
  }
}
```

### EL026: dup-ec839f9f555da955683e7e0c40f6fd6bf9443874327dc7e0c4606685da5c2c07

Status: APPROVED; survivor `elegoo_pla_matteblack_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_matteblack_1000_175_c`|`Matte {color_name}`|`Black`|{"source_file": "elegoo.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|
|`elegoo_pla_plamatteblack_1000_175_c`|`PLA MATTE {color_name}`|`Black`|{"source_file": "elegoo.json", "definition_index": 20, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_matteblack_1000_175_c": 1.26,
    "elegoo_pla_plamatteblack_1000_175_c": 1.31
  },
  "color_hex": {
    "elegoo_pla_matteblack_1000_175_c": "090909",
    "elegoo_pla_plamatteblack_1000_175_c": "000000"
  },
  "extruder_temp": {
    "elegoo_pla_matteblack_1000_175_c": 210,
    "elegoo_pla_plamatteblack_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_matteblack_1000_175_c": null,
    "elegoo_pla_plamatteblack_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_matteblack_1000_175_c": 60,
    "elegoo_pla_plamatteblack_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_matteblack_1000_175_c": null,
    "elegoo_pla_plamatteblack_1000_175_c": [
      50,
      70
    ]
  }
}
```

### EL027: dup-ae1c1c4652f4fe663c3cccc3ae140c0144d3c7860f9fc1baea78d199fd895c67

Status: APPROVED; survivor `elegoo_pla_matteiceblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_matteiceblue_1000_175_c`|`Matte {color_name}`|`Ice Blue`|{"source_file": "elegoo.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|
|`elegoo_pla_plamatteiceblue_1000_175_c`|`PLA MATTE {color_name}`|`Ice Blue`|{"source_file": "elegoo.json", "definition_index": 20, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_matteiceblue_1000_175_c": 1.26,
    "elegoo_pla_plamatteiceblue_1000_175_c": 1.31
  },
  "color_hex": {
    "elegoo_pla_matteiceblue_1000_175_c": "b3f3fd",
    "elegoo_pla_plamatteiceblue_1000_175_c": "B3F3FD"
  },
  "extruder_temp": {
    "elegoo_pla_matteiceblue_1000_175_c": 210,
    "elegoo_pla_plamatteiceblue_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_matteiceblue_1000_175_c": null,
    "elegoo_pla_plamatteiceblue_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_matteiceblue_1000_175_c": 60,
    "elegoo_pla_plamatteiceblue_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_matteiceblue_1000_175_c": null,
    "elegoo_pla_plamatteiceblue_1000_175_c": [
      50,
      70
    ]
  },
  "codes": {
    "elegoo_pla_matteiceblue_1000_175_c": null,
    "elegoo_pla_plamatteiceblue_1000_175_c": [
      "SPUK-EL-MAT-110"
    ]
  }
}
```

### EL028: dup-5d25c9ac62338f47cd8deabe5d2372aee34c5c258e197b515752d1cde913c025

Status: APPROVED; survivor `elegoo_pla_mattelavenderpurple_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_mattelavenderpurple_1000_175_c`|`Matte {color_name}`|`Lavender Purple`|{"source_file": "elegoo.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|
|`elegoo_pla_plamattelavenderpurple_1000_175_c`|`PLA MATTE {color_name}`|`Lavender Purple`|{"source_file": "elegoo.json", "definition_index": 20, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_mattelavenderpurple_1000_175_c": 1.26,
    "elegoo_pla_plamattelavenderpurple_1000_175_c": 1.31
  },
  "color_hex": {
    "elegoo_pla_mattelavenderpurple_1000_175_c": "9d85d1",
    "elegoo_pla_plamattelavenderpurple_1000_175_c": "9D85D1"
  },
  "extruder_temp": {
    "elegoo_pla_mattelavenderpurple_1000_175_c": 210,
    "elegoo_pla_plamattelavenderpurple_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_mattelavenderpurple_1000_175_c": null,
    "elegoo_pla_plamattelavenderpurple_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_mattelavenderpurple_1000_175_c": 60,
    "elegoo_pla_plamattelavenderpurple_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_mattelavenderpurple_1000_175_c": null,
    "elegoo_pla_plamattelavenderpurple_1000_175_c": [
      50,
      70
    ]
  },
  "codes": {
    "elegoo_pla_mattelavenderpurple_1000_175_c": null,
    "elegoo_pla_plamattelavenderpurple_1000_175_c": [
      "SPUK-EL-MAT-108"
    ]
  }
}
```

### EL029: dup-d70ce04bc2e91ec7bd94b497b3d89f608e91bc27dfd70cb6134440745813e117

Status: APPROVED; survivor `elegoo_pla_mattemintgreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_mattemintgreen_1000_175_c`|`Matte {color_name}`|`Mint Green`|{"source_file": "elegoo.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|
|`elegoo_pla_plamattemintgreen_1000_175_c`|`PLA MATTE {color_name}`|`Mint Green`|{"source_file": "elegoo.json", "definition_index": 20, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_mattemintgreen_1000_175_c": 1.26,
    "elegoo_pla_plamattemintgreen_1000_175_c": 1.31
  },
  "color_hex": {
    "elegoo_pla_mattemintgreen_1000_175_c": "dbebba",
    "elegoo_pla_plamattemintgreen_1000_175_c": "DBEBBA"
  },
  "extruder_temp": {
    "elegoo_pla_mattemintgreen_1000_175_c": 210,
    "elegoo_pla_plamattemintgreen_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_mattemintgreen_1000_175_c": null,
    "elegoo_pla_plamattemintgreen_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_mattemintgreen_1000_175_c": 60,
    "elegoo_pla_plamattemintgreen_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_mattemintgreen_1000_175_c": null,
    "elegoo_pla_plamattemintgreen_1000_175_c": [
      50,
      70
    ]
  },
  "codes": {
    "elegoo_pla_mattemintgreen_1000_175_c": null,
    "elegoo_pla_plamattemintgreen_1000_175_c": [
      "SPUK-EL-MAT-112"
    ]
  }
}
```

### EL030: dup-59349c918c6a4d4b3a2896d94952d4ba0766d258cdd39ad68c89b613af15801c

Status: APPROVED; survivor `elegoo_pla_mattenavyblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_mattenavyblue_1000_175_c`|`Matte {color_name}`|`Navy Blue`|{"source_file": "elegoo.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|
|`elegoo_pla_plamattenavyblue_1000_175_c`|`PLA MATTE {color_name}`|`Navy Blue`|{"source_file": "elegoo.json", "definition_index": 20, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_mattenavyblue_1000_175_c": 1.26,
    "elegoo_pla_plamattenavyblue_1000_175_c": 1.31
  },
  "color_hex": {
    "elegoo_pla_mattenavyblue_1000_175_c": "2d3f6f",
    "elegoo_pla_plamattenavyblue_1000_175_c": "2D3F6F"
  },
  "extruder_temp": {
    "elegoo_pla_mattenavyblue_1000_175_c": 210,
    "elegoo_pla_plamattenavyblue_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_mattenavyblue_1000_175_c": null,
    "elegoo_pla_plamattenavyblue_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_mattenavyblue_1000_175_c": 60,
    "elegoo_pla_plamattenavyblue_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_mattenavyblue_1000_175_c": null,
    "elegoo_pla_plamattenavyblue_1000_175_c": [
      50,
      70
    ]
  },
  "codes": {
    "elegoo_pla_mattenavyblue_1000_175_c": null,
    "elegoo_pla_plamattenavyblue_1000_175_c": [
      "SPUK-EL-MAT-104"
    ]
  }
}
```

### EL031: dup-95bb697478b13a7e4707328376d6229a9cb63d765884c710913433121e5caebe

Status: APPROVED; survivor `elegoo_pla_matterubyred_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_matterubyred_1000_175_c`|`Matte {color_name}`|`Ruby Red`|{"source_file": "elegoo.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|
|`elegoo_pla_plamatterubyred_1000_175_c`|`PLA MATTE {color_name}`|`Ruby Red`|{"source_file": "elegoo.json", "definition_index": 20, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_matterubyred_1000_175_c": 1.26,
    "elegoo_pla_plamatterubyred_1000_175_c": 1.31
  },
  "color_hex": {
    "elegoo_pla_matterubyred_1000_175_c": "bb2c2e",
    "elegoo_pla_plamatterubyred_1000_175_c": "BB2C2E"
  },
  "extruder_temp": {
    "elegoo_pla_matterubyred_1000_175_c": 210,
    "elegoo_pla_plamatterubyred_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_matterubyred_1000_175_c": null,
    "elegoo_pla_plamatterubyred_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_matterubyred_1000_175_c": 60,
    "elegoo_pla_plamatterubyred_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_matterubyred_1000_175_c": null,
    "elegoo_pla_plamatterubyred_1000_175_c": [
      50,
      70
    ]
  },
  "codes": {
    "elegoo_pla_matterubyred_1000_175_c": null,
    "elegoo_pla_plamatterubyred_1000_175_c": [
      "SPUK-EL-MAT-103"
    ]
  }
}
```

### EL032: dup-ad154f67e0ed35711fdee6c5b2eed2384ea01519180aa25879a0963164db4de2

Status: APPROVED; survivor `elegoo_pla_mattesakurapink_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_mattesakurapink_1000_175_c`|`Matte {color_name}`|`Sakura Pink`|{"source_file": "elegoo.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|
|`elegoo_pla_plamattesakurapink_1000_175_c`|`PLA MATTE {color_name}`|`Sakura Pink`|{"source_file": "elegoo.json", "definition_index": 20, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_mattesakurapink_1000_175_c": 1.26,
    "elegoo_pla_plamattesakurapink_1000_175_c": 1.31
  },
  "color_hex": {
    "elegoo_pla_mattesakurapink_1000_175_c": "f9c2d5",
    "elegoo_pla_plamattesakurapink_1000_175_c": "F9C2D5"
  },
  "extruder_temp": {
    "elegoo_pla_mattesakurapink_1000_175_c": 210,
    "elegoo_pla_plamattesakurapink_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_mattesakurapink_1000_175_c": null,
    "elegoo_pla_plamattesakurapink_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_mattesakurapink_1000_175_c": 60,
    "elegoo_pla_plamattesakurapink_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_mattesakurapink_1000_175_c": null,
    "elegoo_pla_plamattesakurapink_1000_175_c": [
      50,
      70
    ]
  },
  "codes": {
    "elegoo_pla_mattesakurapink_1000_175_c": null,
    "elegoo_pla_plamattesakurapink_1000_175_c": [
      "SPUK-EL-MAT-109"
    ]
  }
}
```

### EL033: dup-31a0d8e00fef1adf807ee141867f3815afee179c3e07b372b02d85761bc5cf04

Status: APPROVED; survivor `elegoo_pla_matteslategrey_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_matteslategrey_1000_175_c`|`Matte {color_name}`|`Slate Grey`|{"source_file": "elegoo.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|
|`elegoo_pla_plamatteslategrey_1000_175_c`|`PLA MATTE {color_name}`|`Slate Grey`|{"source_file": "elegoo.json", "definition_index": 20, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_matteslategrey_1000_175_c": 1.26,
    "elegoo_pla_plamatteslategrey_1000_175_c": 1.31
  },
  "extruder_temp": {
    "elegoo_pla_matteslategrey_1000_175_c": 210,
    "elegoo_pla_plamatteslategrey_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_matteslategrey_1000_175_c": null,
    "elegoo_pla_plamatteslategrey_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_matteslategrey_1000_175_c": 60,
    "elegoo_pla_plamatteslategrey_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_matteslategrey_1000_175_c": null,
    "elegoo_pla_plamatteslategrey_1000_175_c": [
      50,
      70
    ]
  },
  "codes": {
    "elegoo_pla_matteslategrey_1000_175_c": null,
    "elegoo_pla_plamatteslategrey_1000_175_c": [
      "SPUK-EL-MAT-107"
    ]
  }
}
```

### EL034: dup-19376165c944ab241bdb9b39fd4136de0bbe24a5bd09833af75d11ee14580746

Status: APPROVED; survivor `elegoo_pla_mattesunshineyellow_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_mattesunshineyellow_1000_175_c`|`Matte {color_name}`|`Sunshine Yellow`|{"source_file": "elegoo.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|
|`elegoo_pla_plamattesunshineyellow_1000_175_c`|`PLA MATTE {color_name}`|`Sunshine Yellow`|{"source_file": "elegoo.json", "definition_index": 20, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_mattesunshineyellow_1000_175_c": 1.26,
    "elegoo_pla_plamattesunshineyellow_1000_175_c": 1.31
  },
  "color_hex": {
    "elegoo_pla_mattesunshineyellow_1000_175_c": "f7d863",
    "elegoo_pla_plamattesunshineyellow_1000_175_c": "F7D863"
  },
  "extruder_temp": {
    "elegoo_pla_mattesunshineyellow_1000_175_c": 210,
    "elegoo_pla_plamattesunshineyellow_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_mattesunshineyellow_1000_175_c": null,
    "elegoo_pla_plamattesunshineyellow_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_mattesunshineyellow_1000_175_c": 60,
    "elegoo_pla_plamattesunshineyellow_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_mattesunshineyellow_1000_175_c": null,
    "elegoo_pla_plamattesunshineyellow_1000_175_c": [
      50,
      70
    ]
  },
  "codes": {
    "elegoo_pla_mattesunshineyellow_1000_175_c": null,
    "elegoo_pla_plamattesunshineyellow_1000_175_c": [
      "SPUK-EL-MAT-106"
    ]
  }
}
```

### EL035: dup-7c7e3b7a77d4d46b2df47bc4e0310f0d378d73dbae2b4643c4de3023083b2107

Status: APPROVED; survivor `elegoo_pla_mattetealgreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_mattetealgreen_1000_175_c`|`Matte {color_name}`|`Teal Green`|{"source_file": "elegoo.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|
|`elegoo_pla_plamattetealgreen_1000_175_c`|`PLA MATTE {color_name}`|`Teal Green`|{"source_file": "elegoo.json", "definition_index": 20, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_mattetealgreen_1000_175_c": 1.26,
    "elegoo_pla_plamattetealgreen_1000_175_c": 1.31
  },
  "color_hex": {
    "elegoo_pla_mattetealgreen_1000_175_c": "74cdc7",
    "elegoo_pla_plamattetealgreen_1000_175_c": "74CDC7"
  },
  "extruder_temp": {
    "elegoo_pla_mattetealgreen_1000_175_c": 210,
    "elegoo_pla_plamattetealgreen_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_mattetealgreen_1000_175_c": null,
    "elegoo_pla_plamattetealgreen_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_mattetealgreen_1000_175_c": 60,
    "elegoo_pla_plamattetealgreen_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_mattetealgreen_1000_175_c": null,
    "elegoo_pla_plamattetealgreen_1000_175_c": [
      50,
      70
    ]
  },
  "codes": {
    "elegoo_pla_mattetealgreen_1000_175_c": null,
    "elegoo_pla_plamattetealgreen_1000_175_c": [
      "SPUK-EL-MAT-105"
    ]
  }
}
```

### EL036: dup-ed69b50456a359d5f5f8b401656638729e29f3d48edcbc1ed54fad593bd61469

Status: APPROVED; survivor `elegoo_pla_mattewhite_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_mattewhite_1000_175_c`|`Matte {color_name}`|`White`|{"source_file": "elegoo.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 12, "compiled_records": 12} / True|
|`elegoo_pla_plamattewhite_1000_175_c`|`PLA MATTE {color_name}`|`White`|{"source_file": "elegoo.json", "definition_index": 20, "weights": 2, "diameters": 1, "colors": 17, "compiled_records": 34} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_mattewhite_1000_175_c": 1.26,
    "elegoo_pla_plamattewhite_1000_175_c": 1.31
  },
  "color_hex": {
    "elegoo_pla_mattewhite_1000_175_c": "f6f6f6",
    "elegoo_pla_plamattewhite_1000_175_c": "FFFFFF"
  },
  "extruder_temp": {
    "elegoo_pla_mattewhite_1000_175_c": 210,
    "elegoo_pla_plamattewhite_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_mattewhite_1000_175_c": null,
    "elegoo_pla_plamattewhite_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_mattewhite_1000_175_c": 60,
    "elegoo_pla_plamattewhite_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_mattewhite_1000_175_c": null,
    "elegoo_pla_plamattewhite_1000_175_c": [
      50,
      70
    ]
  }
}
```

### EL037: dup-d285f9d24ea8b1b3660eac66165ebd61f6b21699e00678661481665c4da1feb0

Status: APPROVED; survivor `elegoo_pla_neongreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_neongreen_1000_175_c`|`{color_name}`|`Neon Green`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`elegoo_pla_planeongreen_1000_175_c`|`PLA {color_name}`|`Neon Green`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_pla_neongreen_1000_175_c": "02e601",
    "elegoo_pla_planeongreen_1000_175_c": "08E327"
  },
  "extruder_temp": {
    "elegoo_pla_neongreen_1000_175_c": 210,
    "elegoo_pla_planeongreen_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_neongreen_1000_175_c": null,
    "elegoo_pla_planeongreen_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_neongreen_1000_175_c": 60,
    "elegoo_pla_planeongreen_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_neongreen_1000_175_c": null,
    "elegoo_pla_planeongreen_1000_175_c": [
      50,
      70
    ]
  }
}
```

### EL038: dup-a01dfcc4cd70a54a94e2906f1dc70c3b367d08a20a61c3792e728a004a1d8028

Status: APPROVED; survivor `elegoo_pla_orange_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_orange_1000_175_c`|`{color_name}`|`Orange`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`elegoo_pla_plaorange_1000_175_c`|`PLA {color_name}`|`Orange`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_pla_orange_1000_175_c": "fd7c18",
    "elegoo_pla_plaorange_1000_175_c": "FD7C18"
  },
  "extruder_temp": {
    "elegoo_pla_orange_1000_175_c": 210,
    "elegoo_pla_plaorange_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_orange_1000_175_c": null,
    "elegoo_pla_plaorange_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_orange_1000_175_c": 60,
    "elegoo_pla_plaorange_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_orange_1000_175_c": null,
    "elegoo_pla_plaorange_1000_175_c": [
      50,
      70
    ]
  }
}
```

### EL039: dup-690935fe00797d36134e1821dda1c18ffb1ee5eba0f4eebf9fb80fae6fd29f32

Status: APPROVED; survivor `elegoo_pla_pink_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_pink_1000_175_c`|`{color_name}`|`Pink`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|
|`elegoo_pla_plapink_1000_175_c`|`PLA {color_name}`|`Pink`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_pla_pink_1000_175_c": "f9b0bd",
    "elegoo_pla_plapink_1000_175_c": "F9B0BD"
  },
  "extruder_temp": {
    "elegoo_pla_pink_1000_175_c": 210,
    "elegoo_pla_plapink_1000_175_c": null
  },
  "extruder_temp_range": {
    "elegoo_pla_pink_1000_175_c": null,
    "elegoo_pla_plapink_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_pink_1000_175_c": 60,
    "elegoo_pla_plapink_1000_175_c": null
  },
  "bed_temp_range": {
    "elegoo_pla_pink_1000_175_c": null,
    "elegoo_pla_plapink_1000_175_c": [
      50,
      70
    ]
  }
}
```

### EL040: dup-a0560e4d693bf53be9c2fa27d93e2c25c5bcc0b7397ce59f331b26cda64804ab

Status: APPROVED; survivor `elegoo_pla_purple_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plapurple_1000_175_c`|`PLA {color_name}`|`Purple`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_purple_1000_175_c`|`{color_name}`|`Purple`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_pla_plapurple_1000_175_c": "603BA0",
    "elegoo_pla_purple_1000_175_c": "603ba0"
  },
  "extruder_temp": {
    "elegoo_pla_plapurple_1000_175_c": null,
    "elegoo_pla_purple_1000_175_c": 210
  },
  "extruder_temp_range": {
    "elegoo_pla_plapurple_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_purple_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plapurple_1000_175_c": null,
    "elegoo_pla_purple_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plapurple_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_purple_1000_175_c": null
  }
}
```

### EL041: dup-1b1d9234a76ff760c7d3316170e468e6ad3b05b5d4cff37249adfa75fea51a02

Status: DEFERRED; survivor `elegoo_pla_plarapidplusbeige_250_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplusbeige_250_175_c`|`PLA {color_name}`|`RAPID Plus Beige`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplusbeige_250_175_c`|`RAPID PLA Plus {color_name}`|`Beige`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplusbeige_250_175_c": 1.26,
    "elegoo_pla_rapidplaplusbeige_250_175_c": 1.2
  },
  "color_hex": {
    "elegoo_pla_plarapidplusbeige_250_175_c": "DAC7A0",
    "elegoo_pla_rapidplaplusbeige_250_175_c": "F4E0B8"
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplusbeige_250_175_c": null,
    "elegoo_pla_rapidplaplusbeige_250_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplusbeige_250_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplusbeige_250_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplusbeige_250_175_c": null,
    "elegoo_pla_rapidplaplusbeige_250_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplusbeige_250_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplusbeige_250_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplusbeige_250_175_c": null,
    "elegoo_pla_rapidplaplusbeige_250_175_c": [
      "SPUK-EL-RPP-12"
    ]
  }
}
```

### EL042: dup-e5b830f25acf9d4b674f04468f253e3e48ec519cc1d5c99234a7f0343fb2241a

Status: DEFERRED; survivor `elegoo_pla_plarapidplusbeige_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplusbeige_1000_175_c`|`PLA {color_name}`|`RAPID Plus Beige`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplusbeige_1000_175_c`|`RAPID PLA Plus {color_name}`|`Beige`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplusbeige_1000_175_c": 1.26,
    "elegoo_pla_rapidplaplusbeige_1000_175_c": 1.2
  },
  "color_hex": {
    "elegoo_pla_plarapidplusbeige_1000_175_c": "DAC7A0",
    "elegoo_pla_rapidplaplusbeige_1000_175_c": "F4E0B8"
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplusbeige_1000_175_c": null,
    "elegoo_pla_rapidplaplusbeige_1000_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplusbeige_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplusbeige_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplusbeige_1000_175_c": null,
    "elegoo_pla_rapidplaplusbeige_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplusbeige_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplusbeige_1000_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplusbeige_1000_175_c": null,
    "elegoo_pla_rapidplaplusbeige_1000_175_c": [
      "SPUK-EL-RPP-12"
    ]
  }
}
```

### EL043: dup-a34f4055944cf778a79f35bb110c9f8b5ed9922f667257c21aa74621b45787ed

Status: DEFERRED; survivor `elegoo_pla_plarapidplusblack_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplusblack_1000_175_c`|`PLA {color_name}`|`RAPID Plus Black`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplusblack_1000_175_c`|`RAPID PLA Plus {color_name}`|`Black`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplusblack_1000_175_c": 1.26,
    "elegoo_pla_rapidplaplusblack_1000_175_c": 1.2
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplusblack_1000_175_c": null,
    "elegoo_pla_rapidplaplusblack_1000_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplusblack_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplusblack_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplusblack_1000_175_c": null,
    "elegoo_pla_rapidplaplusblack_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplusblack_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplusblack_1000_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplusblack_1000_175_c": null,
    "elegoo_pla_rapidplaplusblack_1000_175_c": [
      "SPUK-EL-RPP-01"
    ]
  }
}
```

### EL044: dup-f40f91047045561819fe95a941ec33ffd5d4272a33d6d366eae151ee78fef823

Status: DEFERRED; survivor `elegoo_pla_plarapidplusblack_250_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplusblack_250_175_c`|`PLA {color_name}`|`RAPID Plus Black`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplusblack_250_175_c`|`RAPID PLA Plus {color_name}`|`Black`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplusblack_250_175_c": 1.26,
    "elegoo_pla_rapidplaplusblack_250_175_c": 1.2
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplusblack_250_175_c": null,
    "elegoo_pla_rapidplaplusblack_250_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplusblack_250_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplusblack_250_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplusblack_250_175_c": null,
    "elegoo_pla_rapidplaplusblack_250_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplusblack_250_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplusblack_250_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplusblack_250_175_c": null,
    "elegoo_pla_rapidplaplusblack_250_175_c": [
      "SPUK-EL-RPP-01"
    ]
  }
}
```

### EL045: dup-485122a1cb0f281f91100b85edb1ab305533fdf6f6323ce75edc2d8d72968b43

Status: DEFERRED; survivor `elegoo_pla_plarapidplusblue_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplusblue_1000_175_c`|`PLA {color_name}`|`RAPID Plus Blue`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplusblue_1000_175_c`|`RAPID PLA Plus {color_name}`|`Blue`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplusblue_1000_175_c": 1.26,
    "elegoo_pla_rapidplaplusblue_1000_175_c": 1.2
  },
  "color_hex": {
    "elegoo_pla_plarapidplusblue_1000_175_c": "0E21AE",
    "elegoo_pla_rapidplaplusblue_1000_175_c": "2240AF"
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplusblue_1000_175_c": null,
    "elegoo_pla_rapidplaplusblue_1000_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplusblue_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplusblue_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplusblue_1000_175_c": null,
    "elegoo_pla_rapidplaplusblue_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplusblue_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplusblue_1000_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplusblue_1000_175_c": null,
    "elegoo_pla_rapidplaplusblue_1000_175_c": [
      "SPUK-EL-RPP-04"
    ]
  }
}
```

### EL046: dup-e24819a0db881e72a260080782bc11d353fef7c4672d83f93b8581b77573f05e

Status: DEFERRED; survivor `elegoo_pla_plarapidplusblue_250_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplusblue_250_175_c`|`PLA {color_name}`|`RAPID Plus Blue`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplusblue_250_175_c`|`RAPID PLA Plus {color_name}`|`Blue`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplusblue_250_175_c": 1.26,
    "elegoo_pla_rapidplaplusblue_250_175_c": 1.2
  },
  "color_hex": {
    "elegoo_pla_plarapidplusblue_250_175_c": "0E21AE",
    "elegoo_pla_rapidplaplusblue_250_175_c": "2240AF"
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplusblue_250_175_c": null,
    "elegoo_pla_rapidplaplusblue_250_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplusblue_250_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplusblue_250_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplusblue_250_175_c": null,
    "elegoo_pla_rapidplaplusblue_250_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplusblue_250_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplusblue_250_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplusblue_250_175_c": null,
    "elegoo_pla_rapidplaplusblue_250_175_c": [
      "SPUK-EL-RPP-04"
    ]
  }
}
```

### EL047: dup-1415acb0fc41debe5d923045d7f411c3b638803f29de701c6e1003f1be753c15

Status: DEFERRED; survivor `elegoo_pla_plarapidplusbrown_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplusbrown_1000_175_c`|`PLA {color_name}`|`RAPID Plus Brown`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplusbrown_1000_175_c`|`RAPID PLA Plus {color_name}`|`Brown`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplusbrown_1000_175_c": 1.26,
    "elegoo_pla_rapidplaplusbrown_1000_175_c": 1.2
  },
  "color_hex": {
    "elegoo_pla_plarapidplusbrown_1000_175_c": "A45B27",
    "elegoo_pla_rapidplaplusbrown_1000_175_c": "9E6A4B"
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplusbrown_1000_175_c": null,
    "elegoo_pla_rapidplaplusbrown_1000_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplusbrown_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplusbrown_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplusbrown_1000_175_c": null,
    "elegoo_pla_rapidplaplusbrown_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplusbrown_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplusbrown_1000_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplusbrown_1000_175_c": null,
    "elegoo_pla_rapidplaplusbrown_1000_175_c": [
      "SPUK-EL-RPP-11"
    ]
  }
}
```

### EL048: dup-f3a3120ea87f8e913a822f810abc64c99f469f32db51ef286be32c5c2621db15

Status: DEFERRED; survivor `elegoo_pla_plarapidplusbrown_250_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplusbrown_250_175_c`|`PLA {color_name}`|`RAPID Plus Brown`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplusbrown_250_175_c`|`RAPID PLA Plus {color_name}`|`Brown`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplusbrown_250_175_c": 1.26,
    "elegoo_pla_rapidplaplusbrown_250_175_c": 1.2
  },
  "color_hex": {
    "elegoo_pla_plarapidplusbrown_250_175_c": "A45B27",
    "elegoo_pla_rapidplaplusbrown_250_175_c": "9E6A4B"
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplusbrown_250_175_c": null,
    "elegoo_pla_rapidplaplusbrown_250_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplusbrown_250_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplusbrown_250_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplusbrown_250_175_c": null,
    "elegoo_pla_rapidplaplusbrown_250_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplusbrown_250_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplusbrown_250_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplusbrown_250_175_c": null,
    "elegoo_pla_rapidplaplusbrown_250_175_c": [
      "SPUK-EL-RPP-11"
    ]
  }
}
```

### EL049: dup-5f597b989b37413a10a7ef851f9a1ea0d4ef62cc206fb52e001dfe061df77d58

Status: DEFERRED; survivor `elegoo_pla_plarapidplusgreen_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplusgreen_1000_175_c`|`PLA {color_name}`|`RAPID Plus Green`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplusgreen_1000_175_c`|`RAPID PLA Plus {color_name}`|`Green`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplusgreen_1000_175_c": 1.26,
    "elegoo_pla_rapidplaplusgreen_1000_175_c": 1.2
  },
  "color_hex": {
    "elegoo_pla_plarapidplusgreen_1000_175_c": "4DFF64",
    "elegoo_pla_rapidplaplusgreen_1000_175_c": "08E327"
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplusgreen_1000_175_c": null,
    "elegoo_pla_rapidplaplusgreen_1000_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplusgreen_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplusgreen_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplusgreen_1000_175_c": null,
    "elegoo_pla_rapidplaplusgreen_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplusgreen_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplusgreen_1000_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplusgreen_1000_175_c": null,
    "elegoo_pla_rapidplaplusgreen_1000_175_c": [
      "SPUK-EL-RPP-05"
    ]
  }
}
```

### EL050: dup-aa0078b4fa3522dc8e7e56fcff0def49940a676ea69ee5b8756c398ee2dbde27

Status: DEFERRED; survivor `elegoo_pla_plarapidplusgreen_250_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplusgreen_250_175_c`|`PLA {color_name}`|`RAPID Plus Green`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplusgreen_250_175_c`|`RAPID PLA Plus {color_name}`|`Green`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplusgreen_250_175_c": 1.26,
    "elegoo_pla_rapidplaplusgreen_250_175_c": 1.2
  },
  "color_hex": {
    "elegoo_pla_plarapidplusgreen_250_175_c": "4DFF64",
    "elegoo_pla_rapidplaplusgreen_250_175_c": "08E327"
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplusgreen_250_175_c": null,
    "elegoo_pla_rapidplaplusgreen_250_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplusgreen_250_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplusgreen_250_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplusgreen_250_175_c": null,
    "elegoo_pla_rapidplaplusgreen_250_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplusgreen_250_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplusgreen_250_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplusgreen_250_175_c": null,
    "elegoo_pla_rapidplaplusgreen_250_175_c": [
      "SPUK-EL-RPP-05"
    ]
  }
}
```

### EL051: dup-0522d36ad17429ef0ef4c56b43995b1ba979a0693d7c7abaa095501d61aa81cb

Status: DEFERRED; survivor `elegoo_pla_plarapidplusgrey_250_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplusgrey_250_175_c`|`PLA {color_name}`|`RAPID Plus Grey`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplusgrey_250_175_c`|`RAPID PLA Plus {color_name}`|`Grey`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplusgrey_250_175_c": 1.26,
    "elegoo_pla_rapidplaplusgrey_250_175_c": 1.2
  },
  "color_hex": {
    "elegoo_pla_plarapidplusgrey_250_175_c": "9F9F9F",
    "elegoo_pla_rapidplaplusgrey_250_175_c": "8F949B"
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplusgrey_250_175_c": null,
    "elegoo_pla_rapidplaplusgrey_250_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplusgrey_250_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplusgrey_250_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplusgrey_250_175_c": null,
    "elegoo_pla_rapidplaplusgrey_250_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplusgrey_250_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplusgrey_250_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplusgrey_250_175_c": null,
    "elegoo_pla_rapidplaplusgrey_250_175_c": [
      "SPUK-EL-RPP-03"
    ]
  }
}
```

### EL052: dup-d93daecaf2dad9556bacb5bdd4befbb4497784e223d538e3922917fcbc8397de

Status: DEFERRED; survivor `elegoo_pla_plarapidplusgrey_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplusgrey_1000_175_c`|`PLA {color_name}`|`RAPID Plus Grey`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplusgrey_1000_175_c`|`RAPID PLA Plus {color_name}`|`Grey`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplusgrey_1000_175_c": 1.26,
    "elegoo_pla_rapidplaplusgrey_1000_175_c": 1.2
  },
  "color_hex": {
    "elegoo_pla_plarapidplusgrey_1000_175_c": "9F9F9F",
    "elegoo_pla_rapidplaplusgrey_1000_175_c": "8F949B"
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplusgrey_1000_175_c": null,
    "elegoo_pla_rapidplaplusgrey_1000_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplusgrey_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplusgrey_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplusgrey_1000_175_c": null,
    "elegoo_pla_rapidplaplusgrey_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplusgrey_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplusgrey_1000_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplusgrey_1000_175_c": null,
    "elegoo_pla_rapidplaplusgrey_1000_175_c": [
      "SPUK-EL-RPP-03"
    ]
  }
}
```

### EL053: dup-af8a14fb0686ae935a1ef2c34c7e12c23f261ea573977616548481cee1794176

Status: DEFERRED; survivor `elegoo_pla_plarapidplusorange_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplusorange_1000_175_c`|`PLA {color_name}`|`RAPID Plus Orange`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplusorange_1000_175_c`|`RAPID PLA Plus {color_name}`|`Orange`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplusorange_1000_175_c": 1.26,
    "elegoo_pla_rapidplaplusorange_1000_175_c": 1.2
  },
  "color_hex": {
    "elegoo_pla_plarapidplusorange_1000_175_c": "FF8E24",
    "elegoo_pla_rapidplaplusorange_1000_175_c": "FD7C18"
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplusorange_1000_175_c": null,
    "elegoo_pla_rapidplaplusorange_1000_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplusorange_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplusorange_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplusorange_1000_175_c": null,
    "elegoo_pla_rapidplaplusorange_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplusorange_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplusorange_1000_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplusorange_1000_175_c": null,
    "elegoo_pla_rapidplaplusorange_1000_175_c": [
      "SPUK-EL-RPP-07"
    ]
  }
}
```

### EL054: dup-b92be3818953e7c6a7a572df7fc8eb34a83af0b6849c35f3c96f4d8ec25a6469

Status: DEFERRED; survivor `elegoo_pla_plarapidplusorange_250_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplusorange_250_175_c`|`PLA {color_name}`|`RAPID Plus Orange`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplusorange_250_175_c`|`RAPID PLA Plus {color_name}`|`Orange`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplusorange_250_175_c": 1.26,
    "elegoo_pla_rapidplaplusorange_250_175_c": 1.2
  },
  "color_hex": {
    "elegoo_pla_plarapidplusorange_250_175_c": "FF8E24",
    "elegoo_pla_rapidplaplusorange_250_175_c": "FD7C18"
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplusorange_250_175_c": null,
    "elegoo_pla_rapidplaplusorange_250_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplusorange_250_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplusorange_250_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplusorange_250_175_c": null,
    "elegoo_pla_rapidplaplusorange_250_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplusorange_250_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplusorange_250_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplusorange_250_175_c": null,
    "elegoo_pla_rapidplaplusorange_250_175_c": [
      "SPUK-EL-RPP-07"
    ]
  }
}
```

### EL055: dup-3799af5b253b3cbc210e42baa609496eab7cd4027f8084ab49fc0ddd212181bf

Status: DEFERRED; survivor `elegoo_pla_plarapidplusred_250_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplusred_250_175_c`|`PLA {color_name}`|`RAPID Plus Red`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplusred_250_175_c`|`RAPID PLA Plus {color_name}`|`Red`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplusred_250_175_c": 1.26,
    "elegoo_pla_rapidplaplusred_250_175_c": 1.2
  },
  "color_hex": {
    "elegoo_pla_plarapidplusred_250_175_c": "DE1619",
    "elegoo_pla_rapidplaplusred_250_175_c": "EA140E"
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplusred_250_175_c": null,
    "elegoo_pla_rapidplaplusred_250_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplusred_250_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplusred_250_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplusred_250_175_c": null,
    "elegoo_pla_rapidplaplusred_250_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplusred_250_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplusred_250_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplusred_250_175_c": null,
    "elegoo_pla_rapidplaplusred_250_175_c": [
      "SPUK-EL-RPP-06"
    ]
  }
}
```

### EL056: dup-41bb4814cf71ee60c02ce320078ec87034c7102de8fd48945d1be5456efe85e8

Status: DEFERRED; survivor `elegoo_pla_plarapidplusred_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplusred_1000_175_c`|`PLA {color_name}`|`RAPID Plus Red`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplusred_1000_175_c`|`RAPID PLA Plus {color_name}`|`Red`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplusred_1000_175_c": 1.26,
    "elegoo_pla_rapidplaplusred_1000_175_c": 1.2
  },
  "color_hex": {
    "elegoo_pla_plarapidplusred_1000_175_c": "DE1619",
    "elegoo_pla_rapidplaplusred_1000_175_c": "EA140E"
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplusred_1000_175_c": null,
    "elegoo_pla_rapidplaplusred_1000_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplusred_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplusred_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplusred_1000_175_c": null,
    "elegoo_pla_rapidplaplusred_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplusred_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplusred_1000_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplusred_1000_175_c": null,
    "elegoo_pla_rapidplaplusred_1000_175_c": [
      "SPUK-EL-RPP-06"
    ]
  }
}
```

### EL057: dup-dbdaeb7011cfbaf7f0c0901ef55eb4404ce72f2ac959daf9cf020bfaac31104e

Status: DEFERRED; survivor `elegoo_pla_plarapidplussilver_250_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplussilver_250_175_c`|`PLA {color_name}`|`RAPID Plus Silver`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplussilver_250_175_c`|`RAPID PLA Plus {color_name}`|`Silver`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplussilver_250_175_c": 1.26,
    "elegoo_pla_rapidplaplussilver_250_175_c": 1.2
  },
  "color_hex": {
    "elegoo_pla_plarapidplussilver_250_175_c": "6F727E",
    "elegoo_pla_rapidplaplussilver_250_175_c": "9F9F9F"
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplussilver_250_175_c": null,
    "elegoo_pla_rapidplaplussilver_250_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplussilver_250_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplussilver_250_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplussilver_250_175_c": null,
    "elegoo_pla_rapidplaplussilver_250_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplussilver_250_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplussilver_250_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplussilver_250_175_c": null,
    "elegoo_pla_rapidplaplussilver_250_175_c": [
      "SPUK-EL-RPP-09"
    ]
  }
}
```

### EL058: dup-dd044189a170d45217db1ae8f48bb7abbf2afbac511a32a76fc5a9ba4b1440d9

Status: DEFERRED; survivor `elegoo_pla_plarapidplussilver_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplussilver_1000_175_c`|`PLA {color_name}`|`RAPID Plus Silver`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplussilver_1000_175_c`|`RAPID PLA Plus {color_name}`|`Silver`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplussilver_1000_175_c": 1.26,
    "elegoo_pla_rapidplaplussilver_1000_175_c": 1.2
  },
  "color_hex": {
    "elegoo_pla_plarapidplussilver_1000_175_c": "6F727E",
    "elegoo_pla_rapidplaplussilver_1000_175_c": "9F9F9F"
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplussilver_1000_175_c": null,
    "elegoo_pla_rapidplaplussilver_1000_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplussilver_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplussilver_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplussilver_1000_175_c": null,
    "elegoo_pla_rapidplaplussilver_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplussilver_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplussilver_1000_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplussilver_1000_175_c": null,
    "elegoo_pla_rapidplaplussilver_1000_175_c": [
      "SPUK-EL-RPP-09"
    ]
  }
}
```

### EL059: dup-896cb956e68a1f8f0a54fe9eba5b1bad44266fba3ee9ebdb765453ce2e62d872

Status: DEFERRED; survivor `elegoo_pla_plarapidpluswhite_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidpluswhite_1000_175_c`|`PLA {color_name}`|`RAPID Plus White`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplapluswhite_1000_175_c`|`RAPID PLA Plus {color_name}`|`White`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidpluswhite_1000_175_c": 1.26,
    "elegoo_pla_rapidplapluswhite_1000_175_c": 1.2
  },
  "extruder_temp": {
    "elegoo_pla_plarapidpluswhite_1000_175_c": null,
    "elegoo_pla_rapidplapluswhite_1000_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidpluswhite_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplapluswhite_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidpluswhite_1000_175_c": null,
    "elegoo_pla_rapidplapluswhite_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidpluswhite_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplapluswhite_1000_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidpluswhite_1000_175_c": null,
    "elegoo_pla_rapidplapluswhite_1000_175_c": [
      "SPUK-EL-RPP-02"
    ]
  }
}
```

### EL060: dup-de359707fd50d6af8ee29f835a9529737defe57debde9e46f443e1de6ecd58ae

Status: DEFERRED; survivor `elegoo_pla_plarapidpluswhite_250_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidpluswhite_250_175_c`|`PLA {color_name}`|`RAPID Plus White`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplapluswhite_250_175_c`|`RAPID PLA Plus {color_name}`|`White`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidpluswhite_250_175_c": 1.26,
    "elegoo_pla_rapidplapluswhite_250_175_c": 1.2
  },
  "extruder_temp": {
    "elegoo_pla_plarapidpluswhite_250_175_c": null,
    "elegoo_pla_rapidplapluswhite_250_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidpluswhite_250_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplapluswhite_250_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidpluswhite_250_175_c": null,
    "elegoo_pla_rapidplapluswhite_250_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidpluswhite_250_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplapluswhite_250_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidpluswhite_250_175_c": null,
    "elegoo_pla_rapidplapluswhite_250_175_c": [
      "SPUK-EL-RPP-02"
    ]
  }
}
```

### EL061: dup-6df5f8e917c6822ddaa3dd06298be8df621eb4c8ac8dc9c67be67bec01076669

Status: DEFERRED; survivor `elegoo_pla_plarapidplusyellow_250_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplusyellow_250_175_c`|`PLA {color_name}`|`RAPID Plus Yellow`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplusyellow_250_175_c`|`RAPID PLA Plus {color_name}`|`Yellow`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplusyellow_250_175_c": 1.26,
    "elegoo_pla_rapidplaplusyellow_250_175_c": 1.2
  },
  "color_hex": {
    "elegoo_pla_plarapidplusyellow_250_175_c": "FBE200",
    "elegoo_pla_rapidplaplusyellow_250_175_c": "FBEC07"
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplusyellow_250_175_c": null,
    "elegoo_pla_rapidplaplusyellow_250_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplusyellow_250_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplusyellow_250_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplusyellow_250_175_c": null,
    "elegoo_pla_rapidplaplusyellow_250_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplusyellow_250_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplusyellow_250_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplusyellow_250_175_c": null,
    "elegoo_pla_rapidplaplusyellow_250_175_c": [
      "SPUK-EL-RPP-08"
    ]
  }
}
```

### EL062: dup-a7a6d6fa72fc0162c74e614ca474fdbcba27eda527ec68f799491755414a2078

Status: DEFERRED; survivor `elegoo_pla_plarapidplusyellow_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plarapidplusyellow_1000_175_c`|`PLA {color_name}`|`RAPID Plus Yellow`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_rapidplaplusyellow_1000_175_c`|`RAPID PLA Plus {color_name}`|`Yellow`|{"source_file": "elegoo.json", "definition_index": 25, "weights": 3, "diameters": 1, "colors": 11, "compiled_records": 33} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_plarapidplusyellow_1000_175_c": 1.26,
    "elegoo_pla_rapidplaplusyellow_1000_175_c": 1.2
  },
  "color_hex": {
    "elegoo_pla_plarapidplusyellow_1000_175_c": "FBE200",
    "elegoo_pla_rapidplaplusyellow_1000_175_c": "FBEC07"
  },
  "extruder_temp": {
    "elegoo_pla_plarapidplusyellow_1000_175_c": null,
    "elegoo_pla_rapidplaplusyellow_1000_175_c": 205
  },
  "extruder_temp_range": {
    "elegoo_pla_plarapidplusyellow_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_rapidplaplusyellow_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plarapidplusyellow_1000_175_c": null,
    "elegoo_pla_rapidplaplusyellow_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plarapidplusyellow_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_rapidplaplusyellow_1000_175_c": null
  },
  "codes": {
    "elegoo_pla_plarapidplusyellow_1000_175_c": null,
    "elegoo_pla_rapidplaplusyellow_1000_175_c": [
      "SPUK-EL-RPP-08"
    ]
  }
}
```

### EL063: dup-3eee36da08e3e28d7be15987955b734e1f2e5096ba62eaded1199645dd326251

Status: APPROVED; survivor `elegoo_pla_red_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plared_1000_175_c`|`PLA {color_name}`|`Red`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_red_1000_175_c`|`{color_name}`|`Red`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_pla_plared_1000_175_c": "EA140E",
    "elegoo_pla_red_1000_175_c": "ea140e"
  },
  "extruder_temp": {
    "elegoo_pla_plared_1000_175_c": null,
    "elegoo_pla_red_1000_175_c": 210
  },
  "extruder_temp_range": {
    "elegoo_pla_plared_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_red_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plared_1000_175_c": null,
    "elegoo_pla_red_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plared_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_red_1000_175_c": null
  }
}
```

### EL064: dup-bfe731f2c4d64edfafd2874ea23cecb82b1d1e00606b2299856013ac878be23c

Status: APPROVED; survivor `elegoo_pla_seagreen_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plaseagreen_1000_175_c`|`PLA {color_name}`|`Sea Green`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_seagreen_1000_175_c`|`{color_name}`|`Sea Green`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_pla_plaseagreen_1000_175_c": "08B690",
    "elegoo_pla_seagreen_1000_175_c": "1abc83"
  },
  "extruder_temp": {
    "elegoo_pla_plaseagreen_1000_175_c": null,
    "elegoo_pla_seagreen_1000_175_c": 210
  },
  "extruder_temp_range": {
    "elegoo_pla_plaseagreen_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_seagreen_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plaseagreen_1000_175_c": null,
    "elegoo_pla_seagreen_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plaseagreen_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_seagreen_1000_175_c": null
  }
}
```

### EL065: dup-1443da86a88ee2d25bf66f6c5355bbbe21a2512dbfcdf528cb8e3fff79d55b39

Status: APPROVED; survivor `elegoo_pla_skyblue_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plaskyblue_1000_175_c`|`PLA {color_name}`|`Sky Blue`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_skyblue_1000_175_c`|`{color_name}`|`Sky Blue`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_pla_plaskyblue_1000_175_c": "32D0EC",
    "elegoo_pla_skyblue_1000_175_c": "27b2d0"
  },
  "extruder_temp": {
    "elegoo_pla_plaskyblue_1000_175_c": null,
    "elegoo_pla_skyblue_1000_175_c": 210
  },
  "extruder_temp_range": {
    "elegoo_pla_plaskyblue_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_skyblue_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plaskyblue_1000_175_c": null,
    "elegoo_pla_skyblue_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plaskyblue_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_skyblue_1000_175_c": null
  }
}
```

### EL066: dup-c221da5f214938da3b84247d97cfeb7430d05f0a2cb8ae27de89159106f48cc1

Status: APPROVED; survivor `elegoo_pla_spacegrey_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plaspacegrey_1000_175_c`|`PLA {color_name}`|`Space Grey`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_spacegrey_1000_175_c`|`{color_name}`|`Space Grey`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_pla_plaspacegrey_1000_175_c": "7E7E7E",
    "elegoo_pla_spacegrey_1000_175_c": "5d5d5d"
  },
  "extruder_temp": {
    "elegoo_pla_plaspacegrey_1000_175_c": null,
    "elegoo_pla_spacegrey_1000_175_c": 210
  },
  "extruder_temp_range": {
    "elegoo_pla_plaspacegrey_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_spacegrey_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plaspacegrey_1000_175_c": null,
    "elegoo_pla_spacegrey_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plaspacegrey_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_spacegrey_1000_175_c": null
  }
}
```

### EL067: dup-1e848b2f9b0a3bd4719cec6d891331b451021e2848c10f637ed9a6add1d13be6

Status: APPROVED; survivor `elegoo_pla_translucent_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_platranslucent_1000_175_c`|`PLA {color_name}`|`Translucent`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_translucent_1000_175_c`|`{color_name}`|`Translucent`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_pla_platranslucent_1000_175_c": "F5F5F5",
    "elegoo_pla_translucent_1000_175_c": "e9e9e7"
  },
  "extruder_temp": {
    "elegoo_pla_platranslucent_1000_175_c": null,
    "elegoo_pla_translucent_1000_175_c": 210
  },
  "extruder_temp_range": {
    "elegoo_pla_platranslucent_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_translucent_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_platranslucent_1000_175_c": null,
    "elegoo_pla_translucent_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_platranslucent_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_translucent_1000_175_c": null
  }
}
```

### EL068: dup-8ec4278db148a6b51415f56029cf54fb05ca6ca3236e5f35935c9337e22e5e87

Status: APPROVED; survivor `elegoo_pla_white_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plawhite_1000_175_c`|`PLA {color_name}`|`White`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_white_1000_175_c`|`{color_name}`|`White`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_pla_plawhite_1000_175_c": "FFFFFF",
    "elegoo_pla_white_1000_175_c": "ffffff"
  },
  "extruder_temp": {
    "elegoo_pla_plawhite_1000_175_c": null,
    "elegoo_pla_white_1000_175_c": 210
  },
  "extruder_temp_range": {
    "elegoo_pla_plawhite_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_white_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plawhite_1000_175_c": null,
    "elegoo_pla_white_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plawhite_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_white_1000_175_c": null
  }
}
```

### EL069: dup-ba375b5b9d7e8ec92103eee59288fa986cd8a46113ed59fd2d7cf3e95fa0671a

Status: APPROVED; survivor `elegoo_pla_woodcolor_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plawoodcolor_1000_175_c`|`PLA {color_name}`|`Wood Color`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_woodcolor_1000_175_c`|`{color_name}`|`Wood Color`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_pla_plawoodcolor_1000_175_c": "B19870",
    "elegoo_pla_woodcolor_1000_175_c": "b19870"
  },
  "extruder_temp": {
    "elegoo_pla_plawoodcolor_1000_175_c": null,
    "elegoo_pla_woodcolor_1000_175_c": 210
  },
  "extruder_temp_range": {
    "elegoo_pla_plawoodcolor_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_woodcolor_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plawoodcolor_1000_175_c": null,
    "elegoo_pla_woodcolor_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plawoodcolor_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_woodcolor_1000_175_c": null
  }
}
```

### EL070: dup-6a6c547b63260a6514f28dd65dd3e193bd265486d5af68529b47a458d105724d

Status: APPROVED; survivor `elegoo_pla_woodfilled_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_plawoodfilled_1000_175_c`|`PLA {color_name}`|`Wood filled`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_woodfilled_1000_175_c`|`{color_name}`|`Wood Filled`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_pla_plawoodfilled_1000_175_c": "9D8058",
    "elegoo_pla_woodfilled_1000_175_c": "9d8058"
  },
  "extruder_temp": {
    "elegoo_pla_plawoodfilled_1000_175_c": null,
    "elegoo_pla_woodfilled_1000_175_c": 210
  },
  "extruder_temp_range": {
    "elegoo_pla_plawoodfilled_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_woodfilled_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_plawoodfilled_1000_175_c": null,
    "elegoo_pla_woodfilled_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_plawoodfilled_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_woodfilled_1000_175_c": null
  }
}
```

### EL071: dup-2472bb06b6d0b10322bb57b744d3d4ffb1ebce3a8edb9e68459d33650e51201e

Status: APPROVED; survivor `elegoo_pla_yellow_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_playellow_1000_175_c`|`PLA {color_name}`|`Yellow`|{"source_file": "elegoo.json", "definition_index": 17, "weights": 3, "diameters": 1, "colors": 49, "compiled_records": 147} / False|
|`elegoo_pla_yellow_1000_175_c`|`{color_name}`|`Yellow`|{"source_file": "elegoo.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 20, "compiled_records": 20} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "elegoo_pla_playellow_1000_175_c": "FBEC07",
    "elegoo_pla_yellow_1000_175_c": "f6d701"
  },
  "extruder_temp": {
    "elegoo_pla_playellow_1000_175_c": null,
    "elegoo_pla_yellow_1000_175_c": 210
  },
  "extruder_temp_range": {
    "elegoo_pla_playellow_1000_175_c": [
      190,
      230
    ],
    "elegoo_pla_yellow_1000_175_c": null
  },
  "bed_temp": {
    "elegoo_pla_playellow_1000_175_c": null,
    "elegoo_pla_yellow_1000_175_c": 60
  },
  "bed_temp_range": {
    "elegoo_pla_playellow_1000_175_c": [
      50,
      70
    ],
    "elegoo_pla_yellow_1000_175_c": null
  }
}
```

### EL072: dup-d695b65d2bcf8ad2fb7ed883b7eec9907669f74e3c10426f50028c770ac776cf

Status: APPROVED; survivor `elegoo_pla_silkblackpurple_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_silkblackpurple_1000_175_p`|`Silk {color_name}`|`Black Purple`|{"source_file": "elegoo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / True|
|`elegoo_pla_silkplablackpurple_1000_175_p`|`Silk PLA {color_name}`|`Black Purple`|{"source_file": "elegoo.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_silkblackpurple_1000_175_p": 1.25,
    "elegoo_pla_silkplablackpurple_1000_175_p": 1.24
  },
  "color_hex": {
    "elegoo_pla_silkblackpurple_1000_175_p": null,
    "elegoo_pla_silkplablackpurple_1000_175_p": "000000"
  },
  "color_hexes": {
    "elegoo_pla_silkblackpurple_1000_175_p": [
      "000000",
      "7433BA"
    ],
    "elegoo_pla_silkplablackpurple_1000_175_p": null
  },
  "extruder_temp": {
    "elegoo_pla_silkblackpurple_1000_175_p": 220,
    "elegoo_pla_silkplablackpurple_1000_175_p": null
  },
  "extruder_temp_range": {
    "elegoo_pla_silkblackpurple_1000_175_p": null,
    "elegoo_pla_silkplablackpurple_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_silkblackpurple_1000_175_p": 60,
    "elegoo_pla_silkplablackpurple_1000_175_p": null
  },
  "bed_temp_range": {
    "elegoo_pla_silkblackpurple_1000_175_p": null,
    "elegoo_pla_silkplablackpurple_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "elegoo_pla_silkblackpurple_1000_175_p": "glossy",
    "elegoo_pla_silkplablackpurple_1000_175_p": null
  },
  "multi_color_direction": {
    "elegoo_pla_silkblackpurple_1000_175_p": "coaxial",
    "elegoo_pla_silkplablackpurple_1000_175_p": null
  }
}
```

### EL073: dup-e1a800bb11d5c9d72170e85e030077bffea30dd565e3e913d0ccc3b2f0658b74

Status: APPROVED; survivor `elegoo_pla_silkblackred_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_silkblackred_1000_175_p`|`Silk {color_name}`|`Black Red`|{"source_file": "elegoo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / True|
|`elegoo_pla_silkplablackred_1000_175_p`|`Silk PLA {color_name}`|`Black Red`|{"source_file": "elegoo.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_silkblackred_1000_175_p": 1.25,
    "elegoo_pla_silkplablackred_1000_175_p": 1.24
  },
  "color_hex": {
    "elegoo_pla_silkblackred_1000_175_p": null,
    "elegoo_pla_silkplablackred_1000_175_p": "000000"
  },
  "color_hexes": {
    "elegoo_pla_silkblackred_1000_175_p": [
      "000000",
      "ED646B"
    ],
    "elegoo_pla_silkplablackred_1000_175_p": null
  },
  "extruder_temp": {
    "elegoo_pla_silkblackred_1000_175_p": 220,
    "elegoo_pla_silkplablackred_1000_175_p": null
  },
  "extruder_temp_range": {
    "elegoo_pla_silkblackred_1000_175_p": null,
    "elegoo_pla_silkplablackred_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_silkblackred_1000_175_p": 60,
    "elegoo_pla_silkplablackred_1000_175_p": null
  },
  "bed_temp_range": {
    "elegoo_pla_silkblackred_1000_175_p": null,
    "elegoo_pla_silkplablackred_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "elegoo_pla_silkblackred_1000_175_p": "glossy",
    "elegoo_pla_silkplablackred_1000_175_p": null
  },
  "multi_color_direction": {
    "elegoo_pla_silkblackred_1000_175_p": "coaxial",
    "elegoo_pla_silkplablackred_1000_175_p": null
  }
}
```

### EL074: dup-3207600b18bd4c29bf7843bbd76f5a13d538c10eab2e9e81bceb7e5f98374dcb

Status: APPROVED; survivor `elegoo_pla_silkbluegreen_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_silkbluegreen_1000_175_p`|`Silk {color_name}`|`Blue Green`|{"source_file": "elegoo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / True|
|`elegoo_pla_silkplabluegreen_1000_175_p`|`Silk PLA {color_name}`|`Blue Green`|{"source_file": "elegoo.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_silkbluegreen_1000_175_p": 1.25,
    "elegoo_pla_silkplabluegreen_1000_175_p": 1.24
  },
  "color_hex": {
    "elegoo_pla_silkbluegreen_1000_175_p": null,
    "elegoo_pla_silkplabluegreen_1000_175_p": "0099E6"
  },
  "color_hexes": {
    "elegoo_pla_silkbluegreen_1000_175_p": [
      "0565D1",
      "22C36C"
    ],
    "elegoo_pla_silkplabluegreen_1000_175_p": null
  },
  "extruder_temp": {
    "elegoo_pla_silkbluegreen_1000_175_p": 220,
    "elegoo_pla_silkplabluegreen_1000_175_p": null
  },
  "extruder_temp_range": {
    "elegoo_pla_silkbluegreen_1000_175_p": null,
    "elegoo_pla_silkplabluegreen_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_silkbluegreen_1000_175_p": 60,
    "elegoo_pla_silkplabluegreen_1000_175_p": null
  },
  "bed_temp_range": {
    "elegoo_pla_silkbluegreen_1000_175_p": null,
    "elegoo_pla_silkplabluegreen_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "elegoo_pla_silkbluegreen_1000_175_p": "glossy",
    "elegoo_pla_silkplabluegreen_1000_175_p": null
  },
  "multi_color_direction": {
    "elegoo_pla_silkbluegreen_1000_175_p": "coaxial",
    "elegoo_pla_silkplabluegreen_1000_175_p": null
  }
}
```

### EL075: dup-825070101d134ebbf45b312ee33c8119a3c325572d482446da33ad99833607cd

Status: APPROVED; survivor `elegoo_pla_silkbluegreenorange_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_silkbluegreenorange_1000_175_p`|`Silk {color_name}`|`Blue Green Orange`|{"source_file": "elegoo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / True|
|`elegoo_pla_silkplabluegreenorange_1000_175_p`|`Silk PLA {color_name}`|`Blue Green Orange`|{"source_file": "elegoo.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_silkbluegreenorange_1000_175_p": 1.25,
    "elegoo_pla_silkplabluegreenorange_1000_175_p": 1.24
  },
  "color_hex": {
    "elegoo_pla_silkbluegreenorange_1000_175_p": null,
    "elegoo_pla_silkplabluegreenorange_1000_175_p": "0353BA"
  },
  "color_hexes": {
    "elegoo_pla_silkbluegreenorange_1000_175_p": [
      "125CA3",
      "DE6A21",
      "3F9510"
    ],
    "elegoo_pla_silkplabluegreenorange_1000_175_p": null
  },
  "extruder_temp": {
    "elegoo_pla_silkbluegreenorange_1000_175_p": 220,
    "elegoo_pla_silkplabluegreenorange_1000_175_p": null
  },
  "extruder_temp_range": {
    "elegoo_pla_silkbluegreenorange_1000_175_p": null,
    "elegoo_pla_silkplabluegreenorange_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_silkbluegreenorange_1000_175_p": 60,
    "elegoo_pla_silkplabluegreenorange_1000_175_p": null
  },
  "bed_temp_range": {
    "elegoo_pla_silkbluegreenorange_1000_175_p": null,
    "elegoo_pla_silkplabluegreenorange_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "elegoo_pla_silkbluegreenorange_1000_175_p": "glossy",
    "elegoo_pla_silkplabluegreenorange_1000_175_p": null
  },
  "multi_color_direction": {
    "elegoo_pla_silkbluegreenorange_1000_175_p": "coaxial",
    "elegoo_pla_silkplabluegreenorange_1000_175_p": null
  }
}
```

### EL076: dup-4fff49d9d795b08f0c3d2a26844041faf2517d30d1f404ad9a2b8325200c0706

Status: APPROVED; survivor `elegoo_pla_silkbluemagenta_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_silkbluemagenta_1000_175_p`|`Silk {color_name}`|`Blue Magenta`|{"source_file": "elegoo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / True|
|`elegoo_pla_silkplabluemagenta_1000_175_p`|`Silk PLA {color_name}`|`Blue Magenta`|{"source_file": "elegoo.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_silkbluemagenta_1000_175_p": 1.25,
    "elegoo_pla_silkplabluemagenta_1000_175_p": 1.24
  },
  "color_hex": {
    "elegoo_pla_silkbluemagenta_1000_175_p": null,
    "elegoo_pla_silkplabluemagenta_1000_175_p": "77398B"
  },
  "color_hexes": {
    "elegoo_pla_silkbluemagenta_1000_175_p": [
      "294FBA",
      "A92D6F"
    ],
    "elegoo_pla_silkplabluemagenta_1000_175_p": null
  },
  "extruder_temp": {
    "elegoo_pla_silkbluemagenta_1000_175_p": 220,
    "elegoo_pla_silkplabluemagenta_1000_175_p": null
  },
  "extruder_temp_range": {
    "elegoo_pla_silkbluemagenta_1000_175_p": null,
    "elegoo_pla_silkplabluemagenta_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_silkbluemagenta_1000_175_p": 60,
    "elegoo_pla_silkplabluemagenta_1000_175_p": null
  },
  "bed_temp_range": {
    "elegoo_pla_silkbluemagenta_1000_175_p": null,
    "elegoo_pla_silkplabluemagenta_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "elegoo_pla_silkbluemagenta_1000_175_p": "glossy",
    "elegoo_pla_silkplabluemagenta_1000_175_p": null
  },
  "multi_color_direction": {
    "elegoo_pla_silkbluemagenta_1000_175_p": "coaxial",
    "elegoo_pla_silkplabluemagenta_1000_175_p": null
  }
}
```

### EL077: dup-63c23b84f32e5f6e530e0151df72dc0ee68b3e9c9baa4807d26cc9ce0682f0f9

Status: APPROVED; survivor `elegoo_pla_silkbluepurpleblack_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_silkbluepurpleblack_1000_175_p`|`Silk {color_name}`|`Blue Purple Black`|{"source_file": "elegoo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / True|
|`elegoo_pla_silkplabluepurpleblack_1000_175_p`|`Silk PLA {color_name}`|`Blue Purple Black`|{"source_file": "elegoo.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_silkbluepurpleblack_1000_175_p": 1.25,
    "elegoo_pla_silkplabluepurpleblack_1000_175_p": 1.24
  },
  "color_hex": {
    "elegoo_pla_silkbluepurpleblack_1000_175_p": null,
    "elegoo_pla_silkplabluepurpleblack_1000_175_p": "0353BA"
  },
  "color_hexes": {
    "elegoo_pla_silkbluepurpleblack_1000_175_p": [
      "0565D1",
      "7433BA",
      "000000"
    ],
    "elegoo_pla_silkplabluepurpleblack_1000_175_p": null
  },
  "extruder_temp": {
    "elegoo_pla_silkbluepurpleblack_1000_175_p": 220,
    "elegoo_pla_silkplabluepurpleblack_1000_175_p": null
  },
  "extruder_temp_range": {
    "elegoo_pla_silkbluepurpleblack_1000_175_p": null,
    "elegoo_pla_silkplabluepurpleblack_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_silkbluepurpleblack_1000_175_p": 60,
    "elegoo_pla_silkplabluepurpleblack_1000_175_p": null
  },
  "bed_temp_range": {
    "elegoo_pla_silkbluepurpleblack_1000_175_p": null,
    "elegoo_pla_silkplabluepurpleblack_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "elegoo_pla_silkbluepurpleblack_1000_175_p": "glossy",
    "elegoo_pla_silkplabluepurpleblack_1000_175_p": null
  },
  "multi_color_direction": {
    "elegoo_pla_silkbluepurpleblack_1000_175_p": "coaxial",
    "elegoo_pla_silkplabluepurpleblack_1000_175_p": null
  }
}
```

### EL078: dup-d386bbd955989c8f7f4d99015dbd41c15e1720c61c24e760f62c63d924cef5a7

Status: APPROVED; survivor `elegoo_pla_silkbronze_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_silkbronze_1000_175_p`|`Silk {color_name}`|`Bronze`|{"source_file": "elegoo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / True|
|`elegoo_pla_silkplabronze_1000_175_p`|`Silk PLA {color_name}`|`Bronze`|{"source_file": "elegoo.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_silkbronze_1000_175_p": 1.25,
    "elegoo_pla_silkplabronze_1000_175_p": 1.24
  },
  "color_hex": {
    "elegoo_pla_silkbronze_1000_175_p": "965c39",
    "elegoo_pla_silkplabronze_1000_175_p": "A45B27"
  },
  "extruder_temp": {
    "elegoo_pla_silkbronze_1000_175_p": 220,
    "elegoo_pla_silkplabronze_1000_175_p": null
  },
  "extruder_temp_range": {
    "elegoo_pla_silkbronze_1000_175_p": null,
    "elegoo_pla_silkplabronze_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_silkbronze_1000_175_p": 60,
    "elegoo_pla_silkplabronze_1000_175_p": null
  },
  "bed_temp_range": {
    "elegoo_pla_silkbronze_1000_175_p": null,
    "elegoo_pla_silkplabronze_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "elegoo_pla_silkbronze_1000_175_p": "glossy",
    "elegoo_pla_silkplabronze_1000_175_p": null
  }
}
```

### EL079: dup-7a6589e54eb69311bc90430756c68ab2d5ed3b8ab0c871a473d0a196dbe90cdd

Status: APPROVED; survivor `elegoo_pla_silkcoralpink_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_silkcoralpink_1000_175_p`|`Silk {color_name}`|`Coral Pink`|{"source_file": "elegoo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / True|
|`elegoo_pla_silkplacoralpink_1000_175_p`|`Silk PLA {color_name}`|`Coral Pink`|{"source_file": "elegoo.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_silkcoralpink_1000_175_p": 1.25,
    "elegoo_pla_silkplacoralpink_1000_175_p": 1.24
  },
  "color_hex": {
    "elegoo_pla_silkcoralpink_1000_175_p": "f4717d",
    "elegoo_pla_silkplacoralpink_1000_175_p": "FC8397"
  },
  "extruder_temp": {
    "elegoo_pla_silkcoralpink_1000_175_p": 220,
    "elegoo_pla_silkplacoralpink_1000_175_p": null
  },
  "extruder_temp_range": {
    "elegoo_pla_silkcoralpink_1000_175_p": null,
    "elegoo_pla_silkplacoralpink_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_silkcoralpink_1000_175_p": 60,
    "elegoo_pla_silkplacoralpink_1000_175_p": null
  },
  "bed_temp_range": {
    "elegoo_pla_silkcoralpink_1000_175_p": null,
    "elegoo_pla_silkplacoralpink_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "elegoo_pla_silkcoralpink_1000_175_p": "glossy",
    "elegoo_pla_silkplacoralpink_1000_175_p": null
  }
}
```

### EL080: dup-00753c5c84382b5e8a5beec6152b922be78468940ed4043e2c61f7eb5ab13471

Status: APPROVED; survivor `elegoo_pla_silkgold_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_silkgold_1000_175_p`|`Silk {color_name}`|`Gold`|{"source_file": "elegoo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / True|
|`elegoo_pla_silkplagold_1000_175_p`|`Silk PLA {color_name}`|`Gold`|{"source_file": "elegoo.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_silkgold_1000_175_p": 1.25,
    "elegoo_pla_silkplagold_1000_175_p": 1.24
  },
  "color_hex": {
    "elegoo_pla_silkgold_1000_175_p": "ffd10e",
    "elegoo_pla_silkplagold_1000_175_p": "F6C500"
  },
  "extruder_temp": {
    "elegoo_pla_silkgold_1000_175_p": 220,
    "elegoo_pla_silkplagold_1000_175_p": null
  },
  "extruder_temp_range": {
    "elegoo_pla_silkgold_1000_175_p": null,
    "elegoo_pla_silkplagold_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_silkgold_1000_175_p": 60,
    "elegoo_pla_silkplagold_1000_175_p": null
  },
  "bed_temp_range": {
    "elegoo_pla_silkgold_1000_175_p": null,
    "elegoo_pla_silkplagold_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "elegoo_pla_silkgold_1000_175_p": "glossy",
    "elegoo_pla_silkplagold_1000_175_p": null
  }
}
```

### EL081: dup-26ae819834283eac6dcbd4530d88e509ffb957d7b5e626ee5a2907eed7cb3700

Status: APPROVED; survivor `elegoo_pla_silkgreenred_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_silkgreenred_1000_175_p`|`Silk {color_name}`|`Green Red`|{"source_file": "elegoo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / True|
|`elegoo_pla_silkplagreenred_1000_175_p`|`Silk PLA {color_name}`|`Green Red`|{"source_file": "elegoo.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_silkgreenred_1000_175_p": 1.25,
    "elegoo_pla_silkplagreenred_1000_175_p": 1.24
  },
  "color_hex": {
    "elegoo_pla_silkgreenred_1000_175_p": null,
    "elegoo_pla_silkplagreenred_1000_175_p": "3D9441"
  },
  "color_hexes": {
    "elegoo_pla_silkgreenred_1000_175_p": [
      "E76099",
      "5CBC82"
    ],
    "elegoo_pla_silkplagreenred_1000_175_p": null
  },
  "extruder_temp": {
    "elegoo_pla_silkgreenred_1000_175_p": 220,
    "elegoo_pla_silkplagreenred_1000_175_p": null
  },
  "extruder_temp_range": {
    "elegoo_pla_silkgreenred_1000_175_p": null,
    "elegoo_pla_silkplagreenred_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_silkgreenred_1000_175_p": 60,
    "elegoo_pla_silkplagreenred_1000_175_p": null
  },
  "bed_temp_range": {
    "elegoo_pla_silkgreenred_1000_175_p": null,
    "elegoo_pla_silkplagreenred_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "elegoo_pla_silkgreenred_1000_175_p": "glossy",
    "elegoo_pla_silkplagreenred_1000_175_p": null
  },
  "multi_color_direction": {
    "elegoo_pla_silkgreenred_1000_175_p": "coaxial",
    "elegoo_pla_silkplagreenred_1000_175_p": null
  }
}
```

### EL082: dup-6c8a61e98a92eb1f26485b42bd9a9c53a5c89951a71d2b5bb0f0a9096fa92faf

Status: APPROVED; survivor `elegoo_pla_silkhollygreen_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_silkhollygreen_1000_175_p`|`Silk {color_name}`|`Holly Green`|{"source_file": "elegoo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / True|
|`elegoo_pla_silkplahollygreen_1000_175_p`|`Silk PLA {color_name}`|`Holly Green`|{"source_file": "elegoo.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_silkhollygreen_1000_175_p": 1.25,
    "elegoo_pla_silkplahollygreen_1000_175_p": 1.24
  },
  "color_hex": {
    "elegoo_pla_silkhollygreen_1000_175_p": "408E67",
    "elegoo_pla_silkplahollygreen_1000_175_p": "1D7C6A"
  },
  "extruder_temp": {
    "elegoo_pla_silkhollygreen_1000_175_p": 220,
    "elegoo_pla_silkplahollygreen_1000_175_p": null
  },
  "extruder_temp_range": {
    "elegoo_pla_silkhollygreen_1000_175_p": null,
    "elegoo_pla_silkplahollygreen_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_silkhollygreen_1000_175_p": 60,
    "elegoo_pla_silkplahollygreen_1000_175_p": null
  },
  "bed_temp_range": {
    "elegoo_pla_silkhollygreen_1000_175_p": null,
    "elegoo_pla_silkplahollygreen_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "elegoo_pla_silkhollygreen_1000_175_p": "glossy",
    "elegoo_pla_silkplahollygreen_1000_175_p": null
  }
}
```

### EL083: dup-359a9b4155f2956dd28e418b9b1ba89b442f25c6e8861ac93555c9fd3955d041

Status: APPROVED; survivor `elegoo_pla_silkmintgreen_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_silkmintgreen_1000_175_p`|`Silk {color_name}`|`Mint Green`|{"source_file": "elegoo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / True|
|`elegoo_pla_silkplamintgreen_1000_175_p`|`Silk PLA {color_name}`|`Mint Green`|{"source_file": "elegoo.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_silkmintgreen_1000_175_p": 1.25,
    "elegoo_pla_silkplamintgreen_1000_175_p": 1.24
  },
  "color_hex": {
    "elegoo_pla_silkmintgreen_1000_175_p": "53d8d4",
    "elegoo_pla_silkplamintgreen_1000_175_p": "9AE0DD"
  },
  "extruder_temp": {
    "elegoo_pla_silkmintgreen_1000_175_p": 220,
    "elegoo_pla_silkplamintgreen_1000_175_p": null
  },
  "extruder_temp_range": {
    "elegoo_pla_silkmintgreen_1000_175_p": null,
    "elegoo_pla_silkplamintgreen_1000_175_p": [
      190,
      230
    ]
  },
  "bed_temp": {
    "elegoo_pla_silkmintgreen_1000_175_p": 60,
    "elegoo_pla_silkplamintgreen_1000_175_p": null
  },
  "bed_temp_range": {
    "elegoo_pla_silkmintgreen_1000_175_p": null,
    "elegoo_pla_silkplamintgreen_1000_175_p": [
      50,
      70
    ]
  },
  "finish": {
    "elegoo_pla_silkmintgreen_1000_175_p": "glossy",
    "elegoo_pla_silkplamintgreen_1000_175_p": null
  }
}
```

### EL084: dup-707700aa5d925a076f6a313f7ccbc1c554d166071f50f661ea21a7c18ef7ab32

Status: APPROVED; survivor `elegoo_pla_silkred_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_silkplared_1000_175_p`|`Silk PLA {color_name}`|`Red`|{"source_file": "elegoo.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`elegoo_pla_silkred_1000_175_p`|`Silk {color_name}`|`Red`|{"source_file": "elegoo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_silkplared_1000_175_p": 1.24,
    "elegoo_pla_silkred_1000_175_p": 1.25
  },
  "color_hex": {
    "elegoo_pla_silkplared_1000_175_p": "F2BBBE",
    "elegoo_pla_silkred_1000_175_p": "ED646B"
  },
  "extruder_temp": {
    "elegoo_pla_silkplared_1000_175_p": null,
    "elegoo_pla_silkred_1000_175_p": 220
  },
  "extruder_temp_range": {
    "elegoo_pla_silkplared_1000_175_p": [
      190,
      230
    ],
    "elegoo_pla_silkred_1000_175_p": null
  },
  "bed_temp": {
    "elegoo_pla_silkplared_1000_175_p": null,
    "elegoo_pla_silkred_1000_175_p": 60
  },
  "bed_temp_range": {
    "elegoo_pla_silkplared_1000_175_p": [
      50,
      70
    ],
    "elegoo_pla_silkred_1000_175_p": null
  },
  "finish": {
    "elegoo_pla_silkplared_1000_175_p": null,
    "elegoo_pla_silkred_1000_175_p": "glossy"
  }
}
```

### EL085: dup-552bdc7986727bcef0da762afcdf997ab9aa9eb29c0abc232b64aadc18dc87d5

Status: APPROVED; survivor `elegoo_pla_silksilver_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_silkplasilver_1000_175_p`|`Silk PLA {color_name}`|`Silver`|{"source_file": "elegoo.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`elegoo_pla_silksilver_1000_175_p`|`Silk {color_name}`|`Silver`|{"source_file": "elegoo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_silkplasilver_1000_175_p": 1.24,
    "elegoo_pla_silksilver_1000_175_p": 1.25
  },
  "color_hex": {
    "elegoo_pla_silkplasilver_1000_175_p": "C9D0D4",
    "elegoo_pla_silksilver_1000_175_p": "dbdde2"
  },
  "extruder_temp": {
    "elegoo_pla_silkplasilver_1000_175_p": null,
    "elegoo_pla_silksilver_1000_175_p": 220
  },
  "extruder_temp_range": {
    "elegoo_pla_silkplasilver_1000_175_p": [
      190,
      230
    ],
    "elegoo_pla_silksilver_1000_175_p": null
  },
  "bed_temp": {
    "elegoo_pla_silkplasilver_1000_175_p": null,
    "elegoo_pla_silksilver_1000_175_p": 60
  },
  "bed_temp_range": {
    "elegoo_pla_silkplasilver_1000_175_p": [
      50,
      70
    ],
    "elegoo_pla_silksilver_1000_175_p": null
  },
  "finish": {
    "elegoo_pla_silkplasilver_1000_175_p": null,
    "elegoo_pla_silksilver_1000_175_p": "glossy"
  }
}
```

### EL086: dup-82b27713ac98e34b52b7b66a0007e2f646bdf7c762d7b308bf2a16a397c9b156

Status: APPROVED; survivor `elegoo_pla_silkwhite_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`elegoo_pla_silkplawhite_1000_175_p`|`Silk PLA {color_name}`|`White`|{"source_file": "elegoo.json", "definition_index": 26, "weights": 1, "diameters": 1, "colors": 18, "compiled_records": 18} / False|
|`elegoo_pla_silkwhite_1000_175_p`|`Silk {color_name}`|`White`|{"source_file": "elegoo.json", "definition_index": 3, "weights": 1, "diameters": 1, "colors": 15, "compiled_records": 15} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "elegoo_pla_silkplawhite_1000_175_p": 1.24,
    "elegoo_pla_silkwhite_1000_175_p": 1.25
  },
  "color_hex": {
    "elegoo_pla_silkplawhite_1000_175_p": "FFFFFF",
    "elegoo_pla_silkwhite_1000_175_p": "ffffff"
  },
  "extruder_temp": {
    "elegoo_pla_silkplawhite_1000_175_p": null,
    "elegoo_pla_silkwhite_1000_175_p": 220
  },
  "extruder_temp_range": {
    "elegoo_pla_silkplawhite_1000_175_p": [
      190,
      230
    ],
    "elegoo_pla_silkwhite_1000_175_p": null
  },
  "bed_temp": {
    "elegoo_pla_silkplawhite_1000_175_p": null,
    "elegoo_pla_silkwhite_1000_175_p": 60
  },
  "bed_temp_range": {
    "elegoo_pla_silkplawhite_1000_175_p": [
      50,
      70
    ],
    "elegoo_pla_silkwhite_1000_175_p": null
  },
  "finish": {
    "elegoo_pla_silkplawhite_1000_175_p": null,
    "elegoo_pla_silkwhite_1000_175_p": "glossy"
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "elegoo_pla_skyblue_1000_175_c",
      "values": {
        "density": 1.2,
        "extruder_temp": 205,
        "extruder_temp_range": [
          190,
          220
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_mattesunshineyellow_1000_175_c",
      "values": {
        "density": 1.31,
        "extruder_temp": 220,
        "extruder_temp_range": [
          190,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ],
        "codes": [
          "SPUK-EL-MAT-106"
        ]
      },
      "source": "https://www.elegoo.com/products/pla-matte-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "field_sources": {
        "codes": "8317ee58093af0347cf299ec7f02f092c1cc422e"
      }
    },
    {
      "id": "elegoo_pla_translucent_1000_175_c",
      "values": {
        "density": 1.2,
        "extruder_temp": 205,
        "extruder_temp_range": [
          190,
          220
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_yellow_1000_175_c",
      "values": {
        "density": 1.2,
        "extruder_temp": 205,
        "extruder_temp_range": [
          190,
          220
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_matteslategrey_1000_175_c",
      "values": {
        "density": 1.31,
        "extruder_temp": 220,
        "extruder_temp_range": [
          190,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ],
        "codes": [
          "SPUK-EL-MAT-107"
        ]
      },
      "source": "https://www.elegoo.com/products/pla-matte-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "field_sources": {
        "codes": "8317ee58093af0347cf299ec7f02f092c1cc422e"
      }
    },
    {
      "id": "elegoo_pla_red_1000_175_c",
      "values": {
        "density": 1.2,
        "extruder_temp": 205,
        "extruder_temp_range": [
          190,
          220
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_darkblue_1000_175_c",
      "values": {
        "density": 1.2,
        "extruder_temp": 205,
        "extruder_temp_range": [
          190,
          220
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_mattenavyblue_1000_175_c",
      "values": {
        "density": 1.31,
        "extruder_temp": 220,
        "extruder_temp_range": [
          190,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ],
        "codes": [
          "SPUK-EL-MAT-104"
        ]
      },
      "source": "https://www.elegoo.com/products/pla-matte-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "field_sources": {
        "codes": "8317ee58093af0347cf299ec7f02f092c1cc422e"
      }
    },
    {
      "id": "elegoo_pla_mattelavenderpurple_1000_175_c",
      "values": {
        "density": 1.31,
        "extruder_temp": 220,
        "extruder_temp_range": [
          190,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ],
        "codes": [
          "SPUK-EL-MAT-108"
        ]
      },
      "source": "https://www.elegoo.com/products/pla-matte-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "field_sources": {
        "codes": "8317ee58093af0347cf299ec7f02f092c1cc422e"
      }
    },
    {
      "id": "elegoo_pla_grey_1000_175_c",
      "values": {
        "density": 1.2,
        "extruder_temp": 205,
        "extruder_temp_range": [
          190,
          220
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_pink_1000_175_c",
      "values": {
        "density": 1.2,
        "extruder_temp": 205,
        "extruder_temp_range": [
          190,
          220
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_woodfilled_1000_175_c",
      "values": {
        "density": 1.21,
        "extruder_temp": null,
        "extruder_temp_range": [
          200,
          240
        ],
        "bed_temp": null,
        "bed_temp_range": [
          35,
          65
        ]
      },
      "source": "https://www.elegoo.com/en-gb/collections/materials/products/pla-wood",
      "lot": "Current official PLA Wood exact product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "physical_product_line": "PLA Wood",
      "source_color_binding": "Wood Filled = current official Wood filled option"
    },
    {
      "id": "elegoo_asa_white_1000_175_c",
      "values": {
        "density": 1.1,
        "extruder_temp": null,
        "extruder_temp_range": [
          240,
          270
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          100
        ]
      },
      "source": "https://www.elegoo.com/products/asa-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.09,
        "extruder_temp": 265,
        "extruder_temp_range": null,
        "bed_temp": 95,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_mattetealgreen_1000_175_c",
      "values": {
        "density": 1.31,
        "extruder_temp": 220,
        "extruder_temp_range": [
          190,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ],
        "codes": [
          "SPUK-EL-MAT-105"
        ]
      },
      "source": "https://www.elegoo.com/products/pla-matte-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "field_sources": {
        "codes": "8317ee58093af0347cf299ec7f02f092c1cc422e"
      }
    },
    {
      "id": "elegoo_pla_white_1000_175_c",
      "values": {
        "density": 1.2,
        "extruder_temp": 205,
        "extruder_temp_range": [
          190,
          220
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_beige_1000_175_c",
      "values": {
        "density": 1.2,
        "extruder_temp": 205,
        "extruder_temp_range": [
          190,
          220
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_matterubyred_1000_175_c",
      "values": {
        "density": 1.31,
        "extruder_temp": 220,
        "extruder_temp_range": [
          190,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ],
        "codes": [
          "SPUK-EL-MAT-103"
        ]
      },
      "source": "https://www.elegoo.com/products/pla-matte-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "field_sources": {
        "codes": "8317ee58093af0347cf299ec7f02f092c1cc422e"
      }
    },
    {
      "id": "elegoo_pla_orange_1000_175_c",
      "values": {
        "density": 1.2,
        "extruder_temp": 205,
        "extruder_temp_range": [
          190,
          220
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_purple_1000_175_c",
      "values": {
        "density": 1.2,
        "extruder_temp": 205,
        "extruder_temp_range": [
          190,
          220
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_mattesakurapink_1000_175_c",
      "values": {
        "density": 1.31,
        "extruder_temp": 220,
        "extruder_temp_range": [
          190,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ],
        "codes": [
          "SPUK-EL-MAT-109"
        ]
      },
      "source": "https://www.elegoo.com/products/pla-matte-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "field_sources": {
        "codes": "8317ee58093af0347cf299ec7f02f092c1cc422e"
      }
    },
    {
      "id": "elegoo_pla_matteiceblue_1000_175_c",
      "values": {
        "density": 1.31,
        "extruder_temp": 220,
        "extruder_temp_range": [
          190,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ],
        "codes": [
          "SPUK-EL-MAT-110"
        ]
      },
      "source": "https://www.elegoo.com/products/pla-matte-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "field_sources": {
        "codes": "8317ee58093af0347cf299ec7f02f092c1cc422e"
      }
    },
    {
      "id": "elegoo_pla_mattebeige_1000_175_c",
      "values": {
        "density": 1.31,
        "extruder_temp": 220,
        "extruder_temp_range": [
          190,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ],
        "codes": [
          "SPUK-EL-MAT-111"
        ]
      },
      "source": "https://www.elegoo.com/products/pla-matte-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "field_sources": {
        "codes": "8317ee58093af0347cf299ec7f02f092c1cc422e"
      }
    },
    {
      "id": "elegoo_pla_woodcolor_1000_175_c",
      "values": {
        "density": 1.2,
        "extruder_temp": 205,
        "extruder_temp_range": [
          190,
          220
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_seagreen_1000_175_c",
      "values": {
        "density": 1.2,
        "extruder_temp": 205,
        "extruder_temp_range": [
          190,
          220
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_spacegrey_1000_175_c",
      "values": {
        "density": 1.2,
        "extruder_temp": 205,
        "extruder_temp_range": [
          190,
          220
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_black_1000_175_c",
      "values": {
        "density": 1.2,
        "extruder_temp": 205,
        "extruder_temp_range": [
          190,
          220
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_asa_black_1000_175_c",
      "values": {
        "density": 1.1,
        "extruder_temp": null,
        "extruder_temp_range": [
          240,
          270
        ],
        "bed_temp": null,
        "bed_temp_range": [
          90,
          100
        ]
      },
      "source": "https://www.elegoo.com/products/asa-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.09,
        "extruder_temp": 265,
        "extruder_temp_range": null,
        "bed_temp": 95,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_brown_1000_175_c",
      "values": {
        "density": 1.2,
        "extruder_temp": 205,
        "extruder_temp_range": [
          190,
          220
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_neongreen_1000_175_c",
      "values": {
        "density": 1.2,
        "extruder_temp": 205,
        "extruder_temp_range": [
          190,
          220
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_mattemintgreen_1000_175_c",
      "values": {
        "density": 1.31,
        "extruder_temp": 220,
        "extruder_temp_range": [
          190,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ],
        "codes": [
          "SPUK-EL-MAT-112"
        ]
      },
      "source": "https://www.elegoo.com/products/pla-matte-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      },
      "field_sources": {
        "codes": "8317ee58093af0347cf299ec7f02f092c1cc422e"
      }
    },
    {
      "id": "elegoo_pla_matteblack_1000_175_c",
      "values": {
        "density": 1.31,
        "extruder_temp": 220,
        "extruder_temp_range": [
          190,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-matte-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    },
    {
      "id": "elegoo_pla_mattewhite_1000_175_c",
      "values": {
        "density": 1.31,
        "extruder_temp": 220,
        "extruder_temp_range": [
          190,
          230
        ],
        "bed_temp": null,
        "bed_temp_range": [
          50,
          65
        ]
      },
      "source": "https://www.elegoo.com/products/pla-matte-filament-1-75mm-colored-1kg",
      "lot": "Current official product-line page retrieved2026-10-03; no lot/packaging claim",
      "same_variant": true,
      "approved": true,
      "old_values": {
        "density": 1.26,
        "extruder_temp": 210,
        "extruder_temp_range": null,
        "bed_temp": 60,
        "bed_temp_range": null
      }
    }
  ],
  "transfers": [
    {
      "old_id": "elegoo_pla_plamattebeige_1000_175_c",
      "target_id": "elegoo_pla_mattebeige_1000_175_c",
      "field": "codes",
      "values": [
        "SPUK-EL-MAT-111"
      ],
      "source": "8317ee58093af0347cf299ec7f02f092c1cc422e"
    },
    {
      "old_id": "elegoo_pla_plamatteiceblue_1000_175_c",
      "target_id": "elegoo_pla_matteiceblue_1000_175_c",
      "field": "codes",
      "values": [
        "SPUK-EL-MAT-110"
      ],
      "source": "8317ee58093af0347cf299ec7f02f092c1cc422e"
    },
    {
      "old_id": "elegoo_pla_plamattelavenderpurple_1000_175_c",
      "target_id": "elegoo_pla_mattelavenderpurple_1000_175_c",
      "field": "codes",
      "values": [
        "SPUK-EL-MAT-108"
      ],
      "source": "8317ee58093af0347cf299ec7f02f092c1cc422e"
    },
    {
      "old_id": "elegoo_pla_plamattemintgreen_1000_175_c",
      "target_id": "elegoo_pla_mattemintgreen_1000_175_c",
      "field": "codes",
      "values": [
        "SPUK-EL-MAT-112"
      ],
      "source": "8317ee58093af0347cf299ec7f02f092c1cc422e"
    },
    {
      "old_id": "elegoo_pla_plamattenavyblue_1000_175_c",
      "target_id": "elegoo_pla_mattenavyblue_1000_175_c",
      "field": "codes",
      "values": [
        "SPUK-EL-MAT-104"
      ],
      "source": "8317ee58093af0347cf299ec7f02f092c1cc422e"
    },
    {
      "old_id": "elegoo_pla_plamatterubyred_1000_175_c",
      "target_id": "elegoo_pla_matterubyred_1000_175_c",
      "field": "codes",
      "values": [
        "SPUK-EL-MAT-103"
      ],
      "source": "8317ee58093af0347cf299ec7f02f092c1cc422e"
    },
    {
      "old_id": "elegoo_pla_plamattesakurapink_1000_175_c",
      "target_id": "elegoo_pla_mattesakurapink_1000_175_c",
      "field": "codes",
      "values": [
        "SPUK-EL-MAT-109"
      ],
      "source": "8317ee58093af0347cf299ec7f02f092c1cc422e"
    },
    {
      "old_id": "elegoo_pla_plamatteslategrey_1000_175_c",
      "target_id": "elegoo_pla_matteslategrey_1000_175_c",
      "field": "codes",
      "values": [
        "SPUK-EL-MAT-107"
      ],
      "source": "8317ee58093af0347cf299ec7f02f092c1cc422e"
    },
    {
      "old_id": "elegoo_pla_plamattesunshineyellow_1000_175_c",
      "target_id": "elegoo_pla_mattesunshineyellow_1000_175_c",
      "field": "codes",
      "values": [
        "SPUK-EL-MAT-106"
      ],
      "source": "8317ee58093af0347cf299ec7f02f092c1cc422e"
    },
    {
      "old_id": "elegoo_pla_plamattetealgreen_1000_175_c",
      "target_id": "elegoo_pla_mattetealgreen_1000_175_c",
      "field": "codes",
      "values": [
        "SPUK-EL-MAT-105"
      ],
      "source": "8317ee58093af0347cf299ec7f02f092c1cc422e"
    }
  ]
}
```

## Preserved out-of-scope IDs

- `elegoo_petg_rapidpetgsilver_1000_175_c` — RAPID PETG Silver
- `elegoo_petg_petgproblack_1000_175_c` — PETG PRO Black
- `elegoo_petg_petgprowhite_1000_175_c` — PETG PRO White
- `elegoo_petg_petgprogrey_1000_175_c` — PETG PRO Grey
- `elegoo_petg_petgprosilver_1000_175_c` — PETG PRO Silver
- `elegoo_petg_petgpropink_1000_175_c` — PETG PRO Pink
- `elegoo_petg_petgprored_1000_175_c` — PETG PRO Red
- `elegoo_petg_petgproolivegreen_1000_175_c` — PETG PRO Olive Green
- `elegoo_petg_petgproblue_1000_175_c` — PETG PRO Blue
- `elegoo_petg_petgproburgundyred_1000_175_c` — PETG PRO Burgundy Red
- `elegoo_petg_petgprolightblue_1000_175_c` — PETG PRO Light Blue
- `elegoo_petg_petgprogreen_1000_175_c` — PETG PRO Green
- `elegoo_petg_petgproyellow_1000_175_c` — PETG PRO Yellow
- `elegoo_petg_petgpropurple_1000_175_c` — PETG PRO Purple
- `elegoo_pla+_black_1000_175_c` — Black
- `elegoo_pla+_white_1000_175_c` — White
- `elegoo_pla+_grey_1000_175_c` — Grey
- `elegoo_pla+_blue_1000_175_c` — Blue
- `elegoo_pla+_red_1000_175_c` — Red
- `elegoo_pla+_orange_1000_175_c` — Orange
- `elegoo_pla+_yellow_1000_175_c` — Yellow
- `elegoo_pla+_skyblue_1000_175_c` — Sky Blue
- `elegoo_pla+_spacegrey_1000_175_c` — Space Grey
- `elegoo_pla+_purple_1000_175_c` — Purple
- `elegoo_pla+_seagreen_1000_175_c` — Sea Green
- `elegoo_pla+_woodcolor_1000_175_c` — Wood Color
- `elegoo_pla+_brown_1000_175_c` — Brown
- `elegoo_pla+_rapidpla+black_1000_175_c` — RAPID PLA+ Black
- `elegoo_pla+_rapidpla+white_1000_175_c` — RAPID PLA+ White
- `elegoo_pla+_rapidpla+grey_1000_175_c` — RAPID PLA+ Grey
- `elegoo_pla+_rapidpla+green_1000_175_c` — RAPID PLA+ Green
- `elegoo_pla+_rapidpla+blue_1000_175_c` — RAPID PLA+ Blue
- `elegoo_pla+_rapidpla+red_1000_175_c` — RAPID PLA+ Red
- `elegoo_pla+_rapidpla+yellow_1000_175_c` — RAPID PLA+ Yellow
- `elegoo_pla+_rapidpla+orange_1000_175_c` — RAPID PLA+ Orange
- `elegoo_pla+_rapidpla+silver_1000_175_c` — RAPID PLA+ Silver
- `elegoo_pla+_rapidpla+brown_1000_175_c` — RAPID PLA+ Brown
- `elegoo_pla+_rapidpla+beige_1000_175_c` — RAPID PLA+ Beige
- `elegoo_pla+_rapidpla+black_1000_175_r` — RAPID PLA+ Black
- `elegoo_pla+_rapidpla+white_1000_175_r` — RAPID PLA+ White
- `elegoo_pla+_rapidpla+grey_1000_175_r` — RAPID PLA+ Grey
- `elegoo_pla+_rapidpla+green_1000_175_r` — RAPID PLA+ Green
- `elegoo_pla+_rapidpla+blue_1000_175_r` — RAPID PLA+ Blue
- `elegoo_pla+_rapidpla+red_1000_175_r` — RAPID PLA+ Red
- `elegoo_pla+_rapidpla+yellow_1000_175_r` — RAPID PLA+ Yellow
- `elegoo_pla+_rapidpla+orange_1000_175_r` — RAPID PLA+ Orange
- `elegoo_pla+_rapidpla+silver_1000_175_r` — RAPID PLA+ Silver
- `elegoo_pla+_rapidpla+brown_1000_175_r` — RAPID PLA+ Brown
- `elegoo_pla+_rapidpla+beige_1000_175_r` — RAPID PLA+ Beige
- `elegoo_tpu-95a_black_1000_175_p` — Black
- `elegoo_tpu-95a_white_1000_175_p` — White
- `elegoo_tpu-95a_grey_1000_175_p` — Grey
- `elegoo_tpu-95a_blue_1000_175_p` — Blue
- `elegoo_tpu-95a_red_1000_175_p` — Red
- `elegoo_tpu-95a_green_1000_175_p` — Green
- `elegoo_tpu-95a_translucent_1000_175_p` — Translucent
- `elegoo_abs_absblack_1000_175_c` — ABS Black
- `elegoo_abs_absblue_1000_175_c` — ABS Blue
- `elegoo_abs_absgrey_1000_175_c` — ABS Grey
- `elegoo_abs_absorange_1000_175_c` — ABS Orange
- `elegoo_abs_absred_1000_175_c` — ABS Red
- `elegoo_abs_abswhite_1000_175_c` — ABS White
- `elegoo_asa_asablue_1000_175_c` — ASA Blue
- `elegoo_asa_asagreen_1000_175_c` — ASA Green
- `elegoo_asa_asagrey_1000_175_c` — ASA Grey
- `elegoo_asa_asared_1000_175_c` — ASA Red
- `elegoo_pa12_paht-cfblack_1000_175_c` — PAHT-CF Black
- `elegoo_pc_pcblack_1000_175_c` — PC Black
- `elegoo_pc_pcclearblack_1000_175_c` — PC Clear Black
- `elegoo_pc_pctranslucent_1000_175_c` — PC Translucent
- `elegoo_pc_pcwhite_1000_175_c` — PC White
- `elegoo_petg_petgblack_1000_175_c` — PETG Black
- `elegoo_petg_petgblue_1000_175_c` — PETG Blue
- `elegoo_petg_petggrey_1000_175_c` — PETG Grey
- `elegoo_petg_petgolivegreen_1000_175_c` — PETG Olive Green
- `elegoo_petg_petgpink_1000_175_c` — PETG Pink
- `elegoo_petg_petgred_1000_175_c` — PETG Red
- `elegoo_petg_petgsilver_1000_175_c` — PETG Silver
- `elegoo_petg_petgwhite_1000_175_c` — PETG White
- `elegoo_petg_petg-cfblack_1000_175_c` — PETG-CF Black
- `elegoo_petg_petg-cfgrey_1000_175_c` — PETG-CF Grey
- `elegoo_petg_petg-gfblack_1000_175_c` — PETG-GF Black
- `elegoo_petg_petg-gfgrey_1000_175_c` — PETG-GF Grey
- `elegoo_petg_petg-gfwhite_1000_175_c` — PETG-GF White
- `elegoo_pla_plaapplegreen_250_175_c` — PLA Apple Green
- `elegoo_pla_plabeige_250_175_c` — PLA Beige
- `elegoo_pla_plablack_250_175_c` — PLA Black
- `elegoo_pla_plablue_250_175_c` — PLA Blue
- `elegoo_pla_plabronzefilled_250_175_c` — PLA Bronze filled
- `elegoo_pla_plabrown_250_175_c` — PLA Brown
- `elegoo_pla_plaburgundyred_250_175_c` — PLA Burgundy Red
- `elegoo_pla_placlear_250_175_c` — PLA Clear
- `elegoo_pla_placobaltblue_250_175_c` — PLA Cobalt Blue
- `elegoo_pla_placocoabrown_250_175_c` — PLA Cocoa Brown
- `elegoo_pla_placyan_250_175_c` — PLA Cyan
- `elegoo_pla_pladarkblue_250_175_c` — PLA Dark Blue
- `elegoo_pla_plagalaxyblack_250_175_c` — PLA Galaxy Black
- `elegoo_pla_plagalaxypeacockblue_250_175_c` — PLA Galaxy Peacock Blue
- `elegoo_pla_plagalaxypurple_250_175_c` — PLA Galaxy Purple
- `elegoo_pla_plagreen_250_175_c` — PLA Green
- `elegoo_pla_plagrey_250_175_c` — PLA Grey
- `elegoo_pla_plahotpink_250_175_c` — PLA Hot Pink
- `elegoo_pla_plalightblue_250_175_c` — PLA Light Blue
- `elegoo_pla_plamarble_250_175_c` — PLA Marble
- `elegoo_pla_plamarblebrickred_250_175_c` — PLA Marble Brick Red
- `elegoo_pla_plamarblecementgrey_250_175_c` — PLA Marble Cement Grey
- `elegoo_pla_planeongreen_250_175_c` — PLA Neon Green
- `elegoo_pla_plaorange_250_175_c` — PLA Orange
- `elegoo_pla_plapink_250_175_c` — PLA Pink
- `elegoo_pla_plapurple_250_175_c` — PLA Purple
- `elegoo_pla_plared_250_175_c` — PLA Red
- `elegoo_pla_plaseagreen_250_175_c` — PLA Sea Green
- `elegoo_pla_plasilver_250_175_c` — PLA Silver
- `elegoo_pla_plaskyblue_250_175_c` — PLA Sky Blue
- `elegoo_pla_plaspacegrey_250_175_c` — PLA Space Grey
- `elegoo_pla_plasunfloweryellow_250_175_c` — PLA Sunflower Yellow
- `elegoo_pla_platranslucent_250_175_c` — PLA Translucent
- `elegoo_pla_platurquoisegreen_250_175_c` — PLA Turquoise Green
- `elegoo_pla_plawhite_250_175_c` — PLA White
- `elegoo_pla_plawoodcolor_250_175_c` — PLA Wood Color
- `elegoo_pla_plawoodfilled_250_175_c` — PLA Wood filled
- `elegoo_pla_playellow_250_175_c` — PLA Yellow
- `elegoo_pla_plaapplegreen_1000_175_c` — PLA Apple Green
- `elegoo_pla_plablue_1000_175_c` — PLA Blue
- `elegoo_pla_plaburgundyred_1000_175_c` — PLA Burgundy Red
- `elegoo_pla_placlear_1000_175_c` — PLA Clear
- `elegoo_pla_placobaltblue_1000_175_c` — PLA Cobalt Blue
- `elegoo_pla_placocoabrown_1000_175_c` — PLA Cocoa Brown
- `elegoo_pla_placyan_1000_175_c` — PLA Cyan
- `elegoo_pla_plagreen_1000_175_c` — PLA Green
- `elegoo_pla_plahotpink_1000_175_c` — PLA Hot Pink
- `elegoo_pla_plalightblue_1000_175_c` — PLA Light Blue
- `elegoo_pla_plamarblebrickred_1000_175_c` — PLA Marble Brick Red
- `elegoo_pla_plamarblecementgrey_1000_175_c` — PLA Marble Cement Grey
- `elegoo_pla_plasilver_1000_175_c` — PLA Silver
- `elegoo_pla_plasunfloweryellow_1000_175_c` — PLA Sunflower Yellow
- `elegoo_pla_platurquoisegreen_1000_175_c` — PLA Turquoise Green
- `elegoo_pla_plaapplegreen_3000_175_c` — PLA Apple Green
- `elegoo_pla_plabeige_3000_175_c` — PLA Beige
- `elegoo_pla_plablack_3000_175_c` — PLA Black
- `elegoo_pla_plablue_3000_175_c` — PLA Blue
- `elegoo_pla_plabronzefilled_3000_175_c` — PLA Bronze filled
- `elegoo_pla_plabrown_3000_175_c` — PLA Brown
- `elegoo_pla_plaburgundyred_3000_175_c` — PLA Burgundy Red
- `elegoo_pla_placlear_3000_175_c` — PLA Clear
- `elegoo_pla_placobaltblue_3000_175_c` — PLA Cobalt Blue
- `elegoo_pla_placocoabrown_3000_175_c` — PLA Cocoa Brown
- `elegoo_pla_placyan_3000_175_c` — PLA Cyan
- `elegoo_pla_pladarkblue_3000_175_c` — PLA Dark Blue
- `elegoo_pla_plagalaxyblack_3000_175_c` — PLA Galaxy Black
- `elegoo_pla_plagalaxypeacockblue_3000_175_c` — PLA Galaxy Peacock Blue
- `elegoo_pla_plagalaxypurple_3000_175_c` — PLA Galaxy Purple
- `elegoo_pla_plagreen_3000_175_c` — PLA Green
- `elegoo_pla_plagrey_3000_175_c` — PLA Grey
- `elegoo_pla_plahotpink_3000_175_c` — PLA Hot Pink
- `elegoo_pla_plalightblue_3000_175_c` — PLA Light Blue
- `elegoo_pla_plamarble_3000_175_c` — PLA Marble
- `elegoo_pla_plamarblebrickred_3000_175_c` — PLA Marble Brick Red
- `elegoo_pla_plamarblecementgrey_3000_175_c` — PLA Marble Cement Grey
- `elegoo_pla_planeongreen_3000_175_c` — PLA Neon Green
- `elegoo_pla_plaorange_3000_175_c` — PLA Orange
- `elegoo_pla_plapink_3000_175_c` — PLA Pink
- `elegoo_pla_plapurple_3000_175_c` — PLA Purple
- `elegoo_pla_plarapidplusbeige_3000_175_c` — PLA RAPID Plus Beige
- `elegoo_pla_plarapidplusblack_3000_175_c` — PLA RAPID Plus Black
- `elegoo_pla_plarapidplusblue_3000_175_c` — PLA RAPID Plus Blue
- `elegoo_pla_plarapidplusbrown_3000_175_c` — PLA RAPID Plus Brown
- `elegoo_pla_plarapidplusgreen_3000_175_c` — PLA RAPID Plus Green
- `elegoo_pla_plarapidplusgrey_3000_175_c` — PLA RAPID Plus Grey
- `elegoo_pla_plarapidplusorange_3000_175_c` — PLA RAPID Plus Orange
- `elegoo_pla_plarapidplusred_3000_175_c` — PLA RAPID Plus Red
- `elegoo_pla_plarapidplussilver_3000_175_c` — PLA RAPID Plus Silver
- `elegoo_pla_plarapidpluswhite_3000_175_c` — PLA RAPID Plus White
- `elegoo_pla_plarapidplusyellow_3000_175_c` — PLA RAPID Plus Yellow
- `elegoo_pla_plared_3000_175_c` — PLA Red
- `elegoo_pla_plaseagreen_3000_175_c` — PLA Sea Green
- `elegoo_pla_plasilver_3000_175_c` — PLA Silver
- `elegoo_pla_plaskyblue_3000_175_c` — PLA Sky Blue
- `elegoo_pla_plaspacegrey_3000_175_c` — PLA Space Grey
- `elegoo_pla_plasunfloweryellow_3000_175_c` — PLA Sunflower Yellow
- `elegoo_pla_platranslucent_3000_175_c` — PLA Translucent
- `elegoo_pla_platurquoisegreen_3000_175_c` — PLA Turquoise Green
- `elegoo_pla_plawhite_3000_175_c` — PLA White
- `elegoo_pla_plawoodcolor_3000_175_c` — PLA Wood Color
- `elegoo_pla_plawoodfilled_3000_175_c` — PLA Wood filled
- `elegoo_pla_playellow_3000_175_c` — PLA Yellow
- `elegoo_pla_plabasicmistyblue_1000_175_c` — PLA Basic Misty Blue
- `elegoo_pla_plabasicblack_1000_175_c` — PLA Basic Black
- `elegoo_pla_plabasicred_1000_175_c` — PLA Basic Red
- `elegoo_pla_plabasicblue_1000_175_c` — PLA Basic Blue
- `elegoo_pla_plabasicmistyblue_1000_175_r` — PLA Basic Misty Blue
- `elegoo_pla_plabasicblack_1000_175_r` — PLA Basic Black
- `elegoo_pla_plabasicred_1000_175_r` — PLA Basic Red
- `elegoo_pla_plabasicblue_1000_175_r` — PLA Basic Blue
- `elegoo_pla_pla-cfblack_1000_175_c` — PLA-CF Black
- `elegoo_pla_plamattebeige_250_175_c` — PLA MATTE Beige
- `elegoo_pla_plamatteblack_250_175_c` — PLA MATTE Black
- `elegoo_pla_plamattebrown_250_175_c` — PLA MATTE Brown
- `elegoo_pla_plamattedefault_250_175_c` — PLA MATTE Default
- `elegoo_pla_plamatteiceblue_250_175_c` — PLA MATTE Ice Blue
- `elegoo_pla_plamattelavenderpurple_250_175_c` — PLA MATTE Lavender Purple
- `elegoo_pla_plamattematteblack_250_175_c` — PLA MATTE Matte Black
- `elegoo_pla_plamattemattewhite_250_175_c` — PLA MATTE Matte White
- `elegoo_pla_plamattemintgreen_250_175_c` — PLA MATTE Mint Green
- `elegoo_pla_plamattenavyblue_250_175_c` — PLA MATTE Navy Blue
- `elegoo_pla_plamatteorange_250_175_c` — PLA MATTE Orange
- `elegoo_pla_plamatterubyred_250_175_c` — PLA MATTE Ruby Red
- `elegoo_pla_plamattesakurapink_250_175_c` — PLA MATTE Sakura Pink
- `elegoo_pla_plamatteslategrey_250_175_c` — PLA MATTE Slate Grey
- `elegoo_pla_plamattesunshineyellow_250_175_c` — PLA MATTE Sunshine Yellow
- `elegoo_pla_plamattetealgreen_250_175_c` — PLA MATTE Teal Green
- `elegoo_pla_plamattewhite_250_175_c` — PLA MATTE White
- `elegoo_pla_plamattebrown_1000_175_c` — PLA MATTE Brown
- `elegoo_pla_plamattedefault_1000_175_c` — PLA MATTE Default
- `elegoo_pla_plamattematteblack_1000_175_c` — PLA MATTE Matte Black
- `elegoo_pla_plamattemattewhite_1000_175_c` — PLA MATTE Matte White
- `elegoo_pla_plamatteorange_1000_175_c` — PLA MATTE Orange
- `elegoo_pla_plaplusbeige_250_175_c` — PLA Plus Beige
- `elegoo_pla_plaplusblack_250_175_c` — PLA Plus Black
- `elegoo_pla_plaplusbrown_250_175_c` — PLA Plus Brown
- `elegoo_pla_plaplusdarkblue_250_175_c` — PLA Plus Dark Blue
- `elegoo_pla_plaplusgrey_250_175_c` — PLA Plus Grey
- `elegoo_pla_plaplusneongreen_250_175_c` — PLA Plus Neon Green
- `elegoo_pla_plaplusorange_250_175_c` — PLA Plus Orange
- `elegoo_pla_plapluspink_250_175_c` — PLA Plus Pink
- `elegoo_pla_plapluspurple_250_175_c` — PLA Plus Purple
- `elegoo_pla_plaplusred_250_175_c` — PLA Plus Red
- `elegoo_pla_plaplusseagreen_250_175_c` — PLA Plus Sea Green
- `elegoo_pla_plaplusskyblue_250_175_c` — PLA Plus Sky Blue
- `elegoo_pla_plaplusspacegrey_250_175_c` — PLA Plus Space Grey
- `elegoo_pla_plaplustranslucent_250_175_c` — PLA Plus Translucent
- `elegoo_pla_plapluswhite_250_175_c` — PLA Plus White
- `elegoo_pla_plapluswoodcolor_250_175_c` — PLA Plus Wood Color
- `elegoo_pla_plaplusyellow_250_175_c` — PLA Plus Yellow
- `elegoo_pla_plaplusbeige_1000_175_c` — PLA Plus Beige
- `elegoo_pla_plaplusblack_1000_175_c` — PLA Plus Black
- `elegoo_pla_plaplusbrown_1000_175_c` — PLA Plus Brown
- `elegoo_pla_plaplusdarkblue_1000_175_c` — PLA Plus Dark Blue
- `elegoo_pla_plaplusgrey_1000_175_c` — PLA Plus Grey
- `elegoo_pla_plaplusneongreen_1000_175_c` — PLA Plus Neon Green
- `elegoo_pla_plaplusorange_1000_175_c` — PLA Plus Orange
- `elegoo_pla_plapluspink_1000_175_c` — PLA Plus Pink
- `elegoo_pla_plapluspurple_1000_175_c` — PLA Plus Purple
- `elegoo_pla_plaplusred_1000_175_c` — PLA Plus Red
- `elegoo_pla_plaplusseagreen_1000_175_c` — PLA Plus Sea Green
- `elegoo_pla_plaplusskyblue_1000_175_c` — PLA Plus Sky Blue
- `elegoo_pla_plaplusspacegrey_1000_175_c` — PLA Plus Space Grey
- `elegoo_pla_plaplustranslucent_1000_175_c` — PLA Plus Translucent
- `elegoo_pla_plapluswhite_1000_175_c` — PLA Plus White
- `elegoo_pla_plapluswoodcolor_1000_175_c` — PLA Plus Wood Color
- `elegoo_pla_plaplusyellow_1000_175_c` — PLA Plus Yellow
- `elegoo_pla_plaplusbeige_5000_175_c` — PLA Plus Beige
- `elegoo_pla_plaplusblack_5000_175_c` — PLA Plus Black
- `elegoo_pla_plaplusbrown_5000_175_c` — PLA Plus Brown
- `elegoo_pla_plaplusdarkblue_5000_175_c` — PLA Plus Dark Blue
- `elegoo_pla_plaplusgrey_5000_175_c` — PLA Plus Grey
- `elegoo_pla_plaplusneongreen_5000_175_c` — PLA Plus Neon Green
- `elegoo_pla_plaplusorange_5000_175_c` — PLA Plus Orange
- `elegoo_pla_plapluspink_5000_175_c` — PLA Plus Pink
- `elegoo_pla_plapluspurple_5000_175_c` — PLA Plus Purple
- `elegoo_pla_plaplusred_5000_175_c` — PLA Plus Red
- `elegoo_pla_plaplusseagreen_5000_175_c` — PLA Plus Sea Green
- `elegoo_pla_plaplusskyblue_5000_175_c` — PLA Plus Sky Blue
- `elegoo_pla_plaplusspacegrey_5000_175_c` — PLA Plus Space Grey
- `elegoo_pla_plaplustranslucent_5000_175_c` — PLA Plus Translucent
- `elegoo_pla_plapluswhite_5000_175_c` — PLA Plus White
- `elegoo_pla_plapluswoodcolor_5000_175_c` — PLA Plus Wood Color
- `elegoo_pla_plaplusyellow_5000_175_c` — PLA Plus Yellow
- `elegoo_pla_plaproblack_1000_175_c` — PLA PRO Black
- `elegoo_pla_plaproblue_1000_175_c` — PLA PRO Blue
- `elegoo_pla_plaproburgundyred_1000_175_c` — PLA PRO Burgundy Red
- `elegoo_pla_plaprogreen_1000_175_c` — PLA PRO Green
- `elegoo_pla_plaprogrey_1000_175_c` — PLA PRO Grey
- `elegoo_pla_plaprolightblue_1000_175_c` — PLA PRO Light Blue
- `elegoo_pla_plapropurple_1000_175_c` — PLA PRO Purple
- `elegoo_pla_plaprosilver_1000_175_c` — PLA PRO Silver
- `elegoo_pla_plaprowhite_1000_175_c` — PLA PRO White
- `elegoo_pla_plaproyellow_1000_175_c` — PLA PRO Yellow
- `elegoo_pla_plasparkleblack_1000_175_c` — PLA Sparkle Black
- `elegoo_pla_plasparkledarkgrey_1000_175_c` — PLA Sparkle Dark Grey
- `elegoo_pla_plasparklegold_1000_175_c` — PLA Sparkle Gold
- `elegoo_pla_plasparklegreen_1000_175_c` — PLA Sparkle Green
- `elegoo_pla_plasparklepurplishgrey_1000_175_c` — PLA Sparkle Purplish Grey
- `elegoo_pla_plasparklered_1000_175_c` — PLA Sparkle Red
- `elegoo_pla_plasparkleturquoise_1000_175_c` — PLA Sparkle Turquoise
- `elegoo_pla_plawoodoak/lightbrown_1000_175_c` — PLA Wood Oak/Light Brown
- `elegoo_pla_plawoodrosewood_1000_175_c` — PLA Wood Rosewood
- `elegoo_pla_plawoodtanbirch_1000_175_c` — PLA Wood Tan Birch
- `elegoo_pla_plawoodteak_1000_175_c` — PLA Wood Teak
- `elegoo_pla_plawoodwalnut_1000_175_c` — PLA Wood Walnut
- `elegoo_pla_plawoodwoodfilled_1000_175_c` — PLA Wood Wood Filled
- `elegoo_pla_rapidplaplusbeige_5000_175_c` — RAPID PLA Plus Beige
- `elegoo_pla_rapidplaplusblack_5000_175_c` — RAPID PLA Plus Black
- `elegoo_pla_rapidplaplusblue_5000_175_c` — RAPID PLA Plus Blue
- `elegoo_pla_rapidplaplusbrown_5000_175_c` — RAPID PLA Plus Brown
- `elegoo_pla_rapidplaplusgreen_5000_175_c` — RAPID PLA Plus Green
- `elegoo_pla_rapidplaplusgrey_5000_175_c` — RAPID PLA Plus Grey
- `elegoo_pla_rapidplaplusorange_5000_175_c` — RAPID PLA Plus Orange
- `elegoo_pla_rapidplaplusred_5000_175_c` — RAPID PLA Plus Red
- `elegoo_pla_rapidplaplussilver_5000_175_c` — RAPID PLA Plus Silver
- `elegoo_pla_rapidplapluswhite_5000_175_c` — RAPID PLA Plus White
- `elegoo_pla_rapidplaplusyellow_5000_175_c` — RAPID PLA Plus Yellow
- `elegoo_pla_silkplablackgreen_1000_175_p` — Silk PLA Black Green
- `elegoo_pla_silkplabluepurple_1000_175_p` — Silk PLA Blue Purple
- `elegoo_pla_silkplayellowpurple_1000_175_p` — Silk PLA Yellow Purple
- `elegoo_tpu_rapidtpu95ablack_1000_175_p` — Rapid TPU 95A Black
- `elegoo_tpu_rapidtpu95ared_1000_175_p` — Rapid TPU 95A Red
- `elegoo_tpu_rapidtpu95awhite_1000_175_p` — Rapid TPU 95A White
- `elegoo_tpu-72d_tpu72dblack_1000_175_c` — TPU 72D Black
- `elegoo_tpu-72d_tpu72dblue_1000_175_c` — TPU 72D Blue
- `elegoo_tpu-72d_tpu72dgreen_1000_175_c` — TPU 72D Green
- `elegoo_tpu-72d_tpu72dgrey_1000_175_c` — TPU 72D Grey
- `elegoo_tpu-72d_tpu72dred_1000_175_c` — TPU 72D Red
- `elegoo_tpu-72d_tpu72dwhite_1000_175_c` — TPU 72D White
- `elegoo_tpu-72d_tpu72dyellow_1000_175_c` — TPU 72D Yellow
- `elegoo_tpu_tpu95ablack_1000_175_p` — TPU 95A Black
- `elegoo_tpu_tpu95ablue_1000_175_p` — TPU 95A Blue
- `elegoo_tpu_tpu95agreen_1000_175_p` — TPU 95A Green
- `elegoo_tpu_tpu95agrey_1000_175_p` — TPU 95A Grey
- `elegoo_tpu_tpu95ared_1000_175_p` — TPU 95A Red
- `elegoo_tpu_tpu95atranslucent_1000_175_p` — TPU 95A Translucent
- `elegoo_tpu_tpu95awhite_1000_175_p` — TPU 95A White
