import pandas as pd
import os

DATA_PATH = os.environ.get("DATA_PATH", "data/example.csv")

def load_df() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH, parse_dates=["date"])
