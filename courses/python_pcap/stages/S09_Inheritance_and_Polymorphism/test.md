# S09_Inheritance_and_Polymorphism - Test: Inheritance and polymorphism

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
class A:
    def hi(self): return 'A'
class B(A):
    def hi(self): return 'B'
class C(A): pass
for o in (A(), B(), C()):
    print(o.hi(), end=' ')
```
2. What does this print? (If it raises an error, name it.)
```python
class A: pass
class B(A): pass
b = B()
print(isinstance(b, A), isinstance(A(), B), issubclass(B, A), type(b) is A)
```
3. What does this print? (If it raises an error, name it.)
```python
class A:
    def m(self): return 'A'
class B(A):
    def m(self): return 'B'
class C(A):
    def m(self): return 'C'
class D(C, B): pass
print(D().m(), [k.__name__ for k in D.__mro__])
```
4. What does this print? (If it raises an error, name it.)
```python
class Base:
    def __init__(self):
        self.tag = 'base'
class Child(Base):
    def __init__(self):
        super().__init__()
        self.tag += '+child'
print(Child().tag)
```
5. What does this print? (If it raises an error, name it.)
```python
class N:
    def __init__(self, v): self.v = v
    def __str__(self): return 'N(' + str(self.v) + ')'
print([str(N(1))], N(2))
```
6. What does this print? (If it raises an error, name it.)
```python
x = [1, 2]
y = x
z = list(x)
print(x is y, x is z, x == z, x is not z)
```
7. Which are true about Python's handling of a diamond hierarchy? Choose every correct option.
   A. The shared base class is searched only once
   B. The shared base is searched before the second parent
   C. The MRO is visible in __mro__
   D. Multiple inheritance is not allowed
8. Create classes Employee and Manager(Employee) where Manager overrides pay() to add a bonus to the Employee pay via super(), and both have a __str__ used by print.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
A B A 
```
2. Actual result (from running it):
```
True False True False
```
3. Actual result (from running it):
```
C ['D', 'C', 'B', 'A', 'object']
```
4. Actual result (from running it):
```
base+child
```
5. Actual result (from running it):
```
['N(1)'] N(2)
```
6. Actual result (from running it):
```
True False True True
```
7. Correct: A, C (exactly these options, no others)
8. The tutor runs or reads the learner's answer and checks: Correct inheritance, super().pay() used, __str__ returns a string, polymorphic print over a list of both.

## Grading
Apply `rubric.json`'s `stage_rubrics.S09_Inheritance_and_Polymorphism` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S10_Comprehensions_Lambdas_Closures.
