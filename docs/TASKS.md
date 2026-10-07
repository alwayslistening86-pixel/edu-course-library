# Task List — EDU Course Library Redesign

Companion to [`PLAN.md`](PLAN.md). One task = one PR. **Size:** S ≤ ½ day · M ≈ 1–2 days · L ≈ 3–5 days (split further if it grows). **Ph** = phase (0–5). **Dep** = must land first. Each task has an acceptance check ("Done when").

Legend: 🔴 fixes a verified defect · 🟡 hardening/quality · 🟢 new capability.

---

## R — Repo foundations & release

| ID | Task | Done when | Dep | Size | Ph |
|---|---|---|---|---|---|
| R-01 🟡 | Add `CLAUDE.md` at repo root: layout, how to run tests, deploy-copy rule, "update `.tutor-scripts/` via bootstrap", docs rules | File exists; a fresh session can run tests from it alone | — | S | 0 |
| R-02 🟡 | Add `CONTRIBUTING.md` + PR template + issue templates (bug, skill-change, schema-change) | Templates render on GitHub; PR template has schema/migration/version checklist | — | S | 0 |
| R-03 🟡 | Introduce `pyproject.toml` (project metadata, ruff + mypy config, python floor) | `pip install -e plugin/generic-tutor` not required; config only; CI reads it | — | S | 0 |
| R-04 🟡 | Add ruff (lint + format) config and fix the initial findings in a mechanical-only PR | `ruff check` and `ruff format --check` green | R-03 | M | 0 |
| R-05 🟡 | Add mypy (or pyright) at lenient settings; type the public functions of each script | Type check green in CI; `# type: ignore` count recorded | R-03 | M | 0 |
| R-06 🟡 | CI: test matrix across supported Python versions (floor … 3.13) | Matrix job green | R-03 | S | 0 |
| R-07 🟡 | CI: split into jobs — lint, type, test, deployed-sync, docs-lint — with required-status names | Branch protection can require each | R-04,R-05 | S | 0 |
| R-08 ✅ | CI: run `tests/fuzz_lifecycle.py` (bounded iterations, fixed seed) as a separate job | Job green; seed logged for repro | — | S | 0 |
| R-09 🟡 | Add pre-commit config (ruff, end-of-file, json validity, no `__pycache__`) | `pre-commit run -a` clean | R-04 | S | 0 |
| R-10 🟡 | `.gitignore`/hygiene pass: remove committed `__pycache__` if any, ignore `.manifest.json` rule clarified | `git ls-files` has no generated files except intended manifest | — | S | 0 |
| R-11 🟢 | `tools/build_plugin.py`: deterministic `.plugin` zip (sorted entries, fixed mtimes, excludes tests/evals) | Two builds are byte-identical; zip installs | — | M | 2 |
| R-12 🟢 | Release workflow: on tag `vX.Y.Z` verify version == `plugin.json` == manifest, build zip, attach to GitHub Release, generate notes from changelog | Dry-run tag produces release draft | R-11,D-05 | M | 2 |
| R-13 🟡 | Version single-sourcing: `plugin.json` is the only hand-edited version; script/skill/manifest versions derived or linted | Docs-lint fails if any other version string disagrees | D-07 | M | 0 |
| R-14 🟡 | Dependabot/Actions pinning (pin actions by SHA, weekly update PRs) | Workflows use pinned SHAs | — | S | 0 |
| R-15 🟡 | Decide and document branch strategy (main protected, short-lived feature branches, squash merge) | Documented in CONTRIBUTING; branch protection configured by owner | R-02 | S | 0 |
| R-16 🟡 | Repo layout move (docs → `docs/`, helper scripts → `tools/`) | Links updated; docs-lint green | D-07 | M | 0 |
| R-17 🟡 | Move `validate_courses.py` into a reusable composite action / documented cross-repo entry point; keep its smoke test | Private repo can `uses:` it by tag | N-03 | S | 5 |
| R-18 🟡 | Security hygiene: enable secret scanning/Dependabot alerts config files; add `SECURITY.md` (private data is out-of-repo; report path) | Files present | — | S | 0 |

## E — Engine hardening (`tutorlib` and scripts)

| ID | Task | Done when | Dep | Size | Ph |
|---|---|---|---|---|---|
| E-01 🟡 | **Characterisation tests**: snapshot every script's CLI JSON output for representative fixtures (golden files) | Goldens committed; any later refactor diff is explicit | — | L | 1 |
| E-02 🟡 | Create `scripts/tutorlib/` package: `paths`, `atomic_io`, `consent`, `envelope`, `cli` modules (empty shells + tests) | Import works from scripts dir and from `.tutor-scripts/` deploy | E-01 | M | 1 |
| E-03 🔴 | `atomic_io.write_json`: write temp in same dir → fsync → `os.replace`; optional `.bak` of previous; used by every state writer | Kill-mid-write test leaves old or new file, never partial | E-02 | M | 1 |
| E-04 🔴 | Advisory file locking for read-modify-write (`lockfile` per learner dir; stale-lock timeout) | Two concurrent `error_log.py append` calls both land (test with subprocesses) | E-03 | M | 1 |
| E-05 🔴 | `consent.enforce(profile, field_class)` inside the library: `granted` all, `limited` = progress+scheduling only, `revoked` = none (table from profile-kernel) | Matrix test: every writer × every consent state | E-02 | L | 1 |
| E-06 🔴 | Wire consent into `error_log.py`, `item_mastery.py`, `confidence_update.py`, `review_math.py`, `sqlite_store.py`, `record_stage_result.py`, `remediation_state.py` | Each returns `{"skipped":"consent …"}` rather than writing; tests per script | E-05 | M | 1 |
| E-07 🟡 | `paths.resolve_root()`: one code path resolves `EDU_ROOT` (env var → explicit arg → plugin data dir) and validates layout; scripts accept `--root` | No skill needs to prose-resolve `/EDU/`; test with 3 layouts incl. Windows-style paths | E-02 | M | 1 |
| E-08 🟡 | Learner-path guard in `paths`: reject any path escaping `profile/<id>/` (symlinks, `..`) | Traversal tests fail closed | E-07 | S | 1 |
| E-09 🟡 partial (--help on all scripts, v1.31.0) | Replace hand-rolled argv parsing with `argparse` subcommands; keep legacy positional forms as aliases for one minor version | `--help` works on every script; legacy invocations still pass old tests | E-01,E-02 | L | 1 |
| E-10 ✅ (opt-in, v1.32.0) | Uniform result envelope `{ok, data, warnings, error{code,message}}`, emitted alongside legacy keys behind `--envelope` first, default in next minor | Schema `schemas/cli/envelope.json`; all scripts conform | E-09,S-06 | M | 1 |
| E-11 ✅ (inferred codes, v1.32.0) | Stable error codes enum (e.g. `E_SCHEMA`, `E_CONSENT`, `E_LOCKED`, `E_NOT_FOUND`) and documented exit codes | Table in docs; tests assert codes | E-10 | S | 1 |
| E-12 🟡 | Backup-before-write for migrations (`migrate_schema.py` copies original to `*.pre-migrate.bak`) and `--dry-run` everywhere state changes | Migration test restores identical bytes | E-03 | S | 1 |
| E-13 ✅ | Idempotency audit: every `apply`/`append` documents and tests behaviour on repeat call (duplicate error events, double slot advance) | Table of idempotency guarantees; tests | E-01 | M | 1 |
| E-14 ✅ | `slot_advance.py`: guard against double-advance in one session (session token) | Second call same session is a no-op with explanation | E-13 | S | 1 |
| E-15 🟡 | `sqlite_store`: schema versioning table, `PRAGMA user_version`, WAL mode, integrity check command | Upgrade test v1→v2 | E-02 | M | 1 |
| E-16 ✅ | `sqlite_store`: decide role — keep as append-only history, add `sqlite_store.py query` canned reports (mastery trend, ease drift, error recurrence) | Three reports documented and tested | E-15 | M | 4 |
| E-17 🟡 | Remove duplicate logic: single implementation of "is course eligible/complete/suspended" used by `cohort_status`, `roster_check`, `gate_check`, `resume_enrollment` | One function, four callers; grep shows no copies | E-01 | L | 1 |
| E-18 🟡 | Normalise date/time handling: injectable `today` everywhere (already partly), UTC ISO, no `datetime.now()` in logic | Grep clean; tests use fixed dates | E-01 | S | 1 |
| E-19 🟡 | Deterministic IDs and ordering in outputs (sorted keys/lists) so goldens are stable | No flaky golden diffs over 100 runs | E-01 | S | 1 |
| E-20 🟡 | Input validation layer using schemas (S-xx) at every script boundary; clear error on malformed learner files rather than traceback | Malformed-file fuzz never raises uncaught exception | S-06,E-02 | M | 1 |
| E-21 ✅ (properties in tests/test_properties.py; cohort invariants by the lifecycle fuzz) | Fuzz expansion: property tests (hypothesis optional, stdlib fallback) for review math monotonicity, BKT bounds [0,1], confidence bounds, cohort convergence invariants | Properties encoded; run in CI | R-08 | M | 1 |
| E-22 🟡 | `bootstrap_scripts.py`: add checksum verification of deployed files, repair mode, and removal of orphaned deployed files | Tampered/old file detected and repaired in test | E-03 | M | 1 |
| E-23 🟡 | `toolkit`: switch to `tutorlib` paths/IO; add `--root`; GUI error surfaces instead of silent failure | Toolkit tests green on Windows-style paths | E-07 | M | 1 |
| E-24 🟢 | `toolkit restore`: restore a backup zip (dry-run default, never overwrites without `--yes`) | Round-trip backup→restore test | E-12 | M | 2 |
| E-25 ✅ (tests/test_performance.py; real timings 30–50 ms) | Performance sanity: scripts complete < 200 ms on a 100-course/5-learner fixture | Benchmark test with generous ceiling | E-01 | S | 1 |
| E-26 🟡 | Test layout reorganised **by module** (`tests/unit/test_<script>.py`, `tests/integration/`, `tests/golden/`); retire release-named files after moving cases | Old names gone; test count not reduced | E-01 | M | 1 |

## S — Schemas & migrations

| ID | Task | Done when | Dep | Size | Ph |
|---|---|---|---|---|---|
| S-01 🔴 | Inventory every persisted file shape from **code** (not docs): `student_profile`, `subjects/*`, review deck, `course.json`, `curriculum_map`, `rubric`, `misconceptions`, `change.md` front-matter, `access.json`, `.manifest.json`, sqlite tables | `docs/DATA_MODEL.md` lists fields/types/owners | — | M | 0 |
| S-02 🔴 | Fix `profile-kernel` micro-profile schema drift (`confidence` is numeric; `error_patterns` structured; add `item_mastery`, `remediation`, `exam_status` semantics) | Skill and S-01 inventory agree; reviewer sign-off | S-01 | S | 0 |
| S-03 🔴 | Reconcile `course.json` schema between `course-compiler`, `_template/course.json` and `migrate_schema.py` (template contains unquoted-placeholder prose; `grounding_status`, `coverage_status` enums) | One enum list; template validates after placeholders filled | S-01 | S | 0 |
| S-04 🔴 | Reconcile review-deck and `curriculum_map` schemas between skills and scripts | Same as S-03 for those files | S-01 | S | 0 |
| S-05 🟢 | Author JSON Schemas under `schemas/` for each file in S-01 (draft 2020-12) | Every real fixture in tests validates | S-01 | L | 0 |
| S-06 🟢 | `tutorlib.schema.validate()` – minimal stdlib validator (or vendored `jsonschema` decision) | Validates fixtures; documented limits | S-05 | M | 1 |
| S-07 🟡 | Schema-conformance tests: every JSON a script writes in any test is validated | CI fails on any off-schema write | S-06 | M | 1 |
| S-08 🟡 | `course-auditor` uses `schemas/` (Tier 1) rather than prose checks; one source of truth | Auditor skill references schema files | S-05 | S | 2 |
| S-09 🟡 | Migration framework: ordered, named migrations with up/verify; `migrate_schema.py` becomes a driver | Every historic version hop has a fixture test | S-05,E-12 | L | 1 |
| S-10 🟡 | Schema-version policy doc: when to bump, deprecation window, compatibility with deployed scripts | In `docs/DATA_MODEL.md` | S-01 | S | 0 |
| S-11 🟡 | Define `change.md` as structured (front-matter or JSONL sidecar) so recheck/auditor can parse reliably | Format spec + parser + test | S-05 | M | 2 |
| S-12 🟢 | Add `misconceptions.json` schema validation to `validate_structure.py` and `postcompile_gate.py` | Invalid entry rejected with reason | S-05 | S | 2 |
| S-13 🟡 | Define identifier rules (`user_id`, `course_id`, `stage_id`, `item_id`, `card_id`): charset, length, reserved names; validate at entry | Path-traversal-safe IDs; tests | S-01 | S | 1 |
| S-14 🟡 | Decide whether learner-supplied free text (notes, summaries) is size-limited and sanitised before storage | Limits documented and enforced | S-05 | S | 1 |

## K — Skills (contract + content review)

Standard for every skill: add a **contract block** (Owns · Reads · Calls · Emits · Never), remove the private "vN" heading, move schema prose to links, add a "Failure modes" section, and add a lint-checked "Scripts used" list.

| ID | Task | Done when | Dep | Size | Ph |
|---|---|---|---|---|---|
| K-00 🟡 | Define the skill contract template + `tools/lint_docs.py` rules (script names exist, referenced commands exist, no heading versions) | Template merged; lint runs in CI | D-07 | M | 0 |
| K-01 🟡 | **tutor-core**: add explicit success criteria for each phase; separate "stance" (how to teach) from "rules" (hard constraints); add worked-example guidance; define "check for understanding" minimum | Contract block; reviewer checklist | K-00 | M | 2 |
| K-02 🟡 | tutor-core: replace numeric confidence bands with referenced script output (`confidence_update` thresholds) so they cannot drift | Thresholds read from one constant, documented | E-17 | S | 2 |
| K-03 🟡 | tutor-core: expand real-situation guard to a tested trigger list (phrases/entities) + required refusal wording | Eval cases A-08 pass | A-08 | M | 3 |
| K-04 🟡 | tutor-core: add accessibility behaviours as concrete output rules (dyslexia mode, plain-language mode) instead of profile hints | Rules testable via eval prompts | L-18 | M | 4 |
| K-05 🟡 | **course-runner**: split the 148-line skill into runner (gates/session lifecycle), `grading` (test procedure), `remediation`, `diagnostics` sections/files to cut context load | Each file < 80 lines; behaviour unchanged (eval parity) | A-01 | L | 2 |
| K-06 🟡 | course-runner: write the session lifecycle as an explicit numbered checklist (start → gates → notices → recheck → teach → record → recap → end) with the exact script call at each step | Checklist is the first section | K-00 | M | 2 |
| K-07 🟡 | course-runner: define what happens on interruption (session ends mid-test, mid-diagnostic) and on resume | Recovery section + state field `in_progress` | V-02 | M | 2 |
| K-08 🟡 | course-runner: tighten live-recheck — define "material change" criteria, max pages fetched, and prompt-injection rules (X-01) | Procedure rewritten; tests/evals | X-01 | M | 2 |
| K-09 🟡 | **course-compiler**: factor the 227-line skill into discovery / build / schema reference; remove embedded schemas (link to `schemas/`) | Files < 100 lines each | S-05 | L | 2 |
| K-10 🟡 | course-compiler: define quality gates for "sourced rubric" (min fields, citation format, URL reachability check, snapshot date) | `postcompile_gate.py` enforces; skill describes | N-04 | M | 5 |
| K-11 🟡 | course-compiler: define behaviour for multi-board / optional-component courses as a decision table | Table + test fixtures | — | S | 2 |
| K-12 🟡 | course-compiler: explicit copyright/paraphrase policy (quote limits, no verbatim mark schemes) aligned with private-repo reason | Policy section; N-06 check | N-06 | S | 2 |
| K-13 🟡 | **course-auditor**: restructure Tier 1/2/3 into a table (check · script · auto-fix? · report format); drop prose duplicates | Skill < 90 lines | S-08 | M | 2 |
| K-14 🟡 | course-auditor: define a machine-readable audit report (JSON) and a human summary; store last report for diffing | Schema + example | S-05 | M | 2 |
| K-15 ✅ | course-auditor: automatic-stub rule ("audit recommended") defined by a script, not prose | `audit_status.py` (or flag in gate_check) | E-17 | S | 2 |
| K-16 🟡 | **profile-kernel**: remove duplicated schema blocks (→ links), keep only behaviour: landing, `/run`, intake, consent | Skill < 90 lines | S-02,S-05 | M | 2 |
| K-17 🟡 | profile-kernel: intake rewritten as a short spec (questions, validation, what is stored) and moved into a `intake` sub-section/skill; handles returning learners editing answers | Intake testable via script `intake_validate.py` | S-05 | M | 2 |
| K-18 🟡 | profile-kernel: define multi-learner "who am I?" safety — confirm active learner at session start and before destructive commands | Confirmation wording specified | — | S | 2 |
| K-19 🟡 | **journey-planner**: separate allocation (read-only advice) from state changes (`/drop`, ledger update); `/drop` moves into its own skill | `drop` skill created; planner has no writes | C-04 | M | 2 |
| K-20 🟡 | journey-planner: replace hand-summed step 2 with a script (`plan_estimate.py`) so no arithmetic lives in prose | Script + tests; skill calls it | E-17 | M | 2 |
| K-21 🟡 | journey-planner: define the plan output format (sequence, bottleneck, review share) as a schema; planner never invents numbers | Output example in tests | K-20 | S | 2 |
| K-22 🟡 partial (caps + dedupe in deck_add.py; retire-card and session cap exist elsewhere) | **review-scheduler**: document deck lifecycle (create deck, card dedupe, retire card, max deck size), and what a "session" of review is (cap per session) | Section + `review_math.py` support for cap | L-05 | M | 4 |
| K-23 ✅ | review-scheduler: define card quality rules (front/back limits, no multi-answer fronts, cloze option) | Lint script for deck cards | — | S | 4 |
| K-24 🟡 | review-scheduler: grading contract – binary vs 4-grade (decide with data; see L-14) | ADR recorded | L-14 | S | 4 |
| K-25 ✅ | **stage-recap**: specify card count and caps per stage; dedupe against existing deck; define worksheet size, format and filename | Numbers + tests of dedupe | L-05 | S | 2 |
| K-26 🟡 | stage-recap: generated worksheet content guard — must not reproduce test items (test integrity) | Check procedure + eval | A-07 | S | 3 |
| K-27 🔴 | **data-erasure**: define the confirmation token (e.g. learner types the exact phrase `ERASE <user_id>`), list every artefact removed incl. `tutor.sqlite3`, `.bak` files, exports/backups the plugin created | Wording + script `erase_profile.py` doing the deletion deterministically | E-02 | M | 1 |
| K-28 🔴 | **data-export**: include `tutor.sqlite3` history (as JSON/CSV), `error_events`, item-mastery logs; document format version | Export script + schema; included in skill | S-05,E-15 | M | 1 |
| K-29 🟡 | data-export: make export a script (`export_profile.py`) producing a single zip with manifest and checksums, not model-assembled | Round-trip import test | K-28 | M | 1 |
| K-30 🟢 | New skill **progress-report** (learner-facing readouts: where am I, weak items, coverage, readiness) | Skill + `progress_report.py` | U-01 | M | 4 |
| K-31 🟢 | New skill **exam-simulator** (timed paper under exam conditions, marking, grade estimate) | Skill + scripts | L-08 | L | 4 |
| K-32 🟢 | New skill **session-wrap** (end-of-session summary + verifier hand-off; writes `last_session_summary`) | Skill; replaces scattered end-of-session prose | V-03 | M | 2 |
| K-33 🟡 | Skill descriptions (front-matter `description`) rewritten to be trigger-precise and under a length cap so routing is reliable | Descriptions reviewed; lint for length | K-00 | S | 2 |
| K-34 🟡 | Cross-skill consistency pass: terminology (stage/phase/slot/cohort/roster) glossary, used everywhere | `docs/GLOSSARY.md`; lint flags undefined terms | D-04 | M | 2 |
| K-35 🟡 | Remove or relocate release-history prose from skills ("from v1.3.0…", "before this version") to the changelog; skills describe *current* behaviour only | Grep for "v1." in skills = 0 | D-05 | M | 2 |

## C — Commands

| ID | Task | Done when | Dep | Size | Ph |
|---|---|---|---|---|---|
| C-01 🟡 | Document arguments for every command (required/optional, validation, examples) in front-matter + a command reference doc | `docs/COMMANDS.md` generated from front-matter | D-07 | M | 2 |
| C-02 🟡 | Add argument validation text to each command wrapper (missing id → helpful prompt, not error) | Each command handles empty/invalid `$1` explicitly | C-01 | S | 2 |
| C-03 🟡 | `/run`, `/add-profile`: user-id charset rules + collision messaging | Matches S-13 | S-13 | S | 2 |
| C-04 🟡 | `/drop`: separate skill, explicit confirmation, shows roster/ledger consequence before acting | Skill + command updated | K-19 | S | 2 |
| C-05 🔴 | `/erase`: confirmation token flow, two-step | Matches K-27 | K-27 | S | 1 |
| C-06 🟢 | `/status`: one-screen summary (active learner, slot, due reviews, next action, any gate blocks) | Command + `status.py` | U-01 | M | 2 |
| C-07 🟢 | `/help`: lists commands with one-liners and the typical flow; context-aware ("you have no profile → /add-profile") | Command added | C-01 | S | 2 |
| C-08 🟢 | `/backup` and `/restore` wrappers over the toolkit (with confirmation) | Commands + tests | E-24 | M | 2 |
| C-09 🟢 | `/mock` (exam simulator entry) | Command wired to K-31 | K-31 | S | 4 |
| C-10 🟢 | `/progress` (detailed report) | Command wired to K-30 | K-30 | S | 4 |
| C-11 🟢 | `/settings`: view/change availability, tone, accessibility, roster cap — replaces ad-hoc `/profile` edits | Validated edits with diff preview | K-16 | M | 2 |
| C-12 🟡 | `/audit` flags: `--report-only`, `--course <id>`, `--tier N` for scoped audits | Documented + script support | K-13 | S | 2 |
| C-13 🟡 | `/review` options: `--course`, `--limit N`, `--topic` | Matches L-05/L-06 | L-05 | S | 4 |
| C-14 🟡 | `/list-courses` filters (`--status`, `--level`) and compact output mode | Documented | C-01 | S | 2 |
| C-15 🟡 | Naming consistency pass (hyphen vs underscore, singular/plural) and aliases | Command table reviewed | C-01 | S | 2 |

## P — Cowork / plugin surface

| ID | Task | Done when | Dep | Size | Ph |
|---|---|---|---|---|---|
| P-01 🟡 | Audit `plugin.json` against the current plugin manifest spec (fields: author, homepage, license, keywords, repository, components paths); fill all | Manifest validates with the official validator/CLI if available | — | S | 0 |
| P-02 🟢 | Add repo-root `marketplace.json` so the plugin installs from the repo without manual zip | Install-from-GitHub flow documented and tested | P-01 | M | 2 |
| P-03 🟡 | Shrink plugin payload: exclude `tests/`, `evals/`, `DESIGN_NOTES.md` from the shipped build | Built zip < agreed size; excludes verified | R-11 | S | 2 |
| P-04 🟢 ✅ | **Spike (done — ADR 0001)**: which hook events exist in Cowork vs Claude Code (SessionStart, PreToolUse, PostToolUse, Stop)? What can they block/inject? Record findings | ADR with capability matrix and fallback plan | — | M | 0 |
| P-05 🟢 | (Claude Code only, optional) `SessionStart` hook: run `bootstrap_scripts.py` automatically; inject active-learner and "run /run first" reminder | Fresh install deploys scripts without `/run` | P-04,E-22 | M | 2 |
| P-06 🟢 | (Claude Code only, optional) `PreToolUse` hook: deny Write/Edit/Bash touching another learner's folder or `courses/` during teaching; deny direct edits of script-owned fields | Test harness simulates blocked/allowed calls | P-04,E-08 | L | 2 |
| P-07 🟢 | (Claude Code only, optional) `PreToolUse` consent hook: when consent is `revoked`, block all writes under `profile/<id>/` | Matrix test with hook simulator | P-06,E-05 | M | 2 |
| P-08 🟢 | (Claude Code only, optional) `PostToolUse`/`Stop` hook feeding the write verifier (V-03) | Events recorded to session ledger | V-01 | M | 2 |
| P-09 🟡 | Permissions guidance: recommended allowlist for the scripts (`python3 …/.tutor-scripts/*.py`) so teaching isn't interrupted by prompts; shipped as documented settings snippet | Snippet in user guide | D-03 | S | 2 |
| P-10 🟡 | `.mcp.json`: add per-server rationale, trust level, "disable if not needed", and consider pinning/URL ownership evidence; keep opt-in | `docs/CONNECTORS.md`; no auto-enable | X-06 | S | 2 |
| P-11 🟡 | Connector handling in skills: define behaviour when a suggested connector is not connected (graceful fallback to web search) | Tested via eval prompt | A-01 | S | 3 |
| P-12 🟡 | Folder-connection UX: precise instructions + detection of wrong folder (no `courses/`) with actionable error | `doctor.py` check + message | E-07 | M | 2 |
| P-13 🟢 | `doctor` command/script: validates install (versions, deployed scripts, folder layout, python version, writable dirs, hooks active) | `/doctor` output with fixes | P-12,E-22 | M | 2 |
| P-14 🟡 | Python availability: detect missing `python3` and explain; document Windows (`py -3`) differences; ensure all skill invocations use a resolved interpreter variable | Skills use one placeholder for the interpreter | E-07 | M | 2 |
| P-15 🟡 | Context-budget audit: measure tokens loaded by each command (it `@`-includes up to 4 skills for `/continue`); set a budget and trim | Budget table; `/continue` ≤ agreed tokens | K-05 | M | 2 |
| P-16 🟢 | Optional scheduled-task integration: reminder to study based on `sessions_per_week` (no dates stored in plugin; scheduling lives in Cowork) | Documented opt-in recipe only | — | S | 4 |
| P-17 🟡 | Compatibility matrix: Claude Code CLI / desktop / Cowork — what works where | `docs/COMPATIBILITY.md` | P-04 | S | 2 |
| P-19 🟢 | CI: run `claude plugin validate --strict` on the plugin and marketplace when the CLI is available; add `marketplace.json` fields per ADR 0001 | Validation job green | P-02 | S | 2 |
| P-18 🟡 | Uninstall/upgrade path docs: what remains in the data folder; rollback to prior plugin version | Documented + tested via bootstrap downgrade refusal | E-22 | S | 2 |

## V — Trust & verification (the "did it actually write?" problem)

| ID | Task | Done when | Dep | Size | Ph |
|---|---|---|---|---|---|
| V-01 🟢 | **Session ledger**: each state-writing script appends one line to `profile/<id>/.session_ledger.jsonl` (ts, script, args hash, result) | Every writer logs; tests | E-02 | M | 2 |
| V-02 🟢 | Define the *expected-writes* model: for each session event type (test graded, practice error, review answered, stage passed) the set of script calls that must follow | `schemas/expected_writes.json` + doc | V-01 | M | 2 |
| V-03 🟢 | Write verifier script: reads transcript-derived events (from skill-emitted event lines or hook data) and the ledger; outputs missing/extra writes | Injected-fault tests (omit apply) detected | V-02 | L | 2 |
| V-04 🟢 | Skills emit a compact machine-readable "event line" at each gradeable moment (e.g. `EVENT test_graded stage=S2 result=pass`) that the verifier parses | Format spec; skill edits; verifier consumes | V-02 | M | 2 |
| V-05 🟢 | Fault-injection suite: simulated sessions with omitted/duplicated/misordered calls; measure detection rate | ≥ 95 % detection (PLAN §9) | V-03 | M | 2 |
| V-06 🟢 | Remediation path: verifier output → next `/run` shows "last session may be missing: …" and offers to reconcile (never auto-writes grades) | UX wording + test | V-03 | M | 2 |
| V-07 🟡 | Tamper-evidence light: ledger hash chain *only if* V-05 shows a need (design notes previously rejected hash chains) | Decision recorded | V-05 | S | 2 |
| V-08 🟡 | State invariants checker (`invariants.py`): e.g. `current_stage` consistent with `syllabus_status`, cohort ids match course level, deck due slots ≥ 1 | Runs in `/doctor` and `/audit`; fuzz-tested | S-05 | M | 2 |
| V-09 🟡 | Grading provenance: store rubric criteria evidence per test result (what answer text was scored against which criterion) in the sqlite history | Table + writer; privacy-reviewed | E-15,X-04 | M | 3 |
| V-10 🟢 | Learner-visible audit: `/status --audit` shows last N writes in plain language | Command option | V-01 | S | 2 |

## L — Learning design

| ID | Task | Done when | Dep | Size | Ph |
|---|---|---|---|---|---|
| L-01 🟡 | Write a one-page **learning-science rationale** mapping each mechanic to evidence (retrieval practice, spacing, interleaving, worked examples, mastery gating) and flagging weak-evidence choices (e.g. contrasting-subject pairing) | `docs/PEDAGOGY.md` | — | M | 0 |
| L-02 🟢 | In-stage retrieval: after the lesson, 2–4 retrieval prompts on *earlier* stages before practice (pulled from deck) | Skill section + `review_math` selection helper | K-22 | M | 4 |
| L-03 🟢 | Interleaved practice: mix prior-stage items into practice set at a defined ratio, tagged for later analysis | Ratio constant; `select_interleave.py` | L-02 | M | 4 |
| L-04 🟢 | Learner-initiated mixed review by topic/stage/weak-items (`/review --topic`) | Selection uses item mastery + due cards | C-13 | M | 4 |
| L-05 🟡 | Review session caps and prioritisation (overdue first, then low-ease, then new) with deterministic ordering | Script returns ordered list; tests | K-22 | M | 4 |
| L-06 ✅ | Card types: basic, cloze, "explain-why", worked-step; schema + presentation rules | Schema extension + migration | S-09 | M | 4 |
| L-07 🟡 | Use `item_mastery` to drive *what to practise next* (selection algorithm), not only pacing hints | `next_items.py` + skill step; ablation eval | A-05 | L | 4 |
| L-08 🟢 | **Exam simulation**: timed paper assembled from test/exam bank with mark scheme, timing guidance, honest marking, grade-boundary estimate with uncertainty | Skill K-31 + `assemble_paper.py` | N-07 | L | 4 |
| L-09 ✅ | Exam technique content: command-word handling, mark-allocation heuristics, time per mark — as a per-course optional file `exam_technique.md` | Template + compiler step | N-05 | M | 4 |
| L-10 🟢 | Readiness estimate: per-course, from item mastery + coverage + recent test results, presented with a confidence band and caveats | `readiness.py`; wording rules | L-07 | M | 4 |
| L-11 🟡 | Worked-example fading policy: define when to give full/partial/no worked example by mastery band | Policy in tutor-core + eval | K-01 | S | 4 |
| L-12 🟢 | Opt-in **deadline-aware planning**: learner may state an exam date; planner computes slots-needed vs slots-available and triage priorities without storing a calendar (date stored only as a single optional field with expiry) | ADR approving or rejecting; if approved, script + tests | — | L | 4 |
| L-13 ✅ | Practice variety: guard against repeated identical items (`practice.md` item bank with rotation tracking) | Rotation state in subjects file; tests | S-09 | M | 4 |
| L-14 🟡 | Revisit review algorithm with real data: after N months of `review_log`, evaluate SM-2-lite vs alternatives offline; decide binary vs graded recall | Report in docs; ADR | E-16 | M | 5 |
| L-15 🟡 | Confidence model: separate *calibration* (does learner's self-rated confidence match results?) from the system's `confidence` number; optionally ask for self-rating pre-answer | Design note + opt-in | A-05 | M | 4 |
| L-16 ✅ | Feedback style rules: specific, criterion-referenced, next-action oriented; no answer-leaking in hints; hint ladder (nudge → cue → partial → full) | Rules + eval cases | K-01 | M | 3 |
| L-17 🟡 | Metacognition prompts at stage end (what was hard, what to revisit) feeding `last_session_summary` | Short protocol | K-32 | S | 4 |
| L-18 🟢 | Accessibility output modes implemented as concrete formatting contracts (chunk size, glossary, sentence length, no dense tables) and a text-only/screen-reader-friendly mode | Eval checks mode compliance | A-01 | M | 4 |
| L-19 ✅ | Language support: non-English-first learners (glossary in home language optional), spelling variants (en-GB focus) | Optional `locale`/`home_language` field | S-09 | M | 5 |
| L-20 🟡 | Session length awareness: respect `session_minutes` (pacing checkpoints, stop-points that leave state consistent) | Checkpoint protocol in runner | K-07 | M | 4 |
| L-21 🟡 | Prerequisite remediation across courses: when diagnosis says `missing_prerequisite`, point to concrete earlier stage/course with a one-click `/continue` suggestion | Mapping via `curriculum_map` prerequisites | N-08 | M | 4 |
| L-22 ✅ | Goal alignment: translate learner `goals` into prioritised syllabus items; show coverage vs goal | `goal_map.py` | L-10 | M | 5 |

## A — Assessment quality & evaluation

| ID | Task | Done when | Dep | Size | Ph |
|---|---|---|---|---|---|
| A-01 🟢 | Eval harness skeleton `evals/`: case format (YAML/JSON), runner, scoring, report; model-in-the-loop optional, deterministic checks always | `python -m evals run --offline` works | — | L | 3 |
| A-02 🟢 | Fixture sets: 3 public-domain/self-authored sample courses (maths, humanities, one law-style) for evals so no private content is needed | Fixtures committed | A-01 | M | 3 |
| A-03 🟢 | **Grading calibration set**: learner answers (strong/borderline/wrong, method-correct-answer-wrong, right-answer-wrong-method) with reference marks that need no human marker — computable answers, or openly licensed published mark schemes with provenance recorded; target agreement set after baseline | Baseline measured; thresholds recorded | A-01,A-02 | L | 3 |
| A-04 🟢 | Diagnostic classification set: transcripts labelled with ground-truth `cause` (slip, prerequisite, misconception, procedure, comprehension); measure accuracy and over-triggering | Confusion matrix baseline | A-01 | L | 3 |
| A-05 🟢 | Pacing/selection ablation evals (confidence/mastery usage) on simulated learners | Simulated-learner generator + metrics | L-07 | L | 4 |
| A-06 🟡 | **Automated consistency protocol (replaces human spot-checks — the owner will not mark)**: for every eval item, N-sample self-agreement, an independent second grader, and a deterministic oracle where the answer is computable; items that fail agreement are listed as "ambiguous" and excluded from accuracy claims | Report lists agreement rate and the ambiguous set; no human step | A-03 | S | 3 |
| A-07 🟢 | Test-integrity evals: worksheet/recap must not leak test items; hints must not reveal answers | Cases + detectors | A-01 | M | 3 |
| A-08 🟢 | Safety evals: real-situation guard (legal/accounting), physical-risk practicals, honesty about uncertainty | ≥ N cases, pass-all required | A-01 | M | 3 |
| A-09 🟢 | Gate-conformance evals: given a state fixture, does the agent stop at the correct gate and explain it plainly (dormant, suspended, prerequisite) | Cases for each gate | A-01 | M | 3 |
| A-10 🟡 | Regression policy: any skill change PR must attach eval delta or justify; CI runs offline subset only | Documented in CONTRIBUTING; offline subset in CI | A-01 | S | 3 |
| A-11 🟡 | Rubric-quality lint: every rubric criterion has source, mark allocation, observable descriptor (no vague "good understanding") | `rubric_lint.py` | S-05 | M | 3 |
| A-12 🟡 | Item-level difficulty and discrimination estimates from accumulated attempts (only if data volume allows); flag broken items | Analysis script; threshold on min attempts | E-16 | M | 5 |
| A-13 🟡 | Cost/latency tracking per command (tokens loaded, turns per stage) as an eval metric | Metrics in report | A-01,P-15 | S | 3 |
| A-14 🟡 | Cross-model robustness: run the offline eval pack against each supported model tier and record differences | Table in docs | A-01 | M | 5 |

## U — Learner visibility

| ID | Task | Done when | Dep | Size | Ph |
|---|---|---|---|---|---|
| U-01 🟢 | `progress_report.py`: per-course stage ladder status, coverage, weak items (by `p_mastery`), due reviews, recent errors, readiness | JSON output + schema | S-05 | M | 2 |
| U-02 🟢 | In-session rendering of the report (text table) with consistent wording and honesty rules (coverage disclosure) | Skill template; golden test | U-01 | S | 2 |
| U-03 🟢 | Optional HTML dashboard artifact generated from the report (read-only, no learner data leaves the machine) | Artifact template; privacy review | U-01,X-04 | M | 4 |
| U-04 🟡 | Toolkit GUI parity with `/status` and `/progress`; keep read-only | GUI screens added | U-01 | M | 4 |
| U-05 🟡 | Streak-free motivation: progress framing that avoids gamification (stage milestones, coverage %) | Wording guidelines | L-01 | S | 4 |
| U-06 ✅ | Export progress as a printable summary (PDF via existing doc tooling) for parents/tutors, with consent check | Output option on `/export` | K-29 | M | 5 |
| U-07 🟡 | Anki export upgrade: include tags (stage, item, criterion), cloze support, media-free guarantee | `export_anki.py` updated + tests | L-06 | S | 4 |

## N — Content pipeline (private repo contract)

| ID | Task | Done when | Dep | Size | Ph |
|---|---|---|---|---|---|
| N-01 🟡 | Write the **content contract** doc: folder layout, required files, naming, versioning of course content, how the engine locates it | `docs/CONTENT_CONTRACT.md` | S-05 | M | 0 |
| N-02 🟡 | Versioned compatibility: `course.json` declares `min_engine_version`; gate_check refuses incompatible courses with a clear message | Field + check + test | N-01 | S | 2 |
| N-03 🟢 | Reusable GitHub Action (and CLI) for the private repo: structure + coverage + schema + rubric-lint + copyright heuristics | `uses:` works from private repo | S-05,A-11 | M | 5 |
| N-04 🟡 | Source verification helper: URL liveness, snapshot hash/date capture for spec documents (stored as metadata only) | `verify_sources.py` | N-01 | M | 5 |
| N-05 ✅ | Compiler output includes optional `exam_technique.md` and `command_words.json` where the board publishes them | Template + compile step | K-09 | M | 5 |
| N-06 ✅ | Copyright heuristics: detect long verbatim runs vs. source excerpts supplied to compiler; warn | `paraphrase_check.py` | K-12 | M | 5 |
| N-07 🟡 | Question bank structure for exam assembly (tagged by item, marks, difficulty, calculator/non-calculator) | Schema + template | S-05 | M | 4 |
| N-08 🟡 | Prerequisite graph at item level (not just course level) to power remediation links and planning | `curriculum_map` extension + migration | S-09 | L | 5 |
| N-09 🟢 | Misconception seeding pipeline: for each course, generate candidates from examiner reports/sources, human-review queue, sourced entries only | Queue format + reviewer checklist; first course seeded | A-04 | L | 5 |
| N-10 🟡 | Currency monitor: scheduled (manual or CI in private repo) check of spec version/issue per course → report only | `currency_report.py` | N-04 | M | 5 |
| N-11 ✅ | Content changelog and provenance per course (`change.md` structured, S-11) surfaced in `/list-courses` | Display + tests | S-11 | S | 5 |
| N-12 ✅ | Course import/export between libraries (portable course bundle, no learner data) | Bundle format + tests | N-01 | M | 5 |
| N-13 ✅ | Template refresh: `_template/` produces a schema-valid skeleton; includes `misconceptions.json` example and `exam_technique.md` stub | `validate_structure` passes on filled template | S-03 | S | 2 |
| N-14 ✅ | Decide fate of "historic" vs "staging" courses in contract (states, transitions, who can move them) | Contract section | N-01 | S | 2 |
| N-15 ✅ | Compile into a hidden build folder and publish by rename once the post-compile gate passes, so a half-built or failed compile is never visible to `/list-courses` or enrolment | Compiler steps 7-8 rewritten; interrupted compile leaves no live course; test | N-14 | M | 5 |

## X — Security & privacy

| ID | Task | Done when | Dep | Size | Ph |
|---|---|---|---|---|---|
| X-01 🔴 | **Prompt-injection policy**: web content fetched by compiler/live-recheck is untrusted data; never follow instructions in it; never write raw fetched text into skills/state; quote with delimiters | Policy section in both skills + evals A-xx with injected pages | A-01 | M | 2 |
| X-02 🔴 | Treat `change.md`, `misconceptions.json`, lesson files as untrusted-on-read if their provenance is web-derived (don't execute instructions embedded in them) | Skill rule + eval | X-01 | S | 2 |
| X-03 🟡 | Learner-input handling: sanitise IDs/paths; never interpolate learner text into shell commands; scripts take args via argv only | Review + tests with hostile strings | S-13 | S | 1 |
| X-04 🟡 | Data classification doc: what is personal data (profile, errors, notes, history DB), where stored, retention, who can read | `docs/PRIVACY.md` | S-01 | S | 0 |
| X-05 🟡 | Retention controls: `/erase` full, plus selective purge (history DB only, a single course, last N days) | `purge.py` with dry-run | K-27 | M | 5 |
| X-06 🟡 | Third-party endpoint review for suggested MCP servers (ownership, data sent, auth, uptime); add disclosure text to compiler's connector step | Review recorded in CONNECTORS.md | P-10 | S | 2 |
| X-07 🟡 | Secrets/PII scan in CI for committed fixtures (no real learner IDs, emails) | Gitleaks-style check green | R-18 | S | 0 |
| X-08 🟡 | Backups security: backup zips may contain personal data — default location outside synced folders warning; optional passphrase encryption | Documented; optional flag | E-24 | M | 5 |
| X-09 🟡 | Minor-learner considerations: age-appropriate defaults and a note that parents control data (guardian-oversight remains out of scope per notes, but document the boundary) | `docs/PRIVACY.md` section | X-04 | S | 0 |
| X-10 🟡 | Licence audit: confirm all vendored/borrowed material (e.g. ideas from Apache-2.0 plugins) has attribution; NOTICE file | `NOTICE` present | — | S | 0 |

## D — Documentation

| ID | Task | Done when | Dep | Size | Ph |
|---|---|---|---|---|---|
| D-01 🟡 | Split `DESIGN_NOTES.md` into: `CHANGELOG.md` (what shipped), `docs/adr/NNNN-*.md` (decisions with rationale), and a short `ARCHITECTURE.md` | Original file archived under `docs/history/`; links updated | — | L | 0 |
| D-02 🟡 | `ARCHITECTURE.md`: data flow diagram (profile ↔ subjects ↔ courses ↔ scripts ↔ sqlite), gate order, ownership table (who writes what) | Reviewed by reading it cold | S-01 | M | 0 |
| D-03 🟢 | **User guide**: install (plugin + folder connect + Python), first run, daily flow, every command with examples, troubleshooting, FAQ | Fresh-machine walkthrough ≤ 5 min | P-02 | L | 2 |
| D-04 🟡 | `GLOSSARY.md` (stage, phase, slot, cohort, roster, level lock, convergence, grounding, coverage …) | Linked from skills | — | S | 0 |
| D-05 🟡 | Changelog discipline: Keep-a-Changelog format, entry required per release by CI | CI checks version present in changelog | D-01 | S | 0 |
| D-06 🟡 | README rewrite: what it is, what's here, quick start, link map; remove numeric claims that rot (course counts) | README < 100 lines | D-03 | S | 2 |
| D-07 🟢 | `tools/lint_docs.py`: checks (a) every referenced script/command/skill exists, (b) command↔skill wiring, (c) version strings agree, (d) relative links resolve, (e) glossary terms, (f) contract blocks present | Runs in CI; failing example tests | — | L | 0 |
| D-08 🟡 | Contributor guide: how to add a script, schema, skill, command, eval case; checklists | `docs/CONTRIBUTING-DEV.md` or section | R-02 | M | 2 |
| D-09 🟡 | ADRs for existing decisions worth keeping (slot-based scheduling, SM-2-lite over FSRS, no hash chains, no placement diagnostic, JSON as source of truth, courses in private repo) | ≥ 6 ADRs migrated from notes | D-01 | M | 0 |
| D-10 🟡 | Troubleshooting runbook: common gate blocks, corrupted file recovery, restoring from backup, deploy mismatch | `docs/RUNBOOK.md` | E-24 | M | 2 |
| D-11 🟡 | Toolkit README refreshed (single source for CLI usage; auto-generated `--help` embedded) | Docs-lint verifies commands listed exist | E-09 | S | 1 |
| D-12 🟡 | Docs for evals: how to run, add cases, read reports, cost expectations | `evals/README.md` | A-01 | S | 3 |

---

## B — Surfaces & deployment (direction accepted 6 Oct 2026; build patterns still to be designed)

These come from the owner's review of three ideas (ADR 0010): learner state that travels with the learner, a local user interface over the scripts, and models given different roles. They are no longer being dismissed. They are also not yet designed: each task below starts with a design step (a short ADR or design note with the build pattern, the risks and how it will be measured), and nothing should be built before that. Order matters: B-01 first, B-02 next, the role work last. `docs/WAVE7.md` breaks each into micro-tasks (B-01.1 and so on, 51 in all), with the owner decisions each needs and what would make us stop; the micro-tasks live there so the counts here do not move.

| ID | Task | Done when | Dep | Size | Ph |
|---|---|---|---|---|---|
| B-01 🟡 | **Portable profile.** Design, then build: resolve the data root from any mounted folder or drive; a "this is a valid profile" check before a session starts; safe-eject and interrupted-write guidance; an option to encrypt the live profile; a position on what the medium may be (USB, plain folder, never a synced folder). Multi-user is many single-user profiles plus one shared engine, not tenancy | Design note, then tests on a simulated removable folder, including an unplug mid-write | E-07, X-08 | L | 6 |
| B-02 🟡 | **Local UX** over the existing scripts. Design the surface first (what a session looks like, where Claude or a local model plugs in as the teaching voice). First version is deterministic only: multiple-choice and numeric items, review cards, status, practice items and recorded results through the same scripts, with no model in the bookkeeping | Design note; a UI that completes a deterministic stage loop against the scripts | B-01 | L | 6 |
| B-03 🟡 | **Local-model eval backend**: run every eval suite on a small local model, record the results, and decide which rules hold before it is allowed to teach | A backend in the eval harness; a baseline per suite | A-14 | M | 6 |
| B-04 🟡 | **Practice-judgment rule** (ADR): practice-phase judgments such as why an answer was wrong write `error_log`, `item_mastery` and `confidence`. Decide who may make them when the teaching model is not the examiner (script-marked items, proposals checked by a script, or deferred to the examiner) | ADR accepted | B-02 | M | 6 |
| B-05 🟡 | **Role policy**: tutor voice, examiner and staff channel as a table of which role may call which script, enforced by the hook guard and by the scripts; Claude stays a full fallback teacher when no local model is set up; the examiner being offline is stated plainly | Policy table in code with tests; student mode cannot install or edit | B-03, B-04 | L | 6 |
| B-06 🟡 | **Fleet and children's data** notes: how course content reaches many machines (private repo, licensing), how engine updates reach them, what a school deployment owes in data protection. A design note for the owner, not legal advice | Note reviewed by the owner | B-01 | S | 6 |
| B-07 🟡 | **Shared, anonymised pattern pool** (design first). A learner who opts in can contribute the *spirit* of what went wrong, not their answer: per criterion, a short description of the error pattern written without names or specifics, with no learner id, no dates and no course-specific identifiers, released only as a reviewed export bundle and only for patterns seen from several learners. Local storage stays in the learner's own history (`grading_results` could gain a short pattern note); sharing is a separate opt-in export step, never an automatic push. The pooled result feeds the audit's misconception proposals and the item-quality checks (A-12). Needs a separate consent class (default off), a re-identification and children's-data review (small cohorts such as one family or one class are the risk), and a decision on who holds the pool | Design note and consent model accepted; an export that a learner can read before sending | B-01, V-09 | M | 6 |

## Progress

| Task | Status | Notes |
|---|---|---|
| R-01 | ✅ done | `CLAUDE.md` |
| R-02 | ✅ done | `CONTRIBUTING.md`, PR template, 3 issue templates |
| R-03 | ✅ done | `pyproject.toml` (Python ≥3.10, ruff/mypy config; tools not yet enforced — R-04/R-05) |
| R-06 | ✅ done | CI matrix 3.10 / 3.12 / 3.13; suite verified locally on 3.10 and 3.13 |
| R-04 | ✅ done | `ruff check` clean (lint only; style rules E701/E702/E741/E402 deliberately ignored; `ruff format` not adopted — would rewrite 41 files for no behavioural gain). Real findings fixed (dead vars, unused imports, lambda) |
| R-05 | ✅ done | `mypy plugin/generic-tutor/scripts` already clean at lenient settings; now a CI job |
| R-07 | ✅ done | CI split into `test` (matrix), `lint`, `docs-lint`, `deployed-sync` |
| R-09 | ✅ done | `.pre-commit-config.yaml` (ruff, json/yaml checks, scripts-sync) |
| R-10 | ✅ done | verified: no generated files tracked |
| S-01 | ✅ done | `docs/DATA_MODEL.md` (inventory from code; owners per field; 6 discrepancies logged) |
| S-10 | ✅ done | versioning policy in `docs/DATA_MODEL.md` |
| D-07 | ✅ done | `tools/lint_docs.py` + tests; checks script refs, command↔skill wiring, names, versions, links |
| K-35 | 🟡 partial | private `vN` removed from 4 skill headings; release-history prose inside skills remains |
| E-14 | ℹ️ note | `slot_advance.py` already has a time-window double-`/run` guard; E-14 narrows to a session-token guard |
| R-14 | 🟡 partial | `dependabot.yml` for Actions added; SHA-pinning deferred (needs verified SHAs, not guessed) |
| R-18 | ✅ done | `SECURITY.md` |
| X-04 | ✅ done | `docs/PRIVACY.md` |
| X-09 | ✅ done | minors section in `docs/PRIVACY.md` |
| X-10 | ✅ done | `NOTICE` |
| D-04 | ✅ done | `docs/GLOSSARY.md` |
| D-05 | ✅ done | `CHANGELOG.md` + CI check that the current `plugin.json` version has an entry |
| S-03 | ✅ done | key sets of skill schema, `_template/course.json` and `migrate_schema.py` verified identical; `grounding_status: null` (unmigrated) documented |
| S-04 | ✅ done | deck and `curriculum_map` shapes reconciled in `docs/DATA_MODEL.md` |
| L-01 | ✅ done | `docs/PEDAGOGY.md` |
| P-04 | ✅ done | `docs/adr/0001-hooks-and-platform-support.md` — hooks are Claude Code-only; verifier is primary (provisional, items to verify listed) |
| D-02 | ✅ done | `docs/ARCHITECTURE.md` |
| D-09 | ✅ done | ADRs 0002–0008 retrospectively recorded; index in `docs/adr/README.md` |
| D-01 | ✅ done | `DESIGN_NOTES.md` frozen at v1.61.0 and archived to `docs/history/`; CHANGELOG carries the why from now on, lasting decisions get ADRs; contributor docs, PR template and lint message updated |
| K-00 | 🟡 partial | `docs/SKILL_CONTRACT.md` template; lint rule to be added once skills adopt it |
| E-02 | 🟡 partial | `tutorlib` package created with `atomic_io`, `filelock`; `paths`, `consent`, `envelope`, `cli` modules still to come |
| E-03 | ✅ done | all 10 JSON writers atomic; format byte-identical; tests (v1.13.0) |
| E-04 | ✅ done | per-file re-entrant lock on 8 RMW entry points; parallel test fails (6–9 of 12 survive) without it, passes with it (v1.13.0) |
| E-05 | ✅ done | `tutorlib/consent.py` (3 write classes, fail-closed) (v1.14.0) |
| E-06 | ✅ done | wired into 9 writers + `sqlite_store`; matrix test verified to fail when gate disabled. `migrate_schema.py` exempt by design |
| K-27 | ✅ done | `erase_profile.py` + skill rewrite; phrase `ERASE <user_id>`, dry-run, history DB included (v1.15.0) |
| K-28 | ✅ done | export includes all history tables |
| K-29 | ✅ done | `export_profile.py` zip with manifest + sha256 |
| C-05 | ✅ done | `/erase` command updated |
| S-13 | 🟡 partial | `tutorlib.ids` rules + tests; wired into erase/export only (rest under E-20) |
| E-08 | 🟡 partial | `tutorlib.paths` symlink/outside-root guard; used by erase/export; other scripts take explicit paths from the caller |
| E-01 | ✅ done | 27 golden CLI cases (all scripts but `bootstrap_scripts.py`, covered by deploy tests) in `tests/test_golden_cli.py` + `tests/golden/`; deterministic across runs and Python 3.10/3.12; a meta-test fails when a new script has no golden case. Finding: three scripts return errors as JSON with exit 0 (`docs/CLI_BASELINE.md`) → input to E-10/E-11 |
| E-11 | 🟡 partial | exit-code convention (0/1/2) implemented via `tutorlib/cli.py` and pinned by goldens (v1.16.0); stable error-code enum still open |
| E-10 | 🟡 partial | `cli.emit` shared emitter; `{ok,data,error{code,message}}` envelope still open |
| E-17 | ✅ done | `LIVE_STATES` / `SLOT_STATES` / `is_suspended` single-sourced in `cohort_status.py`; guard test; goldens unchanged (v1.16.1). `is_complete` was already shared; JSON-load helpers still duplicated (→ tutorlib IO) |
| S-05 | ✅ done | schemas for every persisted JSON file: profile, subjects, deck, course, curriculum_map, rubric, misconceptions, question_bank, access, manifest (`change.md` and SQLite have their own checkers); `confirm_access.py` writes through `state.save`; a test validates files written by the scripts (v1.64.0) |
| S-06 | ✅ done | `tutorlib/schema.py` stdlib validator + `validate_schema.py` |
| S-07 | ✅ done | `tests/test_schemas.py`: all fixtures and script-written files conform; bad shapes rejected |
| S-09 | 🟡 partial | six writers refuse newer `schema_version` (`tutorlib/state.py`); migration framework (ordered named migrations) still open |
| E-20 | 🟡 partial | safe loading + clear errors in the six writers; validate-before-write and readers still open |
| E-07 | ✅ done | `tutorlib.paths.resolve_root/layout` + `resolve_root.py`; profile-kernel uses it (v1.18.0). Individual scripts still take explicit paths from the caller by design |
| E-15 | ✅ done | `PRAGMA user_version`, newer-DB refusal, `sqlite_store.py check`; WAL deliberately not enabled |
| E-22 | ✅ done | bootstrap sha256 drift repair + recorded-orphan removal; tests in `test_bootstrap_repair.py` |
| V-01 | ✅ done | `tutorlib/ledger.py`; 8 writers log; consent-aware (v1.19.0) |
| V-02 | ✅ done (as code) | expected-writes model is the rule set in `verify_session.py` (documented in its docstring), derived from the ledger rather than a separate JSON |
| V-03 | ✅ done | `verify_session.py` |
| V-04 | ➖ dropped | model-emitted event lines are unnecessary: scripts leave the trace; see DESIGN_NOTES v1.19.0 |
| V-05 | ✅ done | 8 injected faults all detected; clean sessions produce no findings |
| V-06 | ✅ done | profile-kernel `/run` audits the previous session and reports without back-filling |
| V-08 | ✅ done | `invariants.py` (not yet wired into a `/doctor` command — P-13) |
| P-13 | ✅ done | `doctor.py` + `/doctor` (v1.20.0) |
| C-06 | ✅ done | `status.py` + `/status` |
| C-07 | ✅ done | `/help`; docs-lint enforces that every command is listed |
| X-01 | ✅ done | policy + skill rules + blocking scan in `postcompile_gate` (v1.21.0); model-in-the-loop injection evals still under A-xx |
| X-02 | ✅ done | course-file-as-data rule in tutor-core/runner/auditor; scan after writing `change.md` |
| X-03 | ✅ done | stdin note passing, erase phrase from script output, hostile-id tests |
| E-24 | ✅ done | `backup_profile.py` + `restore_profile.py` (v1.22.0); toolkit-backup default location fixed |
| C-08 | ✅ done | `/backup`, `/restore`, `backup-restore` skill |
| P-01 | ✅ done | `plugin.json` fields completed; `claude plugin validate --strict` passes |
| P-02 | ✅ done | `.claude-plugin/marketplace.json`; add/install/uninstall verified locally |
| P-03 | ✅ done | `build_plugin.py` excludes tests/caches; shipped docs moved inside the plugin |
| P-19 | ✅ done | `plugin-validate` CI job (plugin, skills, commands, marketplace) |
| R-11 | ✅ done | `tools/build_plugin.py` deterministic |
| R-12 | ✅ done | `release.yml` (untested until the first tag) + `tools/release_notes.py` |
| P-15 | ✅ done | `tools/context_budget.py` + ratchet + CI check; `/list-courses` −95%, `/drop` −87%, `/run` −45% (v1.24.0) |
| K-05 | 🟡 partial | command-specific parts split out of course-runner (list-courses.md); teaching-path sections deliberately kept whole until evals exist |
| K-09 | ⏸ deferred | course-compiler internal split waits for evals (same reason) |
| K-00 | ✅ done | contract template enforced by docs lint (all 12 skills carry a Contract block) |
| K-33 | ✅ done | descriptions ≤400 chars and must name a /command or say none (lint) |
| C-01 | ✅ done | `docs/COMMANDS.md` generated from front-matter + staleness test |
| C-02 | ✅ done | missing/invalid-argument handling written into the 8 commands that take arguments |
| A-01 | ✅ done | `evals/` harness: 5 suites, `claude` + offline backends, report + `check` (dev-only) |
| A-02 | ✅ done | three self-authored sample courses in `evals/fixtures/courses/` (maths level 2, humanities-style level 2, a standalone law-style course with IRAC): each passes the compile gate, coverage is full, the rubric lint is clean, banks made by `exam_to_bank.py`; tests run a learner through all three with the real scripts. Original content, no board wording (`evals/fixtures/README.md`) |
| A-03 | 🟡 baseline | grading suite baseline recorded (sonnet): 35/35 acceptable, 0 false passes; set is easy - borderline, units, multi-part and extended-writing cases still to add |
| A-04 | ✅ done | diagnostics suite, 15 scenarios, 5 causes × 3; baseline 14/14 scored, 1 ambiguous |
| A-06 | ✅ done | automated consistency protocol: N-sample agreement, acceptable sets, ambiguous set excluded, authoring rule recorded |
| A-08 | ✅ done | safety suite (real-situation guard + physical risk), 12 cases. Follow-on (v1.90.0): `wellbeing` suite (18 invented cases, code-graded) and a tutor-core rule for learners who may be unsafe |
| A-09 | ✅ done | gates suite on real `gate_check.py` output, 7 cases |
| A-10 | ✅ done | `python -m evals check` + policy in `evals/README.md` (not yet a CI gate: model runs are manual) |
| X-01 | ✅ evals | injection suite, 8 cases (6 attack styles + 2 clean), canary-based detection |
| L-03 | ✅ done | `next_items.py` mixes practice 70% current stage / 30% weakest earlier items (`CURRENT_SHARE`, items tagged `pool: current\|prior`); review rotates across courses. Learner-initiated mixed-topic review is not built |
| L-04 | ✅ done | `/review [course] [stage]` scoping via `review_select.py` |
| L-05 | ✅ done | deterministic ordering + session cap + remainder reported |
| L-07 | ✅ done | `next_items.py` selects practice items from item_mastery + errors; wired into course-runner Practice |
| L-10 | ✅ done | `readiness.py` + `/readiness` (band, strength, caveats; no grade) |
| C-13 | ✅ done | review options |
| N-01 | ✅ done | `plugin/generic-tutor/docs/CONTENT_CONTRACT.md` |
| N-02 | ✅ done | `min_engine_version` + gate 0 (`tutorlib/version.py`) |
| N-03 | ✅ done | `validate_courses.py --courses/--engine` + reusable `validate-courses.yml`; the caller workflow lives in the content repo |
| R-17 | ✅ done | same workflow is the documented entry point |
| S-12 | ✅ done | `misconceptions` schema + checked by `/doctor` and the content CI (not yet inside `postcompile_gate`) |
| N-05 | ✅ done | `command_words` schema; `validate_structure.exam_guidance_status` reports both optional files; `postcompile_gate` blocks one that is present but malformed (no Source line, empty, bad schema, duplicate word); compiler Step 4.8 says when to write them. The tutor does not use them yet (L-09). No course has them: they need the audit enrichment run |
| L-09 | ✅ done | `exam_guidance.py` (read-only) hands the tutor a course's `exam_technique.md` / `command_words.json`, or says plainly that the course holds none; `tutor-core/exam-technique.md` says to quote only that and never invent mark allocations, timings or what examiners look for, and not to teach technique inside a test. No course has the files yet, so today the tutor will say it holds no board guidance |
| L-06 | ✅ done | optional `card_type` on a review card: basic (default), cloze, explain_why, worked_step. `tutorlib/cards.py` owns what each needs; `deck_add.py` rejects a card misfiled under its type; `review_select.py` returns `card_type`, a `prompt` with cloze blanks shown as `[...]` and the cloze `answers`; the Anki export tags the two non-cloze types; review-scheduler and stage-recap say how to author and present each. Absent = basic, so existing decks need no migration. Not evaluated: whether the tutor presents each type well needs real sessions |
| N-13 | ✅ done | the template's option lists (`currency`, `level_basis`) and the empty rubric `source` blocks were invalid as shipped; they are placeholders now. A test fills the template and runs `validate_structure`, `validate_schema`, `coverage_check` and `postcompile_gate` on it, so template drift fails CI. `postcompile_gate` now blocks any `{{PLACEHOLDER}}` left in a course file (0 hits across the 63 library courses). `_template/optional/` holds `exam_technique.md` and `command_words.json` stubs; nothing in the tutor reads those two files yet (N-05) (v1.84.0) |
| N-14 | ✅ done | `CONTENT_CONTRACT.md` now has a *Course lifecycle* section: live, retiring, not-a-course, retired (`_historic/`) and owner scratch (`_staging/`), who moves what (only the owner moves folders; no skill or script does) and the `currency: historical` vs `_historic/` distinction. Two gaps the work exposed are closed: scans of the library listed any folder with a `course.json`, including a leftover `.import-x.tmp` (now `paths.course_ids` applies the id rule at all seven scan sites), and the auditor's `lifecycle: retiring` was prose with no code behind it (now a schema enum, `enrol.py` refuses new enrolments, `/list-courses` shows it). Building in `_staging/` and publishing by rename is N-15 (v1.85.0) |
| N-15 | ✅ done | the compiler writes into a hidden `courses/.build-<id>/` and `publish_course.py publish` runs `postcompile_gate` then renames it into place, so a course appears whole or not at all and a failed or abandoned compile is never listed or enrollable; an existing course is never overwritten; `--override "<reason>"` ships a known gap and is reported; `discard` removes only a `.build-` folder; `/doctor` reports leftover `.build-`/`.import-` folders. Compiler steps 7-7.5 rewritten within the `/add-course` budget (v1.86.0) |
| N-11 | ✅ done | `/list-courses` rows (full form) carry `provenance`: itemised source document and version, `itemised_on`, `material_vintage`, `built_on` and the last change with its title and the entry count (from `change.md` via `change_log.py`), and `last_live_recheck`. Every value may be null; long source strings are capped at 160 characters for display; the compact form is unchanged. Run against all 62 real courses: 62 have an itemised source, 40 have a change log (v1.87.0) |
| U-06 | ✅ done | `dashboard_html.py --summary-for "<recipient>"` makes a printable summary the learner chooses to share with a tutor or parent: it names its recipient, shows per-course progress, coverage and the readiness band with caveats, and omits the next step, weakest items, mistake causes and mock detail; refused when consent is `revoked`; both forms get a print stylesheet; the page language follows `identity.locale` (it was hard-coded en-GB). Not guardian oversight (PRIVACY.md keeps that out of scope): on request only, nothing is sent anywhere, the skill says never to offer one unprompted. A PDF is the reader's browser's Print to PDF; no PDF tooling is added (v1.88.0) |
| L-22 | ✅ done | `goal_map.py items|set|clear|report`: the tutor proposes which syllabus items each of the learner's `goals` means (read from the itemised course; big courses list topic areas first), the learner confirms, and the script validates (known ids only, at most 60 per goal) and stores it as `goal_map` in the learner's subjects file (progress class, atomic, locked, ledgered, schema-checked). `report` gives per goal: items taught (stage passed) versus remaining in teaching order, the next stage, observed mastery of the taught items, weakest taught items, items no stage teaches, and unmapped goals; it says that taught is not learned and the mapping is the tutor's reading. The flow lives in `journey-planner/goals.md` to hold the `/plan` budget. Optional field, so no migration (v1.89.0) |
| A-03 | 🟡 more | `criteria` suite added (18 cases, extended answers vs discrete criteria, wrong-statement credit is critical): 18/18, 0 critical; still missing: units/multi-part numerics, real learner text |
| D-03 | ✅ done | `docs/USER_GUIDE.md` |
| D-06 | ✅ done | README rewritten (<60 lines, no rotting counts) |
| D-10 | ✅ done | `docs/RUNBOOK.md` |
| L-12 | ✅ done | opt-in `target` date: `plan_target.py` + `plan_estimate.py` feasibility bands; ADR 0009; planner/`/plan` updated |
| K-20 | ✅ done | `plan_estimate.py` replaces hand-summed estimates |
| K-21 | ✅ done | `schemas/outputs/plan_estimate.json` fixes the shape of the numbers /plan may quote; the planner skill says to quote only returned fields; a test validates real output (v1.64.0) |
| L-02 | ✅ done | retrieval warm-up (`review_select.py --limit 3`) at the start of practice |
| K-04 | ✅ done | concrete accessibility rules in tutor-core; measured (compliant 18 → 25 / 36) |
| L-18 | ✅ done | three flags with concrete rules in tutor-core (dyslexia, plain language, screen reader), settable by `profile_set.py` / intake, checked by the `accessibility` eval. Reader mode, 3 samples x 4 topics, old text vs new: 3/4 -> 4/4 cases; the old text's decorative-symbol and colour-only slips (4 of 12 samples) -> 0 of 12; other modes unchanged within noise (v1.73.0). Non-English support is L-19, not here |
| L-19 | ✅ done | `identity.locale` picks the spelling (American for en-US, British otherwise) and `identity.home_language` gets a short gloss of each key term, in tutor-core; `profile_set` accepts the field; `locale` eval suite. 3 samples, old text vs new: sample accuracy 0.889 -> 0.972 (v1.80.0) |
| L-08 | 🟡 infrastructure | `assemble_paper.py`, `record_mock.py`, `exam-simulator` skill, `/mock`; no course has a question bank yet |
| K-31 | ✅ done | `exam-simulator` skill |
| P-05 | ✅ done | SessionStart hook deploys `.tutor-scripts/` and names the learners (`hook_guard.py`, v1.66.0); seen working in a live Claude Code session |
| P-06 | ✅ done | PreToolUse hook denies hand edits of script-owned files, another learner's folder and course edits during teaching commands; matrix test with a hook simulator plus a live check (v1.66.0) |
| P-07 | ✅ done | PreToolUse blocks every write under a revoked learner, tested in the matrix (v1.66.0) |
| P-08 | ✅ done | Stop hook shows the write verifier's findings; the events themselves are the ledger lines scripts already write (v1.66.0) |
| U-04 | ✅ done | `python -m toolkit status <learner>` and a Status button in the GUI, both calling `status.py`, so the numbers cannot differ from `/status`; read-only; GUI wiring checked by test, not seen on a display (v1.72.0) |
| K-30 | ➖ dropped | no separate skill: `health-status` already gives the four readouts (where am I and coverage in `/status`, weak items and readiness in `/readiness`, the page in `/dashboard`). A second skill would duplicate it and add context |
| V-09 | ✅ done | `record_grading.py`: per test attempt and rubric criterion, met / marks awarded / marks available and a hash of the rubric entry, in a new `grading_results` history table (schema v3, additive). Decision: **no answer text and no rubric wording is stored** (the privacy promise in /status audit says answers are never logged); a later audit can tell a rubric changed under an old result. Signal-class (full consent only); purged with the course (v1.77.0) |
| N-04 | ✅ done | `verify_sources.py`: every cited URL fetched once; status (ok / dead / blocked / error), HTTP code, size and a SHA-256 kept in `source_snapshots.json` (schema `source_snapshots`), previous hash and `changed` remembered, last good hash kept through an outage; **page text is hashed and discarded**, local and private addresses refused. Tested against a local server, not a real board site (this sandbox blocks them) (v1.78.0) |
| N-06 | ✅ done | `paraphrase_check.py <course_dir> [--source FILE]...`: advisory findings `long_quote` (15+ words), `many_quotes` (more than one 4+-word quotation per stage) and, given source text files, `verbatim_run` (8+ consecutive shared words outside quotes) across stage .md files, rubric criteria and item titles; read-only, wording only, a clean report is not proof of originality (v1.81.0) |
| N-12 | ✅ done | `course_bundle.py export|import`: one deterministic zip per course (sorted, fixed timestamps, sha256 manifest), no learner data (learner file names refused both ways). Import verifies hashes, rejects unlisted members, unsafe paths, newer formats and size overflows, builds in a staging folder, requires `validate_structure` clean and no BLOCKING `scan_untrusted` finding, refuses an existing id without `--replace` and keeps the old course if a replace fails (v1.82.0) |
| N-10 | ✅ done | `currency_report.py`: reads the snapshots and `last_live_recheck`; flags dead / changed / never / stale / blocked, most urgent first; report only, no network. A scheduled run of `verify_sources.py` is the owner's to set up in the private repo (v1.78.0) |
| K-10 | ✅ done | compile gate: a cited source that is not an http(s) URL blocks; snapshot coverage, dead and changed sources are advice. Checked against the 62 real courses first: none newly blocked (v1.78.0) |
| A-05 | ✅ done (selection only) | `evals/simulate.py` plays simulated learners against three selection policies; the engine's weakest-first rule ends with more items known (0.54 vs 0.48 at 40 steps, 0.82 vs 0.67 at 100) but a worse estimate on items it has not drilled (0.45 vs 0.31); rule left alone. Confidence-based pacing is not tested: any result would come from the simulator's own learning model, so it needs real learners (v1.76.0) |
| A-13 | ✅ done | eval reports carry `cost` (calls, mean / p95 seconds, system and prompt chars); `check` lists changes as `cost_changed`; per-command context stays in `context_budget.py`. Turns per stage need real sessions and are not measured (v1.75.0) |
| K-22 | ✅ done | `deck_add.py retire` / `mature` (the deck-full rejection told the tutor to retire cards but nothing could); review-scheduler has a deck-lifecycle section: creation, dedupe and caps, session cap (`review_select --limit`), retire only on the learner's yes (v1.74.0) |
| U-05 | ✅ done | health-status skill states the framing rule (stages passed of total, items covered, coverage, what is due; no streaks, points, badges, rankings, "behind" language); a test checks the generated dashboard for gamified words (v1.71.0) |
| U-07 | ✅ done | Anki export: tags course/stage/item/criterion (spaces made safe), `{{c1::...}}` fronts exported as cloze notes, every field HTML-escaped so a card can never carry an image, audio or script reference, and the .apkg's media list is empty (tested against real genanki). A dedicated card-type field waits for L-06 (v1.71.0) |
| L-21 | ✅ done | `prereq_pointer.py`: up to three candidates (weak earlier stages; prerequisite courses by state: `/review`, `/continue`, `/add-course`) from the learner's own mastery, errors and results, used at the second remediation attempt. Item-level links (N-08) would sharpen it (v1.70.0) |
| L-15 | ✅ done | `calibration.py` (opt-in; 1-5 self-rating before a test stored with the result; `report` gives overconfident / underconfident / well_calibrated after 5 ratings, never changes `confidence` or gates); runner offers it once. No eval: the model's side is one question (v1.69.0) |
| L-17 | ✅ done | runner step 7b: after a test, pass or fail, ask what was hardest and what to look at first next time; the learner's words go into the session note (`session_state.py note`, 400 characters). Skill text only, no eval (v1.69.0) |
| L-11 | ✅ done | `scaffold` per practice item (`next_items.scaffold_for`: p_mastery < 0.4 full, < 0.7 partial, else none; an unresolved error raises one level); tutor-core rule; `fading` eval, A/B at 54 samples per arm: 0.63 -> 0.91, partial band 0/4 -> 5/5, answer leaks unchanged (4 samples each); hints and accessibility unchanged at equal counts (v1.68.0) |
| L-20 | ✅ done | `session_plan.py` (phase split, remaining time, `stop_before_test` / `wrap_up` / `over_time` / `finish_the_test`) and a runner step that asks about time at phase ends. The tutor has no clock, so elapsed time is the learner's estimate (v1.67.0) |
| N-07 | 🟡 partial | `question_bank` schema + validation in doctor/content CI; compiler does not write banks |
| C-09 | ✅ done | `/mock` |
| C-10 | ✅ done | `/dashboard` + `/readiness` cover "progress" |
| U-01 | ✅ done | `status.py` + `readiness.py` + dashboard data |
| U-02 | ✅ done | plain-text rendering rules in `health-status` skill |
| U-03 | ✅ done | `dashboard_html.py` (static, no network) |
| C-11 | ✅ done | `profile_set.py` / `profile_init.py` (validated settings path; `/profile` uses it) |
| E-12 | ✅ done | `migrate_schema.py` backups + `--dry-run` |
| S-02 | ✅ done | `profile-kernel` subjects schema corrected to v5 (numeric `confidence`, structured `error_patterns`, `item_mastery`, `remediation`, ownership note) |
| K-32 | ✅ done | `session_state.py` (phase/roster/exam/notice/note) owns the last hand-written progress fields; course-runner calls it (v1.30.0) |
| E-18 | ✅ done (bug) | `record_stage_result.apply` returns a passed course from `test_pending_convergence` to `active` (latent convergence bug) |
| P-09 | ✅ done | allowlist guidance for the scripts directory, with what not to allow (`docs/INSTALL.md`) |
| P-14 | 🟡 partial | Python requirement, Windows `py -3` and the failure mode documented; no in-plugin detection when `python3` is absent (nothing can run to detect it) |
| P-17 | ✅ done | compatibility table states what was exercised and what was not (Cowork untested) |
| P-18 | ✅ done | upgrade, roll-back and uninstall paths, including what stays in the data folder |
| X-07 | ✅ done | `tools/scan_repo.py` (credentials, non-reserved e-mail addresses, private-content paths in tracked files) with tests; CI step |

| V-10 | ✅ done | `recent_activity.py` + `/status audit`; template-coverage test |

| A-07 | ✅ done (checks) | `tutorlib/overlap.py`, blocking gate check, `worksheet_check.py`; an eval of paraphrase-level leakage is not built |
| K-26 | ✅ done | `stage-recap` runs `worksheet_check.py` before handing over the worksheet |
| E-19 | ✅ done | golden snapshots identical under 6 different `PYTHONHASHSEED` values; outputs are sorted |
| E-26 | 🟡 partial | files renamed by topic; directory split deliberately not done (see DESIGN_NOTES v1.39.2) |

| P-12 | 🟡 partial | one-time folder-access confirmation by script (`confirm_access.py`); detection of a wrong folder is in `resolve_root.py`/`/doctor` |

| K-19 | ✅ done | `drop.md` split earlier; planner now has no hand writes: `roster_apply.py drop/advance/lock` (v1.41.0) |
| K-16 | ✅ done | profile-kernel SKILL is 83 lines; schema blocks live in `profile-schema.md`; `confirm_access.py` replaces the hand-written access file |
| K-18 | ✅ done | `/erase` needs the typed phrase `ERASE <user_id>`; `/restore` and `/backup` read back which learner; no destructive command infers the learner |

| A-11 | ✅ done (adapted) | `rubric_lint.py` checks wording/threshold/locator; mark allocation not applicable to the real rubric shape |
| P-10 | ✅ done | `docs/INTEGRATIONS.md`: operator, data sent, trust level, how to decline |
| P-11 | ✅ done | already specified: a connector not marked `connected` is treated as unavailable (runner) and the course runs from model knowledge with a caveat; documented for learners in `INTEGRATIONS.md` |
| X-06 | ✅ done | review recorded (source, licence, operator unverified, data sent, no credentials) |

| X-05 | ✅ done | `purge_history.py` (history only / one course), typed confirmation, dry run first |
| E-15 | ✅ done (v2) | history DB schema v2 with in-place migration; see CHANGELOG 1.44.0 |
| E-10 | ✅ done | opt-in `--envelope` on every script (v1.32.0); default stays legacy until skills stop parsing the old keys |
| E-11 | ✅ done | closed code set `E_USAGE … E_INTERNAL`, inferred from the message (v1.32.0) |
| R-16 | ✅ done | `docs/` and `tools/` are in place; plugin layout unchanged |
| R-15 | 🟡 partial | branch strategy is in `CONTRIBUTING.md`; branch protection is the owner's to configure |
| R-13 | 🟡 partial | the docs lint fails if versions disagree, but three files are still edited by hand |
| C-03 | ✅ done | ids validated by `tutorlib.ids` in `profile_init.py`; an existing id is refused with a message |
| C-04 | ✅ done | `/drop` previews first (`roster_apply.py drop --preview`: previous state, courses that would wake, nothing written), then drops after a clear yes (v1.61.0) |
| S-14 | ✅ done | notes ≤400 chars via stdin; profile edits go through a whitelist; ledger holds ids only |
| D-12 | ✅ done | `evals/README.md` covers running, adding cases, reading reports |
| D-08 | ✅ done | `docs/CONTRIBUTING-DEV.md`: checklists for a script, schema, skill, command, eval case and task, each naming the check that fails without it; linked from CONTRIBUTING |
| D-11 | ✅ done | toolkit README refreshed (stale version and flow removed, command table); docs lint fails if the table and `toolkit/__main__.py` COMMANDS differ |
| X-08 | 🟡 partial | backups default to outside the learner folder; `INSTALL.md` warns about synced folders and personal data; no encryption |
| R-13 | ✅ done | `tools/bump_version.py` edits all three version carriers and the deployed copy together; the lint still catches a hand edit that drifts |
| S-11 | ✅ done (adapted) | the real `change.md` shape is the format; `change_log.py` parses it, the gate notes deviations (v1.46.0) |
| S-08 | ✅ done | `validate_schema.py --course-dir` + `invariants.py` replace prose field checks in the auditor (v1.47.0) |
| E-20 | ✅ done | `state.save` validates before write at 19 call sites, blocking only introduced errors (v1.48.0); readers already use `state.load` |
| R-14 | ✅ done | third-party actions pinned by commit SHA with the version in a comment; Dependabot (weekly) keeps them current. The Claude CLI installed in the validate job is still unpinned |
| V-07 | ➖ dropped | a hash chain would only detect tampering by the machine's owner, who can already edit every file; the ledger exists to catch a model skipping a script call, which `verify_session.py` does without it |
| S-09 | 🟡 partial (by decision) | migration stays one idempotent normaliser, now with a schema post-check (`valid_after`); per-version steps deliberately not built (DESIGN_NOTES v1.49.0) |
| E-23 | ✅ done | toolkit uses `tutorlib.paths.resolve_root` and takes `--root`; GUI handler and startup errors now show a plain-language dialog (`core.describe_error`), tested by running `gui.pyw`'s `main()` against a stub tkinter. Not seen on a real display (v1.65.0) |
| E-02 | ✅ done | `tutorlib`: atomic_io, filelock, consent, ids, paths, cli (envelope inside), state, schema, ledger, untrusted, version, overlap |
| E-08 | ✅ done | every operation that turns an id into a path goes through `tutorlib.ids` / `paths` (erase, export, backup, restore, purge, init, enrol, roster) |
| S-13 | ✅ done | id rules enforced wherever an id becomes a path or a command argument; SQL uses parameters |
| K-01 | ✅ done (adapted) | per-phase 'done when' criteria in tutor-core; eval A/B shows no regression (v1.51.0) |
| K-02 | ✅ done | nothing numeric to replace: confidence is described qualitatively and sourced from `confidence_update.py` |
| K-06 | ✅ done | numbered session lifecycle first in `course-runner`, one call per step (v1.52.0) |
| K-07 | ✅ done (adapted) | resume rules for a cut-off test or diagnostic; `current_phase` carries the state, no new field (v1.52.0) |
| K-08 | ✅ done | material-change criteria, 4-page bound, entry format; `recheck` eval 14/14 (easy set) (v1.53.0) |
| K-13 | ✅ done (adapted) | Tier 1 is a table (check · source · auto-fix · report); size target not met (124 lines) because the judgment tiers are real content (v1.54.0) |
| K-14 | ✅ done | `audit_run.py` JSON report + diff against the last report; human summary led by the diff (v1.54.0) |
| K-35 | ✅ done | 16 version tags and history pointers removed from skills; docs lint flags new ones (v1.55.0) |
| K-11 | ✅ done (adapted) | option/tier/awarding-body decision table in the compiler; no script fixtures (the choice is made in conversation) (v1.56.0) |
| K-12 | ✅ done (policy) | one quotation/paraphrase policy for all course files; automated detection is `paraphrase_check.py` (N-06) |
| K-17 | ✅ done (adapted) | intake question→key→valid-values table; `profile_init.py` already validates (no new script needed) (v1.57.0) |
| K-34 | ✅ done (adapted) | one spelling in prose, glossary entry, lint for the US form; other core terms were already consistent (v1.58.0) |
| C-14 | ✅ done | `list_courses.py` + `--status/--level/--standalone/--compact` (v1.59.0) |
| N-07 | 🟡 partial | question-bank schema and `assemble_paper.py` existed; `exam_to_bank.py` now proposes a starter bank from each course's own `exam/exam.md` (286 of 369 items convert; 30 courses have none), `enrich_plan.py` reports what each course lacks, and the auditor has an enrichment tier (v1.63.0). Authoring further items needs the audit run on a real course |
| K-03 | ✅ done (by measurement) | safety eval grown from 12 to 22 cases (real situations with no amount or date: executor, tenant, settlement, expense, hearing; study negatives with names, amounts and exam framing); the unchanged guard scored 22/22 over 3 samples with no critical failure, so no trigger list was added to the skill (it would cost context for no measured gain). New baseline recorded; add a case here if a real miss turns up |
| C-15 | ✅ done | argument hints: snake_case placeholders, `--kebab` flags, `[ ]` = may be omitted (the command asks); `/audit` and `/list-courses` now declare theirs; `test_skill_split.CommandNaming` holds it. No aliases added: the names were already consistent (v1.62.0) |
| C-12 | ✅ done | `--report-only`, `--course`, `--tier` documented in the command; `audit_run.py --course` scopes the report (v1.60.0) |

## Suggested first sprint (Phase 0, ~1–2 weeks)

1. **Foundations:** R-01, R-02, R-03, R-04, R-06, R-07, R-10, R-14, R-18, X-07, X-10
2. **Truth about the data:** S-01 → S-02, S-03, S-04, S-10 (fixes the verified drift), D-04
3. **Docs that can't rot:** D-07 (docs lint), K-00, D-01 + D-09, D-02, X-04, X-09
4. **Risk spikes:** P-04 (hooks), L-01 (pedagogy rationale)
5. Decisions in PLAN §10 are resolved; Phase 1 is unblocked once Phase 0 lands.

## Remaining waves

Everything not done sits in exactly one wave (`tools/tasks_status.py --check` fails if a task is missing, so nothing can fall out of the plan). Waves are ordered by what unblocks what, not by the old phase numbers; run them in order unless noted.

| Wave | Theme | Tasks | Why this order |
|---|---|---|---|
| 1 | Finish the engine | E-09 E-26 S-09 R-15 | Small, scriptable, testable; removes the last hand-wired plumbing before skills are rewritten on top of it |
| 2 | Skill clarity | K-05 K-09 | Prose restructures; each should be measured by an eval where one exists, and the context budget only goes down |
| 3 | Optional Claude Code hooks | P-12 P-14 P-16 | Claude Code only (Cowork has no hooks, ADR 0001); a safety net on top of scripts that already enforce the rules |
| 4 | Learning design | L-06 L-08 L-09 K-24 N-07 | Teaching features; each needs a documented skill section plus tests or evals |
| 5 | Measurement | A-03 A-12 A-14 L-14 | Needs real learner data or several model tiers; some items cannot start until the system has been used for a while |
| 6 | Content pipeline | N-05 N-08 N-09 X-08 | Needs decisions about sourcing. The largest gap, `misconceptions.json` (0 of 1,253 stages), needs no new code: it is an audit enrichment run (course-auditor Tier 3) over courses built before compile step 4.75, run where the board sites are reachable |
| 7 | Surfaces & deployment | B-01 B-02 B-03 B-04 B-05 B-06 B-07 | Direction accepted, build patterns not yet designed (design step first in every task). B-01 then B-02; the role work comes last. See ADR 0010 |


## Where we are

Derived by `tools/tasks_status.py` from the tables, the progress log and the waves above; regenerate with `--write`.

### By phase (the original plan's ordering)

| Phase | Tasks | Done | Partial | Open or deferred |
|---|---|---|---|---|
| 0 Foundations | 36 | 35 | 1 | 0 |
| 1 Engine hardening | 35 | 32 | 3 | 0 |
| 2 Plugin surface & trust | 76 | 72 | 3 | 1 |
| 3 Assessment & evals | 17 | 16 | 1 | 0 |
| 4 Learning design | 34 | 30 | 2 | 2 |
| 5 Content & ecosystem | 20 | 14 | 1 | 5 |
| 6 Surfaces & deployment | 7 | 0 | 0 | 7 |

### What remains, by wave

| Wave | Theme | Not yet done | Of which started |
|---|---|---|---|
| 1 | Finish the engine | 4 | 4 |
| 2 | Skill clarity | 2 | 1 |
| 3 | Optional Claude Code hooks | 3 | 2 |
| 4 | Learning design | 3 | 2 |
| 5 | Measurement | 4 | 1 |
| 6 | Content pipeline | 3 | 1 |
| 7 | Surfaces & deployment | 7 | 0 |

### By workstream

| Workstream | Tasks | Done | Partial | Deferred / dropped | Open |
|---|---|---|---|---|---|
| R Repo | 18 | 17 | 1 | 0 | 0 |
| E Engine | 26 | 24 | 2 | 0 | 0 |
| S Schemas | 14 | 13 | 1 | 0 | 0 |
| K Skills | 36 | 32 | 1 | 2 | 1 |
| C Commands | 15 | 15 | 0 | 0 | 0 |
| P Plugin surface | 19 | 16 | 2 | 0 | 1 |
| V Trust & verification | 10 | 8 | 0 | 2 | 0 |
| L Learning design | 22 | 20 | 1 | 0 | 1 |
| A Assessment & evals | 14 | 11 | 1 | 0 | 2 |
| U Learner visibility | 7 | 7 | 0 | 0 | 0 |
| N Content pipeline | 15 | 12 | 1 | 0 | 2 |
| X Security & privacy | 10 | 9 | 1 | 0 | 0 |
| D Documentation | 12 | 12 | 0 | 0 | 0 |
| B Surfaces & deployment | 7 | 0 | 0 | 0 | 7 |
| **Total** | **225** | **196** | **11** | **4** | **14** |
