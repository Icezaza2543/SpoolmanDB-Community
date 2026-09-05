# Coverage Backlog

This document records established, unresolved coverage and schema items reserved for future maintenance cycles.

## Phase Status

- **P0 Status:** `SATURATED_WITH_WATCHLIST`
- **P1 Status:** `SATURATED_WITH_BACKLOG`
- **Reopening Condition:** Reopen items when new official/user-approved evidence or explicit identity/schema authorization addresses the recorded blocker.

## Maintenance Posture

Active development is paused after the completed maintenance and frontend/documentation fixes. This backlog is a handoff, not authorization to start another audit, import, migration, or upstream contribution. Resume focused work when the owner requests it, a reported defect is accepted for correction, or new evidence is approved for an unresolved item.

Historical public IDs and baseline identity keys remain immutable. Do not remove or rekey legacy records merely to standardize names or packaging. See [the maintenance guide](maintenance.md) for validation and delivery requirements.

## Evidence Backlog

- **SABIC**: Net mass / current package matrix verification
- **Creality**: Incomplete exact bindings and packaging matrices
- **eSUN**: Incomplete package/SKU bindings
- **MatterHackers**: Namespace ambiguity across product lines
- **FlashForge**: HS/Rapid variant and packaging ambiguity
- **Bambu Lab**: Remaining package and refill bindings
- **Prusament**: Recycled batch-color ambiguity
- **Raise3D**: Multi-weight identifier ambiguity

## Schema Backlog

- **Xioneer VXL**: Material and support filament schema support
- **eSUN**: Package-specific identifier extensions
- **Raise3D**: Multi-weight SKU binding schema support

## Recent Evidence and Identity Handoff — 2026-09-05

These findings were recorded during the evidence-maintenance audit ending at `6525b45630e7f313dea6cf39673ea0a95968386d`. The subsequent frontend/documentation commit `d3c4a04ceb18b8ccb63c5d88115e3aa5138c0838` did not change filament data. This section preserves that audit's evidence; it is not a claim that the linked catalogs were re-audited when this document was updated.

### Smartfil PLA BASIC — BLOCK_EVIDENCE / IDENTITY_REVIEW

- **Finding:** The [official PLA BASIC product](https://www.smartmaterials3d.com/en/pla-basic-filament) is distinct from standard PLA. The manufacturer-linked [TDS attachment](https://www.smartmaterials3d.com/en/index.php?controller=attachment&id_attachment=475) could not be retrieved during the audit. Existing Smartfil / Smart Materials naming also needs a physical-product comparison before importing anything.
- **To unblock:** Obtain the official TDS, including a manufacturer PDF supplied by the owner, and establish the exact family/color/package/identifier mapping against existing records. Do not reuse a generic PLA density, infer spool construction, or expand one verified SKU across other colors.
- **Accepted change in that audit:** None.

### Das Filament 1 kg refills — IDENTITY_DESIGN_REQUIRED

- **Finding:** The [official 1 kg spool/refill FAQ](https://dasfilament.de/2025/10/16/faq-zu-1-kg-spulen-und-1-kg-refills/) provides refill-construction evidence, including the absence of a cardboard core. Legacy PLA/PETG refill definitions retain cardboard/non-refill encoding. Changing their refill semantics changes generated public IDs under current compiler logic.
- **To unblock:** Design and explicitly approve an identity-safe correction/migration, with tests proving preservation of all historical public IDs and baseline keys. `legacy_id_spool_type` alone does not neutralize a change to refill status. Do not create duplicate refills as a workaround.
- **Accepted change in that audit:** None; legacy records preserved.

### NinjaTek Chinchilla — IDENTITY_DESIGN_REQUIRED

- **Finding:** The [official product page](https://ninjatek.com/shop/chinchilla/) and [TDS](https://ninjatek.com/wp-content/uploads/Chinchilla-TDS.pdf) describe a TPE blend; existing names/material identities use TPU.
- **Already completed:** Density 1.13 g/cc, nozzle guidance 225–235°C, matte finish and TDS link. Unsupported numeric bed endpoints were removed; the manufacturer gives a qualitative room-temperature lower bound. Do not repeat those corrections.
- **To unblock:** Establish how to represent the material terminology accurately without renaming/rekeying the historical TPU identities, then obtain approval for that design. No material or identity migration is currently authorized.

### Snapmaker TPU 90A — BLOCK_EVIDENCE

- **Finding:** Nozzle guidance on the [product page](https://shop.snapmaker.com/products/tpu-90a-filament-1kg) differs from the historical database range. The [official TDS V1.0.0](https://s3.us-west-2.amazonaws.com/snapmaker.com/download/manual/Snapmaker+TPU+90A+Technical+Data+Sheet+V1.0.0.pdf) was linked without overwriting the numerical range.
- **To unblock:** Reconcile the product page, the relevant TDS printing table, and the exact product generation. Apply only a supported ID-neutral metadata correction; do not overwrite previously approved data merely because one page differs.

### Snapmaker ASA — BLOCK_EVIDENCE / IDENTITY_REVIEW

- **Finding:** The [current product page](https://shop.snapmaker.com/products/asa-filament-1kg) and [TDS V1.0.1](https://s3.us-west-2.amazonaws.com/snapmaker.com/download/manual/Snapmaker+ASA+Technical+Data+Sheet+V1.0.1.pdf) differ from legacy plastic-generation records in technical guidance and Black naming.
- **To unblock:** Verify the generation/package matrix and whether Black corresponds to the existing Carbon Black identity. Do not blindly overwrite legacy specifications or create a duplicate color identity.
- **Accepted change in that audit:** None.

### Snapmaker PVA packaging — IDENTITY_REVIEW

- **Finding:** The [official PVA page](https://www.snapmaker.com/en/filaments/pva/) shows a current package that needs comparison against the existing unspecified-spool identity. Current imagery alone does not establish that an older public identity should be changed.
- **To unblock:** Establish an exact product-generation/package match and prove baseline preservation before proposing a packaging correction. Do not rekey a historical record or infer a second product solely from imagery.
- **Accepted change in that audit:** None.

### Recent no-delta checks

Snapmaker Matte PLA and SnapSpeed PLA were also inspected; no independently safe additional delta was accepted. This is not a claim of permanent worldwide completeness. Do not rerun those checks without a concrete new gap or evidence trigger.
