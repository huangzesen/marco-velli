# Method Cards — How Velli Does Science

## Overview

This layer distills Marco Velli's cognitive toolkit from 105 physics + methodology arguments. Each card identifies a recurring method, when to apply it, the procedure, why it works, and where it's observed across Velli's work.

**Rule**: Each card is backed by ≥3 VA instances from the arguments layer.

---

## VM001: Start from the Gradient

**When to apply**: Any system where transport, transfer, or transformation occurs — waves, turbulence, reconnection, heating.

**The procedure**: 1. Identify the dominant gradient (density, Alfvén speed, pressure, magnetic shear). 2. Ask what happens at the gradient — is there reflection, instability, critical threshold? 3. Remove the gradient in thought experiment — if the phenomenon disappears, the gradient is the engine.

**Why it works**: Physical systems do interesting things where quantities change, not where they're uniform. Gradient-driven analysis naturally captures causality rather than correlation.

**Observed in**: 16 VA — core method across Alfvén waves, reflection-driven turbulence, switchbacks, coronal heating, PSP-observations.

**Failure modes**: When the system is dominated by boundary conditions or external driving, not internal gradients.

**Transfer hints**: Any gradient-driven transport problem (atmospheric physics, fusion plasmas, stellar interiors).

---

## VM002: Find the Critical Point

**When to apply**: Problems involving a continuous parameter where the system behavior changes qualitatively (current sheet thickness, Lundquist number, expansion rate).

**The procedure**: 1. Identify the parameter space. 2. Look for the threshold where a small change produces a regime shift. 3. Derive the scaling at the threshold — it's often a power law. 4. Check if the threshold is physically accessible.

**Why it works**: Critical points reduce continuous complexity to discrete physics — before the threshold, one regime; after it, another. Nature often operates near thresholds.

**Observed in**: 16 VA — ideal tearing (S^{-1/3}), wave-to-turbulence transition, critical balance, switchback formation threshold.

**Failure modes**: When the system has multiple coupled thresholds; when the threshold lies outside physically accessible parameters.

**Transfer hints**: Phase transitions, self-organized criticality, laminar-to-turbulent transition.

---

## VM003: Cross-Scale Connection

**When to apply**: Problems spanning multiple orders of magnitude in length or time, where the physics at different scales is causally linked.

**The procedure**: 1. Identify the scale-connecting mechanism (cascade, reflection, recursive collapse). 2. Derive the scaling law that bridges scales. 3. Validate with observations at the extreme scale. 4. Check consistency across the full range.

**Why it works**: The solar wind is an intrinsically cross-scale system — photospheric motions (~Mm) → coronal structures (~1000 km) → in-situ measurements (~ion scales). Understanding the connection is the science.

**Observed in**: 18 VA — turbulence cascade (fluid → kinetic), recursive reconnection (macro → micro), 1/f → inertial range transition.

**Failure modes**: When scale separation breaks down; when different physics dominates at different scales.

**Transfer hints**: Any multi-scale system: climate, neuroscience, materials science.

---

## VM004: The Expanding Box Model (EBM)

**When to apply**: Problems where the system expansion is not a background effect but an active physical parameter that controls wave evolution, turbulence, or instability.

**The procedure**: 1. Embed the local dynamics in an expanding reference frame. 2. Treat expansion rate as a control parameter. 3. Derive how expansion modifies wave amplitudes, cascade rates, and instability thresholds. 4. Compare with fixed-box simulations to isolate expansion effects.

**Why it works**: Solar wind expansion is not a perturbation — it's a dominant effect. The EBM captures the dual role of expansion: it both drives the cascade (via reflection) and suppresses it (via adiabatic cooling).

**Observed in**: 10 VA — EBM development, reflection-driven turbulence, switchback growth, wave action conservation.

**Failure modes**: When expansion is too fast for the local equilibrium assumption; when kinetic effects dominate.

**Transfer hints**: Expanding Universe, galactic outflows, supernova remnants.

---

## VM005: Theory-Driven, Data-Validated

**When to apply**: Long-term research programs where theoretical predictions can be made decades before observational confirmation.

**The procedure**: 1. Derive a bold, specific prediction from theory. 2. Make it testable — specify the observable signature. 3. Wait for the data. 4. If confirmed, the theory is validated; if not, revise — don't discard.

**Why it works**: Physics is not a collection of empirical facts. Theory provides the causal narrative; data tests it. This method creates durable knowledge that survives observational surprises.

**Observed in**: 7 VA — 1/f spectrum prediction (1989 → PSP 2019+), ideal tearing (2013 → PSP 2022+), reflection-driven turbulence (2007 → PSP 2020+).

**Failure modes**: When the prediction is not specific enough to test; when the data cannot distinguish between competing theories.

**Transfer hints**: Any field with long experimental cycles (particle physics, cosmology, geophysics).

---

## VM006: Parameterize Uncertainty

**When to apply**: Problems with large parameter uncertainties, inaccessible boundary conditions, or unknown initial states.

**The procedure**: 1. Identify the free parameters (gradient profiles, boundary amplitudes, dissipation coefficients). 2. Vary them systematically. 3. If the result is robust across parameter space, it's a scaling law; if not, the parameter dependence is itself the result.

**Why it works**: Heliophysics has fundamental measurement limitations (can't place probes in the corona). Parameterizing uncertainty avoids false precision while extracting robust scaling relationships.

**Observed in**: 5 VA — reflection-driven turbulence (v_A profile as parameter), ideal tearing (α parameter), turbulent heating rates.

**Failure modes**: When the parameter space is too large or too poorly constrained; when results are not robust.

**Transfer hints**: Climate modeling, astrophysics, systems biology.

---

## VM007: Numerical Experiments

**When to apply**: When the physics is too nonlinear for analytic theory but the question is specific enough to design a controlled numerical test.

**The procedure**: 1. Design the minimal model that captures the target physics (reduced MHD, EBM, 2D slice). 2. Change ONE parameter at a time. 3. Compare with analytic predictions, not just observations. 4. Extract scaling laws from the simulation ensemble.

**Why it works**: MHD simulations are not black boxes — they are controlled experiments where you isolate the physics. The reduced MHD framework is designed to answer specific questions, not to reproduce reality.

**Observed in**: 5 VA — RMHD of coronal heating, resistive MHD of ideal tearing, EBM of switchbacks.

**Failure modes**: When the model is too reduced and misses essential physics; when numerical effects dominate.

**Transfer hints**: Any field using simulation as a scientific tool (climate, fusion, astrophysics).

---

## VM008: Comparative Analysis

**When to apply**: When two or more populations, regimes, or datasets need to be systematically compared to identify what controls the difference.

**The procedure**: 1. Identify the comparison axis (fast vs. slow wind, open vs. closed field, proton vs. electron). 2. Isolate the single variable that differs. 3. Attribute the difference in outcome to the difference in that variable.

**Why it works**: Controlled comparison is a fundamental scientific method. In heliophysics, where experiments are impossible, comparative analysis is the closest substitute.

**Observed in**: 4 VA — fast vs. slow wind thermodynamics, open vs. closed field heating, proton vs. electron temperatures.

**Failure modes**: When multiple variables differ simultaneously; when the comparison is confounded.

**Transfer hints**: Medical trials, comparative planetology, ecology.

---

## VM009: Let Surprise Guide New Theory

**When to apply**: When observations reveal an unexpected phenomenon that existing theory did not predict.

**The procedure**: 1. Acknowledge the surprise — don't force-fit into existing frameworks. 2. Document the phenomenon quantitatively. 3. Ask: what minimal physics must we add to explain this? 4. Build the new theory from the unexpected observation outward.

**Why it works**: Surprise is a signal that current understanding is incomplete. The most productive science often comes from anomalies (switchbacks, 1/f spectrum, nanoflares).

**Observed in**: 3 VA — switchbacks discovery (PSP Enc 1), dust depletion zone, and the broader pattern of PSP surprises.

**Failure modes**: When the surprise is actually a measurement artifact; when the theory community moves to a new fad prematurely.

**Transfer hints**: Any discovery-driven science (biology, astronomy, neuroscience).

---

## VM010: Multi-Point Synergy

**When to apply**: When a single spacecraft cannot distinguish spatial from temporal variations, or when one vantage point is insufficient to map the causal chain from source to observation.

**The procedure**: 1. Place multiple instruments at different radial distances or positions. 2. Correlate features across vantage points. 3. Separate spatial structure from temporal evolution. 4. Trace the causal chain from corona to 1 AU.

**Why it works**: Single-point measurements in the solar wind are fundamentally ambiguous. PSP + Solar Orbiter + SolO's Metis provide the first true multi-point solar wind campaign.

**Observed in**: 3 VA — PSP-Solar Orbiter radial alignments, quadrature campaigns, magnetic connectivity mapping.

**Failure modes**: When separations are too large or too small; when instruments are not cross-calibrated.

**Transfer hints**: Magnetospheric missions (Cluster, MMS), heliospheric fleet, any multi-spacecraft constellation.
