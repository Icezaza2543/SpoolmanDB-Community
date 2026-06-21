# Contributing to SpoolmanDB Community

Thanks for helping keep the filament database current!

## How to Contribute

We welcome contributions of all types. Depending on your experience with Git and JSON, you can:
- **Report an Error or Suggest a New Filament:** If you are not comfortable writing JSON or using Git, please [open an issue](https://github.com/Donkie/SpoolmanDB-Community/issues/new/choose) using one of our structured templates.
- **Submit a Pull Request (PR):** If you can edit JSON directly, feel free to submit a PR with your changes.

## Data changes

- Add or edit manufacturer source files in `filaments/`.
- Keep manufacturer names, color names, weights, diameters, and temperatures aligned with manufacturer-published data when possible.
- Include source links in your pull request description for any new brand, new material, or data correction.
- Keep changes focused. Prefer one manufacturer or one related correction set per pull request.

## Validation

Run these checks before opening a pull request:

```powershell
python scripts/compile_filaments.py
check-jsonschema --schemafile materials.schema.json materials.json
check-jsonschema --schemafile filaments.schema.json filaments/*
```

If `check-jsonschema` is missing, install it in your Python environment:

```powershell
python -m pip install check-jsonschema
```

The generated `filaments.json` should compile cleanly, and schema validation should pass for both materials and filament source files.

## Review expectations

Pull requests are reviewed for:

- valid JSON and schema compliance
- manufacturer/source evidence
- duplicate IDs or conflicting entries
- color naming and hex accuracy
- minimal unrelated formatting churn