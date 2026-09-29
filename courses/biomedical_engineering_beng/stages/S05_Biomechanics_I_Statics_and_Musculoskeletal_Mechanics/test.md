# S05_Biomechanics_I_Statics_and_Musculoskeletal_Mechanics - Test: Biomechanics I: Statics and Musculoskeletal Mechanics

## How to run this
A real checkpoint in the style of a UK engineering degree's structured written papers: short-answer and calculation questions with marks shown (M/A/B tagged in the mark scheme), plus some multiple-select items. Give the whole test at once, with no hints; the learner shows working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A forearm (weight 15 N, centre of mass 15 cm from the elbow) holds a 40 N weight at 35 cm from the elbow. The biceps tendon inserts 5 cm from the elbow. Taking moments about the elbow, calculate the biceps muscle force, then find the vertical joint reaction force at the elbow. [5 marks]
2. Explain, using the lever-class concept, why the human forearm is mechanically inefficient as a lever for lifting, and state the compensating advantage this arrangement gives. [3 marks]
3. Which of the following increase the muscle force required to support a given load held in the hand, for a fixed load and forearm geometry? Choose every correct option.
   A. Increasing the distance of the load from the elbow
   B. Decreasing the muscle insertion's moment arm from the elbow
   C. Increasing the muscle insertion's moment arm from the elbow
   D. Decreasing the distance of the load from the elbow
4. A 700 N (body weight) person's ground reaction force during the push-off peak of walking is measured at 1.15 x body weight. Calculate this force in newtons, and briefly state why joint reaction forces higher up the leg (e.g. at the hip) during more demanding activities such as running can exceed several times body weight even though ground reaction force is 'only' slightly above body weight in walking. [3 marks]
5. Using standard anthropometric fractions, estimate the mass of the forearm segment (as 1.6% of total body mass) for a person of mass 80 kg, and the weight (N) this represents (g = 9.81 N/kg). [3 marks]

## Answer key (for the tutor only)
1. [5] M1 moments about elbow: F x 0.05 = 15 x 0.15 + 40 x 0.35; M1 RHS = 16.25; A1 F = 325.0 N; M1 vertical equilibrium: F = R + 15 + 40 (R downward reaction from joint on forearm, or R = F - 15 - 40 upward from forearm on joint depending on convention -- state one consistently); A1 R = 270.0 N (joint must react to almost the full muscle force plus the weights).
2. [3] B1 the elbow flexion system is a third-class lever (effort/muscle between the fulcrum/elbow and the load/hand), so the muscle force required always exceeds the load; B1 this is mechanically inefficient in terms of force; B1 the compensating advantage is range and speed of motion: a small muscle contraction (shortening) produces a much larger displacement and speed at the hand.
3. Correct: A, B (exactly these options, no others)
4. [3] M1 GRF = 1.15 x 700; A1 = 805 N; B1 internal joint reaction forces also include the (often much larger) muscle forces needed for moment equilibrium at each joint (as in BM1-3/BM1-4), and running increases both the ground reaction force and the required muscle forces well beyond walking values.
5. [3] M1 mass = 0.016 x 80 = 1.28 kg; M1 weight = mass x g; A1 = 12.56 N.

## Grading
Apply `rubric.json`'s `stage_rubrics.S05_Biomechanics_I_Statics_and_Musculoskeletal_Mechanics` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 15 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S06_Biomechanics_II_Mechanics_of_Biological_Tissue.
