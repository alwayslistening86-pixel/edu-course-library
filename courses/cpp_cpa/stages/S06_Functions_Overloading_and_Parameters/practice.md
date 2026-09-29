# S06_Functions_Overloading_and_Parameters - Practice: Functions, overloading and parameters

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, say so and why.
```cpp
int add(int a, int b = 10, int c = 100) { return a + b + c; }
// ---- main ----
    cout << add(1) << " " << add(1, 2) << " " << add(1, 2, 3) << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
void f(int) { cout << "int"; }
void f(long) { cout << "long"; }
// ---- main ----
    f(5L); f('a');
    cout << endl;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
111 103 6
```
2. Actual result (from running it):
```
longint
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
