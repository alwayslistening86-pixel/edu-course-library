# B-04.5: the five checks that need a decision before they can be built

Written 8 Oct 2026 at v1.95.1 while building the B-04.5 tasks of `docs/WAVE7.md`. ADR 0012 listed eleven small checks. Six are built (a, g, h, i, j, k). The other five (b, c, d, e, f) look small in the ADR table, but each turned out to rest on something the code does not have. This note states what was found, the options, and a recommendation, so the owner can decide them together. Nothing here is built, and none of it changes behaviour until a choice is made. Every `file:line` below was read from the code on the day; `tools/check_citations.py` confirms the lines exist, not that the reading is right.

## 5b. When is an error logged? (scenario S3, a miss that is never recorded)
- **Found:** `skills/course-runner/SKILL.md:23` says that after **each** wrong answer the tutor runs `diagnostic_gate.py` and then `error_log.py append`. The section "Diagnosing during practice" (lines 126 to 150) says that when the gate's `fire` is false "keep teaching normally", and only "when it fires" does it elicit, classify a cause and log.
- **Why it matters:** the gate fires on two or more *logged* misses of one item or three of one cause. A wrong answer that is never logged can never help it fire, so the first rule starves the second.
- **The tension:** a log entry needs one of five causes, but the cause is only known after the elicitation that happens when the gate fires. Logging every miss at once therefore means guessing a cause.
- **Options:** (1) add a sixth value `unclassified` to the cause list, logged on every miss and reclassified when the elicitation happens (breaks ADR 0012's "five causes", item 9, built in v1.93.3); (2) keep five causes and add a separate cheap script `miss_log.py` that counts misses per item without a cause (a new write path, a small schema addition); (3) change the skill so the first miss is logged as `slip` and corrected on elicitation (simple, but it writes a label the voice does not believe).
- **Recommendation:** (2). A miss is a fact and a cause is a judgment; they should not share one field. Needs a test that replays a session and compares wrong answers served with misses recorded.

## 5c. Error tags must equal the item served (S4)
- **Found:** nothing records which item was last served. `practice_pick.py` records the number of the fixed practice item (`practice_used`, its docstring lines 6 to 16), which is a position in `practice.md`, not a syllabus item id. `next_items.py` is read-only. `error_log.py append` takes any item id string.
- **Options:** (1) make `practice_pick.py used` also store the syllabus item ids the served practice item covers (needs the practice files to say which items each covers, which they do not today); (2) have `error_log.py` check only that the item id exists in the course's `curriculum_map.json` (catches typos and invented ids, not a wrong-but-real id) and that it belongs to the stage given; (3) both, in that order.
- **Recommendation:** (2) now: cheap, needs only the course folder (see 5d, which needs the same argument). (1) waits for B-02.4, when the selector picks items by id.

## 5d. A misconception id must exist (S1, S4)
- **Found:** entries in `misconceptions.json` have no id (`pattern`, `correction`, `source`; schema `misconceptions.json`), and `error_log.py append` is not given the course folder.
- **Options:** (1) an id by position, `MC-<stage>-<n>`; (2) an optional stable `id` in the schema, written by the compiler, with a script that adds ids to existing files.
- **Recommendation:** (2), because a position changes when a list is reordered. Both need `error_log.py` to learn the course folder, an optional `--course-dir`, and the skill to pass it (a one-line change in two places, which the context budget can absorb).

## 5e. A stage pass needs a grading record (S7)
- **Found:** `pass_threshold` in `rubric.json` is prose (the linter only asks for six words), so there is no number to compare a grading record with. `record_grading.py` writes marks only under signal consent, so when consent is limited no record can exist.
- **Options:** (1) check only that a grading record exists for this stage from this test, waived when consent blocks signal data or when the stage has no rubric entry; (2) add an optional numeric `pass_marks` to a rubric entry, written only where the issuing body publishes one, and check against it when present, falling back to (1).
- **Recommendation:** (2). It is the only version that can refuse a real false pass. It is a content change and the compiler never invents a threshold, so most courses stay on (1) until an enrichment run supplies numbers.

## 5f. Phase and roster moves need evidence (S8)
- **Found:** `session_state.py phase` (line 44) accepts any of `lesson`, `practice`, `test` in any order, with no check. `roster` allows only the two live states. The convergence rule that decides when a test may start is `cohort_status.py`, but `session_state.py phase` neither calls it nor is told the course.
- **Options:** (1) `phase test` requires the course folder and consults `cohort_status` (the existing convergence gate) and refuses if the stage is not test-ready; (2) as (1), plus `phase practice` requires the lesson to have been marked met; (3) leave it, and rely on the skill.
- **Recommendation:** (1). The rule already exists and is tested elsewhere; this only makes the write respect it. (2) needs an evidence record for lessons that does not exist.

## Order I would build them in, once chosen
5d and 5c(2) share the `--course-dir` plumbing and the skill edit, so they go together; then 5f(1); then 5e(1) with 5e(2) when a course supplies numbers; 5b last, because it adds a write path and a schema field and so needs the most review.

## What I need from the owner
A one-word answer per item is enough: **5b** 1/2/3, **5c** 1/2/3, **5d** 1/2, **5e** 1/2, **5f** 1/2/3. If no answer comes I will build only the recommended choice for 5d, 5c(2) and 5f(1), which are the least invasive, and leave 5b and 5e as they are.

## Outcome of the owner's answer (8 Oct 2026)
The owner took the recommended option for each item. Built so far (v1.98.0): **5d(2)** and **5c(2)** together. `misconceptions.json` entries take an optional stable `id` (schema, unique per file, `misconception_ids.py` adds them to older files without changing or reordering anything); `error_log.py append` refuses an item that is not one of the course's syllabus items and a misconception id that is not an `id` in that stage's file, and names the valid ones. One deliberate difference from the text above: an item that belongs to a different stage than the one given is **accepted with a warning**, not refused, because interleaved practice (next_items.py mixes in earlier stages) legitimately revisits them. The course folder is `--course-dir`, else found from the data root; if neither works the check is skipped and the result says so, so a install without a findable course is no worse than before. **5f(1), v1.99.0:** `session_state.py phase <subjects> test` is refused unless the course is in `test_pending_convergence` and its cohort has converged (`cohort_status.py`'s own `converged`); the error names the courses still being waited on. Resuming a cut-off test (already in `test`) is always allowed. If the courses folder cannot be found the cohort check is skipped and the result says so; the roster rule still applies. Moves to `lesson` and `practice` stay unrestricted (a lesson-met record does not exist, so there is no evidence to ask for). Still to build in the agreed order: 5e(2), 5b(2).
