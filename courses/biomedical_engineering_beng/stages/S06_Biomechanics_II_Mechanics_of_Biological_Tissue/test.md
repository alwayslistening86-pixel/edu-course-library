# S06_Biomechanics_II_Mechanics_of_Biological_Tissue - Test: Biomechanics II: Mechanics of Biological Tissue

## How to run this
A real checkpoint in the style of a UK engineering degree's structured written papers: short-answer and calculation questions with marks shown (M/A/B tagged in the mark scheme), plus some multiple-select items. Give the whole test at once, with no hints; the learner shows working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A titanium alloy hip stem (E = 110 GPa) and the surrounding cortical bone (E = 18 GPa) experience the same longitudinal strain of 0.001 (0.1%) while sharing load in parallel. Calculate the stress carried by each material, and the ratio of stem stress to bone stress. [4 marks]
2. Describe the biphasic (fluid + solid matrix) load-bearing mechanism of articular cartilage under (a) a sudden impact load and (b) prolonged sustained standing, and relate this to why cartilage creeps under static loading. [4 marks]
3. Which features are typical of tendon's stress-strain behaviour under load, distinguishing it from a simple linear-elastic material such as bone in its elastic region? Choose every correct option.
   A. A low-stiffness toe region as crimped collagen fibres straighten
   B. A perfectly linear stress-strain relationship from zero load
   C. Stress relaxation under sustained constant strain
   D. Creep under sustained constant load
4. A tissue's stress relaxes according to sigma(t) = sigma_infinity + (sigma_0 - sigma_infinity) e^(-t/tau), with sigma_0 = 5.0 MPa, sigma_infinity = 2.0 MPa and tau = 120 s. Calculate the stress remaining after 300 seconds. [3 marks]
5. Name one documented mitigation used in implant design against fatigue failure at a stress concentration, and explain briefly why it works. [2 marks]

## Answer key (for the tutor only)
1. [4] M1 sigma_implant = E x strain = 110e9 x 0.001 = 110 MPa; M1 sigma_bone = 18e9 x 0.001 = 18.0 MPa; A1 ratio = 110/18 = 6.11; A1 the implant carries about 6 times the stress of the bone for the same strain, illustrating why it takes a disproportionate load share (stress shielding).
2. [4] B1 (a) under sudden load, interstitial fluid cannot escape instantly and pressurises, so the fluid phase carries most of the load initially; B1 (b) under sustained load, fluid gradually exudes from the matrix and load transfers progressively to the much less stiff solid collagen-proteoglycan matrix; B2 because the solid matrix alone is far less stiff than the pressurised fluid-supported composite, strain increases over time under constant load -- i.e. the tissue creeps.
3. Correct: A, C, D (exactly these options, no others)
4. [3] M1 sigma(300) = 2.0 + (5.0-2.0) e^(-300/120); M1 exponent = -2.50; A1 = 2.25 MPa.
5. [2] B1 e.g. shot peening (or avoiding sharp internal corners / smoothing the geometry); B1 shot peening induces a beneficial residual compressive stress at the surface, which must be overcome by the applied tensile stress before a fatigue crack can effectively grow, extending fatigue life (equally accept: removing sharp corners reduces the local stress concentration factor directly).

## Grading
Apply `rubric.json`'s `stage_rubrics.S06_Biomechanics_II_Mechanics_of_Biological_Tissue` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 14 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S07_Biomaterials_I_Tissue_Engineering_and_Implants.
