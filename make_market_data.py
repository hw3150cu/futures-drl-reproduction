#!/usr/bin/env python3
"""Rebuild the index and risk-free series used by this project.

These two files are deliberately **not** committed: they are third-party market
and reference-rate series, and redistributing them would require licences we do
not hold. This script fetches them from public sources so a reader can recreate
the exact inputs locally.

    pip install yfinance pandas
    export FRED_API_KEY=...        # free key: https://fred.stlouisfed.org/docs/api/api_key.html
    python make_market_data.py --out data

Outputs
-------
data/index_data.csv       Date, SP500, VIX, SPY_ETF   (daily)
data/risk_free_rate.csv   Date, RiskFreeRate          (daily, fraction)

If FRED_API_KEY is unset, the risk-free series falls back to the 3-month Treasury
bill via yfinance (``^IRX``), which is annualised in percent and is converted to a
daily fraction here.

Nothing in this repository imports these files at module level; they are inputs
for the exploratory regime work. The reproduction of the paper's tables needs the
vendor futures data described in ``data/README.md``.
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

START, END = "2010-01-01", "2020-01-01"


def fetch_index(out: Path) -> None:
    import pandas as pd
    import yfinance as yf

    tickers = {"SP500": "^GSPC", "VIX": "^VIX", "SPY_ETF": "SPY"}
    frames = {}
    for name, sym in tickers.items():
        df = yf.download(sym, start=START, end=END, progress=False, auto_adjust=False)
        if df.empty:
            print(f"  warning: no data for {sym}", file=sys.stderr)
            continue
        close = df["Close"]
        if hasattr(close, "columns"):  # yfinance sometimes returns a frame
            close = close.iloc[:, 0]
        frames[name] = close.rename(name)
    if not frames:
        raise SystemExit("index download failed for every ticker")
    idx = pd.concat(frames.values(), axis=1)
    idx.index.name = "Date"
    dest = out / "index_data.csv"
    idx.to_csv(dest)
    print(f"  wrote {dest}  ({len(idx)} rows)")


def fetch_risk_free(out: Path) -> None:
    import pandas as pd

    key = os.environ.get("FRED_API_KEY")
    if key:
        from pandas_datareader import data as web

        s = web.DataReader("DTB3", "fred", START, END, api_key=key)["DTB3"]
        s = s.dropna()
        daily = (s / 100.0 / 252.0).rename("RiskFreeRate")  # percent p.a. -> daily fraction
        print("  source: FRED DTB3 (3-Month Treasury Bill, secondary market)")
    else:
        import yfinance as yf

        s = yf.download("^IRX", start=START, end=END, progress=False, auto_adjust=False)["Close"]
        if hasattr(s, "columns"):
            s = s.iloc[:, 0]
        daily = (s.dropna() / 100.0 / 252.0).rename("RiskFreeRate")
        print("  source: yfinance ^IRX (FRED_API_KEY unset)", file=sys.stderr)

    daily.index.name = "Date"
    dest = out / "risk_free_rate.csv"
    daily.to_csv(dest)
    print(f"  wrote {dest}  ({len(daily)} rows)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="data", help="output directory (default: data)")
    ap.add_argument("--skip-index", action="store_true")
    ap.add_argument("--skip-risk-free", action="store_true")
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    if not args.skip_index:
        print("index series:")
        fetch_index(out)
    if not args.skip_risk_free:
        print("risk-free series:")
        fetch_risk_free(out)
    print("done - these files stay out of git; see .gitignore")
    return 0


if __name__ == "__main__":
    sys.exit(main())