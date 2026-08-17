import requests
import pandas as pd
import sqlite3
from datetime import datetime

DB_FILE = "crypto_analytics.db"

def extract_data():
    """1. EXTRACT: Τραβάει live δεδομένα από το CoinGecko API"""
    print("⏳ 1/3 Ανάκτηση δεδομένων από το API...")
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": "false"
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

def transform_data(raw_data):
    """2. TRANSFORM: Καθαρίζει και μορφοποιεί τα δεδομένα"""
    print("⏳ 2/3 Επεξεργασία και καθαρισμός δεδομένων...")
    df = pd.DataFrame(raw_data)
    
    cols = ['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume', 'price_change_percentage_24h']
    df = df[cols].copy()
    
    df['ingested_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df['symbol'] = df['symbol'].str.upper()
    return df

def load_to_sqlite(df):
    """3. LOAD: Αποθηκεύει τα δεδομένα στη SQLite βάση"""
    print("⏳ 3/3 Αποθήκευση στη βάση SQLite...")
    conn = sqlite3.connect(DB_FILE)
    df.to_sql("crypto_metrics", conn, if_exists="append", index=False)
    conn.close()

if __name__ == "__main__":
    print("🚀 Εκκίνηση ETL Pipeline...")
    raw = extract_data()
    cleaned_df = transform_data(raw)
    load_to_sqlite(cleaned_df)
    print(f"✅ Ολοκληρώθηκε! Αποθηκεύτηκαν {len(cleaned_df)} εγγραφές στο {DB_FILE}")