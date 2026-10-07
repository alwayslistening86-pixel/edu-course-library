# ADR 0010 — Role-separated models, a portable profile and a local UX (direction accepted, design pending)

Status: **direction accepted; build patterns not yet designed; not started** (6 Oct 2026). These ideas are no longer being dismissed. They are tracked as tasks B-01 to B-06 in `docs/TASKS.md` (Wave 7). Every one of those tasks starts with a design step, and this ADR will be expanded into detailed build patterns before any code is written. The step-by-step plan is `docs/WAVE7.md`.
Owner's stance (6 Oct 2026): the **portable profile** is the settled answer to multi-user (the USB stick is one example; the principle is that learner state travels with the learner, not with the machine); a **local UX** is now a likely addition, not something to keep refusing; the **role split** is the hardest of the three and comes last. A cloud model (Claude) must remain a full fallback *teacher*, not only an examiner, whenever no local model is set up.

## Where this came from
A conversation the owner had with another assistant, which compared this project with other open tutors and suggested three additions. Its ranking of other projects is unverified and was written from this project's own documents, so it is not evidence of anything; the ideas are what is kept.

## The ideas
1. **Role split.** A small local model is the *tutor voice* for everyday study and never writes durable state. A stronger cloud model is the *examiner*: stage tests, grading against the rubric, diagnosing the cause of an error, anything that moves progress. A separate staff channel (any capable model) does installs, `/audit` and engine changes, and is unavailable in student mode. Optionally a second model double-marks or checks safety.
2. **Per-surface adapters, not one abstract bus.** Claude keeps the deepest path (skills, hooks, commands). A local UI drives the scripts directly. Other models get adapters that implement the same script contracts in their own idiom.
3. **Portable profile.** The engine lives on a shared machine image; `profile/<id>/` lives on the learner's own medium (a USB stick or home folder). Identity is the presence of the medium. Multi-user by many single-user vaults, not by tenancy.

## What already fits
- Scripts own every write, consent and path guards are in code, and the root is resolved by `--root` / `EDU_ROOT` (E-07): the engine does not care where `profile/` is.
- A profile written by a newer engine is refused (`state.load`), and `/doctor` flags a newer history database.
- The eval harness takes a backend, so another model can be measured on the same cases (A-14).
- Cheap deterministic marking already exists in principle: multiple-choice and numeric items need no model.

## Open questions (each could change the design)
- **Practice-phase judgments write state.** Diagnosing why an answer was wrong feeds `error_log`, `item_mastery` and `confidence`. If the local model may not write, who makes those calls? Options: the local model proposes and a script validates against the item's key; deterministic items are marked by script; free-text diagnosis waits for the examiner. Needs a decision before any code.
- **Small-model quality.** Every skill rule (hint ladder, real-situation guard, fading, accessibility modes, injection defence) was measured on one cloud model. A 7B model must be measured on the same suites before it may teach, and some rules may not hold.
- **Examiner availability.** If the examiner is offline, tests wait. Acceptable, but `session_plan` and the runner need to say so plainly.
- **Portable medium risks.** Sudden unplug mid-write (JSON is atomic, SQLite uses the default rollback journal, but a stick can still be pulled during a replace); a lost stick holds a child's learning record unencrypted (X-08 backup security is the nearest task, and would need extending to the live profile); drive letters and paths differ per machine; the stick may meet engines of different versions (older engines already refuse newer files, so the failure is a clear error, not silent damage).
- **Children's data.** A school deployment brings data-protection duties (consent, retention, who may see what). Not assessed here and not something code settles; it needs the owner or a school's advice before any deployment.
- **Course distribution.** Courses live in a private repo for licensing reasons (ADR 0006). Mirroring them to a fleet of machines needs a policy.
- **Teacher visibility.** None by design. If wanted, a read-only export per stick, not a central service.

## If it goes ahead (rough order)
1. Decide the practice-judgment rule above, in an ADR.
2. Add a local-model backend to the eval harness and measure the suites on it.
3. A thin student UI over the existing scripts, deterministic items first.
4. Root resolution from a mounted volume, a "not a valid profile" check, and safe-eject guidance.
5. Role policy as a table of which role may call which script, enforced by the existing hook guard and by the scripts themselves.

## Not decided
Nothing here changes current behaviour.

## Added 7 Oct 2026: a shared, anonymised pattern pool (task B-07)
The owner's idea: answer data can be anonymised (the spirit of an answer, not the verbatim text, and no user ids), which turns it into a shared resource, with a learner's profile letting their data flow into the pool when they choose.

Assessment: sound, and it is the route to the real data that A-03, A-12 and L-14 are waiting for, and to evidence-based misconception entries (the audit already proposes new ones from patterns that recur across learners). The parts that need care:
- **Removing ids is not anonymising.** Free text carries names, schools, places and writing style. A model-written description of the *pattern* ("added the denominators") is far safer than any form of the answer, and is close to what `error_events.note` already is. Verbatim answers, even scrubbed, are not proposed.
- **Small groups re-identify.** A family or one class contributing a rare pattern is identifiable by the pattern alone. Release only patterns seen from several learners, and show the learner the export before it leaves.
- **Local first, share second.** The local record (`grading_results`, possibly with a short pattern note) stays on the learner's own medium. Sharing is a separate export they can read and choose to send, never an automatic push, with its own consent class that is off by default.
- **Who holds the pool** is a real decision (the private content repository is one candidate) and children's data raises duties code does not settle.
Nothing is built. It is tracked as B-07 and depends on B-01 and the grading record from V-09.

