import pandas as pd

def calculate_daily_returns(aligned_data):
    """
    Calculate daily stock returns based on the 'Close' prices in the DataFrame.

    Parameters:
    - aligned_data: DataFrame, the data containing 'Close' prices and 'date'

    Returns:
    - aligned_data: DataFrame, the original DataFrame with an added 'daily_return' column
    """
    # Calculate daily stock returns
    aligned_data['daily_return'] = aligned_data['Close'].pct_change()

    # Drop the first row with NaN values due to pct_change()
    aligned_data = aligned_data.dropna()

    return aligned_data



# # Calculate daily returns
# aligned_data_with_returns = calculate_daily_returns(aligned_data)

# # Display the DataFrame with daily returns
# print(aligned_data_with_returns[['date', 'Close', 'daily_return']].head())
