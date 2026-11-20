# Overture rename migration — 2026-11-19

Starting commit: `a91230b` (Icezaza2543/SpoolmanDB-Community main, after #75). Upstream source: [Donkie/SpoolmanDB#526](https://github.com/Donkie/SpoolmanDB/pull/526), merge commit `641226c7d47ad5834509812247d7b5249b294d62`.

This is an **intentional breaking catalog migration**. It applies the upstream Overture name cleanup: names no longer repeat the material (`"Matte PLA {color_name}"` becomes `"Matte {color_name}"` for PLA).

| Check | Result |
|---|---|
| Groups renamed | 55 (3 distinct template renames: `Matte PLA`, `Rock PLA`, `Silk PLA` → `Matte`, `Rock`, `Silk`) |
| Public IDs retired as renames | 90 |
| New public IDs | 90, each the registered target of exactly one retirement |
| Existing retirements re-pointed to the final ID | 5 (evidence and `retired_key` unchanged) |
| Colours kept on their current IDs | 3 (see below) |
| Catalog size | 51,434 (unchanged) |
| Unregistered removals, changed or rekeyed identities | 0 |
| Material, weight, diameter, spool, colour and metadata changes | None |

## How it was produced

1. The helper generated the full upstream rename from `a91230b`:

   ```sh
   python scripts/rename_migration.py --file overture.json \
       --upstream 641226c7d47ad5834509812247d7b5249b294d62~1 641226c7d47ad5834509812247d7b5249b294d62 \
       --ref https://github.com/Donkie/SpoolmanDB/pull/526 --source 641226c7d47ad5834509812247d7b5249b294d62 \
       --base-ref a91230b --apply
   ```

2. Per review, three colours were then returned to their current IDs (below). The helper renames whole groups, so this was done by hand:
   - The `Rock White` and `Rock Rainbow` groups (one colour each) keep the name `Rock PLA {color_name}`.
   - `Silk Purple` moves out of the renamed Silk group into its own `Silk PLA {color_name}` group, with identical properties. Its compiled record and identity key are unchanged.
   - Their three `rename` entries are removed, and the two re-points they caused are restored to their `main` values.
   - The baseline is regenerated with `compile_id_baseline.py --update --base-ref a91230b`.

3. The result passes the same checks as a helper-only migration:

   ```sh
   python scripts/rename_migration.py --verify --base-ref a91230b
   python scripts/compile_id_baseline.py --base-ref a91230b --strict
   python scripts/validate.py --base-ref a91230b --strict
   ```

Retired IDs disappear from the published catalog. Existing Spoolman spools keep their local imported data; Spoolman does not read the registry or follow these mappings.

## Not included

- **`High Speed 95A {color_name}` (TPU → TPU-95A, `High Speed {color_name}`):** a material change, not a rename. It is left for the material reclassification work.
- **Colour-name cleanups, kept on their current IDs:** upstream also shortened three colour names. A rename keeps colours unchanged, so including them would publish intermediate IDs that would have to be retired again. They stay as they are:
  - `overture_pla_rockplarockwhite_1000_175_c` (`Rock White`; upstream `White`)
  - `overture_pla_rockplarockrainbow_1000_175_c` (`Rock Rainbow`; upstream `Rainbow`)
  - `overture_pla_silkplasilkpurple_1000_175_c` (`Silk Purple`; upstream `Purple`). Community also has a Silk `Purple` with the same hex (`7769BC`). This pair needs its own duplicate review.

## Community exception: Light Gray

Upstream's Matte group spells this colour `Light Grey`. Community keeps `Light Gray`, the spelling chosen in the [2026-10-03 Overture duplicate review](2026-10-03-overture-duplicate-review.md), which retired `overture_pla_matteplalightgrey_1000_175_c` into `overture_pla_matteplalightgray_1000_175_c`. This migration renames that record to `overture_pla_mattelightgray_1000_175_c` and re-points the old `lightgrey` retirement to it. The colour name is not changed to match upstream.

## Re-pointed retirements

These earlier `duplicate` retirements pointed at IDs this migration renames. Only `replaced_by` changes, so the registry never forms a chain.

| Retired ID | Previous target | New target |
|---|---|---|
| `overture_pla_matteplalightgrey_1000_175_c` | `overture_pla_matteplalightgray_1000_175_c` | `overture_pla_mattelightgray_1000_175_c` |
| `overture_pla_plarockfossilrock_1000_175_c` | `overture_pla_rockplafossilrock_1000_175_c` | `overture_pla_rockfossilrock_1000_175_c` |
| `overture_pla_plarockglacierblue_1000_175_c` | `overture_pla_rockplaglacierblue_1000_175_c` | `overture_pla_rockglacierblue_1000_175_c` |
| `overture_pla_plarockmarsred_1000_175_c` | `overture_pla_rockplamarsred_1000_175_c` | `overture_pla_rockmarsred_1000_175_c` |
| `overture_pla_plarocksedimentaryrock_1000_175_c` | `overture_pla_rockplasedimentaryrock_1000_175_c` | `overture_pla_rocksedimentaryrock_1000_175_c` |

## Mapping

| Old public ID | New public ID |
|---|---|
| `overture_pla_mattepla6-color_1000_175_c` | `overture_pla_matte6-color_1000_175_c` |
| `overture_pla_matteplaarmygreen_1000_175_c` | `overture_pla_mattearmygreen_1000_175_c` |
| `overture_pla_matteplababypink_1000_175_c` | `overture_pla_mattebabypink_1000_175_c` |
| `overture_pla_matteplabamboogreen_1000_175_c` | `overture_pla_mattebamboogreen_1000_175_c` |
| `overture_pla_matteplabeige_1000_175_c` | `overture_pla_mattebeige_1000_175_c` |
| `overture_pla_matteplablack&white_1000_175_c` | `overture_pla_matteblack&white_1000_175_c` |
| `overture_pla_matteplablack-white_1000_175_c` | `overture_pla_matteblack-white_1000_175_c` |
| `overture_pla_matteplablack_1000_175_c` | `overture_pla_matteblack_1000_175_c` |
| `overture_pla_matteplablue-red_1000_175_c` | `overture_pla_matteblue-red_1000_175_c` |
| `overture_pla_matteplablue_1000_175_c` | `overture_pla_matteblue_1000_175_c` |
| `overture_pla_matteplabrickred_1000_175_c` | `overture_pla_mattebrickred_1000_175_c` |
| `overture_pla_matteplabutteryellow_1000_175_c` | `overture_pla_mattebutteryellow_1000_175_c` |
| `overture_pla_matteplacandyrainbow_1000_175_c` | `overture_pla_mattecandyrainbow_1000_175_c` |
| `overture_pla_matteplacarbonfiberblack_1000_175_c` | `overture_pla_mattecarbonfiberblack_1000_175_c` |
| `overture_pla_matteplachocolate_1000_175_c` | `overture_pla_mattechocolate_1000_175_c` |
| `overture_pla_mattepladarkorange_1000_175_c` | `overture_pla_mattedarkorange_1000_175_c` |
| `overture_pla_matteplaecomidnightblack_1000_175_c` | `overture_pla_matteecomidnightblack_1000_175_c` |
| `overture_pla_matteplagrassgreen_1000_175_c` | `overture_pla_mattegrassgreen_1000_175_c` |
| `overture_pla_matteplagraygreen_1000_175_c` | `overture_pla_mattegraygreen_1000_175_c` |
| `overture_pla_matteplagreen_1000_175_c` | `overture_pla_mattegreen_1000_175_c` |
| `overture_pla_matteplajeansblue_1000_175_c` | `overture_pla_mattejeansblue_1000_175_c` |
| `overture_pla_matteplajeansred_1000_175_c` | `overture_pla_mattejeansred_1000_175_c` |
| `overture_pla_matteplalavender_1000_175_c` | `overture_pla_mattelavender_1000_175_c` |
| `overture_pla_matteplalightblue-yellow_1000_175_c` | `overture_pla_mattelightblue-yellow_1000_175_c` |
| `overture_pla_matteplalightblue_1000_175_c` | `overture_pla_mattelightblue_1000_175_c` |
| `overture_pla_matteplalightbrown_1000_175_c` | `overture_pla_mattelightbrown_1000_175_c` |
| `overture_pla_matteplalightgray_1000_175_c` | `overture_pla_mattelightgray_1000_175_c` |
| `overture_pla_matteplalightgreen_1000_175_c` | `overture_pla_mattelightgreen_1000_175_c` |
| `overture_pla_matteplalightorange_1000_175_c` | `overture_pla_mattelightorange_1000_175_c` |
| `overture_pla_matteplalightpink_1000_175_c` | `overture_pla_mattelightpink_1000_175_c` |
| `overture_pla_matteplalightteal_1000_175_c` | `overture_pla_mattelightteal_1000_175_c` |
| `overture_pla_matteplalilac_1000_175_c` | `overture_pla_mattelilac_1000_175_c` |
| `overture_pla_matteplanavyblue_1000_175_c` | `overture_pla_mattenavyblue_1000_175_c` |
| `overture_pla_matteplaolivegreen_1000_175_c` | `overture_pla_matteolivegreen_1000_175_c` |
| `overture_pla_matteplaorange-red_1000_175_c` | `overture_pla_matteorange-red_1000_175_c` |
| `overture_pla_matteplaorange_1000_175_c` | `overture_pla_matteorange_1000_175_c` |
| `overture_pla_matteplapalegreen_1000_175_c` | `overture_pla_mattepalegreen_1000_175_c` |
| `overture_pla_matteplapastelred_1000_175_c` | `overture_pla_mattepastelred_1000_175_c` |
| `overture_pla_matteplapink_1000_175_c` | `overture_pla_mattepink_1000_175_c` |
| `overture_pla_matteplapurple_1000_175_c` | `overture_pla_mattepurple_1000_175_c` |
| `overture_pla_matteplarainbow_1000_175_c` | `overture_pla_matterainbow_1000_175_c` |
| `overture_pla_matteplarainbowa1_1000_175_c` | `overture_pla_matterainbowa1_1000_175_c` |
| `overture_pla_matteplared_1000_175_c` | `overture_pla_mattered_1000_175_c` |
| `overture_pla_matteplareposegray_1000_175_c` | `overture_pla_mattereposegray_1000_175_c` |
| `overture_pla_matteplaskin_1000_175_c` | `overture_pla_matteskin_1000_175_c` |
| `overture_pla_matteplaslategray_1000_175_c` | `overture_pla_matteslategray_1000_175_c` |
| `overture_pla_matteplaturquoise_1000_175_c` | `overture_pla_matteturquoise_1000_175_c` |
| `overture_pla_matteplawhite_1000_175_c` | `overture_pla_mattewhite_1000_175_c` |
| `overture_pla_matteplawood_1000_175_c` | `overture_pla_mattewood_1000_175_c` |
| `overture_pla_matteplayellow_1000_175_c` | `overture_pla_matteyellow_1000_175_c` |
| `overture_pla_rockplafossilrock_1000_175_c` | `overture_pla_rockfossilrock_1000_175_c` |
| `overture_pla_rockplaglacierblue_1000_175_c` | `overture_pla_rockglacierblue_1000_175_c` |
| `overture_pla_rockplamarsred_1000_175_c` | `overture_pla_rockmarsred_1000_175_c` |
| `overture_pla_rockplasedimentaryrock_1000_175_c` | `overture_pla_rocksedimentaryrock_1000_175_c` |
| `overture_pla_silkplablue_1000_175_c` | `overture_pla_silkblue_1000_175_c` |
| `overture_pla_silkplacaramel_1000_175_c` | `overture_pla_silkcaramel_1000_175_c` |
| `overture_pla_silkplachristmasred_1000_175_c` | `overture_pla_silkchristmasred_1000_175_c` |
| `overture_pla_silkplachromegray_1000_175_c` | `overture_pla_silkchromegray_1000_175_c` |
| `overture_pla_silkplacopper_1000_175_c` | `overture_pla_silkcopper_1000_175_c` |
| `overture_pla_silkplacoppershore_1000_175_c` | `overture_pla_silkcoppershore_1000_175_c` |
| `overture_pla_silkpladualcolorsblue-silver_1000_175_c` | `overture_pla_silkdualcolorsblue-silver_1000_175_c` |
| `overture_pla_silkpladualcolorsblue-yellow_1000_175_c` | `overture_pla_silkdualcolorsblue-yellow_1000_175_c` |
| `overture_pla_silkpladualcolorsgold-silver_1000_175_c` | `overture_pla_silkdualcolorsgold-silver_1000_175_c` |
| `overture_pla_silkpladualcolorsgreen-blue_1000_175_c` | `overture_pla_silkdualcolorsgreen-blue_1000_175_c` |
| `overture_pla_silkpladualcolorsgreen-magenta_1000_175_c` | `overture_pla_silkdualcolorsgreen-magenta_1000_175_c` |
| `overture_pla_silkpladualcolorsgreen-silver_1000_175_c` | `overture_pla_silkdualcolorsgreen-silver_1000_175_c` |
| `overture_pla_silkpladualcolorsmagenta-gold_1000_175_c` | `overture_pla_silkdualcolorsmagenta-gold_1000_175_c` |
| `overture_pla_silkpladualcolorspurple-gold_1000_175_c` | `overture_pla_silkdualcolorspurple-gold_1000_175_c` |
| `overture_pla_silkpladualcolorsred-gold_1000_175_c` | `overture_pla_silkdualcolorsred-gold_1000_175_c` |
| `overture_pla_silkplaevergreenbronze_1000_175_c` | `overture_pla_silkevergreenbronze_1000_175_c` |
| `overture_pla_silkplafreshred_1000_175_c` | `overture_pla_silkfreshred_1000_175_c` |
| `overture_pla_silkplaglacierflash_1000_175_c` | `overture_pla_silkglacierflash_1000_175_c` |
| `overture_pla_silkplagold_1000_175_c` | `overture_pla_silkgold_1000_175_c` |
| `overture_pla_silkplagoldenember_1000_175_c` | `overture_pla_silkgoldenember_1000_175_c` |
| `overture_pla_silkplagray_1000_175_c` | `overture_pla_silkgray_1000_175_c` |
| `overture_pla_silkplagreen_1000_175_c` | `overture_pla_silkgreen_1000_175_c` |
| `overture_pla_silkplalettucetomato_1000_175_c` | `overture_pla_silklettucetomato_1000_175_c` |
| `overture_pla_silkplalimesurge_1000_175_c` | `overture_pla_silklimesurge_1000_175_c` |
| `overture_pla_silkplaneongreen_1000_175_c` | `overture_pla_silkneongreen_1000_175_c` |
| `overture_pla_silkplaparakeet_1000_175_c` | `overture_pla_silkparakeet_1000_175_c` |
| `overture_pla_silkplaperiwinkle_1000_175_c` | `overture_pla_silkperiwinkle_1000_175_c` |
| `overture_pla_silkplapunchpink_1000_175_c` | `overture_pla_silkpunchpink_1000_175_c` |
| `overture_pla_silkplapurple_1000_175_c` | `overture_pla_silkpurple_1000_175_c` |
| `overture_pla_silkplapurplechrome_1000_175_c` | `overture_pla_silkpurplechrome_1000_175_c` |
| `overture_pla_silkplared_1000_175_c` | `overture_pla_silkred_1000_175_c` |
| `overture_pla_silkplasilver_1000_175_c` | `overture_pla_silksilver_1000_175_c` |
| `overture_pla_silkplatigereye_1000_175_c` | `overture_pla_silktigereye_1000_175_c` |
| `overture_pla_silkplatropic_1000_175_c` | `overture_pla_silktropic_1000_175_c` |
| `overture_pla_silkplavaporwave_1000_175_c` | `overture_pla_silkvaporwave_1000_175_c` |
| `overture_pla_silkplawhite_1000_175_c` | `overture_pla_silkwhite_1000_175_c` |
