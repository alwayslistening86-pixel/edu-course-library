# S04_Operators - Test: Operators and precedence

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
System.out.println(5 + 3 * 2 - 8 / 3 % 2);
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
int i = 4;
int j = i++ + i++;
int k = --i - i--;
System.out.println(i + " " + j + " " + k);
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
int a = 5, b = 0;
boolean r = (b != 0) && (a / b > 1);
boolean s = (a > 3) || (a / b > 1);
System.out.println(r + " " + s);
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
int a = 5, b = 0;
boolean r = (a > 3) && (a / b > 1);
System.out.println(r);
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
int temp = 18;
String feel = temp > 25 ? "hot" : temp > 15 ? "mild" : "cold";
System.out.println(feel + " " + (temp % 2 == 0 ? 'E' : 'O'));
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
int x = 10;
x += x -= 3;
double d = 10;
d /= 4;
System.out.println(x + " " + d + " " + (7 != 7.0));
```
7. Which expressions are true? Choose every correct option.
   A. `10 / 4 == 2`
   B. `10 % 4 == 2`
   C. `-10 % 4 == 2`
   D. `10.0 / 4 == 2.5`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
11
```
2. Actual result (from running it):
```
4 9 0
```
3. Actual result (from running it):
```
false true
```
4. Actual result (from running it):
```
(throws ArithmeticException: / by zero)
```
5. Actual result (from running it):
```
mild E
```
6. Actual result (from running it):
```
17 2.5 false
```
7. Correct: A, B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S04_Operators` exactly. 7 items; a pass needs at least 5 fully correct (65%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S05_String_Random_and_Math.
