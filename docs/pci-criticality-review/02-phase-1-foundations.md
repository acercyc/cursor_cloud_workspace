# Phase 1 — Foundations

## Track A: Brain near-criticality

### What “criticality” is doing in this literature

A critical point is a **phase transition** where macroscopic observables change qualitatively (order ↔ disorder, amplifying ↔ dying activity, stable ↔ chaotic trajectories). Near that point, systems often show: scale-free events, long-range correlations, high susceptibility, and a wide dynamic range. That package is why people connect criticality to computation and, later, to consciousness.

O’Byrne & Jerbi (2022) and Zimmern (2020) both insist on a point that later PCI debates ignore at their peril: **these are not equivalent transitions**. Mixing them produces fake disagreements.

### Three non-equivalent notions (and their markers)

| Notion | Transition between | Typical markers | What “away from critical” looks like |
| --- | --- | --- | --- |
| **Avalanche / absorbing-state / branching-process criticality** | Activity dies out vs activity explodes | Avalanche size/duration power laws (classically τ ≈ 3/2); branching ratio m or σ ≈ 1; DCC (exponent relation); Fano factor; avalanche repertoire | **Subcritical** m < 1: small, brief cascades. **Supercritical** m > 1: system-spanning, stereotyped events |
| **Edge of chaos** | Stable attractors vs chaotic divergence | Largest Lyapunov exponent → 0; modified 0–1 chaos test; covariance-spectrum width (Dahmen-style) | Too stable: perturbations vanish. Too chaotic: perturbations are forgotten by sensitive dependence |
| **Edge of synchronization** | Incoherent vs fully synchronized oscillators | Pair correlation function (PCF) in a narrow band (often alpha); Kuramoto-like order parameter susceptibility | Too sync: low differentiation. Too async: low integration |

Long-range temporal correlations (DFA / Hurst) and aperiodic 1/f slope are **related** but not proprietary to one transition. Lempel–Ziv complexity of spontaneous EEG is even less specific: it rises with both richness *and* certain kinds of randomness.

Beggs & Plenz (2003) is the empirical origin of the avalanche story: organotypic and acute cortical tissue, LFP avalanches, σ ≈ 1, information-transmission argument. Kinouchi & Copelli (2006) give the functional payoff: **dynamic range peaks at criticality** — exactly the property you want if you are about to hit the cortex with TMS and ask how many distinct, graded responses you get.

### Why *near* (slightly subcritical) rather than exact

Wilting & Priesemann (2018) is the key empirical correction. Spatial **subsampling** systematically makes networks look more stable than they are. Their multi-step estimator, applied to rat, cat, and monkey spikes, yields m̂ in a tight band below 1 (median ≈ 0.98): a **reverberating** regime. Perturbations last hundreds of milliseconds, not instantly nor forever.

Why that might be a feature:

- **Safety margin** against supercritical runaway (seizure-like recruitment).
- **Tunability**: a slightly subcritical network can be pushed toward or away from criticality by arousal, attention, neuromodulators (O’Byrne & Jerbi 2022; Wilting et al. related work).
- **State dependence**: sleep, anesthesia, and task engagement all move markers (Zimmern 2020). Cognitive load findings are mixed (sometimes more subcritical during tasks).

**Established:** scale-free-like avalanches exist in many preparations; in vivo cortex is not a simple asynchronous-irregular Poisson soup.  
**Modeling / inferred:** exact membership in the directed-percolation universality class; the “true” m of the whole human cortex.  
**Speculative:** that *every* useful brain function requires occupancy of *the* critical point.

---

## Track B: PCI and perturbational complexity

### Why perturb at all?

IIT-style reasoning (Tononi; Casali et al. 2013): a conscious substrate must be both **integrated** (parts affect each other) and **differentiated** (many distinct states). Spontaneous EEG complexity confounds that capacity with whatever the brain happens to be doing (sensory drive, muscle, arousal). Sensory stimuli fail in DoC because pathways may be broken. **Direct cortical perturbation** (TMS) plus hd-EEG asks: *if I inject a cause, how extended and how non-redundant is the effect?*

Massimini et al. (2005, 2010) already showed the qualitative contrast: NREM → local, simple TEP; REM/wake → widespread, differentiated TEP.

### Original PCI (Casali 2013)

Pipeline, compressed:

1. TMS to a cortical target (often premotor or parietal), hd-EEG.
2. Source-estimate significant spatiotemporal activation vs baseline (bootstrap).
3. Binarize the significant source matrix.
4. Lempel–Ziv compress that binary movie; **normalize** by source strength/length so that a huge stereotyped wave does not score as “complex.”

PCI is high only if the response is **both** distributed **and** hard to compress. That is why propofol (local) and xenon (global but stereotyped) can both score low (Sarasso 2015).

### Clinical validation (Casarotto 2016)

- Benchmark: conditions with vs without subjective report (including delayed dream reports).
- **PCI\* = 0.31** on PCImax; benchmark Se/Sp 100% in that paper’s ROC.
- MCS detection sensitivity 94.7%.
- A subset of VS/UWS (9/43) exceeds PCI\* — the covert-consciousness candidate group.
- Later replication-style work (e.g. *Brain Sci.* 2020, 10:917) reports ~92% MCS sensitivity and a similar high-PCI UWS minority.

### PCIst (Comolatti 2019)

Same scientific target, cheaper statistic: PCA + count of **state transitions** in the evoked trajectory. Matches classification accuracy; works on SPES/SEEG; fast. Useful because later *in silico* papers (Stikvoort 2025) implement this variant, not Casali LZ.

### Empirical track record (states)

| State | Typical PCI / TEP complexity | Notes |
| --- | --- | --- |
| Wake | High (well above 0.31) | Site-dependent; PCImax used clinically |
| REM | High / wake-like | Unresponsive but reportable dreams |
| NREM (N3) | Low | OFF-period / bistability (Pigorini) |
| Propofol, midazolam | Low (local collapse) | Failed integration |
| Xenon | Low (global slow wave) | Failed differentiation |
| Ketamine (anaesthetic dose) | High, wake-like | Unresponsive + vivid reports (Sarasso 2015) |
| Sub-anaesthetic ketamine | PCI ≈ wake | Spontaneous LZ **up** (Farnes 2020) |
| Psychedelics (LSD, psilocybin) | **PCI largely unmeasured** | Spontaneous MEG diversity **up** (Schartner 2017) |
| MCS / LIS / EMCS | Usually high | Casarotto 2016 |
| VS/UWS | Often low; subset high | OFF-periods in low-PCI UWS (Rosanova 2018) |

**Established:** PCI (and PCIst) robustly tracks reportable consciousness vs no-report in sleep and several anesthetics, and stratifies DoC better than chance.  
**Assumed:** that the IIT-inspired interpretation (integration + differentiation as *the* mechanism of consciousness) is why it works. A criticality account is a competing/complementary mechanistic story.  
**Not shown in Phase 1:** that PCI numerically equals distance-to-criticality.
