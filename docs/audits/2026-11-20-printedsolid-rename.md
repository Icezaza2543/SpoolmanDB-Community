# Printed Solid rename migration — 2026-11-20

Starting commit: `861fe11acd2e6d84efc09cc4abaa389bbe65eda5`. Upstream source: [Donkie/SpoolmanDB#527](https://github.com/Donkie/SpoolmanDB/pull/527), merge commit `772db6730b2adfd046be91d64914665268f1362e`.

This is an **intentional breaking catalog migration**. It applies the upstream Printed Solid name cleanup: names no longer repeat the material. `Jessie {color_name} PETG` → `Jessie {color_name}` (PETG); `Jessie {color_name} PLA` → `Jessie {color_name}` (PLA).

| Check | Result |
|---|---|
| Groups renamed | 2 (2 distinct template renames) |
| Public IDs retired as renames | 47 |
| New public IDs | 47, each the registered target of exactly one retirement |
| Existing retirements re-pointed to the final ID | 0 |
| Catalog size | 51,434 (unchanged) |
| Unregistered removals, changed or rekeyed identities | 0 |
| Material, weight, diameter, spool, colour and metadata changes | None |

Upstream #527 changes no colour names or other fields in this file.

Reproduce with:

```sh
python scripts/rename_migration.py --file printedsolid.json \
    --upstream 772db6730b2adfd046be91d64914665268f1362e~1 772db6730b2adfd046be91d64914665268f1362e \
    --ref https://github.com/Donkie/SpoolmanDB/pull/527 --source 772db6730b2adfd046be91d64914665268f1362e \
    --base-ref 861fe11acd2e6d84efc09cc4abaa389bbe65eda5
```

Retired IDs disappear from the published catalog. Existing Spoolman spools keep their local imported data; Spoolman does not read the registry or follow these mappings.

## Mapping

| Old public ID | New public ID |
|---|---|
| `printedsolid_petg_jessieblackpetg_1000_175_p` | `printedsolid_petg_jessieblack_1000_175_p` |
| `printedsolid_petg_jessieboldbluepetg_1000_175_p` | `printedsolid_petg_jessieboldblue_1000_175_p` |
| `printedsolid_petg_jessieclearpetg_1000_175_p` | `printedsolid_petg_jessieclear_1000_175_p` |
| `printedsolid_petg_jessiegunmetalgreypetg_1000_175_p` | `printedsolid_petg_jessiegunmetalgrey_1000_175_p` |
| `printedsolid_petg_jessiemysteryorangepetg_1000_175_p` | `printedsolid_petg_jessiemysteryorange_1000_175_p` |
| `printedsolid_petg_jessieneonyellowpetg_1000_175_p` | `printedsolid_petg_jessieneonyellow_1000_175_p` |
| `printedsolid_petg_jessiepsredpetg_1000_175_p` | `printedsolid_petg_jessiepsred_1000_175_p` |
| `printedsolid_petg_jessiepurecyanpetg_1000_175_p` | `printedsolid_petg_jessiepurecyan_1000_175_p` |
| `printedsolid_petg_jessiesoulblackglitterpetg_1000_175_p` | `printedsolid_petg_jessiesoulblackglitter_1000_175_p` |
| `printedsolid_petg_jessietreegreenpetg_1000_175_p` | `printedsolid_petg_jessietreegreen_1000_175_p` |
| `printedsolid_petg_jessiewhitepetg_1000_175_p` | `printedsolid_petg_jessiewhite_1000_175_p` |
| `printedsolid_petg_jessieyellowbirdpetg_1000_175_p` | `printedsolid_petg_jessieyellowbird_1000_175_p` |
| `printedsolid_pla_jessie3dpnvanillabeanicecreampla_1000_175_p` | `printedsolid_pla_jessie3dpnvanillabeanicecream_1000_175_p` |
| `printedsolid_pla_jessiearmygreenpla_1000_175_p` | `printedsolid_pla_jessiearmygreen_1000_175_p` |
| `printedsolid_pla_jessiebeige500pla_1000_175_p` | `printedsolid_pla_jessiebeige500_1000_175_p` |
| `printedsolid_pla_jessieblackpla_1000_175_p` | `printedsolid_pla_jessieblack_1000_175_p` |
| `printedsolid_pla_jessiebloodredlightglitterpla_1000_175_p` | `printedsolid_pla_jessiebloodredlightglitter_1000_175_p` |
| `printedsolid_pla_jessieblueicepla_1000_175_p` | `printedsolid_pla_jessieblueice_1000_175_p` |
| `printedsolid_pla_jessiebluemoonpla_1000_175_p` | `printedsolid_pla_jessiebluemoon_1000_175_p` |
| `printedsolid_pla_jessiebluewhalegreypla_1000_175_p` | `printedsolid_pla_jessiebluewhalegrey_1000_175_p` |
| `printedsolid_pla_jessieboldbluepla_1000_175_p` | `printedsolid_pla_jessieboldblue_1000_175_p` |
| `printedsolid_pla_jessiedeeppurplepla_1000_175_p` | `printedsolid_pla_jessiedeeppurple_1000_175_p` |
| `printedsolid_pla_jessiedesignwhitepla_1000_175_p` | `printedsolid_pla_jessiedesignwhite_1000_175_p` |
| `printedsolid_pla_jessiegoldenwinnerglitterpla_1000_175_p` | `printedsolid_pla_jessiegoldenwinnerglitter_1000_175_p` |
| `printedsolid_pla_jessiegreenicepla_1000_175_p` | `printedsolid_pla_jessiegreenice_1000_175_p` |
| `printedsolid_pla_jessiegreenslimeglitterpla_1000_175_p` | `printedsolid_pla_jessiegreenslimeglitter_1000_175_p` |
| `printedsolid_pla_jessiegunmetalgreypla_1000_175_p` | `printedsolid_pla_jessiegunmetalgrey_1000_175_p` |
| `printedsolid_pla_jessielimergreenpla_1000_175_p` | `printedsolid_pla_jessielimergreen_1000_175_p` |
| `printedsolid_pla_jessiemysteryorangepla_1000_175_p` | `printedsolid_pla_jessiemysteryorange_1000_175_p` |
| `printedsolid_pla_jessieneongreenpla_1000_175_p` | `printedsolid_pla_jessieneongreen_1000_175_p` |
| `printedsolid_pla_jessieneonpinkpla_1000_175_p` | `printedsolid_pla_jessieneonpink_1000_175_p` |
| `printedsolid_pla_jessieneonyellowpla_1000_175_p` | `printedsolid_pla_jessieneonyellow_1000_175_p` |
| `printedsolid_pla_jessieorangeglitterpla_1000_175_p` | `printedsolid_pla_jessieorangeglitter_1000_175_p` |
| `printedsolid_pla_jessiepsredpla_1000_175_p` | `printedsolid_pla_jessiepsred_1000_175_p` |
| `printedsolid_pla_jessiepurecyanpla_1000_175_p` | `printedsolid_pla_jessiepurecyan_1000_175_p` |
| `printedsolid_pla_jessiepuremagentapla_1000_175_p` | `printedsolid_pla_jessiepuremagenta_1000_175_p` |
| `printedsolid_pla_jessiepurpleeaterpla_1000_175_p` | `printedsolid_pla_jessiepurpleeater_1000_175_p` |
| `printedsolid_pla_jessiepurpleicepla_1000_175_p` | `printedsolid_pla_jessiepurpleice_1000_175_p` |
| `printedsolid_pla_jessiequarterwhitepla_1000_175_p` | `printedsolid_pla_jessiequarterwhite_1000_175_p` |
| `printedsolid_pla_jessieredicepla_1000_175_p` | `printedsolid_pla_jessieredice_1000_175_p` |
| `printedsolid_pla_jessiesafetyorangepla_1000_175_p` | `printedsolid_pla_jessiesafetyorange_1000_175_p` |
| `printedsolid_pla_jessiesoulblackglitterpla_1000_175_p` | `printedsolid_pla_jessiesoulblackglitter_1000_175_p` |
| `printedsolid_pla_jessietan64pla_1000_175_p` | `printedsolid_pla_jessietan64_1000_175_p` |
| `printedsolid_pla_jessietreebrownpla_1000_175_p` | `printedsolid_pla_jessietreebrown_1000_175_p` |
| `printedsolid_pla_jessietreegreenpla_1000_175_p` | `printedsolid_pla_jessietreegreen_1000_175_p` |
| `printedsolid_pla_jessiewhitepla_1000_175_p` | `printedsolid_pla_jessiewhite_1000_175_p` |
| `printedsolid_pla_jessieyellowbirdpla_1000_175_p` | `printedsolid_pla_jessieyellowbird_1000_175_p` |

Rename-only scope check:

```sh
python scripts/rename_migration.py --verify --base-ref 861fe11acd2e6d84efc09cc4abaa389bbe65eda5
```
