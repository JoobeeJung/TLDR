"""
Module: minilm_preprocess
Description:
This module provides preprocess_minilm function that will create embeddings based on input
arguments.
It loads either TED Talks or Podcast transcripts, encodes them using a pre-trained minilm model,
and saves the embeddings to a file.
"""

import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
from . import helper_load_validate

def preprocess_minilm(ted_or_podcast, test):
    """
    This file preprocesses the ted talks/ podcasts and creates the embedding files for each using
    sentence_transformer MiniLM.
    It is run only once for each, ted and podcast to create the embedding files, and not run again
    unless the original dataset has changed.

    Parameters:
    - ted_or_podcast (str): Type of data to preprocess. Should be either 'ted' or 'podcast'.

    Raises:
    - TypeError: If ted_or_podcast is not a string.
    - ValueError: If ted_or_podcast is neither 'ted' nor 'podcast'.

    Returns:
    None
    """

    if not isinstance(test, bool):
        raise TypeError("test must be a boolean")

    _, transcripts = helper_load_validate.load_data(ted_or_podcast, test)

    # Load Sentence Transformer model
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    model = SentenceTransformer(model_name)

    # Create embeddings for TED transcripts and chunk them
    chunk_size = 256

    embeddings = []
    for transcript in transcripts:
        if isinstance(transcript, str):
            chunks = [transcript[i:i+chunk_size] for i in range(0, len(transcript), chunk_size)]
            chunk_embeddings = [model.encode(chunk) for chunk in chunks]
            transcript_embedding = np.mean(chunk_embeddings, axis=0)
            embeddings.append(transcript_embedding)

    if test:
        output_path = '../TLDW/tests/test_output/'
        if ted_or_podcast == "ted":
            with open(output_path + 'test_ted_sentTrans_embeddings.pkl', 'wb') as file:
                pickle.dump(embeddings, file)
        else:
            with open(output_path + 'test_podcast_sentTrans_embeddings.pkl', 'wb') as file:
                pickle.dump(embeddings, file)
    else:
        # Save embeddings to a file
        output_path = '../TLDW/data/'
        if ted_or_podcast == "ted":
            with open(output_path + 'ted_sentTrans_embeddings.pkl', 'wb') as file:
                pickle.dump(embeddings, file)
        else:
            with open(output_path + 'podcast_sentTrans_embeddings.pkl', 'wb') as file:
                pickle.dump(embeddings, file)
