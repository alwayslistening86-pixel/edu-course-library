# S02_Types_Literals_Conversions_Modifiers - Lesson: Types, literals, conversions and modifiers

## Goal
The learner knows the built-in types, their typical ranges and literal forms, predicts implicit conversions and explicit casts, and applies signed, unsigned, static and const.

## Syllabus items taught here
- 1.4 - Predefined types, their ranges and representations
- 1.5 - Literals: decimal, octal, hexadecimal, binary, floating-point, char and bool
- 1.8 - Type conversion, casting, promotion and sizeof
- 1.9 - Declaration modifiers: signed, unsigned, static and const

## How to teach this
Ask what `unsigned u = -1;` stores. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 1.4 Predefined types, their ranges and representations
Integer types, in non-decreasing size: `char`, `short`, `int`, `long`, `long long`, each signed or unsigned (typically 1, 2, 4, 8, 8 bytes on 64-bit Linux). Floating types: `float`, `double`, `long double`. `bool`. Signed integers use two's complement (C++20 guarantees it; universal in practice). `<climits>` and `numeric_limits<T>` give the ranges.
```cpp
#include <climits>
#include <limits>
// ---- main ----
    cout << sizeof(short) << sizeof(int) << sizeof(long long) << sizeof(double) << " " << INT_MAX << " " << INT_MIN << endl;
    cout << numeric_limits<unsigned char>::max() + 0 << " " << numeric_limits<short>::min() << endl;
```
Output:
```
2488 2147483647 -2147483648
255 -32768
```

#### 1.5 Literals: decimal, octal, hexadecimal, binary, floating-point, char and bool
Integer literals: decimal `42`, octal `052`, hexadecimal `0x2A`, binary `0b101010`, with suffixes `u`, `l`, `ll`. Floating: `3.14`, `3.14f`, `1e-3`, `.5`. Char: `'A'`, `'\n'`, `'\x41'`, `'\101'` (octal). Bool: `true` and `false`, which convert to 1 and 0.
```cpp
cout << 052 << " " << 0x2A << " " << 0b101010 << " " << 1e2 << " " << '\101' << '\x42' << " " << true + true << endl;
```
Output:
```
42 42 42 100 AB 2
```

#### 1.8 Type conversion, casting, promotion and sizeof
**Promotion**: `char` and `short` become `int` in arithmetic; with mixed int and double the int converts to double. Signed and unsigned mixed: the signed value converts to **unsigned**, a classic trap (`-1 < 1u` is false). Conversions to a narrower type truncate. **Casts**: `static_cast<T>(v)` for ordinary conversions; the C-style `(T)v` also works but is less explicit. `sizeof` reports a type's or object's size in bytes, at compile time.
```cpp
char c = 'a';
cout << sizeof(c + 1) << " " << (-1 < 1u) << " " << static_cast<int>(3.99) << " " << (double)7 / 2 << " " << sizeof(int[10]) << endl;
unsigned u = -1;
cout << u << " " << static_cast<char>(98) << endl;
```
Output:
```
4 0 3 3.5 40
4294967295 b
```

#### 1.9 Declaration modifiers: signed, unsigned, static and const
`signed` and `unsigned` choose the integer representation (unsigned arithmetic wraps around modulo 2^n). `const` makes a variable read-only (it must be initialised). `static` on a local variable makes it keep its value between calls, initialised once; on a global it restricts visibility to the file. (Static class members are covered in S09.)
```cpp
int counter() { static int n = 0; return ++n; }
// ---- main ----
    const int LIMIT = 3;
    unsigned char uc = 250;
    uc += 10;
    counter(); counter();
    cout << LIMIT << " " << +uc << " " << counter() << endl;
```
Output:
```
3 4 3
```

## Explicitly not here
Strings and aggregates are S03.
