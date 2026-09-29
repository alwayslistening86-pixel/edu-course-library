# S08_Class_and_Instance_Properties_Introspection - Lesson: Class and instance properties, privacy and introspection

## Goal
The learner predicts where each attribute lives (instance or class), reads __dict__, handles name mangling, and inspects classes and objects at run time.

## Syllabus items taught here
- 4.2a - Instance variables versus class variables
- 4.2b - __dict__ on objects and on classes
- 4.2c - Private components and name mangling
- 4.4a - Introspection and hasattr() on objects and classes
- 4.4b - The __name__, __module__ and __bases__ properties

## How to teach this
Ask what happens to Dog.legs when one dog object does `self.legs = 3`. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### 4.2a Instance variables versus class variables
A **class variable** is defined in the class body and shared by all instances. An **instance variable** belongs to one object. Reading `obj.x` looks in the instance first, then the class. **Assigning** `obj.x = ...` always creates or changes an *instance* variable, which then hides the class one for that object only.
```python
class Dog:
    legs = 4
    count = 0
    def __init__(self, name):
        self.name = name
        Dog.count += 1
a, b = Dog("Rex"), Dog("Fido")
a.legs = 3
print(a.legs, b.legs, Dog.legs, Dog.count)
```
Output:
```
3 4 4 2
```

#### 4.2b __dict__ on objects and on classes
`obj.__dict__` is a dictionary of the **instance** variables only. `Class.__dict__` holds the class's own attributes (class variables and methods), as a read-only mapping.
```python
class C:
    shared = 1
    def __init__(self):
        self.own = 2
o = C()
print(o.__dict__, "shared" in C.__dict__, "own" in C.__dict__)
```
Output:
```
{'own': 2} True False
```

#### 4.2c Private components and name mangling
A name starting with **two underscores** (and not ending with them) inside a class is **name-mangled** to `_ClassName__name`. That hides it from outside access and from accidental clashes in subclasses. It isn't true privacy: the mangled name still works.
```python
class Safe:
    def __init__(self):
        self.__code = 1234
        self._hint = "internal by convention"
s = Safe()
print(s.__dict__)
try:
    print(s.__code)
except AttributeError:
    print("AttributeError")
print(s._Safe__code)
```
Output:
```
{'_Safe__code': 1234, '_hint': 'internal by convention'}
AttributeError
1234
```

#### 4.4a Introspection and hasattr() on objects and classes
**Introspection** means examining objects at run time. `hasattr(obj, "name")` returns True if the attribute can be found, on the instance *or* its class. `getattr`, `setattr` and `isinstance` are related tools.
```python
class A:
    x = 1
    def __init__(self):
        self.y = 2
a = A()
print(hasattr(a, "x"), hasattr(a, "y"), hasattr(A, "x"), hasattr(A, "y"))
```
Output:
```
True True True False
```

#### 4.4b The __name__, __module__ and __bases__ properties
`Class.__name__` is the class's name as a string; `Class.__module__` is the name of the module it was defined in (`__main__` for the running script); `Class.__bases__` is a **tuple** of its direct parent classes. An *instance* doesn't have `__name__`; use `type(obj).__name__`.
```python
class Animal: pass
class Cat(Animal): pass
c = Cat()
print(Cat.__name__, Cat.__module__, Cat.__bases__, Animal.__bases__, type(c).__name__, hasattr(c, "__name__"))
```
Output:
```
Cat __main__ (<class '__main__.Animal'>,) (<class 'object'>,) Cat False
```

## Explicitly not here
Inheritance chains and overriding are S09.
