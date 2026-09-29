# S09_Strings - Lesson: Strings

## Goal
The learner builds strings safely, uses indexing, slicing, escapes and multi-line strings, and applies the common string functions and methods.

## Syllabus items taught here
- 3.4a - Constructing strings
- 3.4b - String indexing, slicing and immutability
- 3.4c - Escaping with the backslash
- 3.4d - Quotes and apostrophes inside strings
- 3.4e - Multi-line strings
- 3.4f - Basic string functions and methods

## How to teach this
Ask what `s = 'hello'; s[0] = 'H'` does, and how to actually get 'Hello'. Have the learner predict the output of every example before running it, and run code for real whenever they can.

#### 3.4a Constructing strings
Strings are built from literals, `+` and `*`, `str()`, or methods such as `join`. Strings are sequences of characters, so `len`, `in` and `for` work on them.
```python
name = "Ada"
s = "Hi " + name + "!" * 2
print(s, len(s), "da" in s)
```
Output:
```
Hi Ada!! 8 True
```

#### 3.4b String indexing, slicing and immutability
Strings index and slice exactly like lists, but they are **immutable**: `s[0] = "H"` is a TypeError. Build a new string instead.
```python
s = "python"
print(s[0], s[-1], s[1:4], s[::-1])
s = "P" + s[1:]
print(s)
```
Output:
```
p n yth nohtyp
Python
```

#### 3.4c Escaping with the backslash
The **backslash** starts an escape sequence: `\n` newline, `\t` tab, `\\` one backslash, `\'` and `\"` quotes. Each escape is one character, so `len("a\nb")` is 3.
```python
s = "a\tb\nc\\d"
print(s)
print(len("a\nb"))
```
Output:
```
a	b
c\d
3
```

#### 3.4d Quotes and apostrophes inside strings
To put a quote inside a string, use the other kind of quote outside (`"it's"`, `'say "hi"'`) or escape it (`'it\'s'`).
```python
print("it's", 'say "hi"', 'it\'s')
```
Output:
```
it's say "hi" it's
```

#### 3.4e Multi-line strings
Triple quotes (`'''...'''` or `"""..."""`) make **multi-line strings**; the line breaks become `\n` characters inside the string.
```python
s = '''line one
line two'''
print(s)
print(len(s.split("\n")))
```
Output:
```
line one
line two
2
```

#### 3.4f Basic string functions and methods
Functions: `len()`, `str()`, `ord()` (character to code point), `chr()` (the reverse). Methods (each returns a **new** string or a value; the original never changes): `upper()`, `lower()`, `capitalize()`, `title()`, `strip()`, `find()` (-1 if absent) versus `index()` (ValueError if absent), `count()`, `replace()`, `startswith()`, `endswith()`, `isdigit()`, `isalpha()`, `split()` (returns a list), `sep.join(list)`.
```python
s = "  Hello World  "
t = s.strip()
print(t.upper(), t.lower(), t.find("o"), t.find("z"), t.count("l"))
print(t.replace("World", "Py"), t.split(), "-".join(["a", "b"]), "42".isdigit())
print(ord("A"), chr(66), s)
```
Output:
```
HELLO WORLD hello world 4 -1 3
Hello Py ['Hello', 'World'] a-b True
65 B   Hello World  
```

## Explicitly not here
f-strings and format() are not on the PCEP syllabus.
