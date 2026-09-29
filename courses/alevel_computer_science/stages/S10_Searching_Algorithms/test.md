# S10_Searching_Algorithms - Test: Searching: linear search, binary search and binary tree search

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Trace a binary search for 15 in the sorted list [3, 8, 15, 21, 26, 34, 40, 55] (indices 0-7), showing each middle index checked, and state the number of comparisons. [4 marks]
2. State the Big-O time complexity of linear search and of binary search, and explain the one precondition binary search needs that linear search does not. [3 marks]
3. Explain why binary tree search can degrade from O(log n) towards O(n), and describe the tree structure where this happens. [3 marks]
4. A list of 1,000,000 sorted numbers is searched for a value using binary search. Roughly how many comparisons does this need in the worst case, compared with linear search? Choose every correct option.
   A. around 20, far fewer than linear search's up to 1,000,000
   B. exactly the same number as linear search
   C. around 500,000, half of linear search's worst case
   D. more comparisons than linear search, because binary search checks the middle repeatedly

## Answer key (for the tutor only)
1. [4] M1 middle (0+7)//2=3, list[3]=21 > 15, search left half (0-2); M1 middle (0+2)//2=1, list[1]=8 < 15, search right half (2-2); M1 middle (2+2)//2=2, list[2]=15, found; A1 3 comparisons.
2. [3] B1 linear search: O(n); B1 binary search: O(log n); B1 binary search requires the list to already be sorted, linear search does not.
3. [3] B1 binary tree search's efficiency relies on each comparison eliminating roughly half the remaining nodes, which needs a balanced tree; B1 on a poorly balanced tree (e.g. one where every node only has a right child, or only a left child), each step eliminates almost nothing; B1 such a tree behaves like a simple linked list, so search degrades to O(n).
4. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S10_Searching_Algorithms` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 11 marks in all; a pass needs at least 7 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S11_Sorting_and_Dijkstra.
