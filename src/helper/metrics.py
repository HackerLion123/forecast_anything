import numpy as np


def rmsle(y_true, y_pred):
    """
    Calculate the Root Mean Squared Logarithmic Error (RMSLE)
    Args:
        y_true (array-like): True values
        y_pred (array-like): Predicted values
    Returns:
        float: RMSLE value
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    log_true = np.log1p(y_true)
    log_pred = np.log1p(y_pred)
    squared_log_error = np.square(log_true - log_pred)
    mean_squared_log_error = np.mean(squared_log_error)
    rmsle_value = np.sqrt(mean_squared_log_error)

    print("RMSLE:", rmsle_value)
    return rmsle_value


def wape(y_true, y_pred):
    """
    Calculate the Weighted Absolute Percentage Error (WAPE)
    Args:
        y_true (array-like): True values
        y_pred (array-like): Predicted values
    Returns:
        float: WAPE value
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    absolute_error = np.abs(y_true - y_pred)
    wape_value = np.sum(absolute_error) / np.sum(np.abs(y_true))

    print("WAPE:", wape_value)
    return wape_value


def rmsse(y_true, y_pred, seasonality=1):
    """
    Calculate the Root Mean Squared Scaled Error (RMSSE)
    Args:
        y_true (array-like): True values
        y_pred (array-like): Predicted values
        seasonality (int): Seasonality period for the time series data (e.g., 1 for no seasonality, 12 for monthly data if annual seasonality)
    Returns:
        float: RMSSE value
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    n = len(y_true)
    num = np.sqrt(np.mean((y_true - y_pred) ** 2))
    denom = np.sqrt(np.mean(np.diff(y_true, n=seasonality) ** 2))
    rmsse_value = num / denom

    print("RMSSE:", rmsse_value)
    return rmsse_value
