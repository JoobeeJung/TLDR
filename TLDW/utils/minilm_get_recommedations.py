"""
Module: mini_get_recommendations
Description:
This module provides a functions to get recommendations based on user transcripts using MiniLM
embeddings. The function takes a user transcript and a type of content (TED or podcast), generates
MiniLM embeddings for the transcript, calculates cosine similarity between the user transcript
embedding and preprocessed MiniLM embeddings of TED Talks or Podcasts, and returns top 3
recommendations based on cosine similarity.
"""

import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from . import helper_load_validate

# Function to get recommendations using precomputed embeddings
def get_minilm_recs(input_transcript, ted_or_podcast):
    """
    This function generates recommendations based on input transcript and MiniLM embeddings.

    Parameters:
    - input_transcript (str): The user transcript for which recommendations are needed.
    - ted_or_podcast (str): Type of content, either 'ted' for TED Talks or 'podcast' for Podcasts.

    Raises:
    - TypeError: If input_transcript or ted_or_podcast is not of type str.
    - ValueError: If input_transcript is an empty string or if ted_or_podcast is neither
      'ted' nor 'podcast'.

    Returns:
    top_recommendations: List of top 3 recommendations
    """

    helper_load_validate.validate_input_transcript(input_transcript)
    helper_load_validate.validate_ted_or_podcast(ted_or_podcast)

    titles, urls, embeddings = load_data(ted_or_podcast)

    # Load Sentence Transformer model
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    # Encode user input in chunks
    chunk_size = 256
    chunks = [input_transcript[i:i+chunk_size] for i in range(0, len(input_transcript), chunk_size)]
    user_input_embedding = np.mean([model.encode(chunk) for chunk in chunks], axis=0)

    # Compute cosine similarity between user input and TED transcripts
    similarities = cosine_similarity([user_input_embedding], embeddings)[0]

    # Rank transcripts based on similarity scores
    ranked_transcripts = sorted(zip(titles, urls, similarities), key=lambda x: x[2], reverse=True)

    # Get top 3 recommendations
    top_recommendations = pd.DataFrame(ranked_transcripts, columns=['title', 'url', 'sim_scores'])
    top_recommendations = top_recommendations.head(3)


    # Print top 3 recommendations
    # print("-------------------------------------------------------------")
    # print(f"Top 3 Recommendations for {ted_or_podcast} - Model all-MiniLM-L6-v2:")
    # for i, (title, url, score) in enumerate(top_recommendations.itertuples(index=False), 1):
    #     print(f"Recommendation {i}")
    #     print(f"Title: {title}")
    #     print(f"URL: {url}")
    #     print(f"Similarity Score: {score}")
    #     print()

    return top_recommendations

def load_data(ted_or_podcast):
    """
    Load data and corresponding embeddings for TED Talks or Podcasts.

    This function loads the dataset and precomputed embeddings for either TED Talks or Podcasts,
    depending on the specified type of content.

    Parameters:
    - ted_or_podcast (str): Type of content, either 'ted' for TED Talks or 'podcast' for Podcasts.

    Returns:
    titles (list): List of titles from the loaded dataset.
    urls (list): List of URLs corresponding to the titles.
    embeddings: Precomputed embeddings corresponding to the loaded dataset
    """
    if ted_or_podcast == "ted":
        # Load TED Talks Dataset
        data_df = pd.read_csv("../TLDW/data/ted_talks_en.csv")
        with open('../TLDW/data/ted_sentTrans_embeddings.pkl', 'rb') as file:
            embeddings = pickle.load(file)
    else:
        # Load Podcast Dataset
        data_df = pd.read_csv("../TLDW/data/skeptoid_transcripts.csv")
        data_df = data_df.dropna(subset=['text'])
        with open('../TLDW/data/podcast_sentTrans_embeddings.pkl', 'rb') as file:
            embeddings = pickle.load(file)

    titles = data_df["title"].tolist()
    urls = data_df["url"].tolist()

    return titles, urls, embeddings
