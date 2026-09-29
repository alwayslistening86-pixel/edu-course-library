# S01_Data_Types_and_Programming_Concepts - Test: Data types and core programming concepts

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain the difference between a record and an array as data types. [2 marks]
2. Explain the difference between definite and indefinite iteration, with an example of each. [4 marks]
3. Explain what a pointer/reference data type stores, and why this is different from storing the data itself. [2 marks]
4. Which best describes indefinite iteration? Choose every correct option.
   A. repetition that continues until a condition changes, with the number of repeats not fixed in advance
   B. repetition that always runs exactly once
   C. repetition that only ever nests inside selection
   D. repetition with a fixed, known number of repeats decided before the loop starts

## Answer key (for the tutor only)
1. [2] B1 an array stores multiple values, usually of the same type, indexed by position; B1 a record groups several related fields, possibly of different types, about a single entity under one name.
2. [4] B1 definite: repeats a known, fixed number of times; B1 e.g. printing a 12-times table; B1 indefinite: repeats until a condition changes, number of repeats not known in advance; B1 e.g. reading input until the user types 'quit'.
3. [2] B1 it stores the memory address of another piece of data, not the data's value; B1 following (dereferencing) the pointer is needed to access the actual data it refers to.
4. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S01_Data_Types_and_Programming_Concepts` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 9 marks in all; a pass needs at least 6 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S02_Operators.
