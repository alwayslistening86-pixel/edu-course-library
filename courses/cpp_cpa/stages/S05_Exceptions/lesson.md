# S05_Exceptions - Lesson: Exceptions

## Goal
The learner throws and catches exceptions of any type, orders catch clauses correctly within the standard hierarchy, and understands throw() and noexcept specifications.

## Syllabus items taught here
- 2.5 - Exception handling: try, catch, throw and catch-all
- 2.6 - Exception hierarchies and the throw() specifier

## How to teach this
Ask what happens to the rest of a function after it throws. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 2.5 Exception handling: try, catch, throw and catch-all
`throw expr;` throws any value (an int, a string, or preferably an exception object). The first matching `catch (Type e)` after the `try` runs; `catch (...)` catches **everything**, and must come last. Catch class types by reference (`const exception &e`) to avoid slicing. A bare `throw;` inside a catch re-throws. An uncaught exception terminates the program.
```cpp
void risky(int n) {
    if (n == 1) throw 42;
    if (n == 2) throw string("text");
    if (n == 3) throw 3.14;
}
// ---- main ----
    for (int n = 0; n <= 3; n++) {
        try {
            risky(n);
            cout << "ok ";
        } catch (int e) {
            cout << "int:" << e << " ";
        } catch (const string &s) {
            cout << "string:" << s << " ";
        } catch (...) {
            cout << "other ";
        }
    }
    cout << endl;
```
Output:
```
ok int:42 string:text other 
```

#### 2.6 Exception hierarchies and the throw() specifier
The standard exceptions derive from `std::exception` (`what()` gives the message): `logic_error` (with `invalid_argument`, `out_of_range`, `length_error`, `domain_error`), `runtime_error` (with `overflow_error`, `range_error`), plus `bad_alloc` and `bad_cast`. Catch derived types **before** base types; a base catch listed first would swallow them. Your own exceptions should inherit from one of these. `throw()` after a function's parameters is the old promise that the function throws nothing; since C++11 the preferred form is `noexcept`. If such a function does throw, `std::terminate` is called.
```cpp
#include <stdexcept>
class InsufficientFunds : public runtime_error {
public:
    InsufficientFunds() : runtime_error("insufficient funds") {}
};
void safe() throw() {}
void withdraw(int amount) { if (amount > 100) throw InsufficientFunds(); }
// ---- main ----
    try {
        vector<int> v(2);
        v.at(5);
    } catch (const out_of_range &e) {
        cout << "out_of_range ";
    } catch (const exception &e) {
        cout << "exception ";
    }
    try { withdraw(500); } catch (const exception &e) { cout << e.what() << " "; }
    cout << noexcept(safe()) << endl;
```
Output:
```
out_of_range insufficient funds 1
```

## Explicitly not here
Functions are S06.
