# S07_Inheritance_Polymorphism_Pattern_Matching - Test: Inheritance, sealed types, polymorphism and pattern matching

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
class P { int v = 1; int get() { return v; } static String s() { return "P"; } }
class C extends P { int v = 2; int get() { return v; } static String s() { return "C"; } }
// ---- main ----
P p = new C();
System.out.println(p.v + " " + p.get() + " " + p.s() + " " + ((C) p).v);
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
class P { P(int x) { } }
class C extends P { C() { System.out.println("C"); } }
// ---- main ----
new C();
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
class P { Number val() { return 1; } }
class C extends P { Integer val() { return 2; } }
class D extends P { String val() { return "3"; } }
// ---- main ----
System.out.println(new C().val());
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
sealed interface Shape permits Sq, Circ { }
record Sq(double side) implements Shape { }
record Circ(double r) implements Shape { }
class Area {
    static double of(Shape s) {
        return switch (s) {
            case Sq q -> q.side() * q.side();
            case Circ(double r) when r == 0 -> 0;
            case Circ c -> 3 * c.r() * c.r();
        };
    }
}
// ---- main ----
System.out.println(Area.of(new Sq(3)) + " " + Area.of(new Circ(2)) + " " + Area.of(new Circ(0)));
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
Object o = List.of("a", "b");
if (o instanceof List<?> l && !l.isEmpty() && l.get(0) instanceof String s)
    System.out.println(s.toUpperCase() + l.size());
Object n = 3.5;
Integer i = (Integer) n;
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
record Box(Object content) { }
class Show {
    static String of(Object o) {
        return switch (o) {
            case Box(String s) -> "box of text " + s;
            case Box(Integer i) when i > 9 -> "box of big " + i;
            case Box(var x) -> "box of " + x;
            case null, default -> "not a box";
        };
    }
}
// ---- main ----
System.out.println(Show.of(new Box("hi")) + " | " + Show.of(new Box(12)) + " | " + Show.of(new Box(5)) + " | " + Show.of(null));
```
7. Which are true? (choose two) Choose every correct option.
   A. A permitted subclass of a sealed class must be final, sealed or non-sealed
   B. Static methods are chosen by the object type at run time
   C. Casting between unrelated classes (e.g. String to Integer) compiles but throws at run time
   D. An overriding method may not declare a broader checked exception

## Answer key (for the tutor only)
1. Actual result (from running it):
```
1 2 P 2
```
2. Actual result (from running it):
```
(does not compile: constructor P in class P cannot be applied to given types;)
```
3. Actual result (from running it):
```
(does not compile: val() in D cannot override val() in P)
```
4. Actual result (from running it):
```
9.0 12.0 0.0
```
5. Actual result (from running it):
```
A2
(throws ClassCastException: class java.lang.Double cannot be cast to class java.lang.Integer)
```
6. Actual result (from running it):
```
box of text hi | box of big 12 | box of 5 | not a box
```
7. Correct: A, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S07_Inheritance_Polymorphism_Pattern_Matching` exactly. 7 items; a pass needs at least 5 fully correct (68%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S08_Interfaces_and_Enums.
