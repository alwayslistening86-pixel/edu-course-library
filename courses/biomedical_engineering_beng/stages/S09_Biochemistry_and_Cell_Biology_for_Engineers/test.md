# S09_Biochemistry_and_Cell_Biology_for_Engineers - Test: Biochemistry and Cell Biology for Engineers

## How to run this
A real checkpoint in the style of a UK engineering degree's structured written papers: short-answer and calculation questions with marks shown (M/A/B tagged in the mark scheme), plus some multiple-select items. Give the whole test at once, with no hints; the learner shows working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. An enzyme has Vmax = 5.0 micromol/min and Km = 1.5 mM. Calculate the reaction rate at substrate concentrations of (a) 0.3 mM and (b) 15 mM, and comment on the kinetic regime in each case. [4 marks]
2. Explain why a drug-delivery device's release rate, measured as perfectly steady (zero-order) in a saline beaker, might become unpredictable once implanted in the body, referring to at least two biochemical/cellular factors from this stage. [3 marks]
3. Which of the following are examples of active transport (as distinct from passive or facilitated diffusion)? Choose every correct option.
   A. The Na+/K+ pump moving ions against their concentration gradients using ATP
   B. Oxygen diffusing from alveolar air into pulmonary capillary blood down its partial-pressure gradient
   C. Glucose moving through a specific membrane channel protein down its concentration gradient
   D. A pump actively transporting a drug molecule into a cell against its concentration gradient, consuming ATP
4. A tissue-engineering scaffold is seeded with cells. Explain, using the concept of mechanotransduction, why the scaffold's mechanical stiffness is a biochemical/cell-signalling design requirement and not only a structural one. [3 marks]
5. A biosensor detects a specific target DNA sequence via complementary base-pair hybridisation. Explain briefly what property of DNA base pairing makes this detection method specific to one target sequence. [2 marks]

## Answer key (for the tutor only)
1. [4] M1 v = Vmax[S]/(Km+[S]); A1 (a) v = 5.0x0.3/(1.5+0.3) = 0.83 micromol/min, well below Vmax, roughly first-order regime ([S] << Km is not quite met here but rate is well below Vmax); A1 (b) v = 5.0x15/(1.5+15) = 4.55 micromol/min, close to Vmax, approaching the zero-order/saturated regime ([S] >> Km); B1 the comparison shows the same enzyme's rate law shifts from roughly first-order to roughly zero-order behaviour purely as a function of substrate concentration relative to Km.
2. [3] B1 the body's biochemical environment includes enzymes that may degrade the drug or the delivery vehicle at a rate the beaker test did not include; B1 cells and the extracellular matrix immediately surrounding the implant can respond to it (e.g. a foreign-body/fibrotic response, S07/BIO1-1) altering local diffusion or the microenvironment; B1 active and facilitated transport mechanisms present in living tissue (but absent in a saline beaker) can add extra, non-passive pathways affecting how the drug actually moves once released.
3. Correct: A, D (exactly these options, no others)
4. [3] B1 cells sense the mechanical stiffness and loading of their surrounding extracellular matrix/scaffold through mechanotransduction pathways; B1 this mechanical signal influences cell behaviour, including how the seeded cells differentiate (e.g. towards bone-forming or other lineages); B1 so choosing scaffold stiffness is simultaneously a structural-support decision and a biochemical signalling decision, and the two requirements must be reconciled together, not treated as independent.
5. [2] B2 DNA bases pair specifically (A with T, C with G), so a probe strand will only hybridise strongly with a target strand whose sequence is complementary to it, giving the sensor sequence-specific (rather than generic) binding.

## Grading
Apply `rubric.json`'s `stage_rubrics.S09_Biochemistry_and_Cell_Biology_for_Engineers` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 13 marks in all; a pass needs at least 8 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S10_Bioelectricity_and_Medical_Instrumentation.
