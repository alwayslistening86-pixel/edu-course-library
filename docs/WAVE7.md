# Wave 7 plan: surfaces and deployment, as micro-tasks

Written 7 Oct 2026 at v1.93.0. This turns B-01 to B-07 (see `docs/TASKS.md`, ADR 0010) into steps small enough to finish and check one at a time. The B-tasks stay the unit of record in `TASKS.md`; the micro-tasks below (B-01.1, B-01.2 and so on) live only here, so the live task counts do not move. Nothing in Wave 7 is built yet.

## Progress (updated 7 Oct 2026, v1.93.1)
The owner accepted the recommendations and defaults for D1 to D11 on 7 Oct 2026, so none of them blocks work. Everything below that needs no machine and no real learner has started.

| Done (merged) | What it is |
|---|---|
| B-01.1 | `docs/adr/0011-portable-profile.md` |
| B-02.1 | `docs/wave7/B-02-local-interface-design.md` |
| B-04.1, B-04.2 | `docs/wave7/B-04-practice-judgments.md` (32 rows, classed) |
| B-04.3 | `docs/wave7/B-04-failure-scenarios.md` (twelve scenarios) |
| B-04.4 | `docs/adr/0012-practice-judgments.md` (D7 recorded) |
| B-05.2 | `docs/wave7/B-05-script-roles.md` (all 70 scripts) |
| B-06.1 | `docs/wave7/B-06-personal-data.md` (38 items, 15 gaps) |
| B-06.2 | `docs/wave7/B-06-course-delivery.md` |
| B-04.5 | the eleven build tasks, listed below |

Next, with no machine needed: B-01.2 (separate profile root), B-02.3 (script-markable item types), the B-04 build tasks (small, independent), B-05.1 (role threat model), B-06.3 and B-06.4, B-03.2 to B-03.5 (offline parts of the local-model backend). Still needing the owner or a machine: B-01.10, B-02.10, B-03.6 and B-03.7, B-06.5.

The inventories found work outside Wave 7 too, tracked here so it is not lost: the 15 personal-data gaps in `B-06-personal-data.md` (erase and purge leave backups, exports, migration copies and signal data behind; error notes have no cap), and a stale line in `PRIVACY.md` saying the history database is missing from `/export` (it is included).

## How every micro-task is done

One micro-task is one pull request. It is one of five kinds, and the kind decides what "done" means.

| Kind | What it produces | Done when |
|---|---|---|
| **inventory** | A table taken from the code and docs as they are (nothing invented) | Every row cites the file it came from, and a second pass finds no gaps |
| **design** | A short note or ADR: problem, options, the choice, risks, how it will be measured, and what would make us stop | The note names a failure scenario for each risk, and each scenario has a test or measure written into a later micro-task |
| **decision** | A question only the owner can answer, with a recommendation | The answer is recorded in the ADR; if none comes, the stated default applies and the PR says so |
| **build** | Code, tests, docs, in the repo's usual way (stdlib only, scripts own writes, goldens, budgets) | The failure scenarios from the design each have a test that fails without the change |
| **measure** | A run or a review whose result is recorded, good or bad | The result is committed or reported, including what it does not show |

Rules that hold throughout:
- **Design before build, always.** No build micro-task starts until the design micro-task above it is merged and any decision it names is answered or defaulted.
- **Test the failure, not the happy path.** Each build names the ways it can go wrong (unplug mid-write, wrong role, a page opened from another site) and has a test for each.
- **Security-bearing work gets a threat model first and an adversarial read before merge** (B-02.5, B-05, B-07). The PR lists what was tried and what was not.
- **Be plain about limits.** A PR says what its checks cannot show, as the wellbeing eval PR did.
- **Children's data is a standing constraint**, not a late task: no learner data in this repo, no network by default, nothing shared without a separate opt-in.
- **Existing behaviour must not change** unless a micro-task says so. Where a role or surface is not configured, the system behaves exactly as today (Claude as full teacher); the golden tests are the proof.

## What the code looks like today (the starting facts)

These shape the plan, and each is checked against the code.
- The data root is one folder holding `courses/`, `profile/<id>/` and `.tutor-scripts/` (`tutorlib/paths.py`). There is no separate profile root, so a profile on another drive needs a code change first (B-01.2).
- JSON writes are atomic (temp file then rename); history is SQLite with a rollback journal; locks are files holding a process id and a timestamp, broken after a timeout (`tutorlib/filelock.py`). A lock carries no machine name, which matters when a stick moves between machines (B-01.5).
- Schema migration writes a `.pre-migrate-*.bak` copy first (`migrate_schema.py`); an older engine refuses a newer file (`state.load`).
- Question banks hold prompts, marks and **mark schemes for a marker** (`question_bank.json`). They carry no machine-checkable answer key, so "multiple choice and numeric, marked by script" needs a new item type first (B-02.3). Stage tests are graded against a rubric by the model today.
- There is no concept of a role anywhere in the scripts. A hook guard exists (`hooks/hooks.json`), but the model can run any script through a shell, so a role set by an environment variable would not stop it (B-05.1).
- The eval harness takes a backend; one exists for the `claude` command line, plus scripted ones for offline checks (`evals/backends.py`).

## Decisions only the owner can make

Each has a recommendation and a default, so work is never blocked: if there is no answer, the default applies and the relevant PR says it was defaulted.

| ID | Decision | Recommendation (and default) | Gates |
|---|---|---|---|
| D1 | What may a portable profile live on? | A plain folder or removable drive. Never a synced folder (the check warns). Default: this. | B-01.1 |
| D2 | Encrypt the live profile inside the engine? | No. Stdlib Python has no real encryption, and a home-made scheme is worse than none. Use the operating system's (BitLocker, FileVault, LUKS or a VeraCrypt volume) and have the check say whether it can tell. Default: this; revisit only if you accept one optional dependency (this is also X-08). | B-01.8 |
| D3 | Local interface style | A page served only to this computer (`127.0.0.1`, a token per launch) by the standard library, no framework, no internet. A terminal interface is simpler but worse for children; a desktop shell needs a dependency. Default: local page. | B-02.1 |
| D4 | Can a stage be passed without a model? | Not for rubric-graded tests: practice and review only. A stage test passes without a model only where its items are script-markable (B-02.3). Default: this. | B-02.7, B-04 |
| D5 | Which local-model runtime? | Any server that speaks the common chat-completions format on this machine (Ollama and llama.cpp both do), reached over localhost. Default: this. | B-03.1 |
| D6 | When may a local model teach? | Zero critical failures on safety, wellbeing, injection and locale; other suites within 0.05 of the cloud baseline; otherwise "supervised only" or "not yet". The owner sets the final numbers. Default: these. | B-03.5 |
| D7 | Who judges a practice answer when the tutor voice is not the examiner? | Script-markable items are marked by script; a proposed cause is accepted only if a script can check it against the item; everything else waits for the examiner. Decided in the ADR after the inventory (B-04.4). | B-04, B-05 |
| D8 | How are courses delivered to other machines? | A private repo per site, read-only, pinned to a tag; no public mirror (ADR 0006). Default: this; licensing is the owner's call. | B-06.2 |
| D9 | Minimum group size before a pattern may be shared | At least 5 distinct learners and 2 households or classes. Default: this; lower is a privacy loss, higher means nothing ever ships. | B-07.3 |
| D10 | Who holds a shared pool? | The private content repository, with a named owner. Default: this. | B-07.5 |
| D11 | Under-16s in the pool | Never without an adult's recorded consent, and off by default. Default: this. | B-07.2 |

## B-01 Portable profile (ten micro-tasks)

Learner state travels with the learner. The engine and courses live on a machine; `profile/<id>/` lives on the learner's own folder or drive.

| ID | Kind | Task | Done when | Needs |
|---|---|---|---|---|
| B-01.1 | design | ADR 0011: the medium policy (D1), the two-root model (engine and courses root, profile root), what a lost or half-pulled medium can expose or lose, and what the engine promises | Every risk in ADR 0010 has a scenario and a named test below | D1 |
| B-01.2 | build | A separate profile root: `--profile-root` / `EDU_PROFILE_ROOT`, defaulting to `<root>/profile` so nothing changes by default; `resolve_root.py` reports both | Tests with the profile on a different temp tree, a Windows-style path, and a path with spaces; goldens unchanged | B-01.1 |
| B-01.3 | build | `profile_check.py`: is this a valid, safe profile? Read-only verdict `ok / warn / refuse` with reasons: valid id, profile file passes its schema, version not newer than the engine, history database passes its integrity check and version, no torn temp files, writable, enough free space, and a warning when the path looks like a synced folder | One fixture per refusal and per warning; each fails without the check | B-01.2 |
| B-01.4 | build | Interrupted-write test harness: list every state write point (JSON replace, history insert, lock create and remove) and stop the process at each one | The matrix is generated from the code, so a new write point without a case fails the build; after every stop the file is entirely old or entirely new | B-01.2 |
| B-01.5 | build | Locks that survive a move between machines: record the machine name with the process id; a lock from another machine is reported, never silently broken inside its timeout | Test of a lock file written by "another host"; existing lock tests unchanged | B-01.4 |
| B-01.6 | build | Session start and safe eject: `profile_check` runs before a session and refuses plainly; `profile_close.py` removes locks, writes a "closed cleanly" mark and says "safe to remove"; an unclean mark is reported at the next start | Simulated unplug then reopen: warned, data intact, no manual repair | B-01.3, B-01.4, B-01.5 |
| B-01.7 | build | Version matrix: older engine on newer profile refuses with a clear message; newer engine on older profile migrates after a backup | One test per cell of the matrix; the backup file is checked to exist before the migration writes | B-01.3 |
| B-01.8 | build | Encryption position (D2): documentation and a check that says what it can and cannot tell about the medium; an optional-dependency route only if D2 changes | The text says plainly that the engine does not encrypt; a test pins that no secrets or keys are ever written | B-01.1, D2 |
| B-01.9 | build | Several profiles on one medium: list them, pick one, and prove no script can reach another's folder | Cross-profile read and write attempts all refused (the id and containment guards exist; this proves them on the new root) | B-01.2 |
| B-01.10 | measure | Walk-through on a real removable drive (owner-run), plus the parent checklist in `INSTALL.md` and `USER_GUIDE.md` | Checklist followed once end to end; what went wrong is recorded | B-01.6, B-01.9 |

## B-02 Local interface (ten micro-tasks)

A page on this computer over the existing scripts. First version is deterministic: no model anywhere in the bookkeeping.

| ID | Kind | Task | Done when | Needs |
|---|---|---|---|---|
| B-02.1 | design | Surface design (D3): screens, which script each calls, how accessibility modes and locale apply, where a teaching voice plugs in later | Screen-by-screen table; every screen lists its script and its failure states | D3, B-01.1 |
| B-02.2 | build | A thin command layer over the scripts: one function per screen, schema'd output, no new logic | Each function tested against the fixture; a test fails if the layer writes anything a script does not | B-02.1 |
| B-02.3 | design then build | Script-markable item types (multiple choice, numeric with tolerance and units, exact short answer) with an answer key in the item, and a marking script that is a pure function | Table of edge cases (units, rounding, decimal comma, case, spaces) each with a test; schema and `validate_structure` updated; the compiler learns when to write them | B-02.1 |
| B-02.4 | build | A bank item type `kind` and the practice selector that can pick them | Existing banks unchanged and still pass; goldens updated for new fields only | B-02.3 |
| B-02.5 | design then build | The local server: binds `127.0.0.1` only, token per launch, rejects other Host headers (DNS rebinding), no cross-site requests, strict content policy, size limits, no outbound requests | Threat model written first; a test per attack tried (wrong host, no token, cross-origin, oversized body, path traversal); adversarial read recorded in the PR | B-02.2 |
| B-02.6 | build | The screens: pick profile, status, practice loop, review cards, recorded result; static text only | Browser smoke test on the pre-installed Chromium; accessibility modes change the page as the tutor-core rules say | B-02.4, B-02.5 |
| B-02.7 | build | A deterministic stage loop end to end (D4): lesson text, script-marked practice, review, recorded result, through the real scripts | A headless client completes it on a fixture course and the history database shows the same rows the chat path would write | B-02.6 |
| B-02.8 | design | Teaching-voice interface: `voice(context) -> text` with a null default; how Claude or a local model would attach without gaining write access | Note names what the voice may read and that it can write nothing | B-02.1 |
| B-02.9 | build | Launcher and docs: one command to start it against a profile root; child-friendly first-run text | Fresh clone to running page in the test using only documented commands | B-02.7 |
| B-02.10 | measure | Sit with a real learner and the page (owner-run) | A written list of what confused them | B-02.9 |

## B-03 Local-model evaluation (seven micro-tasks)

No rule is assumed to hold on a small model. Each is measured.

| ID | Kind | Task | Done when | Needs |
|---|---|---|---|---|
| B-03.1 | decision | Runtime choice (D5) | Recorded | D5 |
| B-03.2 | build | A backend for a local chat-completions server, standard-library only, localhost by default, with a timeout and clear errors | Tests against a fake local server, including a refusal to call a non-local address unless told | D5 |
| B-03.3 | build | Record the settings with every result (model name, file hash or tag, temperature, seed, context size) | A result without them is rejected by `evals check` | B-03.2 |
| B-03.4 | build | A runbook and a runner for all suites at equal sample counts, with baselines named `baseline-<suite>-<model>.json` | Offline dry run with the scripted backend produces the same files | B-03.3 |
| B-03.5 | decision | Pass thresholds per rule and what each outcome allows: teach, teach supervised, not yet (D6) | `docs/LOCAL_MODEL_POLICY.md` merged | D6 |
| B-03.6 | measure | Run every suite on at least two sizes of local model (owner-run: needs a machine with a model) | Results committed; rules that fail are listed with their failures | B-03.4, B-03.5 |
| B-03.7 | measure | Read twenty real replies per failing rule by hand | Notes say whether the word-list checks were fair | B-03.6 |

## B-04 Practice-judgment rule (five micro-tasks)

If the voice that teaches is not the examiner, who is allowed to say why an answer was wrong?

| ID | Kind | Task | Done when | Needs |
|---|---|---|---|---|
| B-04.1 | inventory | Every place a judgment made in practice becomes a write: which skill says it, which script writes it, with what input | Table with file references for `error_log`, `item_mastery`, `confidence`, diagnostic gate, review outcomes | none |
| B-04.2 | inventory | Classify each: markable by script, checkable against the item, or examiner-only | Each row has a class and the reason | B-04.1 |
| B-04.3 | design | Failure scenarios for each class when the voice is a small model (wrong cause recorded, mastery inflated, a miss hidden) and how each would be measured | Scenarios written; measures named | B-04.2 |
| B-04.4 | decision | ADR 0012 and D7 | ADR accepted | D7, B-04.3 |
| B-04.5 | design | Spawn build micro-tasks from the ADR | Listed here before any is started | B-04.4 |

### B-04.5: the build tasks from ADR 0012
Each is its own small pull request. None is started. Every one changes only what its test names; none changes behaviour for a learner except by refusing something that was wrong to accept.

| ID | Change | Test that proves it | Scenario |
|---|---|---|---|
| B-04.5a | Boolean inputs accept only `true` or `false`; anything else is an error | Parsing test for `diagnostic_gate`, `item_mastery observe`, `review_math apply` | S6 |
| B-04.5b | The skill text agrees with itself on when an error is logged | A replayed-session test comparing wrong answers served with errors logged | S3 |
| B-04.5c | Error tags must equal the item the script last served | Mismatched tag refused; matching accepted | S4 |
| B-04.5d | A misconception id must exist in that stage's `misconceptions.json` | Unknown id refused | S1, S4 |
| B-04.5e | A stage `pass` needs a matching grading record at or above the threshold | `apply pass` with no or failing record refused | S7 |
| B-04.5f | Phase and roster moves forward need evidence of the work | Forward move without evidence refused | S8 |
| B-04.5g | A mock records marks and errors but not mastery or gate counts | Mock error leaves `item_mastery` unchanged | S9 |
| B-04.5h | A length cap and a scan on error notes and session summaries | A note with a phone number, or over the cap, refused | S5 |
| B-04.5i | Remediation causes limited to the five | A sixth value refused | S11 |
| B-04.5j | Every writing script consults consent, enumerated by a test | The test fails if one does not | S12 |
| B-04.5k | Keyed item types and a marking script (same work as B-02.3) | B-02.3's edge-case table | S2 |

## B-05 Role policy (seven micro-tasks)

The hardest item, and the one with a real limit: a role is only enforceable against a model that cannot run arbitrary commands.

| ID | Kind | Task | Done when | Needs |
|---|---|---|---|---|
| B-05.1 | design | Threat model: what can a role stop? In the local interface the model has no shell, so roles can be enforced. In a chat session with a shell, an environment variable can be set by the model itself, so a role there is advice, not a lock. State this and design around it (launcher-held capability, or interface-only enforcement) | The note says plainly which surfaces are enforced and which are not | B-02.5 |
| B-05.2 | inventory | Every script against the roles tutor voice, examiner, staff: reads only, writes progress, writes anything else | All 70 scripts have a row; a test fails when a new script has none | none |
| B-05.3 | build | The policy as data (`roles.json`) with a schema, and `tutorlib.roles.require(script, role)` | With no role configured behaviour is identical to today (golden tests unchanged) | B-05.1, B-05.2 |
| B-05.4 | build | Enforcement in the scripts and the hook guard | Student role refused on install, audit, erase, purge, restore, course writes; each has a test | B-05.3, B-04.4 |
| B-05.5 | build | The examiner being offline is said plainly by the session plan and the runner | Test of the message; tests wait rather than pass by default | B-05.3 |
| B-05.6 | build | Claude stays the full fallback | A test runs the whole fixture loop with no role and no local model and gets today's results | B-05.4 |
| B-05.7 | measure | Adversarial read: try to act as another role | Everything tried and what was refused are in the PR | B-05.4 |

## B-06 Fleet and children's data notes (five micro-tasks)

A note for the owner. It is not legal advice.

| ID | Kind | Task | Done when | Needs |
|---|---|---|---|---|
| B-06.1 | inventory | Every kind of personal data the system holds, where, how long, who can read it | Table taken from `PRIVACY.md` and `DATA_MODEL.md`, each row with a file reference | none |
| B-06.2 | design | How course content reaches other machines (D8): options, licensing consequences, update and rollback | Option table with the recommendation | D8 |
| B-06.3 | design | How engine updates reach them: release zip, version pin, `min_engine_version`, rollback | Procedure written and followed once on a clean machine | B-01.7 |
| B-06.4 | design | A school-deployment checklist of duties to ask an adviser about (consent, retention, access, breach), pointing to the regulator's guidance rather than restating it | Checklist merged with the "not legal advice" line | B-06.1 |
| B-06.5 | measure | Owner review | Owner's comments recorded | B-06.2, B-06.3, B-06.4 |

## B-07 Shared, anonymised patterns (seven micro-tasks)

The idea has real value and the highest privacy risk in the wave. It is design-led and last.

| ID | Kind | Task | Done when | Needs |
|---|---|---|---|---|
| B-07.1 | design | What is recorded locally: a short pattern note per error with a fixed form (no names, places or dates), and what `error_events.note` already holds | Field spec with a list of what the check rejects | B-06.1 |
| B-07.2 | design | A fourth consent class, off by default (D11), with an adult's recorded consent for children, and what revoking does | Consent table extended; migration listed | D11 |
| B-07.3 | design | Anonymisation: allowed fields only, minimum group size (D9), how patterns are normalised and counted by distinct learner, re-identification risks for a family or one class | Written risk analysis, each risk with a test in B-07.6 | D9 |
| B-07.4 | build | `pool_export.py`: builds a file the learner can read, contains only allowed fields, sends nothing | A test that no id, date, course-specific identifier or free text leaks; the file is deterministic | B-07.1, B-07.3 |
| B-07.5 | design | Who holds the pool (D10) and how the audit reads it (provenance "pooled, n learners") | Decision recorded; import rules written | D10 |
| B-07.6 | measure | Re-identification red team on synthetic bundles | Attempts and results in the PR; any success blocks the wave | B-07.4 |
| B-07.7 | build | The audit-side import as proposals only, never auto-written | Test that nothing is written without the audit's usual confirmation | B-07.5 |

## Order, and what can start today

1. **Now, with no decision needed (six micro-tasks):** B-04.1, B-04.2, B-05.2, B-06.1, B-01.1 (its default holds), B-02.1 (its default holds). All are inventories or designs, so they cost little and tell us whether the plan survives contact with the code.
2. **Then the foundation:** B-01.2 to B-01.7, because the interface (B-02) and every role and sharing task assume a profile root and a trustworthy profile check.
3. **Then the interface:** B-02.2 to B-02.7, deterministic only.
4. **Then, needing a machine with a model:** B-03.6 is owner-run. Everything else in B-03 can be built and tested offline.
5. **Role policy last** (B-05.3 onward), after B-04.4, because enforcing roles before deciding who judges practice would bake in the wrong rule.
6. **Pattern pool after everything else**, behind its own review.

Totals: 10 + 10 + 7 + 5 + 7 + 5 + 7 = **51 micro-tasks**, of which 6 can start now, 11 owner decisions (D1 to D11) gate others (each has a default, so none blocks), and 4 need the owner's hands or a machine this environment does not have (B-01.10, B-02.10, B-03.6, B-06.5).

## What would make us stop or change course

- The interrupted-write matrix (B-01.4) finds a path that can tear a file: fix it before anything else is built on the medium.
- A local model fails a critical rule that no wording fixes (B-03.6): it does not teach children unsupervised, and the role work becomes an examiner-only design.
- The local interface cannot be made safe against another website on the same computer (B-02.5): it ships as a terminal tool or not at all.
- The re-identification red team (B-07.6) succeeds once: the pool does not ship.
- Real sessions in the pilot show the chat path already meets the need: pause B-02 and spend the effort on content.
