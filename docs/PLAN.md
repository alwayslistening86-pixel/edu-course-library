# EDU Course Library — Redesign & Improvement Plan

Status: **draft for review** · Branch: `claude/redesign-roadmap` (from `main` @ 51bc6e3) · Companion: [`TASKS.md`](TASKS.md)

This plan covers the whole repo: the `generic-tutor` engine (scripts, schemas, tests, CI), the Claude Cowork plugin surface (manifest, 12 commands, 10 skills, hooks/MCP), the pedagogy it implements, and the way the repo is built, released and documented. `TASKS.md` breaks every item into numbered, individually shippable tasks.

---

## 1. Where we are (audit baseline)

### What exists and works
| Area | State |
|---|---|
| Engine | ~4k lines stdlib-only Python in `plugin/generic-tutor/scripts/` (19 scripts + `toolkit/`), deployed by `bootstrap_scripts.py` to `.tutor-scripts/`. 298 tests pass (≈10 s). |
| Plugin surface | 12 commands (thin wrappers), 10 skills (≈1.1k lines of markdown), `.mcp.json` with two suggested UK-legal MCP servers. |
| Pedagogy | Phase-gated teaching (lesson → practice → test), cohort convergence, BKT item mastery, SM-2-lite slot-based review, diagnostic gate with cause taxonomy, remediation state machine. |
| Safety | Honesty/coverage rules, real-situation guard for regulated professions, supervision note for physical-risk practicals. |
| CI | Unit tests + new deployed-copy drift check. |
| Docs | README, plugin README, 1,062-line `DESIGN_NOTES.md` (changelog + rationale mixed). |

### Gaps found in this audit (evidence-based)
**Documentation / contract drift**
- `profile-kernel` documents `subjects/*.json` with `"confidence": "low|medium|high"` and `error_patterns: ["string"]`; the scripts and `course-runner` use a numeric `confidence` in [0,1] and structured error entries. The skill that defines the schema is wrong about it. There is no machine-readable schema anywhere.
- Skill headings carry private version numbers (v3, v6, v7, v8) unrelated to the plugin version (1.12.0).
- `sqlite_store.py` is not mentioned by any skill; `/export` omits `tutor.sqlite3`, so export is incomplete and the history DB is a hidden data store.
- `/erase` demands an "explicit confirmation token" but never defines it.
- The README/plugin README disagreed with reality until fixed today; there is no check that docs match code.

**Engine robustness**
- JSON state files are written with plain `open(..., "w")`; no script uses atomic write (`tempfile` + `os.replace`) or file locking. A crash mid-write corrupts a learner's progress.
- `consent.status` (`limited`/`revoked`) is enforced in prose only; only `slot_advance.py` checks it. `error_log.py`, `item_mastery.py`, `confidence_update.py`, `review_math.py`, `sqlite_store.py` write regardless.
- No shared library: path handling, JSON load/save, error envelope and CLI parsing are re-implemented per script (≈19 copies of `usage:` handling, hand-rolled argv parsing).
- `/EDU/` is a documented placeholder resolved by the model, not by code, in every skill invocation.
- Python version support is undeclared; CI runs 3.12 only; no lint/type/format tooling.
- Tests are organised by release (`test_v130.py` …) not by module; the fuzz suite is not run in CI.

**Trust / verification**
- The known residual risk from v1.10.0 is unaddressed: nothing verifies the model actually *called* the state-writing scripts. All state integrity depends on the model following markdown.
- No hooks are shipped; the plugin cannot enforce anything at tool-call time.
- The compiler and live-recheck ingest untrusted web content that is then written to `change.md`/course files, with no stated prompt-injection handling.

**Pedagogy / assessment**
- No evaluation harness for teaching quality or grading accuracy; grading is unverified model judgment.
- Retrieval practice starts only after a stage pass; no in-stage retrieval, no interleaving, no learner-initiated mixed review.
- No exam-simulation: timing, past-paper conditions, grade-boundary estimates, exam technique.
- Misconceptions layer (`misconceptions.json`) is schema-only, unseeded.
- Accessibility is limited to teaching-style hints; no output-format options.

**Learner visibility**
- No in-session progress view beyond `/profile`; the desktop toolkit is read-only and separate.

**Repo / release**
- No packaging automation (manual `zip`), no marketplace manifest, no release workflow, no changelog separate from design notes, no `CLAUDE.md`, `CONTRIBUTING`, issue/PR templates, or lint/pre-commit.
- Third-party MCP endpoints (`*.fly.dev`) are referenced without pinning, provenance or opt-out documentation.

---

## 2. Goals and non-goals

**Goals**
1. **Correctness you can verify** — every persistent field has a schema; every write is atomic, consent-aware and, where possible, enforced by code/hooks rather than prose.
2. **Skills that are precise and testable** — each skill has a contract (inputs, outputs, state it owns, scripts it calls, failure modes) and a lint that proves the contract matches the code.
3. **A tutor that demonstrably teaches** — evals for grading accuracy, diagnostic classification and session quality; stronger learning-science features (retrieval, interleaving, exam practice).
4. **A repo others (and future-you) can maintain** — lint/type/format, single-source packaging, release automation, clear docs split (changelog / design rationale / user guide / contributor guide).
5. **Honest scope** — keep the slot-based, no-calendar, self-hosted, single-learner-first design unless a task explicitly revisits it.

**Non-goals (explicit)**
- Multi-tenant hosting, accounts/auth, XP/streak gamification (already rejected in `DESIGN_NOTES.md`).
- Bundling course content into this public repo (stays in `edu-courses-private`).
- Replacing SM-2-lite with FSRS (decision recorded; revisit only if review logs justify it — see task `L-14`).
- Anything requiring calendar dates for scheduling.

---

## 3. Design principles for the redesign

1. **Code owns state, markdown owns judgment.** Anything deterministic (gates, arithmetic, writes, validation) lives in tested code; skills only describe *when* to call it and how to *talk* about results.
2. **One schema, many consumers.** JSON Schema files are the single definition used by scripts, migrations, the auditor, docs and tests.
3. **Fail closed on learner data.** Atomic writes, backups before migration, consent checks inside the scripts.
4. **Enforce, don't instruct** where the platform allows (plugin hooks, permissions), and *detect* where it doesn't (session-end verifier comparing expected vs. actual writes).
5. **Every claim in docs is checkable.** Docs lint (links, script names, versions, command↔skill wiring) runs in CI.
6. **Small, reversible steps.** Each task is one PR-sized change with an acceptance check; schema/format changes ship with a migration and a rollback note.

---

## 4. Target architecture

```
repo/
  plugin/generic-tutor/
    .claude-plugin/plugin.json          # manifest (+ marketplace.json at repo root)
    commands/            # thin wrappers; argument validation documented
    skills/              # each: contract header + procedures; no schema prose (links to schemas/)
    hooks/               # NEW: SessionStart (bootstrap), PreToolUse (consent/path guard), Stop (write verifier)
    schemas/             # NEW: JSON Schema for every persisted file + CLI output envelopes
    scripts/
      tutorlib/          # NEW: paths, atomic_io, consent, envelope, cli, schema
      <existing scripts, refactored onto tutorlib>
      toolkit/
    evals/               # NEW: graded-sample fixtures, diagnostic transcripts, harness
    tests/               # reorganised by module + schema conformance + docs lint + fuzz
    docs/                # user guide, contributor guide, ADRs, changelog
  tools/                 # NEW: lint_docs.py, build_plugin.py, release helpers
  .github/               # workflows: test matrix, lint, docs-lint, package, release
```

Key changes:
- **`tutorlib`** — shared module for path resolution (`EDU_ROOT` resolved once in code, not in prose), atomic JSON IO with `.bak` rotation, consent gate, uniform `{ok, data, error}` envelope, argparse-based CLI.
- **`schemas/`** — authoritative definitions; `migrate_schema.py` and `course-auditor` validate against them.
- **Hooks** — `SessionStart` runs bootstrap; `PreToolUse` blocks writes outside the active learner folder and honours consent; `Stop` runs a **write verifier** that compares the session's recorded events against state and flags a missed `apply` call.
- **Skill contracts** — standard front-matter block (owns / reads / calls / emits / never) per skill, checked by `tools/lint_docs.py`.
- **Evals** — offline fixtures (graded answers vs. mark schemes, misconception classification cases) plus an optional model-in-the-loop harness, run manually/nightly, not in PR CI.

---

## 5. Workstreams

| ID | Workstream | Outcome |
|---|---|---|
| **R** | Repo foundations & release | Lint/type/format, packaging, release, templates, `CLAUDE.md`, docs split |
| **E** | Engine hardening (`tutorlib`) | Atomic IO, consent in code, shared CLI/envelope, path resolution |
| **S** | Schemas & migrations | JSON Schema for all files; docs/code drift eliminated |
| **K** | Skills (10 existing) | Per-skill contract, correctness fixes, simplification |
| **C** | Commands (12 existing + new) | Argument validation, help, new commands |
| **P** | Cowork plugin surface | Manifest, marketplace, hooks, MCP, permissions, install flow |
| **V** | Trust & verification | Write verifier, audit trail, session-end reconciliation |
| **L** | Learning design | Retrieval, interleaving, exam practice, accessibility, misconceptions |
| **A** | Assessment quality & evals | Grading calibration, diagnostic accuracy, regression evals |
| **U** | Learner visibility | In-session progress, dashboards, toolkit upgrades |
| **N** | Content pipeline | Private-repo contract, compiler quality, currency monitoring |
| **X** | Security & privacy | Prompt-injection handling, erasure/export completeness, MCP provenance |
| **D** | Documentation | User guide, contributor guide, ADRs, changelog |

---

## 6. Phasing

Phases are ordered by risk reduction first, capability second. Each phase ends in a tagged release and a `DESIGN_NOTES`/changelog entry.

### Phase 0 — Foundations (v1.13) · *low risk, unblocks everything*
Repo tooling (R), docs lint, `CLAUDE.md`, test layout, schema extraction **without behaviour change**, fix known doc drift (S-01…S-04, K quick fixes). Exit: CI has lint + type + docs-lint + test matrix; drift items closed.

### Phase 1 — Engine hardening (v1.14) · *data safety*
`tutorlib`, atomic writes, backups-before-migrate, consent enforced in code, path resolution in code, argparse CLIs, envelope. Exit: no script writes non-atomically; consent matrix tested for every writer; fuzz suite in CI.

### Phase 2 — Plugin surface & trust (v1.15) · *enforcement*
Manifest/marketplace, hooks (bootstrap, guard, write-verifier), per-skill contracts, command argument validation, `/status`, `/help`, `/backup`, `/restore`. Exit: a skipped `apply` call is detected at session end; install is one step.

### Phase 3 — Assessment & evals (v1.16) · *prove it teaches*
Eval harness, grading calibration set, diagnostic classification set, misconception seeding pipeline, regression gating. Exit: baseline accuracy numbers recorded; PRs touching skills can be evaluated.

### Phase 4 — Learning design (v1.17–1.18) · *better teaching*
In-stage retrieval, mixed/interleaved review, exam simulation + grade estimation, deadline-aware planning (optional, opt-in, still no calendar writes), accessibility output modes, learner-facing progress view. Exit: each feature behind a documented skill section with tests/evals.

### Phase 5 — Content & ecosystem (v1.19+) · *sustainability*
Content-repo contract + validation as a reusable action, currency monitoring, compiler quality gates, third-party MCP provenance, optional SQLite-backed analytics (only if justified by data).

---

## 7. Cross-cutting rules for every task

- One task = one PR; title prefixed with the task ID (e.g. `E-03: atomic JSON writes`).
- Add/adjust tests in the same PR; schema or format change ⇒ migration + `migrate_schema.py` test + rollback note.
- Plugin behaviour change ⇒ bump `plugin.json` version, update `.tutor-scripts/` via the bootstrap path (CI drift check enforces), add a changelog entry.
- No task widens scope silently; discovered work becomes a new task ID in `TASKS.md`.

## 8. Risks and mitigations

| Risk | Mitigation |
|---|---|
| Refactor onto `tutorlib` regresses behaviour | Characterisation tests first (E-01), then migrate one script at a time; keep CLI output byte-compatible until Phase 2 envelope switch |
| Schema extraction exposes more drift than expected | Treat every mismatch as a finding in `S-xx`; fix code *or* docs deliberately, never silently |
| Hooks unavailable/behave differently in Cowork vs. Claude Code | P-04 spike first; verifier degrades to "report at next `/run`" if hooks absent |
| Evals are expensive / non-deterministic | Keep out of PR CI; fixed seeds + recorded baselines; human spot-check protocol (A-06) |
| Private content repo drift | Contract tests + reusable validation workflow (N-03) |
| Scope explosion | Phase gates; anything not in `TASKS.md` needs a new ID and a phase assignment |

## 9. Success measures

- 0 non-atomic state writes; 100 % of writers consent-gated and tested.
- Docs-lint green: every script/command/skill reference resolves; skill contracts match code.
- Missed-`apply` detection rate ≥ 95 % on injected-fault sessions (V-05).
- Grading eval: agreement with reference marks within agreed tolerance (A-03 sets the target after baseline).
- CI wall-clock < 2 min for PR checks; release = one tag.
- Fresh-machine install to first `/run` ≤ 5 minutes following the user guide (D-03).

## 10. Decisions (resolved)

The owner delegated these; the recommended option was adopted in each case.

| # | Decision | Outcome | Consequence |
|---|---|---|---|
| 1 | Python floor | **3.10+**; CI matrix 3.10–3.13 | `pyproject.toml` declares `requires-python >=3.10`; no 3.11+-only syntax in scripts |
| 2 | Hooks for enforcement | **Yes**, with a detect-and-report fallback | P-04 spike first; if a hook event is unavailable on a surface, the write verifier (V-03) reports at the next `/run` instead of blocking |
| 3 | Eval spend | **Yes, manual/nightly only**, small budget; never in PR CI | Reference marks start from self-authored sample courses (A-02) drafted by Claude; owner only spot-checks (A-06) |
| 4 | Deadline-aware planning | **Yes, opt-in** | One optional `exam_date` field with expiry; planner converts it to slots-needed vs slots-available; no calendar scheduling inside the plugin |
| 5 | Repo layout | **Yes**: `docs/`, `tools/`, `plugin/` stays | R-16 proceeds; docs-lint (D-07) guards links |

Other defaults taken without asking: vendoring a tiny stdlib JSON-Schema validator rather than adding a dependency (S-06); no hash-chained ledger unless V-05 shows a need (V-07); backup encryption is optional and off by default (X-08); the `/erase` token is the exact phrase `ERASE <user_id>` (K-27).
