# S04_Engineering_Design_Process_for_Healthcare - Lesson: Engineering Design Process for Healthcare

## Goal
The learner runs a structured engineering design process -- needs analysis, specification, concept generation, evaluation, and design-for-manufacture/CAD communication -- applied to a healthcare product, entirely as theory and design work.

## Syllabus items taught here
- DP-1 - The engineering design process
- DP-2 - User needs and writing a testable design specification
- DP-3 - Concept generation techniques
- DP-4 - Concept evaluation with a weighted decision (Pugh) matrix
- DP-5 - Design for manufacture/assembly and human factors/ergonomics
- DP-6 - Communicating a design: CAD and technical drawing conventions

## How to teach this
Give the brief 'design a device to help an elderly patient take the correct medication at the correct time' and ask what the very first engineering step should be, before any sketching -- then formalise the process that answer gestures at. Teach from the engineering principle outwards: state the physiological/materials fact, connect it to the governing equation, then work a numerical example with units. Every numerical answer in this course was computed with Python when the course was built. Use real orders of magnitude (joint reaction forces of several times body weight, biopotentials of millivolts, implant moduli tens of GPa) so the learner develops physical intuition, not just formula recall.

#### DP-1 The engineering design process
**The engineering design process** (as taught across UK design-and-technology/engineering curricula, e.g. Loughborough's Integrated Product Design and Design and Make modules): investigate/research the problem and user needs -> write a design specification -> generate a range of concepts -> evaluate concepts against the specification -> develop and detail the chosen concept -> communicate the design (drawings/CAD) -> plan manufacture -> prototype and test -> evaluate and iterate. It is iterative, not strictly linear: evaluation at any stage can send the process back to an earlier one.

#### DP-2 User needs and writing a testable design specification
**User needs and the design specification**: needs are gathered from stakeholders (patients, clinicians, carers, regulators) by observation, interview and task analysis, then translated into a design specification -- a list of measurable, testable requirements (e.g. "device mass < 150 g", "single-handed operation", "audible and visual alert", "IP54 splash resistance", "complies with relevant medical device regulation"). A good specification distinguishes must-have constraints from nice-to-have preferences, and every requirement should be checkable, not vague ("easy to use" is not testable; "operable by a user wearing one-handed with grip strength < 20 N" is).

#### DP-3 Concept generation techniques
**Concept generation**: divergent techniques (brainstorming, morphological analysis -- listing sub-functions and combining different solutions for each, and biomimicry -- drawing design inspiration from biological solutions) are used to generate a genuine range of distinct concepts before narrowing down, avoiding fixation on the first workable idea. Sketches at this stage are freehand and annotated (material, approximate dimensions, how the idea meets specific specification points), the same convention as the OCR R039-style annotated proposal used earlier in UK design education, now applied at degree level to a healthcare brief.

#### DP-4 Concept evaluation with a weighted decision (Pugh) matrix
**Concept evaluation**: a weighted decision (Pugh) matrix scores each concept against each specification criterion relative to a baseline ("datum") concept, with criteria weighted by importance; the concept with the best weighted total is selected (or hybridised from the best features of several). This makes concept selection traceable and defensible to stakeholders, rather than a matter of unrecorded preference -- important where a design decision may later be scrutinised as part of medical device regulatory evidence (S13).

#### DP-5 Design for manufacture/assembly and human factors/ergonomics
**Design for manufacture and assembly (DFMA)** and **human factors/ergonomics**: DFMA principles (minimise part count, design for the intended manufacturing process -- injection moulding draft angles, minimum wall thickness, avoiding undercuts -- and design for easy, foolproof assembly) reduce cost and manufacturing defects. For a healthcare device specifically, human factors engineering additionally considers the full range of intended users (including reduced dexterity, vision or cognition), use-error analysis (what happens if a step is done wrong or out of order), and designing to prevent the most safety-critical use errors by the device's physical form (e.g. a connector that cannot physically be attached the wrong way round) rather than by instructions alone.

#### DP-6 Communicating a design: CAD and technical drawing conventions
**Communicating a design: CAD and technical drawing conventions**: orthographic (first/third-angle) projection shows an object's plan, front and side views to scale; assembly drawings with a bill of materials communicate how parts fit together; a formal presentation/CAD drawing is fully dimensioned and toleranced. This course teaches these conventions and their correct use in design communication, as theory and specification -- see the standing notice on this stage's practical/CAD-tool component.

## Explicitly not here
Hands-on CAD software operation, physical prototyping, 3D printing/machining and the supervised making of a physical artefact are out of scope; this stage teaches the design-process theory, specification-writing, evaluation methods and drawing conventions, matching this library's existing convention (used in engineering_design) of declaring the hands-on/workshop component out of scope and teaching the underpinning theory and design work.
