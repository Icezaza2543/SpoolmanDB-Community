# Upstream Compatibility & Divergence Tracker

This document tracks the compatibility status, technical divergence, and capability matrix between **SpoolmanDB-Community** and upstream repositories.

---

## 1. Upstream Relationships

| Upstream Repository | Role / Type | Status | Observed State & Relationship |
| :--- | :--- | :--- | :--- |
| **`Donkie/Spoolman`** | Application Server & Contract Provider | **ACTIVE UPSTREAM** | Primary target contract provider. Community dataset compiles strictly to Spoolman's `ExternalFilament` contract (`spoolman/externaldb.py`). |
| **`Donkie/SpoolmanDB`** | Static Data Repository | **ACTIVE UPSTREAM** | Latest observed main: `9d53d28703ba1bcc97ab504e069d437ae2053c5a` (2026-10-27), merging COO support #283; Inslogic #297 also merged. No automatic import into Community. |

> [!NOTE]
> **SpoolmanDB-Community** operates as an independent community database for 3D printing filaments. It is compatible with the pinned stable Spoolman contract and monitored against the current master canary. It enforces strict public ID stability, data verification guidelines, and rich technical metadata.

---

## 2. Tested Upstream Pins

Upstream testing configurations are defined in [`contracts/spoolman_upstream.json`](../contracts/spoolman_upstream.json) and machine-tracked via [`contracts/upstream_status.json`](../contracts/upstream_status.json):

* **Spoolman Stable Pin (Required Contract)**: `v0.25.0` (`6e1065009c7c45c9e38d5e1bec21d47273442889`)
  * Local snapshot: [`contracts/spoolman_externaldb.py`](../contracts/spoolman_externaldb.py)
  * Contract Check: **PASSING** (current compiled dataset validated)
* **Spoolman Canary (Advisory)**: Branch `master`
  * Contract Check: **PASSING** (No `ExternalFilament` field or type drift)
* **SpoolmanDB Historical Community Base**: `5b61e755926568ec3b3235701684595872b70b49` (`2025-11-28`)
  * This remains the historical data base used when Community diverged; it is not the current upstream head.
* **SpoolmanDB Latest Observed Main**: `9d53d28703ba1bcc97ab504e069d437ae2053c5a` (`2026-10-27`)
  * Includes country-of-origin support (#283). This does not change Community's historical base or imply automatic data synchronization.
  * Previous observation: `77c3ad7f4eecd342be72845063fe5b34dad69cd0` (2026-08-31), retained for audit history only; no longer the latest observed head.
* **Spoolman Application Observed Master**: `0fb375c33d3a781210545760e3bcdedb2fa1b6d0` (reviewed 2026-10-27).
  * Database COO support does not add the field to the application's `ExternalFilament` contract.

---

## 3. Capability & Divergence Matrix

Status Enum Definitions:
* **`supported`**: Native field/enum in Spoolman's `ExternalFilament` contract.
* **`community-extension`**: Field or feature maintained in community source metadata; emitted or handled safely without breaking Spoolman's contract.
* **`upstream-pending`**: Proposed feature awaiting upstream review or merge.
* **`hold`**: Feature held in community pending further consensus or design review.

| Feature / Capability | Status | Upstream Spoolman Behavior | Community Implementation | Upstream References |
| :--- | :--- | :--- | :--- | :--- |
| **`spool_type` Material Enum** | `supported` | Native enum in `ExternalFilament` (`plastic`, `cardboard`, `metal`) | Normalized to strict enum; legacy null types sanitized. | — |
| **Refill & `is_refill` Boolean** | `community-extension` | Absent from `ExternalFilament`; accepts `plastic`/`cardboard`/`metal` or `null` only | Supported (source `refill` normalized to `null` `spool_type` + explicit `is_refill: true`, preserving `legacy_id_spool_type`). | `Donkie/SpoolmanDB#26` |
| **Country of Origin (COO)** | `community-extension` (application contract) | Absent from `ExternalFilament`; database support is separate | Supported in both databases after #283 merged. Upstream uses an assigned-code enum; Community currently checks two uppercase letters, so validation is not identical. | [Merged #283](https://github.com/Donkie/SpoolmanDB/pull/283) |
| **SDS & TDS URLs** | `community-extension` | Absent from `ExternalFilament` (upstream proposals pending) | Supported with strict URI format validation. | `Donkie/SpoolmanDB#282`, `Donkie/Spoolman#395` |
| **Product & Article Codes** | `community-extension` | Absent from `ExternalFilament` | Supported in community source files. | `Donkie/SpoolmanDB#198`, `Donkie/SpoolmanDB#263`, `Donkie/Spoolman#789` |
| **EAN / GTIN Barcodes** | `community-extension` | Absent from `ExternalFilament` | Supported (`eans` + `eans_refill` metadata in source files). | `Donkie/SpoolmanDB#198`, `Donkie/SpoolmanDB#263`, `Donkie/Spoolman#789` |
| **Public ID Stability** | `community-extension` | Spoolman provides opaque native `id: str` field | Protected by automated CI stability gate & baseline manifest. | — |

---

## 4. Machine-Readable Tracker & Validation

The machine-readable state of this matrix is stored in [`contracts/upstream_status.json`](../contracts/upstream_status.json).

Automated CI tests ([`tests/test_upstream_compatibility.py`](../tests/test_upstream_compatibility.py)) validate that:
1. `contracts/upstream_status.json` is structurally valid and up to date.
2. The referenced Spoolman stable pin (`contracts/spoolman_upstream.json`) remains consistent and valid.
3. All capability status enums match allowed values (`supported`, `community-extension`, `upstream-pending`, `hold`).
4. Repository references use qualified repository notation (`Repository#PR`).
5. SpoolmanDB SHA matches exact 40-character hex SHA.
6. `last_reviewed` matches ISO 8601 date format (`YYYY-MM-DD`).
7. `test_no_false_native_contract_claims` dynamically parses `ExternalFilament` via `load_spoolman_contract()` to ensure native vs extension field assertions remain accurate.
