# S01_What_Is_Java_and_Java_Basics - Lesson: What Java is, and the basics of a Java program

## Goal
The learner can explain what makes Java distinctive, where it is used, what the JDK and JRE are, the building blocks of object-oriented programs, the parts of a basic program, and how to compile and run one.

## Syllabus items taught here
- 1.1 - Describe the features of Java
- 1.2 - Describe the real-world applications of Java
- 2.1 - Describe the Java Development Kit (JDK) and the Java Runtime Environment (JRE)
- 2.2 - Describe the components of object-oriented programming
- 2.3 - Describe the components of a basic Java program
- 2.4 - Compile and execute a Java program

## How to teach this
Ask what 'write once, run anywhere' could mean, then have the learner type, compile and run a first program by hand. Have the learner predict the output of every example before running it, and compile and run code for real (any JDK; the examples were run on JDK 21 but use only features the Foundations syllabus covers).

#### 1.1 Describe the features of Java
Java is **object-oriented** (programs are built from classes and objects), **platform-independent** (source compiles to *bytecode* that any Java Virtual Machine runs: 'write once, run anywhere'), **strongly and statically typed** (every variable has a declared type checked at compile time), **robust** (automatic memory management with garbage collection, no pointer arithmetic, checked exceptions), **secure** (bytecode verification, no direct memory access), **multithreaded** (built-in support for threads), and has a large **standard library** (the Java API). It is compiled to bytecode and then interpreted or just-in-time (JIT) compiled by the JVM, so it is both compiled and interpreted.

#### 1.2 Describe the real-world applications of Java
Java runs enterprise server applications (banking, e-commerce, back ends built with frameworks like Spring and Jakarta EE), Android apps (written in Java or Kotlin on a Java-derived platform), big-data tools (Hadoop, Kafka, Spark's JVM side), desktop applications (IDEs such as IntelliJ IDEA and Eclipse), embedded and IoT devices, scientific tools, and games (Minecraft Java Edition). Point out the common thread: long-lived, large, portable systems.

#### 2.1 Describe the Java Development Kit (JDK) and the Java Runtime Environment (JRE)
The **JVM** runs bytecode. The **JRE** (Java Runtime Environment) is the JVM plus the core class libraries: enough to *run* Java programs. The **JDK** (Java Development Kit) is the JRE plus development tools: `javac` (the compiler), `java` (the launcher), `jar`, `javadoc`, `jshell` and more: needed to *write and compile* programs. So JDK contains JRE contains JVM. (Since Java 11 Oracle ships only the JDK, but the distinction is still examined.)

#### 2.2 Describe the components of object-oriented programming
A **class** is a blueprint; an **object** is an instance of a class with its own **state** (fields) and **behaviour** (methods). The core OOP principles: **encapsulation** (hide fields, expose methods), **inheritance** (a subclass reuses and extends a superclass), **polymorphism** (one reference type, many actual behaviours), and **abstraction** (show what, hide how).
```java
class Dog {
    String name;
    void bark() { System.out.println(name + " says woof"); }
}
// ---- main ----
Dog d = new Dog();
d.name = "Rex";
d.bark();
```
Output:
```
Rex says woof
```

#### 2.3 Describe the components of a basic Java program
A basic program has: optional `package` and `import` statements; a **class declaration** (`public class Hello`, in a file named `Hello.java`); the **main method** `public static void main(String[] args)`, the entry point; **statements** ending in semicolons; and **blocks** in braces. Comments are ignored by the compiler.
```java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello, Java");
    }
}
```
Here `System.out.println` prints a line; `print` prints without a newline.
```java
System.out.print("A");
System.out.print("B");
System.out.println("C");
System.out.println("D");
```
Output:
```
ABC
D
```

#### 2.4 Compile and execute a Java program
Save as `Hello.java` (the file name must match the public class). Compile with `javac Hello.java`, which produces `Hello.class` (bytecode); run with `java Hello` (the class name, no `.class`). Command-line arguments go after the class name and arrive in `args`: `java Hello Ann 42` gives `args[0]` = "Ann" and `args[1]` = "42" (a String). Since Java 11, `java Hello.java` compiles and runs a single file in one step. A compile error means no .class file; a runtime error happens while `java` runs.

## Explicitly not here
Syntax conventions and comments are S02; variables are S03.
