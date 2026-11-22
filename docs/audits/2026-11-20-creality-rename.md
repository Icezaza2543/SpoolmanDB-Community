# Creality rename migration — 2026-11-20

Starting commit: `19ed8d10274754f186bd64a2f218128d67cbb478`. Upstream source: [Donkie/SpoolmanDB#527](https://github.com/Donkie/SpoolmanDB/pull/527), merge commit `772db6730b2adfd046be91d64914665268f1362e`.

This is an **intentional breaking catalog migration**. It applies the upstream Creality name cleanup: names no longer repeat the material. `CR-PETG {color_name}` → `CR {color_name}` (PETG); `Ender-PLA {color_name}` → `Ender {color_name}` (PLA); `{color_name} Hyper ABS` → `{color_name} Hyper` (ABS).

| Check | Result |
|---|---|
| Groups renamed | 3 (3 distinct template renames) |
| Public IDs retired as renames | 13 |
| New public IDs | 13, each the registered target of exactly one retirement |
| Existing retirements re-pointed to the final ID | 0 |
| Catalog size | 51,434 (unchanged) |
| Unregistered removals, changed or rekeyed identities | 0 |
| Material, weight, diameter, spool, colour and metadata changes | None |

Upstream #527 changes no colour names or other fields in this file.

Reproduce with:

```sh
python scripts/rename_migration.py --file creality.json \
    --upstream 772db6730b2adfd046be91d64914665268f1362e~1 772db6730b2adfd046be91d64914665268f1362e \
    --ref https://github.com/Donkie/SpoolmanDB/pull/527 --source 772db6730b2adfd046be91d64914665268f1362e \
    --base-ref 19ed8d10274754f186bd64a2f218128d67cbb478
```

Retired IDs disappear from the published catalog. Existing Spoolman spools keep their local imported data; Spoolman does not read the registry or follow these mappings.

## Mapping

| Old public ID | New public ID |
|---|---|
| `creality_abs_blackhyperabs_1000_175_c` | `creality_abs_blackhyper_1000_175_c` |
| `creality_abs_greyhyperabs_1000_175_c` | `creality_abs_greyhyper_1000_175_c` |
| `creality_abs_whitehyperabs_1000_175_c` | `creality_abs_whitehyper_1000_175_c` |
| `creality_petg_cr-petgblack_1000_175_p` | `creality_petg_crblack_1000_175_p` |
| `creality_petg_cr-petgblue_1000_175_p` | `creality_petg_crblue_1000_175_p` |
| `creality_petg_cr-petggrey_1000_175_p` | `creality_petg_crgrey_1000_175_p` |
| `creality_petg_cr-petgred_1000_175_p` | `creality_petg_crred_1000_175_p` |
| `creality_petg_cr-petgtransparent_1000_175_p` | `creality_petg_crtransparent_1000_175_p` |
| `creality_petg_cr-petgwhite_1000_175_p` | `creality_petg_crwhite_1000_175_p` |
| `creality_pla_ender-plablack_1000_175_c` | `creality_pla_enderblack_1000_175_c` |
| `creality_pla_ender-plablue_1000_175_c` | `creality_pla_enderblue_1000_175_c` |
| `creality_pla_ender-plared_1000_175_c` | `creality_pla_enderred_1000_175_c` |
| `creality_pla_ender-plawhite_1000_175_c` | `creality_pla_enderwhite_1000_175_c` |

Rename-only scope check:

```sh
python scripts/rename_migration.py --verify --base-ref 19ed8d10274754f186bd64a2f218128d67cbb478
```
