import numpy as np
import pandas as pd
from SkewPlotter import SkewPlotter

class DataFrameTransformSkew:
    def __init__(self, df):
        self.df = df
        self.skewed_columns = []

    def identify_skewed_columns(self, threshold=0.5):
        numeric_columns = self.df.select_dtypes(include=['float64', 'int64']).columns
        skewed_columns = []
        for column in numeric_columns:
            # Ensure only numeric columns are considered
            try:
                skewness = self.df[column].skew()
                if abs(skewness) > threshold:
                    skewed_columns.append(column)
                    print(f"Column '{column}' is skewed with skewness {skewness}.")
            except Exception as e:
                print(f"Error computing skewness for column '{column}': {e}")
        return skewed_columns

    def is_numeric_column(self, column):
        return pd.api.types.is_numeric_dtype(self.df[column])

    def log_transform(self, df, column):
        if self.is_numeric_column(column):
            df[column] = np.log1p(df[column])  # Using log1p to handle zero values
        return df

    def sqrt_transform(self):
        for column in self.skewed_columns:
            self.df[column] = np.sqrt(self.df[column])

    def visualize_skew(self, plotter=None):
        if plotter is None:
            plotter = SkewPlotter(self.df)
        plotter.plot_skew(self.skewed_columns)