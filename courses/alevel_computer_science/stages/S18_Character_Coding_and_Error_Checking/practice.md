# S18_Character_Coding_and_Error_Checking - Practice: Character encoding and error checking/correction

## Goal
Low-stakes practice: the learner predicts or attempts each item first, then checks it (by running code, or against the model answer). Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
print(ord('a'))
print(chr(97))
```
2. Using even parity, state the parity bit that should be added to the 7-bit data 1011001. [2 marks]

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
97
a
```
2. [2] B1 count the 1-bits: 1,0,1,1,0,0,1 has four 1-bits (already even); B1 parity bit = 0 (to keep the total even).

## How to run it
One item at a time. For code-output/trace items the learner commits to a prediction before running or checking anything. Offer a worked explanation only after a genuine attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
