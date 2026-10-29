# SpoolmanDB Community

**Find filament. Understand its data. Bring it into Spoolman.**

[![Build](https://github.com/Icezaza2543/SpoolmanDB-Community/actions/workflows/build.yml/badge.svg)](https://github.com/Icezaza2543/SpoolmanDB-Community/actions/workflows/build.yml)
[![MIT license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-2ea44f.svg)](CONTRIBUTING.md)

An independent, community-maintained filament catalog that complements [Donkie/SpoolmanDB](https://github.com/Donkie/SpoolmanDB). Browse colors and materials, inspect technical documents, and use the published database with [Spoolman](https://github.com/Donkie/Spoolman).

[**Open the Explorer →**](https://icezaza2543.github.io/SpoolmanDB-Community/#explorer) · [Contribute data](CONTRIBUTING.md) · [Compatibility](docs/UPSTREAM_COMPATIBILITY.md) · [Data policy](POLICY.md)

## Use with Spoolman

1. Browse the [catalog](https://icezaza2543.github.io/SpoolmanDB-Community/#explorer) and check the product and packaging you need.
2. Set this environment variable in your Spoolman server configuration (for Docker Compose, under your existing service's `environment`):

   ```yaml
   EXTERNAL_DB_URL: https://icezaza2543.github.io/SpoolmanDB-Community/
   ```

3. Restart/recreate your Spoolman service with that configuration, then use its external filament picker. The URL is the **directory**, including the trailing slash; Spoolman requests the JSON files beneath it.

The Explorer's copy button only copies the URL. It cannot configure or access your Spoolman server. See [Spoolman's configuration example](https://github.com/Donkie/Spoolman/blob/master/.env.example) for sync settings.

## Explore the catalog

- Search by manufacturer, material, color, product code or EAN.
- Compare diameter, net weight and packaging; missing values remain visible.
- Follow available TDS/SDS references and inspect the source schemas.
- Use Analytics for catalog coverage and Contributor Tools to find the right source file.

Data completeness describes which fields are present. It does **not** certify a product, measurement or printing profile.

## Data you can review

We prefer manufacturer product pages, technical documents and recorded measurements. Unknown density, colors, identifiers and spool tare must not be invented. A catalog entry is reference data; check the exact package and manufacturer's current guidance.

Historical public IDs are protected by a baseline gate. Community extensions include document links, product identifiers and refill metadata. Some fields are supported by upstream SpoolmanDB but are not consumed by the Spoolman application. [Read the field compatibility matrix](docs/UPSTREAM_COMPATIBILITY.md).

The 2026-10-30 reconciliation adds 20 Sunlu PETG 2.0 variants and support for per-color transmission distance. Conflicting or insufficiently evidenced imports remain in the [reconciliation report](docs/audits/2026-10-30-reconciliation.md). Material reclassification in upstream Issue #309 remains **HOLD**.

## Current snapshot

* **Published records**: 51,432

<!-- readme-snapshot:start -->
| Source | Count |
| --- | ---: |
| Manufacturer source files | 490 |
| Material definitions | 154 |
| Source filament objects | 12,309 |
| Color entries | 34,865 |
| Compiled filament variants | 51,432 |
| Source filaments with country of origin | 9,710 |
| Source filaments with TDS/product links | 5,693 |
| Source filaments with SDS links | 1,851 |
| Manufacturer product code/ID entries | 12,700 |
| EAN/GTIN entries | 2,737 |
| ASEAN manufacturer coverage | 24 brands / 147 source filaments |

Counts in this block are generated from the current repository state. Run `python scripts/readme_snapshot.py --write` after source-data changes. The compiled variant count expands source data across color, diameter, weight, and spool combinations.

### Spool metadata snapshot

| Source weight metadata | Entries |
| --- | ---: |
| `spool_type: plastic` | 9,710 |
| `spool_type: cardboard` | 3,152 |
| `spool_type: metal` | 0 |
| `spool_type: refill` (legacy) | 256 |
| `spool_type: unknow` (legacy) | 26 |
| `spool_type: null` | 0 |
| `spool_type` omitted | 309 |
| Effective refill (`is_refill: true` or legacy `spool_type: refill`) | 277 |
<!-- readme-snapshot:end -->

Counts describe repository source data. The live site reflects the latest deployed main commit; a draft branch is not deployed. ASEAN counts use the [curated brand registry](scripts/asean_manufacturers.json), not manufacturing origin.

## Contribute

[Report missing or incorrect data](https://github.com/Icezaza2543/SpoolmanDB-Community/issues/new/choose), or send a focused manufacturer PR with source evidence. Start with [CONTRIBUTING.md](CONTRIBUTING.md); maintainers should also read the [maintenance guide](docs/maintenance.md).

For local development, use Python 3.11+ and Node.js 22:

```sh
python -m pip install -r requirements-dev.txt
python scripts/compile_filaments.py
python scripts/validate.py --strict
python scripts/compile_id_baseline.py --strict
python -m pytest -q
node tests/test_display_name.cjs
node tests/test_explorer_security.cjs
python scripts/check_spoolman_compat.py --mode stable
python scripts/readme_snapshot.py --check
python -m http.server 8000
```

Open `http://localhost:8000/public/` to preview the Explorer. Do not commit generated `filaments.json`. New, verified identities need safe baseline enrollment as described in the contributor guide.

## Documentation

| Need | Read |
| --- | --- |
| Source fields, schemas, compiler and repository map | [Data reference](docs/data-reference.md) |
| IDs, evidence, packaging and review rules | [Maintenance](docs/maintenance.md) |
| Native fields, extensions and contract checks | [Upstream compatibility](docs/UPSTREAM_COMPATIBILITY.md) |
| Accepted imports and deferred conflicts | [Reconciliation audit](docs/audits/2026-10-30-reconciliation.md) |
| Missing evidence and reopening conditions | [Coverage backlog](docs/coverage-backlog.md) |
| Earlier owner-approved duplicate migrations | [Migration history](docs/migration-history.md) |

Published resources: [filaments.json](https://icezaza2543.github.io/SpoolmanDB-Community/filaments.json) · [materials.json](https://icezaza2543.github.io/SpoolmanDB-Community/materials.json) · [compiled schema](https://icezaza2543.github.io/SpoolmanDB-Community/filaments.compiled.schema.json).

## Thanks to upstream

Thank you to [Donkie](https://github.com/Donkie) for creating and maintaining Spoolman and SpoolmanDB, and to everyone who contributes data and reviews. We appreciate the collaboration on [Inslogic #297](https://github.com/Donkie/SpoolmanDB/pull/297), [country-of-origin support #283](https://github.com/Donkie/SpoolmanDB/pull/283), and the discussion of [material classification #309](https://github.com/Donkie/SpoolmanDB/issues/309).

This project supports that work through focused, evidence-backed contributions. It is independently maintained and does not claim official status or endorsement.

## License and policies

[MIT license](LICENSE), preserved from upstream. [Terms](TERMS.md) and [data/privacy policy](POLICY.md) explain hosted resources and contribution expectations.
