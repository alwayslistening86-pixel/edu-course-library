# PPE (Philosophy, Politics and Economics) — Oxford syllabus structure and examination conventions - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` shows a passed test in the micro-profile - in practice this means Prelims_Politics, Prelims_Philosophy and Prelims_Economics are unlocked and tested together first (they are sat as one examination at Oxford), and the six chosen FHS papers are unlocked and tested together afterwards, exactly mirroring the real two-stage structure of Prelims followed by Finals.

## Format
**Preliminary Examination (Prelims), sat first:** three written papers - Introductory Economics, Introduction to Philosophy, Introduction to the Theory and Practice of Politics. The Philosophy paper requires candidates to show adequate knowledge in each of its three required sections (Logic, General Philosophy, Moral Philosophy). The Politics paper requires four questions answered, at least one from Section A (Theory) and two from Section B (Practice). The Economics paper requires coverage across Microeconomics, Macroeconomics and Quantitative Methods. A candidate passes Prelims only by satisfying the examiners in all three subjects; this course's Prelims papers are examined together as a single unlock/pass event, matching that all-three rule. (The fetched Prelims regulations did not state individual paper duration; assume the standard Oxford written-paper format of several hours per subject, unless the learner's own placement or a more specific source states otherwise - flagged, per material_vintage, for re-verification.)

**Final Honour School (Finals), sat after Prelims:** one written paper per chosen FHS subject - Political Thought: Plato to Rousseau (215), Political Thought: Bentham to Weber (216), International Relations (214), Practical Ethics (128), Theory of Politics (203), and Game Theory (set in two parts, both examined). Each of the essay-based FHS papers follows the standard Oxford Final Honour School format of a three-hour written examination in which candidates answer three questions; this specific figure was not confirmed on the fetched Honour School regulations page for PPE and is flagged in material_vintage as the standard, well-established format rather than a directly read figure. The six chosen FHS papers are examined together as a single unlock/pass event in this course, matching how Finals classification is awarded across a candidate's whole paper set rather than paper-by-paper.

## Example structure
Prelims paper draws on Prelims_Politics, Prelims_Philosophy and Prelims_Economics together - require at least one strong answer from each subject before treating Prelims as passed. Finals paper draws on all six FHS stages (Political Thought x2, International Relations, Practical Ethics, Theory of Politics, Game Theory) - require genuine breadth across at least four of the six papers, with adequate (not necessarily brilliant) performance on the rest, matching how an Oxford class is awarded on a candidate's whole set of papers rather than any single strong paper compensating for a genuinely weak one.

## Grading
Apply `rubric.json`'s `exam_rubric` exactly.

## Outcome
- **Pass** -- record `exam_status: "passed"` in the micro-profile. Course complete.
- **Not yet** -- leave `exam_status: "available"`, name the stage(s) that broke down, offer targeted review or a fresh retry paper.
