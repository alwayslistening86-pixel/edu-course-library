---
name: exam-simulator
description: Runs /mock — a timed-style practice paper assembled from a course's question bank, marked honestly against its mark scheme, with the result recorded as practice (never as a stage pass or a predicted grade). Needs the course to have a question bank.
---

# Exam Simulator

**Contract**
- **Owns:** assembling and administering a mock paper, marking it, and recording the result in `mock_results` (via `record_mock.py`). It never changes `syllabus_status`, `current_stage`, roster state or any level lock.
- **Reads:** `question_bank.json` for the course (prompts, mark schemes, model answers), the learner's `mock_results` (to avoid repeating questions).
- **Calls:** `assemble_paper.py`, `mark_answer.py`, `record_mock.py`, `error_log.py` (source phase `test`).
- **Emits:** the paper (prompts and marks only), per-question marks with mark ids awarded, marks by stage, the weakest items, plain caveats.
- **Never:** shows a mark scheme or model answer before marking; converts marks into a predicted grade or "you'd get a 7" (boundaries are published per series and are not held here); softens a mark; lets the mock count as a stage test; claims the time was enforced.
- **Failure modes:** no question bank → say so and stop (offer `/continue` or `/review`); script bank errors are shown verbatim; `written: false` from `record_mock.py` (consent) → give the result now and say it will not be remembered.

## Invocation
`/mock <course_id> [marks] [minutes]` for the active learner. Requires an enrolled, teachable course (run the usual gate check if unsure); one that cannot be taught right now cannot be mocked.

## Procedure
1. **Set honest expectations.** Say it is practice under approximate conditions: the tutor cannot enforce time, so ask the learner to note when they start and finish and to work without notes or help. It does not count towards any stage or unlock anything.
2. **Assemble the paper.** Collect the question ids from earlier mocks (`mock_results[].questions`) and run:
   ```
   python3 /EDU/.tutor-scripts/assemble_paper.py <the /EDU/courses/ dir> <course_id> [--marks N] [--minutes N] [--stages S1,S2] [--seed <session_slot>] --exclude <earlier ids, comma separated>
   ```
   Default 40 marks if the learner gave none. If every question has been used, offer to repeat (drop `--exclude`) or to pick a different scope.
3. **Present the paper** exactly as returned: question ids, marks, calculator allowance, prompts, and the suggested total time. No hints. Let the learner answer in their own time.
4. **Mark it — honestly.** A question with a `key` is marked by `mark_answer.py <bank> <question id> "<answer as written>"`, not by you: use its marks (`correct: null` = ask for a clearer answer, mark nothing yet). Mark the rest against their `mark_scheme`, applying `tutor-core` and `course-runner`'s grading rules: method as well as answer, a stated-but-wrong point earns nothing, no working shown means ask the learner to explain before awarding method marks, no softening. Show per question: marks awarded of available and which mark ids were earned or missed, with one line on what was missing. Only then reveal model answers.
5. **Record it.** `python3 /EDU/.tutor-scripts/record_mock.py <subjects.json> <total_marks> <marks_awarded> <minutes_taken> <today> <question ids, comma separated>`. For errors you diagnosed while marking, log them with `error_log.py append … test …` as usual (note passed on stdin).
6. **Give feedback that helps.** Marks by stage, the two or three weakest items by name, one concrete next step (usually `/continue` on a weak stage or a targeted `/review`). Compare with earlier mocks by percentage only, noting papers differ in difficulty.
7. **Say what a mock is not.** It is not a grade prediction: the percentage is marks on this paper only. If asked "what grade is that?", say boundaries change every series, are published by the exam board and are not held here, so a percentage is all it can honestly give.
