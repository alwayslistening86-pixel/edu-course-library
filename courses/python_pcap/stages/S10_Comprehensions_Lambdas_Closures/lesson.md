# S10_Comprehensions_Lambdas_Closures - Lesson: Comprehensions, lambdas, map/filter and closures

## Goal
The learner writes conditional and nested comprehensions, uses lambdas with map, filter and their own higher-order functions, and explains and writes closures.

## Syllabus items taught here
- 5.1a - List comprehensions with if conditions
- 5.1b - Nested list comprehensions
- 5.2a - Defining and using lambdas
- 5.2b - Functions that take lambdas as arguments
- 5.2c - map() and filter()
- 5.3a - Closures: meaning, rationale and use

## How to teach this
Ask for the squares of the odd numbers below 10 in one line. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### 5.1a List comprehensions with if conditions
`[expr for x in it if cond]` keeps only the items where cond is true. A conditional **expression** in the output part (`a if c else b`) is different: it transforms every item and filters nothing.
```python
print([n * n for n in range(10) if n % 2])
print(["odd" if n % 2 else "even" for n in range(4)])
```
Output:
```
[1, 9, 25, 49, 81]
['even', 'odd', 'even', 'odd']
```

#### 5.1b Nested list comprehensions
Comprehensions nest. `[[... for c in cols] for r in rows]` builds a list of lists. `[x for row in m for x in row]` flattens: the `for` clauses read left to right like nested loops.
```python
grid = [[r * 3 + c for c in range(3)] for r in range(2)]
print(grid, [x for row in grid for x in row if x % 2 == 0])
```
Output:
```
[[0, 1, 2], [3, 4, 5]] [0, 2, 4]
```

#### 5.2a Defining and using lambdas
A **lambda** is an anonymous one-expression function: `lambda params: expression`. It returns the expression's value, and can't contain statements. It can be assigned to a name, though PEP 8 prefers `def` for that.
```python
sq = lambda x: x * x
add = lambda a, b=1: a + b
print(sq(5), add(2), add(2, 3), (lambda: "no args")())
```
Output:
```
25 3 5 no args
```

#### 5.2b Functions that take lambdas as arguments
Functions can take other functions as arguments. That's where lambdas shine: short throwaway behaviour passed in, as with `sorted(key=...)` or your own helpers.
```python
def apply_twice(f, x):
    return f(f(x))
print(apply_twice(lambda n: n + 10, 1), sorted(["bb", "a", "ccc"], key=lambda s: -len(s)))
```
Output:
```
21 ['ccc', 'bb', 'a']
```

#### 5.2c map() and filter()
`map(f, iterable)` applies f to every element; `filter(f, iterable)` keeps elements for which f is truthy. Both return **lazy iterators**, so wrap them in `list()` to see the values. An iterator can be used up only once.
```python
m = map(lambda x: x * 2, [1, 2, 3])
print(list(m), list(m))
print(list(filter(lambda x: x > 1, [0, 1, 2, 3])), list(map(str.upper, ["a", "b"])))
```
Output:
```
[2, 4, 6] []
[2, 3] ['A', 'B']
```

#### 5.3a Closures: meaning, rationale and use
A **closure** is an inner function that remembers variables from the enclosing function's scope, even after the outer function has returned. It's used to build configured functions (factories) and to keep private state.
```python
def make_multiplier(k):
    def mult(x):
        return x * k
    return mult
double, triple = make_multiplier(2), make_multiplier(3)
print(double(5), triple(5))
def counter():
    n = 0
    def step():
        nonlocal n
        n += 1
        return n
    return step
c = counter()
c(); c()
print(c())
```
Output:
```
10 15
3
```

## Explicitly not here
Generator expressions and decorators are outside PCAP-31-03's listed objectives.
