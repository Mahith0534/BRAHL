# _Docs — FoXYiZ package documentation

Primary project docs only.

| Document | Project | Audience |
|----------|---------|----------|
| [Vision.md](Vision.md) | **QA on Air vision** (canonical) | Everyone — portal, pitch, desktop; sync with [qaonair.com/vision](https://qaonair.com/vision) |
| [BRAHL.md](BRAHL.md) | Lifecycle | Creators, Hunters, agents running Build→Verify |
| [FoXYiZ.md](FoXYiZ.md) | Engine + this package | Operators authoring yPAD and running `FoXYiZ.exe` |
| [DEMO_YPADS.md](DEMO_YPADS.md) | Demo suites | Operators running Math / API_Petstore / UI_internet / BRAHL_Local / AI_* |
| [AI_GUARDRAILS.md](AI_GUARDRAILS.md) | In-app AI | Packed into every BRAHL AI prompt |
| [BRAHL_PROMPT.md](BRAHL_PROMPT.md) | In-app AI | Slim BRAHL lifecycle for LLM context |
| [BRAHL_DESKTOP_BYOK.md](BRAHL_DESKTOP_BYOK.md) | Desktop AI keys | OpenAI BYOK / Ollama setup |
| [rules.md](rules.md) | Agents | Heal / convention notes |

BRAHL’s AI context drawer resolves `Docs/…` to this `_Docs/` folder automatically.

## Skill map

| Skill id | Owns | Primary doc | Users |
|----------|------|-------------|-------|
| `vision` | Why QoA exists — HITL + AI, marketplace story | [Vision.md](Vision.md) | Founders, portal, marketers, agents |
| `brahl` | Build → Run → Analyze → Heal → Loop → Verify → report | [BRAHL.md](BRAHL.md) | Creator, QA Hunter, agents |
| `foxyiz` | `f(x,y)=z`, yPAD, fStart, exe, `z/`, `_pyUtils` | [FoXYiZ.md](FoXYiZ.md) | Operators, architects, agents |

**Start here for “why”:** [Vision.md](Vision.md). **How to run / heal:** BRAHL + FoXYiZ.

## Package root (FoXYiZ_User)

Three main folders:

```
FoXYiZ_User/
  Run FoXYiZ.bat
  Run BRAHL.bat
  _Docs/                    ← documentation
  BRAHL/                    ← desktop Arena UI (port 8766)
  FoXYiZ/                   ← FOXYIZ_ROOT (engine + yPAD)
    f/FoXYiZ.exe + f/_internal/
    f/fStart/  x/  y/  z/
    _pyUtils/
  README.txt
  VERSION.json
```

Paths inside docs that say `f\`, `y\`, `z\` are relative to **`FOXYIZ_ROOT`** (`FoXYiZ_User\FoXYiZ`), not the zip root.

Architect source tree: **FoXYiZ__code/** (rebuild with `packaging/build_exe.ps1`).
