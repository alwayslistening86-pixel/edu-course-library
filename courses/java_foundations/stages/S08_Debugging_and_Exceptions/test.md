# S08_Debugging_and_Exceptions - Test: Debugging and exception handling

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
try {
    System.out.print("1");
    int[] a = new int[2];
    a[2] = 5;
    System.out.print("2");
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.print("3");
} finally {
    System.out.print("4");
}
System.out.println("5");
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
String[] in = {"5", "0", "x"};
for (String s : in) {
    try {
        System.out.print(10 / Integer.parseInt(s) + " ");
    } catch (ArithmeticException e) {
        System.out.print("div ");
    } catch (NumberFormatException e) {
        System.out.print("fmt ");
    }
}
System.out.println();
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
try {
    Object o = "text";
    Integer n = (Integer) o;
    System.out.println(n);
} catch (RuntimeException e) {
    System.out.println(e.getClass().getSimpleName());
}
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
int total = 0;
for (int i = 1; i <= 3; i++)
    total += i
System.out.println(total);
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
ArrayList<Integer> list = new ArrayList<>();
list.add(1);
System.out.println(list.get(1));
```
6. Which statements about try/catch are true? Choose every correct option.
   A. When the try block throws, its remaining statements are skipped
   B. A catch for Exception placed before a catch for ArithmeticException causes a compile error
   C. finally runs only when no exception is thrown
   D. After a matching catch finishes, execution continues after the try statement
7. This method is meant to return the average of an int array but gives 2.0 for {1, 2, 4}: `static double avg(int[] a) { int s = 0; for (int x : a) s += x; return s / a.length; }`. Name the kind of error and fix it.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
1345
```
2. Actual result (from running it):
```
2 div fmt 
```
3. Actual result (from running it):
```
ClassCastException
```
4. Actual result (from running it):
```
(does not compile: ';' expected)
```
5. Actual result (from running it):
```
(throws IndexOutOfBoundsException: Index 1 out of bounds for length 1)
```
6. Correct: A, B, D (exactly these options, no others)
7. The tutor runs or reads the learner's answer and checks: identifies a logic error (integer division); fixes with a cast, e.g. `return (double) s / a.length;`, giving 2.333...

## Grading
Apply `rubric.json`'s `stage_rubrics.S08_Debugging_and_Exceptions` exactly. 7 items; a pass needs at least 5 fully correct (65%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S09_Arrays_and_ArrayLists.
