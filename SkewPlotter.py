import pandas as pd
import matplotlib.pyplot as plt

class SkewPlotter:
    def __init__(self, original_data, transformed_data, numeric_columns):
        # Convert original_data and transformed_data to DataFrame if they are lists
        if isinstance(original_data, list):
            original_data = pd.DataFrame(original_data)
        if isinstance(transformed_data, list):
            transformed_data = pd.DataFrame(transformed_data)

        # Extract column names from the first column of the DataFrame
        column_names = original_data.iloc[:, 0].tolist()

        # Remove the first column (containing column names) from the DataFrame
        self.original_data = original_data.iloc[:, 1:]
        
        # Ensure that the length of column_names matches the number of columns in the DataFrame
        if len(column_names) != self.original_data.shape[1]:
            raise ValueError("Length of column names does not match the number of columns in the DataFrame.")

        # Assign the extracted column names to the DataFrame
        self.original_data.columns = column_names
        
        # Similarly process transformed_data if necessary
        
        self.numeric_columns = numeric_columns

    def visualize_skewness(self):
        fig, axes = plt.subplots(nrows=len(self.numeric_columns), ncols=2, figsize=(12, 6 * len(self.numeric_columns)))

        for i, column in enumerate(self.numeric_columns):
            self.original_data[column].hist(bins=100, ax=axes[i, 0], color='blue', alpha=0.7)
            axes[i, 0].set_title(f'Original - {column}')
            axes[i, 0].set_ylabel('Frequency')

            self.transformed_data[column].hist(bins=100, ax=axes[i, 1], color='orange', alpha=0.7)
            axes[i, 1].set_title(f'Transformed - {column}')
            axes[i, 1].set_ylabel('Frequency')

        plt.tight_layout()
        plt.show()










