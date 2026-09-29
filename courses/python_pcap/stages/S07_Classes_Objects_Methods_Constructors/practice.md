# S07_Classes_Objects_Methods_Constructors - Practice: Classes, objects, methods and constructors

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
class Box:
    def __init__(self, size):
        self.size = size
    def double(self):
        self.size *= 2
b = Box(3)
b.double()
print(b.size)
```
2. In `class Car:` with `wheels = 4` in its body and `self.colour = c` in __init__, which are true? Choose every correct option.
   A. wheels is a class variable
   B. colour is an instance variable
   C. __init__ is the constructor
   D. self must be passed explicitly in car.drive()

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
6
```
2. Correct: A, B, C (exactly these options, no others)

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
