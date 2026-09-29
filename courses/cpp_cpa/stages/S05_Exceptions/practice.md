# S05_Exceptions - Practice: Exceptions

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, say so and why.
```cpp
    try {
        throw 'x';
    } catch (int) {
        cout << "int";
    } catch (char c) {
        cout << "char " << c;
    }
    cout << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
#include <stdexcept>
// ---- main ----
    try { throw invalid_argument("bad"); }
    catch (const logic_error &e) { cout << "logic_error: " << e.what() << endl; }
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
char x
```
2. Actual result (from running it):
```
logic_error: bad
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
