#!/usr/bin/env python3
"""Generate FoXYiZ/y/UI_internet demo yPAD (the-internet.herokuapp.com)."""
from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # FoXYiZ
SUITE = ROOT / "y" / "UI_internet"
FSTART = ROOT / "f" / "fStart" / "UI_internet.json"
BASE = "https://the-internet.herokuapp.com"
TS = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
AUTHOR = "QA_Hunter+Demo"


def wcsv(path: Path, headers: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow({h: row.get(h, "") for h in headers})


def main() -> None:
    SUITE.mkdir(parents=True, exist_ok=True)
    (SUITE / "payloads").mkdir(exist_ok=True)
    sample = SUITE / "payloads" / "upload_demo.txt"
    sample.write_text(
        "FoXYiZ UI_internet demo upload\nHello from BRAHL Local sample yPAD.\n",
        encoding="utf-8",
    )

    designs: dict[str, str] = {
        "base_url": f"{BASE}/",
        "body_locator": "css=body",
        "h3_locator": "css=h3",
        "h2_locator": "css=h2",
        "flash_locator": "css=#flash",
        "content_locator": "css=#content",
        # pages
        "url_home": f"{BASE}/",
        "url_ab": f"{BASE}/abtest",
        "url_add_remove": f"{BASE}/add_remove_elements/",
        "url_basic_auth": f"https://admin:admin@the-internet.herokuapp.com/basic_auth",
        "url_broken": f"{BASE}/broken_images",
        "url_challenging": f"{BASE}/challenging_dom",
        "url_checkboxes": f"{BASE}/checkboxes",
        "url_context": f"{BASE}/context_menu",
        "url_disappear": f"{BASE}/disappearing_elements",
        "url_drag": f"{BASE}/drag_and_drop",
        "url_dropdown": f"{BASE}/dropdown",
        "url_dyn_content": f"{BASE}/dynamic_content",
        "url_dyn_controls": f"{BASE}/dynamic_controls",
        "url_dyn_load1": f"{BASE}/dynamic_loading/1",
        "url_dyn_load2": f"{BASE}/dynamic_loading/2",
        "url_entry_ad": f"{BASE}/entry_ad",
        "url_upload": f"{BASE}/upload",
        "url_floating": f"{BASE}/floating_menu",
        "url_forgot": f"{BASE}/forgot_password",
        "url_login": f"{BASE}/login",
        "url_slider": f"{BASE}/horizontal_slider",
        "url_hovers": f"{BASE}/hovers",
        "url_inputs": f"{BASE}/inputs",
        "url_alerts": f"{BASE}/javascript_alerts",
        "url_keys": f"{BASE}/key_presses",
        "url_large": f"{BASE}/large",
        "url_notify": f"{BASE}/notification_message_rendered",
        "url_redirect": f"{BASE}/redirector",
        "url_status": f"{BASE}/status_codes",
        "url_status_404": f"{BASE}/status_codes/404",
        "url_tables": f"{BASE}/tables",
        "url_typos": f"{BASE}/typos",
        "url_shifting": f"{BASE}/shifting_content",
        # home
        "text_welcome": "Welcome to the-internet",
        "link_login": "css=a[href='/login']",
        # add/remove
        "btn_add_element": "css=button[onclick='addElement()']",
        "btn_delete": "css=button.added-manually",
        "text_add_remove": "Add/Remove Elements",
        # basic auth
        "text_basic_auth": "Congratulations! You must have the proper credentials.",
        # broken images
        "text_broken": "Broken Images",
        "img_first": "css=.example img",
        # challenging DOM
        "text_challenging": "Challenging DOM",
        "btn_challenging": "css=.button",
        "table_cell": "css=#content table tbody tr:nth-of-type(1) td:nth-of-type(1)",
        # checkboxes
        "cb1": "css=#checkboxes input:nth-of-type(1)",
        "cb2": "css=#checkboxes input:nth-of-type(2)",
        "checked": "checked",
        "unchecked": "unchecked",
        # context menu
        "hotspot": "css=#hot-spot",
        "alert_accept": "accept",
        # disappearing
        "text_disappear": "Disappearing Elements",
        "nav_home": "css=ul li a[href='/']",
        # drag drop
        "dnd_ab": "css=#column-a;css=#column-b",
        "col_a": "css=#column-a",
        # dropdown
        "dd_option1": "css=#dropdown;1",
        "dd_option2": "css=#dropdown;2",
        "text_dropdown": "Dropdown List",
        # dynamic content
        "text_dyn_content": "Dynamic Content",
        "dyn_row": "css=#content .row .large-10",
        # dynamic controls
        "btn_remove": "css=#checkbox-example button",
        "btn_enable": "css=#input-example button",
        "dyn_message": "css=#message",
        "dyn_input": "css=#input-example input",
        "type_dyn_enabled": "BRAHL_enabled;css=#input-example input",
        "text_gone": "It's gone!",
        "text_enabled": "It's enabled!",
        # dynamic loading
        "btn_start": "css=#start button",
        "finish_locator": "css=#finish",
        "text_hello": "Hello World!",
        # entry ad
        "btn_modal_close": "css=.modal-footer p",
        "text_entry_ad": "Entry Ad",
        # upload
        "upload_file": f"css=#file-upload;y/UI_internet/payloads/upload_demo.txt",
        "btn_upload": "css=#file-submit",
        "text_uploaded": "File Uploaded!",
        # floating menu
        "text_floating": "Floating Menu",
        "menu_about": "css=a[href='#about']",
        # forgot password
        "type_email": "demo@foxyiz.example;css=#email",
        "btn_retrieve": "css=#form_submit",
        # login
        "type_user_ok": "tomsmith;css=#username",
        "type_pass_ok": "SuperSecretPassword!;css=#password",
        "type_user_bad": "wronguser;css=#username",
        "type_pass_bad": "wrongpass;css=#password",
        "btn_login": "css=button[type='submit']",
        "btn_logout": "css=a.button.secondary.radius",
        "text_login_ok": "You logged into a secure area!",
        "text_login_fail": "Your username is invalid!",
        "text_logout_ok": "You logged out of the secure area!",
        "text_secure": "Secure Area",
        # slider
        "slider": "css=input[type='range']",
        "keys_slider_right": "css=input[type='range'];ARROW_RIGHT",
        "slider_value": "css=#range",
        # hovers
        "hover_user1": "css=.figure:nth-of-type(1) img",
        "hover_caption1": "css=.figure:nth-of-type(1) .figcaption",
        "text_user1": "user1",
        # inputs
        "type_number": "42;css=input[type='number']",
        "input_number": "css=input[type='number']",
        # alerts
        "btn_js_alert": "xpath=//button[normalize-space()='Click for JS Alert']",
        "btn_js_confirm": "xpath=//button[normalize-space()='Click for JS Confirm']",
        "btn_js_prompt": "xpath=//button[normalize-space()='Click for JS Prompt']",
        "alert_dismiss": "dismiss",
        "alert_type_brahl": "type:BRAHL",
        "result_locator": "css=#result",
        "text_alert_ok": "You successfully clicked an alert",
        "text_confirm_ok": "You clicked: Ok",
        "text_confirm_cancel": "You clicked: Cancel",
        "text_prompt_brahl": "You entered: brahl",
        # keys
        "keys_enter": "css=#target;ENTER",
        "keys_tab": "css=#target;TAB",
        "key_result": "css=#result",
        "text_enter": "You entered: ENTER",
        # large DOM
        "text_large": "Large & Deep DOM",
        "large_cell": "css=#large-table tr:nth-of-type(2) td:nth-of-type(2)",
        # notification
        "link_click_here": "css=a[href='/notification_message']",
        "text_notification_hdr": "Notification Message",
        # redirect
        "link_redirect": "css=#redirect",
        "text_status_codes": "Status Codes",
        # status
        "link_status_404": "css=a[href='404']",
        "text_status_404": "404",
        # tables
        "text_tables": "Data Tables",
        "table1_cell": "css=#table1 tbody tr:nth-of-type(1) td:nth-of-type(1)",
        "table1_edit": "css=#table1 tbody tr:nth-of-type(1) a[href='#edit']",
        # typos / shifting
        "text_typos": "Typos",
        "text_shifting": "Shifting Content",
        # viewport
        "viewport_mobile": "390;844",
        "viewport_desktop": "1280;800",
    }

    y3_rows = [{"Type": "UI", "DataName": k, "D1": v} for k, v in designs.items()]

    plans: list[dict] = []
    actions: list[dict] = []

    def plan(
        pid: str,
        name: str,
        tags: str,
        output: str,
        run: str = "Y",
    ) -> None:
        plans.append(
            {
                "PlanId": pid,
                "PlanName": name,
                "DesignId": "D1",
                "Run": run,
                "Tags": tags,
                "Output": output,
                "CreatedBy": AUTHOR,
                "CreatedAt": TS,
            }
        )

    def step(
        pid: str,
        sid: int,
        info: str,
        atype: str,
        aname: str,
        inp: str = "",
        out: str = "",
        exp: str = "",
        crit: str = "Y",
    ) -> None:
        actions.append(
            {
                "PlanId": pid,
                "StepId": sid,
                "StepInfo": info,
                "ActionType": atype,
                "ActionName": aname,
                "Input": inp,
                "Output": out,
                "Expected": exp,
                "Critical": crit,
            }
        )

    def reuse_open(pid: str) -> int:
        step(pid, 1, "Reuse open browser + home", "xReuse", "PReuse_Inet_Open")
        return 2

    def nav_wait(pid: str, start: int, url_key: str, wait: str = "2") -> int:
        step(pid, start, f"Navigate {url_key}", "xUI", "xNavigate", url_key)
        step(pid, start + 1, "Settle", "xTime", "xTimeWait", wait)
        return start + 2

    # --- Reuse ---
    plan(
        "PReuse_Inet_Open",
        "Open Edge and load the-internet home",
        "Reuse",
        "site_loaded",
        run="N",
    )
    step("PReuse_Inet_Open", 1, "Open Edge", "xUI", "xOpenBrowser", "edge")
    step("PReuse_Inet_Open", 2, "Home", "xUI", "xNavigate", "base_url")
    step("PReuse_Inet_Open", 3, "Wait boot", "xTime", "xTimeWait", "2")
    step("PReuse_Inet_Open", 4, "Body present", "xUI", "xGetText", "body_locator", "", "text_welcome")

    # --- Smoke ---
    plan("PInet_Smoke_Home", "Smoke — home lists Available Examples", "UI_internet;Smoke;UI;Shell", "smoke_home")
    s = reuse_open("PInet_Smoke_Home")
    step("PInet_Smoke_Home", s, "Title Welcome", "xUI", "xGetText", "h2_locator", "", "text_welcome")
    step("PInet_Smoke_Home", s + 1, "Login link visible", "xUI", "xGetText", "link_login", "", "", "Y")

    plan("PInet_Smoke_LoginHappy", "Smoke — Form Auth happy path login", "UI_internet;Smoke;UI;Auth", "smoke_login")
    s = reuse_open("PInet_Smoke_LoginHappy")
    s = nav_wait("PInet_Smoke_LoginHappy", s, "url_login")
    step("PInet_Smoke_LoginHappy", s, "Username", "xUI", "xType", "type_user_ok")
    step("PInet_Smoke_LoginHappy", s + 1, "Password", "xUI", "xType", "type_pass_ok")
    step("PInet_Smoke_LoginHappy", s + 2, "Submit", "xUI", "xClick", "btn_login")
    step("PInet_Smoke_LoginHappy", s + 3, "Wait", "xTime", "xTimeWait", "1")
    step("PInet_Smoke_LoginHappy", s + 4, "Flash success", "xUI", "xGetText", "flash_locator", "", "text_login_ok")

    # --- Form Auth deep ---
    plan("PInet_Auth_BadLogin", "Auth — invalid credentials flash error", "UI_internet;UI;Auth;Negative", "auth_bad")
    s = reuse_open("PInet_Auth_BadLogin")
    s = nav_wait("PInet_Auth_BadLogin", s, "url_login")
    step("PInet_Auth_BadLogin", s, "Bad user", "xUI", "xType", "type_user_bad")
    step("PInet_Auth_BadLogin", s + 1, "Bad pass", "xUI", "xType", "type_pass_bad")
    step("PInet_Auth_BadLogin", s + 2, "Submit", "xUI", "xClick", "btn_login")
    step("PInet_Auth_BadLogin", s + 3, "Wait", "xTime", "xTimeWait", "1")
    step("PInet_Auth_BadLogin", s + 4, "Flash fail", "xUI", "xGetText", "flash_locator", "", "text_login_fail")

    plan("PInet_Auth_LoginLogout", "Auth — login then logout round-trip", "UI_internet;UI;Auth;Flow", "auth_logout")
    s = reuse_open("PInet_Auth_LoginLogout")
    s = nav_wait("PInet_Auth_LoginLogout", s, "url_login")
    step("PInet_Auth_LoginLogout", s, "User", "xUI", "xType", "type_user_ok")
    step("PInet_Auth_LoginLogout", s + 1, "Pass", "xUI", "xType", "type_pass_ok")
    step("PInet_Auth_LoginLogout", s + 2, "Submit", "xUI", "xClick", "btn_login")
    step("PInet_Auth_LoginLogout", s + 3, "Wait", "xTime", "xTimeWait", "1")
    step("PInet_Auth_LoginLogout", s + 4, "Secure heading", "xUI", "xGetText", "h2_locator", "", "text_secure")
    step("PInet_Auth_LoginLogout", s + 5, "Logout", "xUI", "xClick", "btn_logout")
    step("PInet_Auth_LoginLogout", s + 6, "Wait", "xTime", "xTimeWait", "1")
    step("PInet_Auth_LoginLogout", s + 7, "Logged out flash", "xUI", "xGetText", "flash_locator", "", "text_logout_ok")

    plan("PInet_Auth_BasicAuth", "Auth — Basic Auth via credentialed URL", "UI_internet;UI;Auth;Security", "auth_basic")
    s = reuse_open("PInet_Auth_BasicAuth")
    s = nav_wait("PInet_Auth_BasicAuth", s, "url_basic_auth", "2")
    step("PInet_Auth_BasicAuth", s, "Congrats text", "xUI", "xGetText", "body_locator", "", "text_basic_auth")

    # --- Classic controls ---
    plan("PInet_UI_Checkboxes", "UI — toggle checkboxes + assert state", "UI_internet;UI;Forms;Checkbox", "ui_cb")
    s = reuse_open("PInet_UI_Checkboxes")
    s = nav_wait("PInet_UI_Checkboxes", s, "url_checkboxes")
    step("PInet_UI_Checkboxes", s, "CB1 initially unchecked", "xUI", "xIsChecked", "cb1", "", "unchecked")
    step("PInet_UI_Checkboxes", s + 1, "CB2 initially checked", "xUI", "xIsChecked", "cb2", "", "checked")
    step("PInet_UI_Checkboxes", s + 2, "Click CB1", "xUI", "xClick", "cb1")
    step("PInet_UI_Checkboxes", s + 3, "CB1 now checked", "xUI", "xIsChecked", "cb1", "", "checked")
    step("PInet_UI_Checkboxes", s + 4, "Click CB2", "xUI", "xClick", "cb2")
    step("PInet_UI_Checkboxes", s + 5, "CB2 now unchecked", "xUI", "xIsChecked", "cb2", "", "unchecked")

    plan("PInet_UI_Dropdown", "UI — select dropdown Option 1 then 2", "UI_internet;UI;Forms;Dropdown", "ui_dd")
    s = reuse_open("PInet_UI_Dropdown")
    s = nav_wait("PInet_UI_Dropdown", s, "url_dropdown")
    step("PInet_UI_Dropdown", s, "Heading", "xUI", "xGetText", "h3_locator", "", "text_dropdown")
    step("PInet_UI_Dropdown", s + 1, "Select 1", "xUI", "xSelectDropdown", "dd_option1")
    step("PInet_UI_Dropdown", s + 2, "Select 2", "xUI", "xSelectDropdown", "dd_option2")

    plan("PInet_UI_Inputs", "UI — type number into Inputs page", "UI_internet;UI;Forms;Inputs", "ui_inputs")
    s = reuse_open("PInet_UI_Inputs")
    s = nav_wait("PInet_UI_Inputs", s, "url_inputs")
    step("PInet_UI_Inputs", s, "Type 42", "xUI", "xType", "type_number")
    step("PInet_UI_Inputs", s + 1, "Input still present", "xUI", "xGetText", "h3_locator", "", "", "Y")

    plan("PInet_UI_AddRemove", "UI — Add Element then Delete", "UI_internet;UI;DOM;AddRemove", "ui_add")
    s = reuse_open("PInet_UI_AddRemove")
    s = nav_wait("PInet_UI_AddRemove", s, "url_add_remove")
    step("PInet_UI_AddRemove", s, "Heading", "xUI", "xGetText", "h3_locator", "", "text_add_remove")
    step("PInet_UI_AddRemove", s + 1, "Add", "xUI", "xClick", "btn_add_element")
    step("PInet_UI_AddRemove", s + 2, "Wait", "xTime", "xTimeWait", "1")
    step("PInet_UI_AddRemove", s + 3, "Delete appears", "xUI", "xGetText", "btn_delete", "", "Delete")
    step("PInet_UI_AddRemove", s + 4, "Delete click", "xUI", "xClick", "btn_delete")

    plan("PInet_UI_DragDrop", "UI — drag Column A onto Column B", "UI_internet;UI;DnD", "ui_dnd")
    s = reuse_open("PInet_UI_DragDrop")
    s = nav_wait("PInet_UI_DragDrop", s, "url_drag")
    step("PInet_UI_DragDrop", s, "Perform DnD", "xUI", "xDragAndDrop", "dnd_ab")
    step("PInet_UI_DragDrop", s + 1, "Column A still present", "xUI", "xGetText", "col_a", "", "", "Y")

    plan("PInet_UI_Hovers", "UI — hover figure reveals user1 caption", "UI_internet;UI;Hover", "ui_hover")
    s = reuse_open("PInet_UI_Hovers")
    s = nav_wait("PInet_UI_Hovers", s, "url_hovers")
    step("PInet_UI_Hovers", s, "Hover user1", "xUI", "xHover", "hover_user1")
    step("PInet_UI_Hovers", s + 1, "Caption user1", "xUI", "xGetText", "hover_caption1", "", "text_user1")

    plan("PInet_UI_ContextMenu", "UI — right-click hotspot + accept alert", "UI_internet;UI;Context;Alert", "ui_ctx")
    s = reuse_open("PInet_UI_ContextMenu")
    s = nav_wait("PInet_UI_ContextMenu", s, "url_context")
    step("PInet_UI_ContextMenu", s, "Context click", "xUI", "xContextClick", "hotspot")
    step("PInet_UI_ContextMenu", s + 1, "Accept alert", "xUI", "xHandleAlert", "alert_accept")

    plan("PInet_UI_JsAlerts", "UI — JS Alert / Confirm / Prompt suite", "UI_internet;UI;Alert;Fancy", "ui_alerts")
    s = reuse_open("PInet_UI_JsAlerts")
    s = nav_wait("PInet_UI_JsAlerts", s, "url_alerts")
    step("PInet_UI_JsAlerts", s, "Click Alert", "xUI", "xClick", "btn_js_alert")
    step("PInet_UI_JsAlerts", s + 1, "Accept", "xUI", "xHandleAlert", "alert_accept")
    step("PInet_UI_JsAlerts", s + 2, "Result alert", "xUI", "xGetText", "result_locator", "", "text_alert_ok")
    step("PInet_UI_JsAlerts", s + 3, "Click Confirm", "xUI", "xClick", "btn_js_confirm")
    step("PInet_UI_JsAlerts", s + 4, "Accept confirm", "xUI", "xHandleAlert", "alert_accept")
    step("PInet_UI_JsAlerts", s + 5, "Result Ok", "xUI", "xGetText", "result_locator", "", "text_confirm_ok")
    step("PInet_UI_JsAlerts", s + 6, "Click Confirm again", "xUI", "xClick", "btn_js_confirm")
    step("PInet_UI_JsAlerts", s + 7, "Dismiss", "xUI", "xHandleAlert", "alert_dismiss")
    step("PInet_UI_JsAlerts", s + 8, "Result Cancel", "xUI", "xGetText", "result_locator", "", "text_confirm_cancel")
    step("PInet_UI_JsAlerts", s + 9, "Click Prompt", "xUI", "xClick", "btn_js_prompt")
    step("PInet_UI_JsAlerts", s + 10, "Type BRAHL", "xUI", "xHandleAlert", "alert_type_brahl")
    step("PInet_UI_JsAlerts", s + 11, "Result prompt", "xUI", "xGetText", "result_locator", "", "text_prompt_brahl")

    plan("PInet_UI_KeyPresses", "UI — send ENTER and assert key result", "UI_internet;UI;Keys", "ui_keys")
    s = reuse_open("PInet_UI_KeyPresses")
    s = nav_wait("PInet_UI_KeyPresses", s, "url_keys")
    step("PInet_UI_KeyPresses", s, "ENTER", "xUI", "xSendKeys", "keys_enter")
    step("PInet_UI_KeyPresses", s + 1, "Result ENTER", "xUI", "xGetText", "key_result", "", "text_enter")

    plan("PInet_UI_Slider", "UI — nudge horizontal slider with ARROW_RIGHT", "UI_internet;UI;Slider", "ui_slider")
    s = reuse_open("PInet_UI_Slider")
    s = nav_wait("PInet_UI_Slider", s, "url_slider")
    step("PInet_UI_Slider", s, "Focus + ARROW_RIGHT", "xUI", "xSendKeys", "keys_slider_right")
    step("PInet_UI_Slider", s + 1, "Value element present", "xUI", "xGetText", "slider_value", "", "", "Y")

    plan("PInet_UI_Upload", "UI — upload sample text file", "UI_internet;UI;Upload;File", "ui_upload")
    s = reuse_open("PInet_UI_Upload")
    s = nav_wait("PInet_UI_Upload", s, "url_upload")
    step("PInet_UI_Upload", s, "Choose file", "xUI", "xUploadFile", "upload_file")
    step("PInet_UI_Upload", s + 1, "Submit", "xUI", "xClick", "btn_upload")
    step("PInet_UI_Upload", s + 2, "Wait", "xTime", "xTimeWait", "2")
    step("PInet_UI_Upload", s + 3, "Uploaded banner", "xUI", "xGetText", "h3_locator", "", "text_uploaded")

    # --- Dynamic / async ---
    plan("PInet_UI_DynLoading1", "UI — Dynamic Loading example 1 (hidden → Hello World)", "UI_internet;UI;Wait;Dynamic", "ui_dyn1")
    s = reuse_open("PInet_UI_DynLoading1")
    s = nav_wait("PInet_UI_DynLoading1", s, "url_dyn_load1")
    step("PInet_UI_DynLoading1", s, "Start", "xUI", "xClick", "btn_start")
    step("PInet_UI_DynLoading1", s + 1, "Wait render", "xTime", "xTimeWait", "8")
    step("PInet_UI_DynLoading1", s + 2, "Hello World", "xUI", "xGetText", "finish_locator", "", "text_hello")

    plan("PInet_UI_DynLoading2", "UI — Dynamic Loading example 2 (rendered later)", "UI_internet;UI;Wait;Dynamic", "ui_dyn2")
    s = reuse_open("PInet_UI_DynLoading2")
    s = nav_wait("PInet_UI_DynLoading2", s, "url_dyn_load2")
    step("PInet_UI_DynLoading2", s, "Start", "xUI", "xClick", "btn_start")
    step("PInet_UI_DynLoading2", s + 1, "Wait render", "xTime", "xTimeWait", "8")
    step("PInet_UI_DynLoading2", s + 2, "Hello World", "xUI", "xGetText", "finish_locator", "", "text_hello")

    plan("PInet_UI_DynControls", "UI — Dynamic Controls remove checkbox + enable input", "UI_internet;UI;Dynamic;Forms", "ui_dync")
    s = reuse_open("PInet_UI_DynControls")
    s = nav_wait("PInet_UI_DynControls", s, "url_dyn_controls")
    step("PInet_UI_DynControls", s, "Remove", "xUI", "xClick", "btn_remove")
    step("PInet_UI_DynControls", s + 1, "Wait gone", "xTime", "xTimeWait", "6")
    step("PInet_UI_DynControls", s + 2, "It's gone", "xUI", "xGetText", "dyn_message", "", "text_gone")
    step("PInet_UI_DynControls", s + 3, "Enable", "xUI", "xClick", "btn_enable")
    step("PInet_UI_DynControls", s + 4, "Wait enabled", "xTime", "xTimeWait", "6")
    step("PInet_UI_DynControls", s + 5, "It's enabled", "xUI", "xGetText", "dyn_message", "", "text_enabled")
    step("PInet_UI_DynControls", s + 6, "Type into enabled", "xUI", "xType", "type_dyn_enabled")

    plan("PInet_UI_DynContent", "UI — Dynamic Content page loads rows", "UI_internet;UI;Dynamic;Content", "ui_dyncnt")
    s = reuse_open("PInet_UI_DynContent")
    s = nav_wait("PInet_UI_DynContent", s, "url_dyn_content")
    step("PInet_UI_DynContent", s, "Heading", "xUI", "xGetText", "h3_locator", "", "text_dyn_content")
    step("PInet_UI_DynContent", s + 1, "Row text present", "xUI", "xGetText", "dyn_row", "", "", "Y")

    plan("PInet_UI_EntryAd", "UI — close Entry Ad modal", "UI_internet;UI;Modal", "ui_ad")
    s = reuse_open("PInet_UI_EntryAd")
    s = nav_wait("PInet_UI_EntryAd", s, "url_entry_ad", "3")
    step("PInet_UI_EntryAd", s, "Close modal", "xUI", "xClick", "btn_modal_close")
    step("PInet_UI_EntryAd", s + 1, "Heading remains", "xUI", "xGetText", "h3_locator", "", "text_entry_ad")

    # --- Navigation / content ---
    plan("PInet_UI_ABTest", "UI — A/B Testing variant heading", "UI_internet;UI;AB", "ui_ab")
    s = reuse_open("PInet_UI_ABTest")
    s = nav_wait("PInet_UI_ABTest", s, "url_ab")
    step("PInet_UI_ABTest", s, "Heading present", "xUI", "xGetText", "h3_locator", "", "", "Y")

    plan("PInet_UI_Disappear", "UI — Disappearing Elements nav Home", "UI_internet;UI;Nav", "ui_dis")
    s = reuse_open("PInet_UI_Disappear")
    s = nav_wait("PInet_UI_Disappear", s, "url_disappear")
    step("PInet_UI_Disappear", s, "Heading", "xUI", "xGetText", "h3_locator", "", "text_disappear")
    step("PInet_UI_Disappear", s + 1, "Click Home", "xUI", "xClick", "nav_home")
    step("PInet_UI_Disappear", s + 2, "Back home", "xUI", "xGetText", "h2_locator", "", "text_welcome")

    plan("PInet_UI_FloatingMenu", "UI — Floating Menu About anchor", "UI_internet;UI;Nav;Menu", "ui_float")
    s = reuse_open("PInet_UI_FloatingMenu")
    s = nav_wait("PInet_UI_FloatingMenu", s, "url_floating")
    step("PInet_UI_FloatingMenu", s, "Heading", "xUI", "xGetText", "h3_locator", "", "text_floating")
    step("PInet_UI_FloatingMenu", s + 1, "About", "xUI", "xClick", "menu_about")

    plan("PInet_UI_Notification", "UI — Notification Message flash present", "UI_internet;UI;Notify", "ui_notify")
    s = reuse_open("PInet_UI_Notification")
    s = nav_wait("PInet_UI_Notification", s, "url_notify")
    step("PInet_UI_Notification", s, "Heading", "xUI", "xGetText", "h3_locator", "", "text_notification_hdr")
    step("PInet_UI_Notification", s + 1, "Flash present", "xUI", "xGetText", "flash_locator", "", "", "Y")
    step("PInet_UI_Notification", s + 2, "Click here refresh", "xUI", "xClick", "link_click_here")
    step("PInet_UI_Notification", s + 3, "Wait", "xTime", "xTimeWait", "1")
    step("PInet_UI_Notification", s + 4, "Flash again", "xUI", "xGetText", "flash_locator", "", "", "Y")

    plan("PInet_UI_Redirect", "UI — Redirector lands on Status Codes", "UI_internet;UI;Redirect", "ui_redir")
    s = reuse_open("PInet_UI_Redirect")
    s = nav_wait("PInet_UI_Redirect", s, "url_redirect")
    step("PInet_UI_Redirect", s, "Click here", "xUI", "xClick", "link_redirect")
    step("PInet_UI_Redirect", s + 1, "Wait", "xTime", "xTimeWait", "2")
    step("PInet_UI_Redirect", s + 2, "Status Codes", "xUI", "xGetText", "h3_locator", "", "text_status_codes")

    plan("PInet_UI_Status404", "UI — Status Codes 404 page", "UI_internet;UI;HTTP;Status", "ui_404")
    s = reuse_open("PInet_UI_Status404")
    s = nav_wait("PInet_UI_Status404", s, "url_status")
    step("PInet_UI_Status404", s, "Open 404", "xUI", "xClick", "link_status_404")
    step("PInet_UI_Status404", s + 1, "Wait", "xTime", "xTimeWait", "1")
    step("PInet_UI_Status404", s + 2, "Body mentions 404", "xUI", "xGetText", "body_locator", "", "text_status_404")

    plan("PInet_UI_Tables", "UI — Sortable Data Tables cell + Edit link", "UI_internet;UI;Table", "ui_tables")
    s = reuse_open("PInet_UI_Tables")
    s = nav_wait("PInet_UI_Tables", s, "url_tables")
    step("PInet_UI_Tables", s, "Heading", "xUI", "xGetText", "h3_locator", "", "text_tables")
    step("PInet_UI_Tables", s + 1, "First last name", "xUI", "xGetText", "table1_cell", "", "", "Y")
    step("PInet_UI_Tables", s + 2, "Edit link", "xUI", "xClick", "table1_edit")

    plan("PInet_UI_ChallengingDOM", "UI — Challenging DOM button + table cell", "UI_internet;UI;DOM;Challenging", "ui_chal")
    s = reuse_open("PInet_UI_ChallengingDOM")
    s = nav_wait("PInet_UI_ChallengingDOM", s, "url_challenging")
    step("PInet_UI_ChallengingDOM", s, "Heading", "xUI", "xGetText", "h3_locator", "", "text_challenging")
    step("PInet_UI_ChallengingDOM", s + 1, "Click button", "xUI", "xClick", "btn_challenging")
    step("PInet_UI_ChallengingDOM", s + 2, "Table cell", "xUI", "xGetText", "table_cell", "", "", "Y")

    plan("PInet_UI_BrokenImages", "UI — Broken Images page loads", "UI_internet;UI;Images", "ui_broken")
    s = reuse_open("PInet_UI_BrokenImages")
    s = nav_wait("PInet_UI_BrokenImages", s, "url_broken")
    step("PInet_UI_BrokenImages", s, "Heading", "xUI", "xGetText", "h3_locator", "", "text_broken")

    plan("PInet_UI_LargeDOM", "UI — Large & Deep DOM table cell", "UI_internet;UI;DOM;Perf", "ui_large")
    s = reuse_open("PInet_UI_LargeDOM")
    s = nav_wait("PInet_UI_LargeDOM", s, "url_large", "3")
    step("PInet_UI_LargeDOM", s, "Heading", "xUI", "xGetText", "h3_locator", "", "text_large")
    step("PInet_UI_LargeDOM", s + 1, "Deep cell", "xUI", "xGetText", "large_cell", "", "", "Y")

    plan("PInet_UI_Typos", "UI — Typos page content", "UI_internet;UI;Content", "ui_typos")
    s = reuse_open("PInet_UI_Typos")
    s = nav_wait("PInet_UI_Typos", s, "url_typos")
    step("PInet_UI_Typos", s, "Heading", "xUI", "xGetText", "h3_locator", "", "text_typos")

    plan("PInet_UI_Shifting", "UI — Shifting Content page", "UI_internet;UI;Content", "ui_shift")
    s = reuse_open("PInet_UI_Shifting")
    s = nav_wait("PInet_UI_Shifting", s, "url_shifting")
    step("PInet_UI_Shifting", s, "Heading", "xUI", "xGetText", "h3_locator", "", "text_shifting")

    plan("PInet_UI_ForgotPassword", "UI — Forgot Password form submit", "UI_internet;UI;Forms;Auth", "ui_forgot")
    s = reuse_open("PInet_UI_ForgotPassword")
    s = nav_wait("PInet_UI_ForgotPassword", s, "url_forgot")
    step("PInet_UI_ForgotPassword", s, "Email", "xUI", "xType", "type_email")
    step("PInet_UI_ForgotPassword", s + 1, "Retrieve", "xUI", "xClick", "btn_retrieve")
    step("PInet_UI_ForgotPassword", s + 2, "Wait", "xTime", "xTimeWait", "2")
    step("PInet_UI_ForgotPassword", s + 3, "Body responded", "xUI", "xGetText", "body_locator", "", "", "Y")

    plan("PInet_UI_Viewport", "UI — mobile viewport then restore desktop", "UI_internet;UI;Responsive", "ui_vp")
    s = reuse_open("PInet_UI_Viewport")
    step("PInet_UI_Viewport", s, "Mobile size", "xUI", "xSetViewport", "viewport_mobile")
    step("PInet_UI_Viewport", s + 1, "Home still welcome", "xUI", "xGetText", "h2_locator", "", "text_welcome")
    step("PInet_UI_Viewport", s + 2, "Desktop size", "xUI", "xSetViewport", "viewport_desktop")

    plan(
        "PInet_UI_CaptureTour",
        "UI — capture screenshot on login success (demo evidence)",
        "UI_internet;UI;Capture;Demo",
        "ui_capture",
    )
    s = reuse_open("PInet_UI_CaptureTour")
    s = nav_wait("PInet_UI_CaptureTour", s, "url_login")
    step("PInet_UI_CaptureTour", s, "User", "xUI", "xType", "type_user_ok")
    step("PInet_UI_CaptureTour", s + 1, "Pass", "xUI", "xType", "type_pass_ok")
    step("PInet_UI_CaptureTour", s + 2, "Submit", "xUI", "xClick", "btn_login")
    step("PInet_UI_CaptureTour", s + 3, "Wait", "xTime", "xTimeWait", "1")
    step("PInet_UI_CaptureTour", s + 4, "Flash", "xUI", "xGetText", "flash_locator", "", "text_login_ok")
    step("PInet_UI_CaptureTour", s + 5, "Screenshot", "xCapture", "xCaptureImage", "secure_area")

    # --- Manual / skip heavy ---
    plan(
        "PInet_Man_Frames",
        "Manual — Frames / Nested Frames (needs frame switch)",
        "UI_internet;Manual;Frames",
        "manual_frames",
        run="N",
    )
    plan(
        "PInet_Man_Windows",
        "Manual — Multiple Windows (needs window switch)",
        "UI_internet;Manual;Windows",
        "manual_windows",
        run="N",
    )
    plan(
        "PInet_Man_Shadow",
        "Manual — Shadow DOM deep pierce",
        "UI_internet;Manual;Shadow",
        "manual_shadow",
        run="N",
    )

    y1_headers = ["PlanId", "PlanName", "DesignId", "Run", "Tags", "Output", "CreatedBy", "CreatedAt"]
    y2_headers = ["PlanId", "StepId", "StepInfo", "ActionType", "ActionName", "Input", "Output", "Expected", "Critical"]
    y3_headers = ["Type", "DataName", "D1"]

    wcsv(SUITE / "y1Plans.csv", y1_headers, plans)
    wcsv(SUITE / "y2Actions.csv", y2_headers, actions)
    wcsv(SUITE / "y3Designs.csv", y3_headers, y3_rows)

    suite_json = {
        "input_files": {
            "yPlans": ["y/UI_internet/y1Plans.csv"],
            "yActions": ["y/UI_internet/y2Actions.csv"],
            "yDesigns": ["y/UI_internet/y3Designs.csv"],
        },
        "name": "UI_internet",
        "description": "UI demo against https://the-internet.herokuapp.com — forms, alerts, DnD, upload, waits, tables",
        "version": "1.0.0",
        "url": f"{BASE}/",
    }
    (SUITE / "UI_internet.json").write_text(json.dumps(suite_json, indent=2) + "\n", encoding="utf-8")

    fstart = {
        "configs": ["y/UI_internet/UI_internet.json"],
        "thread_count": 1,
        "timeout": 12,
        "headless": False,
        "debug": False,
        "tags": ["Smoke", "UI"],
        "capture": {
            "image": "on_fail",
            "video": "off",
            "video_fps": 2,
            "subdir": "",
            "overlay": "off",
            "overlay_ms": 250,
        },
    }
    FSTART.write_text(json.dumps(fstart, indent=2) + "\n", encoding="utf-8")

    (SUITE / "test_plan.md").write_text(
        f"""# UI_internet — demo yPAD

Target: [{BASE}/]({BASE}/) (Elemental Selenium practice app).

## Tag guide

| Tag | Meaning |
|-----|---------|
| Smoke | Fast home + login happy path |
| UI | Browser interaction demos |
| Auth / Forms / Alert / DnD / Upload / Wait / Table | Capability demos |
| Manual | Needs frame/window/shadow helpers not in core xUI yet |

## Suggested demo runs

```powershell
# Smoke UI
python FoXYiZ/f/fEngine2.py --config f/fStart/UI_internet.json

# Fancy alerts + forms only (edit fStart tags or filter in Arena)
# tags: UI;Alert   or   UI;Forms
```

Generated {TS}.
""",
        encoding="utf-8",
    )

    auto = sum(1 for p in plans if p["Run"] == "Y")
    print(f"Wrote {len(plans)} plans ({auto} Run=Y), {len(actions)} steps, {len(y3_rows)} designs -> {SUITE}")


if __name__ == "__main__":
    main()
