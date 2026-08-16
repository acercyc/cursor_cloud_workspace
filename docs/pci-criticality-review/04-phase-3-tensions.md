# Phase 3 — Tensions and dissociations

## 1. Psychedelics and ketamine: fit or break “near-critical = conscious”?

**They fit a *capacity* story and strain a *proximity* story.**

Anaesthetic-dose ketamine (Sarasso 2015; Maschke 2024): behaviorally unresponsive, high PCI, near-wake avalanche and chaos statistics, vivid reports. That is the best pharmacological dissociation of **arousal/responsiveness** from **consciousness-related dynamics**. It *supports* “PCI and near-criticality track consciousness, not motor output.”

Sub-anaesthetic / psychedelic ketamine (Farnes 2020): **PCI does not rise** above wake; spontaneous LZc/ACE/SCE **do**, and those rises correlate with subjective intensity. Schartner et al. (2017): LSD, psilocybin, and ketamine increase spontaneous MEG diversity. Toker et al. (2022): LSD may move slow dynamics *closer* to the edge of chaos.

So:

- If PCI were a linear readout of “how close to criticality / how complex,” it should climb with psychedelics. It does not (where measured).
- If PCI is a **ceilinged capacity** index — “can the thalamocortical system still sustain integrated, differentiated responses?” — wake and psychedelics both pass, and spontaneous diversity measures the *content* surplus.

REBUS (Carhart-Harris & Friston 2019) describes a flattened landscape and higher entropy. That can be “closer to criticality” *or* “slightly supercritical / more chaotic,” depending on the assay. Without TMS–PCI on LSD/psilocybin, the PCI axis for psychedelics is an **open cell** in the quadrant figure, not a measured point.

**Speculative:** psychedelics are a dissociation of spontaneous complexity from perturbational complexity. **Established:** that dissociation exists for sub-anaesthetic ketamine.

## 2. Which transition does PCI actually track?

Different criticality notions make different predictions. The data do not pick one winner.

| If PCI tracked… | Prediction | Observation |
| --- | --- | --- |
| Avalanche branching m → 1 | Low PCI when m ≪ 1 (local die-out) **or** m ≫ 1 (global stereotype) | Propofol *and* xenon look subcritical on avalanches, yet xenon TEPs look “supercritical-ish.” PCI low in both. Avalanche m is aligned with PCI in Maschke, but the xenon micro-story is bistability, not a supercritical branching process. |
| Edge of chaos (LLE → 0) | Low PCI when too stable *or* too chaotic | Maschke: unconsciousness is *more* chaotic and low-PCI. Solovey: unconsciousness is *more* linearly stable and (in other work) low complexity. Opposite-signed “stability” depending on the estimator. |
| Edge of synchrony (PCF) | PCI follows alpha pair correlation | Maschke: PCF did **not** predict PCI (sensor-level). Kim & Lee: PCF and Φ *do* co-peak in a model. Scale and method matter. |
| Escape from bistability | PCI high iff kicks do not trigger OFF-periods | Best qualitative match to NREM, UWS, xenon, slice sPCI. Not traditionally labeled “criticality.” |
| Nonequilibrium / irreversibility | PCI follows time-asymmetry of dynamics | Stikvoort 2025 in silico sfPCI: yes, in Hopf+EC models. Unmeasured for real TMS–PCI. |

**Working conclusion:** PCI is most faithfully described as indexing **whether a perturbation can unfold as a long, non-redundant causal movie**. That is *entailed* by near-critical branching *and* by low bistability *and* by sitting near a Hopf bifurcation with broken detailed balance. Those conditions overlap in healthy wake and come apart in xenon, psychedelics, and probably some DoC lesions.

## 3. Methodological confounds

**Power laws without criticality.** Touboul & Destexhe (2017): non-critical models can display the avalanche hallmarks experimental papers use. Beggs & Timme (2012): demand finite-size scaling and exponent relations. Maschke is more careful than most EEG papers (DCC, truncated-power-law caveats, hyperparameter sweeps) and still reports truncated laws in 25/30 recordings and lognormals in 5 — i.e. not textbook criticality.

**Subsampling.** Wilting & Priesemann (2018): naive m is biased down. Scalp EEG is an extreme subsample of neurons, spatially smeared. Absolute branching ratios from 60-channel EEG should not be compared to Beggs & Plenz’s σ = 1 as if they were the same quantity. Relative drug effects *within* subject are more credible than “the brain is at m = X.”

**Arousal vs consciousness.** PCI’s selling point is partial immunity (ketamine, REM, LIS). Criticality markers are **not** immune: they move with sleep pressure, attention, and eyes open vs closed (Zimmern 2020; Farnes eyes-open LZ). Any study that only contrasts wake vs propofol cannot claim a consciousness-specific criticality effect. The three-drug design (Sarasso / Maschke) is the right control; n = 5 per arm is not.

**PCI depends on site, preprocessing, and PCImax selection.** Casali/Casarotto already note site effects; clinical use takes the **maximum** across targets. A lesioned network can have a high-PCI island and a low-PCI island (Rosanova). Resting-state global criticality cannot see that map — Maschke says this explicitly. Caulfield et al. (preprint 2020) discuss intra-subject reliability by region.

**Spontaneous vs perturbational Lempel–Ziv.** Same algorithm family, different scientific object. Equating LZc(EEG) with PCI is a category error (Farnes 2020 is the demonstration).

**Chaos tests on biological noise.** Maschke’s own limitations: Rosenstein LLE is noise-sensitive; 0–1 test depends on low-pass choice; ketamine’s missing slow peak breaks Toker’s original pipeline. Direction of change *within* subject is safer than distance-to-zero claims.

**In silico PCI.** Hopf-BOLD “PCI” after a bifurcation-parameter punch is a cousin, not a clone. Treat Deco-line results as existence proofs for regime-dependence, not as calibration curves for TMS–EEG.

## 4. Seizure as a conceptual stress test

Toker: generalized seizures move away from edge-of-chaos. Avalanche lore: ictal recruitment is **supercritical**. PCI is rarely (ethically/practically) measured mid-seizure; one expects low differentiation (highly stereotyped dynamics) even if integration is pathologically high. If measured, seizure should sit at **low PCI, far from the useful critical region**, possibly on the opposite side from anesthesia. That would populate the “off-diagonal only if you collapse both sides of criticality onto one ‘distance’ axis” warning: **signed distance** (sub vs super) matters, unsigned distance does not.
