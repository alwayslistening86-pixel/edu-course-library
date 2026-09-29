# S08_Interfaces_and_Enums - Test: Interfaces and enums

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
interface I { static String s() { return "I.s"; } default String d() { return "I.d"; } }
class K implements I { }
// ---- main ----
K k = new K();
System.out.println(I.s() + " " + k.d());
System.out.println(K.s());
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
interface Walker { default String move() { return "walk"; } }
class Animal { public String move() { return "animal"; } }
class Dog extends Animal implements Walker { }
// ---- main ----
System.out.println(new Dog().move());
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
interface Calc { int apply(int x); default Calc twice() { return x -> apply(apply(x)); } }
// ---- main ----
Calc inc = x -> x + 3;
Calc sq = x -> x * x;
System.out.println(inc.twice().apply(1) + " " + sq.twice().apply(2));
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
enum Coin {
    PENNY(1), NICKEL(5), DIME(10) { int value() { return 11; } };
    private final int cents;
    Coin(int c) { cents = c; }
    int value() { return cents; }
}
// ---- main ----
int sum = 0;
for (Coin c : Coin.values()) sum += c.value();
System.out.println(sum + " " + Coin.DIME.getClass().equals(Coin.class) + " " + Coin.DIME.getDeclaringClass().getSimpleName());
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
enum Level { LOW, HIGH }
// ---- main ----
Level l = Level.HIGH;
switch (l) {
    case Level.LOW -> System.out.println("low");
    case HIGH -> System.out.println("high");
}
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
enum Size { S, M; Size() { System.out.print("new "); } }
// ---- main ----
System.out.print("start ");
Size a = Size.M;
Size b = Size.S;
System.out.println(a.name() + b);
```
7. Which are functional interfaces? (choose three) Choose every correct option.
   A. `interface A { void run(); }`
   B. `interface B { void x(); void y(); }`
   C. interface C { boolean test(String s); boolean equals(Object o); }
   D. `interface D { default void d() { } }`
   E. interface E extends A { static void s() { } }

## Answer key (for the tutor only)
1. Actual result (from running it):
```
(does not compile: cannot find symbol)
```
2. Actual result (from running it):
```
animal
```
3. Actual result (from running it):
```
7 16
```
4. Actual result (from running it):
```
17 false Coin
```
5. Actual result (from running it):
```
high
```
6. Actual result (from running it):
```
start new new MS
```
7. Correct: A, C, E (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S08_Interfaces_and_Enums` exactly. 7 items; a pass needs at least 5 fully correct (68%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S09_Exceptions.
