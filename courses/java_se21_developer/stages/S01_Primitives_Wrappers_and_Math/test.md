# S01_Primitives_Wrappers_and_Math - Test: Primitives, wrappers, Math, conversions and casting

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
int a = 5;
a = a++ + ++a * 2;
System.out.println(a);
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
long l = Integer.MAX_VALUE + 1;
long m = Integer.MAX_VALUE + 1L;
System.out.println(l + " " + m);
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
byte b = 127;
b++;
char c = 'x';
c += 2;
System.out.println(b + " " + c + " " + (int) 3.99e10 + " " + (float) 1 / 3);
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
System.out.println(Math.round(-3.5) + " " + Math.round(3.49f) + " " + Math.floorMod(-10, 4) + " " + (-10 % 4) + " " + Math.ceil(-0.5) + " " + Math.max(1, 2L));
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
Long total = 0L;
total += 5;
Double d = 3.0;
System.out.println(total.equals(5) + " " + total.equals(5L) + " " + d.equals(3.0) + " " + (0.1f == 0.1));
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
boolean a = false, b = true;
int i = 0;
if (a & (i++ > 0) | b && (++i > 1)) i += 10;
System.out.println(i);
```
7. Which assignments compile? (choose three) Choose every correct option.
   A. `byte b = 100;`
   B. `float f = 1.0;`
   C. `long n = 2147483648;`
   D. `char c = 65;`
   E. `int i = 'A' + 1;`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
19
```
2. Actual result (from running it):
```
-2147483648 2147483648
```
3. Actual result (from running it):
```
-128 z 2147483647 0.33333334
```
4. Actual result (from running it):
```
-3 3 2 -2 -0.0 2
```
5. Actual result (from running it):
```
false true true false
```
6. Actual result (from running it):
```
12
```
7. Correct: A, D, E (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S01_Primitives_Wrappers_and_Math` exactly. 7 items; a pass needs at least 5 fully correct (68%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S02_Strings_StringBuilder_Text_Blocks.
