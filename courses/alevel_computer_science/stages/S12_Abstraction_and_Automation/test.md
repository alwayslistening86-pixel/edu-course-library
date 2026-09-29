# S12_Abstraction_and_Automation - Test: Problem-solving, abstraction and automation

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain the difference between decomposition and composition. [3 marks]
2. Explain the difference between data abstraction and representational abstraction, with an example of each. [4 marks]
3. Explain what is meant by automation in the context of a solved, implemented algorithm. [2 marks]
4. Which form of abstraction hides how a subroutine internally computes its result, behind its name and interface? Choose every correct option.
   A. procedural abstraction
   B. representational abstraction
   C. problem abstraction
   D. data abstraction

## Answer key (for the tutor only)
1. [3] B1 decomposition breaks a large problem into smaller, more manageable sub-problems; B1 composition builds a solution to the whole problem by combining smaller procedures or pieces of data back together; B1 they are complementary: decomposition happens during design, composition happens when the parts are assembled into the final solution.
2. [4] B1 data abstraction hides how a data structure is represented/implemented internally, exposing only the operations available on it; B1 e.g. a stack's push/pop hides whether it is built from an array or a linked structure; B1 representational abstraction models something in the real world, keeping only details relevant to the problem; B1 e.g. a tube map showing only stations and connections, not true distances.
3. [2] B1 the computer executes the implemented algorithm/code itself, carrying out the process without a human performing each step manually; B1 this only becomes possible once the algorithm has been correctly designed and implemented in code and appropriate data structures.
4. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S12_Abstraction_and_Automation` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 10 marks in all; a pass needs at least 6 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S13_FSM_Regex_and_BNF.
