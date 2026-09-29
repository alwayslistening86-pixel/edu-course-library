# S06_Loops - Practice: Loops: while, for, range, break, continue and else

## Goal
Low-stakes practice: the learner predicts or writes code first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name the exception.)
```python
for i in range(10, 0, -3):
    print(i, end=' ')
```
2. What does this print? (If it raises an error, name the exception.)
```python
total = 0
n = 1
while n <= 5:
    total += n
    n += 1
print(total, n)
```
3. What does this print? (If it raises an error, name the exception.)
```python
for i in range(3):
    if i == 5:
        break
else:
    print('no break, i =', i)
```
4. What does this print? (If it raises an error, name the exception.)
```python
for i in range(1, 4):
    for j in range(i):
        print('*', end='')
    print()
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Output (from running it):
```
10 7 4 1 
```
2. Output (from running it):
```
15 6
```
3. Output (from running it):
```
no break, i = 2
```
4. Output (from running it):
```
*
**
***
```

## How to run it
One item at a time. For output questions the learner writes their prediction before running the code. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
