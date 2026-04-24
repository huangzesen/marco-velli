---
name: velli-arguments
description: Index and search guide for Marco Velli's academic arguments across physics, methodology, culture, and pedagogy.
version: 0.1.0-m1
---

# Marco Velli — Arguments Index

## What This Contains

~100-200 discrete academic arguments, each a complete record with:
- Specific claim (not vague)
- What Velli did (observations, derivations, simulations)
- The product (paper/lecture/discovery)
- Primary results (numbers, scaling laws)
- Context (significance, what it replaced/opened)
- Citekeys (traceable to `velli.bib`)
- Cross-references to related arguments

## Domain Structure

### `physics/` (~80-120 arguments)

| File | Domain | Target Args | Key Periods |
|------|--------|-------------|-------------|
| `alfven-waves.md` | Alfvén wave propagation, reflection, parametric instability | 15-20 | 1989–2026 |
| `turbulence.md` | Reflection-driven turbulence, 1/f spectrum, reduced MHD | 15-20 | 1989–2026 |
| `reconnection.md` | Ideal tearing mode, current sheet collapse, fast reconnection | 10-15 | 2013–2026 |
| `switchbacks.md` | Origin theories, radial evolution, PSP observations | 15-20 | 2018–2026 |
| `coronal-heating.md` | Wave-turbulence models, RMHD simulations, open/closed fields | 10-15 | 1996–2026 |
| `solar-wind.md` | Wind acceleration, expansion effects, global models | 10-15 | 1993–2026 |
| `psp-observations.md` | Mission results, Encounter discoveries, instrument science | 10-15 | 2018–2026 |

### `methodology/` (~15-25 arguments)
- Gradient-first thinking
- Finding critical points (ideal tearing as exemplar)
- Theory-driven but welcomes being overturned
- Parameterizing uncertainty
- Building the right picture at human scale first

### `culture/` (~10-20 arguments)
- Compartmentalization of research programs
- Team science philosophy
- Attitude toward AI and computational methods
- Italian scientific culture influence

### `pedagogy/` (~10-20 arguments)
- Textbook (Living Reviews in Solar Physics)
- Teaching philosophy
- Student mentoring approach
- Lecture style (historical narrative, big picture)

## Search Guide

### By Topic
Each argument has a **Domain tag** (physics/methodology/culture/pedagogy) 
and **Citekeys** linking to `velli.bib`. Arguments are cross-referenced by ID 
(VA001, VA002...).

### By Paper
To find arguments from a specific paper, search citekeys:
```
grep -l "velli1989" physics/*.md
```

### By Concept
Each physics file groups arguments by conceptual thread, 
not chronologically. Use the file-level headers for navigation.

## Claim ID Convention

- **VA001–VA099**: Physics arguments
- **VA100–VA149**: Methodology arguments
- **VA150–VA179**: Culture arguments
- **VA180–VA199**: Pedagogy arguments

## Status

All argument files pending — will be completed in:
- **M3**: 20 exemplar arguments (5 per domain)
- **M4**: Full physics arguments (80-120)
- **M5**: methodology/culture/pedagogy (35-65)

This index will be updated after each milestone.
