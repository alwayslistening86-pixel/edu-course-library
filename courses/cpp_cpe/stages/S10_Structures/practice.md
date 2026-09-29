# S10_Structures - Practice: Structures

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, say so and why.
```cpp
struct P { string n; int a; };
// ---- main ----
    P p{"Bo", 7};
    P q = p;
    q.a = 8;
    cout << p.a << q.a << p.n << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
struct S { int v = 3; };
// ---- main ----
    S s;
    S *ptr = &s;
    ptr->v++;
    cout << s.v << endl;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
78Bo
```
2. Actual result (from running it):
```
4
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
