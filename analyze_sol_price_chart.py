# analyze_sol_price_chart.py

import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load SOL price data
with open("output/sol_price_jan2025.json", "r") as f:
    raw = json.load(f)

data = raw.get("data", {}).get("points", [])

if not data:
    print("[ERROR] No data in sol_price_jan2025.json")
    exit()

# Parse data
sol_price_df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])
sol_price_df["timestamp"] = pd.to_datetime(sol_price_df["timestamp"], unit="s")

# Plot
plt.figure(figsize=(14,7))
plt.plot(sol_price_df["timestamp"], sol_price_df["close"], label="SOL Close Price")

# Mark the BARRON Scam event on 21 January 2025
scam_date = datetime(2025, 1, 21)
plt.axvline(scam_date, color='red', linestyle='--', label='BARRON Scam Event (21 Jan 2025)')

plt.title("SOL Price Chart - January 2025")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save output
plt.savefig("output/sol_price_chart_jan2025_updated.png")
print("[+] Saved updated SOL price chart to output/sol_price_chart_jan2025_updated.png")
