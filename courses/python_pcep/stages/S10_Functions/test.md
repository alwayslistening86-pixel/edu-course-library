# S10_Functions - Test: Functions, arguments and scope

## How to run this
A real checkpoint in the style of PCEP items (code-output, multiple-select and short code-writing). Give all the items at once with no hints and no running of code until the learner has submitted every answer. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name the exception.)
```python
def area(w, h=1):
    return w * h
print(area(4), area(4, 2), area(h=3, w=2))
```
2. What does this print? (If it raises an error, name the exception.)
```python
def f(x):
    if x > 0:
        return 'pos'
print(f(1), f(-1))
```
3. What does this print? (If it raises an error, name the exception.)
```python
n = 5
def g():
    global n
    n += 1
g()
g()
print(n)
```
4. What does this print? (If it raises an error, name the exception.)
```python
def add(lst):
    lst.append(len(lst))
items = [7]
add(items)
add(items)
print(items)
```
5. What does this print? (If it raises an error, name the exception.)
```python
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)
print([fib(i) for i in range(7)])
```
6. What does this print? (If it raises an error, name the exception.)
```python
def evens(limit):
    for i in range(0, limit, 2):
        yield i
print(list(evens(7)))
```
7. Given def f(a, b, c=0), which calls are valid? Choose every correct option.
   A. `f(1, 2)`
   B. `f(1, b=2)`
   C. `f(a=1, 2)`
   D. `f(1, 2, 3, 4)`
   E. `f(c=1, b=2, a=3)`
8. Write a function `largest(a, b, c)` that returns the largest of three numbers without using max(), and print largest(3, 9, 5).

## Answer key (for the tutor only)
1. Output (from running it):
```
4 8 6
```
2. Output (from running it):
```
pos None
```
3. Output (from running it):
```
7
```
4. Output (from running it):
```
[7, 1, 2]
```
5. Output (from running it):
```
[0, 1, 1, 2, 3, 5, 8]
```
6. Output (from running it):
```
[0, 2, 4, 6]
```
7. Correct: A, B, E (exactly these options, no others)
8. The tutor runs the learner's code and checks: Correct comparisons including ties; returns rather than prints inside; prints 9.

## Grading
Apply `rubric.json`'s `stage_rubrics.S10_Functions` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions shown by the wrong answers, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S11_Exceptions.
