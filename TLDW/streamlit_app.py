"""
Streamlit App for TED Talk Recommendations.

This app allows users to enter a YouTube URL, obtain the transcript,
summary, and keywords using Gemini, and get recommendations for TED Talks
using various recommendation algorithms.
"""

import streamlit as st

from utils.process_transcripts import get_transcript
from utils.summarize_transcripts import get_ai_extract
from utils.bert_get_recommendations import get_bert_recs
from utils.minilm_get_recommedations import get_minilm_recs
from utils.tdidf_get_recommendations import get_tdidf_recs
from utils.chat_to_search import get_search_result


st.title("📝 TL;DW ")
st.caption("🚀 Get a TED Talk Recommendation based on your interest!")

# Function to create accordion-style recommendations
def create_accordion_recs(recommendations):
    """
    Creates an accordion-style display of recommendations.

    Args:
        recommendations (DataFrame): DataFrame containing recommendations with 
        columns 'title', 'url', and 'cosine_similarity'.

    Returns:
        None
    """
    i = 1
    for _, row in recommendations.iterrows():
        with st.expander(f"Recommendation {i}: {row['title']}"):
            st.markdown("- **URL:** " + row['url'])
            st.markdown("- **Similarity Score:** " + str(round(row['sim_scores'], 2)))
        i += 1

# Function to get transcript, summary, and keywords if not already obtained
def get_transcript_summary_keywords(link):
    """
    Retrieves transcript, summary, and keywords for the provided YouTube video link.

    Args:
        link (str): The YouTube video link.

    Returns:
        None
    """
    if 'transcript' not in st.session_state:
        with st.spinner('Getting transcript...'):
            st.session_state.transcript = get_transcript(link)
    if 'summary' not in st.session_state:
        with st.spinner('Summarizing using Gemini...'):
            st.session_state.summary = get_ai_extract(
                "Summarize the following transcript in 150 words: ", st.session_state.transcript)
            st.success('Summary is ready!')
    if 'keywords' not in st.session_state:
        with st.spinner('Getting keywords using Gemini...'):
            st.session_state.keywords = get_ai_extract(
                "Generate the top 10 most important keywords: ", st.session_state.transcript)
            st.success('Keywords are ready!')

# Starting information
st.info(
    """
    So... how does this work?  
        :one:  Enter a youtube link in the text box below.  
        :two:  Get a summary and keywords from Google's Gemini.  
        :three: Choose to get recommendations from either hundreds of TED Talks or Podcasts.  
        :four: Not satisfied? Test out our different models for different recommendations.  
    """,
    icon="👾",
)
# Get user input
def rerun():
    for key in st.session_state.keys():
        del st.session_state[key]

title = st.text_input('Youtube URL' , on_change=rerun)

# Check if user input is provided
if title:
    # Get transcript, summary, and keywords if not already obtained
    get_transcript_summary_keywords(title)

    # Display summary if available
    if 'summary' in st.session_state:
        st.header("Summary")
        st.write(st.session_state.summary)

    st.divider()

    # Display keywords if available
    if 'keywords' in st.session_state:
        st.header("Keywords")
        st.write(st.session_state.keywords)

    st.divider()

    content_mapping = {"TED Talks": "ted", "Podcasts": "podcast"}
    content_type = st.radio("Choose Content Type", list(content_mapping.keys()))
    selected_content_type = content_mapping[content_type]
    st.session_state.selected_content_type = selected_content_type
    
    # Display recommender buttons based on content type choice
    if selected_content_type:
        st.write(f"Choose a recommender to get recommendations for {content_type}:")
        col1, col2, col3 = st.columns(3)

        # SBERT Recommender button
        if col1.button('SBERT Recommender', type='primary'):
            bert_recs = get_bert_recs(st.session_state.transcript, selected_content_type)
            if bert_recs is not None and not bert_recs.empty:
                st.header('Top 3 SBERT Recommendations')
                create_accordion_recs(bert_recs.head(3))

        # MiniLM Recommender button
        if col2.button('MiniLM Recommender', type='primary'):
            miniLM_recs = get_minilm_recs(st.session_state.transcript, selected_content_type)
            if miniLM_recs is not None and not miniLM_recs.empty:
                st.header('Top 3 MiniLM Recommendations')
                create_accordion_recs(miniLM_recs.head(3))

        # TF-IDF Recommender button
        if col3.button('TF-IDF Recommender', type='primary'):
            tf_idf_recs = get_tdidf_recs(st.session_state.transcript, selected_content_type)
            if tf_idf_recs is not None and not tf_idf_recs.empty:
                st.header('Top 3 TF-IDF Recommendations')
                create_accordion_recs(tf_idf_recs.head(3))

    st.divider()

    st.header("🔎 Learn More - Chat with GEMINI ")
    st.write("If you want to learn more about the content, ask GEMINI using this chat function!")

    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content":
             "Hi, I'm a chatbot who can search the web. How can I help you?"}
        ]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input(placeholder="Type any questions you have about the YouTube video."):
        st.write(get_search_result(st.session_state.transcript, prompt))
