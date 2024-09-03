import matplotlib.pyplot as plt

def plot_rolling_averages(final_data):
    """
    Plot the rolling averages of sentiment scores and stock returns over time.

    Parameters:
    - final_data: DataFrame, the data containing 'date', 'rolling_sentiment', and 'rolling_return' columns

    Returns:
    - None, displays the plot
    """
    plt.figure(figsize=(12, 8))
    plt.plot(final_data['date'], final_data['rolling_sentiment'], label='Rolling Average Sentiment Score', color='blue')
    plt.plot(final_data['date'], final_data['rolling_return'], label='Rolling Average Daily Return', color='red')
    plt.title('Rolling Averages of Sentiment Scores and Stock Returns')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()



# Plot rolling averages of sentiment scores and stock returns
# plot_rolling_averages(final_data_example)
