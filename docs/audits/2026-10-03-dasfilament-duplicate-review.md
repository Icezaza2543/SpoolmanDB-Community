# dasfilament duplicate migration review

Base `5220497d01a2c78f890419ca4803d1948dc5d20f`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `b994ca88c6d7edc51ae9dc0534bb33db299bbbc530a2b46248db358b87d8eb7d`.

## Authorization and result

{"groups": 53, "approved_groups": 51, "retired": 51, "deferred": 2, "hard_stops": 0, "before_count": 52192, "after_count": 52141, "brand_before": 180, "brand_after": 129, "registry_before": 1242, "registry_after": 1293, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Rule1 upstream survivors retained. PETG scalar230/75/d1.29 agree with current exact PETG recommendations; no need to replace valid point values with unrelated source defaults. All HEX/tare/finish conflicts stay unresolved; no packaging/tare changes. DAS FILAMENT Grün color-label duplication and Toms3D line/color decomposition are Rule5 backlog. No exact ordinary-PLA all-variant current TDS bound, so no printing guesses. Identifier transfers only if needed on exact reviewed target IDs.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://dasfilament.de/produkt/petg-filament-50-g-sample-285-mm-7016/", "density": 1.29, "nozzle": [210, 235], "bed": [75, 85], "note": "Current exact PETG page corroborates retained survivor density1.29, nozzle230 and bed75. No sample packaging, tare or 2.85 availability is imported."}
- {"url": "https://dasfilament.de/produkt/pla-filament-175-mm-schwarz-matt-50-g-sample/", "note": "Exact matte-black sample page is not treated as evidence for every ordinary PLA color; no cross-line metadata correction."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`dasfilament_petg_petgalu-silber_1000_175_c`|`dasfilament_petg_alu-silber_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Alu-Silber::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petganthrazitv2_1000_175_c`|`dasfilament_petg_anthrazitv2_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Anthrazit V2::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgbeige_1000_175_c`|`dasfilament_petg_beige_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Beige::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgblau_1000_175_c`|`dasfilament_petg_blau_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Blau::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgburntcopper_1000_175_c`|`dasfilament_petg_burntcopper_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Burnt Copper::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgfeuerrot_1000_175_c`|`dasfilament_petg_feuerrot_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Feuerrot::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgflammschutzschwarz_1000_175_c`|`dasfilament_petg_flammschutzschwarz_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Flammschutz Schwarz::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petggrasgrn_1000_175_c`|`dasfilament_petg_grasgrn_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Grasgrün::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgleuchtorange_1000_175_c`|`dasfilament_petg_leuchtorange_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Leuchtorange::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petglila_1000_175_c`|`dasfilament_petg_lila_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Lila::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgmaisgelb_1000_175_c`|`dasfilament_petg_maisgelb_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Maisgelb::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgmelonengelb_1000_175_c`|`dasfilament_petg_melonengelb_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Melonengelb::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgmetallicblau_1000_175_c`|`dasfilament_petg_metallicblau_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Metallic Blau::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgmilitr-grn_1000_175_c`|`dasfilament_petg_militr-grn_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Militär-Grün::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgnatur_1000_175_c`|`dasfilament_petg_natur_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Natur::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgopalgrn_1000_175_c`|`dasfilament_petg_opalgrn_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Opalgrün::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgrubinrot_1000_175_c`|`dasfilament_petg_rubinrot_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Rubinrot::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgsaphirblau_1000_175_c`|`dasfilament_petg_saphirblau_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Saphirblau::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgschiefergrau_1000_175_c`|`dasfilament_petg_schiefergrau_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Schiefergrau::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgschwarz_1000_175_c`|`dasfilament_petg_schwarz_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Schwarz::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgsilber_1000_175_c`|`dasfilament_petg_silber_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Silber::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgsturmgrau_1000_175_c`|`dasfilament_petg_sturmgrau_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Sturmgrau::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgtransluzentneongelb_1000_175_c`|`dasfilament_petg_transluzentneongelb_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Transluzent Neongelb::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgtransluzentneongrn_1000_175_c`|`dasfilament_petg_transluzentneongrn_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Transluzent Neongrün::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgtransparentblau_1000_175_c`|`dasfilament_petg_transparentblau_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Transparent Blau::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgtransparentneongrn_1000_175_c`|`dasfilament_petg_transparentneongrn_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Transparent Neongrün::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgtransparentrot_1000_175_c`|`dasfilament_petg_transparentrot_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Transparent Rot::PETG::1000::1.75::cardboard::False`|
|`dasfilament_petg_petgwei_1000_175_c`|`dasfilament_petg_wei_1000_175_c`|`dasfilament.json::Das Filament::PETG {color_name}::PETG Weiß::PETG::1000::1.75::cardboard::False`|
|`dasfilament_pla_plaanthrazitv2_1000_175_c`|`dasfilament_pla_anthrazitv2_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Anthrazit V2::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_plabronze_1000_175_c`|`dasfilament_pla_bronze_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Bronze::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_plafeuerrot_1000_175_c`|`dasfilament_pla_feuerrot_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Feuerrot::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_plagoldv2_1000_175_c`|`dasfilament_pla_goldv2_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Gold V2::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_plagrasgrn_1000_175_c`|`dasfilament_pla_grasgrn_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Grasgrün::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_plagrau_1000_175_c`|`dasfilament_pla_grau_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Grau::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_plahimmelblau_1000_175_c`|`dasfilament_pla_himmelblau_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Himmelblau::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_plakastanienbraun_1000_175_c`|`dasfilament_pla_kastanienbraun_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Kastanienbraun::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_plakirschrot_1000_175_c`|`dasfilament_pla_kirschrot_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Kirschrot::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_plaknigsblau_1000_175_c`|`dasfilament_pla_knigsblau_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Königsblau::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_plamagenta_1000_175_c`|`dasfilament_pla_magenta_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Magenta::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_plametallicrot_1000_175_c`|`dasfilament_pla_metallicrot_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Metallic Rot::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_planatur_1000_175_c`|`dasfilament_pla_natur_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Natur::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_planeonorange_1000_175_c`|`dasfilament_pla_neonorange_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Neonorange::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_plareinorange_1000_175_c`|`dasfilament_pla_reinorange_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Reinorange::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_plaschwarz_1000_175_c`|`dasfilament_pla_schwarz_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Schwarz::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_plasilber_1000_175_c`|`dasfilament_pla_silber_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Silber::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_plasonnengelb_1000_175_c`|`dasfilament_pla_sonnengelb_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Sonnengelb::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_platannengrn_1000_175_c`|`dasfilament_pla_tannengrn_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Tannengrün::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_plathermo-rot_1000_175_c`|`dasfilament_pla_thermo-rot_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Thermo-Rot::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_platransluzent-blau_1000_175_c`|`dasfilament_pla_transluzentblau_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Transluzent-Blau::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_platransluzent-grn_1000_175_c`|`dasfilament_pla_transluzentgrn_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Transluzent-Grün::PLA::1000::1.75::cardboard::False`|
|`dasfilament_pla_plawei_1000_175_c`|`dasfilament_pla_wei_1000_175_c`|`dasfilament.json::Das Filament::PLA {color_name}::PLA Weiß::PLA::1000::1.75::cardboard::False`|

## Per-group decisions and unresolved metadata

### DA001: dup-74c75b72ff3d70689bd1b257856328acd39ed6bb47bfdd02d2d4c29cd3577bb6

Status: APPROVED; survivor `dasfilament_petg_alu-silber_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_alu-silber_1000_175_c`|`{color_name}`|`Alu-silber`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|
|`dasfilament_petg_petgalu-silber_1000_175_c`|`PETG {color_name}`|`Alu-Silber`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_alu-silber_1000_175_c": 250,
    "dasfilament_petg_petgalu-silber_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_petg_alu-silber_1000_175_c": "afafa9",
    "dasfilament_petg_petgalu-silber_1000_175_c": "C5C5BF"
  },
  "extruder_temp": {
    "dasfilament_petg_alu-silber_1000_175_c": 230,
    "dasfilament_petg_petgalu-silber_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_petg_alu-silber_1000_175_c": null,
    "dasfilament_petg_petgalu-silber_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "dasfilament_petg_alu-silber_1000_175_c": 75,
    "dasfilament_petg_petgalu-silber_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_petg_alu-silber_1000_175_c": null,
    "dasfilament_petg_petgalu-silber_1000_175_c": [
      70,
      90
    ]
  },
  "finish": {
    "dasfilament_petg_alu-silber_1000_175_c": "glossy",
    "dasfilament_petg_petgalu-silber_1000_175_c": null
  }
}
```

### DA002: dup-7cc1e276f8981e3b3f1260bf423925271ff5c0d8b9cd380627678e541da6d9d8

Status: APPROVED; survivor `dasfilament_petg_anthrazitv2_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_anthrazitv2_1000_175_c`|`{color_name}`|`Anthrazit V2`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|
|`dasfilament_petg_petganthrazitv2_1000_175_c`|`PETG {color_name}`|`Anthrazit V2`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_anthrazitv2_1000_175_c": 250,
    "dasfilament_petg_petganthrazitv2_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_petg_anthrazitv2_1000_175_c": "313131",
    "dasfilament_petg_petganthrazitv2_1000_175_c": "6A6C6E"
  },
  "extruder_temp": {
    "dasfilament_petg_anthrazitv2_1000_175_c": 230,
    "dasfilament_petg_petganthrazitv2_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_petg_anthrazitv2_1000_175_c": null,
    "dasfilament_petg_petganthrazitv2_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "dasfilament_petg_anthrazitv2_1000_175_c": 75,
    "dasfilament_petg_petganthrazitv2_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_petg_anthrazitv2_1000_175_c": null,
    "dasfilament_petg_petganthrazitv2_1000_175_c": [
      70,
      90
    ]
  },
  "finish": {
    "dasfilament_petg_anthrazitv2_1000_175_c": "glossy",
    "dasfilament_petg_petganthrazitv2_1000_175_c": null
  }
}
```

### DA003: dup-994571fe37f68605098a737452a0e5aee06e9819f17d4b2bb1f57130c1d968a1

Status: APPROVED; survivor `dasfilament_petg_beige_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_beige_1000_175_c`|`{color_name}`|`Beige`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|
|`dasfilament_petg_petgbeige_1000_175_c`|`PETG {color_name}`|`Beige`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_beige_1000_175_c": 250,
    "dasfilament_petg_petgbeige_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_petg_beige_1000_175_c": "bda791",
    "dasfilament_petg_petgbeige_1000_175_c": "E9D1C1"
  },
  "extruder_temp": {
    "dasfilament_petg_beige_1000_175_c": 230,
    "dasfilament_petg_petgbeige_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_petg_beige_1000_175_c": null,
    "dasfilament_petg_petgbeige_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "dasfilament_petg_beige_1000_175_c": 75,
    "dasfilament_petg_petgbeige_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_petg_beige_1000_175_c": null,
    "dasfilament_petg_petgbeige_1000_175_c": [
      70,
      90
    ]
  }
}
```

### DA004: dup-967b60815a26dab889715b1bb78b821bd854e3b16acbe9afc2a575a6389c73d8

Status: APPROVED; survivor `dasfilament_petg_blau_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_blau_1000_175_c`|`{color_name}`|`Blau`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|
|`dasfilament_petg_petgblau_1000_175_c`|`PETG {color_name}`|`Blau`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_blau_1000_175_c": 250,
    "dasfilament_petg_petgblau_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_petg_blau_1000_175_c": "006ace",
    "dasfilament_petg_petgblau_1000_175_c": "0066D9"
  },
  "extruder_temp": {
    "dasfilament_petg_blau_1000_175_c": 230,
    "dasfilament_petg_petgblau_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_petg_blau_1000_175_c": null,
    "dasfilament_petg_petgblau_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "dasfilament_petg_blau_1000_175_c": 75,
    "dasfilament_petg_petgblau_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_petg_blau_1000_175_c": null,
    "dasfilament_petg_petgblau_1000_175_c": [
      70,
      90
    ]
  }
}
```

### DA005: dup-57e54c019f2f2368cefa081bf0739e6247caee6da250be609c6cc2812a2fa0fa

Status: APPROVED; survivor `dasfilament_petg_burntcopper_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_burntcopper_1000_175_c`|`{color_name}`|`Burnt Copper`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|
|`dasfilament_petg_petgburntcopper_1000_175_c`|`PETG {color_name}`|`Burnt Copper`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_burntcopper_1000_175_c": 250,
    "dasfilament_petg_petgburntcopper_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_petg_burntcopper_1000_175_c": "9d3707",
    "dasfilament_petg_petgburntcopper_1000_175_c": "C66547"
  },
  "extruder_temp": {
    "dasfilament_petg_burntcopper_1000_175_c": 230,
    "dasfilament_petg_petgburntcopper_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_petg_burntcopper_1000_175_c": null,
    "dasfilament_petg_petgburntcopper_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "dasfilament_petg_burntcopper_1000_175_c": 75,
    "dasfilament_petg_petgburntcopper_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_petg_burntcopper_1000_175_c": null,
    "dasfilament_petg_petgburntcopper_1000_175_c": [
      70,
      90
    ]
  },
  "finish": {
    "dasfilament_petg_burntcopper_1000_175_c": "glossy",
    "dasfilament_petg_petgburntcopper_1000_175_c": null
  }
}
```

### DA006: dup-d86f50611418d804d88a2a482a090750ffef6da1bce48145b6fe5f9778084df2

Status: APPROVED; survivor `dasfilament_petg_feuerrot_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_feuerrot_1000_175_c`|`{color_name}`|`Feuerrot`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|
|`dasfilament_petg_petgfeuerrot_1000_175_c`|`PETG {color_name}`|`Feuerrot`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_feuerrot_1000_175_c": 250,
    "dasfilament_petg_petgfeuerrot_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_petg_feuerrot_1000_175_c": "d81919",
    "dasfilament_petg_petgfeuerrot_1000_175_c": "FF2C29"
  },
  "extruder_temp": {
    "dasfilament_petg_feuerrot_1000_175_c": 230,
    "dasfilament_petg_petgfeuerrot_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_petg_feuerrot_1000_175_c": null,
    "dasfilament_petg_petgfeuerrot_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "dasfilament_petg_feuerrot_1000_175_c": 75,
    "dasfilament_petg_petgfeuerrot_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_petg_feuerrot_1000_175_c": null,
    "dasfilament_petg_petgfeuerrot_1000_175_c": [
      70,
      90
    ]
  }
}
```

### DA007: dup-63bccbc80b878963ec95ed9bbf277324d5bbafd385f05eeb912517f3f4b92dc1

Status: APPROVED; survivor `dasfilament_petg_flammschutzschwarz_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_flammschutzschwarz_1000_175_c`|`{color_name}`|`Flammschutz Schwarz`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|
|`dasfilament_petg_petgflammschutzschwarz_1000_175_c`|`PETG {color_name}`|`Flammschutz Schwarz`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_flammschutzschwarz_1000_175_c": 250,
    "dasfilament_petg_petgflammschutzschwarz_1000_175_c": null
  },
  "extruder_temp": {
    "dasfilament_petg_flammschutzschwarz_1000_175_c": 230,
    "dasfilament_petg_petgflammschutzschwarz_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_petg_flammschutzschwarz_1000_175_c": null,
    "dasfilament_petg_petgflammschutzschwarz_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "dasfilament_petg_flammschutzschwarz_1000_175_c": 75,
    "dasfilament_petg_petgflammschutzschwarz_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_petg_flammschutzschwarz_1000_175_c": null,
    "dasfilament_petg_petgflammschutzschwarz_1000_175_c": [
      70,
      90
    ]
  },
  "finish": {
    "dasfilament_petg_flammschutzschwarz_1000_175_c": "matte",
    "dasfilament_petg_petgflammschutzschwarz_1000_175_c": null
  }
}
```

### DA008: dup-d402e65badd332c66ea489d223e1de29bdb63756ec5849ce937bffc4533d7289

Status: APPROVED; survivor `dasfilament_petg_grasgrn_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_grasgrn_1000_175_c`|`{color_name}`|`Grasgrün`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|
|`dasfilament_petg_petggrasgrn_1000_175_c`|`PETG {color_name}`|`Grasgrün`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_grasgrn_1000_175_c": 250,
    "dasfilament_petg_petggrasgrn_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_petg_grasgrn_1000_175_c": "35934b",
    "dasfilament_petg_petggrasgrn_1000_175_c": "06B100"
  },
  "extruder_temp": {
    "dasfilament_petg_grasgrn_1000_175_c": 230,
    "dasfilament_petg_petggrasgrn_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_petg_grasgrn_1000_175_c": null,
    "dasfilament_petg_petggrasgrn_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "dasfilament_petg_grasgrn_1000_175_c": 75,
    "dasfilament_petg_petggrasgrn_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_petg_grasgrn_1000_175_c": null,
    "dasfilament_petg_petggrasgrn_1000_175_c": [
      70,
      90
    ]
  }
}
```

### DA009: dup-55780acbed4cebf6a43be1bba0f35c8bc1a4716fa8680991b504dacc289de79d

Status: APPROVED; survivor `dasfilament_petg_leuchtorange_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_leuchtorange_1000_175_c`|`{color_name}`|`Leuchtorange`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|
|`dasfilament_petg_petgleuchtorange_1000_175_c`|`PETG {color_name}`|`Leuchtorange`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_leuchtorange_1000_175_c": 250,
    "dasfilament_petg_petgleuchtorange_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_petg_leuchtorange_1000_175_c": "f05000",
    "dasfilament_petg_petgleuchtorange_1000_175_c": "EA5E1A"
  },
  "extruder_temp": {
    "dasfilament_petg_leuchtorange_1000_175_c": 230,
    "dasfilament_petg_petgleuchtorange_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_petg_leuchtorange_1000_175_c": null,
    "dasfilament_petg_petgleuchtorange_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "dasfilament_petg_leuchtorange_1000_175_c": 75,
    "dasfilament_petg_petgleuchtorange_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_petg_leuchtorange_1000_175_c": null,
    "dasfilament_petg_petgleuchtorange_1000_175_c": [
      70,
      90
    ]
  }
}
```

### DA010: dup-d6bf70969dde4970b35ed33aa5fa9c5d2ec4b1ccaa30c7c607213fd9180daa60

Status: APPROVED; survivor `dasfilament_petg_lila_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_lila_1000_175_c`|`{color_name}`|`Lila`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|
|`dasfilament_petg_petglila_1000_175_c`|`PETG {color_name}`|`Lila`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_lila_1000_175_c": 250,
    "dasfilament_petg_petglila_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_petg_lila_1000_175_c": "8804ad",
    "dasfilament_petg_petglila_1000_175_c": "D93382"
  },
  "extruder_temp": {
    "dasfilament_petg_lila_1000_175_c": 230,
    "dasfilament_petg_petglila_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_petg_lila_1000_175_c": null,
    "dasfilament_petg_petglila_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "dasfilament_petg_lila_1000_175_c": 75,
    "dasfilament_petg_petglila_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_petg_lila_1000_175_c": null,
    "dasfilament_petg_petglila_1000_175_c": [
      70,
      90
    ]
  }
}
```

### DA011: dup-7a81385b27730aad55f4a2c643d18b0fb24f6bf787babba84742a5bc62759d6b

Status: APPROVED; survivor `dasfilament_petg_maisgelb_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_maisgelb_1000_175_c`|`{color_name}`|`Maisgelb`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|
|`dasfilament_petg_petgmaisgelb_1000_175_c`|`PETG {color_name}`|`Maisgelb`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_maisgelb_1000_175_c": 250,
    "dasfilament_petg_petgmaisgelb_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_petg_maisgelb_1000_175_c": "bc9624",
    "dasfilament_petg_petgmaisgelb_1000_175_c": "E8BD00"
  },
  "extruder_temp": {
    "dasfilament_petg_maisgelb_1000_175_c": 230,
    "dasfilament_petg_petgmaisgelb_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_petg_maisgelb_1000_175_c": null,
    "dasfilament_petg_petgmaisgelb_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "dasfilament_petg_maisgelb_1000_175_c": 75,
    "dasfilament_petg_petgmaisgelb_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_petg_maisgelb_1000_175_c": null,
    "dasfilament_petg_petgmaisgelb_1000_175_c": [
      70,
      90
    ]
  }
}
```

### DA012: dup-1a9f821fbaf7e027f048447bd0fa11da49a0709d3b170c5c412e46e138bbc40e

Status: APPROVED; survivor `dasfilament_petg_melonengelb_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_melonengelb_1000_175_c`|`{color_name}`|`Melonengelb`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|
|`dasfilament_petg_petgmelonengelb_1000_175_c`|`PETG {color_name}`|`Melonengelb`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_melonengelb_1000_175_c": 250,
    "dasfilament_petg_petgmelonengelb_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_petg_melonengelb_1000_175_c": "bc6831",
    "dasfilament_petg_petgmelonengelb_1000_175_c": "FF9A14"
  },
  "extruder_temp": {
    "dasfilament_petg_melonengelb_1000_175_c": 230,
    "dasfilament_petg_petgmelonengelb_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_petg_melonengelb_1000_175_c": null,
    "dasfilament_petg_petgmelonengelb_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "dasfilament_petg_melonengelb_1000_175_c": 75,
    "dasfilament_petg_petgmelonengelb_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_petg_melonengelb_1000_175_c": null,
    "dasfilament_petg_petgmelonengelb_1000_175_c": [
      70,
      90
    ]
  }
}
```

### DA013: dup-bb8cb1206d3d838ffc763f0106ae6739cb0baedbee426a13c1290483b60c7f01

Status: APPROVED; survivor `dasfilament_petg_metallicblau_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_metallicblau_1000_175_c`|`{color_name}`|`Metallic Blau`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|
|`dasfilament_petg_petgmetallicblau_1000_175_c`|`PETG {color_name}`|`Metallic Blau`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_metallicblau_1000_175_c": 250,
    "dasfilament_petg_petgmetallicblau_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_petg_metallicblau_1000_175_c": "002f68",
    "dasfilament_petg_petgmetallicblau_1000_175_c": "0353BA"
  },
  "extruder_temp": {
    "dasfilament_petg_metallicblau_1000_175_c": 230,
    "dasfilament_petg_petgmetallicblau_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_petg_metallicblau_1000_175_c": null,
    "dasfilament_petg_petgmetallicblau_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "dasfilament_petg_metallicblau_1000_175_c": 75,
    "dasfilament_petg_petgmetallicblau_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_petg_metallicblau_1000_175_c": null,
    "dasfilament_petg_petgmetallicblau_1000_175_c": [
      70,
      90
    ]
  },
  "finish": {
    "dasfilament_petg_metallicblau_1000_175_c": "glossy",
    "dasfilament_petg_petgmetallicblau_1000_175_c": null
  }
}
```

### DA014: dup-ba2785925bc853343f6b5f28a66bb63f60c6c95e2ad780c1d7284698b6b655ad

Status: APPROVED; survivor `dasfilament_petg_militr-grn_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_militr-grn_1000_175_c`|`{color_name}`|`Militär-Grün`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|
|`dasfilament_petg_petgmilitr-grn_1000_175_c`|`PETG {color_name}`|`Militär-Grün`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_militr-grn_1000_175_c": 250,
    "dasfilament_petg_petgmilitr-grn_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_petg_militr-grn_1000_175_c": "394807",
    "dasfilament_petg_petgmilitr-grn_1000_175_c": "6E8451"
  },
  "extruder_temp": {
    "dasfilament_petg_militr-grn_1000_175_c": 230,
    "dasfilament_petg_petgmilitr-grn_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_petg_militr-grn_1000_175_c": null,
    "dasfilament_petg_petgmilitr-grn_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "dasfilament_petg_militr-grn_1000_175_c": 75,
    "dasfilament_petg_petgmilitr-grn_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_petg_militr-grn_1000_175_c": null,
    "dasfilament_petg_petgmilitr-grn_1000_175_c": [
      70,
      90
    ]
  }
}
```

### DA015: dup-a30c718338bb3c1f621602b4095197b4fe2cff62a5e2fe1cd86013af19047f02

Status: APPROVED; survivor `dasfilament_petg_natur_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_natur_1000_175_c`|`{color_name}`|`Natur`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|
|`dasfilament_petg_petgnatur_1000_175_c`|`PETG {color_name}`|`Natur`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_natur_1000_175_c": 250,
    "dasfilament_petg_petgnatur_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_petg_natur_1000_175_c": "ffffff22",
    "dasfilament_petg_petgnatur_1000_175_c": "D9D8DE"
  },
  "extruder_temp": {
    "dasfilament_petg_natur_1000_175_c": 230,
    "dasfilament_petg_petgnatur_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_petg_natur_1000_175_c": null,
    "dasfilament_petg_petgnatur_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "dasfilament_petg_natur_1000_175_c": 75,
    "dasfilament_petg_petgnatur_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_petg_natur_1000_175_c": null,
    "dasfilament_petg_petgnatur_1000_175_c": [
      70,
      90
    ]
  }
}
```

### DA016: dup-9d150b444861f5f81032236f845516aaa44ed84486793db690b2b02952c373a8

Status: APPROVED; survivor `dasfilament_petg_opalgrn_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_opalgrn_1000_175_c`|`{color_name}`|`Opalgrün`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|
|`dasfilament_petg_petgopalgrn_1000_175_c`|`PETG {color_name}`|`Opalgrün`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_opalgrn_1000_175_c": 250,
    "dasfilament_petg_petgopalgrn_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_petg_opalgrn_1000_175_c": "004747",
    "dasfilament_petg_petgopalgrn_1000_175_c": "008059"
  },
  "extruder_temp": {
    "dasfilament_petg_opalgrn_1000_175_c": 230,
    "dasfilament_petg_petgopalgrn_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_petg_opalgrn_1000_175_c": null,
    "dasfilament_petg_petgopalgrn_1000_175_c": [
      220,
      250
    ]
  },
  "bed_temp": {
    "dasfilament_petg_opalgrn_1000_175_c": 75,
    "dasfilament_petg_petgopalgrn_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_petg_opalgrn_1000_175_c": null,
    "dasfilament_petg_petgopalgrn_1000_175_c": [
      70,
      90
    ]
  }
}
```

### DA017: dup-ddf83c475b23d54a865c25b95268bf43a43232688dcd990efffd9f75127027c1

Status: APPROVED; survivor `dasfilament_petg_rubinrot_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_petgrubinrot_1000_175_c`|`PETG {color_name}`|`Rubinrot`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|
|`dasfilament_petg_rubinrot_1000_175_c`|`{color_name}`|`Rubinrot`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_petgrubinrot_1000_175_c": null,
    "dasfilament_petg_rubinrot_1000_175_c": 250
  },
  "color_hex": {
    "dasfilament_petg_petgrubinrot_1000_175_c": "AC1A17",
    "dasfilament_petg_rubinrot_1000_175_c": "8b2411"
  },
  "extruder_temp": {
    "dasfilament_petg_petgrubinrot_1000_175_c": null,
    "dasfilament_petg_rubinrot_1000_175_c": 230
  },
  "extruder_temp_range": {
    "dasfilament_petg_petgrubinrot_1000_175_c": [
      220,
      250
    ],
    "dasfilament_petg_rubinrot_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_petg_petgrubinrot_1000_175_c": null,
    "dasfilament_petg_rubinrot_1000_175_c": 75
  },
  "bed_temp_range": {
    "dasfilament_petg_petgrubinrot_1000_175_c": [
      70,
      90
    ],
    "dasfilament_petg_rubinrot_1000_175_c": null
  }
}
```

### DA018: dup-e80bbc68b36714dbc19dc347a034a865701f7d9533b64fc76b1796eff38214f1

Status: APPROVED; survivor `dasfilament_petg_saphirblau_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_petgsaphirblau_1000_175_c`|`PETG {color_name}`|`Saphirblau`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|
|`dasfilament_petg_saphirblau_1000_175_c`|`{color_name}`|`Saphirblau`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_petgsaphirblau_1000_175_c": null,
    "dasfilament_petg_saphirblau_1000_175_c": 250
  },
  "color_hex": {
    "dasfilament_petg_petgsaphirblau_1000_175_c": "0353BA",
    "dasfilament_petg_saphirblau_1000_175_c": "02224d"
  },
  "extruder_temp": {
    "dasfilament_petg_petgsaphirblau_1000_175_c": null,
    "dasfilament_petg_saphirblau_1000_175_c": 230
  },
  "extruder_temp_range": {
    "dasfilament_petg_petgsaphirblau_1000_175_c": [
      220,
      250
    ],
    "dasfilament_petg_saphirblau_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_petg_petgsaphirblau_1000_175_c": null,
    "dasfilament_petg_saphirblau_1000_175_c": 75
  },
  "bed_temp_range": {
    "dasfilament_petg_petgsaphirblau_1000_175_c": [
      70,
      90
    ],
    "dasfilament_petg_saphirblau_1000_175_c": null
  }
}
```

### DA019: dup-b4644959d5778489b90f170cbcc10253a8d42c406c4a5a9164a21d59996d314e

Status: APPROVED; survivor `dasfilament_petg_schiefergrau_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_petgschiefergrau_1000_175_c`|`PETG {color_name}`|`Schiefergrau`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|
|`dasfilament_petg_schiefergrau_1000_175_c`|`{color_name}`|`Schiefergrau`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_petgschiefergrau_1000_175_c": null,
    "dasfilament_petg_schiefergrau_1000_175_c": 250
  },
  "color_hex": {
    "dasfilament_petg_petgschiefergrau_1000_175_c": "5A696C",
    "dasfilament_petg_schiefergrau_1000_175_c": "484848"
  },
  "extruder_temp": {
    "dasfilament_petg_petgschiefergrau_1000_175_c": null,
    "dasfilament_petg_schiefergrau_1000_175_c": 230
  },
  "extruder_temp_range": {
    "dasfilament_petg_petgschiefergrau_1000_175_c": [
      220,
      250
    ],
    "dasfilament_petg_schiefergrau_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_petg_petgschiefergrau_1000_175_c": null,
    "dasfilament_petg_schiefergrau_1000_175_c": 75
  },
  "bed_temp_range": {
    "dasfilament_petg_petgschiefergrau_1000_175_c": [
      70,
      90
    ],
    "dasfilament_petg_schiefergrau_1000_175_c": null
  }
}
```

### DA020: dup-bfe9c5c8dcfec10d394930aab3250ba960f09703fd1571a462541bb7e417ccf0

Status: APPROVED; survivor `dasfilament_petg_schwarz_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_petgschwarz_1000_175_c`|`PETG {color_name}`|`Schwarz`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|
|`dasfilament_petg_schwarz_1000_175_c`|`{color_name}`|`Schwarz`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_petgschwarz_1000_175_c": null,
    "dasfilament_petg_schwarz_1000_175_c": 250
  },
  "extruder_temp": {
    "dasfilament_petg_petgschwarz_1000_175_c": null,
    "dasfilament_petg_schwarz_1000_175_c": 230
  },
  "extruder_temp_range": {
    "dasfilament_petg_petgschwarz_1000_175_c": [
      220,
      250
    ],
    "dasfilament_petg_schwarz_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_petg_petgschwarz_1000_175_c": null,
    "dasfilament_petg_schwarz_1000_175_c": 75
  },
  "bed_temp_range": {
    "dasfilament_petg_petgschwarz_1000_175_c": [
      70,
      90
    ],
    "dasfilament_petg_schwarz_1000_175_c": null
  }
}
```

### DA021: dup-9b0b7a9490e819e48e104c1191f78a918ba853388a99a7c596a5bc4559111d01

Status: APPROVED; survivor `dasfilament_petg_silber_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_petgsilber_1000_175_c`|`PETG {color_name}`|`Silber`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|
|`dasfilament_petg_silber_1000_175_c`|`{color_name}`|`Silber`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_petgsilber_1000_175_c": null,
    "dasfilament_petg_silber_1000_175_c": 250
  },
  "color_hex": {
    "dasfilament_petg_petgsilber_1000_175_c": "A8B0BD",
    "dasfilament_petg_silber_1000_175_c": "bdbdbd"
  },
  "extruder_temp": {
    "dasfilament_petg_petgsilber_1000_175_c": null,
    "dasfilament_petg_silber_1000_175_c": 230
  },
  "extruder_temp_range": {
    "dasfilament_petg_petgsilber_1000_175_c": [
      220,
      250
    ],
    "dasfilament_petg_silber_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_petg_petgsilber_1000_175_c": null,
    "dasfilament_petg_silber_1000_175_c": 75
  },
  "bed_temp_range": {
    "dasfilament_petg_petgsilber_1000_175_c": [
      70,
      90
    ],
    "dasfilament_petg_silber_1000_175_c": null
  },
  "finish": {
    "dasfilament_petg_petgsilber_1000_175_c": null,
    "dasfilament_petg_silber_1000_175_c": "glossy"
  }
}
```

### DA022: dup-40fcbeff53ebe6312d2485396b44b3a63157323affbc095ea2884ae149a73652

Status: APPROVED; survivor `dasfilament_petg_sturmgrau_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_petgsturmgrau_1000_175_c`|`PETG {color_name}`|`Sturmgrau`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|
|`dasfilament_petg_sturmgrau_1000_175_c`|`{color_name}`|`Sturmgrau`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_petgsturmgrau_1000_175_c": null,
    "dasfilament_petg_sturmgrau_1000_175_c": 250
  },
  "color_hex": {
    "dasfilament_petg_petgsturmgrau_1000_175_c": "808080",
    "dasfilament_petg_sturmgrau_1000_175_c": "434343"
  },
  "extruder_temp": {
    "dasfilament_petg_petgsturmgrau_1000_175_c": null,
    "dasfilament_petg_sturmgrau_1000_175_c": 230
  },
  "extruder_temp_range": {
    "dasfilament_petg_petgsturmgrau_1000_175_c": [
      220,
      250
    ],
    "dasfilament_petg_sturmgrau_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_petg_petgsturmgrau_1000_175_c": null,
    "dasfilament_petg_sturmgrau_1000_175_c": 75
  },
  "bed_temp_range": {
    "dasfilament_petg_petgsturmgrau_1000_175_c": [
      70,
      90
    ],
    "dasfilament_petg_sturmgrau_1000_175_c": null
  }
}
```

### DA023: dup-7cd75e4bf30ddeb98e09002a92742e6a8fbd3971b327bb762818284358075de2

Status: APPROVED; survivor `dasfilament_petg_transluzentneongelb_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_petgtransluzentneongelb_1000_175_c`|`PETG {color_name}`|`Transluzent Neongelb`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|
|`dasfilament_petg_transluzentneongelb_1000_175_c`|`{color_name}`|`Transluzent Neongelb`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_petgtransluzentneongelb_1000_175_c": null,
    "dasfilament_petg_transluzentneongelb_1000_175_c": 250
  },
  "color_hex": {
    "dasfilament_petg_petgtransluzentneongelb_1000_175_c": "E4FF33",
    "dasfilament_petg_transluzentneongelb_1000_175_c": "e6ff0088"
  },
  "extruder_temp": {
    "dasfilament_petg_petgtransluzentneongelb_1000_175_c": null,
    "dasfilament_petg_transluzentneongelb_1000_175_c": 230
  },
  "extruder_temp_range": {
    "dasfilament_petg_petgtransluzentneongelb_1000_175_c": [
      220,
      250
    ],
    "dasfilament_petg_transluzentneongelb_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_petg_petgtransluzentneongelb_1000_175_c": null,
    "dasfilament_petg_transluzentneongelb_1000_175_c": 75
  },
  "bed_temp_range": {
    "dasfilament_petg_petgtransluzentneongelb_1000_175_c": [
      70,
      90
    ],
    "dasfilament_petg_transluzentneongelb_1000_175_c": null
  }
}
```

### DA024: dup-c20066c181b2d1c12eb024cf4a335e602eea47e4f234c1625493487806563066

Status: APPROVED; survivor `dasfilament_petg_transluzentneongrn_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_petgtransluzentneongrn_1000_175_c`|`PETG {color_name}`|`Transluzent Neongrün`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|
|`dasfilament_petg_transluzentneongrn_1000_175_c`|`{color_name}`|`Transluzent Neongrün`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_petgtransluzentneongrn_1000_175_c": null,
    "dasfilament_petg_transluzentneongrn_1000_175_c": 250
  },
  "color_hex": {
    "dasfilament_petg_petgtransluzentneongrn_1000_175_c": "70FA00",
    "dasfilament_petg_transluzentneongrn_1000_175_c": "00ff3388"
  },
  "extruder_temp": {
    "dasfilament_petg_petgtransluzentneongrn_1000_175_c": null,
    "dasfilament_petg_transluzentneongrn_1000_175_c": 230
  },
  "extruder_temp_range": {
    "dasfilament_petg_petgtransluzentneongrn_1000_175_c": [
      220,
      250
    ],
    "dasfilament_petg_transluzentneongrn_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_petg_petgtransluzentneongrn_1000_175_c": null,
    "dasfilament_petg_transluzentneongrn_1000_175_c": 75
  },
  "bed_temp_range": {
    "dasfilament_petg_petgtransluzentneongrn_1000_175_c": [
      70,
      90
    ],
    "dasfilament_petg_transluzentneongrn_1000_175_c": null
  }
}
```

### DA025: dup-625a7239fcd670307d853c4d299c3359ef9db2ab666b8fe014e689e30174c558

Status: APPROVED; survivor `dasfilament_petg_transparentblau_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_petgtransparentblau_1000_175_c`|`PETG {color_name}`|`Transparent Blau`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|
|`dasfilament_petg_transparentblau_1000_175_c`|`{color_name}`|`Transparent Blau`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_petgtransparentblau_1000_175_c": null,
    "dasfilament_petg_transparentblau_1000_175_c": 250
  },
  "color_hex": {
    "dasfilament_petg_petgtransparentblau_1000_175_c": "0353BA",
    "dasfilament_petg_transparentblau_1000_175_c": "2437b922"
  },
  "extruder_temp": {
    "dasfilament_petg_petgtransparentblau_1000_175_c": null,
    "dasfilament_petg_transparentblau_1000_175_c": 230
  },
  "extruder_temp_range": {
    "dasfilament_petg_petgtransparentblau_1000_175_c": [
      220,
      250
    ],
    "dasfilament_petg_transparentblau_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_petg_petgtransparentblau_1000_175_c": null,
    "dasfilament_petg_transparentblau_1000_175_c": 75
  },
  "bed_temp_range": {
    "dasfilament_petg_petgtransparentblau_1000_175_c": [
      70,
      90
    ],
    "dasfilament_petg_transparentblau_1000_175_c": null
  }
}
```

### DA026: dup-5d675b9c980578bc632584f77d6d21126cee74709cda0ed11122d1d148a9f5a2

Status: APPROVED; survivor `dasfilament_petg_transparentneongrn_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_petgtransparentneongrn_1000_175_c`|`PETG {color_name}`|`Transparent Neongrün`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|
|`dasfilament_petg_transparentneongrn_1000_175_c`|`{color_name}`|`Transparent Neongrün`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_petgtransparentneongrn_1000_175_c": null,
    "dasfilament_petg_transparentneongrn_1000_175_c": 250
  },
  "color_hex": {
    "dasfilament_petg_petgtransparentneongrn_1000_175_c": "06B100",
    "dasfilament_petg_transparentneongrn_1000_175_c": "00ff3322"
  },
  "extruder_temp": {
    "dasfilament_petg_petgtransparentneongrn_1000_175_c": null,
    "dasfilament_petg_transparentneongrn_1000_175_c": 230
  },
  "extruder_temp_range": {
    "dasfilament_petg_petgtransparentneongrn_1000_175_c": [
      220,
      250
    ],
    "dasfilament_petg_transparentneongrn_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_petg_petgtransparentneongrn_1000_175_c": null,
    "dasfilament_petg_transparentneongrn_1000_175_c": 75
  },
  "bed_temp_range": {
    "dasfilament_petg_petgtransparentneongrn_1000_175_c": [
      70,
      90
    ],
    "dasfilament_petg_transparentneongrn_1000_175_c": null
  }
}
```

### DA027: dup-b12043ae2b5d0d86fbef977d1eec578ebac27a7105774211fe5dcd25a462c2ce

Status: APPROVED; survivor `dasfilament_petg_transparentrot_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_petgtransparentrot_1000_175_c`|`PETG {color_name}`|`Transparent Rot`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|
|`dasfilament_petg_transparentrot_1000_175_c`|`{color_name}`|`Transparent Rot`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_petgtransparentrot_1000_175_c": null,
    "dasfilament_petg_transparentrot_1000_175_c": 250
  },
  "color_hex": {
    "dasfilament_petg_petgtransparentrot_1000_175_c": "AC1A17",
    "dasfilament_petg_transparentrot_1000_175_c": "be000022"
  },
  "extruder_temp": {
    "dasfilament_petg_petgtransparentrot_1000_175_c": null,
    "dasfilament_petg_transparentrot_1000_175_c": 230
  },
  "extruder_temp_range": {
    "dasfilament_petg_petgtransparentrot_1000_175_c": [
      220,
      250
    ],
    "dasfilament_petg_transparentrot_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_petg_petgtransparentrot_1000_175_c": null,
    "dasfilament_petg_transparentrot_1000_175_c": 75
  },
  "bed_temp_range": {
    "dasfilament_petg_petgtransparentrot_1000_175_c": [
      70,
      90
    ],
    "dasfilament_petg_transparentrot_1000_175_c": null
  }
}
```

### DA028: dup-193fbd6b3b072477a14a0e0b3e61cc0889449945a954440fe1982916da7a648d

Status: APPROVED; survivor `dasfilament_petg_wei_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_petg_petgwei_1000_175_c`|`PETG {color_name}`|`Weiß`|{"source_file": "dasfilament.json", "definition_index": 4, "weights": 1, "diameters": 1, "colors": 30, "compiled_records": 30} / False|
|`dasfilament_petg_wei_1000_175_c`|`{color_name}`|`Weiß`|{"source_file": "dasfilament.json", "definition_index": 2, "weights": 1, "diameters": 1, "colors": 29, "compiled_records": 29} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_petg_petgwei_1000_175_c": null,
    "dasfilament_petg_wei_1000_175_c": 250
  },
  "color_hex": {
    "dasfilament_petg_petgwei_1000_175_c": "FFFFFF",
    "dasfilament_petg_wei_1000_175_c": "ffffff"
  },
  "extruder_temp": {
    "dasfilament_petg_petgwei_1000_175_c": null,
    "dasfilament_petg_wei_1000_175_c": 230
  },
  "extruder_temp_range": {
    "dasfilament_petg_petgwei_1000_175_c": [
      220,
      250
    ],
    "dasfilament_petg_wei_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_petg_petgwei_1000_175_c": null,
    "dasfilament_petg_wei_1000_175_c": 75
  },
  "bed_temp_range": {
    "dasfilament_petg_petgwei_1000_175_c": [
      70,
      90
    ],
    "dasfilament_petg_wei_1000_175_c": null
  }
}
```

### DA029: dup-1d63dfdd2d61c647947b18af8cd478bd7c099b6fed4c65705e7081b2d3ac1562

Status: APPROVED; survivor `dasfilament_pla_anthrazitv2_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_anthrazitv2_1000_175_c`|`{color_name}`|`Anthrazit V2`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|
|`dasfilament_pla_plaanthrazitv2_1000_175_c`|`PLA {color_name}`|`Anthrazit V2`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_anthrazitv2_1000_175_c": 212,
    "dasfilament_pla_plaanthrazitv2_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_pla_anthrazitv2_1000_175_c": "313131",
    "dasfilament_pla_plaanthrazitv2_1000_175_c": "6A6C6E"
  },
  "extruder_temp": {
    "dasfilament_pla_anthrazitv2_1000_175_c": 220,
    "dasfilament_pla_plaanthrazitv2_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_pla_anthrazitv2_1000_175_c": null,
    "dasfilament_pla_plaanthrazitv2_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "dasfilament_pla_anthrazitv2_1000_175_c": 60,
    "dasfilament_pla_plaanthrazitv2_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_pla_anthrazitv2_1000_175_c": null,
    "dasfilament_pla_plaanthrazitv2_1000_175_c": [
      50,
      70
    ]
  },
  "finish": {
    "dasfilament_pla_anthrazitv2_1000_175_c": "glossy",
    "dasfilament_pla_plaanthrazitv2_1000_175_c": null
  }
}
```

### DA030: dup-0179a6c39ba3a4c953999077ceeb0efebfb3d651b81ece82ee646abb93c92b23

Status: APPROVED; survivor `dasfilament_pla_bronze_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_bronze_1000_175_c`|`{color_name}`|`Bronze`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|
|`dasfilament_pla_plabronze_1000_175_c`|`PLA {color_name}`|`Bronze`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_bronze_1000_175_c": 212,
    "dasfilament_pla_plabronze_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_pla_bronze_1000_175_c": "3a2918",
    "dasfilament_pla_plabronze_1000_175_c": "805F3C"
  },
  "extruder_temp": {
    "dasfilament_pla_bronze_1000_175_c": 220,
    "dasfilament_pla_plabronze_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_pla_bronze_1000_175_c": null,
    "dasfilament_pla_plabronze_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "dasfilament_pla_bronze_1000_175_c": 60,
    "dasfilament_pla_plabronze_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_pla_bronze_1000_175_c": null,
    "dasfilament_pla_plabronze_1000_175_c": [
      50,
      70
    ]
  },
  "finish": {
    "dasfilament_pla_bronze_1000_175_c": "glossy",
    "dasfilament_pla_plabronze_1000_175_c": null
  }
}
```

### DA031: dup-b463522edccf59e7a62f6261ccfd03439a99445c2ac18bdae691181ac733d490

Status: DEFERRED; survivor `dasfilament_pla_dasfilamentgrn_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_dasfilamentgrn_1000_175_c`|`{color_name}`|`DAS FILAMENT Grün`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|
|`dasfilament_pla_plagrn_1000_175_c`|`PLA {color_name}`|`Grün`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_dasfilamentgrn_1000_175_c": 212,
    "dasfilament_pla_plagrn_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_pla_dasfilamentgrn_1000_175_c": "85ff58",
    "dasfilament_pla_plagrn_1000_175_c": "7FE200"
  },
  "extruder_temp": {
    "dasfilament_pla_dasfilamentgrn_1000_175_c": 220,
    "dasfilament_pla_plagrn_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_pla_dasfilamentgrn_1000_175_c": null,
    "dasfilament_pla_plagrn_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "dasfilament_pla_dasfilamentgrn_1000_175_c": 60,
    "dasfilament_pla_plagrn_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_pla_dasfilamentgrn_1000_175_c": null,
    "dasfilament_pla_plagrn_1000_175_c": [
      50,
      70
    ]
  }
}
```

### DA032: dup-9a9ff1b03017aa9c2588e2cb746c21760db4a49a6a3a39305ecb8a96d3180093

Status: APPROVED; survivor `dasfilament_pla_feuerrot_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_feuerrot_1000_175_c`|`{color_name}`|`Feuerrot`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|
|`dasfilament_pla_plafeuerrot_1000_175_c`|`PLA {color_name}`|`Feuerrot`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_feuerrot_1000_175_c": 212,
    "dasfilament_pla_plafeuerrot_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_pla_feuerrot_1000_175_c": "d81919",
    "dasfilament_pla_plafeuerrot_1000_175_c": "EC0000"
  },
  "extruder_temp": {
    "dasfilament_pla_feuerrot_1000_175_c": 220,
    "dasfilament_pla_plafeuerrot_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_pla_feuerrot_1000_175_c": null,
    "dasfilament_pla_plafeuerrot_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "dasfilament_pla_feuerrot_1000_175_c": 60,
    "dasfilament_pla_plafeuerrot_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_pla_feuerrot_1000_175_c": null,
    "dasfilament_pla_plafeuerrot_1000_175_c": [
      50,
      70
    ]
  }
}
```

### DA033: dup-2af6f91e88042329a61abf2d593f63a1ee97e7098a4d21d2bc1d01026ec1cf8c

Status: APPROVED; survivor `dasfilament_pla_goldv2_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_goldv2_1000_175_c`|`{color_name}`|`Gold V2`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|
|`dasfilament_pla_plagoldv2_1000_175_c`|`PLA {color_name}`|`Gold V2`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_goldv2_1000_175_c": 212,
    "dasfilament_pla_plagoldv2_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_pla_goldv2_1000_175_c": "dddd00",
    "dasfilament_pla_plagoldv2_1000_175_c": "AF7D00"
  },
  "extruder_temp": {
    "dasfilament_pla_goldv2_1000_175_c": 220,
    "dasfilament_pla_plagoldv2_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_pla_goldv2_1000_175_c": null,
    "dasfilament_pla_plagoldv2_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "dasfilament_pla_goldv2_1000_175_c": 60,
    "dasfilament_pla_plagoldv2_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_pla_goldv2_1000_175_c": null,
    "dasfilament_pla_plagoldv2_1000_175_c": [
      50,
      70
    ]
  },
  "finish": {
    "dasfilament_pla_goldv2_1000_175_c": "glossy",
    "dasfilament_pla_plagoldv2_1000_175_c": null
  }
}
```

### DA034: dup-3246d69b767ecb5d9b4aee708080430e52393fc539592bd6cd15347942bb2c41

Status: APPROVED; survivor `dasfilament_pla_grasgrn_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_grasgrn_1000_175_c`|`{color_name}`|`Grasgrün`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|
|`dasfilament_pla_plagrasgrn_1000_175_c`|`PLA {color_name}`|`Grasgrün`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_grasgrn_1000_175_c": 212,
    "dasfilament_pla_plagrasgrn_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_pla_grasgrn_1000_175_c": "35934b",
    "dasfilament_pla_plagrasgrn_1000_175_c": "26A648"
  },
  "extruder_temp": {
    "dasfilament_pla_grasgrn_1000_175_c": 220,
    "dasfilament_pla_plagrasgrn_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_pla_grasgrn_1000_175_c": null,
    "dasfilament_pla_plagrasgrn_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "dasfilament_pla_grasgrn_1000_175_c": 60,
    "dasfilament_pla_plagrasgrn_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_pla_grasgrn_1000_175_c": null,
    "dasfilament_pla_plagrasgrn_1000_175_c": [
      50,
      70
    ]
  }
}
```

### DA035: dup-93de4ac40d1e51e5d74b9bee4556a6d2ddb0ae8ea3955a0393850d4bd41e5aea

Status: APPROVED; survivor `dasfilament_pla_grau_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_grau_1000_175_c`|`{color_name}`|`Grau`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|
|`dasfilament_pla_plagrau_1000_175_c`|`PLA {color_name}`|`Grau`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_grau_1000_175_c": 212,
    "dasfilament_pla_plagrau_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_pla_grau_1000_175_c": "797979",
    "dasfilament_pla_plagrau_1000_175_c": "A2AAAD"
  },
  "extruder_temp": {
    "dasfilament_pla_grau_1000_175_c": 220,
    "dasfilament_pla_plagrau_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_pla_grau_1000_175_c": null,
    "dasfilament_pla_plagrau_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "dasfilament_pla_grau_1000_175_c": 60,
    "dasfilament_pla_plagrau_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_pla_grau_1000_175_c": null,
    "dasfilament_pla_plagrau_1000_175_c": [
      50,
      70
    ]
  }
}
```

### DA036: dup-f53dd171298d245775b36af28e7e18f68e9d8fc229e63e9c8ce10a7df9b30b02

Status: APPROVED; survivor `dasfilament_pla_himmelblau_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_himmelblau_1000_175_c`|`{color_name}`|`Himmelblau`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|
|`dasfilament_pla_plahimmelblau_1000_175_c`|`PLA {color_name}`|`Himmelblau`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_himmelblau_1000_175_c": 212,
    "dasfilament_pla_plahimmelblau_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_pla_himmelblau_1000_175_c": "1361ab",
    "dasfilament_pla_plahimmelblau_1000_175_c": "0099E6"
  },
  "extruder_temp": {
    "dasfilament_pla_himmelblau_1000_175_c": 220,
    "dasfilament_pla_plahimmelblau_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_pla_himmelblau_1000_175_c": null,
    "dasfilament_pla_plahimmelblau_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "dasfilament_pla_himmelblau_1000_175_c": 60,
    "dasfilament_pla_plahimmelblau_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_pla_himmelblau_1000_175_c": null,
    "dasfilament_pla_plahimmelblau_1000_175_c": [
      50,
      70
    ]
  }
}
```

### DA037: dup-a0c8248ccf58e3498a3ce09dccf252057d43843b97a59fb6a4b95ff7b33e27c4

Status: APPROVED; survivor `dasfilament_pla_kastanienbraun_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_kastanienbraun_1000_175_c`|`{color_name}`|`Kastanienbraun`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|
|`dasfilament_pla_plakastanienbraun_1000_175_c`|`PLA {color_name}`|`Kastanienbraun`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_kastanienbraun_1000_175_c": 212,
    "dasfilament_pla_plakastanienbraun_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_pla_kastanienbraun_1000_175_c": "6a1904",
    "dasfilament_pla_plakastanienbraun_1000_175_c": "9A491A"
  },
  "extruder_temp": {
    "dasfilament_pla_kastanienbraun_1000_175_c": 220,
    "dasfilament_pla_plakastanienbraun_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_pla_kastanienbraun_1000_175_c": null,
    "dasfilament_pla_plakastanienbraun_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "dasfilament_pla_kastanienbraun_1000_175_c": 60,
    "dasfilament_pla_plakastanienbraun_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_pla_kastanienbraun_1000_175_c": null,
    "dasfilament_pla_plakastanienbraun_1000_175_c": [
      50,
      70
    ]
  }
}
```

### DA038: dup-cc708c0954bde9724d756fcf264484bc4fb796090a5dc1c3a9e85c47bdadb6ff

Status: APPROVED; survivor `dasfilament_pla_kirschrot_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_kirschrot_1000_175_c`|`{color_name}`|`Kirschrot`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|
|`dasfilament_pla_plakirschrot_1000_175_c`|`PLA {color_name}`|`Kirschrot`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_kirschrot_1000_175_c": 212,
    "dasfilament_pla_plakirschrot_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_pla_kirschrot_1000_175_c": "e70000",
    "dasfilament_pla_plakirschrot_1000_175_c": "EC0000"
  },
  "extruder_temp": {
    "dasfilament_pla_kirschrot_1000_175_c": 220,
    "dasfilament_pla_plakirschrot_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_pla_kirschrot_1000_175_c": null,
    "dasfilament_pla_plakirschrot_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "dasfilament_pla_kirschrot_1000_175_c": 60,
    "dasfilament_pla_plakirschrot_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_pla_kirschrot_1000_175_c": null,
    "dasfilament_pla_plakirschrot_1000_175_c": [
      50,
      70
    ]
  }
}
```

### DA039: dup-1b9081d6994ff0ba70d9c89a230d39ea81b50ce4532aa0c6b716172469d8f9e2

Status: APPROVED; survivor `dasfilament_pla_knigsblau_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_knigsblau_1000_175_c`|`{color_name}`|`Königsblau`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|
|`dasfilament_pla_plaknigsblau_1000_175_c`|`PLA {color_name}`|`Königsblau`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_knigsblau_1000_175_c": 212,
    "dasfilament_pla_plaknigsblau_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_pla_knigsblau_1000_175_c": "040ea3",
    "dasfilament_pla_plaknigsblau_1000_175_c": "0353BA"
  },
  "extruder_temp": {
    "dasfilament_pla_knigsblau_1000_175_c": 220,
    "dasfilament_pla_plaknigsblau_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_pla_knigsblau_1000_175_c": null,
    "dasfilament_pla_plaknigsblau_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "dasfilament_pla_knigsblau_1000_175_c": 60,
    "dasfilament_pla_plaknigsblau_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_pla_knigsblau_1000_175_c": null,
    "dasfilament_pla_plaknigsblau_1000_175_c": [
      50,
      70
    ]
  }
}
```

### DA040: dup-69d246d885fdfb27c54e4895ff3d8d4e69fe0609ef195903cdf253bc1837f192

Status: APPROVED; survivor `dasfilament_pla_magenta_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_magenta_1000_175_c`|`{color_name}`|`Magenta`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|
|`dasfilament_pla_plamagenta_1000_175_c`|`PLA {color_name}`|`Magenta`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_magenta_1000_175_c": 212,
    "dasfilament_pla_plamagenta_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_pla_magenta_1000_175_c": "ca004d",
    "dasfilament_pla_plamagenta_1000_175_c": "F14147"
  },
  "extruder_temp": {
    "dasfilament_pla_magenta_1000_175_c": 220,
    "dasfilament_pla_plamagenta_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_pla_magenta_1000_175_c": null,
    "dasfilament_pla_plamagenta_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "dasfilament_pla_magenta_1000_175_c": 60,
    "dasfilament_pla_plamagenta_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_pla_magenta_1000_175_c": null,
    "dasfilament_pla_plamagenta_1000_175_c": [
      50,
      70
    ]
  }
}
```

### DA041: dup-7578c2bf052d3d215927003cd3f3b42fe7b8b873eb3f2a0931a76ceea10f257d

Status: APPROVED; survivor `dasfilament_pla_metallicrot_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_metallicrot_1000_175_c`|`{color_name}`|`Metallic Rot`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|
|`dasfilament_pla_plametallicrot_1000_175_c`|`PLA {color_name}`|`Metallic Rot`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_metallicrot_1000_175_c": 212,
    "dasfilament_pla_plametallicrot_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_pla_metallicrot_1000_175_c": "b11111",
    "dasfilament_pla_plametallicrot_1000_175_c": "AC1A17"
  },
  "extruder_temp": {
    "dasfilament_pla_metallicrot_1000_175_c": 220,
    "dasfilament_pla_plametallicrot_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_pla_metallicrot_1000_175_c": null,
    "dasfilament_pla_plametallicrot_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "dasfilament_pla_metallicrot_1000_175_c": 60,
    "dasfilament_pla_plametallicrot_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_pla_metallicrot_1000_175_c": null,
    "dasfilament_pla_plametallicrot_1000_175_c": [
      50,
      70
    ]
  },
  "finish": {
    "dasfilament_pla_metallicrot_1000_175_c": "glossy",
    "dasfilament_pla_plametallicrot_1000_175_c": null
  }
}
```

### DA042: dup-6c88646eb5ab4f7ad138e8f936643ca5fac697980b48a3a4da109f26c7a2104c

Status: APPROVED; survivor `dasfilament_pla_natur_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_natur_1000_175_c`|`{color_name}`|`Natur`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|
|`dasfilament_pla_planatur_1000_175_c`|`PLA {color_name}`|`Natur`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_natur_1000_175_c": 212,
    "dasfilament_pla_planatur_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_pla_natur_1000_175_c": "fffbc988",
    "dasfilament_pla_planatur_1000_175_c": "DFDFD3"
  },
  "extruder_temp": {
    "dasfilament_pla_natur_1000_175_c": 220,
    "dasfilament_pla_planatur_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_pla_natur_1000_175_c": null,
    "dasfilament_pla_planatur_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "dasfilament_pla_natur_1000_175_c": 60,
    "dasfilament_pla_planatur_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_pla_natur_1000_175_c": null,
    "dasfilament_pla_planatur_1000_175_c": [
      50,
      70
    ]
  },
  "translucent": {
    "dasfilament_pla_natur_1000_175_c": true,
    "dasfilament_pla_planatur_1000_175_c": false
  }
}
```

### DA043: dup-7eff5f3ba4137bf2435d47373a6af227ebdec7d4cb236203ce4c54f0c6ebfe69

Status: APPROVED; survivor `dasfilament_pla_neonorange_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_neonorange_1000_175_c`|`{color_name}`|`Neonorange`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|
|`dasfilament_pla_planeonorange_1000_175_c`|`PLA {color_name}`|`Neonorange`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_neonorange_1000_175_c": 212,
    "dasfilament_pla_planeonorange_1000_175_c": null
  },
  "color_hex": {
    "dasfilament_pla_neonorange_1000_175_c": "ff5500",
    "dasfilament_pla_planeonorange_1000_175_c": "FF7A33"
  },
  "extruder_temp": {
    "dasfilament_pla_neonorange_1000_175_c": 220,
    "dasfilament_pla_planeonorange_1000_175_c": null
  },
  "extruder_temp_range": {
    "dasfilament_pla_neonorange_1000_175_c": null,
    "dasfilament_pla_planeonorange_1000_175_c": [
      190,
      230
    ]
  },
  "bed_temp": {
    "dasfilament_pla_neonorange_1000_175_c": 60,
    "dasfilament_pla_planeonorange_1000_175_c": null
  },
  "bed_temp_range": {
    "dasfilament_pla_neonorange_1000_175_c": null,
    "dasfilament_pla_planeonorange_1000_175_c": [
      50,
      70
    ]
  }
}
```

### DA044: dup-1b2238537557a6f71d830ab731d1f5aa83064711241f055f1120c19006ce3e1f

Status: APPROVED; survivor `dasfilament_pla_reinorange_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_plareinorange_1000_175_c`|`PLA {color_name}`|`Reinorange`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`dasfilament_pla_reinorange_1000_175_c`|`{color_name}`|`Reinorange`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_plareinorange_1000_175_c": null,
    "dasfilament_pla_reinorange_1000_175_c": 212
  },
  "color_hex": {
    "dasfilament_pla_plareinorange_1000_175_c": "FF5F2E",
    "dasfilament_pla_reinorange_1000_175_c": "ca4000"
  },
  "extruder_temp": {
    "dasfilament_pla_plareinorange_1000_175_c": null,
    "dasfilament_pla_reinorange_1000_175_c": 220
  },
  "extruder_temp_range": {
    "dasfilament_pla_plareinorange_1000_175_c": [
      190,
      230
    ],
    "dasfilament_pla_reinorange_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_pla_plareinorange_1000_175_c": null,
    "dasfilament_pla_reinorange_1000_175_c": 60
  },
  "bed_temp_range": {
    "dasfilament_pla_plareinorange_1000_175_c": [
      50,
      70
    ],
    "dasfilament_pla_reinorange_1000_175_c": null
  }
}
```

### DA045: dup-88c05ba43f545d07a405898075dda2950e4a15aef631a7ff74838caafdbccb8e

Status: APPROVED; survivor `dasfilament_pla_schwarz_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_plaschwarz_1000_175_c`|`PLA {color_name}`|`Schwarz`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`dasfilament_pla_schwarz_1000_175_c`|`{color_name}`|`Schwarz`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_plaschwarz_1000_175_c": null,
    "dasfilament_pla_schwarz_1000_175_c": 212
  },
  "extruder_temp": {
    "dasfilament_pla_plaschwarz_1000_175_c": null,
    "dasfilament_pla_schwarz_1000_175_c": 220
  },
  "extruder_temp_range": {
    "dasfilament_pla_plaschwarz_1000_175_c": [
      190,
      230
    ],
    "dasfilament_pla_schwarz_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_pla_plaschwarz_1000_175_c": null,
    "dasfilament_pla_schwarz_1000_175_c": 60
  },
  "bed_temp_range": {
    "dasfilament_pla_plaschwarz_1000_175_c": [
      50,
      70
    ],
    "dasfilament_pla_schwarz_1000_175_c": null
  }
}
```

### DA046: dup-c9f73c3b9135838402d44dbc1d436e95b339ea30e49b6287069484d9967faa69

Status: APPROVED; survivor `dasfilament_pla_silber_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_plasilber_1000_175_c`|`PLA {color_name}`|`Silber`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`dasfilament_pla_silber_1000_175_c`|`{color_name}`|`Silber`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_plasilber_1000_175_c": null,
    "dasfilament_pla_silber_1000_175_c": 212
  },
  "color_hex": {
    "dasfilament_pla_plasilber_1000_175_c": "C5C5BF",
    "dasfilament_pla_silber_1000_175_c": "a2a2a2"
  },
  "extruder_temp": {
    "dasfilament_pla_plasilber_1000_175_c": null,
    "dasfilament_pla_silber_1000_175_c": 220
  },
  "extruder_temp_range": {
    "dasfilament_pla_plasilber_1000_175_c": [
      190,
      230
    ],
    "dasfilament_pla_silber_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_pla_plasilber_1000_175_c": null,
    "dasfilament_pla_silber_1000_175_c": 60
  },
  "bed_temp_range": {
    "dasfilament_pla_plasilber_1000_175_c": [
      50,
      70
    ],
    "dasfilament_pla_silber_1000_175_c": null
  },
  "finish": {
    "dasfilament_pla_plasilber_1000_175_c": null,
    "dasfilament_pla_silber_1000_175_c": "glossy"
  }
}
```

### DA047: dup-d8ceb31665c61ff3f3e3d957e3b8df274f6dbee9660c5c72b040d89a341fe1af

Status: APPROVED; survivor `dasfilament_pla_sonnengelb_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_plasonnengelb_1000_175_c`|`PLA {color_name}`|`Sonnengelb`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`dasfilament_pla_sonnengelb_1000_175_c`|`{color_name}`|`Sonnengelb`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_plasonnengelb_1000_175_c": null,
    "dasfilament_pla_sonnengelb_1000_175_c": 212
  },
  "color_hex": {
    "dasfilament_pla_plasonnengelb_1000_175_c": "FADB24",
    "dasfilament_pla_sonnengelb_1000_175_c": "ffd500"
  },
  "extruder_temp": {
    "dasfilament_pla_plasonnengelb_1000_175_c": null,
    "dasfilament_pla_sonnengelb_1000_175_c": 220
  },
  "extruder_temp_range": {
    "dasfilament_pla_plasonnengelb_1000_175_c": [
      190,
      230
    ],
    "dasfilament_pla_sonnengelb_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_pla_plasonnengelb_1000_175_c": null,
    "dasfilament_pla_sonnengelb_1000_175_c": 60
  },
  "bed_temp_range": {
    "dasfilament_pla_plasonnengelb_1000_175_c": [
      50,
      70
    ],
    "dasfilament_pla_sonnengelb_1000_175_c": null
  }
}
```

### DA048: dup-925db702cec7c69fab892e07dc429b0e66bd9530085adbc5fc0695ff67e53ab7

Status: APPROVED; survivor `dasfilament_pla_tannengrn_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_platannengrn_1000_175_c`|`PLA {color_name}`|`Tannengrün`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`dasfilament_pla_tannengrn_1000_175_c`|`{color_name}`|`Tannengrün`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_platannengrn_1000_175_c": null,
    "dasfilament_pla_tannengrn_1000_175_c": 212
  },
  "color_hex": {
    "dasfilament_pla_platannengrn_1000_175_c": "02776F",
    "dasfilament_pla_tannengrn_1000_175_c": "23514f"
  },
  "extruder_temp": {
    "dasfilament_pla_platannengrn_1000_175_c": null,
    "dasfilament_pla_tannengrn_1000_175_c": 220
  },
  "extruder_temp_range": {
    "dasfilament_pla_platannengrn_1000_175_c": [
      190,
      230
    ],
    "dasfilament_pla_tannengrn_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_pla_platannengrn_1000_175_c": null,
    "dasfilament_pla_tannengrn_1000_175_c": 60
  },
  "bed_temp_range": {
    "dasfilament_pla_platannengrn_1000_175_c": [
      50,
      70
    ],
    "dasfilament_pla_tannengrn_1000_175_c": null
  }
}
```

### DA049: dup-5788a32a9e6e87fb5a99637ab15dedd9d7905f91863073281e164205bc9c7635

Status: APPROVED; survivor `dasfilament_pla_thermo-rot_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_plathermo-rot_1000_175_c`|`PLA {color_name}`|`Thermo-Rot`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`dasfilament_pla_thermo-rot_1000_175_c`|`{color_name}`|`Thermo-Rot`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_plathermo-rot_1000_175_c": null,
    "dasfilament_pla_thermo-rot_1000_175_c": 212
  },
  "color_hex": {
    "dasfilament_pla_plathermo-rot_1000_175_c": "EC0000",
    "dasfilament_pla_thermo-rot_1000_175_c": "bd0000"
  },
  "extruder_temp": {
    "dasfilament_pla_plathermo-rot_1000_175_c": null,
    "dasfilament_pla_thermo-rot_1000_175_c": 220
  },
  "extruder_temp_range": {
    "dasfilament_pla_plathermo-rot_1000_175_c": [
      190,
      230
    ],
    "dasfilament_pla_thermo-rot_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_pla_plathermo-rot_1000_175_c": null,
    "dasfilament_pla_thermo-rot_1000_175_c": 60
  },
  "bed_temp_range": {
    "dasfilament_pla_plathermo-rot_1000_175_c": [
      50,
      70
    ],
    "dasfilament_pla_thermo-rot_1000_175_c": null
  }
}
```

### DA050: dup-ed6c288ca4b209532175ec18d5b4446c6da897b63ff5b96e0701b266beb12cc4

Status: DEFERRED; survivor `dasfilament_pla_toms3dinfinityblue_1000_175_c`; Rule 5 physical line/color decomposition mismatch.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_platoms3dinfinityblue_1000_175_c`|`PLA Toms3D {color_name}`|`Infinity Blue`|{"source_file": "dasfilament.json", "definition_index": 8, "weights": 1, "diameters": 1, "colors": 1, "compiled_records": 1} / False|
|`dasfilament_pla_toms3dinfinityblue_1000_175_c`|`{color_name}`|`Toms3D Infinity Blue`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_platoms3dinfinityblue_1000_175_c": null,
    "dasfilament_pla_toms3dinfinityblue_1000_175_c": 212
  },
  "color_hex": {
    "dasfilament_pla_platoms3dinfinityblue_1000_175_c": "0099E6",
    "dasfilament_pla_toms3dinfinityblue_1000_175_c": "007fd4"
  },
  "extruder_temp": {
    "dasfilament_pla_platoms3dinfinityblue_1000_175_c": null,
    "dasfilament_pla_toms3dinfinityblue_1000_175_c": 220
  },
  "extruder_temp_range": {
    "dasfilament_pla_platoms3dinfinityblue_1000_175_c": [
      190,
      230
    ],
    "dasfilament_pla_toms3dinfinityblue_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_pla_platoms3dinfinityblue_1000_175_c": null,
    "dasfilament_pla_toms3dinfinityblue_1000_175_c": 60
  },
  "bed_temp_range": {
    "dasfilament_pla_platoms3dinfinityblue_1000_175_c": [
      50,
      70
    ],
    "dasfilament_pla_toms3dinfinityblue_1000_175_c": null
  }
}
```

### DA051: dup-bccbd9a162ceb0d3d943e60dcd0b9d24f10c028dbe1c254eb16d3a4079e1386a

Status: APPROVED; survivor `dasfilament_pla_transluzentblau_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_platransluzent-blau_1000_175_c`|`PLA {color_name}`|`Transluzent-Blau`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`dasfilament_pla_transluzentblau_1000_175_c`|`{color_name}`|`Transluzent Blau`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_platransluzent-blau_1000_175_c": null,
    "dasfilament_pla_transluzentblau_1000_175_c": 212
  },
  "color_hex": {
    "dasfilament_pla_platransluzent-blau_1000_175_c": "0078BF",
    "dasfilament_pla_transluzentblau_1000_175_c": "2437b988"
  },
  "extruder_temp": {
    "dasfilament_pla_platransluzent-blau_1000_175_c": null,
    "dasfilament_pla_transluzentblau_1000_175_c": 220
  },
  "extruder_temp_range": {
    "dasfilament_pla_platransluzent-blau_1000_175_c": [
      190,
      230
    ],
    "dasfilament_pla_transluzentblau_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_pla_platransluzent-blau_1000_175_c": null,
    "dasfilament_pla_transluzentblau_1000_175_c": 60
  },
  "bed_temp_range": {
    "dasfilament_pla_platransluzent-blau_1000_175_c": [
      50,
      70
    ],
    "dasfilament_pla_transluzentblau_1000_175_c": null
  }
}
```

### DA052: dup-fa0d7533625f6cdff48218cb94af1e510f3a4b131b0226807d6a51c3bff494d3

Status: APPROVED; survivor `dasfilament_pla_transluzentgrn_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_platransluzent-grn_1000_175_c`|`PLA {color_name}`|`Transluzent-Grün`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`dasfilament_pla_transluzentgrn_1000_175_c`|`{color_name}`|`Transluzent Grün`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_platransluzent-grn_1000_175_c": null,
    "dasfilament_pla_transluzentgrn_1000_175_c": 212
  },
  "color_hex": {
    "dasfilament_pla_platransluzent-grn_1000_175_c": "97D7D0",
    "dasfilament_pla_transluzentgrn_1000_175_c": "44b49c88"
  },
  "extruder_temp": {
    "dasfilament_pla_platransluzent-grn_1000_175_c": null,
    "dasfilament_pla_transluzentgrn_1000_175_c": 220
  },
  "extruder_temp_range": {
    "dasfilament_pla_platransluzent-grn_1000_175_c": [
      190,
      230
    ],
    "dasfilament_pla_transluzentgrn_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_pla_platransluzent-grn_1000_175_c": null,
    "dasfilament_pla_transluzentgrn_1000_175_c": 60
  },
  "bed_temp_range": {
    "dasfilament_pla_platransluzent-grn_1000_175_c": [
      50,
      70
    ],
    "dasfilament_pla_transluzentgrn_1000_175_c": null
  }
}
```

### DA053: dup-2305c56f263957b48c02fb8b6fe86e92293edb40678313087542315b2651a7b5

Status: APPROVED; survivor `dasfilament_pla_wei_1000_175_c`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`dasfilament_pla_plawei_1000_175_c`|`PLA {color_name}`|`Weiß`|{"source_file": "dasfilament.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 31, "compiled_records": 31} / False|
|`dasfilament_pla_wei_1000_175_c`|`{color_name}`|`Weiß`|{"source_file": "dasfilament.json", "definition_index": 0, "weights": 1, "diameters": 1, "colors": 27, "compiled_records": 27} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "spool_weight": {
    "dasfilament_pla_plawei_1000_175_c": null,
    "dasfilament_pla_wei_1000_175_c": 212
  },
  "color_hex": {
    "dasfilament_pla_plawei_1000_175_c": "FFFFFF",
    "dasfilament_pla_wei_1000_175_c": "ffffff"
  },
  "extruder_temp": {
    "dasfilament_pla_plawei_1000_175_c": null,
    "dasfilament_pla_wei_1000_175_c": 220
  },
  "extruder_temp_range": {
    "dasfilament_pla_plawei_1000_175_c": [
      190,
      230
    ],
    "dasfilament_pla_wei_1000_175_c": null
  },
  "bed_temp": {
    "dasfilament_pla_plawei_1000_175_c": null,
    "dasfilament_pla_wei_1000_175_c": 60
  },
  "bed_temp_range": {
    "dasfilament_pla_plawei_1000_175_c": [
      50,
      70
    ],
    "dasfilament_pla_wei_1000_175_c": null
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

- `dasfilament_pla_schwarzmatt_1000_175_c` — Schwarz matt
- `dasfilament_pla_tonweimatt_1000_175_c` — Tonweiß matt
- `dasfilament_pla_schwarz-refill_1000_175_c` — Schwarz - Refill
- `dasfilament_pla_schwarzmatt-refill_1000_175_c` — Schwarz matt - Refill
- `dasfilament_pla_goldv2-refill_1000_175_c` — Gold V2 - Refill
- `dasfilament_pla_anthrazitv2-refill_1000_175_c` — Anthrazit V2 - Refill
- `dasfilament_pla_tonweimatt-refill_1000_175_c` — Tonweiß matt - Refill
- `dasfilament_pla_metallicrot-refill_1000_175_c` — Metallic Rot - Refill
- `dasfilament_pla_toms3dinfinityblue-refill_1000_175_c` — Toms3D Infinity Blue - Refill
- `dasfilament_pla_magenta-refill_1000_175_c` — Magenta - Refill
- `dasfilament_pla_kirschrot-refill_1000_175_c` — Kirschrot - Refill
- `dasfilament_pla_transluzentblau-refill_1000_175_c` — Transluzent Blau - Refill
- `dasfilament_pla_dasfilamentgrn-refill_1000_175_c` — DAS FILAMENT Grün - Refill
- `dasfilament_pla_bronze-refill_1000_175_c` — Bronze - Refill
- `dasfilament_pla_silber-refill_1000_175_c` — Silber - Refill
- `dasfilament_pla_thermo-rot-refill_1000_175_c` — Thermo-Rot - Refill
- `dasfilament_pla_neonorange-refill_1000_175_c` — Neonorange - Refill
- `dasfilament_pla_feuerrot-refill_1000_175_c` — Feuerrot - Refill
- `dasfilament_pla_knigsblau-refill_1000_175_c` — Königsblau - Refill
- `dasfilament_pla_grasgrn-refill_1000_175_c` — Grasgrün - Refill
- `dasfilament_pla_reinorange-refill_1000_175_c` — Reinorange - Refill
- `dasfilament_pla_wei-refill_1000_175_c` — Weiß - Refill
- `dasfilament_pla_tannengrn-refill_1000_175_c` — Tannengrün - Refill
- `dasfilament_pla_transluzentgrn-refill_1000_175_c` — Transluzent Grün - Refill
- `dasfilament_pla_himmelblau-refill_1000_175_c` — Himmelblau - Refill
- `dasfilament_pla_grau-refill_1000_175_c` — Grau - Refill
- `dasfilament_pla_kastanienbraun-refill_1000_175_c` — Kastanienbraun - Refill
- `dasfilament_pla_sonnengelb-refill_1000_175_c` — Sonnengelb - Refill
- `dasfilament_pla_natur-refill_1000_175_c` — Natur - Refill
- `dasfilament_petg_transl.wassergrn_1000_175_c` — Transl. Wassergrün
- `dasfilament_petg_schwarz-refill_1000_175_c` — Schwarz - Refill
- `dasfilament_petg_flammschutzschwarz-refill_1000_175_c` — Flammschutz Schwarz - Refill
- `dasfilament_petg_alu-silber-refill_1000_175_c` — Alu-silber - Refill
- `dasfilament_petg_silber-refill_1000_175_c` — Silber - Refill
- `dasfilament_petg_anthrazitv2-refill_1000_175_c` — Anthrazit V2 - Refill
- `dasfilament_petg_beige-refill_1000_175_c` — Beige - Refill
- `dasfilament_petg_militr-grn-refill_1000_175_c` — Militär-Grün - Refill
- `dasfilament_petg_burntcopper-refill_1000_175_c` — Burnt Copper - Refill
- `dasfilament_petg_sturmgrau-refill_1000_175_c` — Sturmgrau - Refill
- `dasfilament_petg_metallicblau-refill_1000_175_c` — Metallic Blau - Refill
- `dasfilament_petg_lila-refill_1000_175_c` — Lila - Refill
- `dasfilament_petg_rubinrot-refill_1000_175_c` — Rubinrot - Refill
- `dasfilament_petg_transparentblau-refill_1000_175_c` — Transparent Blau - Refill
- `dasfilament_petg_melonengelb-refill_1000_175_c` — Melonengelb - Refill
- `dasfilament_petg_maisgelb-refill_1000_175_c` — Maisgelb - Refill
- `dasfilament_petg_transparentrot-refill_1000_175_c` — Transparent Rot - Refill
- `dasfilament_petg_transl.wassergrn-refill_1000_175_c` — Transl. Wassergrün - Refill
- `dasfilament_petg_transluzentneongrn-refill_1000_175_c` — Transluzent Neongrün - Refill
- `dasfilament_petg_transluzentneongelb-refill_1000_175_c` — Transluzent Neongelb - Refill
- `dasfilament_petg_leuchtorange-refill_1000_175_c` — Leuchtorange - Refill
- `dasfilament_petg_feuerrot-refill_1000_175_c` — Feuerrot - Refill
- `dasfilament_petg_opalgrn-refill_1000_175_c` — Opalgrün - Refill
- `dasfilament_petg_grasgrn-refill_1000_175_c` — Grasgrün - Refill
- `dasfilament_petg_wei-refill_1000_175_c` — Weiß - Refill
- `dasfilament_petg_transparentneongrn-refill_1000_175_c` — Transparent Neongrün - Refill
- `dasfilament_petg_schiefergrau-refill_1000_175_c` — Schiefergrau - Refill
- `dasfilament_petg_blau-refill_1000_175_c` — Blau - Refill
- `dasfilament_petg_saphirblau-refill_1000_175_c` — Saphirblau - Refill
- `dasfilament_petg_natur-refill_1000_175_c` — Natur - Refill
- `dasfilament_petg_petgral7016_1000_175_c` — PETG RAL 7016
- `dasfilament_petg_petgtransluzentwassergrn_1000_175_c` — PETG Transluzent Wassergrün
- `dasfilament_pla_glowplaglow-grnv2_1000_175_c` — Glow PLA Glow-Grün V2
- `dasfilament_pla_matteplaschwarzmatt_1000_175_c` — Matte PLA Schwarz matt
- `dasfilament_pla_matteplatonweimatt_1000_175_c` — Matte PLA Tonweiß matt
- `dasfilament_pla_plabluepearl_1000_175_c` — PLA Blue Pearl
- `dasfilament_pla_plagrngold_1000_175_c` — PLA Grüngold
- `dasfilament_pla_plalavendel_1000_175_c` — PLA Lavendel
- `dasfilament_pla_plamulticolorgalaxy_1000_175_c` — PLA Multicolor Galaxy
- `dasfilament_pla_plamulticolorpolarlicht_1000_175_c` — PLA Multicolor Polarlicht
- `dasfilament_pla_plapfefferminze_1000_175_c` — PLA Pfefferminze
- `dasfilament_pla_plavanille_1000_175_c` — PLA Vanille
- `dasfilament_tpu_tpuv2flexibelnatur_1000_175_c` — TPU V2 Flexibel Natur
- `dasfilament_tpu_tpuv2flexibelschwarz_1000_175_c` — TPU V2 Flexibel Schwarz
- `dasfilament_tpu_tpuv2flexibelwei_1000_175_c` — TPU V2 Flexibel Wei
