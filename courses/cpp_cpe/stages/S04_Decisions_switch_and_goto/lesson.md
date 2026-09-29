# S04_Decisions_switch_and_goto - Lesson: if, switch and goto

## Goal
The learner writes and traces if/else chains and switch statements (including fall-through), and recognises goto and labels.

## Syllabus items taught here
- 2.1 - Conditional statements if and else
- 2.3 - The goto statement and labelled statements
- 2.4 - Multiple selection with switch, case and default

## How to teach this
Ask which if an else belongs to when there are two ifs and one else without braces. Have the learner predict the output of every example before compiling it, and compile and run code for real (any C++17 compiler).

#### 2.1 Conditional statements if and else
`if (condition) statement else statement`; the condition is converted to bool (nonzero means true). Without braces, only one statement is controlled, and an `else` pairs with the **nearest unmatched if** (the dangling-else rule). Using `=` instead of `==` compiles, and assigns.
```cpp
int x = 5, y = 0;
if (x > 3)
    if (x > 10) cout << "big";
    else cout << "medium";
cout << endl;
if (y = 0) cout << "never"; else cout << "y was assigned 0, which is false" << endl;
```
Output:
```
medium
y was assigned 0, which is false
```

#### 2.3 The goto statement and labelled statements
`goto label;` jumps to `label:` in the same function. It's legal, but it makes code hard to follow; the exam only expects you to recognise and trace it. It can't jump over a variable's initialisation into that variable's scope.
```cpp
    int i = 0;
again:
    cout << i << " ";
    if (++i < 3) goto again;
    cout << endl;
```
Output:
```
0 1 2 
```

#### 2.4 Multiple selection with switch, case and default
`switch (integral expression) { case const: ...; break; default: ...; }`. Execution jumps to the matching case and **falls through** into the following cases until a `break`. `default` handles no match. Case labels must be constant integral values (int, char, enum), never strings, and must not repeat.
```cpp
for (int n : {1, 2, 5}) {
    switch (n) {
        case 1: cout << "one ";
        case 2: cout << "two "; break;
        default: cout << "other ";
    }
}
cout << endl;
char grade = 'B';
switch (grade) { case 'A': case 'B': cout << "pass" << endl; break; default: cout << "retry" << endl; }
```
Output:
```
one two two other 
pass
```

## Explicitly not here
Loops are S05.
