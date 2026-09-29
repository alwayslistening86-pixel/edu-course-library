# S05_Characters_and_String_Operations - Lesson: Characters, encodings and string operations

## Goal
The learner explains how text is stored (ASCII, Unicode, UTF-8, code points) and predicts the result of any string operation on the syllabus, including comparisons.

## Syllabus items taught here
- 3.1a - Encoding standards: ASCII, Unicode, UTF-8
- 3.1b - Code points and escape sequences
- 3.2a - ord() and chr()
- 3.2b - String indexing, slicing and immutability
- 3.2c - String iteration, concatenation, repetition and comparison
- 3.2d - Membership: in and not in

## How to teach this
Ask why `'Z' < 'a'` is True but `'z' < 'A'` is False. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### 3.1a Encoding standards: ASCII, Unicode, UTF-8
**ASCII** encodes 128 characters (English letters, digits, punctuation, control codes) in 7 bits. **Unicode** assigns a number, a **code point**, to every character in every script. **UTF-8** is the most common way to store code points as bytes: ASCII characters take 1 byte, others 2 to 4, so plain English UTF-8 is identical to ASCII. Python 3 strings are sequences of Unicode code points.
```python
for s in ("A", "é", "€", "😀"):
    print(s, ord(s), len(s.encode("utf-8")), "bytes in UTF-8")
```
Output:
```
A 65 1 bytes in UTF-8
é 233 2 bytes in UTF-8
€ 8364 3 bytes in UTF-8
😀 128512 4 bytes in UTF-8
```

#### 3.1b Code points and escape sequences
An **escape sequence** writes a character that is hard to type: `\n`, `\t`, `\\`, `\'`, and code-point escapes `\xhh` (2 hex digits), `\uhhhh` (4) and `\Uhhhhhhhh` (8). Each produces **one** character.
```python
s = "\u00e9\x41\t!"
print(s, len(s), ord(s[0]))
```
Output:
```
éA	! 4 233
```

#### 3.2a ord() and chr()
`ord(ch)` returns a one-character string's code point; `chr(n)` returns the character for code point n. They are inverses. `ord` of a longer string is a TypeError.
```python
print(ord("a"), chr(98), chr(ord("A") + 25), ord(chr(8364)))
```
Output:
```
97 b Z 8364
```

#### 3.2b String indexing, slicing and immutability
Strings index and slice like lists (negative indices, `[start:stop:step]`, out-of-range slices are safe) but are **immutable**: item assignment is a TypeError, and every 'change' builds a new string.
```python
s = "immutable"
print(s[2:6], s[-3:], s[::-2])
try:
    s[0] = "I"
except TypeError as e:
    print("TypeError")
```
Output:
```
muta ble ebtmi
TypeError
```

#### 3.2c String iteration, concatenation, repetition and comparison
`for ch in s` iterates characters; `+` concatenates; `*` repeats. Comparisons (`== < >` ...) compare **code point by code point** from the left; the first difference decides, and a prefix is smaller than the longer string. All uppercase ASCII letters come before all lowercase ones.
```python
print("apple" < "banana", "Zebra" < "apple", "app" < "apple", "10" < "9", "a" * 3 + "b")
```
Output:
```
True True True True aaab
```

#### 3.2d Membership: in and not in
`in` tests for a **substring**, not just a single character; `not in` is its negation. The empty string is in every string.
```python
print("ell" in "hello", "le" in "hello", "" in "x", "H" not in "hello")
```
Output:
```
True False True True
```

## Explicitly not here
String methods are S06.
