# analyze_wallet_helius.py

import requests
import json
import os

API_KEY = "df1dba6d-d54d-4fc8-b253-6cc5c5bf3fa4"
wallet_address = "BiN2VggT6LxNKL8NRvnUBE4pGqTHqSi8CgT3aAEd8zxS"
BASE_URL = f"https://api.helius.xyz/v0/addresses/{wallet_address}/transactions?api-key={API_KEY}"

OUTPUT_DIR = "output"
RAW_OUTPUT = os.path.join(OUTPUT_DIR, "helius_BiN2V_transactions.json")
FILTERED_OUTPUT = os.path.join(OUTPUT_DIR, "helius_BiN2V_pumpfun_only.json")

# Known Pump.fun Program ID
PUMPFUN_PROGRAM_ID = "6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P"

def fetch_wallet_transactions():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        txs = response.json()
        with open(RAW_OUTPUT, "w") as f:
            json.dump(txs, f, indent=2)
        print(f"[+] Saved full transaction history to {RAW_OUTPUT}")
        return txs
    else:
        print(f"[ERROR] Failed to fetch transactions: {response.status_code}")
        print(response.text)
        return None

def filter_pumpfun_transactions(txs):
    if not txs:
        return

    pumpfun_txs = []
    for tx in txs:
        if "tokenTransfers" in tx:
            for transfer in tx["tokenTransfers"]:
                if transfer.get("programId") == PUMPFUN_PROGRAM_ID:
                    pumpfun_txs.append(tx)
                    break

    with open(FILTERED_OUTPUT, "w") as f:
        json.dump(pumpfun_txs, f, indent=2)

    print(f"[+] Saved pump.fun related transactions to {FILTERED_OUTPUT}")
    print(f"[INFO] Found {len(pumpfun_txs)} pump.fun transactions.")

if __name__ == "__main__":
    transactions = fetch_wallet_transactions()
    if transactions:
        filter_pumpfun_transactions(transactions)
