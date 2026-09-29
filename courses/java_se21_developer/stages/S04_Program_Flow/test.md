# S04_Program_Flow - Test: Program flow: if, switch statements and expressions, loops

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
String day = "TUE";
int n = switch (day) {
    case "MON", "TUE" -> 1;
    case "WED" -> 2;
};
System.out.println(n);
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
char c = 'b';
switch (c) {
    case 'a' -> System.out.print("A");
    case 'b' -> System.out.print("B");
    case 'c' -> System.out.print("C");
}
switch (c) {
    case 'b': System.out.print("b");
    case 'c': System.out.print("c");
    default: System.out.print("d");
}
System.out.println();
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
int x = 1;
int r = switch (x) {
    case 1:
        System.out.print("one ");
    case 2:
        yield 20;
    default:
        yield 0;
};
System.out.println(r);
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
int i = 0, j = 10;
while (i++ < j--) ;
System.out.println(i + " " + j);
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
int sum = 0;
loop:
for (int a = 1; a <= 3; a++)
    for (int b = 1; b <= 3; b++) {
        if (b > a) continue loop;
        if (a * b == 6) break loop;
        sum += a * b;
    }
System.out.println(sum);
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
int k = 0;
do {
    k++;
    if (k == 2) break;
    continue;
    k += 10;
} while (k < 5);
System.out.println(k);
```
7. Which types can be the selector of a switch expression that uses only constant case labels in Java 21? (choose three) Choose every correct option.
   A. `String`
   B. `long`
   C. `Character`
   D. an enum type
   E. `boolean`

## Answer key (for the tutor only)
1. Actual result (from running it):
```
(does not compile: the switch expression does not cover all possible input values)
```
2. Actual result (from running it):
```
Bbcd
```
3. Actual result (from running it):
```
one 20
```
4. Actual result (from running it):
```
6 4
```
5. Actual result (from running it):
```
10
```
6. Actual result (from running it):
```
(does not compile: unreachable statement)
```
7. Correct: A, C, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S04_Program_Flow` exactly. 7 items; a pass needs at least 5 fully correct (68%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S05_Objects_Classes_and_Records.
