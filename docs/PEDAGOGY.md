# Pedagogy rationale (L-01)

What each mechanic in the tutor is for, how strong the supporting evidence is, and what is a design judgment rather than a finding. Evidence labels: **strong** (replicated, many settings), **moderate** (good evidence, context-dependent), **weak** (plausible, thin or mixed), **design choice** (no claim of evidence). This is a summary from general knowledge of the literature, not a systematic review; it should be revisited with citations when evals (Phase 3) exist.

| Mechanic | Where | Purpose | Evidence | Notes / risks |
|---|---|---|---|---|
| Spaced review of past material | `review-scheduler`, `stage-recap` cards | Slow forgetting | **strong** (spacing effect) | Slot-based scheduling approximates elapsed time; five sessions in a day are not distinguishable from five weeks (accepted trade-off, see FSRS note in DESIGN_NOTES) |
| Retrieval practice (cards, test-as-learning) | review passes, practice | Recall strengthens memory more than re-reading | **strong** | Cards only start after a stage pass; in-stage retrieval is task L-02 |
| Mastery gating (no test until ready; fail ⇒ remediate, don't advance) | `course-runner` | Prevent building on gaps | **moderate** | Gating can frustrate; escalation after 2 remediation attempts is a design choice |
| Phase order: explain plainly → practise with framework → test | `tutor-core` | Reduce load before demanding structure | **moderate** (worked examples, expertise-reversal) | "No framework in lesson" is a design choice, not a finding |
| Elicit before explaining (diagnosis) | `tutor-core`, `diagnostic_gate.py` | Respond to the actual cause of an error | **moderate** (formative feedback, misconception research) | Cause classification is model judgment; accuracy unmeasured (A-04) |
| Cause-specific response (slip vs misconception vs prerequisite …) | taxonomy | Avoid re-teaching what's known | **moderate** | Taxonomy is a design simplification |
| Per-item Bayesian knowledge tracing | `item_mastery.py` | Track which items are weak | **moderate** (established in ITS research) | Parameters (slip/guess/transit) are fixed defaults, not fitted; few observations per learner |
| Worked examples early, faded later | pacing rules | Lower cognitive load for novices | **strong** for novices | Fading policy is informal (L-11) |
| Interleaving | not implemented | Better discrimination between problem types | **moderate** | Task L-03 |
| Cohort convergence (test together) | `course-runner` | Keep a level's courses in step | **design choice** | No learning evidence; exists for roster/level logic |
| Pairing contrasting subjects in one session | `journey-planner` | Reduce fatigue | **weak** | Documented as a heuristic in the skill |
| Confidence number steering pace | `confidence_update.py` | Adjust speed/scaffolding | **weak** | A proxy from test outcomes; calibration against self-report untested (L-15) |
| Honest grading (no softening) | `tutor-core` | Accurate feedback | **moderate** | Grading accuracy itself unverified (A-03) |
| Coverage disclosure | `course-runner` | Don't overstate readiness | n/a (integrity) | |
| Take-home worksheet, untracked | `stage-recap` | Optional extra practice | **design choice** | Not tracked by design |

## Principles drawn from this
1. Prefer mechanics with strong evidence (spacing, retrieval, worked examples); add the missing ones (in-stage retrieval, interleaving) before inventing new ones.
2. Label design choices as such in skills and to the learner; do not claim evidence we do not have.
3. Anything that steers pacing from a derived number (confidence, mastery) must be evaluated, not assumed (Phase 3/4).
