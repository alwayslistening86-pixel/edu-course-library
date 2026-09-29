# S09_Pointers_Casts_and_Dynamic_Memory - Test: Pointers, casts and dynamic memory

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
    int a = 1, b = 2;
    int *p = &a;
    p = &b;
    *p = 20;
    cout << a << " " << b << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    int v = 7;
    int *p = &v, **pp = &p;
    **pp = 9;
    cout << v << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
    double d = 2.99;
    int i = static_cast<int>(d);
    char c = static_cast<char>(65 + i);
    cout << i << c << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
struct B { virtual ~B() {} };
struct D1 : B {};
struct D2 : B {};
// ---- main ----
    B *b = new D2;
    cout << (dynamic_cast<D1*>(b) == nullptr) << (dynamic_cast<D2*>(b) != nullptr) << endl;
    delete b;
```
5. What is the output? If it does not compile, say so and why.
```cpp
struct B {};
struct D : B {};
// ---- main ----
    B *b = new D;
    D *d = dynamic_cast<D*>(b);
```
6. What is the output? If it does not compile, say so and why.
```cpp
    int *p = new int(5);
    int *q = p;
    *q += 1;
    cout << *p << endl;
    delete p;
```
7. Which pairs are correct? Choose every correct option.
   A. `new int -> delete`
   B. `new int[10] -> delete[]`
   C. `new int[10] -> delete`
   D. `nullptr -> safe to delete`
8. Allocate an array of n ints on the heap (n read from a variable), fill it with the squares 1..n, print the sum, and free the memory.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
1 20
```
2. Actual result (from running it):
```
9
```
3. Actual result (from running it):
```
2C
```
4. Actual result (from running it):
```
11
```
5. Actual result (from running it):
```
(does not compile: cannot ‘dynamic_cast’ ‘b’ (of type ‘struct B*’) to type ‘struct D*’ (source type is not polymorphic))
```
6. Actual result (from running it):
```
6
```
7. Correct: A, B, D (exactly these options, no others)
8. The tutor runs or reads the learner's answer and checks: new int[n], loop fill, sum printed, delete[] used exactly once.

## Grading
Apply `rubric.json`'s `stage_rubrics.S09_Pointers_Casts_and_Dynamic_Memory` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S10_Structures.
