# Upstream Compatibility & Divergence Tracker

This document tracks the compatibility status, technical divergence, and capability matrix between **SpoolmanDB-Community** and upstream repositories.

---

## 1. Upstream Relationships

| Upstream Repository | Role / Type | Status | Relationship & Governance |
| :--- | :--- | :--- | :--- |
| **`Donkie/Spoolman`** | Application Server & Contract Provider | **ACTIVE UPSTREAM** | Primary target contract provider. Community dataset compiles strictly to Spoolman's `ExternalFilament` contract (`spoolman/externaldb.py`). |
| **`Donkie/SpoolmanDB`** | Static Data Repository | **INACTIVE UPSTREAM** | Original upstream static data repository. Currently inactive / unmerged upstream. |

> [!NOTE]
> **SpoolmanDB-Community** operates as an independent community database for 3D printing filaments. It enforces strict public ID stability, data verification guidelines, and rich technical metadata while maintaining full backward and forward compatibility with Spoolman.

---

## 2. Tested Upstream Pins

Upstream testing configurations are defined in [`contracts/spoolman_upstream.json`](file:///contracts/spoolman_upstream.json) and machine-tracked via [`contracts/upstream_status.json`](file:///contracts/upstream_status.json):

* **Spoolman Stable Pin (Required Contract)**: `v0.25.0` (`6e1065009c7c45c9e38d5e1bec21d47273442889`)
  * Local snapshot: [`contracts/spoolman_externaldb.py`](file:///contracts/spoolman_externaldb.py)
  * Contract Check: **PASSING** (51,626 compiled records validated)
* **Spoolman Canary (Advisory)**: Branch `master`
  * Contract Check: **PASSING** (No `ExternalFilament` field or type drift)
* **SpoolmanDB Original Base**: `upstream/main`

---

## 3. Capability & Divergence Matrix

Status Enum Definitions:
* **`supported`**: Native feature fully supported by both Spoolman core and SpoolmanDB-Community.
* **`community-extension`**: Field or feature maintained in community source metadata; emitted or handled safely without breaking Spoolman's contract.
* **`upstream-pending`**: Proposed feature awaiting upstream review or merge.
* **`hold`**: Feature held in community pending further consensus or design review.

| Feature / Capability | Status | Upstream Spoolman Behavior | Community Implementation | Upstream References |
| :--- | :--- | :--- | :--- | :--- |
| **`spool_type` Material Enum** | `supported` | Native enum (`plastic`, `cardboard`, `metal`) | Normalized to strict enum; legacy null types sanitized. | — |
| **Refill & `is_refill` Boolean** | `community-extension` | Legacy `spool_type: refill` mapped to `is_refill` | Explicit `is_refill` boolean with `legacy_id_spool_type` sentinel preservation. | #282, #283 |
| **Country of Origin (COO)** | `community-extension` | Ignored by Spoolman core schema | Maintained in source metadata (ISO 3166-1 alpha-2 standard). | #198 |
| **SDS & TDS URLs** | `supported` | Native optional URI fields (`sds_url`, `tds_url`) | Fully supported with strict URI format validation. | — |
| **Product & Article Codes** | `supported` | Native optional string list | Fully supported in community source files. | — |
| **EAN / GTIN Barcodes** | `community-extension` | Native `eans` string list; `eans_refill` extended | Supported (`eans` + `eans_refill` metadata). | #282 |
| **Public ID Stability** | `supported` | Primary key for external DB filament binding | Enforced via automated PR-base trusted stability gate & baseline manifest. | — |

---

## 4. Machine-Readable Tracker & Validation

The machine-readable state of this matrix is stored in [`contracts/upstream_status.json`](file:///contracts/upstream_status.json).

Automated CI tests ([`tests/test_upstream_compatibility.py`](file:///tests/test_upstream_compatibility.py)) validate that:
1. `contracts/upstream_status.json` is structurally valid and up to date.
2. The referenced Spoolman stable pin (`contracts/spoolman_upstream.json`) remains consistent and valid.
3. All capability status enums match allowed values (`supported`, `community-extension`, `upstream-pending`, `hold`).
