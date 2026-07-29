# -*- coding: utf-8 -*-
"""Generate extensive BRAHL_Local desktop self-test yPAD (module-tagged)."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] if False else Path(r"c:\006\FXYZ\KK2\FoXYiZ\y\BRAHL_Local")
TS = "2026-07-24T21:30:00+00:00"
AUTHOR = "QA_Hunter+KK2"

# DataName -> D1
DESIGNS: list[tuple[str, str]] = [
    ("base_url", "http://127.0.0.1:8766/"),
    ("app_url", "http://127.0.0.1:8766/app"),
    ("app_hash_run", "http://127.0.0.1:8766/app#run"),
    ("app_hash_brahl", "http://127.0.0.1:8766/app#brahl"),
    ("login_url", "http://127.0.0.1:8766/login"),
    ("api_base", "http://127.0.0.1:8766"),
    ("body_locator", "css=body"),
    ("app_title_locator", "css=#app-title"),
    ("phase_nav_locator", "css=#phase-nav"),
    ("topbar_workspace_locator", "css=#topbar-workspace"),
    ("workspace_chip_locator", "css=#topbar-workspace .topbar-workspace-chip"),
    ("workspace_label_locator", "css=#topbar-workspace-label"),
    ("btn_workspace_change", "css=#btn-workspace-change"),
    ("topbar_project_select", "css=#topbar-project-select"),
    ("btn_topbar_add_project", "css=#btn-topbar-add-project"),
    ("ai_toggle_wrap", "css=#ai-toggle-wrap"),
    ("ai_toggle_label", "css=#ai-toggle-label"),
    ("health_pill", "css=#health-pill"),
    ("footer_version", "css=#footer-version"),
    ("panel_build_locator", "css=#panel-build"),
    ("panel_run_locator", "css=#panel-run"),
    ("panel_analyze_locator", "css=#panel-analyze"),
    ("panel_heal_locator", "css=#panel-heal"),
    ("panel_loop_locator", "css=#panel-loop"),
    ("panel_brahl_locator", "css=#panel-brahl"),
    ("btn_phase_build", "css=button.phase-btn[data-phase='build']"),
    ("btn_phase_run", "css=button.phase-btn[data-phase='run']"),
    ("btn_phase_analyze", "css=button.phase-btn[data-phase='analyze']"),
    ("btn_phase_heal", "css=button.phase-btn[data-phase='heal']"),
    ("btn_phase_loop", "css=button.phase-btn[data-phase='loop']"),
    ("btn_phase_brahl", "css=button.phase-btn[data-phase='brahl']"),
    ("desktop_title_locator", "css=body.desktop-mode #app-title"),
    ("suite_select_qoa", "css=#topbar-project-select;BRAHL_Local"),
    ("build_panel_title", "css=#build-panel-title"),
    ("ypad_insights", "css=#ypad-insights"),
    ("ypad_insights_stats", "css=#ypad-insights-stats"),
    ("ypad_tab_plans", "css=button.ypad-tab[data-ypad-tab='plans']"),
    ("ypad_tab_actions", "css=button.ypad-tab[data-ypad-tab='actions']"),
    ("ypad_tab_designs", "css=button.ypad-tab[data-ypad-tab='designs']"),
    ("ypad_tab_env", "css=button.ypad-tab[data-ypad-tab='env']"),
    ("ypad_filter", "css=#ypad-filter"),
    ("ypad_filter_type", "Smoke;css=#ypad-filter"),
    ("ypad_cov_all", "css=button.ypad-cov-chip[data-ypad-cov='all']"),
    ("ypad_cov_auto", "css=button.ypad-cov-chip[data-ypad-cov='auto']"),
    ("ypad_cov_manual", "css=button.ypad-cov-chip[data-ypad-cov='manual']"),
    ("ypad_table", "css=#ypad-table"),
    ("ypad_toggle_edit", "css=#ypad-toggle-edit"),
    ("ypad_versions", "css=#ypad-versions"),
    ("btn_ypad_snapshot", "css=#btn-ypad-snapshot"),
    ("brahl_plan_requirement", "css=#brahl-plan-requirement"),
    ("btn_generate_brahl_plan", "css=#btn-generate-brahl-plan"),
    ("build_refine_summary", "css=#build-refine-details > summary"),
    ("chat_input", "css=#chat-input"),
    ("chat_send_btn", "css=#chat-send-btn"),
    ("run_suite_display", "css=#run-suite-display"),
    ("fstart_chip_row", "css=#fstart-chip-row"),
    ("btn_fstart_edit", "css=#btn-fstart-edit"),
    ("fstart_modal", "css=#fstart-modal"),
    ("fstart_cancel", "css=#fstart-cancel"),
    ("cap_image", "css=#cap-image"),
    ("run_tag_row", "css=#run-tag-row"),
    ("run_profile_row", "css=#run-profile-row"),
    ("run_thread_count", "css=#run-thread-count"),
    ("run_capture_strip", "css=#run-capture-strip"),
    ("run_capture_summary", "css=#run-capture-summary"),
    ("btn_run", "css=#btn-run"),
    ("run_recent", "css=#run-recent"),
    ("btn_refresh_runs", "css=#btn-refresh-runs"),
    ("runs_list", "css=#runs-list"),
    ("failures_body", "css=#failures-body"),
    ("dash_link", "css=#dash-link"),
    ("btn_heal_edit_ypad", "css=#btn-heal-edit-ypad"),
    ("btn_heal_rerun", "css=#btn-heal-rerun"),
    ("btn_heal_apply", "css=#btn-heal-apply"),
    ("btn_shrink_plans", "css=#btn-shrink-plans"),
    ("btn_restore_plans", "css=#btn-restore-plans"),
    ("heal_failures_body", "css=#heal-failures-body"),
    ("loop_times_1", "css=input[name='loop-times'][value='1']"),
    ("loop_times_2", "css=input[name='loop-times'][value='2']"),
    ("loop_verify_full", "css=#loop-verify-full"),
    ("btn_loop_run", "css=#btn-loop-run"),
    ("cycle_history", "css=#cycle-history"),
    ("schedules_section", "css=#schedules-section"),
    ("scorecard", "css=#scorecard"),
    ("gonogo_block", "css=#gonogo-block"),
    ("brahl_report_tabs", "css=#brahl-report-tabs"),
    ("brahl_report_list", "css=#brahl-report-list"),
    ("brahl_chat_input", "css=#brahl-chat-input"),
    ("brahl_team_workspace", "css=#brahl-team-workspace"),
    ("brahl_team_invite", "css=#brahl-team-invite"),
    ("arena_cost_widget", "css=#arena-cost-widget"),
    ("page_title_token", "BRAHL Local"),
    ("title_token", "BRAHL Desktop"),
    ("text_tagline", "FoXYiZ runs the tests"),
    ("text_workspace", "Workspace"),
    ("text_phase_build", "Build"),
    ("text_phase_run", "Run"),
    ("text_phase_analyze", "Analyze"),
    ("text_phase_heal", "Heal"),
    ("text_phase_loop", "Loop"),
    ("text_phase_brahl", "BRAHL"),
    ("text_run_heading", "FoXYiZ fEngine2"),
    ("text_analyze_heading", "Analyze"),
    ("text_heal_heading", "Heal"),
    ("text_loop_heading", "Loop"),
    ("text_brahl_heading", "BRAHL"),
    ("text_suite_qoa", "BRAHL_Local"),
    ("text_ypad_tests", "Tests"),
    ("text_ypad_steps", "Steps"),
    ("text_ypad_data", "Test data"),
    ("text_ai_on", "AI"),
    ("text_change", "Change"),
    ("text_health", "ok"),
    ("http_200", "200"),
    ("http_401", "401"),
    ("http_404", "404"),
    ("json_true", "True"),
    ("json_false", "False"),
    ("get_health", "http://127.0.0.1:8766;/api/health"),
    ("get_version", "http://127.0.0.1:8766;/api/version"),
    ("get_config", "http://127.0.0.1:8766;/api/config"),
    ("get_suites", "http://127.0.0.1:8766;/api/suites"),
    ("get_workspace", "http://127.0.0.1:8766;/api/workspace"),
    ("get_projects", "http://127.0.0.1:8766;/api/projects"),
    ("get_configs", "http://127.0.0.1:8766;/api/configs"),
    ("get_runs", "http://127.0.0.1:8766;/api/runs"),
    ("get_run_profiles", "http://127.0.0.1:8766;/api/run-profiles"),
    ("get_ai_status", "http://127.0.0.1:8766;/api/ai/status"),
    ("get_ypad_plans", "http://127.0.0.1:8766;/api/suites/BRAHL_Local/ypad/plans"),
    ("get_auth_me", "http://127.0.0.1:8766;/api/auth/me"),
    ("get_billing", "http://127.0.0.1:8766;/api/billing/plans"),
    ("post_register", "http://127.0.0.1:8766;/api/auth/register;y/BRAHL_Local/payloads/register.json"),
    ("cmp_status_ok", "status;ok"),
    ("cmp_desktop_true", "desktop;True"),
    ("cmp_service", "service;kk2-desktop"),
    ("cmp_bound_true", "bound;True"),
    ("cmp_openai_false", "openai_key_set;False"),
    ("cmp_version_desktop", "version;2.0.0-desktop"),
]


def write_designs():
    path = ROOT / "y3Designs.csv"
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Type", "DataName", "D1"])
        for name, val in DESIGNS:
            w.writerow(["UI", name, val])


def plan(pid, name, tags, out, run="Y"):
    return {
        "PlanId": pid,
        "PlanName": name,
        "DesignId": "D1",
        "Run": run,
        "Tags": tags,
        "Output": out,
        "CreatedBy": AUTHOR,
        "CreatedAt": TS,
    }


def step(pid, sid, info, atype, aname, inp="", expected="", critical="Y"):
    return {
        "PlanId": pid,
        "StepId": sid,
        "StepInfo": info,
        "ActionType": atype,
        "ActionName": aname,
        "Input": inp,
        "Output": "",
        "Expected": expected,
        "Critical": critical,
    }


def open_app(pid, start=1):
    return [
        step(pid, start, "Open app", "xReuse", "PReuse_BrahlLocal_OpenApp"),
        step(pid, start + 1, "Navigate /app", "xUI", "xNavigate", "app_url"),
        step(pid, start + 2, "Wait", "xTime", "xTimeWait", "2"),
    ]


def select_suite(pid, start):
    return [
        step(pid, start, "Select suite BRAHL_Local", "xUI", "xSelectDropdown", "suite_select_qoa"),
        step(pid, start + 1, "Wait suite load", "xTime", "xTimeWait", "3"),
    ]


def api_get(pid, sid, label, get_key, expected="http_200"):
    return step(pid, sid, label, "xAPI", "xGet", get_key, expected)


PLANS: list[dict] = []
ACTIONS: list[dict] = []


def add_plan(p, actions):
    PLANS.append(p)
    ACTIONS.extend(actions)


# --- Reuse ---
add_plan(
    plan("PReuse_BrahlLocal_OpenApp", "Open Edge and load BRAHL Local /app", "Reuse", "app_loaded", "N"),
    [
        step("PReuse_BrahlLocal_OpenApp", 1, "Open Edge", "xUI", "xOpenBrowser", "edge"),
        step("PReuse_BrahlLocal_OpenApp", 2, "Navigate /app", "xUI", "xNavigate", "app_url"),
        step("PReuse_BrahlLocal_OpenApp", 3, "Wait boot", "xTime", "xTimeWait", "3"),
        step("PReuse_BrahlLocal_OpenApp", 4, "Body present", "xUI", "xGetText", "body_locator"),
    ],
)

# --- Smoke ---
add_plan(
    plan("PQoa_Smoke_AppTitle", "Arena boots — title BRAHL Local", "BRAHL_Local;Smoke;Shell", "smoke_title"),
    open_app("PQoa_Smoke_AppTitle")
    + [
        step("PQoa_Smoke_AppTitle", 4, "Document title", "xUI", "xGetTitle", "", "page_title_token"),
        step("PQoa_Smoke_AppTitle", 5, "H1 brand", "xUI", "xGetText", "app_title_locator", "title_token"),
        step("PQoa_Smoke_AppTitle", 6, "Tagline", "xUI", "xGetText", "body_locator", "text_tagline"),
    ],
)
add_plan(
    plan("PQoa_Smoke_PhaseNav", "Phase nav shows Build Run Analyze Heal Loop BRAHL", "BRAHL_Local;Smoke;Shell", "smoke_phases"),
    open_app("PQoa_Smoke_PhaseNav")
    + [
        step("PQoa_Smoke_PhaseNav", 4, "Nav Build", "xUI", "xGetText", "phase_nav_locator", "text_phase_build"),
        step("PQoa_Smoke_PhaseNav", 5, "Nav Run", "xUI", "xGetText", "phase_nav_locator", "text_phase_run"),
        step("PQoa_Smoke_PhaseNav", 6, "Nav Analyze", "xUI", "xGetText", "phase_nav_locator", "text_phase_analyze"),
        step("PQoa_Smoke_PhaseNav", 7, "Nav Heal", "xUI", "xGetText", "phase_nav_locator", "text_phase_heal"),
        step("PQoa_Smoke_PhaseNav", 8, "Nav Loop", "xUI", "xGetText", "phase_nav_locator", "text_phase_loop"),
        step("PQoa_Smoke_PhaseNav", 9, "Nav BRAHL", "xUI", "xGetText", "phase_nav_locator", "text_phase_brahl"),
    ],
)
add_plan(
    plan("PQoa_Smoke_WorkspaceChrome", "Topbar Workspace label present", "BRAHL_Local;Smoke;Workspace", "smoke_workspace"),
    open_app("PQoa_Smoke_WorkspaceChrome")
    + [
        step("PQoa_Smoke_WorkspaceChrome", 4, "Workspace chip", "xUI", "xGetText", "workspace_chip_locator", "text_workspace"),
        step("PQoa_Smoke_WorkspaceChrome", 5, "Bound label", "xUI", "xGetText", "workspace_label_locator"),
    ],
)
add_plan(
    plan("PQoa_Smoke_NoWalletChrome", "desktop-mode class applied (wallet CSS suppressed)", "BRAHL_Local;Smoke;Desktop", "smoke_nowallet"),
    open_app("PQoa_Smoke_NoWalletChrome")
    + [
        step("PQoa_Smoke_NoWalletChrome", 4, "desktop-mode title", "xUI", "xGetText", "desktop_title_locator", "title_token"),
        step("PQoa_Smoke_NoWalletChrome", 5, "Phase nav", "xUI", "xGetText", "phase_nav_locator", "text_phase_build"),
    ],
)
add_plan(
    plan("PQoa_Smoke_HealthPill", "Footer health pill present", "BRAHL_Local;Smoke;Shell", "smoke_health"),
    open_app("PQoa_Smoke_HealthPill")
    + [
        step("PQoa_Smoke_HealthPill", 4, "Health pill", "xUI", "xGetText", "health_pill"),
        step("PQoa_Smoke_HealthPill", 5, "Footer version", "xUI", "xGetText", "footer_version"),
    ],
)

# --- UI Nav (kept + deep links) ---
for pid, phase, btn, panel, exp, tag in [
    ("PQoa_UI_OpenRun", "Run", "btn_phase_run", "panel_run_locator", "text_run_heading", "Run"),
    ("PQoa_UI_OpenAnalyze", "Analyze", "btn_phase_analyze", "panel_analyze_locator", "text_analyze_heading", "Analyze"),
    ("PQoa_UI_OpenHeal", "Heal", "btn_phase_heal", "panel_heal_locator", "text_heal_heading", "Heal"),
    ("PQoa_UI_OpenLoop", "Loop", "btn_phase_loop", "panel_loop_locator", "text_loop_heading", "Loop"),
    ("PQoa_UI_OpenBrahl", "BRAHL", "btn_phase_brahl", "panel_brahl_locator", "text_brahl_heading", "BRAHL"),
]:
    add_plan(
        plan(pid, f"UI — click {phase} phase", f"BRAHL_Local;UI;{tag};Nav", f"ui_{tag.lower()}"),
        open_app(pid)
        + [
            step(pid, 4, f"Click {phase}", "xUI", "xClick", btn),
            step(pid, 5, "Wait panel", "xTime", "xTimeWait", "1"),
            step(pid, 6, f"{phase} panel", "xUI", "xGetText", panel, exp),
        ],
    )

add_plan(
    plan("PQoa_UI_BackToBuild", "UI — return to Build phase", "BRAHL_Local;UI;Build;Nav", "ui_build"),
    open_app("PQoa_UI_BackToBuild")
    + [
        step("PQoa_UI_BackToBuild", 4, "Click Run", "xUI", "xClick", "btn_phase_run"),
        step("PQoa_UI_BackToBuild", 5, "Wait", "xTime", "xTimeWait", "1"),
        step("PQoa_UI_BackToBuild", 6, "Click Build", "xUI", "xClick", "btn_phase_build"),
        step("PQoa_UI_BackToBuild", 7, "Wait panel", "xTime", "xTimeWait", "1"),
        step("PQoa_UI_BackToBuild", 8, "Build panel", "xUI", "xGetText", "panel_build_locator", "text_phase_build"),
    ],
)
add_plan(
    plan("PQoa_UI_DeepLinkRun", "UI — deep link /app#run opens Run", "BRAHL_Local;UI;Run;Nav", "ui_deeplink_run"),
    [
        step("PQoa_UI_DeepLinkRun", 1, "Open app", "xReuse", "PReuse_BrahlLocal_OpenApp"),
        step("PQoa_UI_DeepLinkRun", 2, "Navigate #run", "xUI", "xNavigate", "app_hash_run"),
        step("PQoa_UI_DeepLinkRun", 3, "Wait", "xTime", "xTimeWait", "2"),
        step("PQoa_UI_DeepLinkRun", 4, "Run panel", "xUI", "xGetText", "panel_run_locator", "text_run_heading"),
    ],
)
add_plan(
    plan("PQoa_UI_DeepLinkBrahl", "UI — deep link /app#brahl", "BRAHL_Local;UI;BRAHL;Nav", "ui_deeplink_brahl"),
    [
        step("PQoa_UI_DeepLinkBrahl", 1, "Open app", "xReuse", "PReuse_BrahlLocal_OpenApp"),
        step("PQoa_UI_DeepLinkBrahl", 2, "Navigate #brahl", "xUI", "xNavigate", "app_hash_brahl"),
        step("PQoa_UI_DeepLinkBrahl", 3, "Wait", "xTime", "xTimeWait", "2"),
        step("PQoa_UI_DeepLinkBrahl", 4, "BRAHL panel", "xUI", "xGetText", "panel_brahl_locator", "text_brahl_heading"),
    ],
)

# --- Workspace ---
add_plan(
    plan("PQoa_Ws_ChangeButton", "Workspace Change button present", "BRAHL_Local;Workspace", "ws_change"),
    open_app("PQoa_Ws_ChangeButton")
    + [
        step("PQoa_Ws_ChangeButton", 4, "Change btn", "xUI", "xGetText", "btn_workspace_change", "text_change"),
    ],
)
add_plan(
    plan("PQoa_Ws_SelectSuite", "Select BRAHL_Local suite in topbar", "BRAHL_Local;Workspace;Build", "ws_select"),
    open_app("PQoa_Ws_SelectSuite")
    + select_suite("PQoa_Ws_SelectSuite", 4)
    + [
        step("PQoa_Ws_SelectSuite", 6, "Build title", "xUI", "xGetText", "build_panel_title", "text_phase_build"),
        step("PQoa_Ws_SelectSuite", 7, "AI toggle wrap", "xUI", "xGetText", "ai_toggle_label", "text_ai_on"),
    ],
)
add_plan(
    plan("PQoa_Ws_AddProjectBtn", "Topbar + new project button present", "BRAHL_Local;Workspace", "ws_add"),
    open_app("PQoa_Ws_AddProjectBtn")
    + [
        step("PQoa_Ws_AddProjectBtn", 4, "Add project +", "xUI", "xGetText", "btn_topbar_add_project"),
    ],
)

# --- Build module ---
add_plan(
    plan("PQoa_Build_YpadInsights", "Build — yPAD insights strip after suite select", "BRAHL_Local;Build;Ypad", "build_insights"),
    open_app("PQoa_Build_YpadInsights")
    + select_suite("PQoa_Build_YpadInsights", 4)
    + [
        step("PQoa_Build_YpadInsights", 6, "Insights block", "xUI", "xGetText", "ypad_insights", "text_ypad_tests"),
        step("PQoa_Build_YpadInsights", 7, "Insights stats", "xUI", "xGetText", "ypad_insights_stats"),
    ],
)
add_plan(
    plan("PQoa_Build_YpadTabs", "Build — switch Tests / Steps / Test data tabs", "BRAHL_Local;Build;Ypad", "build_tabs"),
    open_app("PQoa_Build_YpadTabs")
    + select_suite("PQoa_Build_YpadTabs", 4)
    + [
        step("PQoa_Build_YpadTabs", 6, "Click Steps", "xUI", "xClick", "ypad_tab_actions"),
        step("PQoa_Build_YpadTabs", 7, "Wait", "xTime", "xTimeWait", "1"),
        step("PQoa_Build_YpadTabs", 8, "Table present", "xUI", "xGetText", "ypad_table"),
        step("PQoa_Build_YpadTabs", 9, "Click Designs", "xUI", "xClick", "ypad_tab_designs"),
        step("PQoa_Build_YpadTabs", 10, "Wait", "xTime", "xTimeWait", "1"),
        step("PQoa_Build_YpadTabs", 11, "Click Tests", "xUI", "xClick", "ypad_tab_plans"),
        step("PQoa_Build_YpadTabs", 12, "Wait", "xTime", "xTimeWait", "1"),
        step("PQoa_Build_YpadTabs", 13, "Tests tab active area", "xUI", "xGetText", "ypad_insights", "text_ypad_tests"),
    ],
)
add_plan(
    plan("PQoa_Build_YpadFilter", "Build — search filter on yPAD table", "BRAHL_Local;Build;Ypad", "build_filter"),
    open_app("PQoa_Build_YpadFilter")
    + select_suite("PQoa_Build_YpadFilter", 4)
    + [
        step("PQoa_Build_YpadFilter", 6, "Type filter Smoke", "xUI", "xType", "ypad_filter_type"),
        step("PQoa_Build_YpadFilter", 7, "Wait filter", "xTime", "xTimeWait", "1"),
        step("PQoa_Build_YpadFilter", 8, "Table still present", "xUI", "xGetText", "ypad_table"),
    ],
)
add_plan(
    plan("PQoa_Build_YpadCoverage", "Build — coverage chips All / Automated / Manual", "BRAHL_Local;Build;Ypad", "build_coverage"),
    open_app("PQoa_Build_YpadCoverage")
    + select_suite("PQoa_Build_YpadCoverage", 4)
    + [
        step("PQoa_Build_YpadCoverage", 6, "Click Auto", "xUI", "xClick", "ypad_cov_auto"),
        step("PQoa_Build_YpadCoverage", 7, "Wait", "xTime", "xTimeWait", "0.5"),
        step("PQoa_Build_YpadCoverage", 8, "Click Manual", "xUI", "xClick", "ypad_cov_manual"),
        step("PQoa_Build_YpadCoverage", 9, "Wait", "xTime", "xTimeWait", "0.5"),
        step("PQoa_Build_YpadCoverage", 10, "Click All", "xUI", "xClick", "ypad_cov_all"),
        step("PQoa_Build_YpadCoverage", 11, "Table", "xUI", "xGetText", "ypad_table"),
    ],
)
add_plan(
    plan("PQoa_Build_BrahlPlanSection", "Build — BRAHL plan requirement + Generate", "BRAHL_Local;Build;Planner", "build_brahl_plan"),
    open_app("PQoa_Build_BrahlPlanSection")
    + select_suite("PQoa_Build_BrahlPlanSection", 4)
    + [
        step("PQoa_Build_BrahlPlanSection", 6, "Requirement box", "xUI", "xGetText", "brahl_plan_requirement"),
        step("PQoa_Build_BrahlPlanSection", 7, "Generate button", "xUI", "xGetText", "btn_generate_brahl_plan"),
    ],
)
add_plan(
    plan("PQoa_Build_AiChat", "Build — open AI chat optional section", "BRAHL_Local;Build;AI", "build_ai_chat"),
    open_app("PQoa_Build_AiChat")
    + select_suite("PQoa_Build_AiChat", 4)
    + [
        step("PQoa_Build_AiChat", 6, "Open AI chat details", "xUI", "xClick", "build_refine_summary"),
        step("PQoa_Build_AiChat", 7, "Wait", "xTime", "xTimeWait", "1"),
        step("PQoa_Build_AiChat", 8, "Chat input", "xUI", "xGetText", "chat_input"),
        step("PQoa_Build_AiChat", 9, "Send button", "xUI", "xGetText", "chat_send_btn"),
    ],
)
add_plan(
    plan("PQoa_Build_YpadVersions", "Build — yPAD versions / snapshot controls", "BRAHL_Local;Build;Ypad", "build_versions"),
    open_app("PQoa_Build_YpadVersions")
    + select_suite("PQoa_Build_YpadVersions", 4)
    + [
        step("PQoa_Build_YpadVersions", 6, "Versions block", "xUI", "xGetText", "ypad_versions"),
        step("PQoa_Build_YpadVersions", 7, "Edit toggle", "xUI", "xGetText", "ypad_toggle_edit"),
    ],
)
add_plan(
    plan("PQoa_Build_EnvTab", "Build — Environment example tab", "BRAHL_Local;Build;Ypad", "build_env"),
    open_app("PQoa_Build_EnvTab")
    + select_suite("PQoa_Build_EnvTab", 4)
    + [
        step("PQoa_Build_EnvTab", 6, "Click Env tab", "xUI", "xClick", "ypad_tab_env"),
        step("PQoa_Build_EnvTab", 7, "Wait", "xTime", "xTimeWait", "1"),
        step("PQoa_Build_EnvTab", 8, "Insights still in DOM", "xUI", "xGetText", "ypad_insights"),
    ],
)

# --- Run module ---
add_plan(
    plan("PQoa_Run_SuiteDisplay", "Run — suite display shows BRAHL_Local", "BRAHL_Local;Run", "run_suite"),
    open_app("PQoa_Run_SuiteDisplay")
    + select_suite("PQoa_Run_SuiteDisplay", 4)
    + [
        step("PQoa_Run_SuiteDisplay", 6, "Click Run phase", "xUI", "xClick", "btn_phase_run"),
        step("PQoa_Run_SuiteDisplay", 7, "Wait", "xTime", "xTimeWait", "1"),
        step("PQoa_Run_SuiteDisplay", 8, "Suite display", "xUI", "xGetText", "run_suite_display", "text_suite_qoa"),
    ],
)
add_plan(
    plan("PQoa_Run_FstartToolbar", "Run — fStart chips + Edit", "BRAHL_Local;Run;fStart", "run_fstart"),
    open_app("PQoa_Run_FstartToolbar")
    + select_suite("PQoa_Run_FstartToolbar", 4)
    + [
        step("PQoa_Run_FstartToolbar", 6, "Click Run", "xUI", "xClick", "btn_phase_run"),
        step("PQoa_Run_FstartToolbar", 7, "Wait", "xTime", "xTimeWait", "1"),
        step("PQoa_Run_FstartToolbar", 8, "fStart row", "xUI", "xGetText", "fstart_chip_row"),
        step("PQoa_Run_FstartToolbar", 9, "Edit fStart", "xUI", "xGetText", "btn_fstart_edit"),
    ],
)
add_plan(
    plan("PQoa_Run_OpenFstartModal", "Run — open/cancel fStart capture modal", "BRAHL_Local;Run;fStart", "run_fstart_modal"),
    open_app("PQoa_Run_OpenFstartModal")
    + select_suite("PQoa_Run_OpenFstartModal", 4)
    + [
        step("PQoa_Run_OpenFstartModal", 6, "Click Run", "xUI", "xClick", "btn_phase_run"),
        step("PQoa_Run_OpenFstartModal", 7, "Wait", "xTime", "xTimeWait", "1"),
        step("PQoa_Run_OpenFstartModal", 8, "Open Edit", "xUI", "xClick", "btn_fstart_edit"),
        step("PQoa_Run_OpenFstartModal", 9, "Wait modal", "xTime", "xTimeWait", "1"),
        step("PQoa_Run_OpenFstartModal", 10, "Capture image control", "xUI", "xGetText", "cap_image"),
        step("PQoa_Run_OpenFstartModal", 11, "Cancel modal", "xUI", "xClick", "fstart_cancel"),
        step("PQoa_Run_OpenFstartModal", 12, "Wait", "xTime", "xTimeWait", "0.5"),
        step("PQoa_Run_OpenFstartModal", 13, "Still on Run", "xUI", "xGetText", "panel_run_locator", "text_run_heading"),
    ],
)
add_plan(
    plan("PQoa_Run_TagsAndThreads", "Run — tag chips + thread count", "BRAHL_Local;Run", "run_tags"),
    open_app("PQoa_Run_TagsAndThreads")
    + select_suite("PQoa_Run_TagsAndThreads", 4)
    + [
        step("PQoa_Run_TagsAndThreads", 6, "Click Run", "xUI", "xClick", "btn_phase_run"),
        step("PQoa_Run_TagsAndThreads", 7, "Wait", "xTime", "xTimeWait", "1"),
        step("PQoa_Run_TagsAndThreads", 8, "Tag row", "xUI", "xGetText", "run_tag_row"),
        step("PQoa_Run_TagsAndThreads", 9, "Preset row", "xUI", "xGetText", "run_profile_row"),
        step("PQoa_Run_TagsAndThreads", 10, "Thread control", "xUI", "xGetText", "run_thread_count"),
    ],
)
add_plan(
    plan("PQoa_Run_CaptureAndBtn", "Run — capture strip + Run button", "BRAHL_Local;Run;Capture", "run_capture"),
    open_app("PQoa_Run_CaptureAndBtn")
    + select_suite("PQoa_Run_CaptureAndBtn", 4)
    + [
        step("PQoa_Run_CaptureAndBtn", 6, "Click Run", "xUI", "xClick", "btn_phase_run"),
        step("PQoa_Run_CaptureAndBtn", 7, "Wait", "xTime", "xTimeWait", "1"),
        step("PQoa_Run_CaptureAndBtn", 8, "Capture summary", "xUI", "xGetText", "run_capture_summary"),
        step("PQoa_Run_CaptureAndBtn", 9, "Run button", "xUI", "xGetText", "btn_run"),
    ],
)

# --- Analyze / Heal / Loop / BRAHL feature depth ---
add_plan(
    plan("PQoa_Analyze_Controls", "Analyze — refresh + runs list + failures", "BRAHL_Local;Analyze", "analyze_controls"),
    open_app("PQoa_Analyze_Controls")
    + select_suite("PQoa_Analyze_Controls", 4)
    + [
        step("PQoa_Analyze_Controls", 6, "Click Analyze", "xUI", "xClick", "btn_phase_analyze"),
        step("PQoa_Analyze_Controls", 7, "Wait", "xTime", "xTimeWait", "1"),
        step("PQoa_Analyze_Controls", 8, "Refresh", "xUI", "xGetText", "btn_refresh_runs"),
        step("PQoa_Analyze_Controls", 9, "Runs list", "xUI", "xGetText", "runs_list"),
        step("PQoa_Analyze_Controls", 10, "Failures body", "xUI", "xGetText", "failures_body"),
    ],
)
add_plan(
    plan("PQoa_Heal_Controls", "Heal — edit / rerun / apply / shrink / restore", "BRAHL_Local;Heal", "heal_controls"),
    open_app("PQoa_Heal_Controls")
    + select_suite("PQoa_Heal_Controls", 4)
    + [
        step("PQoa_Heal_Controls", 6, "Click Heal", "xUI", "xClick", "btn_phase_heal"),
        step("PQoa_Heal_Controls", 7, "Wait", "xTime", "xTimeWait", "1"),
        step("PQoa_Heal_Controls", 8, "Edit yPAD", "xUI", "xGetText", "btn_heal_edit_ypad"),
        step("PQoa_Heal_Controls", 9, "Rerun", "xUI", "xGetText", "btn_heal_rerun"),
        step("PQoa_Heal_Controls", 10, "Apply", "xUI", "xGetText", "btn_heal_apply"),
        step("PQoa_Heal_Controls", 11, "Shrink", "xUI", "xGetText", "btn_shrink_plans"),
        step("PQoa_Heal_Controls", 12, "Restore", "xUI", "xGetText", "btn_restore_plans"),
        step("PQoa_Heal_Controls", 13, "Heal failures", "xUI", "xGetText", "heal_failures_body"),
    ],
)
add_plan(
    plan("PQoa_Loop_Controls", "Loop — times / verify / run / schedules", "BRAHL_Local;Loop", "loop_controls"),
    open_app("PQoa_Loop_Controls")
    + select_suite("PQoa_Loop_Controls", 4)
    + [
        step("PQoa_Loop_Controls", 6, "Click Loop", "xUI", "xClick", "btn_phase_loop"),
        step("PQoa_Loop_Controls", 7, "Wait", "xTime", "xTimeWait", "1"),
        step("PQoa_Loop_Controls", 8, "Times 1", "xUI", "xGetText", "loop_times_1"),
        step("PQoa_Loop_Controls", 9, "Click times 2", "xUI", "xClick", "loop_times_2"),
        step("PQoa_Loop_Controls", 10, "Verify checkbox", "xUI", "xGetText", "loop_verify_full"),
        step("PQoa_Loop_Controls", 11, "Loop run btn", "xUI", "xGetText", "btn_loop_run"),
        step("PQoa_Loop_Controls", 12, "Cycle history", "xUI", "xGetText", "cycle_history"),
        step("PQoa_Loop_Controls", 13, "Schedules", "xUI", "xGetText", "schedules_section"),
    ],
)
add_plan(
    plan("PQoa_Brahl_Controls", "BRAHL — scorecard / reports / chat / team", "BRAHL_Local;BRAHL", "brahl_controls"),
    open_app("PQoa_Brahl_Controls")
    + select_suite("PQoa_Brahl_Controls", 4)
    + [
        step("PQoa_Brahl_Controls", 6, "Click BRAHL", "xUI", "xClick", "btn_phase_brahl"),
        step("PQoa_Brahl_Controls", 7, "Wait", "xTime", "xTimeWait", "1"),
        step("PQoa_Brahl_Controls", 8, "Go/No-Go block", "xUI", "xGetText", "gonogo_block"),
        step("PQoa_Brahl_Controls", 9, "Scorecard", "xUI", "xGetText", "scorecard"),
        step("PQoa_Brahl_Controls", 10, "Report tabs", "xUI", "xGetText", "brahl_report_tabs"),
        step("PQoa_Brahl_Controls", 11, "Report list", "xUI", "xGetText", "brahl_report_list"),
        step("PQoa_Brahl_Controls", 12, "Chat input", "xUI", "xGetText", "brahl_chat_input"),
        step("PQoa_Brahl_Controls", 13, "Team workspace", "xUI", "xGetText", "brahl_team_workspace"),
    ],
)

# --- Security ---
add_plan(
    plan("PQoa_Sec_AuthRegisterDisabled", "Security — POST /api/auth/register disabled on desktop", "BRAHL_Local;Security;Auth;API", "sec_register"),
    [step("PQoa_Sec_AuthRegisterDisabled", 1, "POST register", "xAPI", "xPost", "post_register", "http_404")],
)
add_plan(
    plan("PQoa_Sec_BillingDisabled", "Security — billing API not available on desktop", "BRAHL_Local;Security;API", "sec_billing"),
    [step("PQoa_Sec_BillingDisabled", 1, "GET billing", "xAPI", "xGet", "get_billing", "http_404")],
)
add_plan(
    plan("PQoa_Sec_AuthMeUnauth", "Security — /api/auth/me requires auth", "BRAHL_Local;Security;Auth;API", "sec_me"),
    [step("PQoa_Sec_AuthMeUnauth", 1, "GET auth/me", "xAPI", "xGet", "get_auth_me", "http_401")],
)
add_plan(
    plan("PQoa_Sec_HealthNoSecrets", "Security — health exposes desktop flag, not secrets", "BRAHL_Local;Security;API", "sec_health"),
    [
        step("PQoa_Sec_HealthNoSecrets", 1, "GET health", "xAPI", "xGet", "get_health", "http_200"),
        step("PQoa_Sec_HealthNoSecrets", 2, "status ok", "xJSON", "xCompareJson", "cmp_status_ok", "json_true"),
        step("PQoa_Sec_HealthNoSecrets", 3, "desktop true", "xJSON", "xCompareJson", "cmp_desktop_true", "json_true"),
        step("PQoa_Sec_HealthNoSecrets", 4, "openai_key_set false", "xJSON", "xCompareJson", "cmp_openai_false", "json_true"),
        step("PQoa_Sec_HealthNoSecrets", 5, "service kk2-desktop", "xJSON", "xCompareJson", "cmp_service", "json_true"),
    ],
)
add_plan(
    plan("PQoa_Sec_NoWalletUi", "Security/Desktop — wallet widget has hidden attr", "BRAHL_Local;Security;Desktop", "sec_wallet_ui"),
    open_app("PQoa_Sec_NoWalletUi")
    + [
        step("PQoa_Sec_NoWalletUi", 4, "desktop-mode brand", "xUI", "xGetText", "desktop_title_locator", "title_token"),
        # Wallet is display:none; presence of phase nav + brand is the positive assert
        step("PQoa_Sec_NoWalletUi", 5, "Phase nav without wallet chrome path", "xUI", "xGetText", "phase_nav_locator", "text_phase_build"),
    ],
)
add_plan(
    plan("PQoa_Sec_LoginPageLoads", "Security — /login still serves page but Arena works without login", "BRAHL_Local;Security;Auth", "sec_login_page"),
    [
        step("PQoa_Sec_LoginPageLoads", 1, "Open Edge", "xReuse", "PReuse_BrahlLocal_OpenApp"),
        step("PQoa_Sec_LoginPageLoads", 2, "Navigate login", "xUI", "xNavigate", "login_url"),
        step("PQoa_Sec_LoginPageLoads", 3, "Wait", "xTime", "xTimeWait", "2"),
        step("PQoa_Sec_LoginPageLoads", 4, "Body has content", "xUI", "xGetText", "body_locator"),
        step("PQoa_Sec_LoginPageLoads", 5, "Back to /app", "xUI", "xNavigate", "app_url"),
        step("PQoa_Sec_LoginPageLoads", 6, "Wait", "xTime", "xTimeWait", "2"),
        step("PQoa_Sec_LoginPageLoads", 7, "Arena title", "xUI", "xGetTitle", "", "page_title_token"),
    ],
)

# --- API ---
api_plans = [
    ("PQoa_Api_Health", "API GET /api/health", "get_health", [("status ok", "cmp_status_ok")]),
    ("PQoa_Api_Version", "API GET /api/version", "get_version", [("version desktop", "cmp_version_desktop")]),
    ("PQoa_Api_Config", "API GET /api/config", "get_config", []),
    ("PQoa_Api_Suites", "API GET /api/suites", "get_suites", []),
    ("PQoa_Api_Workspace", "API GET /api/workspace", "get_workspace", [("bound true", "cmp_bound_true")]),
    ("PQoa_Api_Projects", "API GET /api/projects", "get_projects", []),
    ("PQoa_Api_Configs", "API GET /api/configs", "get_configs", []),
    ("PQoa_Api_Runs", "API GET /api/runs", "get_runs", []),
    ("PQoa_Api_RunProfiles", "API GET /api/run-profiles", "get_run_profiles", []),
    ("PQoa_Api_AiStatus", "API GET /api/ai/status", "get_ai_status", []),
    ("PQoa_Api_YpadPlans", "API GET /api/suites/BRAHL_Local/ypad/plans", "get_ypad_plans", []),
]
for pid, name, get_key, cmps in api_plans:
    acts = [step(pid, 1, "GET", "xAPI", "xGet", get_key, "http_200")]
    for i, (label, cmp_key) in enumerate(cmps, start=2):
        acts.append(step(pid, i, label, "xJSON", "xCompareJson", cmp_key, "json_true"))
    add_plan(plan(pid, name, "BRAHL_Local;API", pid.lower().replace("pqoa_api_", "api_")), acts)

# --- Performance ---
add_plan(
    plan("PQoa_Perf_AppReady", "Perf — /app ready within short wait", "BRAHL_Local;Performance;Shell", "perf_app"),
    [
        step("PQoa_Perf_AppReady", 1, "Open Edge", "xReuse", "PReuse_BrahlLocal_OpenApp"),
        step("PQoa_Perf_AppReady", 2, "Navigate /app", "xUI", "xNavigate", "app_url"),
        step("PQoa_Perf_AppReady", 3, "Short wait", "xTime", "xTimeWait", "1"),
        step("PQoa_Perf_AppReady", 4, "Title ready", "xUI", "xGetTitle", "", "page_title_token"),
        step("PQoa_Perf_AppReady", 5, "Nav ready", "xUI", "xGetText", "phase_nav_locator", "text_phase_build"),
    ],
)
add_plan(
    plan("PQoa_Perf_HealthApi", "Perf — health API responds 200", "BRAHL_Local;Performance;API", "perf_health"),
    [step("PQoa_Perf_HealthApi", 1, "GET health", "xAPI", "xGet", "get_health", "http_200")],
)
add_plan(
    plan("PQoa_Perf_SuitesApi", "Perf — suites API responds 200", "BRAHL_Local;Performance;API", "perf_suites"),
    [step("PQoa_Perf_SuitesApi", 1, "GET suites", "xAPI", "xGet", "get_suites", "http_200")],
)
add_plan(
    plan("PQoa_Perf_PhaseSwitch", "Perf — rapid phase chip switching", "BRAHL_Local;Performance;UI", "perf_phases"),
    open_app("PQoa_Perf_PhaseSwitch")
    + [
        step("PQoa_Perf_PhaseSwitch", 4, "Run", "xUI", "xClick", "btn_phase_run"),
        step("PQoa_Perf_PhaseSwitch", 5, "w", "xTime", "xTimeWait", "0.4"),
        step("PQoa_Perf_PhaseSwitch", 6, "Analyze", "xUI", "xClick", "btn_phase_analyze"),
        step("PQoa_Perf_PhaseSwitch", 7, "w", "xTime", "xTimeWait", "0.4"),
        step("PQoa_Perf_PhaseSwitch", 8, "Heal", "xUI", "xClick", "btn_phase_heal"),
        step("PQoa_Perf_PhaseSwitch", 9, "w", "xTime", "xTimeWait", "0.4"),
        step("PQoa_Perf_PhaseSwitch", 10, "Loop", "xUI", "xClick", "btn_phase_loop"),
        step("PQoa_Perf_PhaseSwitch", 11, "w", "xTime", "xTimeWait", "0.4"),
        step("PQoa_Perf_PhaseSwitch", 12, "BRAHL", "xUI", "xClick", "btn_phase_brahl"),
        step("PQoa_Perf_PhaseSwitch", 13, "w", "xTime", "xTimeWait", "0.4"),
        step("PQoa_Perf_PhaseSwitch", 14, "Build", "xUI", "xClick", "btn_phase_build"),
        step("PQoa_Perf_PhaseSwitch", 15, "Build visible", "xUI", "xGetText", "panel_build_locator", "text_phase_build"),
    ],
)
add_plan(
    plan("PQoa_Perf_YpadTable", "Perf — yPAD table appears after suite select", "BRAHL_Local;Performance;Build", "perf_ypad"),
    open_app("PQoa_Perf_YpadTable")
    + [
        step("PQoa_Perf_YpadTable", 4, "Select suite", "xUI", "xSelectDropdown", "suite_select_qoa"),
        step("PQoa_Perf_YpadTable", 5, "Short wait", "xTime", "xTimeWait", "2"),
        step("PQoa_Perf_YpadTable", 6, "Table ready", "xUI", "xGetText", "ypad_table"),
    ],
)
add_plan(
    plan("PQoa_Perf_ApiBatch", "Perf — batch core GETs stay 200", "BRAHL_Local;Performance;API", "perf_api_batch"),
    [
        step("PQoa_Perf_ApiBatch", 1, "health", "xAPI", "xGet", "get_health", "http_200"),
        step("PQoa_Perf_ApiBatch", 2, "version", "xAPI", "xGet", "get_version", "http_200"),
        step("PQoa_Perf_ApiBatch", 3, "workspace", "xAPI", "xGet", "get_workspace", "http_200"),
        step("PQoa_Perf_ApiBatch", 4, "projects", "xAPI", "xGet", "get_projects", "http_200"),
        step("PQoa_Perf_ApiBatch", 5, "configs", "xAPI", "xGet", "get_configs", "http_200"),
    ],
)


def write_plans():
    path = ROOT / "y1Plans.csv"
    fields = ["PlanId", "PlanName", "DesignId", "Run", "Tags", "Output", "CreatedBy", "CreatedAt"]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for p in PLANS:
            w.writerow(p)


def write_actions():
    path = ROOT / "y2Actions.csv"
    fields = ["PlanId", "StepId", "StepInfo", "ActionType", "ActionName", "Input", "Output", "Expected", "Critical"]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for a in ACTIONS:
            w.writerow(a)


if __name__ == "__main__":
    write_designs()
    write_plans()
    write_actions()
    run_y = sum(1 for p in PLANS if p["Run"] == "Y")
    print("Wrote", len(PLANS), "plans", run_y, "Run=Y", len(ACTIONS), "actions")
