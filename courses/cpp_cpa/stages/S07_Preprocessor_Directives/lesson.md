# S07_Preprocessor_Directives - Lesson: The preprocessor

## Goal
The learner uses #define macros (with and without parameters) and conditional compilation, and avoids the classic macro pitfalls.

## Syllabus items taught here
- 3.7 - Conditional compilation: #if, #ifdef, #else, #endif
- 3.8 - Parameterised and non-parameterised macros

## How to teach this
Ask what `#define SQ(x) x * x` gives for SQ(1 + 2). Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 3.7 Conditional compilation: #if, #ifdef, #else, #endif
The preprocessor runs **before** compilation. `#if EXPR ... #elif ... #else ... #endif` keeps or removes code depending on constant expressions; `#ifdef NAME` and `#ifndef NAME` test whether a macro is defined (as in include guards). `defined(NAME)` can be used inside `#if`.
```cpp
#define DEBUG 1
#define VERSION 3
// ---- main ----
#if DEBUG
    cout << "debug on ";
#else
    cout << "debug off ";
#endif
#ifdef VERSION
    cout << "v" << VERSION << " ";
#endif
#if defined(RELEASE) || VERSION > 2
    cout << "new build";
#endif
    cout << endl;
```
Output:
```
debug on v3 new build
```

#### 3.8 Parameterised and non-parameterised macros
`#define NAME value` is plain text substitution. `#define F(x) ...` takes parameters; parenthesise **every** parameter and the whole body, because the text is pasted in without regard to precedence, and arguments may be evaluated twice. `#undef NAME` removes a macro. Prefer const and inline functions in modern C++.
```cpp
#define PI 3
#define BAD_SQ(x) x * x
#define SQ(x) ((x) * (x))
#define MAX(a, b) ((a) > (b) ? (a) : (b))
// ---- main ----
    int i = 3;
    cout << PI * 2 << " " << BAD_SQ(1 + 2) << " " << SQ(1 + 2) << " " << MAX(i++, 2) << " " << i << endl;
```
Output:
```
6 5 9 4 5
```

## Explicitly not here
Pointers are S08.
