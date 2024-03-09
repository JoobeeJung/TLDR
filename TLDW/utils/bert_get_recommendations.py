"""
Module: bert_get_recommendations
Description:
This module provides a functions to get recommendations based on user transcripts using Roberta
embeddings. The function takes a user transcript and a type of content (TED or podcast), generates
Roberta embeddings for the transcript, calculates cosine similarity between the user transcript
embedding and preprocessed Roberta embeddings of TED Talks or Podcasts, and returns top 3
recommendations based on cosine similarity.
"""

import torch
import pandas as pd
from sentence_transformers import SentenceTransformer, util
from . import helper_load_validate

def get_bert_recs(user_transcript, ted_or_podcast):
    """
    This function generates recommendations based on user transcript and Roberta embeddings.

    Parameters:
    - user_transcript (str): The user transcript for which recommendations are needed.
    - ted_or_podcast (str): Type of content, either 'ted' for TED Talks or 'podcast' for Podcasts.

    Raises:
    - TypeError: If user_transcript or ted_or_podcast is not of type str.
    - ValueError: If user_transcript is an empty string or if ted_or_podcast is neither
      'ted' nor 'podcast'.

    Returns:
    - top_recommendations: List of top 3 recommendations
    """

    helper_load_validate.validate_input_transcript(user_transcript)
    helper_load_validate.validate_ted_or_podcast(ted_or_podcast)

    if ted_or_podcast == "ted":
        # Load preprocessed TED Talks embeddings and TED Dataset
        embeddings = torch.load('../TLDW/data/ted_sbert_embeddings.pt')
        filepath = "../TLDW/data/ted_talks_en.csv"
        data_df = pd.read_csv(filepath)
    else:
        # Load preprocessed Podcast Talks embeddings and Podcast Dataset
        embeddings = torch.load('../TLDW/data/podcast_sbert_embeddings.pt')
        filepath = "../TLDW/data/skeptoid_transcripts.csv"
        data_df = pd.read_csv(filepath)

    titles = data_df["title"].tolist()  # List of titles
    urls = data_df["url"].tolist()

    # Load pre-trained SBERT model
    model = SentenceTransformer('stsb-roberta-large')

    # Generate SBERT embedding for the user transcript
    user_embedding = model.encode(user_transcript)

    # Calculate cosine similarity between user transcript embedding and all TED Talks embeddings
    similarities = util.cos_sim(user_embedding, embeddings)
    similarities = similarities.flatten()

    # Create a DataFrame with TED Talks titles, descriptions, and cosine similarities
    ted_talks_df = pd.DataFrame({'title': titles, 'url':urls, 'sim_scores': similarities})

    # Get top 3 recommendations based on cosine similarity
    top_recommendations = ted_talks_df.nlargest(3, 'sim_scores')

    # Print top 3 recommendations
    print("-------------------------------------------------------------")
    print(f"Top 3 Recommendations for {ted_or_podcast} - Model Roberta:")
    i = 1
    for _, row in top_recommendations.iterrows():
        print(f"Recommendation {i}")
        print(f"Title: {row['title']}")
        print(f"Url: {row['url']}")
        print(f"Similarity Score: {row['sim_scores']}")
        i += 1
        print()

    return top_recommendations
