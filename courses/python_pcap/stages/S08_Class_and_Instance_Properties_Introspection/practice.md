# S08_Class_and_Instance_Properties_Introspection - Practice: Class and instance properties, privacy and introspection

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
class K:
    n = 0
    def __init__(self):
        K.n += 1
        self.id = K.n
a, b = K(), K()
print(a.id, b.id, K.n, a.n)
```
2. What does this print? (If it raises an error, name it.)
```python
class S:
    def __init__(self):
        self.__x = 1
print(S().__dict__)
```
3. What does this print? (If it raises an error, name it.)
```python
class Base: pass
class Kid(Base): pass
print(Kid.__bases__[0].__name__, Kid.__name__)
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
1 2 2 2
```
2. Actual result (from running it):
```
{'_S__x': 1}
```
3. Actual result (from running it):
```
Base Kid
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
