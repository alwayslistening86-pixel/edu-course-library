# S10_Classes_and_Constructors - Practice: Classes, objects and constructors

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, or throws, say so and why.
```java
class Dot {
    int x;
    Dot() { x = 1; }
    Dot(int x) { this.x = x * 2; }
}
// ---- main ----
System.out.println(new Dot().x + new Dot(4).x);
```
2. Which are local variables? Choose every correct option.
   A. A variable declared inside a method
   B. A method parameter
   C. A static field
   D. An instance field

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
9
```
2. Correct: A, B (exactly these options, no others)

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
