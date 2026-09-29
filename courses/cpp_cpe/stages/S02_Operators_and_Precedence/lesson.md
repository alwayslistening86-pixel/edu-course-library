# S02_Operators_and_Precedence - Lesson: Operators, precedence and short-circuiting

## Goal
The learner predicts the value of any expression built from the syllabus operators, including precedence, associativity, integer arithmetic and short-circuiting.

## Syllabus items taught here
- 1.4 - Arithmetic, relational, logical, bitwise and assignment operators
- 1.5 - Operator precedence and associativity, and their effect on expressions
- 1.6 - Short-circuit evaluation in control expressions

## How to teach this
Ask what `5 / 2 * 2.0` and `5 / 2.0 * 2` each give. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 1.4 Arithmetic, relational, logical, bitwise and assignment operators
Arithmetic `+ - * / %` (integer `/` truncates towards zero; `%` needs integers). Relational `== != < > <= >=` give `bool`. Logical `! && ||`. Bitwise `~ & | ^ << >>`. Assignment `=` and compound forms `+= -= *= /= %= &= |= ^= <<= >>=`. Increment and decrement: prefix `++x` changes x and then yields it; postfix `x++` yields the old value.
```cpp
int a = 7, b = 2;
cout << a / b << " " << a % b << " " << -7 / 2 << " " << -7 % 2 << endl;
cout << (a & b) << " " << (a | b) << " " << (a ^ b) << " " << (a << 2) << " " << (a >> 1) << " " << (~0) << endl;
int x = 5;
int y = x++ + ++x;
a += 3; a *= 2;
cout << a << " " << x << " " << y << endl;
```
Output:
```
3 1 -3 -1
2 7 5 28 3 -1
20 7 12
```

#### 1.5 Operator precedence and associativity, and their effect on expressions
Precedence, high to low (simplified): postfix `++ --`, calls and indexing; prefix `++ -- ! ~` and unary `-`; `* / %`; `+ -`; `<< >>`; `< <= > >=`; `== !=`; `&`; `^`; `|`; `&&`; `||`; `?:`; assignment. Binary operators are **left-associative**, except assignment and `?:`, which are right-associative. Classic trap: `a & b == c` means `a & (b == c)`. Mixed types are promoted before the operation (int to double).
```cpp
int a = 6, b = 4;
cout << 2 + 3 * 4 << " " << (2 + 3) * 4 << " " << 20 / 4 / 2 << " " << (a & b == 4) << " " << ((a & b) == 4) << endl;
int p, q;
p = q = 3;
cout << p + q << " " << 5 / 2 * 2.0 << " " << 5 / 2.0 * 2 << endl;
```
Output:
```
14 20 2 0 1
6 4 5
```

#### 1.6 Short-circuit evaluation in control expressions
`&&` stops at the first false operand, and `||` at the first true one; the right-hand side is then **not evaluated at all**. That's used for guards such as `p != nullptr && p->x > 0`, and it means side effects on the right may never happen.
```cpp
int calls = 0;
auto check = [&](bool v) { calls++; return v; };
bool r1 = check(false) && check(true);
bool r2 = check(true) || check(false);
int *p = nullptr;
bool safe = (p != nullptr) && (*p > 0);
cout << r1 << r2 << safe << " calls=" << calls << endl;
```
Output:
```
010 calls=2
```

## Explicitly not here
Stream formatting is S03.
