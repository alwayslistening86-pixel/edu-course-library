# Python: PCAP-31-03 Certified Associate Python Programmer (Python Institute) - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` has a passed test.

## Format
40 items in PCAP's real proportions: 6 from S01-S02, 5 from S03-S04, 8 from S05-S06, 12 from S07-S09 and 9 from S10-S11. Mix single-select, multiple-select, code-output and short code items, in non-sequential order. No running code until everything is answered. Suggested time: 65 minutes (the real exam's timing is set by the exam provider).

## 8 ready-made items (write the rest fresh, never reusing stage-test items)
1. What does this print? (If it raises an error, name it.)
```python
import math
print(math.trunc(-7.8) + math.floor(-7.8), math.hypot(6, 8))
```
2. What does this print? (If it raises an error, name it.)
```python
try:
    raise KeyError('k')
except LookupError as e:
    print('lookup', e.args)
else:
    print('else')
finally:
    print('fin')
```
3. What does this print? (If it raises an error, name it.)
```python
print('Mississippi'.rfind('s'), '-'.join(sorted('cab')), 'AbC'.lower().isalpha())
```
4. What does this print? (If it raises an error, name it.)
```python
class A:
    x = 'A'
    def who(self): return self.x
class B(A):
    x = 'B'
print(A().who(), B().who())
```
5. What does this print? (If it raises an error, name it.)
```python
class P:
    def __init__(self):
        self.__n = 1
        self._m = 2
print(sorted(P().__dict__))
```
6. What does this print? (If it raises an error, name it.)
```python
print(list(map(lambda x, y: x * y, [1, 2, 3], [4, 5, 6])))
```
7. What does this print? (If it raises an error, name it.)
```python
def f(n):
    def g(x):
        return x ** n
    return g
print([f(k)(2) for k in range(4)])
```
8. What does this print? (If it raises an error, name it.)
```python
class E1(Exception): pass
class E2(E1): pass
try:
    raise E2('z')
except E1 as e:
    print(type(e).__name__, isinstance(e, Exception))
```

## Answer key for the ready-made items (tutor only)
1. Actual result (from running it):
```
-15 10.0
```
2. Actual result (from running it):
```
lookup ('k',)
fin
```
3. Actual result (from running it):
```
6 a-b-c True
```
4. Actual result (from running it):
```
A B
```
5. Actual result (from running it):
```
['_P__n', '_m']
```
6. Actual result (from running it):
```
[4, 10, 18]
```
7. Actual result (from running it):
```
[1, 2, 4, 8]
```
8. Actual result (from running it):
```
E2 True
```

## Grading
Apply `rubric.json`'s `exam_rubric` exactly: at least 28 of 40 (70%) for a pass, and report the score per section.

## Outcome
- **Pass:** record `exam_status: "passed"`. The course is complete.
- **Not yet:** leave `exam_status: "available"`, name the weakest section, offer targeted review, and retry with a fresh paper.
