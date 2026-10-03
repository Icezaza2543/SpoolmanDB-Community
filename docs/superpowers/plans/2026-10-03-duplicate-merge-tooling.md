# Duplicate-merge tooling implementation plan

**Goal:** Implement STEP 2 without retiring any catalog data, on local `design/duplicate-merge`.

**Architecture:** Shared ordered normalization and catalog snapshots feed a registry checker, read-only auditor, explicit reviewed merge planner, and trusted-base CI guard. Registry identities come from stored keys, not recovered source history.

**Tech stack:** Python 3.11+, pytest, existing JSON compiler, Git, GitHub Actions. No new dependencies.

**Spec:** `docs/superpowers/specs/2026-10-03-duplicate-merge-design.md`, approved with amendments in `c30a727`.

## Global Constraints

- Empty retirement/non-duplicate registries; no changes to filaments or enrolled baseline.
- No push, PR, GitHub comment, main integration, Kingroon pilot, or other repository writes.
- Exact reinstatement alone permits registry deletion; stored retired keys are immutable.
- No automatic retirement based on normalization; apply requires exact owner-reviewed mappings.
- No new Cartesian variants; unique colors, survivor IDs and baseline keys stay intact.
- One focused tooling commit after all tasks and final review, not per-task commits.

## Review Focus

- Malformed registry or unavailable nonzero base must fail closed, never silently become empty.
- A reviewed decomposition must not drop color/line qualifiers or allow Black to map to White.
- Later re-pointing must preserve original keys/evidence and only flatten a newly retired target.
- Partial weight/diameter/package overlaps must preserve untouched records byte-for-byte in compiled output.
- Stale review files or incomplete multi-file apply must not silently authorize a changed catalog.

### Task 1: Registry and baseline enforcement

**Files:** `scripts/duplicate_catalog.py`, `scripts/retired_ids.py`, `scripts/compile_id_baseline.py`, `contracts/{retired_ids,not_duplicates}.json`, `tests/test_duplicate_registry.py`.

**Interfaces:** Produce `normalize_name(name, manufacturer='', material='', color=False) -> tuple[str,...]`; `identity_from_key(key, binding=None) -> dict`; `check_registry(head, base, base_manifest, current_manifest, head_manifest, audits=None) -> (errors, retired_ids, reinstated_ids)`. Baseline checker accepts optional registry payloads/files and reviewed audit bindings.

1. Write synthetic real-compiler tests for rules 1–6, stale IDs, wrong keys, cross-color/line mappings, later re-pointing, malformed input, exact reinstatement and its two rejection cases, safe enrollment and unregistered removal.
2. Run `python -m pytest tests/test_duplicate_registry.py -q`. Expected: failures for missing registry enforcement/API.
3. Implement strict registry validation and integrate both current-source and trusted-baseline removal checks. Update uses a prospective enrolled manifest but final strict checks require the actual HEAD baseline.
4. Run the same test command. Expected: all pass; existing baseline tests remain green.

### Task 2: Candidate audit and reviewed merge planner

**Files:** `scripts/audit_duplicates.py`, `scripts/merge_duplicates.py`, `tests/test_duplicate_tools.py`.

**Interfaces:** Consume Task 1 identities. Produce `catalog_records(root, ref=None) -> list[dict]`, `candidate_groups(records) -> dict`, `audit_brand(root, brand, upstream_ref=None) -> dict`, `plan_merge(root, brand, review, exclude=()) -> dict`, `apply_plan(root, plan) -> None`.

1. Write tests for ordered protected tokens, exact non-duplicate memberships, read-only audit, pinned upstream membership/survivor preference, metadata conflicts, dry-run default, owner approval/evidence gates, stale reviews, unique colors and partial package matrices, metadata changes confined to supplied evidence variants, and transactional apply failure.
2. Run `python -m pytest tests/test_duplicate_tools.py -q`. Expected: failures for missing tooling.
3. Implement snapshots with source locations, deterministic groups, JSON/Markdown reports, and explicit reviewed mappings. Apply splits source definitions rather than moving colors and checks the exact ID/key delta before writing.
4. Run the same command. Expected: all pass. Run Task 1 tests again.

### Task 3: Trusted-base duplicate guard and CI integration

**Files:** `scripts/ci_base_ref.py`, `scripts/validate.py`, `.github/workflows/build.yml`, `tests/test_duplicate_guard.py`.

**Interfaces:** Consume catalog groups. Produce `check_duplicate_candidates(root, base_ref=None) -> (errors,warnings)` and `resolve_base(event, before='', pr_base='', root=ROOT) -> str|None`.

1. Write real temporary-Git tests for new group failure, existing warning, exact exemptions/new-member rejection, push/PR base selection, all-zero HEAD-only fallback, unavailable nonzero base, and malformed contracts.
2. Run `python -m pytest tests/test_duplicate_guard.py -q`. Expected: failures for missing guard/base resolver.
3. Wire validation and one shared CI base-selection step into both gates. Publish the registry alongside the catalog; retain existing contributor base behavior.
4. Run the same command. Expected: all pass.

### Task 4: Documentation, full verification and final review

**Files:** `docs/maintenance.md`, `README.md`; no generated catalog or baseline changes.

1. Document limited owner-approved breaking retirements, exact reinstatement, naming/version and newest-lot rules, reviewed audit format and CLI usage.
2. Run every command in maintenance §7 with the immutable starting main `b050e684b88a1622cd25ea5a47b6447c3e14d021`. Expected: all required gates pass; inspect canary output.
3. Verify original/final compiled manifest and records, baseline bytes, empty registries and main refs. Expected: 53,434 before/after; retired/new/changed/rekeyed IDs all zero.
4. Obtain one fresh read-only whole-change reviewer. Address important findings with RED→GREEN tests and repeat the full suite.
5. Commit exactly once: `feat: add reviewed duplicate migration tooling`. Leave local design branch intact and stop; no push or brand audit/apply.
