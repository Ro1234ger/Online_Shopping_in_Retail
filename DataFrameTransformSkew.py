import numpy as np

class DataFrameTransformSkew:
    def __init__(self, df):
        self.df = df

    def identify_skewed_columns(self, threshold=0.5):

        numeric_columns = self.df.select_dtypes(include=['float64', 'int64']).columns
        skewed_columns = []
        for column in numeric_columns:
            skewness = self.df[column].skew()
            if abs(skewness) > threshold:
                skewed_columns.append(column)
                print(f"Column '{column}' is skewed with skewness {skewness}.")
        return skewed_columns

    def log_transform(self, column):
        if self.is_numeric_column(column):
            self.df[column] = np.log1p(self.df[column])  # Using log1p to handle zero values
        return self.df

    def sqrt_transform(self, column):
        if self.is_numeric_column(column):
            self.df[column] = np.sqrt(self.df[column])
        return self.df
    
    def is_numeric_column(self, column):
        return np.issubdtype(self.df[column].dtype, np.number)