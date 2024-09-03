import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_sentiment_distribution(aligned_data):
    """
    Plot the distribution of sentiment scores using a histogram.

    Parameters:
    - aligned_data: DataFrame, the data containing a 'sentiment' column

    Returns:
    - None, displays the plot
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(aligned_data['sentiment'], bins=20, kde=True)
    plt.title('Distribution of Sentiment Scores')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.show()



# Plot sentiment distribution
# plot_sentiment_distribution(aligned_data_with_sentiment)
