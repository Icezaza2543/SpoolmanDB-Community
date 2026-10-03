# creality duplicate migration review

Base `0f986a5c11df60e7dfe4ca92ad96a0f0d8f74289`; read-only upstream `8f1a99f9cda7a58ca3118d6bd28c707647caa3db`; digest `8f529c8189786635f2ca5371e14885f3c7fadac4606b63b080ef14f86bf8e5ca`.

## Authorization and result

{"groups": 2, "approved_groups": 0, "retired": 0, "deferred": 2, "hard_stops": 0, "before_count": 51702, "after_count": 51702, "brand_before": 202, "brand_after": 202, "registry_before": 1732, "registry_after": 1732, "metadata_fields_changed": 0, "code_transfers": 0, "new": 0, "changed_identity": 0, "rekeyed": 0}

Two same-template genericPLA Gray/Grey ties, HEX959FA1 versusACB1BA across spool/refill, no same-SKU binding. Preserve allIDs and metadata; Hyper/Soleyin formulas not imported.

This is an audit-only result: no records are retired and no catalog migration is applied. Packaging, tare and all identities remain unchanged. Future reviewed retirements would not redirect external catalog lookups automatically.

## Current first-party evidence

- {"url": "https://store.creality.com/eu/products/hyper-1-75mm-pla-3d-printing-filament-1kg", "note": "HyperPLA is distinct; not proof for genericPLA Gray/Grey."}

## Complete approved retired ID list

| Retired ID | Survivor | Original baseline key |
|---|---|---|

## Per-group decisions and unresolved metadata

### CR001: dup-eb4c14f13d80d3665089641be27c68030271374c8c4c1a3006a86e9df11c8c04

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`creality_pla_plagray_1000_175_r`|`PLA {color_name}`|`Gray`|{"source_file": "creality.json", "definition_index": 18, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|
|`creality_pla_plagrey_1000_175_r`|`PLA {color_name}`|`Grey`|{"source_file": "creality.json", "definition_index": 18, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "creality_pla_plagray_1000_175_r": "959FA1",
    "creality_pla_plagrey_1000_175_r": "ACB1BA"
  }
}
```

### CR002: dup-edce4abdd5cab29b4fd8105360be2efa3008314921926c74659a6672e86c2fd2

Status: DEFERRED; survivor `None`; Identity-only tie: no verified official spelling or same-SKU binding; owner rule6 permits deferral.

| ID | Source template | Source color | Axes / upstream |
|---|---|---|---|
|`creality_pla_plagray_1000_175_p`|`PLA {color_name}`|`Gray`|{"source_file": "creality.json", "definition_index": 18, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|
|`creality_pla_plagrey_1000_175_p`|`PLA {color_name}`|`Grey`|{"source_file": "creality.json", "definition_index": 18, "weights": 2, "diameters": 1, "colors": 25, "compiled_records": 50} / False|



Conflicts (both original values retained; unresolved unless explicitly corrected below):
```json
{
  "color_hex": {
    "creality_pla_plagray_1000_175_p": "959FA1",
    "creality_pla_plagrey_1000_175_p": "ACB1BA"
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

- `creality_pla_whitehyper_1000_175_c` — White Hyper
- `creality_pla_greyhyper_1000_175_c` — Grey Hyper
- `creality_pla_redhyper_1000_175_c` — Red Hyper
- `creality_pla_veryperihyper_1000_175_c` — Very Peri Hyper
- `creality_pla_yellowhyper_1000_175_c` — Yellow Hyper
- `creality_pla_greenhyper_1000_175_c` — Green Hyper
- `creality_pla_orangehyper_1000_175_c` — Orange Hyper
- `creality_pla_brownhyper_1000_175_c` — Brown Hyper
- `creality_pla_fleshhyper_1000_175_c` — Flesh Hyper
- `creality_pla_peachfuzzhyper_1000_175_c` — Peach Fuzz Hyper
- `creality_pla_vivamagentahyper_1000_175_c` — Viva Magenta Hyper
- `creality_pla_purplehyper_1000_175_c` — Purple Hyper
- `creality_pla_goldhyper_1000_175_c` — Gold Hyper
- `creality_pla_blackhyper_1000_175_c` — Black Hyper
- `creality_pla_bluehyper_1000_175_c` — Blue Hyper
- `creality_pla_whitehyperrfid_1000_175_c` — White Hyper RFID
- `creality_pla_greyhyperrfid_1000_175_c` — Grey Hyper RFID
- `creality_pla_redhyperrfid_1000_175_c` — Red Hyper RFID
- `creality_pla_veryperihyperrfid_1000_175_c` — Very Peri Hyper RFID
- `creality_pla_yellowhyperrfid_1000_175_c` — Yellow Hyper RFID
- `creality_pla_greenhyperrfid_1000_175_c` — Green Hyper RFID
- `creality_pla_orangehyperrfid_1000_175_c` — Orange Hyper RFID
- `creality_pla_brownhyperrfid_1000_175_c` — Brown Hyper RFID
- `creality_pla_skinhyperrfid_1000_175_c` — Skin Hyper RFID
- `creality_pla_peachfuzzhyperrfid_1000_175_c` — Peach Fuzz Hyper RFID
- `creality_pla_vivamagentahyperrfid_1000_175_c` — Viva Magenta Hyper RFID
- `creality_pla_purplehyperrfid_1000_175_c` — Purple Hyper RFID
- `creality_pla_goldhyperrfid_1000_175_c` — Gold Hyper RFID
- `creality_pla_blackhyperrfid_1000_175_c` — Black Hyper RFID
- `creality_pla_bluehyperrfid_1000_175_c` — Blue Hyper RFID
- `creality_abs_whitehyperabs_1000_175_c` — White Hyper ABS
- `creality_abs_greyhyperabs_1000_175_c` — Grey Hyper ABS
- `creality_abs_blackhyperabs_1000_175_c` — Black Hyper ABS
- `creality_pla_white_1000_175_c` — White
- `creality_pla_silver_1000_175_c` — Silver
- `creality_pla_grey_1000_175_c` — Grey
- `creality_pla_black_1000_175_c` — Black
- `creality_pla_yellow_1000_175_c` — Yellow
- `creality_pla_green_1000_175_c` — Green
- `creality_pla_blue_1000_175_c` — Blue
- `creality_pla_red_1000_175_c` — Red
- `creality_pla_raindow_1000_175_c` — Raindow
- `creality_pla_ender-plawhite_1000_175_c` — Ender-PLA White
- `creality_pla_ender-plablack_1000_175_c` — Ender-PLA Black
- `creality_pla_ender-plablue_1000_175_c` — Ender-PLA Blue
- `creality_pla_ender-plared_1000_175_c` — Ender-PLA Red
- `creality_petg_cr-petgwhite_1000_175_p` — CR-PETG White
- `creality_petg_cr-petgblack_1000_175_p` — CR-PETG Black
- `creality_petg_cr-petgtransparent_1000_175_p` — CR-PETG Transparent
- `creality_petg_cr-petgred_1000_175_p` — CR-PETG Red
- `creality_petg_cr-petgblue_1000_175_p` — CR-PETG Blue
- `creality_petg_cr-petggrey_1000_175_p` — CR-PETG Grey
- `creality_abs_absblack_1000_175_p` — ABS Black
- `creality_abs_absblue_1000_175_p` — ABS Blue
- `creality_abs_absgray_1000_175_p` — ABS Gray
- `creality_abs_absyellow_1000_175_p` — ABS Yellow
- `creality_asa_hpasahpasa_1000_175_p` — HP ASA HP ASA
- `creality_pc_hyperpchyperpc_1000_175_c` — Hyper PC Hyper PC
- `creality_petg_hyperpetgblack_1000_175_c` — Hyper PETG Black
- `creality_petg_hyperpetgblue_1000_175_c` — Hyper PETG Blue
- `creality_petg_hyperpetggreen_1000_175_c` — Hyper PETG Green
- `creality_petg_hyperpetggrey_1000_175_c` — Hyper PETG Grey
- `creality_petg_hyperpetgred_1000_175_c` — Hyper PETG Red
- `creality_petg_hyperpetgtransparent_1000_175_c` — Hyper PETG Transparent
- `creality_petg_hyperpetgwhite_1000_175_c` — Hyper PETG White
- `creality_petg_hyperpetgyellow_1000_175_c` — Hyper PETG Yellow
- `creality_petg_petgblack_1000_175_p` — PETG Black
- `creality_petg_petgblue_1000_175_p` — PETG Blue
- `creality_petg_petgdigitalblue_1000_175_p` — PETG Digital Blue
- `creality_petg_petggray_1000_175_p` — PETG Gray
- `creality_petg_petggreen_1000_175_p` — PETG Green
- `creality_petg_petgpink_1000_175_p` — PETG Pink
- `creality_petg_petgpurple_1000_175_p` — PETG Purple
- `creality_petg_petgred_1000_175_p` — PETG Red
- `creality_petg_petgtranslucentlightpink_1000_175_p` — PETG Translucent Light Pink
- `creality_petg_petgtransparent_1000_175_p` — PETG Transparent
- `creality_petg_petgtransparentblue_1000_175_p` — PETG Transparent Blue
- `creality_petg_petgwhite_1000_175_p` — PETG White
- `creality_petg_petgblack_1000_175_r` — PETG Black
- `creality_petg_petgblue_1000_175_r` — PETG Blue
- `creality_petg_petgdigitalblue_1000_175_r` — PETG Digital Blue
- `creality_petg_petggray_1000_175_r` — PETG Gray
- `creality_petg_petggreen_1000_175_r` — PETG Green
- `creality_petg_petgpink_1000_175_r` — PETG Pink
- `creality_petg_petgpurple_1000_175_r` — PETG Purple
- `creality_petg_petgred_1000_175_r` — PETG Red
- `creality_petg_petgtranslucentlightpink_1000_175_r` — PETG Translucent Light Pink
- `creality_petg_petgtransparent_1000_175_r` — PETG Transparent
- `creality_petg_petgtransparentblue_1000_175_r` — PETG Transparent Blue
- `creality_petg_petgwhite_1000_175_r` — PETG White
- `creality_pla_placfblack_1000_175_p` — PLA CF Black
- `creality_pla_cr-placarboncr-placarbon_1000_175_p` — CR-PLA Carbon CR-PLA Carbon
- `creality_pla_placr-woodcr-wood_1000_175_p` — PLA CR-Wood CR-Wood
- `creality_pla_enderfastplablack_1000_175_p` — Ender Fast PLA Black
- `creality_pla_enderfastplared_1000_175_p` — Ender Fast PLA Red
- `creality_pla_enderfastplawhite_1000_175_p` — Ender Fast PLA White
- `creality_pla_hyperplablack_1000_175_c` — Hyper PLA Black
- `creality_pla_hyperplablue_1000_175_c` — Hyper PLA Blue
- `creality_pla_hyperplabrown_1000_175_c` — Hyper PLA Brown
- `creality_pla_hyperplagold_1000_175_c` — Hyper PLA Gold
- `creality_pla_hyperplagreen_1000_175_c` — Hyper PLA Green
- `creality_pla_hyperplagrey_1000_175_c` — Hyper PLA Grey
- `creality_pla_hyperplaorange_1000_175_c` — Hyper PLA Orange
- `creality_pla_hyperplapeachfuzz_1000_175_c` — Hyper PLA Peach Fuzz
- `creality_pla_hyperplapurple_1000_175_c` — Hyper PLA Purple
- `creality_pla_hyperplared_1000_175_c` — Hyper PLA Red
- `creality_pla_hyperplaskin_1000_175_c` — Hyper PLA Skin
- `creality_pla_hyperplaveryperi_1000_175_c` — Hyper PLA Very Peri
- `creality_pla_hyperplavivamagenta_1000_175_c` — Hyper PLA Viva Magenta
- `creality_pla_hyperplawhite_1000_175_c` — Hyper PLA White
- `creality_pla_hyperplayellow_1000_175_c` — Hyper PLA Yellow
- `creality_pla_hyperpla-cfblack_1000_175_c` — Hyper PLA-CF Black
- `creality_pla_hyperpla-cfdarkgreen_1000_175_c` — Hyper PLA-CF Dark Green
- `creality_pla_hyperpla-cfgreyishyellow_1000_175_c` — Hyper PLA-CF Greyish Yellow
- `creality_pla_hyperpla-cfochre_1000_175_c` — Hyper PLA-CF Ochre
- `creality_pla_hyperpla-cfpurple_1000_175_c` — Hyper PLA-CF Purple
- `creality_pla_hyperrainbowplaspringlake_1000_175_c` — Hyper Rainbow PLA Spring Lake
- `creality_pla_hyperrainbowplawildblossom-long_1000_175_c` — Hyper Rainbow PLA Wild Blossom-Long
- `creality_pla_hyperrainbowplawildblossom-short_1000_175_c` — Hyper Rainbow PLA Wild Blossom-Short
- `creality_pla_plaapplegreen_1000_175_p` — PLA Apple Green
- `creality_pla_plabeige_1000_175_p` — PLA Beige
- `creality_pla_plablack_1000_175_p` — PLA Black
- `creality_pla_plablue_1000_175_p` — PLA Blue
- `creality_pla_pladeeppink_1000_175_p` — PLA Deep Pink
- `creality_pla_pladeepred_1000_175_p` — PLA Deep Red
- `creality_pla_plafluorescentgreen_1000_175_p` — PLA Fluorescent Green
- `creality_pla_plafluorescentorange_1000_175_p` — PLA Fluorescent Orange
- `creality_pla_plafluorescentpink_1000_175_p` — PLA Fluorescent Pink
- `creality_pla_plafluorescentyellow_1000_175_p` — PLA Fluorescent Yellow
- `creality_pla_plagreen_1000_175_p` — PLA Green
- `creality_pla_plaivorywhite_1000_175_p` — PLA Ivory White
- `creality_pla_plajadegreen_1000_175_p` — PLA Jade Green
- `creality_pla_planavyblue_1000_175_p` — PLA Navy Blue
- `creality_pla_plarainbow_1000_175_p` — PLA Rainbow
- `creality_pla_plarainbowupgrade_1000_175_p` — PLA Rainbow Upgrade
- `creality_pla_plared_1000_175_p` — PLA Red
- `creality_pla_plasilver_1000_175_p` — PLA Silver
- `creality_pla_plaupgrade+jadegreen_1000_175_p` — PLA Upgrade + Jade Green
- `creality_pla_plaviolet_1000_175_p` — PLA Violet
- `creality_pla_plawhite_1000_175_p` — PLA White
- `creality_pla_plawood_1000_175_p` — PLA Wood
- `creality_pla_playellow_1000_175_p` — PLA Yellow
- `creality_pla_plaapplegreen_1000_175_r` — PLA Apple Green
- `creality_pla_plabeige_1000_175_r` — PLA Beige
- `creality_pla_plablack_1000_175_r` — PLA Black
- `creality_pla_plablue_1000_175_r` — PLA Blue
- `creality_pla_pladeeppink_1000_175_r` — PLA Deep Pink
- `creality_pla_pladeepred_1000_175_r` — PLA Deep Red
- `creality_pla_plafluorescentgreen_1000_175_r` — PLA Fluorescent Green
- `creality_pla_plafluorescentorange_1000_175_r` — PLA Fluorescent Orange
- `creality_pla_plafluorescentpink_1000_175_r` — PLA Fluorescent Pink
- `creality_pla_plafluorescentyellow_1000_175_r` — PLA Fluorescent Yellow
- `creality_pla_plagreen_1000_175_r` — PLA Green
- `creality_pla_plaivorywhite_1000_175_r` — PLA Ivory White
- `creality_pla_plajadegreen_1000_175_r` — PLA Jade Green
- `creality_pla_planavyblue_1000_175_r` — PLA Navy Blue
- `creality_pla_plarainbow_1000_175_r` — PLA Rainbow
- `creality_pla_plarainbowupgrade_1000_175_r` — PLA Rainbow Upgrade
- `creality_pla_plared_1000_175_r` — PLA Red
- `creality_pla_plasilver_1000_175_r` — PLA Silver
- `creality_pla_plaupgrade+jadegreen_1000_175_r` — PLA Upgrade + Jade Green
- `creality_pla_plaviolet_1000_175_r` — PLA Violet
- `creality_pla_plawhite_1000_175_r` — PLA White
- `creality_pla_plawood_1000_175_r` — PLA Wood
- `creality_pla_playellow_1000_175_r` — PLA Yellow
- `creality_pla_silkplablue_1000_175_p` — Silk PLA Blue
- `creality_pla_silkplagold_1000_175_p` — Silk PLA Gold
- `creality_pla_silkplagolden-red_1000_175_p` — Silk PLA Golden-Red
- `creality_pla_silkplagolden-silver_1000_175_p` — Silk PLA Golden-Silver
- `creality_pla_silkplapink-purple_1000_175_p` — Silk PLA Pink-Purple
- `creality_pla_silkplapurple_1000_175_p` — Silk PLA Purple
- `creality_pla_silkplarainbow_1000_175_p` — Silk PLA Rainbow
- `creality_pla_silkplaredcopper_1000_175_p` — Silk PLA Red Copper
- `creality_pla_silkplasilver_1000_175_p` — Silk PLA Silver
- `creality_pla_silkplawhite_1000_175_p` — Silk PLA White
- `creality_pla_silkplayellow-blue_1000_175_p` — Silk PLA Yellow-Blue
- `creality_pla_soleyinultraplaalmondpurple_1000_175_p` — Soleyin Ultra PLA Almond Purple
- `creality_pla_soleyinultraplablack_1000_175_p` — Soleyin Ultra PLA Black
- `creality_pla_soleyinultraplagray_1000_175_p` — Soleyin Ultra PLA Gray
- `creality_pla_soleyinultraplagreenery_1000_175_p` — Soleyin Ultra PLA Greenery
- `creality_pla_soleyinultraplalightgreen_1000_175_p` — Soleyin Ultra PLA Light Green
- `creality_pla_soleyinultraplamatteblack_1000_175_p` — Soleyin Ultra PLA Matte Black
- `creality_pla_soleyinultraplamattefluonte_1000_175_p` — Soleyin Ultra PLA Matte Fluonte
- `creality_pla_soleyinultraplamattegray_1000_175_p` — Soleyin Ultra PLA Matte Gray
- `creality_pla_soleyinultraplamattemoonstone_1000_175_p` — Soleyin Ultra PLA Matte Moonstone
- `creality_pla_soleyinultraplamatterosestone_1000_175_p` — Soleyin Ultra PLA Matte Rose Stone
- `creality_pla_soleyinultraplamattewhite_1000_175_p` — Soleyin Ultra PLA Matte White
- `creality_pla_soleyinultraplaoceanblue_1000_175_p` — Soleyin Ultra PLA Ocean Blue
- `creality_pla_soleyinultraplapineappleyellow_1000_175_p` — Soleyin Ultra PLA Pineapple Yellow
- `creality_pla_soleyinultraplarosehip_1000_175_p` — Soleyin Ultra PLA Rosehip
- `creality_pla_soleyinultraplastrawberrymilk_1000_175_p` — Soleyin Ultra PLA Strawberry Milk
- `creality_pla_soleyinultraplawhite_1000_175_p` — Soleyin Ultra PLA White
- `creality_ppa_ppa-cfppa-cf_1000_175_p` — PPA-CF PPA-CF
- `creality_tpu_95atpublack_1000_175_p` — 95A TPU Black
- `creality_tpu_95atpugreen_1000_175_p` — 95A TPU Green
- `creality_tpu_95atpured_1000_175_p` — 95A TPU Red
- `creality_tpu_hp-tputransparent_1000_175_p` — HP-TPU Transparent
- `creality_tpu_hp-tpuwhite_1000_175_p` — HP-TPU White
