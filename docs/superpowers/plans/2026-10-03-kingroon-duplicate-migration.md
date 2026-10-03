# Kingroon Duplicate Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans. The owner explicitly authorized immediate local execution of STEP 4.

**Goal:** Retire only the five owner-approved Kingroon duplicate IDs, preserve every survivor's metadata, validate and make one local commit.

**Architecture:** The existing reviewed merge CLI consumes the pinned STEP 3 audit and exact owner decisions. It updates Kingroon source, retirement registry and baseline together; documentation retains the unresolved evidence and breaking consequences.

**Tech Stack:** Existing Python compiler/merge tooling, pytest, Node display-name tests and Git.

**Spec:** `docs/superpowers/specs/2026-10-03-duplicate-merge-design.md`, STEP 4, supplemented by the owner's G1-G5 approval on 2026-10-03.

## Global Constraints

- Work on existing local `design/duplicate-merge`, starting at `3db1f4550d55995c34db4fd147a7f5c6a31a987b`.
- Trusted starting main: `b050e684b88a1622cd25ea5a47b6447c3e14d021`; do not move main or origin/main.
- No push, GitHub writes, other-brand changes, schema/compiler/test/workflow edits or unreviewed retirements.
- Exactly 53,434 -> 53,429 records; five registered retirements, zero new/changed/rekeyed identities.
- Keep all survivor metadata. Record G1/G4 density/nozzle and G5 HEX conflicts as unresolved.
- Preserve PETG Basic's ten records and unique prefixed PLA Grey/Red/Blue byte-for-byte in compiled output.
- Registry entries use reason `duplicate`, ref `#66`, source equal to the audited commit SHA, and exact original baseline keys.
- One focused final commit with `Closes #66`; no integration or delivery.

## Review Focus

- Exact removal set, baseline keys and registry mappings match the approved groups.
- No metadata change, family collapse or Cartesian expansion, including refill variants.
- Conflict evidence is retained without claiming an unbound PLA Basic page proves newer-lot metadata.
- Breaking catalog lookup behavior and absence of automatic Spoolman redirect are documented.
- Only Kingroon, its contracts, audit and documentation change; main stays untouched.

### Task 1: Apply, validate and commit the approved Kingroon migration

**Files:** `docs/audits/2026-10-03-kingroon-duplicate-review.json`, `filaments/kingroon.json`, `contracts/retired_ids.json`, `contracts/compiled_id_baseline.json`, `README.md`, this focused plan.

**Interfaces:** Consume `merge_duplicates.py --brand kingroon --review FILE --apply`; produce the exact five retirement mappings and unchanged surviving compiled records.

- [ ] Verify clean branch, original count/baseline and audit digest. Expected: HEAD 3db1f45, 53,434 records, empty registry.
- [ ] Write approved decisions with original audit snapshot and unresolved conflicts. No metadata updates.
- [ ] Run a pre-apply invariant assertion against the intended after state. Expected: FAIL because the five IDs still exist.
- [ ] Run reviewed merge dry-run, inspect exact changes, then run `--apply`. Expected: only Kingroon source and the two contracts change, 53,429 records and five retirements.
- [ ] Document the breaking migration and all five old-to-survivor mappings in README; regenerate snapshot.
- [ ] Run maintenance section 7 in full, including trusted-base strict baseline check against b050e68. Inspect actual canary drift. The pre-commit no-base tests use the committed registry and fail closed during this first retirement; immutable-base checks must pass before commit, and the full suite must be rerun on actual committed state afterward.
- [ ] Compare original/final full compiled records and manifests. Expected: exactly the five approved IDs removed, all surviving records/keys unchanged, no new IDs; PETG Basic and unique PLA preserved.
- [ ] Obtain one read-only fresh review and resolve important findings within this scope.
- [ ] Commit once: `data: retire approved Kingroon duplicates`, body `Closes #66`. Verify clean design branch and unchanged main/origin/main, then stop.
