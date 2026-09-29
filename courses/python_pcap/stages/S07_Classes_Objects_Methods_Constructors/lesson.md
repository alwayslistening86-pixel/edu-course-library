# S07_Classes_Objects_Methods_Constructors - Lesson: Classes, objects, methods and constructors

## Goal
The learner uses OOP vocabulary precisely and writes classes with constructors and methods that use self correctly.

## Syllabus items taught here
- 4.1a - Class, object, property and method
- 4.1b - Encapsulation, inheritance, superclass and subclass
- 4.1c - Identifying a class's components
- 4.3a - Declaring and using methods
- 4.3b - The self parameter
- 4.6a - Declaring and invoking constructors

## How to teach this
Ask the learner to describe a bank account as data plus behaviour, then show the class. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### 4.1a Class, object, property and method
A **class** is a blueprint; an **object** (instance) is one thing built from it. **Properties** (attributes) hold an object's data; **methods** are functions defined in the class that act on the object.

#### 4.1b Encapsulation, inheritance, superclass and subclass
**Encapsulation**: bundling data with the methods that use it, and hiding internal detail behind an interface. **Inheritance**: a **subclass** (child) reuses and extends a **superclass** (parent). Every class ultimately inherits from `object`.

#### 4.1c Identifying a class's components
Identifying components: in `class Account:`, anything assigned in the class body is a **class variable**; `def` inside the class makes a **method**; `__init__` is the **constructor**; attributes assigned as `self.x = ...` are **instance variables**.
```python
class Account:
    bank = "PyBank"
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
a = Account("Ann")
print(a.deposit(50), a.owner, Account.bank)
```
Output:
```
50 Ann PyBank
```

#### 4.3a Declaring and using methods
A method is a function defined inside a class. Call it through an instance (`obj.method(args)`) or through the class, passing the instance explicitly (`Class.method(obj, args)`). Methods can call each other through self.
```python
class Counter:
    def __init__(self):
        self.n = 0
    def inc(self):
        self.n += 1
        return self
    def twice(self):
        return self.inc().inc()
c = Counter()
c.twice()
Counter.inc(c)
print(c.n)
```
Output:
```
3
```

#### 4.3b The self parameter
`self` is the first parameter of every instance method and refers to the instance the method was called on. Python passes it automatically in `obj.method()`. The name is a convention, but it's always the first parameter. Forgetting it gives a TypeError about the number of arguments.
```python
class Bad:
    def hello():
        return "hi"
try:
    Bad().hello()
except TypeError as e:
    print("TypeError:", e)
```
Output:
```
TypeError: Bad.hello() takes 0 positional arguments but 1 was given
```

#### 4.6a Declaring and invoking constructors
The **constructor** `__init__(self, ...)` runs automatically when an object is created with `ClassName(args)`, and initialises its instance variables. It must not return a value (other than None). A class without `__init__` inherits one from its parent (ultimately `object`). A subclass constructor usually calls `super().__init__(...)`.
```python
class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
p, q = Point(), Point(3, 4)
print(p.x, p.y, q.x, q.y)
```
Output:
```
0 0 3 4
```

## Explicitly not here
Class-versus-instance variables in depth and name mangling are S08; inheritance is S09.
