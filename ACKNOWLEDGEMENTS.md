# Acknowledgements

## Contributors

This is joint work. It was produced by three people for **IEOR 4733** (Columbia University) and is
published here in cleaned form with all contributions retained.

| Contributor | Scope |
|---|---|
| **Hao Wang** ([@hw3150cu](https://github.com/hw3150cu)) | Reproduction harness, data loader, indicators, metrics, strategies, volume scaling, baseline runner, research reports and audits, A2C data branch |
| **[@ly2700](https://github.com/ly2700)** | DQN ensemble: models, training loops, report generation, figures |
| **[@arabbit20131208](https://github.com/arabbit20131208)** | Regime-detection branch and supporting analysis |

Copyright in the combined work is held collectively by the contributors; the `LICENSE` reflects that
rather than asserting sole authorship. If you are a contributor and want a change to how this is
published, please open an issue.

## Paper being reproduced

Zhang, Zohren and Roberts (2019), *Deep Reinforcement Learning for Trading*,
[arXiv:1911.10107](https://arxiv.org/abs/1911.10107).

This repository is an independent reproduction with an added A2C regime-detection branch and a
Streamlit dashboard. It is not affiliated with the authors of the paper.

## Third-party material

- **No vendor futures data is redistributed.** The CLCData series used for the backtests is licensed
  and is excluded; see [`DATA_POLICY.md`](DATA_POLICY.md) and `data/README.md`.
- **Index and risk-free series are not committed.** They are rebuilt from public sources by
  `make_market_data.py`.
- Figures exporting results of the reproduced paper are our own renders, not scanned material.