import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose


class TimeSeriesEDA:

    def __init__(self):
        pass

    def run(self, **config):
        """Run the EDA process based on the provided configuration."""
        pass

    def monthly_seasonality(self):
        pass

    def day_of_week_seasonality(self):
        pass

    def plot_timeseries(self, data, column):
        """Plot the time series data.

        Args:
            data (pd.DataFrame): DataFrame containing the time series data.
            column (str): Column name of the time series to plot.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(data["ds"], data[column])
        plt.title(f"Time Series of {column}")
        plt.xlabel("Date")
        plt.ylabel(column)
        plt.grid(True)
        plt.show()

    def plot_acf_pacf(self, data, column, lags=20):
        """Plot the ACF and PACF.

        Args:
            data (pd.DataFrame): DataFrame containing the time series data.
            column (str): Column name of the time series.
            lags (int): Number of lags to display.
        """
        plt.figure(figsize=(12, 6))
        plt.subplot(121)
        plot_acf(data[column], lags=lags, ax=plt.gca())
        plt.subplot(122)
        plot_pacf(data[column], lags=lags, ax=plt.gca())
        plt.tight_layout()
        plt.show()

    def plot_seasonal_decomposition(self, data, column, model="additive", period=12):
        """Plot seasonal decomposition of the time series data.

        Args:
            data (pd.DataFrame): DataFrame containing the time series data.
            column (str): Column name of the time series.
            model (str): Type of seasonal decomposition ('additive' or 'multiplicative').
            period (int): Number of periods in one season.
        """
        decomposition = seasonal_decompose(data[column], model=model, period=period)
        decomposition.plot()
        plt.show()

    def causal_analysis(self, data, target_column, feature_columns):
        """Plot causal analysis between target and feature columns.

        Args:
            data (pd.DataFrame): DataFrame containing the time series data.
            target_column (str): Column name of the target variable.
            feature_columns (list): List of column names of the feature variables.
        """
        for feature in feature_columns:
            plt.figure(figsize=(10, 6))
            plt.scatter(data[feature], data[target_column])
            plt.title(f"{feature} vs {target_column}")
            plt.xlabel(feature)
            plt.ylabel(target_column)
            plt.grid(True)
            plt.show()

    def grangers_test(self, data, columns):
        pass

    def check_intmediant(self):
        """
        Check if given time series is intermediant.
        """
        pass

    def check_new_product(self):
        pass

    def identify_seasonal_length(self):
        pass

    def pair_plot(self, data, columns):
        """Plot pair plot for the given columns.

        Args:
            data (pd.DataFrame): DataFrame containing the time series data.
            columns (list): List of column names to include in the pair plot.
        """
        sns.pairplot(data[columns])
        plt.show()

    def identify_column_types(self, df):
        """Identify column types in the DataFrame.

        Args:
            df (pd.DataFrame): DataFrame to identify column types.

        Returns:
            dict: Dictionary with lists of categorical, numerical, and datetime columns.
        """
        categorical_columns = []
        numerical_columns = []
        datetime_columns = []

        for column in df.columns:
            if (
                pd.api.types.is_categorical_dtype(df[column])
                or df[column].dtype == object
            ):
                categorical_columns.append(column)
            elif pd.api.types.is_numeric_dtype(df[column]):
                numerical_columns.append(column)
            elif pd.api.types.is_datetime64_any_dtype(df[column]):
                datetime_columns.append(column)

        return {
            "categorical": categorical_columns,
            "numerical": numerical_columns,
            "datetime": datetime_columns,
        }
