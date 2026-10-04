# Changelog

User-visible history of the generic-tutor plugin, newest first. The reasoning behind each change lives in [`plugin/generic-tutor/DESIGN_NOTES.md`](plugin/generic-tutor/DESIGN_NOTES.md) (to be split into decision records, task D-01). Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); version = `plugin.json`.

## [Unreleased] — redesign programme (see `docs/PLAN.md`)
### Added
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
