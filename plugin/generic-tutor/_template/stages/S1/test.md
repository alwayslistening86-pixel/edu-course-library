# {{STAGE_ID}} — Test: {{STAGE_TOPIC}}

## How to run this
Real checkpoint, not more practice. Present the scenario once, let the learner submit a full answer, then grade against this stage's entry in `rubric.json` — never grade without it.

## Test scenario
{{TEST_SCENARIO — should be new, not reused from practice.md}}

## Grading
Apply `rubric.json`'s `stage_rubrics.{{STAGE_ID}}` criteria exactly, then record the verdict:
```
python3 /EDU/.tutor-scripts/record_stage_result.py apply <subjects.json> <course.json> {{STAGE_ID}} pass|fail
```
This writes `syllabus_status` itself, and on a genuine pass advances `current_stage` to the next stage in the ladder — don't hand-write either field. Give the learner a short honest note on strengths/weaknesses either way.

## If fail
Name the specific weak or missing criterion, offer to revisit practice, then re-test with a new scenario of the same type.

## On pass
Tell the learner they can move to {{NEXT_STAGE_ID}} — `record_stage_result.py` has already advanced `current_stage` there.
