# S09_OOP_Principles_and_Class_Definitions - Practice: OOP principles and class definitions

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, say so and why.
```cpp
class C {
    int v = 1;
public:
    int get() const;
};
int C::get() const { return v * 10; }
// ---- main ----
    cout << C().get() << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
class C { int hidden = 5; };
// ---- main ----
    C c;
    cout << c.hidden;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
10
```
2. Actual result (from running it):
```
(does not compile: ‘int C::hidden’ is private within this context)
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
