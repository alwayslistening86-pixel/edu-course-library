# S15_The_Computing_and_IT_Project - Test: The computing and IT project: methodology and practice

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems, code-trace/code-output items, multiple-select conceptual items and, where the topic is genuinely discursive (professional/ethical/HCI content), extended-response items marked on levels. Give the whole test at once, with no hints; the learner shows full working/code. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain the difference between a literature review that is merely descriptive and one that is genuinely critical/comparative, giving an example of each for a project comparing two caching strategies. [4 marks]
2. A student's project plan for implementing and evaluating a sorting-algorithm visualiser has one risk identified: 'the chosen GUI library might be hard to learn'. Explain what is missing from this as a risk-management entry, and complete it properly. [4 marks]
3. Explain why a project report's Evaluation section should be written against success criteria defined before the system was built, rather than criteria chosen afterwards based on what the system happens to do well. [3 marks]
4. Explain what 'critical reflection' means in a project report's conclusion, and why a report claiming the project had no limitations at all is generally viewed unfavourably at honours level. [3 marks]
5. Which statements about computing project methodology are correct? Choose every correct option.
   A. A Gantt chart is used to visualise a project's milestones and their dependencies/timing
   B. Qualitative methods such as interviews and thematic analysis are appropriate when a project directly evaluates real users' experience
   C. A risk-management entry is complete once a risk has simply been named
   D. Regular, meaningful version-control commits provide evidence of a project's genuine progression over time

## Answer key (for the tutor only)
1. [4] B1 descriptive: lists what each source/prior approach did, e.g. 'Source A implemented an LRU cache; Source B implemented an LFU cache', with no comparison or judgement; B1 comparative/critical: explicitly compares the sources against each other and against the project's own aims, e.g. 'Source A's LRU approach performs well under recency-biased access patterns but Source B shows LFU outperforms it under a stable long-term popularity distribution, suggesting the choice should depend on the workload this project's own evaluation will need to characterise'; B1 the descriptive version fails to identify a gap or justify the project's own direction; B1 the comparative version explicitly uses the comparison to motivate/justify a choice the project itself then makes.
2. [4] B1 the entry names a risk but has no assessment of likelihood/impact and no mitigation or contingency plan, so it is incomplete as risk management; B1 a likelihood/impact judgement should be added, e.g. 'medium likelihood, high impact if it delays core implementation'; B2 a genuine, specific mitigation/contingency, e.g. 'allocate a fixed 3-day time-box to learn the library, with a documented fallback to a simpler, already-familiar library if progress is insufficient by then' (B1 if a mitigation is given but is vague/unspecific, e.g. just 'try to learn it faster').
3. [3] B1 success criteria set in advance are a genuine, falsifiable test of whether the project achieved its stated aims; B1 criteria chosen afterwards, based on the finished system's actual behaviour, risk being unconsciously (or consciously) tailored to make the project look more successful than a fair, independent evaluation would show; B1 predefined criteria also make the evaluation reproducible/checkable by a reader, and demonstrate the student planned the work rigorously rather than only building something and post-hoc justifying it.
4. [3] B1 critical reflection means evaluating one's own work, decisions and process with genuine rigour -- what worked, what did not, what would be done differently with hindsight -- not simply narrating what was done; B1 every real project has genuine limitations (time constraints, scope decisions, things that did not work as planned, threats to validity of an evaluation); B1 a report claiming none is read as either lacking the self-awareness/rigour to identify them, or lacking the honesty to report them, both of which undermine the report's credibility rather than strengthening it.
5. Correct: A, B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S15_The_Computing_and_IT_Project` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 15 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass. Every stage is now passed, so the cumulative exam becomes available.
