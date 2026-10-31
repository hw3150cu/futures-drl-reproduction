# Data Directory

Market data required to reproduce the backtests. Due to licensing restrictions, **vendor data is not included** in this repository.

## Required Data Sources

### CLCData (Primary — Required)

- **Source**: [Pinnacle Data / CLC](https://pinnacledata2.com/clc.html) — Continuous Linked Contracts (CLC) futures data
- **Format**: Per-contract RAD (Ratio-Adjusted) CSV files — one file per ticker (e.g., `ES_RAD.CSV`)
- **Location**: Place files under `data/CLC/`
- **Contracts**: 50 futures contracts across 4 asset classes (Commodity, Equity Index, Fixed Income, Forex). See `config.py` → `PAPER_50` for the full list.
- **Date range**: 2009-01-01 through 2019-12-31 (2011-01-01 through 2019-12-31 for backtesting)

### Yahoo Finance (Supplementary — Optional)

Used as fallback for a small number of equity-index contracts. Place under `data/yahoo/`. You can download these yourself using the `yfinance` Python package:

```bash
pip install yfinance
python -c "import yfinance as yf; yf.download('ES=F', start='2009-01-01', end='2019-12-31').to_csv('data/yahoo/ES_yahoo.csv')"
```

### Generated Files (Not in Repo)

| File | Description |
|---|---|
| `data/index_data.csv` | Index-level daily prices (S&P 500, VIX, SPY) |
| `data/risk_free_rate.csv` | Daily risk-free rate series |

These are third-party market and reference-rate series, so they are **not committed** — redistributing
them would need licences this project does not hold. Rebuild them from public sources:

```bash
pip install yfinance pandas
export FRED_API_KEY=...            # optional; free key from https://fred.stlouisfed.org
python make_market_data.py --out data
```

The script fetches `^GSPC`, `^VIX`, `SPY` from Yahoo Finance and the 3-month bill series from FRED
(falling back to `^IRX` when no key is set). No code in this repository imports these files at module
level; they feed the exploratory regime work.

### config/TEMP/

CLCData `.ASC` files used for roll-date extraction. These are **not** included due to licensing. Contact CLCData for access.

## Quick Setup

```bash
# 1. Obtain CLCData and place files
mkdir -p data/CLC
cp /path/to/clcdata/*_RAD.CSV data/CLC/

# 2. Verify everything is in place
python verify_setup.py

# 3. Run baseline backtests
python baseline_run.py --table 3 --all-metrics
```
