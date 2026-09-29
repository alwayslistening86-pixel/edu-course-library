# S11_Sorting_and_Dijkstra - Lesson: Sorting: bubble sort and merge sort; Dijkstra's shortest path algorithm

## Goal
The learner traces and analyses the time complexity of bubble sort and merge sort, and traces Dijkstra's shortest path algorithm.

## Syllabus items taught here
- 4.3.5.1 - Bubble sort
- 4.3.5.2 - Merge sort
- 4.3.6.1 - Dijkstra's shortest path algorithm

## How to teach this
Ask the learner to imagine finding the fastest route between two towns on a map with distances marked on each road -- how would they decide which road to try next at each junction? AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.3.5.1 Bubble sort
**Bubble sort**: repeatedly step through the list comparing neighbouring pairs, swapping them if out of order; each full pass moves the largest unsorted item to its correct position at the end, so passes can shorten; repeat until a pass makes no swaps. Worst case: roughly n² comparisons/swaps, giving **O(n²)** time complexity -- simple, but inefficient on large lists. *Worked pass:* [6, 2, 7, 1] -- compare 6,2 swap -> [2,6,7,1]; compare 6,7 no swap; compare 7,1 swap -> [2,6,1,7] after pass 1.

#### 4.3.5.2 Merge sort
**Merge sort**: a divide-and-conquer algorithm -- repeatedly split the list in half until each sub-list has one item, then repeatedly merge pairs of sorted sub-lists (comparing their front items, taking the smaller each time) until one sorted list remains. Needs O(n log n) comparisons overall (splitting takes log n levels, merging at each level takes O(n)), so **O(n log n)** time complexity -- far more efficient than bubble sort's O(n²) on large lists, at the cost of needing extra memory to hold the sub-lists during merging.

#### 4.3.6.1 Dijkstra's shortest path algorithm
**Dijkstra's shortest path algorithm** finds the shortest (lowest total weight) path from a start node to every other node in a **weighted graph** with non-negative edge weights. Keep a running shortest-known distance to each node (initially 0 for the start, infinity for all others); repeatedly pick the unvisited node with the smallest known distance, mark it visited, and **relax** its edges (for each neighbour, if going via the current node gives a shorter distance than currently known, update it); stop once every node is visited. *Worked trace* on edges A-B(1), A-C(4), B-C(2), B-D(5), C-D(1): start dist A=0; visit A, relax: B=1, C=4; visit B (smallest, 1), relax: C = min(4, 1+2)=3, D=1+5=6; visit C (smallest unvisited, 3), relax: D = min(6, 3+1)=4; visit D (4) -- shortest distance A to D is 4, via the path A-B-C-D.

## Explicitly not here
This is the last algorithms stage; S12 begins theory of computation.
