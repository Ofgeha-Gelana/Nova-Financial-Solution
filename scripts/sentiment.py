from textblob import TextBlob
import pandas as pd

def get_sentiment(text):

    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def apply_sentiment_analysis(aligned_data):

    aligned_data['sentiment'] = aligned_data['headline'].apply(get_sentiment)
    return aligned_data



# Apply sentiment analysis
# aligned_data_with_sentiment = apply_sentiment_analysis(aligned_data)

# Display the DataFrame with sentiment scores
# print(aligned_data_with_sentiment[['headline', 'sentiment']].head())
