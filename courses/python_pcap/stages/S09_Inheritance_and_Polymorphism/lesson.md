# S09_Inheritance_and_Polymorphism - Lesson: Inheritance and polymorphism

## Goal
The learner builds single and multiple inheritance hierarchies, predicts method resolution (including diamonds), and uses isinstance, is, overriding and __str__ correctly.

## Syllabus items taught here
- 4.5a - Single and multiple inheritance
- 4.5b - isinstance(), overriding, is and is not
- 4.5c - Polymorphism and overriding __str__()
- 4.5d - Diamond problems and method resolution order

## How to teach this
Show two classes that both define speak(), and a list mixing their objects, looped over with the same call. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### 4.5a Single and multiple inheritance
**Single inheritance**: `class B(A)`. B gets all of A's attributes and methods, and can add or replace them. **Multiple inheritance**: `class C(A, B)`. Lookup searches C, then its parents **left to right** (following the MRO, below).
```python
class Flyer:
    def move(self): return "fly"
    def eat(self): return "seeds"
class Swimmer:
    def move(self): return "swim"
    def dive(self): return "dive"
class Duck(Flyer, Swimmer): pass
d = Duck()
print(d.move(), d.dive(), d.eat(), [c.__name__ for c in Duck.__mro__])
```
Output:
```
fly dive seeds ['Duck', 'Flyer', 'Swimmer', 'object']
```

#### 4.5b isinstance(), overriding, is and is not
**Overriding**: a subclass method with the same name replaces the parent's; `super().method()` still reaches the parent version. `isinstance(obj, Class)` is True for the class **and all its ancestors** (and `issubclass` works on classes). `is` / `is not` test **identity** (the same object), unlike `==`, which tests equality.
```python
class Animal:
    def sound(self): return "..."
class Dog(Animal):
    def sound(self): return "woof, not " + super().sound()
d = Dog()
print(d.sound(), isinstance(d, Animal), isinstance(Animal(), Dog), issubclass(Dog, object))
a, b = [1], [1]
print(a == b, a is b, a is not b)
```
Output:
```
woof, not ... True False True
True False True
```

#### 4.5c Polymorphism and overriding __str__()
**Polymorphism**: the same method call behaves according to each object's own class, so code can work on a mixture of types. Overriding `__str__(self)` controls what `print(obj)` and `str(obj)` show; it must return a string.
```python
class Shape:
    def area(self): return 0
    def __str__(self): return f"{type(self).__name__} with area {self.area()}"
class Sq(Shape):
    def __init__(self, s): self.s = s
    def area(self): return self.s ** 2
class Rect(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h
for shape in (Sq(3), Rect(2, 5), Shape()):
    print(shape)
```
Output:
```
Sq with area 9
Rect with area 10
Shape with area 0
```

#### 4.5d Diamond problems and method resolution order
In a **diamond** (B and C both inherit from A, and D inherits from B and C), A must be searched only once, and after both B and C. Python's **MRO** (C3 linearisation) gives D, B, C, A, object; `D.__mro__` shows it. A class order that can't be made consistent is a TypeError when the class is defined.
```python
class A:
    def who(self): return "A"
class B(A):
    def who(self): return "B"
class C(A):
    def who(self): return "C"
class D(B, C): pass
print(D().who(), [k.__name__ for k in D.__mro__])
try:
    class E(A, B): pass
except TypeError as e:
    print("TypeError: cannot create a consistent MRO")
```
Output:
```
B ['D', 'B', 'C', 'A', 'object']
TypeError: cannot create a consistent MRO
```

## Explicitly not here
Abstract base classes and properties with @property are not on PCAP-31-03.
