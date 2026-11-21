# Overture Easy PLA rename migration — 2026-11-20

Starting commit: `f195426ddd9e4f0d2f589d0bc3b8943d25016496`. Upstream source: [Donkie/SpoolmanDB#532](https://github.com/Donkie/SpoolmanDB/pull/532), merge commit `8e391c16be4bfde29dfc184e2f0b9a8d154ab550`.

This is an **intentional breaking catalog migration**. Upstream #532 adds Overture Easy PLA as `Easy {color_name}`. Community already lists the same product line as `PLA Easy {color_name}` (24 colours) and `PLA Easy Glow {color_name}` (4 colours). Renaming both groups gives exactly upstream's 28 IDs, so the two catalogs agree on these filaments without adding duplicates: `PLA Easy {color_name}` → `Easy {color_name}` (PLA); `PLA Easy Glow {color_name}` → `Easy Glow {color_name}` (PLA).

| Check | Result |
|---|---|
| Groups renamed | 2 (2 distinct template renames) |
| Public IDs retired as renames | 28 |
| New public IDs | 28, each the registered target of exactly one retirement and identical to the ID upstream's #532 data produces |
| Existing retirements re-pointed to the final ID | 0 |
| Catalog size | 51,434 (unchanged) |
| Unregistered removals, changed or rekeyed identities | 0 |
| Material, weight, diameter, spool, colour and metadata changes | None |

Upstream has no `PLA Easy` group to rename, so this uses explicit `--rename` arguments. Community keeps the glow colours in their own group (upstream puts `Glow Blue` etc. in the `Easy` group); both give the same IDs, for example `overture_pla_easyglowblue_1000_175_c`.

Reproduce with:

```sh
python scripts/rename_migration.py --file overture.json \
    --rename "PLA Easy {color_name}" "Easy {color_name}" PLA \
    --rename "PLA Easy Glow {color_name}" "Easy Glow {color_name}" PLA \
    --ref https://github.com/Donkie/SpoolmanDB/pull/532 --source 8e391c16be4bfde29dfc184e2f0b9a8d154ab550 \
    --base-ref f195426ddd9e4f0d2f589d0bc3b8943d25016496
```

Retired IDs disappear from the published catalog. Existing Spoolman spools keep their local imported data; Spoolman does not read the registry or follow these mappings.

## Values not changed here

Upstream's record differs from Community in fields that do not affect IDs. This migration is rename-only, so it keeps the Community values. Overture's product page states only diameter (1.75 mm ± 0.02) and net weight (1 kg); it gives no density, temperatures or spool tare, so neither set is confirmed by the manufacturer.

| Field | Community | Upstream #532 |
|---|---|---|
| Density (`Easy`) | 1.16 | 1.24 |
| Spool weight (tare) | 173 g | 155 g |
| Extruder temperature range | 190–230 °C | 190–220 °C (210 °C recommended) |
| Bed temperature range | 50–70 °C | 25–60 °C (60 °C recommended) |
| Natural | `D9D8DE` | `CCCCCC` |
| Digital Blue | `0066D9` | `0696EF` |
| Shimmer Bronze | `99A45F` | `81BA6D` |
| Glow Blue | `5FBCDD` | `5EB7D4` |
| Glow Yellow | `EBFF57` | `EBFF6B` |

Upstream also marks the Shimmer colours `finish: glossy` and omits the Community colour codes (for example `VSA090017`).

## Mapping

| Old public ID | New public ID |
|---|---|
| `overture_pla_plaeasybeige_1000_175_c` | `overture_pla_easybeige_1000_175_c` |
| `overture_pla_plaeasyblack_1000_175_c` | `overture_pla_easyblack_1000_175_c` |
| `overture_pla_plaeasycaramel_1000_175_c` | `overture_pla_easycaramel_1000_175_c` |
| `overture_pla_plaeasycobaltblue_1000_175_c` | `overture_pla_easycobaltblue_1000_175_c` |
| `overture_pla_plaeasydigitalblue_1000_175_c` | `overture_pla_easydigitalblue_1000_175_c` |
| `overture_pla_plaeasyglowblue_1000_175_c` | `overture_pla_easyglowblue_1000_175_c` |
| `overture_pla_plaeasygloworange_1000_175_c` | `overture_pla_easygloworange_1000_175_c` |
| `overture_pla_plaeasyglowred_1000_175_c` | `overture_pla_easyglowred_1000_175_c` |
| `overture_pla_plaeasyglowyellow_1000_175_c` | `overture_pla_easyglowyellow_1000_175_c` |
| `overture_pla_plaeasygreen_1000_175_c` | `overture_pla_easygreen_1000_175_c` |
| `overture_pla_plaeasymagenta_1000_175_c` | `overture_pla_easymagenta_1000_175_c` |
| `overture_pla_plaeasynatural_1000_175_c` | `overture_pla_easynatural_1000_175_c` |
| `overture_pla_plaeasyorange_1000_175_c` | `overture_pla_easyorange_1000_175_c` |
| `overture_pla_plaeasypinegreen_1000_175_c` | `overture_pla_easypinegreen_1000_175_c` |
| `overture_pla_plaeasypink_1000_175_c` | `overture_pla_easypink_1000_175_c` |
| `overture_pla_plaeasypumpkinorange_1000_175_c` | `overture_pla_easypumpkinorange_1000_175_c` |
| `overture_pla_plaeasypurple_1000_175_c` | `overture_pla_easypurple_1000_175_c` |
| `overture_pla_plaeasyred_1000_175_c` | `overture_pla_easyred_1000_175_c` |
| `overture_pla_plaeasyrockwhite_1000_175_c` | `overture_pla_easyrockwhite_1000_175_c` |
| `overture_pla_plaeasyshimmerbronze_1000_175_c` | `overture_pla_easyshimmerbronze_1000_175_c` |
| `overture_pla_plaeasyshimmerdarkgreen_1000_175_c` | `overture_pla_easyshimmerdarkgreen_1000_175_c` |
| `overture_pla_plaeasyshimmerpurple_1000_175_c` | `overture_pla_easyshimmerpurple_1000_175_c` |
| `overture_pla_plaeasyshimmersilvergreen_1000_175_c` | `overture_pla_easyshimmersilvergreen_1000_175_c` |
| `overture_pla_plaeasyskyblue_1000_175_c` | `overture_pla_easyskyblue_1000_175_c` |
| `overture_pla_plaeasyspacegray_1000_175_c` | `overture_pla_easyspacegray_1000_175_c` |
| `overture_pla_plaeasywhite_1000_175_c` | `overture_pla_easywhite_1000_175_c` |
| `overture_pla_plaeasyyellow_1000_175_c` | `overture_pla_easyyellow_1000_175_c` |
| `overture_pla_plaeasyyolkyellow_1000_175_c` | `overture_pla_easyyolkyellow_1000_175_c` |

Rename-only scope check:

```sh
python scripts/rename_migration.py --verify --base-ref f195426ddd9e4f0d2f589d0bc3b8943d25016496
```
