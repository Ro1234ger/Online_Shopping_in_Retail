
class DataFrameTransformNull:
    def __init__(self, df):
        self.df = df

    def missing_values_percentage(self):
        missing_percentage = (self.df.isnull().sum() / len(self.df)) * 100
        return missing_percentage

    def drop_rows_with_high_null_proportion(self, threshold):
        """
        Drop rows with a high proportion of null values.
        """
        # Calculate the proportion of null values in each row
        row_null_proportion = self.df.isnull().mean(axis=1)

        # Drop rows where the proportion of null values exceeds the threshold
        self.df = self.df[row_null_proportion <= threshold]

        return self.df