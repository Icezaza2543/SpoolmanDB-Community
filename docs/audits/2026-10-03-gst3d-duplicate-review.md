# gst3d duplicate migration review

Base `41faacca40e01ac50bb86f3321700682eeb505d9`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `56921a32d195c1fd1c5d60c16fefd3f53425d01c986aa9d80e602d56e0a58089`.

## Authorization and result

{"groups": 4, "approved_groups": 4, "retired": 4, "deferred": 0, "hard_stops": 0, "before_count": 51719, "after_count": 51715, "brand_before": 186, "brand_after": 182, "registry_before": 1715, "registry_after": 1719, "metadata_fields_changed": 2, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Four Rule1 strict duplicates. Exact target PETG density corrected1.26→manufacturer approximate1.27 nominal; existing240/70 remains valid. ABS240/90 corroborated by current calibration, density1.04 unverified retained. RetiringABS1.25 is not used. No identifiers or packaging/tare edits.

This is an intentional breaking catalog migration. Existing Spoolman spools retain local data; retired external catalog lookups do not redirect automatically. Packaging, tare, survivor and unique identities remain unchanged.

## Current first-party evidence

- {"url": "https://gst3d.eu/products/petg-transluscent", "density": "approximately1.27", "note": "Current product endpoint explicitly includes ordinary White and Black1kg/1.75 variants (8437028773432/8437028773425); the legacy transluscent URL slug is not a translucent-only product. Existing source identifiers are not enriched or altered.", "nozzle": [220, 250], "bed": [70, 90]}
- {"url": "https://gst3d.eu/pages/calibracion", "material": "ABS", "nozzle": [230, 250], "bed": [90, 110]}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|
|`gst3d_abs_absblack_1000_175_p`|`gst3d_abs_black_1000_175_p`|`gst3d.json::GST3D::ABS {color_name}::ABS Black::ABS::1000::1.75::plastic::False`|
|`gst3d_abs_abswhite_1000_175_p`|`gst3d_abs_white_1000_175_p`|`gst3d.json::GST3D::ABS {color_name}::ABS White::ABS::1000::1.75::plastic::False`|
|`gst3d_petg_petgblack_1000_175_p`|`gst3d_petg_black_1000_175_p`|`gst3d.json::GST3D::PETG {color_name}::PETG Black::PETG::1000::1.75::plastic::False`|
|`gst3d_petg_petgwhite_1000_175_p`|`gst3d_petg_white_1000_175_p`|`gst3d.json::GST3D::PETG {color_name}::PETG White::PETG::1000::1.75::plastic::False`|

## Per-group decisions and unresolved metadata

### GS001: dup-d2f8e8de6153a24c18c4850f1a7c0f59775d3ca5f9a3b05c55cdd470007868da

Status: APPROVED; survivor `gst3d_abs_black_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gst3d_abs_absblack_1000_175_p`|`ABS {color_name}`|`Black`|{"source_file": "gst3d.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / False|
|`gst3d_abs_black_1000_175_p`|`{color_name}`|`Black`|{"source_file": "gst3d.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "gst3d_abs_absblack_1000_175_p": 1.25,
    "gst3d_abs_black_1000_175_p": 1.04
  },
  "spool_weight": {
    "gst3d_abs_absblack_1000_175_p": null,
    "gst3d_abs_black_1000_175_p": 200
  },
  "bed_temp": {
    "gst3d_abs_absblack_1000_175_p": 100,
    "gst3d_abs_black_1000_175_p": 90
  },
  "country_of_origin": {
    "gst3d_abs_absblack_1000_175_p": "ES",
    "gst3d_abs_black_1000_175_p": "AR"
  }
}
```

### GS002: dup-e32d235f3158dc1874c2956c23ea0cda003adbc77a4a524219bc17b407f9e4d3

Status: APPROVED; survivor `gst3d_abs_white_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gst3d_abs_abswhite_1000_175_p`|`ABS {color_name}`|`White`|{"source_file": "gst3d.json", "definition_index": 7, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / False|
|`gst3d_abs_white_1000_175_p`|`{color_name}`|`White`|{"source_file": "gst3d.json", "definition_index": 5, "weights": 1, "diameters": 1, "colors": 2, "compiled_records": 2} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "gst3d_abs_abswhite_1000_175_p": 1.25,
    "gst3d_abs_white_1000_175_p": 1.04
  },
  "spool_weight": {
    "gst3d_abs_abswhite_1000_175_p": null,
    "gst3d_abs_white_1000_175_p": 200
  },
  "bed_temp": {
    "gst3d_abs_abswhite_1000_175_p": 100,
    "gst3d_abs_white_1000_175_p": 90
  },
  "country_of_origin": {
    "gst3d_abs_abswhite_1000_175_p": "ES",
    "gst3d_abs_white_1000_175_p": "AR"
  }
}
```

### GS003: dup-f9269bf6eeddcfb023c2fb8a56589b773332e13659674affda5f3d1e7211039a

Status: APPROVED; survivor `gst3d_petg_black_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gst3d_petg_black_1000_175_p`|`{color_name}`|`Black`|{"source_file": "gst3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / True|
|`gst3d_petg_petgblack_1000_175_p`|`PETG {color_name}`|`Black`|{"source_file": "gst3d.json", "definition_index": 9, "weights": 3, "diameters": 1, "colors": 3, "compiled_records": 9} / False|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "gst3d_petg_black_1000_175_p": 1.26,
    "gst3d_petg_petgblack_1000_175_p": 1.25
  },
  "spool_weight": {
    "gst3d_petg_black_1000_175_p": 200,
    "gst3d_petg_petgblack_1000_175_p": null
  },
  "bed_temp": {
    "gst3d_petg_black_1000_175_p": 70,
    "gst3d_petg_petgblack_1000_175_p": 75
  },
  "country_of_origin": {
    "gst3d_petg_black_1000_175_p": "AR",
    "gst3d_petg_petgblack_1000_175_p": "ES"
  }
}
```

### GS004: dup-d2bd0bd2bbd7396d934ffbd4c7ee93800265ece22668811893426db34a5e5546

Status: APPROVED; survivor `gst3d_petg_white_1000_175_p`; Rule 1.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`gst3d_petg_petgwhite_1000_175_p`|`PETG {color_name}`|`White`|{"source_file": "gst3d.json", "definition_index": 9, "weights": 3, "diameters": 1, "colors": 3, "compiled_records": 9} / False|
|`gst3d_petg_white_1000_175_p`|`{color_name}`|`White`|{"source_file": "gst3d.json", "definition_index": 1, "weights": 1, "diameters": 1, "colors": 3, "compiled_records": 3} / True|

Exact physical identity matches; authorized catalog survivor priority

Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "density": {
    "gst3d_petg_petgwhite_1000_175_p": 1.25,
    "gst3d_petg_white_1000_175_p": 1.26
  },
  "spool_weight": {
    "gst3d_petg_petgwhite_1000_175_p": null,
    "gst3d_petg_white_1000_175_p": 200
  },
  "bed_temp": {
    "gst3d_petg_petgwhite_1000_175_p": 75,
    "gst3d_petg_white_1000_175_p": 70
  },
  "country_of_origin": {
    "gst3d_petg_petgwhite_1000_175_p": "ES",
    "gst3d_petg_white_1000_175_p": "AR"
  }
}
```

## Exact metadata and identifier decisions

```json
{
  "metadata": [
    {
      "id": "gst3d_petg_white_1000_175_p",
      "values": {
        "density": 1.27
      },
      "source": "https://gst3d.eu/products/petg-transluscent",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    },
    {
      "id": "gst3d_petg_black_1000_175_p",
      "values": {
        "density": 1.27
      },
      "source": "https://gst3d.eu/products/petg-transluscent",
      "lot": "current exact product-line manufacturer recommendations; no packaging/tare inference",
      "same_variant": true,
      "approved": true
    }
  ],
  "transfers": []
}
```

## Preserved out-of-scope IDs

- `gst3d_pla+_white_1000_175_p` — White
- `gst3d_pla+_black_1000_175_p` — Black
- `gst3d_pla+_yellow_1000_175_p` — Yellow
- `gst3d_pla+_violet_1000_175_p` — Violet
- `gst3d_pla+_silver/grey_1000_175_p` — Silver/Grey
- `gst3d_pla+_pinkpanther_1000_175_p` — Pink Panther
- `gst3d_pla+_orange_1000_175_p` — Orange
- `gst3d_pla+_mustard_1000_175_p` — Mustard
- `gst3d_pla+_metallicbronze_1000_175_p` — Metallic Bronze
- `gst3d_pla+_mellowyellow_1000_175_p` — Mellow Yellow
- `gst3d_pla+_lightpink_1000_175_p` — Light Pink
- `gst3d_pla+_lightblue_1000_175_p` — Light Blue
- `gst3d_pla+_iceblue_1000_175_p` — Ice Blue
- `gst3d_pla+_gold_1000_175_p` — Gold
- `gst3d_pla+_fuchsia_1000_175_p` — Fuchsia
- `gst3d_pla+_fluorescentyellow_1000_175_p` — Fluorescent Yellow
- `gst3d_pla+_fluorescentorange_1000_175_p` — Fluorescent Orange
- `gst3d_pla+_fluorescentgreen_1000_175_p` — Fluorescent Green
- `gst3d_pla+_firefly(glowinthedark)_1000_175_p` — Firefly (Glow in the dark)
- `gst3d_pla+_crystal/clear_1000_175_p` — Crystal/Clear
- `gst3d_pla+_brown_1000_175_p` — Brown
- `gst3d_pla+_armygreen_1000_175_p` — Army Green
- `gst3d_pla+_aquamarine_1000_175_p` — Aquamarine
- `gst3d_pla+_applegreen_1000_175_p` — Apple Green
- `gst3d_pla+_marble_1000_175_p` — Marble
- `gst3d_pla+_blue_1000_175_p` — Blue
- `gst3d_pla+_red_1000_175_p` — Red
- `gst3d_pla+_brightsilver_1000_175_p` — Bright Silver
- `gst3d_pla+_brightred_1000_175_p` — Bright Red
- `gst3d_pla+_brightgreen_1000_175_p` — Bright Green
- `gst3d_pla+_brightgold_1000_175_p` — Bright Gold
- `gst3d_pla+_brightblue_1000_175_p` — Bright Blue
- `gst3d_pla+_brightblack_1000_175_p` — Bright Black
- `gst3d_petg_crystal/clear_1000_175_p` — Crystal/Clear
- `gst3d_petg-cf_blackcarbonfiber_1000_175_p` — Black Carbon Fiber
- `gst3d_tpu_black93a_1000_175_p` — Black 93A
- `gst3d_tpu_silver93a_1000_175_p` — Silver 93A
- `gst3d_tpu_applegreen93a_1000_175_p` — Apple Green 93A
- `gst3d_tpu_blue93a_1000_175_p` — Blue 93A
- `gst3d_tpu_red93a_1000_175_p` — Red 93A
- `gst3d_tpu_white93a_1000_175_p` — White 93A
- `gst3d_pla_silkblue_1000_175_p` — Silk Blue
- `gst3d_pla_silkgold_1000_175_p` — Silk Gold
- `gst3d_pla_silkgoldrose_1000_175_p` — Silk Gold Rose
- `gst3d_pla_silkgreen_1000_175_p` — Silk Green
- `gst3d_pla_silksand_1000_175_p` — Silk Sand
- `gst3d_pla_silkaluminium_1000_175_p` — Silk Aluminium
- `gst3d_pla_silkfuchsia_1000_175_p` — Silk Fuchsia
- `gst3d_pla_silkgraphite_1000_175_p` — Silk Graphite
- `gst3d_pla_silkpeach_1000_175_p` — Silk Peach
- `gst3d_pla_silkpurple_1000_175_p` — Silk Purple
- `gst3d_pla_silkred_1000_175_p` — Silk Red
- `gst3d_asa_black_900_175_p` — Black
- `gst3d_asa_white_900_175_p` — White
- `gst3d_asa_asa900grsblack_1000_175_p` — ASA 900Grs Black
- `gst3d_asa_asa900grswhite_1000_175_p` — ASA 900Grs White
- `gst3d_petg_petgcrystal_1000_175_p` — PETG Crystal
- `gst3d_petg_petgblack_3500_175_p` — PETG Black
- `gst3d_petg_petgcrystal_3500_175_p` — PETG Crystal
- `gst3d_petg_petgwhite_3500_175_p` — PETG White
- `gst3d_petg_petgblack_5000_175_p` — PETG Black
- `gst3d_petg_petgcrystal_5000_175_p` — PETG Crystal
- `gst3d_petg_petgwhite_5000_175_p` — PETG White
- `gst3d_petg_petg-cfcarbonfiber_1000_175_p` — PETG-CF Carbon fiber
- `gst3d_petg_petg-cfcarbonfiber_3500_175_p` — PETG-CF Carbon fiber
- `gst3d_petg_petg-cfcarbonfiber_5000_175_p` — PETG-CF Carbon fiber
- `gst3d_petg_petgtranslucentbluetranslucent_1000_175_p` — PETG translucent Blue translucent
- `gst3d_petg_petgtranslucentgreentranslucent_1000_175_p` — PETG translucent Green translucent
- `gst3d_petg_petgtranslucentredtranslucent_1000_175_p` — PETG translucent Red translucent
- `gst3d_petg_petgtranslucentyellowtranslucent_1000_175_p` — PETG translucent Yellow translucent
- `gst3d_pla_brightpla+spaceblack_1000_175_p` — Bright Pla+ Space black
- `gst3d_pla_brightpla+spaceblue_1000_175_p` — Bright Pla+ Space Blue
- `gst3d_pla_brightpla+spacegold_1000_175_p` — Bright Pla+ Space gold
- `gst3d_pla_brightpla+spacegreen_1000_175_p` — Bright Pla+ Space green
- `gst3d_pla_brightpla+spacered_1000_175_p` — Bright Pla+ Space red
- `gst3d_pla_brightpla+spacesilver_1000_175_p` — Bright Pla+ Space Silver
- `gst3d_pla_pla+applegreen_1000_175_p` — PLA+ Apple green
- `gst3d_pla_pla+armygreen_1000_175_p` — PLA+ Army green
- `gst3d_pla_pla+black_1000_175_p` — PLA+ Black
- `gst3d_pla_pla+blue_1000_175_p` — PLA+ Blue
- `gst3d_pla_pla+bonewhite_1000_175_p` — PLA+ Bone white
- `gst3d_pla_pla+bronze_1000_175_p` — PLA+ Bronze
- `gst3d_pla_pla+brown_1000_175_p` — PLA+ Brown
- `gst3d_pla_pla+crystal_1000_175_p` — PLA+ Crystal
- `gst3d_pla_pla+fuchsia_1000_175_p` — PLA+ Fuchsia
- `gst3d_pla_pla+gold_1000_175_p` — PLA+ Gold
- `gst3d_pla_pla+khaki_1000_175_p` — PLA+ Khaki
- `gst3d_pla_pla+lightblue_1000_175_p` — PLA+ Light Blue
- `gst3d_pla_pla+lightbrown_1000_175_p` — PLA+ Light Brown
- `gst3d_pla_pla+lightpink_1000_175_p` — PLA+ Light Pink
- `gst3d_pla_pla+ocre_1000_175_p` — PLA+ Ocre
- `gst3d_pla_pla+olivegreen_1000_175_p` — PLA+ Olive green
- `gst3d_pla_pla+orange_1000_175_p` — PLA+ Orange
- `gst3d_pla_pla+pinkpanter_1000_175_p` — PLA+ Pink Panter
- `gst3d_pla_pla+red_1000_175_p` — PLA+ Red
- `gst3d_pla_pla+silver_1000_175_p` — PLA+ Silver
- `gst3d_pla_pla+violet_1000_175_p` — PLA+ Violet
- `gst3d_pla_pla+white_1000_175_p` — PLA+ White
- `gst3d_pla_pla+yellow_1000_175_p` — PLA+ Yellow
- `gst3d_pla_pla+applegreen_3500_175_p` — PLA+ Apple green
- `gst3d_pla_pla+armygreen_3500_175_p` — PLA+ Army green
- `gst3d_pla_pla+black_3500_175_p` — PLA+ Black
- `gst3d_pla_pla+blue_3500_175_p` — PLA+ Blue
- `gst3d_pla_pla+bonewhite_3500_175_p` — PLA+ Bone white
- `gst3d_pla_pla+bronze_3500_175_p` — PLA+ Bronze
- `gst3d_pla_pla+brown_3500_175_p` — PLA+ Brown
- `gst3d_pla_pla+crystal_3500_175_p` — PLA+ Crystal
- `gst3d_pla_pla+fuchsia_3500_175_p` — PLA+ Fuchsia
- `gst3d_pla_pla+gold_3500_175_p` — PLA+ Gold
- `gst3d_pla_pla+khaki_3500_175_p` — PLA+ Khaki
- `gst3d_pla_pla+lightblue_3500_175_p` — PLA+ Light Blue
- `gst3d_pla_pla+lightbrown_3500_175_p` — PLA+ Light Brown
- `gst3d_pla_pla+lightpink_3500_175_p` — PLA+ Light Pink
- `gst3d_pla_pla+ocre_3500_175_p` — PLA+ Ocre
- `gst3d_pla_pla+olivegreen_3500_175_p` — PLA+ Olive green
- `gst3d_pla_pla+orange_3500_175_p` — PLA+ Orange
- `gst3d_pla_pla+pinkpanter_3500_175_p` — PLA+ Pink Panter
- `gst3d_pla_pla+red_3500_175_p` — PLA+ Red
- `gst3d_pla_pla+silver_3500_175_p` — PLA+ Silver
- `gst3d_pla_pla+violet_3500_175_p` — PLA+ Violet
- `gst3d_pla_pla+white_3500_175_p` — PLA+ White
- `gst3d_pla_pla+yellow_3500_175_p` — PLA+ Yellow
- `gst3d_pla_pla+applegreen_5000_175_p` — PLA+ Apple green
- `gst3d_pla_pla+armygreen_5000_175_p` — PLA+ Army green
- `gst3d_pla_pla+black_5000_175_p` — PLA+ Black
- `gst3d_pla_pla+blue_5000_175_p` — PLA+ Blue
- `gst3d_pla_pla+bonewhite_5000_175_p` — PLA+ Bone white
- `gst3d_pla_pla+bronze_5000_175_p` — PLA+ Bronze
- `gst3d_pla_pla+brown_5000_175_p` — PLA+ Brown
- `gst3d_pla_pla+crystal_5000_175_p` — PLA+ Crystal
- `gst3d_pla_pla+fuchsia_5000_175_p` — PLA+ Fuchsia
- `gst3d_pla_pla+gold_5000_175_p` — PLA+ Gold
- `gst3d_pla_pla+khaki_5000_175_p` — PLA+ Khaki
- `gst3d_pla_pla+lightblue_5000_175_p` — PLA+ Light Blue
- `gst3d_pla_pla+lightbrown_5000_175_p` — PLA+ Light Brown
- `gst3d_pla_pla+lightpink_5000_175_p` — PLA+ Light Pink
- `gst3d_pla_pla+ocre_5000_175_p` — PLA+ Ocre
- `gst3d_pla_pla+olivegreen_5000_175_p` — PLA+ Olive green
- `gst3d_pla_pla+orange_5000_175_p` — PLA+ Orange
- `gst3d_pla_pla+pinkpanter_5000_175_p` — PLA+ Pink Panter
- `gst3d_pla_pla+red_5000_175_p` — PLA+ Red
- `gst3d_pla_pla+silver_5000_175_p` — PLA+ Silver
- `gst3d_pla_pla+violet_5000_175_p` — PLA+ Violet
- `gst3d_pla_pla+white_5000_175_p` — PLA+ White
- `gst3d_pla_pla+yellow_5000_175_p` — PLA+ Yellow
- `gst3d_pla_pla+militaryarmygreen_1000_175_p` — PLA+ Military Army green
- `gst3d_pla_pla+militarykhaki_1000_175_p` — PLA+ Military Khaki
- `gst3d_pla_pla+militarylightbrown_1000_175_p` — PLA+ Military Light Brown
- `gst3d_pla_pla+militaryocre_1000_175_p` — PLA+ Military Ocre
- `gst3d_pla_pla+militaryolivegreen_1000_175_p` — PLA+ Military Olive green
- `gst3d_pla_pla+silkaluminum_1000_175_p` — PLA+ SILK Aluminum
- `gst3d_pla_pla+silkblue_1000_175_p` — PLA+ SILK Blue
- `gst3d_pla_pla+silkfuchsia_1000_175_p` — PLA+ SILK Fuchsia
- `gst3d_pla_pla+silkgold_1000_175_p` — PLA+ SILK Gold
- `gst3d_pla_pla+silkgoldrose_1000_175_p` — PLA+ SILK Gold Rose
- `gst3d_pla_pla+silkgraphite_1000_175_p` — PLA+ SILK Graphite
- `gst3d_pla_pla+silkgreen_1000_175_p` — PLA+ SILK Green
- `gst3d_pla_pla+silkgreenmint_1000_175_p` — PLA+ SILK Green mint
- `gst3d_pla_pla+silkpeach_1000_175_p` — PLA+ SILK Peach
- `gst3d_pla_pla+silkpurple_1000_175_p` — PLA+ SILK Purple
- `gst3d_pla_pla+silkred_1000_175_p` — PLA+ SILK Red
- `gst3d_pla_pla+silksand_1000_175_p` — PLA+ SILK Sand
- `gst3d_pla_pla+silkwhitepearl_1000_175_p` — PLA+ SILK White pearl
- `gst3d_pla_pla+specialaquamarine_1000_175_p` — PLA+ Special Aquamarine
- `gst3d_pla_pla+specialfirefly_1000_175_p` — PLA+ Special Firefly
- `gst3d_pla_pla+specialfluorgreen_1000_175_p` — PLA+ Special Fluor green
- `gst3d_pla_pla+specialfluororange_1000_175_p` — PLA+ Special Fluor Orange
- `gst3d_pla_pla+specialfluoryellow_1000_175_p` — PLA+ Special Fluor yellow
- `gst3d_pla_pla+specialiceblue_1000_175_p` — PLA+ Special Ice Blue
- `gst3d_pla_pla+specialmarble_1000_175_p` — PLA+ Special Marble
- `gst3d_pla_pla+specialmellowyellow_1000_175_p` — PLA+ Special Mellow yellow
- `gst3d_pla_pla+specialmustard_1000_175_p` — PLA+ Special Mustard
- `gst3d_tpu_tpuapplegreen_1000_175_p` — TPU Apple green
- `gst3d_tpu_tpublack_1000_175_p` — TPU Black
- `gst3d_tpu_tpublue_1000_175_p` — TPU Blue
- `gst3d_tpu_tpured_1000_175_p` — TPU Red
- `gst3d_tpu_tpusilver_1000_175_p` — TPU Silver
- `gst3d_tpu_tpuwhite_1000_175_p` — TPU White
