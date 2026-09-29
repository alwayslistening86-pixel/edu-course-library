# S07_Parameter_Passing_and_Recursion - Practice: Passing arguments and recursion

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, say so and why.
```cpp
void inc(int x) { x++; }
void incRef(int &x) { x++; }
// ---- main ----
    int v = 5;
    inc(v); incRef(v);
    cout << v << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
int sum(int n) { return n == 0 ? 0 : n + sum(n - 1); }
// ---- main ----
    cout << sum(10) << endl;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
6
```
2. Actual result (from running it):
```
55
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
