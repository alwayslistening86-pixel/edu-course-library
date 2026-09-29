# S11_Methods - Test: Methods: accessors, mutators, overloading and static

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
class Calc {
    static int add(int a, int b) { return a + b; }
    static double add(double a, double b) { return a + b + 0.5; }
    static long add(long a, long b) { return a + b + 100; }
}
// ---- main ----
System.out.println(Calc.add(1, 2) + " " + Calc.add(1, 2.0) + " " + Calc.add(1L, 2));
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
class Swap {
    static void swap(int a, int b) { int t = a; a = b; b = t; }
    static void swap(int[] arr) { int t = arr[0]; arr[0] = arr[1]; arr[1] = t; }
}
// ---- main ----
int x = 1, y = 2;
int[] p = {1, 2};
Swap.swap(x, y);
Swap.swap(p);
System.out.println(x + "" + y + " " + p[0] + p[1]);
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
class Score {
    private int points;
    public int getPoints() { return points; }
    public void addPoints(int p) { if (p > 0) points += p; }
}
// ---- main ----
Score s = new Score();
s.addPoints(5); s.addPoints(-3); s.addPoints(10);
System.out.println(s.getPoints());
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
class Shape {
    int sides = 4;
    static int describe() { return this.sides; }
}
// ---- main ----
System.out.println(Shape.describe());
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
class Grade {
    static String of(int s) {
        if (s >= 50) return "pass";
    }
}
// ---- main ----
System.out.println(Grade.of(60));
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
class Tally {
    static int total;
    int mine;
    void add() { mine++; total++; }
}
// ---- main ----
Tally a = new Tally(), b = new Tally();
a.add(); a.add(); b.add();
System.out.println(a.mine + " " + b.mine + " " + Tally.total);
```
7. Which pairs of methods in one class are valid overloads of `int f(int x)`? Choose every correct option.
   A. `int f(double x)`
   B. `double f(int y)`
   C. `int f(int x, int y)`
   D. `void f(String s)`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
3 3.5 103
```
2. Actual result (from running it):
```
12 21
```
3. Actual result (from running it):
```
15
```
4. Actual result (from running it):
```
(does not compile: non-static variable this cannot be referenced from a static context)
```
5. Actual result (from running it):
```
(does not compile: missing return statement)
```
6. Actual result (from running it):
```
2 1 3
```
7. Correct: A, C, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S11_Methods` exactly. 7 items; a pass needs at least 5 fully correct (65%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass. Every stage is now passed, so the cumulative exam becomes available.
