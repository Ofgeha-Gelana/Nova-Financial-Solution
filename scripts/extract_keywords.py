import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def extract_keywords(df, column_name, max_features=10):
    """
    Extracts the top keywords from a specified column in the DataFrame using TF-IDF.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    column_name (str): The column name containing the text data (e.g., headlines).
    max_features (int): The maximum number of keywords to extract. Default is 10.

    Returns:
    list: A sorted list of tuples with keywords and their corresponding TF-IDF scores.
    """
    # Initialize TF-IDF Vectorizer
    tfidf = TfidfVectorizer(stop_words='english', max_features=max_features)

    # Fit and transform the data
    tfidf_matrix = tfidf.fit_transform(df[column_name])

    # Get the feature names
    feature_names = tfidf.get_feature_names_out()

    # Sum the TF-IDF scores for each feature over all documents
    sum_tfidf = tfidf_matrix.sum(axis=0)

    # Extract keywords with their scores
    keywords = [(feature_names[i], sum_tfidf[0, i]) for i in range(len(feature_names))]

    # Sort keywords by their scores in descending order
    keywords = sorted(keywords, key=lambda x: x[1], reverse=True)

    return keywords


