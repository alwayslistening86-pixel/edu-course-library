# S07_Lists - Test: Lists

## How to run this
A real checkpoint in the style of PCEP items (code-output, multiple-select and short code-writing). Give all the items at once with no hints and no running of code until the learner has submitted every answer. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name the exception.)
```python
a = [10, 20, 30, 40]
print(a[-1], a[1:], a[:-2], a[5:])
```
2. What does this print? (If it raises an error, name the exception.)
```python
a = [3, 1, 2]
a.append(0)
a.insert(1, 9)
print(a, a.index(2), len(a))
```
3. What does this print? (If it raises an error, name the exception.)
```python
a = [1, 2, 3, 4, 5]
del a[1:3]
x = a.pop()
print(a, x)
```
4. What does this print? (If it raises an error, name the exception.)
```python
a = [4, 2, 6]
b = sorted(a)
c = a.sort()
print(a, b, c)
```
5. What does this print? (If it raises an error, name the exception.)
```python
x = [1, 2]
y = x
y[0] = 99
z = x.copy()
z[1] = 0
print(x, y, z)
```
6. What does this print? (If it raises an error, name the exception.)
```python
print([c for c in 'banana' if c not in 'ab'], 3 not in [1, 2])
```
7. What does this print? (If it raises an error, name the exception.)
```python
g = [[0] * 2] * 2
g[0][0] = 1
print(g)
```
8. Build a 3x3 matrix `m` whose element m[r][c] is r * 3 + c, using a nested list comprehension, then print the middle element.

## Answer key (for the tutor only)
1. Output (from running it):
```
40 [20, 30, 40] [10, 20] []
```
2. Output (from running it):
```
[3, 9, 1, 2, 0] 3 5
```
3. Output (from running it):
```
[1, 4] 5
```
4. Output (from running it):
```
[2, 4, 6] [2, 4, 6] None
```
5. Output (from running it):
```
[99, 2] [99, 2] [99, 0]
```
6. Output (from running it):
```
['n', 'n'] True
```
7. Output (from running it):
```
[[1, 0], [1, 0]]
```
8. The tutor runs the learner's code and checks: m == [[0,1,2],[3,4,5],[6,7,8]] built by a nested comprehension; prints 4.

## Grading
Apply `rubric.json`'s `stage_rubrics.S07_Lists` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions shown by the wrong answers, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S08_Tuples_and_Dictionaries.
