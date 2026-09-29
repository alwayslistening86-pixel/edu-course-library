# S11_Overloading_Members_and_Operators - Practice: Overloading member functions and operators

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, say so and why.
```cpp
struct V {
    int x, y;
    V operator+(const V &o) const { return {x + o.x, y + o.y}; }
};
// ---- main ----
    V a{1, 2}, b{3, 4};
    V c = a + b;
    cout << c.x << c.y << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
class C {
    int n = 0;
public:
    int &val() { return n; }
    int val() const { return -1; }
};
// ---- main ----
    C c;
    const C k;
    c.val() = 5;
    cout << c.val() << " " << k.val() << endl;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
46
```
2. Actual result (from running it):
```
5 -1
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
