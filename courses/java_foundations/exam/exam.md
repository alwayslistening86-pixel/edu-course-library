# Java: 1Z0-811 Java Foundations (Oracle) - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` has a passed test.

## Format
60 items spread over all 13 areas roughly by objective count (about 2 per area-1 objective up to 8 for Classes and Constructors). Mix code-output, single-answer and multiple-select items in non-sequential order. 120 minutes, matching the real exam. No running of code until everything is answered.

## 8 ready-made items (write the rest fresh, never reusing stage-test items)
1. What is the output? If it does not compile, or throws, say so and why.
```java
int a = 9, b = 4;
System.out.println(a / b + " " + a % b + " " + (double) a / b + " " + a++ * --b + " " + a + b);
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
String s = "Foundations";
System.out.println(s.substring(0, 5).toUpperCase() + s.length() + s.indexOf("at") + s.charAt(4));
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
int n = 4;
switch (n % 3) {
    case 0: System.out.print("zero ");
    case 1: System.out.print("one ");
    case 2: System.out.print("two "); break;
    default: System.out.print("none ");
}
System.out.println();
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
ArrayList<Integer> v = new ArrayList<>(List.of(5, 3, 8));
v.add(1, 7);
int total = 0;
for (int x : v) total += x;
System.out.println(v + " " + total + " " + v.get(v.size() - 1));
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
class Coin {
    static int made;
    int value;
    Coin() { this(1); }
    Coin(int v) { value = v; made++; }
}
// ---- main ----
Coin a = new Coin(), b = new Coin(5);
System.out.println(a.value + b.value + " " + Coin.made);
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
int count = 0;
int i = 10;
while (i > 0) { i -= 3; if (i % 2 == 0) continue; count++; }
System.out.println(i + " " + count);
```
7. What is the output? If it does not compile, or throws, say so and why.
```java
try {
    int[] a = {1, 2, 3};
    System.out.print(a[1] / (a[0] - 1));
} catch (ArithmeticException e) {
    System.out.print("A");
} catch (Exception e) {
    System.out.print("E");
}
System.out.println("!");
```
8. Which are true? Choose every correct option.
   A. java.lang is imported automatically
   B. String objects are immutable
   C. == compares the characters of two String objects
   D. Math.random() returns a double from 0.0 up to but not including 1.0

## Answer key for the ready-made items (tutor only)
1. Actual result (from running it):
```
2 1 2.25 27 103
```
2. Actual result (from running it):
```
FOUND115d
```
3. Actual result (from running it):
```
one two 
```
4. Actual result (from running it):
```
[5, 7, 3, 8] 23 8
```
5. Actual result (from running it):
```
6 2
```
6. Actual result (from running it):
```
-2 2
```
7. Actual result (from running it):
```
A!
```
8. Correct: A, B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `exam_rubric` exactly: at least 39 of 60 (65%) for a pass, and report the score per area.

## Outcome
- **Pass:** record `exam_status: "passed"`. The course is complete, and java_se21_developer unlocks.
- **Not yet:** leave `exam_status: "available"`, name the weakest areas, offer targeted review, and retry with a fresh paper.
