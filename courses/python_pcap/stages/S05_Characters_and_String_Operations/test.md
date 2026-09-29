# S05_Characters_and_String_Operations - Test: Characters, encodings and string operations

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
print(chr(65) + chr(97), ord('a') - ord('A'))
```
2. What does this print? (If it raises an error, name it.)
```python
s = 'Unicode'
print(s[-4:], s[::3], len(s * 2))
```
3. What does this print? (If it raises an error, name it.)
```python
print(len('a\tb\\c'), len('\x41\u0042'))
```
4. What does this print? (If it raises an error, name it.)
```python
print(sorted(['b', 'B', 'a', 'A']), 'Z' > 'a', '2' > '10')
```
5. What does this print? (If it raises an error, name it.)
```python
print('' in 'abc', 'ca' in 'abc', 'bc' not in 'abc')
```
6. Which raise an error? Choose every correct option.
   A. `'abc'[1] = 'x'`
   B. `ord('ab')`
   C. `chr(9731)`
   D. `'abc'[5:9]`
7. What does this print? (If it raises an error, name it.)
```python
total = 0
for ch in 'a1b2c3':
    if '0' <= ch <= '9':
        total += int(ch)
print(total)
```
8. Write code that shifts every lowercase letter in 'hello' three places along the alphabet, wrapping z to c, using ord and chr.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
Aa 32
```
2. Actual result (from running it):
```
code Uce 14
```
3. Actual result (from running it):
```
5 2
```
4. Actual result (from running it):
```
['A', 'B', 'a', 'b'] False True
```
5. Actual result (from running it):
```
True False False
```
6. Correct: A, B (exactly these options, no others)
7. Actual result (from running it):
```
6
```
8. The tutor runs or reads the learner's answer and checks: Correct arithmetic with modulo 26; produces 'khoor'.

## Grading
Apply `rubric.json`'s `stage_rubrics.S05_Characters_and_String_Operations` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S06_String_Methods.
