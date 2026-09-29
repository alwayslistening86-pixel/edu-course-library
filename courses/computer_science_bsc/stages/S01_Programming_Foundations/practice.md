# S01_Programming_Foundations - Practice: Programming foundations

## Goal
Low-stakes practice: the learner attempts each question, trace or piece of code in full before seeing the solution. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
print([x for x in range(10) if x % 3 == 0])
```
2. What does this print? (If it raises an error, name it.)
```python
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)
print(fact(5))
```
3. Write a Python class `Counter` with an `__init__` that sets `count=0`, an `increment()` method that adds 1, and a `__str__` that returns f"Counter({self.count})". Show the output of creating one, calling increment() twice, and printing it. [3 marks]

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
[0, 3, 6, 9]
```
2. Actual result (from running it):
```
120
```
3. [3] M1 correct __init__ and increment; M1 correct __str__; A1 output 'Counter(2)'.

## How to run it
One question at a time. Let the learner finish a genuine attempt (including full working for a trace or calculation) before offering a hint; then walk through the model solution/actual output and have them redo any step they missed.

## When to move to test
When the learner gets a new item of each type right without prompting.
