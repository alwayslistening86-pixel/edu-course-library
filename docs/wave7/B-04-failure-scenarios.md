# B-04.3: What goes wrong when the voice that teaches is not the examiner

Micro-task B-04.3 of `docs/WAVE7.md`. Design only; nothing is built. It reads the inventory in `docs/wave7/B-04-practice-judgments.md` (row numbers below refer to its table) and asks, for each judgment that becomes a durable write, what happens if a weaker or less careful voice makes it, how we would notice, and how it would be measured. B-04.4 then decides the rule (owner decision D7, default accepted: script-markable items are marked by script; a proposed cause is accepted only if a script can check it against the item; everything else waits for the examiner).

"The voice" below means whichever model is talking to the learner when it is not the examiner: a small local model, or Claude acting without the rubric in front of it. The failures are not unique to small models; a small model makes them more often, and nothing in the system today stops either.

## The scenarios

Each has the state it damages, the way the damage stays hidden, and the measure that would catch it. **Existing** means a suite or test already in the repository; **Needs building** names the micro-task that would add it.

| # | Scenario | Rows | Damage | Why it stays hidden | Measure |
|---|---|---|---|---|---|
| S1 | **Wrong cause.** The voice labels a misconception as a slip (or the reverse) | 5 | Remediation picks the wrong response; the diagnostic gate under- or over-counts; cards and the auditor learn the wrong thing | The script accepts any of the five valid causes; nothing compares the label to the exchange | Existing: the `diagnostics` suite (15 scenarios, five causes) run on the voice model (B-03.6). Needs building: a threshold per D6 |
| S2 | **Inflated mastery.** The voice marks a wrong answer right, or a right answer for the wrong reason | 3, 4, 10, 13, 14 | `item_mastery` and `confidence` rise, a review card's interval grows, the learner is told they know it | Correctness arrives as a flag the script cannot verify; a typo or a lenient judgment looks the same as truth | Existing: the `grading` suite (false passes are critical). Needs building: for script-markable items the flag stops being an input (B-02.3) |
| S3 | **Silent miss.** The voice does not log a wrong answer at all | 3, 4 | No error entry, so the diagnostic gate (which counts logged entries) never fires and mastery never drops | The inventory found the skill text inconsistent about when to log (after every wrong answer in one place, only when the gate fires in another; B-04.5 re-reads both), so a voice that follows the second may never log | Needs building: a replayed-session test comparing wrong answers served with errors logged. Also fix the skill text (B-04.5) |
| S4 | **Mis-tagged error.** The item, stage or criterion is wrong | 7 | The wrong item's mastery drops; the right one is never practised | Tags are free strings; only the type is checked | Needs building: a script check that the tag equals the item the script last served (`next_items.py` / `practice_pick.py`) |
| S5 | **Personal detail in a note.** The free-text diagnosis note carries a name, a disclosure, or a sentence the learner typed | 8, 26 | Stored in JSON and the history database, copied into backups, exports and the auditor's cross-learner reading | No length cap, no scan, and every later copy inherits it (see `B-06-personal-data.md` gaps) | Existing: the `wellbeing` suite's privacy cases cover what the voice says, not what it writes. Needs building: a cap and a scan on the way in, and a test that a note with a phone number is refused |
| S6 | **Flag typo.** A correct recall is sent as `True`, `yes` or `1` | 1, 11, 13 | The script reads anything but `"true"` as false: a lapse is recorded for a right answer, or a confusion flag is dropped | Silent; the call succeeds | Needs building: a parsing test that rejects anything but `true`/`false`, so a typo is an error, not a wrong answer |
| S7 | **Stage passed by assertion.** The voice records `pass` without a graded test | 18, 19, 20 | `syllabus_status` flips, `current_stage` moves, the next stage unlocks; confidence rises | `record_stage_result.py apply` checks the stage exists and the verdict is `pass` or `fail`; it does not look at the recorded marks or the pass threshold | Needs building: a rule that a pass needs a matching grading record (a script-checkable invariant, candidate for `invariants.py`) |
| S8 | **Phase advanced early.** The voice says lesson or practice is done | 23 | The learner reaches the test unprepared, or a course leaves the practice queue | "Done when" is prose; the script only checks the value is a valid phase | Needs building: evidence checks (items met, mastery floor) before `set_phase`/`set_roster` accept a move forward |
| S9 | **Mock marking moves progress.** Errors diagnosed during a mock change mastery and the gate counts | 28 | A practice paper quietly changes progress state, although the skill says a mock changes none | Skill and script disagree; nothing flags it | Needs building: a decision (B-04.4) and a test of whichever way it goes |
| S10 | **Hand-written course state.** The voice edits `change.md`, `grounding_status`, `last_live_recheck`, or an auditor addition | 31, 32 | A course can be suspended or marked live by free editing; the audit trail is the model's own words | No script owns these writes at all | Not a practice judgment but a role matter: student-mode must make these impossible (B-05). Measure: role-policy tests |
| S11 | **Cause string drift.** The remediation record stores any cause string | 21 | `last_cause` becomes noise; escalation advice keys off it | The script stores whatever it is given | Needs building: the five-cause enum applied here as in `error_log.py` |
| S12 | **Consent skipped by the caller.** A call is made for a class the learner limited or revoked | all writes | Most writers check consent in the script; any write that does not would persist data against the learner's choice | Depends on each script remembering to check | Existing: consent tests per writer. Needs building: a test that enumerates every writing script and fails if one never consults `consent.py` |

## What each class of judgment needs

The inventory sorted every row into script-markable, checkable, or examiner-only. The failures above say what each class needs before a non-examiner voice may touch it.

- **Script-markable** (rows 3, 9, 11, 12, 13, 17, 20, 22, 25, 30). Remove the voice from the decision. The script derives correctness from the item's key and the learner's answer; the voice supplies the answer and receives the verdict. This closes S2, S6 and part of S3 for those rows. It depends on items carrying a machine-checkable key, which question banks do not yet have (B-02.3).
- **Checkable** (rows 6, 7, 10, 16, 19, 21, 23, 29). The voice may propose; a script verifies against data it already holds, and refuses a proposal it cannot verify. This closes S4, S7, S8 and S11. Each needs a small verifying rule, none of which exists yet.
- **Examiner-only** (rows 1, 2, 4, 5, 8, 14, 15, 18, 24, 26, 27, 28, 31, 32). A voice that is not the examiner does not make the judgment. The open design question is what happens to the learner's exchange meanwhile: (a) nothing is recorded and the item is simply retried later; (b) the exchange is queued for the examiner as a pending judgment (new state, new privacy surface, and a place for S5 to leak); or (c) the examiner is the same model and the distinction is moot. B-04.4 should choose, and the default for D7 already leans to (a) for the first version because it adds nothing to store.

## What this does not tell us

- **How often a real small model makes each mistake.** That needs B-03.6, which needs a machine with a model. Until then these are scenarios that can happen, not measured rates.
- **Whether the examiner role is any safer.** The same rows exist when Claude plays both parts; the difference is that today there is no other voice to separate it from. These scenarios are the case for building the checks regardless of which model is in use.
- **Whether the word-list style of the existing suites is enough** for S1 and S2. They were built for cloud-model regression; B-03.7 reads real replies to see if they are fair for a smaller model.

## Hand-off to later micro-tasks

| Finding | Goes to |
|---|---|
| The rule choice among (a), (b) and (c), and which rows each class covers | B-04.4 (ADR 0012) |
| Fix the skill text that disagrees with itself on when to log (S3), and the mock/progress mismatch (S9) | B-04.5 |
| Marking script and keyed item types | B-02.3, B-02.4 |
| Verifying rules for S4, S7, S8, S11, S6, S5 | B-04.5 turns these into build tasks, each with the test named above |
| Enumerating writers for consent (S12) | B-04.5 |
| Role enforcement for S10 | B-05.3, B-05.4 |
