import pandas as pd

class DataFrameTransform:
    def __init__(self, df):
        self.df = df

    def missing_values_percentage(self):
        missing_percentage = (self.df.isnull().sum() / len(self.df)) * 100
        return missing_percentage

    def drop_columns_with_missing_values(self, threshold=20):
        missing_percentage = self.missing_values_percentage()
        columns_to_drop = missing_percentage[missing_percentage > threshold].index.tolist()
        self.df.drop(columns_to_drop, axis=1, inplace=True)
        return self.df
