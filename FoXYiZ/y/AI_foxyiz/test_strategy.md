# AI_foxyiz — test strategy

**Target:** https://foxyiz.com/ hero AI — *Describe task → Generate → AI builds yPAD*.

## Why this suite exists

Modern products ship chat / generate UIs whose outputs are **non-deterministic**. Classic exact asserts fail. This suite shows a FoXYiZ pattern for AI UX:

| Layer | What we assert | Run |
|-------|----------------|-----|
| **Chrome** | Page, textarea, chips, Generate control | `Smoke` Y |
| **Contract** | After Generate: `AI GENERATED YPAD`, `y1Plans.csv` / `y2Actions.csv`, domain keywords (`xUI` / `xAPI` / `xMath`), Download CTA | `AI;Gen` Y |
| **Dataset** | Same steps, different prompts via **y3 D1/D2/D3** (`type_prompt_custom`) | `Dataset` Y |
| **Quality** | Useful, on-brand, no invented ActionNames, multi-turn refine | `Manual` N |

## Varying the input dataset

Do **not** edit y2 for each prompt. Change data only:

1. Edit `y3Designs.csv` column **D1 / D2 / D3** on `type_prompt_custom`, **or**
2. Add files under `prompts/` and copy text into y3, **or**
3. Click different chips (`chip_login`, `chip_api`, `chip_math`, …).

Plans `PGen_Custom_D1|D2|D3` already point `DesignId` at each column.

## Soft evaluation (today)

Engine asserts are **substring / equality** via `xGetText` → `Expected` DataName. That is enough for:

- “A result panel appeared”
- “Output mentions yPAD CSV names”
- “Login prompt produced UI actions (`xUI`)”

Not enough for: “answer is excellent”. Those stay **Manual**.

## Optional next (engine / architect)

- `xContains` / regex soft match
- LLM-as-judge action (separate from Run policy — or Human-in-the-loop only)
- Capture raw model text to `z/` for offline scoring

## API note

Browser traffic uses `POST …/integration-endpoints/Core/InvokeLLM`. A future plan can mirror Petstore (`xPost` + payload) once auth/contract is documented; UI path is the demo default.

## How to run

```powershell
$env:FOXYIZ_ROOT = "$PWD\FoXYiZ"
.\FoXYiZ\f\FoXYiZ.exe --config FoXYiZ\f\fStart\AI_foxyiz.json
# widen tags in fStart to ["AI","Gen"] or ["Dataset"] for deeper runs
```

Needs network + Edge/Chrome. Generate waits ~20s per plan.
