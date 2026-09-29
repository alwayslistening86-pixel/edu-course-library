# S01_Human_Anatomy_and_Physiology_for_Engineers - Lesson: Human Anatomy and Physiology for Engineers

## Goal
The learner describes the structure and function of the musculoskeletal, cardiovascular and respiratory systems, and the levels of biological organisation, in the terms a biomedical engineer needs to model and instrument them.

## Syllabus items taught here
- AP-1 - Levels of biological organisation, tissue types and anatomical terminology
- AP-2 - The skeletal system: bone types, bone composite structure and joint classification
- AP-3 - Synovial joint types, degrees of freedom, and ligament/tendon function
- AP-4 - Skeletal muscle structure, motor units and force generation
- AP-5 - The cardiovascular system: cardiac output and blood pressure
- AP-6 - Excitable tissue and the action potential
- AP-7 - The respiratory system and gas exchange
- AP-8 - Homeostasis and negative-feedback control

## How to teach this
Ask the learner to name every system in the body a hip-replacement engineer, a pacemaker engineer and a ventilator engineer would each need to understand -- then show how all three routes come back to the same anatomical vocabulary. Teach from the engineering principle outwards: state the physiological/materials fact, connect it to the governing equation, then work a numerical example with units. Every numerical answer in this course was computed with Python when the course was built. Use real orders of magnitude (joint reaction forces of several times body weight, biopotentials of millivolts, implant moduli tens of GPa) so the learner develops physical intuition, not just formula recall.

#### AP-1 Levels of biological organisation, tissue types and anatomical terminology
**Levels of organisation**: cell -> tissue -> organ -> organ system -> organism. The four basic tissue types are epithelial (covering/lining), connective (bone, cartilage, tendon, blood -- supports and connects), muscle (generates force) and nervous (signal transmission). Anatomical position and planes: sagittal (left/right), coronal/frontal (front/back), transverse (top/bottom); directional terms proximal/distal, medial/lateral, superior/inferior, anterior/posterior are the standard vocabulary in implant and prosthetic specifications.

#### AP-2 The skeletal system: bone types, bone composite structure and joint classification
**The skeletal system**: 206 bones in the adult, classified as long (femur), short (carpals), flat (skull), irregular (vertebrae) and sesamoid (patella). Bone is a composite of collagen (tensile strength) and hydroxyapatite mineral (compressive stiffness) -- the biomaterials link developed in S06/S07. Compact (cortical) bone forms the dense outer shell; cancellous (trabecular) bone is the porous interior, lower density and lower stiffness but able to remodel along load lines (Wolff's law). Joints are classified as fibrous (immovable, e.g. skull sutures), cartilaginous (slightly movable, e.g. intervertebral discs) and synovial (freely movable, e.g. hip, knee, elbow) -- synovial joints are the ones orthopaedic implants replace.

#### AP-3 Synovial joint types, degrees of freedom, and ligament/tendon function
**Synovial joint types and degrees of freedom**: ball-and-socket (hip, shoulder: 3 rotational DOF), hinge (elbow, knee: primarily 1 rotational DOF flexion/extension), pivot (radioulnar: 1 rotational DOF), condyloid/saddle (wrist, thumb: 2 DOF). The knee is technically a modified hinge with a small amount of rotation and translation, which is why knee-replacement kinematics is harder to reproduce than hip kinematics. Ligaments connect bone to bone (stability); tendons connect muscle to bone (force transmission) -- both are dense connective tissue, mostly type I collagen, and both are viscoelastic (S06).

#### AP-4 Skeletal muscle structure, motor units and force generation
**Skeletal muscle and contraction**: muscle is arranged in a hierarchy -- fibre -> myofibril -> sarcomere, the sliding-filament contractile unit of actin and myosin. A motor neuron and the fibres it innervates form a motor unit; recruiting more motor units, and firing them at higher frequency, increases force (a concept used directly when interpreting EMG amplitude in S10). Muscle force is roughly proportional to physiological cross-sectional area, which is why muscle force is estimated from anatomical cross-section in biomechanical models (S05). Muscle contraction is triggered by an action potential (AP-6) travelling down the motor neuron and across the neuromuscular junction.

#### AP-5 The cardiovascular system: cardiac output and blood pressure
**The cardiovascular system**: a closed double-circuit pump. The heart's four chambers (right/left atrium, right/left ventricle) and four valves (tricuspid, pulmonary, mitral, aortic) drive the pulmonary circuit (right heart -> lungs -> left heart, gas exchange) and the systemic circuit (left heart -> body -> right heart). Cardiac output CO = heart rate (HR) x stroke volume (SV); a typical resting adult has HR ~70 bpm and SV ~70 mL, giving CO ~4.9 L/min. Blood pressure is quoted systolic/diastolic (e.g. 120/80 mmHg); mean arterial pressure MAP ~= diastolic + (1/3)(systolic - diastolic).

#### AP-6 Excitable tissue and the action potential
**Excitable tissue and the action potential**: nerve and muscle cell membranes maintain a resting potential of about -70 mV (inside negative) via the Na+/K+ pump and selective ion permeability. A stimulus that depolarises the membrane past threshold triggers an action potential: fast Na+ influx (depolarisation), then K+ efflux (repolarisation), briefly overshooting to hyperpolarisation before returning to rest. This all-or-nothing electrical event is the origin of the ECG, EMG and EEG signals engineered in S10, and its ~1 ms timescale sets the bandwidth those instruments must capture.

#### AP-7 The respiratory system and gas exchange
**The respiratory system and gas exchange**: air moves through the trachea, bronchi, bronchioles to ~300 million alveoli, where O2 and CO2 diffuse across a thin membrane into and out of pulmonary capillary blood, driven by partial-pressure gradients (Fick's law of diffusion: flux proportional to area and concentration gradient, inversely proportional to membrane thickness). Tidal volume (~500 mL at rest) x respiratory rate (~12-16 breaths/min) gives minute ventilation, the quantity a mechanical ventilator must reproduce or support.

#### AP-8 Homeostasis and negative-feedback control
**Homeostasis and negative feedback**: physiological variables (blood pressure, blood glucose, core temperature, blood pH ~7.35-7.45) are held within a narrow range by negative-feedback control loops -- a sensor (receptor), a comparator (control centre, e.g. the medulla for blood pressure via baroreceptors) and an effector that opposes the deviation. This is the same control-loop structure used in closed-loop medical devices (e.g. an insulin pump reading a continuous glucose sensor), making physiology a natural entry point to control-system thinking for a bioengineer.

## Explicitly not here
Detailed neuroanatomy, embryology and full systemic pathology are out of scope; only the anatomy and physiology load-bearing for later biomechanics, biomaterials and instrumentation stages is taught.
