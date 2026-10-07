# B-06.2: How course content reaches other machines

Micro-task B-06.2 of `docs/WAVE7.md`. A design note for the owner, **not legal advice**. Nothing is built. It uses the owner's accepted default for D8: a private repository per site, read-only, pinned to a tag, with no public mirror (ADR 0006).

## The constraint that shapes everything
Courses paraphrase copyrighted exam-board specifications and mark schemes. The engine is MIT-licensed and public; the courses are not (ADR 0006), and live in the private companion repository. Moving courses to another machine is therefore a decision about **who may hold a copy**, not only a technical one. The engine cannot settle that. What it can do is make every route verify what arrives and keep learner data out of it.

## What the engine already provides for moving courses
- **Course bundles** (`course_bundle.py`, N-12): one zip per course with a manifest and a sha256 for every file; refuses learner-data file names, absolute or `..` paths and a bundle from a newer plugin; imports through a staging folder and only renames into place after `validate_structure` passes and the injection scan finds nothing blocking. An existing course is kept unless `--replace`, and a failed replace leaves it untouched.
- **A minimum engine version** per course (`min_engine_version` in `course.json`, N-02): a course that needs a newer engine than the machine has is reported, not half-used.
- **Publish by rename** (`publish_course.py`, N-15): a compiled course appears whole or not at all.
- **A reusable validation workflow** (`validate-courses.yml`, N-03): a content repository calls it to check its courses against a chosen engine tag.
- **A content contract** (`docs/CONTENT_CONTRACT.md`): the folder layout and lifecycle a library must follow.

## The options

| Option | How courses arrive | How an update arrives | Rollback | What can go wrong | Verified on arrival |
|---|---|---|---|---|---|
| **A. Private repository checkout per site** (the accepted default) | `git clone` of the private repository on each machine, read-only, at a release tag | `git fetch` and check out the next tag | Check out the previous tag | A site holding more than the licence allows; an engine older than a course needs; a half-finished pull | The content repository's own CI ran `validate-courses` against a pinned engine tag before the tag was cut |
| **B. Course bundles** | `course_bundle.py export` on the library machine, a zip carried or sent, `import` on the target | Export and import again with `--replace` | The replace moves the old course aside first; keep the previous zip | The bundle is trusted content from outside the machine | Manifest hashes, path rules, structure check and injection scan, all before anything goes live |
| **C. A shared read-only folder** (a school server or mounted drive) | The machines point `courses/` at the share | The share changes under every machine at once | Restore the share from its own backup | Every machine changes together, mid-lesson; a network drop leaves a session without a course | None on the machine; whatever put the files there must have run the checks |
| **D. Copy by hand** (a stick, a file transfer) | Copy folders | Copy again | Keep the old folder | Partial copies, stray learner data, drift between machines | Nothing; the post-compile gate can be run by hand |

## Recommendation
- **One site, one machine, a few courses:** B (bundles). It carries the checks with it and moves exactly one course.
- **A household or a small school with several machines:** A, pinned to a tag, read-only. Updates are a deliberate step, rollback is one command, and the content repository's CI is the gate.
- **Avoid C** until a site has its own backup and change process; one bad push changes every machine at once.
- **Avoid D** for anything a learner depends on.

## What has to be true for A to be safe
1. **Teaching needs read access to courses only.** Teaching commands are not supposed to edit course files (the hook guard refuses it for the commands it knows). This claim has not been proven by a test that runs the teaching path against a read-only courses folder; that test is the first follow-up and gates recommending A for a site with a read-only mount.
2. **A tag is only cut after validation passes.** The content repository calls `validate-courses.yml` with a pinned engine tag; a tag without a green run is not deployed.
3. **The engine and the courses move together.** The deployment note names the engine release each course tag was validated against; `min_engine_version` catches a course that needs a newer one.
4. **No learner data ever enters the content repository.** `.gitignore` and the content contract already say so; a site must not put `profile/` inside the checkout (the profile root can now be separate, ADR 0011).

## What this note does not decide
- **Licensing.** Whether an exam board's terms allow a school to hold a derived course on several machines is a legal question for the owner or the school. Nothing in the engine enforces a licence.
- **Authentication to the private repository** (deploy key, token, or a mirror inside a school's own network) is the site's choice; keeping a credential off the learners' machines matters and is not designed here.
- **Who may add courses** on a school machine. That is the role question (B-05) and the staff channel.

## Follow-ups this note creates
| Follow-up | Proves |
|---|---|
| A test that runs the teaching path (status, next items, practice, review, record) with the courses folder read-only | Claim 1 above |
| A deployment procedure for A, followed once on a clean machine (owner-run) | The steps are complete and in the right order (B-06.3 covers engine updates; this covers courses) |
| A bundle round-trip check on a course carrying `exam_technique.md` and `command_words.json` | The new optional files survive a move (the export walks the whole course folder apart from learner-data names, so they should travel; nothing tests it yet) |
