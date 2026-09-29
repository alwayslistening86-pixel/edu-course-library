# S05_Objects_Classes_and_Records - Practice: Objects, life-cycle, nested classes, classes and records

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, or throws, say so and why.
```java
class Q {
    static { System.out.print("s "); }
    { System.out.print("i "); }
    Q() { System.out.print("c "); }
}
// ---- main ----
new Q(); new Q();
System.out.println();
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
record Money(String cur, long cents) {
    Money { if (cents < 0) throw new IllegalArgumentException("negative"); cur = cur.toUpperCase(); }
}
// ---- main ----
System.out.println(new Money("gbp", 250) + " " + new Money("gbp", 250).equals(new Money("GBP", 250)));
new Money("eur", -1);
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
s i c i c 
```
2. Actual result (from running it):
```
Money[cur=GBP, cents=250] true
(throws IllegalArgumentException: negative)
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
