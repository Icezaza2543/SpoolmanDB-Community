# Contributing to SpoolmanDB Community

Thanks for helping keep the filament database current!

## How to Contribute

We welcome contributions of all types. Depending on your experience with Git and JSON, you can:
- **Report an Error or Suggest a New Filament:** If you are not comfortable writing JSON or using Git, please [open an issue](https://github.com/Icezaza2543/SpoolmanDB-Community/issues/new/choose) using one of our structured templates.
- **Submit a Pull Request (PR):** If you can edit JSON directly, feel free to submit a PR with your changes.

## Data changes

- Add or edit manufacturer source files in `filaments/`.
- Keep manufacturer names, color names, weights, diameters, and temperatures aligned with manufacturer-published data when possible.
- Include source links in your pull request description for any new brand, new material, or data correction.
- Keep changes focused. Prefer one manufacturer or one related correction set per pull request.
- When adding an ASEAN manufacturer, register its source filename in `scripts/asean_manufacturers.json`. Use the brand's location; never infer it from `country_of_origin`.
- If setting `country_of_origin`, use ISO 3166-1 alpha-2 only (`CN`, `US`, `DE`, …), and only when product/SKU manufacturing origin is source-backed. Prefer omitting the field over HQ, store, or distributor region.

## Validation

Run these checks before opening a pull request:

```bash
# Refresh generated repository metrics in README.md
python scripts/readme_snapshot.py --write

# Compile the individual filament files into filaments.json
python scripts/compile_filaments.py

# Validate all files, compiled outputs, and Public ID baseline
python scripts/validate.py

# Check Public Compiled ID baseline manifest directly
python scripts/compile_id_baseline.py

# If you legitimately added new filament variants, update the baseline:
python scripts/compile_id_baseline.py --update

# Run unit tests to verify compile and baseline functionality
python -m pytest -q

# Required: deterministic offline check against the pinned Spoolman contract
# (version/commit: contracts/spoolman_upstream.json only)
python scripts/check_spoolman_compat.py --mode stable

# Advisory: fetch Donkie/Spoolman master and report ExternalFilament field/type drift
# Canary failures are diagnostic only; they do not block normal data PRs.
python scripts/check_spoolman_compat.py --mode canary

# Maintainer / weekly only: fetch the configured stable commit and assert the
# local snapshot matches (not part of normal PR stable CI).
python scripts/check_spoolman_compat.py --mode verify-pin
```

The stable pin and canary ref are configured only in [`contracts/spoolman_upstream.json`](contracts/spoolman_upstream.json). Do not hardcode Spoolman SHAs elsewhere. See [docs/spoolman-compatibility.md](docs/spoolman-compatibility.md). Updating the pin is a deliberate maintainer change (edit the config, refresh `contracts/spoolman_externaldb.py`, run stable + verify-pin).

New filament variants (additions) generate informational baseline warnings until `python scripts/compile_id_baseline.py --update` is run. `--update` will safely refuse to write if the existing baseline is malformed, or if breaking changes (altered historical IDs / removed variants) are detected without specifying `--accept-breaking-baseline-changes` (breaking flags cannot bypass malformed baseline files).

The generated `filaments.json` should compile cleanly, and all schema, unit, and **stable** Spoolman compatibility checks must pass.

For refill products, use `"is_refill": true` in the relevant weight object and omit `spool_type`. The legacy source value `"spool_type": "refill"` is still accepted to avoid changing existing public IDs, but it is normalized to `spool_type: null` in the published database.

## Review expectations

Pull requests are reviewed for:

- valid JSON and schema compliance
- manufacturer/source evidence
- duplicate IDs or conflicting entries
- color naming and hex accuracy
- minimal unrelated formatting churn
