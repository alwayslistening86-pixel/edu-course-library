# S06_String_Methods - Lesson: String methods and sorting strings

## Goal
The learner predicts the results of the syllabus string methods, including the isxxx() family, and sorts strings correctly.

## Syllabus items taught here
- 3.3a - The isxxx() methods
- 3.3b - join(), split() and strip()
- 3.3c - index(), find() and rfind()
- 3.3d - Ordering strings with sorted()

## How to teach this
Ask what `'  a,b '.strip().split(',')` returns, step by step. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### 3.3a The isxxx() methods
The `isxxx()` methods return a Boolean about the **whole** string, and are False for an empty string: `isalpha()` (letters only), `isdigit()` (digits only), `isalnum()` (letters or digits), `isspace()`, `islower()`, `isupper()`.
```python
for s in ("abc", "abc1", "123", "  ", "", "ABC", "Abc"):
    print(repr(s), s.isalpha(), s.isdigit(), s.isalnum(), s.isspace(), s.islower(), s.isupper())
```
Output:
```
'abc' True False True False True False
'abc1' False False True False True False
'123' False True True False False False
'  ' False False False True False False
'' False False False False False False
'ABC' True False True False False True
'Abc' True False True False False False
```

#### 3.3b join(), split() and strip()
`sep.join(iterable)` glues **strings** together with sep between them (non-strings are a TypeError). `split()` with no argument splits on runs of whitespace and drops empty parts; `split(",")` splits on every comma and keeps empty fields. `strip()` removes whitespace (or the given characters) from both ends; `lstrip()` and `rstrip()` from one end.
```python
print(" a  b ".split(), "a,,b".split(","), "-".join(["x", "y", "z"]))
print("xxhixx".strip("x"), "  pad ".rstrip() + "|")
```
Output:
```
['a', 'b'] ['a', '', 'b'] x-y-z
hi   pad|
```

#### 3.3c index(), find() and rfind()
`find(sub)` returns the lowest index of sub, or **-1** if absent; `rfind(sub)` the highest index, or -1; `index(sub)` is like find but raises **ValueError** if absent. All accept optional start and end positions.
```python
s = "banana"
print(s.find("na"), s.rfind("na"), s.find("x"), s.find("a", 2))
try:
    s.index("x")
except ValueError:
    print("ValueError")
```
Output:
```
2 4 -1 3
ValueError
```

#### 3.3d Ordering strings with sorted()
`sorted(iterable)` returns a new **list**. Sorting a string gives a list of its characters; sorting a list of strings uses code-point order, so capitals come first. `key=str.lower` sorts case-insensitively, and `reverse=True` sorts descending.
```python
print(sorted("cab"), "".join(sorted("cab")))
words = ["pear", "Apple", "banana"]
print(sorted(words), sorted(words, key=str.lower), sorted(words, reverse=True))
```
Output:
```
['a', 'b', 'c'] abc
['Apple', 'banana', 'pear'] ['Apple', 'banana', 'pear'] ['pear', 'banana', 'Apple']
```

## Explicitly not here
Regular expressions are not on the syllabus.
