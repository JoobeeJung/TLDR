"""
Module: helper_load_validate
Description:
This module provides functions to validate if the correct input is provided to a function, and
also provides a function to load the required data and transcripts.
"""
import pandas as pd

def validate_ted_or_podcast(ted_or_podcast):
    """
    Validates the type and value of 'ted_or_podcast'.

    Parameters:
    - ted_or_podcast (str): Can be either 'ted' for TED Talks or 'podcast' for Podcasts.

    Raises:
    - TypeError: If ted_or_podcast is not a string.
    - ValueError: If ted_or_podcast is not 'ted' or 'podcast'.
    """
    if not isinstance(ted_or_podcast, str):
        raise TypeError("ted_or_podcast must be of type str")

    if ted_or_podcast not in ('ted', 'podcast'):
        raise ValueError("ted_or_podcast must be either 'ted' or 'podcast'")

def validate_input_transcript(input_transcript):
    """
    Validates the type and content of 'input_transcript'.

    Parameters:
    - input_transcript (str): The transcript based on user provided YouTube video.

    Raises:
    - TypeError: If input_transcript is not a string.
    - ValueError: If input_transcript is an empty string.
    """
    if not isinstance(input_transcript, str):
        raise TypeError("input_transcript must be of type str")

    if not input_transcript:
        raise ValueError("input_transcript must not be empty")

def load_data(ted_or_podcast, test):
    """
    Loads data for TED Talks or Podcasts.

    Parameters:
    - ted_or_podcast (str): Can be either 'ted' for TED Talks or 'podcast' for Podcasts.

    Returns:
    - data_df (DataFrame): The DataFrame containing the loaded data.
    - transcripts (list): The list of transcripts.
    """
    validate_ted_or_podcast(ted_or_podcast)

    if not isinstance(test, bool):
        raise TypeError("test must be a boolean")

    if ted_or_podcast == "ted":
        # Load TED Talks Dataset
        filepath = "../TLDW/data/ted_talks_en.csv"
        data_df = pd.read_csv(filepath)
        transcripts = data_df["transcript"].tolist()  # List of transcripts
    else:
        # Load Podcast Dataset
        filepath = "../TLDW/data/skeptoid_transcripts.csv"
        data_df = pd.read_csv(filepath)
        data_df = data_df.dropna(subset=["text"])
        transcripts = data_df["text"].tolist()  # List of transcripts

    if test:
        data_df = data_df[:5]
        transcripts = transcripts[:5]

    return data_df, transcripts
