from textblob import TextBlob
import pandas as pd

def analyze_and_display_sentiment(df, text_column):
    """
    Analyzes the sentiment of text in the specified column of a DataFrame, adds a sentiment score column, and displays the DataFrame.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the text data.
    - text_column (str): The name of the column containing text data for sentiment analysis.
    """
    # Function to get sentiment score
    def get_sentiment(text):
        analysis = TextBlob(text)
        return analysis.sentiment.polarity

    # Apply sentiment analysis to the specified column
    df['sentiment'] = df[text_column].apply(get_sentiment)

    # Display the DataFrame with sentiment scores
    print(df[[text_column, 'sentiment']].head())