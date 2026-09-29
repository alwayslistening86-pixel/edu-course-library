# S05_Loops - Lesson: Loops, break and continue

## Goal
The learner writes while, do-while and for loops, and predicts the effect of break and continue.

## Syllabus items taught here
- 2.2 - Loops while, do and for; break and continue

## How to teach this
Ask how many times `for (int i = 10; i > 0; i -= 3)` runs. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 2.2 Loops while, do and for; break and continue
`while (cond)` tests first (0 or more passes); `do { } while (cond);` tests last (at least one pass; note the semicolon); `for (init; cond; step)` is the counting loop, and any part may be empty (`for (;;)` loops forever). The range-for, `for (auto v : container)`, visits each element. `break` exits the innermost loop; `continue` jumps to the next pass (in a for loop, the step still runs).
```cpp
int n = 0;
while (n > 0) cout << "never";
do { cout << "do runs once "; } while (n > 0);
cout << endl;
for (int i = 10; i > 0; i -= 3) cout << i << " ";
cout << endl;
for (int i = 0; i < 10; i++) {
    if (i % 2 == 0) continue;
    if (i > 7) break;
    cout << i << " ";
}
cout << endl;
```
Output:
```
do runs once 
10 7 4 1 
1 3 5 7 
```

## Explicitly not here
Functions are S06.
