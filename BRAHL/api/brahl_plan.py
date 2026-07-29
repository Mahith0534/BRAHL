"""Generate structured BRAHL Plans from requirements (qoa2-style).

Local-model friendly: larger target sizes, JSON repair + one retry, honest
fallback labeling when the model cannot return parseable JSON.
"""

from __future__ import annotations

import json
import re
from typing import Any

from ai_assist import chat_metered, is_ai_available

# Target sizes for end-to-end regression-oriented plans (local or cloud).
TARGET_STORIES = 10
TARGET_CASES = 28
MAX_PLAN_TOKENS = 2800
MAX_AUTO_MATERIALIZE = 36


def _fallback_plan(requirement: str) -> dict[str, Any]:
    """Scripted plan when AI is unavailable or returns unusable JSON."""
    req = (requirement or "").strip()
    # Seed a few titles from requirement words so offline plans aren't identical
    words = re.findall(r"[A-Za-z][A-Za-z0-9_-]{3,}", req)
    stop = {
        "need",
        "want",
        "that",
        "this",
        "with",
        "from",
        "every",
        "almost",
        "create",
        "testing",
        "tested",
        "application",
        "component",
        "deeper",
        "many",
        "more",
        "so",
        "the",
        "and",
        "for",
        "end",
    }
    seeds = [w for w in words if w.lower() not in stop][:8]
    while len(seeds) < 8:
        seeds.append(f"Area{len(seeds) + 1}")

    stories = [
        {"title": "Landing & navigation smoke", "description": "Home and primary nav load", "automated": True},
        {"title": "Auth & session", "description": "Login, logout, session persistence", "automated": True},
        {"title": "Core happy path", "description": "Primary user journey end-to-end", "automated": True},
        {"title": "Forms & validation", "description": "Required fields, errors, submit", "automated": True},
        {"title": "Search / list / detail", "description": "Browse, filter, open detail", "automated": True},
        {"title": "Checkout or submit flow", "description": "Multi-step submit / cart / confirm", "automated": True},
        {"title": "Settings / account", "description": "Profile and preference changes", "automated": True},
        {"title": "Error & empty states", "description": "404, empty lists, API failures", "automated": True},
        {"title": "Mobile viewport", "description": "Layout on phone — manual on real device", "automated": False},
        {"title": "QA Hunter exploration", "description": "UX, a11y, visual polish", "automated": False},
    ]
    tests: list[dict[str, Any]] = []
    for i in range(TARGET_CASES):
        seed = seeds[i % len(seeds)]
        area = stories[i % len(stories)]["title"].split("&")[0].strip()
        automated = i % 4 != 3  # ~75% automated
        tests.append(
            {
                "id": f"T{i + 1}",
                "title": f"{area}: {seed} check {i + 1}",
                "automated": automated,
            }
        )
    auto = sum(1 for t in tests if t.get("automated"))
    return {
        "summary": (req[:500] or "Regression-oriented BRAHL strategy for MVP launch")
        + "\n\n_(Template plan — local AI JSON was missing or invalid. Re-generate or tighten the requirement.)_",
        "user_stories": stories,
        "test_cases": tests,
        "automated_count": auto,
        "manual_count": len(tests) - auto,
        "run_how": "Run FoXYiZ fEngine2 locally or on server — Tests / Steps / Test data CSVs in y/<suite>/",
    }


def _looks_like_generic_titles(plan: dict[str, Any]) -> bool:
    titles = [str(t.get("title") or "") for t in plan.get("test_cases") or []]
    if len(titles) < 4:
        return False
    generic = sum(1 for t in titles if re.fullmatch(r"Test case \d+", t.strip(), re.I))
    return generic >= max(4, len(titles) // 2)


def _normalize_plan(plan: dict[str, Any], requirement: str) -> dict[str, Any]:
    stories = list(plan.get("user_stories") or [])
    cases = list(plan.get("test_cases") or [])
    # Soft-cap runaway models; keep room for regression depth
    if len(stories) > 16:
        stories = stories[:16]
    if len(cases) > 48:
        cases = cases[:48]
    for i, t in enumerate(cases):
        if not t.get("id"):
            t["id"] = f"T{i + 1}"
        if "automated" not in t:
            t["automated"] = True
    plan["user_stories"] = stories
    plan["test_cases"] = cases
    plan["automated_count"] = sum(1 for t in cases if t.get("automated") is not False)
    plan["manual_count"] = len(cases) - plan["automated_count"]
    if not (plan.get("summary") or "").strip():
        plan["summary"] = requirement[:500]
    if not plan.get("run_how"):
        plan["run_how"] = (
            "Run FoXYiZ fEngine2 locally or on server — Tests / Steps / Test data CSVs in y/<suite>/"
        )
    return plan


def _repair_json_text(raw: str) -> str:
    text = (raw or "").strip()
    text = re.sub(r"^```(?:json)?\s*", "", text, flags=re.I)
    text = re.sub(r"\s*```$", "", text)
    m = re.search(r"\{[\s\S]*\}", text)
    if m:
        text = m.group(0)
    # Common local-model breakage
    text = re.sub(r",\s*([}\]])", r"\1", text)
    text = text.replace("True", "true").replace("False", "false").replace("None", "null")
    return text


def _close_truncated_json(text: str) -> str:
    """Best-effort close of truncated JSON from local models."""
    stack: list[str] = []
    in_str = False
    esc = False
    for ch in text:
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch in "{[":
            stack.append(ch)
        elif ch == "}" and stack and stack[-1] == "{":
            stack.pop()
        elif ch == "]" and stack and stack[-1] == "[":
            stack.pop()
    if in_str:
        text += '"'
    text = re.sub(r",\s*$", "", text)
    closers = {"{": "}", "[": "]"}
    while stack:
        text += closers[stack.pop()]
    return re.sub(r",\s*([}\]])", r"\1", text)


def _parse_plan_json(raw: str) -> dict[str, Any] | None:
    text = _repair_json_text(raw)
    if not text:
        return None
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        try:
            data = json.loads(_close_truncated_json(text))
        except json.JSONDecodeError:
            return None
    if not isinstance(data, dict):
        return None
    if not (data.get("test_cases") or data.get("user_stories")):
        return None
    return data


def _plan_system_prompt() -> str:
    return (
        "You are a QA architect for QAonAir BRAHL (Build Run Analyze Heal Loop).\n"
        "Return ONE JSON object only — no markdown fences, no commentary, no word-count limit.\n"
        "Schema:\n"
        '{"summary":"...", "user_stories":[{"title":"...","description":"...","automated":true|false}], '
        '"test_cases":[{"id":"T1","title":"...","automated":true|false}], '
        '"automated_count":N, "manual_count":M, '
        '"run_how":"Execute via FoXYiZ fEngine2 — low-code Tests/Steps/Test data CSVs. No Playwright."}\n'
        f"Target about {TARGET_STORIES} user_stories and {TARGET_CASES} test_cases "
        "(more if the requirement asks for deep regression / full E2E).\n"
        "Each test_cases.title must be a concrete scenario (page + action + expected), "
        "never generic names like 'Test case 1'.\n"
        "Cover: landing, nav, auth, forms, lists/detail, submit/checkout, settings, errors, "
        "and a few manual mobile/UX cases (automated:false).\n"
        "FoXYiZ automates; QA Hunters cover manual-only scenarios."
    )


def generate_brahl_plan(
    requirement: str,
    project_name: str = "project",
    app_url: str = "",
    budget_usd: float = 0,
) -> dict[str, Any]:
    requirement = (requirement or "").strip()
    if not requirement:
        raise ValueError("Requirement text required")

    if not is_ai_available():
        plan = _normalize_plan(_fallback_plan(requirement), requirement)
        md = _plan_to_markdown(plan)
        return {
            "brahl_plan": plan,
            "preview_markdown": md,
            "ai": False,
            "source": "fallback",
            "warning": "AI unavailable — showing template plan. Configure FoXYiZ/f/.env (Ollama or OpenAI).",
        }

    system = _plan_system_prompt()
    user = (
        f"Project: {project_name}\nApp URL: {app_url or 'not set'}\nBudget: ${budget_usd:.0f}\n\n"
        f"Requirement:\n{requirement}\n\n"
        "Produce a deep regression-oriented plan. Prefer specific page names and flows "
        "inferred from the URL/requirement. JSON only."
    )

    raw, meta = chat_metered(
        system,
        user,
        role="brahl_plan",
        max_tokens=MAX_PLAN_TOKENS,
    )
    plan = _parse_plan_json(raw) if raw else None
    source = "ai"
    warning = None
    retries = 0

    # One repair pass — local models often wrap JSON or truncate mid-array
    if not plan and raw:
        retries = 1
        fix_user = (
            "Your previous reply was not valid JSON (or was truncated).\n"
            "Reply again with ONLY the full JSON object matching the schema. "
            f"Include ~{TARGET_CASES} concrete test_cases with real titles.\n\n"
            f"Broken reply was:\n{(raw or '')[:1800]}"
        )
        raw2, meta2 = chat_metered(
            system,
            fix_user,
            role="brahl_plan",
            max_tokens=MAX_PLAN_TOKENS,
        )
        meta = meta2 or meta
        plan = _parse_plan_json(raw2) if raw2 else None

    if not plan or _looks_like_generic_titles(plan):
        plan = _fallback_plan(requirement)
        source = "fallback"
        warning = (
            "Local model returned invalid or generic JSON after retry — using template plan. "
            "Try a clearer requirement, a larger local model, or cloud later for richer titles."
        )
        if meta.get("error"):
            warning += f" ({meta.get('error')})"

    plan = _normalize_plan(plan, requirement)
    md = _plan_to_markdown(plan)
    if warning:
        md = f"> **Note:** {warning}\n\n{md}"
    return {
        "brahl_plan": plan,
        "preview_markdown": md,
        "ai": source == "ai",
        "source": source,
        "warning": warning,
        "retries": retries,
    }


def _plan_to_markdown(plan: dict[str, Any]) -> str:
    lines = [
        f"## BRAHL Plan\n\n{plan.get('summary', '')}\n",
        f"**{plan.get('automated_count', 0)}** automated · **{plan.get('manual_count', 0)}** manual test cases\n",
        "### User stories\n",
    ]
    for s in plan.get("user_stories") or []:
        tag = "FoXYiZ" if s.get("automated") else "QA Hunter"
        lines.append(f"- **{s.get('title', '')}** ({tag}) — {s.get('description', '')}")
    lines.append("\n### Test cases\n")
    for t in plan.get("test_cases") or []:
        tag = "auto" if t.get("automated") else "manual"
        lines.append(f"- {t.get('id', '')} {t.get('title', '')} [{tag}]")
    if plan.get("run_how"):
        lines.append(f"\n### Run\n\n{plan['run_how']}")
    return "\n".join(lines)
