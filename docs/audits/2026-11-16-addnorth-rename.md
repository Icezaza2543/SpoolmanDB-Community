# add:north rename migration (pilot) — 2026-11-16

Starting commit: `d494ac0917292ea55b92964a96ecdc6525d1a8f9` (rename-retirement tooling, proposed in Icezaza2543/SpoolmanDB-Community#72). Upstream source: [Donkie/SpoolmanDB#521](https://github.com/Donkie/SpoolmanDB/pull/521), merge commit `bbdc012ba9270d545f2be0f3e66603640d60d800`.

This is an **intentional breaking catalog migration** and the first `reason: "rename"` use. It applies the upstream add:north name cleanup: names no longer repeat the material (`"PETG - {color_name}"` becomes `"{color_name}"` for PETG).

| Check | Result |
|---|---|
| Groups renamed | 23 (16 distinct template renames) |
| Public IDs retired as renames | 137 |
| New public IDs | 137, each the registered target of exactly one retirement |
| Catalog size | 51,434 (unchanged) |
| Unregistered removals, changed or rekeyed identities | 0 |
| Material, weight, diameter, spool, colour and metadata changes | None |

Reproduce with:

```sh
python scripts/rename_migration.py --file addnorth.json \
    --upstream bbdc012ba9270d545f2be0f3e66603640d60d800~1 bbdc012ba9270d545f2be0f3e66603640d60d800 \
    --ref https://github.com/Donkie/SpoolmanDB/pull/521 --source bbdc012ba9270d545f2be0f3e66603640d60d800 \
    --base-ref d494ac0917292ea55b92964a96ecdc6525d1a8f9
```

Retired IDs disappear from the published catalog. Existing Spoolman spools keep their local imported data; Spoolman does not read the registry or follow these mappings.

## Not renamed: Community-only groups

These 27 add:north groups exist only in Community and also repeat the material in their names. Most overlap an upstream group but carry a less specific material, for example `TPU Pro Matte 85A {color_name}` (TPU) next to `Pro Matte - {color_name}` (TPU-85A), or `PA12 Adura {color_name}` next to `Adura - {color_name}` (PA). Renaming them now would create IDs that a later duplicate or material review would retire again. They need that review first.

- `ABS {color_name}` (ABS)
- `PA12 Addbor N25 {color_name}` (PA12)
- `PA12 Addlantis {color_name}` (PA12)
- `PA12 Adura {color_name}` (PA12)
- `PA12 Adura FDA {color_name}` (PA12)
- `PA12 Adura X {color_name}` (PA12)
- `PA6 {color_name}` (PA6)
- `PC CF {color_name}` (PC)
- `PETG Koltron G1 {color_name}` (PETG)
- `Matte PETG {color_name}` (PETG)
- `PETG Rigid X {color_name}` (PETG)
- `Rigid X CF PETG {color_name}` (PETG)
- `Glow PLA {color_name}` (PLA)
- `High Speed PLA {color_name}` (PLA)
- `Matte High Speed PLA {color_name}` (PLA)
- `Matte PLA {color_name}` (PLA)
- `PLA Matte Textura {color_name}` (PLA)
- `PLA {color_name}` (PLA)
- `PLA CF {color_name}` (PLA)
- `PLA Wood {color_name}` (PLA)
- `Silk PLA {color_name}` (PLA)
- `PLA Textura Flare {color_name}` (PLA)
- `PVDF Adamant S1 {color_name}` (PVDF)
- `TPU EasyFlex {color_name}` (TPU)
- `Matte TPU {color_name}` (TPU)
- `TPU Pro Matte 85A {color_name}` (TPU)
- `TPU Pro Matte 95A {color_name}` (TPU)

## Mapping

| Retired public ID | New public ID |
| --- | --- |
| `add:north_pc_pcblendhtlcf-black_1000_175_p` | `add:north_pc_blendhtlcf-black_1000_175_p` |
| `add:north_pc_pcblendhtlcf-black_500_175_p` | `add:north_pc_blendhtlcf-black_500_175_p` |
| `add:north_petg_esdpetg-black_750_175_p` | `add:north_petg_esd-black_750_175_p` |
| `add:north_petg_petg-black_2300_175_p` | `add:north_petg_black_2300_175_p` |
| `add:north_petg_petg-black_5000_175_p` | `add:north_petg_black_5000_175_p` |
| `add:north_petg_petg-black_750_175_p` | `add:north_petg_black_750_175_p` |
| `add:north_petg_petg-clear_5000_175_p` | `add:north_petg_clear_5000_175_p` |
| `add:north_petg_petg-clear_750_175_p` | `add:north_petg_clear_750_175_p` |
| `add:north_petg_petg-esd_5000_175_p` | `add:north_petg_esd_5000_175_p` |
| `add:north_petg_petg-glitzgrey_5000_175_p` | `add:north_petg_glitzgrey_5000_175_p` |
| `add:north_petg_petg-glitzgrey_750_175_p` | `add:north_petg_glitzgrey_750_175_p` |
| `add:north_petg_petg-green_5000_175_p` | `add:north_petg_green_5000_175_p` |
| `add:north_petg_petg-green_750_175_p` | `add:north_petg_green_750_175_p` |
| `add:north_petg_petg-grey_5000_175_p` | `add:north_petg_grey_5000_175_p` |
| `add:north_petg_petg-grey_750_175_p` | `add:north_petg_grey_750_175_p` |
| `add:north_petg_petg-lightgrey_5000_175_p` | `add:north_petg_lightgrey_5000_175_p` |
| `add:north_petg_petg-lightgrey_750_175_p` | `add:north_petg_lightgrey_750_175_p` |
| `add:north_petg_petg-lucentorange_5000_175_p` | `add:north_petg_lucentorange_5000_175_p` |
| `add:north_petg_petg-lucentorange_750_175_p` | `add:north_petg_lucentorange_750_175_p` |
| `add:north_petg_petg-mediumblue_5000_175_p` | `add:north_petg_mediumblue_5000_175_p` |
| `add:north_petg_petg-mediumblue_750_175_p` | `add:north_petg_mediumblue_750_175_p` |
| `add:north_petg_petg-red_5000_175_p` | `add:north_petg_red_5000_175_p` |
| `add:north_petg_petg-red_750_175_p` | `add:north_petg_red_750_175_p` |
| `add:north_petg_petg-white_2300_175_p` | `add:north_petg_white_2300_175_p` |
| `add:north_petg_petg-white_5000_175_p` | `add:north_petg_white_5000_175_p` |
| `add:north_petg_petg-white_750_175_p` | `add:north_petg_white_750_175_p` |
| `add:north_petg_petg-yellow_5000_175_p` | `add:north_petg_yellow_5000_175_p` |
| `add:north_petg_petg-yellow_750_175_p` | `add:north_petg_yellow_750_175_p` |
| `add:north_petg_petgeconomy-black_1000_175_p` | `add:north_petg_economy-black_1000_175_p` |
| `add:north_petg_petgeconomy-lightgrey_1000_175_p` | `add:north_petg_economy-lightgrey_1000_175_p` |
| `add:north_petg_petgeconomy-white_1000_175_p` | `add:north_petg_economy-white_1000_175_p` |
| `add:north_petg_petgflameretardantv0-black_750_175_p` | `add:north_petg_flameretardantv0-black_750_175_p` |
| `add:north_petg_petgflameretardantv0-natural_750_175_p` | `add:north_petg_flameretardantv0-natural_750_175_p` |
| `add:north_petg_petgflameretardantv0-white_750_175_p` | `add:north_petg_flameretardantv0-white_750_175_p` |
| `add:north_petg_petgpromatte-black_2300_175_p` | `add:north_petg_promatte-black_2300_175_p` |
| `add:north_petg_petgpromatte-black_750_175_p` | `add:north_petg_promatte-black_750_175_p` |
| `add:north_petg_petgpromatte-white_2300_175_p` | `add:north_petg_promatte-white_2300_175_p` |
| `add:north_petg_petgpromatte-white_750_175_p` | `add:north_petg_promatte-white_750_175_p` |
| `add:north_pla+wood_plawood-lightoak_1000_175_p` | `add:north_pla+wood_wood-lightoak_1000_175_p` |
| `add:north_pla+wood_plawood-lightoak_500_175_p` | `add:north_pla+wood_wood-lightoak_500_175_p` |
| `add:north_pla+wood_plawood-nordicbirch_1000_175_p` | `add:north_pla+wood_wood-nordicbirch_1000_175_p` |
| `add:north_pla+wood_plawood-nordicbirch_500_175_p` | `add:north_pla+wood_wood-nordicbirch_500_175_p` |
| `add:north_pla-cf_placf-black_1000_175_p` | `add:north_pla-cf_black_1000_175_p` |
| `add:north_pla_e-pla-armygreen_2300_175_p` | `add:north_pla_e-armygreen_2300_175_p` |
| `add:north_pla_e-pla-armygreen_750_175_p` | `add:north_pla_e-armygreen_750_175_p` |
| `add:north_pla_e-pla-auroragreen_2300_175_p` | `add:north_pla_e-auroragreen_2300_175_p` |
| `add:north_pla_e-pla-auroragreen_750_175_p` | `add:north_pla_e-auroragreen_750_175_p` |
| `add:north_pla_e-pla-black_2300_175_p` | `add:north_pla_e-black_2300_175_p` |
| `add:north_pla_e-pla-black_750_175_p` | `add:north_pla_e-black_750_175_p` |
| `add:north_pla_e-pla-coldwhite_2300_175_p` | `add:north_pla_e-coldwhite_2300_175_p` |
| `add:north_pla_e-pla-coldwhite_750_175_p` | `add:north_pla_e-coldwhite_750_175_p` |
| `add:north_pla_e-pla-glitzblack_2300_175_p` | `add:north_pla_e-glitzblack_2300_175_p` |
| `add:north_pla_e-pla-glitzblack_750_175_p` | `add:north_pla_e-glitzblack_750_175_p` |
| `add:north_pla_e-pla-glitzgrey_2300_175_p` | `add:north_pla_e-glitzgrey_2300_175_p` |
| `add:north_pla_e-pla-glitzgrey_750_175_p` | `add:north_pla_e-glitzgrey_750_175_p` |
| `add:north_pla_e-pla-glitzpurple_2300_175_p` | `add:north_pla_e-glitzpurple_2300_175_p` |
| `add:north_pla_e-pla-glitzpurple_750_175_p` | `add:north_pla_e-glitzpurple_750_175_p` |
| `add:north_pla_e-pla-glitzsapphire_2300_175_p` | `add:north_pla_e-glitzsapphire_2300_175_p` |
| `add:north_pla_e-pla-glitzsapphire_750_175_p` | `add:north_pla_e-glitzsapphire_750_175_p` |
| `add:north_pla_e-pla-glitzsilver_2300_175_p` | `add:north_pla_e-glitzsilver_2300_175_p` |
| `add:north_pla_e-pla-glitzsilver_750_175_p` | `add:north_pla_e-glitzsilver_750_175_p` |
| `add:north_pla_e-pla-glowinthedarkgreen_2300_175_p` | `add:north_pla_e-glowinthedarkgreen_2300_175_p` |
| `add:north_pla_e-pla-glowinthedarkgreen_750_175_p` | `add:north_pla_e-glowinthedarkgreen_750_175_p` |
| `add:north_pla_e-pla-gold_2300_175_p` | `add:north_pla_e-gold_2300_175_p` |
| `add:north_pla_e-pla-gold_750_175_p` | `add:north_pla_e-gold_750_175_p` |
| `add:north_pla_e-pla-green_2300_175_p` | `add:north_pla_e-green_2300_175_p` |
| `add:north_pla_e-pla-green_750_175_p` | `add:north_pla_e-green_750_175_p` |
| `add:north_pla_e-pla-lightgrey_2300_175_p` | `add:north_pla_e-lightgrey_2300_175_p` |
| `add:north_pla_e-pla-lightgrey_750_175_p` | `add:north_pla_e-lightgrey_750_175_p` |
| `add:north_pla_e-pla-lucentorange_2300_175_p` | `add:north_pla_e-lucentorange_2300_175_p` |
| `add:north_pla_e-pla-lucentorange_750_175_p` | `add:north_pla_e-lucentorange_750_175_p` |
| `add:north_pla_e-pla-lucentpink_2300_175_p` | `add:north_pla_e-lucentpink_2300_175_p` |
| `add:north_pla_e-pla-lucentpink_750_175_p` | `add:north_pla_e-lucentpink_750_175_p` |
| `add:north_pla_e-pla-marble_2300_175_p` | `add:north_pla_e-marble_2300_175_p` |
| `add:north_pla_e-pla-marble_750_175_p` | `add:north_pla_e-marble_750_175_p` |
| `add:north_pla_e-pla-mediumblue_2300_175_p` | `add:north_pla_e-mediumblue_2300_175_p` |
| `add:north_pla_e-pla-mediumblue_750_175_p` | `add:north_pla_e-mediumblue_750_175_p` |
| `add:north_pla_e-pla-natural_2300_175_p` | `add:north_pla_e-natural_2300_175_p` |
| `add:north_pla_e-pla-natural_750_175_p` | `add:north_pla_e-natural_750_175_p` |
| `add:north_pla_e-pla-red_2300_175_p` | `add:north_pla_e-red_2300_175_p` |
| `add:north_pla_e-pla-red_750_175_p` | `add:north_pla_e-red_750_175_p` |
| `add:north_pla_e-pla-stemfieorange_2300_175_p` | `add:north_pla_e-stemfieorange_2300_175_p` |
| `add:north_pla_e-pla-stemfieorange_750_175_p` | `add:north_pla_e-stemfieorange_750_175_p` |
| `add:north_pla_e-pla-tropicalturquoise_2300_175_p` | `add:north_pla_e-tropicalturquoise_2300_175_p` |
| `add:north_pla_e-pla-tropicalturquoise_750_175_p` | `add:north_pla_e-tropicalturquoise_750_175_p` |
| `add:north_pla_e-pla-ultramarineblue_2300_175_p` | `add:north_pla_e-ultramarineblue_2300_175_p` |
| `add:north_pla_e-pla-ultramarineblue_750_175_p` | `add:north_pla_e-ultramarineblue_750_175_p` |
| `add:north_pla_e-pla-white_2300_175_p` | `add:north_pla_e-white_2300_175_p` |
| `add:north_pla_e-pla-white_750_175_p` | `add:north_pla_e-white_750_175_p` |
| `add:north_pla_e-pla-yellow_2300_175_p` | `add:north_pla_e-yellow_2300_175_p` |
| `add:north_pla_e-pla-yellow_750_175_p` | `add:north_pla_e-yellow_750_175_p` |
| `add:north_pla_ht-plapromatte-black_2300_175_p` | `add:north_pla_htpromatte-black_2300_175_p` |
| `add:north_pla_ht-plapromatte-black_750_175_p` | `add:north_pla_htpromatte-black_750_175_p` |
| `add:north_pla_ht-plapromatte-white_2300_175_p` | `add:north_pla_htpromatte-white_2300_175_p` |
| `add:north_pla_ht-plapromatte-white_750_175_p` | `add:north_pla_htpromatte-white_750_175_p` |
| `add:north_pla_plaeconomy-black_1000_175_p` | `add:north_pla_economy-black_1000_175_p` |
| `add:north_pla_plaeconomy-lightgrey_1000_175_p` | `add:north_pla_economy-lightgrey_1000_175_p` |
| `add:north_pla_plaeconomy-white_1000_175_p` | `add:north_pla_economy-white_1000_175_p` |
| `add:north_pla_plapremiumsilk-blue_750_175_p` | `add:north_pla_premiumsilk-blue_750_175_p` |
| `add:north_pla_plapremiumsilk-gold_750_175_p` | `add:north_pla_premiumsilk-gold_750_175_p` |
| `add:north_pla_plapremiumsilk-green_750_175_p` | `add:north_pla_premiumsilk-green_750_175_p` |
| `add:north_pla_plapremiumsilk-red_750_175_p` | `add:north_pla_premiumsilk-red_750_175_p` |
| `add:north_pla_plapremiumsilk-silver_750_175_p` | `add:north_pla_premiumsilk-silver_750_175_p` |
| `add:north_pla_x-pla-black_2300_175_p` | `add:north_pla_x-black_2300_175_p` |
| `add:north_pla_x-pla-black_5000_175_p` | `add:north_pla_x-black_5000_175_p` |
| `add:north_pla_x-pla-black_750_175_p` | `add:north_pla_x-black_750_175_p` |
| `add:north_pla_x-pla-coldwhite_5000_175_p` | `add:north_pla_x-coldwhite_5000_175_p` |
| `add:north_pla_x-pla-coldwhite_750_175_p` | `add:north_pla_x-coldwhite_750_175_p` |
| `add:north_pla_x-pla-lightgrey_2300_175_p` | `add:north_pla_x-lightgrey_2300_175_p` |
| `add:north_pla_x-pla-lightgrey_5000_175_p` | `add:north_pla_x-lightgrey_5000_175_p` |
| `add:north_pla_x-pla-lightgrey_750_175_p` | `add:north_pla_x-lightgrey_750_175_p` |
| `add:north_pla_x-pla-mediumblue_5000_175_p` | `add:north_pla_x-mediumblue_5000_175_p` |
| `add:north_pla_x-pla-mediumblue_750_175_p` | `add:north_pla_x-mediumblue_750_175_p` |
| `add:north_pla_x-pla-powertoolblue_5000_175_p` | `add:north_pla_x-powertoolblue_5000_175_p` |
| `add:north_pla_x-pla-powertoolblue_750_175_p` | `add:north_pla_x-powertoolblue_750_175_p` |
| `add:north_pla_x-pla-powertoollightgreen_5000_175_p` | `add:north_pla_x-powertoollightgreen_5000_175_p` |
| `add:north_pla_x-pla-powertoollightgreen_750_175_p` | `add:north_pla_x-powertoollightgreen_750_175_p` |
| `add:north_pla_x-pla-powertoollimegreen_5000_175_p` | `add:north_pla_x-powertoollimegreen_5000_175_p` |
| `add:north_pla_x-pla-powertoollimegreen_750_175_p` | `add:north_pla_x-powertoollimegreen_750_175_p` |
| `add:north_pla_x-pla-powertoolred_5000_175_p` | `add:north_pla_x-powertoolred_5000_175_p` |
| `add:north_pla_x-pla-powertoolred_750_175_p` | `add:north_pla_x-powertoolred_750_175_p` |
| `add:north_pla_x-pla-powertoolyellow_5000_175_p` | `add:north_pla_x-powertoolyellow_5000_175_p` |
| `add:north_pla_x-pla-powertoolyellow_750_175_p` | `add:north_pla_x-powertoolyellow_750_175_p` |
| `add:north_pla_x-pla-red_5000_175_p` | `add:north_pla_x-red_5000_175_p` |
| `add:north_pla_x-pla-red_750_175_p` | `add:north_pla_x-red_750_175_p` |
| `add:north_pla_x-pla-white_2300_175_p` | `add:north_pla_x-white_2300_175_p` |
| `add:north_pla_x-pla-white_5000_175_p` | `add:north_pla_x-white_5000_175_p` |
| `add:north_pla_x-pla-white_750_175_p` | `add:north_pla_x-white_750_175_p` |
| `add:north_pla_x-plahighspeed-black_750_175_p` | `add:north_pla_xhighspeed-black_750_175_p` |
| `add:north_pla_x-plahighspeed-white_750_175_p` | `add:north_pla_xhighspeed-white_750_175_p` |
| `add:north_tpu-85a_tpupromatte85a-black_1000_175_p` | `add:north_tpu-85a_promatte-black_1000_175_p` |
| `add:north_tpu-85a_tpupromatte85a-brownleather_500_175_p` | `add:north_tpu-85a_promatte-brownleather_500_175_p` |
| `add:north_tpu-85a_tpupromatte85a-white_1000_175_p` | `add:north_tpu-85a_promatte-white_1000_175_p` |
| `add:north_tpu-85a_tpupromatte85a-yellow_500_175_p` | `add:north_tpu-85a_promatte-yellow_500_175_p` |
| `add:north_tpu-95a_tpupromatte95a-black_1000_175_p` | `add:north_tpu-95a_promatte-black_1000_175_p` |
| `add:north_tpu-95a_tpupromatte95a-black_500_175_p` | `add:north_tpu-95a_promatte-black_500_175_p` |
| `add:north_tpu-95a_tpupromatte95a-white_1000_175_p` | `add:north_tpu-95a_promatte-white_1000_175_p` |

Rename-only scope check (no other IDs, rekeys or field changes):

```sh
python scripts/rename_migration.py --verify --base-ref d494ac0917292ea55b92964a96ecdc6525d1a8f9
```
