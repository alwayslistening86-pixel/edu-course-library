# S07_Biomaterials_I_Tissue_Engineering_and_Implants - Test: Biomaterials I: Tissue Engineering and Implants

## How to run this
A real checkpoint in the style of a UK engineering degree's structured written papers: short-answer and calculation questions with marks shown (M/A/B tagged in the mark scheme), plus some multiple-select items. Give the whole test at once, with no hints; the learner shows working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. A design team is selecting a scaffold material for a bone tissue-engineering application. List three properties the scaffold should have, and explain why the scaffold's degradation rate matters mechanically, not just biologically. [5 marks]
2. Explain why UHMWPE wear debris is a clinically significant failure mode for a hip replacement, even though UHMWPE itself has low friction and good wear resistance compared with alternatives. [3 marks]
3. Which of the following are genuine engineering reasons to choose a titanium alloy over stainless steel or cobalt-chromium for a load-bearing implant, based on this stage? Choose every correct option.
   A. Lower Young's modulus than steel/CoCr, reducing (though not eliminating) stress shielding
   B. Excellent corrosion resistance via a stable, self-healing oxide layer
   C. Higher wear resistance than cobalt-chromium as a bearing surface
   D. Good osseointegration
4. Explain why gamma irradiation, despite being an effective and packaging-penetrating sterilisation method, historically caused a documented problem for UHMWPE implant components, and name the materials-science response that addressed it. [3 marks]
5. A design team must choose a sterilisation method for a device containing both a heat-sensitive electronic sensor and a metal housing. State which of the three methods in this stage is most appropriate and why, and name the main practical drawback of that method. [2 marks]

## Answer key (for the tutor only)
1. [5] B3 (1 mark each, any three of: biocompatible; interconnected porosity of a suitable pore size for cell infiltration and nutrient/waste diffusion; adequate initial mechanical strength; a degradation rate that can be tuned/matched to tissue formation); B2 if the scaffold degrades faster than new tissue can bear load, the construct loses mechanical support prematurely and can fail or collapse before healing is complete, so degradation rate is itself a mechanical-design requirement, not only a biological one.
2. [3] B1 even a low wear rate produces some polymer wear particles over years of cyclic loading; B1 these particles can provoke an inflammatory (osteolytic) response in the surrounding bone; B1 this bone loss (osteolysis) can loosen the implant, a major cause of long-term implant failure and revision surgery, distinct from the mechanical wear itself.
3. Correct: A, B, D (exactly these options, no others)
4. [3] B1 gamma irradiation can cause oxidative degradation/embrittlement of the polymer, worsening over shelf-life storage; B1 this reduced the material's toughness and wear resistance over time, a real documented cause of accelerated implant wear; B1 addressed by developing highly cross-linked, vitamin-E-stabilised UHMWPE formulations that resist this oxidative degradation.
5. [2] B1 ethylene oxide (EtO) gas, because it sterilises effectively at low temperature, suiting the heat-sensitive electronics (autoclaving's high temperature and gamma's potential to affect electronics make them less suitable here); B1 drawback: requires a lengthy aeration period afterwards to remove toxic EtO residue before the device is safe to use.

## Grading
Apply `rubric.json`'s `stage_rubrics.S07_Biomaterials_I_Tissue_Engineering_and_Implants` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 14 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass and move on to S08_Data_Analysis_and_Modelling_for_Bioengineers.
