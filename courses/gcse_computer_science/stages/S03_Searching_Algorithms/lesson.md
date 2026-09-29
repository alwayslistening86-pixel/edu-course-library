# S03_Searching_Algorithms - Lesson: Searching algorithms: linear and binary search

## Goal
The learner explains how linear search and binary search work, traces both by hand, and compares and contrasts them.

## Syllabus items taught here
- 3.1.3 - Searching algorithms: linear search and binary search

## How to teach this
Ask the learner to find the number 47 in the sorted list [3, 8, 15, 23, 31, 42, 47, 56, 61, 70] two ways: reading left to right, and by repeatedly checking the middle of what's left. Have the learner predict the output of every Python example before running it, and run code for real whenever they can. AQA's own exams are set in AQA's pseudo-code, not any specific language; Python (AQA's widely-used reference teaching language) is used here so examples can be run for real and their output verified, but the learner should also be shown the equivalent pseudo-code form for exam-style tracing questions, since Paper 1 code-reading/writing questions are set in pseudo-code with only the constructs taught in 3.2. Binary/hex conversions, storage and sound/image size calculations, Huffman/RLE compression and logic-gate truth tables were computed/verified when this course was built.

#### 3.1.3 Searching algorithms: linear search and binary search
**Linear search**: start at the first item and check each item in turn until the target is found or the list is exhausted; it works on any list, sorted or not, and is O(n) -- worst case it checks every item. Pseudo-code:
```
FOR i = 0 TO length(list) - 1
    IF list[i] = target THEN
        RETURN i
    ENDIF
ENDFOR
RETURN -1  // not found
```
**Binary search**: the list must already be **sorted**. Compare the target with the middle item; if equal, found; if the target is smaller, repeat the search on the left half; if larger, repeat on the right half; keep halving the remaining section until the target is found or nothing is left to search. It is far more efficient on large sorted lists: each comparison roughly halves the amount left to search, so it needs far fewer comparisons than linear search once the list is large; *worked trace*: searching for 47 in [3, 8, 15, 23, 31, 42, 47, 56, 61, 70] (10 items, indices 0-9): middle index (0+9)//2 = 4, list[4] = 31 < 47, so search the right half (indices 5-9); new middle (5+9)//2 = 7, list[7] = 56 > 47, so search the left half (indices 5-6); new middle (5+6)//2 = 5, list[5] = 42 < 47, so search the right half (index 6 only); list[6] = 47, found in 4 comparisons (linear search would also have taken 7 comparisons here, but on a much larger list the gap grows dramatically).

## Explicitly not here
Sorting algorithms (getting a list into order in the first place) are S04.
