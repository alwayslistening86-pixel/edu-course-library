# C++: CPA-21-02 C++ Certified Associate Programmer (C++ Institute) - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` has a passed test.

## Format
40 items in CPA's real proportions: 9 from S01-S03, 8 from S04-S05, 9 from S06-S07, 4 from S08 and 10 from S09-S13. Mix single-choice, multiple-choice and code-output items, in non-sequential order. 65 minutes, matching the real exam. No compiling until everything is answered.

## 8 ready-made items (write the rest fresh, never reusing stage-test items)
1. What is the output? If it does not compile, say so and why.
```cpp
    int a = 7;
    cout << (a & 3) + (a >> 1) << " " << (a % 3 ? "odd-ish" : "multiple") << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
#define CUBE(x) ((x) * (x) * (x))
// ---- main ----
    int n = 2;
    cout << CUBE(n + 1) << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
void f(int &a, int b = 3) { a *= b; }
// ---- main ----
    int x = 2;
    f(x); f(x, 2);
    cout << x << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
#include <stdexcept>
// ---- main ----
    try { vector<int> v(1); v.at(2) = 1; }
    catch (const logic_error &) { cout << "logic"; }
    catch (...) { cout << "other"; }
    cout << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
struct A { virtual string n() { return "A"; } virtual ~A() {} };
struct B : A { string n() override { return "B" + A::n(); } };
// ---- main ----
    A *p = new B;
    cout << p->n() << endl;
    delete p;
```
6. What is the output? If it does not compile, say so and why.
```cpp
class C {
    static int k;
public:
    C() { ++k; }
    ~C() { --k; }
    static int count() { return k; }
};
int C::k = 0;
// ---- main ----
    C a;
    { C b, c; cout << C::count(); }
    cout << C::count() << endl;
```
7. What is the output? If it does not compile, say so and why.
```cpp
    int arr[] = {3, 6, 9, 12};
    int *p = arr, *q = arr + 3;
    cout << *q - *p << " " << q - p << endl;
```
8. What is the output? If it does not compile, say so and why.
```cpp
namespace m { int f(int x) { return x + 1; } }
namespace k = m;
// ---- main ----
    cout << k::f(m::f(0)) << endl;
```

## Answer key for the ready-made items (tutor only)
1. Actual result (from running it):
```
6 odd-ish
```
2. Actual result (from running it):
```
27
```
3. Actual result (from running it):
```
12
```
4. Actual result (from running it):
```
logic
```
5. Actual result (from running it):
```
BA
```
6. Actual result (from running it):
```
31
```
7. Actual result (from running it):
```
9 3
```
8. Actual result (from running it):
```
2
```

## Grading
Apply `rubric.json`'s `exam_rubric` exactly: at least 28 of 40 (70%) for a pass, and report the score per block.

## Outcome
- **Pass:** record `exam_status: "passed"`. The course is complete.
- **Not yet:** leave `exam_status: "available"`, name the weakest block, offer targeted review, and retry with a fresh paper.
