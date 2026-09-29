# S03_Data_Types_and_Casting - Practice: Variables, data types, casting and String variables

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, or throws, say so and why.
```java
double d = 10 / 4;
int i = (int) 3.99;
System.out.println(d + " " + i + " " + (char) ('a' + 2));
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
final int X;
X = 5;
X = 6;
System.out.println(X);
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
2.0 3 c
```
2. Actual result (from running it):
```
(does not compile: variable X might already have been assigned)
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
