import talib
def technical_indicators(df):
    df['SMA_50'] = talib.SMA(df['Close'], timeperiod=50)
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    df['MACD'], df['MACD_Signal'], _ = talib.MACD(df['Close'], fastperiod=12, slowperiod=26,   signalperiod=9)
    return df