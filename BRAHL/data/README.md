# BRAHL runtime data

Created/updated while the app runs. Safe to reset for a clean demo.

| Path | Need it? | Role |
|------|----------|------|
| `projects.json` | **Yes** | Arena project list + last-run metadata |
| `projects.seed.json` | Optional | Reset template for projects |
| `workspace.json` | Runtime | Last Workspace chip bind (app under test) |
| `schedules.json` | Runtime | Local schedules (often empty `[]`) |
| `ai_usage.json` | Runtime | Optional AI token usage (BRAHL helpers only) |
| `user_ai_docs/` | Optional | User `.md` uploads for the AI context drawer |
| `users.db` | Optional | Local auth if you use sign-in |
| `uploads/` | Runtime | Temp uploads |

**Removed from this desktop package:** marketplace leftovers (`nalanda*`, `invites*`, Stripe billing).

Suites live under `FoXYiZ/y/` (not here). fStart: `FoXYiZ/f/fStart/`. FoXYiZ.exe runs tests only — AI helpers are BRAHL-side.
