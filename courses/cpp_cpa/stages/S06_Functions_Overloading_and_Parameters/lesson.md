# S06_Functions_Overloading_and_Parameters - Lesson: Functions, overloading and parameters

## Goal
The learner declares, defines, overloads and calls functions with default parameters and all passing styles, uses recursion, and applies main() conventions.

## Syllabus items taught here
- 3.1 - Defining, declaring and invoking functions
- 3.2 - Typed and void functions with return
- 3.3 - Overloading functions and default parameters
- 3.4 - Passing arguments by value, reference and pointer
- 3.5 - Recursion
- 3.6 - main() conventions

## How to teach this
Ask which overload `print(5.0f)` calls when print(int) and print(double) both exist. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 3.1 Defining, declaring and invoking functions
Declare (prototype) before use; define once. Declarations may omit parameter names. Calling a function requires matching arguments after conversions.
```cpp
int area(int, int);                                       // declaration
int doubleArea(int w, int h) { return 2 * area(w, h); }   // uses area before its definition
int area(int w, int h) { return w * h; }                  // definition
// ---- main ----
    cout << doubleArea(3, 4) << endl;
```
Output:
```
24
```

#### 3.2 Typed and void functions with return
A typed function returns a value of its type; a `void` function returns nothing and can't be used in an expression. A returned value can be ignored by the caller.
```cpp
int twice(int x) { return 2 * x; }
void show(int x) { cout << "[" << x << "]"; }
// ---- main ----
    twice(5);
    show(twice(4));
    cout << endl;
```
Output:
```
[8]
```

#### 3.3 Overloading functions and default parameters
**Overloading**: several functions share a name but differ in the number or types of their parameters (return type alone doesn't count). The compiler picks the best match: exact match first, then promotion (float to double, char to int), then conversion; an ambiguity is a compile error. **Default parameters** fill in trailing arguments; they're specified once (usually in the declaration) and must be the rightmost ones.
```cpp
void p(int x) { cout << "int "; }
void p(double x) { cout << "double "; }
void p(const string &s) { cout << "string "; }
int volume(int l, int w = 1, int h = 1) { return l * w * h; }
// ---- main ----
    p(1); p(1.5f); p('c'); p(string("s"));
    cout << volume(2) << " " << volume(2, 3) << " " << volume(2, 3, 4) << endl;
```
Output:
```
int double int string 2 6 24
```

#### 3.4 Passing arguments by value, reference and pointer
By value: a copy. By reference (`T&`): an alias for the caller's variable. By `const T&`: efficient and read-only. By pointer (`T*`): the caller passes an address, and it may be nullptr. Arrays passed to functions decay to pointers, so the function doesn't know the size.
```cpp
void a(int x) { x = 1; }
void b(int &x) { x = 2; }
void c(int *x) { if (x) *x = 3; }
int sizeInFunction(int arr[]) { return sizeof(arr); }
// ---- main ----
    int v = 0;
    a(v); cout << v;
    b(v); cout << v;
    c(&v); cout << v;
    c(nullptr);
    int arr[10];
    cout << " " << sizeof(arr) << " " << sizeInFunction(arr) << endl;
```
Output:
```
023 40 8
```

#### 3.5 Recursion
Recursion: a function calling itself, with a base case. Useful for naturally recursive problems (factorials, trees, divide-and-conquer).
```cpp
int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
int fib(int n) { return n < 2 ? n : fib(n - 1) + fib(n - 2); }
// ---- main ----
    cout << gcd(84, 36) << " " << fib(10) << endl;
```
Output:
```
12 55
```

#### 3.6 main() conventions
`int main()` or `int main(int argc, char *argv[])`: argc counts the arguments including the program name, and `argv[argc]` is a null pointer. The return value is the exit status (0 is success; `EXIT_SUCCESS` and `EXIT_FAILURE` come from `<cstdlib>`). There's exactly one main, and it can't be overloaded, called recursively or have its address taken.
```cpp
#include <cstdlib>
// ---- main ----
    cout << EXIT_SUCCESS << " " << (EXIT_FAILURE != 0) << endl;
```
Output:
```
0 1
```

## Explicitly not here
The preprocessor is S07.
