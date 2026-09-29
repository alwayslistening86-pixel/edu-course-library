# S01_Programming_Foundations - Lesson: Programming foundations

## Goal
The learner writes and reads Python using comprehensions, generators and iterators; designs and traces recursive functions including their call stack; writes classes using encapsulation, inheritance, polymorphism and dunder methods; and uses higher-order functions, closures and lambdas in a functional style.

## Syllabus items taught here
- 1a - Python control flow beyond A-level: list/dict/set comprehensions, generators and iterators
- 1b - Recursion: recursive function design, base and recursive cases, tracing recursive calls and call-stack depth
- 1c - Object-oriented programming in Python: classes, encapsulation, inheritance, polymorphism, dunder methods
- 1d - Functional programming: higher-order functions, closures, lambda, map/filter/reduce, first-class functions

## How to teach this
Ask the learner to write a one-line list comprehension that squares every even number in a list, then ask them to explain what a for-loop version of it would look like -- to show comprehensions are sugar, not magic. Work every algorithm trace, calculation and code example with the learner step by step before revealing the next stage; have the learner predict a program's output before it is run. This is honours-degree material: insist on precise terminology and full justification, not just a right answer. Every computed value, algorithm trace and program output in these files was produced by actually running Python when the course was built, never hand-typed.

#### 1a Python control flow beyond A-level: list/dict/set comprehensions, generators and iterators
**Comprehensions.** A list comprehension `[expr for item in iterable if cond]` builds a list without an explicit loop; dict and set comprehensions follow the same pattern with `{k: v for ...}` and `{expr for ...}`. *Example:* `[x*x for x in range(6) if x % 2 == 0]` gives `[0, 4, 16]`. **Generators and iterators.** A generator function uses `yield` instead of `return`; each call to `next()` resumes execution from where it last yielded, so a generator produces values lazily (one at a time, on demand) rather than building a whole list in memory -- important for large or infinite sequences. Any object with a `__next__` method (and `__iter__` returning itself) is an *iterator*; a `for` loop calls `iter()` then repeatedly `next()` until `StopIteration`.
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

g = countdown(3)
print(next(g))
print(next(g))
print(list(g))
```
Output:
```
3
2
[1]
```

#### 1b Recursion: recursive function design, base and recursive cases, tracing recursive calls and call-stack depth
**Exception handling with custom exceptions.** `try`/`except`/`else`/`finally` catches and handles runtime errors; `raise` signals one. A custom exception is a class inheriting from `Exception` (or a more specific built-in), letting code distinguish *this* error condition from any other.
```python
class InsufficientFundsError(Exception):
    def __init__(self, shortfall):
        super().__init__(f"short by {shortfall}")
        self.shortfall = shortfall

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(amount - balance)
    return balance - amount

try:
    withdraw(50, 80)
except InsufficientFundsError as e:
    print("blocked:", e, "-- shortfall", e.shortfall)
```
Output:
```
blocked: short by 30 -- shortfall 30
```
`finally` always runs, whether or not an exception occurred, and is used for cleanup (e.g. closing a file) that must happen either way.

#### 1c Object-oriented programming in Python: classes, encapsulation, inheritance, polymorphism, dunder methods
**Object-oriented programming.** A class bundles data (attributes) and behaviour (methods). *Encapsulation*: attributes prefixed `_` (convention: internal) or `__` (name-mangled: `_ClassName__attr`) signal that outside code should not access them directly; a `@property` exposes a controlled, computed view. *Inheritance*: `class Dog(Animal)` reuses and extends `Animal`'s behaviour; `super().__init__()` calls the parent constructor. *Polymorphism*: different subclasses can be used interchangeably wherever the parent type is expected, each responding to the same method call in its own way. *Dunder (magic) methods* let a class integrate with Python's own syntax: `__init__` (construction), `__str__` (str()/print), `__eq__` (==), `__len__` (len()), `__repr__` (developer-facing representation).
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return f"{self.name} makes a sound"
    def __str__(self):
        return f"Animal({self.name})"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"

for a in [Dog("Rex"), Cat("Tom")]:
    print(str(a), "->", a.speak())
```
Output:
```
Animal(Rex) -> Rex says Woof
Animal(Tom) -> Tom says Meow
```

#### 1d Functional programming: higher-order functions, closures, lambda, map/filter/reduce, first-class functions
**Functional programming.** Functions are *first-class*: they can be assigned to variables, passed as arguments, and returned from other functions. A *higher-order function* takes and/or returns a function; `map(f, xs)` applies `f` to every element, `filter(pred, xs)` keeps elements where `pred` is true, `reduce(f, xs, init)` (from `functools`) combines elements pairwise into a single value. A `lambda` is a small anonymous function (`lambda x: x*2`). A *closure* is a function that remembers variables from its enclosing scope even after that scope has finished executing.
```python
from functools import reduce

def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

triple = make_multiplier(3)
print(triple(7))
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * x, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))
print(reduce(lambda a, b: a + b, nums, 0))
```
Output:
```
21
[1, 4, 9, 16, 25]
[2, 4]
15
```
`triple` is a closure: it remembers `factor=3` from `make_multiplier`'s scope even though that call has already returned.

## Explicitly not here
Recursion is 1b's sibling item; object orientation is 1c; functional programming (map/filter/reduce, closures) is 1d.
