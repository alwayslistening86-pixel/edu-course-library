# S11_Methods - Practice: Methods: accessors, mutators, overloading and static

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, or throws, say so and why.
```java
class M {
    static int twice(int n) { return n * 2; }
    static String twice(String s) { return s + s; }
}
// ---- main ----
System.out.println(M.twice(4) + M.twice("ab"));
```
2. Write a class Thermostat with a private int target, a getter, and a setter that ignores values outside 10 to 30. Show it rejecting 35.

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
8abab
```
2. The tutor runs or reads the learner's answer and checks: private field; getTarget(); setTarget(int) with the 10..30 check; demo shows the value unchanged after setTarget(35).

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
