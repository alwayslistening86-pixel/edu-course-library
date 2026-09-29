# S08_Tuples_and_Dictionaries - Test: Tuples and dictionaries

## How to run this
A real checkpoint in the style of PCEP items (code-output, multiple-select and short code-writing). Give all the items at once with no hints and no running of code until the learner has submitted every answer. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name the exception.)
```python
t = (4, 5, 6)
print(t[-1], t[:2], t.index(5), t + (7,))
```
2. Which lines raise an error for t = (1, [2, 3])? Choose every correct option.
   A. `t[0] = 9`
   B. `t[1].append(4)`
   C. `t[1][0] = 9`
   D. `t.append(5)`
3. What does this print? (If it raises an error, name the exception.)
```python
stock = {'pens': 3, 'pads': 0}
stock['ink'] = 7
del stock['pads']
print(stock, len(stock))
```
4. What does this print? (If it raises an error, name the exception.)
```python
d = {'a': 1}
print(d.get('b'), d.get('b', 0), 'a' in d, 1 in d)
```
5. What does this print? (If it raises an error, name the exception.)
```python
d = {'k1': 'v1', 'k2': 'v2'}
print(list(d.keys()), list(d.values()))
```
6. What does this print? (If it raises an error, name the exception.)
```python
ages = {'Ann': 30, 'Bo': 20}
total = 0
for name in ages:
    total += ages[name]
print(total)
```
7. Given `words = ['to', 'be', 'or', 'not', 'to', 'be']`, build a dictionary counting each word, then print it.

## Answer key (for the tutor only)
1. Output (from running it):
```
6 (4, 5) 1 (4, 5, 6, 7)
```
2. Correct: A, D (exactly these options, no others)
3. Output (from running it):
```
{'pens': 3, 'ink': 7} 2
```
4. Output (from running it):
```
None 0 True False
```
5. Output (from running it):
```
['k1', 'k2'] ['v1', 'v2']
```
6. Output (from running it):
```
50
```
7. The tutor runs the learner's code and checks: Uses a loop with an `in` check or get(); prints {'to': 2, 'be': 2, 'or': 1, 'not': 1}.

## Grading
Apply `rubric.json`'s `stage_rubrics.S08_Tuples_and_Dictionaries` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions shown by the wrong answers, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S09_Strings.
