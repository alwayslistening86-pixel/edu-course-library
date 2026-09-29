# S05_Programming_and_Software_Engineering - Practice: Programming and software engineering

## Goal
Low-stakes practice: the learner attempts each question, trace or piece of code in full before seeing the solution. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
class Logger:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

a = Logger()
b = Logger()
print(a is b)
```
2. Name the SOLID principle violated by a `ReportGenerator` class that both computes report data and formats it as HTML, and explain why. [2 marks]

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
True
```
2. [2] B1 Single Responsibility Principle; B1 the class has two reasons to change (a change to the computation logic and a change to the HTML formatting/presentation), so it has more than one responsibility.

## How to run it
One question at a time. Let the learner finish a genuine attempt (including full working for a trace or calculation) before offering a hint; then walk through the model solution/actual output and have them redo any step they missed.

## When to move to test
When the learner gets a new item of each type right without prompting.
