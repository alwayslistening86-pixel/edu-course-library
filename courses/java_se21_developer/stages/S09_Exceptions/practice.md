# S09_Exceptions - Practice: Exception handling

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, or throws, say so and why.
```java
class F {
    static String t() {
        try { throw new RuntimeException("x"); }
        catch (RuntimeException e) { return "catch"; }
        finally { System.out.print("finally "); }
    }
}
// ---- main ----
System.out.println(F.t());
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
class R implements AutoCloseable { String n; R(String n) { this.n = n; } public void close() { System.out.print("close " + n + " "); } }
// ---- main ----
try (R a = new R("a"); R b = new R("b")) { System.out.print("body "); }
finally { System.out.println("fin"); }
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
finally catch
```
2. Actual result (from running it):
```
body close b close a fin
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
