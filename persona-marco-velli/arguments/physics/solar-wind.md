# Physics Arguments — Solar Wind

---

## VA700: Polytropic Solar Wind Acceleration: PSP Observations Constrain 1D Wind Models Beyond Isothermal Parker

**Domain**: physics
**Claim**: A simple one-dimensional polytropic solar wind model — extending the classic Parker (1958) isothermal solution to include separate proton and electron polytropic indices — can quantitatively reproduce Parker Solar Probe's observed radial profiles of solar wind speed, density, and temperature from ~13 R☉ to 1 AU when the polytropic indices are fitted from PSP measurements, demonstrating that the thermodynamic acceleration mechanism alone (without explicit wave pressure terms) can account for the bulk of solar wind acceleration in both fast and slow streams.

**What he did**: Shi, Velli and collaborators compared PSP encounter data (speed, density, proton and electron temperatures as functions of heliocentric distance) against numerical solutions of the 1D polytropic wind equations. They fitted separate polytropic indices γ_p and γ_e to match the observed radial gradients. The model treats electrons and protons as separate polytropic fluids flowing radially from a coronal base, with the polytropic index encoding all unresolved heating physics into a single effective parameter.

**The product**:
- Shi, Velli, Bale, Réville, Maksimović & Dakeyo, "Acceleration of polytropic solar wind: Parker Solar Probe observation and one-dimensional model," Physics of Plasmas 29, 2022

**Primary results**:
- Polytropic indices γ_p ≈ 1.25 (protons) and γ_e ≈ 1.15 (electrons) for slow wind; different values for fast wind
- The model reproduces PSP-observed speed profiles from subsonic corona to supersonic wind
- Demonstrates that bulk acceleration is captured by polytropic expansion without explicit turbulent heating terms
- Provides a baseline against which wave-driven and turbulence-driven acceleration models must show improvement

**Context**: The Parker (1958) isothermal wind was the first analytical model of solar wind acceleration but assumed an unrealistic constant temperature. The polytropic extension allows a physically motivated temperature decline. This paper provided a modern observational calibration using PSP data, establishing the simplest quantitative benchmark. More sophisticated models (wave-driven, turbulence-driven — see alfven-waves.md) must improve upon this baseline to demonstrate that additional physics matters for acceleration.

**Citekeys**: shi2022
**Cross-refs**: VA001 (Velli 1989, 1/f spectrum), VA002 (Verdini & Velli 2007)

---

## VA701: Proton and Electron Temperature Correlations Reveal Dual Thermodynamic Structure of Fast vs. Slow Solar Wind

**Domain**: physics
**Claim**: The proton and electron temperatures in the solar wind exhibit distinct correlations with solar wind speed that cannot be explained by a single heating mechanism — protons in fast wind are much hotter than in slow wind (T_p ∝ v_sw^2 approximately), while electrons show a much weaker speed dependence, revealing that fast and slow wind are thermodynamically distinct plasma populations heated by different mechanisms operating at different heliocentric distances.

**What he did**: Shi, Velli, Lionello, Sioulas, Huang, Halekas, Tenerani, Réville, Dakeyo, Maksimović & Bale compiled comprehensive proton and electron temperature measurements from PSP encounters spanning ~13–50 R☉, and compared them with global coronal model predictions using the Predictive Science Inc. MAS (Magnetohydrodynamic Algorithm outside a Sphere) model. They traced the temperature-speed correlations from the inner corona outward and separated the thermodynamic evolution of the two species.

**The product**:
- Shi, Velli, Lionello, Sioulas, Huang, Halekas, Tenerani, Réville, Dakeyo, Maksimović & Bale, "Proton and electron temperatures in the solar wind and their correlations with the solar wind speed," ApJ 945, 2023

**Primary results**:
- T_p ∝ v_sw^(1.5–2) in the inner heliosphere, confirming proton heating scales strongly with flow speed
- T_e shows much weaker speed dependence: electrons are thermally similar in fast and slow wind
- The T_p–v_sw correlation strengthens with heliocentric distance, indicating ongoing proton heating in transit
- MAS model reproduces electron but not proton temperatures — proton heating requires physics beyond global MHD (consistent with reflection-driven turbulence)
- Implies fast wind receives more proton-specific heating, likely via cyclotron/resonant interactions with Alfvénic fluctuations

**Context**: The temperature-speed correlation was known since the Helios era (1970s), but PSP provided the first measurements deep enough to determine where the correlation is established — in the low corona or in transit. This paper showed that the fast-slow wind dichotomy is fundamentally thermodynamic, not merely kinematic, and that the heating mechanism discriminates by species. The failure of global MHD to capture proton heating directly motivates the reflection-driven turbulence model (see alfven-waves.md, VA002).

**Citekeys**: shi2023
**Cross-refs**: VA700 (polytropic acceleration baseline), VA002 (Verdini & Velli 2007)

---

## VA702: Total Wave Action Conservation Governs the Global Energetics of the Expanding Solar Wind

**Domain**: physics
**Claim**: The total wave action — the conserved quantity combining Alfvén wave energy flux with Doppler shifting by the background solar wind flow — is conserved in the expanding solar wind even when nonlinear effects (parametric decay, reflection, turbulent dissipation) are present, providing a powerful integral constraint that governs the global energy budget from the corona to 1 AU and links wave energy deposition directly to solar wind acceleration.

**What he did**: Huang, Shi, Sioulas & Velli derived and demonstrated the conservation of total wave action for Alfvénic fluctuations in a spherically expanding solar wind with a background flow. Starting from the WKB framework and extending to include nonlinear corrections, they showed that the action density A = E/(ω₀ − k·U) (wave energy divided by intrinsic frequency Doppler-shifted by the flow) is conserved along ray paths, even when the wave amplitude is large and the background varies steeply.

**The product**:
- Huang, Shi, Sioulas & Velli, "Conservation of Total Wave Action in the Expanding Solar Wind," ApJ 934, 2022

**Primary results**:
- Wave action conservation holds across the Alfvén critical point, where WKB wave energy flux alone breaks down
- The conserved action integral provides a direct link between wave energy launched at the photosphere and energy deposited in the corona and wind
- This constrains the total energy available for coronal heating and wind acceleration from wave-driven mechanisms
- Explains why the Alfvén surface is energetically important: it marks where wave energy transitions from Sun-bound to advected by the wind

**Context**: Wave action conservation is a fundamental principle from plasma physics (Bretherton & Garrett 1968) that Velli's group applied systematically to the solar wind problem. It provides the theoretical backbone for connecting wave-driven heating models to observational constraints: if you know the wave amplitude at one radius, wave action conservation tells you the maximum energy available for heating at every other radius. This is the energy-budget foundation on which the reflection-driven turbulence model (VA002) and the wave-turbulence-driven (WTD) solar wind acceleration models are built.

**Citekeys**: huang2022
**Cross-refs**: VA001 (Velli 1989, wave reflection), VA002 (Verdini & Velli 2007)

---

## VA703: The Heliospheric Current Sheet Shapes the Global Evolution of Solar Wind Turbulence

**Domain**: physics
**Claim**: The heliospheric current sheet (HCS) fundamentally modifies the evolution of solar wind turbulence in its vicinity, creating a zone of enhanced turbulence intensity, reduced cross-helicity (more balanced turbulence), and altered spectral properties that differ markedly from the surrounding solar wind.

**What he did**: Shi, Velli, Tenerani, Réville & Rappazzo performed numerical simulations of MHD turbulence evolution in an expanding solar wind containing a model heliospheric current sheet. They solved the RMHD equations in the expanding-box framework with a magnetic polarity reversal, tracking how the turbulence cascade and cross-helicity evolve across the HCS. The HCS provides a source of counter-propagating Alfvén waves (via reconnection and shear), which feeds the local turbulent cascade.

**The product**:
- Shi, Velli, Tenerani, Réville & Rappazzo, "Influence of the heliospheric current sheet on the evolution of solar wind turbulence," ApJ 930, 2022

**Primary results**:
- The HCS region develops enhanced turbulence levels compared to the surrounding solar wind
- Cross-helicity σ_c drops toward zero near the HCS (balanced turbulence), whereas the surrounding wind is imbalanced (σ_c ≈ +0.5–0.8)
- Magnetic reconnection at the HCS contributes to turbulence generation and plasma heating
- The turbulence transition across the HCS is sharp — occurring over a few correlation lengths
- PSP observations of enhanced fluctuations near sector boundaries confirm these predictions

**Context**: The HCS is the largest-scale magnetic structure in the heliosphere, yet its role in turbulence evolution was poorly quantified before this work. Velli's group showed that the HCS is not merely a passive boundary but an active turbulence generation zone. This connects solar wind large-scale structure (sector boundaries) to small-scale turbulent dynamics — a bridge between heliospheric structure physics and turbulence physics. PSP's crossings of the HCS near the Sun provided direct validation.

**Citekeys**: chen2022
**Cross-refs**: VA001 (wave reflection), VA002 (reflection-driven turbulence), VA711 (magnetic imprints)

---

## VA704: Alfvénic Slow Solar Wind Is a Distinct Plasma Population Traced Back to Coronal Streamer Origins

**Domain**: physics
**Claim**: A significant fraction of the slow solar wind exhibits Alfvénic fluctuations (high cross-helicity, velocity-magnetic field correlations) previously thought characteristic only of fast polar wind — and this "Alfvénic slow wind" originates from the boundaries of coronal streamers and active regions, not from the deep heliospheric current sheet, implying that interchange reconnection at streamer boundaries launches Alfvénic fluctuations into the slow wind.

**What he did**: D'Amicis, Perrone, Bruno & Velli analyzed multi-spacecraft data (Helios, Wind, Ulysses, Parker Solar Probe) to identify and characterize intervals of Alfvénic slow solar wind. They traced the source regions using magnetic mapping (PFSS models) and compared the properties of Alfvénic vs. non-Alfvénic slow wind. Velli provided the theoretical interpretation linking the observations to interchange reconnection at streamer boundaries.

**The product**:
- D'Amicis, Perrone, Bruno & Velli, "On Alfvénic Slow Wind: A Journey From the Earth Back to the Sun," JGR: Space Physics 126, 2021

**Primary results**:
- Alfvénic slow wind has σ_c ≈ +0.5 to +0.8, similar to fast wind — contradicting the expectation that slow wind is non-Alfvénic
- Source regions map to streamer boundaries and active region edges, not the HCS center
- The Alfvénic character persists from near the Sun to 1 AU with only gradual degradation
- Explained by interchange reconnection at streamer stalks injecting open flux and Alfvénic perturbations into the slow wind channel
- The slow wind is not a single plasma population: it has both Alfvénic (streamer boundary origin) and non-Alfvénic (HCS/streamer body origin) components

**Context**: Before this work, the slow solar wind was treated as a monolithic entity — non-Alfvénic, variable, originating from the closed-field regions. The discovery that a substantial fraction is Alfvénic unified the fast and slow wind pictures: both can carry Alfvénic fluctuations, and the difference lies in source region geometry rather than fundamental plasma physics. This connects to Bale, Drake, Velli et al. 2023 (Nature) on interchange reconnection as the fast wind source — the same mechanism operates at different scales for both fast and Alfvénic slow wind.

**Citekeys**: damicis2021
**Cross-refs**: VA708 (SO Alfvénic intervals), VA310 (reconnection), VA001 (Alfvén wave basics)

---

## VA705: Solar Orbiter Measures the Sun's Angular Momentum Loss via the Bφ Component of the Interplanetary Magnetic Field

**Domain**: physics
**Claim**: Solar Orbiter's first-orbit measurements of the azimuthal magnetic field component Bφ provide a direct observational constraint on the solar wind's angular momentum flux, confirming that magnetic torques (the "Parker spiral tension") dominate the Sun's angular momentum loss and validating the theoretical prediction that the solar wind carries away the Sun's rotational angular momentum via the field-line tension of the spiraled interplanetary magnetic field.

**What he did**: Verscharen, Stansby, Finley, Owen, Horbury, Velli and collaborators analyzed Solar Orbiter's magnetic field and plasma measurements during its first orbit (2020), computing the angular momentum flux carried by both the plasma flow and the magnetic stress. Velli contributed the theoretical framework linking the Bφ measurement to angular momentum transport. The Parker spiral geometry produces a Bφ component that exerts a tangential Maxwell stress on the Sun.

**The product**:
- Verscharen, Stansby, Finley, Owen, Horbury, Velli et al., "The solar-wind angular-momentum flux observed during Solar Orbiter's first orbit," EGU General Assembly 2021

**Primary results**:
- The magnetic (Maxwell stress) contribution to angular momentum flux dominates over the plasma (Reynolds stress) contribution
- Bφ measurements from Solar Orbiter are consistent with Parker spiral predictions at the observed radial distances
- Confirms the classical picture: the Sun's rotational braking is primarily mediated by the solar wind's magnetic field, not by direct plasma momentum
- The angular momentum loss rate is consistent with solar spin-down timescales of ~10 billion years

**Context**: The question of how the Sun loses angular momentum has been fundamental since Parker's 1958 model predicted the spiral IMF. The Bφ component is the observational signature of this mechanism. Solar Orbiter, with its combined magnetometer and plasma instruments, provided the first modern in-situ confirmation of the angular momentum flux decomposition. This connects to broader questions of stellar spin-down and the magnetic braking of solar-type stars.

**Citekeys**: verscharen2021
**Cross-refs**: VA001 (Alfvén wave propagation in expanding wind), VA711 (magnetic imprints)

---

## VA706: PSP–Solar Orbiter Quadrature Campaigns Trace Solar Wind from Coronal Source to In-Situ Acceleration Region

**Domain**: physics
**Claim**: The first Solar Orbiter–Parker Solar Probe quadrature enabled simultaneous remote-sensing imaging of the solar wind's coronal source and in-situ measurement of the accelerating wind plasma, establishing that the slow solar wind originates in the streamer belt and accelerates through the subsonic-to-supersonic transition within 10–20 R☉, as predicted by Parker-type models.

**What he did**: Telloni, Andretta, Antonucci, Velli and the Solar Orbiter team coordinated observations during the first PSP–Solar Orbiter quadrature. Solar Orbiter's Metis coronagraph imaged the corona in visible light and UV Ly-α, providing electron density and outflow speed maps. PSP simultaneously measured the solar wind plasma in-situ. The combined dataset traced a single plasma parcel from its coronal source (imaged by Metis) through the acceleration region (sampled by PSP).

**The product**:
- Telloni, Andretta, Antonucci, Velli et al., "Exploring the Solar Wind from Its Source on the Corona into the Inner Heliosphere during the First Solar Orbiter–Parker Solar Probe Quadrature," ApJL 912, 2021

**Primary results**:
- First combined remote-sensing + in-situ tracing of a single solar wind flow tube from corona to inner heliosphere
- Slow wind outflow speeds measured by Metis in the outer corona (~3–8 R☉) match extrapolation to PSP in-situ speeds at ~30 R☉
- Confirms streamer belt as the primary slow wind source
- The acceleration profile is consistent with a polytropic or wave-driven model with effective γ ≈ 1.1–1.3
- Demonstrates the transformative power of PSP–Solar Orbiter quadrature campaigns for solar wind physics

**Context**: Solar wind source identification has been a central challenge since the discovery of the wind. Remote sensing alone cannot measure plasma properties; in-situ alone cannot image the source. The PSP–Solar Orbiter quadrature geometry breaks this impasse. Velli, as both PSP Observatory Scientist and Solar Orbiter Co-I, was uniquely positioned to coordinate this synergy. This is the observational realization of the long-held vision of multi-point heliospheric measurements.

**Citekeys**: telloni2021
**Cross-refs**: VA700 (polytropic acceleration), VA002 (wave-driven acceleration)

---

## VA707: Magnetic Connectivity Mapping from PSP to the Solar Surface via PFSS Models Reveals Wind Source Regions

**Domain**: physics
**Claim**: Potential Field Source Surface (PFSS) magnetic field models, combined with PSP's in-ecliptic trajectory within 0.5 AU, enable reliable mapping of the sub-Alfvénic solar wind back to its coronal source regions — demonstrating that the first PSP encounters sampled wind originating from a small equatorial coronal hole adjacent to a streamer belt, explaining the observed hybrid Alfvénic/variable character of the near-Sun wind.

**What he did**: Badman, Bale, Martínez Oliveros, Panasenco, Velli et al. applied PFSS extrapolation to map PSP's magnetic footpoints back to the solar surface during Encounter 1. They used synoptic magnetograms from SDO/HMI as boundary conditions and traced field lines from PSP's position through the PFSS model to identify the photospheric source regions. The PFSS model assumes the magnetic field is current-free between the photosphere and a spherical source surface (typically at 2.5 R☉), beyond which the field is forced radial.

**The product**:
- Badman, Bale, Martínez Oliveros, Panasenco, Velli et al., "Magnetic Connectivity of the Ecliptic Plane within 0.5 au: Potential Field Source Surface Modeling of the First Parker Solar Probe Encounter," ApJS 246, 2020

**Primary results**:
- PSP Encounter 1 footpoints map to a small equatorial coronal hole and adjacent streamer boundary
- PFSS connectivity is consistent with the observed wind speed and composition (high-FIP bias pattern)
- The model successfully predicts the heliospheric magnetic field polarity observed by PSP
- Limitations: PFSS cannot capture dynamic reconnection that opens and closes field lines (requires global MHD)
- Established the methodology for all subsequent PSP connectivity studies

**Context**: Knowing where the solar wind comes from on the Sun is fundamental. PFSS is the simplest model for magnetic connectivity — it neglects currents and dynamics but provides a useful first-order mapping. Velli's group used it as a baseline, then compared against more sophisticated global MHD models. This paper established the connectivity framework that underpins all PSP source-region science.

**Citekeys**: badman2020
**Cross-refs**: VA706 (Solar Orbiter–PSP quadrature), VA704 (Alfvénic slow wind)

---

## VA708: Solar Orbiter Observations Identify Alfvénic Intervals and Their Coronal Source Regions in the Near-Sun Slow Wind

**Domain**: physics
**Claim**: Solar Orbiter's SWA (Solar Wind Analyzer) plasma suite detects Alfvénic intervals in the slow solar wind at heliocentric distances of 0.5–1 AU, and magnetic mapping reveals these intervals originate from coronal hole boundaries and active region edges — confirming the streamer-boundary interchange reconnection model for Alfvénic slow wind and extending the PSP near-Sun discovery to Solar Orbiter's broader spatial coverage.

**What he did**: D'Amicis, Raines, Benella, Velli and the SWA team analyzed Solar Orbiter plasma and magnetic field data to identify intervals of Alfvénic slow wind. They computed cross-helicity and residual energy for candidate intervals and mapped the source regions using PFSS and global MHD models. Velli provided the theoretical framework linking interchange reconnection at the source to the Alfvénic character observed in-situ.

**The product**:
- D'Amicis, Raines, Benella, Velli et al., "Alfvénic solar wind intervals observed by Solar Orbiter: Exploiting the capability of the SWA plasma suite and source region investigation," arXiv, 2025

**Primary results**:
- Solar Orbiter confirms Alfvénic slow wind extends beyond PSP's near-Sun region to at least 0.5 AU
- Source regions are consistently mapped to streamer boundaries and active region peripheries
- The Alfvénic intervals have properties (σ_c, residual energy, spectral index) intermediate between classic fast and slow wind
- The SWA plasma suite provides the multi-species measurements (protons, alphas, electrons) needed to distinguish Alfvénic slow wind from compositional slow wind
- Supports a unified model: interchange reconnection at open-closed boundaries launches Alfvénic fluctuations into both fast and slow wind channels

**Context**: This paper extends the Alfvénic slow wind paradigm (VA704) to Solar Orbiter's orbital range, providing a bridge between PSP's ultra-near-Sun measurements and the 1 AU observations from Wind and ACE. Solar Orbiter's ability to combine remote sensing (imaging the source) with in-situ measurements (characterizing the wind) makes it uniquely powerful for source-region science.

**Citekeys**: damicis2025
**Cross-refs**: VA704 (Alfvénic slow wind discovery), VA706 (PSP–SO quadrature), VA707 (connectivity mapping)

---

## VA709: Coronal Plumes and Fine-Scale Structure in High-Speed Solar Wind Streams — Early Constraints on Wind Origin Geometry

**Domain**: physics
**Claim**: Coronal plumes — the bright, linear density structures observed in polar coronal holes — are associated with fine-scale density fluctuations in the high-speed solar wind, suggesting that the fast wind's source is not a smooth, uniform coronal hole but a structured, filamentary network of open flux tubes rooted in the chromospheric network and plume/interplume regions.

**What he did**: Velli, Habbal & Esser analyzed coordinated observations of polar coronal holes from the SPARTAN 201-1 white-light coronagraph and ground-based instruments, measuring density fluctuations in plumes and interplume regions. They compared these with in-situ measurements of density microstructure in the high-speed wind from Ulysses. Velli developed the theoretical framework linking coronal fine structure to solar wind microstructure through flux-tube expansion geometry.

**The product**:
- Velli, Habbal & Esser, "Coronal Plumes and Fine Scale Structure in High Speed Solar Wind Streams," Space Science Reviews 70, 1994

**Primary results**:
- Coronal plumes carry enhanced density (factor 3–10 over background) but similar outflow speeds as interplume regions
- The density contrast of plumes decreases with heliocentric distance, merging into the wind by ~10 R☉
- Fine-scale density fluctuations in the wind (observed by Ulysses) are consistent with the remnants of coronal plume structure
- Suggests the fast wind originates from both plume and interplume regions, with different expansion factors
- The filamentary source geometry imposes a transverse scale on wind fluctuations that may seed the turbulent cascade

**Context**: This is one of Velli's early papers connecting coronal structure to wind properties. It established the idea that the solar wind's source is geometrically complex — a network of flux tubes rather than a uniform outflow. This geometric complexity is directly relevant to understanding why the wind shows structured variability (switchbacks, microstreams) and why the turbulent cascade may be seeded at particular transverse scales. The plume-wind connection has been dramatically confirmed by PSP's observations of switchback patches and their correlation with coronal structure.

**Citekeys**: velli1994
**Cross-refs**: VA001 (Alfvén waves in structured wind), VA707 (connectivity mapping)

---

## VA710: High-Amplitude Waves in the Expanding Solar Wind — Wave-Driven Acceleration Beyond WKB

**Domain**: physics
**Claim**: Large-amplitude Alfvén waves in the expanding solar wind evolve nonlinearly — departing from WKB predictions at amplitudes δB/B₀ ~ 0.3–1 — through parametric decay, steepening, and wave pressure effects that directly accelerate the solar wind, demonstrating that wave pressure (the ponderomotive force of Alfvén waves) contributes significantly to solar wind acceleration in the low corona where wave amplitudes are largest.

**What he did**: Schmidt, Velli & Grappin performed numerical simulations of finite-amplitude Alfvén waves propagating in a spherically expanding solar wind atmosphere with a background flow. They solved the full compressible MHD equations, including the wave pressure gradient force on the background wind. The simulations tracked wave amplitude evolution from the coronal base through the sonic point and beyond, including nonlinear effects (parametric decay, shock formation) that transfer wave momentum to the mean flow.

**The product**:
- Schmidt, Velli & Grappin, "High amplitude waves in the expanding solar wind plasma," 1995

**Primary results**:
- Wave pressure gradient force: −∇(⟨δB²⟩/8π) directly accelerates the solar wind plasma
- For wave amplitudes δv/v_A ~ 0.3–1 at the coronal base, wave pressure contributes 10–30% of the total wind acceleration below 10 R☉
- Parametric decay of the primary Alfvén wave generates compressive (sound) waves that steepen into shocks, providing an additional dissipation channel
- The wave-driven acceleration is strongest near the sonic point where the Alfvén speed gradient is steepest
- Nonlinear wave evolution modifies the WKB amplitude decay law, potentially explaining deviations from WKB observed by PSP

**Context**: This paper bridged the gap between linear wave theory (WKB) and the nonlinear reality of the near-Sun solar wind where δB/B₀ ~ 1. It showed that wave pressure is not a minor correction but a significant contributor to wind acceleration in the region where PSP now makes direct measurements. The wave-pressure mechanism is complementary to (and can operate alongside) the reflection-driven turbulence heating mechanism (VA002): wave pressure accelerates the flow directly, while turbulence dissipation heats the plasma (which also contributes to acceleration via the pressure gradient).

**Citekeys**: schmidt1995
**Cross-refs**: VA001 (Velli 1989, wave reflection), VA002 (Verdini & Velli 2007), VA702 (wave action conservation)

---

## VA711: Magnetic Imprints in the Solar Wind — The Corona Shapes the Wind's Large-Scale Magnetic Structure

**Domain**: physics
**Claim**: The large-scale structure of the interplanetary magnetic field — including sector boundaries, magnetic polarity inversions, and the heliospheric current sheet — directly imprints the coronal magnetic field topology into the solar wind, meaning that measurements of the wind's magnetic structure at any heliocentric distance encode information about the corona's magnetic geometry, including active regions, coronal holes, and streamer belt topology.

**What he did**: Velli authored a synthesis review connecting coronal magnetic field structure (as modeled by PFSS and global MHD) to the observed interplanetary magnetic field. He traced how the magnetic field topology transitions from the closed-field corona (dominated by active regions and streamers) to the open-field interplanetary medium (dominated by the Parker spiral). The review synthesizes results from Ulysses' high-latitude observations, PSP's near-Sun measurements, and Solar Orbiter's combined remote-sensing and in-situ data.

**The product**:
- Velli, "Magnetic imprints in the solar wind," Nature Astronomy 7, 2023

**Primary results**:
- The HCS warp and tilt are direct imprints of the photospheric magnetic field's longitudinal asymmetry
- Sector boundary thickness and structure encode information about reconnection at the coronal source
- The magnetic field expansion factor (super-radial vs. radial) controls wind speed, composition, and turbulence properties
- PSP's observations of sub-Alfvénic wind confirm the magnetic connectivity picture — the wind below the Alfvén surface is magnetically dominated
- Solar Orbiter's out-of-ecliptic observations will map the 3D magnetic structure of the heliosphere

**Context**: This is Velli's authoritative review synthesizing decades of work on the magnetic connection between corona and heliosphere. It frames the solar wind not just as a plasma outflow but as a magnetic structure — the Sun's magnetic field extended into interplanetary space. The "magnetic imprints" concept unifies coronal structure science with solar wind physics, providing the theoretical language for interpreting PSP and Solar Orbiter observations. The paper reflects Velli's central insight: the corona and wind are one connected system, and the magnetic field is the connecting thread.

**Citekeys**: velli2023
**Cross-refs**: VA705 (Bφ and angular momentum), VA707 (PFSS connectivity), VA709 (coronal plumes)

---

## VA712: Global Solar Wind Structure: PSP Reveals the Shear-Driven Transition from Coronal to Turbulent Wind

**Domain**: physics
**Claim**: The solar wind transitions from a magnetically dominated, shear-driven regime inside the Alfvén critical zone to an isotropically turbulent regime outside it — and this transition, driven by velocity shears between adjacent flux tubes originating from different coronal source regions, is the fundamental process establishing the large-scale structure of the heliospheric magnetic field and the turbulence properties observed at 1 AU.

**What he did**: Ruffolo, Matthaeus, Chhiber, Usmanov, Yang, Bandyopadhyay, Parashar, Goldstein, DeForest, Wan, Chasapis, Maruca, Velli & Kasper combined PSP observations from the first orbits with global 3D MHD simulations of the solar wind. They identified velocity shear layers in the near-Sun wind and showed these shears drive a transition from anisotropic (magnetically dominated) fluctuations to isotropic turbulence. Velli contributed the theoretical interpretation connecting coronal source geometry to the observed shear structure.

**The product**:
- Ruffolo, Matthaeus, Chhiber, Usmanov, Yang, Bandyopadhyay, Parashar, Goldstein, DeForest, Wan, Chasapis, Maruca, Velli & Kasper, "Shear-Driven Transition to Isotropically Turbulent Solar Wind Outside the Alfven Critical Zone," ApJ 892, 2020

**Primary results**:
- Inside the Alfvén critical zone: fluctuations are Alfvénic, anisotropic, and organized by the radial magnetic field
- Outside the Alfvén critical zone: velocity shears between adjacent streams drive the turbulence toward isotropy
- The shear-driven transition produces the mixed-propagation-direction turbulence (reduced σ_c) observed at 1 AU
- The transition distance depends on the strength and scale of the velocity shear, varying with solar wind stream structure
- PSP data confirm the transition occurs between 15–50 R☉ for typical stream interaction scales

**Context**: This paper addresses the fundamental question of how the "pristine" Alfvénic wind near the Sun transforms into the turbulent wind observed at Earth. Velli's contribution links the velocity shears to coronal source geometry: different coronal regions (holes, streamers, active regions) produce wind at different speeds, and these streams rub against each other as they expand. The shear-driven transition is a large-scale structural process that complements the reflection-driven cascade (which is a local, small-scale process) — both contribute to the radial evolution of turbulence.

**Citekeys**: ruffolo2020
**Cross-refs**: VA001 (Alfvén wave reflection), VA003 (expanding box model), VA703 (HCS turbulence)
