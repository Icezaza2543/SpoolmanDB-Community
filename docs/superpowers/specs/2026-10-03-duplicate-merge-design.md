# Duplicate Filament Merge: Design

Date: 2026-10-03 · Related: Community issue #66 (Kingroon PETG duplicates)

Status: implemented and owner-authorized campaign delivered through 2026-10-04. The original staged approvals below are historical rollout notes, superseded by the owner's continuous A–D authorization. Registered retirements and per-brand evidence are published; full-catalog enforcement is active with exact temporary owner-pending exemptions. Closed 2026-10-05: all owner-sheet decisions are applied, owner-pending is empty, and the whole-catalog audit reports 0 unresolved groups; see [the campaign closure](../../audits/2026-10-04-duplicate-campaign-final.md#closure-2026-10-05). No GitHub comments are authorized.

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
      "source": "<evidence commit SHA or URL>",
      "retired_key": "<exact original baseline key>"
    }
  }
}
```

`reason` has one allowed value, `duplicate`. Each entry requires a review reference in `ref`, a commit SHA or evidence URL in `source`, and the retired record's original baseline key in `retired_key`. Store that key byte-for-byte. The brand audit preserves the before/after records and evidence needed to reproduce the decision.

`scripts/compile_id_baseline.py --strict` enforces these rules:

1. A historical baseline ID may be absent only when a valid registry entry records its approved retirement. Unregistered removals remain breaking errors. A new entry must refer to a historical record, not a fabricated ID.
2. `replaced_by` must name a surviving record in the current compiled data. The duplicate-color migration selects an existing survivor; it does not generate a replacement ID by renaming a unique record.
3. No chains, cycles or self-mappings. A replacement must not itself be retired. If a later migration retires a target, that same commit must re-point all affected entries to the final surviving target and validate those mappings.
4. A retired ID must not reappear in the compiled data, except through exact reinstatement under the rollback rule below.
5. Retired and replacement records must match on manufacturer, material, weight, diameter, `spool_type`, `is_refill`, normalized color name and normalized product-line tokens. Black must not map to White. The checker reads the retired identity from `retired_key`, plus the reviewed audit, and compares it with the current replacement. It does not recover the retired identity from Git history. A newly registered key must match the trusted base's mapping to the retired ID. Some source styles put line words inside color labels; the audit must document that decomposition without dropping physical color words. An ambiguous decomposition does not authorize retirement.
6. Compare the registry with `--base-ref`. Entries are append-only except for rule 3 target re-pointing and exact reinstatement. Other deletions or modifications are errors. A re-pointing preserves the original `reason`, `ref`, `source` and `retired_key`, with its rationale and evidence in the new migration audit.

`--update` removes exactly the registered retired keys from the baseline without `--accept-breaking-baseline-changes`. It preserves surviving mappings and checks that the updated baseline matches the current compiled manifest. Unregistered removals remain breaking and cannot use the registry as a bypass; the existing explicit breaking flag is not part of this migration workflow.

The build workflow publishes `retired_ids.json` beside `filaments.json` on GitHub Pages. The registry records migration history; it provides no automatic compatibility behavior in Spoolman.

### Rollback: exact reinstatement only

A migration may delete a registry entry only if the same commit restores that retired ID in compiled data with a baseline key byte-identical to the entry's `retired_key`, and re-enrolls that exact key-to-ID mapping in the baseline. Reinstatement with a different key, deletion without reinstatement, or any other registry modification is an error, apart from rule 3 target re-pointing.

Use a normal commit or revert commit for an exact reinstatement. The checker validates the source, baseline and registry together against the trusted base. Do not force-push, rewrite history or use an unchecked breaking override. Exact reinstatement is the sole exception to rule 4's no-reappearance requirement.

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

Evidence from the **newest production lot** wins for package-specific metadata, including buyer-submitted manufacturer labels. Packaging, spool material and tare require the same family/SKU and packaging/lot binding. Current official TDS/product pages are valid evidence for density/nozzle/bed of the exact product line without separate lot binding. Record the revision/current source. Do not use Git commit recency to choose values, average conflicting values or infer another family's specifications.

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
- `scripts/validate.py` fails on every unresolved current candidate, existing or new. Only exact memberships in `not_duplicates.json` or the temporary `owner_pending_duplicates.json` may be exempt. Pending memberships must match the single owner sheet and current catalog; stale, mismatched or overlapping entries fail closed. A new member requires review. `audit_duplicates.py --all` reports zero unresolved outside those exact lists; final campaign closure also requires an empty pending list. A failure requests review, not automatic retirement.
- CI passes the resolved trusted base to both `validate.py` and `compile_id_baseline.py`. For a push to main, use `${{ github.event.before }}`. For an all-zero new-branch SHA, run the HEAD-only checks and report that no previous base exists. A nonzero base that cannot be fetched or resolved is an error, not a reason to fall back to HEAD-only. Existing contributor checks continue using their event's base SHA.
- Publish `retired_ids.json` with the catalog. Update `docs/maintenance.md` section 4 with the limited registered-retirement exception and naming rules, and document the breaking consequences in the README or changelog. Do not weaken protection for unrelated IDs.

Tests cover:

- Registry rules 1–6, including missing targets, self-mappings, cycles, stale IDs, cross-color/line mappings, registry edits and validated target re-pointing.
- Retired identity checks from the stored `retired_key`, including a later target change without Git-history recovery.
- Exact reinstatement passes; reinstatement with a different key fails; registry deletion without reinstatement fails.
- Registered retirement enrollment without the breaking flag, rejection of unregistered removals, and exact HEAD baseline synchronization.
- Ordered normalization: PLA versus PLA+, PETG versus PETG Basic, protected version tokens, multi-color order and repeated tokens.
- Merge preservation of unique colors, surviving IDs and partial package matrices, with no new Cartesian variants.
- Existing/new candidate failures, exact non-duplicate and owner-sheet exemptions, and rejection of added members, stale/malformed memberships, missing/mismatched sheets and overlapping contracts.
- Push-to-main base selection, the all-zero fallback and failure on an unavailable nonzero base.

## 4. Rollout and stop gates

Follow the owner's no-PR maintenance workflow in `docs/maintenance.md` section 8. Use one focused local commit per step and later per approved brand. Do not create or push remote feature branches. Fast-forward local main only for an accepted delivery; push only when the owner authorizes it. Do not post GitHub comments or change issue status under this request.

1. **Spec revision:** apply the two owner-approved amendments, self-review and commit this document on `design/duplicate-merge`. The owner has authorized proceeding to STEP 2 after that commit. No registry, baseline or filament changes belong in the spec commit.
2. **Tooling:** after spec approval, use TDD to implement the empty registries, scripts, CI checks and documentation, without data retirements. Run the full validation suite in maintenance section 7, make one focused local commit and stop with command results. Do not proceed to data apply or push.
3. **Kingroon pilot review:** after the preceding approvals, run the Kingroon audit and merge dry-run. Show the exact proposed mappings and conflicts. Expected candidates include `Kingroon PETG {Black,White,Grey}` versus `PETG {Black,White,Gray}` and the older PLA groups where confirmed duplicates. These expectations are not merge approvals. Leave PETG Basic untouched, touch no other brand and stop for owner approval before `--apply`.
4. **Accepted Kingroon delivery:** only after owner approval of the mappings, apply the selected changes, validate and commit under the exact-reinstatement rule. Fast-forward and push only under explicit owner delivery authorization; verify hosted checks and publication before cleanup. Closing issue #66 or posting a response requires separate authorization.
5. **Later brands:** after the Kingroon pilot succeeds, seek authorization for the next brand. Candidate group counts help set the order; they do not authorize merging all roughly 2,300 records. Use one focused commit per approved brand and the same audit, approval, validation and delivery gates.

Each report lists changed files, commands with pass/fail output, exact retired mappings, unresolved metadata, counts before/after and open decisions. Report intentional historical retirements as retirements, not as zero historical impact. Require zero unregistered removals, zero changed survivor/unique IDs and zero unintended new variants, and inspect the baseline delta against the immutable starting commit.
