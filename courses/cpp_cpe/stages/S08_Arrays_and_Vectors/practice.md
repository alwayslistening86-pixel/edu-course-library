# S08_Arrays_and_Vectors - Practice: Arrays and vectors

## Goal
Low-stakes practice: the learner predicts or writes first, then runs it to check. Mistakes are expected and corrected here, before any grading.

## Practice items
1. What is the output? If it does not compile, say so and why.
```cpp
    int a[4] = {3};
    cout << a[0] << a[1] << a[3] << " " << sizeof(a) / sizeof(int) << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    vector<int> v;
    for (int i = 1; i <= 3; i++) v.push_back(i * i);
    cout << v.size() << " " << v[1] << " " << v.back() << endl;
```

## Answers (for the tutor; reveal only after a genuine attempt)
1. Actual result (from running it):
```
300 4
```
2. Actual result (from running it):
```
3 4 9
```

## How to run it
One item at a time. For output questions the learner commits to a prediction before running anything. Offer a worked explanation only after an attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
