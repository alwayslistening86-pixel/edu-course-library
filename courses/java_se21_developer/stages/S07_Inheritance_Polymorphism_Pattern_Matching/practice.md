# S07_Inheritance_Polymorphism_Pattern_Matching - Practice: Inheritance, sealed types, polymorphism and pattern matching

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, or throws, say so and why.
```java
class A { String who() { return "A"; } String hi() { return "hi " + who(); } }
class B extends A { String who() { return "B"; } }
// ---- main ----
A a = new B();
System.out.println(a.hi() + " " + ((A) a).who());
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
Object o = 42;
String r = switch (o) {
    case Integer i when i > 50 -> "big";
    case Integer i -> "int " + (i + 1);
    default -> "other";
};
System.out.println(r);
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
hi B B
```
2. Actual result (from running it):
```
int 43
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
