

"""
Module for summarizing transcripts using Gemini AI API.
"""
import os
# Gemini API
import google.generativeai as genai

# .env
from dotenv import load_dotenv
# load .env
load_dotenv()
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

safety_settings = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

genai.configure(api_key=GEMINI_API_KEY)
genai_model = genai.GenerativeModel('gemini-pro')

# Extract information from text based on prompt instructions
def get_ai_extract(prompt, text, api_client=None):
    """
    Extract information from text based on prompt instructions.

    Args:
        prompt (str): The prompt to be used for extraction.
        text (str): The text from which information needs to be extracted.

    Returns:
        tuple: A tuple containing extracted text, prompt feedback, and candidates.
    Raises:
        ValueError: If prompt or text is empty.
    """
    if len(prompt) == 0:
        raise ValueError("Prompt cannot be empty")
    if len(text) == 0:
        raise ValueError("Text cannot be empty")

    if api_client is None:
        response = genai_model.generate_content(prompt + text, safety_settings=safety_settings)
    else:
        response = api_client(prompt + text, safety_settings=safety_settings)

    for candidate in response.candidates:
        return ' '.join([part.text for part in candidate.content.parts])
    #return response.text, response.prompt_feedback, response.candidates
