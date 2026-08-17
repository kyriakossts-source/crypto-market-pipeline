# Automated Crypto Market ETL Pipeline & Dashboard

An end-to-end data pipeline built with Python, SQLite, and Streamlit that fetches real-time market data, transforms it, and presents actionable insights on an interactive dashboard.

---

##  Architecture Flow
1. **Extract**: Ingests real-time cryptocurrency metrics from CoinGecko REST API using `requests`.
2. **Transform**: Formats data types, cleans null values, and appends ingestion timestamps with `pandas`.
3. **Load**: Persists structured data into an embedded `SQLite` database (`crypto_analytics.db`).
4. **Visualize**: Renders interactive KPI cards and distribution charts via `Streamlit` & `Plotly`.

---

## Tech Stack
- **Language**: Python
- **Database**: SQLite
- **Data Engineering**: Pandas, Requests
- **Visualization**: Streamlit, Plotly

---

##  How to Run Locally

1. **Clone the repository & install dependencies:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

2. **Run the ETL pipeline:**
   \`\`\`bash
   python etl.py
   \`\`\`

3. **Launch the Streamlit Dashboard:**
   \`\`\`bash
   python -m streamlit run app.py
   \`\`\`