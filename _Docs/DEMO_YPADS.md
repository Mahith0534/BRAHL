# Demo yPAD templates

Ready-to-run sample suites in this end-user package — **Math**, **API_Petstore**, **UI_internet**, **BRAHL_Local**, **AI_foxyiz**, **AI_ux**.

| Suite | Folder | fStart | What it demos |
|-------|--------|--------|----------------|
| **Math** | `FoXYiZ/y/Math/` | `FoXYiZ/f/fStart/Math.json` | Offline **xMath** domain demo (add/sub/mul/div/power) — no browser |
| **API_Petstore** | `FoXYiZ/y/API_Petstore/` | `…/API_Petstore.json` | [Swagger Petstore](https://petstore.swagger.io/) xAPI: pet/store/user CRUD, security, smoke |
| **UI_internet** | `FoXYiZ/y/UI_internet/` | `…/UI_internet.json` | [the-internet](https://the-internet.herokuapp.com/) heavy UI: forms, alerts, DnD, upload, waits, tables |
| **BRAHL_Local** | `FoXYiZ/y/BRAHL_Local/` | `…/BRAHL_Local.json` | Desktop self-test of BRAHL UI (white pads; needs UI on port **8766**) |
| **AI_foxyiz** | `FoXYiZ/y/AI_foxyiz/` | `…/AI_foxyiz.json` | [foxyiz.com](https://foxyiz.com/) Generate→yPAD exams (`EX-FXZ-*`) + Manual scorecard · `_Docs/AI_tests.md` |
| **AI_ux** | `FoXYiZ/y/AI_ux/` | `…/AI_ux.json` | Portable chat/Generate template (D1–D3 domain anchors + chips + Manual) — retarget from FoXYiZ seed |
| **KonfigAI** | `FoXYiZ/y/KonfigAI/` | `…/KonfigAI.json` | [konfigai.com](https://www.konfigai.com/) public links, titles, form chrome |
| **LAEats** | `FoXYiZ/y/LAEats/` | `…/LAEats.json` | [laeats.base44.app](https://laeats.base44.app/) Fusion by Fire menu + Chef AI |

## Quick start (CLI)

From `FoXYiZ_User/`:

```powershell
$env:FOXYIZ_ROOT = "$PWD\FoXYiZ"

# API smoke — Petstore (also the bat default)
.\FoXYiZ\f\FoXYiZ.exe --config FoXYiZ\f\fStart\API_Petstore.json

# Math smoke (offline)
.\FoXYiZ\f\FoXYiZ.exe --config FoXYiZ\f\fStart\Math.json

# UI smoke — the-internet (needs Edge/Chrome)
.\FoXYiZ\f\FoXYiZ.exe --config FoXYiZ\f\fStart\UI_internet.json
```

Or start **BRAHL Local** and pick the project in the Arena:

```powershell
# Double-click "Run BRAHL.bat", or:
$env:FOXYIZ_ROOT = "$PWD\FoXYiZ"
$env:BRAHL_LOCAL = "1"
python BRAHL\run_local.py
```

Open http://127.0.0.1:8766/app → select **UI_internet** / **API_Petstore** / **Math** / **BRAHL_Local**.

## UI_internet tag map

| Tags | Showcase |
|------|----------|
| `Smoke` | Home + Form Auth happy path |
| `UI;Auth` | Login / logout / basic auth / negative |
| `UI;Forms` | Checkboxes, dropdown, inputs, forgot password |
| `UI;Alert` | JS Alert / Confirm / Prompt |
| `UI;DnD` / `Upload` / `Hover` / `Keys` / `Slider` | Interaction primitives |
| `UI;Wait;Dynamic` | Dynamic Loading + Dynamic Controls |
| `UI;Table` / `DOM` | Data tables, challenging DOM, large DOM |
| `Manual` | Frames / windows / shadow (not automated yet) |

Edit `FoXYiZ/f/fStart/UI_internet.json` → `"tags": ["Smoke","UI"]` (or narrow to `["UI","Alert"]`) before a demo run.

## Notes

- Engine cwd is **`FOXYIZ_ROOT`** (`FoXYiZ_User/FoXYiZ/`).
- Upload sample: `FoXYiZ/y/UI_internet/payloads/upload_demo.txt`.
- Petstore payloads: `FoXYiZ/y/API_Petstore/payloads/`.
- Suite generators (if present) live next to each suite; architects also keep them in **FoXYiZ__code**.
