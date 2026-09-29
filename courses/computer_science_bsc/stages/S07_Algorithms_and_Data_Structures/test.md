# S07_Algorithms_and_Data_Structures - Test: Algorithms and data structures

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems, code-trace/code-output items, multiple-select conceptual items and, where the topic is genuinely discursive (professional/ethical/HCI content), extended-response items marked on levels. Give the whole test at once, with no hints; the learner shows full working/code. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
def f(n):
    total = 0
    for i in range(n):
        for j in range(i, n):
            total += 1
    return total
print(f(4))
```
2. State the Big-O time complexity of the function `f(n)` shown, which has a nested loop where the inner loop runs from i to n-1 for each i from 0 to n-1. Justify your answer. [3 marks]
3. Trace insertion sort on the list [5, 2, 4, 1] step by step, showing the list's state after each element is inserted into its correct position. [5 marks]
4. A hash table of size 5 stores keys using h(k) = k mod 5 with chaining. Keys 12, 7, 22 are inserted. State which keys collide (share a chain) and why, using the hash function. [3 marks]
5. Explain why inserting the already-sorted sequence 1,2,3,4,5,6,7 one at a time into a plain (non-self-balancing) binary search tree produces worst-case O(n) search performance, and state how a self-balancing tree avoids this. [4 marks]
6. Which statements about merge sort and quicksort are correct? Choose every correct option.
   A. Merge sort's worst-case time complexity is O(n log n)
   B. Quicksort's worst-case time complexity is O(n^2)
   C. Quicksort's worst case typically arises from a consistently poor pivot choice, e.g. on already-sorted data with a naive first-element pivot
   D. Merge sort requires no additional (auxiliary) memory beyond the input array

## Answer key (for the tutor only)
1. Actual result (from running it):
```
10
```
2. [3] B1 O(n^2); B1 the total number of inner-loop iterations is n + (n-1) + ... + 1 = n(n+1)/2, a quadratic expression in n; B1 Big-O drops the constant factor and lower-order term, leaving O(n^2), the same growth class as a full nested loop even though this one does slightly fewer iterations.
3. [5] M1 start with [5] as the sorted prefix; M1 insert 2: shifts 5 right, gives [2, 5, 4, 1]; M1 insert 4: shifts 5 right (2<4), gives [2, 4, 5, 1]; M1 insert 1: shifts 5,4,2 right, gives [1, 2, 4, 5]; A1 final sorted list [1, 2, 4, 5] correctly reached with all intermediate states shown.
4. [3] M1 h(12)=2, h(7)=2, h(22)=2 (all give remainder 2 when divided by 5); A1 all three keys collide, sharing the same chain at index 2; A1 because h(k)=k mod 5 maps every key of the form 5m+2 to index 2, so 12, 7 and 22 (12=5x2+2, 7=5x1+2, 22=5x4+2) all land there.
5. [4] B1 each new value is larger than every value already inserted, so each goes to the right child of the previous node, producing a degenerate tree that is really just a linked list (a single rightward chain); B1 searching this degenerate tree therefore takes O(n) time in the worst case, not the O(log n) a balanced BST would give; B1 a self-balancing tree (e.g. AVL) detects when an insertion makes the tree too unbalanced and performs rotations to restore balance; B1 this guarantees the tree's height stays O(log n), so search/insert/delete stay O(log n) even for adversarial insertion orders.
6. Correct: A, B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S07_Algorithms_and_Data_Structures` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 17 marks in all; a pass needs at least 11 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S08_Computability_and_Complexity_Theory.
