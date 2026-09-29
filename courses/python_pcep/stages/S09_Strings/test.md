# S09_Strings - Test: Strings

## How to run this
A real checkpoint in the style of PCEP items (code-output, multiple-select and short code-writing). Give all the items at once with no hints and no running of code until the learner has submitted every answer. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name the exception.)
```python
s = 'Hello'
print(s[1:4], s[-1], s[::-1], s * 2)
```
2. Which raise an error for s = 'text'? Choose every correct option.
   A. `s[0] = 'T'`
   B. `s.upper()`
   C. `s[10]`
   D. `s[2:10]`
3. What does this print? (If it raises an error, name the exception.)
```python
print(len('a\nb\\c'))
```
4. What does this print? (If it raises an error, name the exception.)
```python
print('banana'.find('an'), 'banana'.find('x'), 'banana'.count('a'))
```
5. What does this print? (If it raises an error, name the exception.)
```python
print('a,b,,c'.split(','), '+'.join('xyz'))
```
6. What does this print? (If it raises an error, name the exception.)
```python
s = '''one
two'''
print(len(s), s.upper())
```
7. What does this print? (If it raises an error, name the exception.)
```python
print(ord('a'), chr(ord('a') + 2), '5' + str(5), 'abc'.isalpha())
```
8. Write code that counts the vowels in `s = 'Programming in Python'` (either case) and prints the count.

## Answer key (for the tutor only)
1. Output (from running it):
```
ell o olleH HelloHello
```
2. Correct: A, C (exactly these options, no others)
3. Output (from running it):
```
5
```
4. Output (from running it):
```
1 -1 3
```
5. Output (from running it):
```
['a', 'b', '', 'c'] x+y+z
```
6. Output (from running it):
```
7 ONE
TWO
```
7. Output (from running it):
```
97 c 55 True
```
8. The tutor runs the learner's code and checks: Handles case with lower() or both cases; prints 5.

## Grading
Apply `rubric.json`'s `stage_rubrics.S09_Strings` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions shown by the wrong answers, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S10_Functions.
