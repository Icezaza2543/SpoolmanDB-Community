# AzureFilm line/color backlog resolution

Base `10e2a62bfa255c66bbad9701cd15f3f82660179a`. Only 9 previously deferred scoped groups.

This is an intentional breaking catalog migration: registered retired external IDs leave the catalog; existing Spoolman spools retain their copied local data. No automatic external-ID redirect. Packaging/tare and survivor identities are unchanged.

Exact decisions, retired IDs/keys, bindings, both-value conflicts, unresolved defaults and targeted identifiers: [review JSON](2026-10-04-azurefilm-line-color-review.json).

```json
{
  "groups": 9,
  "approved_groups": 0,
  "retired": 0,
  "deferred": 9,
  "before_count": 51697,
  "after_count": 51697,
  "metadata_fields_changed": 0,
  "code_transfers": 0
}
```
