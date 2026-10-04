# gizmodorks line/color backlog resolution

Base `46d4e6a66147f3bbcb5dcd0bd26752e471ba6e81`. Only 10 previously deferred scoped groups.

This is an intentional breaking catalog migration: registered retired external IDs leave the catalog; existing Spoolman spools retain their copied local data. No automatic external-ID redirect. Packaging/tare and survivor identities are unchanged.

Exact decisions, retired IDs/keys, bindings, both-value conflicts, unresolved defaults and targeted identifiers: [review JSON](2026-10-04-gizmodorks-line-color-review.json).

```json
{
  "groups": 10,
  "approved_groups": 10,
  "retired": 10,
  "deferred": 0,
  "before_count": 51673,
  "after_count": 51663,
  "metadata_fields_changed": 0,
  "code_transfers": 0
}
```
