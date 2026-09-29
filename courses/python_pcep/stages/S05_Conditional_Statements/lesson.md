# S05_Conditional_Statements - Lesson: Making decisions with if, elif and else

## Goal
The learner writes and traces if, elif and else chains, sequences of separate ifs, and nested conditions.

## Syllabus items taught here
- 2.1a - if, if-else, if-elif and if-elif-else
- 2.1b - Several independent conditional statements in sequence
- 2.1c - Nested conditional statements

## How to teach this
Give a mark of 72 and ask the learner to write the grade logic twice: once with elif and once with separate ifs. Then run both and compare. Have the learner predict the output of every example before running it, and run code for real whenever they can.

#### 2.1a if, if-else, if-elif and if-elif-else
`if condition:` runs its block only when the condition is truthy. `else:` catches everything else. `elif` adds further tests, checked **in order**; the first true branch runs and the rest are skipped, so order matters: put the most specific test first. There can be any number of `elif`s and at most one `else`, which must be last.
```python
mark = 72
if mark >= 80:
    grade = "A"
elif mark >= 70:
    grade = "B"
elif mark >= 60:
    grade = "C"
else:
    grade = "U"
print(grade)
```
Output:
```
B
```

#### 2.1b Several independent conditional statements in sequence
**Separate `if` statements** are each tested independently, so several can run. That is different from an elif chain, where at most one branch runs. This is a classic exam trap.
```python
n = 15
if n % 3 == 0:
    print("fizz")
if n % 5 == 0:
    print("buzz")
if n > 100:
    print("big")
```
Output:
```
fizz
buzz
```

#### 2.1c Nested conditional statements
An `if` can sit inside another `if` (or `else`). Indentation shows which `else` belongs to which `if`. Nested conditions can often be flattened with `and`, but the exam expects you to trace either form.
```python
x, y = 5, -2
if x > 0:
    if y > 0:
        print("both positive")
    else:
        print("only x positive")
else:
    print("x not positive")
```
Output:
```
only x positive
```

## Explicitly not here
Loops are S06.
