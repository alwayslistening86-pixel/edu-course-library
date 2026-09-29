# S06_Overloading_Scope_and_Immutability - Practice: Overloading and varargs, scope, encapsulation, immutability and var

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, or throws, say so and why.
```java
class O {
    static String m(double d) { return "double"; }
    static String m(Object o) { return "Object"; }
}
// ---- main ----
System.out.println(O.m(1) + " " + O.m('c') + " " + O.m("s"));
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
var a = new int[]{1, 2};
var b = a;
b[0] = 9;
System.out.println(a[0]);
var c = {1, 2};
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
double double Object
```
2. Actual result (from running it):
```
(does not compile: cannot infer type for local variable c)
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
