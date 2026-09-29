# S13_Healthcare_Engineering_Systems_Regulation_and_Professional_Practice - Test: Healthcare Engineering Systems, Regulation and Professional Practice

## How to run this
A real checkpoint in the style of a UK engineering degree's structured written papers: short-answer and calculation questions with marks shown (M/A/B tagged in the mark scheme), plus some multiple-select items. Give the whole test at once, with no hints; the learner shows working and may use a calculator. Then mark against the mark schemes below and this stage's entry in `rubric.json`.

## Test items
1. Explain why a Class III implantable device requires substantially more design-history and biocompatibility evidence than a Class I device before it can be placed on the market, and name one specific standard series relevant to that evidence. [3 marks]
2. Using the ISO 14971 risk-control hierarchy (inherently safe design, protective measures, information for safety), rank these three mitigations for the risk of a syringe pump being set to the wrong drug-infusion rate, from most to least preferred, and justify the order. [4 marks]
3. Which of the following are genuine expectations for a professional engineer as described in this stage (drawing on the QAA Engineering benchmark statement)? Choose every correct option.
   A. Holding paramount the health, safety and welfare of the public
   B. Working only within one's actual area of competence
   C. Prioritising project speed over patient safety when the two conflict
   D. Exercising responsible judgement about the broader societal impact of engineering decisions
4. A clinical engineer discovers that an infusion pump model in routine hospital use has a rare software fault that can, under a specific sequence of user inputs, deliver a drug at double the intended rate. Using the risk-management concepts from this stage, outline the steps a responsible engineering response should include. [4 marks]
5. Explain, referring to reimbursement pathway and stage-gate development, why a technically excellent biomedical device design can still fail as a commercial product. [3 marks]

## Answer key (for the tutor only)
1. [3] B1 classification is risk-based, and a Class III device (implantable/life-sustaining) poses far greater potential harm to the patient if it fails than a low-risk Class I device; B1 more rigorous conformity-assessment evidence (design documentation, biocompatibility and fatigue-life testing, clinical evaluation) is therefore required to demonstrate the higher risk has been adequately controlled before market approval; B1 ISO 10993 (biocompatibility testing series).
2. [4] B3 (1 mark each, correct order): 1) inherently safe design -- e.g. the pump software enforces a hard maximum rate limit so an unsafe value cannot physically be set; 2) protective measures -- e.g. an alarm that triggers if the set rate is outside a normal clinical range, requiring active override; 3) information for safety -- e.g. a warning label or training reminding staff to double-check the rate; B1 justification: inherently safe design removes the hazard's possibility altogether rather than relying on a person noticing and reacting correctly, so it is the most reliable and thus most preferred control.
3. Correct: A, B, D (exactly these options, no others)
4. [4] B1 formally record and investigate the hazard (incident investigation, feeding into the device's risk management file per ISO 14971); B1 estimate and evaluate the risk (severity of harm x probability of the triggering input sequence occurring in real clinical use); B1 implement the most effective available risk control, preferring an inherently safe fix (e.g. a software update preventing the fault sequence) over merely warning users; B1 report the issue as required (e.g. to the MHRA and/or the manufacturer) and verify, after the fix, that the control is actually effective before considering the risk adequately managed.
5. [3] B1 a device's commercial viability depends on who pays for it (patient, insurer or national health system) and whether that payer's reimbursement pathway/criteria are satisfied, not on technical performance alone; B1 a device that is clinically effective but not covered by, or cost-effective within, the relevant reimbursement system may struggle to be adopted regardless of its engineering merit; B1 stage-gate development is meant to catch this by reviewing commercial (not only technical) viability at each phase, but a design that only optimises for technical/clinical criteria can still pass technical gates while ultimately failing to find a viable market or payer.

## Grading
Apply `rubric.json`'s `stage_rubrics.S13_Healthcare_Engineering_Systems_Regulation_and_Professional_Practice` exactly. Mark each answer against its mark scheme (method marks need the method shown; a multiple-choice item is worth 1 mark and needs every correct option and nothing else). 15 marks in all; a pass needs at least 9 (60%, rounded up). Record `pass` or `fail` in `syllabus_status`, with the mark and a short honest note on what was missed.

## If not passed
Name the specific misconceptions the wrong answers show, run remediation on those, then re-test with fresh items of the same types (never this exact set).

## On pass
Record the pass. Every stage is now passed, so the cumulative exam becomes available.
