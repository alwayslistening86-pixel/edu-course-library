---
description: Full-suite check across every course, active or not — structural fixes, schema migration, grounding re-verification, and a syllabus-coverage pass. Reports before applying anything beyond Tier 1.
argument-hint: [--report-only] [--course course_id] [--tier N]
---

@${CLAUDE_PLUGIN_ROOT}/skills/course-auditor/SKILL.md
@${CLAUDE_PLUGIN_ROOT}/skills/course-auditor/suspension.md

Run the `/audit` flow described above. Arguments: `--report-only` (change nothing, not even Tier 1), `--course <course_id>` (one course; also `audit_run.py --course`, and do not save that report as the baseline), `--tier N` (only tier 1, 2 or 3). Anything else: say what is accepted and run nothing.
