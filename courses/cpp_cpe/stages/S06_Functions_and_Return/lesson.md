# S06_Functions_and_Return - Lesson: Functions and return

## Goal
The learner declares, defines and calls functions correctly, including prototypes and void functions.

## Syllabus items taught here
- 2.5 - Defining, declaring and calling functions
- 2.6 - return in typed and void functions

## How to teach this
Ask why the compiler complains when main calls a function defined further down the file. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 2.5 Defining, declaring and calling functions
A **definition** gives the body: `int sq(int x) { return x * x; }`. A **declaration** (prototype) states only the signature, `int sq(int);`, so the function can be called before it's defined. Arguments are converted to the parameter types; a call with the wrong number of arguments doesn't compile.
```cpp
int cube(int);          // declaration (prototype)
double half(double x) { return x / 2; }
int cube(int x) { return x * x * x; }  // definition
// ---- main ----
    cout << cube(3) << " " << half(5) << " " << half(cube(2)) << endl;
```
Output:
```
27 2.5 4
```

#### 2.6 return in typed and void functions
A function with a return type must `return` a value of (or convertible to) that type on every path; the value is converted (`return 3.9;` from an int function gives 3). A `void` function returns nothing; `return;` may end it early. Only main may omit its return.
```cpp
int toInt() { return 3.9; }
void greet(bool shy) {
    if (shy) return;
    cout << "hello" << endl;
}
// ---- main ----
    greet(true);
    greet(false);
    cout << toInt() << endl;
```
Output:
```
hello
3
```

## Explicitly not here
Reference and pointer parameters are S07.
