# printwithsmile line/color backlog resolution

Base `3377a6a65f9344ad60b6115816a80f683cae04c0`. Only 2 previously deferred scoped groups.

This is an intentional breaking catalog migration: registered retired external IDs leave the catalog; existing Spoolman spools retain their copied local data. No automatic external-ID redirect. Packaging/tare and survivor identities are unchanged.

Exact decisions, retired IDs/keys, bindings, both-value conflicts, unresolved defaults and targeted identifiers: [review JSON](2026-10-04-printwithsmile-line-color-review.json).

```json
{
  "groups": 2,
  "approved_groups": 0,
  "retired": 0,
  "deferred": 2,
  "before_count": 51661,
  "after_count": 51661,
  "metadata_fields_changed": 0,
  "code_transfers": 0
}
```
