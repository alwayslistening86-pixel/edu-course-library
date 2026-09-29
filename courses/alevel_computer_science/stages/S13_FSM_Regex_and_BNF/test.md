# S13_FSM_Regex_and_BNF - Test: Finite state machines, regular expressions and BNF/syntax diagrams

## How to run this
A real checkpoint in the style of AQA's papers: a mix of multiple-choice, short-answer, code-tracing/ writing and longer written questions, with marks shown. Give the whole test at once, with no hints and no running of code until every answer is in. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. For the sets A = {2, 4, 6, 8} and B = {4, 8, 12}, state A union B, A intersection B, and A - B (A difference B). [3 marks]
2. Explain what the regular expression b*a+ describes, and give one string it matches and one it does not. [3 marks]
3. Using the BNF rules <digit> ::= 0|1|...|9 and <integer> ::= <digit> | <digit><integer>, explain how "53" is shown to be a valid <integer>. [3 marks]
4. Explain the relationship between finite state machines and regular expressions. [2 marks]
5. Why is BNF able to describe more complex language structures than a regular expression can? Choose every correct option.
   A. its production rules can refer to other rules, including themselves recursively, allowing nested structure
   B. it can only describe a finite list of exact strings
   C. it does not support alternatives (the | operator)
   D. it can only be used for numeric data types

## Answer key (for the tutor only)
1. [3] B1 A union B = {2, 4, 6, 8, 12}; B1 A intersection B = {4, 8}; B1 A - B = {2, 6}.
2. [3] B1 zero or more b's followed by one or more a's; B1 a valid matching string, e.g. "bba" or "a"; B1 a non-matching string, e.g. "ab" (an a followed by a b is not described) or "" the empty string (needs at least one a).
3. [3] B1 '5' is a valid <digit>, and '3' is a valid <digit> which is therefore also a valid <integer> (the base case of the rule); B1 so <digit><integer> matches '5' followed by the <integer> '3', giving "53"; B1 this recursive rule can build any length of digit string this way.
4. [2] B1 every regular expression can be converted into an equivalent FSM that accepts exactly the strings it describes, and every FSM's accepted language can be described by some regular expression; B1 they are two different (interchangeable) ways of specifying the same regular language.
5. Correct: A (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S13_FSM_Regex_and_BNF` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 12 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S14_Complexity_and_Turing_Machines.
