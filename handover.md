# handover.md

**Last updated:** 2026-10-18

Monday slice: RUL target, daily label builder, and leave-one-failure-out baselines. Remote: [grid-gnn-faults-2](https://github.com/mehmetertac/grid-gnn-faults-2). Upstream twin: [wind-digital-twin](https://github.com/mehmetertac/wind-digital-twin).

---

## What is done

| Item | Status |
|------|--------|
| Git remote `origin` → grid-gnn-faults-2 | Done |
| [docs/RUL_DESIGN.md](docs/RUL_DESIGN.md) — 90-day C-MAPSS cap, 4 events, LOFO | Done |
| [docs/WEEK_11_TODO.md](docs/WEEK_11_TODO.md) — Monday items checked | Done |
| [src/rul/labels.py](src/rul/labels.py) — daily aggregates + capped labels | Done |
| [src/rul/evaluate.py](src/rul/evaluate.py) — constant/linear baselines, LOFO metrics | Done |
| [tests/](tests/) — labels, evaluate, file-size smoke | Done |
| Pre-commit: file size + pytest | Done |
| Quantile model, conformal, SHAP, GNN notebook | Not started |

### Test run (2026-10-18)

`pytest tests/ -q` — 15 passed. `python scripts/check_file_size.py` — OK.

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
│   └── evaluate.py
├── scripts/check_file_size.py
└── tests/
    ├── fixtures/
    ├── test_labels.py
    ├── test_evaluate.py
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

Feature list: `DAILY_FEATURE_COLUMNS` in labels.py. Catalog: `CATALOGUED_GEARBOX_EVENTS` (4 lines, 3 turbines).

---

## Suggested next step

**Tuesday:** add `src/rul/quantile.py` and score q10/q50/q90 on the same LOFO split — no second evaluation protocol. Export a fleet scored CSV from wind-digital-twin without refitting the thermal stack.

---

## Key commit

Pending push — Monday RUL labels + LOFO baselines.
