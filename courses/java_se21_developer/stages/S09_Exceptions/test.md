# S09_Exceptions - Test: Exception handling

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
class F {
    static int f() {
        int x = 10;
        try { x = 20; throw new Exception(); }
        catch (Exception e) { x = 30; return x; }
        finally { x = 40; }
    }
}
// ---- main ----
System.out.println(F.f());
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
try {
    throw new java.io.FileNotFoundException("f");
} catch (java.io.IOException e) {
    System.out.println("io");
} catch (java.io.FileNotFoundException e) {
    System.out.println("fnf");
}
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
class F {
    static void go() {
        try { System.out.println("safe"); }
        catch (java.io.IOException e) { }
    }
}
// ---- main ----
F.go();
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
class Res implements AutoCloseable {
    public void close() { throw new IllegalStateException("close"); }
}
// ---- main ----
try (Res r = new Res()) {
    throw new IllegalArgumentException("body");
} catch (RuntimeException e) {
    System.out.println(e.getMessage() + " " + e.getSuppressed().length + " " + e.getSuppressed()[0].getMessage());
}
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
class Res implements AutoCloseable { public void close() { } }
// ---- main ----
try (Res r = new Res()) {
    r = null;
}
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
class P { void run() throws java.io.IOException { } }
class C extends P { @Override void run() throws Exception { } }
// ---- main ----
System.out.println("ok");
```
7. Which are true? (choose two) Choose every correct option.
   A. In multi-catch, the exception variable is implicitly final
   B. Resources are closed after the catch block runs
   C. A custom checked exception extends RuntimeException
   D. An Error such as StackOverflowError is unchecked

## Answer key (for the tutor only)
1. Actual result (from running it):
```
30
```
2. Actual result (from running it):
```
(does not compile: exception FileNotFoundException has already been caught)
```
3. Actual result (from running it):
```
(does not compile: exception IOException is never thrown in body of corresponding try statement)
```
4. Actual result (from running it):
```
body 1 close
```
5. Actual result (from running it):
```
(does not compile: auto-closeable resource r may not be assigned)
```
6. Actual result (from running it):
```
(does not compile: run() in C cannot override run() in P)
```
7. Correct: A, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S09_Exceptions` exactly. 7 items; a pass needs at least 5 fully correct (68%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S10_Collections_Generics_Annotations.
