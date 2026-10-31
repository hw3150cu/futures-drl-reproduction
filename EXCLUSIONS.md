# Exclusions - futures-drl-reproduction

This repository reproduces a published paper jointly with two co-authors; their work is included and
credited. Two categories are withheld: (1) third-party licensed market data, and (2) generated
artifacts that duplicate something already committed.

The index and risk-free series that were previously committed are replaced by `make_market_data.py`,
which rebuilds them from public sources (Yahoo Finance and FRED) under the user's own credentials.
No vendor futures data is redistributed.

---

**2 paths are deliberately not published.** Grouped by reason; every
path is listed so the boundary is auditable rather than implied.

| Reason | Files |
|---|---:|
| Third-party licensed index data: 7,045 daily S&P 500 / VIX / SPY closes (replaced by make_market_data.py) | 1 |
| Third-party risk-free series with a documented fetch key (replaced by make_market_data.py) | 1 |

## Third-party licensed index data: 7,045 daily S&P 500 / VIX / SPY closes (replaced by make_market_data.py)

1 file(s).

<details><summary>Show paths</summary>

```text
data/index_data.csv
```

</details>

## Third-party risk-free series with a documented fetch key (replaced by make_market_data.py)

1 file(s).

<details><summary>Show paths</summary>

```text
data/risk_free_rate.csv
```

</details>

