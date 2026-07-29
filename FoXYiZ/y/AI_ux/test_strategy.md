# AI_ux — portable AI chatbot yPAD template

Use this when the product under test has a **chat / prompt box on the main page**.

## Pattern (copy → retarget)

1. Set `base_url`, `prompt_locator`, `btn_send`, `response_locator` in `y3Designs.csv`.
2. Put prompt variants in **D1 / D2 / D3** on `type_prompt` (same automation steps).
3. Keep **Manual** plans for quality / safety / multi-turn / latency.
4. Flip `PAPI_ChatPost` / `PAI_TextPrompt` to `Run=Y` when you have a real chat API or OpenAI-compatible endpoint (+ key).

## Default seed

Ships pointed at **foxyiz.com** as a working example of the UI chat pattern (same product as `AI_foxyiz`, but generic plan names). Prefer **`AI_foxyiz`** for FoXYiZ-specific chips/keywords; use **`AI_ux`** as the blank canvas for *other* AI products.

## Mix of UI + API + AI

| Tag | Mechanism |
|-----|-----------|
| `UI;Chat` | Type → Send → `xGetText` response region |
| `API;Chat` | `xPost` + `payloads/chat_prompt.json` + `xCompareJson` (httpbin placeholder) |
| `AI;Prompt` | Catalog `xTextPrompt` (key placeholder — leave Manual until configured) |
| `Manual` | Human evaluation pads |

## Run

```powershell
$env:FOXYIZ_ROOT = "$PWD\FoXYiZ"
.\FoXYiZ\f\FoXYiZ.exe --config FoXYiZ\f\fStart\AI_ux.json
```
