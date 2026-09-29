# S06_Overloading_Scope_and_Immutability - Test: Overloading and varargs, scope, encapsulation, immutability and var

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
class O {
    static String f(int... x) { return "varargs"; }
    static String f(Integer x) { return "Integer"; }
    static String f(long x) { return "long"; }
}
// ---- main ----
byte b = 1;
System.out.println(O.f(b) + " " + O.f(Integer.valueOf(1)) + " " + O.f(1, 2) + " " + O.f());
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
class O {
    static String g(Long x) { return "Long"; }
}
// ---- main ----
System.out.println(O.g(5));
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
class O {
    static String h(Integer a, long b) { return "A"; }
    static String h(long a, Integer b) { return "B"; }
}
// ---- main ----
System.out.println(O.h(1, 2));
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
int total = 0;
for (var i = 0; i < 3; i++) total += i;
var list = new ArrayList<>();
list.add("x"); list.add(1);
System.out.println(total + " " + list + " " + list.get(1).getClass().getSimpleName());
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
String label = "a";
List<String> out = new ArrayList<>();
for (String s : List.of("x", "y")) {
    label = label + s;
    out.add(label);
}
Runnable r = () -> System.out.println(out);
r.run();
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
final class Holder {
    private final int[] data;
    Holder(int[] d) { data = d; }
    int[] data() { return data; }
}
// ---- main ----
int[] src = {1, 2};
Holder h = new Holder(src);
src[0] = 50;
h.data()[1] = 60;
System.out.println(Arrays.toString(h.data()));
```
7. Where may var be used? (choose three) Choose every correct option.
   A. A local variable with an initializer
   B. An instance field
   C. The variable of an enhanced for loop
   D. A method parameter
   E. A try-with-resources resource

## Answer key (for the tutor only)
1. Actual result (from running it):
```
long Integer varargs varargs
```
2. Actual result (from running it):
```
(does not compile: incompatible types: int cannot be converted to Long)
```
3. Actual result (from running it):
```
(does not compile: reference to h is ambiguous)
```
4. Actual result (from running it):
```
3 [x, 1] Integer
```
5. Actual result (from running it):
```
[ax, axy]
```
6. Actual result (from running it):
```
[50, 60]
```
7. Correct: A, C, E (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S06_Overloading_Scope_and_Immutability` exactly. 7 items; a pass needs at least 5 fully correct (68%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S07_Inheritance_Polymorphism_Pattern_Matching.
