#!/usr/bin/env python3
"""Generate FoXYiZ/y/AI_foxyiz yPAD — AI UX against https://foxyiz.com hero Generate.

Evaluation model
----------------
1. Chrome (deterministic): page, prompt box, chips, Generate enable/disable.
2. Contract (semi-soft): after Generate, body must include markers like
   "AI GENERATED YPAD", "y1Plans.csv", and domain keywords (xUI / xAPI / xMath).
3. Quality (Manual Run=N): tone, usefulness, hallucination, multi-turn.

Vary inputs via y3 DataNames (and D1/D2/D3 on custom prompts) — not by editing y2.
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STAMP = "2026-07-27T19:00:00+00:00"
AUTHOR = "QA_Hunter+AI_Demo"

Y1 = [
    "PlanId,PlanName,DesignId,Run,Tags,Output,CreatedBy,CreatedAt",
    f"PReuse_Open,Open Edge and load foxyiz.com home,D1,N,Reuse,preuse_open,{AUTHOR},{STAMP}",
    f"PSmoke_Hero,Smoke — hero + prompt box + Generate,D1,Y,AI_foxyiz;Smoke;UI;Shell,psmoke_hero,{AUTHOR},{STAMP}",
    f"PSmoke_ChipFill,Smoke — type prompt + Generate returns yPAD,D1,Y,AI_foxyiz;Smoke;UI;Chat,psmoke_chip,{AUTHOR},{STAMP}",
    f"PGen_Login,Generate — Automate website login → yPAD with xUI,D1,Y,AI_foxyiz;AI;UI;Chat;Gen,pgen_login,{AUTHOR},{STAMP}",
    f"PGen_API,Generate — Test a REST API → yPAD with xAPI,D1,Y,AI_foxyiz;AI;API;Chat;Gen,pgen_api,{AUTHOR},{STAMP}",
    f"PGen_Math,Generate — Run math calculations → yPAD with xMath,D1,Y,AI_foxyiz;AI;Math;Chat;Gen,pgen_math,{AUTHOR},{STAMP}",
    f"PGen_Custom_D1,Generate — custom prompt dataset D1,D1,Y,AI_foxyiz;AI;Chat;Dataset,pgen_d1,{AUTHOR},{STAMP}",
    f"PGen_Custom_D2,Generate — custom prompt dataset D2,D2,Y,AI_foxyiz;AI;Chat;Dataset,pgen_d2,{AUTHOR},{STAMP}",
    f"PGen_Custom_D3,Generate — custom prompt dataset D3,D3,Y,AI_foxyiz;AI;Chat;Dataset,pgen_d3,{AUTHOR},{STAMP}",
    f"PMan_Quality,Manual — response is useful on-brand yPAD,D1,N,AI_foxyiz;Manual;Quality,pman_quality,{AUTHOR},{STAMP}",
    f"PMan_Hallucination,Manual — no invented ActionNames / broken CSV,D1,N,AI_foxyiz;Manual;Safety,pman_halluc,{AUTHOR},{STAMP}",
    f"PMan_MultiTurn,Manual — second prompt refines previous yPAD,D1,N,AI_foxyiz;Manual;Chat;MultiTurn,pman_multi,{AUTHOR},{STAMP}",
]

# Step template helpers
def steps_open() -> list[str]:
    return [
        "PReuse_Open,1,Open Edge,xUI,xOpenBrowser,edge,,,Y",
        "PReuse_Open,2,Home,xUI,xNavigate,base_url,,,Y",
        "PReuse_Open,3,Wait boot,xTime,xTimeWait,3,,,Y",
        "PReuse_Open,4,Body present,xUI,xGetText,body_locator,,text_hero,Y",
    ]


def steps_gen(plan: str, fill_mode: str, fill_input: str, expect: str) -> list[str]:
    """fill_mode: chip | type"""
    rows = [
        f"{plan},1,Reuse open home,xReuse,PReuse_Open,,,,Y",
        f"{plan},2,Settle,xTime,xTimeWait,1,,,Y",
    ]
    if fill_mode == "chip":
        rows.append(f"{plan},3,Click prompt chip,xUI,xClick,{fill_input},,,Y")
    else:
        rows.append(f"{plan},3,Type custom prompt,xUI,xType,{fill_input},,,Y")
    rows.extend(
        [
            f"{plan},4,Generate enabled settle,xTime,xTimeWait,1,,,Y",
            f"{plan},5,Click Generate,xUI,xClick,btn_generate,,,Y",
            f"{plan},6,Wait AI response,xTime,xTimeWait,20,,,Y",
            f"{plan},7,Result panel marker,xUI,xGetText,body_locator,,text_ai_generated,Y",
            f"{plan},8,Has y1Plans section,xUI,xGetText,body_locator,,text_y1,Y",
            f"{plan},9,Has y2Actions section,xUI,xGetText,body_locator,,text_y2,Y",
            f"{plan},10,Domain keyword check,xUI,xGetText,body_locator,,{expect},Y",
            f"{plan},11,Download CTA present,xUI,xGetText,body_locator,,text_download,Y",
        ]
    )
    return rows


Y2 = [
    "PlanId,StepId,StepInfo,ActionType,ActionName,Input,Output,Expected,Critical",
    *steps_open(),
    "PSmoke_Hero,1,Reuse open home,xReuse,PReuse_Open,,,,Y",
    "PSmoke_Hero,2,Hero headline,xUI,xGetText,h1_locator,,text_hero,Y",
    "PSmoke_Hero,3,Prompt box present,xUI,xGetText,prompt_locator,,,Y",
    "PSmoke_Hero,4,Generate control present,xUI,xGetText,btn_generate_locator,,,Y",
    "PSmoke_Hero,5,Chip login visible,xUI,xGetText,chip_login,,,Y",
    "PSmoke_ChipFill,1,Reuse open home,xReuse,PReuse_Open,,,,Y",
    "PSmoke_ChipFill,2,Type login prompt,xUI,xType,type_prompt_login,,,Y",
    "PSmoke_ChipFill,3,Settle,xTime,xTimeWait,1,,,Y",
    "PSmoke_ChipFill,4,Click Generate,xUI,xClick,btn_generate,,,Y",
    "PSmoke_ChipFill,5,Wait AI response,xTime,xTimeWait,25,,,Y",
    "PSmoke_ChipFill,6,Result panel marker,xUI,xGetText,body_locator,,text_ai_generated,Y",
    "PSmoke_ChipFill,7,Has y1Plans section,xUI,xGetText,body_locator,,text_y1,Y",
    "PSmoke_ChipFill,8,Login-ish yPAD keyword,xUI,xGetText,body_locator,,expect_login_kw,Y",
    *steps_gen("PGen_Login", "type", "type_prompt_login", "expect_login_kw"),
    *steps_gen("PGen_API", "type", "type_prompt_api", "expect_api_kw"),
    *steps_gen("PGen_Math", "type", "type_prompt_math", "expect_math_kw"),
    *steps_gen("PGen_Custom_D1", "type", "type_prompt_custom", "expect_any_ypad"),
    *steps_gen("PGen_Custom_D2", "type", "type_prompt_custom", "expect_any_ypad"),
    *steps_gen("PGen_Custom_D3", "type", "type_prompt_custom", "expect_any_ypad"),
    "PMan_Quality,1,Reuse open home,xReuse,PReuse_Open,,,,Y",
    "PMan_Quality,2,Hunter judges usefulness of generated yPAD,xUI,xGetText,body_locator,,text_ai_generated,N",
    "PMan_Hallucination,1,Reuse open home,xReuse,PReuse_Open,,,,Y",
    "PMan_Hallucination,2,Hunter checks ActionNames exist in xCapa,xUI,xGetText,body_locator,,text_ai_generated,N",
    "PMan_MultiTurn,1,Reuse open home,xReuse,PReuse_Open,,,,Y",
    "PMan_MultiTurn,2,Hunter sends follow-up refine prompt,xUI,xGetText,prompt_locator,,,N",
]

# y3: D1/D2/D3 vary the custom prompt dataset
Y3_ROWS = [
    # locators / chrome
    ("UI", "base_url", "https://foxyiz.com/", "https://foxyiz.com/", "https://foxyiz.com/"),
    ("UI", "body_locator", "css=body", "css=body", "css=body"),
    ("UI", "h1_locator", "css=h1", "css=h1", "css=h1"),
    (
        "UI",
        "prompt_locator",
        "css=textarea[placeholder*=\"Describe your automation\"]",
        "css=textarea[placeholder*=\"Describe your automation\"]",
        "css=textarea[placeholder*=\"Describe your automation\"]",
    ),
    (
        "UI",
        "btn_generate",
        "xpath=//button[contains(normalize-space(.),'Generate')]",
        "xpath=//button[contains(normalize-space(.),'Generate')]",
        "xpath=//button[contains(normalize-space(.),'Generate')]",
    ),
    (
        "UI",
        "btn_generate_locator",
        "xpath=//button[contains(normalize-space(.),'Generate')]",
        "xpath=//button[contains(normalize-space(.),'Generate')]",
        "xpath=//button[contains(normalize-space(.),'Generate')]",
    ),
    (
        "UI",
        "chip_login",
        "xpath=//button[normalize-space()='Automate website login']",
        "xpath=//button[normalize-space()='Automate website login']",
        "xpath=//button[normalize-space()='Automate website login']",
    ),
    (
        "UI",
        "chip_api",
        "xpath=//button[normalize-space()='Test a REST API']",
        "xpath=//button[normalize-space()='Test a REST API']",
        "xpath=//button[normalize-space()='Test a REST API']",
    ),
    (
        "UI",
        "chip_math",
        "xpath=//button[normalize-space()='Run math calculations']",
        "xpath=//button[normalize-space()='Run math calculations']",
        "xpath=//button[normalize-space()='Run math calculations']",
    ),
    (
        "UI",
        "chip_scrape",
        "xpath=//button[normalize-space()='Scrape product prices']",
        "xpath=//button[normalize-space()='Scrape product prices']",
        "xpath=//button[normalize-space()='Scrape product prices']",
    ),
    (
        "UI",
        "chip_signup",
        "xpath=//button[normalize-space()='Validate a signup form']",
        "xpath=//button[normalize-space()='Validate a signup form']",
        "xpath=//button[normalize-space()='Validate a signup form']",
    ),
    (
        "UI",
        "chip_upload",
        "xpath=//button[normalize-space()='Automate file uploads']",
        "xpath=//button[normalize-space()='Automate file uploads']",
        "xpath=//button[normalize-space()='Automate file uploads']",
    ),
    # type prompts = text;locator — primary dataset (chips kept as optional locators)
    (
        "UI",
        "type_prompt_login",
        "Automate website login;css=textarea[placeholder*=\"Describe your automation\"]",
        "Automate website login;css=textarea[placeholder*=\"Describe your automation\"]",
        "Automate website login;css=textarea[placeholder*=\"Describe your automation\"]",
    ),
    (
        "UI",
        "type_prompt_api",
        "Test a REST API;css=textarea[placeholder*=\"Describe your automation\"]",
        "Test a REST API;css=textarea[placeholder*=\"Describe your automation\"]",
        "Test a REST API;css=textarea[placeholder*=\"Describe your automation\"]",
    ),
    (
        "UI",
        "type_prompt_math",
        "Run math calculations;css=textarea[placeholder*=\"Describe your automation\"]",
        "Run math calculations;css=textarea[placeholder*=\"Describe your automation\"]",
        "Run math calculations;css=textarea[placeholder*=\"Describe your automation\"]",
    ),
    (
        "UI",
        "type_prompt_custom",
        "Automate login to example.com and verify the dashboard loads;css=textarea[placeholder*=\"Describe your automation\"]",
        "Test GET and POST against a public REST petstore API;css=textarea[placeholder*=\"Describe your automation\"]",
        "Add two numbers and assert the sum equals expected;css=textarea[placeholder*=\"Describe your automation\"]",
    ),
    # expected fragments (soft contract)
    ("UI", "text_hero", "AUTOMATE", "AUTOMATE", "AUTOMATE"),
    ("UI", "text_chip_login", "Automate website login", "Automate website login", "Automate website login"),
    ("UI", "text_ai_generated", "AI GENERATED YPAD", "AI GENERATED YPAD", "AI GENERATED YPAD"),
    ("UI", "text_y1", "y1Plans.csv", "y1Plans.csv", "y1Plans.csv"),
    ("UI", "text_y2", "y2Actions.csv", "y2Actions.csv", "y2Actions.csv"),
    ("UI", "text_download", "Download", "Download", "Download"),
    ("UI", "expect_login_kw", "xUI", "xUI", "xUI"),
    ("UI", "expect_api_kw", "xAPI", "xAPI", "xAPI"),
    ("UI", "expect_math_kw", "xMath", "xMath", "xMath"),
    ("UI", "expect_any_ypad", "PlanId", "PlanId", "PlanId"),
]


def write_csv(path: Path, rows: list[str]) -> None:
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")


def write_y3(path: Path) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Type", "DataName", "D1", "D2", "D3"])
        for row in Y3_ROWS:
            w.writerow(row)


def main() -> None:
    write_csv(ROOT / "y1Plans.csv", Y1)
    write_csv(ROOT / "y2Actions.csv", Y2)
    write_y3(ROOT / "y3Designs.csv")
    (ROOT / "AI_foxyiz.json").write_text(
        '{\n  "input_files": {\n'
        '    "yPlans": ["y/AI_foxyiz/y1Plans.csv"],\n'
        '    "yActions": ["y/AI_foxyiz/y2Actions.csv"],\n'
        '    "yDesigns": ["y/AI_foxyiz/y3Designs.csv"]\n'
        "  },\n"
        '  "url": "https://foxyiz.com/"\n'
        "}\n",
        encoding="utf-8",
    )
    # sample prompt library (human-editable dataset — also mirrored in y3)
    prompts = ROOT / "prompts"
    prompts.mkdir(exist_ok=True)
    (prompts / "login.txt").write_text("Automate website login\n", encoding="utf-8")
    (prompts / "api.txt").write_text("Test a REST API\n", encoding="utf-8")
    (prompts / "math.txt").write_text("Run math calculations\n", encoding="utf-8")
    (prompts / "custom_d1.txt").write_text(
        "Automate login to example.com and verify the dashboard loads\n", encoding="utf-8"
    )
    (prompts / "custom_d2.txt").write_text(
        "Test GET and POST against a public REST petstore API\n", encoding="utf-8"
    )
    (prompts / "custom_d3.txt").write_text(
        "Add two numbers and assert the sum equals expected\n", encoding="utf-8"
    )
    print(f"Wrote AI_foxyiz -> {ROOT}")


if __name__ == "__main__":
    main()
