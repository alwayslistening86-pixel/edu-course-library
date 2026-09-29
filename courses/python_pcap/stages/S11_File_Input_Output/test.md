# S11_File_Input_Output - Test: Files and input/output

## How to run this
A real checkpoint in the style of the certification's items (code-output, multiple-select and short code-writing). Give all the items at once, with no hints and no running of code until every answer is in. Then grade against this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
with open('t.txt', 'w') as f:
    n = f.write('hello')
print(n)
with open('t.txt', 'a') as f:
    f.write(' world')
print(open('t.txt').read())
```
2. What does this print? (If it raises an error, name it.)
```python
open('t.txt', 'w').write('x\ny\nz')
f = open('t.txt')
print(repr(f.readline()), f.readlines(), repr(f.read()))
f.close()
```
3. What does this print? (If it raises an error, name it.)
```python
with open('b.bin', 'wb') as f:
    f.write(bytearray([72, 105]))
with open('b.bin', 'rb') as f:
    d = f.read()
print(d, type(d).__name__, d.decode())
```
4. What does this print? (If it raises an error, name it.)
```python
buf = bytearray(3)
open('c.bin', 'wb').write(b'ABCDE')
with open('c.bin', 'rb') as f:
    print(f.readinto(buf), buf)
```
5. What does this print? (If it raises an error, name it.)
```python
open('e.txt', 'w').close()
try:
    open('e.txt', 'x')
except OSError as e:
    import errno
    print(type(e).__name__, e.errno == errno.EEXIST)
```
6. Which are predefined streams in sys? Choose every correct option.
   A. `stdin`
   B. `stdout`
   C. `stderr`
   D. `stdfile`
7. Which are true of text mode compared with binary mode? Choose every correct option.
   A. Text mode reads str, binary mode reads bytes
   B. Opening with 'w' in either mode truncates an existing file
   C. `readinto() needs a binary-mode handle`
   D. Binary mode translates newline characters
8. Write code that copies a text file line by line to a new file, numbering each line ('1: ...'), and reports a missing source file by printing the errno name.

## Answer key (for the tutor only)
1. Actual result (from running it):
```
5
hello world
```
2. Actual result (from running it):
```
'x\n' ['y\n', 'z'] ''
```
3. Actual result (from running it):
```
b'Hi' bytes Hi
```
4. Actual result (from running it):
```
3 bytearray(b'ABC')
```
5. Actual result (from running it):
```
FileExistsError True
```
6. Correct: A, B, C (exactly these options, no others)
7. Correct: A, B, C (exactly these options, no others)
8. The tutor runs or reads the learner's answer and checks: Opens source for read and target for write; loops over lines; handles OSError with errno.errorcode[e.errno] or equivalent.

## Grading
Apply `rubric.json`'s `stage_rubrics.S11_File_Input_Output` exactly. 8 items; a pass needs at least 6 fully correct (70%, rounded up). Record `pass` or `fail` in `syllabus_status`, with a short honest note on which items were missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass. Every stage is now passed, so the cumulative exam becomes available.
