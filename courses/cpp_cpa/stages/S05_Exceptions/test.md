# S05_Exceptions - Test: Exceptions

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
void f() { throw 1; cout << "after"; }
// ---- main ----
    try { f(); cout << "x"; } catch (int) { cout << "caught"; }
    cout << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
#include <stdexcept>
// ---- main ----
    try { throw out_of_range("idx"); }
    catch (const exception &e) { cout << "exception "; }
    catch (const out_of_range &e) { cout << "range "; }
    cout << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
    try {
        try { throw 5; }
        catch (int e) { cout << "inner " << e << " "; throw; }
    } catch (...) {
        cout << "outer";
    }
    cout << endl;
```
4. What is the output? If it does not compile, say so and why.
```cpp
#include <stdexcept>
struct MyErr : public std::runtime_error { MyErr() : runtime_error("mine") {} };
// ---- main ----
    try { throw MyErr(); }
    catch (const runtime_error &e) { cout << e.what() << endl; }
```
5. What is the output? If it does not compile, say so and why.
```cpp
    try { throw string("s"); }
    catch (const char *m) { cout << "cstr"; }
    catch (const string &m) { cout << "string"; }
    cout << endl;
```
6. What is the output? If it does not compile, say so and why.
```cpp
void safe() noexcept {}
void risky() {}
// ---- main ----
    cout << noexcept(safe()) << noexcept(risky()) << endl;
```
7. Which derive from std::logic_error? Choose every correct option.
   A. `std::invalid_argument`
   B. `std::out_of_range`
   C. `std::overflow_error`
   D. `std::length_error`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
caught
```
2. Actual result (from running it):
```
exception 
```
3. Actual result (from running it):
```
inner 5 outer
```
4. Actual result (from running it):
```
mine
```
5. Actual result (from running it):
```
string
```
6. Actual result (from running it):
```
10
```
7. Correct: A, B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S05_Exceptions` exactly. 7 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S06_Functions_Overloading_and_Parameters.
