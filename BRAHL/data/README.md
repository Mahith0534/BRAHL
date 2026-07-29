# BRAHL runtime data

Created/updated while the app runs. Safe to reset for a clean demo.

| Path | Need it? | Role |
|------|----------|------|
| `projects.json` | **Yes** | Arena project list + last-run metadata |
| `projects.seed.json` | Optional | Reset template for projects |
| `workspace.json` | Runtime | Last Workspace chip bind (app under test) |
| `schedules.json` | Runtime | Local schedules (often empty `[]`) |
| `user_ai_docs/` | **No for ship** | Optional user `.md` uploads for the `.md` drawer / AI prompt — created on first upload |
| `users.db` | Cloud leftover | Auth/wallets — not needed for desktop demos |
| `invites*.json` / `nalanda*.json` | Cloud leftover | Marketplace / Nalanda — desktop usually ignores |
| `uploads/` | Runtime | Temp uploads |

Suites live under `FoXYiZ/y/` (not here). fStart: `FoXYiZ/f/fStart/`.
