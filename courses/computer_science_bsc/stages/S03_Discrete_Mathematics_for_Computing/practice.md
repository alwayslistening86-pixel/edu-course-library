# S03_Discrete_Mathematics_for_Computing - Practice: Discrete mathematics for computing

## Goal
Low-stakes practice: the learner attempts each question, trace or piece of code in full before seeing the solution. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A & B, A | B, A - B)
```
2. Use a truth table to determine whether P OR (NOT P AND Q) is logically equivalent to P OR Q. [4 marks]

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
{3, 4} {1, 2, 3, 4, 5, 6} {1, 2}
```
2. [4] M1 constructs the truth table for both expressions over all 4 combinations of P, Q; A2 both expressions evaluate to the same truth value in every row (T,T,T,F for P=T,Q=T / P=T,Q=F / P=F,Q=T / P=F,Q=F, or equivalent correct values); A1 conclusion: yes, they are logically equivalent.

## How to run it
One question at a time. Let the learner finish a genuine attempt (including full working for a trace or calculation) before offering a hint; then walk through the model solution/actual output and have them redo any step they missed.

## When to move to test
When the learner gets a new item of each type right without prompting.
