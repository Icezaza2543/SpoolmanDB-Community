# Extrudr PLA NX2 Matt verified colours — 2026-11-25

Starting commit: `e3d5c3fd397c2f8a1573d08b86fdc258084ed829` (Community `main` after #91). Upstream source: [Donkie/SpoolmanDB#505](https://github.com/Donkie/SpoolmanDB/pull/505), merge commit `db7eb60a04ecd67abd26e0c8989389fd7b7a7ffc`.

#505 adds 56 PLA NX2 Matt colours as a 1 kg / 1.75 mm group. It was held out of Icezaza2543/SpoolmanDB-Community#87 because, on [review](https://github.com/Icezaza2543/SpoolmanDB-Community/pull/87#issuecomment-7100717124), only 20 of the 56 had an exact 1 kg / 1.75 mm offer with SKU and GTIN in Extrudr's GB store. This adds the colours that do, with Extrudr's own colour data.

| Check | Result |
|---|---|
| Colours proposed upstream | 56 |
| With an exact 1.75 mm / 1 kg GB-store offer | 20 |
| Added | 19 (Metallic left out, see below) |
| New public IDs | 19, all identical to upstream's |
| Existing IDs removed, changed or rekeyed | 0 |
| Catalog size | 52,158 → 52,177 |

**Source:** the [GB store page](https://extrudr.com/en/gb/products/pla-nx2-matt/), fetched 2026-11-25. Its product data lists every variant with colour, size, SKU and GTIN-13 (the SKU is the GTIN), and each colour's RAL code and hex from Extrudr's colour data. A colour counts as verified when the store has a variant with that colour name and size `1.75 mm / 1 kg`. Stock status is recorded but not required. The other 36 colours have no variant of any size in this store; as Icezaza noted, that doesn't mean they are discontinued, so they stay out until a listing is found.

**Group values:** the same as the existing `NX2-MATT - {color_name}` group and the #87 port of #505: density 1.3, 1 kg plastic spool with 260 g tare, 230 °C nozzle, 60 °C bed, `country_of_origin` AT and the existing TDS link. Only the colours, hexes and the single 1.75 mm / 1 kg package differ. All colours are `finish: "matte"`.

## Colours

| Colour | GTIN (variant link) | RAL | Hex (Extrudr) | Stock | Note |
|---|---|---|---|---|---|
| Japanese White | [9010241602360](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NTEyMw%3D%3D) | 080 90 05 | `ECE6D9` | in stock |  |
| Light Corn | [9010241602353](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NTEyMg%3D%3D) | 070 90 10 | `EEE3D0` | in stock |  |
| Pebble Grey | [9010241601608](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NDk5Nw%3D%3D) | 7032 | `B1B1A1` | out of stock |  |
| Northern Light Grey | [9010241602056](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NTA5Mg%3D%3D) | 260 70 05 | `A6ABB3` | in stock |  |
| Tiger Yellow | [9010241602322](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NTExOQ%3D%3D) | 090 90 50 | `F5E485` | in stock |  |
| Autumn Yellow | [9010241602070](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NTA5NA%3D%3D) | 075 70 80 | `D6A209` | in stock |  |
| Indian Yellow | [9010241602339](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NTEyMA%3D%3D) | 060 70 70 | `E17C30` | in stock | Upstream `E79539` |
| Light Pink | [9010241602490](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NTE0Mw%3D%3D) | 3015 | `CC9EA4` | in stock |  |
| Vibrant Red | [9010241602278](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NTExNA%3D%3D) | 010 50 50 | `B54867` | in stock |  |
| Carmine Red | [9010241602469](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NTE0MA%3D%3D) | 3002 | `8D1F24` | out of stock |  |
| Active Green | [9010241602186](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NTEwNQ%3D%3D) | 170 60 50 | `47A185` | in stock |  |
| Dream Green | [9010241602179](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NTEwNA%3D%3D) | 170 50 30 | `4C816E` | in stock |  |
| Military Dark Green | [9010241041442](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NDA1NQ%3D%3D) | 6009 | `2A372C` | in stock |  |
| Pastel Blue | [9010241602506](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NTE0NA%3D%3D) | 5024 | `6C8DAA` | in stock |  |
| Kingfisher Blue | [9010241602414](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NTEyOA%3D%3D) | 250 40 35 | `0E457A` | in stock | Upstream `1F5B90` |
| Halite Blue | [9010241602407](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NTEyNw%3D%3D) | 260 20 20 | `1E314B` | in stock |  |
| Date Fruit Brown | [9010241601967](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NTA4Mw%3D%3D) | 060 50 50 | `A06932` | in stock |  |
| Chestnut Red | [9010241602001](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NTA4Nw%3D%3D) | 010 30 25 | `633640` | in stock |  |
| Neon Pink | [9010241602483](https://extrudr.com/en/gb/products/pla-nx2-matt/?variant=UHJvZHVjdFZhcmlhbnQ6NTE0Mg%3D%3D) | 1026 | `FF1493` | in stock | Upstream `FFFF00` |

Three hexes differ from upstream, which derived them from RAL numbers; Extrudr's colour data is used instead:

- **Neon Pink:** upstream `FFFF00` is yellow. Extrudr's RAL field says 1026 (luminous yellow), which is where upstream's value came from, but its hex is `#FF1493`, and the product image is pink.
- **Indian Yellow** (`E79539` → `E17C30`) and **Kingfisher Blue** (`1F5B90` → `0E457A`): Extrudr's hex for the same RAL Design code.

## Not included

- **Metallic** (GTIN 9010241043057, RAL 9023, `#4D4C50`): the existing group already has `Metallic Grey`, also RAL 9023, and the store has no `metallic grey` variant. It looks like the same product under its current store name, so adding it would likely duplicate an existing record. Left for a separate review.
- The 36 colours with no GB-store offer (listed in #505).
- Store colours not in #505 and not in Community (`camouflage grey`, `leather brown`) are out of scope.
