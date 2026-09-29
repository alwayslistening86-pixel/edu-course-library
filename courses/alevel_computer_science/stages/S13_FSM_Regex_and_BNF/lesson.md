# S13_FSM_Regex_and_BNF - Lesson: Finite state machines, regular expressions and BNF/syntax diagrams

## Goal
The learner draws/interprets finite state machines, uses set notation, writes and relates regular expressions to finite state machines, and checks language syntax using BNF/syntax diagrams.

## Syllabus items taught here
- 4.4.2.1 - Finite state machines
- 4.4.2.2 - Set notation for regular expressions
- 4.4.2.3 - Regular expressions and regular languages
- 4.4.3.1 - Backus-Naur Form and syntax diagrams

## How to teach this
Ask the learner to imagine a simple turnstile: locked, until a coin is inserted (unlocks), until it is pushed through (locks again) -- that's a finite state machine with two states. AQA's A-level Paper 1 is an on-screen exam: the learner writes, adapts and runs real code in a skeleton program, in one of AQA's four supported languages (C#, Java, Python, VB.Net) -- Python is used throughout this course so code can be run for real and its output verified, which is also one of AQA's own supported choices. Paper 1 also includes algorithm-tracing and theory-of-computation questions (4.3, 4.4) answered in AQA's own pseudo-code on paper within the on-screen exam, not in the candidate's chosen language; show the learner both the runnable Python and the equivalent AQA pseudo-code for any algorithm likely to be traced or written from scratch (searches, sorts, traversals, FSMs, Turing-machine transition tables). Paper 2 is a conventional written exam with no code execution, covering the theory sections (4.5-4.12). Have the learner predict output/traces before running or checking anything. Binary/hex conversions, two's-complement and floating-point workings, Big-O comparisons, truth tables and algorithm traces were computed/verified when this course was built.

#### 4.4.2.1 Finite state machines
A **finite state machine (FSM)** is a model of computation with a finite set of **states**, one of which is the **start state**, and (usually) one or more **accepting (final) states**; **transitions** between states are triggered by input symbols. Shown as a **state transition diagram** (circles for states, double circles for accepting states, labelled arrows for transitions) or a **state transition table** (rows = states, columns = input symbols, cells = the resulting state). *Example:* an FSM accepting binary strings ending in '1' has two states (S0 start/non-accepting, S1 accepting); on input '0' stay/return to S0, on input '1' go to S1; the string "101" ends in S1 (accepted), "100" ends in S0 (rejected).

#### 4.4.2.2 Set notation for regular expressions
**Set notation** describes a collection of distinct values: `{1, 2, 3}` lists elements explicitly; `{x | x is even}` describes a set by a rule (read "the set of all x such that x is even"); `∅` or `{}` is the **empty set**. Sets can be **finite** (a fixed number of elements), **infinite**, or **countably infinite** (can be listed 1st, 2nd, 3rd, ... even though the list never ends, e.g. the natural numbers). A **subset** (`⊆`) contains only elements also in another set; a **proper subset** (`⊂`) is a subset that is not equal to the whole set. Set operations: **union** (`∪`, all elements in either set), **intersection** (`∩`, only elements in both sets), **difference** (`-`, elements in the first set but not the second), and **membership** (`∈`, is this element in this set?).

#### 4.4.2.3 Regular expressions and regular languages
A **regular expression (regex)** is a compact notation describing a **set** of strings (a **language**) using literal characters plus operators such as `*` (zero or more repeats), `+` (one or more repeats), `|` (alternation/or), and brackets for grouping. *Example:* `a(b|c)*` describes all strings starting with 'a' followed by any number (including zero) of 'b's and 'c's in any order/mixture, e.g. "a", "abc", "acbb". Every regular expression can be converted to an equivalent FSM that accepts exactly the strings it describes, and vice versa -- they are two representations of the same underlying idea. A language describable by some regular expression (equivalently, accepted by some FSM) is called a **regular language**.

#### 4.4.3.1 Backus-Naur Form and syntax diagrams
**Backus-Naur Form (BNF)** defines a language's **syntax** (its valid structure) using **production rules** of the form `<non-terminal> ::= expression`, where `|` separates alternatives. *Example:* `<digit> ::= 0|1|2|3|4|5|6|7|8|9` and `<integer> ::= <digit> | <digit><integer>` together define any non-negative whole number as one digit, or a digit followed by another (shorter) integer -- so "247" is valid ('2' followed by the integer "47", itself '4' followed by the integer "7"). A **syntax diagram** shows the same rules visually, as a flowchart-like path through the valid structure. BNF's advantage over a regular expression is that its rules can refer to each other (including themselves, recursively, as `<integer>` does above), letting it describe more complex, nested structures (like a whole programming language's grammar) that regular expressions cannot.

## Explicitly not here
How efficient different algorithms are (Big-O), and the theoretical limits of what can be computed at all, are S14.
