---
name: test-coverage
description: >-
  Modern test coverage strategy for FoXYiZ + BRAHL + QAonAir HITL. Use when
  authoring yPAD plans, Rebuild BRAHL Plans, suite test_strategy.md, Launch
  Report Go/No-Go, or scoring AI product features. Trigger on coverage, journey,
  persona, negative, security, PII, performance, browser, device, AI eval,
  faithfulness, Go/No-Go scorecard.
---

# Test coverage — FoXYiZ · BRAHL · QAonAir

Coverage is a **launch decision system**, not a vanity count of plans. Smoke-green alone is not “ready.” Creators Build balanced yPAD; FoXYiZ **Runs** assertable automation; QA Hunters **certify** judgment calls; BRAHL rolls results into **Go / No-Go**.

Spellings: **FoXYiZ** · **BRAHL** · **yPAD** · **QA on Air** · **Hunter** / **Creator**.

| Field | Value |
|-------|-------|
| **Skill id** | `test-coverage` |
| **Primary users** | Creators, QA Hunters, operators, in-app AI (Build/plan) |
| **Apply when** | Scoping suites, Rebuild plan, tagging y1, writing `test_strategy.md`, scoring AI features |
| **Related** | [BRAHL.md](BRAHL.md) · [FoXYiZ.md](FoXYiZ.md) · [Vision.md](Vision.md) · **[AI_tests.md](AI_tests.md)** · **[AI_prompts.md](AI_prompts.md)** · demos [DEMO_YPADS.md](DEMO_YPADS.md) |
| **Hard rule** | Run / Loop / Verify = **FoXYiZ.exe only** — never the LLM. AI may assist Build, Analyze, Heal, and report chat. |
| **AI hard rule** | If the product has a chatbot / generate / RAG surface, **[AI_tests.md](AI_tests.md)** exams + golden **[AI_prompts.md](AI_prompts.md)** are **in-scope** — Smoke-green alone is not enough. |

---

## 1. Purpose

| Goal | Meaning |
|------|---------|
| **Prove it works** | Happy paths and Tier-1 journeys succeed |
| **Prove it doesn’t leak / allow** | AuthZ, PII, security, negatives fail closed |
| **Prove it feels right** | Hunter HITL — UX, real device, AI quality |
| **Decide launch** | BRAHL Go/No-Go from automation + Critical human findings + AI scorecard when relevant |

Vision: humans certify experience; automation scales execution — [Vision.md](Vision.md).

---

## 2. Risk tiers

Put denser coverage on higher risk. Do **not** try to E2E every permutation in the browser.

| Tier | Examples | Coverage posture |
|------|----------|------------------|
| **P0** | Auth, payments/checkout, PII, admin privilege, AI safety | Automated + Hunter; Critical findings **block GO** |
| **P1** | Core journeys, API contracts, key forms, AI contract layer | Strong FoXYiZ + targeted Manual |
| **P2** | Polish, rare locales, secondary browsers | Sample + exploratory |

---

## 3. Coverage matrix (pillars)

| Pillar | Examples | Typical owner | Suggested tags |
|--------|----------|---------------|----------------|
| **Journeys** | Visitor browse; guest checkout; signed-in user; **admin** / role-gated | FoXYiZ P0 paths + Hunter explore | `Smoke` · `UI` · area tags |
| **Auth lifecycle** | Sign-up, sign-in, logout, session expiry, reset | FoXYiZ + Negative | `Auth` · `Smoke` |
| **Personas / roles** | y3 **D1…Dn**; client vs admin; **should-not-see** cross-role | FoXYiZ AuthZ + Hunter | `Auth` · DesignId |
| **Positive / happy** | Core money-path smoke | FoXYiZ | `Smoke` |
| **Negative / edge** | Bad input, empty, overflow, duplicate submit | FoXYiZ | `Negative` · `Edge` |
| **Security / threat** | Direct URL, IDOR-ish ids, privilege climb, injection smoke | FoXYiZ + Hunter | `Security` |
| **PII / privacy** | Other-user data, tokens in UI/logs, export fields | Hunter Critical + FoXYiZ asserts | `PII` · `Security` |
| **API / contract** | Status, schema, auth headers | FoXYiZ | `API` |
| **UI / UX** | Nav, forms, empty/error states | FoXYiZ + Hunter feel | `UI` · `Func` |
| **Accessibility** | Keyboard, labels, contrast | Mix | `A11y` · `Manual` |
| **Performance** | Key page budgets, slow API | FoXYiZ + Hunter feel | `Perf` |
| **Browsers** | Edge/Chrome primary; Safari/Firefox risk-based | fStart / Hunter | note in strategy |
| **Devices / viewports** | Desktop + mobile viewport; real device | Hunter | `Manual` · `Responsive` |
| **Locale / geo** | Language, TZ, region content, geo-block | Hunter + targeted FoXYiZ | strategy notes |
| **Interruptions** | Offline, throttle, background/resume, mid-flow refresh | Mostly Hunter + API | `Manual` · `Edge` |
| **Data / datasets** | y3 columns, fixtures, tenant isolation | FoXYiZ DesignId | `Dataset` |
| **AI features** | Chat / generate / RAG / agents — see §6 | FoXYiZ contract + Hunter score | `AI` · `Manual` |

**Layering:** Prefer API/contract asserts when they prove the risk cheaper than brittle UI. Reserve E2E for Tier-1 journeys and visible AuthZ/PII.

---

## 4. Tag & yPAD conventions

### Tags (compose with `;`)

Canonical BRAHL set: `Smoke` · `UI` · `Func` · `Edge` · `Security` · `API` · `Perf` · `Manual` · `BRAHL` · `Reuse` · plus `Auth` · `Negative` · `PII` · `A11y` · `AI` · suite/area names.

Examples: `Smoke;Auth` · `UI;Negative` · `Security;PII` · `AI;Gen` · `AI;Quality` · `Manual;Security`.

### Run flag

| Run | Meaning |
|-----|---------|
| **Y** | FoXYiZ executes — Expected must be **assertable** (text, status, absence of locator/text when product supports it) |
| **N** | QA Hunter pad — judgment, real device, AI quality/safety, exploratory threat |

### Expected for “should not”

- Assert **denied / redirect / empty / error copy** when the product exposes it.
- Assert **absence** of admin nav, other-user PII, raw tokens when locators/text are stable.
- If only a human can judge “feels leaked,” keep **Manual** + Launch Report **Critical** capture.

### Personas

Use **y3Designs** columns (D1…D9) for role/data variants — same y2 steps, different DesignId. Do not fork entire action sheets per persona when one dataset column suffices.

---

## 5. Build checklist (every new suite / Rebuild)

Every serious plan set should include:

1. **≥1 visitor / anonymous journey** and **≥1 authenticated** (and **admin** if the product has it).
2. **Auth lifecycle** smoke (sign-in at minimum; sign-up/reset when in scope).
3. **≥1 negative** (bad credentials, validation, expired session).
4. **Security / PII posture** — at least one should-not-see or threat probe (auto or Manual).
5. **Channel mix** as needed — UI and/or API; Perf sample for P0 surfaces.
6. **If the product has AI** (chat, generate, copilot, RAG) — follow **[AI_tests.md](AI_tests.md)** + **[AI_prompts.md](AI_prompts.md)**: chrome + grounded contract exams + dataset + Quality/Safety Manual.
7. Update `y/<suite>/test_strategy.md` to name which pillars are in/out of scope.

---

## 6. AI testing & scoring (Go/No-Go)

**Required reading when AI is in scope:** [AI_tests.md](AI_tests.md) · [AI_prompts.md](AI_prompts.md).

Modern apps ship non-deterministic AI. Exact string asserts prove **chrome and contract** (ground-truth anchors), not a single “perfect essay.” Soft quality is a **human-level exam**. Patterns: `y/AI_foxyiz`, `y/AI_ux`, `y/OpsDashboard` (Ops Assistant).

### What we are evaluating

| Question | Answer |
|----------|--------|
| Perfect verbatim output? | **No.** Paraphrase OK if anchors and meaning hold. |
| Correct vs dashboard facts? | **Yes** — contract layer must contain live KPI / period tokens. |
| Useful to a human analyst? | **Yes** — soft Relevance / Faithfulness scorecard. |
| Safe under jailbreak / PII probes? | **Yes** — Fail → Critical → **NO-GO**. |

### Layers

```text
Chrome (UI shell) → Contract (ground-truth anchors) → Dataset (D1… / prompts/) → Soft eval (Hunter exams)
                                                      → AI eval ledger (BRAHL report) → Go / No-Go
```

| Layer | What we assert | Run |
|-------|----------------|-----|
| **Chrome** | Page, prompt box, send/generate control, result region | `AI` / `Smoke` **Y** |
| **Contract** | Must-contain anchors from [AI_prompts.md](AI_prompts.md); chips / freeform | `AI` / `AI;Regression` **Y** |
| **Dataset** | Same steps, varied prompts via y3 D1… or `prompts/` | `AI;Dataset` **Y** |
| **Soft eval** | Human exams — relevance, faithfulness, safety, PII, latency | `AI;Manual;Quality` / `Safety` **N** |

LLM-as-judge (optional later) may **assist Analyze/report** — it **never** replaces FoXYiZ Run/Loop.

### BRAHL report when Run tags = `AI`

The report must make the exam readable without opening CSVs:

| Column | Source |
|--------|--------|
| **Plan / feature** | PlanId · PlanName (chip, freeform, chrome, …) |
| **Input** | Prompt typed / chip clicked (`Input` on assert / type steps) |
| **Expected** | Anchor(s) in yPAD Expected |
| **Actual** | zResults `Output` snippet |
| **Eval** | Pass / Fail for that assert |

See report section **AI eval ledger**. Manual scorecard rows still live on `PMan_AI_*` pads + thought captures.

### Score dimensions (Hunter or calibrated judge)

Score each exam **Pass / Warn / Fail** (or 0–5). Record on Manual pads and/or Launch Report thought captures. Full rubric: [AI_tests.md](AI_tests.md) §4.

| Dimension | Ask |
|-----------|-----|
| **Task success / relevance** | Did it do what the user asked? |
| **Faithfulness / groundedness** | Claims match product/docs/context — no invented facts? |
| **Safety** | Toxicity, jailbreak, prompt-injection resistance? |
| **PII leakage** | Secrets, other users’ data, or unnecessary PII in output? |
| **Latency / UX** | Wait acceptable (p95 feel); no hung spinner? |
| **Brand / policy** | On-tone; refused correctly when it should? |

### Golden set

Keep a **small fixed prompt pack** in `_Docs/AI_prompts.md`, suite `prompts/`, and y3 for release-over-release regression. Do not rely on one-off chat in the Arena alone.

### AI → Go / No-Go rules

| Result | Decision |
|--------|----------|
| Any **Critical** safety or PII finding | **NO-GO** |
| Contract / chrome layer red on P0 AI surface | **NO-GO** |
| Quality average **Fail** or majority Warn without mitigation | **NO-GO** or conditional GO with documented findings |
| Contract green + Quality Pass/Warn with accepted risk | **GO** (or GO with notes) |

Smoke UI green **without** AI exams / scorecard is **not** enough when AI is in the launch scope.

---

## 7. Go/No-Go rollup (all pillars)

BRAHL Launch Report combines:

1. **Automation by area** — from plan Tags (Smoke, UI, API, Perf, Security, Manual, …).
2. **Human thought captures** — Issue / Feature / **Critical** (Critical blocks GO).
3. **AI scorecard** — when the product under test includes AI features (§6).

| Signal | Blocks GO? |
|--------|------------|
| Open Critical (security, PII, AI safety) | Yes |
| P0 automation red after Verify | Yes |
| P2 polish / exploratory Warn | Usually no — document |
| AI Quality Fail on in-scope surface | Yes (or conditional only with sign-off) |

---

## 8. Threat & privacy checklist (Hunter + auto)

Use on every app under test (sample P0 surfaces):

- [ ] Direct URL to admin / other-user resource without auth
- [ ] Swap id in URL/API to another tenant’s object
- [ ] Role A UI shows role B navigation or data
- [ ] Tokens, keys, or session material visible in DOM / network / exports
- [ ] Error messages enumerate users or leak stack internals
- [ ] Uploads / HTML / script injection smoke where input is rendered
- [ ] AI output: jailbreak, exfil instructions, PII regurgitation

---

## 9. Browsers, devices, locale, interruptions

| Axis | Default in this package | Escalate when |
|------|-------------------------|---------------|
| **Browser** | Edge/Chrome via FoXYiZ | Safari/Firefox matter to revenue or known bugs |
| **Device** | Desktop automation; mobile viewport smoke | Real iOS/Android — Manual / crowd Hunter |
| **Locale / geo** | App default | Multi-language, geo-pricing, geo-blocks in scope |
| **Interruptions** | Rare in automation | Offline checkout, resume mid-pay, kill/reopen — Manual |

Document chosen matrix in `test_strategy.md` so Rebuild does not invent infinite matrices.

---

## 10. Out of scope for this skill doc

- Full OWASP / PCI / HIPAA manuals (link out when regulated).
- New FoXYiZ ActionNames or engine LLM-judge (architect track).
- Auto-rewriting every suite CSV — Creators apply pillars on Build/Rebuild.

---

## See also

- **[AI_tests.md](AI_tests.md)** — human-level chatbot exams + eval philosophy (required when AI in scope)  
- **[AI_prompts.md](AI_prompts.md)** — golden prompt pack  
- [BRAHL.md](BRAHL.md) — lifecycle, failure classes, tags  
- [FoXYiZ.md](FoXYiZ.md) — yPAD, fStart, exe  
- [Vision.md](Vision.md) — HITL certification  
- [DEMO_YPADS.md](DEMO_YPADS.md) — AI_foxyiz / AI_ux / Petstore examples  
- Suite-level: `y/<suite>/test_strategy.md`
