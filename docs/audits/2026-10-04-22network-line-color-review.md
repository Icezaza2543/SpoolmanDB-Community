# 22network line/color backlog resolution

Base `3ea46d278f4e11109d4dd6d417d85cc73a889ed1`. Only 3 previously deferred scoped groups.

This is an intentional breaking catalog migration: registered retired external IDs leave the catalog; existing Spoolman spools retain their copied local data. No automatic external-ID redirect. Packaging/tare and survivor identities are unchanged.

Exact decisions, retired IDs/keys, bindings, both-value conflicts, unresolved defaults and targeted identifiers: [review JSON](2026-10-04-22network-line-color-review.json).

```json
{
  "groups": 3,
  "approved_groups": 3,
  "retired": 3,
  "deferred": 0,
  "before_count": 51701,
  "after_count": 51698,
  "metadata_fields_changed": 0,
  "code_transfers": 0
}
```
