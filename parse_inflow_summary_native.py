# parse_inflow_summary_native.py

import json
import os
from collections import defaultdict

INPUT_FILE = "output/helius_BiN2V_transactions.json"
SUMMARY_FILE = "output/helius_BiN2V_inflow_native_summary.json"

def summarize_native_inflows():
    if not os.path.exists(INPUT_FILE):
        print("[ERROR] Input file not found.")
        return

    with open(INPUT_FILE, "r") as f:
        txs = json.load(f)

    inflow_summary = defaultdict(lambda: {"count": 0, "total_lamports": 0, "senders": set()})

    for tx in txs:
        if "nativeTransfers" in tx:
            for transfer in tx["nativeTransfers"]:
                if transfer.get("toUserAccount") == "BiN2VggT6LxNKL8NRvnUBE4pGqTHqSi8CgT3aAEd8zxS":
                    amount = int(transfer.get("amount", 0))
                    sender = transfer.get("fromUserAccount", "unknown")

                    inflow_summary["SOL"]["count"] += 1
                    inflow_summary["SOL"]["total_lamports"] += amount
                    inflow_summary["SOL"]["senders"].add(sender)

    # Final processing
    for token_data in inflow_summary.values():
        token_data["senders"] = list(token_data["senders"])
        token_data["total_SOL"] = token_data["total_lamports"] / 1e9  # Convert lamports to SOL
        del token_data["total_lamports"]

    with open(SUMMARY_FILE, "w") as f:
        json.dump(inflow_summary, f, indent=2)

    print(f"[+] Saved native SOL inflow summary to {SUMMARY_FILE}")

if __name__ == "__main__":
    summarize_native_inflows()
