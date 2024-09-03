import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_heatmap(correlation_matrix):
    """
    Plot a correlation heatmap.

    Parameters:
    - correlation_matrix: DataFrame, the correlation matrix to be visualized

    Returns:
    - None, displays the heatmap
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Heatmap')
    plt.show()

# # Example usage:
# import numpy as np

# # Example correlation matrix
# data = {
#     'sentiment': [1.0, 0.3, -0.2],
#     'daily_return': [0.3, 1.0, -0.4],
#     'rolling_return': [-0.2, -0.4, 1.0]
# }

# correlation_matrix_example = pd.DataFrame(data, index=['sentiment', 'daily_return', 'rolling_return'])

# # Plot correlation heatmap
# plot_correlation_heatmap(correlation_matrix_example)
