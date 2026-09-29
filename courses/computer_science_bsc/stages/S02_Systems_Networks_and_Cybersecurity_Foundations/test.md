# S02_Systems_Networks_and_Cybersecurity_Foundations - Test: Systems, networks and cybersecurity foundations

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems, code-trace/code-output items, multiple-select conceptual items and, where the topic is genuinely discursive (professional/ethical/HCI content), extended-response items marked on levels. Give the whole test at once, with no hints; the learner shows full working/code. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. What does this print? (If it raises an error, name it.)
```python
import sys
print((5).bit_length())
print((256).bit_length())
```
2. Explain why 0.1 + 0.2 does not print exactly 0.3 in Python, referring to IEEE 754 representation. [3 marks]
3. A UTF-8 encoded text file starts with the byte sequence for an ASCII letter followed by a 3-byte sequence for another character. Explain why UTF-8 can represent both in the same file without ambiguity. [3 marks]
4. Distinguish client-server and peer-to-peer network architectures, giving one advantage of each. [4 marks]
5. An organisation suffers a distributed denial-of-service attack against its public website. State which element of the CIA triad this primarily attacks, and explain why it is that element rather than confidentiality. [3 marks]
6. Which statements correctly distinguish authentication from authorisation? Choose every correct option.
   A. Authentication establishes who a user is; authorisation establishes what that user may do
   B. A user can be authenticated correctly but still be denied authorisation for a specific action
   C. Authorisation must always happen before authentication
   D. A password is a mechanism used for authentication, not authorisation

## Answer key (for the tutor only)
1. Actual result (from running it):
```
3
9
```
2. [3] B1 floats are stored in binary using a fixed number of mantissa bits (sign/exponent/mantissa, IEEE 754); B1 0.1 and 0.2 have no exact finite binary fraction representation, so each is stored as the nearest representable approximation; B1 adding two such approximations produces a tiny rounding error, giving a result that differs from the exact decimal 0.3 at the level of floating-point precision.
3. [3] B1 UTF-8 is a variable-length encoding: ASCII characters (code points 0-127) are encoded in exactly 1 byte, identical to plain ASCII; B1 non-ASCII characters use 2, 3 or 4 bytes, with leading bits in the first byte of a multi-byte sequence marking how many continuation bytes follow; B1 continuation bytes have a reserved bit pattern (10......) that cannot be confused with the start of a new character, so a decoder can always tell where one character ends and the next begins.
4. [4] B1 client-server: clients request services from a central, dedicated server; B1 advantage: centralised, easier to secure/manage/update; B1 peer-to-peer: nodes act as both client and server to each other, with no central server; B1 advantage: no single point of failure, and it can scale its total capacity as more peers join.
5. [3] B1 availability; B1 because a DDoS attack floods the system with traffic/requests so legitimate users cannot access it, rather than reading or exfiltrating any data; B1 confidentiality would instead be attacked by, e.g., unauthorised access to or theft of stored data, which a pure DDoS does not attempt.
6. Correct: A, B, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S02_Systems_Networks_and_Cybersecurity_Foundations` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 15 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S03_Discrete_Mathematics_for_Computing.
