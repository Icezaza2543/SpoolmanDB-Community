# buddy3d line/color backlog resolution

Base `d901e4348e63a721d8d4df6d841441f1dd252f66`. Only 1 previously deferred scoped groups.

This is an intentional breaking catalog migration: registered retired external IDs leave the catalog; existing Spoolman spools retain their copied local data. No automatic external-ID redirect. Packaging/tare and survivor identities are unchanged.

Exact decisions, retired IDs/keys, bindings, both-value conflicts, unresolved defaults and targeted identifiers: [review JSON](2026-10-04-buddy3d-line-color-review.json).

```json
{
  "groups": 1,
  "approved_groups": 1,
  "retired": 1,
  "deferred": 0,
  "before_count": 51697,
  "after_count": 51696,
  "metadata_fields_changed": 0,
  "code_transfers": 0
}
```
