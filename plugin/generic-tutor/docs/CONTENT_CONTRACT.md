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
  connectors.md            optional   records which suggested connectors are connected
  change.md                optional   dated records of detected source changes (facts and sources only)
```
`<course_id>` is 1-64 letters, digits, `_`, `.`, `-`, starting with a letter or digit. Anything else in a course folder is ignored by the engine. `_staging/` and `_historic/` next to `courses/` are **not** courses: the engine never lists, teaches or counts them (staging = being compiled, historic = retired).

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
