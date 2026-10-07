# Sample courses for evals and tests (A-02)

Three small, self-authored courses so that evals and tests never need the private content repository: `fx_maths_fractions` (a maths level-2 course), `fx_english_persuasion` (a humanities-style level-2 course) and `fx_law_contract` (a standalone, law-style course using the IRAC framework). Each has two stages, a lesson, practice and test per stage, a sourced rubric, an itemised curriculum map, misconceptions, an exam and a question bank.

- **Original content.** Every example and question was written for this repository. None of it comes from an exam board, a publisher or a real specification, and the law course states only generic common-law principles as a sample, not any real jurisdiction's rules. The "source" on each rubric entry says so.
- **Real shape.** They pass the same gate as real courses (`postcompile_gate.py`), coverage is `full`, the rubric lint is clean, and the question banks were produced by `exam_to_bank.py` from each course's own `exam/exam.md`.
- **Regenerating.** Edit the files directly; `tests/test_fixture_courses.py` keeps them valid.
- **Not for learners.** They are minimal on purpose; do not copy them into a real library.
