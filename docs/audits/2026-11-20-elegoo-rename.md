# ELEGOO rename migration — 2026-11-20

Starting commit: `af20509b64b3a278c3db130c903a09c376979b97`. Upstream source: [Donkie/SpoolmanDB#527](https://github.com/Donkie/SpoolmanDB/pull/527), merge commit `772db6730b2adfd046be91d64914665268f1362e`.

This is an **intentional breaking catalog migration**. It applies the upstream ELEGOO name cleanup: names no longer repeat the material. `PETG PRO {color_name}` → `PRO {color_name}` (PETG); `RAPID PETG {color_name}` → `RAPID {color_name}` (PETG); `RAPID PLA+ {color_name}` → `RAPID {color_name}` (PLA+).

| Check | Result |
|---|---|
| Groups renamed | 3 (3 distinct template renames) |
| Public IDs retired as renames | 48 |
| New public IDs | 48, each the registered target of exactly one retirement |
| Existing retirements re-pointed to the final ID | 12 (evidence and `retired_key` unchanged) |
| Catalog size | 51,434 (unchanged) |
| Unregistered removals, changed or rekeyed identities | 0 |
| Material, weight, diameter, spool, colour and metadata changes | None |

Upstream #527 changes no colour names or other fields in this file.

Reproduce with:

```sh
python scripts/rename_migration.py --file elegoo.json \
    --upstream 772db6730b2adfd046be91d64914665268f1362e~1 772db6730b2adfd046be91d64914665268f1362e \
    --ref https://github.com/Donkie/SpoolmanDB/pull/527 --source 772db6730b2adfd046be91d64914665268f1362e \
    --base-ref af20509b64b3a278c3db130c903a09c376979b97
```

Retired IDs disappear from the published catalog. Existing Spoolman spools keep their local imported data; Spoolman does not read the registry or follow these mappings.

## Re-pointed retirements

These earlier retirements pointed at IDs this migration renames. Only `replaced_by` changes, so the registry never forms a chain.

| Retired ID | Previous target | New target |
|---|---|---|
| `elegoo_petg_petgrapidbeige_1000_175_c` | `elegoo_petg_rapidpetgbeige_1000_175_c` | `elegoo_petg_rapidbeige_1000_175_c` |
| `elegoo_petg_petgrapidblack_1000_175_c` | `elegoo_petg_rapidpetgblack_1000_175_c` | `elegoo_petg_rapidblack_1000_175_c` |
| `elegoo_petg_petgrapidblue_1000_175_c` | `elegoo_petg_rapidpetgblue_1000_175_c` | `elegoo_petg_rapidblue_1000_175_c` |
| `elegoo_petg_petgrapidbrown_1000_175_c` | `elegoo_petg_rapidpetgbrown_1000_175_c` | `elegoo_petg_rapidbrown_1000_175_c` |
| `elegoo_petg_petgrapidgreen_1000_175_c` | `elegoo_petg_rapidpetggreen_1000_175_c` | `elegoo_petg_rapidgreen_1000_175_c` |
| `elegoo_petg_petgrapidgrey_1000_175_c` | `elegoo_petg_rapidpetggrey_1000_175_c` | `elegoo_petg_rapidgrey_1000_175_c` |
| `elegoo_petg_petgrapidorange_1000_175_c` | `elegoo_petg_rapidpetgorange_1000_175_c` | `elegoo_petg_rapidorange_1000_175_c` |
| `elegoo_petg_petgrapidred_1000_175_c` | `elegoo_petg_rapidpetgred_1000_175_c` | `elegoo_petg_rapidred_1000_175_c` |
| `elegoo_petg_petgrapidspacegrey_1000_175_c` | `elegoo_petg_rapidpetgspacegrey_1000_175_c` | `elegoo_petg_rapidspacegrey_1000_175_c` |
| `elegoo_petg_petgrapidtransparent_1000_175_c` | `elegoo_petg_rapidpetgtransparent_1000_175_c` | `elegoo_petg_rapidtransparent_1000_175_c` |
| `elegoo_petg_petgrapidwhite_1000_175_c` | `elegoo_petg_rapidpetgwhite_1000_175_c` | `elegoo_petg_rapidwhite_1000_175_c` |
| `elegoo_petg_petgrapidyellow_1000_175_c` | `elegoo_petg_rapidpetgyellow_1000_175_c` | `elegoo_petg_rapidyellow_1000_175_c` |

## Mapping

| Old public ID | New public ID |
|---|---|
| `elegoo_petg_petgproblack_1000_175_c` | `elegoo_petg_problack_1000_175_c` |
| `elegoo_petg_petgproblue_1000_175_c` | `elegoo_petg_problue_1000_175_c` |
| `elegoo_petg_petgproburgundyred_1000_175_c` | `elegoo_petg_proburgundyred_1000_175_c` |
| `elegoo_petg_petgprogreen_1000_175_c` | `elegoo_petg_progreen_1000_175_c` |
| `elegoo_petg_petgprogrey_1000_175_c` | `elegoo_petg_progrey_1000_175_c` |
| `elegoo_petg_petgprolightblue_1000_175_c` | `elegoo_petg_prolightblue_1000_175_c` |
| `elegoo_petg_petgproolivegreen_1000_175_c` | `elegoo_petg_proolivegreen_1000_175_c` |
| `elegoo_petg_petgpropink_1000_175_c` | `elegoo_petg_propink_1000_175_c` |
| `elegoo_petg_petgpropurple_1000_175_c` | `elegoo_petg_propurple_1000_175_c` |
| `elegoo_petg_petgprored_1000_175_c` | `elegoo_petg_prored_1000_175_c` |
| `elegoo_petg_petgprosilver_1000_175_c` | `elegoo_petg_prosilver_1000_175_c` |
| `elegoo_petg_petgprowhite_1000_175_c` | `elegoo_petg_prowhite_1000_175_c` |
| `elegoo_petg_petgproyellow_1000_175_c` | `elegoo_petg_proyellow_1000_175_c` |
| `elegoo_petg_rapidpetgbeige_1000_175_c` | `elegoo_petg_rapidbeige_1000_175_c` |
| `elegoo_petg_rapidpetgblack_1000_175_c` | `elegoo_petg_rapidblack_1000_175_c` |
| `elegoo_petg_rapidpetgblue_1000_175_c` | `elegoo_petg_rapidblue_1000_175_c` |
| `elegoo_petg_rapidpetgbrown_1000_175_c` | `elegoo_petg_rapidbrown_1000_175_c` |
| `elegoo_petg_rapidpetggreen_1000_175_c` | `elegoo_petg_rapidgreen_1000_175_c` |
| `elegoo_petg_rapidpetggrey_1000_175_c` | `elegoo_petg_rapidgrey_1000_175_c` |
| `elegoo_petg_rapidpetgorange_1000_175_c` | `elegoo_petg_rapidorange_1000_175_c` |
| `elegoo_petg_rapidpetgred_1000_175_c` | `elegoo_petg_rapidred_1000_175_c` |
| `elegoo_petg_rapidpetgsilver_1000_175_c` | `elegoo_petg_rapidsilver_1000_175_c` |
| `elegoo_petg_rapidpetgspacegrey_1000_175_c` | `elegoo_petg_rapidspacegrey_1000_175_c` |
| `elegoo_petg_rapidpetgtransparent_1000_175_c` | `elegoo_petg_rapidtransparent_1000_175_c` |
| `elegoo_petg_rapidpetgwhite_1000_175_c` | `elegoo_petg_rapidwhite_1000_175_c` |
| `elegoo_petg_rapidpetgyellow_1000_175_c` | `elegoo_petg_rapidyellow_1000_175_c` |
| `elegoo_pla+_rapidpla+beige_1000_175_c` | `elegoo_pla+_rapidbeige_1000_175_c` |
| `elegoo_pla+_rapidpla+beige_1000_175_r` | `elegoo_pla+_rapidbeige_1000_175_r` |
| `elegoo_pla+_rapidpla+black_1000_175_c` | `elegoo_pla+_rapidblack_1000_175_c` |
| `elegoo_pla+_rapidpla+black_1000_175_r` | `elegoo_pla+_rapidblack_1000_175_r` |
| `elegoo_pla+_rapidpla+blue_1000_175_c` | `elegoo_pla+_rapidblue_1000_175_c` |
| `elegoo_pla+_rapidpla+blue_1000_175_r` | `elegoo_pla+_rapidblue_1000_175_r` |
| `elegoo_pla+_rapidpla+brown_1000_175_c` | `elegoo_pla+_rapidbrown_1000_175_c` |
| `elegoo_pla+_rapidpla+brown_1000_175_r` | `elegoo_pla+_rapidbrown_1000_175_r` |
| `elegoo_pla+_rapidpla+green_1000_175_c` | `elegoo_pla+_rapidgreen_1000_175_c` |
| `elegoo_pla+_rapidpla+green_1000_175_r` | `elegoo_pla+_rapidgreen_1000_175_r` |
| `elegoo_pla+_rapidpla+grey_1000_175_c` | `elegoo_pla+_rapidgrey_1000_175_c` |
| `elegoo_pla+_rapidpla+grey_1000_175_r` | `elegoo_pla+_rapidgrey_1000_175_r` |
| `elegoo_pla+_rapidpla+orange_1000_175_c` | `elegoo_pla+_rapidorange_1000_175_c` |
| `elegoo_pla+_rapidpla+orange_1000_175_r` | `elegoo_pla+_rapidorange_1000_175_r` |
| `elegoo_pla+_rapidpla+red_1000_175_c` | `elegoo_pla+_rapidred_1000_175_c` |
| `elegoo_pla+_rapidpla+red_1000_175_r` | `elegoo_pla+_rapidred_1000_175_r` |
| `elegoo_pla+_rapidpla+silver_1000_175_c` | `elegoo_pla+_rapidsilver_1000_175_c` |
| `elegoo_pla+_rapidpla+silver_1000_175_r` | `elegoo_pla+_rapidsilver_1000_175_r` |
| `elegoo_pla+_rapidpla+white_1000_175_c` | `elegoo_pla+_rapidwhite_1000_175_c` |
| `elegoo_pla+_rapidpla+white_1000_175_r` | `elegoo_pla+_rapidwhite_1000_175_r` |
| `elegoo_pla+_rapidpla+yellow_1000_175_c` | `elegoo_pla+_rapidyellow_1000_175_c` |
| `elegoo_pla+_rapidpla+yellow_1000_175_r` | `elegoo_pla+_rapidyellow_1000_175_r` |

Rename-only scope check:

```sh
python scripts/rename_migration.py --verify --base-ref af20509b64b3a278c3db130c903a09c376979b97
```
