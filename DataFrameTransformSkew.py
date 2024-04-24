import numpy as np
from SkewPlotter import SkewPlotter

class DataFrameTransformSkew:
    def __init__(self, df):
        self.df = df
        self.skewed_columns = []

    def identify_skewed_columns(self, threshold=0.5):
        numeric_columns = self.df.select_dtypes(include=['float64', 'int64']).columns
        for column in numeric_columns:
            skewness = self.df[column].skew()
            if abs(skewness) > threshold:
                self.skewed_columns.append(column)

    def log_transform(self):
        for column in self.skewed_columns:
            self.df[column] = np.log1p(self.df[column])  # Using log1p to handle zero values

    def sqrt_transform(self):
        for column in self.skewed_columns:
            self.df[column] = np.sqrt(self.df[column])

    def visualize_skew(self, plotter=None):
        if plotter is None:
            plotter = SkewPlotter(self.df)
        plotter.plot_skew(self.skewed_columns)