# S01_Primitives_Wrappers_and_Math - Practice: Primitives, wrappers, Math, conversions and casting

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, or throws, say so and why.
```java
short s = 10;
s = s * 2;
System.out.println(s);
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
Integer x = 1000, y = 1000;
int z = 1000;
System.out.println((x == y) + " " + (x == z) + " " + x.equals(z));
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
(does not compile: incompatible types: possible lossy conversion from int to short)
```
2. Actual result (from running it):
```
false true true
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
