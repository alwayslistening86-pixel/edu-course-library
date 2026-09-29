# Python: PCEP-30-02 - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` has a passed test.

## Format
30 items in PCEP's real proportions: 7 from Block 1 (S01-S04), 8 from Block 2 (S05-S06), 7 from Block 3 (S07-S09) and 8 from Block 4 (S10-S11). Mix single-select, multiple-select, code-output and short code items, in non-sequential order. No running code until the learner has answered everything. Suggested time: 45 minutes (the real exam's timing is set by the exam provider).

## Ten ready-made items (write the other 20 fresh, never reusing stage-test items)
1. What does this print? (If it raises an error, name the exception.)
```python
print(0x10 + 0b10, 7 // 2 * 2 + 7 % 2)
```
2. What does this print? (If it raises an error, name the exception.)
```python
x = 3
x **= 2
print(x, x / 3)
```
3. What does this print? (If it raises an error, name the exception.)
```python
print(1, 2, sep='/', end='!\n')
```
4. What does this print? (If it raises an error, name the exception.)
```python
n = 0
for i in range(1, 10, 2):
    if i > 6:
        break
    n += i
else:
    n = -1
print(n)
```
5. What does this print? (If it raises an error, name the exception.)
```python
a = [1, 2, 3]
b = a
b += [4]
print(a, len(b))
```
6. What does this print? (If it raises an error, name the exception.)
```python
d = {'a': [1]}
d['a'].append(2)
d['b'] = d.get('b', 0) + 1
print(d)
```
7. What does this print? (If it raises an error, name the exception.)
```python
s = 'Exam'
print(s[::-1].lower(), s.find('a'))
```
8. What does this print? (If it raises an error, name the exception.)
```python
def f(x, y=[]):
    y.append(x)
    return y
f(1)
print(f(2))
```
9. What does this print? (If it raises an error, name the exception.)
```python
try:
    print({'k': 1}['K'])
except LookupError:
    print('missing')
```
10. What does this print? (If it raises an error, name the exception.)
```python
print(bool('0'), bool(0), not None, [] or 'e')
```

## Answer key for the ready-made items (tutor only)
1. Output (from running it):
```
18 7
```
2. Output (from running it):
```
9 3.0
```
3. Output (from running it):
```
1/2!
```
4. Output (from running it):
```
9
```
5. Output (from running it):
```
[1, 2, 3, 4] 4
```
6. Output (from running it):
```
{'a': [1, 2], 'b': 1}
```
7. Output (from running it):
```
maxe 2
```
8. Output (from running it):
```
[1, 2]
```
9. Output (from running it):
```
missing
```
10. Output (from running it):
```
True False True e
```

## Grading
Apply `rubric.json`'s `exam_rubric` exactly: at least 21 of 30 (70%) for a pass, and report the score per block.

## Outcome
- **Pass:** record `exam_status: "passed"`. The course is complete, and it now satisfies the prerequisite for the PCAP course.
- **Not yet:** leave `exam_status: "available"`, name the weakest block, offer targeted review, and retry with a fresh paper.
