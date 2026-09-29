# S01_What_Is_Java_and_Java_Basics - Test: What Java is, and the basics of a Java program

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. Which are features of Java? Choose every correct option.
   A. Source is compiled to platform-independent bytecode
   B. Memory is freed automatically by garbage collection
   C. Programs can do pointer arithmetic on memory addresses
   D. It supports multithreading in the language and library
2. Which statements about the JDK and JRE are true? Choose every correct option.
   A. The JRE contains the JVM and the core class libraries
   B. The JDK includes the javac compiler
   C. The JRE alone is enough to compile Java source code
   D. The JDK includes everything needed to run Java programs
3. Which is a valid main method for launching a program? Choose every correct option.
   A. `public static void main(String[] args)`
   B. `public void main(String[] args)`
   C. `public static int main(String[] args)`
   D. `static public void main(String args)`
4. A class Report is saved in Report.java. Which command runs it after compiling? Choose every correct option.
   A. java Report
   B. java Report.class
   C. javac Report
   D. run Report.java
5. Which OOP idea is shown by making fields private and providing public methods to use them? Choose every correct option.
   A. `Encapsulation`
   B. `Inheritance`
   C. `Polymorphism`
   D. `Compilation`
6. What is the output? If it does not compile, or throws, say so and why.
```java
System.out.print("Java");
System.out.println(" is");
System.out.print("fun");
System.out.println();
System.out.println("!");
```
7. Which are common real-world uses of Java? Choose every correct option.
   A. Server-side enterprise applications
   B. Android app development
   C. `Writing the firmware of a CPU's microcode`
   D. Big-data processing tools such as Hadoop and Kafka

## Answer key (for the tutor only)
1. Correct: A, B, D (exactly these options, no others)
2. Correct: A, B, D (exactly these options, no others)
3. Correct: A (exactly these options, no others)
4. Correct: A (exactly these options, no others)
5. Correct: A (exactly these options, no others)
6. Actual result (from running it):
```
Java is
fun
!
```
7. Correct: A, B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S01_What_Is_Java_and_Java_Basics` exactly. 7 items; a pass needs at least 5 fully correct (65%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S02_Basic_Java_Elements.
