"""
Module: tdidf_preprocess
Description:
This module provides preprocess_tdidf function that will create embeddings based on input arguments.
It loads either TED Talks or Podcast transcripts, encodes them using tdidf vectorizer and saves the
embeddings to a file.
"""
# pylint: disable=E1101 # Added this as pylint can't understand dynamic code causing pylint issues
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from . import helper_load_validate

def preprocess_tdidf(ted_or_podcast, test):
    """
    This file preprocesses the ted talks/ podcasts and creates the embedding files for each using
    tdidf vectorizer.
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

    helper_load_validate.validate_ted_or_podcast(ted_or_podcast)

    if not isinstance(test, bool):
        raise TypeError("test must be a boolean")

    data_df, transcripts = helper_load_validate.load_data(ted_or_podcast, test)

    tfidf_vectorizer = TfidfVectorizer()
    tokenized_transcripts = tfidf_vectorizer.fit_transform(transcripts)

    data_df['token'] = (
    [" ".join(tokens) for tokens in tfidf_vectorizer.inverse_transform(tokenized_transcripts)])

    if test:
        output_path = '../TLDW/tests/test_output/'
        # Save the preprocessed DataFrame and TF-IDF vectorizer to files
        if ted_or_podcast == "ted":
            data_df.to_csv(output_path + 'test_ted_tdidf_preprocessed.csv', index=False)
            joblib.dump(tfidf_vectorizer, output_path + 'test_ted_tfidf_vectorizer.joblib')
        else:
            data_df.to_csv(output_path + 'test_podcast_tdidf_preprocessed.csv', index=False)
            joblib.dump(tfidf_vectorizer, output_path + 'test_podcast_tfidf_vectorizer.joblib')
    else:
        # Save the preprocessed DataFrame and TF-IDF vectorizer to files
        output_path = '../TLDW/data/'
        if ted_or_podcast == "ted":
            data_df.to_csv(output_path + 'ted_tdidf_preprocessed.csv', index=False)
            joblib.dump(tfidf_vectorizer, output_path + 'ted_tfidf_vectorizer.joblib')
        else:
            data_df.to_csv(output_path + 'podcast_tdidf_preprocessed.csv', index=False)
            joblib.dump(tfidf_vectorizer, output_path + 'podcast_tfidf_vectorizer.joblib')
