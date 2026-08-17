import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Ρύθμιση τίτλου και διάταξης σελίδας
st.set_page_config(page_title="Crypto Pipeline", layout="wide")
st.title("📊 Live Crypto Analytics Dashboard")
st.caption("SQLite + Python Data Pipeline")

# Σύνδεση στη SQLite βάση και ανάγνωση δεδομένων
conn = sqlite3.connect("crypto_analytics.db")
try:
    df = pd.read_sql_query("SELECT * FROM crypto_metrics ORDER BY ingested_at DESC", conn)
except Exception:
    st.error("⚠️ Δεν βρέθηκε η βάση δεδομένων. Τρέξε πρώτα το python etl.py!")
    st.stop()
finally:
    conn.close()

if not df.empty:
    # Παίρνουμε την πιο πρόσφατη καταγραφή
    latest_time = df['ingested_at'].max()
    latest_df = df[df['ingested_at'] == latest_time]

    # KPI κάρτες στην κορυφή
    col1, col2, col3 = st.columns(3)
    col1.metric("Top Crypto", latest_df.iloc[0]['name'], f"${latest_df.iloc[0]['current_price']:,.2f}")
    col2.metric("Συνολικό Market Cap (Top 10)", f"${latest_df['market_cap'].sum():,.0f}")
    col3.metric("Τελευταίο Ingestion", str(latest_time))

    st.divider()

    # Διαδραστικό Bar Chart
    fig = px.bar(
        latest_df,
        x="symbol",
        y="price_change_percentage_24h",
        color="price_change_percentage_24h",
        color_continuous_scale="RdYlGn",
        title="24ωρη Ποσοστιαία Μεταβολή Τιμών (%)"
    )
    st.plotly_chart(fig, use_container_width=True)

    # Προβολή πίνακα δεδομένων
    st.subheader("📋 Εγγραφές από τη βάση δεδομένων (SQLite Table)")
    st.dataframe(latest_df, use_container_width=True)