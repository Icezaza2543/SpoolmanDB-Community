# Ambrosia rename migration — 2026-11-20

Starting commit: `3f4df3a0a6db8761b87ee69b68a8a641ec9e5b69`. Upstream source: [Donkie/SpoolmanDB#527](https://github.com/Donkie/SpoolmanDB/pull/527), merge commit `772db6730b2adfd046be91d64914665268f1362e`.

This is an **intentional breaking catalog migration**. It applies the upstream Ambrosia name cleanup: names no longer repeat the material. `Über ABS {color_name}` → `Über {color_name}` (ABS).

| Check | Result |
|---|---|
| Groups renamed | 1 (1 distinct template rename) |
| Public IDs retired as renames | 6 |
| New public IDs | 6, each the registered target of exactly one retirement |
| Existing retirements re-pointed to the final ID | 0 |
| Catalog size | 51,434 (unchanged) |
| Unregistered removals, changed or rekeyed identities | 0 |
| Material, weight, diameter, spool, colour and metadata changes | None |

Upstream #527 changes no colour names or other fields in this file.

Reproduce with:

```sh
python scripts/rename_migration.py --file ambrosia.json \
    --upstream 772db6730b2adfd046be91d64914665268f1362e~1 772db6730b2adfd046be91d64914665268f1362e \
    --ref https://github.com/Donkie/SpoolmanDB/pull/527 --source 772db6730b2adfd046be91d64914665268f1362e \
    --base-ref 3f4df3a0a6db8761b87ee69b68a8a641ec9e5b69
```

Retired IDs disappear from the published catalog. Existing Spoolman spools keep their local imported data; Spoolman does not read the registry or follow these mappings.

## Mapping

| Old public ID | New public ID |
|---|---|
| `ambrosia_abs_berabsblack_1000_175_c` | `ambrosia_abs_berblack_1000_175_c` |
| `ambrosia_abs_berabsnatural_1000_175_c` | `ambrosia_abs_bernatural_1000_175_c` |
| `ambrosia_abs_berabspastelpink_1000_175_c` | `ambrosia_abs_berpastelpink_1000_175_c` |
| `ambrosia_abs_berabspurple_1000_175_c` | `ambrosia_abs_berpurple_1000_175_c` |
| `ambrosia_abs_berabsred_1000_175_c` | `ambrosia_abs_berred_1000_175_c` |
| `ambrosia_abs_berabswhite_1000_175_c` | `ambrosia_abs_berwhite_1000_175_c` |

Rename-only scope check:

```sh
python scripts/rename_migration.py --verify --base-ref 3f4df3a0a6db8761b87ee69b68a8a641ec9e5b69
```
