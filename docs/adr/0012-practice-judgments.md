# ADR 0012 — Who may make a practice-phase judgment that becomes a record

Status: **accepted (rule); nothing built** (7 Oct 2026). Micro-task B-04.4 in `docs/WAVE7.md`. The owner accepted the recommended default for D7. The build tasks it implies are listed at the end and are not started.

## Context
Scripts own every write, but the model decides what to tell them. In practice the teaching model makes judgments (this answer is wrong, this is why, this card was recalled, this tag is the item) and a script records them. `docs/wave7/B-04-practice-judgments.md` inventories 32 such places and sorts each into one of three classes. `docs/wave7/B-04-failure-scenarios.md` lists twelve ways a voice that is not the examiner can damage the record from them (S1 to S12). ADR 0010 asks the open question: if the voice that teaches may not write, who makes these calls?

Today one model plays every part, so nothing here is separated. The rule matters in two ways: some of its parts close real gaps now, whichever model is in use, and the rest bind only once roles are configured (B-05).

## Decision
Every judgment is handled according to its class in the inventory.

1. **Script-markable: a script decides, from the item's key.** For multiple choice, numeric and cloze items, and for outcomes a script already computes (which practice item was served, a recorded pass resetting remediation, a goal's date), the voice supplies what the learner said and receives the verdict. It never supplies "correct" as an input. This needs items that carry a machine-checkable key (B-02.3); until an item has one, its judgment falls into class 3.
2. **Checkable: the voice may propose; a script writes only what it can verify.** The script checks the proposal against data it already holds and refuses, with a reason and no write, what it cannot confirm. Examples: the item, stage and criterion tags equal what the script last served; a misconception id exists in that stage's `misconceptions.json`; a stage verdict `pass` has a matching grading record at or above the pass threshold; a remediation cause is one of the five; a move to the next phase has evidence of the work. A refusal tells the voice what to do instead (retry the item, or leave it unrecorded).
3. **Examiner-only: a voice that is not the examiner does not make the judgment.** In the first version **nothing is recorded** for it: the item is simply met again later, and the learner is told plainly that this one will be checked by the examiner or the adult. There is no queue of pending judgments. Rubric marking, stage verdicts, the cause of an error, whether a free-text answer shows understanding, and the examination itself stay with the examiner.

**Who is the examiner.** Whichever model or person is configured with that role. With no roles configured, which is every install today, the single model is both voice and examiner, class 3 changes nothing, and behaviour is exactly as now. Parts 1 and 2 apply from the day they are built, for every model, because they remove a trust that was never earned (S2, S4, S6, S7, S8, S11).

**Mocks.** A mock paper records its marks and errors but does not move `item_mastery` or the diagnostic gate. The exam-simulator skill already says a mock changes no progress state; the code disagrees (S9), so the code changes to match the skill. This is the default, flagged for the owner in the build task below.

## Why not the alternatives
- **Queue the voice's proposals for the examiner (option b in the scenarios).** It adds state to store and secure, a place for a learner's words to leak (S5), and a timing problem when the examiner is offline. Worth revisiting after the pilot shows how often a class 3 item is skipped; not worth building blind.
- **Let a small model write and audit afterwards.** An audit that finds a wrong cause after a plan has been changed on it comes too late, and the audit itself needs an examiner.
- **Forbid all practice-phase writes by anything but the examiner.** It would remove the diagnostic value the system is built on and make the examiner the bottleneck for every wrong answer.
- **Trust the voice and measure it.** Measurement (B-03.6) tells us how often a model errs; it does not make an unchecked write safe. Parts 1 and 2 are cheap and independent of which model is used.

## Consequences
- The record gets harder to corrupt by accident, by a typo, or by a weaker model, without any role being configured.
- Some learner exchanges will leave no record in the first version (class 3 with a non-examiner voice). That is deliberate: a missing record is better than a wrong one, and the learner is told.
- Parts 1 and 2 add checks to scripts and so change golden outputs and tests; each is a small change of its own.
- It depends on keyed items (B-02.3). Without them class 1 covers only outcomes a script already computes.
- It does not decide the role-enforcement mechanism (B-05.1) or what the examiner sees (B-04's follow-ups).

## Build tasks this implies (B-04.5)
Each is a separate small pull request with the test named. None is started.

| # | Change | Test that proves it |
|---|---|---|
| 1 | Boolean inputs accept only `true` or `false`; anything else is an error, not a wrong answer (S6) | Parsing test for `diagnostic_gate`, `item_mastery observe`, `review_math apply` |
| 2 | Make the skill text consistent on when an error is logged (S3) | A replayed-session test comparing wrong answers served with errors logged |
| 3 | Error tags must equal the item the script last served (S4) | Mismatched tag refused; matching tag accepted |
| 4 | A misconception id must exist in that stage's `misconceptions.json` | Unknown id refused |
| 5 | A stage `pass` needs a matching grading record at or above the threshold (S7) | `apply pass` with no or failing record refused |
| 6 | Phase and roster moves need evidence of the work (S8) | Forward move without evidence refused |
| 7 | A mock records marks and errors but not mastery or gate counts (S9) | Mock error leaves `item_mastery` unchanged |
| 8 | A length cap and a scan on error notes and session summaries (S5) | A note with a phone number or over the cap is refused |
| 9 | Remediation causes limited to the five (S11) | A sixth value refused |
| 10 | Every writing script consults consent, enumerated by a test (S12) | The test fails if one does not |
| 11 | Keyed item types and a marking script (class 1) | B-02.3's edge-case table |

## Not decided
- Whether the first version's "nothing recorded" is acceptable to the owner for a child's session with a local voice; the pilot should say.
- Whether the examiner must be a different model from the voice, or may be the same model with the rubric in view. The rule works either way.
