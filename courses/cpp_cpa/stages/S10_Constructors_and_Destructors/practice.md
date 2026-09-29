# S10_Constructors_and_Destructors - Practice: Constructors and destructors

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, say so and why.
```cpp
class T {
    int id;
public:
    T(int i) : id(i) { cout << "+" << id; }
    ~T() { cout << "-" << id; }
};
// ---- main ----
    { T a(1); T b(2); }
    cout << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
class W { public: explicit W(int) {} };
void take(W) {}
// ---- main ----
    take(5);
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
+1+2-2-1
```
2. Actual result (from running it):
```
(does not compile: could not convert ‘5’ from ‘int’ to ‘W’)
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
