# S13_IO_and_NIO2 - Lesson: I/O streams, serialization and java.nio.file

## Goal
The learner reads and writes files and the console with byte and character streams, serializes and deserializes objects (including transient fields and constructor behaviour), and uses Path and Files to build, inspect, create, copy, move, walk and delete files and directories.

## Syllabus items taught here
- 9.1 - Read and write console and file data using I/O streams
- 9.2 - Serialize and deserialize Java objects
- 9.3 - Construct, traverse, create, read and write Path objects and their properties using the java.nio.file API

## How to teach this
Ask what `Path.of("a/b/../c").normalize()` and `Path.of("/x/y").relativize(Path.of("/x/z/w"))` give. Have the learner predict the result of every example before running it, and compile and run code for real on a JDK 21 (the answer keys were produced on JDK 21). The real exam's code-reading assumptions (missing imports exist, fragments have supporting code) apply to every item here too.

#### 9.1 Read and write console and file data using I/O streams
**Streams in java.io:** byte streams (`InputStream`/`OutputStream`: `FileInputStream`, `FileOutputStream`, `BufferedInputStream`, `ObjectInputStream`...) and character streams (`Reader`/`Writer`: `FileReader`, `FileWriter`, `BufferedReader` with `readLine()` (null at end), `BufferedWriter` with `newLine()`, `PrintWriter` with `println`/`printf`, `InputStreamReader` bridging bytes to characters). Wrap low-level streams in buffered or higher-level ones, close them with try-with-resources, and pass a `true` append flag to `FileWriter`/`FileOutputStream` to append rather than overwrite. `read()` returns -1 at end of stream. **Console:** `System.out`, `System.err`, `System.in` (wrap in `BufferedReader` or `Scanner`) and `System.console()`, which returns **null** when there's no interactive console (as in an IDE or this runner); `Console.readLine` and `readPassword` (returns `char[]`).
```java
import java.io.*;
// ---- main ----
try (PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter("notes.txt")))) {
    pw.println("line one");
    pw.printf("line %d%n", 2);
}
try (FileWriter fw = new FileWriter("notes.txt", true)) { fw.write("line three\n"); }
int count = 0;
try (BufferedReader br = new BufferedReader(new FileReader("notes.txt"))) {
    String line;
    while ((line = br.readLine()) != null) { count++; System.out.print("[" + line + "]"); }
}
System.out.println(" " + count);
try (OutputStream os = new FileOutputStream("bytes.bin")) { os.write(new byte[]{65, 66, 67}); os.write(300); }
try (InputStream is = new BufferedInputStream(new FileInputStream("bytes.bin"))) {
    int b; StringBuilder sb = new StringBuilder();
    while ((b = is.read()) != -1) sb.append(b).append(' ');
    System.out.println(sb + "| console is " + System.console());
}
BufferedReader in = new BufferedReader(new InputStreamReader(new ByteArrayInputStream("typed input\n".getBytes())));
System.out.println(in.readLine().toUpperCase());
new FileReader("missing.txt");
```
Output:
```
[line one][line 2][line three] 3
65 66 67 44 | console is null
TYPED INPUT
(throws FileNotFoundException: missing.txt (No such file or directory))
```
(`os.write(300)` writes only the low 8 bits, 300 - 256 = 44. `System.console()` is null here; run the program from a terminal to get a Console.)

#### 9.2 Serialize and deserialize Java objects
**Serialization** turns an object graph into bytes with `ObjectOutputStream.writeObject` and back with `ObjectInputStream.readObject` (returns Object; cast it). The class must implement `Serializable` (a marker interface), as must every non-transient field's type, or `NotSerializableException` is thrown. `transient` and `static` fields aren't saved: transient fields come back as defaults (0/false/null). Declare `private static final long serialVersionUID` to control version compatibility. On deserialization **no constructor of the serializable class runs** and field initialisers don't run; only the no-arg constructor of the first **non-serializable** superclass runs. Records are the exception: they're rebuilt through their canonical constructor, so its validation runs.
```java
import java.io.*;
class Base { int baseVal = 7; Base() { System.out.print("Base() "); baseVal = 1; } }
class Account extends Base implements Serializable {
    private static final long serialVersionUID = 1L;
    String owner; transient String password; int visits = 5;
    Account(String o, String p) { owner = o; password = p; visits = 9; System.out.print("Account() "); }
}
record Version(int major) implements Serializable { Version { System.out.print("record-ctor(" + major + ") "); } }
// ---- main ----
Account a = new Account("amy", "s3cret");
a.baseVal = 42;
System.out.println();
try (var out = new ObjectOutputStream(new FileOutputStream("acct.ser"))) { out.writeObject(a); out.writeObject(new Version(3)); }
System.out.println();
try (var in = new ObjectInputStream(new FileInputStream("acct.ser"))) {
    Account b = (Account) in.readObject();
    Version v = (Version) in.readObject();
    System.out.println();
    System.out.println(b.owner + " " + b.password + " " + b.visits + " " + b.baseVal + " " + v);
}
```
Output:
```
Base() Account() 
record-ctor(3) 
Base() record-ctor(3) 
amy null 9 1 Version[major=3]
```
```java
import java.io.*;
class Plain { int x = 1; }
// ---- main ----
try (var out = new ObjectOutputStream(new ByteArrayOutputStream())) { out.writeObject(new Plain()); }
```
Output:
```
(throws NotSerializableException: Plain)
```

#### 9.3 Construct, traverse, create, read and write Path objects and their properties using the java.nio.file API
**Path** (`java.nio.file`) represents a location, which needn't exist: `Path.of("a", "b")` or `Paths.get(...)`. Syntactic operations (no file-system access): `getFileName`, `getParent`, `getRoot`, `getNameCount`, `getName(i)`, `subpath(from, to)`, `isAbsolute`, `resolve` (appends a relative path; an absolute argument wins), `resolveSibling`, `relativize` (both relative or both absolute), `normalize` (removes `.` and `name/..`), `startsWith`/`endsWith` (whole name elements). `toRealPath` does touch the file system (the file must exist).
```java
import java.nio.file.*;
// ---- main ----
Path p = Path.of("docs", "2024", "..", "reports", ".", "q1.txt");
Path n = p.normalize();
System.out.println(p.getNameCount() + " " + n + " " + n.getFileName() + " " + n.getParent() + " " + n.getRoot() + " " + n.subpath(0, 1) + " " + n.getName(1));
Path base = Path.of("/data/app");
System.out.println(base.resolve("logs/x.log") + " " + base.resolve("/etc/hosts") + " " + base.resolveSibling("lib") + " " + Path.of("/x/y").relativize(Path.of("/x/z/w")) + " " + n.startsWith("docs") + " " + n.startsWith("doc") + " " + n.endsWith("q1.txt"));
Path.of("a").relativize(Path.of("/b"));
```
Output:
```
6 docs/reports/q1.txt q1.txt docs/reports null docs reports
/data/app/logs/x.log /etc/hosts /data/lib ../z/w true false true
(throws IllegalArgumentException: 'other' is different type of Path)
```
**Files** does the I/O: `exists`, `isDirectory`, `isRegularFile`, `size`, `createFile` (throws `FileAlreadyExistsException` if present), `createDirectory` / `createDirectories`, `writeString` / `write` / `readString` / `readAllLines` / `lines` (a lazy Stream to close), `newBufferedReader` / `newBufferedWriter`, `copy` and `move` (with `StandardCopyOption.REPLACE_EXISTING`, `ATOMIC_MOVE`...; otherwise an existing target throws), `delete` (throws `NoSuchFileException` if missing, `DirectoryNotEmptyException` for a non-empty directory) and `deleteIfExists`, `list` (one level), `walk` (depth-first, recursive, optional max depth), `find`, `isSameFile`, `getLastModifiedTime`, and `readAttributes(path, BasicFileAttributes.class)`.
```java
import java.nio.file.*;
import java.nio.file.attribute.*;
// ---- main ----
Path root = Path.of("proj");
Files.createDirectories(root.resolve("src/main"));
Files.writeString(root.resolve("src/main/App.java"), "class App {}\n");
Files.write(root.resolve("README.md"), List.of("# Proj", "notes"));
Path copy = Files.copy(root.resolve("README.md"), root.resolve("src/README.bak"));
Files.move(copy, root.resolve("OLD.md"));
try (var s = Files.walk(root)) { System.out.println(s.map(Path::toString).sorted().toList()); }
try (var s = Files.list(root)) { System.out.println(s.map(x -> x.getFileName().toString()).sorted().toList()); }
BasicFileAttributes at = Files.readAttributes(root.resolve("README.md"), BasicFileAttributes.class);
System.out.println(Files.readAllLines(root.resolve("OLD.md")) + " " + at.size() + " " + at.isDirectory() + " " + Files.size(root.resolve("src/main/App.java")) + " " + Files.exists(root.resolve("src/README.bak")) + " " + Files.deleteIfExists(root.resolve("nope")));
try { Files.delete(root.resolve("src")); } catch (DirectoryNotEmptyException e) { System.out.println("not empty: " + e.getFile()); }
Files.copy(root.resolve("README.md"), root.resolve("OLD.md"));
```
Output:
```
[proj, proj/OLD.md, proj/README.md, proj/src, proj/src/main, proj/src/main/App.java]
[OLD.md, README.md, src]
[# Proj, notes] 13 false 13 false false
not empty: proj/src
(throws FileAlreadyExistsException: proj/OLD.md)
```

## Explicitly not here
Reading localised resource bundles from files is S14.
