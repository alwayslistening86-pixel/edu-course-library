# S05_Biomechanics_I_Statics_and_Musculoskeletal_Mechanics - Lesson: Biomechanics I: Statics and Musculoskeletal Mechanics

## Goal
The learner models the musculoskeletal system as a system of rigid-body levers in static equilibrium, drawing free body diagrams and solving for unknown muscle and joint reaction forces.

## Syllabus items taught here
- BM1-1 - Rigid-body static equilibrium and free body diagrams
- BM1-2 - Lever classes in the musculoskeletal system
- BM1-3 - Worked elbow-flexion lever model
- BM1-4 - Joint reaction force
- BM1-5 - Centre of mass and anthropometric segment models
- BM1-6 - Gait cycle and ground reaction force basics

## How to teach this
Ask the learner to hold an arm out horizontally and guess how much force their biceps muscle must produce to support even a light weight in the hand -- most guess far too low. Build the lever model that gives the real, surprising answer. Teach from the engineering principle outwards: state the physiological/materials fact, connect it to the governing equation, then work a numerical example with units. Every numerical answer in this course was computed with Python when the course was built. Use real orders of magnitude (joint reaction forces of several times body weight, biopotentials of millivolts, implant moduli tens of GPa) so the learner develops physical intuition, not just formula recall.

#### BM1-1 Rigid-body static equilibrium and free body diagrams
**Rigid-body static equilibrium**: for any body (or free body diagram cut from it) not accelerating, the sum of forces in each direction is zero (Sum Fx = 0, Sum Fy = 0) and the sum of moments about any point is zero (Sum M = 0). A free body diagram isolates the body segment of interest (e.g. the forearm) and replaces everything else (muscle, ligaments, the rest of the body) with the forces/moments they exert on it, drawn as vectors at their true points of application.

#### BM1-2 Lever classes in the musculoskeletal system
**Lever classes in the body**: a first-class lever has the fulcrum (joint) between the effort (muscle) and the load (e.g. the head balanced on the atlanto-occipital joint by neck muscles); a second-class lever has the load between the fulcrum and the effort (e.g. standing on tiptoe, ankle joint as fulcrum, load = body weight, effort = calf muscle via Achilles tendon, mechanically efficient); a third-class lever has the effort between the fulcrum and the load (e.g. the elbow flexing the forearm: fulcrum = elbow, effort = biceps inserting close to the elbow, load = hand) -- the most common arrangement in the human body, and mechanically inefficient by design, trading force for range and speed of motion.

#### BM1-3 Worked elbow-flexion lever model
**The elbow flexion model (worked)**: modelling the forearm as a rigid lever about the elbow joint, with the biceps tendon inserting a short moment arm d_m from the joint and a load W held at a longer distance d_L from the joint, moment equilibrium about the elbow gives F_muscle x d_m = W x d_L, so F_muscle = W x d_L / d_m. Because d_m is typically only a few centimetres while d_L can be 30+ cm, F_muscle is typically several times larger than the load itself -- this is why biceps forces of hundreds of newtons are needed to hold even a modest weight in the hand, and why joint reaction forces (below) are correspondingly large.

#### BM1-4 Joint reaction force
**Joint reaction force**: once the muscle force is found from moment equilibrium, force equilibrium (Sum Fy = 0) gives the joint reaction force: R = F_muscle + W_forearm - W (signs depending on direction convention), i.e. the elbow joint itself must react to almost the full muscle force plus the load, since the muscle force and load both act on the same side of a short-lever system. This is why joint reaction forces at the hip and knee during activities like stair-climbing or running can reach several times body weight -- a figure directly relevant to designing implant fatigue life (S06) and gait-analysis instrumentation.

#### BM1-5 Centre of mass and anthropometric segment models
**Centre of mass and segment models**: the whole-body centre of mass, and the centre of mass of each body segment (forearm, thigh, trunk, etc.), can be estimated from standard anthropometric tables (segment mass as a fraction of total body mass, segment centre of mass as a fraction of segment length from the proximal end) -- e.g. the forearm is roughly 1.6% of body mass with its centre of mass roughly 43% of forearm length from the elbow. These standard fractions let a biomechanical model be built for any individual from just their total body mass and segment lengths, without needing to measure each segment's mass directly.

#### BM1-6 Gait cycle and ground reaction force basics
**Basic gait analysis concepts**: a gait cycle runs from one heel-strike to the next heel-strike of the same foot, divided into stance phase (~60%, foot in contact with the ground) and swing phase (~40%). Ground reaction force (GRF), measured with a force plate, typically shows a double-peaked vertical profile during walking (loading response, then push-off), each peak somewhat above body weight; these GRF measurements are the standard input to inverse-dynamics models that estimate internal joint moments and forces during walking, extending the static lever analysis of this stage to a dynamic, whole-limb calculation.

## Explicitly not here
Full multi-segment inverse dynamics, muscle-force optimisation for redundant (multi-muscle) systems, and motion-capture instrumentation are out of scope; this stage builds single-lever static equilibrium as the foundation those extend.
