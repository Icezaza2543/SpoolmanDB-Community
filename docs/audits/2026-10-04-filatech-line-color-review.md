# filatech line/color backlog resolution

Base `0fc756abcb0a8a1fec76812c92d2d28035eeaebb`. Only 16 previously deferred scoped groups.

This is an intentional breaking catalog migration: registered retired external IDs leave the catalog; existing Spoolman spools retain their copied local data. No automatic external-ID redirect. Packaging/tare and survivor identities are unchanged.

Exact decisions, retired IDs/keys, bindings, both-value conflicts, unresolved defaults and targeted identifiers: [review JSON](2026-10-04-filatech-line-color-review.json).

```json
{
  "groups": 16,
  "approved_groups": 0,
  "retired": 0,
  "deferred": 16,
  "before_count": 51673,
  "after_count": 51673,
  "metadata_fields_changed": 0,
  "code_transfers": 0
}
```
