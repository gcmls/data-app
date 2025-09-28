from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
import pandas as pd
from src.app_core.repo import load_df

app = FastAPI(title="Data App API", version="1.0.0")
DF = load_df()

class Stats(BaseModel):
    rows: int
    cols: int
    columns: list[str]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/stats", response_model=Stats)
def stats():
    return Stats(rows=len(DF), cols=DF.shape[1], columns=list(DF.columns))

@app.get("/sample")
def sample(n: int = Query(5, ge=1, le=100)):
    return DF.head(n).to_dict(orient="records")

@app.get("/agg")
def agg(by: str = Query("region"), metric: str = Query("revenue")):
    if by not in DF.columns or metric not in DF.columns:
        return {"error": "invalid column"}
    out = DF.groupby(by, as_index=False)[metric].sum().sort_values(metric, ascending=False)
    return out.to_dict(orient="records")
