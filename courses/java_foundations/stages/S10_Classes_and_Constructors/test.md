# S10_Classes_and_Constructors - Test: Classes, objects and constructors

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
class Ticket {
    static int issued = 0;
    int number;
    Ticket() { issued++; number = issued; }
}
// ---- main ----
Ticket a = new Ticket(), b = new Ticket(), c = new Ticket();
System.out.println(a.number + " " + c.number + " " + Ticket.issued + " " + b.issued);
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
class Box {
    int size;
    Box(int size) { size = size; }
}
// ---- main ----
System.out.println(new Box(5).size);
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
class Pen {
    String colour;
    Pen(String c) { colour = c; }
}
// ---- main ----
Pen p = new Pen();
System.out.println(p.colour);
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
class Pair {
    int a, b;
    Pair(int a) { this(a, 0); }
    Pair(int a, int b) { this.a = a; this.b = b; }
}
// ---- main ----
Pair p = new Pair(3);
Pair q = p;
q.b = 7;
System.out.println(p.a + " " + p.b + " " + (p == q));
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
class Secret {
    private int code = 42;
}
// ---- main ----
Secret s = new Secret();
System.out.println(s.code);
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
class Thing {
    void Thing() { System.out.print("method "); }
}
// ---- main ----
Thing t = new Thing();
t.Thing();
System.out.println("done");
```
7. Which are true of constructors? Choose every correct option.
   A. They have the same name as the class
   B. They declare a return type of void
   C. The compiler supplies a no-arg constructor only if the class declares none
   D. this(...) calling another constructor must be the first statement

## Answer key (for the tutor only)
1. Actual result (from running it):
```
1 3 3 3
```
2. Actual result (from running it):
```
0
```
3. Actual result (from running it):
```
(does not compile: constructor Pen in class Pen cannot be applied to given types;)
```
4. Actual result (from running it):
```
3 7 true
```
5. Actual result (from running it):
```
(does not compile: code has private access in Secret)
```
6. Actual result (from running it):
```
method done
```
7. Correct: A, C, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S10_Classes_and_Constructors` exactly. 7 items; a pass needs at least 5 fully correct (65%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S11_Methods.
