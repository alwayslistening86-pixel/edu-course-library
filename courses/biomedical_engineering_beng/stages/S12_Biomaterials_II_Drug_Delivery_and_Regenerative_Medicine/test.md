# S12_Biomaterials_II_Drug_Delivery_and_Regenerative_Medicine - Test: Biomaterials II: Drug Delivery and Regenerative Medicine

## How to run this
A real checkpoint in the style of a UK engineering degree's structured written papers: short-answer and calculation questions with marks shown (M/A/B tagged in the mark scheme), plus some multiple-select items. Give the whole test at once, with no hints; the learner shows working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A diffusion-controlled (Higuchi, square-root-of-time) release device has released 40% of its drug load after 4 days. Assuming the square-root model Q(t) = A root(t) holds, estimate the fraction released after 16 days, and comment on whether the release rate is increasing or decreasing over this period. [4 marks]
2. A first-order-release device has M0 = 200 mg loaded and a rate constant k = 0.08 per day. Calculate the amount of drug remaining after 10 days, and the fraction of the original load released by that time. [4 marks]
3. Which release profile(s) are generally preferred, as this stage describes it, for maintaining a steady therapeutic drug concentration over an extended period? Choose every correct option.
   A. Zero-order (constant rate) release
   B. First-order release, where rate falls proportionally to the amount remaining
   C. Square-root-of-time (Higuchi/diffusion-controlled) release
   D. Zero-order release engineered via degradation-controlled (erosion-controlled) kinetics
4. Explain the practical difference between diffusion-controlled and degradation-controlled drug release from a polymer matrix, and state which is more naturally suited to achieving a near-zero-order release profile, and why. [4 marks]
5. A tissue-engineering scaffold releasing a growth factor is measured to release drug approximately linearly with ln(amount remaining) plotted against time. Identify which of the three kinetic models in this stage this matches, and state the mathematical form of cumulative release fraction released as a function of time and rate constant k. [3 marks]

## Answer key (for the tutor only)
1. [4] M1 A = 40/root(4) = 20.0 (% per root-day); M1 Q(16) = A x root(16); A1 = 80% (state clearly this exceeds 100% only because the simple early-time approximation is being extrapolated beyond its valid range, illustrating a real modelling-validity limitation); B1 the release rate dQ/dt is proportional to 1/root(t), so it decreases over time even though cumulative release keeps increasing.
2. [4] M1 M(10) = 200 e^(-0.08x10); A1 = 89.9 mg remaining; M1 fraction released = 1 - M(10)/M0; A1 = 0.551 (55.1%).
3. Correct: A, D (exactly these options, no others)
4. [4] B1 diffusion-controlled release depends on the drug diffusing through an intact (non-degrading, or slowly degrading) polymer matrix, following Fickian/Higuchi square-root kinetics; B1 degradation-controlled release depends on the polymer matrix itself breaking down (e.g. PLGA by hydrolysis), exposing/releasing drug at a rate set by the degradation process; B1 degradation-controlled release is more naturally suited to a near-zero-order profile; B1 because degradation rate can be engineered (via polymer composition/molecular weight) to proceed at a roughly constant rate, whereas diffusion through an intact matrix inherently slows as the diffusion path lengthens and the concentration gradient falls.
5. [3] B1 first-order release (since ln(amount remaining) linear in time is the signature of exponential decay, M(t) = M0 e^(-kt)); B1 fraction released = 1 - e^(-kt); B1 this recognition lets the same half-life calculation (t(1/2) = ln2/k) used for pharmacokinetic clearance (S08) be reused directly for the delivery device's release rate.

## Grading
Apply `rubric.json`'s `stage_rubrics.S12_Biomaterials_II_Drug_Delivery_and_Regenerative_Medicine` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 16 marks in all; a pass needs at least 10 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S13_Healthcare_Engineering_Systems_Regulation_and_Professional_Practice.
