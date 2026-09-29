# S01_Programming_Foundations - Test: Programming foundations

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems, code-trace/code-output items, multiple-select conceptual items and, where the topic is genuinely discursive (professional/ethical/HCI content), extended-response items marked on levels. Give the whole test at once, with no hints; the learner shows full working/code. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
def flatten_once(xs):
    result = []
    for x in xs:
        if isinstance(x, list):
            result.extend(x)
        else:
            result.append(x)
    return result
print(flatten_once([1, [2, 3], 4, [5, [6]]]))
```
2. What does this print? (If it raises an error, name it.)
```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

print(Vector(1, 2) + Vector(3, 4))
```
3. What does this print? (If it raises an error, name it.)
```python
def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

g = fib_gen()
print([next(g) for _ in range(8)])
```
4. Trace the call stack for `fact(4)` where `fact(n)` returns 1 if n<=1 else n*fact(n-1). Give the sequence of calls made and the sequence of return values, in order. [4 marks]
5. Write a custom exception class `NegativeAgeError` and a function `set_age(age)` that raises it (with a message including the invalid value) if age < 0, otherwise returns age. Show the output of calling set_age(-5) inside a try/except that prints the caught message. [4 marks]
6. Which statements about Python generators are correct? Choose every correct option.
   A. A generator function contains at least one `yield` statement
   B. Calling a generator function immediately runs its whole body
   C. A generator produces its values lazily, one at a time, via `next()`
   D. A generator can be iterated only once (once exhausted, it cannot restart without creating a new one)

## Answer key (for the tutor only)
1. Actual result (from running it):
```
[1, 2, 3, 4, 5, [6]]
```
2. Actual result (from running it):
```
Vector(4, 6)
```
3. Actual result (from running it):
```
[0, 1, 1, 2, 3, 5, 8, 13]
```
4. [4] M1 calls: fact(4) calls fact(3) calls fact(2) calls fact(1); A1 fact(1) returns 1 (base case); M1 unwinding: fact(2) returns 2*1=2, fact(3) returns 3*2=6; A1 fact(4) returns 4*6=24.
5. [4] M1 class NegativeAgeError(Exception) defined; M1 set_age raises NegativeAgeError with a message including -5 when age<0; A1 try/except catches it and prints a message containing '-5'; A1 the exception is a subclass of Exception, not a bare raise of a string.
6. Correct: A, C, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S01_Programming_Foundations` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S02_Systems_Networks_and_Cybersecurity_Foundations.
