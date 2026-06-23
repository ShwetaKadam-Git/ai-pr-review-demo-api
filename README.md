# ai-pr-review-demo-api

FastAPI backend demo for the [ai-pr-review-platform](https://github.com/ShwetaKadam-Git/ai-pr-review-platform).

Accepts PR diffs over HTTP, runs the mock AI review engine, and persists
results to SQLite. Serves history to [ai-pr-review-demo-frontend](https://github.com/ShwetaKadam-Git/ai-pr-review-demo-frontend).

## Run locally

```bash
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

## Endpoints

- `POST /review` — submit a diff, get findings back
- `GET /reviews` — list recent reviews
- `GET /reviews/{id}` — get a single review's findings

## Deployment

Free-tier deploy target: Render. See [ai-pr-review-platform/docs/cost.md](https://github.com/ShwetaKadam-Git/ai-pr-review-platform/blob/main/docs/cost.md).