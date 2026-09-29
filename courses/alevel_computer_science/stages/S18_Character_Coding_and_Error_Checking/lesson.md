# S18_Character_Coding_and_Error_Checking - Lesson: Character encoding and error checking/correction

## Goal
The learner explains character encoding (ASCII and Unicode) and error checking/correction methods.

## Syllabus items taught here
- 4.5.5.1 - Character encoding: ASCII and Unicode
- 4.5.5.3 - Error checking and correction

## How to teach this
Ask the learner why an emoji or a Chinese character can't be stored in the original 7-bit ASCII scheme, but can be stored in Unicode. AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.5.5.1 Character encoding: ASCII and Unicode
Each character needs a numeric **character code** so it can be stored in binary. **ASCII** is a 7-bit (or 8-bit extended) code representing 128 (or 256) characters -- enough for English letters, digits, punctuation and control characters, but not most other scripts. **Unicode** is a much larger character set (over 149,000 characters as of recent versions) covering virtually every writing system and symbol in use, including emoji; its first 128 code points deliberately match ASCII, so ASCII text is also valid Unicode text. Unicode characters are commonly stored using encodings such as **UTF-8** (a variable-length encoding, 1-4 bytes per character, backward-compatible with ASCII for the first 128 characters) or **UTF-16**.

#### 4.5.5.3 Error checking and correction
**Error checking and correction** detects (and sometimes fixes) errors introduced when data is transmitted or stored. A **parity bit** adds one extra bit so the total number of 1-bits is always even (**even parity**) or always odd (**odd parity**); a single-bit error flips the parity, so it can be **detected** (but not, from parity alone, which bit or corrected). *Example:* the byte 01000001 has two 1-bits (even); using even parity, the parity bit added is 0 (keeping the total even); if the byte 01000011 (three 1-bits, odd) was received under an even-parity scheme, an error is detected. A **checksum** sums (or otherwise combines) blocks of data into a single check value sent alongside the data; the receiver repeats the calculation and compares, detecting most errors. More advanced schemes (e.g. Hamming codes, referenced conceptually) can also correct certain errors, not just detect them, by adding enough redundant bits to pinpoint which bit is wrong.

## Explicitly not here
Representing images, sound and other multimedia data is S19.
