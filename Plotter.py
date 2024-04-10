import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, df):
        self.df = df

    def visualize_removal_of_values(self, original_df, transformed_df):
        original_missing_values = original_df.isnull().sum()
        transformed_missing_values = transformed_df.isnull().sum()

        plt.figure(figsize=(12, 6))
        plt.subplot(1, 2, 1)
        original_missing_values.plot(kind='bar', color='blue', alpha=0.7, label='Before Removal')
        for i, v in enumerate(original_missing_values):
            plt.text(i, v + 1, str(v), ha='center', va='bottom')
        plt.title('Missing Values Before Removal')
        plt.xlabel('Columns')
        plt.ylabel('Number of Missing Values')
        plt.xticks(rotation=45)
        plt.legend()

        plt.subplot(1, 2, 2)
        transformed_missing_values.plot(kind='bar', color='orange', alpha=0.7, label='After Removal')
        for i, v in enumerate(transformed_missing_values):
            plt.text(i, v + 1, str(v), ha='center', va='bottom')
        plt.title('Missing Values After Removal')
        plt.xlabel('Columns')
        plt.ylabel('Number of Missing Values')
        plt.xticks(rotation=45)
        plt.legend()

        plt.tight_layout()
        plt.show()
