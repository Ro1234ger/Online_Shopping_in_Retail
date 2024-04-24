class DataFrameInfo:
    def __init__(self, df):
        self.df = df

    def describe_columns(self):
        return self.df.info()

    def extract_statistics(self):
        return self.df.describe()

    def count_distinct_values(self):
        categorical_columns = self.df.select_dtypes(include=['object', 'category']).columns
        distinct_values = {}
        for column in categorical_columns:
            distinct_values[column] = len(self.df[column].unique())
        return distinct_values

    def print_shape(self):
        return self.df.shape

    def generate_value_counts(self):
        value_counts = {}
        for column in self.df.columns:
            value_counts[column] = self.df[column].value_counts()
            value_counts[column + '_percentage'] = (self.df[column].value_counts(normalize=True) * 100).round(2)
        return value_counts
