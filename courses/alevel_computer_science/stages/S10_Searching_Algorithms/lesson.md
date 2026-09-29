# S10_Searching_Algorithms - Lesson: Searching: linear search, binary search and binary tree search

## Goal
The learner traces and analyses the time complexity of linear search, binary search and binary tree search.

## Syllabus items taught here
- 4.3.4.1 - Linear search
- 4.3.4.2 - Binary search
- 4.3.4.3 - Binary tree search

## How to teach this
Ask the learner to compare finding a name in an unsorted pile of index cards versus a sorted one, versus one already organised into a binary search tree. AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.3.4.1 Linear search
**Linear search**: check each item in order, from the start, until the target is found or the list is exhausted. Works on any list (sorted or not). Worst case (target absent, or at the end) checks every item: **O(n)** time complexity.

#### 4.3.4.2 Binary search
**Binary search**: requires a **sorted** list. Compare the target with the middle item; if equal, found; if smaller, repeat on the left half; if larger, repeat on the right half; continue until found or nothing remains to search. Each comparison discards half the remaining items, giving **O(log n)** time complexity -- far fewer comparisons than linear search once the list is large. *Worked trace:* searching for 26 in [3, 8, 15, 21, 26, 34, 40, 55] (indices 0-7): middle (0+7)//2=3, list[3]=21 < 26, search right half (4-7); middle (4+7)//2=5, list[5]=34 > 26, search left half (4-4); middle (4+4)//2=4, list[4]=26, found -- 3 comparisons.

#### 4.3.4.3 Binary tree search
**Binary tree search**: applied to a **binary search tree** (a binary tree where every node's left subtree holds only smaller values and its right subtree only larger values). Starting at the root, compare the target with the current node; if equal, found; if smaller, move to the left child; if larger, move to the right child; repeat until found or a missing child is reached (not found). Like binary search, this gives **O(log n)** time complexity on a **balanced** tree (roughly equal-sized left/right subtrees), because each comparison eliminates one whole subtree -- but on a poorly balanced (e.g. list-like, one-sided) tree, it degrades towards **O(n)**, since the tree is effectively no better than a linear chain.

## Explicitly not here
Sorting algorithms (getting data into order in the first place) are S11.
