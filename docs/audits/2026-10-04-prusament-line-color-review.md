# prusament line/color backlog resolution

Base `18c5a1f685bd3d60f230c6129e21f5facc756410`. Only 1 previously deferred scoped groups.

This is an intentional breaking catalog migration: registered retired external IDs leave the catalog; existing Spoolman spools retain their copied local data. No automatic external-ID redirect. Packaging/tare and survivor identities are unchanged.

Exact decisions, retired IDs/keys, bindings, both-value conflicts, unresolved defaults and targeted identifiers: [review JSON](2026-10-04-prusament-line-color-review.json).

```json
{
  "groups": 1,
  "approved_groups": 1,
  "retired": 1,
  "deferred": 0,
  "before_count": 51657,
  "after_count": 51656,
  "metadata_fields_changed": 0,
  "code_transfers": 0
}
```
