# Discovery and integration roadmap

Research date: **2026-10-30**. These are proposals unless marked implemented. Keep the static catalog and protected public IDs as the common foundation. No marketplace backend, plugin installer or preset generator was built in this maintenance cycle.

## OrcaSlicer: what is available

The [v2.5.0-alpha release](https://github.com/OrcaSlicer/OrcaSlicer/releases/tag/v2.5.0-alpha) (16 October, tag commit `3880f2c`) introduces embedded Python plugins distributed as `.py` or `.whl`, installed locally or through Orca Cloud. Capabilities include scripts, pages and slicing hooks. The release explicitly calls the API experimental and subject to change. Permission prompts cover network, files and processes; they are not a security sandbox. This is a feasibility reference, not a stable integration contract.

The [official development guide](https://www.orcaslicer.com/wiki/developer_reference/plugin_development/plugin_development) describes an embedded `orca` module, `@orca.plugin`, `orca.base`, `register_capabilities()` and capability registration. Metadata includes name, author, version and description under `[tool.orcaslicer.plugin]`; dependencies use Python script/package metadata. Its host interface is largely read-only. Documentation examples are illustrative, and current wiki content can evolve beyond the alpha tag: validate any implementation against the chosen release's source and runtime before promising support.

The [plugin UI guide](https://github.com/OrcaSlicer/OrcaSlicer/wiki/plugins_getting_started) shows searchable discovery and separate information, configuration, changelog and diagnostics. [Cloud plugins](https://github.com/OrcaSlicer/OrcaSlicer/wiki/plugins_cloud) use account subscriptions and slicer-managed installation/update flows. [Orca Cloud help](https://cloud.orcaslicer.com/wiki/) covers profile synchronization and shared printer/filament/process bundles. These are useful patterns for discovery, compatibility metadata and change history; creator or community badges do not establish physical measurement accuracy.

An [open alpha network-permission report](https://github.com/OrcaSlicer/OrcaSlicer/issues/16592) describes repeated prompts for changing URLs and socket events. Treat this as reported behavior to reproduce, not a confirmed guarantee for every release. It reinforces the need for a narrowly scoped, read-only prototype before designing one-click workflows.

## Priorities and tradeoffs

Effort and maintenance are relative estimates, not delivery promises. Compatibility means both database identity preservation and the consumer application's supported fields.

| Horizon / opportunity | User value and deliverable | Effort | Technical risk | Compatibility | Ongoing maintenance |
| --- | --- | --- | --- | --- | --- |
| Quick win A: discovery hub — implemented | Responsive cards, optional table, search, filters and expandable details | Small | Low | Static UI only; original IDs retained | Low; browser checks |
| Quick win B: setup guidance — implemented | Copy External DB directory URL, clear server-side configuration steps | Small | Low | Existing Spoolman `EXTERNAL_DB_URL`; website does not configure a server | Low; check upstream config docs |
| Quick win C: completeness — implemented in details | Show available documents/identifiers and missing tare; no verified badge | Small | Low | Display existing metadata without changing source meaning | Low |
| Quick win F: shareable catalog — implemented | Search/filter URLs and exact-variant links | Small | Low | Protected IDs and URL-encoded filters | Low; retain link tests |
| Medium C: evidence ledger | Field-level source URL, document date, package/lot and measurement provenance | Medium | Medium: contradictory or stale evidence | Sidecar extension first; preserve source contract and IDs | Medium; reviewers revisit evidence |
| Medium D: contribution wizard | Generate a reviewable issue/JSON draft with tare photo, packaging and source checklist | Medium | Medium: incomplete or misleading submissions | Existing schemas and review gate; no automatic catalog writes | Medium; schema/template updates |
| Medium B: deployment-specific setup helper | User-selected Compose example with explicit restart instructions | Small–medium | Medium: differing deployment versions | No credentials or server discovery in the static website | Medium; supported-version matrix |
| Experimental E: read-only Orca catalog plugin | Search cached catalog; open product evidence and browser deep links | Medium | High: alpha API and permissions | Pin Orca version and catalog schema; do not modify presets or IDs | High; OS/release testing |
| Experimental E: preset import adapter | Import only an independently validated profile for an exact printer/nozzle/material combination | Large | High: printing behavior and profile inheritance | Separate adapter, explicit review, supported-release matrix | High; physical calibration and regression testing |
| Upstream: focused contributions | Offer isolated schema/compiler tests, contract fixes, or one measured brand update | Small–medium | Low–medium: maintainer fit | Upstream style, required tare evidence, no Community UI dependency | Low–medium; maintainers decide acceptance |

## Experimental integration acceptance gate

Start in a separate branch with a local plugin. Pin the Orca tag, plugin version and database schema. Cache downloads with a timestamp and handle offline/invalid data without blocking slicing. Request only required network access. Show manufacturer, package, source and missing fields; reuse catalog IDs solely as catalog references. Test load/unload, permissions, update/rollback and Windows/macOS/Linux behavior on the supported release.

Do not infer flow, temperature, speed, pressure advance or calibration values from generic filament properties. A catalog record is not an Orca printing preset. There is no verified Community-to-Orca preset API adapter in this branch. Cloud publication requires a separate reviewed package and release process; account subscriptions are not a way for this website to install software automatically.

## Material classification remains HOLD

[Issue #309](https://github.com/Donkie/SpoolmanDB/issues/309) remains open. The [maintainer's response](https://github.com/Donkie/SpoolmanDB/issues/309#issuecomment-6426915078) favors specific material labels when the format permits. This establishes direction, not permission to rewrite this Community catalog's historical identities. The task explicitly holds mass migration.

For example, a source named PLA+ 2.0 currently classified `PLA` would produce a different identity if its material changed to `PLA+`. Likewise, changing `PA` to `PA6-CF20` requires evidence of both polymer and filler proportion. This branch changes neither example nor any existing material classification. Before a future migration, agree with Donkie on classification evidence, stable-ID behavior, an old-to-new mapping, consumer impact and whether display metadata can carry specificity without replacing identity.

See [compatibility](UPSTREAM_COMPATIBILITY.md), [reconciliation](audits/2026-10-30-reconciliation.md) and [manufacturer coverage](audits/2026-10-30-manufacturer-coverage.md) for evidence and deferred work.
