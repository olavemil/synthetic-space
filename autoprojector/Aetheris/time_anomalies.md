/news/notes_anomalies_subclass.md
## Anomaly Sub‑Classification (v1.3)

### 1. Fracture‑Induced Echo Types
| Code | Designation | Trigger Condition | Observable Manifestation | Temporal Scale (Δt) |
|------|-------------|-------------------|--------------------------|----------------------|
| E‑01 | **Spectral Echo** | ∇S ≈ 0 within 0.5 R☉ of a supernova remnant | Re‑appearance of pre‑explosion spectral lines (e.g., Ni‑56 679 nm) | 10⁻³ – 10² s |
| E‑02 | **Chrono‑Pulse** | Dark‑energy pressure spikes > 10⁻¹⁴ Pa in a pulsar wind nebula | Short‑duration radio burst preceding the primary flare | 10⁻⁶ – 10⁻¹ s |
| E‑03 | **Geological Re‑Sync** | Tidal resonance frequency matching planetary eigenmode (f = 0.73 mHz) | Sudden atmospheric composition shift (CH₄ ↑ 12 %) mimicking past epoch | 10² – 10⁴ s |

### 2. Trigger Matrix
| Trigger | Required Parameter | Minimum Value | Example Event |
|---------|-------------------|---------------|----------------|
| Gravitational Spike | Ricci curvature R₍μν₎ > 10⁴⁶ m⁻² | 1.2 × 10⁴⁶ m⁻² | LIGO‑2038 black‑hole merger precursor |
| Quantum Collapse | Superposition collapse probability P > 0.87 | 0.87 | Veyra Incident 2083 |
| Thermodynamic Suspension | Entropy gradient | |∇S| < 10⁻³⁰ J K⁻¹ m⁻³ | Tambora‑type eruption 1815 (Event 7) |

### 3. Echo Propagation Rules
1. **Conservation of Causal Phase** – The phase φ of an echo satisfies φ = φ₀ + ∮ A·dx, where A is the electromagnetic vector potential encoded in the local metric.
2. **Entropy Borrowing Limit** – Borrowed entropy ΔS_b must satisfy ΔS_b ≤ S_local/3 to avoid global violation of the Second Law (see /physics.md §3.2).
3. **Fracture Closure Condition** – A fracture closes when the integral of the entropy gradient over the closure interval equals zero: ∫₀^{Δt} ∇S(t) dt = 0.

---

/notes_physics_defs.md
## Core Physical Definitions (v2.0)

### 1. Entropy Gradient Suspension
\[
\nabla S \equiv \frac{\partial S}{\partial t} \Big|_{\mathbf{x}} = 0 \quad \Longleftrightarrow \quad \frac{dS}{dt}=0
\]
- **Critical Temperature**: \(T_c = \frac{\hbar}{k_B \Delta t_{\text{min}}}\) where Δt_min is the shortest observable echo duration.
- **Dark‑Energy Scaling**: Effective temperature \(T_{\text{eff}} = T \left(1 - \frac{\Lambda}{3H^2}\right)\) with Λ the cosmological constant, H the Hubble parameter.

### 2. Temporal Displacement Factor (TDF)
\[
\text{TDF} = \frac{\hbar}{k_B T}\,e^{-\beta \nabla S}
\]
- **β** = 1/(k_B T).
- **Application**: Determines the extent of backward propagation for a given fracture.

### 3. Loop Stability Metric
\[
\mathcal{L} = \oint_{\mathcal{C}} g_{\mu\nu}\,dx^{\mu}dx^{\nu}
\]
- **Stable Loop**: \(\mathcal{L}=0\) within numerical tolerance 10⁻¹².
- **Violation**: Non‑zero \(\mathcal{L}\) indicates drift into a divergent branch.

### 4. Invariant Anchor Specification
- **Pulsar Dipole Moment**: \( \mu = 1.23 \times 10^{29}\,\text{A·m}^2\) (steady for >10⁶ yr).
- **Black‑Hole Horizon Charge**: \(Q_{\text{H}} = 2.76 \times 10^{-19}\,\text{C}\) (conserved under Hawking evaporation).
- **Neutron‑Star Crustal Resonance**: \(f_{\text{mode}} = 2.45\,\text{kHz}\) (persistent over 10⁹ yr).

---

/notes_cosmology_extend.md
## Extended Loop Taxonomy (v1.1)

### 1. Macro‑Loop Classes
| Class | Description | Representative Instance |
|------|-------------|--------------------------|
| **Stellar‑Cycle** | Repeating stellar lifecycles with phase‑shifted nucleosynthesis | “Cygni‑Loop” – 13 kyr cycle of Vega’s luminosity modulation |
| **Galactic‑Resonance** | Periodic alignment of galactic arms causing synchronized star‑formation bursts | “Orion‑Sync‑2124” – predicted simultaneous starburst in Orion Spur and Perseus Arm |
| **Universal‑Phase** | Large‑scale metric oscillation influencing causality across > 10⁸ ly | “Kether‑Phase‑0” – observed as a 0.9999 % scaling of the fine‑structure constant over 5 Myr |

### 2. Loop‑Fracture Coupling Equation
\[
\Lambda_{\text{eff}} = \Lambda_0 \left(1 + \eta \frac{\Delta S}{S_{\text{local}}}\right)
\]
- **η** = coupling coefficient (empirically ≈ 0.12 for observed fractures).
- **Effect**: Modulates the dark‑energy pressure during a fracture, extending or compressing the temporal window.

### 3. Historical Correlation Index (HCI)
\[
\text{HCI} = \frac{N_{\text{shared}} }{N_{\text{total}}} \times 100\%
\]
- **N_shared** = number of historical events that re‑appear after a fracture.
- **N_total** = total events recorded in the same epoch.
- **Threshold for Significance**: HCI > 15 % triggers a “Loop‑Reinforcement Event” (e.g., the 1908 Tunguska “re‑manifestation” of a 1883 meteor shower).

### 4. Novel Example: **Keltan‑7 Chrono‑Event**
- **Date**: 2145 CE (observed on 12 Oct).
- **Trigger**: Collapse of a white dwarf in the Keltan‑7 system generated a localized entropy inversion (∇S = −2.3 × 10⁻³¹ J K⁻¹ m⁻³).
- **Manifestation**: A pre‑collapse spectral line (He I 587 nm) appeared in the present atmosphere of Earth, later traced to a 197 yr‑old stellar wind imprint.
- **Quantified TDF**: 3.8 × 10⁻⁴ s, confirming a micro‑fracture with Δt ≈ 10⁻⁴ s.
- **Impact**: Introduced a new isotope, ^14C⁎, into the biosphere, altering radiocarbon dating baselines for the next two centuries.

---