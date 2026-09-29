# S04_Operators - Lesson: Operators and precedence

## Goal
The learner evaluates expressions using arithmetic, increment/decrement, relational, compound-assignment and conditional operators, and applies precedence rules.

## Syllabus items taught here
- 5.1 - Use basic arithmetic operators to manipulate data, including +, -, *, / and %
- 5.2 - Use the increment and decrement operators
- 5.3 - Use relational operators, including ==, !=, >, >=, < and <=
- 5.4 - Use arithmetic assignment operators
- 5.5 - Use conditional operators, including &&, || and ?
- 5.6 - Describe operator precedence and the use of parentheses

## How to teach this
Ask what `x++ + ++x` gives when x is 1, and have them trace it step by step before running it. Have the learner predict the output of every example before running it, and compile and run code for real (any JDK; the examples were run on JDK 21 but use only features the Foundations syllabus covers).

#### 5.1 Use basic arithmetic operators to manipulate data, including +, -, *, / and %
`+ - * /` and `%` (remainder). Integer `/` truncates towards zero; if either operand is floating-point the result is floating-point. `%` takes the sign of the left operand. Integer division by zero throws `ArithmeticException`; floating-point division by zero gives `Infinity` or `NaN`.
```java
System.out.println(17 / 5 + " " + 17 % 5 + " " + -17 % 5 + " " + 17.0 / 5 + " " + 5.5 % 2 + " " + 1.0 / 0);
```
Output:
```
3 2 -2 3.4 1.5 Infinity
```

#### 5.2 Use the increment and decrement operators
`++` and `--` add or subtract 1. **Prefix** (`++x`) changes first, then the new value is used; **postfix** (`x++`) uses the old value, then changes.
```java
int x = 5;
int a = x++;
int b = ++x;
int c = x--;
System.out.println(a + " " + b + " " + c + " " + x);
int y = 1;
int z = y++ + ++y;
System.out.println(y + " " + z);
```
Output:
```
5 7 7 6
3 4
```

#### 5.3 Use relational operators, including ==, !=, >, >=, < and <=
`== != > >= < <=` compare values and give a boolean. For primitives they compare values; numeric types are promoted first, so `5 == 5.0` is true. `=` is assignment, not comparison: `if (x = 5)` doesn't compile for an int x.
```java
int a = 5;
double b = 5.0;
char c = 'a';
System.out.println((a == b) + " " + (a != 6) + " " + (c > 90) + " " + (a >= 5) + " " + (a < 5));
```
Output:
```
true true true true false
```

#### 5.4 Use arithmetic assignment operators
`+= -= *= /= %=` combine an operation with assignment. They include an implicit cast back to the variable's type, so `int x = 5; x *= 1.5;` compiles and truncates (while `x = x * 1.5;` would not compile).
```java
int x = 10;
x += 5;
x -= 3;
x *= 2;
x /= 5;
x %= 3;
System.out.print(x + " ");
int y = 5;
y *= 1.5;
String s = "a";
s += 1 + 2;
System.out.println(y + " " + s);
```
Output:
```
1 7 a3
```

#### 5.5 Use conditional operators, including &&, || and ?
`&&` (and) and `||` (or) **short-circuit**: the right side is evaluated only if needed. `!` negates. The ternary `condition ? valueIfTrue : valueIfFalse` chooses one of two values.
```java
int n = 0;
boolean safe = n != 0 && 10 / n > 1;
int count = 0;
boolean r = true || ++count > 0;
String sign = n > 0 ? "positive" : n < 0 ? "negative" : "zero";
System.out.println(safe + " " + r + " " + count + " " + sign + " " + !safe);
```
Output:
```
false true 0 zero true
```

#### 5.6 Describe operator precedence and the use of parentheses
Precedence, highest first: postfix `x++ x--`; unary `++x --x + - !` and casts; `* / %`; `+ -`; relational `< > <= >=`; equality `== !=`; `&&`; `||`; `?:`; assignment `= += -=`.... Operators of equal precedence group left to right (assignment right to left). Parentheses override everything and make intent clear.
```java
int r1 = 2 + 3 * 4;
int r2 = (2 + 3) * 4;
int r3 = 20 - 6 / 2 * 3;
boolean r4 = 3 + 2 > 4 && 1 == 2 || true;
int a, b;
a = b = 7;
System.out.println(r1 + " " + r2 + " " + r3 + " " + r4 + " " + a + b);
```
Output:
```
14 20 11 true 77
```

## Explicitly not here
Comparing objects with == is S06.
