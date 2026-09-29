# S11_Methods - Lesson: Methods: accessors, mutators, overloading and static

## Goal
The learner writes methods with parameters and return values, accessor and mutator methods, overloaded methods, and static methods, and explains pass-by-value.

## Syllabus items taught here
- 13.1 - Describe and create a method
- 13.2 - Create and use accessor and mutator methods
- 13.3 - Create overloaded methods
- 13.4 - Describe a static method and demonstrate its use within a program

## How to teach this
Ask whether a method can change an int passed to it, and then whether it can change an object passed to it. Have the learner predict the output of every example before running it, and compile and run code for real (any JDK; the examples were run on JDK 21 but use only features the Foundations syllabus covers).

#### 13.1 Describe and create a method
A method is declared as `modifiers returnType name(parameters) { body }`. `void` methods return nothing; others must `return` a value of the declared type on every path. The method signature is the name plus parameter types. Java passes arguments **by value**: a method gets a copy of a primitive, so it can't change the caller's variable, and a copy of a reference, so it *can* change the object that reference points to (but not make the caller's variable point elsewhere).
```java
class Tools {
    int square(int n) { return n * n; }
    void tryChange(int n) { n = 100; }
    void grow(int[] arr) { arr[0] = 100; }
}
// ---- main ----
Tools t = new Tools();
int x = 5;
int[] a = {5};
t.tryChange(x);
t.grow(a);
System.out.println(t.square(x) + " " + x + " " + a[0]);
```
Output:
```
25 5 100
```

#### 13.2 Create and use accessor and mutator methods
**Accessors** (getters) return a field's value: `getName()`, or `isActive()` for booleans. **Mutators** (setters) change a field, usually with validation: `setAge(int age)`. With private fields, they control exactly how an object's state is read and changed.
```java
class Person {
    private String name;
    private int age;
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public int getAge() { return age; }
    public void setAge(int age) { if (age >= 0 && age <= 150) this.age = age; }
}
// ---- main ----
Person p = new Person();
p.setName("Lee");
p.setAge(34);
p.setAge(-5);
System.out.println(p.getName() + " " + p.getAge());
```
Output:
```
Lee 34
```

#### 13.3 Create overloaded methods
**Overloaded methods** share a name but differ in parameter list. The compiler picks the best match at compile time: an exact match first, then widening (int to long to double...), then boxing. A different return type alone is not enough to overload: that's a compile error.
```java
class Printer {
    String show(int x) { return "int " + x; }
    String show(double x) { return "double " + x; }
    String show(String s) { return "String " + s; }
    String show(int a, int b) { return "two ints " + (a + b); }
}
// ---- main ----
Printer p = new Printer();
System.out.println(p.show(3) + " | " + p.show(3.0) + " | " + p.show('A') + " | " + p.show("3") + " | " + p.show(1, 2) + " | " + p.show(5L));
```
Output:
```
int 3 | double 3.0 | int 65 | String 3 | two ints 3 | double 5.0
```
```java
class Bad {
    int f(int x) { return x; }
    double f(int x) { return x; }
}
// ---- main ----
System.out.println("never");
```
Output:
```
(does not compile: method f(int) is already defined in class Bad)
```

#### 13.4 Describe a static method and demonstrate its use within a program
A **static** method belongs to the class, not an object: call it as `ClassName.method()` without creating an object (like `Math.sqrt` or `main`). A static method can't use instance fields or `this` directly, because there is no object; it can use static fields and call other static methods. Instance methods can use both.
```java
class Temp {
    static double toF(double c) { return c * 9 / 5 + 32; }
    static int conversions = 0;
    static double convert(double c) { conversions++; return toF(c); }
}
// ---- main ----
System.out.println(Temp.convert(100) + " " + Temp.convert(-40) + " " + Temp.conversions);
```
Output:
```
212.0 -40.0 2
```
```java
class Widget {
    int size = 3;
    static int twice() { return size * 2; }
}
// ---- main ----
System.out.println(Widget.twice());
```
Output:
```
(does not compile: non-static variable size cannot be referenced from a static context)
```

## Explicitly not here
Varargs, generics and lambdas belong to java_se21_developer.
