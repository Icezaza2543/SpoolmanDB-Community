# Soleyin rename migration — 2026-11-20

Starting commit: `bad9f5d6d420e9a586c85d07a2fa267cdc5eba2b`. Upstream source: [Donkie/SpoolmanDB#527](https://github.com/Donkie/SpoolmanDB/pull/527), merge commit `772db6730b2adfd046be91d64914665268f1362e`.

This is an **intentional breaking catalog migration**. It applies the upstream Soleyin name cleanup: names no longer repeat the material. `Ultra PLA {color_name}` → `Ultra {color_name}` (PLA).

| Check | Result |
|---|---|
| Groups renamed | 1 (1 distinct template rename) |
| Public IDs retired as renames | 17 |
| New public IDs | 17, each the registered target of exactly one retirement |
| Existing retirements re-pointed to the final ID | 0 |
| Catalog size | 51,434 (unchanged) |
| Unregistered removals, changed or rekeyed identities | 0 |
| Material, weight, diameter, spool, colour and metadata changes | None |

Upstream #527 changes no colour names or other fields in this file.

Reproduce with:

```sh
python scripts/rename_migration.py --file soleyin.json \
    --upstream 772db6730b2adfd046be91d64914665268f1362e~1 772db6730b2adfd046be91d64914665268f1362e \
    --ref https://github.com/Donkie/SpoolmanDB/pull/527 --source 772db6730b2adfd046be91d64914665268f1362e \
    --base-ref bad9f5d6d420e9a586c85d07a2fa267cdc5eba2b
```

Retired IDs disappear from the published catalog. Existing Spoolman spools keep their local imported data; Spoolman does not read the registry or follow these mappings.

## Mapping

| Old public ID | New public ID |
|---|---|
| `soleyin_pla_ultraplaalmondpurple_1000_175_p` | `soleyin_pla_ultraalmondpurple_1000_175_p` |
| `soleyin_pla_ultraplablack_1000_175_p` | `soleyin_pla_ultrablack_1000_175_p` |
| `soleyin_pla_ultraplagray_1000_175_p` | `soleyin_pla_ultragray_1000_175_p` |
| `soleyin_pla_ultraplagreenery_1000_175_p` | `soleyin_pla_ultragreenery_1000_175_p` |
| `soleyin_pla_ultraplalightgreen_1000_175_p` | `soleyin_pla_ultralightgreen_1000_175_p` |
| `soleyin_pla_ultraplamatteblack_1000_175_p` | `soleyin_pla_ultramatteblack_1000_175_p` |
| `soleyin_pla_ultraplamattefluorite_1000_175_p` | `soleyin_pla_ultramattefluorite_1000_175_p` |
| `soleyin_pla_ultraplamattegreenery_1000_175_p` | `soleyin_pla_ultramattegreenery_1000_175_p` |
| `soleyin_pla_ultraplamattegrey_1000_175_p` | `soleyin_pla_ultramattegrey_1000_175_p` |
| `soleyin_pla_ultraplamattemoonstone_1000_175_p` | `soleyin_pla_ultramattemoonstone_1000_175_p` |
| `soleyin_pla_ultraplamatterosestone_1000_175_p` | `soleyin_pla_ultramatterosestone_1000_175_p` |
| `soleyin_pla_ultraplamattewhite_1000_175_p` | `soleyin_pla_ultramattewhite_1000_175_p` |
| `soleyin_pla_ultraplaoceanblue_1000_175_p` | `soleyin_pla_ultraoceanblue_1000_175_p` |
| `soleyin_pla_ultraplapineappleyellow_1000_175_p` | `soleyin_pla_ultrapineappleyellow_1000_175_p` |
| `soleyin_pla_ultraplarosehip_1000_175_p` | `soleyin_pla_ultrarosehip_1000_175_p` |
| `soleyin_pla_ultraplastrawberrymilk_1000_175_p` | `soleyin_pla_ultrastrawberrymilk_1000_175_p` |
| `soleyin_pla_ultraplawhite_1000_175_p` | `soleyin_pla_ultrawhite_1000_175_p` |

Rename-only scope check:

```sh
python scripts/rename_migration.py --verify --base-ref bad9f5d6d420e9a586c85d07a2fa267cdc5eba2b
```
