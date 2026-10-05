# Duplicate migration owner-pending backlog

**Closed on 2026-10-05.** No candidate groups are pending.

The owner decided all 180 rows of the former decision sheet:

- 179 rows were merged. Each brand has its own `2026-10-04-<brand>-owner-closure.json` audit.
- OV083, Overture TPU Gray/Grey, was recorded as not a duplicate in `contracts/not_duplicates.json`.

`contracts/owner_pending_duplicates.json` and `backlog-decisions.csv` are now empty, so the duplicate guard enforces with no temporary exemptions.

A whole-catalog audit (`audit_duplicates.py --all`) scanned 490 sources and 51,412 records. It reported 1 candidate, which is the recorded not-duplicate, and 0 owner-pending or unresolved groups.

Separate future work, outside this campaign:

- OFD-imported variants with no evidence that they are sold, such as Nebula 2.85 mm.
- Brand-prefix `display_name` cleanup.
- Quality of SKU fanout that predates this campaign.
