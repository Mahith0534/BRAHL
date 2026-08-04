# WorkInProgress

## 1. UI clutter (Teach / Discuss / Invite)

**Source:** [ThoughtStream view](https://jusdone.base44.app/view/6a6ba66c260735da17e66448) · PDF `feedback_on_ui_clutter_in_brahl_local.pdf`  
**Fix:** Removed orphaned Nalanda sections from `BRAHL/web/index.html`; keep Build→BRAHL phases visible.

## 2. Missing visualization + fStart stacks

**Source:** PDF `fixing_missing_test_visualization_and_dashboard_cl.pdf`  
**Asks:** One editable fStart (not Smoke/AI/Perf stacks); screenshots/video in Analyze; blank Execution Summary.

**Fix (2026-07-30):**
- Canonical fStarts only: `f/fStart/OpsDashboard.json`, `f/fStart/ThoughtStream.json` (extras moved to `f/fStart/archive/`). Use **Run tags** to filter.
- Analyze shows **Execution summary** (from zlogs), thumbnail grid, video players, playback/zDash links.
- Artifacts API lists videos + video-frame folders.
- Job log backfill finds `z/<run>_<Suite>/` even when runtime fStart is `.runtime/run_*` (fixes blank console summary after Run).

**Verify:** Hard-refresh BRAHL → open OpsDashboard → one fStart chip → Edit capture → Run Smoke → Analyze → see summary + evidence.
