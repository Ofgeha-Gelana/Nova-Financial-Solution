import matplotlib.pyplot as plt

def plot_time_series(daily_sentiment, daily_returns, date_column='date', sentiment_column='sentiment_score', return_column='daily_return'):
    """
    Plot time series of daily sentiment scores and daily stock returns.

    Parameters:
    daily_sentiment (pd.DataFrame): DataFrame containing average daily sentiment scores.
    daily_returns (pd.Series): Series containing daily stock returns.
    date_column (str): The name of the date column.
    sentiment_column (str): The name of the sentiment score column.
    return_column (str): The name of the daily return column.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(daily_sentiment[date_column], daily_sentiment[sentiment_column], label='Daily Sentiment Score')
    plt.plot(daily_sentiment[date_column], daily_returns, label='Daily Stock Return', alpha=0.7)
    plt.title('Time Series of Daily Sentiment Scores and Stock Returns')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_scatter_sentiment_vs_returns(daily_sentiment, daily_returns, sentiment_column='sentiment_score', return_column='daily_return'):
    """
    Plot scatter plot of sentiment scores vs stock returns.

    Parameters:
    daily_sentiment (pd.DataFrame): DataFrame containing average daily sentiment scores.
    daily_returns (pd.Series): Series containing daily stock returns.
    sentiment_column (str): The name of the sentiment score column.
    return_column (str): The name of the daily return column.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(daily_sentiment[sentiment_column], daily_returns)
    plt.title('Scatter Plot of Sentiment Scores vs Stock Returns')
    plt.xlabel('Daily Sentiment Score')
    plt.ylabel('Daily Stock Return')
    plt.grid(True)
    plt.show()

def plot_distribution(data, column_name, title):
    """
    Plot a histogram of a specific column in the DataFrame.

    Parameters:
    data (pd.DataFrame): DataFrame containing the data.
    column_name (str): The name of the column to plot.
    title (str): The title of the plot.
    """
    plt.figure(figsize=(8, 6))
    plt.hist(data[column_name], bins=30, edgecolor='k', alpha=0.7)
    plt.title(title)
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def plot_rolling_average(daily_sentiment, window_size=7, date_column='date', sentiment_column='sentiment_score'):
    """
    Plot the rolling average of sentiment scores over a specified window.

    Parameters:
    daily_sentiment (pd.DataFrame): DataFrame containing average daily sentiment scores.
    window_size (int): The window size for calculating the rolling average.
    date_column (str): The name of the date column.
    sentiment_column (str): The name of the sentiment score column.
    """
    daily_sentiment['rolling_average'] = daily_sentiment[sentiment_column].rolling(window=window_size).mean()
    plt.figure(figsize=(14, 7))
    plt.plot(daily_sentiment[date_column], daily_sentiment['rolling_average'], label=f'{window_size}-Day Rolling Average')
    plt.title(f'{window_size}-Day Rolling Average of Sentiment Scores')
    plt.xlabel('Date')
    plt.ylabel('Rolling Average Sentiment Score')
    plt.legend()
    plt.grid(True)
    plt.show()
