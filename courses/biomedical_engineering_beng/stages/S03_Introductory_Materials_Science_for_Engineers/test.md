# S03_Introductory_Materials_Science_for_Engineers - Test: Introductory Materials Science for Engineers

## How to run this
A real checkpoint in the style of a UK engineering degree's structured written papers: short-answer and calculation questions with marks shown (M/A/B tagged in the mark scheme), plus some multiple-select items. Give the whole test at once, with no hints; the learner shows working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A cortical bone specimen of original length 40 mm and cross-sectional area 30 mm^2 is stretched by 0.12 mm under a load of 600 N (within the elastic region). Calculate the stress, the strain and the Young's modulus. [4 marks]
2. Sketch (in words) and explain the key features of a ductile metal's stress-strain curve from the origin to fracture, naming each feature. [4 marks]
3. Which of the following are typically true of ceramics compared with metals? Choose every correct option.
   A. Higher stiffness (Young's modulus)
   B. Greater ductility before fracture
   C. Lower fracture toughness
   D. Better wear resistance
4. Explain, using the concept of a stress concentration and cyclic loading, why an orthopaedic implant is more likely to fail by fatigue than by exceeding its static ultimate tensile strength. [3 marks]
5. A UHMWPE component (Young's modulus 1.0 GPa) and a titanium alloy component (Young's modulus 110 GPa) are each loaded to the same strain of 0.5%. Calculate the stress each carries, and state which is more prone to load-related failure in this comparison. [3 marks]

## Answer key (for the tutor only)
1. [4] M1 sigma = F/A = 600/(30e-6) = 20.0 MPa; M1 strain = 0.12/40 = 0.0030; A1 E = sigma/strain; A1 = 6.67 GPa.
2. [4] B1 linear elastic region from the origin, gradient = Young's modulus; B1 yield point where the curve departs from linearity, onset of permanent (plastic) deformation; B1 rise to a maximum, the ultimate tensile strength (UTS); B1 necking (localised reduction in area) with falling engineering stress until fracture.
3. Correct: A, C, D (exactly these options, no others)
4. [3] B1 walking loads the implant on the order of a million cycles per year, each well below the static UTS; B1 a microscopic crack initiates at a stress concentration (surface defect, sharp corner, porosity) and grows a small amount each cycle; B1 the crack eventually reaches a critical size and the remaining cross-section fails suddenly, at a stress far below the static UTS.
5. [3] M1 sigma = E x strain for each; A1 UHMWPE: 1.0e9 x 0.005 = 5.0 MPa; A1 Ti alloy: 110e9 x 0.005 = 550 MPa (the titanium carries far more stress for the same strain, since stiffness, not failure per se, is being compared here).

## Grading
Apply `rubric.json`'s `stage_rubrics.S03_Introductory_Materials_Science_for_Engineers` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 15 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S04_Engineering_Design_Process_for_Healthcare.
