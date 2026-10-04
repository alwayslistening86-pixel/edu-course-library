---
name: health-status
description: Runs /status (a one-screen summary of where the active learner stands and what to do next) and /doctor (a read-only health check of the install and the learner's data). Reports and suggests; never repairs anything itself.
---

# Health & Status

**Contract**
- **Owns:** nothing — both commands are read-only.
- **Reads:** via `status.py` and `doctor.py` only.
- **Calls:** `status.py`, `doctor.py`.
- **Emits:** a short plain-language summary; for `/doctor`, failures first, each with its suggested fix.
- **Never:** edits a learner file, deletes a lock, redeploys scripts or "fixes" anything on its own; reads or shows another learner's data in `/status`.
- **Failure modes:** a script `error` (no profile, no data root) is shown verbatim with the one next step it implies (`/run <id>`, `/add-profile`, connect the folder).

## `/status`
Requires an active learner (`/run <user_id>` first). Run:
```
python3 /EDU/.tutor-scripts/status.py <the active learner's folder> <the /EDU/courses/ dir>
```
Present, in this order, in a few lines (not a data dump):
1. **Where you are** — session number (`session_slot`), roster `occupancy` of `max`.
2. **Each course** — name, stages passed of total, current stage and phase, roster state. A `dormant` course is "waiting for a lower level", a `dropped` one is paused. Mention `theory_only` completions as such. If `coverage_status` is not `full`, say the course does not yet cover the whole specification (same honesty rule as `course-runner`).
3. **Confidence** — only as a rough word ("building", "steady", "wobbly"), from the number; never present it as an exam-readiness or grade prediction.
4. **Reviews due** — `due_reviews_total`, and `unresolved_errors` only if non-zero.
5. **Next step** — `next_action.command` and its reason, as a suggestion.
If `consent` is `limited` or `revoked`, add one line saying what is not being remembered.

## `/doctor`
Does not need an active learner. Run:
```
python3 /EDU/.tutor-scripts/doctor.py [--learner <user_id>]
```
(If `.tutor-scripts` is not deployed yet, run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/doctor.py --root <data root>` instead.) Present `fail` checks first, then `warn`, then one line for how many passed. For each non-ok check give `detail` and the `fix`. Offer to help with a fix, but only act on the learner's say-so and never delete or overwrite learner data as part of a "fix" without an explicit yes. A `last-session` warning means the previous session's bookkeeping is incomplete — explain it exactly as `profile-kernel` does after `/run`.
