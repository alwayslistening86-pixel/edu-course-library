# S02_Literals_Variables_and_Number_Systems - Lesson: Literals, variables and number systems

## Goal
The learner writes and reads every literal the exam uses, converts between number bases, and names variables legally and in PEP 8 style.

## Syllabus items taught here
- 1.3a - Boolean, integer and floating-point literals
- 1.3b - Scientific (exponent) notation for floats
- 1.3c - String literals
- 1.3d - Binary, octal, decimal and hexadecimal literals
- 1.3e - Variables and assignment
- 1.3f - Variable naming rules and conventions
- 1.3g - PEP 8 style recommendations

## How to teach this
Show `0x1F`, `0b11111`, `0o37` and `31` and ask which is biggest. (They are all the same number.) Have the learner predict the output of every example before running it, and run code for real whenever they can.

#### 1.3a Boolean, integer and floating-point literals
A **literal** is a value written directly in code. `True` and `False` are the Boolean literals (capital first letter). Integers have no decimal point (`7`, `-12`, `1_000_000` where underscores are allowed for readability). Floats have a point or an exponent (`7.0`, `.5`, `4.`). The type matters: `7` and `7.0` compare equal but are different types.
```python
print(type(7), type(7.0), type(True))
print(1_000_000, 7 == 7.0, .5 + 4.)
```
Output:
```
<class 'int'> <class 'float'> <class 'bool'>
1000000 True 4.5
```

#### 1.3b Scientific (exponent) notation for floats
**Scientific notation** writes a float as mantissa `e` exponent: `3e8` means 3 x 10^8, `1.5E-3` means 0.0015. The result is always a float, even when it looks whole. Python prints very large or small floats in this notation itself.
```python
print(3e8, type(3e8))
print(1.5E-3)
print(0.00000001)
```
Output:
```
300000000.0 <class 'float'>
0.0015
1e-08
```

#### 1.3c String literals
**String literals** are text in single or double quotes; both mean the same. `"it's"` needs double quotes (or an escape, see S09). An empty string is `""`. Strings are a different type from numbers: `"5"` is not `5`.

#### 1.3d Binary, octal, decimal and hexadecimal literals
Integers can be written in four bases. Prefixes: `0b` binary, `0o` octal, `0x` hexadecimal (upper or lower case), no prefix for decimal. Python stores the same integer however you wrote it and prints it in decimal. `bin()`, `oct()` and `hex()` go the other way and return strings. To convert by hand: 0b1011 = 8 + 0 + 2 + 1 = 11; 0o17 = 1 x 8 + 7 = 15; 0x1F = 1 x 16 + 15 = 31.
```python
print(0b1011, 0o17, 0x1F)
print(bin(11), oct(15), hex(31))
```
Output:
```
11 15 31
0b1011 0o17 0x1f
```

#### 1.3e Variables and assignment
A **variable** is a name bound to a value by `=` (assignment, not equality). It is created the first time it is assigned; using it before that is a NameError. Python variables have no fixed type: the same name can later hold a value of a different type. Multiple assignment works: `a, b = 1, 2`, and `a, b = b, a` swaps.
```python
a, b = 1, 2
a, b = b, a
print(a, b)
a = "now a string"
print(a)
```
Output:
```
2 1
now a string
```

#### 1.3f Variable naming rules and conventions
**Naming rules** (breaking them is a SyntaxError): letters, digits and underscores only; must not start with a digit; must not be a keyword; case matters (`Total` and `total` are different). So `_count`, `total2`, `MAX_SIZE` are legal; `2total`, `my-var`, `for` are not.

#### 1.3g PEP 8 style recommendations
**PEP 8** is Python's style guide (a recommendation, not a rule the interpreter enforces). The exam expects: lower-case names with underscores for variables and functions (`max_speed`), UPPER_CASE for constants, CapWords for classes, four-space indentation, spaces around `=` and operators in statements, and no spaces just inside brackets.

## Explicitly not here
Operators and conversions between types are S03.
