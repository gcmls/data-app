import streamlit as st
import requests, os
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data App", layout="wide")
st.title("📊 Data App — FastAPI + Streamlit")

api = os.environ.get("API_URL", "http://localhost:8001")

with st.sidebar:
    st.header("Controls")
    n = st.slider("Sample rows", 1, 50, 5)
    group_by = st.selectbox("Aggregate by", ["region","channel"])
    metric = st.selectbox("Metric", ["revenue","orders"])

cols = st.columns(2)
with cols[0]:
    if st.button("Health"):
        try:
            st.json(requests.get(f"{api}/health", timeout=5).json())
        except Exception as e:
            st.error(e)
    st.subheader("Sample")
    r = requests.get(f"{api}/sample", params={"n": n})
    df = pd.DataFrame(r.json())
    st.dataframe(df)

with cols[1]:
    st.subheader("Aggregate")
    r = requests.get(f"{api}/agg", params={"by": group_by, "metric": metric})
    agg = pd.DataFrame(r.json())
    if "error" in agg:
        st.error(agg["error"])
    else:
        st.dataframe(agg)
        fig = px.bar(agg, x=group_by, y=metric)
        st.plotly_chart(fig, use_container_width=True)
