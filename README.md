# grid-gnn-faults-2

Week 11 capstone: probabilistic **gearbox remaining useful life** on the [wind-digital-twin](https://github.com/mehmetertac/wind-digital-twin) hybrid residual stack, plus a later **IEEE 39-bus GNN fault-localization** demo. Physics and anomaly detection stay in the twin; this repo adds daily RUL labels and evaluation.

Status and layout: [handover.md](handover.md). Agent rules: [AGENT.md](AGENT.md).

## Quickstart

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
pytest tests/ -q
python scripts/check_file_size.py
```

Optional hooks:

```powershell
pre-commit install
```

## RUL labels, baselines, and quantile model

Design contract: [docs/RUL_DESIGN.md](docs/RUL_DESIGN.md). Week checklist: [docs/WEEK_11_TODO.md](docs/WEEK_11_TODO.md).

From Python (after you have a 10-minute **scored** CSV from the twin — do not refit the ODE here):

```python
import pandas as pd
from rul.labels import daily_from_scored_frame, attach_rul_labels, summarize_events
from rul.evaluate import evaluate_baselines
from rul.quantile import evaluate_quantile_model

scored = pd.read_csv("path/to/scored_10min.csv")
failures = pd.read_csv("path/to/gearbox_log.csv")
print(summarize_events(failures))  # catalog expects 4 gearbox events

daily = daily_from_scored_frame(scored)
labeled = attach_rul_labels(daily, failures)
metrics = evaluate_baselines(labeled)
quantile_metrics, coverage, warnings, folds = evaluate_quantile_model(labeled)
```

Leave-one-failure-out quantile evaluation and headline band figures:

```powershell
python scripts/evaluate_quantile_rul.py --scored path/to/scored_10min.csv --failures path/to/gearbox_log.csv --out reports/rul
```

Required scored columns: `oil_residual`, `bear_residual`, `anomaly_score`, `theta_oil`, `theta_bear`, `delta_bear_oil`, `turbine_id`, `timestamp`.

## What this means for maintenance (O&M)

A capped RUL is an **inspection planning window**, not a guaranteed failure date. When daily hybrid residuals and the anomaly score trend toward the held-out failure pattern, operations can prioritize gearbox oil, bearing temperatures, and log review within the 90-day horizon Week 10 already uses as a training buffer. With **four** catalogued gearbox events in the EDP log, probabilistic bands and leave-one-failure-out scores describe what the twin can support on those run-to-failure windows — not fleet-wide calendar certainty.

## Roadmap (same repo)

| Track | Scope |
|-------|--------|
| **B — RUL** | Quantile LightGBM, conformal intervals, SHAP, twin API (Tue–Thu) |
| **C — Grid** | One notebook: torch-geometric + pandapower fault localization on IEEE 39-bus |

## License

Apache-2.0 — see [LICENSE](LICENSE).
