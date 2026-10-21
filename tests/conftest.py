"""Pytest hooks shared across the RUL test suite."""

# LightGBM must initialize before pandas on some Windows builds (native AV otherwise).
from lightgbm import LGBMRegressor as _LGBMRegressor  # noqa: F401
