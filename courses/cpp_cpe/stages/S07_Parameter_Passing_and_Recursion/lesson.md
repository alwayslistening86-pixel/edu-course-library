# S07_Parameter_Passing_and_Recursion - Lesson: Passing arguments and recursion

## Goal
The learner predicts the effect of passing by value, by reference and by pointer, and writes simple recursive functions.

## Syllabus items taught here
- 2.7 - Passing arguments by value, by reference and by pointer
- 2.8 - Basic recursion

## How to teach this
Write a swap function that doesn't work, then fix it twice: once with references and once with pointers. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 2.7 Passing arguments by value, by reference and by pointer
**By value** (`void f(int x)`): the function gets a copy, and the caller's variable is unchanged. **By reference** (`void f(int &x)`): x is another name for the caller's variable, so changes are visible outside. **By pointer** (`void f(int *p)`): the caller passes an address (`f(&v)`), and the function changes the value through `*p`. `const T&` passes large objects efficiently without allowing changes. A literal can't be passed to a non-const reference.
```cpp
void byValue(int x) { x = 100; }
void byRef(int &x) { x = 200; }
void byPtr(int *p) { *p = 300; }
void swapRef(int &a, int &b) { int t = a; a = b; b = t; }
// ---- main ----
    int v = 1;
    byValue(v); cout << v << " ";
    byRef(v); cout << v << " ";
    byPtr(&v); cout << v << endl;
    int a = 1, b = 2;
    swapRef(a, b);
    cout << a << b << endl;
```
Output:
```
1 200 300
21
```

#### 2.8 Basic recursion
A recursive function calls itself on a smaller problem, and needs a base case. Each call has its own copies of its local variables.
```cpp
int factorial(int n) { return n <= 1 ? 1 : n * factorial(n - 1); }
void countdown(int n) { if (n == 0) { cout << "go" << endl; return; } cout << n << " "; countdown(n - 1); }
// ---- main ----
    cout << factorial(5) << endl;
    countdown(3);
```
Output:
```
120
3 2 1 go
```

## Explicitly not here
Arrays and vectors are S08.
