# S05_Game_Theory_and_Strategic_Behaviour - Test: Game theory and strategic behaviour

## How to run this
A real checkpoint in the style of this stage's real OU module: short calculations with full working, and explain/evaluate questions marked by points, mirroring undergraduate economics assessment. Give the whole test at once, with no hints; the learner may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain the difference between a dominant strategy and a Nash equilibrium. [3 marks]
2. Two symmetric Cournot duopolists face P = 120 - (q1+q2) and MC = 20. Find each firm's reaction function and the Cournot-Nash equilibrium output and price. [5 marks]
3. Explain why cartels (e.g. OPEC) often struggle to sustain the collusive, monopoly-like outcome, using the prisoner's dilemma. [4 marks]
4. In Bertrand competition with identical products, constant marginal cost, and only two firms, which are true? Choose every correct option.
   A. Equilibrium price equals marginal cost
   B. Both firms earn zero economic profit
   C. The outcome resembles perfect competition despite only two firms
   D. Firms can sustain a price above marginal cost indefinitely

## Answer key (for the tutor only)
1. [3] B1 a dominant strategy is best for a player regardless of what rivals do; B1 a Nash equilibrium is a combination of strategies where no player can gain by unilaterally deviating, given the others' actual choices; B1 a game can have a Nash equilibrium with no player having a dominant strategy (each is only best-responding to the specific strategy the other has chosen).
2. [5] M1 firm 1 maximises (120-q1-q2)q1 - 20q1, FOC gives q1 = (100-q2)/2 (reaction function); B1 symmetric for firm 2; M1 solve simultaneously: q = (100-q)/2; A1 q1=q2 = 33.3; A1 P = 120 - 66.7 = 53.3.
3. [4] B1 collusion (restrict output, keep price high) is jointly optimal for cartel members; B1 but each member has an individual incentive to cheat -- produce more than its quota to capture extra sales at the high price; B1 if all members reason this way, output rises and price falls toward the (worse for all) Cournot or competitive outcome; B1 cartels need credible enforcement/punishment (or repeated interaction) to sustain cooperation, which the one-shot prisoner's dilemma logic otherwise undermines.
4. Correct: A, B, C (exactly these options, no others)

## Grading
Apply `rubric.json`'s `stage_rubrics.S05_Game_Theory_and_Strategic_Behaviour` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 13 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S06_Welfare_Economics_and_Market_Failure.
