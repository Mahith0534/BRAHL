---
name: foxyiz
description: >-
  FoXYiZ packaged engine f(x,y)=z. Use when running FoXYiZ.exe, authoring yPAD
  (y1/y2/y3), editing fStart, reading z/ or zlogs, using _pyUtils helpers, or
  explaining package layout (_internal, xCapa). Trigger on FoXYiZ, foxyiz, yPAD,
  fStart, zResults, zDash, zlogs, xCapa, FoXYiZ.exe, _pyUtils.
---

# FoXYiZ — engine & package

Automation engine for this distributable. **No** shippable `fEngine2.py` / `xActions.py` — Run is **`FoXYiZ\f\FoXYiZ.exe`** (paths below are relative to **`FOXYIZ_ROOT`**).

Spellings: **FoXYiZ** · **yPAD** · **fStart** · **zlogs**.

In the end-user zip, **`FOXYIZ_ROOT` = `FoXYiZ_User\FoXYiZ`** (not the zip root). `Run FoXYiZ.bat` sets this.

## Skill

| Field | Value |
|-------|-------|
| **Skill id** | `foxyiz` |
| **Primary users** | Operators, suite authors, architects (rebuild), agents editing yPAD only |
| **Apply when** | Running the exe; authoring suites; reading `z/`; using `_pyUtils`; ship/layout questions |
| **Do not use for** | Arena UI product surface → `BRAHL/`; lifecycle triage policy → [BRAHL.md](BRAHL.md) |
| **Related skills** | `brahl` (lifecycle) |
| **Triggers** | FoXYiZ, foxyiz, yPAD, fStart, zResults, zDash, zlogs, xCapa, `_internal`, `_pyUtils` |

**Agent default:** edit **yPAD + fStart + `_Docs`** only. Do not modify `f\_internal\` or the exe unless the user explicitly asks.

---

## Formula

```
f(x, y) = z
```

| Folder | Role |
|--------|------|
| **f/** | `FoXYiZ.exe` + **`_internal/` (required)** + `fStart/` + optional `.env` |
| **x/** | `xCapa.csv` — ActionName catalog for y2 |
| **y/** | Editable yPAD suites |
| **z/** | Results (`*_zResults.csv`, `*_zDash.html`, `zlogs.txt`, reports) |
| **_pyUtils/** | Only editable Python in the package (Analyze helpers; needs Python) |
| **_Docs/** | BRAHL · FoXYiZ · Test_Coverage · DEMO_YPADS (at FoXYiZ_User root) |

---

## `f/` layout (keep it lean)

| Path | Role |
|------|------|
| `FoXYiZ.exe` + `_internal/` | Frozen engine — do not edit |
| `fStart/*.json` | Which suite + tags to run |
| `.env.example` → `.env` | **Optional BRAHL AI only** (not required for Run) |
| `.env.integrations.example` | Optional Gmail/LinkedIn/etc. when those plans are on |
| `README.txt` | One-screen map of this folder |

### Optional AI (BRAHL helpers)

Copy `f/.env.example` → `f/.env`, then **restart BRAHL**.

| Mode | Settings |
|------|----------|
| **Cloud OpenAI (BYOK)** | `OPENAI_API_KEY=sk-…` · `OPENAI_MODEL=gpt-4o-mini` |
| **Local Ollama (free)** | `OPENAI_API_KEY=ollama` · `OPENAI_BASE_URL=http://127.0.0.1:11434/v1` · `OPENAI_MODEL=llama3.2` |

AI assists **Build / Analyze / Heal chat** in the Arena. **Run / Loop / Verify never call an LLM** — see [BRAHL.md](BRAHL.md).

Gmail, LinkedIn, Google OAuth are **not** part of “turn AI on.” They live in `.env.integrations.example` only if you enable those suite plans.

---

## Quick start

From the **FoXYiZ_User** zip root:

```powershell
$env:FOXYIZ_ROOT = "$PWD\FoXYiZ"
.\FoXYiZ\f\FoXYiZ.exe --config FoXYiZ\f\fStart\Math.json
```

Double-click **`Run FoXYiZ.bat`** → `f\fStart\default.json` (API_Petstore Smoke).

Or from **`FOXYIZ_ROOT`** (`FoXYiZ\`):

```powershell
.\f\FoXYiZ.exe --config f\fStart\Math.json
```

Results: `z\<timestamp>_<suite>\` including **`zlogs.txt`**. Flat index: `z\zlogs.txt`.

### fStart (minimal)

```json
{
  "configs": ["y/Math/Math.json"],
  "thread_count": 1,
  "timeout": 6,
  "headless": true,
  "debug": false,
  "tags": ["Smoke"],
  "capture": { "image": "on_fail", "video": "off", "video_fps": 2, "subdir": "" }
}
```

### Add a suite

1. Copy `y\Math\` → `y\<mysuite>\`
2. Edit y1 / y2 / y3 + `<mysuite>.json`
3. Add `f\fStart\<mysuite>.json`
4. Run with `--config f\fStart\<mysuite>.json`

Use **`x\xCapa.csv`** for valid `ActionType` / `ActionName` pairs.

### Modular reuse (scale past ~100 plans)

Keep the three core sheets, then **attach** shared modules via `input_files` arrays (already supported by FoXYiZ + BRAHL):

| File | Role |
|------|------|
| `y1Plans.csv` | Plan catalog (always one primary sheet is fine) |
| `y2Actions.csv` | Suite-specific steps |
| `y2Actions_reusable.csv` | Shared `PReuse_*` / common flows |
| `y3Designs.csv` | Suite-specific DataNames |
| `y3Designs_reusable.csv` | Shared vars — especially **`vbrowser`** |

```json
"input_files": {
  "yPlans":   ["y/MySuite/y1Plans.csv"],
  "yActions": ["y/MySuite/y2Actions_reusable.csv", "y/MySuite/y2Actions.csv"],
  "yDesigns": ["y/MySuite/y3Designs_reusable.csv", "y/MySuite/y3Designs.csv"]
}
```

**Rules:** do not duplicate `PlanId` / `DataName` across merged files. Never hard-code the browser — use `xOpenBrowser,vbrowser` with `UI,vbrowser,edge,edge,edge` in `y3Designs_reusable.csv`. Templates: `y/_reusable/`. fStart still points at the suite JSON (one fStart per suite); multi-CSV lives in that suite config.

**Also attach from fStart** (optional overlay — BRAHL folds this into a runtime suite JSON before Run):

```json
{
  "configs": ["y/MySuite/MySuite.json"],
  "attach": {
    "yActions": ["y/_reusable/y2Actions_reusable.csv"],
    "yDesigns": ["y/_reusable/y3Designs_reusable.csv"]
  },
  "tags": ["Smoke"]
}
```

Prefer listing reusables in the suite JSON for day-to-day authorship; use fStart `attach` when sharing package-level modules across suites without editing each suite file.

BRAHL gate/journey filters always keep `*_reusable*` action/plan files so shared modules are not dropped.---

## Ship layout (was DISTRIBUTION)

**You need both** `f\FoXYiZ.exe` and `f\_internal\` (PyInstaller onedir). Shipping the exe alone will not start.

Zip the whole `FoXYiZ_User` folder:

```text
FoXYiZ_User\
  Run FoXYiZ.bat
  Run BRAHL Local.bat
  FoXYiZ\                 ← FOXYIZ_ROOT
    f\FoXYiZ.exe
    f\_internal\          ← required
    f\fStart\
    x\
    y\
    z\
    _pyUtils\             ← optional Analyze helpers
  BRAHL\
  _Docs\
  README.txt
  VERSION.json
```

**Not shipped as source:** `fEngine2.py`, `xActions.py` (frozen inside `_internal` only).

### `_pyUtils` (editable Python only)

| Script | Role |
|--------|------|
| `_paths.py` | Package paths |
| `cleaner.py` | Archive old `z/` (dry-run default) |
| `yVisualizer.py` | yPAD map HTML |
| `zDefects.py` | Failure rollup HTML |
| `zBatchDash.py` | Multi-run batch dashboard |

```powershell
python _pyUtils\cleaner.py
python _pyUtils\yVisualizer.py
python _pyUtils\zDefects.py
python _pyUtils\zBatchDash.py --name mybatch --since 20260721
```

### Glossary

| Term | Meaning |
|------|---------|
| **yPAD** | y1Plans · y2Actions · y3Designs (+ optional `*_reusable`) |
| **fStart** | `f/fStart/{suite}.json` |
| **zlogs.txt** | Per-run console transcript (+ flat `z/zlogs.txt`) |
| **brawl** | Full BRAHL cycle to Verify |
| **smoke** / **deep** | Shell only vs expanded tags |

### Coverage (what to author)

yPAD Tags and Expected should cover journeys, auth, negatives, security/PII—not only happy path. For “should not see,” assert denied/empty/absent text when stable; otherwise `Run=N` Hunter. Full matrix + **AI scoring → Go/No-Go**: [Test_Coverage.md](Test_Coverage.md).

### Rebuild (architects)

From KK2 (source tree is **FoXYiZ__code**):

```powershell
powershell -ExecutionPolicy Bypass -File FoXYiZ__code\packaging\build_exe.ps1 -Version 1.0.0
```

Produces **FoXYiZ_User/** with `FoXYiZ\f\FoXYiZ.exe` for end users. Do not ship engine source there.

---

## Do not

- Delete or move `f\_internal\` without the exe  
- Ship only `FoXYiZ.exe`  
- Put secrets in `y3Designs.csv`  

## See also

- [Vision.md](Vision.md) — QA on Air vision (marketplace + desktop)  
- [BRAHL.md](BRAHL.md) — lifecycle, failure classes, report  
- [Test_Coverage.md](Test_Coverage.md) — coverage pillars · AI eval · Go/No-Go  
- [DEMO_YPADS.md](DEMO_YPADS.md) — demo suites  
- [README.md](README.md) — doc index + skill map  
