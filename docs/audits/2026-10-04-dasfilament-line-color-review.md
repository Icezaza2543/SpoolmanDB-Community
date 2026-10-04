# dasfilament line/color backlog resolution

Base `fb5b7104798a1b9d37daf456f9c0154c517ae448`. Only 2 previously deferred scoped groups.

This is an intentional breaking catalog migration: registered retired external IDs leave the catalog; existing Spoolman spools retain their copied local data. No automatic external-ID redirect. Packaging/tare and survivor identities are unchanged.

Exact decisions, retired IDs/keys, bindings, both-value conflicts, unresolved defaults and targeted identifiers: [review JSON](2026-10-04-dasfilament-line-color-review.json).

```json
{
  "groups": 2,
  "approved_groups": 1,
  "retired": 1,
  "deferred": 1,
  "before_count": 51694,
  "after_count": 51693,
  "metadata_fields_changed": 0,
  "code_transfers": 0
}
```
