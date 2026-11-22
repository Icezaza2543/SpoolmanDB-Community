# QIDI Tech rename migration — 2026-11-20

Starting commit: `3e2bc1bdc6accba996b8d32657f376a4313d2141`. Upstream source: [Donkie/SpoolmanDB#527](https://github.com/Donkie/SpoolmanDB/pull/527), merge commit `772db6730b2adfd046be91d64914665268f1362e`.

This is an **intentional breaking catalog migration**. It applies the upstream QIDI Tech name cleanup: names no longer repeat the material. `PETG-Tough {color_name}` → `Tough {color_name}` (PETG).

| Check | Result |
|---|---|
| Groups renamed | 1 (1 distinct template rename) |
| Public IDs retired as renames | 7 |
| New public IDs | 7, each the registered target of exactly one retirement |
| Existing retirements re-pointed to the final ID | 0 |
| Catalog size | 51,434 (unchanged) |
| Unregistered removals, changed or rekeyed identities | 0 |
| Material, weight, diameter, spool, colour and metadata changes | None |

Upstream #527 changes no colour names or other fields in this file.

Reproduce with:

```sh
python scripts/rename_migration.py --file qiditech.json \
    --upstream 772db6730b2adfd046be91d64914665268f1362e~1 772db6730b2adfd046be91d64914665268f1362e \
    --ref https://github.com/Donkie/SpoolmanDB/pull/527 --source 772db6730b2adfd046be91d64914665268f1362e \
    --base-ref 3e2bc1bdc6accba996b8d32657f376a4313d2141
```

Retired IDs disappear from the published catalog. Existing Spoolman spools keep their local imported data; Spoolman does not read the registry or follow these mappings.

## Not included

- '95A HF {color_name}' [TPU] -> 'HF {color_name}' [TPU-95A]: a material change, not a rename. It is left for the material reclassification work.

## Mapping

| Old public ID | New public ID |
|---|---|
| `qiditech_petg_petg-toughblack_1000_175_p` | `qiditech_petg_toughblack_1000_175_p` |
| `qiditech_petg_petg-toughblue_1000_175_p` | `qiditech_petg_toughblue_1000_175_p` |
| `qiditech_petg_petg-toughgreen_1000_175_p` | `qiditech_petg_toughgreen_1000_175_p` |
| `qiditech_petg_petg-toughorange_1000_175_p` | `qiditech_petg_toughorange_1000_175_p` |
| `qiditech_petg_petg-toughred_1000_175_p` | `qiditech_petg_toughred_1000_175_p` |
| `qiditech_petg_petg-toughwhite_1000_175_p` | `qiditech_petg_toughwhite_1000_175_p` |
| `qiditech_petg_petg-toughyellow_1000_175_p` | `qiditech_petg_toughyellow_1000_175_p` |

Rename-only scope check:

```sh
python scripts/rename_migration.py --verify --base-ref 3e2bc1bdc6accba996b8d32657f376a4313d2141
```
