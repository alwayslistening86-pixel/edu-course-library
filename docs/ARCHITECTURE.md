# Architecture (D-02)

## Shape
A **markdown layer** (commands + skills) tells Claude *when* to do things and *how to talk*. A **script layer** (`plugin/generic-tutor/scripts/`, stdlib Python) owns every deterministic decision and every state write. **State** is plain JSON per learner plus shared course content, with an append-only SQLite history on the side.

```
learner ──► Claude (Cowork/Code) ── reads ──► commands/ skills/        (behaviour, tone, procedure)
                  │
                  ├── calls ──► /EDU/.tutor-scripts/*.py               (gates, math, validation, writes)
                  │                 │
                  │                 ├── reads  /EDU/courses/<id>/      (shared, canonical, sourced)
                  │                 ├── reads/writes /EDU/profile/<user>/{student_profile.json, subjects/*.json}
                  │                 └── appends /EDU/profile/<user>/tutor.sqlite3   (history, never read back)
                  └── web search/fetch ──► specs (compiler, live recheck)   [untrusted input]
```
`.tutor-scripts/` is a deployed copy of `plugin/generic-tutor/scripts/`, installed by `bootstrap_scripts.py` on `/run` (version-gated). CI fails if the two drift.

## Session lifecycle (what runs when)
1. `/run <user>` → bootstrap scripts → load profile → `slot_advance.py` (once per session).
2. `/continue <course>` → `gate_check.py` (folder access → grounding → enrollment/prerequisites → recheck needed? → convergence) → notices → optional live recheck → teach lesson/practice → (convergence) → test → `record_stage_result.py` → confidence/mastery/error scripts → `stage-recap` seeds the review deck.
3. `/review` → `review_math.py apply` per card.
4. `/plan`, `/drop`, `/add-course`, `/audit`, `/export`, `/erase`, `/profile`, `/list-courses` as described in each skill.

## Who owns what
| Concern | Owner |
|---|---|
| Gate decisions (access, grounding, enrollment, prerequisites, convergence) | `gate_check.py` → `cohort_status.py`, `prereq_check.py`, `roster_check.py` |
| Level lock / ledger | `roster_check.py`, `resume_enrollment.py`, `cohort_status.py` |
| Stage result, current stage | `record_stage_result.py` |
| Confidence | `confidence_update.py` |
| Errors / diagnostics | `diagnostic_gate.py`, `error_log.py`; cause is **model judgment** |
| Mastery | `item_mastery.py` |
| Remediation | `remediation_state.py` |
| Review scheduling | `review_math.py` |
| Coverage | `coverage_check.py` |
| Structure / post-compile gate / publishing | `validate_structure.py`, `postcompile_gate.py`, `publish_course.py` |
| Migration | `migrate_schema.py` |
| History DB | `sqlite_store.py` |
| Grading, teaching, discovery, compiling, audit judgment | the model, guided by skills |

Field-level owners: [`DATA_MODEL.md`](../plugin/generic-tutor/docs/DATA_MODEL.md). Terms: [`GLOSSARY.md`](GLOSSARY.md).

## Trust boundaries
- **Learner folder isolation** is structural (one folder per learner); enforcement in code is task E-08.
- **Model vs script:** the model is trusted to *call* scripts, not to compute; omissions are the open risk (V-xx ledger/verifier).
- **Untrusted inputs:** web content (specs, rechecks), connector output, and learner text. Policy: X-01..X-03.
- **Platform:** Cowork has no hooks ([ADR 0001](adr/0001-hooks-and-platform-support.md)); safety is script-level.

## Known architectural debt
Per-script argv parsing and path handling (→ `tutorlib`, E-02..E-09); non-atomic writes (E-03); consent enforced in prose (E-05); schemas in prose (S-05); 148–227-line skills mixing procedure and schema (K-05, K-09).
