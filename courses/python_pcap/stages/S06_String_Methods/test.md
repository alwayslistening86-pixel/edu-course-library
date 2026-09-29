# S06_String_Methods - Test: String methods and sorting strings

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
print('ABC'.isupper(), 'aBc'.islower(), ' \t'.isspace(), '12'.isdigit())
```
2. What does this print? (If it raises an error, name it.)
```python
print(', '.join(['x', 'y']), '|'.join('ab'), 'k=v'.split('='))
```
3. What does this print? (If it raises an error, name it.)
```python
s = '--data--'
print(s.strip('-'), s.lstrip('-'), s.rstrip('-'))
```
4. What does this print? (If it raises an error, name it.)
```python
s = 'repeat repeat'
print(s.find('peat'), s.rfind('peat'), s.find('peat', 5))
```
5. What does this print? (If it raises an error, name it.)
```python
try:
    'abc'.index('d')
except ValueError:
    print('ValueError')
print('abc'.find('d'))
```
6. What does this print? (If it raises an error, name it.)
```python
print(sorted('hello'), ''.join(sorted('hello', reverse=True)))
```
7. What does this print? (If it raises an error, name it.)
```python
print(sorted(['beta', 'Alpha', 'gamma'], key=str.lower))
```
8. Given a line 'Ann, 31 ,London', produce the list ['Ann', '31', 'London'] with no stray spaces, in one expression.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
True False True True
```
2. Actual result (from running it):
```
x, y a|b ['k', 'v']
```
3. Actual result (from running it):
```
data data-- --data
```
4. Actual result (from running it):
```
2 9 9
```
5. Actual result (from running it):
```
ValueError
-1
```
6. Actual result (from running it):
```
['e', 'h', 'l', 'l', 'o'] ollhe
```
7. Actual result (from running it):
```
['Alpha', 'beta', 'gamma']
```
8. The tutor runs or reads the learner's answer and checks: Uses split(',') plus strip() on each part (e.g. a comprehension).

## Grading
Apply `rubric.json`'s `stage_rubrics.S06_String_Methods` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S07_Classes_Objects_Methods_Constructors.
