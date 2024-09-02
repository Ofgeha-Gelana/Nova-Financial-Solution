import pandas as pd
from .convert_and_align_date import convert_and_align_dates

def load_data(news_path, stock_path):

    # Load the news data
    news_data = pd.read_csv(news_path)

    # Load the stock price data
    stock_data = pd.read_csv(stock_path)

    aligned_data = convert_and_align_dates(news_data, stock_data, 'date')
        
    return aligned_data

# Usage example:
# news_data, stock_data = load_data('../Data/raw_analyst_ratings.csv', '../Data/AAPL_historical_data.csv')
