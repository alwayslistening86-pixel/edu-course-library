# S04_Control_Flow - Lesson: Control flow

## Goal
The learner traces every control statement on the syllabus, including loops with break, continue and goto, switch fall-through, and return.

## Syllabus items taught here
- 2.1 - Conditional statements and loops: if, else, while, do, for
- 2.2 - break, continue and goto
- 2.3 - switch, case and default
- 2.4 - return statements

## How to teach this
Ask what `for (int i = 0; i < 3; ++i) if (i == 1) continue; else cout << i;` prints. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 2.1 Conditional statements and loops: if, else, while, do, for
`if/else` (else binds to the nearest if), `while` (test first), `do ... while` (test last, so at least once), `for (init; cond; step)`, and range-for `for (auto &x : container)`. Variables declared in a for's init are local to the loop.
```cpp
int n = 0;
do { n += 2; } while (n < 5);
for (int i = 3; i > 0; --i) cout << i;
cout << " " << n << endl;
vector<int> v{1, 2, 3};
for (auto &x : v) x *= x;
cout << v[2] << endl;
```
Output:
```
321 6
9
```

#### 2.2 break, continue and goto
`break` leaves the innermost loop or switch; `continue` goes to the next pass (in a for loop, the step still runs); `goto label` jumps within the function, and is legal but discouraged.
```cpp
    for (int i = 0; i < 5; ++i) {
        if (i == 1) continue;
        if (i == 3) break;
        cout << i;
    }
    int k = 0;
top:
    if (++k < 3) goto top;
    cout << " " << k << endl;
```
Output:
```
02 3
```

#### 2.3 switch, case and default
`switch` selects on an integral or enum value. Execution falls through into later cases until a `break`; `default` catches everything else. Case labels must be distinct constant expressions. A variable declared inside a case needs its own braces.
```cpp
for (int c : {1, 2, 3, 9}) {
    switch (c) {
        case 1:
        case 2: cout << "low "; break;
        case 3: { int sq = c * c; cout << sq << " "; }
        default: cout << "def ";
    }
}
cout << endl;
```
Output:
```
low low 9 def def 
```

#### 2.4 return statements
`return expr;` ends a function and gives its value, converted to the return type; `return;` ends a void function. Every path of a non-void function must return a value (flowing off the end is undefined behaviour, except in main, where `return 0` is implied).
```cpp
int classify(int n) {
    if (n < 0) return -1;
    if (n == 0) return 0;
    return 1;
}
double half(int n) { return n / 2; }
// ---- main ----
    cout << classify(-5) << classify(0) << classify(8) << " " << half(7) << endl;
```
Output:
```
-101 3
```

## Explicitly not here
Exceptions are S05.
