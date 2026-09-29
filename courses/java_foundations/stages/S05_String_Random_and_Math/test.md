# S05_String_Random_and_Math - Test: The String, Random and Math classes

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
String s = "Hello World";
String t = s.toLowerCase().replace("o", "0");
System.out.println(t + " " + s.indexOf("World") + " " + s.contains("world") + " " + s.substring(6).length());
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
String s = "abc";
System.out.println(s.charAt(3));
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
String s = " pad ";
s.trim();
System.out.println("[" + s + "]" + s.length() + "[" + s.trim() + "]");
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
System.out.print("a\tb\n");
System.out.printf("%d + %d = %d%n", 2, 3, 2 + 3);
System.out.println(String.format("%s|%5.2f|", "x", 3.14159) + "\\done");
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
System.out.println(Math.round(4.5) + " " + Math.round(4.49) + " " + Math.ceil(-1.5) + " " + Math.floor(1.9) + " " + Math.abs(-3.0) + " " + (int) Math.pow(3, 3));
```
6. Which expressions always produce a whole number from 5 to 10 inclusive? (r is a java.util.Random) Choose every correct option.
   A. `5 + r.nextInt(6)`
   B. `5 + r.nextInt(5)`
   C. `r.nextInt(6) + 5`
   D. `(int) (Math.random() * 6) + 5`
7. Which are true? Choose every correct option.
   A. Math methods are static, so no Math object is created
   B. new Random(7) produces the same sequence each time the program runs
   C. Math.sqrt returns an int
   D. String methods such as toUpperCase change the original string

## Answer key (for the tutor only)
1. Actual result (from running it):
```
hell0 w0rld 6 false 5
```
2. Actual result (from running it):
```
(throws StringIndexOutOfBoundsException: Index 3 out of bounds for length 3)
```
3. Actual result (from running it):
```
[ pad ]5[pad]
```
4. Actual result (from running it):
```
a	b
2 + 3 = 5
x| 3.14|\done
```
5. Actual result (from running it):
```
5 4 -1.0 1.0 3.0 27
```
6. Correct: A, C, D (exactly these options, no others)
7. Correct: A, B (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S05_String_Random_and_Math` exactly. 7 items; a pass needs at least 5 fully correct (65%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S06_Decision_Statements.
