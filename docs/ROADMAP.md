# Roadmap: where we are and what comes next

Written 7 Oct 2026 at v1.88.0. This is the plain-words companion to the task list. The numbers and task states come from `docs/TASKS.md` (run `python3 tools/tasks_status.py` for the live count); this file says what they mean and what order to do things in. It is a plan, not a promise: update it when the plan changes.

## Where we are
**192 of 225 tasks are done**, 11 are partly done by decision, 4 are deferred and 18 are open. The engine is finished in the sense that matters for a household tool:

- Scripts own every progress record; the model teaches and never writes state. Consent, atomic writes, locks, backups, erase and an injection scanner are enforced in code, not left to prose.
- A course is built from a cited source, gated before it goes live (structure, coverage, leftover template text, injected instructions), and published by rename so a half-built course is never visible.
- The teaching rules (hints that keep the answer for last, worked examples that fade, the real-situation guard, accessibility modes, locale spelling) are each measured by an eval suite, and the whole thing runs on about 900 tests on Linux and Windows CI.
- Every version from 1.79.0 on has a GitHub release with an installable `.plugin` zip.

## What is actually left, in four piles

**1. Needs a person, not code.** Branch protection on `main` (R-15) and the About box are yours. Three Dependabot PRs wait for a decision. The biggest content gap, `misconceptions.json` (empty for all 1,253 stages), is not a coding job: it is an audit enrichment run (`/audit`, Tier 3) over courses built before that step existed, and it needs somewhere that can reach the exam-board sites (your machine or Cowork), because this sandbox cannot.

**2. Needs real learners first.** L-14 (is the review schedule right?), A-12 (which questions are too easy or broken?) and K-24 (pass/fail or graded recall?) can only be answered from months of real attempts. A-14 needs the evals run on other model sizes. None of these can be built ahead of the data; the household pilot below is what starts the clock on them.

**3. Buildable now, and worth doing in this order.**
- **L-22** goal alignment: turn a learner's stated goal into a prioritised set of syllabus items and show progress against it.
- **N-05, then L-09 and L-08**: have the compiler write exam technique and command words, then make the tutor use them and the mock-exam flow. The mock-exam machinery exists (`/mock`); it is waiting on question banks.
- **N-08** an item-level prerequisite graph (a schema migration, so it is the largest).
- **X-08** backup encryption. Standard-library Python has no real encryption, so this needs a decision about adding one dependency or only warning.
- **L-06** more card types. Later: K-05 and K-09 (splitting two long skills; deliberately waiting for evals), and the small hook and polish items (P-12, P-14, P-16).

**4. The surfaces (Wave 7, tasks B-01 to B-07).** Direction is accepted in `docs/adr/0010-proposed-roles-and-portable-profile.md`; nothing is designed or built yet, and every task starts with a design step. This is the "next rebuilds" below.

## The next few rebuilds
Each is a stage you can stop after. Order matters: each one is cheaper and safer because of the one before it.

**Rebuild 1: the household pilot (no new architecture).** Use what exists with your own children, supervised, and fix what real use finds. This is deliberately first because the biggest unknown is no longer code: learning outcomes have never been measured, the Cowork surface is untested, and the new publish path has not yet run a real compile. It also starts the data that unlocks pile 2. Alongside it: run the misconception enrichment over a few courses, and build L-22.

**Rebuild 2: the portable profile (B-01).** Learner state travels with the learner: the engine finds the profile on any mounted folder or drive, checks it is a valid profile before a session starts, copes with an unplug mid-write, and can encrypt it. This is the settled answer to several children on one machine, and it is where X-08 (encryption) naturally lands.

**Rebuild 3: a local interface (B-02).** A simple window over the same scripts, deterministic questions first (multiple choice, numeric, review cards), with no model involved in the bookkeeping. This is the first surface a child can open without a chat window. Claude or a local model plugs in later as the teaching voice.

**Rebuild 4: role-separated models (B-03, B-04, B-05).** A small local model as the everyday tutor voice, a stronger model as examiner for anything that moves progress, and Claude as the full fallback when no local model is set up. Before any of that, three things are decided and measured: who may judge why an answer was wrong when the tutor is not the examiner, how the local model scores on every eval suite, and a table of which role may call which script.

**Rebuild 5, only if wanted: fleet and shared patterns (B-06, B-07).** Notes on running this on many machines or at a school (including children's data duties, which are for you or a school's adviser, not code), and an optional, opt-in, anonymised pool of error patterns.

## Is it ready for your children?
Closer than it looks, with honest limits. What is solid: scripts, not the model, make every write to a learner's record, atomically and under the learner's consent setting; coverage numbers come from a script and the tutor is told to disclose gaps; backups and erase are tested; and you can hand a tutor or parent a short progress summary (`/dashboard`, on request). What is not yet known: whether it actually teaches well (nobody has measured learning), how it behaves on the Cowork surface, and how the real-situation guard handles what children raise in practice (distress, safeguarding), which the evals only cover with synthetic cases.

A sensible way in: sit with the first two or three sessions per child, read `/status audit` after each, keep backups outside any synced folder (they are not encrypted yet), and write down what confuses them. That list is the best input the next rebuild could have. The one extra piece of work I would do before they use it unsupervised is a focused review of how the real-situation guard handles under-16s; say the word and it goes to the top.

## Where things live
- `docs/TASKS.md`: every task, its state, the waves and the live counts.
- `docs/PLAN.md`: the original redesign plan and decisions. `docs/adr/`: lasting decisions, including ADR 0010 for the surfaces.
- `CHANGELOG.md` and the Releases page: what changed in each version, and the installable zip.
- `plugin/generic-tutor/docs/`: the data model, privacy notes and content contract the shipped plugin refers to.
