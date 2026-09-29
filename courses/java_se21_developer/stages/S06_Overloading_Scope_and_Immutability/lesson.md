# S06_Overloading_Scope_and_Immutability - Lesson: Overloading and varargs, scope, encapsulation, immutability and var

## Goal
The learner resolves overloaded calls (exact, widening, boxing, varargs), reasons about scope and shadowing, designs genuinely immutable classes, and knows exactly where var is and isn't allowed.

## Syllabus items taught here
- 3.3 - Implement overloaded methods, including var-arg methods
- 3.4 - Understand variable scopes, apply encapsulation, create immutable objects, and use local variable type inference

## How to teach this
Ask which overload `f(5)` picks when only `f(long)`, `f(Integer)` and `f(int...)` exist, and why. Have the learner predict the result of every example before running it, and compile and run code for real on a JDK 21 (the answer keys were produced on JDK 21). The real exam's code-reading assumptions (missing imports exist, fragments have supporting code) apply to every item here too.

#### 3.3 Implement overloaded methods, including var-arg methods
**Overload resolution** happens at compile time, in phases: (1) exact match or primitive widening, with no boxing or varargs; (2) boxing and unboxing allowed; (3) varargs allowed. The most specific method within the first successful phase wins; if two are equally specific, the call is **ambiguous** (compile error). Widening then boxing is allowed (`int` to `long`? no boxing needed); boxing then widening only to a supertype (`int` to `Integer` to `Object`/`Number`), never `int` to `Long`. Overloads differ in parameter types; return type and parameter names don't count.
```java
class Pick {
    static String f(long x) { return "long"; }
    static String f(Integer x) { return "Integer"; }
    static String f(Object x) { return "Object"; }
    static String f(int... x) { return "varargs"; }
    static String g(Object o) { return "Object"; }
    static String g(String s) { return "String"; }
    static String h(Long x) { return "Long"; }
    static String h(Number n) { return "Number"; }
}
// ---- main ----
System.out.println(Pick.f(5) + " " + Pick.f(Integer.valueOf(5)) + " " + Pick.f("s") + " " + Pick.f() + " " + Pick.f(1, 2) + " " + Pick.g(null) + " " + Pick.h(5));
```
Output:
```
long Integer Object varargs varargs String Number
```
**Varargs** (`Type... name`): must be the last parameter, at most one per method, and is an array inside the method. You may pass zero or more arguments, or an array. Passing `null` passes a null array.
```java
class V {
    static int count(String label, int... nums) { return nums == null ? -1 : nums.length; }
}
// ---- main ----
System.out.println(V.count("a") + " " + V.count("b", 1, 2, 3) + " " + V.count("c", new int[]{4, 5}) + " " + V.count("d", (int[]) null));
```
Output:
```
0 3 2 -1
```
```java
class Bad {
    static void f(int... a, String s) { }
}
// ---- main ----
System.out.println("x");
```
Output:
```
(does not compile: varargs parameter must be the last parameter)
```

#### 3.4 Understand variable scopes, apply encapsulation, create immutable objects, and use local variable type inference
**Scope:** a local variable is visible from its declaration to the end of its block; a loop variable to the end of the loop; a parameter throughout the method. You can't redeclare a local in an enclosing local's scope (unlike fields, which locals may shadow). Lambdas and local/anonymous classes may use locals only if they are **effectively final** (never reassigned).
```java
int n = 1;
for (int i = 0; i < 2; i++) { int t = i * 10; n += t; }
int i = 99;
Runnable r = () -> System.out.println("captured " + i);
r.run();
System.out.println(n);
```
Output:
```
captured 99
11
```
```java
int count = 0;
Runnable r = () -> System.out.println(count);
count++;
```
Output:
```
(does not compile: local variables referenced from a lambda expression must be final or effectively final)
```
**Encapsulation:** private fields, public methods that enforce invariants. **Immutable class recipe:** make the class `final` (or give it private constructors), all fields `private final`, no setters, and make **defensive copies** of mutable inputs (in the constructor) and outputs (in getters). Otherwise a caller keeps a reference and can mutate your 'immutable' object. `List.copyOf` and `List.of` give unmodifiable lists.
```java
final class Team {
    private final String name;
    private final List<String> members;
    Team(String name, List<String> members) { this.name = name; this.members = List.copyOf(members); }
    List<String> members() { return members; }
    Team withMember(String m) { List<String> l = new ArrayList<>(members); l.add(m); return new Team(name, l); }
}
record Leaky(List<String> items) { }
// ---- main ----
List<String> src = new ArrayList<>(List.of("ann"));
Team t = new Team("red", src);
Leaky k = new Leaky(src);
src.add("bob");
Team t2 = t.withMember("cy");
System.out.println(t.members() + " " + t2.members() + " " + k.items());
t.members().add("dan");
```
Output:
```
[ann] [ann, cy] [ann, bob]
(throws UnsupportedOperationException)
```
**Local variable type inference (`var`):** allowed for local variables with an initialiser, enhanced-for and basic-for variables, try-with-resources resources, and lambda parameters (all or none of them). Not allowed for fields, method parameters or return types, without an initialiser, with a `null` initialiser, with an array initialiser `{...}`, or in a compound declaration (`var a = 1, b = 2;`). The inferred type is fixed at compile time. `var` is a reserved type name, not a keyword, so `var var = 1;` compiles.
```java
var list = new ArrayList<String>();
list.add("x");
var num = 10;
var big = 10L;
var var = "legal";
for (var s : list) System.out.print(s + " ");
java.util.function.BiFunction<Integer, Integer, Integer> add = (var a, var b) -> a + b;
System.out.println(((Object) num).getClass().getSimpleName() + " " + ((Object) big).getClass().getSimpleName() + " " + var + " " + add.apply(2, 3));
```
Output:
```
x Integer Long legal 5
```
```java
var nothing = null;
```
Output:
```
(does not compile: cannot infer type for local variable nothing)
```
```java
var x = 1;
x = "text";
```
Output:
```
(does not compile: incompatible types: String cannot be converted to int)
```

## Explicitly not here
Inheritance and overriding are S07.
