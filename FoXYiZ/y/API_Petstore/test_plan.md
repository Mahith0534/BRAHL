# petstore — Swagger Petstore API suite

**App / docs:** [Swagger Petstore UI](https://petstore.swagger.io/#/pet/addPet)  
**API base:** `https://petstore.swagger.io/v2` (OpenAPI: `/v2/swagger.json`)

Purpose: exercise FoXYiZ **xAPI / xJSON** automation against a public reference API (Pet, Store, User), including happy-path CRUD, negatives, and light performance smokes.

## Module tags

| Tag | Plans |
|-----|--------|
| `Smoke` | findByStatus available, store inventory |
| `Pet` / `CRUD` | add → get → update → delete; status filters |
| `Store` | place/get/delete order, inventory |
| `User` | create → get → login → logout; update |
| `Security` | missing pet/user → 404 |
| `Performance` | findByStatus, inventory, small GET batch |
| `API` | all of the above (shared) |

## Payloads

JSON bodies live under `y/petstore/payloads/` (pet add/update, order, user create/update). Pet/user ids are fixed demo values (`922337001001`) so runs are repeatable.

## fStart

`f/fStart/petstore.json` — tags `Smoke`+`API`, capture off (API-only), timeout 15s.

## Suggested Run chips

- Gate: `Smoke`
- Pet focus: `Pet`
- Hardening: `Security` + `Performance`
- Full: `API` (or leave multi-select)
