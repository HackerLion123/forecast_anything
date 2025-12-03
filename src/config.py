from pathlib import Path

# Random seed for reproducibility of experiments
SEED = 73


# Project directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "output"
MODEL_DIR = PROJECT_DIR / "model"
LOG_DIR = PROJECT_DIR / "logs"


# --- Unified Forecasting Configuration ---
FORECASTING_CONFIG = {
    "num_trails": 200,
    "target": "",
    "partition_dim": "",  # Dimension which defines the splits of dims
    "interval": "day",
    "eda": {
        "correlation_threshold": 0.8,
        "zero_threshold": 0.6, # Threshold to identify intermittent series
    },
    "feature_engineering": {
        "lags": [1, 7, 14],
        "rolling_windows": [7, 14, 28],
        "rolling_functions": ["mean", "std"],
        "date_features": ["dayofweek", "month", "year", "weekofyear"],
    },
    "models": {
        "general": {
            "models": ["arima", "exponential_smoothing", "lightgbm"],
            "metric": ["rmse", "mape"],
        },
        "intermittent": {
            # For series with many zero values.
            "models": ["croston", "adida"],
            "metric": ["mae", "mase"],
            "inference": ["point"],
        },
        "new_product": {
            # Cold start for newly launched products.
            "models": [],
        },
    },
}
