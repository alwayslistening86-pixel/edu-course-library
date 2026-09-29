# S09_OOP_Principles_and_Class_Definitions - Test: OOP principles and class definitions

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
struct S { int a = 1; };
class K { int a = 1; };
// ---- main ----
    S s;
    cout << s.a << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
class Counter {
    int n = 0;
public:
    Counter &add(int k) { n += k; return *this; }
    int get() const { return n; }
};
// ---- main ----
    Counter c;
    cout << c.add(2).add(3).get() << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
class P {
    int x;
public:
    void set(int x) { this->x = x; }
    int get() { return x; }
};
// ---- main ----
    P p;
    p.set(7);
    cout << p.get() << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
class U {
public:
    static int made;
    U() { made++; }
};
int U::made = 0;
// ---- main ----
    U a, b, c;
    cout << U::made << " " << a.made << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
class R {
    int v = 2;
public:
    int get() const { return v; }
    void set(int n) { v = n; }
};
// ---- main ----
    const R r;
    r.set(5);
```
6. Which OOP principle is about hiding an object's internal data behind a public interface? Choose every correct option.
   A. `Encapsulation`
   B. `Inheritance`
   C. `Polymorphism`
   D. `Recursion`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
1
```
2. Actual result (from running it):
```
5
```
3. Actual result (from running it):
```
7
```
4. Actual result (from running it):
```
3 3
```
5. Actual result (from running it):
```
(does not compile: passing ‘const R’ as ‘this’ argument discards qualifiers [-fpermissive])
```
6. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S09_OOP_Principles_and_Class_Definitions` exactly. 6 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S10_Constructors_and_Destructors.
