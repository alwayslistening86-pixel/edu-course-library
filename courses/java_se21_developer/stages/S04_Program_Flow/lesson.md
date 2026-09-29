# S04_Program_Flow - Lesson: Program flow: if, switch statements and expressions, loops

## Goal
The learner writes and reads if/else, switch statements and switch expressions (arrow and colon forms, yield, exhaustiveness), all loop forms, and labelled break/continue.

## Syllabus items taught here
- 2.1 - Create program flow control constructs, including if/else, switch statements and expressions, loops, and break and continue

## How to teach this
Ask what a switch *expression* must do that a switch *statement* need not, then show one that won't compile because it isn't exhaustive. Have the learner predict the result of every example before running it, and compile and run code for real on a JDK 21 (the answer keys were produced on JDK 21). The real exam's code-reading assumptions (missing imports exist, fragments have supporting code) apply to every item here too.

#### 2.1 Create program flow control constructs, including if/else, switch statements and expressions, loops, and break and continue
**Switch statements** (`case X:` with fall-through, or `case X ->` without) can switch on `int` and smaller, their wrappers, `char`, `String`, enums and, with patterns, any reference type; not `long`, `float`, `double` or `boolean`. Case constants must be compile-time constants; `case 1, 2 ->` lists several. **Switch expressions** yield a value: each arrow either gives an expression, a block that ends in `yield`, or throws; they must be **exhaustive** (cover every value, usually via `default`, or all enum constants).
```java
enum Size { S, M, L }
// ---- main ----
int day = 6;
String kind = switch (day) {
    case 1, 2, 3, 4, 5 -> "weekday";
    case 6, 7 -> {
        String k = "weekend";
        yield k.toUpperCase();
    }
    default -> throw new IllegalArgumentException("bad day " + day);
};
Size s = Size.M;
int price = switch (s) { case S -> 5; case M -> 7; case L -> 9; };
int legacy = switch (day) {
    case 6:
    case 7:
        yield 1;
    default:
        yield 0;
};
System.out.println(kind + " " + price + " " + legacy);
switch (day) {
    case 5: System.out.print("five ");
    case 6: System.out.print("six ");
    case 7: System.out.print("seven ");
    default: System.out.print("other ");
}
System.out.println();
```
Output:
```
WEEKEND 7 1
six seven other 
```
A switch expression that doesn't cover every case doesn't compile:
```java
int n = 3;
String r = switch (n) {
    case 1 -> "one";
    case 2 -> "two";
};
System.out.println(r);
```
Output:
```
(does not compile: the switch expression does not cover all possible input values)
```
**Loops:** `for` (any part optional: `for (;;)` is infinite), enhanced `for` (arrays and `Iterable`s; the loop variable is a copy), `while`, `do/while` (runs at least once). A label on a loop lets `break label` or `continue label` target it. Unreachable statements (code after an unconditional `break`, `continue`, `return` or `throw`, or after `while (true)` with no break) are compile errors.
```java
int total = 0;
outer:
for (int i = 0; i < 4; i++) {
    for (int j = 0; j < 4; j++) {
        if (j == i) continue outer;
        if (i + j > 4) break outer;
        total += 10 * i + j;
    }
}
int k = 10;
do k -= 3; while (k > 0);
int[] arr = {1, 2, 3};
for (int x : arr) x *= 10;
for (int a = 0, b = 10; a < b; a += 3, b -= 3) System.out.print(a + ":" + b + " ");
System.out.println(total + " " + k + " " + Arrays.toString(arr));
```
Output:
```
0:10 3:7 112 -2 [1, 2, 3]
```
```java
int x = 0;
while (true) { x++; }
System.out.println(x);
```
Output:
```
(does not compile: unreachable statement)
```
**if/else:** the condition must be `boolean` (no int truthiness); an `else` binds to the nearest `if`; `if (b = true)` compiles because assignment yields a boolean.
```java
boolean flag = false;
if (flag = true) System.out.print("assigned ");
int v = 5;
if (v > 1) if (v > 10) System.out.print("big"); else System.out.print("medium");
System.out.println();
```
Output:
```
assigned medium
```

## Explicitly not here
Pattern matching in switch (type patterns, record patterns, guards) is S07.
