# S04_Console_Input_and_Output - Practice: Console input and output

## Goal
Low-stakes practice: the learner predicts or writes code first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name the exception.)
```python
print("a", "b", "c", sep="")
print("x", end="-")
print("y")
```
2. What does this print? (If it raises an error, name the exception.)
```python
n = "4"
print(n * 2, int(n) * 2, float(n) / 2)
```
3. Write a program that asks for two whole numbers and prints their sum, on one line, as: `3 + 4 = 7`.

## Answers (for the tutor; reveal only after a genuine attempt)
1. Output (from running it):
```
abc
x-y
```
2. Output (from running it):
```
44 8 2.0
```
3. The tutor runs the learner's code and checks: Converts both inputs with int(); uses sep or concatenation to produce exactly `a + b = total`.

## How to run it
One item at a time. For output questions the learner writes their prediction before running the code. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
