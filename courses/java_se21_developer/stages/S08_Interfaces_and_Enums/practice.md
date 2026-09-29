# S08_Interfaces_and_Enums - Practice: Interfaces and enums

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, or throws, say so and why.
```java
interface Named { String name(); default String greet() { return "Hi " + name(); } }
record Person(String name) implements Named { }
// ---- main ----
System.out.println(new Person("Ann").greet());
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
enum Dir { N, E, S, W; Dir right() { return values()[(ordinal() + 1) % 4]; } }
// ---- main ----
System.out.println(Dir.W.right() + " " + Dir.valueOf("S").ordinal() + " " + Dir.N.compareTo(Dir.S));
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
Hi Ann
```
2. Actual result (from running it):
```
N 2 -2
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
