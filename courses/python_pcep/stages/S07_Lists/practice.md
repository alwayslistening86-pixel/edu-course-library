# S07_Lists - Practice: Lists

## Goal
Low-stakes practice: the learner predicts or writes code first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name the exception.)
```python
a = [5, 3, 8, 1]
print(a[1:3], a[-2], a[::-1], sorted(a), a)
```
2. What does this print? (If it raises an error, name the exception.)
```python
a = [1, 2, 3]
b = a
c = a[:]
a.append(4)
print(b, c)
```
3. What does this print? (If it raises an error, name the exception.)
```python
print([x * 2 for x in range(5) if x != 2])
```
4. What does this print? (If it raises an error, name the exception.)
```python
m = [[1, 2], [3, 4], [5, 6]]
print(m[2][0], len(m), [row[1] for row in m])
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Output (from running it):
```
[3, 8] 8 [1, 8, 3, 5] [1, 3, 5, 8] [5, 3, 8, 1]
```
2. Output (from running it):
```
[1, 2, 3, 4] [1, 2, 3]
```
3. Output (from running it):
```
[0, 2, 6, 8]
```
4. Output (from running it):
```
5 3 [2, 4, 6]
```

## How to run it
One item at a time. For output questions the learner writes their prediction before running the code. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
