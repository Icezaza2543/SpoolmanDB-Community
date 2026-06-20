# Contributing to SpoolmanDB Community

Thanks for helping keep the filament database current.

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