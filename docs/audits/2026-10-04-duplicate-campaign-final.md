# Full-repository duplicate campaign — owner decision gate

Date: 2026-10-04. Community only; no PR, remote feature branch or GitHub comments.

## Exact campaign identity proof

Campaign base `b050e684b88a1622cd25ea5a47b6447c3e14d021`: **53,434 → 51,592** compiled records, **1,842 registered retirements**. No new IDs, changed survivor identity, rekeys, unregistered removals or dangling targets. Every retired key equals the original baseline key byte-for-byte; surviving keys remain unchanged. Phase C/D introduces no compiled payload changes.

These are intentional breaking catalog removals, not zero historical impact. Existing Spoolman spools retain local copied data; Spoolman does not consume the registry automatically.

## Current full-catalog audit

```json
{
  "sources": 490,
  "records": 51592,
  "candidates": 180,
  "not_duplicates": 0,
  "owner_pending": 180,
  "unresolved": 0
}
```

All **490** source files were enumerated. **180 groups in 28 brands remain owner-pending**, not resolved. [Single decision sheet](backlog-decisions.csv), [exact pending contract](../../contracts/owner_pending_duplicates.json), [original records, templates, conflicts and recommendations](2026-10-04-full-repo-owner-review.json). No clear distinct-product findings were guessed into not_duplicates.json.

Part A frozen114:45 retirements,69 deferred. PhaseB resolves64 further groups after exact evidence:ELEGOO22,FILATECH16,ERYONE5,Verbatim17,AmericanFilament4. Only9survivor IDs gain codes;206printing/document fields change. All other compiled data, unique code/EAN values and packaging/tare are preserved. Each brand has its own committed audit and full local gate evidence.

## Enforcement

Final local verification: **255 pytest tests passed**, 33 focused guard/audit regressions passed. Original-campaign baseline `--strict --base-ref b050e68` passes: 53,434 baseline records, 51,592 matched current, 1,842 registered retired, zero added/changed/rekeyed/unregistered removed. [Machine-readable audit and gate proof](2026-10-04-duplicate-enforcement-proof.json). PhaseB [Build](https://github.com/Icezaza2543/SpoolmanDB-Community/actions/runs/37194811978) and [CodeQL](https://github.com/Icezaza2543/SpoolmanDB-Community/actions/runs/37194811668) passed; Pages full payloads match51,592/1,842. Final guard delivery receives its own hosted checks before cleanup.

`validate.py` rejects **every** current unresolved group, existing or new. Exact not-duplicate memberships and exact temporary owner-sheet memberships are the only exemptions. Missing/mismatched/duplicate/incomplete sheets, new members, stale pending entries and overlapping contracts fail closed. `audit_duplicates.py --all` exits nonzero for unresolved candidates outside those lists. Baseline retirement/rollback checks remain intact.

Regression coverage includes existing/head-only failures, new-member failures, exact non-duplicate/pending passes, malformed/stale/overlap/CSV failures, and whole-repo enumeration. Red→green evidence retained in the local campaign gate logs. Full maintenance §7 plus original-campaign strict baseline and independent whole-payload proof are required before delivery.

Fresh-review finding fixed in one tested pass: a three-column sheet previously retained exemptions while losing review context. The guard now requires all 11 unique columns, exact cell counts and nonempty review values (evidence URL may remain empty). Four schema and seven blank-value regressions were observed RED, then GREEN. The full catalog remains unchanged. Enforcement covers the established candidate algorithm; it does not prove that every physically equivalent product worldwide is detectable.

## Registered retirements by manufacturer

|Manufacturer|Retired IDs|
|---|---:|
|22 Network|15|
|3DE|3|
|3DJAKE|27|
|ANYCUBIC|36|
|AURAPOL|16|
|Aceaddity|4|
|Alzament|1|
|AmazonBasics|3|
|American Filament|17|
|AzureFilm|77|
|Bambu Lab|124|
|Buddy3D|37|
|CHCKX|1|
|Conjure|1|
|Das Filament|52|
|Devil Design|115|
|ELEGOO|86|
|Eryone|7|
|Extrudr|29|
|Filatech|16|
|Fillamentum|120|
|GEEETECH|23|
|GST3D|4|
|Gizmo Dorks|65|
|IC3D|14|
|IEMAI|3|
|JAYO|6|
|Kingroon|5|
|LDO|11|
|Nebula|345|
|NinjaTek|20|
|Nobufil|5|
|Overture|82|
|Paramount 3D|115|
|Polar Filament|40|
|PolyTerra|1|
|Polymaker|8|
|Protopasta|45|
|Prusament|75|
|Push Plastic|29|
|QIDI Tech|8|
|Sakata 3D|28|
|Sunlu|47|
|TEQStone|6|
|Tecbears|12|
|VOXELPLA|3|
|Verbatim|22|
|Winkle|27|
|Zyltech|6|

## Owner follow-up

### Execution rulings and retained limitations

- Reused the active isolated branch and audit workspace. Frozen base SHAs disambiguate phases; the cost is bookkeeping in one workspace.
- Reviewers inspected complete gate logs instead of duplicating every suite. The cost is no second execution; final gates run again on the delivered tree.
- Reviewers did not independently reopen every manufacturer page. The executor reopened exact sources; the cost is no second provenance check and no claim of historical sales availability.
- Controlled synthetic binding tests are supplemented by exact vendor-ID/key audits. Unit fixtures alone do not attest physical products.
- The qualifier allowlist is bounded: galaxy, flexible, glitter, silk, matte, dual, metallic, rapid, plus, basic, hyper, fluorescent, glow, crystal, his, toms3d. Remaining ordered tokens must match; material/version tokens are not discarded. Valid unsupported qualifiers remain deferred.
- Unproven metadata/lot applicability and historical SKU fanout stay untouched. Documented legacy values may remain imperfect; identity safety is not a metadata-accuracy claim.
- Earlier batch reviews excluded unfinished later phases. The final full-repo audit/review covers those separately; batch approval alone is not campaign completion.
- The independent proof initially compared raw source order to the compiler's sorted array. Zero payload differences were found; verification now checks unique-ID payloads and exact compiler order. No data gate was weakened.
- Ignored campaign logs are retained for owner follow-up rather than deleted. The cost is local disk use; durable decisions/mappings are committed.
- Integration follows the owner's explicit main-only fast-forward/push decision instead of a new PR/menu. Mandatory post-push checks are verified before cleanup.

Deferred minor: older approved audit rows contain inherited “candidate-only” notes. Explicit approved decisions/mappings remain authoritative; this wording authorizes no additional identity or metadata change.

Resolve the180 rows with merge direction / not duplicate / unknown. No PhaseC group was applied. After accepted decisions, update the catalog/registry or exact not-duplicate evidence, remove corresponding pending memberships and update the sheet in the same change. Campaign closes only when pending is empty and the audit remains clean.

Future work only: OFD variants without sale evidence (Nebula2.85mm etc), brand-prefix display_name cleanup and pre-existing SKU fanout quality. No packaging/tare migration is included.
