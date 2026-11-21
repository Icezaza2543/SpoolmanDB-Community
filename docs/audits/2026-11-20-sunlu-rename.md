# Sunlu rename migration — 2026-11-20

Starting commit: `460cbf0f5e1eca293bb60ffb79e07269a672a6be`. Upstream source: [Donkie/SpoolmanDB#527](https://github.com/Donkie/SpoolmanDB/pull/527), merge commit `772db6730b2adfd046be91d64914665268f1362e`.

This is an **intentional breaking catalog migration**. It applies the upstream Sunlu name cleanup: names no longer repeat the material. `High Speed Matte PETG - {color_name}` → `High Speed Matte - {color_name}` (PETG).

| Check | Result |
|---|---|
| Groups renamed | 1 (1 distinct template rename) |
| Public IDs retired as renames | 12 |
| New public IDs | 12, each the registered target of exactly one retirement |
| Existing retirements re-pointed to the final ID | 0 |
| Catalog size | 51,434 (unchanged) |
| Unregistered removals, changed or rekeyed identities | 0 |
| Material, weight, diameter, spool, colour and metadata changes | None |

Upstream #527 changes no colour names or other fields in this file.

Reproduce with:

```sh
python scripts/rename_migration.py --file sunlu.json \
    --upstream 772db6730b2adfd046be91d64914665268f1362e~1 772db6730b2adfd046be91d64914665268f1362e \
    --ref https://github.com/Donkie/SpoolmanDB/pull/527 --source 772db6730b2adfd046be91d64914665268f1362e \
    --base-ref 460cbf0f5e1eca293bb60ffb79e07269a672a6be
```

Retired IDs disappear from the published catalog. Existing Spoolman spools keep their local imported data; Spoolman does not read the registry or follow these mappings.

## Mapping

| Old public ID | New public ID |
|---|---|
| `sunlu_petg_highspeedmattepetg-black_1000_175_p` | `sunlu_petg_highspeedmatte-black_1000_175_p` |
| `sunlu_petg_highspeedmattepetg-blue_1000_175_p` | `sunlu_petg_highspeedmatte-blue_1000_175_p` |
| `sunlu_petg_highspeedmattepetg-green_1000_175_p` | `sunlu_petg_highspeedmatte-green_1000_175_p` |
| `sunlu_petg_highspeedmattepetg-grey_1000_175_p` | `sunlu_petg_highspeedmatte-grey_1000_175_p` |
| `sunlu_petg_highspeedmattepetg-mint_1000_175_p` | `sunlu_petg_highspeedmatte-mint_1000_175_p` |
| `sunlu_petg_highspeedmattepetg-olivegreen_1000_175_p` | `sunlu_petg_highspeedmatte-olivegreen_1000_175_p` |
| `sunlu_petg_highspeedmattepetg-orange_1000_175_p` | `sunlu_petg_highspeedmatte-orange_1000_175_p` |
| `sunlu_petg_highspeedmattepetg-pink_1000_175_p` | `sunlu_petg_highspeedmatte-pink_1000_175_p` |
| `sunlu_petg_highspeedmattepetg-red_1000_175_p` | `sunlu_petg_highspeedmatte-red_1000_175_p` |
| `sunlu_petg_highspeedmattepetg-skyblue_1000_175_p` | `sunlu_petg_highspeedmatte-skyblue_1000_175_p` |
| `sunlu_petg_highspeedmattepetg-white_1000_175_p` | `sunlu_petg_highspeedmatte-white_1000_175_p` |
| `sunlu_petg_highspeedmattepetg-yellow_1000_175_p` | `sunlu_petg_highspeedmatte-yellow_1000_175_p` |

Rename-only scope check:

```sh
python scripts/rename_migration.py --verify --base-ref 460cbf0f5e1eca293bb60ffb79e07269a672a6be
```
