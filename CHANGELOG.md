# Changelog

User-visible history of the generic-tutor plugin, newest first. The reasoning behind each change lives in [`plugin/generic-tutor/DESIGN_NOTES.md`](plugin/generic-tutor/DESIGN_NOTES.md) (to be split into decision records, task D-01). Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); version = `plugin.json`.

## [Unreleased] — redesign programme (see `docs/PLAN.md`)
### Added
- **Evaluation harness** (`plugin/generic-tutor/evals/`, dev-only, excluded from the plugin build): six suites — `grading`, `criteria`, `safety`, `injection`, `diagnostics`, `gates` — run through the `claude` CLI (`python -m evals run --suite all --backend claude`) or offline sanity backends. Reference answers never need a human marker: they come from construction, deterministic oracles and openly licensed data (GSM8K, MIT). Baselines for sonnet are committed under `evals/results/`; `python -m evals check` compares a new run with them and fails on any rise in critical failures.
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

## [1.64.0] — 2026-10-06
### Changed
- S-05, K-21: schemas for access.json and the deployed manifest (confirm_access now writes through state.save), plus a schema for plan_estimate output that /plan quotes from

## [1.63.0] — 2026-10-06

Why: the plan is to enrich courses after the build through `/audit`, but the auditor only reported missing misconceptions and could not make a bank. A pilot on `gcse_psychology` found the second problem: the sandbox's egress proxy blocks `aqa.org.uk` and `filestore.aqa.org.uk` (WebSearch works, WebFetch does not), so examiner-report passages cannot be read here and a "documented" misconception would have to rest on a search summary. The skill now says to write `plausible, not board-documented` or omit in that case. What does not need the web: 62 of 62 courses have an `exam/exam.md`, and over the library 369 ready-made items carry answer keys. `exam_to_bank.py` converts the 286 that convert cleanly (mark points, levels guides, multiple choice) and lists the other 83 with reasons (65 code-output items, 16 whose scheme is free prose, 2 that are instructions to the tutor); 30 courses have no ready-made items at all and need items authored. Not eval-measured: no suite covers the audit, so this is untested against a model run.
### Changed
- Audit enrichment tier: enrich_plan.py (what each course lacks, where to look) and exam_to_bank.py (starter question bank from a course's own exam/exam.md, no invented content); the auditor skill gains the pass, with a rule against claiming sources it could not read

## [1.62.0] — 2026-10-06
### Changed
- C-15: command argument hints use one convention (snake_case placeholders, --kebab flags); /audit and /list-courses declare theirs; a test holds it

## [1.61.0] — 2026-10-06
### Changed
- C-04: /drop previews its consequence (roster_apply drop --preview) before the confirmed drop

## [1.60.0] — 2026-10-06
### Changed
- `/audit` takes `--report-only`, `--course <id>` and `--tier N`; `audit_run.py --course` scopes the deterministic report to one course (C-12)

## [1.59.0] — 2026-10-06
### Changed
- `/list-courses` is a script (`list_courses.py`) with filters `--status`, `--level`, `--standalone`, `--compact`; the model presents its rows instead of rebuilding the list from files (C-14)

## [1.58.0] — 2026-10-06
### Changed
- one spelling in skill prose (enrol / enrolment; 27 US spellings changed, script names untouched), an Enrolment entry in the glossary, and a lint that flags the US form (K-34)

## [1.57.0] — 2026-10-06
### Changed
- profile intake is specified as a question-to-key table with valid values and one `profile_init.py` call; the duplicated profile JSON blocks in profile-kernel are replaced by pointers to the schemas (K-16, K-17)

## [1.56.0] — 2026-10-06
### Changed
- `course-compiler`: a decision table for optional components, tiers and multiple awarding bodies (K-11) and one explicit copyright policy for every course file (K-12)

## [1.55.0] — 2026-10-05
### Changed
- release-history prose removed from skills ('(v1.3.0)' tags, DESIGN_NOTES pointers); the docs lint now flags it (K-35)

## [1.54.0] — 2026-10-05
### Changed
- `audit_run.py`: the whole deterministic audit as one JSON report (structure, schema, injection and test-integrity, rubric wording, change.md shape, audit status) with a diff against the previous report; `course-auditor` Tier 1 is now a table that starts from it (K-13, K-14)

## [1.53.0] — 2026-10-05
### Changed
- live recheck is bounded (4 pages, issuing-body domains only) and defines 'material change' (version/issue, graded criteria or threshold, items added/removed/moved); new `recheck` eval, 14 constructed cases, 14/14 on sonnet — an easy set (K-08)

## [1.52.0] — 2026-10-05
### Changed
- `course-runner` opens with a numbered session lifecycle (the script call at each step) and says how to resume a session cut off mid-test or mid-diagnostic; the gates eval is unchanged at 1.0 (K-06, K-07)

## [1.51.0] — 2026-10-05
### Changed
- `tutor-core` gives each phase a 'done when' criterion (lesson, practice, test); eval A/B at 6 samples shows no measurable change (K-01, K-02)

## [1.50.0] — 2026-10-05
### Changed
- toolkit uses the plugin's root resolver and accepts `--root <folder>` (E-23, partial: the GUI's error surfacing is untested here)

## [1.49.0] — 2026-10-05
### Changed
- `migrate_schema.py` reports `valid_after` (and the first schema errors) for the file it migrated, so a migration that leaves a file structurally wrong says so (S-09)

## [1.48.0] — 2026-10-05
### Changed
- every state writer validates before it writes: a change that would add a schema error the file did not already have is refused (legacy quirks present at load never block a session) (E-20)

## [1.47.0] — 2026-10-05
### Changed
- `validate_schema.py --course-dir` checks every schema-covered file of a course in one call (all 186 files of the 62 real courses pass); `course-auditor` uses it and `invariants.py` instead of prose checks (S-08)

## [1.46.0] — 2026-10-05
### Changed
- `change_log.py` reads a course's change.md as data (entries, dates, labels) and the compile gate notes malformed ones; format written into CONTENT_CONTRACT (S-11)

## [1.45.2] — 2026-10-05
### Fixed
- JSON state files are now always written with LF line endings. On Windows they were written with CRLF, so the same data had different bytes (and checksums) on different machines. Windows CI went from 30 failing tests to 6 and the remaining ones were path quoting and these line endings.

## [1.45.1] — 2026-10-05
### Fixed
- Found by the first CI runs (Linux 3.10/3.12/3.13 green; a mypy error in `purge_history.py`; 30 failures on Windows). Reported file paths in script output (injection-scan findings, erase inventory, purge plan) now always use `/`, so messages and snapshots are identical on every platform. Windows-only test assumptions (POSIX root paths, golden snapshots, symlink creation) corrected. CI now also runs on every branch push and has an informational Windows job.

## [1.45.0] — 2026-10-05
### Fixed
- Windows robustness (the maintainer's deployment is Windows): text piped to a script (session notes, review cards, worksheets, intake answers, error notes) is now decoded as UTF-8 regardless of the console code page, so £, accents and dashes survive; `--help` no longer crashes on a console that cannot show a character; and every atomic write (progress files, backups, exports, dashboard, restore swap) retries briefly when a sync client or antivirus holds the destination, instead of failing the save. Verified here only by simulating a legacy code page and a locked file; not run on Windows.

## [1.44.0] — 2026-10-05
### Fixed
- **History database lost events across courses.** `error_events` and `review_cards` were keyed by `id` alone, and ids repeat between courses (`err_<date>_<stage>_001`, a card `S1-c1`), so one course's event or card silently replaced another's and `resolve` could close the other course's errors. History schema v2 keys them by `(course_id, id)` and adds `course_id` to `review_log`; existing databases migrate in place on first use. Events already overwritten under v1 cannot be recovered.
### Added
- `purge_history.py`: selective deletion short of `/erase` — `history` (analytics database and write ledger only) or one `course` (its enrolment, deck, history rows and ledger lines), each behind a typed `PURGE …` phrase and a dry run first. (X-05)

## [1.43.0] — 2026-10-05
### Added
- `rubric_lint.py` (A-11): advisory wording lint for rubric criteria (too few/many, too short, vague "understands" wording, duplicates, missing pass threshold or source locator, stages whose criteria are all topic labels). `postcompile_gate` notes label-only stages. On the real library: 50 of 1,253 stages have only label-like criteria.

## [1.42.0] — 2026-10-05
### Added
- `enrol.py`: the one way a progress file is created. Both `/add-course` paths and `course-runner`'s defensive create call it (cohort from the course, all stages `unsat`, practical stages `withheld` without the capability, schema-validated, refuses a duplicate or a full roster). The lifecycle fuzz enrols through it.

## [1.41.0] — 2026-10-05
### Added
- `roster_apply.py drop|advance|lock`: the roster and level-ledger edits the skills used to describe as hand edits (set a course `dropped` and wake what it unblocked; raise `highest_level_cleared` and wake what that unlocks; mark courses `dormant` when a new or resumed course locks them) are now one locked, ledgered, consent-aware script that takes its decisions from `roster_check` / `cohort_status`. `journey-planner`, `/drop`, and `course-compiler` call it, and the lifecycle fuzz now drives it (1,000 random sequences, 0 invariant violations). (K-19)

## [1.40.0] — 2026-10-05
### Added
- `confirm_access.py`: records the one-time "isolated or shared folder?" answer in `<folder>/access.json`. `gate_check.py` gate 1 now accepts a confirmed `courses/access.json` for every course, so a library whose courses ship as `pending_confirmation` (54 of the 62 real ones) asks once instead of once per course. A course's own confirmed status still counts; garbage or unconfirmed files never unlock.

## [1.39.2] — 2026-10-05
### Changed
- Release-named test files renamed by topic (no test changed). Hash-seed stability of the golden snapshots checked (E-19).

## [1.39.1] — 2026-10-05
### Changed
- `postcompile_gate` reports misconceptions coverage as one line ("0 of 29 stages …") instead of dumping a per-stage structure, which made the output of the real 29-stage courses unreadable.

## [1.39.0] — 2026-10-05
### Added
- Test-integrity checks (`tutorlib/overlap.py`): `postcompile_gate` blocks shipping a course whose stage test items appear word for word in that stage's practice or lesson, and notes shared 20-word runs; `worksheet_check.py` lets `stage-recap` verify a take-home worksheet does not reproduce the test. Verified clean on all 1,253 real stages. (A-07, K-26)

## [1.38.0] — 2026-10-05
### Added
- `/status audit` (`recent_activity.py`): the learner's write ledger as plain sentences — what the tutor saved, in which session, and what was NOT saved because of consent. Only ids and numbers are logged, never answers or messages. (V-10)
- `tools/scan_repo.py` (credentials, e-mail addresses, private-content paths in tracked files), `tools/tasks_status.py` (TASKS.md counts derived, checked in CI), `docs/INSTALL.md`.

## [1.37.0] — 2026-10-05
### Added
- `practice_pick.py next|used`: tracks which written practice items a learner has met (`practice_used` in the progress file, optional, no migration) and says `use_fixed:<n>` or `generate_new`, so a repeated stage or a retry after a failed test no longer replays the same prompts. Real stages hold only 1–5 written items (`docs/CONTENT_SURVEY.md`). `course-runner` calls it. (L-13)

## [1.36.0] — 2026-10-05
### Added
- `tutor-core`: hint ladder (nudge → cue → one worked step → full solution only on request; none in a test) and criterion-referenced, next-action feedback. New `hints` eval suite measures it by code: before the rules 6 of 54 early-turn replies stated the final answer (91.7 % of samples acceptable, 6 of 24 cases ambiguous); after, 0 of 54 (100 %, none ambiguous). 72 samples per run, sonnet, six problems: an easy set, so read it as "no longer leaks", not "teaches well". (L-16)

## [1.35.1] — 2026-10-05
### Fixed
- Found by running the engine over the real course library (`docs/CONTENT_SURVEY.md`): the injection scanner blocked a legitimate GCSE English lesson (*post* used as a noun), reported the shipped stage-test script call 1,262 times, and `course.json` rejected a course-wide notice with `stages: null`. All 62 real courses now validate.

## [1.35.0] — 2026-10-05
### Added
- `audit_status.py`: the "audit recommended" check as a read-only script (old schema, never audited, audited under an earlier major.minor, never live-rechecked); `course-auditor` calls it. (K-15)

## [1.34.0] — 2026-10-05
### Added
- `deck_add.py`: new review cards enter the deck only through it (quality limits, duplicate skip, per-stage and deck caps, standard scheduling defaults, consent-aware); `stage-recap` calls it instead of hand-editing the deck. (K-22, K-23, K-25)

## [1.33.0] — 2026-10-05
### Added
- `history_report.py mastery|ease|errors`: read-only canned reports over the learner's history database (mastery trend per item, ease drift per card, recurring errors by stage/item/cause); `course-auditor` points to it. (E-16)

## [1.32.0] — 2026-10-05
### Added
- `--envelope` on every script: `{ok, data, warnings, error{code,message}}` with a closed set of error codes (`docs/CLI_BASELINE.md`). Default output unchanged. (E-10, E-11)

## [1.31.0] — 2026-10-05
### Added
- Every script answers `--help` / `-h` with plain-text usage and exit 0 (E-09, `tutorlib.cli.handle_help`); a test covers all scripts.

## [1.30.1] — 2026-10-05
### Fixed
- Replaying a pass for an earlier stage (a repeated or re-ordered call) moved `current_stage` backwards; it now never does.
### Added
- Repeat-call behaviour of every state writer documented (`DATA_MODEL.md`) and pinned by `tests/test_idempotency.py` (E-13).

## [1.30.0] — 2026-10-05
### Added
- `session_state.py` (`phase|roster|exam|notice|note`): the last hand-written progress fields (`current_phase`, live `roster_state`, `exam_status`, `notices_acknowledged`, `last_session_summary`) now have a script owner; `course-runner` calls it.
### Fixed
- A passed stage never returned a course from `test_pending_convergence` to `active`, so the course counted as already "ready to test" for its next stage and cohort convergence could be satisfied without it. `record_stage_result.py apply` now resets it on a pass (a fail keeps the wait).

## [1.29.0] — 2026-10-05
### Added
- **Accessibility modes with concrete rules** (`tutor-core`): `dyslexia_mode` (short sentences, at most three sentences per block incl. list items and examples, numbered steps, bold only for the key term, no italics/ALL CAPS, chunking) and `plain_language_mode` (everyday words, every technical term explained at first use, concrete example first). They change wording only, never content or marking standard. Measured with a new deterministic `accessibility` eval (replies are scored by code, no marker): on mode cases, compliant replies rose 18 → 25 of 36 samples; italics, missing steps and unexplained terms mostly disappeared; over-long blocks did not change.
- **`/mock <course>`** — exam simulation: `assemble_paper.py` builds a timed-style paper from an optional per-course `question_bank.json` (new schema; deterministic per seed, spread across stages and items, no mark scheme or answers in the paper, no grade boundaries claimed), `record_mock.py` records the result, and the new `exam-simulator` skill administers and marks it with the normal grading rules. Mocks are practice: they never change `syllabus_status`. `/readiness` lists recent mock percentages beside (not inside) its band.
- **`/dashboard`** (`dashboard_html.py`): one self-contained HTML page (no scripts, no network, escaped, light/dark, phone-width) with progress, reviews due, readiness with caveats, weak items, unresolved mistakes by cause, recent mocks.
- **`profile_init.py` / `profile_set.py`**: the one validated write path for creating a profile and changing settings (whitelist, schema check, atomic, locked, ledgered, consent-aware, `--dry-run`). Learner words travel on stdin. `/profile` and `/add-profile` no longer hand-edit JSON.
- **Migrations keep a backup**: `migrate_schema.py` writes `<file>.pre-migrate-v<old>.bak` (oldest copy per source version kept) and supports `--dry-run`.
- Doctor and the content CI validate `question_bank.json`.
### Evals
- Seven suites now (added `criteria`, `accessibility`); all baselines re-recorded after the `tutor-core` change; no regressions (grading, safety, injection, diagnostics, gates, criteria all 100%, 0 critical failures). `sample_accuracy` added for comparing skill versions.

## [1.28.0] — 2026-10-05
### Added
- **Deadline-aware planning, opt-in** (`plan_estimate.py`, `plan_target.py`; ADR 0009). The planner no longer sums per-stage estimates by hand (a field the compiler never wrote): the script gives per-course remaining slots (3 per stage by default, plus ~10% review, overridable with `slot_estimates` / `slots_per_stage`) and a weeks projection from the learner's `sessions_per_week`. If a learner gives a real exam date, `plan_target.py set` stores it as an optional `target` (the only calendar date in the system) and `plan_estimate.py --today` reports `on_track` / `tight` / `short` / `expired` with the options that would close a shortfall. Nothing is scheduled on a calendar; the tutor never asks for a date unprompted.
- **Retrieval warm-up** at the start of practice: two or three due recall cards from earlier stages (`review_select.py --limit 3`) before new material.
- Optional `slots_per_stage` / `slot_estimates` in `course.json`; optional `target` in progress files (both in the schemas).

## [1.27.0] — 2026-10-05
### Added
- **Content contract** (`plugin/generic-tutor/docs/CONTENT_CONTRACT.md`): what a course library must contain, the rules the engine enforces on it, and how to validate it in CI.
- **Reusable content-CI workflow** (`.github/workflows/validate-courses.yml`): the private courses repository can call it (`uses: alwayslistening86-pixel/edu-course-library/.github/workflows/validate-courses.yml@<tag>`). The driver `validate_courses.py` now takes `--courses <dir> --engine <dir>` (the old single-argument form still works) and checks, per course: structure, coverage, JSON Schemas (`course`, `curriculum_map`, `rubric`, every `misconceptions.json`), instruction-like text (blocking), and `min_engine_version`.
- **`min_engine_version`** in `course.json`: an install older than a course requires stops at a new gate 0 with "update the plugin" (never blocks when the running version cannot be determined). Schema pattern enforced.
- `misconceptions` JSON Schema (non-empty array of `{pattern, correction, source}`).
- `/doctor` now validates each course's curriculum map, rubric and misconceptions against their schemas too.

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
