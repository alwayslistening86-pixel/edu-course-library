# S08_Computability_and_Complexity_Theory - Test: Computability and complexity theory

## How to run this
A real checkpoint in the style of OU-module-level questions: structured problems, code-trace/code-output items, multiple-select conceptual items and, where the topic is genuinely discursive (professional/ethical/HCI content), extended-response items marked on levels. Give the whole test at once, with no hints; the learner shows full working/code. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain, in your own words, what the Church-Turing thesis claims, and state why it cannot be formally proved. [3 marks]
2. Summarise the proof (by contradiction/diagonalisation) that the halting problem is undecidable, in your own words, naming the key contradiction reached. [6 marks]
3. Give a real-world practical consequence of the undecidability of the halting problem for software tools. [2 marks]
4. Explain the difference between a problem being 'in NP' and a problem being 'NP-complete'. [4 marks]
5. Explain why finding an efficient (polynomial-time) algorithm for a single NP-complete problem would be an extraordinary result, referring to the definition of NP-completeness. [3 marks]
6. Which statements about complexity classes are correct? Choose every correct option.
   A. Every problem in P is also in NP
   B. A problem being NP-hard means it must itself be in NP
   C. `It is currently unknown whether P = NP`
   D. Boolean satisfiability (SAT) is a well-known NP-complete problem

## Answer key (for the tutor only)
1. [3] B1 it claims that any function that is 'effectively/mechanically computable' by some well-defined step-by-step procedure can be computed by a Turing machine; B1 it is a claim relating an informal, intuitive notion ('effectively computable') to a precise formal one (Turing machine computability), so there is no formal object corresponding to the informal side to prove the equivalence rigorously against; B1 it is instead accepted because every alternative formal model of computation proposed (e.g. lambda calculus, general recursive functions) has been proved exactly equivalent in power to Turing machines, and no broader notion of mechanical computability has ever been found.
2. [6] B1 assumes for contradiction that a general algorithm HALT(P, I) exists that always correctly decides whether program P halts on input I; B1 constructs a new program WEIRD(P) that calls HALT(P, P) and does the opposite of what it reports (loops forever if HALT says P halts on itself, halts immediately if HALT says P does not); B1 asks whether WEIRD(WEIRD) halts; B1 if HALT says it halts, then by WEIRD's own construction it must loop forever -- a contradiction; B1 if HALT says it does not halt, then by construction it halts immediately -- a contradiction; B1 concludes the assumption that HALT exists must be false, so no general halting-detection algorithm can exist.
3. [2] B1 no static-analysis tool or compiler can, in general, perfectly detect all infinite loops (or perfectly prove program termination) for arbitrary code; B1 such tools must accept some limitation -- false positives, false negatives, or refusing to give an answer on some inputs -- rather than a universally correct answer.
4. [4] B2 a problem is in NP if a proposed solution to it can be verified in polynomial time, even if no efficient way to find that solution is known (B1 if stated without the verification-not-solving distinction); B2 a problem is NP-complete if it is in NP AND every other problem in NP can be reduced to it in polynomial time, meaning it is, in a precise sense, at least as hard as any problem in NP (B1 if only 'it is a hard NP problem' is stated without the reduction/universality property).
5. [3] B1 by the definition of NP-completeness, every problem in NP can be reduced to that NP-complete problem in polynomial time; B1 so an efficient (polynomial-time) algorithm for it could be combined with those reductions to give an efficient algorithm for every problem in NP; B1 this would prove P = NP, resolving one of the most significant open problems in computer science and having enormous practical consequences (e.g. for cryptography, which relies on some problems being hard).
6. Correct: A, C, D (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S08_Computability_and_Complexity_Theory` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 19 marks in all; a pass needs at least 12 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S09_Computer_Systems_and_Architecture.
