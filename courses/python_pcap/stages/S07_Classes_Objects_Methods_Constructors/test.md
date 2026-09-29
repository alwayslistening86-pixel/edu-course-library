# S07_Classes_Objects_Methods_Constructors - Test: Classes, objects, methods and constructors

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
class P:
    def __init__(self, name):
        self.name = name
    def greet(self, other):
        return self.name + ' greets ' + other.name
a, b = P('A'), P('B')
print(a.greet(b), P.greet(b, a))
```
2. What does this print? (If it raises an error, name it.)
```python
class C:
    def __init__(self):
        print('init')
x = C()
y = C()
print(x is y)
```
3. What does this print? (If it raises an error, name it.)
```python
class C:
    def m():
        return 1
try:
    C().m()
except TypeError:
    print('TypeError')
print(C.m())
```
4. Which are true? Choose every correct option.
   A. An object is an instance of a class
   B. Encapsulation means bundling data with the methods that act on it
   C. A subclass inherits from its superclass
   D. Every class must define __init__
5. What does this print? (If it raises an error, name it.)
```python
class T:
    def __init__(self, v=5):
        self.v = v
    def add(self, n):
        self.v += n
        return self
print(T().add(1).add(2).v, T(0).v)
```
6. Write a class Rectangle with a constructor taking width and height, and methods area() and perimeter(). Show Rectangle(3, 4) giving 12 and 14.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
A greets B B greets A
```
2. Actual result (from running it):
```
init
init
False
```
3. Actual result (from running it):
```
TypeError
1
```
4. Correct: A, B, C (exactly these options, no others)
5. Actual result (from running it):
```
8 0
```
6. The tutor runs or reads the learner's answer and checks: Correct constructor storing instance variables; methods using self; 12 and 14.

## Grading
Apply `rubric.json`'s `stage_rubrics.S07_Classes_Objects_Methods_Constructors` exactly. 6 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S08_Class_and_Instance_Properties_Introspection.
