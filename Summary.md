# FoXYiZ_User — restart handoff

**Open this folder alone in Cursor** (`FoXYiZ_User/`). This file is the context to continue work.

**Version:** 1.0.1 (`VERSION.json`)  
**Last major push:** 2026-07-25 → 2026-07-27 (packaging + BRAHL UI + BRAHL_Local white pads)  
**Spellings:** FoXYiZ · BRAHL · yPAD · BRAHL_Local (suite name)

---

## What this package is

End-user distributable for **FoXYiZ** + optional **BRAHL** desktop UI.

| Symbol | Meaning |
|--------|---------|
| **f** | Frozen engine — `FoXYiZ.exe` (no `fEngine2.py` / `xActions.py` here) |
| **x** | Action catalog reference (`xCapa.csv` only) |
| **y** | yPAD suites (Plans / Actions / Designs CSVs) — **editable** |
| **z** | Run results (dashboards, CSV, screenshots) |

Formula: **f(x, y) = z**

Architects keep engine source in a sibling tree (`FoXYiZ__code`) and publish a new User zip when the exe changes. **Inside this folder you only edit yPAD / fStart / helpers / docs / BRAHL UI.**

---

## Current layout (important)

Three main folders:

```
FoXYiZ_User/                 ← open this as Cursor root
  Summary.md                 ← this file
  README.txt                 ← end-user quick start
  VERSION.json
  Run FoXYiZ.bat             ← sets FOXYIZ_ROOT → FoXYiZ\; default = API_Petstore
  Run BRAHL.bat              ← desktop UI (Run BRAHL Local.bat = alias)
  _Docs/                     ← Vision.md (canonical), FoXYiZ.md, BRAHL.md, DEMO_YPADS.md
  BRAHL/                     ← desktop Arena UI (Python, port 8766)
  FoXYiZ/                    ← engine + yPAD package  ★ FOXYIZ_ROOT
    f/
      FoXYiZ.exe
      _internal/
      fStart/                ← Math, API_Petstore, UI_internet, BRAHL_Local, default
      .env.example
    x/                       ← xCapa.csv + README
    y/                       ← suites (see below)
    z/                       ← results
    _pyUtils/                ← optional helpers
```

**Set / assume:**

```text
FOXYIZ_ROOT = <this folder>/FoXYiZ
```

Not the `FoXYiZ_User` root. Root bats already set this.

### Run

```powershell
cd <FoXYiZ_User>
# bats: "Run FoXYiZ.bat" / "Run BRAHL.bat"
$env:FOXYIZ_ROOT = "$PWD\FoXYiZ"
.\FoXYiZ\f\FoXYiZ.exe --config FoXYiZ\f\fStart\default.json
# or
.\FoXYiZ\f\FoXYiZ.exe --config FoXYiZ\f\fStart\BRAHL_Local.json

$env:BRAHL_LOCAL = "1"
$env:QOA_DESKTOP = "1"
python BRAHL\run_local.py
# → http://127.0.0.1:8766/app
```

`BRAHL/api/paths.py` / `run_local.py` auto-detect sibling `FoXYiZ/` when `FOXYIZ_ROOT` is unset; setting it explicitly is safer.

---

## Suites under `FoXYiZ/y/`

| Suite | Role | fStart |
|-------|------|--------|
| **Math** | Offline xMath domain demo | `FoXYiZ/f/fStart/Math.json` |
| **API_Petstore** | Online Swagger Petstore API demo (default smoke) | `…/API_Petstore.json` |
| **UI_internet** | the-internet.herokuapp.com UI demo | `…/UI_internet.json` |
| **BRAHL_Local** | Desktop self-test of BRAHL UI (white pads) | `…/BRAHL_Local.json` |
| **KonfigAI** | Public site konfigai.com (links / titles / forms) | `FoXYiZ/f/fStart/KonfigAI.json` (+ `_Link` `_Title` `_Form`) |
| **AI_foxyiz** | foxyiz.com AI Generate (prompt → yPAD) | `FoXYiZ/f/fStart/AI_foxyiz.json` |
| **AI_ux** | Portable AI chatbot UX template | `…/AI_ux.json` |

Docs: `_Docs/DEMO_YPADS.md`, per-suite `test_plan.md` / `test_strategy.md` where present.

### BRAHL projects

`BRAHL/data/projects.json` seeds include **KonfigAI**, **AI_foxyiz**, **AI_ux**, demos, **BRAHL_Local**.

---

## How to run (cheat sheet)

| Goal | Command |
|------|---------|
| Petstore API smoke | `FoXYiZ\f\FoXYiZ.exe --config FoXYiZ\f\fStart\API_Petstore.json` |
| Math offline | `…\Math.json` |
| UI internet | `…\UI_internet.json` |
| BRAHL_Local self-test | `…\BRAHL_Local.json` (needs BRAHL on **8766** for UI plans) |
| AI_foxyiz (foxyiz.com) | `…\AI_foxyiz.json` (network; Smoke = chrome only) |
| AI_ux template | `…\AI_ux.json` |
| Arena UI | `python BRAHL\run_local.py` → http://127.0.0.1:8766/app |

Needs: **Python** (BRAHL server), **Edge/Chrome** (UI suites). Optional AI: copy `FoXYiZ/f/.env.example` → `.env` (OpenAI **or** local Ollama) — Run never needs a key.

---

## Major changes (last ~2 days) — resume from here

### Packaging
- End-user package vs architect `FoXYiZ__code` (frozen exe only in User)
- Curated demos; stripped API unit tests / heavy product docs from BRAHL ship
- Default fStart → API_Petstore; Math rewritten as **offline xMath** (no example.com UI fake)

### BRAHL Local UI (ThoughtStream-driven)
- Phase hints: **Tests (/y)** · **Results (/z)** · **Heal Tests (/y)** · **Verify /y → /z** · **Go / No-Go**
- Click **/y** or **/z** → `POST /api/reveal-folder` opens Explorer (toast shows path)
- Build: **Rebuild** (collapsible); no FoXYiZ / latest-verify clutter under title on desktop
- Tagline **FoXYiZ** opens docs (general `_Docs` + project `.md`)
- Desktop hides: Advanced, AI chat, Team workspace

### BRAHL_Local white pads + verify
- Suite regenerated for desktop user cases (`y/BRAHL_Local/`, generator `_gen_desktop_whitepads.py` in architect tree if present)
- Last green verify: **48/48 Pass** — `FoXYiZ/z/20260726_031539_BRAHL_Local/` (+ `brahl_report.md` if still present)
- ThoughtStream source: https://jusdone.base44.app/view/6a65db11d1301b5daeb45249

---

## What you may edit vs not

| Edit freely | Do not edit |
|-------------|-------------|
| `FoXYiZ/y/**` yPAD CSVs + suite `.md` | `FoXYiZ/f/FoXYiZ.exe` + `_internal/` |
| `FoXYiZ/f/fStart/*.json` | Expect architects to ship a new User zip for engine/xActions changes |
| `BRAHL/web/**`, `BRAHL/api/**` (UI/API) | |
| `_Docs/**`, `_pyUtils/**` | |
| `FoXYiZ/z/**` (results; safe to clean) | |

---

## Known issues / next work

1. ~~Path drift (bats / stray root `f/`)~~ — **done** (nested `FoXYiZ/`; bats + README/`_Docs` aligned 2026-07-27).
2. **Restart BRAHL Local after API changes** — Python loads routes at process start (`/api/reveal-folder` needs a live server with current `main.py`).
3. **Workspace chip** — bind the *app under test*, not the FoXYiZ tool folder; yPAD still lives under `FOXYIZ_ROOT/y`.
4. **Final polish** — BRAHL Local UI cleanup touches; optional re-zip + bump `VERSION.json` when shipping.
5. Optional: flatten tree later so `FOXYIZ_ROOT` = zip root (not required; nested is ship truth today).

---

## Agent / Cursor tips (this folder only)

- Port **8766** = BRAHL Local; do not assume KK2 or `FoXYiZ__code` exist in this workspace.
- Engine cwd / paths are relative to **`FOXYIZ_ROOT`** (`…/FoXYiZ`).
- UI source of truth in this package: `BRAHL/web/` (`index.html`, `app.js`, `styles.css`).
- Self-test suite: `FoXYiZ/y/BRAHL_Local/` + `FoXYiZ/f/fStart/BRAHL_Local.json`.
- When user pastes a ThoughtStream URL, treat it as product feedback and implement in `BRAHL/web` then sync behavior with yPAD if needed.

---

## Quick health check

```powershell
cd <FoXYiZ_User>
$env:FOXYIZ_ROOT = "$PWD\FoXYiZ"
Test-Path .\FoXYiZ\f\FoXYiZ.exe          # True
python BRAHL\run_local.py          # then browser /api/health
.\FoXYiZ\f\FoXYiZ.exe --config .\FoXYiZ\f\fStart\API_Petstore.json
```

**Last known BRAHL_Local self-test:** GO — 48/48 (2026-07-26).
