# S05_Objects_Classes_and_Records - Lesson: Objects, life-cycle, nested classes, classes and records

## Goal
The learner creates objects of top-level, nested, local and anonymous classes, traces initialisation order through static and instance initialisers and constructors, writes records correctly, and reasons about garbage-collection eligibility.

## Syllabus items taught here
- 3.1 - Declare and instantiate Java objects, including nested class objects, and explain the object life-cycle: creation, reassigning references and garbage collection
- 3.2 - Create classes and records, and define and use instance and static fields and methods, constructors, and instance and static initializers

## How to teach this
Ask in what order a static initialiser, an instance initialiser, a field initialiser and a constructor run, then prove it. Have the learner predict the result of every example before running it, and compile and run code for real on a JDK 21 (the answer keys were produced on JDK 21). The real exam's code-reading assumptions (missing imports exist, fragments have supporting code) apply to every item here too.

#### 3.1 Declare and instantiate Java objects, including nested class objects, and explain the object life-cycle: creation, reassigning references and garbage collection
**Creating objects:** `new` allocates, runs initialisers and the constructor, and returns a reference. Variables hold references; assignment copies the reference. An object is **eligible for garbage collection** when no live thread can reach it through any chain of references (islands of objects that point only to each other are eligible). You can't force collection: `System.gc()` is only a request; `finalize` is deprecated for removal.
```java
class Node { Node next; String name; Node(String n) { name = n; } }
// ---- main ----
Node a = new Node("a"), b = new Node("b"), c = new Node("c");
a.next = b; b.next = c; c.next = a;
Node keep = b;
a = null; b = null; c = null;
System.out.println(keep.name + keep.next.name + keep.next.next.name);
keep = null;
System.out.println("all three are now eligible for GC");
```
Output:
```
bca
all three are now eligible for GC
```
**Nested classes:** a *static nested* class is created without an outer instance (`new Outer.Nested()`); an *inner* (non-static member) class needs one (`outer.new Inner()`) and can use the outer object's members (`Outer.this.x`); a *local* class is declared inside a method and can capture effectively final locals; an *anonymous* class declares and instantiates in one expression.
```java
class Outer {
    private int x = 10;
    static class Nested { int get() { return 1; } }
    class Inner {
        int x = 20;
        int sum(int x) { return x + this.x + Outer.this.x; }
    }
}
// ---- main ----
Outer o = new Outer();
Outer.Inner in = o.new Inner();
Outer.Nested ns = new Outer.Nested();
int base = 100;
class Local { int plus(int n) { return base + n; } }
Comparator<String> byLen = new Comparator<>() {
    public int compare(String p, String q) { return p.length() - q.length(); }
};
List<String> ws = new ArrayList<>(List.of("ccc", "a", "bb"));
ws.sort(byLen);
System.out.println(in.sum(1) + " " + ns.get() + " " + new Local().plus(5) + " " + ws);
```
Output:
```
31 1 105 [a, bb, ccc]
```

#### 3.2 Create classes and records, and define and use instance and static fields and methods, constructors, and instance and static initializers
**Initialisation order:** when a class is first used, its static field initialisers and `static { }` blocks run once, top to bottom (superclass first). For each `new`: the superclass constructor chain runs first; then this class's instance field initialisers and `{ }` instance blocks, top to bottom; then the rest of the constructor body. `this(...)` or `super(...)` must be the first statement in a constructor, and a constructor that calls `this(...)` doesn't run the initialisers twice.
```java
class Base {
    static { System.out.print("Bs "); }
    { System.out.print("Bi "); }
    Base() { System.out.print("Bc "); }
}
class Child extends Base {
    static int count;
    static { System.out.print("Cs "); count = 0; }
    int id = ++count;
    { System.out.print("Ci" + id + " "); }
    Child() { this("x"); System.out.print("C() "); }
    Child(String s) { System.out.print("C(" + s + ") "); }
}
// ---- main ----
new Child();
System.out.println();
new Child("y");
System.out.println("| " + Child.count);
```
Output:
```
Bs Cs Bi Bc Ci1 C(x) C() 
Bi Bc Ci2 C(y) | 2
```
**Static vs instance:** static members belong to the class; a static method can't use `this` or instance members directly. A static member can be reached through a reference (even `null`), though it's poor style.
```java
class Counter {
    static int total;
    int mine;
    void hit() { total++; mine++; }
    static String report() { return "total=" + total; }
}
// ---- main ----
Counter a = new Counter(), b = new Counter();
a.hit(); a.hit(); b.hit();
Counter nothing = null;
System.out.println(a.mine + " " + b.mine + " " + Counter.report() + " " + nothing.total);
```
Output:
```
2 1 total=3 3
```
**Records** (`record Point(int x, int y) {}`) are final, shallowly immutable data carriers. The compiler generates private final fields, a **canonical constructor**, accessors named after the components (`x()`, not `getX()`), and `equals`, `hashCode` and `toString`. You may add a **compact constructor** (no parameter list; validates or normalises the parameters before the fields are assigned), other constructors (which must call `this(...)`), static fields, and instance or static methods. Records can't declare instance fields, can't extend a class (they implicitly extend `Record`), but can implement interfaces.
```java
record Range(int lo, int hi) {
    Range {
        if (lo > hi) { int t = lo; lo = hi; hi = t; }
    }
    Range(int single) { this(single, single); }
    int length() { return hi - lo; }
    static Range empty() { return new Range(0); }
}
// ---- main ----
Range r = new Range(9, 3);
System.out.println(r + " " + r.lo() + " " + r.length() + " " + r.equals(new Range(3, 9)) + " " + Range.empty() + " " + (r.hashCode() == new Range(3, 9).hashCode()));
```
Output:
```
Range[lo=3, hi=9] 3 6 true Range[lo=0, hi=0] true
```
```java
record Temp(double c) {
    double f;
}
// ---- main ----
System.out.println(new Temp(1));
```
Output:
```
(does not compile: field declaration must be static)
```

## Explicitly not here
Inheritance with records and sealed types is S07; immutability in general is S06.
