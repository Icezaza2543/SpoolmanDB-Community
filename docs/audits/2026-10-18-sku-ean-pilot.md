# SKU/EAN binding inventory and 3D4Makers ABS pilot

Date: 2026-10-18. Starting main: `df9fcf53eb4b02ee58d47a0b88a6d3a4e8ab41a2`.

## Scope and interpretation

Expanded all 490 manufacturer source files using the current compiler (`scripts.duplicate_catalog.catalog_records`): 51,412 records; 74 manufacturers carry at least one identifier. Indexed exact string values separately for `codes`, `eans`, and `eans_refill`, retaining each value's compiled ID memberships. Also indexed codes within each manufacturer: short SKU strings are not globally unique.

This is a catalog-wide **structural inventory**, not a claim that every shared identifier has been checked against product evidence. A value on multiple IDs is an audit candidate, not automatically an error. Historical packaging aliases and the legacy meaning of `eans_refill` need individual review. No global uniqueness gate or new binding format is introduced.

| Field | Unique raw values before / after | Compiled bindings before / after | Values on multiple IDs before / after |
| --- | ---: | ---: | ---: |
| codes | 8,031 / 8,031 | 24,149 / 24,137 | 3,119 / 3,107 |
| eans | 2,129 / 2,141 | 5,883 / 5,895 | 1,086 / 1,086 |
| eans_refill | 65 / 65 | 90 / 90 | 5 / 5 |

Largest per-manufacturer review queues at the starting commit (shared values, not confirmed errors):

| Manufacturer | Multi-ID codes | Multi-ID eans | Multi-ID eans_refill |
| --- | ---: | ---: | ---: |
| Polymaker | 407 | 407 | 0 |
| Sunlu | 807 | 0 | 0 |
| 3DE | 316 | 17 | 5 |
| Fiberlogy | 152 | 152 | 0 |
| Print With Smile | 102 | 101 | 0 |
| 3D4Makers | 185 | 0 | 0 |
| Spectrum | 86 | 86 | 0 |
| 3DTrcek | 0 | 145 | 0 |
| Eolas Prints | 70 | 72 | 0 |
| 3D Printing Canada | 84 | 34 | 0 |
| Winkle | 118 | 0 | 0 |
| Protopasta | 105 | 0 | 0 |
| eSun | 88 | 12 | 0 |
| Filatech | 97 | 0 | 0 |
| Formfutura | 41 | 41 | 0 |

Full before/after inventories, compiled manifests and the exact compiled delta were retained as local audit artifacts. The figures above can be reproduced by grouping the compiler's output by each identifier field and counting distinct public ID memberships; no source-array-position interpretation is used.

## Pilot choice and first-party evidence

Selected **3D4Makers ABS Filament only**: six colors, 750 g and 2,300 g, 1.75 mm, twelve existing plastic-spool records. The old single definition attached both weight-specific SKUs to each color, so each SKU appeared on both weights. Other 3D4Makers families are not repaired in this pilot.

The live [manufacturer ABS page](https://www.3d4makers.com/products/abs-filament) was checked in Chrome. Its embedded `application/ld+json` `ProductGroup.hasVariant` explicitly pairs the full color / diameter / weight name with `sku`, `gtin`, and a variant-specific product URL. The [focused evidence capture](2026-10-18-3d4makers-abs-identifier-evidence.json) retains those twelve variant tuples. These are manufacturer SKUs and GTINs, not Shopify numeric variant IDs used as identifiers. Numeric variant IDs below are source locators only. The binding is read from each complete variant object, not inferred from SKU spelling or selector Cartesian products.

The current page rebrands 3D4Makers to 3D4M. The database manufacturer and all historical names remain unchanged. The page also lists 2.85 mm variants; none are added or receive these 1.75 mm identifiers.

## Exact target bindings

All source changes preserve the existing color/HEX and original weight objects. Split the ABS definition by weight; keep one matching SKU and add its manufacturer GTIN to each color. Every listed identifier must resolve to the exact target ID only (SKU checked within manufacturer; GTIN checked globally across both EAN fields).

| Exact existing public ID | Manufacturer SKU | GTIN | Exact source |
| --- | --- | --- | --- |
| `3d4makers_abs_absfilamentblue(ral5002)_750_175_p` | `ABSXX-5002-175-750-3D4M` | `8721632470086` | [3497129540](https://www.3d4makers.com/products/abs-filament?variant=3497129540) |
| `3d4makers_abs_absfilamentblue(ral5002)_2300_175_p` | `ABSXX-5002-175-2300-3D4M` | `8721632470093` | [40215259152431](https://www.3d4makers.com/products/abs-filament?variant=40215259152431) |
| `3d4makers_abs_absfilamentgreen(ral6029)_750_175_p` | `ABSXX-6029-175-750-3D4M` | `8721632470123` | [3497129604](https://www.3d4makers.com/products/abs-filament?variant=3497129604) |
| `3d4makers_abs_absfilamentgreen(ral6029)_2300_175_p` | `ABSXX-6029-175-2300-3D4M` | `8721632470130` | [40215259250735](https://www.3d4makers.com/products/abs-filament?variant=40215259250735) |
| `3d4makers_abs_absfilamentblack(ral9011)_750_175_p` | `ABSXX-9011-175-750-3D4M` | `8721632470161` | [2697752516](https://www.3d4makers.com/products/abs-filament?variant=2697752516) |
| `3d4makers_abs_absfilamentblack(ral9011)_2300_175_p` | `ABSXX-9011-175-2300-3D4M` | `8721632470178` | [40218889125935](https://www.3d4makers.com/products/abs-filament?variant=40218889125935) |
| `3d4makers_abs_absfilamentwhite(ral9016)_750_175_p` | `ABSXX-9016-175-750-3D4M` | `8721632470208` | [3497129412](https://www.3d4makers.com/products/abs-filament?variant=3497129412) |
| `3d4makers_abs_absfilamentwhite(ral9016)_2300_175_p` | `ABSXX-9016-175-2300-3D4M` | `8721632470215` | [40218889224239](https://www.3d4makers.com/products/abs-filament?variant=40218889224239) |
| `3d4makers_abs_absfilamentred(ral3020)_750_175_p` | `ABSXX-3020-175-750-3D4M` | `8721632470246` | [3497129476](https://www.3d4makers.com/products/abs-filament?variant=3497129476) |
| `3d4makers_abs_absfilamentred(ral3020)_2300_175_p` | `ABSXX-3020-175-2300-3D4M` | `8721632470253` | [40218889289775](https://www.3d4makers.com/products/abs-filament?variant=40218889289775) |
| `3d4makers_abs_absfilamentnatural_750_175_p` | `ABSXX-0000-175-750-3D4M` | `8721632470284` | [3549458820](https://www.3d4makers.com/products/abs-filament?variant=3549458820) |
| `3d4makers_abs_absfilamentnatural_2300_175_p` | `ABSXX-0000-175-2300-3D4M` | `8721632470291` | [40218889355311](https://www.3d4makers.com/products/abs-filament?variant=40218889355311) |

## Verified delta and regression

- Records: 51,412 -> 51,412; new / removed / changed identity / rekeyed: 0 / 0 / 0 / 0.
- Exactly the twelve IDs above change, only `codes` and `eans`. No other compiled field or record changes.
- Twelve incorrect cross-weight SKU bindings removed; all twelve unique existing SKUs preserved on their matching targets.
- Twelve checksum-valid, globally unique manufacturer GTINs added, one per target. No refill EAN changes.
- 3D4Makers multi-ID SKU values: 185 -> 173; other families remain evidence-review backlog.
- Every canonical baseline key unchanged; baseline and retired registry unchanged (2,022 retirements).
- Complete Spoolman-native projections before/after are equal when compared by public ID.
- The twelve literal regression cases were run before the data edit: twelve failures on cross-weight SKU inheritance. After the edit: twelve passed. They compile real source data and check exact identifier memberships, including other colors, weights, diameters, packages and globally conflicting GTINs.

## Deliberate omissions and remaining evidence work

- This does not certify all other shared identifiers, remove unknown identifiers, introduce a global SKU uniqueness constraint, or change `eans_refill` semantics.
- Remaining 3D4Makers multi-weight SKU families include ASA, PLA, PETG, Facilan, Luvocom and engineering polymers. They require exact variant-object/label review before corrections; SKU text alone is not evidence.
- The current ABS page reports density 1.05, nozzle 220-260 C and tare 213 g / 666 g, differing from parts of the existing definition. Those are recorded here for a separate metadata/lot review; this identifier-only pilot keeps density, temperatures, packaging and tare untouched.
- No 2.85 mm additions, product/manufacturer renames, retirement migrations, schema/compiler/workflow changes, or upstream activity.
- A separate identifier registry is not necessary for this pilot; retain current published array fields for existing barcode integrations.

## Validation

Full maintenance section 7 suite passed on the pilot state:

- `readme_snapshot.py --write` and `--check`: passed. Source definitions 12,307 -> 12,308 and color entries 34,839 -> 34,845 reflect the weight split, not new products; source EAN entries 2,725 -> 2,737. Compiled count remains 51,412.
- `compile_filaments.py`: passed; generated catalog not committed.
- `audit_duplicates.py --all`: zero unresolved/owner-pending groups; existing OV083 non-duplicate exemption retained.
- `validate.py --strict --base-ref df9fcf53eb4b02ee58d47a0b88a6d3a4e8ab41a2`: passed; pre-existing informational display-name warnings remain.
- `python -B -m pytest -q -p no:cacheprovider`: 277 passed. The unchanged starting tree passed 265 tests before the pilot; sandbox temp/Git restrictions required a normal-permissions rerun. Cache provider disabled for final validation because the existing cache directory was not writable.
- `node tests/test_display_name.cjs`: passed, including schema viewer checks.
- Stable compatibility: all 51,412 records accepted, pinned v0.25.0, 18 native fields.
- Canary compatibility: all 51,412 accepted; no ExternalFilament field/type drift against the stable pin.
- `project_spoolman.py`: passed; 51,412 records projected.
- `compile_id_baseline.py --strict --base-ref df9fcf53eb4b02ee58d47a0b88a6d3a4e8ab41a2`: matched 51,412; added/removed/changed/rekeyed/reinstated all zero; registered retired 2,022.
- `git diff --check`: passed. No changes under contracts, scripts or workflows.
- Independent read-only review approved the source/evidence/test diff and separately recompiled both complete catalogs: no Critical/Important/Minor findings; same IDs/keys, exact twelve-record identifier-only delta and identical native projections.

Hosted CI and published-artifact checks occur after the single authorized main push and are reported in the delivery response; this committed audit does not pre-claim those outcomes.
