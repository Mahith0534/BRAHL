# Test strategy — varkasa

## Purpose

Deep Regression Testing Plan for varkasa App

## App under test

https://varkasa.com/

## Approach

- **Automated** — FoXYiZ runs yPAD plans marked `Run=Y` (engine only; no LLM required).
- **Manual** — QA Hunters cover `Run=N` UX, real-device, and exploratory gaps.
- **AI (optional)** — assists Build / Analyze / Heal when AI is on; never replaces FoXYiZ Run.

## Coverage posture

- **23** automated · **7** manual · **30** plans in scope (from yPAD / BRAHL draft).

## BRAHL QA agent cycle

1. **Build** — strategy, test plan, and yPAD (plans · steps · data).
2. **Run** — FoXYiZ executes automated plans.
3. **Analyze** — failures from `z/` (Input · Expected · Output).
4. **Heal** — fix yPAD locators / steps / data.
5. **Loop** — retry fails (up to 3×) · optional full Verify.
6. **BRAHL** — Go/No-Go launch report.

_Source: `y/varkasa/test_strategy.md` (synthesized if the file was missing)._