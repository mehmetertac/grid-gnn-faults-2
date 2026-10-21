# handover.md

**Last updated:** 2026-10-21

Tuesday slice: LightGBM quantile RUL (q10/q50/q90) on Monday features, LOFO scoring, band figures, P10 warning lead time. Remote: [grid-gnn-faults-2](https://github.com/mehmetertac/grid-gnn-faults-2). Upstream twin: [wind-digital-twin](https://github.com/mehmetertac/wind-digital-twin).

---

## What is done

| Item | Status |
|------|--------|
| Git remote `origin` → grid-gnn-faults-2 | Done |
| [docs/RUL_DESIGN.md](docs/RUL_DESIGN.md) — 90-day cap, quantile model, P10 warning table | Done |
| [docs/WEEK_11_TODO.md](docs/WEEK_11_TODO.md) — Monday + Tuesday quantile checked | Done |
| [src/rul/labels.py](src/rul/labels.py) — daily aggregates + capped labels | Done |
| [src/rul/evaluate.py](src/rul/evaluate.py) — constant/linear baselines, LOFO metrics | Done |
| [src/rul/quantile.py](src/rul/quantile.py) — LightGBM q10/q50/q90, PDP, coverage vs 80% | Done |
| [src/rul/plots.py](src/rul/plots.py) — true RUL vs P50 + P10–P90 band PNGs | Done |
| [scripts/evaluate_quantile_rul.py](scripts/evaluate_quantile_rul.py) — LOFO CLI + reports | Done |
| [tests/](tests/) — labels, evaluate, quantile, file-size smoke | Done |
| Pre-commit: file size + pytest | Done |
| Conformal (MAPIE), SHAP, GNN notebook | Not started |

### Test run (2026-10-21)

`pytest tests/ -q` — 22 passed. `python scripts/check_file_size.py` — OK.

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
│   └── plots.py
├── scripts/
│   ├── check_file_size.py
│   └── evaluate_quantile_rul.py
└── tests/
    ├── conftest.py
    ├── fixtures/
    ├── test_labels.py
    ├── test_evaluate.py
    ├── test_quantile.py
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
| `write_all_band_figures` | [plots.py](src/rul/plots.py) | Headline RUL band PNG per held-out event |

Feature list: `DAILY_FEATURE_COLUMNS` in labels.py. Catalog: `CATALOGUED_GEARBOX_EVENTS` (4 lines, 3 turbines).

---

## Suggested next step

**Wednesday:** add MAPIE conformal intervals on the same LOFO split (CQR on q10/q50/q90). Export a fleet scored CSV from wind-digital-twin and fill the P10 warning table in [docs/RUL_DESIGN.md](docs/RUL_DESIGN.md).

---

## Key commit

`b47445a` — LightGBM quantile RUL, LOFO CLI, band figures, docs and tests.
