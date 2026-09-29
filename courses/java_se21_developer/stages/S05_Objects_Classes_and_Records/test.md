# S05_Objects_Classes_and_Records - Test: Objects, life-cycle, nested classes, classes and records

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
class A {
    static String log = "";
    static { log += "As "; }
    int x = init("Ax ");
    A() { log += "A() "; }
    static int init(String s) { log += s; return 1; }
}
class B extends A {
    static { log += "Bs "; }
    { log += "Bi "; }
    B() { super(); log += "B() "; }
}
// ---- main ----
new B();
System.out.println(A.log);
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
class Outer {
    int v = 1;
    class Inner { int v = 2; int get() { return v * 10 + Outer.this.v; } }
    static class Nest { int get() { return 3; } }
}
// ---- main ----
Outer o = new Outer();
o.v = 5;
Outer.Inner in = o.new Inner();
System.out.println(in.get() + " " + new Outer.Nest().get());
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
class Outer {
    class Inner { }
}
// ---- main ----
Outer.Inner in = new Outer.Inner();
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
record P(int x, int y) {
    P(int v) { this(v, v); }
    public int x() { return x * 100; }
}
// ---- main ----
P p = new P(2);
System.out.println(p + " " + p.x() + " " + p.equals(new P(2, 2)));
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
record R(int a) {
    R(int a) { if (a < 0) a = 0; }
}
// ---- main ----
System.out.println(new R(-5));
```
6. After the line marked X runs, which objects are eligible for garbage collection? `Object a = new Object(), b = new Object(), c = a; a = b; b = null; // X`  (choose one) Choose every correct option.
   A. `None`
   B. Only the object first assigned to a
   C. Only the object first assigned to b
   D. Both objects
7. Which are true of records? (choose three) Choose every correct option.
   A. They are implicitly final
   B. They may declare additional instance fields
   C. They may implement interfaces
   D. `Their accessor for component name is name()`
   E. They can extend an abstract class

## Answer key (for the tutor only)
1. Actual result (from running it):
```
As Bs Ax A() Bi B() 
```
2. Actual result (from running it):
```
25 3
```
3. Actual result (from running it):
```
(does not compile: an enclosing instance that contains Outer.Inner is required)
```
4. Actual result (from running it):
```
P[x=2, y=2] 200 true
```
5. Actual result (from running it):
```
(does not compile: variable a might not have been initialized)
```
6. Correct: A (exactly these options, no others)
7. Correct: A, C, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S05_Objects_Classes_and_Records` exactly. 7 items; a pass needs at least 5 fully correct (68%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S06_Overloading_Scope_and_Immutability.
