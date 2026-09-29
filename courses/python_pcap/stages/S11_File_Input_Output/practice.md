# S11_File_Input_Output - Practice: Files and input/output

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name it.)
```python
with open('p.txt', 'w') as f:
    f.write('a\nb\n')
with open('p.txt') as f:
    print(f.readlines())
```
2. Which modes create the file if it does not exist? Choose every correct option.
   A. `r`
   B. `w`
   C. `a`
   D. `x`
3. What does this print? (If it raises an error, name it.)
```python
import errno
try:
    open('nope.txt', 'r')
except OSError as e:
    print(e.errno == errno.ENOENT, type(e).__name__)
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
['a\n', 'b\n']
```
2. Correct: B, C, D (exactly these options, no others)
3. Actual result (from running it):
```
True FileNotFoundError
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
