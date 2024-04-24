import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot
from matplotlib import pyplot as plt

class SkewPlotter:
    def __init__(self, data):
        self.data = data

    def plot_skew(self, columns, transformed_data=None):
        data_to_plot = transformed_data if transformed_data is not None else self.data
        for column in columns:
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
            
            # Histogram
            ax1.hist(data_to_plot[column], bins=30, alpha=0.5)
            ax1.set_title(f'{column} - Skewness: {data_to_plot[column].skew()}')
            ax1.set_xlabel(column)
            ax1.set_ylabel('Frequency')
            
            # QQ Plot
            qq_plot = qqplot(data_to_plot[column], line='q', fit=True, ax=ax2)
            ax2.set_title(f'QQ Plot for {column}')
            plt.show()









