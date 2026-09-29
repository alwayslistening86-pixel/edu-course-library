# S11_File_Input_Output - Lesson: Files and input/output

## Goal
The learner opens files in the right mode, reads and writes text and binary data, handles I/O errors with errno, and uses bytearray buffers.

## Syllabus items taught here
- 5.4a - I/O modes; text versus binary
- 5.4b - Predefined streams; handles versus streams
- 5.5a - open() and errno values
- 5.5b - close(), read(), write(), readline(), readlines()
- 5.5c - bytearray as an input/output buffer

## How to teach this
Ask what happens to an existing file's contents when you open it with 'w'. Have the learner predict the result of every example before running it, and run code for real whenever they can.

#### 5.4a I/O modes; text versus binary
`open()` modes: `r` read (the default; the file must exist), `w` write (creates, or **truncates** an existing file), `a` append (writes go to the end), `x` exclusive create (fails if the file exists), and `+` for read and write. Add `t` for text (the default: str, with newlines translated and characters decoded) or `b` for binary (raw bytes).
```python
with open("demo.txt", "w") as f:
    f.write("one\n")
with open("demo.txt", "a") as f:
    f.write("two\n")
print(open("demo.txt").read().splitlines())
with open("demo.txt", "w") as f:
    pass
print(repr(open("demo.txt").read()))
try:
    open("demo.txt", "x")
except FileExistsError:
    print("FileExistsError")
```
Output:
```
['one', 'two']
''
FileExistsError
```

#### 5.4b Predefined streams; handles versus streams
A **stream** is the abstract flow of data; a **handle** (file object) is what `open()` returns, and your code uses it to operate on the stream. Three streams are already open when a program starts: `sys.stdin` (keyboard input), `sys.stdout` (normal output, used by print) and `sys.stderr` (error messages).
```python
import sys
n = sys.stdout.write("written via sys.stdout\n")
print(n, "characters written; print() uses the same stream")
print(all(hasattr(s, "write") or hasattr(s, "read") for s in (sys.stdin, sys.stdout, sys.stderr)))
```
Output:
```
written via sys.stdout
23 characters written; print() uses the same stream
True
```

#### 5.5a open() and errno values
Failed I/O raises `OSError` (or a subclass such as FileNotFoundError or PermissionError). Its `errno` attribute is a numeric code, and the `errno` module names them: `errno.ENOENT` (no such file), `errno.EACCES` (permission denied), `errno.EEXIST` (already exists) and others. `os.strerror(code)` gives the text.
```python
import errno, os
try:
    open("missing_file.txt")
except OSError as e:
    print(type(e).__name__, e.errno == errno.ENOENT, os.strerror(e.errno))
```
Output:
```
FileNotFoundError True No such file or directory
```

#### 5.5b close(), read(), write(), readline(), readlines()
`read()` reads everything (or `read(n)`: n characters or bytes); `readline()` reads one line **including** its `\n`, and returns `""` at end of file; `readlines()` returns a list of lines; `write(s)` writes and returns the count written, adding no newline. `close()` releases the file. A `with` block closes it automatically, even after an error.
```python
with open("lines.txt", "w") as f:
    print(f.write("alpha\nbeta\ngamma"))
f = open("lines.txt")
print(repr(f.readline()), repr(f.read(3)), f.readlines())
print(repr(f.readline()))
f.close()
print(f.closed)
```
Output:
```
16
'alpha\n' 'bet' ['a\n', 'gamma']
''
True
```

#### 5.5c bytearray as an input/output buffer
A `bytearray` is a **mutable** sequence of bytes (integers 0-255). In binary mode, `write(bytearray)` writes it, and `readinto(buffer)` fills an existing bytearray in place, returning the number of bytes read.
```python
data = bytearray(4)
for i in range(4):
    data[i] = 65 + i
with open("bin.dat", "wb") as f:
    f.write(data)
buf = bytearray(10)
with open("bin.dat", "rb") as f:
    n = f.readinto(buf)
print(n, buf[:n], bytes(buf[:n]).decode())
```
Output:
```
4 bytearray(b'ABCD') ABCD
```

## Explicitly not here
The os and shutil modules beyond errno and strerror are not on the syllabus.
