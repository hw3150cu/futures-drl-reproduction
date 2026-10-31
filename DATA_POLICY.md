# Data Policy

**No vendor market data is redistributed by this repository.**

The paper reproduction runs on 50 continuous futures contracts from **CLCData / Pinnacle Data**
(ratio-adjusted continuous contracts). That feed is licensed to the original authors of this project
and cannot be republished. What this repository *does* contain is the complete pipeline: loaders,
indicators, models, training code, evaluation code, and the aggregate results and figures those
produce.

## Rebuilding what is not committed

Two series used by the exploratory regime work are generated rather than shipped, because they are
third-party market and reference-rate data:

```bash
pip install yfinance pandas
export FRED_API_KEY=...            # optional, free: https://fred.stlouisfed.org/docs/api/api_key.html
python make_market_data.py --out data
```

This writes:

| File | Contents | Source |
|---|---|---|
| `data/index_data.csv` | `Date, SP500, VIX, SPY_ETF` daily closes | Yahoo Finance (`^GSPC`, `^VIX`, `SPY`) |
| `data/risk_free_rate.csv` | `Date, RiskFreeRate` daily fraction | FRED `DTB3`, or `^IRX` via Yahoo when no key is set |

Neither file is imported at module level anywhere in the codebase.

## The futures data you need

Place per-contract RAD CSVs under `data/CLC/`:

```
data/CLC/
├── <TICKER>_RAD.CSV      # one file per continuous contract
└── ...
```

Contract ordering comes from the vendor manual and is documented in `config.py` (`PAPER_50`) and
`data/README.md`. Roll dates can be extracted from the companion `.ASC` files under `config/TEMP/`,
which are also not shipped.

```bash
python verify_setup.py     # checks that everything is in place
python baseline_run.py --table 3 --all-metrics
```

## What is deliberately absent, and why

| Absent | Reason |
|---|---|
| `data/CLC/` RAD contract files | Licensed vendor data |
| `config/TEMP/` `.ASC` roll files | Licensed vendor data |
| `data/futures/`, `data/futures_processed/` | Licensed vendor data |
| `data/index_data.csv`, `data/risk_free_rate.csv` | Third-party series; regenerate with `make_market_data.py` |

The full path-by-path list is in [`EXCLUSIONS.md`](EXCLUSIONS.md).

## What *is* committed, and why that is fine

- **Positions and returns** (`drl_models/dqn/reports/**/positions.csv`): these are *our strategy's*
  holdings and daily returns, i.e. backtest output, not market prices.
- **Aggregate result tables** across `reproduction_of_figures/baseline_results/` and
  `drl_models/**/*_results_wide.csv`: performance summaries by asset class.
- **Figures**: our own renders of our own results.

None of these reproduce a vendor price series. If you believe something here crosses that line, please
open an issue and it will be removed promptly.