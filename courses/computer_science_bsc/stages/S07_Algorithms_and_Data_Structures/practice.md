# S07_Algorithms_and_Data_Structures - Practice: Algorithms and data structures

## Goal
Low-stakes practice: the learner attempts each question, trace or piece of code in full before seeing the solution. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
def linear_search(xs, target):
    for i, x in enumerate(xs):
        if x == target:
            return i
    return -1
print(linear_search([5, 3, 9, 1], 9))
```
2. State the Big-O time complexity of accessing an element by index in an array, and of accessing an element by position (the k-th node) in a singly linked list. Explain the difference. [3 marks]

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
2
```
2. [3] B1 array by index: O(1); B1 linked list k-th node: O(n); B1 an array supports direct address calculation from the index, while a linked list must follow next-references one node at a time from the head, so the time grows with the position accessed.

## How to run it
One question at a time. Let the learner finish a genuine attempt (including full working for a trace or calculation) before offering a hint; then walk through the model solution/actual output and have them redo any step they missed.

## When to move to test
When the learner gets a new item of each type right without prompting.
