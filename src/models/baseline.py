import numpy as np


class BaselineForecaster:
    """
    A collection of baseline forecasting methods for benchmarking
    """
    
    def __init__(self, method='naive', seasonality=1):
        """
        Initialize the baseline forecaster
        Args:
            method (str): Forecasting method ('naive', 'seasonal_naive', 'mean', 'drift')
            seasonality (int): Seasonality period (only used for seasonal_naive method)
        """
        self.method = method
        self.seasonality = seasonality
        self.y_train = None
        
    def fit(self, y_train):
        """
        Fit the baseline model
        Args:
            y_train (array-like): Training data
        """
        self.y_train = np.array(y_train)
        return self
    
    def forecast(self, horizon):
        """
        Generate forecasts
        Args:
            horizon (int): Number of periods to forecast
        Returns:
            array: Forecast values
        """
        if self.y_train is None:
            raise ValueError("Model must be fitted before prediction. Call fit() first.")
        
        if self.method == 'naive':
            return self._naive_forecast(horizon)
        elif self.method == 'seasonal_naive':
            return self._seasonal_naive_forecast(horizon)
        elif self.method == 'mean':
            return self._mean_forecast(horizon)
        elif self.method == 'drift':
            return self._drift_forecast(horizon)
        else:
            raise ValueError(f"Unknown method: {self.method}")
    
    def _naive_forecast(self, horizon):
        """Naive forecast: last observed value"""
        return np.full(horizon, self.y_train[-1])
    
    def _seasonal_naive_forecast(self, horizon):
        """Seasonal naive forecast: values from same season in previous cycle"""
        forecast = np.array([self.y_train[-(self.seasonality - i % self.seasonality)] 
                           for i in range(horizon)])
        return forecast
    
    def _mean_forecast(self, horizon):
        """Mean forecast: historical mean"""
        return np.full(horizon, np.mean(self.y_train))
    
    def _drift_forecast(self, horizon):
        """Drift forecast: linear extrapolation"""
        n = len(self.y_train)
        drift = (self.y_train[-1] - self.y_train[0]) / (n - 1)
        forecast = np.array([self.y_train[-1] + drift * i for i in range(1, horizon + 1)])
        return forecast