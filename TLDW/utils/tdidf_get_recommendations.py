"""
Module: tdidf_get_recommendations
Description:
This module provides a functions to get recommendations based on user transcripts using tdidf
embeddings. The function takes a user transcript and a type of content (TED or podcast), generates
tdidf embeddings for the transcript, calculates cosine similarity between the user transcript
embedding and preprocessed tdidf embeddings of TED Talks or Podcasts, and returns top 3
recommendations based on cosine similarity.
"""

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import joblib
from . import helper_load_validate

def get_tdidf_recs(input_transcript, ted_or_podcast):
    """
    This function generates recommendations based on input transcript and tdidf embeddings.

    Parameters:
    - input_transcript (str): The user transcript for which recommendations are needed.
    - ted_or_podcast (str): Type of content, either 'ted' for TED Talks or 'podcast' for Podcasts.

    Raises:
    - TypeError: If input_transcript or ted_or_podcast is not of type str.
    - ValueError: If n is an empty string or if ted_or_podcast is neither
      'ted' nor 'podcast'.

    Returns:
    - top_recommendations: List of top 3 recommendations
    """
    helper_load_validate.validate_input_transcript(input_transcript)
    helper_load_validate.validate_ted_or_podcast(ted_or_podcast)

    # Load preprocessed dataset and embeddings
    if ted_or_podcast == "ted":
        # Load TED Talks Dataset
        data_df = pd.read_csv("../TLDW/data/ted_tdidf_preprocessed.csv")
        tfidf_vectorizer = joblib.load('../TLDW/data/ted_tfidf_vectorizer.joblib')
        transcripts = data_df['transcript']
    else:
        # Load Podcast Dataset
        data_df = pd.read_csv("../TLDW/data/podcast_tdidf_preprocessed.csv")
        tfidf_vectorizer = joblib.load('../TLDW/data/podcast_tfidf_vectorizer.joblib')
        transcripts = data_df["text"].tolist()  # List of transcripts

    # Generate TF-IDF vector for transcript from Gemini
    tfidf_matrix = tfidf_vectorizer.transform([input_transcript])

    # Transform transcripts into TF-IDF vectors and calculate cosine similarities
    tfidf_vectors = tfidf_vectorizer.transform(transcripts)
    cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_vectors).flatten()

    # Add cosine similarities as a column in the DataFrame
    data_df['sim_scores'] = cosine_similarities

    # Get top 3 recommendations based on cosine similarity
    top_recommendations = data_df.nlargest(3, 'sim_scores')

    # Print top 3 recommendations
    # print("-------------------------------------------------------------")
    # print(f"Top 3 Recommendations for {ted_or_podcast} - TDIDF:")
    # for i in range(3):
    #     print("Recommendation", i + 1)
    #     print("Title:", top_recommendations.iloc[i]["title"])
    #     print("Title:", top_recommendations.iloc[i]["url"])
    #     print("Similarity Score:", top_recommendations.iloc[i]["sim_scores"])
    #     print()

    return top_recommendations
