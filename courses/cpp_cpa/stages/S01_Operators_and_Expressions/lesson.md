# S01_Operators_and_Expressions - Lesson: Operators and expressions

## Goal
The learner classifies operators by arity, predicts precedence and associativity, and evaluates expressions using every operator family, including ?:.

## Syllabus items taught here
- 1.1 - Unary, binary and ternary operators; precedence and associativity
- 1.2 - Arithmetic, relational, logical, bitwise and assignment operators
- 1.3 - The conditional operator ?:

## How to teach this
Ask how many operands `?:` has, and what `a = b = c` does. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 1.1 Unary, binary and ternary operators; precedence and associativity
**Unary** operators take one operand (`-x`, `!b`, `~x`, `++i`, `*p`, `&v`, `sizeof x`); **binary** operators take two (`a + b`); the **ternary** `?:` takes three. Postfix operators bind tightest, then prefix and unary, then `* / %`, `+ -`, shifts, relational, equality, `&`, `^`, `|`, `&&`, `||`, `?:`, and assignment. Assignment and `?:` are right-associative; the other binary operators are left-associative.
```cpp
int a, b, c = 4;
a = b = c;
cout << a << b << " " << -2 * -3 << " " << 16 / 4 / 2 << " " << (1 + 2 << 1) << endl;
```
Output:
```
44 6 2 6
```

#### 1.2 Arithmetic, relational, logical, bitwise and assignment operators
Arithmetic `+ - * / %` (integer division truncates towards zero; the sign of `%` follows the dividend). Relational and equality operators yield bool. Logical `! && ||` short-circuit. Bitwise `~ & | ^ << >>` work on the integer's bits. Compound assignment (`+=`, `<<=`...) combines an operation with assignment.
```cpp
int x = 13;
cout << x / 4 << " " << x % 4 << " " << -x % 4 << " " << (x & 6) << " " << (x | 2) << " " << (x ^ x) << " " << (x << 1) << endl;
x >>= 2;
x |= 8;
cout << x << " " << (!x) << " " << (x > 5 && x < 20) << endl;
```
Output:
```
3 1 -1 4 15 0 26
11 0 1
```

#### 1.3 The conditional operator ?:
`cond ? a : b` evaluates cond, then **only one** of a or b. If both are lvalues of the same type, the result is an lvalue (so it can even be assigned to); otherwise both are converted to a common type, which affects the output.
```cpp
int a = 3, b = 7;
int m = a > b ? a : b;
(a < b ? a : b) = 0;
cout << m << " " << a << b << " " << (true ? 1 : 2.5) << endl;
```
Output:
```
7 07 1
```

## Explicitly not here
Types and literals are S02.
