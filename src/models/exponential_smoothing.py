from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
from hyperopt import hp, fmin, tpe, Trials, STATUS_OK
import pandas as pd
import numpy as np
import warnings
import config

warnings.filterwarnings("ignore")


class ExponentialSmoothingModels:
    def __init__(self):
        self.models = {
            "simple_exp": SimpleExpSmoothing,
            "holt": Holt,
            "exp_smoothing": ExponentialSmoothing,
        }
        self.best_model = None
        self.best_params = None
        self.best_model_type = None

    def train(self, train, test, metric_fn=None):
        """
        Train and optimize Simple Exponential Smoothing, Holt's Linear Trend, and Exponential Smoothing models.

        Parameters:
        train (pd.Series): The time series data for training.
        test (pd.Series): The time series data for testing.
        metric_fn (function): The metric function for evaluation.
        """

        def objective(params):
            model_type = params["model_type"]
            model_class = self.models[model_type]
            model_params = params["model_params"]

            if model_type == "exp_smoothing":
                model = model_class(
                    train, seasonal="add", seasonal_periods=12, **model_params
                ).fit()
            else:
                model = model_class(train, **model_params).fit()

            predictions = model.fittedvalues
            metric = (
                metric_fn(train, predictions)
                if metric_fn
                else np.mean((train - predictions) ** 2)
            )
            return {
                "loss": metric,
                "status": STATUS_OK,
                "params": model_params,
                "model_type": model_type,
            }

        space = hp.choice(
            "model",
            [
                {
                    "model_type": "simple_exp",
                    "model_params": {
                        "smoothing_level": hp.uniform(
                            "simple_exp_smoothing_level", 0.1, 1.0
                        )
                    },
                },
                {
                    "model_type": "holt",
                    "model_params": {
                        "smoothing_level": hp.uniform("holt_smoothing_level", 0.1, 1.0),
                        "smoothing_slope": hp.uniform("holt_smoothing_slope", 0.1, 1.0),
                    },
                },
                {
                    "model_type": "exp_smoothing",
                    "model_params": {
                        "smoothing_level": hp.uniform("exp_smoothing_level", 0.1, 1.0),
                        "smoothing_slope": hp.uniform("exp_smoothing_slope", 0.1, 1.0),
                        "smoothing_seasonal": hp.uniform(
                            "exp_smoothing_seasonal", 0.1, 1.0
                        ),
                    },
                },
            ],
        )

        trials = Trials()
        best = fmin(
            fn=objective,
            space=space,
            algo=tpe.suggest,
            max_evals=config.NUM_TRAILS,
            trials=trials,
        )

        best_trial = min(trials.results, key=lambda x: x["loss"])
        self.best_params = best_trial["params"]
        self.best_model_type = best_trial["model_type"]

    def forecast(self, steps):
        return self.best_model.forecast(steps)


if __name__ == "__main__":
    pass
