# S13_IO_and_NIO2 - Test: I/O streams, serialization and java.nio.file

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What is the output? If it does not compile, or throws, say so and why.
```java
import java.nio.file.*;
// ---- main ----
Path a = Path.of("/home/u/docs");
Path b = Path.of("/home/u/pics/cat.png");
System.out.println(a.relativize(b) + " " + a.resolve(b.getFileName()) + " " + Path.of("x/./y/../z").normalize() + " " + Path.of("a/b").resolve("/c"));
```
2. What is the output? If it does not compile, or throws, say so and why.
```java
import java.nio.file.*;
// ---- main ----
Path f = Path.of("data.txt");
Files.writeString(f, "v1");
Files.writeString(f, "v2", StandardOpenOption.APPEND);
Files.copy(f, Path.of("copy.txt"));
Files.writeString(f, "v3");
System.out.println(Files.readString(f) + " " + Files.readString(Path.of("copy.txt")) + " " + Files.isSameFile(f, Path.of("./data.txt")));
Files.copy(f, Path.of("copy.txt"));
```
3. What is the output? If it does not compile, or throws, say so and why.
```java
import java.nio.file.*;
// ---- main ----
Files.createDirectories(Path.of("t/a/b"));
Files.writeString(Path.of("t/a/b/f.txt"), "hi");
Files.writeString(Path.of("t/g.txt"), "hi");
try (var s = Files.walk(Path.of("t"), 2)) { System.out.println(s.map(Path::toString).sorted().toList()); }
try (var s = Files.find(Path.of("t"), 10, (p, attr) -> attr.isRegularFile())) { System.out.println(s.count()); }
```
4. What is the output? If it does not compile, or throws, say so and why.
```java
import java.io.*;
// ---- main ----
try (var w = new BufferedWriter(new FileWriter("o.txt"))) { w.write("a"); w.newLine(); w.write("b"); }
try (var r = new BufferedReader(new FileReader("o.txt"))) {
    System.out.println(r.readLine() + r.readLine() + r.readLine());
}
```
5. What is the output? If it does not compile, or throws, say so and why.
```java
import java.io.*;
class Cfg implements Serializable {
    String name = "default";
    transient int cache = 99;
    static int shared = 1;
    Cfg() { name = "ctor"; }
}
// ---- main ----
Cfg c = new Cfg();
c.name = "saved"; c.cache = 5;
try (var out = new ObjectOutputStream(new FileOutputStream("c.ser"))) { out.writeObject(c); }
Cfg.shared = 2;
try (var in = new ObjectInputStream(new FileInputStream("c.ser"))) {
    Cfg d = (Cfg) in.readObject();
    System.out.println(d.name + " " + d.cache + " " + Cfg.shared);
}
```
6. What is the output? If it does not compile, or throws, say so and why.
```java
import java.nio.file.*;
// ---- main ----
Files.delete(Path.of("no-such-file.txt"));
```
7. Which are true? (choose two) Choose every correct option.
   A. Path.of("a").normalize() checks that the file exists
   B. `System.console() may return null`
   C. BufferedReader.readLine returns null at end of stream
   D. transient fields are restored to their saved values

## Answer key (for the tutor only)
1. Actual result (from running it):
```
../pics/cat.png /home/u/docs/cat.png x/z /c
```
2. Actual result (from running it):
```
v3 v1v2 true
(throws FileAlreadyExistsException: copy.txt)
```
3. Actual result (from running it):
```
[t, t/a, t/a/b, t/g.txt]
2
```
4. Actual result (from running it):
```
abnull
```
5. Actual result (from running it):
```
saved 0 2
```
6. Actual result (from running it):
```
(throws NoSuchFileException: no-such-file.txt)
```
7. Correct: B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S13_IO_and_NIO2` exactly. 7 items; a pass needs at least 5 fully correct (68%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S14_Localization_and_Logging.
