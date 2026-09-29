# S02_Algorithm_Efficiency - Test: Efficiency of algorithms

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain what is meant by comparing the efficiency of two algorithms that solve the same problem. [3 marks]
2. Two algorithms both correctly sort a list of numbers. Algorithm A takes far longer than Algorithm B on a list of 10,000 numbers, but they take about the same time on a list of 10 numbers. Explain why testing only on small lists could be misleading. [3 marks]
3. Which is the best general definition of an algorithm's efficiency? Choose every correct option.
   A. how few steps or how little memory it needs to solve a problem, especially as the input grows
   B. how short the program code is
   C. how recently the algorithm was written
   D. how many programming languages it can be written in

## Answer key (for the tutor only)
1. [3] B1 how many steps/comparisons, or how much memory, each needs; B1 especially as the size of the input (the data set) grows; B1 the more efficient algorithm reliably needs fewer resources for the same size of problem.
2. [3] B1 an inefficient algorithm can look fine on a small input because the difference in steps needed is small; B1 the difference in efficiency shows up (and matters) as the input size grows large; B1 so efficiency should be judged on larger, more realistic inputs, not just small test cases.
3. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S02_Algorithm_Efficiency` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 7 marks in all; a pass needs at least 5 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S03_Searching_Algorithms.
