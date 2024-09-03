import matplotlib.pyplot as plt

def plot_daily_returns_over_time(aligned_data):
    """
    Plot daily stock returns over time.

    Parameters:
    - aligned_data: DataFrame, the data containing 'date' and 'daily_return' columns

    Returns:
    - None, displays the plot
    """
    plt.figure(figsize=(10, 6))
    plt.plot(aligned_data['date'], aligned_data['daily_return'], marker='o', linestyle='-')
    plt.title('Daily Stock Returns Over Time')
    plt.xlabel('Date')
    plt.ylabel('Daily Return')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()



# Plot daily returns over time
# plot_daily_returns_over_time(aligned_data_with_returns)
