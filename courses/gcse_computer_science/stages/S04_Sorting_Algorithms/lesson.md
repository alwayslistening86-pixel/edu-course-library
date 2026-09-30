# S04_Sorting_Algorithms - Lesson: Sorting algorithms: bubble sort and merge sort

## Goal
The learner explains how bubble sort and merge sort work, traces both by hand, and compares and contrasts them.

## Syllabus items taught here
- 3.1.4 - Sorting algorithms: bubble sort and merge sort

## How to teach this
Ask the learner to sort five playing cards into order by repeatedly swapping neighbours, then again by splitting the pile in half, sorting each half, and merging. Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.1.4 Sorting algorithms: bubble sort and merge sort
**Bubble sort**: repeatedly step through the list, comparing each pair of neighbouring items; if they are in the wrong order, swap them; after one full pass the largest unsorted item has 'bubbled' to its correct position at the end, so each pass can be one item shorter; repeat until a full pass makes no swaps (the list is sorted). *Worked trace* on [5, 2, 4, 1]: pass 1: compare 5,2 -> swap -> [2,5,4,1]; compare 5,4 -> swap -> [2,4,5,1]; compare 5,1 -> swap -> [2,4,1,5]; pass 2: compare 2,4 -> no swap; compare 4,1 -> swap -> [2,1,4,5]; compare 4,5 -> no swap; pass 3: compare 2,1 -> swap -> [1,2,4,5]; compare 2,4 -> no swap; pass 4: no swaps needed, sorted: [1,2,4,5]. Bubble sort is simple but inefficient on large lists (worst case compares/swaps roughly n^2 times). **Merge sort**: a divide-and-conquer algorithm -- repeatedly split the list in half until each sub-list has one item (a list of one item is already sorted), then repeatedly **merge** pairs of sorted sub-lists back together by comparing their front items and taking the smaller each time, until one fully sorted list remains. *Worked trace* on [5, 2, 4, 1]: split into [5,2] and [4,1]; split again into [5],[2] and [4],[1] (each a single item, sorted); merge [5],[2] -> compare 5,2, take 2 first -> [2,5]; merge [4],[1] -> compare 4,1, take 1 first -> [1,4]; merge [2,5] and [1,4] -> compare 2,1 take 1; compare 2,4 take 2; compare 5,4 take 4; take remaining 5 -> [1,2,4,5]. Merge sort is more efficient than bubble sort on large lists (it needs far fewer comparisons as the list grows), but needs extra memory to hold the sub-lists during merging.

## Explicitly not here
This is the last algorithms stage; S05 begins programming.

## Further resources (optional)

These are optional, hand-picked, externally hosted resources -- not part of the syllabus content above, not graded, and not embedded in this file. Nothing here is required to pass the stage.
- **AQA GCSE (8525) SLR7 - 3.1 Bubble sort (Craig'n'Dave)** (https://www.youtube.com/watch?v=vy_domkFPxw) -- Board-matched to this course's AQA 8525 specification. Traces bubble sort through a worked array step by step, mirroring how it should be traced on paper for the exam.
