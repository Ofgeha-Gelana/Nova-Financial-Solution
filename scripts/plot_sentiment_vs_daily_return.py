import matplotlib.pyplot as plt
import seaborn as sns

def plot_sentiment_vs_daily_return(final_data):
    """
    Plot the correlation between sentiment scores and daily returns.

    Parameters:
    - final_data: DataFrame, the data containing 'sentiment' and 'daily_return' columns

    Returns:
    - None, displays the plot
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='sentiment', y='daily_return', data=final_data)
    plt.title('Correlation Between Sentiment Scores and Daily Returns')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Daily Return')
    plt.grid(True)
    plt.show()


# Plot correlation between sentiment scores and daily returns
# plot_sentiment_vs_daily_return(final_data_example)
