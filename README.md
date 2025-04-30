# Solana $BARRON Scam Event Analysis

This repository analyzes the $BARRON scam token incident on Solana in January 2025 using Messari API + Helius API.

# Context
In January 2025, a fake meme token "$BARRON" was launched via Pump.fun and promoted by a misleading viral X (Twitter) account posing as Barron Trump. It pumped to $73M market cap and rugpulled 99% within minutes.

This repo uses Messari’s free API for Solana asset price history and metrics, and Helius API to trace wallet activity.

# Features
- Analyze SOL price trend in January 2025 (analyze_sol_price_chart.py)
- Fetch token metrics from Messari API (fetch_solana_asset_metrics.py)
- Trace inflow patterns to scam-linked wallet via Helius (analyze_wallet_helius.py)
- Summarize and visualize fund inflows (parse_inflow_summary_native.py, visualize_inflow_senders.py)


# Folder Structure

```
solana-barron-analysis/
├── analyze_sol_price_chart.py
├── fetch_solana_asset_metrics.py
├── analyze_wallet_helius.py
├── parse_inflow_summary_native.py
├── visualize_inflow_senders.py
├── output/
│   ├── sol_price_jan2025.json
│   ├── helius_BiN2V_inflow_native_summary.json
│   └── ...
├── README.md
├── requirements.txt
```

# How to Run
```
# Clone repo
git clone https://github.com/zkreum/solana-barron-analysis.git
cd solana-barron-analysis

# Install dependencies
pip install -r requirements.txt

# Fetch data and analyze
python fetch_solana_asset_metrics.py
python analyze_sol_price_chart.py
python analyze_wallet_helius.py
python parse_inflow_summary_native.py
python visualize_inflow_senders.py
```

# APIs Used
- Messari Asset Metrics API : https://docs.messari.io
- Helius Enhanced Solana API : https://helius.dev
