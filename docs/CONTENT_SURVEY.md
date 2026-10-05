# What the content repo actually holds (survey of 5 Oct 2026)

Aggregate facts only — no course text. Produced by running this repo's own tools (`validate_courses.py`, `postcompile_gate.py`,
`coverage_check.py`, `validate_structure.py`, `audit_status.py`) over the private content repo. Re-run them to refresh; do not hand-edit counts.

| Fact | Value |
|---|---|
| Courses | 62 (GCSE, A-level, vocational/professional, degree-level, language, programming certificates) |
| Stages | 1,253 (3 files each: `lesson.md`, `practice.md`, `test.md`) |
| Per course | `course.json`, `curriculum_map.json`, `rubric.json`, `connectors.md`, `exam/`, `change.md` (45 courses) |
| Passing `postcompile_gate` | 62 / 62 can ship; `grounding_status: verified` and `currency: live` on all 62 |
| Syllabus-item coverage | all 62 declare `full`; 5,325 of 5,751 itemised syllabus items are taught, the rest are declared exclusions |
| Lesson length | median 694 words, p90 1,071, max 2,039 |
| Practice file | median 171 words: 3–4 scenarios per stage to "use or adapt", not an item bank |
| Test file | median 472 words: one scenario per stage, graded against `rubric.json` (median 4 criteria per stage) |
| Exams | enabled on all 62; **no `question_bank.json` in any course** |
| `misconceptions.json` | **none of the 1,253 stages has one** (the diagnostic and remediation paths cite them) |
| Audit stamps | 22 courses carry a `last_audited_plugin_version` from an earlier release, 40 carry none; 21 were never live-rechecked (`audit_status.py`) |

## What a brand-new learner can start (gate_check over all 62, fresh profile)
After the library-level folder confirmation, 35 courses can start immediately (all level-2 and standalone ones); 27 are held at gate 3 by `requires_complete` prerequisites (A-levels need their GCSEs, degrees need A-levels). That is the designed no-prior-credit policy (`course-compiler` Step 0.6): a learner who already holds a GCSE still has to complete it here first. 17 courses carry a due learner notice and 16 require a coverage disclosure at session start.

## Test integrity (checked 5 Oct 2026, v1.39.0)
Across all 1,253 stages no graded test item (806 stages with several, 447 with one scenario) appears word for word in that stage's `practice.md` or `lesson.md`. 15 stages in 4 courses share a 20-word run between test and practice (templated question stems and shared data tables, not copied items). The gate now blocks a verbatim item and notes shared runs.

## What the survey changed in the engine (v1.35.1)
Running the engine over real content found three defects that the fixtures could not:
1. The injection scanner's `exfiltration` rule blocked a real GCSE English lesson ("a blog post for teenagers … Teach the learner to"): *post* as a noun. The rule now needs the verb in command position.
2. The scanner reported the shipped stage-test directive (`record_stage_result.py apply …`) 1,262 times, drowning real findings. That one template call is now exempt; every other script call is still reported.
3. `course.json` schema rejected a course-wide notice (`stages: null`) that `gate_check` documents as valid.

## Gaps this exposes (feeds the task list)
- **Misconceptions are the largest missing content layer** (N-04/N-08): without them the diagnostic can only classify against generic causes. They must be sourced (examiner reports, published research), never invented; compile them per course with a sourced citation or leave the file absent.
- **No question banks**, so `/mock` and `assemble_paper.py` have nothing to assemble from (N-07).
- **Practice is 3–4 scenarios per stage**, so a learner repeating a stage meets the same prompts; the tutor adapts them, but nothing records which variants were used (L-13).
- **One test scenario per stage** means a re-test after a fail depends on the model inventing a comparable question; there is no second parallel form (A-07).
