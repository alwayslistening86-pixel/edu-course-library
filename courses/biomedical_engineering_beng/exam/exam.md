# Biomedical Engineering BEng (Hons) -- Loughborough University programme structure, QAA Engineering Benchmark graded - Cumulative Exam

## Unlock condition
Only available once every stage in `stage_ladder` has a passed test.

## Format
Three sections mirroring the three years: Year 1 (S01-S04: anatomy/physiology, mathematical methods, materials science, design process), Year 2 (S05-S09: biomechanics I/II, biomaterials 1, data analysis, biochemistry/cell biology), Year 3 (S10-S13: bioelectricity/medical instrumentation, biophotonics/imaging, biomaterials 2/drug delivery, healthcare engineering/regulation/professional practice). Questions are original; write fresh ones rather than reusing stage tests. The ready-made questions below are a starter bank; the tutor writes the rest.

## 12 ready-made items (write the rest fresh, never reusing stage-test items)
1. [Year 1] A biceps tendon inserts 4.5 cm from the elbow joint. Ignoring forearm weight, a 60 N weight is held 30 cm from the elbow. Calculate the biceps force required for moment equilibrium. [3 marks]
2. [Year 1] A tensile specimen of cross-sectional area 20 mm^2, original length 50 mm, extends by 0.15 mm under a 400 N load within its elastic region. Calculate stress, strain and Young's modulus. [4 marks]
3. [Year 1] Which of the following are true of a third-class lever, as found at the elbow? Choose every correct option.
   A. The effort lies between the fulcrum and the load
   B. It is mechanically efficient (muscle force less than load)
   C. It trades force for range and speed of motion
   D. The fulcrum lies between the effort and the load
4. [Year 1] A drug's plasma concentration falls from 10 mg/L to 4 mg/L in 5 hours, following first-order elimination C(t) = C0 e^(-kt). Find k and the half-life. [4 marks]
5. [Year 2] A titanium implant (E = 110 GPa) and adjacent cortical bone (E = 18 GPa) carry the same strain of 0.0008. Calculate the stress in each and comment on the implication for stress shielding. [4 marks]
6. [Year 2] An enzyme has Vmax = 8.0 micromol/min and Km = 2.0 mM. Calculate the reaction rate at [S] = 2.0 mM. [2 marks]
7. [Year 2] Which are properties a bone-tissue-engineering scaffold should have, per this course? Choose every correct option.
   A. Interconnected porosity suited to cell infiltration
   B. Zero porosity for maximum initial strength
   C. A degradation rate matched to new tissue formation
   D. Biocompatibility
8. [Year 3] An instrumentation amplifier has differential gain 800 and common-mode gain 0.08. Calculate its CMRR in dB. [2 marks]
9. [Year 3] A biosignal contains frequency content up to 250 Hz. State the Nyquist rate and explain what happens if the signal is sampled below it. [3 marks]
10. [Year 3] A first-order drug-release device has M0 = 150 mg and rate constant k = 0.10 per day. Calculate the fraction of drug released after 7 days. [3 marks]
11. [Year 3] Which device would require Class III conformity assessment under UK medical device regulation, per this course? Choose every correct option.
   A. An implantable pacemaker
   B. A simple adhesive bandage
   C. A hip replacement implant
   D. A non-invasive digital thermometer
12. [Year 3] Explain, using the ISO 14971 risk-control hierarchy, why an inherently safe design (e.g. a hard-coded maximum infusion rate) is preferred over a warning label for the same hazard. [3 marks]

## Answer key for the ready-made items (tutor only)
1. [3] M1 moments about elbow: F x 0.045 = 60 x 0.30; A1 RHS = 18.0; A1 F = 400.0 N.
2. [4] M1 stress = 400/(20e-6) = 20.0 MPa; M1 strain = 0.15/50 = 0.0030; A1 E = stress/strain; A1 = 6.67 GPa.
3. Correct: A, C (exactly these options, no others)
4. [4] M1 4 = 10 e^(-5k); M1 k = -ln(0.4)/5; A1 k = 0.1833 per hour; A1 half-life = ln2/k = 3.78 hours.
5. [4] M1 sigma_Ti = 110e9 x 0.0008 = 88 MPa; A1 sigma_bone = 18e9 x 0.0008 = 14.4 MPa; A1 ratio = 110/18 = 6.1, the implant carrying about 6 times the stress of the bone; B1 the implant therefore takes a disproportionate share of the load, under-loading (and over time weakening) the surrounding bone.
6. [2] M1 v = Vmax[S]/(Km+[S]) = 8.0x2.0/(2.0+2.0); A1 = 4.0 micromol/min (half of Vmax, as expected when [S] = Km).
7. Correct: A, C, D (exactly these options, no others)
8. [2] M1 CMRR = 20 log10(800/0.08); A1 = 80 dB.
9. [3] B1 Nyquist rate = 2 x 250 = 500 Hz (sampling must exceed this); B1 sampling below the Nyquist rate causes aliasing; B1 high-frequency content folds back and becomes indistinguishable from genuine low-frequency content, corrupting the sampled signal.
10. [3] M1 M(7) = 150 e^(-0.10x7); A1 = 74.5 mg remaining; A1 fraction released = 1 - e^(-0.7) = 0.503.
11. Correct: A, C (exactly these options, no others)
12. [3] B1 the hierarchy prefers inherently safe design, then protective measures, then information for safety (warnings), in that order of reliability; B1 an inherently safe design removes the possibility of the hazard occurring at all, rather than relying on a person noticing and correctly reacting to a warning; B1 warnings are the least reliable control because they depend on human behaviour, which can fail (fatigue, distraction, unfamiliarity).

## Grading
Mark every question against a written mark scheme. A pass needs at least 60% of the marks overall and at least 50% on each of the three year-sections. Report the total, the percentage per section and the weakest topic areas.

## Outcome
- **Pass:** record `exam_status: "passed"`. The course is complete.
- **Not yet:** leave `exam_status: "available"`, name the weakest topic areas, offer targeted review, and retry with fresh papers.
