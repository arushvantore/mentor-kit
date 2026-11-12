# SOURCE DATA FOR AP PHYSICS 1 IA-1 — paste below the PROMPT.md

## OFFICIAL IA-1 SYLLABUS (Slack, nikhil.menon, 14 Oct) — Lecture 1 to Lecture 10
Sizes in the Universe; Introduction to Measurement; Units and Dimensions; Order of Magnitude; Significant Digits; Scientific Notation; Error and Propagation; Scalars and Vectors; Vector Arithmetic; Vector Products; Vector Resolution; Differentiation; Integration; Distance and Displacement; Speed and Velocity; Acceleration and Jerk; Graphical Understanding of Motion; Motion in Straight Line; Equations of Motion; Relative Motion; Solving 1-D Motion; Projectile Motion; Breaking Down Multi-D Motion; Forces & Types; Newton's Laws of Motion; Frames of Reference; Pseudo Forces & Inertia; Free Body Diagrams; Friction & Types; Normal & Coefficient of Friction; Multi-D FBDs with Friction; Multi-D NLM & Friction Problems; Angular Coordinate System; Radial and Tangential Vectors; CM: Angular Displacement & Speed; CM: Angular Velocity & Acceleration; CM: Centripetal & Centrifugal; Solving Circular Motion; Kinetic Energy; Potential Energy; Work Done; Spring Force; Conservative vs Non-Conservative Forces; Work and Energy Theorem; Centre of Mass; CoM: System of Objects; CoM: Distributed Systems; CoM: Multi-Dimensional Objects; Linear Momentum; Conservation of Linear Momentum; Conservation of LM: Multi-Dimensional; Conservation of LM: Multi-Stage; Collisions for Rigid Bodies; Elastic Collision; Inelastic Collision; Coefficient of Restitution; Multi-Dimensional Collisions.

## LECTURE MAP (portal)
L1 31 Aug Measurement | L2 2 Sep Vectors+Math | L3 7 Sep Kinematics | L4 9 Sep Relative+Projectile | L5 16 Sep NLM+FBD | L6 21 Sep Friction | L7 23 Sep Circular | L8 28 Sep Work and Energy | L9 30 Sep Circular/CM | L10 5 Oct Circular/CM. L11-13 are OUTSIDE IA-1 (syllabus stops at L10). g used: 9.8 in worksheets, 10 in some contest questions. sin37=0.6, cos37=0.8.

## ALL MY QUESTIONS (worksheet + contest). Solve these exact styles, then go harder.
# AP-IA1 COUNTER — THE SETTER'S OWN BANK, SOLVED
Exam: Applied Physics 1 IA-1, Tue 27 Oct 2026, 9:40 AM. Format (S-VYASA template, same as maths today): Section A 5×3M all, Section B 3×5M choose (A)-or-(B), 30M, 2h, show reasoning, no calculator, g=9.8 m/s² unless told (ONE question used g=10 — check the paper!).

Paper-setter's DNA (from his contests): MCQ = precise definition; 2M = single-step calc; 5M = (a)(b)(c) clean multi-part; signature = "explain without calculating" + story context (airplane, ball-kick, ice-tray). Questions are RE-PICKED FROM HIS WORKSHEETS WITH NEW NUMBERS. Own every method below.

---
# BLOCK 1 — MEASUREMENT (L1) — his worksheet Q1–Q11
**Q1 (defn, 3M script).** Importance of measurement in engineering.
REASON: Measurement = numerical value + unit. Engineering needs it for (i) accuracy/quality control (ii) comparison across teams (iii) manufacturing consistency/tolerances (iv) scientific communication (v) safety limits. Without standardized units → mismatches (NASA Mars Orbiter).

**Q2.** Fundamental vs derived + SI units of any 5 fundamental.
REASON: Fundamental = independent, cannot be defined via others (mass M, length L, time T, temperature Θ, electric current I, amount of substance N, luminous intensity J). Derived = defined from fundamentals via laws (velocity LT⁻¹, force MLT⁻²). Examples: length → meter; derived: speed = distance/time.
His 5: pick M, L, T, Θ, I (or N, J).

**Q3. Dimensional formulas — memorize cold:**
(a) Velocity = LT⁻¹  (b) Acceleration = LT⁻²  (c) Force = MLT⁻²  (d) Work = ML²T⁻²  (e) Pressure = ML⁻¹T⁻²
Bonus he wrote on student paper: Planck constant h = ML²T⁻¹; gravitational constant G = M⁻¹L³T⁻². Also know: momentum MLT⁻¹, energy ML²T⁻², power ML²T⁻³, angular momentum ML²T⁻¹, surface tension MT⁻², viscosity ML⁻¹T⁻¹, frequency T⁻¹.

**Q4. Scientific notation + order of magnitude:**
(a) 0.000456 = 4.56×10⁻⁴, order 10⁻⁴  (b) 7,850,000 = 7.85×10⁶, order 10⁷ (7.85≥√10≈3.16 rounds up)
(c) 299,792,458 = 2.99792458×10⁸, order 10⁸  (d) 0.0000000082 = 8.2×10⁻⁹, order 10⁻⁸
RULE: order of magnitude = round mantissa to 1,10-power: if mantissa ≥√10≈3.16 → up, else down.

**Q5.** Rod measured 25.60 cm, true 25.30 cm. (a) Absolute error (b) Relative (c) Percentage.
(a) ΔL = |25.60−25.30| = 0.30 cm  (b) relative = 0.30/25.30 = 0.0119  (c) %= 1.19%
(His student wrote true=25.50 by misreading → 0.10, 0.00392, 3.92% — DON'T copy student's numbers, follow the printed text.)

**Q6.** Disc r=(10.0±0.2) cm. % error in area A=πr².
ΔA/A = 2(Δr/r) = 2×0.2/10 = 0.04 → **4%**. (Power rule: exponent multiplies relative error.)

**Q7.** A=(50.0±0.5), B=(20.0±0.2), Z=A/B. Max absolute + relative error.
ΔZ/Z = ΔA/A + ΔB/B = 0.01+0.01 = 0.02 → relative 2%. Z=2.5 → ΔZ = 0.05 → **Z = 2.5 ± 0.05**.

**Q8.** s = ut + ½at² dimensional check.
[s]=L; [ut]=LT⁻¹·T=L; [at²]=LT⁻²·T²=L. L = L+L ✓. (Write "both terms have dimension L, equation dimensionally correct".)

**Q9 (story, his signature!).** SI vs Imperial teams → mission failure. 
REASON: 1999 Mars Climate Orbiter — Lockheed Martin used pound-force-seconds (Imperial thrust data), NASA navigation used newton-seconds (SI). Mixed units in same equation → navigation model off by factor 4.45 → orbiter entered Mars atmosphere too low and disintegrated. Lessons: enforce SI-only pipelines; unit-tag every variable; automated unit-checking software; dimensional analysis as sanity check; standardized interfaces between teams.

**Q10.** Cube side (5.00±0.02) cm. (a) % error in volume (b) max absolute error.
V=s³. (a) ΔV/V = 3Δs/s = 3×0.02/5 = 0.012 → **1.2%**. (b) ΔV = 3s²Δs = 3×25×0.02 = **1.5 cm³** (or 1.2%×125=1.5).

**Q11 (story!).** Mars Climate Orbiter: what happened, which units, lessons — same as Q9 answer. (1999, lost ~$125M; thrust data in lbf·s vs required N·s.)

**EXAM PREDICTION for Block 1:** error-propagation 5M (Q6/Q7/Q10 type) + dimensional-check 2M + Mars story 3M "explain". Q3-style MCQ on random vs systematic (from contest Q3: unpredictable variations = RANDOM error).

---
# BLOCK 4/6 — FRICTION + NLM (L5–L6) — his worksheet Q1–Q11, g=9.8
**Q1.** 5 kg, μs=0.40, max force without moving. f_s,max = μs·m·g = 0.40×5×9.8 = **19.6 N**.
**Q2.** 10 kg pulled 35 N, μk=0.20. (a) N=mg=98 N (b) f_k=19.6 N (c) F_net=35−19.6=15.4 N (d) a=15.4/10=**1.54 m/s²**.
**Q3.** 6 kg, μs=0.50, μk=0.30, F=20 N. f_s,max=0.5×6×9.8=29.4 N > 20 → DOES NOT MOVE. Actual static friction = **20 N** (self-adjusting, equals applied).
**Q4.** 8 kg, μs=0.40, μk=0.25, force ramped from 0. (a) moves at 0.40×8×9.8=**31.36 N** (b) just after: f_k=0.25×8×9.8=**19.6 N** (c) a=(31.36−19.6)/8=**1.47 m/s²**.
**Q5.** 5 kg, F=40 N at 30° ABOVE horizontal, μk=0.20. (a) Fx=40cos30=**34.64 N** (b) Fy=40sin30=**20 N** (c) N=mg−Fy=49−20=**29 N** (pull reduces normal!) (d) f_k=0.2×29=**5.8 N** (e) a=(34.64−5.8)/5=**5.77 m/s²**.
**Q6.** 10 kg, F=50 N at 30° BELOW horizontal (push!), μk=0.25. (a) N=mg+Fsin30=98+25=**123 N** (push increases normal!) (b) f_k=0.25×123=**30.75 N** (c) F_net=50cos30−30.75=43.30−30.75=**12.55 N** (d) a=12.55/10=**1.26 m/s²**.
**Q7.** 10 kg on 30° incline, μk=0.20, slides down. (a) W∥=mg sin30=**49 N** (b) W⊥=mg cos30=**84.87 N** (c) N=84.87 N (d) f_k=0.2×84.87=**16.97 N** (opposes slide, up the plane) (e) a=(49−16.97)/10=**3.20 m/s²** down the plane.
**Q8.** 5 kg on 37° incline, μs=0.50, rest or slide? g=10, sin37=0.6, cos37=0.8. W∥=5×10×0.6=30 N; f_s,max=0.5×5×10×0.8=20 N. 30>20 → **SLIDES**. (Test: tan37=0.75 > μs=0.50 → slides. General rule: slides iff tanθ > μs.)
**Q9.** 4 kg on 30° incline, F=30 N up-parallel, μk=0.20. N=4×9.8×cos30=33.95; f_k=6.79; W∥=19.6. Net up = 30−19.6−6.79 = +3.61 → a = 3.61/4 = **0.90 m/s² UP the plane**.
**Q10.** 6 kg pulled up 30° incline by T=50 N, μk=0.15. Draw FBD (weight components, N, T up-parallel, f_k down-parallel). N=6×9.8×cos30=50.92; f_k=7.64; W∥=29.4; a=(50−29.4−7.64)/6=**2.16 m/s²** up.
**Q11 (pulley!).** 5 kg on rough table (μk=0.20) + 3 kg hanging, frictionless pulley. Whole-system method: a = (m₂g − μk m₁ g)/(m₁+m₂) = (29.4 − 9.8)/8 = **2.45 m/s²**. T = m₂(g−a) = 3×7.35 = **22.05 N** (check: T − f_k = m₁a → 22.05−9.8=12.25=5×2.45 ✓).
FBD SCRIPT (he draws these!): box → N up, mg down, T right, f_k left. On incline: mg sinθ down-parallel, mg cosθ into plane.

---
# BLOCK 5/7 — CIRCULAR MOTION (L7) — his worksheet Q1–Q30
**Q1.** Car, r=50 m, v=10 m/s. ω = v/r = **0.2 rad/s**.
**Q6.** Wheel r=0.5 m at 120 rpm. (a) ω=120×2π/60=**4π ≈ 12.57 rad/s** (b) v=rω=0.5×4π=**2π ≈ 6.28 m/s**.
**Q11.** Torque, F=100 N at r=0.5 m, angle with radius 90°/60°/0°. τ=rF sinθ: (a) **50 N·m** (b) 100×0.5×sin60=**43.3 N·m** (c) sin0=0 → **0** (force along radius does no torque — same reason centripetal does no work).
Formulas cold: ω=v/r=2πf=2π/T; a_c=v²/r=rω²; v=rω; τ=rF sinθ; α=dω/dt; rotational kinematics mirror linear (θ↔x, ω↔v, α↔a); point on axis r=0 → v=0, a_c=0. rpm→rad/s: ×2π/60. Q27-type: "car moves, speed doubles → a_c quadruples (v²)". Q19: linear velocity of object at radius r on rotating wheel = rω. Q20: difference between linear and angular velocity — dimension + frame (tangent vs rotation). Q28-30: (a) angular acceleration (b) linear velocity (c) radial/centripetal (d) tangential acceleration a_t=rα (e) total a=√(a_t²+a_c²).

---
# BLOCK 6 — WORK & ENERGY (L8) — his worksheet Q1–Q15 (from photo inventory)
Core pattern of his Qs: W=Fs cosθ; KE=½mv²; W_net=ΔKE (work-energy theorem); PE_g=mgh; spring PE=½kx²; power=W/t=Fv; conservative force (gravity, spring) → path-independent, closed loop W=0; friction → non-conservative, W=−f_k d, converts to heat.
Q13 pattern: 4 kg block pushed — (a) work done by applied force (b) work done by friction (c) net work (d) final KE (e) final speed [W_net=ΔKE=½mv²]. Q14: block mass m, energy remains unchanged → only conservative forces act / KE+PE constant. Q15: particle falls under gravity with friction → total energy NOT conserved, lost to heat = f_k·d.
ZERO-WORK SCRIPT: force perpendicular to motion → W=0 (centripetal on circular path; normal force on flat road; gravity at constant height).

---
# BLOCK 8 — COLLISIONS + MOMENTUM (L10) — his worksheet (Q1–15 across photos)
**Two-equation machine (write every time):**
(1) momentum: m₁u₁+m₂u₂ = m₁v₁+m₂v₂
(2) restitution: v₂−v₁ = e(u₁−u₂)  [separation speed = e × approach speed]
**Q13.** Two identical balls elastic, first 8 m/s, second at rest. e=1 identical masses → EXCHANGE velocities: v₁=0, v₂=8 m/s. (One-line theorem: elastic + equal mass + target at rest → swap.)
**Q9.** 3 kg at 6 m/s hits 2 kg at rest, e=0.4. (a) approach=6; separation=e×6=2.4. Eqs: 3v₁+2v₂=18; v₂−v₁=2.4 → v₂=5.04, v₁=2.64 m/s. (b) separation speed=2.4 m/s (c) approach speed=6 m/s.
**Stick-together type** (m_074: "objects move together", e=0.5/0.6/0.4): perfectly inelastic → common velocity v=(m₁u₁+m₂u₂)/(m₁+m₂); KE lost = ½μ_rel u² (reduced mass form) — show that KE is max lost when e=0.
**Impulse:** J=FΔt=Δp=m(v−u). Q8 of momentum worksheet: (a) initial momentum=mu (b) final common momentum (c) change in momentum (d) impulse — all equal to J.
**Q17 conceptual:** net external force zero → (a) total momentum CONSTANT (conserved) (b) velocity of centre of mass constant/zero-change (c) acceleration of CM = 0. REASON script: F_ext=dp/dt; isolated system → p const.
**Two-stage (notes m_106):** explosion → internal forces, momentum conserved each stage: (m_A+m_B)v_before = m_A v_A + m_B v_B.
**2D momentum (notes m_107):** resolve into x/y; conserve separately: m₁u₁x+m₂u₂x = m₁v₁x+m₂v₂x, same for y; then combine √(vx²+vy²).

---
# BLOCK 7 — CENTRE OF MASS (L9) + HIS CONTEST-2 SUBJECTIVE
**His Worksheet Q1–4 (m_104):** two particles, three particles CoM.
x_CM=(m₁x₁+m₂x₂+…)/(m₁+m₂+…); 2D → both x_CM, y_CM; R_CM=Σmᵢrᵢ/M. Symmetry shortcut: uniform rod → midpoint; uniform disc/cube/sphere → geometric centre; L-shaped → split into rectangles.
**His Contest-2 question (0/40 XP, still open — STUDY THE ANSWER PATTERN):** ice cube (m, L) melts on tray (M), water spreads thin. Does CoM change?
REASONING SCRIPT (his marking scheme wants this): CoM height depends on vertical distribution of mass. Before melt: ice CoM at L/2 above tray base, so combined CoM sits slightly above base ~ mL/2/(M+m). After melt: all mass lies in negligibly thin layer at tray base → water CoM at base level. Combined CoM drops toward the base. Magnitude of drop = [mL/2]/(M+m) — larger when m≫M, smaller when M≫m. Direction: always downward (mass redistributed toward base). No numbers, pure physical reasoning — EXACTLY his style: "without performing numerical calculations, explain... discuss how redistribution affects... relative masses influence magnitude."
**Ice-tray TEMPLATE for exam variants:** (i) does CM move? yes/no (ii) which direction (iii) what sets magnitude (mass ratio + height change).

---
# BLOCK 2/3 — VECTORS, CALCULUS, KINEMATIC GRAPHS, PROJECTILE (L2–L4)
**His contest Q13 (MCQ):** vector × negative scalar → MAGNITUDE scales, DIRECTION REVERSED (option: direction is reversed).
**His contest Q18:** (1) dy/dx of y=4x²−3x+7 = 8x−3 (2) ∫(3x²+2x)dx = x³+x²+C.
**His contest Q19:** position-time graphs: slope = velocity; straight line → constant velocity (avg = instantaneous, both constant); curved (parabola) → velocity changing (avg over interval ≠ instantaneous at point; instantaneous = slope of tangent).
**His contest Q24:** ball kicked 25 m/s at 37°: (1) ux=25cos37=20 m/s, uy=25sin37=15 m/s (2) T=2uy/g=30/9.8≈3.06 s (or g=10 → 3.0 s) (3) H=uy²/(2g)=225/19.6≈11.5 m (g=10 → 11.25 m).
**His contest Q28b:** airplane 100 km/h pointing north, wind 60 km/h east. v_ground = vector sum: magnitude √(100²+60²)=√13600≈116.6 km/h; direction θ=tan⁻¹(60/100)≈31° east of north. REASON: ground velocity = airspeed (through air) + wind velocity (air over ground).
**Projectile master formulas:** ux=u cosθ, uy=u sinθ; T=2uy/g; H=uy²/2g; R=u²sin2θ/g; at any time: vx=ux (constant), vy=uy−gt; angle of velocity: tanφ=vy/vx. RANGE MAX at θ=45°; complementary angles (θ, 90−θ) → same range.
**Relative motion (worksheet Q types m_050):** v_AB = v_A − v_B; boat/river: time to cross = d/v_boat (perpendicular), drift = v_stream × t; rain-man umbrella angle: tanθ = v_rain/v_man.
**Vector arithmetic:** A·B=AB cosθ (scalar), A×B=AB sinθ (vector, right-hand); unit vector Â=A/|A|; resolution along x/y; triangle law + parallelogram law: |A+B|=√(A²+B²+2AB cosθ).

---
# DEFINITION FLASH — his 1M MCQs test THESE exact words
- Error from unpredictable/random variations = **Random error** (vs systematic = consistent bias, gross = human blunder)
- Vector × (−k): magnitude ×k, direction reversed
- Work by centripetal force on circular motion = **zero** (force ⊥ displacement)
- Static friction = self-adjusting, ≤ μsN; kinetic = constant μkN (usually μk < μs)
- Coefficient of restitution e = separation speed / approach speed; e=1 elastic, e=0 perfectly inelastic
- Momentum conserved when **net external force = 0** (internal forces cancel in pairs — Newton's 3rd)
- CoM of uniform symmetric body = geometric centre
- Order of magnitude: mantissa ≥√10 → round up the power
- Dimensions: M mass, L length, T time, Θ temp, I current, N amount, J luminous
- SI base units: kg, m, s, K, A, mol, cd
- Torque τ = rF sinθ; zero when force ∥ r
- Angular: ω=v/r, a_c=v²/r=rω², a_t=rα
- Normal force on horizontal surface = mg (no other vertical force); with F at angle above: mg−F sinθ; push below: mg+F sinθ

---
# EXAM-DAY PROTOCOL (calibrated to today's maths pain)
1. FIRST pass (35 min): Section A all five — definitions flash + one-step calcs from this bank. Never blank: write the formula + definition sentence (partial marks exist; today's paper awarded (1)(1)(1) splits).
2. SECOND pass (60 min): Section B — pick the (A)/(B) pair matching THIS bank hardest (friction-incline pulley / collisions e / error propagation). Each 5M = (a)(b)(c) — label parts, show numbers+units.
3. LAST (15 min): the "explain" questions — use the REASONING SCRIPTS above verbatim-structure: claim → physical law → why → magnitude-influence. His CM ice-tray answer = the template.
4. If a question looks novel: it's a worksheet question with changed numbers. Identify block → pull THIS method → re-run numbers. The gaps that hurt maths (novelty panic) die here because you own his bank.
5. g: default 9.8; if the paper says g=10 (like friction Q8 did), switch immediately. sin37=0.6, cos37=0.8 given when needed.
6. Units on every line, diagrams for FBD/incline/pulley (he draws them in his notes), reasoning words: "because", "therefore", "since net force..." — his papers reward written justification over bare answers.

---
# BLOCK 5/7 FULL — CIRCULAR MOTION WORKSHEET Q1–Q30 (ALL SOLVED — HIS BANK)
**Q1.** r=2 m, arc 6 m. θ=s/r=**3 rad**.
**Q2.** 120° → 120π/180=**2π/3 ≈ 2.09 rad**.
**Q3.** θ=3π/4, r=4 m. s=rθ=**3π ≈ 9.42 m**.
**Q4.** θ=60°, r=5 m. (x,y)=(r cos60, r sin60)=**(2.5, 4.33) m**.
**Q5.** r=3 m, v=6 m/s. a_c=v²/r=**12 m/s²**.
**Q6.** r=2 m, ω=5 rad/s. (a) v=rω=**10 m/s** (b) a_c=rω²=**50 m/s²**.
**Q7.** a_t=4 m/s², r=2 m. α=a_t/r=**2 rad/s²**.
**Q8.** r=4, ω=3, α=2. (a) a_t=rα=**8** (b) a_r=rω²=**36** (c) a=√(64+1296)=**36.9 m/s²**.
**Q9.** 20 rev in 10 s. (a) θ=40π ≈ **125.7 rad** (b) ω=**4π ≈ 12.6 rad/s**.
**Q10.** T=0.5 s. ω=2π/T=**4π ≈ 12.6 rad/s**.
**Q11.** f=5 Hz. (a) ω=2πf=**10π ≈ 31.4 rad/s** (b) T=1/f=**0.2 s**.
**Q12.** 8π rad in 4 s. avg ω=**2π ≈ 6.3 rad/s**; revs=8π/2π=**4**.
**Q13.** rest, α=3, t=5. (a) ω=αt=**15 rad/s** (b) θ=½αt²=**37.5 rad**.
**Q14.** ω₀=4, α=3, t=6. ω=4+18=**22 rad/s**; θ=24+54=**78 rad**.
**Q15.** ω₀=20, α=−4→rest. (a) t=20/4=**5 s** (b) θ=(0−400)/(−8)=**50 rad**.
**Q16.** θ=20, 4→12 rad/s. α=(144−16)/40=**3.2 rad/s²**.
**Q17.** m=2, r=4, v=8. (a) a_c=**16 m/s²** (b) F=**32 N**.
**Q18.** 1000 kg, r=50, v=10. F_c=1000×100/50=**2000 N**.
**Q19.** 5 kg, ω=4, r=2. (a) v=**8 m/s** (b) a_c=**32 m/s²** (c) F_c=**160 N**.
**Q20 (explain — his style).** Centripetal vs centrifugal. SCRIPT: Centripetal is the REAL inward net force (tension/friction/gravity) that continuously redirects the velocity of a body toward the centre so the circular path continues; it acts ON the moving body, in an inertial frame. Centrifugal is a PSEUDO (fictitious) force that appears only in the rotating (non-inertial) reference frame, directed radially outward; it has no physical agent/interaction — it accounts for the inertia of the body resisting the inward turn. Examples: centripetal — tension in the string of a whirled stone, friction force banking a car, gravity on a satellite; centrifugal — the outward push felt by a passenger on a merry-go-round, clothes in a spinning dryer flinging water outward.
**Q21.** 4 kg, L=2 m, v=6 m/s horizontal. T=mv²/r=**72 N**.
**Q22.** 2 kg, 1.5 m, 4 m/s. (a) a_c=16/1.5=**10.7 m/s²** (b) T=**21.3 N**.
**Q23.** 1200 kg, r=40, v=12. F_c=1200×144/40=**4320 N**.
**Q24 (friction-circular combo!).** 5 kg, r=2 m, μ=0.4, max v no-slip. μmg=mv²/r → v=√(μgr)=√7.84=**2.8 m/s**.
**Q25.** r=5, ω=2, α=3. (a) a_t=**15** (b) a_r=**20** (c) a=√(225+400)=**25 m/s²**.
**Q26.** 3 kg, r=2, 4→8 m/s in 2 s. (a) a_t avg=**2 m/s²** (b) a_c at 8: **32 m/s²** (c) a=√(4+1024)=**32.1 m/s²**.
**Q27 (comment question!).** r=100, v=20: a_c=**4 m/s²**. Speed doubled: a_c'=v'²/r=4v²/r=**16 m/s²**. COMMENT: centripetal acceleration depends on the SQUARE of speed — doubling v multiplies a_c by 4 (r fixed). This is why highway curves require much stricter speed limits for heavy/fast vehicles.
**Q28.** r=0.5, 120 rpm. (a) ω=**4π ≈ 12.6 rad/s** (b) v=**2π ≈ 6.3 m/s** (c) a_c=0.5×16π²=**8π² ≈ 79 m/s²**.
**Q29 (function type!).** r=3, θ(t)=2t²+3t. (a) ω=dθ/dt=4t+3 → t=2: **11 rad/s** (b) α=**4 rad/s²** (c) v=rω=**33 m/s** (d) a_t=rα=**12 m/s²** (e) a_c=rω²=**363 m/s²**.
**Q30.** r=2, ω(t)=3t²+2. (a) α=6t → t=2: **12 rad/s²** (b) v=rω=2(14)=**28 m/s** (c) a_t=rα=**24 m/s²** (d) a_c=rω²=2×196=**392 m/s²**.

---
# BLOCK 6 FULL — WORK & ENERGY WORKSHEET Q1–Q12 (SOLVED)
**Q1.** 5 kg, 4 m/s. KE=½×5×16=**40 J**.
**Q2.** p=10 kg·m/s, m=2. K=p²/2m=100/4=**25 J**.
**Q3.** 5 kg, h=10 m. PE=5×9.8×10=**490 J**.
**Q4.** F=80 N, d=8 m along force. W=**640 J**.
**Q5.** F=100 N, d=5 m at 60°. W=100×5×cos60=**250 J**.
**Q6.** Spring 0.1→0.3 m, k=200. Work by spring = −½k(x₂²−x₁²)=−100×(0.09−0.01)=**−8 J** (spring does negative work when stretched further; work done by external agent = +8 J).
**Q7 (explain!).** Same work both paths → FORCE IS CONSERVATIVE. SCRIPT: Work done is path-independent (equal for the two paths), hence the work over any closed loop is zero; that is exactly the defining property of a conservative force. (Contrast: friction would give longer path → more negative work — path-dependent, non-conservative.)
**Q8.** 4 kg rest, W_net=200 J. 200=½×4×v² → v=**10 m/s**.
**Q9.** 5 kg, 4 m/s, W=90 J. 90=2.5(v²−16) → v=√52=**7.21 m/s**.
**Q10.** 2 kg from rest h=20. v=√(2gh)=√392=**19.8 m/s**.
**Q11.** 5 kg h=8, friction −50 J. 392−50=2.5v² → v=√136.8=**11.7 m/s**.
**Q12.** 10 kg h=5, friction −100 J. 490−100=5v² → v=√78=**8.83 m/s**.

**Q13 (5-part!).** 4 kg pushed 30 N through 10 m, friction 5 N opposing, from rest. (a) W_app=30×10=**300 J** (b) W_fric=−5×10=**−50 J** (c) W_net=**250 J** (d) KE_f=250 J (e) v=√(2×250/4)=√125=**11.2 m/s**.
**Q14.** KE=½mv²=K kept constant, m→4m. ½mv²=½(4m)v'² → **v'=v/2** (speed halves; momentum doubles... wait p=4m×v/2=2mv — increases).
**Q15 (explain!).** A→B with gravity+friction. SCRIPT: Gravity is conservative — its work (−mgh) depends only on the vertical height difference, not path. Friction is non-conservative — it always does negative work −f_k·d proportional to path length, converting mechanical energy into heat. Hence total mechanical energy (KE+PE) is NOT conserved between A and B: ΔE_mech = W_friction = −f_k d. (Total energy including heat is conserved.)

---
# BLOCK 8 FULL — COLLISIONS WORKSHEET Q1–Q12 (SOLVED)
**Q1.** 2 kg @6 m/s head-on, stationary 4 kg. Total momentum before = 2×6 = **12 kg·m/s**.
**Q2.** 5 kg @4 + stationary 3, stick. v=(5×4)/8=**2.5 m/s**.
**Q3.** 2 kg @8 + stationary 6, perfectly inelastic. (a) p_i=16 (b) v=16/8=**2 m/s** (c) KE_i=½×2×64=**64 J** (d) KE_f=½×8×4=**16 J** (e) lost=**48 J**. (Check: ½μu²=½(12/8)×64=48 ✓.)
**Q4.** 2 kg @10 elastic, stationary 3. v1=(m1−m2)u/(m1+m2)=−10/5=**−2 m/s** (rebounds back); v2=2m1u/(m1+m2)=40/5=**8 m/s**.
**Q5.** 4 kg @6 vs 2 kg @3 opposite. u1=6, u2=−3. v1=[(4−2)6+2×2×(−3)]/6=(12−12)/6=**0**; v2=[(2−4)(−3)+2×4×6]/6=(6+48)/6=**9 m/s**.
**Q6.** 5 kg @8 + stationary 3, stick. (a) **5 m/s** (b) KE_i=160 J (c) KE_f=100 J (d) lost=**60 J**.
**Q7.** 2 kg @10, stationary 3, e=0.6. v2−v1=6; 2v1+3v2=20 → v1=**0.4**, v2=**6.4 m/s**.
**Q8.** 4 kg @8, stationary 6, e=0.5. v2−v1=4; 4v1+6v2=32 → v1=**0.8**, v2=**4.8 m/s**.
**Q9.** 3 kg @6, stationary 2, e=0.4. approach=6; separation=**2.4 m/s**; solve → v1=**2.64**, v2=**5.04 m/s**.
**Q10.** 2 kg @12, stationary 4, e=0.5. v2−v1=6; 2v1+4v2=24 → v2=6, v1=**0**; v2=**6 m/s**. (Special: lighter object stops dead.)
**Q11 (2D stick — HIS FAVOURITE).** 4 kg east@5 + 6 kg north@3, stick. px=20, py=18. v=√(400+324)/10=√724/10≈**2.69 m/s**; θ=tan⁻¹(18/20)≈**42° north of east**.
**Q12.** 5 kg +x@8, 3 kg +y@6, stick. px=40, py=18. v=√(1600+324)/8≈**5.48 m/s**; θ=tan⁻¹(18/40)≈**24° from x-axis**.
**Q13.** Identical balls elastic, first@8, second at rest → **swap**: (0, 8 m/s).
**Q9-rematch from photo Q15-type:** 4 kg block at speed, e=0.5 — same two-equation machine.
**KE-loss shortcut:** ΔKE=½ m1m2(u1−u2)²(1−e²)/(m1+m2). Perfectly inelastic: ΔKE=½μu² (max possible loss).

---
# HIS CONTEST-1 5M QUESTIONS (SOLVED — closest to Section B tomorrow)
**Q21 error-propagation (memorize this exact template).** F=80.0±0.8 N, a=25.0±0.5 m/s². (1) m=F/a=**3.20 kg** (2) Δm/m=0.8/80+0.5/25=0.03 → Δm=**0.096 kg** (3) relative=**0.03** (4) % = **3%**. RULE: multiply/divide → relative errors ADD; power n → multiply by n; add/subtract → absolute errors ADD.
**a(t) integration.** a=10t+6, v(0)=4, x(0)=3. v(t)=∫a=**5t²+6t+4**; x(t)=∫v=**(5/3)t³+3t²+4t+3**; x(1)=**14.67 m**. (His integration questions = this exact skeleton: integrate, fix constant from initial condition, evaluate.)
**Car traffic-signal.** 0→20 m/s in 5 s, then 20 for 5 s. Displacement=area under v-t=½×5×20+5×20=**100 m**; avg v=**10 m/s**; avg a first 5 s=**4 m/s²**. Graph: ramp then flat.
**Q24 projectile (3-part).** 25 m/s at 37°: ux=20, uy=15 (sin37=0.6, cos37=0.8 given); T=2uy/g=3.06 s (g=9.8) or 3.0 (g=10); H=uy²/2g=11.5 m (or 11.25).
**Q28b airplane.** 100 north + wind 60 east: |v|=√(10000+3600)=**116.6 km/h**; θ=tan⁻¹(60/100)=**31° east of north**. (Check if question asks "where must it point to go due north": then aim θ west of north with sinθ=60/100 → θ=37°; read the exact ask.)

# HIS CONTEST-1 MCQs (1M each — definition precision)
Q3: unpredictable variations = **random error**. Q8: max range at **45°**. Q9: sig figs in 0.00456 = **3**. Q10: SI unit acceleration = **m/s²**. Q11: perpendicular vectors dot product = **5×4×cos90=0**. Q12: (30−10)/5=**4 m/s²**. Q13: negative scalar reverses **direction**.

# MOMENTUM WORKSHEET Q5–Q9 (SOLVED)
Q5. Rod 6 m, 12 kg, from x=2 to x=8. CoM=midpoint=**x=5 m**.
Q6. 5 kg @4. p=**20 kg·m/s**.
Q7. 2 kg right@8 + 4 kg left@3. Total p=16−12=**4 kg·m/s to the right**.
Q8 (wall-rebound classic). 0.5 kg @10 hits wall, rebounds @6 opposite. (a) p_i=5 (b) p_f=−3 (c) Δp=**−8 kg·m/s** (d) impulse=**−8 N·s** (direction: away from wall... actually Δp is opposite to initial direction = outward).
Q9. 4 kg @6 + stationary 2, stick. v=24/6=**4 m/s**.

# CoM WORKSHEET Q1–Q4 (SOLVED)
Q1. 2 kg at 0, 8 kg at 5. x_CM=(8×5)/10=**4 m**.
Q2. (2,0),(3,4),(5,10). x_CM=(0+12+50)/10=**6.2 m**.
Q3. 2 & 8 kg, 10 m apart. From 2 kg: x=(8×10)/10=**8 m** (near the heavy one — CoM always closer to larger mass).
Q4. 2@(0,0), 3@(6,0), 5@(0,4). x=18/10=**1.8**; y=20/10=**2.0** → **(1.8, 2.0)**. (His student note: solve x and y separately → (x,y).)

# THE 30-SECOND TEMPLATES FOR HIS FAVOURITE 5M SHAPES
1. **Error propagation:** m=F/a style → value, Δ via relative add, relative, %.
2. **a(t)→v(t)→x(t):** integrate twice, pin constants, evaluate.
3. **v-t graph story:** draw ramp/flat, displacement=area, avg v=disp/time, avg a=Δv/Δt.
4. **Projectile (a)(b)(c):** components → T → H. (Add R if asked.)
5. **Collision with e:** momentum eq + restitution eq → solve system.
6. **2D stick:** conserve px and py separately → v=√(vx²+vy²), θ=tan⁻¹(py/px).
7. **Incline+pulley friction:** whole-system a=(driving−resisting)/total mass; T from one body.
8. **CoM 2D:** weighted means per axis.
9. **Ice-tray explain:** claim → redistribution → direction → mass-ratio controls magnitude.

---
# CONTEST-1 Q18–Q20 + FULL Q28b (VERBATIM, SOLVED)
**Q18 (2).** dy/dx of y=4x²−3x+7 → **8x−3**. ∫(3x²+2x)dx → **x³+x²+C**.
**Q19 (2).** Graph 1 (straight line, rising): uniform motion — velocity constant; avg velocity = instantaneous velocity = slope (both constant). Graph 2 (curving upward, slope steepens): velocity increasing with time; instantaneous = slope grows; avg over [0,t] also grows.
**Q20 (2).** A=20 m/s, B=12 m/s same dir: v_A/B=**8 m/s**. Opposite: **32 m/s**.
**Q28b (10) An Airplane Flying in Wind.** Plane 100 km/h through air, points due north; wind 60 km/h east. East=+î, north=+ĵ.
(a) Pilot's claim WRONG: ground velocity = sum of air-relative + wind; pointing north still adds eastward wind → drifts northeast.
(b) v_air=100ĵ, v_wind=60î → v_ground=**60î+100ĵ**, |v|=√(3600+10000)=**116.6 km/h**, θ=**31° east of north**. In 30 min: displacement = **50î+50ĵ km** (30E, 50N... actually (30,50)). Sketch vector triangle (north leg 100, east leg 60, hypotenuse).
(c) To go due north: east component of v_air must cancel wind: v_air,x = **−60 km/h** (i.e., 60 west), north component = **100 km/h** (full? no: speed fixed at 100 → north comp = √(10000−3600)=**80 km/h**). Ground speed = 80 km/h due north. Point slightly west of north (sketch only, no angle).
(d) Wind 120 > plane speed 100: CANNOT — east component can cancel at most 100, wind is 120. Impossible.

# MOMENTUM WORKSHEET Q10–Q17 (SOLVED)
Q10. 2 kg east@6, 3 kg north@4. (a) p_x=**12** (b) p_y=**12** (c) |p|=**12√2≈17.0 kg·m/s** (d) θ=tan⁻¹(12/12)=**45° north of east**.
Q11. 2 kg east@5 + 1 kg north@4, stick. px=10, py=4 → vx=10/3, vy=4/3. (b) v=√(100+16)/3=**√116/3≈3.57 m/s** (c) θ=tan⁻¹(4/10)=**21.8° north of east**.
Q12. 2 kg@4 + 3 kg@6 same dir. (a) p=8+18=**26** (b) v_cm=26/5=**5.2 m/s**.
Q13. Mass 20, F=60 N → a_cm=**3 m/s²**. (His note: F=Ma on the whole system.)
Q14. m=10, a_cm=2 → F_net=**20 N**.
Q15 (double collision). 2@10 → hit 3 stationary stick → v=4; then 5 kg total @4 hits 5 stationary stick → **v=2 m/s**.
Q16 (explosion). 10 kg at rest → 4 kg piece @12. 0=48+6v → **v=−8 m/s** (6 kg piece: 8 m/s opposite).
Q17. F_net=0: (a) total momentum **constant/conserved** (b) v_cm **constant** (c) a_cm=**0**.

---
# CONTEST-1 Q28a (10M), Q24, Q25 (FULL, SOLVED)
**Q28a Ball-in-accelerating-truck (g=10).** Truck 10 m/s, a=2; ball thrown 5.0 m/s up relative to truck.
(a) Claim WRONG: ball keeps truck's release velocity, but truck accelerates → truck pulls ahead.
(b) v_ball ground=10î+5ĵ. T=2×5/10=**1.0 s**. Ball x=10 m; hand x=10+½·2·1=11 m → **1 m behind the hand**.
(c) Need ball x = hand x over T=1 s: vx·1=11 → vx=11 ground → **+1 m/s relative to truck (forward)**. Doubling truck's initial speed: truck disp=20·1+1=21, ball needs vx=21 → rel=21−20=**still 1 m/s** — design UNCHANGED (relative toss depends only on ½aT, not u).
(d) Time 1.0 s from 5.0 and 10.0 (2 sig figs) → **2 significant digits**.
**Q24 Projectile (g=10 GIVEN, sin37=0.6, cos37=0.8).** 25 m/s @37°: ux=**20**, uy=**15**; T=2uy/g=**3.0 s**; H=uy²/2g=**11.25 m**. (Check g per question: Q24 says g=10; worksheets say g=9.8 — READ IT.)
**Q25 Drone s(t)/y(t).** x=3t²+4t+2, y=2t³−3t²+5t. vx=6t+4, vy=6t²−6t+5. t=2: vx=**16**, vy=**17**, speed=**√545≈23.3 m/s**. ax=6, ay=12t−6 → t=2: ay=**18**, |a|=**√360≈19.0 m/s²**. θ=tan⁻¹(17/16)=**46.7°** above +x.

---
# FINAL EXAM-DAY REMINDER (physics-setter's DNA)
His Part-D 10M: "Evaluate a claim → Support your judgment (compute) → Design → Check/Assess a limitation" — ALWAYS answer all four verb-led parts in order, even if qualitative. His Part-C 5M: clean multi-part calc with given g and trig values. His Part-B 2M: one derivative/integral/graph statement. His Part-A 1M: exact-definition MCQ. If a mock appears tomorrow, expect sections in that order. Formula card: p=mv; p_i=p_f; e=−v_rel(f)/v_rel(i); v_cm=Σmivi/Σmi; a_cm=F_ext/M; x_cm=Σmixi/M; KE=½mv²; W=∫F·dr; work-energy ΔKE=W; friction f=μN (kinetic), f≤μsN; v²=u²+2as; T=2π√(L/g), ω²=r, a_c=v²/r=ω²r; relative v A/B=vA−vB; error: mult→relative add, power→×n.

---
# CONTEST-1 PART-A/B MCQs + SHORTS (FULL, SOLVED)
Q3. Unpredictable variations → **random error**. Q4. v=u+at=0+2(5)=**10 m/s**. Q5. Vector → **velocity**. Q6. Cross-product direction → **right-hand rule** (NOT parallelogram). Q7. Rate of change of velocity → **acceleration** (jerk = rate of change of acceleration — trap).
Q13. Vector × negative scalar → **direction reversed**. Q14. Triangle law → vectors arranged **head-to-tail**. Q15. Projectile vertical acceleration → **−g** (constant, downward; NOT zero, NOT +g).
**Q16 (2). Order of magnitude.** Write x=a×10ⁿ with 1≤a<10; if a≥√10≈3.16 round n up. 0.00000487=4.87×10⁻⁶, a=4.87≥3.16 → **10⁻⁵**. 564000000=5.64×10⁸, a≥3.16 → **10⁹**.
**Q17 (2). Dot vs cross.** Dot: scalar result, A·B=ABcosθ, commutative, defined via angle only. Cross: vector result (direction by right-hand rule, ⊥ to both), A×B=ABsinθ n̂, anti-commutative (A×B=−B×A). At least 2 differences each.

## MY LEARN-BY-QUESTIONS COURSE (already written by the other AI — use as the baseline to beat).
# AP PHYSICS 1 — IA-1 COMPLETE COURSE (Concept + Questions, From Scratch)
**Learn every concept AND solve every level of question you have, then go harder.**

HOW TO USE:
- Each block: READ the concept boxes first (understand, don't memorise). Then SOLVE the questions in order.
- Questions marked [HIS] are from your own WhatsApp worksheets / contests / Slack. Do these exactly.
- Questions marked [HARDER] are the same concept one step up — what he could ask beyond your bank.
- Check answers only AFTER you write your own.

---

# BLOCK 1 — MEASUREMENT & UNITS (L1)

## CONCEPT 1.1 — What measurement is
Measurement = a **number + a unit** that tells how much of something you have.
Example: length = 25.60 cm. The number alone (25.60) means nothing without "cm".
Why engineering needs it: quality control, comparing across teams, manufacturing tolerances, safety limits, scientific communication. Two teams using different units → disaster (see CONCEPT 1.4).

## CONCEPT 1.2 — Fundamental vs derived quantities
- **Fundamental** = defined on its own, not from others. The 7 SI ones: mass (kg), length (m), time (s), temperature (K), electric current (A), amount of substance (mol), luminous intensity (cd).
- **Derived** = built from fundamentals. Speed = length/time. Force = mass × acceleration.

## CONCEPT 1.3 — Dimensions
Write every quantity using **M** (mass), **L** (length), **T** (time).
- Velocity = L/T = **LT⁻¹**
- Acceleration = velocity/time = **LT⁻²**
- Force = mass × acceleration = **MLT⁻²**
- Work = force × distance = **ML²T⁻²**
- Pressure = force/area = **ML⁻¹T⁻²**
Rule of the game: in any correct equation, every term you add must have the SAME dimensions. That is a **dimensional check**.

## CONCEPT 1.4 — Scientific notation & order of magnitude
- Scientific notation: write as a × 10ⁿ where 1 ≤ a < 10.
  0.000456 = 4.56×10⁻⁴.  7,850,000 = 7.85×10⁶.
- Order of magnitude: look at the leading digit of a. If a ≥ 5, round the power UP by 1; if < 5, keep it.
  7.85×10⁶ → **10⁷**.  4.56×10⁻⁴ → **10⁻⁴**.  8.2×10⁻⁹ → **10⁻⁸**.

## CONCEPT 1.5 — Errors
Three families (his favourite MCQ):
- **Random error** = unpredictable up/down scatter (parallax, vibration). Fix: average many readings.
- **Systematic error** = one-way consistent bias (zero error, wrong calibration). Averaging does NOT remove it.
- **Gross error** = human blunder (misread, wrong button). Fix: re-measure carefully.

Three numbers you can always compute:
- **Absolute error** Δx = |measured − true| (has units)
- **Relative error** = Δx / true (no units)
- **Percentage error** = relative × 100

## CONCEPT 1.6 — Error propagation (how errors travel through a formula)
- **Add/subtract** quantities → their **absolute** errors add.
- **Multiply/divide** quantities → their **relative** errors add.
- Raise to power n → the relative error gets **multiplied by n**.
- Constants (like π) carry **no error**.

## CONCEPT 1.7 — Significant figures
Count the meaningful digits. Leading zeros do NOT count.
0.00456 → **3** significant figures (4, 5, 6).

## HIS QUESTIONS (do these exactly)
[HIS Q1] Why is measurement important in engineering? (write 4–5 reasons)
[HIS Q2] Name any 5 fundamental SI quantities and their units.
[HIS Q3] Write dimensional formulas of velocity, acceleration, force, work, pressure.
[HIS Q4] Write in scientific notation + give order of magnitude: 0.000456; 7,850,000; 299,792,458; 0.0000000082.
[HIS Q5] A rod is measured 25.60 cm; true value is 25.30 cm. Find absolute, relative, percentage error.
[HIS Q6] Disc radius r = (10.0 ± 0.2) cm. Find the % error in area A = πr².
[HIS Q7] A = (50.0 ± 0.5), B = (20.0 ± 0.2). Find the max absolute and relative error in Z = A/B.
[HIS Q8] Check dimensionally whether s = ut + ½at² is correct.
[HIS Q9] Explain the Mars Climate Orbiter failure: what units were mixed, what happened, and list lessons a company should enforce.
[HIS Q10] Cube side = (5.00 ± 0.02) cm. Find (a) % error in volume (b) max absolute error in volume.
[HIS Q11] Same story question as Q9 in another form — retell what happened and the lessons.
[HIS CONTEST] What type of error comes from unpredictable variations in measurements? (answer: random error)
[HIS CONTEST] What is the order of magnitude of 0.00000487 and 564000000?

## ANSWERS
Q1 → Measurement = number + unit. Engineering needs: accuracy/quality control, comparison across teams, manufacturing consistency/tolerances, scientific communication, safety limits. Missing a standard unit system caused a real spacecraft loss.
Q2 → mass kg, length m, time s, temperature K, current A (any 5 of the 7).
Q3 → LT⁻¹, LT⁻², MLT⁻², ML²T⁻², ML⁻¹T⁻².
Q4 → 4.56×10⁻⁴ (10⁻⁴); 7.85×10⁶ (10⁷); 2.998×10⁸ (10⁸); 8.2×10⁻⁹ (10⁻⁸).
Q5 → ΔL = 0.30 cm; relative = 0.30/25.30 = 0.0119; % = 1.19%.
Q6 → ΔA/A = 2 × (0.2/10.0) = 0.04 → **4%**. (power rule: the square multiplies the relative error by 2; π has no error.)
Q7 → relative = 0.5/50 + 0.2/20 = 0.01 + 0.01 = 0.02 = 2%. Z = 2.5, so ΔZ = 0.02 × 2.5 = 0.05 → **Z = 2.5 ± 0.05**.
Q8 → [s] = L. [ut] = LT⁻¹·T = L. [at²] = LT⁻²·T² = L. All terms L → dimensionally correct.
Q9/Q11 → One team sent thrust in pound-force·seconds (Imperial), the navigation team expected newton·seconds (SI). Same equation, two unit systems → model wrong by ~4.45× → craft entered the atmosphere too low and was lost (~$125M, 1999). Lessons: enforce SI-only pipelines, unit-tag every variable, automated unit-checking software, dimensional analysis as a sanity check, standardised interfaces between teams.
Q10 → V = s³. % error = 3 × (0.02/5.00) = 0.012 = **1.2%**. ΔV = 3s²Δs = 3×25×0.02 = **1.5 cm³**.
Contest → random error. 0.00000487 → 4.87×10⁻⁶ → **10⁻⁵** (4.87 ≥ √10≈3.16, round up). 564000000 → 5.64×10⁸ → **10⁹**.

## [HARDER] — go beyond your bank
[H1] A length is measured as (12.5 ± 0.1) cm and time as (2.00 ± 0.02) s. Speed = L/T. Find the speed and its max percentage error. (answer ≈ 6.25 m/s, 2%)
[H2] Explain why averaging readings reduces random error but NOT systematic error. (answer: random errors scatter both ways and cancel in the mean; systematic errors shift every reading the same way, so the mean keeps the bias.)
[H3] A student measures g = 9.81, 9.83, 9.79, 9.82, 9.80 m/s². True value 9.80. Comment on random vs systematic error present. (answer: scatter around the mean = small random error; the mean 9.81 vs true 9.80 = tiny systematic bias.)

---
---

# BLOCK 2 — VECTORS & CALCULUS TOOLS (L2)

## CONCEPT 2.1 — Scalar vs vector
- **Scalar**: magnitude only (mass, time, speed, energy).
- **Vector**: magnitude + direction (displacement, velocity, acceleration, force, momentum).
Represent a vector with an arrow, or in components **A = (Ax, Ay)**, magnitude |A| = √(Ax² + Ay²), direction θ = tan⁻¹(Ay/Ax).

## CONCEPT 2.2 — Vector addition
- **Triangle law**: place vectors head-to-tail; the resultant closes the triangle.
- **Parallelogram law**: place tail-to-tail, complete the parallelogram; the diagonal is the sum.
- Magnitude of A + B = √(A² + B² + 2AB cosθ) where θ is the angle between them.
- Adding components: (A+B)x = Ax + Bx, same for y. This is the method you will use for every problem.

## CONCEPT 2.3 — Multiplying a vector by a scalar
kA: magnitude scales by |k|. If k is **negative, the direction reverses**. (His MCQ: vector × negative scalar → direction is reversed.)

## CONCEPT 2.4 — Two products (his 2-mark comparison)
- **Dot product** A·B = AB cosθ. Result is a **scalar**. Perpendicular → cos90° = 0, so A·B = 0. Commutative (A·B = B·A).
- **Cross product** A×B = AB sinθ n̂. Result is a **vector**, perpendicular to both A and B, direction by the **right-hand rule**. Parallel → sin0° = 0, so A×B = 0. NOT commutative (A×B = −B×A).

## CONCEPT 2.5 — Unit vector and resolution
Unit vector Â = A/|A| (magnitude 1, keeps direction).
Any vector resolved: A = Ax î + Ay ĵ. To resolve a vector of magnitude A at angle θ to the x-axis: Ax = A cosθ, Ay = A sinθ.

## CONCEPT 2.6 — Differentiation (how fast a quantity changes)
The derivative gives the instantaneous rate of change. On a graph, it is the **slope of the tangent**.
- Power rule: d/dx (xⁿ) = n xⁿ⁻¹. Multiply by the power, then drop the power by 1. Constants die.
- d/dx (4x² − 3x + 7) = 8x − 3.
- In physics: position → velocity (v = dx/dt) → acceleration (a = dv/dt).

## CONCEPT 2.7 — Integration (the reverse — accumulating)
- Power rule: ∫ xⁿ dx = xⁿ⁺¹/(n+1) + C. Raise the power by 1, divide by the new power. Always add **+ C**.
- ∫ (3x² + 2x) dx = x³ + x² + C.
- On a graph, the integral is the **area under the curve**.
- In physics: acceleration → velocity (v = ∫ a dt) → position (x = ∫ v dt). The constants are fixed by the starting (initial) conditions.

## HIS QUESTIONS
[HIS Q18a] Find dy/dx of y = 4x² − 3x + 7.
[HIS Q18b] Integrate ∫ (3x² + 2x) dx.
[HIS CONTEST] What happens to a vector when multiplied by a negative scalar? (answer: magnitude scales, direction reverses)
[HIS CONTEST] According to the triangle law, vectors are arranged how? (answer: head-to-tail)
[HIS CONTEST] Dot product of two perpendicular vectors is? (answer: 0)
[HIS CONTEST] Which determines the direction of a cross product? (answer: the right-hand rule)
[HIS CONTEST] Differentiate dot product from cross product (at least two differences each).

## ANSWERS
Q18a → 8x − 3.
Q18b → x³ + x² + C.
Q17 → Dot: scalar result, A·B = AB cosθ, commutative, zero when perpendicular. Cross: vector result, A×B = AB sinθ n̂, right-hand rule direction, anti-commutative, zero when parallel.

## [HARDER]
[H4] If A = 3î + 4ĵ and B = 2î − ĵ, find A·B and |A×B|. (answer: A·B = 6 − 4 = 2; |A×B| = |3(−1) − 4(2)| = 11)
[H5] d/dx of y = 5x³ − 2x + 1, then integrate your answer back. (answer: 15x² − 2; back = 5x³ − 2x + C)
[H6] A vector has magnitude 10 at 30° to the x-axis. Resolve it. (answer: 8.66î + 5ĵ)

---
---

# BLOCK 3 — KINEMATICS (L3–L4)

## CONCEPT 3.1 — The basic quantities
- **Distance** = path length travelled (scalar). **Displacement** = change in position (vector, straight line from start to finish).
- **Speed** = distance/time (scalar). **Velocity** = displacement/time (vector).
- **Acceleration** = rate of change of velocity (vector). **Jerk** = rate of change of acceleration. (His MCQ trap: "rate of change of velocity" = acceleration, NOT jerk.)

## CONCEPT 3.2 — The three equations of motion (constant acceleration)
Only valid when a is constant:
1. v = u + at            (no distance involved)
2. v² = u² + 2as         (no time involved)
3. s = ut + ½at²         (no final velocity involved)
where u = initial velocity, v = final, a = acceleration, t = time, s = displacement.
Pick by what is MISSING from the question.

## CONCEPT 3.3 — Graphs (the ladder)
- Position–time graph: **slope = velocity**.
- Velocity–time graph: **slope = acceleration**, **area = displacement**.
- Straight rising line = constant velocity. Curved steepening line = increasing velocity.

## CONCEPT 3.4 — Relative motion
v(A/B) = v_A − v_B (velocity of A relative to B). Pick a positive direction and write it down; then signs take care of themselves.
- River crossing: time to cross = width / boat-speed-perpendicular; drift = stream-speed × time.
- Rain and umbrella: the umbrella tilts at tanθ = v_rain / v_man.

## CONCEPT 3.5 — Projectile motion
Split the launch velocity into components, then treat the two directions separately (horizontal = constant velocity, vertical = constant acceleration −g).
- u_x = u cosθ, u_y = u sinθ
- Time of flight T = 2u_y/g
- Max height H = u_y²/(2g)
- Range R = u² sin2θ / g. Range is maximum at **44–45°**; complementary angles (θ and 90−θ) give the same range.
- At any time: v_x = u_x (constant), v_y = u_y − gt.

## HIS QUESTIONS
[HIS Q4] Two cars on the same road: A at 20 m/s, B at 12 m/s, same direction. Velocity of A relative to B? If opposite directions?
[HIS Q19] Two position-time graphs — one a straight rising line, one curving upward. State how average and instantaneous velocity change in each.
[HIS Q20] A body starts from rest with a = 2 m/s². What is its velocity after 5 s?
[HIS Q24] A ball is kicked at 25 m/s, 37° to the horizontal. Find (1) horizontal and vertical components (2) time to return to the ground (3) max height. (sin37 = 0.6, cos37 = 0.8)
[HIS Q25] A drone's position is x(t) = 3t² + 4t + 2 and y(t) = 2t³ − 3t² + 5t. Find velocity components and speed at t = 2 s; acceleration components and magnitude at t = 2 s; direction of motion.
[HIS CONTEST] In projectile motion the vertical acceleration is? (answer: −g)

## ANSWERS
Q4 → Same direction: 20 − 12 = **8 m/s**. Opposite: 20 − (−12) = **32 m/s**.
Q19 → Straight line: velocity constant, average = instantaneous, both unchanging. Curving upward: velocity increases with time; instantaneous velocity (tangent slope) grows; average over an interval is less than the instantaneous at the end.
Q20 → v = u + at = 0 + 2×5 = **10 m/s**.
Q24 → u_x = 25×0.8 = **20 m/s**, u_y = 25×0.6 = **15 m/s**. T = 2×15/g. With g=10 → **3.0 s** (with g=9.8 → 3.06 s). H = 15²/(2×10) = **11.25 m** (with g=9.8 → 11.5 m).
Q25 → v_x = 6t+4 → **16**, v_y = 6t²−6t+5 → **17** at t=2. Speed = √(16²+17²) = **√545 ≈ 23.3 m/s**. a_x = 6, a_y = 12t−6 → **18**. |a| = √(6²+18²) = **√360 ≈ 19.0 m/s²**. Direction θ = tan⁻¹(17/16) ≈ **46.7°** from +x.

## [HARDER]
[H7] A ball is thrown horizontally at 15 m/s from a 45 m high cliff. Where does it land? (answer: t = √(2×45/10) = 3 s; range = 15×3 = 45 m)
[H8] A car goes 0→20 m/s in 5 s, then holds 20 m/s for 5 more. Using the velocity–time graph, find displacement, average velocity, average acceleration in the first 5 s. (answer: 100 m, 10 m/s, 4 m/s² — area under the graph)
[H9] A boat points straight across a 200 m river at 4 m/s while the current flows at 3 m/s. Crossing time and downstream drift. (answer: 50 s, 150 m)

---
---

# BLOCK 4 — FORCES, NLM & FRICTION (L5–L6)

## CONCEPT 4.1 — What a force is
A push or pull from one object on another. Types you will meet: weight (mg, down), normal force (N, perpendicular to the surface), tension (T, along a string), friction (f, opposes slipping), applied force, spring force.

## CONCEPT 4.2 — Newton's three laws
1. **First law (inertia):** an object stays at rest or moves with constant velocity unless a net external force acts. This defines an **inertial frame**.
2. **Second law:** F_net = ma (net force = mass × acceleration). This is the workhorse.
3. **Third law:** every action has an equal and opposite reaction (the two forces act on DIFFERENT objects, so they never cancel in one free-body diagram).

## CONCEPT 4.3 — Frames of reference and pseudo forces
- **Inertial frame:** not accelerating; Newton's laws hold directly.
- **Non-inertial (accelerating) frame:** to make the laws appear to hold, you must add a **pseudo force** = −(acceleration of the frame) × mass, opposite to the frame's acceleration. (Example: in an accelerating car you feel thrown backward — that "force" is the pseudo force.)

## CONCEPT 4.4 — Free body diagrams (FBD) — his constant companion
Draw ONE object. On it, draw every force acting ON that object as an arrow:
- Box on a floor: N up, mg down, applied force, friction opposite to motion.
- Box on an incline: split mg into mg sinθ (down the slope) and mg cosθ (into the slope). N = mg cosθ. Friction acts up the slope if it is sliding down.
Always draw the FBD before writing any equation. He draws them in his notes and rewards them.

## CONCEPT 4.5 — Friction
- **Static friction** f_s: opposes the tendency to move. Self-adjusting — it equals the applied force up to a maximum f_s,max = μ_s N. The object moves only when the applied force exceeds f_s,max.
- **Kinetic friction** f_k = μ_k N: constant, acts once sliding. Usually μ_k < μ_s.
- On an incline: the block slides if the down-slope component beats max static friction. Quick test: **slides if tanθ > μ_s**.
- Pulling UP at an angle reduces the normal force (N = mg − F sinθ). Pushing DOWN at an angle increases it (N = mg + F sinθ).

## CONCEPT 4.6 — Whole-system method (for pulleys)
If two masses are tied by a light inextensible string over a frictionless pulley, they share one acceleration a.
a = (driving force − resisting force) / total mass.
Then find the tension from ONE of the bodies alone.

## HIS QUESTIONS
[HIS F1] 5 kg, μ_s = 0.40. What is the maximum force you can apply without moving it?
[HIS F2] 10 kg pulled by 35 N, μ_k = 0.20. Find N, friction, net force, acceleration.
[HIS F3] 6 kg, μ_s = 0.50, μ_k = 0.30, applied force 20 N. Does it move? What is the actual friction?
[HIS F4] 8 kg, μ_s = 0.40, μ_k = 0.25, force slowly increased from 0. At what force does it start moving? Just after moving, what is friction and acceleration?
[HIS F5] 5 kg, F = 40 N applied at 30° above the horizontal, μ_k = 0.20. Find acceleration.
[HIS F6] 10 kg, F = 50 N applied at 30° below the horizontal (a push), μ_k = 0.25. Find acceleration.
[HIS F7] 10 kg on a 30° incline, μ_k = 0.20, sliding down. Find acceleration.
[HIS F8] 5 kg on a 37° incline, μ_s = 0.50. Does it stay or slide? (g = 10)
[HIS F9] 4 kg on a 30° incline, F = 30 N applied up the slope, μ_k = 0.20. Find acceleration.
[HIS F10] 6 kg pulled up a 30° incline by a 50 N rope, μ_k = 0.15. Find acceleration.
[HIS F11] 5 kg on a rough table (μ_k = 0.20) tied to a hanging 3 kg over a frictionless pulley. Find acceleration and tension.

## ANSWERS (g = 9.8 unless stated)
F1 → f_s,max = 0.40 × 5 × 9.8 = **19.6 N**.
F2 → N = 98 N, f_k = 19.6 N, net = 15.4 N, a = **1.54 m/s²**.
F3 → f_s,max = 29.4 N > 20 N, so it does NOT move. Actual friction = **20 N** (self-adjusting, matches the applied force).
F4 → Starts at 0.40×8×9.8 = **31.36 N**. Just after: f_k = 0.25×8×9.8 = **19.6 N**, a = (31.36 − 19.6)/8 = **1.47 m/s²**.
F5 → F_x = 34.64 N, F_y = 20 N, N = 49 − 20 = 29 N, f_k = 5.8 N, a = (34.64 − 5.8)/5 = **5.77 m/s²**. (Pulling up reduces N, so a is larger.)
F6 → N = 98 + 25 = 123 N, f_k = 30.75 N, a = (43.30 − 30.75)/10 = **1.26 m/s²**. (Pushing down increases N, so a is smaller.)
F7 → a = g(sin30 − μ_k cos30) = 9.8(0.5 − 0.20×0.866) = **3.20 m/s²** down the slope.
F8 → tan37 = 0.75 > μ_s = 0.50 → **it slides**.
F9 → N = 4×9.8×cos30 = 33.95 N, f_k = 6.79 N, down-slope weight = 19.6 N. Net up = 30 − 19.6 − 6.79 = 3.61 N → a = **0.90 m/s² up the slope**.
F10 → N = 50.92 N, f_k = 7.64 N, down-slope weight = 29.4 N, a = (50 − 29.4 − 7.64)/6 = **2.16 m/s² up**.
F11 → a = (3×9.8 − 0.20×5×9.8)/(5+3) = (29.4 − 9.8)/8 = **2.45 m/s²**. T = 3(9.8 − 2.45) = **22.05 N**.

## [HARDER]
[H10] A 15° incline, μ_k = 0.10, 20 kg block. Does it slide? If yes, find a. (answer: tan15 = 0.27 > 0.10 → slides; a = 9.8(sin15 − 0.10 cos15) = 9.8(0.259 − 0.097) = 1.59 m/s²)
[H11] Three blocks (2 kg, 3 kg, 4 kg) tied on a frictionless table, pulled by 18 N. Find a and each tension. (answer: a = 2 m/s²; T between 4 and 3 = 4×2 = 8 N; T between 3 and 2 = 2×2 = 4 N)
[H12] A 10 kg block on a rough horizontal table (μ_k = 0.30) is pulled by a rope at 20° above horizontal with 50 N. Find a. (answer: N = 98 − 50 sin20 = 98 − 17.1 = 80.9 N; f_k = 24.27 N; a = (50 cos20 − 24.27)/10 = (46.98 − 24.27)/10 = 2.27 m/s²)

---
---

# BLOCK 5 — CIRCULAR MOTION (L7)

## CONCEPT 5.1 — Angular description
An angle in **radians**: θ (radians) = arc length / radius = s/r. Full circle = 2π rad.
- **Angular velocity** ω = θ/t = v/r = 2πf = 2π/T_period.
- **Angular acceleration** α = ω/t (the angular version of a).
Rotational kinematics mirror the linear ones: θ ↔ x, ω ↔ v, α ↔ a.

## CONCEPT 5.2 — Radial and tangential directions
At any point on a circle:
- **Tangential** direction: along the tangent, where the linear speed lives. Tangential acceleration a_t = rα (changes the SPEED).
- **Radial (centripetal) direction**: toward the centre. Centripetal acceleration a_c = v²/r = rω² (changes the DIRECTION, not the speed).
- Total acceleration a = √(a_t² + a_c²).

## CONCEPT 5.3 — Centripetal vs centrifugal (his favourite explanation)
- **Centripetal** = the REAL inward net force (tension, friction, gravity) that constantly redirects the velocity so the circular path continues. Acts ON the body, in an inertial frame. Agent: a string, friction, gravity.
- **Centrifugal** = a **pseudo (fictitious) force** that appears only in the rotating (non-inertial) frame, directed radially OUTWARD. No physical agent — it represents the body's inertia resisting the inward turn. Example: the outward push you feel on a merry-go-round; clothes flung outward in a spinning dryer.
- Key point: centripetal does NO work, because it is always perpendicular to the motion (W = Fd cos90° = 0).

## CONCEPT 5.4 — Torque
τ = rF sinθ, where θ is the angle between the radius vector and the force. It is zero when the force points along the radius (sin0° = 0) — the same reason centripetal force does no work.

## HIS QUESTIONS
[HIS C1] A car moves in a circle of radius 50 m at 10 m/s. Find ω and a_c.
[HIS C2] A wheel of radius 0.5 m spins at 120 rpm. Find ω and the linear speed v.
[HIS C3] Torque from a 100 N force at radius 0.5 m when the force is at 90°, 60°, 0° to the radius.
[HIS C4] 2 kg, r = 4 m, v = 8 m/s. Find centripetal acceleration and the centripetal force.
[HIS C5] A 1200 kg car goes around a bend of radius 40 m at 12 m/s. Find the required centripetal force.
[HIS C6] A 5 kg mass spins on a string of length 2 m at 6 m/s. What is the tension?
[HIS C7] Explain the difference between centripetal and centrifugal force, with an example of each.
[HIS C8] A 5 kg block on a rough turntable (radius 2 m, μ = 0.4). What is the maximum speed it can have without slipping?
[HIS C9] A car travels at 20 m/s around a bend of radius 100 m. Find a_c. What happens to a_c if the speed doubles?

## ANSWERS
C1 → ω = 10/50 = **0.2 rad/s**; a_c = 10²/50 = **2 m/s²**.
C2 → ω = 120 × 2π/60 = **4π ≈ 12.57 rad/s**; v = 0.5 × 4π = **2π ≈ 6.28 m/s**.
C3 → 90°: **50 N·m**. 60°: **43.3 N·m**. 0°: **0**.
C4 → a_c = 8²/4 = **16 m/s²**; F = 2 × 16 = **32 N**.
C5 → F = 1200 × 144/40 = **4320 N**.
C6 → T = mv²/r = 5×36/2 = **90 N**.
C7 → See CONCEPT 5.3. Centripetal = real inward force (string tension, friction, gravity) in an inertial frame. Centrifugal = pseudo outward force felt in the rotating frame, no physical agent.
C8 → μmg = mv²/r → v = √(μgr) = √(0.4×9.8×2) = **2.8 m/s**.
C9 → a_c = 400/100 = **4 m/s²**. If v doubles, a_c quadruples (**16 m/s²**) because a_c depends on v².

## [HARDER]
[H13] A satellite orbits at radius r with speed v. Derive the orbital speed if gravity provides the centripetal force. (answer: mv²/r = GMm/r² → v = √(GM/r))
[H14] A wheel accelerates from ω = 2 to 8 rad/s in 4 s at radius 0.3 m. Find a_t, a_c at the end, and total a. (answer: α = 1.5; a_t = 0.45; a_c = 0.3×64 = 19.2; a ≈ 19.2 m/s² — dominated by the radial part)
[H15] Why does a car need a larger banking angle for a higher speed on the same curve? (answer: the horizontal component of the normal force must supply mv²/r, which grows with v², so a larger angle is needed for the same radius.)

---
---

# BLOCK 6 — WORK & ENERGY (L8)

## CONCEPT 6.1 — Work
Work done by a constant force: **W = F d cosθ**, where θ is the angle between the force and the displacement.
- Positive work if the force has a component along the motion; negative if opposite (friction).
- **Zero work** when the force is perpendicular to the motion (cos90° = 0). Example: centripetal force on a circular path, normal force on a flat road, gravity at constant height.

## CONCEPT 6.2 — Energy
- **Kinetic energy** KE = ½mv² (energy of motion).
- **Gravitational potential energy** PE = mgh (energy of position).
- **Spring potential energy** = ½kx².
- **Power** = work/time = Fv.

## CONCEPT 6.3 — Work–energy theorem
**W_net = ΔKE** — the net work done on an object equals its change in kinetic energy. This often replaces the equations of motion when forces vary or when you only care about speeds.

## CONCEPT 6.4 — Conservative vs non-conservative forces
- **Conservative** (gravity, spring force): the work done depends ONLY on the start and end points, not on the path taken. Over any closed loop the work is zero. Hence KE + PE = constant (mechanical energy conserved).
- **Non-conservative** (friction, air resistance): the work depends on the path — a longer path means more energy removed. Mechanical energy is NOT conserved; it turns into heat. W_friction = −f_k × d.

## HIS QUESTIONS
[HIS E1] 5 kg moving at 4 m/s. What is its kinetic energy?
[HIS E2] An object has momentum 10 kg·m/s and mass 2 kg. Find its kinetic energy.
[HIS E3] 5 kg at a height of 10 m. What is its gravitational potential energy?
[HIS E4] An 80 N force acts over 8 m in the direction of the force. Find the work done.
[HIS E5] A 100 N force acts over 5 m at 60° to the displacement. Find the work done.
[HIS E6] A spring of spring constant 200 N/m is stretched from 0.1 m to 0.3 m. Find the work done by the spring.
[HIS E7] The same amount of work is done moving an object along two different paths between the same two points. What does this tell you about the force?
[HIS E8] A 4 kg object at rest has 200 J of net work done on it. Find its final speed.
[HIS E9] A 5 kg object moving at 4 m/s has 90 J of work done on it. Find its final speed.
[HIS E10] A 2 kg object falls freely from rest off a height of 20 m. Find its speed just before hitting the ground.
[HIS E11] A 5 kg object falls 8 m and loses 50 J to friction. Find its speed at the bottom.
[HIS E12] A 10 kg object falls 5 m and loses 100 J to friction. Find its speed at the bottom.
[HIS E13] A 4 kg block is pushed by 30 N through 10 m against 5 N of friction, from rest. Find: work by the push, work by friction, net work, final KE, final speed.
[HIS E14] KE = ½mv² is kept constant while the mass becomes 4m. What happens to the speed?
[HIS E15] A particle falls under gravity with friction present. Is total mechanical energy conserved between start and finish? Explain.

## ANSWERS
E1 → ½×5×16 = **40 J**.
E2 → K = p²/2m = 100/4 = **25 J**.
E3 → 5×9.8×10 = **490 J**.
E4 → **640 J**.
E5 → 100×5×cos60 = **250 J**.
E6 → −½k(x₂² − x₁²) = −100(0.09 − 0.01) = **−8 J** (the spring does negative work when stretched further; the external agent does +8 J).
E7 → The force is **conservative** — work is path-independent, so over a closed loop it is zero.
E8 → 200 = ½×4×v² → v = **10 m/s**.
E9 → 90 = ½×5(v² − 16) → v = **7.21 m/s**.
E10 → v = √(2gh) = √(2×9.8×20) = **19.8 m/s**.
E11 → mgh − 50 = ½mv² → 392 − 50 = 2.5v² → v = **11.7 m/s**.
E12 → 490 − 100 = 5v² → v = **8.83 m/s**.
E13 → W_push = 300 J; W_friction = −50 J; W_net = 250 J; KE_final = 250 J; v = √(2×250/4) = **11.2 m/s**.
E14 → ½mv² = ½(4m)v'² → v' = **v/2** (speed halves).
E15 → **No.** Gravity is conservative (work depends only on the height difference), but friction is non-conservative and always does negative work −f_k·d proportional to path length, converting mechanical energy into heat. So KE + PE is not conserved (total energy including heat still is).

## [HARDER]
[H16] A 3 kg block slides down a 30° incline of length 5 m with μ_k = 0.15. Find its speed at the bottom using energy. (answer: work by gravity = mg sinθ × d = 3×9.8×0.5×5 = 73.5 J; N = mg cosθ = 25.46 N; f_k = 3.82 N; work by friction = −3.82×5 = −19.1 J; net = 54.4 J = ½×3×v² → v = 6.03 m/s)
[H17] A spring (k = 500 N/m) is compressed 0.2 m and launches a 0.5 kg block on a frictionless surface. Find the launch speed. (answer: ½kx² = ½mv² → 500×0.04 = 0.5v² → v = √40 = 6.32 m/s)
[H18] Derive why the centripetal force does no work, and connect it to why circular motion at constant speed keeps KE constant. (answer: force ⊥ displacement at every instant, so W = ∫F·ds = 0; by the work–energy theorem ΔKE = 0, so speed stays the same.)

---
---

# BLOCK 7 — CENTRE OF MASS (L9)

## CONCEPT 7.1 — What it is
The **centre of mass (CoM)** is the average position of the mass in a system — the single point that moves as if all the mass were concentrated there and all external forces acted there.

## CONCEPT 7.2 — The formula
For particles on a line: **x_cm = (m₁x₁ + m₂x₂ + …) / (m₁ + m₂ + …)**.
In 2D, do each axis separately: x_cm = Σmᵢxᵢ/M and y_cm = Σmᵢyᵢ/M, then write the point (x_cm, y_cm).
Vector form: **R_cm = Σmᵢrᵢ / M**.

## CONCEPT 7.3 — Symmetry shortcut
For a uniform symmetric body the CoM is at the geometric centre:
- Uniform rod → midpoint.
- Uniform disc, cube, sphere → geometric centre.
- L-shaped object → split into rectangles, treat each piece's CoM as a point mass.

## CONCEPT 7.4 — How the CoM moves
The CoM of an isolated system (no net external force) moves with **constant velocity** — internal forces cannot change it. When mass is redistributed (e.g. ice melting, a person walking on a boat) the CoM of the whole system shifts to keep this true.

## HIS QUESTIONS
[HIS M1] Two particles: 2 kg at x = 0 and 8 kg at x = 5. Find the CoM.
[HIS M2] Three particles: 2 kg at (0,0), 3 kg at (4,0), 5 kg at (10,0). Find the CoM.
[HIS M3] A 2 kg and an 8 kg mass are 10 m apart. Where is the CoM measured from the 2 kg mass?
[HIS M4] 2 kg at (0,0), 3 kg at (6,0), 5 kg at (0,4). Find the CoM.
[HIS CONTEST-2 — the one he set and nobody solved] An ice cube of mass m and side L melts in a tray of mass M. The water spreads out thin on the tray base. Does the centre of mass move? If so, in which direction, and what determines the size of the change? Explain WITHOUT numerical calculation.

## ANSWERS
M1 → x_cm = (2×0 + 8×5)/10 = **4 m**.
M2 → x_cm = (0 + 12 + 50)/10 = **6.2 m**.
M3 → x_cm = (8×10)/10 = **8 m** from the 2 kg mass (closer to the heavier mass — the CoM always sits nearer the larger mass).
M4 → x_cm = (0 + 18 + 0)/10 = **1.8**; y_cm = (0 + 0 + 20)/10 = **2.0** → **(1.8, 2.0)**.
CONTEST-2 → Yes, it moves. While solid, the ice's mass sits at height L/2, so the combined CoM is slightly above the base, about (mL/2)/(M+m). After melting, the water is a thin layer at the base, so its mass is at base level. The mass has been redistributed downward, so the combined CoM **drops toward the base**. The size of the drop is roughly (mL/2)/(M+m): larger when the ice is heavy compared to the tray (m ≫ M) and smaller when the tray is heavy (M ≫ m). Direction is always downward.

**Template for any variant of this question:** (i) does the CoM move? yes/no (ii) which direction (iii) what sets the magnitude (the mass ratio and the height change).

## [HARDER]
[H19] A rod of mass 2 kg and length 4 m has a 1 kg mass attached to one end. Where is the CoM measured from that end? (answer: treat the rod's mass at its own centre, 2 m from the end: x_cm = (1×0 + 2×2)/3 = **1.33 m**)
[H20] An L-shape is made of two uniform rods: one 3 kg × 4 m horizontal, one 4 kg × 3 m vertical joined at one end. Find the CoM. (answer: horizontal piece CoM at (2, 0); vertical piece CoM at (0, 1.5); x_cm = (3×2 + 4×0)/7 = 0.86 m; y_cm = (3×0 + 4×1.5)/7 = 0.86 m → (0.86, 0.86))
[H21] A man of 60 kg walks from one end of a 120 kg boat (length 4 m) to the other. If the boat is free to slide on water, how far does the boat move? (answer: the CoM of the man+boat system does not move, so the boat slides 60/(60+120) × 4 = **1.33 m** opposite to his walk.)

---
---

# BLOCK 8 — MOMENTUM & COLLISIONS (L10)

## CONCEPT 8.1 — Momentum
**p = mv** (mass × velocity). It is a vector, so it has direction. Units kg·m/s (= N·s).

## CONCEPT 8.2 — Impulse
Impulse = force × time = change in momentum: **J = FΔt = Δp = m(v − u)**. This is why a longer collision time (airbag, padding) reduces the peak force for the same change in momentum.

## CONCEPT 8.3 — Conservation of linear momentum
If the **net external force on a system is zero**, the total momentum is conserved: **p_before = p_after**.
Internal forces (the collision forces between the two bodies) cancel in pairs (Newton's third law), so they cannot change the total.
This is the single most important equation in this block.

## CONCEPT 8.4 — Types of collision
- **Perfectly inelastic (e = 0):** the bodies stick and move with one common velocity v = (m₁u₁ + m₂u₂)/(m₁+m₂). Maximum possible loss of kinetic energy.
- **Elastic (e = 1):** both momentum AND kinetic energy are conserved.
- **Inelastic (0 < e < 1):** momentum conserved, kinetic energy partly lost.
Special theorem: for two EQUAL masses in an elastic collision with the second at rest, they **exchange velocities** (the first stops, the second takes all the speed).

## CONCEPT 8.5 — Coefficient of restitution
**e = separation speed / approach speed** = (v₂ − v₁)/(u₁ − u₂). It measures how "bouncy" a collision is. e = 1 elastic, e = 0 perfectly inelastic.

## CONCEPT 8.6 — The two-equation machine (solve every general collision with this)
1. Momentum: m₁u₁ + m₂u₂ = m₁v₁ + m₂v₂
2. Restitution: v₂ − v₁ = e(u₁ − u₂)
Two equations, two unknowns (v₁, v₂). Solve them simultaneously.

## CONCEPT 8.7 — Multi-dimensional collisions
Resolve everything into x and y components. Conserve momentum separately on each axis, then combine: |p| = √(px² + py²), direction θ = tan⁻¹(py/px).

## CONCEPT 8.8 — Centre of mass link
If F_net = 0: total momentum constant, CoM velocity constant, CoM acceleration = 0. And a_cm = F_net/M (works even when F_net ≠ 0).

## HIS QUESTIONS
[HIS P1] 2 kg at 6 m/s hits a stationary 4 kg. What is the total momentum before the collision?
[HIS P2] 5 kg at 4 m/s hits a stationary 3 kg and they stick. Find the common velocity.
[HIS P3] 2 kg at 8 m/s hits a stationary 6 kg perfectly inelastically. Find initial momentum, common velocity, initial KE, final KE, and energy lost.
[HIS P4] 2 kg at 10 m/s elastically hits a stationary 3 kg. Find both final velocities.
[HIS P5] 4 kg at 6 m/s collides head-on with 2 kg at 3 m/s in the opposite direction. Find both final velocities (elastic).
[HIS P6] 5 kg at 8 m/s hits a stationary 3 kg and they stick. Find the common velocity, initial KE, final KE, and energy lost.
[HIS P7] 2 kg at 10 m/s hits a stationary 3 kg with e = 0.6. Find both final velocities.
[HIS P8] 4 kg at 8 m/s hits a stationary 6 kg with e = 0.5. Find both final velocities.
[HIS P9] 3 kg at 6 m/s hits a stationary 2 kg with e = 0.4. Find the approach speed, separation speed, and both final velocities.
[HIS P10] 2 kg at 12 m/s hits a stationary 4 kg with e = 0.5. Find both final velocities.
[HIS P11] 4 kg moving east at 5 m/s sticks to 6 kg moving north at 3 m/s. Find the final speed and direction.
[HIS P12] 5 kg moving along +x at 8 m/s sticks to 3 kg moving along +y at 6 m/s. Find the final speed and direction.
[HIS P13] A 0.5 kg ball moving at 10 m/s hits a wall and rebounds at 6 m/s in the opposite direction. Find initial momentum, final momentum, change in momentum, and the impulse on the ball.
[HIS P14] A 10 kg body at rest explodes into two pieces, 4 kg at 12 m/s and a 6 kg piece. Find the velocity of the second piece.
[HIS P15] 2 kg east at 6 m/s and 3 kg north at 4 m/s collide. Find the components, magnitude, and direction of the total momentum.
[HIS P16] 2 kg east at 5 m/s and 1 kg north at 4 m/s stick together. Find the final speed and direction.
[HIS P17] If the net external force on a system is zero, what can you say about (a) the total momentum (b) the velocity of the CoM (c) the acceleration of the CoM?

## ANSWERS
P1 → 2×6 = **12 kg·m/s**.
P2 → v = (5×4)/8 = **2.5 m/s**.
P3 → p_i = 16; v = 16/8 = **2 m/s**; KE_i = 64 J; KE_f = 16 J; lost = **48 J**.
P4 → v₁ = (m₁−m₂)u/(m₁+m₂) = (2−3)×10/5 = **−2 m/s** (rebounds back); v₂ = 2m₁u/(m₁+m₂) = **8 m/s**.
P5 → Take u₁ = 6, u₂ = −3. v₁ = [(4−2)×6 + 2×2×(−3)]/6 = **0**; v₂ = [(2−4)(−3) + 2×4×6]/6 = **9 m/s**.
P6 → v = 40/8 = **5 m/s**; KE_i = 160 J; KE_f = 100 J; lost = **60 J**.
P7 → v₂ − v₁ = 6; 2v₁ + 3v₂ = 20 → v₁ = **0.4**, v₂ = **6.4 m/s**.
P8 → v₂ − v₁ = 4; 4v₁ + 6v₂ = 32 → v₁ = **0.8**, v₂ = **4.8 m/s**.
P9 → approach = 6, separation = e×6 = **2.4 m/s**; 3v₁ + 2v₂ = 18 and v₂ − v₁ = 2.4 → v₁ = **2.64**, v₂ = **5.04 m/s**.
P10 → v₂ − v₁ = 6; 2v₁ + 4v₂ = 24 → v₁ = **0**, v₂ = **6 m/s** (the lighter body stops dead).
P11 → p_x = 20, p_y = 18, total mass 10 → v = √(400+324)/10 = √724/10 ≈ **2.69 m/s**; θ = tan⁻¹(18/20) ≈ **42° north of east**.
P12 → p_x = 40, p_y = 18, mass 8 → v ≈ **5.48 m/s**; θ = tan⁻¹(18/40) ≈ **24° from the x-axis**.
P13 → p_i = 5; p_f = −3; Δp = **−8 kg·m/s**; impulse = **−8 N·s** (opposite to the original direction).
P14 → 0 = 4×12 + 6v → v = **−8 m/s** (8 m/s in the opposite direction).
P15 → p_x = 12, p_y = 12; |p| = **17.0 kg·m/s**; θ = **45° north of east**.
P16 → p_x = 10, p_y = 4, mass 3 → v = √(100+16)/3 ≈ **3.57 m/s**; θ = tan⁻¹(4/10) ≈ **21.8° north of east**.
P17 → (a) total momentum is constant/conserved (b) the CoM velocity is constant (c) the CoM acceleration is **zero**.

## [HARDER]
[H23] A 3 kg ball at 5 m/s collides elastically with a 1 kg ball at rest. Find both final velocities using the two-equation machine with e = 1. (answer: v₁ = [(3−1)×5]/4 = 2.5 m/s; v₂ = [2×3×5]/4 = 7.5 m/s)
[H24] In a collision, the initial kinetic energy is 200 J and e = 0.8. What is the maximum possible fraction of KE that can be lost? Use ΔKE = ½m₁m₂(u₁−u₂)²(1−e²)/(m₁+m₂). (answer: fraction lost = (1−e²) = 0.36, so up to 36% — 72 J)
[H25] A 60 kg person jumps off a 120 kg boat at 3 m/s relative to the boat. How fast does the boat move? (answer: by conservation of momentum 0 = 60×3 + 120×v → v = **1.5 m/s** opposite to the jump)

---
---

# THE 9 EXAM-DAY TEMPLATES (his favourite shapes)

1. **Error propagation** → value, then Δ by adding relatives, then relative, then %.
2. **a(t) → v(t) → x(t)** → integrate twice, pin the constants from the initial conditions, then evaluate.
3. **Velocity–time graph story** → draw the ramp/flat, displacement = area, average velocity = displacement/time, average acceleration = Δv/Δt.
4. **Projectile (a)(b)(c)** → components, then time of flight, then max height (add range if asked).
5. **Collision with e** → momentum equation + restitution equation → solve the system.
6. **2-Dimensional stick** → conserve p_x and p_y separately → v = √(vx² + vy²), θ = tan⁻¹(py/px).
7. **Incline + pulley with friction** → whole-system a = (driving − resisting)/total mass → tension from one body.
8. **CoM in 2D** → weighted means per axis.
9. **Ice-tray style explanation** → claim → redistribution → direction → mass-ratio controls the magnitude.

---

# FORMULA CARD (copy this onto one page)

- v = u + at; v² = u² + 2as; s = ut + ½at²
- Projectile: T = 2u_y/g, H = u_y²/2g, R = u²sin2θ/g
- Relative velocity: v(A/B) = v_A − v_B
- Errors: multiply/divide → add relatives; power n → ×n; add/subtract → add absolutes
- Circular: ω = v/r, a_c = v²/r = rω², a_t = rα, τ = rF sinθ
- Friction: f_k = μ_k N, f_s ≤ μ_s N, incline slides iff tanθ > μ_s
- Work/Energy: W = Fd cosθ, KE = ½mv², PE = mgh, W_net = ΔKE
- Momentum: p = mv, J = FΔt = Δp, p_before = p_after
- CoM: x_cm = Σmx/Σm, v_cm = Σmv/Σm, a_cm = F_net/M
- Restitution: e = (v₂ − v₁)/(u₁ − u₂)

---

# EXAM-DAY PROTOCOL (calibrated to how his papers actually mark)

1. **First pass (35 min):** all five 3-mark questions. These are definitions and one-step calculations from the flash cards and CONCEPT boxes. Never leave one blank — write the formula and one sentence. Partial marks exist.
2. **Second pass (60 min):** the three 5-mark questions. Use the (A)/(B) choice to pick the pair whose technique you can write from memory. Label the sub-parts (a)(b)(c). Show numbers and units on every line.
3. **Last 15 min:** the 10-mark story question. Use the four-verb structure: (a) evaluate the claim (b) support with calculation (c) design/decide (d) assess the limitation. Four labelled paragraphs beat one long one.
4. **If a question looks new:** it is one of his worksheets with different numbers. Identify the block, pull the matching template, re-run the numbers.
5. **g:** read it from the paper. Worksheets use 9.8, one contest used 10. sin37 = 0.6, cos37 = 0.8 when needed.
6. **Three-minute rule:** stuck more than 3 min? Write the formula and what you know, move on, return at the end.
7. **Marks live in the method.** Show every step, add units, and use words like "because", "therefore", "since the net force is zero". His papers reward written justification over bare numbers.

All the best tomorrow.
