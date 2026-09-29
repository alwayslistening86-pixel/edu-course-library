# S13_Friends_and_Namespaces - Test: Friends and namespaces

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
int n = 1;
namespace ns { int n = 2; }
// ---- main ----
    int n = 3;
    cout << n << ::n << ns::n << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
namespace one { int f() { return 1; } }
namespace one { int g() { return f() + 1; } }
// ---- main ----
    cout << one::g() << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
class A { int secret = 5; friend class B; };
class B { public: int read(const A &a) { return a.secret; } };
class C : public B { public: int peek(const A &a) { return a.secret; } };
// ---- main ----
    cout << B().read(A());
```
4. What is the output? If it does not compile, say so and why.
```cpp
namespace { int hidden = 9; }
// ---- main ----
    cout << hidden << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
namespace x { int val = 4; }
using x::val;
// ---- main ----
    cout << val * 2 << endl;
```
6. Which are true of friendship? Choose every correct option.
   A. A friend function can access private members
   B. Friendship is inherited by derived classes
   C. Friendship is not automatically mutual
   D. A class can declare another class as a friend

## Answer key (for the tutor only)
1. Actual result (from running it):
```
312
```
2. Actual result (from running it):
```
2
```
3. Actual result (from running it):
```
(does not compile: ‘int A::secret’ is private within this context)
```
4. Actual result (from running it):
```
9
```
5. Actual result (from running it):
```
8
```
6. Correct: A, C, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S13_Friends_and_Namespaces` exactly. 6 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass. Every stage is now passed, so the cumulative exam becomes available.
