# Duplicate Filament Merge: Design

Date: 2026-10-03 · Related: Community issue #66 (Kingroon PETG duplicates)

Status: revised spec awaiting owner review. This revision authorizes no implementation, data retirement, push or GitHub comment.

## Problem

Commit `9b88f22` (2026-06-28, "enrich brand filament models and colors from Open Filament Database (OFD)") added families next to existing ones using a different naming style. Candidate overlaps include Bambu Lab `Matte Lemon Yellow` / `PLA Matte Lemon Yellow` and Kingroon `Kingroon PETG Black` / `PETG Black`.

A scan dated 2026-10-03 reported about 2,283 candidate groups across 72 brands, from 239 family pairings involving 405 families, with about 2,300 potentially redundant records. These are unconfirmed candidates, not approved retirements. A per-brand audit must establish the exact groups, record mappings and metadata conflicts before the owner approves a merge.

The current maintenance contract forbids public-ID removals. The owner has selected a limited exception for approved true duplicates, with a registry and validation that reject unrelated removals.

## Goals and boundaries

- Keep one compiled record for each confirmed duplicate physical variant.
- Record each retired public ID and its surviving replacement in an auditable contract.
- Preserve unique variants, survivor IDs and their existing weight/diameter/package combinations.
- Prevent unreviewed duplicate candidates from entering the catalog and document naming rules for new product lines.
- Add no filament schema fields.

Bulk manufacturer-prefix cleanup is out of scope. The separate scan of 1,172 prefix-bearing records does not authorize their renaming or retirement. Work stays in SpoolmanDB-Community; upstream data serves as read-only comparison evidence.

## 1. Retired-ID registry

### Breaking migration

The owner intends this as a **breaking migration** of the published `filaments.json`. Approved retired IDs disappear from that catalog. Existing Spoolman spools keep their local copy of imported filament data. Spoolman does not read `retired_ids.json`, redirect old catalog lookups or migrate stored external IDs. Other tools that look up a retired ID must use the mapping themselves.

We will publish no separate compatibility dataset or second catalog. The migration commit must state these consequences in the README or changelog and list the exact retired IDs. The exception to ID immutability covers only owner-approved registry entries; it does not permit unrelated renames, rekeys or deletions.

New contract file `contracts/retired_ids.json`, initially with an empty `retired` object:

```json
{
  "version": 1,
  "retired": {
    "<old_id>": {
      "replaced_by": "<surviving_id>",
      "reason": "duplicate",
      "ref": "#66",
      "source": "<evidence commit SHA or URL>"
    }
  }
}
```

`reason` has one allowed value, `duplicate`. Each entry requires a review reference in `ref` and a commit SHA or evidence URL in `source`. The brand audit preserves the before/after records and evidence needed to reproduce the decision.

`scripts/compile_id_baseline.py --strict` enforces these rules:

1. A historical baseline ID may be absent only when a valid registry entry records its approved retirement. Unregistered removals remain breaking errors. A new entry must refer to a historical record, not a fabricated ID.
2. `replaced_by` must name a surviving record in the current compiled data. The duplicate-color migration selects an existing survivor; it does not generate a replacement ID by renaming a unique record.
3. No chains, cycles or self-mappings. A replacement must not itself be retired. If a later migration retires a target, that same commit must re-point all affected entries to the final surviving target and validate those mappings.
4. A retired ID must not reappear in the compiled data during normal maintenance.
5. Retired and replacement records must match on manufacturer, material, weight, diameter, `spool_type`, `is_refill`, normalized color name and normalized product-line tokens. Black must not map to White. The checker compiles the retired source from the trusted base ref and compares it with the current replacement. It uses source definitions and the reviewed audit to identify the color and line. Some source styles put line words inside color labels; the audit must document that decomposition without dropping physical color words. An ambiguous decomposition does not authorize retirement. For an older retirement whose target changes, the checker must recover the original retired record from the retirement's Git history and retained audit evidence; the immediate base catalog no longer contains that ID.
6. Compare the registry with `--base-ref`. Entries are append-only; deletion or modification is an error. The sole normal-maintenance exception is changing `replaced_by` under rule 3. Preserve the original `reason`, `ref` and `source`, and record the re-pointing rationale and evidence in the new migration audit.

`--update` removes exactly the registered retired keys from the baseline without `--accept-breaking-baseline-changes`. It preserves surviving mappings and checks that the updated baseline matches the current compiled manifest. Unregistered removals remain breaking and cannot use the registry as a bypass; the existing explicit breaking flag is not part of this migration workflow.

The build workflow publishes `retired_ids.json` beside `filaments.json` on GitHub Pages. The registry records migration history; it provides no automatic compatibility behavior in Spoolman.

### Rollback decision before a data retirement

The current append-only and no-reappearance rules would reject a normal revert that restores retired records and removes their registry entries. This revision adds no rollback exception. The owner must approve a checked rollback rule before authorizing the first data-retirement apply. Until then, work may reach the no-data tooling stage and Kingroon dry-run review, but must not retire IDs. Do not solve this conflict with a force-push, history rewrite or unchecked breaking override.

## 2. Duplicate definition and merge rules

### Candidate detection and normalization

A duplicate candidate matches manufacturer, material, weight, diameter, `spool_type` and `is_refill`, and has the same normalized expanded name. The audit retains the source template and source color name for the separate color/line checks in registry rule 5. Candidates are audit warnings and review proposals, never evidence that a merge is valid. The owner confirms each group before apply; unresolved product identity remains a blocker.

Normalize names in this order:

1. Lowercase and normalize whitespace while keeping token order and repeated tokens.
2. Preserve line/version markers before tokenizing punctuation: `+`, `2.0`, `v2`, `cf`, `hf`, `hs`, `plus`, `pro`, `basic`, `high speed`, `rapid`, `matte`, `silk` and similar qualifiers.
3. Strip a leading manufacturer name on a token boundary, the standalone material token and bracket characters. Keep bracket contents. Do not delete other words or punctuation that carries line/version meaning.
4. Treat standalone `gray` and `grey` as the same word for comparison. Keep the original source spelling.
5. Compare ordered token sequences, not unordered sets. Do not infer equivalence between distinct line/version markers, such as `hf` and `hs` or `v2` and `2.0`.

PLA and PLA+ remain distinct, as do PETG and PETG Basic. Multi-color names with a different token order remain distinct. Apply color normalization without stripping manufacturer or material words from the color name.

### Confirmed non-duplicates

New contract file `contracts/not_duplicates.json`, initially empty:

```json
{
  "version": 1,
  "groups": {
    "<group-id>": {
      "ids": ["<first_id>", "<second_id>"],
      "reason": "<why these are different products>",
      "ref": "<human review reference>",
      "source": "<evidence commit SHA or URL>"
    }
  }
}
```

Derive a stable group ID from the sorted involved public IDs. Record the exact reviewed membership, reason and evidence. The auditor and CI guard skip only that confirmed group. A new member requires new review; manufacturer-wide or name-pattern exemptions are not allowed. This file does not authorize ID retirement.

### Survivor family

1. Prefer the family in Donkie/SpoolmanDB `upstream/main`, unless manufacturer evidence shows that upstream name is wrong. Record the resolved upstream commit and any evidence supporting the exception in the audit.
2. If upstream preference selects no single family, prefer the name without a manufacturer prefix.
3. Then prefer the name closest to the manufacturer's current product name.
4. If still tied, prefer the family with more records. A remaining tie requires the owner's selection.

Survivor preference proposes which existing IDs to keep. It does not prove that the two families describe the same product.

### Colors and package combinations

Retire only owner-confirmed duplicate color variants. Do not move unique colors into the survivor definition. Unique colors keep their source names and IDs, and a product line may retain multiple definitions.

Remove a source color only if all variants it generates have approved retirements. If only some weight/diameter/package combinations overlap, split the definition as needed to preserve the exact remaining combinations and IDs. Remove an empty definition only after accounting for every compiled record it generated.

The merge must create no new weight × diameter × color combinations. For this duplicate-only workflow, the final ID set must equal the starting ID set minus the approved retired IDs. Surviving and unique IDs remain unchanged; replacement IDs already exist.

### Metadata conflicts

Evidence from the **newest production lot** wins: a manufacturer label, TDS or product page tied to that lot, including a buyer-submitted manufacturer label. Evidence must describe the same family/SKU and packaging. Record the lot or revision and source used to establish recency. Do not use Git commit recency to choose values, average conflicting values or infer another family's specifications.

Keep the older values and their evidence in the audit report. Use the wording "manufacturer revised recommended values in newer lot" for changed recommendations; do not claim that the manufacturer changed the formula. Density and temperature corrections do not create new IDs.

If neither side has evidence, keep the survivor's value, record both values and mark the conflict unresolved. That metadata conflict does not block a merge whose product identity the owner has confirmed. Apply supplied evidence only to its matching variants; split source definitions if needed to avoid changing unrelated variants.

### Future product lines

Document these rules in `docs/maintenance.md` during implementation:

- New versions or lines, including `PETG 2.0`, `PETG Basic` and `Sunlu PETG v2`, remain separate families. Use the manufacturer's product name without a redundant manufacturer prefix; keep the old family.
- A pure rename of the same product uses `display_name` rather than a new family. Preserve the public ID, and obtain owner approval for any resulting baseline-key refresh. Duplicate-retirement approval does not authorize unrelated display-name changes.
- Do not merge different lines without SKU, label or TDS evidence and owner confirmation. Kingroon `PETG` and `PETG Basic` remain separate; the pilot leaves PETG Basic untouched.

## 3. Tooling and CI guard

- `scripts/audit_duplicates.py` reads catalog sources without modifying tracked data. It writes per-brand JSON and Markdown reports with candidate groups, upstream membership and commit, proposed survivors, exact retirement mappings, evidence and metadata conflicts.
- `scripts/merge_duplicates.py --brand <slug> [--exclude <group-id>]` runs in dry-run mode by default. `--apply` requires reviewed group decisions, removes only approved duplicate variants, applies supplied metadata evidence under section 2, appends registry entries and updates the baseline. Keep survivor values when no evidence is supplied and report the unresolved conflicts. No automatic application follows candidate discovery.
- `scripts/validate.py` compares groups with the trusted base. Existing candidates produce warnings. A newly introduced, unreviewed candidate group fails the change-review guard unless an exact human-confirmed non-duplicate entry exempts it. This failure requests review; it does not confirm a duplicate or authorize a merge.
- CI passes the resolved trusted base to both `validate.py` and `compile_id_baseline.py`. For a push to main, use `${{ github.event.before }}`. For an all-zero new-branch SHA, run the HEAD-only checks and report that no previous base exists. A nonzero base that cannot be fetched or resolved is an error, not a reason to fall back to HEAD-only. Existing contributor checks continue using their event's base SHA.
- Publish `retired_ids.json` with the catalog. Update `docs/maintenance.md` section 4 with the limited registered-retirement exception and naming rules, and document the breaking consequences in the README or changelog. Do not weaken protection for unrelated IDs.

Tests cover:

- Registry rules 1–6, including missing targets, self-mappings, cycles, stale IDs, cross-color/line mappings, registry edits and validated target re-pointing.
- Evidence and audit retention for an older retirement whose target changes.
- Registered retirement enrollment without the breaking flag, rejection of unregistered removals, and exact HEAD baseline synchronization.
- Ordered normalization: PLA versus PLA+, PETG versus PETG Basic, protected version tokens, multi-color order and repeated tokens.
- Merge preservation of unique colors, surviving IDs and partial package matrices, with no new Cartesian variants.
- A new-candidate CI failure, warnings for existing candidates, and exact `not_duplicates.json` exemptions that do not exempt new members.
- Push-to-main base selection, the all-zero fallback and failure on an unavailable nonzero base.

## 4. Rollout and stop gates

Follow the owner's no-PR maintenance workflow in `docs/maintenance.md` section 8. Use one focused local commit per step and later per approved brand. Do not create or push remote feature branches. Fast-forward local main only for an accepted delivery; push only when the owner authorizes it. Do not post GitHub comments or change issue status under this request.

1. **Spec revision:** commit only this document on `design/duplicate-merge`, self-review it and stop for owner approval. No implementation, registry files, baseline or filament changes.
2. **Tooling:** after spec approval, use TDD to implement the empty registries, scripts, CI checks and documentation, without data retirements. Run the full validation suite in maintenance section 7, make one focused local commit and stop with command results. Do not proceed to data apply or push.
3. **Kingroon pilot review:** after the preceding approvals, run the Kingroon audit and merge dry-run. Show the exact proposed mappings and conflicts. Expected candidates include `Kingroon PETG {Black,White,Grey}` versus `PETG {Black,White,Gray}` and the older PLA groups where confirmed duplicates. These expectations are not merge approvals. Leave PETG Basic untouched, touch no other brand and stop for owner approval before `--apply`.
4. **Accepted Kingroon delivery:** only after owner approval of the mappings and rollback rule, apply the selected changes, validate and commit. Fast-forward and push only under explicit owner delivery authorization; verify hosted checks and publication before cleanup. Closing issue #66 or posting a response requires separate authorization.
5. **Later brands:** after the Kingroon pilot succeeds, seek authorization for the next brand. Candidate group counts help set the order; they do not authorize merging all roughly 2,300 records. Use one focused commit per approved brand and the same audit, approval, validation and delivery gates.

Each report lists changed files, commands with pass/fail output, exact retired mappings, unresolved metadata, counts before/after and open decisions. Report intentional historical retirements as retirements, not as zero historical impact. Require zero unregistered removals, zero changed survivor/unique IDs and zero unintended new variants, and inspect the baseline delta against the immutable starting commit.
