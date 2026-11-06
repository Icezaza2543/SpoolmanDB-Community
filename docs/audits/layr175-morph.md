# Layr175 MORPH — issue #67

Reviewed 2026-11-06. Owner explicitly approved omitting all color values because
this product has unpredictable production-transition colors, including variation
along a spool. MORPH is the product name, not a guaranteed physical color.

- Request: https://github.com/Icezaza2543/SpoolmanDB-Community/issues/67
- Official product: https://ebb3d.se/produkt/layr175-morph-1-75-mm-1000g/
- Official profiles: https://ebb3d.se/wp-content/uploads/Layr175-Bambulabprofiles.zip

The product page establishes PLA, 1.75 mm, 1000 g, SKU `LYR-HPLA-MOR`, and
manufacturing in Karlstad, Sweden. It describes filament made during color
changes, with the same quality requirements as regular Layr175 filament, not
second-grade material. It does not establish recycled feedstock. Product images
are examples, not a repeatable palette.

The nine official Bambu profiles specify density 1.24 g/cm³ and nozzle range
205–230 °C. The 230 °C default matches the issue and the official profiles
(some multi-extruder profiles also list 220 °C). Density is a manufacturer
profile value, not a claimed TDS measurement.
Bed 55 °C matches the issue and the textured/hot/engineering plate settings in
the H2C/H2D/H2S/P1S/P2S/X1/X1 Carbon profiles; it is a profile-specific default,
not a universal range. A1/A1 mini and cool plates use other settings (35–65 °C).
No global bed range is fabricated from those plate-specific settings.

Spool type and tare are left unspecified: the manufacturer's packaging transition
announcement does not bind an exact MORPH production lot. No refill claim is made.
No document URL is mislabeled as a TDS.

Source `hex: null` deliberately emits `color_hex: null`, `color_hexes: null` and
`multi_color_direction: null`. No placeholder swatch or invented fixed palette.
The existing Explorer labels absent color as "No color"; Spoolman compatibility
and projection are validated with the actual new record.

Exactly one new identity: `layr175_pla_morph_1000_175_n`.
Historical records and IDs must remain byte-for-byte equivalent after parsing.
