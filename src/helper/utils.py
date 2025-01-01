import pandas as pd
import numpy as np


from hyperopt import hp, fmin, tpe, Trials, STATUS_OK

import config


def reduce_mem_usage(df, verbose=True):
    """_summary_

    Args:
        df (_type_): _description_
        verbose (bool, optional): _description_. Defaults to True.

    Returns:
        _type_: _description_
    """
    numerics = ["int16", "int32", "int64", "float16", "float32", "float64"]
    start_mem = df.memory_usage().sum() / 1024**2
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == "int":
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if (
                    c_min > np.finfo(np.float16).min
                    and c_max < np.finfo(np.float16).max
                ):
                    df[col] = df[col].astype(np.float16)
                elif (
                    c_min > np.finfo(np.float32).min
                    and c_max < np.finfo(np.float32).max
                ):
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
    end_mem = df.memory_usage().sum() / 1024**2
    if verbose:
        print(
            "Mem. usage decreased to {:5.2f} Mb ({:.1f}% reduction)".format(
                end_mem, 100 * (start_mem - end_mem) / start_mem
            )
        )
    return df


def objective(params, metric_fn):
    """_summary_

    Args:
        params (_type_): _description_
        metric_fn (_type_): _description_

    Returns:
        _type_: _description_
    """
    model_class = params["model_class"]
    hyperparams = params["hyperparams"]
    model = model_class(**hyperparams)
    metric = metric_fn()
    return {"loss": metric, "status": STATUS_OK}


def optimize(model_class, hyperparams_space):
    """_summary_

    Args:
        model_class (_type_): _description_
        hyperparams_space (_type_): _description_

    Returns:
        _type_: _description_
    """
    space = {"model_class": model_class, "hyperparams": hyperparams_space}

    trials = Trials()
    best = fmin(
        fn=objective,
        space=space,
        algo=tpe.suggest,
        max_evals=config.NUM_TRAILS,
        trials=trials,
    )

    return best, trials
