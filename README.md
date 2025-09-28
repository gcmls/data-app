# Data App (FastAPI + Streamlit) — Full
A clean data app pattern with a FastAPI backend exposing dataset stats/samples/aggregates and a Streamlit front-end.

## Quickstart
```bash
make setup
make serve-api   # :8001
make serve-ui    # :8501
```
Then open http://localhost:8501

## Features
- FastAPI endpoints: /health, /stats, /sample, /agg
- Streamlit UI: filters, interactive table, simple chart
- DuckDB-ready pattern, using CSV by default
- Tests (pytest) + CI
