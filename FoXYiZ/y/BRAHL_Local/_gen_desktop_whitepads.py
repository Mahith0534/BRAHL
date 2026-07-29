# -*- coding: utf-8 -*-
"""Generate BRAHL_Local desktop white pads — every desktop user case (2026-07-26)."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TS = "2026-07-26T10:00:00+00:00"
AUTHOR = "BRAHL_Local"

DESIGNS: list[tuple[str, str, str]] = [
    ("UI", "base_url", "http://127.0.0.1:8766/"),
    ("UI", "app_url", "http://127.0.0.1:8766/app"),
    ("UI", "app_hash_run", "http://127.0.0.1:8766/app#run"),
    ("UI", "app_hash_analyze", "http://127.0.0.1:8766/app#analyze"),
    ("UI", "app_hash_heal", "http://127.0.0.1:8766/app#heal"),
    ("UI", "app_hash_loop", "http://127.0.0.1:8766/app#loop"),
    ("UI", "app_hash_brahl", "http://127.0.0.1:8766/app#brahl"),
    ("UI", "login_url", "http://127.0.0.1:8766/login"),
    ("UI", "about_url", "http://127.0.0.1:8766/about"),
    ("UI", "body_locator", "css=body"),
    ("UI", "app_title_locator", "css=#app-title"),
    ("UI", "tagline_foxyiz", "css=#tagline-foxyiz"),
    ("UI", "phase_nav_locator", "css=#phase-nav"),
    ("UI", "hint_build", "css=.phase-nav-item[data-phase='build'] .phase-hint"),
    ("UI", "hint_run", "css=.phase-nav-item[data-phase='run'] .phase-hint"),
    ("UI", "hint_analyze", "css=.phase-nav-item[data-phase='analyze'] .phase-hint"),
    ("UI", "hint_heal", "css=.phase-nav-item[data-phase='heal'] .phase-hint"),
    ("UI", "hint_loop", "css=.phase-nav-item[data-phase='loop'] .phase-hint"),
    ("UI", "hint_brahl", "css=.phase-nav-item[data-phase='brahl'] .phase-hint"),
    ("UI", "phase_path_y", "css=.phase-nav-item[data-phase='build'] .phase-path"),
    ("UI", "phase_path_z", "css=.phase-nav-item[data-phase='analyze'] .phase-path"),
    ("UI", "topbar_workspace", "css=#topbar-workspace"),
    ("UI", "topbar_workspace_label", "css=#topbar-workspace-label"),
    ("UI", "topbar_project_select", "css=#topbar-project-select"),
    ("UI", "btn_topbar_add_project", "css=#btn-topbar-add-project"),
    ("UI", "health_pill", "css=#health-pill"),
    ("UI", "footer_version", "css=#footer-version"),
    ("UI", "btn_phase_build", "css=button.phase-btn[data-phase='build']"),
    ("UI", "btn_phase_run", "css=button.phase-btn[data-phase='run']"),
    ("UI", "btn_phase_analyze", "css=button.phase-btn[data-phase='analyze']"),
    ("UI", "btn_phase_heal", "css=button.phase-btn[data-phase='heal']"),
    ("UI", "btn_phase_loop", "css=button.phase-btn[data-phase='loop']"),
    ("UI", "btn_phase_brahl", "css=button.phase-btn[data-phase='brahl']"),
    ("UI", "panel_build", "css=#panel-build"),
    ("UI", "panel_run", "css=#panel-run"),
    ("UI", "panel_analyze", "css=#panel-analyze"),
    ("UI", "panel_heal", "css=#panel-heal"),
    ("UI", "panel_loop", "css=#panel-loop"),
    ("UI", "panel_brahl", "css=#panel-brahl"),
    ("UI", "build_title", "css=#build-panel-title"),
    ("UI", "btn_rebuild", "css=#btn-build-edit-project"),
    ("UI", "build_one_liner", "css=.build-one-liner"),
    ("UI", "build_verify", "css=#build-verify-summary"),
    ("UI", "build_advanced", "css=#build-advanced"),
    ("UI", "build_ai_chat", "css=#build-refine-details"),
    ("UI", "build_team", "css=#brahl-team-workspace"),
    ("UI", "build_brahl_plan", "css=#build-brahl-plan"),
    ("UI", "ypad_coverage", "css=#ypad-coverage-chips"),
    ("UI", "ypad_tabs", "css=#ypad-tabs"),
    ("UI", "ypad_table", "css=#ypad-table-wrap"),
    ("UI", "run_btn", "css=#btn-run"),
    ("UI", "fstart_toolbar", "css=#fstart-chips"),
    ("UI", "desktop_body", "css=body.desktop-mode"),
    ("API", "get_health", "http://127.0.0.1:8766;/api/health"),
    ("API", "get_version", "http://127.0.0.1:8766;/api/version"),
    ("API", "get_suites", "http://127.0.0.1:8766;/api/suites"),
    ("API", "get_projects", "http://127.0.0.1:8766;/api/projects"),
    ("API", "get_workspace", "http://127.0.0.1:8766;/api/workspace"),
    ("API", "get_configs", "http://127.0.0.1:8766;/api/configs"),
    ("API", "get_runs", "http://127.0.0.1:8766;/api/runs"),
    ("API", "post_reveal_y", "http://127.0.0.1:8766;/api/reveal-folder;y/BRAHL_Local/payloads/reveal_y.json"),
    ("API", "post_reveal_z", "http://127.0.0.1:8766;/api/reveal-folder;y/BRAHL_Local/payloads/reveal_z.json"),
    ("API", "post_register", "http://127.0.0.1:8766;/api/auth/register;y/BRAHL_Local/payloads/register.json"),
    ("UI", "http_200", "200"),
    ("UI", "http_404", "404"),
    ("UI", "json_true", "True"),
    ("JSON", "cmp_status_ok", "status;ok"),
    ("JSON", "cmp_desktop_true", "desktop;True"),
    ("JSON", "cmp_service", "service;BRAHL_Local"),
    ("JSON", "cmp_ok_true", "ok;True"),
    ("JSON", "cmp_which_y", "which;y"),
    ("JSON", "cmp_which_z", "which;z"),
]


def plan(pid, name, tags, run="Y", design="D1"):
    return {
        "PlanId": pid,
        "PlanName": name,
        "DesignId": design,
        "Run": run,
        "Tags": tags,
        "Output": pid.lower(),
        "CreatedBy": AUTHOR,
        "CreatedAt": TS,
    }


def step(pid, sid, info, atype, aname, inp="", out="", exp="", crit="Y"):
    return {
        "PlanId": pid,
        "StepId": str(sid),
        "StepInfo": info,
        "ActionType": atype,
        "ActionName": aname,
        "Input": inp,
        "Output": out,
        "Expected": exp,
        "Critical": crit,
    }


PLANS: list[dict] = []
ACTIONS: list[dict] = []


def add(p, steps):
    PLANS.append(p)
    ACTIONS.extend(steps)


# --- Reuse ---
add(
    plan("PReuse_OpenApp", "Open Edge and load BRAHL Local /app", "Reuse", "N"),
    [
        step("PReuse_OpenApp", 1, "Open browser", "xUI", "xOpenBrowser", "edge"),
        step("PReuse_OpenApp", 2, "Navigate /app", "xUI", "xNavigate", "app_url", "", "http://127.0.0.1:8766/app"),
        step("PReuse_OpenApp", 3, "Body present", "xUI", "xGetText", "body_locator"),
    ],
)

# --- Smoke ---
for pid, name, tags, exp_loc, exp_text in [
    ("PSmoke_Title", "Arena boots — title BRAHL Local", "BRAHL_Local;Smoke;Shell", "app_title_locator", "BRAHL Local"),
    ("PSmoke_PhaseNav", "Phase nav present", "BRAHL_Local;Smoke;Shell", "phase_nav_locator", "Build"),
    ("PSmoke_Workspace", "Workspace chip present", "BRAHL_Local;Smoke;Workspace", "topbar_workspace", "Workspace"),
    ("PSmoke_DesktopMode", "desktop-mode brand present", "BRAHL_Local;Smoke;Desktop", "app_title_locator", "BRAHL Local"),
    ("PSmoke_Health", "Footer health pill", "BRAHL_Local;Smoke;Shell", "health_pill", ""),
    ("PSmoke_FoXYiZLink", "Tagline FoXYiZ is clickable", "BRAHL_Local;Smoke;Docs", "tagline_foxyiz", "FoXYiZ"),
]:
    steps = [step(pid, 1, "Open app", "xReuse", "PReuse_OpenApp")]
    if exp_text:
        steps.append(step(pid, 2, name, "xUI", "xGetText", exp_loc, "", exp_text))
    else:
        steps.append(step(pid, 2, name, "xUI", "xGetText", exp_loc))
    add(plan(pid, name, tags), steps)

# --- Phase hints (ThoughtStream labels) ---
for pid, name, loc, text, tags in [
    ("PHint_Build", "Build hint Tests (/y)", "hint_build", "Tests", "BRAHL_Local;UI;Hints;Build"),
    ("PHint_Run", "Run hint Tests (/y)", "hint_run", "Tests", "BRAHL_Local;UI;Hints;Run"),
    ("PHint_Analyze", "Analyze hint Results (/z)", "hint_analyze", "Results", "BRAHL_Local;UI;Hints;Analyze"),
    ("PHint_Heal", "Heal hint Heal Tests (/y)", "hint_heal", "Heal Tests", "BRAHL_Local;UI;Hints;Heal"),
    ("PHint_Loop", "Loop hint Verify /y -> /z", "hint_loop", "Verify", "BRAHL_Local;UI;Hints;Loop"),
    ("PHint_Brahl", "BRAHL hint Go / No-Go", "hint_brahl", "Go / No-Go", "BRAHL_Local;UI;Hints;BRAHL"),
    ("PHint_PathY", "Build /y path button present", "phase_path_y", "/y", "BRAHL_Local;UI;Hints;Reveal"),
    ("PHint_PathZ", "Analyze /z path button present", "phase_path_z", "/z", "BRAHL_Local;UI;Hints;Reveal"),
]:
    add(
        plan(pid, name, tags),
        [
            step(pid, 1, "Open app", "xReuse", "PReuse_OpenApp"),
            step(pid, 2, name, "xUI", "xGetText", loc, "", text),
        ],
    )

# --- Phase navigation ---
for pid, phase_btn, panel, label in [
    ("PNav_Run", "btn_phase_run", "panel_run", "Run"),
    ("PNav_Analyze", "btn_phase_analyze", "panel_analyze", "Analyze"),
    ("PNav_Heal", "btn_phase_heal", "panel_heal", "Heal"),
    ("PNav_Loop", "btn_phase_loop", "panel_loop", "Loop"),
    ("PNav_Brahl", "btn_phase_brahl", "panel_brahl", "BRAHL"),
    ("PNav_Build", "btn_phase_build", "panel_build", "Build"),
]:
    add(
        plan(pid, f"UI — open {label} phase", f"BRAHL_Local;UI;Nav;{label}"),
        [
            step(pid, 1, "Open app", "xReuse", "PReuse_OpenApp"),
            step(pid, 2, f"Click {label}", "xUI", "xClick", phase_btn),
            step(pid, 3, f"{label} panel visible", "xUI", "xGetText", panel),
        ],
    )

# Deep links
for pid, url_key, panel, label in [
    ("PNav_DeepRun", "app_hash_run", "panel_run", "Run"),
    ("PNav_DeepBrahl", "app_hash_brahl", "panel_brahl", "BRAHL"),
]:
    add(
        plan(pid, f"Deep link #{label.lower()}", f"BRAHL_Local;UI;Nav;{label}"),
        [
            step(pid, 1, "Open browser", "xUI", "xOpenBrowser", "edge"),
            step(pid, 2, "Navigate hash", "xUI", "xNavigate", url_key),
            step(pid, 3, f"{label} panel", "xUI", "xGetText", panel),
        ],
    )

# --- Build (ThoughtStream: Rebuild, no verify clutter, no Advanced/AI) ---
add(
    plan("PBuild_RebuildBtn", "Build header shows Rebuild (not Add/Edit)", "BRAHL_Local;Build;Rebuild"),
    [
        step("PBuild_RebuildBtn", 1, "Open app", "xReuse", "PReuse_OpenApp"),
        step("PBuild_RebuildBtn", 2, "Rebuild button", "xUI", "xGetText", "btn_rebuild", "", "Rebuild"),
    ],
)
add(
    plan("PBuild_NoVerifyLine", "Build verify summary stays hidden on desktop", "BRAHL_Local;Build;Desktop"),
    [
        step("PBuild_NoVerifyLine", 1, "Open app", "xReuse", "PReuse_OpenApp"),
        step("PBuild_NoVerifyLine", 2, "Title present", "xUI", "xGetText", "build_title", "", "Build"),
        step("PBuild_NoVerifyLine", 3, "Verify node exists (hidden)", "xUI", "xGetText", "build_verify", "", "", "N"),
    ],
)
add(
    plan("PBuild_OpenRebuild", "Rebuild opens collapsible rebuild plan", "BRAHL_Local;Build;Rebuild"),
    [
        step("PBuild_OpenRebuild", 1, "Open app", "xReuse", "PReuse_OpenApp"),
        step("PBuild_OpenRebuild", 2, "Click Rebuild", "xUI", "xClick", "btn_rebuild"),
        step("PBuild_OpenRebuild", 3, "Rebuild plan visible", "xUI", "xGetText", "build_brahl_plan", "", "Rebuild"),
        step("PBuild_OpenRebuild", 4, "Done label on button", "xUI", "xGetText", "btn_rebuild", "", "Done"),
    ],
)
add(
    plan("PBuild_FoXYiZDocs", "Click FoXYiZ opens docs modal", "BRAHL_Local;Build;Docs"),
    [
        step("PBuild_FoXYiZDocs", 1, "Open app", "xReuse", "PReuse_OpenApp"),
        step("PBuild_FoXYiZDocs", 2, "Click FoXYiZ", "xUI", "xClick", "tagline_foxyiz"),
        step("PBuild_FoXYiZDocs", 3, "Docs modal body", "xUI", "xGetText", "body_locator", "", "md"),
    ],
)
add(
    plan("PBuild_YpadCoverage", "Test coverage chips present when suite selected", "BRAHL_Local;Build;Ypad"),
    [
        step("PBuild_YpadCoverage", 1, "Open app", "xReuse", "PReuse_OpenApp"),
        step("PBuild_YpadCoverage", 2, "Coverage chips", "xUI", "xGetText", "ypad_coverage", "", "", "N"),
    ],
)

# --- Workspace / projects ---
add(
    plan("PWs_ProjectsSelect", "Projects dropdown present", "BRAHL_Local;Workspace;Projects"),
    [
        step("PWs_ProjectsSelect", 1, "Open app", "xReuse", "PReuse_OpenApp"),
        step("PWs_ProjectsSelect", 2, "Select present", "xUI", "xGetText", "topbar_project_select"),
    ],
)
add(
    plan("PWs_AddProject", "Topbar + new project", "BRAHL_Local;Workspace"),
    [
        step("PWs_AddProject", 1, "Open app", "xReuse", "PReuse_OpenApp"),
        step("PWs_AddProject", 2, "Add button", "xUI", "xGetText", "btn_topbar_add_project"),
    ],
)

# --- Run / Analyze / Heal / Loop / BRAHL controls ---
add(
    plan("PRun_Controls", "Run — Run phase panel opens", "BRAHL_Local;Run"),
    [
        step("PRun_Controls", 1, "Open app", "xReuse", "PReuse_OpenApp"),
        step("PRun_Controls", 2, "Go Run", "xUI", "xClick", "btn_phase_run"),
        step("PRun_Controls", 3, "Run panel", "xUI", "xGetText", "panel_run"),
    ],
)
add(
    plan("PAnalyze_Panel", "Analyze panel opens", "BRAHL_Local;Analyze"),
    [
        step("PAnalyze_Panel", 1, "Open app", "xReuse", "PReuse_OpenApp"),
        step("PAnalyze_Panel", 2, "Go Analyze", "xUI", "xClick", "btn_phase_analyze"),
        step("PAnalyze_Panel", 3, "Panel", "xUI", "xGetText", "panel_analyze"),
    ],
)
add(
    plan("PHeal_Panel", "Heal panel opens", "BRAHL_Local;Heal"),
    [
        step("PHeal_Panel", 1, "Open app", "xReuse", "PReuse_OpenApp"),
        step("PHeal_Panel", 2, "Go Heal", "xUI", "xClick", "btn_phase_heal"),
        step("PHeal_Panel", 3, "Panel", "xUI", "xGetText", "panel_heal"),
    ],
)
add(
    plan("PLoop_Panel", "Loop panel opens", "BRAHL_Local;Loop"),
    [
        step("PLoop_Panel", 1, "Open app", "xReuse", "PReuse_OpenApp"),
        step("PLoop_Panel", 2, "Go Loop", "xUI", "xClick", "btn_phase_loop"),
        step("PLoop_Panel", 3, "Panel", "xUI", "xGetText", "panel_loop"),
    ],
)
add(
    plan("PBrahl_Panel", "BRAHL Go/No-Go panel opens", "BRAHL_Local;BRAHL"),
    [
        step("PBrahl_Panel", 1, "Open app", "xReuse", "PReuse_OpenApp"),
        step("PBrahl_Panel", 2, "Go BRAHL", "xUI", "xClick", "btn_phase_brahl"),
        step("PBrahl_Panel", 3, "Panel", "xUI", "xGetText", "panel_brahl"),
    ],
)

# --- Security / desktop ---
add(
    plan("PSec_AuthRegisterOff", "POST /api/auth/register disabled on desktop", "BRAHL_Local;Security;Auth;API"),
    [
        step("PSec_AuthRegisterOff", 1, "POST register", "xAPI", "xPost", "post_register", "", "http_404"),
    ],
)
add(
    plan("PSec_HealthNoSecrets", "Health exposes desktop, not secrets", "BRAHL_Local;Security;API"),
    [
        step("PSec_HealthNoSecrets", 1, "GET health", "xAPI", "xGet", "get_health", "", "http_200"),
        step("PSec_HealthNoSecrets", 2, "status ok", "xJSON", "xCompareJson", "cmp_status_ok", "", "json_true"),
        step("PSec_HealthNoSecrets", 3, "desktop true", "xJSON", "xCompareJson", "cmp_desktop_true", "", "json_true"),
        step("PSec_HealthNoSecrets", 4, "service BRAHL_Local", "xJSON", "xCompareJson", "cmp_service", "", "json_true"),
    ],
)

# --- API ---
for pid, name, url in [
    ("PApi_Health", "API GET /api/health", "get_health"),
    ("PApi_Version", "API GET /api/version", "get_version"),
    ("PApi_Suites", "API GET /api/suites", "get_suites"),
    ("PApi_Projects", "API GET /api/projects", "get_projects"),
    ("PApi_Workspace", "API GET /api/workspace", "get_workspace"),
    ("PApi_Configs", "API GET /api/configs", "get_configs"),
    ("PApi_Runs", "API GET /api/runs", "get_runs"),
]:
    add(
        plan(pid, name, "BRAHL_Local;API"),
        [step(pid, 1, name, "xAPI", "xGet", url, "", "http_200")],
    )

add(
    plan("PApi_RevealY", "API POST /api/reveal-folder y", "BRAHL_Local;API;Reveal"),
    [
        step("PApi_RevealY", 1, "Reveal y", "xAPI", "xPost", "post_reveal_y", "", "http_200"),
        step("PApi_RevealY", 2, "ok true", "xJSON", "xCompareJson", "cmp_ok_true", "", "json_true"),
        step("PApi_RevealY", 3, "which y", "xJSON", "xCompareJson", "cmp_which_y", "", "json_true"),
    ],
)
add(
    plan("PApi_RevealZ", "API POST /api/reveal-folder z", "BRAHL_Local;API;Reveal"),
    [
        step("PApi_RevealZ", 1, "Reveal z", "xAPI", "xPost", "post_reveal_z", "", "http_200"),
        step("PApi_RevealZ", 2, "ok true", "xJSON", "xCompareJson", "cmp_ok_true", "", "json_true"),
        step("PApi_RevealZ", 3, "which z", "xJSON", "xCompareJson", "cmp_which_z", "", "json_true"),
    ],
)

# --- Performance ---
add(
    plan("PPerf_AppReady", "Perf — /app ready", "BRAHL_Local;Performance;Shell"),
    [
        step("PPerf_AppReady", 1, "Open app", "xReuse", "PReuse_OpenApp"),
        step("PPerf_AppReady", 2, "Title", "xUI", "xGetText", "app_title_locator", "", "BRAHL Local"),
    ],
)
add(
    plan("PPerf_Health", "Perf — health 200", "BRAHL_Local;Performance;API"),
    [step("PPerf_Health", 1, "GET health", "xAPI", "xGet", "get_health", "", "http_200")],
)
add(
    plan("PPerf_PhaseSwitch", "Perf — rapid phase switching", "BRAHL_Local;Performance;UI"),
    [
        step("PPerf_PhaseSwitch", 1, "Open app", "xReuse", "PReuse_OpenApp"),
        step("PPerf_PhaseSwitch", 2, "Run", "xUI", "xClick", "btn_phase_run"),
        step("PPerf_PhaseSwitch", 3, "Analyze", "xUI", "xClick", "btn_phase_analyze"),
        step("PPerf_PhaseSwitch", 4, "Build", "xUI", "xClick", "btn_phase_build"),
        step("PPerf_PhaseSwitch", 5, "Build panel", "xUI", "xGetText", "panel_build"),
    ],
)

# --- Manual ---
add(
    plan("PMan_TeamWorkspace", "Manual — confirm Team workspace absent on desktop", "BRAHL_Local;Manual;Desktop", "N"),
    [step("PMan_TeamWorkspace", 1, "Visual check team hidden", "xUI", "xGetText", "body_locator", "", "", "N")],
)
add(
    plan("PMan_AdvancedHidden", "Manual — Advanced / AI chat absent on desktop", "BRAHL_Local;Manual;Desktop", "N"),
    [step("PMan_AdvancedHidden", 1, "Visual check", "xUI", "xGetText", "body_locator", "", "", "N")],
)


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fieldnames})


def main() -> None:
    y1 = ROOT / "y1Plans.csv"
    y2 = ROOT / "y2Actions.csv"
    y3 = ROOT / "y3Designs.csv"
    write_csv(
        y1,
        PLANS,
        ["PlanId", "PlanName", "DesignId", "Run", "Tags", "Output", "CreatedBy", "CreatedAt"],
    )
    write_csv(
        y2,
        ACTIONS,
        ["PlanId", "StepId", "StepInfo", "ActionType", "ActionName", "Input", "Output", "Expected", "Critical"],
    )
    y3_rows = [{"Type": t, "DataName": n, "D1": v, "D2": "", "D3": ""} for t, n, v in DESIGNS]
    write_csv(y3, y3_rows, ["Type", "DataName", "D1", "D2", "D3"])
    (ROOT / "BRAHL_Local.json").write_text(
        '{\n  "input_files": {\n'
        '    "yPlans": ["y/BRAHL_Local/y1Plans.csv"],\n'
        '    "yActions": ["y/BRAHL_Local/y2Actions.csv"],\n'
        '    "yDesigns": ["y/BRAHL_Local/y3Designs.csv"]\n'
        "  }\n}\n",
        encoding="utf-8",
    )
    (ROOT / "test_strategy.md").write_text(
        "# BRAHL_Local — test strategy\n\n"
        "Desktop BRAHL Local self-test. Layers: **general** (`_Docs/FoXYiZ.md`, `_Docs/BRAHL.md`) "
        "+ **project** (`y/BRAHL_Local/*.md`).\n\n"
        "Cover Shell, phase hints `/y` `/z`, Rebuild, docs link, Run->BRAHL, security, reveal API, perf.\n",
        encoding="utf-8",
    )
    (ROOT / "test_plan.md").write_text(
        "# BRAHL_Local — test plan\n\n"
        "Source: ThoughtStream https://jusdone.base44.app/view/6a65db11d1301b5daeb45249\n\n"
        "## User cases\n"
        "- Smoke shell / desktop mode\n"
        "- Phase hints Tests (/y), Results (/z), Heal Tests, Verify, Go/No-Go\n"
        "- Rebuild (not Add/Edit); no verify clutter under Build title\n"
        "- FoXYiZ tagline -> docs (general + project .md)\n"
        "- Phase nav + deep links\n"
        "- Reveal-folder API for /y and /z\n"
        "- Run / Analyze / Heal / Loop / BRAHL panels\n"
        "- Security: auth register off; health no secrets\n"
        "- Performance: app ready, health, phase switch\n",
        encoding="utf-8",
    )
    y_count = sum(1 for p in PLANS if p["Run"] == "Y")
    print(f"Wrote {len(PLANS)} plans ({y_count} Run=Y), {len(ACTIONS)} steps -> {ROOT}")


if __name__ == "__main__":
    main()
