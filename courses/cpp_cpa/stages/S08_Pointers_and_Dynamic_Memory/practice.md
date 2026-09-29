# S08_Pointers_and_Dynamic_Memory - Practice: Pointers and dynamic memory

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, say so and why.
```cpp
    int a[4] = {1, 2, 3, 4};
    int *p = a + 1;
    cout << *p << " " << p[2] << " " << *(a + 3) - *p << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
int inc(int v) { return v + 1; }
// ---- main ----
    int (*f)(int) = inc;
    cout << f(f(1)) << endl;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
2 4 2
```
2. Actual result (from running it):
```
3
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
