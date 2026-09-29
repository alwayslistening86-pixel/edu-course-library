# S13_FSM_Regex_and_BNF - Practice: Finite state machines, regular expressions and BNF/syntax diagrams

## Goal
Low-stakes practice: the learner predicts or attempts each item first, then checks it (by running code, or against the model answer). Mistakes are expected and corrected here, before any grading.

## Practice items
1. An FSM has states S0 (start) and S1 (accepting): on '0' from S0 go to S0, on '1' from S0 go to S1; on '0' from S1 go to S0, on '1' from S1 go to S1. Trace the string "1101" through the FSM and state whether it is accepted. [3 marks]

## Answers (for the tutor; reveal only after a genuine attempt)
1. [3] M1 S0 -1-> S1 -1-> S1 -0-> S0 -1-> S1; A1 ends in S1, the accepting state; B1 accepted (the FSM accepts strings ending in '1', which "1101" does).

## How to run it
One item at a time. For code-output/trace items the learner commits to a prediction before running or checking anything. Offer a worked explanation only after a genuine attempt.

## When to move to test
When the learner gets a new item of each type right without prompting.
