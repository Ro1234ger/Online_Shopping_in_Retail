import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class CorrelationManager:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input 'df' must be a DataFrame.")
        self.df = df

    def drop_highly_correlated_columns(self, threshold=0.7):
        # Check if df is a DataFrame
        if not isinstance(self.df, pd.DataFrame):
            raise ValueError("DataFrame 'df' is not initialized properly.")

        # Drop non-numeric columns
        numeric_df = self.df.select_dtypes(include=['float64', 'int64'])

        # Calculate correlation matrix
        corr_matrix = numeric_df.corr().abs()
        
        # Create a mask to identify highly correlated features
        upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool_))
        
        # Find columns to drop
        to_drop = [column for column in upper.columns if any(upper[column] > threshold)]
        
        # Drop highly correlated columns
        numeric_df.drop(to_drop, axis=1, inplace=True)
        
        return numeric_df, to_drop
    
    def visualize_correlation_matrix(self):
        # Check if df is a DataFrame
        if not isinstance(self.df, pd.DataFrame):
            raise ValueError("DataFrame 'df' is not initialized properly.")

        # Drop non-numeric columns
        numeric_df = self.df.select_dtypes(include=['float64', 'int64'])

        # Calculate correlation matrix
        corr_matrix = numeric_df.corr()

        # Create a heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
        plt.title("Correlation Matrix")
        plt.show()