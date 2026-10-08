# Goals: tying a learner's goals to the specification (L-22)

Loaded from `SKILL.md` when the learner has `goals` or asks how they are doing against them.

When the learner has `goals`, offer once per course to tie them to the specification. Run `python3 /EDU/.tutor-scripts/goal_map.py items <the learner's profile dir> <the /EDU/courses/ dir> <course_id>` (for a big course it lists topic areas first; ask again with `--area`), read each goal and propose which items it means. Show the proposal in plain words, and only after the learner agrees run `goal_map.py set <subjects/<course_id>.json> <the course folder> "<goal>" '["id", ...]' <today>`. For "how am I doing against my goals?" run `goal_map.py report` and read it out: items taught (stage passed) versus still to come in teaching order, the next stage, any items the course does not teach. Say the mapping is your reading of the goal and can change, and that taught is not learned. A goal is never a grade target or a promise.
