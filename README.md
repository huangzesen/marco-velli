# Marco Velli Persona Skill

> **Unofficial.** Not endorsed by Marco Velli. Built from public sources for impersonation research and educational purposes.

A structured persona skill that enables AI agents to converse in the voice of **Marco Velli** — UCLA solar physicist, Parker Solar Probe Observatory Scientist, and one of the leading theorists in Alfvén-wave-driven solar wind turbulence, switchbacks, and the ideal tearing mode.

This repository is not written by Velli. It is a **research artifact** — a systematic distillation of his public persona (papers, lectures, interviews, biography) into a machine-readable knowledge base. It is the companion case study to the [impersonate-meta methodology](https://github.com/huangzesen/impersonate-meta).

---

## Ethical Notice

**Please read this before using the skill.**

- This repository is **unofficial** and **not endorsed by Marco Velli**.
- All content is derived from **publicly available sources**: published papers, conference recordings (AGU, ISSI, SOLARNET), interviews, and institutional biographies.
- The purpose is **impersonation research**, **educational use**, and **exploring the boundaries of AI persona engineering** — not identity fraud, academic dishonesty, or impersonation for gain.
- **If Marco Velli or his representatives request removal of this repository, we will comply promptly.**
- **Users are responsible for:**
  - Never passing AI-generated output as Velli's own words
  - Never using this skill to endorse or oppose any position on Velli's behalf
  - Never using this skill in academic fraud (paper authorship, peer review impersonation)
  - Clearly labeling any AI-generated text as such when it uses this persona

---

## What's Inside

This repository follows the [LingTai recipe bundle format](https://github.com/huangzesen/lingtai/blob/main/tui/internal/preset/skills/lingtai-recipe/references/recipe-format.md): a `.recipe/` dotfolder with the recipe manifest, plus a sibling library folder named `persona-marco-velli` containing the skill itself.

```
marco-velli/                                  # this repo (recipe bundle root)
├── .recipe/
│   └── recipe.json                           # bundle manifest (id, name, description, library_name)
├── README.md                                 # you are here
└── persona-marco-velli/                      # the library folder
    └── persona-marco-velli/                  # the skill (one library, one skill)
        ├── SKILL.md                          # entry point — loads the whole persona
        ├── profile/                          # who Velli is
        │   ├── SKILL.md
        │   ├── biography.md                  #   education, career, honors
        │   ├── voice.md                      #   speech patterns, humor, storytelling
        │   ├── values.md                     #   scientific philosophy, priorities
        │   └── relationships.md              #   collaborator network, mentors, students
        ├── arguments/                        # what Velli knows and believes
        │   ├── SKILL.md
        │   ├── physics/                      #   7 subdomains of solar physics
        │   │   ├── alfven-waves.md           #   reflection-driven turbulence, 1/f spectrum
        │   │   ├── turbulence.md             #   MHD turbulence, reduced MHD, intermittency
        │   │   ├── switchbacks.md            #   switchback origins, expansion-driven model
        │   │   ├── coronal-heating.md        #   wave-turbulence heating models
        │   │   ├── reconnection.md           #   ideal tearing mode, fast reconnection
        │   │   ├── psp-observations.md       #   Parker Solar Probe discoveries
        │   │   └── solar-wind.md             #   solar wind acceleration, large-scale structure
        │   ├── methodology/                  #   how Velli thinks
        │   │   └── thinking-methods.md       #   argumentation style, cognitive heuristics
        │   └── culture/                      #   broader scientific culture
        │       └── scientific-culture.md     #   Velli on the field, mentoring, collaboration
        ├── methods/                          # distilled method cards
        │   └── SKILL.md                      #   10 reusable thinking patterns
        ├── scripts/
        │   └── generate_bib.py
        └── velli.bib                         # 338 entries — Velli's core works + field context
```

### Key Numbers

| Dimension | Count |
|-----------|-------|
| Physics arguments (VA claims) | 105 structured entries across 7 domains |
| Method cards (VM) | 10 reusable thinking patterns |
| Bibliography entries | 338 (77 directly cited, the rest as reference pool) |
| Profile sections | 4 (biography, voice, values, relationships) |
| Input tokens (estimated) | ~90,000 for the full skill bundle |

---

## How to Use

### As a LingTai recipe

If you use the [LingTai](https://github.com/huangzesen/lingtai) agent platform, clone this repo into your agora directory and select it from the TUI's recipe picker:

```bash
# 1. Clone into your agora's recipes directory
mkdir -p ~/lingtai-agora/recipes
git clone https://github.com/huangzesen/marco-velli ~/lingtai-agora/recipes/marco-velli

# 2. Start a new LingTai project and pick "marco-velli" in the recipe wizard
mkdir ~/work/my-velli-network && cd ~/work/my-velli-network
lingtai-tui
# In the recipe-picker step, choose "marco-velli (Marco Velli (Persona))"
```

The TUI will copy the bundle into your project, register `persona-marco-velli/` as a library, and make every agent in your network Velli-aware on first launch.

### As a framework-agnostic skill

Any AI framework that reads `SKILL.md` (Claude Code, Cursor, custom projects) can load this directly. Point your framework at `persona-marco-velli/persona-marco-velli/` (the skill folder, two levels deep) and reference its `SKILL.md`:

```
persona-marco-velli/persona-marco-velli/SKILL.md
```

Sample prompts once loaded:

- *"What's Velli's view on reflection-driven turbulence?"*
- *"How does the ideal tearing model differ from standard Sweet-Parker?"*
- *"Tell me about the Parker Solar Probe switchback discoveries."*

You can also fork and pick individual argument files (`persona-marco-velli/persona-marco-velli/arguments/physics/switchbacks.md`) for narrower contexts.

### Quick Start Prompt

```
Load the persona-marco-velli skill, then ask:
"What's your take on reflection-driven turbulence, and how does it connect to the 1/f spectrum in the solar wind?"
```

---

## Limitations & Known Failure Modes

This skill was developed and stress-tested through the [impersonate-meta methodology](https://github.com/huangzesen/impersonate-meta). These are the known boundaries:

| Issue | Status |
|-------|--------|
| **Values/philosophy** | Heavily dependent on a single ISSI interview (2021). May be fragile — Velli's public philosophy is less documented than his physics. |
| **Post-2026 knowledge** | None. The skill only knows publications up to early 2026. |
| **Paper title hallucination** | The AI **will** fabricate paper titles and citation details if asked to generate references. Do not use for bibliography generation — use the actual `velli.bib`. |
| **Private conversation** | The skill is tuned for **public-register impersonation** (lecture style, interview tone). It does not model private conversation, humor between friends, or off-the-record opinions. |
| **Single-source bias** | Where public sources are sparse (e.g., early career, teaching philosophy), the skill extrapolates from the closest available data. Treat those sections as plausible reconstructions, not facts. |
| **Self-contradiction** | Like any real academic, Velli's views have evolved over 40 years. The skill may present conflicting positions from different eras without flagging the evolution. |

---

## Methodology

This persona was generated using the [impersonate-meta](https://github.com/huangzesen/impersonate-meta) methodology — a reusable framework for distilling any academic/public figure into a structured persona skill. The process involved:

1. **Research phase**: Google Scholar, NASA ADS, AGU/ISSI lecture recordings, interviews, institutional profiles
2. **Avatar orchestration**: 6 specialized LLM agents (Alfvén waves, PSP mission, switchbacks, coronal heating, reconnection, voice analysis) working in parallel
3. **VA claim extraction**: 6,889 lines of structured arguments using a 7-field schema (Claim / What he did / The product / Primary results / Context / Citekeys / Cross-refs)
4. **Quality assurance**: Independent human review, citekey cross-validation, semantic drift detection
5. **Method card distillation**: 10 reusable thinking patterns extracted from 105 VA entries

See the [impersonate-meta repository](https://github.com/huangzesen/impersonate-meta) for the full methodology, templates, scripts, and failure catalog.

---

## License

MIT — feel free to use, modify, and distribute. See the [LICENSE](LICENSE) file (or the LingTai ecosystem default).

---

## Related

- [impersonate-meta](https://github.com/huangzesen/impersonate-meta) — The methodology used to build this persona
- [LingTai](https://github.com/huangzesen/lingtai) — The multi-agent orchestration platform (TUI + portal)
- Marco Velli at UCLA — [EPSS faculty page](https://epss.ucla.edu/person/marco-velli/)
