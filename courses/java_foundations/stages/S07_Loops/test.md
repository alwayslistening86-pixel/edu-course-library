# S07_Loops - Test: Looping statements, break and continue

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
int count = 0;
for (int i = 1; i <= 20; i *= 3) count++;
System.out.println(count);
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
int n = 5;
do { n -= 2; } while (n > 10);
System.out.println(n);
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
String out = "";
for (int i = 1; i <= 3; i++)
    for (int j = i; j <= 3; j++)
        out += j;
System.out.println(out);
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
int[] xs = {3, 8, 1, 9, 4};
int best = xs[0];
for (int x : xs) { if (x > best) best = x; }
System.out.println(best);
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
int k = 0;
outer:
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        if (j > i) continue outer;
        if (i == 2 && j == 1) break outer;
        k++;
    }
}
System.out.println(k);
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
for (int i = 0; i < 3; i++) { }
System.out.println(i);
```
7. Which statements are true? Choose every correct option.
   A. A do-while body always runs at least once
   B. `A while loop's body may run zero times`
   C. An enhanced for loop gives you the current index
   D. continue in a for loop still runs the update expression

## Answer key (for the tutor only)
1. Actual result (from running it):
```
3
```
2. Actual result (from running it):
```
3
```
3. Actual result (from running it):
```
123233
```
4. Actual result (from running it):
```
9
```
5. Actual result (from running it):
```
4
```
6. Actual result (from running it):
```
(does not compile: cannot find symbol)
```
7. Correct: A, B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S07_Loops` exactly. 7 items; a pass needs at least 5 fully correct (65%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S08_Debugging_and_Exceptions.
