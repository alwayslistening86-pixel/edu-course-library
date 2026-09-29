# S08_Computability_and_Complexity_Theory - Lesson: Computability and complexity theory

## Goal
The learner relates finite state machines and regular expressions to the Chomsky hierarchy, describes a Turing machine and the Church-Turing thesis, explains the halting problem and sketches why it is undecidable, and distinguishes the complexity classes P, NP, NP-complete and NP-hard.

## Syllabus items taught here
- 8a - Formal languages and automata: finite state machines, regular expressions, an outline of the Chomsky hierarchy
- 8b - Turing machines: definition, the Church-Turing thesis, the universal Turing machine
- 8c - Decidability: the halting problem and a proof sketch of its undecidability
- 8d - Complexity classes: P, NP, NP-complete and NP-hard; the significance of the P vs NP question

## How to teach this
Ask the learner: can we write a general program that takes any other program and its input, and always correctly says whether that program will eventually stop? Most instinctively say yes -- this stage proves it is impossible. Work every algorithm trace, calculation and code example with the learner step by step before revealing the next stage; have the learner predict a program's output before it is run. This is honours-degree material: insist on precise terminology and full justification, not just a right answer. Every computed value, algorithm trace and program output in these files was produced by actually running Python when the course was built, never hand-typed.

#### 8a Formal languages and automata: finite state machines, regular expressions, an outline of the Chomsky hierarchy
**Finite state machines (FSMs).** An FSM consists of a finite set of states, a start state, one or more accepting states, and transitions between states triggered by input symbols; it accepts a string if processing it, symbol by symbol, ends in an accepting state. FSMs recognise exactly the **regular languages** -- the same class of languages describable by **regular expressions** (patterns built from literal symbols, concatenation, alternation `|` and repetition `*`/`+`). The **Chomsky hierarchy** classifies formal languages by the grammars that generate them, in increasing power: *regular* (recognised by an FSM), *context-free* (recognised by a pushdown automaton, an FSM plus a stack -- needed for e.g. matching nested brackets, which a plain FSM cannot do since it cannot count arbitrarily deep nesting), *context-sensitive*, and *unrestricted/recursively enumerable* (recognised by a Turing machine, the most powerful class). Each level strictly contains the languages of the level below it.
```python
import re

pattern = re.compile(r'^a+b+$')  # regular: one or more a's followed by one or more b's
for s in ["aabb", "ab", "abc", "aaabbb", ""]:
    print(s, "matches" if pattern.match(s) else "does not match")
```
Output:
```
aabb matches
ab matches
abc does not match
aaabbb matches
 does not match
```

#### 8b Turing machines: definition, the Church-Turing thesis, the universal Turing machine
**Turing machines.** A Turing machine (TM) has an infinite tape (memory), a read/write head, and a finite set of states with transition rules based on the current state and the symbol under the head; each step it may write a symbol, move the head left or right, and change state. Despite this simplicity, a TM can compute anything any real computer can compute given enough time and memory -- this is the **Church-Turing thesis**: any function that is 'effectively computable' by some mechanical procedure can be computed by a Turing machine (not provable, since 'effectively computable' is an informal notion, but universally accepted and never contradicted). A **universal Turing machine (UTM)** is a single TM that can simulate any other TM given a description of it and its input -- the theoretical ancestor of the general-purpose, stored-program computer: one machine that runs any program, rather than needing a different physical machine built for each task.

#### 8c Decidability: the halting problem and a proof sketch of its undecidability
**The halting problem.** Is there a general algorithm HALT(P, I) that, given any program P and input I, always correctly outputs whether P halts (finishes) or runs forever on I? Turing (1936) proved no such algorithm exists. **Proof sketch (by contradiction, using diagonalisation):** suppose HALT exists. Construct a new program WEIRD(P) that runs HALT(P, P) (does P halt when given itself as input?); if HALT says P halts on P, WEIRD deliberately loops forever; if HALT says P does not halt on P, WEIRD halts immediately. Now ask: does WEIRD(WEIRD) halt? If HALT(WEIRD, WEIRD) says 'halts', then by WEIRD's own definition it loops forever -- contradiction. If HALT(WEIRD, WEIRD) says 'does not halt', then by definition WEIRD halts immediately -- contradiction. Either way, a contradiction follows purely from assuming HALT exists, so no such general algorithm can exist -- the halting problem is **undecidable**. This has a practical consequence: no tool can, in general, perfectly detect infinite loops in arbitrary code (real static analysers must accept false positives, false negatives, or refuse to answer on some inputs).

#### 8d Complexity classes: P, NP, NP-complete and NP-hard; the significance of the P vs NP question
**Complexity classes.** **P** ('polynomial time') is the class of decision problems solvable by a deterministic algorithm in time polynomial in the input size (e.g. sorting, searching, shortest path -- 'efficiently solvable' in the usual theoretical sense). **NP** ('nondeterministic polynomial time') is the class of decision problems whose *proposed solution* can be *verified* in polynomial time, even if finding that solution may take far longer (e.g. given a proposed route, checking it visits every city and has total length <= k is fast, even though the Travelling Salesperson decision problem itself is believed hard to solve). Every problem in P is also in NP (if you can solve it quickly, you can certainly verify a solution quickly). A problem is **NP-complete** if it is in NP and every other NP problem can be reduced to it in polynomial time (so an efficient algorithm for one NP-complete problem would give an efficient algorithm for *all* of NP) -- e.g. Boolean satisfiability (SAT), the travelling salesperson decision problem, graph colouring. A problem is **NP-hard** if it is at least as hard as every NP problem (every NP problem reduces to it in polynomial time), whether or not it is itself in NP (so an NP-hard problem need not even have a solution that is quickly verifiable). The **P vs NP question** -- whether P = NP, i.e. whether every quickly-verifiable problem is also quickly solvable -- is one of the most important open problems in computer science and mathematics (a Clay Millennium Prize problem); most computer scientists believe P != NP, but this remains unproven.

## Explicitly not here
Applied algorithm design and complexity of concrete algorithms (sorting, searching) is S07.
