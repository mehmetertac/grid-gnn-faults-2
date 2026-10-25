# handover.md

**Last updated:** 2026-10-23

Wednesday slice: MAPIE CQR on LightGBM quantile RUL, LOFO coverage tables, raw vs conformal band figures, end-to-end `run_twin.py` with conformal RUL timeline. Remote: [grid-gnn-faults-2](https://github.com/mehmetertac/grid-gnn-faults-2). Upstream twin: [wind-digital-twin](https://github.com/mehmetertac/wind-digital-twin).

---

## What is done

| Item | Status |
|------|--------|
| Git remote `origin` → grid-gnn-faults-2 | Done |
| [docs/RUL_DESIGN.md](docs/RUL_DESIGN.md) — quantile + conformal CQR, coverage caveat, P10 warning table | Done |
| [docs/WEEK_11_TODO.md](docs/WEEK_11_TODO.md) — Monday–Wednesday RUL checked | Done |
| [src/rul/labels.py](src/rul/labels.py) — daily aggregates + capped labels | Done |
| [src/rul/evaluate.py](src/rul/evaluate.py) — constant/linear baselines, LOFO metrics | Done |
| [src/rul/quantile.py](src/rul/quantile.py) — LightGBM q10/q50/q90, PDP, coverage vs 80% | Done |
| [src/rul/conformal.py](src/rul/conformal.py) — MAPIE CQR 80%/90%, LOFO calibration split | Done |
| [src/rul/plots.py](src/rul/plots.py) — RUL band overlays + four-panel twin timeline | Done |
| [scripts/evaluate_quantile_rul.py](scripts/evaluate_quantile_rul.py) — LOFO CLI + conformal reports | Done |
| [scripts/run_twin.py](scripts/run_twin.py) — SCADA → conformal RUL turbine-day CSV + timeline | Done |
| [tests/](tests/) — labels, evaluate, quantile, conformal, file-size smoke | Done |
| Pre-commit: file size + pytest | Done |
| SHAP, GNN notebook | Not started |

### Test run (2026-10-23)

`pytest tests/ -q` — 27 passed. `python scripts/check_file_size.py` — OK.

---

## Repo layout

```
grid-gnn-faults-2/
├── handover.md
├── AGENT.md
├── docs/
│   ├── RUL_DESIGN.md
│   └── WEEK_11_TODO.md
├── src/rul/
│   ├── labels.py
│   ├── evaluate.py
│   ├── quantile.py
│   ├── conformal.py
│   └── plots.py
├── scripts/
│   ├── check_file_size.py
│   ├── evaluate_quantile_rul.py
│   └── run_twin.py
└── tests/
    ├── conftest.py
    ├── fixtures/
    ├── test_labels.py
    ├── test_evaluate.py
    ├── test_quantile.py
    ├── test_conformal.py
    └── test_check_file_size.py
```

---

## Core module API

| Symbol | Module | Purpose |
|--------|--------|---------|
| `daily_from_scored_frame` | [labels.py](src/rul/labels.py) | 10-min twin output → turbine-day features |
| `attach_rul_labels` | labels.py | Join gearbox log; cap RUL; censor healthy rows |
| `summarize_events` | labels.py | Count events in a failure CSV |
| `leave_one_failure_out` | [evaluate.py](src/rul/evaluate.py) | One fold per gearbox event |
| `evaluate_baselines` | evaluate.py | Constant + linear anomaly on every fold |
| `evaluate_quantile_model` | [quantile.py](src/rul/quantile.py) | LOFO LightGBM quantiles + coverage detail |
| `evaluate_conformal_rul` | [conformal.py](src/rul/conformal.py) | LOFO CQR coverage + width vs horizon |
| `predict_conformal_rul_for_frame` | conformal.py | Deployment CQR on a daily frame |
| `write_all_band_figures` | [plots.py](src/rul/plots.py) | Headline RUL band PNG per held-out event |
| `plot_headline_timeline` | plots.py | Four-panel twin timeline with RUL band |

Feature list: `DAILY_FEATURE_COLUMNS` in labels.py. Catalog: `CATALOGUED_GEARBOX_EVENTS` (4 lines, 3 turbines).

---

## Suggested next step

**Thursday:** TreeSHAP on daily RUL features, Streamlit/FastAPI twin view, IEEE 39-bus GNN notebook. Export a fleet scored CSV from wind-digital-twin and fill the P10 warning table in [docs/RUL_DESIGN.md](docs/RUL_DESIGN.md).

---

## Key commit

`e96ea79` — MAPIE conformal RUL, twin `run_twin.py`, coverage reports, docs and tests.
