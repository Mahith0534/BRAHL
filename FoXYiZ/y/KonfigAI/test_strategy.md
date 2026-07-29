# KonfigAI — public site test strategy

**Target:** [https://www.konfigai.com/](https://www.konfigai.com/)

## Scope

| Tag | What | Run |
|-----|------|-----|
| `Smoke` | Home H1, Request Demo, Solutions | Y |
| `Link` | Every public HTML URL loads + H1 contract | Y |
| `Title` | `document.title` matches **correct** product name | Y (expect A1 fails) |
| `Form` | Request Demo + Contact field chrome (no submit) | Y |
| `Nav` / `Footer` | Product + legal destinations | Y |
| `Manual` | Social externals, form submit HITL, a11y, title debt | N |

## Known defects (pre-BRAHL crawl 2026-07-28)

| Page | Observed `<title>` | Expected (suite) |
|------|--------------------|------------------|
| form-builder / workflow-builder / api-builder | `Konfig AI : Batch Processing` | Product-specific titles |
| about-us / contact-us | `Konfig AI : Home` | About Us / Contact Us |
| legal `?tab=terms` / `cookie` | `Konfig AI : Privacy Policy` | Terms / Cookie Policy |

Treat `Title` tag failures as **A1** (app defect) — do not heal Expected down to the wrong title.

## How to run

```powershell
$env:FOXYIZ_ROOT = "$PWD\FoXYiZ"
# gate
.\FoXYiZ\f\FoXYiZ.exe --config FoXYiZ\f\fStart\KonfigAI.json
# full link health — edit fStart tags to ["Link"]
# title audit — tags ["Title"]
# forms — tags ["Form"]
```

Regenerate CSVs: `python FoXYiZ/y/KonfigAI/_gen_konfigai.py`

## BRAHL

1. Smoke green → Link green  
2. Title run → catalog A1 title mismatches in `brahl_report.md`  
3. Manual Hunter pads for social + submit + a11y  
4. Verify Smoke+Link+Form after any site fix
