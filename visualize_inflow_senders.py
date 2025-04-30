# visualize_inflow_senders.py

import json
import os
import matplotlib.pyplot as plt
import pandas as pd

INPUT_FILE = "output/helius_BiN2V_inflow_native_summary.json"
OUTPUT_IMAGE = "output/sol_inflow_per_sender.png"

def visualize_sender_inflow():
    if not os.path.exists(INPUT_FILE):
        print("[ERROR] Inflow summary not found.")
        return

    with open(INPUT_FILE, "r") as f:
        data = json.load(f)

    sol_data = data.get("SOL", {})
    total_sol = sol_data.get("total_SOL", 0)
    senders = sol_data.get("senders", [])

    if not senders:
        print("[INFO] No sender data found.")
        return

    avg_amount = total_sol / len(senders)
    rows = [{"Sender Wallet": sender, "Estimated SOL": round(avg_amount, 4)} for sender in senders]
    df = pd.DataFrame(rows).sort_values("Estimated SOL", ascending=False)

    plt.figure(figsize=(10, 6))
    plt.barh(df["Sender Wallet"], df["Estimated SOL"])
    plt.xlabel("Estimated SOL Received")
    plt.title("Inflow SOL per Sender (Estimated Average)")
    plt.tight_layout()

    plt.savefig(OUTPUT_IMAGE)
    print(f"[+] Saved plot to {OUTPUT_IMAGE}")

if __name__ == "__main__":
    visualize_sender_inflow()
