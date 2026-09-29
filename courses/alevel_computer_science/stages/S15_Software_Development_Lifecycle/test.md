# S15_Software_Development_Lifecycle - Test: The systematic approach to problem solving: analysis, design, implementation, testing, evaluation

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Describe what happens during the analysis stage of the systematic approach to problem solving. [3 marks]
2. Explain the difference between normal, boundary and erroneous test data, giving an example of each for a field accepting whole-number ages from 0 to 120. [3 marks]
3. Explain what acceptance testing is, and why it matters in addition to testing individual parts of the code. [2 marks]
4. Describe two criteria that could be used to evaluate a finished computer system, beyond simply whether it works. [2 marks]
5. Which stage of the systematic approach involves designing the data structures, algorithms and modular structure of a solution, before any code is written? Choose every correct option.
   A. `design`
   B. `analysis`
   C. `implementation`
   D. `evaluation`

## Answer key (for the tutor only)
1. [3] B1 the problem is clearly defined and the requirements of the system are established; B1 this is usually done by interacting directly with the system's intended users; B1 a data model of the information the system will handle is created (possibly clarified iteratively through prototyping/an agile approach).
2. [3] B1 normal: a typical, clearly valid value, e.g. 45; B1 boundary: a value right at the edge of the valid range, e.g. 0 or 120 (or 121/-1, just outside it); B1 erroneous: an invalid value that should be rejected, e.g. -5, 200, or "abc".
3. [2] B1 acceptance testing checks the finished system with its intended users, against the original requirements from analysis; B1 code can work correctly (pass technical tests) while still failing to actually meet what the users needed -- acceptance testing catches that gap.
4. [2] B1 any valid criterion with explanation, e.g. efficiency (does it use time/memory reasonably); B1 a second valid criterion, e.g. usability, robustness (handles errors gracefully) or maintainability (easy to understand and modify later).
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S15_Software_Development_Lifecycle` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 11 marks in all; a pass needs at least 7 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S16_Number_Systems_Bases_Units.
