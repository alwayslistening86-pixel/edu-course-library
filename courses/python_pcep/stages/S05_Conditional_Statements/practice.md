# S05_Conditional_Statements - Practice: Making decisions with if, elif and else

## Goal
Low-stakes practice: the learner predicts or writes code first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What does this print? (If it raises an error, name the exception.)
```python
t = 18
if t > 25:
    print('hot')
elif t > 15:
    print('mild')
elif t > 5:
    print('cool')
else:
    print('cold')
```
2. What does this print? (If it raises an error, name the exception.)
```python
n = 12
if n % 2 == 0:
    print('even')
if n % 3 == 0:
    print('three')
if n % 5 == 0:
    print('five')
```
3. A ticket is free for under 5s, 5 pounds for 5-15, 10 pounds for 16-64 and 7 pounds for 65+. Write the if-elif chain that sets `price` from `age`.

## Answers (for the tutor; reveal only after a genuine attempt)
1. Output (from running it):
```
mild
```
2. Output (from running it):
```
even
three
```
3. The tutor runs the learner's code and checks: Correct boundaries for all four bands, one elif chain, else for the final band; age 5 -> 5, 15 -> 5, 16 -> 10, 65 -> 7, 4 -> 0.

## How to run it
One item at a time. For output questions the learner writes their prediction before running the code. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
