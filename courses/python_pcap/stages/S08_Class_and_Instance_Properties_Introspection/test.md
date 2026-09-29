# S08_Class_and_Instance_Properties_Introspection - Test: Class and instance properties, privacy and introspection

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
class A:
    v = 1
a, b = A(), A()
a.v = 2
A.v = 3
print(a.v, b.v, A.v)
```
2. What does this print? (If it raises an error, name it.)
```python
class A:
    items = []
    def add(self, x):
        self.items.append(x)
p, q = A(), A()
p.add(1)
q.add(2)
print(p.items, A.items)
```
3. What does this print? (If it raises an error, name it.)
```python
class C:
    k = 1
    def __init__(self):
        self.j = 2
c = C()
print(c.__dict__, hasattr(c, 'k'), hasattr(C, 'j'))
```
4. What does this print? (If it raises an error, name it.)
```python
class Vault:
    def __init__(self):
        self.__pin = 7
v = Vault()
print(hasattr(v, '__pin'), hasattr(v, '_Vault__pin'))
```
5. What does this print? (If it raises an error, name it.)
```python
class X: pass
class Y(X): pass
print(Y.__bases__, X.__bases__, Y.__module__)
```
6. Which expressions are valid and return the string 'Y' for an instance y of class Y? Choose every correct option.
   A. `Y.__name__`
   B. `y.__name__`
   C. `type(y).__name__`
   D. `y.__class__.__name__`
7. Write a class that counts how many instances have been created, using a class variable, and give each instance its own serial number.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
2 3 3
```
2. Actual result (from running it):
```
[1, 2] [1, 2]
```
3. Actual result (from running it):
```
{'j': 2} True False
```
4. Actual result (from running it):
```
False True
```
5. Actual result (from running it):
```
(<class '__main__.X'>,) (<class 'object'>,) __main__
```
6. Correct: A, C, D (exactly these options, no others)
7. The tutor runs or reads the learner's answer and checks: Class variable incremented in __init__ via the class name; instance variable stores the serial; correct values.

## Grading
Apply `rubric.json`'s `stage_rubrics.S08_Class_and_Instance_Properties_Introspection` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S09_Inheritance_and_Polymorphism.
