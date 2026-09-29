# S10_Comprehensions_Lambdas_Closures - Test: Comprehensions, lambdas, map/filter and closures

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
print([n if n % 3 else 'x' for n in range(1, 7)])
```
2. What does this print? (If it raises an error, name it.)
```python
m = [[1, 2], [3, 4]]
print([[r[i] for r in m] for i in range(2)])
```
3. What does this print? (If it raises an error, name it.)
```python
f = lambda a, b=2: a ** b
print(f(3), f(2, 3), (lambda *xs: sum(xs))(1, 2, 3))
```
4. What does this print? (If it raises an error, name it.)
```python
nums = [5, 2, 8]
print(list(map(lambda x: x % 3, nums)), list(filter(lambda x: x > 4, nums)))
```
5. What does this print? (If it raises an error, name it.)
```python
it = filter(lambda x: x, [0, 3, 0, 4])
print(next(it), list(it), list(it))
```
6. What does this print? (If it raises an error, name it.)
```python
def adder(n):
    return lambda x: x + n
add5 = adder(5)
print(add5(1), adder(-1)(1))
```
7. What does this print? (If it raises an error, name it.)
```python
fs = [lambda: i for i in range(3)]
print([f() for f in fs])
```
8. Write a function make_counter(start) that returns a closure; each call to the closure returns the next number, starting from start.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
[1, 2, 'x', 4, 5, 'x']
```
2. Actual result (from running it):
```
[[1, 3], [2, 4]]
```
3. Actual result (from running it):
```
9 8 6
```
4. Actual result (from running it):
```
[2, 2, 2] [5, 8]
```
5. Actual result (from running it):
```
3 [4] []
```
6. Actual result (from running it):
```
6 0
```
7. Actual result (from running it):
```
[2, 2, 2]
```
8. The tutor runs or reads the learner's answer and checks: Uses a nested function with nonlocal; make_counter(10) gives 10, 11, 12 on successive calls.

## Grading
Apply `rubric.json`'s `stage_rubrics.S10_Comprehensions_Lambdas_Closures` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S11_File_Input_Output.
