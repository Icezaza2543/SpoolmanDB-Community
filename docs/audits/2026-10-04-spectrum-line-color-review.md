# spectrum line/color backlog resolution

Base `69a47e37483096b69c2f6b370b01942cbee5f3ef`. Only 1 previously deferred scoped groups.

This is an intentional breaking catalog migration: registered retired external IDs leave the catalog; existing Spoolman spools retain their copied local data. No automatic external-ID redirect. Packaging/tare and survivor identities are unchanged.

Exact decisions, retired IDs/keys, bindings, both-value conflicts, unresolved defaults and targeted identifiers: [review JSON](2026-10-04-spectrum-line-color-review.json).

```json
{
  "groups": 1,
  "approved_groups": 0,
  "retired": 0,
  "deferred": 1,
  "before_count": 51656,
  "after_count": 51656,
  "metadata_fields_changed": 0,
  "code_transfers": 0
}
```
