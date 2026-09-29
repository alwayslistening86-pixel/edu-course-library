# S06_Loops - Test: Loops: while, for, range, break, continue and else

## How to run this
A real checkpoint in the style of PCEP items (code-output, multiple-select and short code-writing). Give all the items at once with no hints and no running of code until the learner has submitted every answer. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name the exception.)
```python
print(list(range(3, 12, 4)), list(range(5, 5)))
```
2. What does this print? (If it raises an error, name the exception.)
```python
i = 0
while i < 10:
    i += 3
print(i)
```
3. What does this print? (If it raises an error, name the exception.)
```python
for n in range(6):
    if n % 2:
        continue
    print(n, end=' ')
```
4. What does this print? (If it raises an error, name the exception.)
```python
for n in [1, 3, 4, 5]:
    if n % 2 == 0:
        print('even', n)
        break
else:
    print('none')
```
5. What does this print? (If it raises an error, name the exception.)
```python
count = 0
for a in range(3):
    for b in range(4):
        count += 1
print(count)
```
6. What does this print? (If it raises an error, name the exception.)
```python
for ch in 'loop':
    pass
print(ch)
```
7. When does a loop's else block run? Choose every correct option.
   A. `Always`
   B. Only if the loop ended without break
   C. Only if the loop body never ran
   D. Only after a break
8. Using a while loop and break, print the first power of 2 that is greater than 1000.

## Answer key (for the tutor only)
1. Output (from running it):
```
[3, 7, 11] []
```
2. Output (from running it):
```
12
```
3. Output (from running it):
```
0 2 4 
```
4. Output (from running it):
```
even 4
```
5. Output (from running it):
```
12
```
6. Output (from running it):
```
p
```
7. Correct: B (exactly these options, no others)
8. The tutor runs the learner's code and checks: Prints 1024, uses while and break correctly, no infinite loop.

## Grading
Apply `rubric.json`'s `stage_rubrics.S06_Loops` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions shown by the wrong answers, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S07_Lists.
