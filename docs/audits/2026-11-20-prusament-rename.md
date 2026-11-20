# Prusament rename migration — 2026-11-20

Starting commit: `07206f18e85d65fb4c04fd5b12c1ea7c12ac40d6`. Upstream source: [Donkie/SpoolmanDB#527](https://github.com/Donkie/SpoolmanDB/pull/527), merge commit `772db6730b2adfd046be91d64914665268f1362e`.

This is an **intentional breaking catalog migration**. It applies the upstream Prusament name cleanup: names no longer repeat the material. `PC Blend Carbon Fiber {color_name}` → `Blend {color_name}` (PC-CF).

| Check | Result |
|---|---|
| Groups renamed | 1 (1 distinct template rename) |
| Public IDs retired as renames | 1 |
| New public IDs | 1, each the registered target of exactly one retirement |
| Existing retirements re-pointed to the final ID | 0 |
| Catalog size | 51,434 (unchanged) |
| Unregistered removals, changed or rekeyed identities | 0 |
| Material, weight, diameter, spool, colour and metadata changes | None |

Upstream #527 changes no colour names or other fields in this file.

Reproduce with:

```sh
python scripts/rename_migration.py --file prusament.json \
    --upstream 772db6730b2adfd046be91d64914665268f1362e~1 772db6730b2adfd046be91d64914665268f1362e \
    --ref https://github.com/Donkie/SpoolmanDB/pull/527 --source 772db6730b2adfd046be91d64914665268f1362e \
    --base-ref 07206f18e85d65fb4c04fd5b12c1ea7c12ac40d6
```

Retired IDs disappear from the published catalog. Existing Spoolman spools keep their local imported data; Spoolman does not read the registry or follow these mappings.

## Mapping

| Old public ID | New public ID |
|---|---|
| `prusament_pc-cf_pcblendcarbonfiberblack_800_175_p` | `prusament_pc-cf_blendblack_800_175_p` |

Rename-only scope check:

```sh
python scripts/rename_migration.py --verify --base-ref 07206f18e85d65fb4c04fd5b12c1ea7c12ac40d6
```
