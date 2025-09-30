# PMM Insights → Messaging Agent

A Streamlit prototype that transforms multi-source inputs (product background, reviews, interviews)
into **proto-personas → JTBD → positioning → messaging** using reusable prompt frameworks.

## Quick Start (Poetry)

```bash
# 1) Install poetry if needed
# macOS: brew install poetry
# otherwise: pipx install poetry

# 2) From the repo root:
poetry install

# 3) Add your OpenAI key
cp .env.example .env
# then edit .env and set OPENAI_API_KEY=...

# 4) Run
poetry run streamlit run pmm_messaging/app.py
```

## Inputs
- Background form (product, goals, category, competitors)
- Evidence files (CSV reviews, interview notes, win/loss, competitor PDFs/URLs)

## Outputs
- Personas (with confidence), JTBD, Positioning (Dunford template), Messaging framework
- Export: JSON/Markdown review packet

> This prototype is intentionally lightweight to demonstrate **agentic flows + reusable prompts**
for PMM enablement.
