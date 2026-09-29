# S08_Tuples_and_Dictionaries - Lesson: Tuples and dictionaries

## Goal
The learner chooses correctly between tuples, lists and dictionaries, and reads, updates and iterates through dictionaries without errors.

## Syllabus items taught here
- 3.2a - Tuples: building, indexing, slicing, immutability
- 3.2b - Tuples compared with lists
- 3.2c - Lists inside tuples and tuples inside lists
- 3.3a - Dictionaries: building, indexing, adding and removing keys
- 3.3b - Iterating through a dictionary's keys and values
- 3.3c - Checking whether a key exists
- 3.3d - Dictionary methods keys(), items() and values()

## How to teach this
Ask why `t = (5)` is not a tuple while `t = (5,)` is. Have the learner predict the output of every example before running it, and run code for real whenever they can.

#### 3.2a Tuples: building, indexing, slicing, immutability
A **tuple** is an ordered, **immutable** sequence: `(1, 2, 3)`, or just `1, 2, 3`. A one-item tuple needs a trailing comma: `(5,)`. `()` is empty. It indexes and slices like a list, but assignment to an element is a TypeError. `+` and `*` build new tuples.
```python
t = (1, 2, 3)
print(t[0], t[-1], t[1:], type((5)), type((5,)), t + (4,), t * 2)
try:
    t[0] = 9
except TypeError as e:
    print("TypeError:", e)
```
Output:
```
1 3 (2, 3) <class 'int'> <class 'tuple'> (1, 2, 3, 4) (1, 2, 3, 1, 2, 3)
TypeError: 'tuple' object does not support item assignment
```

#### 3.2b Tuples compared with lists
Both are ordered and indexable, support `len`, `in`, slicing and iteration, and can mix types. Lists are mutable (append, remove, item assignment); tuples are not, so they are safer for fixed data and can be used as dictionary keys. Tuples have only the methods `count()` and `index()`.

#### 3.2c Lists inside tuples and tuples inside lists
A tuple can **contain a list**, and that list can still be changed, because the tuple holds a reference to it, not a frozen copy. A list can hold tuples.
```python
t = ([1, 2], "x")
t[0].append(3)
print(t)
pairs = [(1, "a"), (2, "b")]
print(pairs[1][1])
```
Output:
```
([1, 2, 3], 'x')
b
```

#### 3.3a Dictionaries: building, indexing, adding and removing keys
A **dictionary** maps unique keys to values: `{"uk": "London", "fr": "Paris"}`. Keys must be immutable (strings, numbers, tuples). Read with `d[key]` (a missing key is a KeyError) or `d.get(key)` (returns None or a default). Assigning `d[key] = v` adds or replaces; `del d[key]` removes; `pop(key)` removes and returns the value; `clear()` empties it. Dictionaries keep insertion order.
```python
d = {"uk": "London", "fr": "Paris"}
d["de"] = "Berlin"
d["uk"] = "LONDON"
del d["fr"]
print(d, d.get("es"), d.get("es", "?"), len(d))
```
Output:
```
{'uk': 'LONDON', 'de': 'Berlin'} None ? 2
```

#### 3.3b Iterating through a dictionary's keys and values
Looping over a dictionary gives its **keys**. Use `.values()` for values and `.items()` for key-value pairs, which unpack neatly.
```python
ages = {"Ann": 31, "Bo": 25}
for k in ages:
    print(k, end=" ")
print()
for name, age in ages.items():
    print(name, "is", age)
```
Output:
```
Ann Bo 
Ann is 31
Bo is 25
```

#### 3.3c Checking whether a key exists
`key in d` checks **keys only**, not values. Test before reading to avoid a KeyError.
```python
d = {"a": 1}
print("a" in d, 1 in d, 1 in d.values())
```
Output:
```
True False True
```

#### 3.3d Dictionary methods keys(), items() and values()
`keys()`, `values()` and `items()` return live **views**, which you can loop over, test with `in`, or convert with `list()`.
```python
d = {"x": 1, "y": 2}
print(list(d.keys()), list(d.values()), list(d.items()))
```
Output:
```
['x', 'y'] [1, 2] [('x', 1), ('y', 2)]
```

## Explicitly not here
Dictionary comprehensions and sets are not on the PCEP syllabus.
