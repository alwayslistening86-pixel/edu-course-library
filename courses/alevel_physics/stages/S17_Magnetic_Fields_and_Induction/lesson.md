# S17_Magnetic_Fields_and_Induction - Lesson: Magnetic fields and electromagnetic induction

## Goal
The learner applies F = BIl and F = BQv, explains circular paths of charged particles, calculates flux and flux linkage, applies Faraday's and Lenz's laws, describes alternating currents and transformers, and carries out required practicals 10 and 11.

## Syllabus items taught here
- 3.7.5.1 - Magnetic flux density
- 3.7.5.2 - Moving charges in a magnetic field
- 3.7.5.3 - Magnetic flux and flux linkage
- 3.7.5.4 - Electromagnetic induction
- 3.7.5.5 - Alternating currents
- 3.7.5.6 - The operation of a transformer
- RP10 - Required practical 10: force on a current-carrying wire with a top pan balance
- RP11 - Required practical 11: flux linkage with a search coil and oscilloscope

## How to teach this
Ask how a bicycle dynamo lights a lamp with no battery. Teach from the physics outwards: state the principle, derive or justify the equation, then do a worked example with units and sensible significant figures. Use AQA's data and formulae booklet values (e.g. g = 9.81 N kg^-1, e = 1.60 x 10^-19 C, h = 6.63 x 10^-34 J s, c = 3.00 x 10^8 m s^-1). Every numerical answer here was computed when the course was built.

#### 3.7.5.1 Magnetic flux density
A current-carrying wire at right angles to a magnetic field feels F = BIl (Fleming's left-hand rule gives the direction); at angle θ, F = BIl sin θ. Magnetic flux density B (tesla, T) is defined by this: 1 T gives a force of 1 N on 1 m of wire carrying 1 A at right angles. *Example:* 0.050 m of wire carrying 3.0 A in a 0.20 T field: F = 0.030 N.

#### 3.7.5.2 Moving charges in a magnetic field
A charge moving at right angles to B feels F = BQv, perpendicular to its velocity, so it moves in a circle: BQv = mv^2/r gives r = mv/(BQ). Applications: the cyclotron (a particle accelerator whose dees give energy each half-turn; the period 2πm/(BQ) does not depend on speed at non-relativistic speeds), and the mass spectrometer. *Example:* a proton at 2.0 x 10^6 m/s in 0.50 T: r = 4.2 cm.

#### 3.7.5.3 Magnetic flux and flux linkage
Magnetic flux Φ = BA (weber, Wb) when B is perpendicular to the area; flux linkage NΦ (Wb-turns) for a coil of N turns. At angle θ between the field and the normal to the coil: NΦ = BAN cos θ. *Example:* a 200-turn coil of area 4.0 cm^2 in a 0.30 T field, normal at 60°: NΦ = 0.012 Wb-turns.

#### 3.7.5.4 Electromagnetic induction
Faraday's law: the induced emf equals the rate of change of flux linkage: ε = N ΔΦ/Δt. Lenz's law: the induced current opposes the change producing it (conservation of energy). A rod of length l moving at v through B: ε = Blv. A coil rotating at ω: ε = BANω sin(ωt), peak BANω. *Example:* a 0.20 m rod moving at 5.0 m/s in 0.10 T: ε = 0.10 V.

#### 3.7.5.5 Alternating currents
Alternating current: peak (I0, V0), peak-to-peak (2V0) and root-mean-square values: I_rms = I0/root2, V_rms = V0/root2; the rms value gives the same power as the equivalent dc. Mains in the UK is 230 V rms (peak 325 V), 50 Hz. An oscilloscope displays voltage (Y-gain in V/div) against time (time base in s/div): read the peak and the period, and f = 1/T.

#### 3.7.5.6 The operation of a transformer
A transformer: an alternating current in the primary coil creates a changing flux in the iron core, linked to the secondary coil. Vs/Vp = Ns/Np; ideal transformers have IpVp = IsVs; efficiency = IsVs/(IpVp). Losses: eddy currents (reduced by a laminated core), resistance of the windings (thick low-resistance wire), hysteresis (soft iron) and flux leakage. Power is transmitted at high voltage and low current to reduce I^2 R losses in cables. *Example:* 1.0 MW sent through cables of 5.0 Ω at 25 kV loses I^2 R = 8000 W; at 400 kV it loses 31.25 W.

#### RP10 Required practical 10: force on a current-carrying wire with a top pan balance
**Method:** a horseshoe (U-shaped) magnet on a top pan balance, a stiff wire clamped horizontally between its poles; zero the balance, pass current I and read the change in mass Δm. The force on the wire is equal and opposite to the force on the magnet: F = Δm g. **Analysis:** plot F against I: gradient = Bl, so B = gradient/l.

#### RP11 Required practical 11: flux linkage with a search coil and oscilloscope
**Method:** a search coil connected to an oscilloscope, placed in the alternating field of a large coil; rotate the search coil and record the peak emf at different angles θ between its normal and the field. **Analysis:** the peak emf is proportional to cos θ; plot peak emf against cos θ for a straight line through the origin. Also vary the distance from the field coil to investigate how B changes.

## Explicitly not here
Nuclear radiation is S18.

## Further resources (optional)

These are optional, hand-picked, externally hosted tools -- not part of the syllabus content above, not graded, and not embedded in this file. Nothing here is required to pass the stage.
- **Faraday's Law** (https://phet.colorado.edu/en/simulations/faradays-law) -- PhET sim -- move a magnet through a coil at different speeds and see induced current and bulb brightness respond; direct visual for Faraday's and Lenz's laws.
