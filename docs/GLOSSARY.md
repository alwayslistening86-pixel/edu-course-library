# Glossary

| Term | Meaning |
|---|---|
| **Stage** | One unit of a course's ladder (`S1`, `S2`, …). Has a lesson, practice and test. |
| **Phase** | Where a learner is inside a stage: `lesson`, `practice` or `test`. |
| **Slot / session slot** | One study session. Time is counted in slots, never dates. `student_profile.json.session_slot` advances once per `/run`. |
| **Roster** | The courses a learner holds incomplete at once; capped by `roster.max_incomplete_courses`. Dormant (level-locked) courses count. |
| **Roster state** | Per-enrolment: `active`, `dormant`, `test_pending_convergence`, `dropped`. Completion is derived, not stored. |
| **Level / level lock** | A course's `academic_level`. Courses above the lowest unfinished level (and above `highest_level_cleared`) stay `dormant`. |
| **`highest_level_cleared`** | The single cumulative unlock ledger; raised only when every course at a level is complete. |
| **Cohort** | All of a learner's courses at the same level (`cohort_id`); a standalone course is its own cohort. |
| **Convergence** | Nobody in a cohort sits a stage test until every eligible member is test-ready. |
| **Bottleneck** | The cohort member furthest from test-ready; it gets most of the cohort's slots. |
| **Grounding** | A course's rubric being traceable to a live, verifiable source. `suspended_ungrounded` freezes the course. |
| **Coverage** | Whether every item in the itemised specification is taught by some stage: `full`, `partial`, `unverified`. Declared, not mastery. |
| **Standalone course** | A qualification with no level; never enters the level ledger. |
| **Theory-only** | Practical stages withheld because the learner hasn't declared the needed capability. |
| **Diagnostic exchange** | Eliciting why an answer was wrong, then classifying `cause` (slip, missing_prerequisite, misconception, misapplied_procedure, comprehension). |
| **Remediation** | Structured response to a failed stage test; escalates after attempt 2. |
| **Item mastery** | Per-syllabus-item probability of mastery (BKT), distinct from course-level `confidence`. |
| **Confidence** | Course-level number in [0,1] (default 0.5) updated only by `confidence_update.py`. |
| **Deck / card** | Spaced-repetition flashcards, seeded by stage-recap, scheduled by slot. |
| **Consent status** | `granted`, `limited` or `revoked`; controls what may be persisted. |
| **Deployed copy** | `.tutor-scripts/`, the runtime copy of the plugin's scripts. |
