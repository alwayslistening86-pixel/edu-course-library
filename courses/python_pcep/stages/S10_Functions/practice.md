# S10_Functions - Practice: Functions, arguments and scope

## Goal
Low-stakes practice: the learner predicts or writes code first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name the exception.)
```python
def f(a, b=2):
    return a * b
print(f(3), f(3, 3), f(b=1, a=4))
```
2. What does this print? (If it raises an error, name the exception.)
```python
def g():
    print('in g')
r = g()
print(r)
```
3. What does this print? (If it raises an error, name the exception.)
```python
x = 1
def h():
    x = 2
    return x
print(h(), x)
```
4. What does this print? (If it raises an error, name the exception.)
```python
def s(n):
    if n == 0:
        return 0
    return n + s(n - 1)
print(s(4))
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Output (from running it):
```
6 9 4
```
2. Output (from running it):
```
in g
None
```
3. Output (from running it):
```
2 1
```
4. Output (from running it):
```
10
```

## How to run it
One item at a time. For output questions the learner writes their prediction before running the code. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
