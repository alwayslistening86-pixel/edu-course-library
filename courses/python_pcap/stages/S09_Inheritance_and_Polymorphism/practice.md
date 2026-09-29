# S09_Inheritance_and_Polymorphism - Practice: Inheritance and polymorphism

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
class A:
    def f(self): return 'A'
class B(A): pass
class C(B):
    def f(self): return 'C' + super().f()
print(C().f(), B().f())
```
2. What does this print? (If it raises an error, name it.)
```python
class L:
    def who(self): return 'L'
class R:
    def who(self): return 'R'
class M(R, L): pass
print(M().who())
```
3. What does this print? (If it raises an error, name it.)
```python
class Pet:
    def __str__(self): return 'Pet ' + self.name
    def __init__(self, n): self.name = n
print(Pet('Rex'), str(Pet('Bo')))
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
CA A
```
2. Actual result (from running it):
```
R
```
3. Actual result (from running it):
```
Pet Rex Pet Bo
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
