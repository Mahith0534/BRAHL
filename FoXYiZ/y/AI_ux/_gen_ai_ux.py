#!/usr/bin/env python3
"""Generate FoXYiZ/y/AI_ux — portable AI chatbot UX template (UI + API + Manual).

Copy this suite, set base_url / locators / prompts in y3, then flip Run=Y on
automation plans once the target chat widget is stable.

Layers
------
- UI chrome: open app → chat widget visible → type → send → response region
- API (optional): POST prompt payload; assert JSON keys (status / message)
- AI catalog (optional): xTextPrompt / xContextPrompt when you have an endpoint+key
- Manual: quality, safety, multi-turn, visual polish
"""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STAMP = "2026-07-27T19:00:00+00:00"
AUTHOR = "QA_Hunter+AI_UX"

Y1 = [
    "PlanId,PlanName,DesignId,Run,Tags,Output,CreatedBy,CreatedAt",
    f"PReuse_OpenChat,Open browser and load AI chat app,D1,N,Reuse,preuse_open,{AUTHOR},{STAMP}",
    f"PSmoke_ChatShell,Smoke — chat shell visible (widget + input + send),D1,Y,AI_ux;Smoke;UI;Shell,psmoke_shell,{AUTHOR},{STAMP}",
    f"PChat_SendPrompt_D1,UI — send prompt dataset D1 and expect response region,D1,Y,AI_ux;UI;Chat;Dataset,pchat_d1,{AUTHOR},{STAMP}",
    f"PChat_SendPrompt_D2,UI — send prompt dataset D2 and expect response region,D2,Y,AI_ux;UI;Chat;Dataset,pchat_d2,{AUTHOR},{STAMP}",
    f"PChat_SendPrompt_D3,UI — send prompt dataset D3 and expect response region,D3,Y,AI_ux;UI;Chat;Dataset,pchat_d3,{AUTHOR},{STAMP}",
    f"PAPI_ChatPost,API — POST chat payload and compare JSON key,D1,N,AI_ux;API;Chat,papi_chat,{AUTHOR},{STAMP}",
    f"PAI_TextPrompt,AI — xTextPrompt against configured endpoint,D1,N,AI_ux;AI;Prompt,pai_text,{AUTHOR},{STAMP}",
    f"PMan_Quality,Manual — answer is helpful and on-brand,D1,N,AI_ux;Manual;Quality,pman_quality,{AUTHOR},{STAMP}",
    f"PMan_Safety,Manual — refusal / safe completion for risky prompt,D1,N,AI_ux;Manual;Safety,pman_safety,{AUTHOR},{STAMP}",
    f"PMan_MultiTurn,Manual — follow-up uses prior context,D1,N,AI_ux;Manual;MultiTurn,pman_multi,{AUTHOR},{STAMP}",
    f"PMan_Latency,Manual — response time feels acceptable,D1,N,AI_ux;Manual;Perf,pman_latency,{AUTHOR},{STAMP}",
]

Y2 = [
    "PlanId,StepId,StepInfo,ActionType,ActionName,Input,Output,Expected,Critical",
    "PReuse_OpenChat,1,Open Edge,xUI,xOpenBrowser,edge,,,Y",
    "PReuse_OpenChat,2,Navigate app,xUI,xNavigate,base_url,,,Y",
    "PReuse_OpenChat,3,Wait boot,xTime,xTimeWait,3,,,Y",
    "PReuse_OpenChat,4,Body present,xUI,xGetText,body_locator,,text_shell,Y",
    "PSmoke_ChatShell,1,Reuse open,xReuse,PReuse_OpenChat,,,,Y",
    "PSmoke_ChatShell,2,Chat input visible,xUI,xGetText,prompt_locator,,,Y",
    "PSmoke_ChatShell,3,Send control visible,xUI,xGetText,btn_send_locator,,,Y",
    "PChat_SendPrompt_D1,1,Reuse open,xReuse,PReuse_OpenChat,,,,Y",
    "PChat_SendPrompt_D1,2,Type prompt,xUI,xType,type_prompt,,,Y",
    "PChat_SendPrompt_D1,3,Send,xUI,xClick,btn_send,,,Y",
    "PChat_SendPrompt_D1,4,Wait model,xTime,xTimeWait,15,,,Y",
    "PChat_SendPrompt_D1,5,Response region,xUI,xGetText,response_locator,,expect_response_kw,Y",
    "PChat_SendPrompt_D2,1,Reuse open,xReuse,PReuse_OpenChat,,,,Y",
    "PChat_SendPrompt_D2,2,Type prompt,xUI,xType,type_prompt,,,Y",
    "PChat_SendPrompt_D2,3,Send,xUI,xClick,btn_send,,,Y",
    "PChat_SendPrompt_D2,4,Wait model,xTime,xTimeWait,15,,,Y",
    "PChat_SendPrompt_D2,5,Response region,xUI,xGetText,response_locator,,expect_response_kw,Y",
    "PChat_SendPrompt_D3,1,Reuse open,xReuse,PReuse_OpenChat,,,,Y",
    "PChat_SendPrompt_D3,2,Type prompt,xUI,xType,type_prompt,,,Y",
    "PChat_SendPrompt_D3,3,Send,xUI,xClick,btn_send,,,Y",
    "PChat_SendPrompt_D3,4,Wait model,xTime,xTimeWait,15,,,Y",
    "PChat_SendPrompt_D3,5,Response region,xUI,xGetText,response_locator,,expect_response_kw,Y",
    "PAPI_ChatPost,1,POST chat,xAPI,xPost,post_chat,,,Y",
    "PAPI_ChatPost,2,Compare message key,xJSON,xCompareJson,cmp_message,,,Y",
    "PAI_TextPrompt,1,Send catalog prompt,xAI,xTextPrompt,ai_text_prompt,ai_out,,Y",
    "PMan_Quality,1,Reuse open,xReuse,PReuse_OpenChat,,,,Y",
    "PMan_Quality,2,Hunter rates answer quality,xUI,xGetText,response_locator,,,N",
    "PMan_Safety,1,Reuse open,xReuse,PReuse_OpenChat,,,,Y",
    "PMan_Safety,2,Hunter checks safe refusal,xUI,xGetText,response_locator,,,N",
    "PMan_MultiTurn,1,Reuse open,xReuse,PReuse_OpenChat,,,,Y",
    "PMan_MultiTurn,2,Hunter validates context carry,xUI,xGetText,response_locator,,,N",
    "PMan_Latency,1,Reuse open,xReuse,PReuse_OpenChat,,,,Y",
    "PMan_Latency,2,Hunter times perceived latency,xUI,xGetText,response_locator,,,N",
]

Y3 = [
    ("UI", "base_url", "https://foxyiz.com/", "https://foxyiz.com/", "https://foxyiz.com/"),
    ("UI", "body_locator", "css=body", "css=body", "css=body"),
    (
        "UI",
        "prompt_locator",
        "css=textarea[placeholder*=\"Describe your automation\"]",
        "css=textarea[placeholder*=\"Describe your automation\"]",
        "css=textarea[placeholder*=\"Describe your automation\"]",
    ),
    (
        "UI",
        "btn_send",
        "xpath=//button[contains(normalize-space(.),'Generate')]",
        "xpath=//button[contains(normalize-space(.),'Generate')]",
        "xpath=//button[contains(normalize-space(.),'Generate')]",
    ),
    (
        "UI",
        "btn_send_locator",
        "xpath=//button[contains(normalize-space(.),'Generate')]",
        "xpath=//button[contains(normalize-space(.),'Generate')]",
        "xpath=//button[contains(normalize-space(.),'Generate')]",
    ),
    ("UI", "response_locator", "css=body", "css=body", "css=body"),
    (
        "UI",
        "type_prompt",
        "Automate website login;css=textarea[placeholder*=\"Describe your automation\"]",
        "Test a REST API;css=textarea[placeholder*=\"Describe your automation\"]",
        "Run math calculations;css=textarea[placeholder*=\"Describe your automation\"]",
    ),
    ("UI", "text_shell", "AUTOMATE", "AUTOMATE", "AUTOMATE"),
    ("UI", "expect_response_kw", "AI GENERATED YPAD", "AI GENERATED YPAD", "AI GENERATED YPAD"),
    (
        "API",
        "post_chat",
        "https://httpbin.org;/post;y/AI_ux/payloads/chat_prompt.json",
        "https://httpbin.org;/post;y/AI_ux/payloads/chat_prompt.json",
        "https://httpbin.org;/post;y/AI_ux/payloads/chat_prompt.json",
    ),
    ("API", "cmp_message", "json.prompt;hello AI", "json.prompt;hello AI", "json.prompt;hello AI"),
    (
        "AI",
        "ai_text_prompt",
        "https://api.openai.com/v1/chat/completions;REPLACE_KEY;Say hello in one word",
        "https://api.openai.com/v1/chat/completions;REPLACE_KEY;Say hello in one word",
        "https://api.openai.com/v1/chat/completions;REPLACE_KEY;Say hello in one word",
    ),
]


def main() -> None:
    (ROOT / "y1Plans.csv").write_text("\n".join(Y1) + "\n", encoding="utf-8")
    (ROOT / "y2Actions.csv").write_text("\n".join(Y2) + "\n", encoding="utf-8")
    with (ROOT / "y3Designs.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Type", "DataName", "D1", "D2", "D3"])
        w.writerows(Y3)
    (ROOT / "AI_ux.json").write_text(
        '{\n  "input_files": {\n'
        '    "yPlans": ["y/AI_ux/y1Plans.csv"],\n'
        '    "yActions": ["y/AI_ux/y2Actions.csv"],\n'
        '    "yDesigns": ["y/AI_ux/y3Designs.csv"]\n'
        "  },\n"
        '  "url": "https://foxyiz.com/"\n'
        "}\n",
        encoding="utf-8",
    )
    payloads = ROOT / "payloads"
    payloads.mkdir(exist_ok=True)
    (payloads / "chat_prompt.json").write_text(
        '{\n  "prompt": "hello AI",\n  "stream": false\n}\n', encoding="utf-8"
    )
    prompts = ROOT / "prompts"
    prompts.mkdir(exist_ok=True)
    (prompts / "d1.txt").write_text("Automate website login\n", encoding="utf-8")
    (prompts / "d2.txt").write_text("Test a REST API\n", encoding="utf-8")
    (prompts / "d3.txt").write_text("Run math calculations\n", encoding="utf-8")
    print(f"Wrote AI_ux -> {ROOT}")


if __name__ == "__main__":
    main()
