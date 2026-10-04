# sakata3d line/color backlog resolution

Base `9565d569e2e55c6f5597801b07f5fd21adb0e12e`. Only 13 previously deferred scoped groups.

This is an intentional breaking catalog migration: registered retired external IDs leave the catalog; existing Spoolman spools retain their copied local data. No automatic external-ID redirect. Packaging/tare and survivor identities are unchanged.

Exact decisions, retired IDs/keys, bindings, both-value conflicts, unresolved defaults and targeted identifiers: [review JSON](2026-10-04-sakata3d-line-color-review.json).

```json
{
  "groups": 13,
  "approved_groups": 0,
  "retired": 0,
  "deferred": 13,
  "before_count": 51656,
  "after_count": 51656,
  "metadata_fields_changed": 0,
  "code_transfers": 0
}
```
