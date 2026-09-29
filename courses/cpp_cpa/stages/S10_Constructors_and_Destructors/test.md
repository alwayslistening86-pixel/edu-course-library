# S10_Constructors_and_Destructors - Test: Constructors and destructors

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
class A {
public:
    A() { cout << "A"; }
    A(const A &) { cout << "C"; }
    ~A() { cout << "~"; }
};
void f(A a) {}
// ---- main ----
    A x;
    f(x);
    cout << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
struct Noisy { Noisy(const char *n) { cout << n; } };
class B {
    Noisy x;
    Noisy y;
public:
    B() : y("y"), x("x") {}
};
// ---- main ----
    B b;
    cout << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
class P {
public:
    int v;
    P(int x) : v(x) {}
};
// ---- main ----
    P p;
```
4. What is the output? If it does not compile, say so and why.
```cpp
class Q {
public:
    int v;
    Q(int x = 4) : v(x) {}
};
// ---- main ----
    Q a, b(9);
    Q c = 7;
    cout << a.v << b.v << c.v << endl;
```
5. What is the output? If it does not compile, say so and why.
```cpp
class D {
public:
    D() { cout << "D"; }
    ~D() { cout << "d"; }
};
// ---- main ----
    D *p = new D;
    D arr[2];
    delete p;
    cout << "|";
```
6. When is the copy constructor called? Choose every correct option.
   A. Initialising a new object from an existing one
   B. Passing an object by value
   C. Assigning one existing object to another
   D. Passing an object by reference
7. Write a class Buffer that allocates an int array of a given size in its constructor and frees it in its destructor, and a copy constructor that makes a deep copy.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
AC~
~
```
2. Actual result (from running it):
```
xy
```
3. Actual result (from running it):
```
(does not compile: no matching function for call to ‘P::P()’)
```
4. Actual result (from running it):
```
497
```
5. Actual result (from running it):
```
DDDd|dd
```
6. Correct: A, B (exactly these options, no others)
7. The tutor runs or reads the learner's answer and checks: new[] in the constructor, delete[] in the destructor, and a copy constructor allocating its own array and copying the elements.

## Grading
Apply `rubric.json`'s `stage_rubrics.S10_Constructors_and_Destructors` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S11_Overloading_Members_and_Operators.
