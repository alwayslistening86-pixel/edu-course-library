# S07_Lists - Lesson: Lists

## Goal
The learner builds, indexes, slices, modifies, copies and nests lists, and predicts the result of every list operation on the syllabus.

## Syllabus items taught here
- 3.1a - Building lists (vectors)
- 3.1b - List indexing and slicing
- 3.1c - len() and sorted() on lists
- 3.1d - List methods: append, insert, index and others
- 3.1e - The del instruction
- 3.1f - Iterating through a list with for
- 3.1g - Initialising and building lists in loops
- 3.1h - Membership: in and not in
- 3.1i - List comprehensions
- 3.1j - Copying versus aliasing (cloning) lists
- 3.1k - Nested lists: matrices and cubes

## How to teach this
Run `a = [1, 2]; b = a; b.append(3); print(a)` and ask why a changed. That is the key idea of this stage. Have the learner predict the output of every example before running it, and run code for real whenever they can.

#### 3.1a Building lists (vectors)
A list is an ordered, **mutable** collection in square brackets: `[3, "x", 2.5]`. Elements can have mixed types. `[]` is empty; `list("abc")` gives `['a', 'b', 'c']`; `list(range(3))` gives `[0, 1, 2]`.

#### 3.1b List indexing and slicing
**Indexing** starts at 0; negative indices count from the end (`-1` is last). Out of range is an IndexError. **Slicing** `a[start:stop:step]` returns a *new* list, with stop excluded; omitted parts default to the ends. Slicing out of range never errors. `a[::-1]` reverses. Assigning to an index or a slice changes the list in place.
```python
a = [10, 20, 30, 40, 50]
print(a[0], a[-1], a[1:3], a[:2], a[3:], a[::2], a[::-1], a[10:])
a[1] = 99
print(a)
```
Output:
```
10 50 [20, 30] [10, 20] [40, 50] [10, 30, 50] [50, 40, 30, 20, 10] []
[10, 99, 30, 40, 50]
```

#### 3.1c len() and sorted() on lists
`len(a)` gives the number of elements. `sorted(a)` returns a **new** sorted list and leaves `a` unchanged; `sorted(a, reverse=True)` sorts descending. By contrast, the method `a.sort()` sorts in place and returns None.
```python
a = [3, 1, 2]
b = sorted(a)
print(len(a), a, b, sorted(a, reverse=True))
print(a.sort(), a)
```
Output:
```
3 [3, 1, 2] [1, 2, 3] [3, 2, 1]
None [1, 2, 3]
```

#### 3.1d List methods: append, insert, index and others
Common methods (all change the list in place): `append(x)` adds one item at the end; `insert(i, x)` puts x before index i; `extend(iterable)` adds several; `remove(x)` deletes the first x (ValueError if absent); `pop()` removes and returns the last item, or `pop(i)` item i; `index(x)` returns the first position of x (ValueError if absent); `count(x)`; `reverse()`; `sort()`.
```python
a = [1, 2]
a.append(3); a.insert(0, 0); a.extend([4, 5])
print(a, a.index(3), a.pop(), a)
a.remove(0); a.reverse()
print(a, a.count(2))
```
Output:
```
[0, 1, 2, 3, 4] 3 5 [0, 1, 2, 3, 4]
[4, 3, 2, 1] 1
```

#### 3.1e The del instruction
`del a[i]` removes item i; `del a[i:j]` removes a slice; `del a` removes the *name* itself (using it afterwards is a NameError).
```python
a = [0, 1, 2, 3, 4]
del a[1]
del a[1:3]
print(a)
```
Output:
```
[0, 4]
```

#### 3.1f Iterating through a list with for
`for x in a:` visits each element. To change elements you need their index: `for i in range(len(a)):` then `a[i] = ...`. Assigning to the loop variable does not change the list.
```python
a = [1, 2, 3]
for x in a:
    x = x * 10
print(a)
for i in range(len(a)):
    a[i] *= 10
print(a)
```
Output:
```
[1, 2, 3]
[10, 20, 30]
```

#### 3.1g Initialising and building lists in loops
**Initialising** means creating the list before the loop that fills it, often empty (`result = []`) or pre-sized (`[0] * 5`).
```python
squares = []
for n in range(1, 6):
    squares.append(n * n)
print(squares, [0] * 4)
```
Output:
```
[1, 4, 9, 16, 25] [0, 0, 0, 0]
```

#### 3.1h Membership: in and not in
`x in a` and `x not in a` test membership and return a Boolean.
```python
print(3 in [1, 2, 3], "z" not in ["a", "b"])
```
Output:
```
True True
```

#### 3.1i List comprehensions
A **list comprehension** builds a list in one expression: `[expression for item in iterable if condition]`.
```python
print([n * n for n in range(6) if n % 2 == 0])
print([c.upper() for c in "hey"])
```
Output:
```
[0, 4, 16]
['H', 'E', 'Y']
```

#### 3.1j Copying versus aliasing (cloning) lists
Assignment **does not copy**: `b = a` makes both names refer to the same list, so a change through one shows through the other. Copy with a full slice `a[:]`, `list(a)` or `a.copy()`. These are shallow copies: a nested inner list is still shared.
```python
a = [1, 2]
b = a
c = a[:]
b.append(3)
print(a, b, c, a is b, a is c)
```
Output:
```
[1, 2, 3] [1, 2, 3] [1, 2] True False
```

#### 3.1k Nested lists: matrices and cubes
Lists can hold lists: a 2-D **matrix** is a list of rows, indexed `m[row][col]`; a 3-D **cube** adds another level. Build them with a comprehension: `[[0] * 3 for _ in range(2)]`. The shortcut `[[0] * 3] * 2` repeats the *same* row object twice, so changing one row changes both.
```python
m = [[1, 2, 3], [4, 5, 6]]
print(m[1][2], len(m), len(m[0]))
good = [[0] * 3 for _ in range(2)]
bad = [[0] * 3] * 2
good[0][0] = 9; bad[0][0] = 9
print(good, bad)
cube = [[[0] * 2 for _ in range(2)] for _ in range(2)]
cube[1][0][1] = 7
print(cube)
```
Output:
```
6 2 3
[[9, 0, 0], [0, 0, 0]] [[9, 0, 0], [9, 0, 0]]
[[[0, 0], [0, 0]], [[0, 7], [0, 0]]]
```

## Explicitly not here
Tuples and dictionaries are S08; strings in depth are S09.
