# S10_Current_Electricity - Lesson: Current, potential difference, resistance and resistivity

## Goal
The learner uses the definitions of current, potential difference and resistance, interprets I-V characteristics (ohmic conductor, filament lamp, diode, superconductor), uses resistivity and the temperature dependence of thermistors, and carries out required practical 5.

## Syllabus items taught here
- 3.5.1.1 - Basics of electricity
- 3.5.1.2 - Current-voltage characteristics
- 3.5.1.3 - Resistivity
- RP5 - Required practical 5: resistivity of a wire using a micrometer, ammeter and voltmeter

## How to teach this
Ask why a lamp's resistance is much lower when it's cold than when it's glowing. Teach from the physics outwards: state the principle, derive or justify the equation, then do a worked example with units and sensible significant figures. Use AQA's data and formulae booklet values (e.g. g = 9.81 N kg^-1, e = 1.60 x 10^-19 C, h = 6.63 x 10^-34 J s, c = 3.00 x 10^8 m s^-1). Every numerical answer here was computed when the course was built.

#### 3.5.1.1 Basics of electricity
Current I = ΔQ/Δt (A); potential difference V = W/Q (V, J per C); resistance R = V/I (Ω). *Example:* 5.0 C passes in 2.0 s: 2.5 A. Charge carriers in metals are free electrons. Power P = IV = I^2 R = V^2/R; energy E = IVt.

#### 3.5.1.2 Current-voltage characteristics
I-V characteristics: an ohmic conductor (metal at constant temperature) gives a straight line through the origin (V ∝ I). A filament lamp's graph curves: resistance rises as it heats (more lattice vibrations). A semiconductor diode conducts only in the forward direction beyond a threshold of about 0.6 V (silicon). Ammeters are ideal with zero resistance (in series), voltmeters with infinite resistance (in parallel).

#### 3.5.1.3 Resistivity
R = ρL/A, where ρ is the resistivity (Ω m). *Example:* 2.5 m of constantan (ρ = 4.9 x 10^-7 Ω m) with diameter 0.32 mm: R = 15.2 Ω. Metals: resistance increases with temperature. An NTC thermistor's resistance falls as temperature rises (more charge carriers released); used in temperature sensors. A **superconductor** has zero resistivity below its critical temperature; applications include strong magnets (MRI, particle accelerators) and power cables with no energy loss.

#### RP5 Required practical 5: resistivity of a wire using a micrometer, ammeter and voltmeter
**Method:** measure the wire's diameter with a micrometer at several points, taking the mean; connect a length of wire in a circuit with an ammeter and voltmeter (use a crocodile clip to vary the length L), keeping the current small to avoid heating. Record V and I for several lengths; R = V/I. **Analysis:** plot R against L: a straight line with gradient ρ/A, so ρ = gradient x A (a non-zero intercept is due to contact resistance and doesn't affect the gradient). *Example:* gradient 6.3 Ω m^-1, d = 0.315 mm: ρ = 6.3 x π(0.1575 x 10^-3)^2 = 4.91 x 10^-7 Ω m.

## Explicitly not here
Circuits are S11.

## Further resources (optional)

These are optional, hand-picked, externally hosted tools -- not part of the syllabus content above, not graded, and not embedded in this file. Nothing here is required to pass the stage.
- **Circuit Construction Kit: DC** (https://phet.colorado.edu/en/simulations/circuit-construction-kit-dc) -- PhET sim -- build a real circuit (battery, resistors, bulbs, ammeter/voltmeter) and read current/voltage directly; good for series vs parallel intuition before Kirchhoff's laws.
