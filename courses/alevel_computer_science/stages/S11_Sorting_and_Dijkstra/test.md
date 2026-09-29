# S11_Sorting_and_Dijkstra - Test: Sorting: bubble sort and merge sort; Dijkstra's shortest path algorithm

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. State the Big-O time complexity of bubble sort and of merge sort in the worst case, and explain why merge sort scales better to large lists. [3 marks]
2. Describe how merge sort works, including what happens once every sub-list holds a single item. [3 marks]
3. Using the graph with edges P-Q(2), P-R(6), Q-R(3), Q-S(8), R-S(1), trace Dijkstra's algorithm from P to find the shortest distance to every node, showing each node visited and its final distance. [5 marks]
4. Which statement about Dijkstra's algorithm is correct? Choose every correct option.
   A. it works correctly only when all edge weights are non-negative
   B. it always visits nodes in alphabetical order regardless of distance
   C. it finds the longest path between two nodes
   D. it cannot be used on a graph with more than two nodes

## Answer key (for the tutor only)
1. [3] B1 bubble sort: O(n^2); B1 merge sort: O(n log n); B1 merge sort's divide-and-conquer approach needs far fewer total comparisons as n grows large, because n log n grows much more slowly than n^2.
2. [3] B1 repeatedly split the list in half until each sub-list holds one item (a single item is already 'sorted'); B1 repeatedly merge pairs of sorted sub-lists by comparing their front items and taking the smaller each time; B1 continue merging pairs of (growing) sorted sub-lists until one fully sorted list remains.
3. [5] M1 dist P=0; visit P, relax: Q=2, R=6; M1 visit Q (smallest, 2), relax: R = min(6, 2+3)=5; M1 visit R (5), relax: S = min(inf, 5+1)=6; also compare with Q-S=2+8=10, so 6 is smaller; M1 visit S (6); A1 final distances P=0, Q=2, R=5, S=6, shortest path to S is P-Q-R-S.
4. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S11_Sorting_and_Dijkstra` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S12_Abstraction_and_Automation.
