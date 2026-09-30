# S16_Capacitance - Lesson: Capacitance and exponential change

## Goal
The learner defines capacitance, relates it to plate geometry and dielectrics, calculates stored energy, models charge and discharge exponentially with time constants and logarithmic graphs, and carries out required practical 9.

## Syllabus items taught here
- 3.7.4.1 - Capacitance
- 3.7.4.2 - Parallel plate capacitor
- 3.7.4.3 - Energy stored by a capacitor
- 3.7.4.4 - Capacitor charge and discharge
- RP9 - Required practical 9: charge and discharge of capacitors, with a log-linear plot for RC
- MS 2.5 - Use logarithms in relation to quantities that range over several orders of magnitude
- MS 3.10 - Interpret logarithmic plots
- MS 3.11 - Use logarithmic plots to test exponential and power law variations

## How to teach this
Ask how a camera flash can deliver far more power than its small battery could supply directly. Teach from the physics outwards: state the principle, derive or justify the equation, then do a worked example with units and sensible significant figures. Use AQA's data and formulae booklet values (e.g. g = 9.81 N kg^-1, e = 1.60 x 10^-19 C, h = 6.63 x 10^-34 J s, c = 3.00 x 10^8 m s^-1). Every numerical answer here was computed when the course was built.

#### 3.7.4.1 Capacitance
Capacitance C = Q/V: the charge stored per unit pd (farad, F = C/V). Practical values are μF, nF and pF.

#### 3.7.4.2 Parallel plate capacitor
A parallel-plate capacitor: C = Aε0εr/d, where εr is the relative permittivity (dielectric constant) of the material between the plates. A dielectric's polar molecules align with the field, creating an opposing field, so more charge is stored for the same pd. *Example:* plates 0.10 m x 0.10 m, 1.0 mm apart in air: C = 88.5 pF; with a dielectric of εr = 4.0 it becomes 354 pF.

#### 3.7.4.3 Energy stored by a capacitor
Energy stored E = (1/2)QV = (1/2)CV^2 = (1/2)Q^2/C: the area under a Q-V graph (a straight line through the origin). *Example:* a 470 μF capacitor at 12 V stores 0.0338 J.

#### 3.7.4.4 Capacitor charge and discharge
Discharge through R: Q = Q0 e^(-t/RC), and V and I decay the same way. The time constant RC is the time to fall to 1/e (37%); the half-life t_1/2 = 0.69RC. Charging from a supply V0: Q = Q0(1 - e^(-t/RC)) and V = V0(1 - e^(-t/RC)), while the current decays exponentially. Rate of discharge is proportional to charge (ΔQ/Δt = -Q/RC), which is why the decay is exponential. The area under an I-t graph gives the charge. *Example:* 220 μF and 10 kΩ: RC = 2.2 s; after 5.0 s, V has fallen to 10.3% of V0.

#### RP9 Required practical 9: charge and discharge of capacitors, with a log-linear plot for RC
**Method:** charge the capacitor, then discharge it through a known resistor; record the pd across it (voltmeter or data logger) at regular intervals. **Analysis:** ln V = ln V0 - t/RC, so a graph of ln V against t is a straight line with gradient -1/RC; find RC (and hence C if R is known). Using a large RC (e.g. 1000 μF with 100 kΩ) gives times long enough to read by hand.

#### MS 2.5 Use logarithms in relation to quantities that range over several orders of magnitude
Logarithms handle quantities spanning orders of magnitude: log10 of 1, 10, 100, 1000 are 0, 1, 2, 3. ln(e^x) = x; ln(ab) = ln a + ln b; ln(a^n) = n ln a. Take natural logs of exponential relationships to make them linear.

#### MS 3.10 Interpret logarithmic plots
Reading a log scale or a log graph: a unit change in log10 y is a factor of 10 in y. On an ln V against t graph, the gradient has units of s^-1 and the intercept is ln V0, so V0 = e^(intercept).

#### MS 3.11 Use logarithmic plots to test exponential and power law variations
Testing relationships: if y = Ae^(kx), then ln y = ln A + kx: plot ln y against x for a straight line (gradient k). If y = ax^n, then log y = log a + n log x: plot log y against log x for a straight line (gradient n). *Example:* a log-log gradient of -2.0 confirms an inverse-square law.

## Explicitly not here
Radioactive exponential decay is S18.

## Further resources (optional)

These are optional, hand-picked, externally hosted tools -- not part of the syllabus content above, not graded, and not embedded in this file. Nothing here is required to pass the stage.
- **Capacitor Lab: Basics** (https://phet.colorado.edu/en/simulations/capacitor-lab-basics) -- PhET sim -- change plate area/separation/voltage and watch charge and field respond live, plus a discharging RC circuit; useful for the C = Q/V relationship and time-constant behaviour.
