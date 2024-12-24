import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose


class TimeSeriesEDA:

    def __init__(self):
        pass

    def run(self, **config):
        pass

    def plot_timeseries(self):
        pass

    def plot_acf_pacf(self):
        pass

    def plot_seasonal_decompostion(self):
        pass

    def identify_column_types(self, df):
        """_summary_

        Args:
            df (_type_): _description_

        Returns:
            _type_: _description_
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
