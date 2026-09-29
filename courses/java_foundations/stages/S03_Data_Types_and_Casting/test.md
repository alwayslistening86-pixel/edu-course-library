# S03_Data_Types_and_Casting - Test: Variables, data types, casting and String variables

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
int a = 7, b = 2;
double r1 = a / b;
double r2 = (double) a / b;
double r3 = (double) (a / b);
System.out.println(r1 + " " + r2 + " " + r3);
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
long big = 100;
int small = big;
System.out.println(small);
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
char c = 'B';
int code = c + 1;
System.out.println(c + 1 + " " + (char) code + " " + c);
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
System.out.println("" + 2 + 3 + " " + (2 + 3) + " " + 2 + 3);
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
byte b = (byte) 200;
short s = (short) 70000;
System.out.println(b + " " + s + " " + (int) -2.7);
```
6. Which declarations compile? Choose every correct option.
   A. `float f = 2.5;`
   B. `long n = 5;`
   C. `char c = "x";`
   D. `double d = 'x';`
7. Which are true of a final local variable? Choose every correct option.
   A. It can be assigned exactly once
   B. It must be initialised on the same line it is declared
   C. Trying to assign it a second time is a compile error
   D. Its name must be in upper case

## Answer key (for the tutor only)
1. Actual result (from running it):
```
3.0 3.5 3.0
```
2. Actual result (from running it):
```
(does not compile: incompatible types: possible lossy conversion from long to int)
```
3. Actual result (from running it):
```
67 C B
```
4. Actual result (from running it):
```
23 5 23
```
5. Actual result (from running it):
```
-56 4464 -2
```
6. Correct: B, D (exactly these options, no others)
7. Correct: A, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S03_Data_Types_and_Casting` exactly. 7 items; a pass needs at least 5 fully correct (65%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S04_Operators.
