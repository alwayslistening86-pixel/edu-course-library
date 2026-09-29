# S07_Loops - Lesson: Looping statements, break and continue

## Goal
The learner writes for, enhanced for, while and do-while loops, chooses between them, and controls them with break and continue.

## Syllabus items taught here
- 9.1 - Describe looping statements
- 9.2 - Use a for loop, including an enhanced for loop
- 9.3 - Use a while loop
- 9.4 - Use a do-while loop
- 9.5 - Compare and contrast the for, while and do-while loops
- 9.6 - Develop code that uses break and continue statements

## How to teach this
Ask how many times a do-while runs when its condition is false from the start. Have the learner predict the output of every example before running it, and compile and run code for real (any JDK; the examples were run on JDK 21 but use only features the Foundations syllabus covers).

#### 9.1 Describe looping statements
A loop repeats a block while a condition holds. Every loop needs an initialisation, a condition, and an update that eventually makes the condition false; otherwise it is an **infinite loop**. Java has four forms: `for`, enhanced `for` (for-each), `while` and `do-while`. Loops can be nested: the inner loop completes fully for each pass of the outer.
```java
for (int row = 1; row <= 3; row++) {
    for (int col = 1; col <= row; col++) System.out.print("*");
    System.out.println();
}
```
Output:
```
*
**
***
```

#### 9.2 Use a for loop, including an enhanced for loop
`for (init; condition; update) body`: the init runs once, the condition is checked before each pass, and the update runs after each pass. The loop variable's scope is the loop. The **enhanced for** `for (Type item : arrayOrCollection)` visits each element in order, read-only for the index (you can't see or change the position).
```java
int sum = 0;
for (int i = 10; i > 0; i -= 3) { System.out.print(i + " "); sum += i; }
System.out.println("sum=" + sum);
int[] nums = {4, 8, 15};
for (int n : nums) System.out.print(n * 2 + " ");
System.out.println();
for (int i = 0, j = 5; i < j; i++, j--) System.out.print(i + ":" + j + " ");
System.out.println();
```
Output:
```
10 7 4 1 sum=22
8 16 30 
0:5 1:4 2:3 
```

#### 9.3 Use a while loop
`while (condition) body` checks first, so the body may run zero times. Use it when the number of passes isn't known in advance.
```java
int n = 37, steps = 0;
while (n != 1) {
    n = (n % 2 == 0) ? n / 2 : 3 * n + 1;
    steps++;
}
System.out.println(steps);
int k = 10;
while (k < 5) System.out.println("never");
System.out.println("done");
```
Output:
```
21
done
```

#### 9.4 Use a do-while loop
`do { body } while (condition);` runs the body first and checks afterwards, so it always runs **at least once**. Note the semicolon after the condition.
```java
int k = 10;
do {
    System.out.println("ran with k=" + k);
    k++;
} while (k < 5);
int total = 0, i = 1;
do { total += i; i++; } while (i <= 4);
System.out.println(total);
```
Output:
```
ran with k=10
10
```

#### 9.5 Compare and contrast the for, while and do-while loops
Use **for** when you know the count or are stepping through indexes; **enhanced for** to visit every element without needing the index; **while** when repeating until a condition changes (zero or more times); **do-while** when the body must run at least once (e.g. a menu or input prompt). Any loop can be rewritten as another; the choice is about clarity.
```java
int i = 0;
while (i < 3) { System.out.print(i); i++; }
System.out.print(" | ");
for (int j = 0; j < 3; j++) System.out.print(j);
System.out.print(" | ");
int m = 0;
do { System.out.print(m); m++; } while (m < 3);
System.out.println();
```
Output:
```
012 | 012 | 012
```

#### 9.6 Develop code that uses break and continue statements
`break` exits the innermost loop (or switch) immediately; `continue` skips the rest of the current pass and goes to the next (in a for loop, the update still runs). A **labelled** break or continue (`outer: for (...)` then `break outer;`) acts on the named outer loop.
```java
for (int i = 1; i <= 10; i++) {
    if (i % 3 == 0) continue;
    if (i > 7) break;
    System.out.print(i + " ");
}
System.out.println();
outer:
for (int a = 1; a <= 3; a++) {
    for (int b = 1; b <= 3; b++) {
        if (b == 2) continue outer;
        if (a == 3) break outer;
        System.out.print(a + "" + b + " ");
    }
}
System.out.println();
```
Output:
```
1 2 4 5 7 
11 21 
```

## Explicitly not here
Iterators over ArrayLists are S09.
