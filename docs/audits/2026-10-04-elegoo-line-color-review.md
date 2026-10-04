# elegoo line/color backlog resolution

Base `ec7b78dd282cd9f7f7e93beb80cf35946a072e3c`. Only 37 previously deferred scoped groups.

This is an intentional breaking catalog migration: registered retired external IDs leave the catalog; existing Spoolman spools retain their copied local data. No automatic external-ID redirect. Packaging/tare and survivor identities are unchanged.

Exact decisions, retired IDs/keys, bindings, both-value conflicts, unresolved defaults and targeted identifiers: [review JSON](2026-10-04-elegoo-line-color-review.json).

```json
{
  "groups": 37,
  "approved_groups": 15,
  "retired": 15,
  "deferred": 22,
  "before_count": 51688,
  "after_count": 51673,
  "metadata_fields_changed": 0,
  "code_transfers": 0
}
```
