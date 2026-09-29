# S04_Sorting_Algorithms - Test: Sorting algorithms: bubble sort and merge sort

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Describe how the bubble sort algorithm works. [3 marks]
2. Describe how the merge sort algorithm works. [3 marks]
3. Trace a full bubble sort of [4, 3, 1, 2], listing the list after each pass. [4 marks]
4. Compare and contrast bubble sort and merge sort. [4 marks]
5. Which is true of merge sort? Choose every correct option.
   A. it splits the list before merging sorted sub-lists back together
   B. it only ever swaps neighbouring items
   C. it cannot be used on a list with duplicate values
   D. it needs the list to already be partly sorted

## Answer key (for the tutor only)
1. [3] B1 repeatedly step through the list comparing neighbouring pairs; B1 swap them if they are in the wrong order; B1 repeat full passes (each can be shorter, as the largest remaining item bubbles to the end) until a pass makes no swaps.
2. [3] B1 repeatedly split the list in half until each sub-list holds one item; B1 repeatedly merge pairs of sorted sub-lists by comparing their front items and taking the smaller each time; B1 continue merging until one fully sorted list remains.
3. [4] M1 pass 1: compare 4,3 swap->[3,4,1,2]; compare 4,1 swap->[3,1,4,2]; compare 4,2 swap-> list is [3,1,2,4]; M1 pass 2: compare 3,1 swap->[1,3,2,4]; compare 3,2 swap-> list is [1,2,3,4]; A1 pass 3: compare 1,2 no swap; compare 2,3 no swap -- no swaps made, so sorted; A1 final sorted list [1,2,3,4].
4. [4] B1 bubble sort compares/swaps neighbouring pairs in place; merge sort splits the list and merges sorted sub-lists, needing extra memory; B1 merge sort is far more efficient than bubble sort on large lists; B1 bubble sort is simpler to write/trace by hand and needs no extra memory; B1 for a very small or already nearly-sorted list, bubble sort can be efficient enough in practice.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S04_Sorting_Algorithms` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 15 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S05_Data_Types_and_Programming_Concepts.
