# 📈 Automated Crypto Market ETL Pipeline & Dashboard

An end-to-end data pipeline built with Python, SQLite, and Streamlit that fetches real-time cryptocurrency market data, cleans and transforms it, and presents actionable insights through an interactive web dashboard[cite: 1].

---

## 🏗️ Architecture Flow
1. **Extract**: Ingests real-time crypto financial metrics directly from the CoinGecko REST API using `requests`.
2. **Transform**: Cleans null values, formats data types, and appends ingestion timestamps using `pandas`.
3. **Load**: Persists structured time-series data into an embedded `SQLite` database (`crypto_analytics.db`).
4. **Visualize**: Queries the database to render interactive KPI metrics and distribution charts using `Streamlit` & `Plotly`.

---

## 🛠️ Tech Stack
* **Language**: Python
* **Database**: SQLite
* **Data Engineering / Ingestion**: Pandas, Requests
* **Web Dashboard & Visualization**: Streamlit, Plotly

---

## ✨ Key Features
* **Automated Data Pipeline**: Single-command ETL process to ingest and store market metrics.
* **Persistent Historical Data**: Appends new ingestion cycles into SQLite to track crypto trends.
* **Interactive UI**: Live metric cards (24h high, low, volume) and responsive Plotly visual charts.

---

## 🚀 How to Run Locally (Windows CMD / PowerShell)

### 1. Clone the Repository
```bash
git clone https://github.com/kyriakossts-source/crypto-market-pipeline.git
```

### 2. Navigate to the Directory
```bash
cd crypto-market-pipeline
```

### 3. Create a Virtual Environment 
```bash
python -m venv env
```

### 4. Activate the Environment
* **Command Prompt (CMD):**
  ```cmd
  env\Scripts\activate.bat
  ```
* **PowerShell:**
  ```powershell
  .\env\Scripts\Activate.ps1
  ```

### 5. Install Dependencies
```bash
pip install -r requirements.txt
```

### 6. Run the ETL Pipeline
Fetches latest market data and updates `crypto_analytics.db`:
```bash
python etl.py
```

### 7. Launch the Dashboard
```bash
python -m streamlit run app.py
```
### 8. Open in Browser
Visit your local server at:
```text
http://localhost:8501
```
