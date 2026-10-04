# protopasta line/color backlog resolution

Base `e933c168c154ee4e875dfb1689226ad436816358`. Only 4 previously deferred scoped groups.

This is an intentional breaking catalog migration: registered retired external IDs leave the catalog; existing Spoolman spools retain their copied local data. No automatic external-ID redirect. Packaging/tare and survivor identities are unchanged.

Exact decisions, retired IDs/keys, bindings, both-value conflicts, unresolved defaults and targeted identifiers: [review JSON](2026-10-04-protopasta-line-color-review.json).

```json
{
  "groups": 4,
  "approved_groups": 4,
  "retired": 4,
  "deferred": 0,
  "before_count": 51661,
  "after_count": 51657,
  "metadata_fields_changed": 0,
  "code_transfers": 0
}
```
