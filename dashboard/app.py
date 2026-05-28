import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from streamlit_autorefresh import st_autorefresh

DATABASE_URL = (
    "postgresql+psycopg2://"
    "postgres:postgres@localhost:5432/crypto_db"
)

st.set_page_config(
    page_title="Crypto Anomaly Detection Dashboard",
    layout="wide"
)

st_autorefresh(
    interval=5000,
    key="anomaly_refresh"
)



engine = create_engine(DATABASE_URL)

st.title("🚨 Crypto Anomaly Detection Dashboard")

query = """
SELECT *
FROM anomalous_trades
ORDER BY trade_time DESC
LIMIT 100
"""

df = pd.read_sql(
    query,
    engine
)

total_anomalies = len(df)

price_anomalies = len(
    df[df["anomaly_type"] == "price_anomaly"]
)

volume_anomalies = len(
    df[df["anomaly_type"] == "volume_spike_anomaly"]
)

whale_anomalies = len(
    df[df["anomaly_type"].str.contains("whale", case=False, na=False)]
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total anomalies", total_anomalies)
col2.metric("Price anomalies", price_anomalies)
col3.metric("Volume spikes", volume_anomalies)
col4.metric("Whale trades", whale_anomalies)

if not df.empty:
    st.subheader("Anomalies by Type")

    anomaly_counts = df["anomaly_type"].value_counts()

    st.bar_chart(anomaly_counts)

    st.subheader("Anomalous Trade Values Over Time")

    chart_df = df.sort_values("trade_time")

    st.line_chart(
        chart_df,
        x="trade_time",
        y="trade_value"
    )

    st.subheader("Latest Detected Anomalies")

    st.dataframe(
        df,
        use_container_width=True
    )

else:
    st.info("No anomalies detected yet.")