# handover.md

**Last updated:** 2026-10-26

Thursday slice (partial): TreeSHAP on P10/P50 LOFO quantile RUL, sensor-level ranking CSV, global/local SHAP figures. Remote: [grid-gnn-faults-2](https://github.com/mehmetertac/grid-gnn-faults-2). Upstream twin: [wind-digital-twin](https://github.com/mehmetertac/wind-digital-twin).

---

## What is done

| Item | Status |
|------|--------|
| Git remote `origin` → grid-gnn-faults-2 | Done |
| [docs/RUL_DESIGN.md](docs/RUL_DESIGN.md) — quantile + conformal CQR, coverage caveat, P10 warning table, TreeSHAP section | Done |
| [docs/WEEK_11_TODO.md](docs/WEEK_11_TODO.md) — Monday–Wednesday RUL + SHAP checked | Done |
| [docs/EXPLANATIONS.md](docs/EXPLANATIONS.md) — sensor map, outputs, field-intuition template | Done |
| [src/rul/labels.py](src/rul/labels.py) — daily aggregates + capped labels | Done |
| [src/rul/evaluate.py](src/rul/evaluate.py) — constant/linear baselines, LOFO metrics | Done |
| [src/rul/quantile.py](src/rul/quantile.py) — LightGBM q10/q50/q90, PDP, bundle save/load | Done |
| [src/rul/conformal.py](src/rul/conformal.py) — MAPIE CQR 80%/90%, LOFO calibration split | Done |
| [src/rul/plots.py](src/rul/plots.py) — RUL band overlays + four-panel twin timeline | Done |
| [src/rul/explain.py](src/rul/explain.py) — TreeSHAP global/local figures, sensor ranking CSV | Done |
| [scripts/evaluate_quantile_rul.py](scripts/evaluate_quantile_rul.py) — LOFO CLI + conformal reports | Done |
| [scripts/explain_rul.py](scripts/explain_rul.py) — SHAP CLI → `results/` | Done |
| [scripts/run_twin.py](scripts/run_twin.py) — SCADA → conformal RUL turbine-day CSV + timeline | Done |
| [tests/](tests/) — labels, evaluate, quantile, conformal, explain, file-size smoke | Done |
| Pre-commit: file size + pytest | Done |
| Twin deployment UI, GNN notebook | Not started |

### Test run (2026-10-26)

`pytest tests/ -q` — 34 passed. `python scripts/check_file_size.py` — OK.

---

## Repo layout

```
grid-gnn-faults-2/
├── handover.md
├── AGENT.md
├── docs/
│   ├── RUL_DESIGN.md
│   ├── EXPLANATIONS.md
│   └── WEEK_11_TODO.md
├── src/rul/
│   ├── labels.py
│   ├── evaluate.py
│   ├── quantile.py
│   ├── conformal.py
│   ├── plots.py
│   └── explain.py
├── scripts/
│   ├── check_file_size.py
│   ├── evaluate_quantile_rul.py
│   ├── explain_rul.py
│   └── run_twin.py
├── results/
│   ├── shap_sensor_ranking.csv
│   └── figures/
└── tests/
    ├── conftest.py
    ├── fixtures/
    ├── test_labels.py
    ├── test_evaluate.py
    ├── test_quantile.py
    ├── test_conformal.py
    ├── test_explain.py
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
| `save_quantile_bundle` / `load_quantile_bundle` | quantile.py | Persist fitted boosters for SHAP / deployment |
| `evaluate_conformal_rul` | [conformal.py](src/rul/conformal.py) | LOFO CQR coverage + width vs horizon |
| `predict_conformal_rul_for_frame` | conformal.py | Deployment CQR on a daily frame |
| `write_all_band_figures` | [plots.py](src/rul/plots.py) | Headline RUL band PNG per held-out event |
| `plot_headline_timeline` | plots.py | Four-panel twin timeline with RUL band |
| `run_explain` | [explain.py](src/rul/explain.py) | TreeSHAP figures + `shap_sensor_ranking.csv` |

Feature list: `DAILY_FEATURE_COLUMNS` in labels.py. Catalog: `CATALOGUED_GEARBOX_EVENTS` (4 lines, 3 turbines).

---

## Suggested next step

**Thursday (remaining):** Streamlit/FastAPI twin view, IEEE 39-bus GNN notebook. Re-run `scripts/explain_rul.py` on a fleet scored CSV from wind-digital-twin (T06 hold-out) and refresh the field-intuition paragraph in [docs/EXPLANATIONS.md](docs/EXPLANATIONS.md). Fill the P10 warning table in [docs/RUL_DESIGN.md](docs/RUL_DESIGN.md).

---

## Key commit

Pending — TreeSHAP explain module, bundle persistence, `results/shap_sensor_ranking.csv`, tests and docs.
