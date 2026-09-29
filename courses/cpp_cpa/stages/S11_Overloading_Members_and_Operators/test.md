# S11_Overloading_Members_and_Operators - Test: Overloading member functions and operators

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
class N {
    int v;
public:
    N(int x) : v(x) {}
    N &operator++() { ++v; return *this; }
    N operator++(int) { N t = *this; v += 10; return t; }
    int get() const { return v; }
};
// ---- main ----
    N a(1);
    N b = a++;
    ++a;
    cout << a.get() << " " << b.get() << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
struct P { int x; };
bool operator==(const P &a, const P &b) { return a.x == b.x; }
// ---- main ----
    cout << (P{3} == P{3}) << (P{3} == P{4}) << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
class Arr {
    int d[3] = {5, 6, 7};
public:
    int &operator[](int i) { return d[i]; }
};
// ---- main ----
    Arr a;
    a[1] = 60;
    cout << a[0] + a[1] << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
struct Pt { int x, y; };
ostream &operator<<(ostream &os, const Pt &p) { return os << "(" << p.x << "," << p.y << ")"; }
// ---- main ----
    cout << Pt{1, 2} << Pt{3, 4} << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
class A { public: void f(int) { cout << "i"; } void f(double) { cout << "d"; } };
// ---- main ----
    A a;
    a.f(1); a.f(1.0); a.f('x');
    cout << endl;
```
6. Which operators cannot be overloaded? Choose every correct option.
   A. `::`
   B. `+`
   C. `?:`
   D. `sizeof`
   E. `[]`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
12 1
```
2. Actual result (from running it):
```
10
```
3. Actual result (from running it):
```
65
```
4. Actual result (from running it):
```
(1,2)(3,4)
```
5. Actual result (from running it):
```
idi
```
6. Correct: A, C, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S11_Overloading_Members_and_Operators` exactly. 6 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S12_Inheritance_Casting_and_Polymorphism.
