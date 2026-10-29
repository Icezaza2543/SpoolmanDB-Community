# Manufacturer coverage: Silver3D, CC3D and Alchemakes

Checked 2026-10-30. Upstream pin: `c67dcd85dd4ff8de9bbc4f1eaa617aa837e95b1a`. Community starting pin: `2a2c6370292b30732ddc80921fa67d65f4e7abf4`. None of these manufacturers was added, renamed or changed in this cycle.

The audit searched manufacturer values, serialized source contents and the brand alias registry, not just filenames. Case-insensitive patterns included `silver.?3d`, `cc.?3d` and `alchema`. Expanded records were compared by public ID and fields using the compiler; spelling similarity was not treated as identity evidence.

## Coverage and decisions

| Identity | Upstream | Community | Families in Community | Missing evidence / next action |
| --- | --- | --- | --- | --- |
| Silver3D; official site identifies Guangdong Silver AM Technology | Absent | Absent | None imported | Obtain exact filament catalog/TDS files, package/color identifiers and measured empty-spool tare before adding a focused manufacturer file |
| CC3D | 3 source groups / 10 variants | 14 groups / 87 variants | ABS, HIPS, PC, PETG, PLA, TPE, TPU | All 10 upstream IDs already represented; retain 77 additional variants, gather primary sources and package-specific tare |
| Alchemakes | Absent | 16 groups / 122 variants | ABS, ABS-CF, ABS-GF, ASA, ASA-CF, ASA-GF, PA6-CF, PETG, PETG-CF, PLA, PLA-CF, PP-GF | Retain existing data; obtain official product/identity evidence and measured tare for all groups |
| Alchemaker | Absent | Absent | None | Relationship to Alchemakes unresolved; no alias or manufacturer rename authorized by evidence |

## Silver3D

The [official site](https://silver3d.com/) and [About page](https://silver3d.com/gywm) provide an identity lead. The indexed [official TDS library](https://silver3d.com/sjzx_tds) lists filament documents for PLA, PLA-CF, PETG-CF, PC, Nylon-GF, TPU 98A, PVA, PPS-TF and PMMA, as well as powder grades. The [product catalog](https://silver3d.com/ProductInfoCategory?categoryId=199610) is a further manufacturer source to inspect.

Direct retrieval of the TDS index timed out during this audit; search-index content exposed document titles, but the PDF contents and package-specific measurements were not verified. Powder datasheets must not be mistaken for FDM filament. These links establish research leads, not imported density, HEX, material formulation or spool weight. No traceable empty-spool tare was obtained, so **defer all additions**. Ask for a real package/lot and a scale measurement, then bind every imported value to its source.

## CC3D

The three upstream groups are ABS+, PETG and PLA. Their 10 expanded records are already present with matching IDs and core values; Community additionally carries `country_of_origin: CN`. Upstream omission is not a reason to erase that historical metadata. The audit did not independently re-certify its provenance.

Only these three Community groups (10 variants) contain the inherited **180 g** tare. The remaining 11 groups (77 variants) omit tare. Neither database field presence nor repetition of 180 g proves a fresh measurement for another package. No Community group has a TDS/SDS URL. The additional families therefore remain coverage with evidence gaps, not newly verified products.

[CC3D Global products](https://cc3dglobal.com/products/) is a primary-source lead but returned an access error during research. [cc3dfilament.com](https://cc3dfilament.com/) makes manufacturer claims; ownership and its relationship to the existing catalog were not independently established. Contradictory reseller identity claims are insufficient to change COO. Obtain manufacturer documents and packaging evidence before any corrective update. Importing the upstream file again would duplicate existing products; broader name/package matches still require individual review.

## Alchemaker versus Alchemakes

All 16 Alchemakes groups lack spool tare and TDS/SDS URLs. Third-party listings such as [Peek Machinery's Alchemakes ASA-CF](https://peekmachinery.co.nz/products/3d-printer-filament-asa-cf-1-75mm-1kg) corroborate that spelling in commerce, but do not validate every catalog value or tare. No new properties were inferred from those listings.

[Materialise's South Korea distributor page](https://www.materialise.com/ko/healthcare/hcps/pressure-measurements-orthotics/distributors/south-korea) lists **Alchemaker** in an orthotics context. That is not evidence that it is the filament brand Alchemakes. No primary evidence links the two names. Keep the requested spelling unresolved until the requester supplies a product label/site or a manufacturer confirms the relationship; do not create an alias based on edit distance.

## Reproduce internal checks

Use `scripts.reconcile_upstream.read_sources(ref)` and `scripts.compile_filaments.get_filaments_from_data(source)` to inspect the pinned source objects and expand variants. Compare upstream CC3D records to Community by `id`, retaining null/omitted upstream fields as missing evidence, not deletion instructions. Inspect each group's `weights[].spool_weight`, `tds_url` and `sds_url` explicitly. The [reconciliation command and field-level ledger](2026-10-30-reconciliation.md) reproduce the broader comparison.

No alias, material migration or upstream PR was created. Next contributions should be one manufacturer at a time, with measured tare, exact package binding and the historical-ID gate.
