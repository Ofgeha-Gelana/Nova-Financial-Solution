import matplotlib.pyplot as plt

def visualize_stock_data(df):
    # Ensure the DataFrame has the necessary columns
    required_columns = ['Close', 'SMA', 'MACD', 'MACD_signal']
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"DataFrame is missing required column: {col}")
    
    plt.figure(figsize=(14, 7))

    # Plot the closing price and SMA
    plt.plot(df['Close'], label='Close Price')
    plt.plot(df['SMA'], label='50-Day SMA', color='orange')
    plt.title('Close Price and 50-Day SMA')
    plt.legend()
    plt.show()

    # Plot MACD and signal line
    plt.figure(figsize=(14, 7))
    plt.plot(df['MACD'], label='MACD')
    plt.plot(df['MACD_signal'], label='MACD Signal', color='red')
    plt.title('MACD and MACD Signal')
    plt.legend()
    plt.show()



