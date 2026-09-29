# S10_Functions - Lesson: Functions, arguments and scope

## Goal
The learner defines and calls functions with every argument style on the syllabus, predicts return values including None, traces recursion and scope, and recognises a simple generator.

## Syllabus items taught here
- 4.1a - Defining and calling functions, and simple generators
- 4.1b - The return keyword and returning results
- 4.1c - The None value
- 4.1d - Recursion
- 4.2a - Parameters versus arguments
- 4.2b - Positional, keyword and mixed argument passing
- 4.2c - Default parameter values
- 4.2d - Name scopes, shadowing and the global keyword

## How to teach this
Ask what `def f(): print('hi')` then `x = f()` then `print(x)` displays. (hi, then None.) Have the learner predict the output of every example before running it, and run code for real whenever they can.

#### 4.1a Defining and calling functions, and simple generators
`def name(parameters):` defines a function, and the indented body runs only when it is **called**: `name(arguments)`. A function must be defined before the line that calls it runs. A function containing `yield` is a **generator**: calling it returns a generator object that produces values one at a time, resuming after each `yield`.
```python
def greet(who):
    print("Hello,", who)
greet("Sam")
def count_up(n):
    for i in range(n):
        yield i
print(list(count_up(3)))
```
Output:
```
Hello, Sam
[0, 1, 2]
```

#### 4.1b The return keyword and returning results
`return value` ends the function immediately and sends the value back to the caller. Code after the `return` doesn't run. A function can have several `return` statements; the first one reached wins.
```python
def sign(n):
    if n < 0:
        return "negative"
    return "non-negative"
    print("never printed")
print(sign(-4), sign(0))
```
Output:
```
negative non-negative
```

#### 4.1c The None value
`None` means "no value". A function with no `return`, or a bare `return`, returns None. It is falsy, and it is tested with `is None`.
```python
def nothing():
    pass
r = nothing()
print(r, r is None, bool(r))
```
Output:
```
None True False
```

#### 4.1d Recursion
A **recursive** function calls itself. It needs a base case that stops the recursion; without one Python raises RecursionError.
```python
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)
print(fact(5))
```
Output:
```
120
```

#### 4.2a Parameters versus arguments
**Parameters** are the names in the definition (`def area(w, h)`); **arguments** are the values passed in the call (`area(3, 4)`). The number of arguments must match, or you get a TypeError.

#### 4.2b Positional, keyword and mixed argument passing
**Positional** arguments are matched by order; **keyword** arguments by name (`area(h=4, w=3)`). In a mixed call, positional arguments must come first, and one parameter can't be given twice.
```python
def show(a, b, c):
    print(a, b, c)
show(1, 2, 3)
show(c=3, a=1, b=2)
show(1, c=3, b=2)
try:
    show(1, a=1, c=3)
except TypeError as e:
    print("TypeError:", e)
```
Output:
```
1 2 3
1 2 3
1 2 3
TypeError: show() got multiple values for argument 'a'
```

#### 4.2c Default parameter values
**Default values** make a parameter optional: `def power(x, n=2)`. Parameters with defaults must come after those without.
```python
def power(x, n=2):
    return x ** n
print(power(3), power(3, 3), power(n=0, x=9))
```
Output:
```
9 27 1
```

#### 4.2d Name scopes, shadowing and the global keyword
Names assigned inside a function are **local**: they exist only during the call and **shadow** (hide) any global of the same name. A function can *read* a global that it doesn't assign. Assigning a global from inside needs `global name`. Parameters are local too. Changing a mutable argument (such as appending to a list) is visible outside, because it's the same object.
```python
x = 10
def f():
    x = 99
    return x
def g():
    global x
    x = 5
print(f(), x)
g()
print(x)
def add_item(lst):
    lst.append("new")
items = []
add_item(items)
print(items)
```
Output:
```
99 10
5
['new']
```

## Explicitly not here
Lambdas, closures and modules belong to PCAP, not PCEP.
