# S08_Tuples_and_Dictionaries - Practice: Tuples and dictionaries

## Goal
Low-stakes practice: the learner predicts or writes code first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name the exception.)
```python
t = (1, 2, 3)
print(t[1:], len(t), (7,) * 2, type((7)))
```
2. What does this print? (If it raises an error, name the exception.)
```python
d = {'a': 1, 'b': 2}
d['c'] = 3
d['a'] = 10
print(d, 'b' in d, 2 in d)
```
3. What does this print? (If it raises an error, name the exception.)
```python
d = {'x': 5, 'y': 6}
for k, v in d.items():
    print(k, v * 2)
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Output (from running it):
```
(2, 3) 3 (7, 7) <class 'int'>
```
2. Output (from running it):
```
{'a': 10, 'b': 2, 'c': 3} True False
```
3. Output (from running it):
```
x 10
y 12
```

## How to run it
One item at a time. For output questions the learner writes their prediction before running the code. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
