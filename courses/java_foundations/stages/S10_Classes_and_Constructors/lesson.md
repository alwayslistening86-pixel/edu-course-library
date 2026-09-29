# S10_Classes_and_Constructors - Lesson: Classes, objects and constructors

## Goal
The learner writes classes with private fields and constructors (default, no-arg, parameterised and overloaded), creates objects, and distinguishes class, instance and local variables.

## Syllabus items taught here
- 12.1 - Create a new class, including a main method
- 12.2 - Use the private modifier
- 12.3 - Describe the relationship between an object and its members
- 12.4 - Describe the difference between a class variable, an instance variable and a local variable
- 12.5 - Develop code that creates an object's default constructor and modifies the object's fields
- 12.6 - Use constructors with and without parameters
- 12.7 - Develop code that overloads constructors

## How to teach this
Ask what happens to the default constructor the moment you write any constructor of your own. Have the learner predict the output of every example before running it, and compile and run code for real (any JDK; the examples were run on JDK 21 but use only features the Foundations syllabus covers).

#### 12.1 Create a new class, including a main method
A class groups fields and methods. An **executable** class has `public static void main(String[] args)`. A file can hold several classes, but at most one public class, and it must match the file name. Objects are created with `new`, which calls a constructor and returns a reference.
```java
class Counter {
    int value;
    void increment() { value++; }
}
// ---- main ----
Counter c = new Counter();
c.increment(); c.increment();
System.out.println(c.value);
```
Output:
```
2
```

#### 12.2 Use the private modifier
`private` members are visible only inside their own class. Making fields private (encapsulation) forces other classes to use methods, which can validate changes. Accessing a private field from outside is a compile error.
```java
class Account {
    private double balance;
    void deposit(double amt) { if (amt > 0) balance += amt; }
    double getBalance() { return balance; }
}
// ---- main ----
Account a = new Account();
a.deposit(50); a.deposit(-20);
System.out.println(a.getBalance());
```
Output:
```
50.0
```
```java
class Account {
    private double balance;
}
// ---- main ----
Account a = new Account();
a.balance = 1000;
```
Output:
```
(does not compile: balance has private access in Account)
```

#### 12.3 Describe the relationship between an object and its members
An object **has** members: fields (its state) and methods (its behaviour). Each object has its own copy of the instance fields; methods act on the object they are called on (`this`). A variable of a class type holds a **reference** to an object, so two variables can refer to the same object, and a change through one is visible through the other. `null` means no object; using a member through null throws `NullPointerException`.
```java
class Point { int x, y; }
// ---- main ----
Point p = new Point();
Point q = p;
Point r = new Point();
q.x = 5;
System.out.println(p.x + " " + r.x + " " + (p == q) + " " + (p == r));
```
Output:
```
5 0 true false
```

#### 12.4 Describe the difference between a class variable, an instance variable and a local variable
A **class variable** (`static` field) has one copy shared by every object, accessed as `ClassName.var`. An **instance variable** (non-static field) has one copy per object, with default values (0, false, null). A **local variable** is declared inside a method or block, exists only there, has no default, and must be assigned before use. A local variable with the same name as a field **shadows** it; `this.name` reaches the field.
```java
class Student {
    static int count = 0;
    String name;
    int grade;
    Student(String name) { this.name = name; count++; }
    String describe() { String label = name + ":" + grade; return label; }
}
// ---- main ----
Student a = new Student("Ann"), b = new Student("Ben");
b.grade = 90;
System.out.println(a.describe() + " " + b.describe() + " " + Student.count);
```
Output:
```
Ann:0 Ben:90 2
```
```java
int x;
System.out.println(x);
```
Output:
```
(does not compile: variable x might not have been initialized)
```

#### 12.5 Develop code that creates an object's default constructor and modifies the object's fields
If a class declares **no** constructor, the compiler supplies a **default constructor** (no parameters, empty body) and fields keep their default values; you can then set fields on the object. As soon as you write any constructor, the default one is no longer generated.
```java
class Car {
    String make;
    int year;
    boolean electric;
}
// ---- main ----
Car c = new Car();
System.out.println(c.make + " " + c.year + " " + c.electric);
c.make = "Volvo"; c.year = 2022;
System.out.println(c.make + " " + c.year);
```
Output:
```
null 0 false
Volvo 2022
```

#### 12.6 Use constructors with and without parameters
A constructor has the class's name and **no return type** (with a return type it is just a method). A no-arg constructor can set sensible defaults; a parameterised constructor takes initial values. Once a parameterised constructor exists, `new X()` fails unless you also write a no-arg one.
```java
class Lamp {
    boolean on;
    int watts;
    Lamp() { watts = 60; }
    Lamp(boolean on, int watts) { this.on = on; this.watts = watts; }
}
// ---- main ----
Lamp a = new Lamp(), b = new Lamp(true, 100);
System.out.println(a.on + " " + a.watts + " " + b.on + " " + b.watts);
```
Output:
```
false 60 true 100
```
```java
class Box {
    int size;
    Box(int size) { this.size = size; }
}
// ---- main ----
Box b = new Box();
```
Output:
```
(does not compile: constructor Box in class Box cannot be applied to given types;)
```

#### 12.7 Develop code that overloads constructors
**Overloaded constructors** share the class name but differ in parameter list (number, types or order). `this(...)` as the **first** statement calls another constructor of the same class, avoiding duplicated code.
```java
class Rect {
    int w, h;
    Rect() { this(1); System.out.print("[no-arg] "); }
    Rect(int side) { this(side, side); System.out.print("[square] "); }
    Rect(int w, int h) { this.w = w; this.h = h; System.out.print("[full] "); }
    int area() { return w * h; }
}
// ---- main ----
Rect a = new Rect();
Rect b = new Rect(3);
Rect c = new Rect(2, 5);
System.out.println();
System.out.println(a.area() + " " + b.area() + " " + c.area());
```
Output:
```
[full] [square] [no-arg] [full] [square] [full] 
1 9 10
```

## Explicitly not here
Inheritance, interfaces and records belong to java_se21_developer.
