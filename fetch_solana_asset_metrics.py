# fetchers/fetch_solana_asset_metrics.py

import requests
import json
import os

API_KEY = "ZI8F0cXqY0JB-RHBmzZnawVqRm3FbAXaJodsamGCEsHqe0tx"
BASE_URL = "https://api.messari.io"

headers = {
    "accept": "application/json",
    "x-messari-api-key": API_KEY
}

def fetch_solana_price_timeseries():
    url = f"{BASE_URL}/metrics/v2/assets/solana/metrics/price/time-series/1d"
    params = {
        "start": "2025-01-01T00:00:00Z",
        "end": "2025-01-31T23:59:59Z"
    }
    response = requests.get(url, headers=headers, params=params)

    print("[DEBUG] Response content:")
    print(response.text)

    if response.status_code == 200:
        os.makedirs("output", exist_ok=True)
        with open("output/sol_price_jan2025.json", "w") as f:
            json.dump(response.json(), f, indent=2)
        print("[+] Saved output/sol_price_jan2025.json")
    else:
        print(f"[ERROR] Failed to fetch Solana price timeseries: {response.status_code}")

if __name__ == "__main__":
    fetch_solana_price_timeseries()
