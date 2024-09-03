import pandas as pd

def calculate_daily_sentiment_and_merge(aligned_data):
    """
    Calculate the daily mean sentiment score and merge it with daily returns.

    Parameters:
    - aligned_data: DataFrame, the data containing 'date', 'sentiment', and 'daily_return' columns

    Returns:
    - final_data: DataFrame, the final dataset with 'date', 'sentiment', and 'daily_return' columns
    """
    # Group by date and calculate the mean sentiment score
    daily_sentiment = aligned_data.groupby('date')['sentiment'].mean().reset_index()

    # Merge with daily returns
    final_data = pd.merge(daily_sentiment, aligned_data[['date', 'daily_return']], on='date')

    return final_data

# # Example usage:
# aligned_data_with_sentiment_and_returns = pd.DataFrame({
#     'date': ['2024-08-26', '2024-08-26', '2024-08-27', '2024-08-28', '2024-08-28'],
#     'sentiment': [0.5, -0.2, 0.1, 0.3, -0.1],
#     'daily_return': [0.0083, 0.0083, 0.0099, -0.0163, -0.0163]
# })

# Calculate daily sentiment and merge with returns
# final_data = calculate_daily_sentiment_and_merge(aligned_data_with_sentiment_and_returns)

# Display the final dataset
# print(final_data.head())
