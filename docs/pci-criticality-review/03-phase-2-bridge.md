# Phase 2 — The bridge

This is the core of the review: mechanisms that could make PCI *track* criticality, and the papers that actually measure both (or a proxy of both).

## Mechanism: bistability and OFF-periods

Pigorini et al. (2015) give the cellular-network reason PCI falls in NREM. Intracortical stimulation in humans during N3 still activates cortex, but the activation is followed by a **down-state**: high-frequency (>20 Hz) power collapses (an OFF-period). When firing resumes, **deterministic phase-locking to the stimulus has been wiped**. Causal chains cannot accumulate. The TEP becomes a stereotyped slow wave — low Lempel–Ziv complexity after normalization.

Rosanova et al. (2018) show the same motif in **awake UWS**: TMS reveals OFF-periods that healthy wake never produces, locally destroying causality and blocking global complexity. The 2024 *Nat. Commun.* update (sleep-like dynamics after injury) treats this as a general principle: disconnected or neuromodulator-poor cortex reverts to a default bistable mode.

**Criticality reinterpretation (partly established, partly interpretive):**

- An asynchronous, near-critical branching process is a regime in which a kick produces a long-tailed family of cascade sizes (Kinouchi & Copelli; Shew & Plenz).
- A forced down-state is a **reset**: the branching process is absorbed. That is operationally subcritical on short timescales, even if slow-wave oscillations look “big.”
- Xenon’s TMS response is the pedagogical case (Sarasso 2015): huge amplitude, tiny PCI. Maschke et al. (2024) still classify xenon EEG avalanches as **subcritical** (earlier drop-off, lower branching ratio) despite large raw voltages. Power ≠ criticality.

D’Andola et al. (2017) close a mechanistic loop at slice scale: pharmacologically reducing Up/Down bistability (NE + carbachol) **raises sPCI**; cranking excitability alone does less. That is the closest causal evidence that the PCI family indexes *escape from bistability*, which is overlapping with, but not identical to, “approaching avalanche criticality.”

## Dynamics / stability: Solovey 2015

Solovey et al. treat cortex as a high-dimensional dynamical system and ask how close the Jacobian (via multivariate models of ECoG) sits to the **edge of instability**. In monkeys, propofol and ketamine–medetomidine both **stabilize** eigenmodes as consciousness is lost; modes drift back during recovery. Stability is not a property of single channels.

This is the “consciousness = near-unstable / critical” slogan in linear-systems language. It **predicts** that a TMS kick should persist and spread more in wake than under anesthesia — PCI-compatible.

**Caveat (important for Phase 3):** “stabilization” is not the same observable as the 0–1 chaos test or LLE on slow waves. Maschke (2024) finds *increased* chaoticity under propofol/xenon. Solovey finds *fewer* near-unstable linear modes. Both can be true if slow-wave bistability is locally unstable/chaotic while the network’s stimulus-relevant modes are overdamped. Do not collapse them into one “distance from criticality” axis.

## Most direct pre-2024 link: Toker 2022

Toker et al. apply a **modified 0–1 chaos test** to slow (roughly 1–6 Hz, peak-selected) cortical oscillations in human/macaque ECoG, MEG, and clinical EEG.

- Wake: near the edge of chaos.
- Anesthesia, generalized seizures: away from that point; information processing suffers.
- Psychedelics (LSD): may **tune closer** to the point, with higher information richness.
- DoC: proximity proposed as a clinical index.

This paper does **not** compute PCI. It computes a spontaneous, oscillation-dependent chaos statistic plus LZ-like richness. It is the right *family* of claim (near-critical slow dynamics support consciousness) but a different *instrument* than TMS–EEG.

Limitations the authors and later users (including Maschke) flag: the test needs a slow oscillatory peak; ketamine can lack one; seizures and anesthesia may leave the edge in different directions; edge-of-chaos ≠ avalanche criticality.

## The paper that actually predicts PCI from criticality: Maschke, O’Byrne et al. 2024

This is the citation-intersection that the plan hoped for, published after Toker and using the Sarasso 2015 PCI dataset.

**Design.** n = 15 healthy adults (5 propofol, 5 xenon, 5 ketamine) to Ramsay 6. Resting EEG before TMS. PCImax from Sarasso. Metrics: avalanche statistics (DCC, branching ratio, Fano, repertoire), chaoticity (0–1 test, LLE, covariance width), plus LZC, fractal dimension, MSE, Hurst, spectral slope, PCF.

**Findings (treat as empirical, small-n):**

1. Propofol and xenon: fewer/smaller avalanches, worse power-law behavior, higher DCC, lower branching ratio → **subcritical** relative to wake. Ketamine ≈ wake.
2. Propofol and xenon: **higher** chaoticity (LLE, 0–1, covariance width). Ketamine ≈ wake. Authors interpret wake as slightly on the chaotic side of the edge; unconsciousness moves *further into* chaos.
3. Resting-state battery predicts PCImax (ridge regression, LOSO error ~0.065, ~6.5%). A 0.35 threshold separated conscious vs unconscious on both true and predicted PCI in this sample.
4. PCF (edge of synchrony, sensor-level alpha) **did not** track PCI or drug condition — a live example of non-equivalent criticalities.

**What this does and does not show.**

- Does: in this pharmacological model, *some* spontaneous criticality statistics share enough variance with PCI to predict it.
- Does not: identity of PCI with distance-to-criticality; causal tuning; DoC validity (authors explicitly warn against generalizing to injured networks; Liu et al. differences MCS vs anesthesia).
- Surprise vs naive mapping: xenon was expected (by the authors) to look **supercritical** because TEPs are global. Avalanche metrics said **subcritical**. Bistability can produce big waves that are still poor branching processes.

## Modeling: tuning a network and computing (something like) PCI

| Work | What is tuned | What is “PCI” | Result |
| --- | --- | --- | --- |
| Shew / Plenz cultures | E–I balance | Evoked pattern entropy | Peaks at avalanche criticality |
| D’Andola 2017 | Neuromodulators / bistability | sPCI (LZ of evoked MUA) | Rises when bistability falls |
| Kim & Lee 2019 | Coupling toward Hopf/synchrony criticality | Φ, not PCI | Φ max at criticality; drops under propofol |
| Sanz Perl / Deco 2022 | Hopf: subcritical fluctuations vs supercritical oscillations | Adapted PCI on simulated BOLD | Fluctuation (subcritical) regime more perturbable; oscillatory regime PCI-like score barely budges |
| Stikvoort / Deco / Sanz Perl 2025 | Personalized Hopf + generative EC | sfPCI (PCIst-style on simulated BOLD) | Lower arousal/awareness → less irreversibility, more symmetric EC, lower sfPCI. Mechanism emphasized: **nonequilibrium**, not avalanches |

**How to read the models.** They support a family resemblance: *something* about operating near a bifurcation (Hopf, branching, E–I) maximizes the complexity of a kick. They do **not** show that Casali PCI is a calibrated ruler of branching ratio m. Timescale (BOLD vs EEG), perturbation (parameter kick vs TMS pulse), and complexity statistic all differ.

## Search note (Casali × Toker × keywords)

Forward-looking from Casali 2013 and Toker 2022 with {criticality, avalanche, branching, edge of chaos, bistability} × {PCI, PCIst, TMS-EEG, Lempel-Ziv} yields a short list. The **non-redundant hits** that actually join the constructs are Maschke 2024 (empirical PCI ← resting criticality), D’Andola 2017 (sPCI ← bistability), Sanz Perl 2022 and Stikvoort 2025 (in silico PCI-like ← regime / irreversibility), Kim & Lee 2019 (Φ ← criticality). Everything else is either PCI without criticality or criticality without PCI.

That scarcity is itself a result: until 2024, the two literatures mostly cited each other as *philosophy*.
