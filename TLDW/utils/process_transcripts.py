

"""
process_transcripts.py

This script provides functions to process transcripts from YouTube videos.
"""

from youtube_transcript_api import YouTubeTranscriptApi,  TranscriptsDisabled, NoTranscriptAvailable

DEBUG_MODE = False

def get_video_id(youtube_url):
    """
    Extracts the video ID from a YouTube URL.

    Args:
        youtube_url (str): The URL of the YouTube video.

    Returns:
        str: The extracted video ID.
        
    Raises:
        ValueError: If the URL is not in the correct format.
    """
    if 'v=' not in youtube_url:
        raise ValueError("URL is not correct")
    # Split the URL by "=" sign
    parts = youtube_url.split("v=")
    # Take the last part of the resulting list
    video_id = parts[-1]
    # Edge conditions for unit testing:
    if len(video_id) == 0: # check this
        raise ValueError("Video id for input video cannot be blank")
    #if len(video_id) != 11:
     #   raise ValueError("Video ID needs to have 11 characters")
    if not video_id[:11].isalnum():
        raise ValueError("Video ID is not correct")
    if DEBUG_MODE: # check this
        print("Video ID: " + video_id)
    return video_id

def get_video_transcript(video_id):
    """
    Retrieves and formats the transcript for a given video ID.

    Args:
        video_id (str): The ID of the YouTube video.

    Returns:
        str: The formatted transcript.
        
    Raises:
        ValueError: If the transcript is not available in English.
    """
    try:
        transcript_dict = YouTubeTranscriptApi.get_transcript(video_id, languages=['en-US', 'en'])
        # desired_languages = {'en-US', 'en'}  # Desired languages
        # available_languages = {segment.get('language') for segment in transcript_dict}
        # if not desired_languages.intersection(available_languages):
        #     raise ValueError("Transcript does not contain any of the desired languages.")
        formatted_transcript = format_transcript(transcript_dict)
        if DEBUG_MODE:
            print("Processed transcript: " + formatted_transcript)
        return formatted_transcript
    except TranscriptsDisabled as exc :
        raise ValueError("Transcripts are disabled for this video.") from exc
    except NoTranscriptAvailable as exc:
        raise ValueError("No transcript available for this video.") from exc
    except Exception as exc:
        raise exc
   # except Exception as error:
   #     print("Failed to get transcript")
   #     if DEBUG_MODE:
   #         print(f"Error: {error}")
   #     return None

def format_transcript(transcript_dict):
    """
    Formats the transcript dictionary into a single string.

    Args:
        transcript_dict (list): List of dictionary items representing transcript segments.

    Returns:
        str: The formatted transcript string.
        
    Raises:
        ValueError: If there is no transcript associated with the video.
    """
    transcript_string = ""
    for item in transcript_dict:
        transcript_string += item['text'] + " "
    # Replace multiple spaces with a single space
    transcript_string = ' '.join(transcript_string.split())
    #if len(transcript_string) == 0:
     #   raise ValueError('There is no transcript associated with the video')
    return transcript_string.strip()

def get_transcript(youtube_url):
    """
    Retrieves the transcript for a YouTube video given its URL.

    Args:
        youtube_url (str): The URL of the YouTube video.

    Returns:
        str: The formatted transcript.
        
    Raises:
        ValueError: If the URL is not in the correct format or transcript retrieval fails.
    """
    if not youtube_url.startswith("https://www.youtube.com"):
        raise ValueError("Video URL should start with 'https://www.youtube.com'")
    video_id = get_video_id(youtube_url)
    transcript = get_video_transcript(video_id)
    return transcript
