#!/usr/bin/env python3
"""Generate FoXYiZ/y/KonfigAI — public-site yPAD for https://www.konfigai.com/

Layers
------
Smoke     Home + primary CTA chrome
Link      Every public HTML page loads; H1 contract (content)
Nav       Top-nav / footer destinations
Form      Request Demo + Contact field chrome (no submit spam)
Title     document.title correctness — known mismatches → A1 on BRAHL
Manual    Social externals + visual / a11y / form submit HITL

Crawl note (2026-07-28): several product pages share wrong <title>
\"Konfig AI : Batch Processing\"; About/Contact titled \"Home\"; Legal tabs
stay on Privacy title. Title plans assert the *correct* string so fails
document app defects (A1) — do not weaken Expected.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STAMP = "2026-07-28T17:00:00+00:00"
AUTHOR = "QA_Hunter+KonfigAI"

# path, plan_suffix, h1_keyword, correct_title
PAGES = [
    ("/", "Home", "No-Code", "Konfig AI : Home"),
    ("/form-builder.html", "FormBuilder", "Design Smart", "Konfig AI : Form Builder"),
    ("/workflow-builder.html", "Workflow", "Automate Smarter", "Konfig AI : Workflow Builder"),
    ("/api-builder.html", "ApiBuilder", "Build APIs", "Konfig AI : API Builder"),
    ("/batch-processing.html", "Batch", "Automate Data", "Konfig AI : Batch Processing"),
    ("/document-central.html", "DocCentral", "Smart Docs", "Konfig AI : Document Central"),
    ("/solutions.html", "Solutions", "Industry-Tailored", "Konfig AI : Solutions"),
    ("/integrations.html", "Integrations", "Connect Everything", "Konfig AI : Integration"),
    ("/about-us.html", "About", "Innovation at Scale", "Konfig AI : About Us"),
    ("/platform-overview.html", "Platform", "Build Smarter", "Konfig AI : Platform Overview"),
    ("/contact-us.html", "Contact", "Have Questions", "Konfig AI : Contact Us"),
    ("/request-demo.html", "RequestDemo", "Unlock AI Automation", "Konfig AI : Request Demo"),
    ("/legal.html", "Legal", "Your Trust", "Konfig AI : Privacy Policy"),
    ("/legal.html?tab=terms", "LegalTerms", "Your Trust", "Konfig AI : Terms"),
    ("/legal.html?tab=privacy", "LegalPrivacy", "Your Trust", "Konfig AI : Privacy Policy"),
    ("/legal.html?tab=cookie", "LegalCookie", "Your Trust", "Konfig AI : Cookie Policy"),
]

Y1: list[str] = [
    "PlanId,PlanName,DesignId,Run,Tags,Output,CreatedBy,CreatedAt",
    f"PReuse_Open,Open Edge and load KonfigAI home,D1,N,Reuse,preuse_open,{AUTHOR},{STAMP}",
    f"PSmoke_Home,Smoke — home H1 No-Code / AI-Driven,D1,Y,KonfigAI;Smoke;UI;Shell,psmoke_home,{AUTHOR},{STAMP}",
    f"PSmoke_DemoCTA,Smoke — Request Demo page from CTA URL,D1,Y,KonfigAI;Smoke;UI;CTA,psmoke_demo,{AUTHOR},{STAMP}",
    f"PSmoke_NavSolutions,Smoke — Solutions page loads,D1,Y,KonfigAI;Smoke;UI;Nav,psmoke_sol,{AUTHOR},{STAMP}",
]

Y2: list[str] = [
    "PlanId,StepId,StepInfo,ActionType,ActionName,Input,Output,Expected,Critical",
    "PReuse_Open,1,Open Edge,xUI,xOpenBrowser,edge,,,Y",
    "PReuse_Open,2,Home,xUI,xNavigate,base_url,,,Y",
    "PReuse_Open,3,Wait boot,xTime,xTimeWait,3,,,Y",
    "PReuse_Open,4,Body present,xUI,xGetText,body_locator,,text_home_kw,Y",
    "PSmoke_Home,1,Reuse open,xReuse,PReuse_Open,,,,Y",
    "PSmoke_Home,2,H1 contract,xUI,xGetText,h1_locator,,text_home_h1,Y",
    "PSmoke_Home,3,Products nav present,xUI,xGetText,body_locator,,text_nav_products,Y",
    "PSmoke_Home,4,Request Demo chrome,xUI,xGetText,body_locator,,text_request_demo,Y",
    "PSmoke_DemoCTA,1,Reuse open,xReuse,PReuse_Open,,,,Y",
    "PSmoke_DemoCTA,2,Open request-demo,xUI,xNavigate,url_requestdemo,,,Y",
    "PSmoke_DemoCTA,3,Settle,xTime,xTimeWait,2,,,Y",
    "PSmoke_DemoCTA,4,Demo H1,xUI,xGetText,h1_locator,,text_demo_h1,Y",
    "PSmoke_DemoCTA,5,Email field,xUI,xGetText,demo_email_locator,,,Y",
    "PSmoke_NavSolutions,1,Reuse open,xReuse,PReuse_Open,,,,Y",
    "PSmoke_NavSolutions,2,Open solutions,xUI,xNavigate,url_solutions,,,Y",
    "PSmoke_NavSolutions,3,Settle,xTime,xTimeWait,2,,,Y",
    "PSmoke_NavSolutions,4,Solutions H1,xUI,xGetText,h1_locator,,text_solutions_h1,Y",
]

Y3_ROWS: list[tuple[str, str, str]] = [
    ("UI", "base_url", "https://www.konfigai.com/"),
    ("UI", "body_locator", "css=body"),
    ("UI", "h1_locator", "css=h1"),
    ("UI", "text_home_kw", "No-Code"),
    ("UI", "text_home_h1", "No-Code"),
    ("UI", "text_nav_products", "Products"),
    ("UI", "text_request_demo", "Request a Demo"),
    ("UI", "text_demo_h1", "Unlock AI Automation"),
    ("UI", "text_solutions_h1", "Industry-Tailored"),
    ("UI", "demo_email_locator", "css=input[type=email]"),
    ("UI", "demo_first_locator", "css=input[placeholder*=\"First Name\"]"),
    ("UI", "demo_last_locator", "css=input[placeholder*=\"Last Name\"]"),
    ("UI", "demo_org_locator", "css=input[placeholder*=\"Organization\"]"),
    ("UI", "demo_phone_locator", "css=input[type=number]"),
    ("UI", "demo_size_locator", "css=#orgSize"),
    ("UI", "demo_submit_locator", "xpath=//button[@type='submit' and contains(.,'Submit')]"),
    ("UI", "contact_email_locator", "css=input[placeholder*=\"Email\"]"),
    ("UI", "contact_desc_locator", "css=textarea"),
    ("UI", "contact_submit_locator", "xpath=//button[contains(.,'Contact Us')]"),
    ("UI", "schedule_btn_locator", "xpath=//button[contains(.,'Schedule Now')]"),
    ("UI", "text_footer_platform", "Platform Overview"),
    ("UI", "text_footer_terms", "Terms"),
    ("UI", "text_footer_privacy", "Privacy"),
    ("UI", "text_footer_cookie", "Cookie"),
    ("UI", "text_form_builder_h1", "Design Smart"),
    ("UI", "text_workflow_h1", "Automate Smarter"),
    ("UI", "text_api_h1", "Build APIs"),
    ("UI", "text_batch_h1", "Automate Data"),
    ("UI", "text_doc_h1", "Smart Docs"),
    ("UI", "text_integrations_h1", "Connect Everything"),
    ("UI", "text_about_h1", "Innovation at Scale"),
    ("UI", "text_platform_h1", "Build Smarter"),
    ("UI", "text_contact_h1", "Have Questions"),
    ("UI", "text_legal_h1", "Your Trust"),
]


def add_page_plans() -> None:
    for path, suf, h1_kw, title in PAGES:
        url_key = f"url_{suf.lower()}"
        h1_key = f"text_{suf.lower()}_h1"
        title_key = f"title_{suf.lower()}"
        # reuse shared h1 keys where already defined
        shared = {
            "Home": "text_home_h1",
            "RequestDemo": "text_demo_h1",
            "Solutions": "text_solutions_h1",
            "FormBuilder": "text_form_builder_h1",
            "Workflow": "text_workflow_h1",
            "ApiBuilder": "text_api_h1",
            "Batch": "text_batch_h1",
            "DocCentral": "text_doc_h1",
            "Integrations": "text_integrations_h1",
            "About": "text_about_h1",
            "Platform": "text_platform_h1",
            "Contact": "text_contact_h1",
            "Legal": "text_legal_h1",
            "LegalTerms": "text_legal_h1",
            "LegalPrivacy": "text_legal_h1",
            "LegalCookie": "text_legal_h1",
        }
        h1_expect = shared.get(suf, h1_key)
        if h1_expect == h1_key:
            Y3_ROWS.append(("UI", h1_key, h1_kw))
        Y3_ROWS.append(("UI", url_key, f"https://www.konfigai.com{path}" if path != "/" else "https://www.konfigai.com/"))
        Y3_ROWS.append(("UI", title_key, title))

        # Link health
        pid = f"PLink_{suf}"
        Y1.append(
            f"{pid},Link — {path or '/'} loads + H1,D1,Y,KonfigAI;Link;UI;Shell,{pid.lower()},{AUTHOR},{STAMP}"
        )
        Y2.extend(
            [
                f"{pid},1,Reuse open,xReuse,PReuse_Open,,,,Y",
                f"{pid},2,Navigate page,xUI,xNavigate,{url_key},,,Y",
                f"{pid},3,Settle,xTime,xTimeWait,2,,,Y",
                f"{pid},4,H1 contract,xUI,xGetText,h1_locator,,{h1_expect},Y",
            ]
        )

        # Title correctness (A1 when wrong)
        tid = f"PTitle_{suf}"
        Y1.append(
            f"{tid},Title — {path or '/'} document.title correct,D1,Y,KonfigAI;Title;UI;A1,{tid.lower()},{AUTHOR},{STAMP}"
        )
        Y2.extend(
            [
                f"{tid},1,Reuse open,xReuse,PReuse_Open,,,,Y",
                f"{tid},2,Navigate page,xUI,xNavigate,{url_key},,,Y",
                f"{tid},3,Settle,xTime,xTimeWait,2,,,Y",
                f"{tid},4,Assert title,xUI,xGetTitle,,,{title_key},Y",
            ]
        )


def add_form_and_footer() -> None:
    Y1.extend(
        [
            f"PForm_DemoChrome,Form — Request Demo fields visible,D1,Y,KonfigAI;Form;UI;Demo,pform_demo,{AUTHOR},{STAMP}",
            f"PForm_ContactChrome,Form — Contact Us fields visible,D1,Y,KonfigAI;Form;UI;Contact,pform_contact,{AUTHOR},{STAMP}",
            f"PNav_FooterLegal,Footer — Platform + Legal links present on home,D1,Y,KonfigAI;Nav;UI;Footer,pnav_footer,{AUTHOR},{STAMP}",
            f"PNav_ProductsMenu,Nav — Form Builder destination from URL,D1,Y,KonfigAI;Nav;UI;Products,pnav_products,{AUTHOR},{STAMP}",
            f"PMan_SocialExt,Manual — LinkedIn / X / YouTube footer externals,D1,N,KonfigAI;Manual;Social,pman_social,{AUTHOR},{STAMP}",
            f"PMan_DemoSubmit,Manual — submit Request Demo (HITL / no spam),D1,N,KonfigAI;Manual;Form;Demo,pman_demosubmit,{AUTHOR},{STAMP}",
            f"PMan_ContactSubmit,Manual — submit Contact Us (HITL),D1,N,KonfigAI;Manual;Form;Contact,pman_contactsubmit,{AUTHOR},{STAMP}",
            f"PMan_VisualA11y,Manual — visual / responsive / a11y sweep,D1,N,KonfigAI;Manual;A11y,pman_a11y,{AUTHOR},{STAMP}",
            f"PMan_TitleDebt,Manual — catalog remaining title mismatches after Title tag run,D1,N,KonfigAI;Manual;Title;A1,pman_titledebt,{AUTHOR},{STAMP}",
        ]
    )
    Y2.extend(
        [
            "PForm_DemoChrome,1,Reuse open,xReuse,PReuse_Open,,,,Y",
            "PForm_DemoChrome,2,Open demo,xUI,xNavigate,url_requestdemo,,,Y",
            "PForm_DemoChrome,3,Settle,xTime,xTimeWait,2,,,Y",
            "PForm_DemoChrome,4,First name,xUI,xGetText,demo_first_locator,,,Y",
            "PForm_DemoChrome,5,Last name,xUI,xGetText,demo_last_locator,,,Y",
            "PForm_DemoChrome,6,Email,xUI,xGetText,demo_email_locator,,,Y",
            "PForm_DemoChrome,7,Org,xUI,xGetText,demo_org_locator,,,Y",
            "PForm_DemoChrome,8,Phone,xUI,xGetText,demo_phone_locator,,,Y",
            "PForm_DemoChrome,9,Org size,xUI,xGetText,demo_size_locator,,,Y",
            "PForm_DemoChrome,10,Submit btn,xUI,xGetText,demo_submit_locator,,,Y",
            "PForm_ContactChrome,1,Reuse open,xReuse,PReuse_Open,,,,Y",
            "PForm_ContactChrome,2,Open contact,xUI,xNavigate,url_contact,,,Y",
            "PForm_ContactChrome,3,Settle,xTime,xTimeWait,2,,,Y",
            "PForm_ContactChrome,4,Email field,xUI,xGetText,contact_email_locator,,,Y",
            "PForm_ContactChrome,5,Description,xUI,xGetText,contact_desc_locator,,,Y",
            "PForm_ContactChrome,6,Contact CTA,xUI,xGetText,contact_submit_locator,,,Y",
            "PForm_ContactChrome,7,Schedule chrome,xUI,xGetText,schedule_btn_locator,,,Y",
            "PNav_FooterLegal,1,Reuse open,xReuse,PReuse_Open,,,,Y",
            "PNav_FooterLegal,2,Platform Overview text,xUI,xGetText,body_locator,,text_footer_platform,Y",
            "PNav_FooterLegal,3,Terms text,xUI,xGetText,body_locator,,text_footer_terms,Y",
            "PNav_FooterLegal,4,Privacy text,xUI,xGetText,body_locator,,text_footer_privacy,Y",
            "PNav_FooterLegal,5,Cookie text,xUI,xGetText,body_locator,,text_footer_cookie,Y",
            "PNav_ProductsMenu,1,Reuse open,xReuse,PReuse_Open,,,,Y",
            "PNav_ProductsMenu,2,Form builder URL,xUI,xNavigate,url_formbuilder,,,Y",
            "PNav_ProductsMenu,3,Settle,xTime,xTimeWait,2,,,Y",
            "PNav_ProductsMenu,4,Form builder H1,xUI,xGetText,h1_locator,,text_form_builder_h1,Y",
            "PMan_SocialExt,1,Reuse open,xReuse,PReuse_Open,,,,Y",
            "PMan_SocialExt,2,Hunter checks LinkedIn X YouTube,xUI,xGetText,body_locator,,,N",
            "PMan_DemoSubmit,1,Open demo,xUI,xNavigate,url_requestdemo,,,Y",
            "PMan_DemoSubmit,2,Hunter fills+submits carefully,xUI,xGetText,demo_submit_locator,,,N",
            "PMan_ContactSubmit,1,Open contact,xUI,xNavigate,url_contact,,,Y",
            "PMan_ContactSubmit,2,Hunter fills+submits carefully,xUI,xGetText,contact_submit_locator,,,N",
            "PMan_VisualA11y,1,Reuse open,xReuse,PReuse_Open,,,,Y",
            "PMan_VisualA11y,2,Hunter visual sweep,xUI,xGetText,body_locator,,,N",
            "PMan_TitleDebt,1,Reuse open,xReuse,PReuse_Open,,,,Y",
            "PMan_TitleDebt,2,Hunter triages Title tag fails as A1,xUI,xGetText,body_locator,,,N",
        ]
    )


def main() -> None:
    add_page_plans()
    add_form_and_footer()

    # Fix url keys used in form plans — generator used url_requestdemo / url_contact / url_formbuilder
    # Page loop created url_requestdemo from RequestDemo -> url_requestdemo ✓
    # Contact -> url_contact ✓
    # FormBuilder -> url_formbuilder ✓

    (ROOT / "y1Plans.csv").write_text("\n".join(Y1) + "\n", encoding="utf-8")
    (ROOT / "y2Actions.csv").write_text("\n".join(Y2) + "\n", encoding="utf-8")
    with (ROOT / "y3Designs.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Type", "DataName", "D1"])
        seen: set[str] = set()
        for typ, name, d1 in Y3_ROWS:
            if name in seen:
                continue
            seen.add(name)
            w.writerow([typ, name, d1])

    (ROOT / "KonfigAI.json").write_text(
        "{\n"
        '  "input_files": {\n'
        '    "yPlans": ["y/KonfigAI/y1Plans.csv"],\n'
        '    "yActions": ["y/KonfigAI/y2Actions.csv"],\n'
        '    "yDesigns": ["y/KonfigAI/y3Designs.csv"]\n'
        "  },\n"
        '  "name": "KonfigAI",\n'
        '  "description": "Public site link + title + form chrome for https://www.konfigai.com/",\n'
        '  "version": "1.0.0",\n'
        '  "url": "https://www.konfigai.com/"\n'
        "}\n",
        encoding="utf-8",
    )
    print(f"Wrote KonfigAI plans={len(Y1)-1} steps={len(Y2)-1} designs={len(seen)} -> {ROOT}")


if __name__ == "__main__":
    main()
