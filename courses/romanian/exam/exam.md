# Romanian (ACLro) — Institutul Limbii Române, CEFR A1 through C2 - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` shows a passed test in the micro-profile, for the CEFR level currently being certified (the learner and tutor agree in advance which level -- A1, A2, B1, B2, C1 or C2 -- is being targeted for this sitting, since Romanian language proficiency, unlike a single GCSE-style qualification, is genuinely certified one CEFR level at a time by bodies such as ILR).

## Format
This is not a single cumulative exam testing all six levels together (a genuine CEFR-style proficiency check makes no more sense that way than a real ILR sitting would). Instead, at whichever CEFR level the learner has just completed (all of that level's stages passed), run a combined proficiency assessment with four parts, mirroring the structure of real CEFR-aligned language certification:
1. **Listening** -- two or three short passages at the target level (dialogue, monologue, announcement, as appropriate to the level) with comprehension questions, drawing on that level's CD-listen descriptor and vocabulary/grammar from that level's stages.
2. **Reading** -- two or three short texts at the target level (notice, letter, article, literary extract, as appropriate) with comprehension questions, drawing on that level's CD-read descriptor.
3. **Speaking** (spoken interaction and spoken production combined) -- one short role-play/interaction task and one longer monologue/presentation task, drawing on that level's CD-spokeninteract and CD-spokenprod descriptors and the grammar taught at that level.
4. **Writing** -- one writing task appropriate to the level (postcard/form at A1, up to a structured essay/report at C1-C2), drawing on that level's CD-write descriptor.
Each part is graded against the CEFR can-do descriptor wording for that level and skill (as taught in that level's CD-* stage), not against a fixed mark scheme, since CEFR-based certification is criterion-referenced rather than marks-based. Grammar and vocabulary accuracy from that level's G/V stages is assessed as part of how well the learner performs the four skill tasks, not as a separate section.

## Example structure
For an A1 sitting: draw listening/reading material from S01-S04 vocabulary and grammar, and set the speaking/writing tasks to the A1 CD descriptors taught in S05. For a B1 sitting: draw material from S06-S14 (imperfect, subjunctive, reported speech, opinions, media) and set tasks to the B1 CD descriptors from S15. For a C2 sitting: draw material from S16-S23 (full subjunctive/conditional/passive system, register control, idiom, rare constructions) and set tasks to the C2 CD descriptors from S24, expecting near-native fluency and register control throughout. Once a learner has passed every level's exam in sequence from A1 to C2, the course as a whole is complete.

## Grading
Apply `rubric.json`'s `exam_rubric` exactly. A pass at any given level requires performance consistent with that level's CEFR can-do descriptors across all four parts (listening, reading, speaking, writing), with grammar and vocabulary from that level's stages used accurately enough not to obstruct communication at that level's expected standard (increasingly demanding as the level rises: A1 tolerates frequent minor error if meaning is clear; C2 expects near-native precision).

## Outcome
- **Pass** -- record `exam_status: "passed"` in the micro-profile for that CEFR level. If it is C2, the whole course is complete; if it is a lower level, the learner proceeds to the next level's stages, which unlock in sequence.
- **Not yet** -- leave `exam_status: "available"`, name which stage(s) or skill area(s) broke down (for example, "spoken production at B1 was not yet connected enough" or "the passive voice from S16 was not used correctly in the C1 writing task"), offer targeted review of those specific stages, and offer a fresh retry sitting with new listening/reading/speaking/writing material at the same level.
