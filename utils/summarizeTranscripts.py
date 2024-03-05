
GEMINI_API_KEY = 'AIzaSyAIDOlnc6NVX9LCwvNNuF6zXqBWplJsVpM' # Anurag Key

# Gemini API
import google.generativeai as genai

genai.configure(api_key=GEMINI_API_KEY)
genai_model = genai.GenerativeModel('gemini-pro')

# Extract information from text based on prompt instructions
def get_ai_extract(prompt, text):
    response = genai_model.generate_content(prompt + text, stream=False)
    return response.text, response.prompt_feedback, response.candidates