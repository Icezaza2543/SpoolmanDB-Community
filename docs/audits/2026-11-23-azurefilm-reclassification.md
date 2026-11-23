# AzureFilm material reclassification — 2026-11-23

Starting commit: `d54e3eb` (Community `main` after #89). Upstream source: [Donkie/SpoolmanDB#515](https://github.com/Donkie/SpoolmanDB/pull/515), merge commit `f320e26d16906cfaa10943c82714cab22600810b`. Process: [Icezaza2543/SpoolmanDB-Community#86](https://github.com/Icezaza2543/SpoolmanDB-Community/issues/86).

This is an **intentional breaking catalog migration** and the pilot for `reason: "reclassification"`. It moves AzureFilm groups from a generic material code to a more specific one for the same physical product. Upstream #515 is the reason to look, but not the evidence: each mapping below is backed by a product listing that names the hardness or base polymer for that colour. Following #86, a colour without such a listing keeps its material and ID.

| Check | Result |
|---|---|
| Groups reclassified | 5 (two runs, because the two `Carbon Fiber` groups go to different codes) |
| Public IDs retired as reclassifications | 20 |
| New public IDs | 20, each the registered target of exactly one retirement |
| Kept on their current material and ID | 1 (PC ABS White) |
| Catalog size | 51,446 (unchanged) |
| Unregistered removals, changed or rekeyed identities | 0 |
| Weight, diameter, spool, colour and metadata changes | None |
| `materials.json` | `TPU-98A` added, density 1.16 (the existing AzureFilm 98A value) |

## Mappings and evidence

| Community group (before) | After | IDs | Evidence |
|---|---|---:|---|
| `85A {color_name}` (TPU) | `{color_name}` (TPU-85A) | 8 | 3DJake lists each colour as AzureFilm Flexible 85A, Shore hardness A85: [Transparent](https://www.3djake.com/azurefilm/flexible-85a-transparent), [White](https://www.3djake.com/azurefilm/flexible-85a-white), [Neon Yellow](https://www.3djake.com/azurefilm/flexible-85a-neon-yellow), [Neon Orange](https://www.3djake.com/azurefilm/flexible-85a-neon-orange), [Red](https://www.3djake.com/azurefilm/flexible-85a-red), [Neon Green](https://www.3djake.com/azurefilm/flexible-85a-neon-green), [Blue](https://www.3djake.com/azurefilm/flexible-85a-blue), [Black](https://www.3djake.com/azurefilm/flexible-85a-black). |
| `98A {color_name}` (TPU) | `{color_name}` (TPU-98A) | 8 | 3DJake, Shore hardness A98: [White](https://www.3djake.com/azurefilm/flexible-98a-white), [Neon Yellow](https://www.3djake.com/azurefilm/flexible-98a-neon-yellow), [Red](https://www.3djake.com/azurefilm/flexible-98a-red), [Blue](https://www.3djake.com/azurefilm/flexible-98a-blue), [Black](https://www.3djake.com/azurefilm/flexible-98a-black). Tinytronics, material TPU, hardness 98A, with AzureFilm SKUs: [Transparent](https://www.tinytronics.nl/en/azurefilm-tpu-98a-filament-1.75mm-300g-transparent) (FT983-0000), [Neon Orange](https://www.tinytronics.nl/en/azurefilm-tpu-98a-filament-1.75mm-300g-neon-orange) (FT983-2007FL), [Neon Green](https://www.tinytronics.nl/en/azurefilm-tpu-98a-filament-1.75mm-300g-neon-green) (FT983-6018FL). |
| `PC ABS {color_name}` (PC), Natural and Black | `{color_name}` (PC+ABS) | 2 | Tinytronics, material PC+ABS: [Natural](https://www.tinytronics.nl/en/azurefilm-pc-abs-filament-1.75mm-1kg-natural) (FB171-0000), [Black](https://www.tinytronics.nl/en/azurefilm-pc-abs-filament-1.75mm-1kg-black) (FB171-9005). 3DJake, product type PC-ABS: [Natural](https://www.3djake.com/azurefilm/pc-abs-natural-2), [Black](https://www.3djake.com/azurefilm/pc-abs-black-1). |
| `Carbon Fiber {color_name}` (CF), colour `PAHT` | `{color_name}` (PAHT-CF) | 1 | [3DJake](https://www.3djake.com/azurefilm/paht-carbon-fibre-1): "a high-temperature material based on polyamide", sold as PAHT Carbon Fibre. |
| `Carbon Fiber {color_name}` (CF), colour `PET` | `{color_name}` (PET-CF) | 1 | [3DJake](https://www.3djake.com/azurefilm/pet-carbon-fibre): "a carbon fibre reinforced PET material", product type PET / Copolyester. |

AzureFilm's own pages for these discontinued products now return 404, and the Wayback Machine was unavailable on 2026-11-23, so the evidence is from retailer listings that carry the manufacturer's specifications (and, at Tinytronics, its SKUs). Some listings are for 300 g or 650 g spools; hardness and base polymer belong to the product, and this migration does not change the 1 kg package.

### Differences from upstream #515

- **PET Carbon Fiber → `PET-CF`, not `PETG-CF`.** The product is sold as carbon fibre reinforced PET. `PETG-CF` would name a different polymer.
- **PAHT Carbon Fiber → `PAHT-CF`, not `PA-CF`.** Both refine `CF` and both are true; `PAHT-CF` is already in `materials.json` and matches the product name.
- **PC ABS White is kept on `PC`** (`azurefilm_pc_pcabswhite_1000_175_p`). Only Natural and Black have a product listing. Upstream moved all three.

So 18 of the 20 new IDs match upstream's; the two carbon fibre IDs differ.

## ID mapping

| Retired ID | Replacement |
|---|---|
| `azurefilm_tpu_85a85atransparent_1000_175_p` | `azurefilm_tpu-85a_85atransparent_1000_175_p` |
| `azurefilm_tpu_85a85awhite_1000_175_p` | `azurefilm_tpu-85a_85awhite_1000_175_p` |
| `azurefilm_tpu_85a85aneonyellow_1000_175_p` | `azurefilm_tpu-85a_85aneonyellow_1000_175_p` |
| `azurefilm_tpu_85a85aneonorange_1000_175_p` | `azurefilm_tpu-85a_85aneonorange_1000_175_p` |
| `azurefilm_tpu_85a85ared_1000_175_p` | `azurefilm_tpu-85a_85ared_1000_175_p` |
| `azurefilm_tpu_85a85aneongreen_1000_175_p` | `azurefilm_tpu-85a_85aneongreen_1000_175_p` |
| `azurefilm_tpu_85a85ablue_1000_175_p` | `azurefilm_tpu-85a_85ablue_1000_175_p` |
| `azurefilm_tpu_85a85ablack_1000_175_p` | `azurefilm_tpu-85a_85ablack_1000_175_p` |
| `azurefilm_tpu_98a98atransparent_1000_175_p` | `azurefilm_tpu-98a_98atransparent_1000_175_p` |
| `azurefilm_tpu_98a98awhite_1000_175_p` | `azurefilm_tpu-98a_98awhite_1000_175_p` |
| `azurefilm_tpu_98a98aneonyellow_1000_175_p` | `azurefilm_tpu-98a_98aneonyellow_1000_175_p` |
| `azurefilm_tpu_98a98aneonorange_1000_175_p` | `azurefilm_tpu-98a_98aneonorange_1000_175_p` |
| `azurefilm_tpu_98a98ared_1000_175_p` | `azurefilm_tpu-98a_98ared_1000_175_p` |
| `azurefilm_tpu_98a98aneongreen_1000_175_p` | `azurefilm_tpu-98a_98aneongreen_1000_175_p` |
| `azurefilm_tpu_98a98ablue_1000_175_p` | `azurefilm_tpu-98a_98ablue_1000_175_p` |
| `azurefilm_tpu_98a98ablack_1000_175_p` | `azurefilm_tpu-98a_98ablack_1000_175_p` |
| `azurefilm_pc_pcabsnatur_1000_175_p` | `azurefilm_pc+abs_natur_1000_175_p` |
| `azurefilm_pc_pcabsblack_1000_175_p` | `azurefilm_pc+abs_black_1000_175_p` |
| `azurefilm_cf_carbonfiberpaht_1000_175_p` | `azurefilm_paht-cf_paht_1000_175_p` |
| `azurefilm_cf_carbonfiberpet_1000_175_p` | `azurefilm_pet-cf_pet_1000_175_p` |

Reproduce with (after adding `TPU-98A` to `materials.json`):

```sh
python scripts/rename_migration.py --file AzureFilm.json \
    --reclassify "85A {color_name}" "{color_name}" TPU TPU-85A \
    --reclassify "98A {color_name}" "{color_name}" TPU TPU-98A \
    --reclassify "PC ABS {color_name}" "{color_name}" PC PC+ABS --keep "PC ABS {color_name}" WHITE \
    --reclassify "Carbon Fiber {color_name}" "{color_name}" CF PAHT-CF --keep "Carbon Fiber {color_name}" PET \
    --ref https://github.com/Donkie/SpoolmanDB/pull/515 --source f320e26d16906cfaa10943c82714cab22600810b \
    --base-ref d54e3eb --apply
# commit, then:
python scripts/rename_migration.py --file AzureFilm.json \
    --reclassify "Carbon Fiber {color_name}" "{color_name}" CF PET-CF \
    --ref https://github.com/Donkie/SpoolmanDB/pull/515 --source f320e26d16906cfaa10943c82714cab22600810b \
    --base-ref d54e3eb --apply
```

Retired IDs disappear from the published catalog. Existing Spoolman spools keep their local imported data; Spoolman does not read the registry or follow these mappings.

## Not changed here

- `TPU 85A {color_name}` (TPU, 8 colours) and `TPU/TPE {color_name}` (TPU, 300 g, 10 colours) are not part of upstream #515. They stay as they are; they could be reviewed separately (the first looks like the same 1 kg 85A product as the reclassified group).
- After this migration the `CF` material code has no records in the catalog. Whether to keep it is open in #86.
