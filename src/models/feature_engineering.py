import pandas as pd


class FeatureEngineering:

    def __init__(self):
        pass

    def make_lags(self, ts, lags, lead_time=1):
        return pd.concat(
            {f"y_lag_{i}": ts.shift(i) for i in range(lead_time, lags + lead_time)},
            axis=1,
        )

    def make_multistep_target(self, ts, steps):
        return pd.concat(
            {f"y_step_{i + 1}": ts.shift(-i) for i in range(steps)}, axis=1
        )
