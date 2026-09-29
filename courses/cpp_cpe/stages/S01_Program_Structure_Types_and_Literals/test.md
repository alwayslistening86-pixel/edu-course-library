# S01_Program_Structure_Types_and_Literals - Test: Program structure, types and literals

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, say so and why.
```cpp
    char c = 'a';
    cout << char(c + 2) << " " << int('0') << endl;
```
2. What is the output? If it does not compile, say so and why.
```cpp
    cout << 0b1111 << " " << 017 << " " << 0xF << " " << 1e2 << endl;
```
3. What is the output? If it does not compile, say so and why.
```cpp
    int int = 5;
    cout << int << endl;
```
4. Which are valid declarations of main? Choose every correct option.
   A. `int main()`
   B. `int main(int argc, char *argv[])`
   C. `void main()`
   D. `int main(int argc, char **argv)`
5. What is the output? If it does not compile, say so and why.
```cpp
    cout << 5 / 2 << " " << 5.0f / 2 << " " << (true + true) << endl;
```
6. A program is started as `prog a b c`. What is argc? Choose every correct option.
   A. `3`
   B. `4`
   C. `1`
   D. It depends on the compiler

## Answer key (for the tutor only)
1. Actual result (from running it):
```
c 48
```
2. Actual result (from running it):
```
15 15 15 100
```
3. Actual result (from running it):
```
(does not compile: expected unqualified-id before ‘=’ token)
```
4. Correct: A, B, D (exactly these options, no others)
5. Actual result (from running it):
```
2 2.5 2
```
6. Correct: B (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S01_Program_Structure_Types_and_Literals` exactly. 6 items; a pass needs at least 5 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S02_Operators_and_Precedence.
