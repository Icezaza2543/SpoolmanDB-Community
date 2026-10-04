# overture line/color backlog resolution

Base `39cf047a0da6807d9394cfe1152607cbb17ba8dd`. Only 1 previously deferred scoped groups.

This is an intentional breaking catalog migration: registered retired external IDs leave the catalog; existing Spoolman spools retain their copied local data. No automatic external-ID redirect. Packaging/tare and survivor identities are unchanged.

Exact decisions, retired IDs/keys, bindings, both-value conflicts, unresolved defaults and targeted identifiers: [review JSON](2026-10-04-overture-line-color-review.json).

```json
{
  "groups": 1,
  "approved_groups": 1,
  "retired": 1,
  "deferred": 0,
  "before_count": 51663,
  "after_count": 51662,
  "metadata_fields_changed": 0,
  "code_transfers": 0
}
```
