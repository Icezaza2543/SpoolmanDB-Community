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

## Validation

Run these checks before opening a pull request:

```bash
# Compile the individual filament files into filaments.json
python scripts/compile_filaments.py

# Validate all files and compiled outputs against schemas
python scripts/validate.py

# Run unit tests to verify compile functionality
python -m pytest
```

If requirements are missing, install the development dependencies:

```bash
pip install -r requirements-dev.txt
```

The generated `filaments.json` should compile cleanly, and all validations and unit tests must pass.

## Review expectations

Pull requests are reviewed for:

- valid JSON and schema compliance
- manufacturer/source evidence
- duplicate IDs or conflicting entries
- color naming and hex accuracy
- minimal unrelated formatting churn