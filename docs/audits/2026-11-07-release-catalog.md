# Spoolman v0.27.1 and selective upstream catalog audit

Starting Community main: `b0d30eefdc5dae32f7aa1d687b4f3e4e6d4fd902`.
Scope: release compatibility, then the changes proposed in upstream #502/#501/#500.
No upstream writes, namespace consolidation or historical identity changes.

## Release contract

Release: https://github.com/Donkie/Spoolman/releases/tag/v0.27.1
Resolved tag commit: `ff8efd517b76a4b2783f29c89e9b9fbcd8cd167b`.
Contract: https://raw.githubusercontent.com/Donkie/Spoolman/ff8efd517b76a4b2783f29c89e9b9fbcd8cd167b/spoolman/externaldb.py

All 51,433 starting records pass the exact release contract. AST comparison with
the reviewed v0.25.0 snapshot reports zero field/type/enum changes (18 native
fields). Advance the stable pin; retain the semantically identical local contract
snapshot. The snapshot is intentionally an AST-only model extract, not a full
byte-for-byte copy of the upstream server module. Verify-pin checks its contract.
No upstream code is executed. This is not a live Spoolman server/UI import test.

## Das Filament — partial safe addition

Upstream: https://github.com/Donkie/SpoolmanDB/pull/502
Community already has 1 kg PLA/PETG definitions and 1 kg TPU V2 Natur/Schwarz/Wei.
Do not replay the upstream 800-to-1000 weight edits or add generic TPU duplicates.

The current exact white SKU is **800 g on a plastic spool**, not 1 kg:
https://dasfilament.de/produkt/tpu-v2-filament-flexibel-175-mm-weiss-800-g/

Add one separate definition: TPU V2 Flexibel Weiß, 1.75 mm, 800 g, plastic,
density 1.23 (1230 kg/m³), nozzle 205–235 °C (220 ±15), SKU F10445 and
manufacturer part number F10445DAS. Retain TPU material naming consistent with
the existing line; the page specifies hardness 94A. White FFFFFF is a conservative
representative swatch reused from the existing white record, not a claimed
manufacturer HEX or exact conversion of its RAL 9003. No numeric bed temperature
is invented from "heated bed not required". No tare is inferred from gross weight.
Country DE is established by https://dasfilament.de/ (all filament made in Germany).

Cross-checks:
- https://dasfilament.de/produkt/tpu-v2-filament-flexibel-175-mm-schwarz-1-kg/
- https://dasfilament.de/produkt/tpu-v2-filament-flexibel-175-mm-natur-1-kg/
- https://dasfilament.de/produkt-kategorie/tpu/tpu-175-mm/tpu-175-mm-spule/

Existing TPU metadata conflicts (density 1.21 vs current 1.23, temperature ranges,
and the existing 1 kg white packaging/availability) are recorded, not silently
corrected in this additions-only task. Existing refill semantics/tare also stay
untouched; no new combination is inferred from a category menu.

## Fusion — BLOCK_EVIDENCE

Upstream: https://github.com/Donkie/SpoolmanDB/pull/501
Targets: Atomic Orange, Cold Fusion Blue, Reactor Red PCTG, 1 kg.
Checked both existing namespaces: Fusion (158 records) and Fusion Filaments
(41 records, including PCTG Geomagnetic Mauve/Heavy Water Blue/Natural).
The three requested PCTG colors are not covered by these existing PCTG entries.

Official catalog confirms the product names and 1 kg:
https://www.fusionfilaments.com/shop/category/pctg-24
Exact blue page: https://www.fusionfilaments.com/shop/850076511586-1kg-pctg-filament-cold-fusion-blue-10163

Direct retrieval of product/category pages returned HTTP 403, while indexed
first-party catalog text was available. Required density and exact package/spec
binding were not verified. Upstream's 1.24 density, 200 g tare, HEX and printing
values come from third-party profiles, not sufficient independent manufacturer
proof here. An indexed manufacturer PDF at `/web/content/14867` gives 1.08 density
but is not bound to this PCTG line: rejected, not reused. No import or namespace
change. Reopen with the exact PCTG TDS/product specification and package evidence.

## Deeplee — BLOCK_EVIDENCE

Upstream: https://github.com/Donkie/SpoolmanDB/pull/500
Target: PLA+ High Speed 2.0 Hot Pink, 1.75 mm, 1 kg.
Official site checked: https://deeplee3d.com/
It describes Rapid PLA Plus on cardboard, but does not bind the exact Hot Pink
2.0 SKU or verify its density. The PR's plastic/113 g tare and HEX come from a
third-party profile/contributor; cannot substitute the site's other cardboard
product for this variant. No addition, rename or existing-record modification.
Reopen with the exact manufacturer product/label and density evidence.

## Expected safety result

51,433 -> 51,434 records; one new identity, no retirements. New ID:
`dasfilament_tpu_tpuv2flexibelwei_800_175_p` (compiler ASCII normalization).
All historical compiled records, baseline keys and IDs remain unchanged.
No code transfers; both new manufacturer identifiers bind only to the 800 g SKU.
