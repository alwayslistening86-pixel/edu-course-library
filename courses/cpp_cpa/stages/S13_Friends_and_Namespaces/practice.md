# S13_Friends_and_Namespaces - Practice: Friends and namespaces

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, say so and why.
```cpp
namespace a { int v = 1; namespace b { int v = 2; } }
namespace ab = a::b;
// ---- main ----
    cout << a::v << ab::v << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
class S { int x = 7; friend void show(const S &); };
void show(const S &s) { cout << s.x << endl; }
// ---- main ----
    show(S());
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
12
```
2. Actual result (from running it):
```
7
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
