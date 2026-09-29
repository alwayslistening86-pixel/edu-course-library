# S11_Introduction_to_Machine_Learning_and_AI - Practice: Introduction to machine learning and AI

## Goal
Low-stakes practice: the learner attempts each question, trace or piece of code in full before seeing the solution. Mistakes are expected and corrected here, before any grading.

## Practice items
1. State whether predicting a customer's spending category (low/medium/high) is a classification or a regression problem, and whether predicting their exact spend in pounds is classification or regression. [2 marks]
2. What does this print? (If it raises an error, name it.)
```python
def euclidean(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5
print(round(euclidean((0, 0), (3, 4)), 2))
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. [2] B1 predicting a category (low/medium/high) is classification; B1 predicting an exact numeric amount is regression.
2. Actual result (from running it):
```
5.0
```

## How to run it
One question at a time. Let the learner finish a genuine attempt (including full working for a trace or calculation) before offering a hint; then walk through the model solution/actual output and have them redo any step they missed.

## When to move to test
When the learner gets a new item of each type right without prompting.
