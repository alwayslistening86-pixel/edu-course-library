# S06_Decision_Statements - Test: Decision statements and comparing values

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
int n = 15;
if (n % 3 == 0 && n % 5 == 0) System.out.println("FizzBuzz");
else if (n % 3 == 0) System.out.println("Fizz");
else if (n % 5 == 0) System.out.println("Buzz");
else System.out.println(n);
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
int a = 5, b = 10;
if (a > b)
    if (a > 0) System.out.println("x");
else
    System.out.println("y");
System.out.println("z");
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
char grade = 'B';
switch (grade) {
    default: System.out.print("?");
    case 'A': System.out.print("A");
    case 'B': System.out.print("B");
    case 'C': System.out.print("C"); break;
    case 'D': System.out.print("D");
}
System.out.println();
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
long code = 2;
switch (code) {
    case 1: System.out.println("one"); break;
    case 2: System.out.println("two"); break;
}
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
System.out.println("dog".compareTo("cat") > 0);
System.out.println("Dog".compareTo("dog") < 0);
System.out.println("app".compareTo("apple"));
System.out.println("HELLO".equalsIgnoreCase("hello"));
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
String s = "tea";
String t = "te";
t = t + "a";
System.out.println((s == t) + " " + s.equals(t) + " " + (s.length() == t.length()));
```
7. Which types can a switch statement's expression have in this course's syntax? Choose every correct option.
   A. `int`
   B. `String`
   C. `double`
   D. `char`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
FizzBuzz
```
2. Actual result (from running it):
```
z
```
3. Actual result (from running it):
```
BC
```
4. Actual result (from running it):
```
(does not compile: selector type long is not allowed)
```
5. Actual result (from running it):
```
true
true
-2
true
```
6. Actual result (from running it):
```
false true true
```
7. Correct: A, B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S06_Decision_Statements` exactly. 7 items; a pass needs at least 5 fully correct (65%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S07_Loops.
