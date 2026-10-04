# aurapol line/color backlog resolution

Base `0eeb49f4d03aff5911a0a9588b9c174784d08d7b`. Only 3 previously deferred scoped groups.

This is an intentional breaking catalog migration: registered retired external IDs leave the catalog; existing Spoolman spools retain their copied local data. No automatic external-ID redirect. Packaging/tare and survivor identities are unchanged.

Exact decisions, retired IDs/keys, bindings, both-value conflicts, unresolved defaults and targeted identifiers: [review JSON](2026-10-04-aurapol-line-color-review.json).

```json
{
  "groups": 3,
  "approved_groups": 1,
  "retired": 1,
  "deferred": 2,
  "before_count": 51698,
  "after_count": 51697,
  "metadata_fields_changed": 0,
  "code_transfers": 0
}
```
