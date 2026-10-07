# Content contract (N-01)

What the engine expects of a course library, and what it promises back. The library may live anywhere (today: the private `edu-courses-private` repository); the engine finds it through the data root (`resolve_root.py`) and reads `<root>/courses/`.

## Folder layout
```
<root>/courses/<course_id>/
  course.json              required   schema: tutorlib/schemas/course.json (schema_version 4)
  curriculum_map.json      required   schema: curriculum_map.json - stage index + itemised specification
  rubric.json              required   schema: rubric.json - every entry sourced (issuing body, document, reference)
  stages/<stage_id>/lesson.md, practice.md, test.md      required for every id in course.json.stage_ladder
  stages/<stage_id>/misconceptions.json                  optional; if present, schema misconceptions.json (non-empty array)
  exam/exam.md             required only when course.json.exam.enabled
  question_bank.json       optional   schema: question_bank.json - questions with marks, items, mark scheme and model answer; enables /mock
  connectors.md            optional   records which suggested connectors are connected
  change.md                optional   dated records of detected source changes (facts and sources only); format below
```
`<course_id>` is 1-64 letters, digits, `_`, `.`, `-`, starting with a letter or digit. Anything else in a course folder is ignored by the engine. A folder in `courses/` is a course only if its name is a valid id **and** it holds a `course.json`; every script that scans the library applies that one rule (`tutorlib.paths.course_ids`), so a leftover `.import-<id>.tmp`, a `_scratch` folder or a stray directory is never listed, audited or counted. See *Course lifecycle* below for `_staging/` and `_historic/`.

## Course lifecycle
A course is in exactly one of these places. The engine decides what each means; people move courses between them.

| Place | Meaning | Engine behaviour |
|---|---|---|
| `courses/<id>/`, `course.json` without `lifecycle` (or `"live"`) | **Live.** | Listed, audited, taught subject to the gates, open to new enrolments. |
| `courses/<id>/`, `"lifecycle": "retiring"` in `course.json` | **Retiring**: a duplicate being phased out. | As live, except `enrol.py` refuses new enrolments and `/list-courses` labels it. Learners already enrolled carry on to completion. |
| `courses/.build-<id>/` | **Being compiled.** | Not a course: invisible to every listing and to enrolment until `publish_course.py publish` renames it into place. |
| `courses/` entry that is not a valid id or has no `course.json` | **Not a course.** | Ignored everywhere, never an error. |
| `_historic/<id>/` (next to `courses/`) | **Retired** by the library owner. | Never read, listed or taught. |
| `_staging/` (next to `courses/`) | **Owner scratch space**: build and migration tooling, work in progress. | Never read or written. |

- **Transitions.** live to retiring: the auditor's duplicate merge sets `lifecycle: retiring` in `course.json` when enrolled learners are far enough through a duplicate copy that they should finish on it. Retiring to retired, and retired back to live: the library owner moves the folder between `courses/` and `_historic/` by hand. The auditor, a skill or the model never moves, renames or deletes a course folder; once the last enrolled learner has finished or moved, the auditor only tells the owner the copy can go.
- **A retired course and its learners.** A move touches no learner file. A learner enrolled in a retired course stops at the first gate with a `read_error` (the course cannot be read); their progress is untouched, and moving the folder back restores teaching.
- **Who adds a course.** `publish_course.py publish` (the compiler's last step) and `course_bundle.py import` (only when asked). The only folders a script removes are its own `.build-` and `.import-` scratch folders; never a course.
- **`currency: "historical"` is a different thing.** It is a field meaning the underlying subject is frozen or discontinued, so the live recheck is skipped permanently (gate 4). Such a course is still live and still taught. A course in `_historic/` is one the owner has retired. The words are similar; neither implies the other.
- **A compile is invisible until it passes.** The compiler writes into `courses/.build-<id>/` and `publish_course.py publish` runs the post-compile gate, then renames the folder to `courses/<id>/` in one step, so a course appears whole or not at all and a failed or abandoned compile never shows in `/list-courses` or can be enrolled in. `publish_course.py discard` removes a leftover build folder, and `/doctor` reports one. An interrupted `course_bundle.py import` leaves a `.import-<id>.tmp` folder the same way. Neither is a course. `_staging/` is not used for this.

## Rules the engine enforces
1. **Sourced rubric or no course.** Every ladder stage has a rubric entry whose `source` names issuing body, document and reference. The compiler never authors criteria.
2. **Structure.** Every ladder stage has its three files; no orphaned stage folders (reported as advisory).
3. **Coverage honesty.** `coverage_status` is *derived* by `coverage_check.py`; a stored value that disagrees is a mismatch. Itemised specifications map items to stages through `covers_items`; unmapped items are listed, not hidden.
4. **Content is data.** Files derived from web sources must contain no instruction-like text (`scan_untrusted.py`; blocking hits stop a course shipping). `change.md` records facts and sources, never page prose. See `UNTRUSTED_CONTENT.md`.
5. **No exam-board verbatim.** Paraphrase specifications and mark schemes; this is why the library is private.
6. **Compatibility.** A course that relies on a newer engine sets `min_engine_version` (`"1.26.0"`); older installs stop at gate 0 with a clear message. Schema versions only move through `migrate_schema.py` (`/audit`).

## How a library validates itself in CI
In the content repository, call the reusable workflow in this repository:
```yaml
jobs:
  validate:
    uses: alwayslistening86-pixel/edu-course-library/.github/workflows/validate-courses.yml@main   # pin a release tag for reproducible CI
    with: { engine_ref: main, courses_path: courses }
```
or run it yourself: `python3 .github/scripts/validate_courses.py --courses <dir> --engine <path to this repo>`. It runs structure, coverage, JSON-Schema, injection-scan and engine-version checks on every course and fails the build if any course has a problem. Locally on an installed system, `/doctor` runs the same schema and structure checks, and `/audit` adds the live-web verification that CI deliberately does not do.

## What the engine promises
It never writes into `courses/` during teaching; only the compiler (at build time), the live recheck (`last_live_recheck`, `grounding_status`, `change.md`) and `/audit` modify a course. Learner data lives under `profile/`, never in a course folder.

## `change.md` format
```
# Change log - <course_id>
## YYYY-MM-DD - <title>          (the dash may be -, – or —; entries run oldest first; the first is "built")
Free text. Optional bold labels: **Found by:** · **Fixed:** · **Revalidated:** · **Source:**
```
`change_log.py <course_dir>` reads it as data (entries, dates, labels, `built_on`) and `postcompile_gate` notes any deviation (advisory only). On the 62 real courses 45 have a file with 69 entries; 5 lack a "built" entry and 4 lack the title line.
