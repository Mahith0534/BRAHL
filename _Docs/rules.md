# Agent & team rules (KK)

Standing conventions for humans and AI working in this workspace.

Related: [terminology.md](./terminology.md) · [BRAHL_PROMPT.md](./BRAHL_PROMPT.md) · [AI_GUARDRAILS.md](./AI_GUARDRAILS.md) · **[AI_tests.md](./AI_tests.md)** · **[AI_prompts.md](./AI_prompts.md)** · [Test_Coverage.md](./Test_Coverage.md) · [../qoa_web/MEMORY.md](../qoa_web/MEMORY.md)

## Vocabulary first

Always spell **BRAHL** and **FoXYiZ**. Use **brawled** for a completed BRAHL cycle. Full glossary: [terminology.md](./terminology.md).

## Explore apps with Playwright MCP — no new Python

**Hard rule:** Do **not** write new Python programs, generators, `_tmp_*.py`, `_build_*.py`, `_expand_*.py`, or one-off scrapers to research apps or author suites. Those become cleanup debt.

**Do this instead:**
1. Research the app with **Playwright MCP** (`browser_navigate`, `browser_snapshot`, `browser_click`, …) or the live UI.
2. Build / heal **yPAD only** — `y/<suite>/y1Plans.csv`, `y2Actions.csv`, `y3Designs.csv`, optional `*_reusable.csv`, suite `.json`, `f/fStart/*.json`, and slim `test_strategy.md`.
3. Register BRAHL projects via **BRAHL Arena / API** when needed — not by scripting `projects.json` from a throwaway `.py`.

When a suite grows large, split common steps/data into `y2Actions_reusable.csv` / `y3Designs_reusable.csv` and list them in the suite JSON `input_files` arrays. Use DataName **`vbrowser`** (not hard-coded `edge`). See `_Docs/FoXYiZ.md` · Modular reuse.
Existing package utilities (`_pyUtils/cleaner.py`, scaffold already in the product, etc.) are fine to **run**. Do **not** invent new ones for a chat task.

## Default edit scope

| Touch | Avoid unless asked |
|-------|--------------------|
| `qoa_web/web/*`, `qoa_web/api/*` | `FoXYiZ/f/fEngine2.py`, `FoXYiZ/x/xActions.py` |
| `FoXYiZ/y/<suite>/*.csv`, `*.json` | Dumping `FoXYiZ/z/**` into chat |
| `FoXYiZ/f/fStart/{suite}.json` | `archive/**`, `f/fStart/archive/**` |
| `Docs/*.md` (keep slim) | Re-expanding retired docs |

## BRAHL lifecycle

**Build → Run → Analyze → Heal → Loop → Verify → BRAHL report.**  
Run/Loop = FoXYiZ only (no LLM). Heal in yPAD first; never weaken A1 assertions.

## Naming & layout

- Engine lives in **`KK/FoXYiZ/{f,x,y,z,pyUtils}`**. From `KK/`:  
  `python FoXYiZ\f\fEngine2.py --config f/fStart/Math.json`
- UI: `python qoa_web/run_local.py` → http://127.0.0.1:8765

## Suite habits

- Unique `PReuse_<Suite>_…` IDs; `Run=N` for pure setup reuses.
- Tags semicolon-separated; filter via fStart `"tags"`.
- After `xReuse`, parent plan must navigate (base_url / profile_url).
- Assert **visible live UI** text; **snapshot yPAD before every major expansion** (`y/<suite>/versions/`).
- Lean day smoke: `y/Math/`. Product deep example: `y/thoughtstream/` + `thoughtstream_deep.json`.

## End of session

```powershell
python FoXYiZ\_pyUtils\cleaner.py --apply
python FoXYiZ\_pyUtils\cleaner.py --apply --ypad-versions      # older version CSVs → archive (keep 2)
python FoXYiZ\_pyUtils\cleaner.py --apply --suite-generators   # y/<suite>/_gen_*.py → archive
```

Optional: `--runtime-scratch` after temporary heal fStarts. Safe to delete `archive/cleanup/` anytime. Session log: [todaysummary.md](../todaysummary.md).
