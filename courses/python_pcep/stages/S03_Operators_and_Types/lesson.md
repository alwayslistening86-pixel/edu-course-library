# S03_Operators_and_Types - Lesson: Operators, priorities and types

## Goal
The learner predicts the value and type of any expression the exam can pose, including priorities, bitwise and Boolean operators, float inaccuracy and casting.

## Syllabus items taught here
- 1.4a - Arithmetic operators ** * / % // + -
- 1.4b - String operators * and +
- 1.4c - Assignment and shortcut (augmented) operators
- 1.4d - Unary and binary operators
- 1.4e - Operator priority and binding (associativity)
- 1.4f - Bitwise operators ~ & ^ | << >>
- 1.4g - Boolean operators not, and, or
- 1.4h - Boolean expressions
- 1.4i - Relational (comparison) operators
- 1.4j - Floating-point accuracy
- 1.4k - Type casting between int, float, str and bool

## How to teach this
Ask the learner to predict `2 ** 3 ** 2` and `-3 // 2` before running them. Both surprise most people. Have the learner predict the output of every example before running it, and run code for real whenever they can.

#### 1.4a Arithmetic operators ** * / % // + -
Arithmetic: `+ - *` as usual; `/` true division, which always returns a float; `//` floor division, rounding down towards minus infinity (not towards zero); `%` remainder, whose sign follows the divisor; `**` power. Any float operand makes the result a float.
```python
print(7 / 2, 6 / 3, 7 // 2, -7 // 2, 7 % 3, -7 % 3, 2 ** 10, 7.0 // 2)
```
Output:
```
3.5 2.0 3 -4 1 2 1024 3.0
```

#### 1.4b String operators * and +
With strings, `+` concatenates and `*` repeats (string times integer). Mixing a string and a number with `+` is a TypeError.
```python
print("ab" + "cd", "ab" * 3, 3 * "-")
```
Output:
```
abcd ababab ---
```

#### 1.4c Assignment and shortcut (augmented) operators
`=` assigns. **Shortcut (augmented)** operators combine an operation with assignment: `x += 1` means `x = x + 1`; likewise `-= *= /= //= %= **=`. Note `x /= 2` makes `x` a float.
```python
x = 10
x += 5
x //= 4
x **= 2
print(x)
```
Output:
```
9
```

#### 1.4d Unary and binary operators
A **binary** operator has two operands (`a - b`); a **unary** operator has one (`-a`, `+a`, `not a`, `~a`). The same symbol `-` can be either, depending on position.

#### 1.4e Operator priority and binding (associativity)
**Priority** (highest first) for the exam: `**`; unary `+ - ~`; `* / // %`; binary `+ -`; `<< >>`; `&`; `^`; `|`; comparisons `< <= > >= == !=`; `not`; `and`; `or`. **Binding**: most operators bind left to right (`10 - 4 - 3` is 3), but `**` binds right to left (`2 ** 3 ** 2` is `2 ** 9`). And `**` binds tighter than a unary minus on its left: `-2 ** 2` is -4. Brackets override everything.
```python
print(2 ** 3 ** 2, -2 ** 2, (-2) ** 2, 10 - 4 - 3, 2 + 3 * 4 ** 2)
```
Output:
```
512 -4 4 3 50
```

#### 1.4f Bitwise operators ~ & ^ | << >>
**Bitwise** operators work on the binary digits of integers: `&` and, `|` or, `^` exclusive or, `~` not (for integers `~x` equals `-x - 1`), `<<` shift left (x2 per place), `>>` shift right (floor-halve per place).
```python
a, b = 12, 10          # 1100 and 1010
print(a & b, a | b, a ^ b, ~a, a << 2, a >> 2)
```
Output:
```
8 14 6 -13 48 3
```

#### 1.4g Boolean operators not, and, or
**Boolean operators**: `not` flips; `and` is true only if both are; `or` is true if either is. They **short-circuit**: `and` stops at the first falsy operand, `or` at the first truthy one, and they return that operand itself, not necessarily `True` or `False`.
```python
print(True and False, True or False, not 0)
print(0 or "default", 5 and 7, "" and 1/0)
```
Output:
```
False True True
default 7 
```

#### 1.4h Boolean expressions
A **Boolean expression** evaluates to a truth value. Falsy values: `False`, `None`, `0`, `0.0`, `""`, and empty lists, tuples and dictionaries; everything else is truthy. Comparisons chain: `1 < x < 10` means `1 < x and x < 10`.
```python
x = 5
print(1 < x < 10, bool([]), bool("0"), bool(0.0))
```
Output:
```
True False True False
```

#### 1.4i Relational (comparison) operators
**Relational** operators: `==` equal, `!=` not equal, `> >= < <=`. They return `True`/`False`. Equality compares values across numeric types (`1 == 1.0` is True); strings compare character by character by code point, so `"Z" < "a"` is True. Don't confuse `==` (compare) with `=` (assign).

#### 1.4j Floating-point accuracy
**Floats are approximations** in binary, so some decimal values can't be stored exactly. Never test floats with `==` after arithmetic; compare the difference with a small tolerance instead.
```python
print(0.1 + 0.2, 0.1 + 0.2 == 0.3, abs((0.1 + 0.2) - 0.3) < 1e-9)
```
Output:
```
0.30000000000000004 False True
```

#### 1.4k Type casting between int, float, str and bool
**Type casting** converts explicitly: `int()` truncates a float towards zero (`int(-3.9)` is -3) and parses a whole-number string (`int("42")`, but `int("4.2")` is a ValueError); `float()` parses numbers and number-strings; `str()` turns anything into text; `bool()` applies the truthiness rules. Python never adds a number to a string for you.
```python
print(int(3.9), int(-3.9), int("42"), float("4.2"), str(7) + "7", bool("False"))
```
Output:
```
3 -3 42 4.2 77 True
```

## Explicitly not here
Input conversion is S04; string methods are S09.
