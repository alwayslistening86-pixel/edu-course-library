# S08_Interfaces_and_Enums - Lesson: Interfaces and enums

## Goal
The learner writes interfaces with abstract, default, static and private methods, resolves default-method conflicts, recognises functional interfaces, and builds enums with fields, constructors, methods and constant-specific bodies.

## Syllabus items taught here
- 3.6 - Create and use interfaces, identify functional interfaces, and use private, static and default interface methods
- 3.7 - Create and use enum types with fields, methods and constructors

## How to teach this
Ask what happens when a class implements two interfaces that both declare `default String hi()`. Have the learner predict the result of every example before running it, and compile and run code for real on a JDK 21 (the answer keys were produced on JDK 21). The real exam's code-reading assumptions (missing imports exist, fragments have supporting code) apply to every item here too.

#### 3.6 Create and use interfaces, identify functional interfaces, and use private, static and default interface methods
An **interface** declares abstract methods (implicitly `public abstract`), constants (implicitly `public static final`), `default` methods (with bodies; inherited and overridable), `static` methods (called only as `Iface.m()`, not inherited by implementers), and `private` / `private static` helper methods (Java 9+). A class `implements` any number of interfaces; an interface `extends` any number of interfaces. If two inherited defaults clash, the class must override and may call `A.super.hi()`. A class's own method (even inherited from a superclass) wins over an interface default.
```java
interface Greeter {
    String name();
    default String greet() { return prefix() + name(); }
    private String prefix() { return "Hi "; }
    static Greeter of(String n) { return () -> n; }
}
interface Polite {
    default String greet() { return "Good day"; }
}
class Both implements Greeter, Polite {
    public String name() { return "Bo"; }
    public String greet() { return Greeter.super.greet() + " / " + Polite.super.greet(); }
}
// ---- main ----
System.out.println(Greeter.of("Al").greet() + " | " + new Both().greet());
```
Output:
```
Hi Al | Hi Bo / Good day
```
```java
interface A { default String hi() { return "A"; } }
interface B { default String hi() { return "B"; } }
class AB implements A, B { }
// ---- main ----
System.out.println(new AB().hi());
```
Output:
```
(does not compile: types A and B are incompatible;)
```
A **functional interface** has exactly one abstract method (not counting public methods of `Object` such as `equals`, or default and static methods), so a lambda or method reference can implement it. `@FunctionalInterface` makes the compiler check this. Key built-ins in `java.util.function`: `Supplier<T>` get, `Consumer<T>` accept, `BiConsumer`, `Function<T,R>` apply, `BiFunction`, `UnaryOperator<T>`, `BinaryOperator<T>`, `Predicate<T>` test, `BiPredicate`, plus primitive forms such as `IntPredicate`, `ToIntFunction`, `IntUnaryOperator`. Also `Runnable`, `Callable` and `Comparator` (whose `equals` doesn't count).
```java
@FunctionalInterface
interface Check { boolean ok(String s); boolean equals(Object o); default Check not() { return s -> !ok(s); } }
// ---- main ----
Check empty = String::isEmpty;
Supplier<List<String>> mk = ArrayList::new;
Function<String, Integer> len = String::length;
UnaryOperator<String> up = String::toUpperCase;
BinaryOperator<Integer> mul = (a, b) -> a * b;
Predicate<String> longish = s -> s.length() > 3;
List<String> l = mk.get();
l.add("java");
System.out.println(empty.ok("") + " " + empty.not().ok("") + " " + len.andThen(x -> x * 10).apply("abc") + " " + up.apply("x") + " " + mul.apply(6, 7) + " " + longish.negate().or(s -> s.startsWith("j")).test("java") + " " + l);
```
Output:
```
true false 30 X 42 true [java]
```

#### 3.7 Create and use enum types with fields, methods and constructors
An **enum** is a class with a fixed set of instances. Constants come first (ending with `;` if more members follow); constructors are implicitly private and run once per constant when the enum is first used; enums can have fields, methods, abstract methods implemented per constant (constant-specific bodies), and can implement interfaces, but can't extend a class. Built-ins: `values()`, `valueOf("NAME")` (throws `IllegalArgumentException` if unknown), `name()`, `ordinal()`, `compareTo` (by ordinal). Enums work in switch (use bare constant names in the cases) and are exhaustive when all constants are covered. `==` is safe for enums.
```java
enum Planet {
    MERCURY(3.7), EARTH(9.8) { String describe() { return "home " + super.describe(); } }, MARS(3.7);
    private final double g;
    Planet(double g) { this.g = g; System.out.print("init " + name() + " "); }
    double weigh(double mass) { return Math.round(mass * g); }
    String describe() { return name().charAt(0) + name().substring(1).toLowerCase() + "(" + ordinal() + ")"; }
}
// ---- main ----
Planet p = Planet.valueOf("EARTH");
System.out.println();
System.out.println(p.weigh(10) + " " + p.describe() + " " + Planet.MARS.describe() + " " + Planet.values().length + " " + Planet.MARS.compareTo(Planet.MERCURY) + " " + (p == Planet.EARTH));
String zone = switch (p) { case MERCURY -> "hot"; case EARTH -> "fine"; case MARS -> "cold"; };
System.out.println(zone);
Planet.valueOf("Pluto");
```
Output:
```
init MERCURY init EARTH init MARS 
98.0 home Earth(1) Mars(2) 3 2 true
fine
(throws IllegalArgumentException: No enum constant Planet.Pluto)
```

## Explicitly not here
Generic interfaces and wildcards are S10; streams over these interfaces are S11.
