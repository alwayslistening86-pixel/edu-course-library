# S03_Searching_Algorithms - Test: Searching algorithms: linear and binary search

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer and longer written or code-tracing questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Describe how the linear search algorithm works. [2 marks]
2. Describe how the binary search algorithm works. [3 marks]
3. Trace a binary search for 15 in the sorted list [2, 5, 9, 12, 15, 18, 21, 30] (indices 0-7), showing each middle index checked. [4 marks]
4. Compare and contrast linear search and binary search. [4 marks]
5. A list of 1,000 sorted numbers is searched for a value that is not present. Which statement is true? Choose every correct option.
   A. binary search will need far fewer comparisons than linear search
   B. linear search will need far fewer comparisons than binary search
   C. both algorithms need exactly the same number of comparisons
   D. binary search cannot be used because the value is not present

## Answer key (for the tutor only)
1. [2] B1 start at the first item; B1 check each item in turn (in order) until the target is found or every item has been checked.
2. [3] B1 the list must be sorted; B1 repeatedly compare the target with the middle item of the remaining section; B1 discard the half that cannot contain the target and repeat on the remaining half, until found or nothing is left.
3. [4] M1 middle (0+7)//2=3, list[3]=12 < 15, search right half (4-7); M1 middle (4+7)//2=5, list[5]=18 > 15, search left half (4-4); M1 middle (4+4)//2=4, list[4]=15, found; A1 3 comparisons in total.
4. [4] B1 linear search works on any list (sorted or not); binary search needs a sorted list; B1 linear search checks items one by one from the start; binary search repeatedly halves the section searched; B1 binary search is far more efficient (fewer comparisons) on large lists; B1 linear search can be more efficient for a very small list, or when the list is not sorted and sorting it first would cost more than it saves.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S03_Searching_Algorithms` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 14 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S04_Sorting_Algorithms.
