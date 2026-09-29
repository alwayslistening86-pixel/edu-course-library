# S01_How_Python_Runs_Code - Practice: How Python runs code: interpreters, keywords, indentation, comments

## Goal
Low-stakes practice: the learner predicts or writes code first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. Which of these are Python keywords? Choose every correct option.
   A. `print`
   B. `while`
   C. `True`
   D. `input`
   E. `pass`
2. What does this print? (If it raises an error, name the exception.)
```python
print("start")
# print("hidden")
print("end")  # trailing comment
```
3. This file has one syntax error and one semantic error. Find both, say which is which, and fix them:
```
length = 4
width = 3
area = length + width
if area > 10
    print("big")
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Correct: B, C, E (exactly these options, no others)
2. Output (from running it):
```
start
end
```
3. The tutor runs the learner's code and checks: Syntax: missing colon after `if area > 10`. Semantic: area should be length * width. Fixed code prints big (12 > 10).

## How to run it
One item at a time. For output questions the learner writes their prediction before running the code. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
