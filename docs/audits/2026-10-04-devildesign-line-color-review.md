# devildesign line/color backlog resolution

Base `2695fe9f151fe7ee07f1373f2e09b2271fab6e11`. Only 5 previously deferred scoped groups.

This is an intentional breaking catalog migration: registered retired external IDs leave the catalog; existing Spoolman spools retain their copied local data. No automatic external-ID redirect. Packaging/tare and survivor identities are unchanged.

Exact decisions, retired IDs/keys, bindings, both-value conflicts, unresolved defaults and targeted identifiers: [review JSON](2026-10-04-devildesign-line-color-review.json).

```json
{
  "groups": 5,
  "approved_groups": 5,
  "retired": 5,
  "deferred": 0,
  "before_count": 51693,
  "after_count": 51688,
  "metadata_fields_changed": 20,
  "code_transfers": 0
}
```
