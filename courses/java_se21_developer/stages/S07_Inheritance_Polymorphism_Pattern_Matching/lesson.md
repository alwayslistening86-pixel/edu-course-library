# S07_Inheritance_Polymorphism_Pattern_Matching - Lesson: Inheritance, sealed types, polymorphism and pattern matching

## Goal
The learner applies inheritance rules for classes, abstract classes, sealed hierarchies and records; overrides correctly (including Object's methods); distinguishes reference and object type; casts safely; and uses type and record patterns with instanceof and switch.

## Syllabus items taught here
- 3.5 - Implement inheritance with abstract and sealed types and records; override methods including Object's; polymorphism, object vs reference type, reference casting, instanceof, and pattern matching with instanceof and switch

## How to teach this
Ask which method runs for `Animal a = new Dog(); a.speak();` and which field `a.name` reads if both classes declare `name`. Have the learner predict the result of every example before running it, and compile and run code for real on a JDK 21 (the answer keys were produced on JDK 21). The real exam's code-reading assumptions (missing imports exist, fragments have supporting code) apply to every item here too.

#### 3.5 Implement inheritance with abstract and sealed types and records; override methods including Object's; polymorphism, object vs reference type, reference casting, instanceof, and pattern matching with instanceof and switch
**Inheritance and overriding.** A class extends one class (default `Object`). An override has the same signature; its return type is the same or a subtype (covariant); its access is the same or wider; it may not declare broader checked exceptions; and it can't override a `final` method. `static` methods are **hidden**, not overridden, and fields are hidden too: both are chosen by the **reference type**, while overridden instance methods are chosen by the **object type** at run time. `super.m()` calls the parent's version. Constructors aren't inherited; each starts with `super(...)` (implicitly `super()`, which must exist).
```java
class Animal {
    String name = "animal";
    static String kind() { return "Animal.kind"; }
    String speak() { return "..."; }
    Animal self() { return this; }
    public String toString() { return "I am " + speak(); }
}
class Dog extends Animal {
    String name = "dog";
    static String kind() { return "Dog.kind"; }
    @Override String speak() { return "Woof"; }
    @Override Dog self() { return this; }
}
// ---- main ----
Animal a = new Dog();
Dog d = (Dog) a;
System.out.println(a.name + " " + d.name + " " + a.speak() + " " + a.kind() + " " + d.kind() + " " + a + " " + d.self().name);
```
Output:
```
animal dog Woof Animal.kind Dog.kind I am Woof dog
```
```java
class P { protected void run() { } }
class C extends P { void run() { } }
// ---- main ----
System.out.println("x");
```
Output:
```
(does not compile: run() in C cannot override run() in P)
```
**Abstract classes** can't be instantiated and may have abstract methods (no body), which the first concrete subclass must implement. They can have constructors, fields and concrete methods. A method can't be both `abstract` and `final`, `private` or `static`.
```java
abstract class Shape {
    private final String label;
    Shape(String label) { this.label = label; }
    abstract double area();
    String describe() { return label + "=" + Math.round(area()); }
}
class Circle extends Shape {
    final double r;
    Circle(double r) { super("circle"); this.r = r; }
    double area() { return Math.PI * r * r; }
}
// ---- main ----
Shape s = new Circle(2);
System.out.println(s.describe());
```
Output:
```
circle=13
```
**Sealed types:** `sealed class/interface X permits A, B` limits the direct subtypes to those listed (which must be in the same module, or the same package in the unnamed module; the `permits` clause can be omitted if they're in the same file). Each permitted subtype must be `final`, `sealed` or `non-sealed`. Records are implicitly final, so they fit sealed interfaces well. A switch over a sealed type with a case for every permitted subtype is exhaustive without `default`.
```java
sealed interface Expr permits Num, Add, Neg { }
record Num(int v) implements Expr { }
record Add(Expr l, Expr r) implements Expr { }
non-sealed class Neg implements Expr { final Expr e; Neg(Expr e) { this.e = e; } }
class Eval {
    static int eval(Expr e) {
        return switch (e) {
            case Num n -> n.v();
            case Add(Expr l, Expr r) -> eval(l) + eval(r);
            case Neg n -> -eval(n.e);
        };
    }
}
// ---- main ----
Expr e = new Add(new Num(4), new Neg(new Add(new Num(1), new Num(2))));
System.out.println(Eval.eval(e));
```
Output:
```
1
```
```java
sealed class Vehicle permits Car { }
class Car extends Vehicle { }
// ---- main ----
System.out.println("x");
```
Output:
```
(does not compile: sealed, non-sealed or final modifiers expected)
```
**Object's methods:** override `equals(Object)` (reflexive, symmetric, transitive, consistent, `x.equals(null)` false) together with `hashCode` (equal objects must have equal hash codes), and `toString`. Writing `equals(Dog other)` **overloads** rather than overrides, a classic trap that `@Override` catches.
```java
class Pt {
    final int x, y;
    Pt(int x, int y) { this.x = x; this.y = y; }
    public boolean equals(Pt o) { return o != null && x == o.x && y == o.y; }
}
// ---- main ----
Pt a = new Pt(1, 2), b = new Pt(1, 2);
Object ob = b;
Set<Pt> set = new HashSet<>(List.of(a));
System.out.println(a.equals(b) + " " + a.equals(ob) + " " + set.contains(b));
```
Output:
```
true false false
```
**Casting and instanceof:** upcasting is implicit; downcasting needs a cast and throws `ClassCastException` at run time if the object isn't that type. A cast between unrelated class types (neither a subtype of the other) doesn't compile; casts to interfaces usually compile, since a subclass might implement them. **Pattern matching for instanceof** (`if (o instanceof String s)`) tests, casts and binds; the binding is in scope only where the match is definitely true (including after `&&`, or after an `if (!(o instanceof String s)) return;`).
```java
Object o = "hello";
if (o instanceof String s && s.length() > 3) System.out.print(s.toUpperCase() + " ");
if (!(o instanceof String t)) return;
System.out.print(t.length() + " ");
Object n = 42;
System.out.print((n instanceof Integer i ? i + 1 : 0) + " ");
Number num = Integer.valueOf(5);
Double dbl = (Double) num;
```
Output:
```
HELLO 5 43 
(throws ClassCastException: class java.lang.Integer cannot be cast to class java.lang.Double)
```
```java
String s = "text";
Integer i = (Integer) s;
```
Output:
```
(does not compile: incompatible types: String cannot be converted to Integer)
```
**Pattern matching in switch** (Java 21): case labels can be type patterns (`case Integer i`), record patterns (`case Point(int x, var y)`, nestable), guarded with `when`, and `case null`. Cases are checked top to bottom; a pattern that is **dominated** by an earlier one (a subtype after its supertype, or an unguarded pattern before the same type guarded) is a compile error. A pattern switch must be exhaustive; without `case null`, a null selector throws `NullPointerException`.
```java
record Point(int x, int y) { }
record Line(Point a, Point b) { }
class Desc {
    static String of(Object o) {
        return switch (o) {
            case null -> "null!";
            case Integer i when i > 100 -> "big int " + i;
            case Integer i -> "int " + i;
            case String s -> "string of " + s.length();
            case Line(Point(var x1, var y1), Point b) when x1 == 0 -> "line from y-axis at " + y1 + " to " + b;
            case Point(int x, int y) -> "point " + (x + y);
            default -> "other " + o.getClass().getSimpleName();
        };
    }
}
// ---- main ----
for (Object o : new Object[]{7, 700, "hey", new Point(2, 3), new Line(new Point(0, 5), new Point(1, 1)), 2.5, null})
    System.out.println(Desc.of(o));
```
Output:
```
int 7
big int 700
string of 3
point 5
line from y-axis at 5 to Point[x=1, y=1]
other Double
null!
```
```java
class D {
    static String of(Object o) {
        return switch (o) {
            case CharSequence cs -> "cs";
            case String s -> "s";
            default -> "x";
        };
    }
}
// ---- main ----
System.out.println(D.of("a"));
```
Output:
```
(does not compile: this case label is dominated by a preceding case label)
```

## Explicitly not here
Interfaces and enums are S08.
