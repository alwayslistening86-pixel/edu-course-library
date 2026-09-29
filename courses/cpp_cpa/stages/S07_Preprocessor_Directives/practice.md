# S07_Preprocessor_Directives - Practice: The preprocessor

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, say so and why.
```cpp
#define TRIPLE(x) ((x) * 3)
// ---- main ----
    cout << TRIPLE(2 + 1) << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
#define FEATURE
// ---- main ----
#ifdef FEATURE
    cout << "on";
#else
    cout << "off";
#endif
    cout << endl;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
9
```
2. Actual result (from running it):
```
on
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
