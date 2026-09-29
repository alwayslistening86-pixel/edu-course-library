# S02_Basic_Java_Elements - Test: Conventions, reserved words, comments, imports and java.lang

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. Which follow Java naming conventions? Choose every correct option.
   A. class ShoppingCart
   B. `int MaxValue = 3; (an ordinary variable)`
   C. `static final int MAX_VALUE = 3;`
   D. `void calculateTotal()`
2. Which cannot be used as identifiers? Choose every correct option.
   A. `goto`
   B. `String`
   C. `null`
   D. `main`
3. What is the output? If it does not compile, or throws, say so and why.
```java
int value = 10;
/* value = 20;
value = 30; */ value += 5; // value = 40;
System.out.println(value);
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
int new = 3;
System.out.println(new);
```
5. Which classes can be used without any import statement? Choose every correct option.
   A. `java.lang.Math`
   B. `java.util.ArrayList`
   C. `java.lang.String`
   D. `java.util.Random`
6. Which statements about `import java.util.*;` are true? Choose every correct option.
   A. It lets you use ArrayList by its short name
   B. It also imports classes in java.util.concurrent
   C. It must come after any package statement
   D. It copies the library code into your class file
7. What is the output? If it does not compile, or throws, say so and why.
```java
java.util.ArrayList<String> xs = new java.util.ArrayList<>();
xs.add("ok");
System.out.println(xs + " " + Integer.MAX_VALUE);
```

## Answer key (for the tutor only)
1. Correct: A, C, D (exactly these options, no others)
2. Correct: A, C (exactly these options, no others)
3. Actual result (from running it):
```
15
```
4. Actual result (from running it):
```
(does not compile: not a statement)
```
5. Correct: A, C (exactly these options, no others)
6. Correct: A, C (exactly these options, no others)
7. Actual result (from running it):
```
[ok] 2147483647
```

## Grading
Apply `rubric.json`'s `stage_rubrics.S02_Basic_Java_Elements` exactly. 7 items; a pass needs at least 5 fully correct (65%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S03_Data_Types_and_Casting.
