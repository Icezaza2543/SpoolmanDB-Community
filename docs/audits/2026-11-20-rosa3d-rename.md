# Rosa3D rename migration — 2026-11-20

Starting commit: `480cad8110dc92ce01280e06cf702913b408f50f`. Upstream source: [Donkie/SpoolmanDB#527](https://github.com/Donkie/SpoolmanDB/pull/527), merge commit `772db6730b2adfd046be91d64914665268f1362e`.

This is an **intentional breaking catalog migration**. It applies the upstream Rosa3D name cleanup: names no longer repeat the material. `PLA Starter {color_name}` → `Starter {color_name}` (PLA).

| Check | Result |
|---|---|
| Groups renamed | 1 (1 distinct template rename) |
| Public IDs retired as renames | 41 |
| New public IDs | 41, each the registered target of exactly one retirement |
| Existing retirements re-pointed to the final ID | 0 |
| Catalog size | 51,434 (unchanged) |
| Unregistered removals, changed or rekeyed identities | 0 |
| Material, weight, diameter, spool, colour and metadata changes | None |

Upstream #527 changes no colour names or other fields in this file.

Reproduce with:

```sh
python scripts/rename_migration.py --file rosa3d.json \
    --upstream 772db6730b2adfd046be91d64914665268f1362e~1 772db6730b2adfd046be91d64914665268f1362e \
    --ref https://github.com/Donkie/SpoolmanDB/pull/527 --source 772db6730b2adfd046be91d64914665268f1362e \
    --base-ref 480cad8110dc92ce01280e06cf702913b408f50f
```

Retired IDs disappear from the published catalog. Existing Spoolman spools keep their local imported data; Spoolman does not read the registry or follow these mappings.

## Mapping

| Old public ID | New public ID |
|---|---|
| `rosa3d_pla_plastarterarmygreen_1000_175_p` | `rosa3d_pla_starterarmygreen_1000_175_p` |
| `rosa3d_pla_plastarterblack_1000_175_p` | `rosa3d_pla_starterblack_1000_175_p` |
| `rosa3d_pla_plastarterblue_1000_175_p` | `rosa3d_pla_starterblue_1000_175_p` |
| `rosa3d_pla_plastarterbluepearl_1000_175_p` | `rosa3d_pla_starterbluepearl_1000_175_p` |
| `rosa3d_pla_plastarterbluesky_1000_175_p` | `rosa3d_pla_starterbluesky_1000_175_p` |
| `rosa3d_pla_plastartercarpibluesatin_1000_175_p` | `rosa3d_pla_startercarpibluesatin_1000_175_p` |
| `rosa3d_pla_plastarterchocolatebrown_1000_175_p` | `rosa3d_pla_starterchocolatebrown_1000_175_p` |
| `rosa3d_pla_plastarterdarkblue_1000_175_p` | `rosa3d_pla_starterdarkblue_1000_175_p` |
| `rosa3d_pla_plastarteremeraldgreensatin_1000_175_p` | `rosa3d_pla_starteremeraldgreensatin_1000_175_p` |
| `rosa3d_pla_plastarterglitterbronze_1000_175_p` | `rosa3d_pla_starterglitterbronze_1000_175_p` |
| `rosa3d_pla_plastarterglittergraphite_1000_175_p` | `rosa3d_pla_starterglittergraphite_1000_175_p` |
| `rosa3d_pla_plastartergray_1000_175_p` | `rosa3d_pla_startergray_1000_175_p` |
| `rosa3d_pla_plastartergreen_1000_175_p` | `rosa3d_pla_startergreen_1000_175_p` |
| `rosa3d_pla_plastarterhuntergreen_1000_175_p` | `rosa3d_pla_starterhuntergreen_1000_175_p` |
| `rosa3d_pla_plastarterjuicygreen_1000_175_p` | `rosa3d_pla_starterjuicygreen_1000_175_p` |
| `rosa3d_pla_plastarterkarminred_1000_175_p` | `rosa3d_pla_starterkarminred_1000_175_p` |
| `rosa3d_pla_plastarterlightbrown_1000_175_p` | `rosa3d_pla_starterlightbrown_1000_175_p` |
| `rosa3d_pla_plastarterlightgray_1000_175_p` | `rosa3d_pla_starterlightgray_1000_175_p` |
| `rosa3d_pla_plastartermochamousse_1000_175_p` | `rosa3d_pla_startermochamousse_1000_175_p` |
| `rosa3d_pla_plastarternatural_1000_175_p` | `rosa3d_pla_starternatural_1000_175_p` |
| `rosa3d_pla_plastarterneonfluo_1000_175_p` | `rosa3d_pla_starterneonfluo_1000_175_p` |
| `rosa3d_pla_plastarterneongreen_1000_175_p` | `rosa3d_pla_starterneongreen_1000_175_p` |
| `rosa3d_pla_plastarterneonorange_1000_175_p` | `rosa3d_pla_starterneonorange_1000_175_p` |
| `rosa3d_pla_plastarterorange_1000_175_p` | `rosa3d_pla_starterorange_1000_175_p` |
| `rosa3d_pla_plastarteroxygreen_1000_175_p` | `rosa3d_pla_starteroxygreen_1000_175_p` |
| `rosa3d_pla_plastarterpearlgold_1000_175_p` | `rosa3d_pla_starterpearlgold_1000_175_p` |
| `rosa3d_pla_plastarterpink_1000_175_p` | `rosa3d_pla_starterpink_1000_175_p` |
| `rosa3d_pla_plastarterporcelainskin_1000_175_p` | `rosa3d_pla_starterporcelainskin_1000_175_p` |
| `rosa3d_pla_plastarterred_1000_175_p` | `rosa3d_pla_starterred_1000_175_p` |
| `rosa3d_pla_plastarterredjaspersatin_1000_175_p` | `rosa3d_pla_starterredjaspersatin_1000_175_p` |
| `rosa3d_pla_plastarterresedagreen_1000_175_p` | `rosa3d_pla_starterresedagreen_1000_175_p` |
| `rosa3d_pla_plastarterrosebeigeskin_1000_175_p` | `rosa3d_pla_starterrosebeigeskin_1000_175_p` |
| `rosa3d_pla_plastarterrubinred_1000_175_p` | `rosa3d_pla_starterrubinred_1000_175_p` |
| `rosa3d_pla_plastartersatingrey_1000_175_p` | `rosa3d_pla_startersatingrey_1000_175_p` |
| `rosa3d_pla_plastartersatinpink_1000_175_p` | `rosa3d_pla_startersatinpink_1000_175_p` |
| `rosa3d_pla_plastartersignalviolet_1000_175_p` | `rosa3d_pla_startersignalviolet_1000_175_p` |
| `rosa3d_pla_plastartertannedskin_1000_175_p` | `rosa3d_pla_startertannedskin_1000_175_p` |
| `rosa3d_pla_plastartervioletdynamic_1000_175_p` | `rosa3d_pla_startervioletdynamic_1000_175_p` |
| `rosa3d_pla_plastarterwhite_1000_175_p` | `rosa3d_pla_starterwhite_1000_175_p` |
| `rosa3d_pla_plastarterwinterwhite_1000_175_p` | `rosa3d_pla_starterwinterwhite_1000_175_p` |
| `rosa3d_pla_plastarteryellow_1000_175_p` | `rosa3d_pla_starteryellow_1000_175_p` |

Rename-only scope check:

```sh
python scripts/rename_migration.py --verify --base-ref 480cad8110dc92ce01280e06cf702913b408f50f
```
