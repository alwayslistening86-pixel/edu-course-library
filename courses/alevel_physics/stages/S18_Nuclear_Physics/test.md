# S18_Nuclear_Physics - Test: Nuclear physics

## How to run this
A real checkpoint in the style of AQA's papers: structured questions with marks shown (and some multiple choice). Give the whole test at once, with no hints; the learner shows working and may use a calculator and the data booklet. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Iodine-131 has a half-life of 8.0 days. Calculate the number of nuclei in a sample of activity 5.0 MBq, and the activity 30 days later. [4 marks]
2. Calculate the binding energy per nucleon of iron-56 (nuclear mass 55.92068 u; m_p = 1.00728 u, m_n = 1.00867 u). [3 marks]
3. Describe the roles of the moderator, the control rods and the coolant in a thermal fission reactor. [3 marks]
4. Explain what Rutherford concluded from the observation that a very small fraction of alpha particles were scattered through more than 90°. [2 marks]
5. A gamma source gives a corrected count rate of 240 counts per minute at 0.10 m from a detector. Estimate the count rate at 0.30 m, stating the assumption. [2 marks]
6. Uranium-238 (Z = 92) decays by alpha emission and then by two beta-minus decays. State the proton and nucleon numbers of the final nucleus. [2 marks]
7. Explain what the decay constant represents in terms of probability, and why the activity of a large sample is predictable when individual decays are not. [2 marks]

## Answer key (for the tutor only)
1. [4] M1 λ = ln2/(8 x 86400) = 1.003 x 10^-6 s^-1; A1 N = A/λ = 4.99 x 10^12; M1 A = 5.0 e^(-λ x 30 days); A1 0.37 MBq.
2. [3] M1 mass defect = 26(1.00728) + 30(1.00867) - 55.92068 = 0.52870 u; M1 x 931.5; A1 8.79 MeV per nucleon.
3. [3] B1 moderator slows neutrons (by elastic collisions) so they are likely to cause fission; B1 control rods absorb neutrons to control the rate (so each fission causes on average one further fission); B1 coolant carries heat from the core to the heat exchanger.
4. [2] B1 the positive charge and most of the mass are concentrated; B1 in a tiny nucleus (much smaller than the atom).
5. [2] M1 inverse square: (1/3)^2; A1 about 27 counts per minute (assuming a point source and negligible absorption in air).
6. [2] B1 A = 234; B1 Z = 92 (uranium-234).
7. [2] B1 λ is the probability that a given nucleus decays per unit time; B1 with very many nuclei, the proportion decaying per unit time is close to λ (random fluctuations are relatively small).

## Grading
Apply `rubric.json`'s `stage_rubrics.S18_Nuclear_Physics` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 18 marks in all; a pass needs at least 11 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S19_Astrophysics_Telescopes.
