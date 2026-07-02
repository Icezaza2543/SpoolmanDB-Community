# Filament display name policy

## Problem

Many filament source templates describe a product line without repeating the material code. After compilation, a variant can look like:

```json
{
  "name": "Plus BLACK",
  "material": "ABS"
}
```

Read in isolation, `name` does not make the material obvious. The Community Explorer should still present a clear label to humans without changing the upstream-compatible compiled data contract.

## Decisions

### Keep compiled `name` upstream-compatible

Compiled `filaments.json` follows [Donkie/SpoolmanDB](https://github.com/Donkie/SpoolmanDB):

- `name` = source template + color expansion only
- `material` = separate authoritative field
- `id` generation is unchanged

The compiler must not prefix material into compiled `name`.

### No schema changes

Do not add `display_name` or any other compiled field. Spoolman and other consumers already treat `name` and `material` as separate values.

### Do not mass-edit source templates

Templates such as `"Plus {color_name}"` are valid upstream-style data. Only change a source template when the manufacturer’s official product name actually includes the material.

### Improve UX in Explorer only

Display and search logic may compose a user-facing label from `material` and `name` when the material is not already present as its own token in the product name.

## Implementation

| Layer | Responsibility |
| --- | --- |
| `scripts/compile_filaments.py` | Expand templates only |
| `public/display-name.js` | `getDisplayName()`, `buildFilamentSearchText()` |
| `public/app.js` | Render display names and search against them |
| `scripts/validate.py` | Non-blocking `WARN display-name` hints |
| Explorer quality dashboard | Informational `display-name` signals |

Token matching avoids false positives such as treating `ePLA` as standalone `PLA` or `PCABS` as standalone `ABS`.

## Examples

### Raw compiled data

```json
{
  "manufacturer": "AzureFilm",
  "name": "Plus BLACK",
  "material": "ABS"
}
```

### Explorer display

```text
ABS Plus BLACK
```

The Material column still shows `ABS`. Hovering the name can show the raw product name.

### Search behavior

Search matches:

- raw `name` (`Plus BLACK`)
- composed display text (`ABS Plus BLACK`)
- `material` (`ABS`)
- manufacturer, SKU/EAN, and color hex values already indexed by Explorer

Searching `ABS Plus` finds the variant even though raw `name` does not contain `ABS`.

### Names that already include material

```json
{
  "name": "ABS Prime White",
  "material": "ABS"
}
```

Explorer display remains `ABS Prime White`.

### Embedded material substrings

```json
{
  "name": "ePLA Matte BLACK",
  "material": "PLA"
}
```

`ePLA` is not treated as standalone `PLA`, so Explorer displays `PLA ePLA Matte BLACK`.

## Contributor guidance

- Put manufacturer/product-line wording in `name`.
- Put the authoritative material code in `material`.
- Do not add material to `name` unless it is part of the official product name on the manufacturer page or packaging.
- `python scripts/validate.py` prints informational display-name warnings.
- Use `python scripts/validate.py --strict-display-names` only when you intentionally want ambiguous templates to fail validation.

## Migration policy

- Do not run repo-wide template prefixing.
- Do not reintroduce compiler-level material mutation.
- When editing a manufacturer file for other reasons, keep official naming intact and rely on Explorer composition for UX.