# Changelog

User-visible history of the generic-tutor plugin, newest first. The reasoning behind each change lives in [`plugin/generic-tutor/DESIGN_NOTES.md`](plugin/generic-tutor/DESIGN_NOTES.md) (to be split into decision records, task D-01). Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); version = `plugin.json`.

## [Unreleased] — redesign programme (see `docs/PLAN.md`)
### Added
- **Evaluation harness** (`plugin/generic-tutor/evals/`, dev-only, excluded from the plugin build): five suites — `grading`, `safety`, `injection`, `diagnostics`, `gates` — run through the `claude` CLI (`python -m evals run --suite all --backend claude`) or offline sanity backends. Reference answers never need a human marker: they come from construction, deterministic oracles and openly licensed data (GSM8K, MIT). Baselines for sonnet are committed under `evals/results/`; `python -m evals check` compares a new run with them and fails on any rise in critical failures.
- `docs/adr/0001` (hooks are Claude Code-only), `docs/PEDAGOGY.md`, `CHANGELOG.md`.
- Planning docs: `docs/PLAN.md`, `docs/TASKS.md`, `docs/DATA_MODEL.md`, `docs/GLOSSARY.md`, `docs/PRIVACY.md`.
- `tools/lint_docs.py` (script references, command↔skill wiring, versions, links) with tests.
- CI: lint (ruff, mypy), docs-lint, Python 3.10/3.12/3.13 test matrix, deployed-copy drift check, `validate_courses.py` smoke test.
- `CLAUDE.md`, `CONTRIBUTING.md`, PR/issue templates, `SECURITY.md`, `NOTICE`, `pyproject.toml`, `.pre-commit-config.yaml`, Dependabot for Actions.
### Fixed
- `profile-kernel` documented the learner-progress schema incorrectly (numeric `confidence`, structured `error_patterns`, `item_mastery`, `remediation`, `session_slot_advanced_at` now correct).
- README claims about course validation, course count and a Releases page.
- Dead variables / unused imports found by ruff.
### Changed
- Private `vN` removed from four skill headings.

## [1.26.0] — 2026-10-05
### Added
- **Smarter review sessions** (`review_select.py`): due cards chosen and ordered by the script — most overdue first, then the items the learner knows least, then lowest ease — dealt round-robin across courses (interleaving), capped per session with the remainder reported. `/review [course] [stage]` can scope a session. The `review-scheduler` skill now calls it instead of "gather every due card".
- **Practice that targets weakness** (`next_items.py`): picks which syllabus items practice should exercise — weakest first (low mastery, unresolved errors, never-observed), ~70% from the current stage and ~30% from earlier stages, presented interleaved. `item_mastery` is now used to *select*, not only to pace. Wired into `course-runner`'s Practice step for itemised courses.
- **`/readiness <course>`** (`readiness.py`): an honest, bounded answer to "am I ready?" — a band (not enough evidence / early / building / solid), the strength of the evidence behind it, the weakest items, and caveats; never a grade, mark or percentage. Coverage gaps cap the band. Added to the `health-status` skill and `/help`.
- Tests for all three (`tests/test_learning_tools.py`) and golden CLI cases.

## [1.25.0] — 2026-10-04
### Changed
- **Every skill now opens with a Contract block** (Owns / Reads / Calls / Emits / Never / Failure modes) — the eight older skills gained one, written from what the scripts actually own. The docs lint fails if a skill lacks one, lacks a field, or names a script that doesn't exist.
- **Skill descriptions are checked**: at most 400 characters and they must name a `/command` (or say there is none); `course-auditor`'s (483 characters) was rewritten.
- **Commands validate their arguments in the prompt**: a missing id lists the valid choices instead of guessing (`/run`, `/add-profile`, `/continue`, `/drop`, `/restore`, `/add-course`, `/doctor`); ids must follow the identifier rule; `/erase` no longer advertises an unused argument.
### Added
- `docs/COMMANDS.md`, generated from the commands' front-matter by `tools/gen_commands_doc.py`; a test fails if it is stale.
- Context budget raised deliberately for the added contract/argument text (≈ +0.6–1.1 K chars per command).

## [1.24.0] — 2026-10-04
### Changed
- **Commands load far less context.** Command-specific sections of four big skills moved (verbatim — a line-by-line check found nothing lost) into reference files that only the commands needing them include: `course-runner/list-courses.md`, `journey-planner/drop.md`, `course-auditor/suspension.md`, `profile-kernel/intake.md` and `profile-kernel/profile-schema.md`. Approximate size of text loaded per command: `/list-courses` 30,496 → 1,672 chars (−95%), `/drop` 39,073 → 4,957 (−87%), `/run` 23,196 → 12,826 (−45%), `/profile` 23,294 → 22,632, `/audit`/`/add-profile` unchanged in substance. `/continue` (48,895) and `/add-course` (39,736) are untouched on purpose — see below.
### Added
- `tools/context_budget.py` measures each command's loaded text; `tools/context_budget.json` is a ratchet (CI fails if a command's context grows without a deliberate edit), with a test that pins the big reductions.
- Docs lint: reference files in skill folders must be included by a command or named in their `SKILL.md`; command includes of non-`SKILL.md` files must exist.

## [1.23.0] — 2026-10-04
### Added
- **One-step install**: `.claude-plugin/marketplace.json` makes the repository a plugin marketplace (`claude plugin marketplace add alwayslistening86-pixel/edu-course-library`, then `claude plugin install generic-tutor@edu-course-library` — both run successfully against this repo).
- `tools/build_plugin.py`: deterministic `generic-tutor-<version>.plugin` zip (sorted entries, fixed timestamps; excludes tests, caches); `tools/release_notes.py`; tag-driven `release.yml` workflow that checks tag = `plugin.json` version, requires a CHANGELOG section, runs the tests and attaches the zip to the GitHub release.
- CI job running `claude plugin validate --strict` on the plugin, its skills, its commands and the marketplace, plus a build-determinism check.
### Changed
- `plugin.json` now carries author, homepage, repository, license and keywords (the validator warned about missing author).
- The three docs that shipped skills and scripts refer to (`DATA_MODEL.md`, `PRIVACY.md`, `UNTRUSTED_CONTENT.md`) moved inside the plugin (`plugin/generic-tutor/docs/`) so references from skills resolve after install; skills now cite `${CLAUDE_PLUGIN_ROOT}/docs/…`.
- The docs lint also checks the marketplace entry's version.

## [1.22.0] — 2026-10-04
### Added
- **`/backup`** (`backup_profile.py`): full physical backup of a learner — profile, progress, decks, session ledger and a consistent copy of the history database (SQLite online-backup API) — with a manifest of sha256 checksums. Default location `<root>/backups/`, outside the learner folder; never overwrites an earlier backup.
- **`/restore`** (`restore_profile.py`): verifies the whole zip first (manifest, every checksum, no unlisted members, no `..`/absolute paths, format not newer than the plugin); refuses to touch an existing learner without `--replace`; with `--replace` takes a safety backup first and swaps the restored copy in atomically (the live folder is moved aside, so a failed swap is undone). `--dry-run` and `--user-id` (restore beside the original) supported.
- `backup-restore` skill (with contract block) and the two commands; `/help` updated.
### Fixed
- The desktop toolkit's `backup` defaulted to `<learner>/exports/` — inside the data it protects, so `/erase` (or losing the folder) destroyed the backups. It now defaults to `<root>/backups/`.

## [1.21.0] — 2026-10-04
### Security
- **Prompt-injection defence for web-derived content.** Specification pages, mark schemes and connector output are treated as data, never instructions: the compiler, the live recheck, the auditor and `tutor-core` now say so explicitly, `change.md` entries record facts and sources only, and a course file that appears to instruct the model is ignored and flagged for `/audit`. Policy: `docs/UNTRUSTED_CONTENT.md`.
- `scan_untrusted.py` / `tutorlib/untrusted.py` detect instruction-like text (override attempts, impersonation, system-prompt references, exfiltration requests, invisible characters = blocking; tool commands, hidden HTML comments, encoded blobs, role hijacks = advisory). `postcompile_gate.py` now **blocks shipping** a course with a blocking hit (documented override for reviewed false positives).
- **Learner text never reaches a shell argument**: `error_log.py append … @stdin` reads the note from stdin (quoted heredoc), and `course-runner` and `data-erasure` were rewritten accordingly (a quote or `$(…)` in a note could previously have run as a command).
### Added
- Tests: every attack class flagged, legitimate teaching text ("disregard unlawfully obtained evidence") not flagged, gate behaviour, hostile note/ids.

## [1.20.0] — 2026-10-04
### Added
- **`/doctor`** (`doctor.py`): read-only health check — Python version, data-root layout, deployed scripts, course structure, and per learner: schema + cross-file invariants, history DB, last-session completeness, stale locks, folder writability, consent in force. Each check carries a plain fix.
- **`/status`** (`status.py`): one-screen summary of a learner — session number, roster, per-course progress, reviews due, unresolved errors, and a suggested next command.
- **`/help`**: command list and usual flow; the docs lint now fails if a command is missing from it.
- New `health-status` skill (with contract block) for the two commands.

## [1.19.0] — 2026-10-04
### Added
- **Session ledger and verifier — closes the "model never called the script" gap.** Every state-changing script appends a line to `<learner>/.session_ledger.jsonl` (slot, script, action, course, stage, outcome; written under `granted`/`limited`, never `revoked`). `verify_session.py` checks a session's lines against "A implies B" rules (a stage pass needs a confidence update and review cards; a fail needs a confidence update and a remediation attempt; no duplicates; the slot was advanced). `/run` now audits the previous session and tells the learner about any gap — it reports and offers a repair, never back-fills a grade.
- `invariants.py`: cross-file consistency checks (schemas, ladder vs progress, linear order, deck stages, duplicate ids, slot regression).
- Fault-injection tests: 8 injected omissions/repeats, all detected (target ≥95%), and complete sessions produce no findings.
- `/export` includes the ledger.

## [1.18.0] — 2026-10-04
### Added
- **Data root resolved in code** (`tutorlib.paths.resolve_root`, `resolve_root.py`): `--root`, `$EDU_ROOT`, or the folder containing the deployed `.tutor-scripts/`; reports missing `courses/`, `profile/` or undeployed scripts with actionable messages. `profile-kernel` now calls it instead of resolving `/EDU/` by prose.
- **History DB versioning**: `tutor.sqlite3` is stamped with `PRAGMA user_version`; a DB from a newer plugin is refused (not modified); `sqlite_store.py check <learner_dir>` reports version, integrity and row counts.
### Fixed
- **Deployed scripts could silently drift**: at an unchanged plugin version a modified or missing deployed file was never restored. The bootstrap now compares against the bundle and repairs (`action: "repaired"`, with the drift listed).
- Upgrades now remove files and packages a previous deploy recorded but the new bundle no longer ships (never unknown files).

## [1.17.0] — 2026-10-04
### Added
- JSON Schemas for `student_profile`, `subjects`, `review_deck`, `course`, `curriculum_map`, `rubric` (`tutorlib/schemas/`), a stdlib validator (`tutorlib/schema.py`) and `validate_schema.py <kind> <file>`.
- `tests/test_schemas.py`: every fixture and every file the scripts write validates; known-bad shapes (string confidence, `passed` vs `pass`, unknown roster state) are rejected.
### Fixed
- State-writing scripts no longer rewrite a file written by a **newer** plugin version (`schema_version` above what they understand) — they stop with a clear "update the plugin" error and leave the file untouched.
- Malformed JSON, a non-object document or a lock timeout now produce `{"error": …}` with exit 1 instead of a Python traceback.
### Changed
- Six duplicated `_load` helpers replaced by `tutorlib/state.py`.

## [1.16.1] — 2026-10-04
### Changed
- Eligibility rules ("which roster states may be taught", "which hold a slot", "is a course grounding-suspended") now have one definition in `cohort_status.py` (`LIVE_STATES`, `SLOT_STATES`, `is_suspended`) used by `gate_check`, `roster_check` and `cohort_status`. No behaviour change; golden CLI snapshots unchanged. A test fails if a script re-derives the rule with its own literals.

## [1.16.0] — 2026-10-04
### Fixed
- Scripts disagreed about failure: `coverage_check.py`, `review_math.py apply` and `validate_structure.py` returned `{"error": …}` but exited 0, so a caller checking the exit status saw success. Convention is now uniform (0 success/decision, 1 failed with `error`, 2 usage), via `tutorlib/cli.py`.
### Added
- Golden-output tests for every script CLI (`tests/test_golden_cli.py`, `tests/golden/`); `docs/CLI_BASELINE.md`.

## [1.15.0] — 2026-10-04
### Fixed
- `/export` omitted the history database (`tutor.sqlite3`); it now includes every table. `/export` and `/erase` are performed by scripts (`export_profile.py`, `erase_profile.py`) instead of model-driven file handling.
- `/erase` referred to an undefined "confirmation token". The learner must now type exactly `ERASE <user_id>`; a dry run lists what will be deleted first.
### Added
- `tutorlib.ids` (identifier rules) and `tutorlib.paths` (symlink-safe path guards); `tests/test_erase_export.py`.
- Export bundle with `manifest.json` (format version, sha256 per file).

## [1.14.0] — 2026-10-04
### Fixed
- **Consent was only honoured by prose and one script.** `limited`/`revoked` consent is now enforced inside every state-writing script and the history database (progress and scheduling persist under `limited`; learner signals persist only under `granted`; nothing under `revoked`). Unreadable or unknown consent fails closed. Skipped writes return `written: false` with the computed values.
### Added
- `tutorlib/consent.py`; `tests/test_consent.py` (writer × consent-state matrix).

## [1.13.0] — 2026-10-04
### Fixed
- **Lost updates under concurrency.** Overlapping calls to the state-writing scripts could each read the same file and overwrite one another's change (12 parallel `error_log.py append` calls kept only 6–9 entries). Writers now hold a per-file lock for the whole read-modify-write.
- **Torn writes.** State files were written in place, so a crash mid-write could leave an unparseable file. All JSON state writes are now atomic (temp file + fsync + rename).
### Added
- `tutorlib` package (`atomic_io`, `filelock`) deployed alongside `toolkit` by the bootstrap; tests in `tests/test_tutorlib.py`.

## [1.12.0] — 2026-09-30
- Coverage exclusions are disclosed to the learner even when `coverage_status` is `full`.

## [1.11.0] — 2026-09-30
- Fixed the `passed`/`not_passed` bug; `record_stage_result.py` now owns `syllabus_status` and `current_stage` write-back.

## [1.10.0] — 2026-09-30
- `sqlite_store.py` wired in (per-learner `tutor.sqlite3` history). `confidence_update.py apply` and `review_math.py apply` perform the write themselves.

## [1.9.0] — 2026-09-30
- `uk-legal-mcp` / `govuk-mcp` added as opt-in suggested connectors.

## [1.8.0] — (not separately recorded; see DESIGN_NOTES)

## [1.7.0]
- Toolkit `export_anki.py`.

## [1.6.0]
- Optional read-only desktop toolkit (GUI + CLI): backup, health, progress, review-due, errors.

## [1.5.0]
- Per-item BKT mastery, rubric-criterion-tagged errors and review cards, blocking post-compile structural gate.

## [1.4.0]
- Adaptive teaching layer: diagnostic gate, error taxonomy and log, remediation state machine, confidence updates.

## [1.3.0]
- Standalone courses, prerequisites, practical stages by capability declaration, learner notices.

## [1.2.0]
- Whole-syllabus coverage as a checkable property (`coverage_check.py`, itemised curriculum maps).

## [1.1.x]
- Deterministic logic extracted from prose into scripts; bootstrap deployment; first test suite; fuzz suite; a series of review-driven fixes to level-lock, resume/reopen and roster messaging.

## [1.0.1] / [1.0.0] / [0.3.0]
- 1.0.1: cohort scoping fixed. 1.0.0: shared canonical courses, level-lock, roster cap, phase convergence, journey planner, review scheduler, stage recap, auditor, export/erase. 0.3.0: original upload.
