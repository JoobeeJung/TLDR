"""
This module is implementing the Gemini chatbot feature into the main interface.
"""
import os
import streamlit as st

# Gemini API
from langchain_google_genai import ChatGoogleGenerativeAI, HarmBlockThreshold, HarmCategory
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks.streamlit.streamlit_callback_handler import StreamlitCallbackHandler
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun
# from langchain_community.callbacks import StreamlitCallbackHandler

# .env
from dotenv import load_dotenv
# load .env
load_dotenv()

API_KEY = os.environ.get('GEMINI_API_KEY')

# Extract information from text based on prompt instructions
def get_search_result(context, user_prompt):
    """
    This function returns the ressult of user query using Gemini.
    """
    if not context or len(context) == 0:
        raise TypeError("Context should be given")
    if not user_prompt or len(user_prompt) == 0:
        raise TypeError("User prompt should be given")

    if not API_KEY:
        st.info("Please add your GEMINI API key to continue.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": user_prompt})
    st.chat_message("user").write(user_prompt)

    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=API_KEY, safety_settings={
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    },)

    with st.spinner('Asking to GEMINI...'):
        context_prompt = "Answer the question based on the context below. Context:" + context
        prompt =  context_prompt + "Question:" + user_prompt

        llm.invoke(prompt)
        search = DuckDuckGoSearchRun(name="Search")
        search_agent = initialize_agent(
            [search], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True
        )

        with st.chat_message("assistant"):
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
            st.session_state.messages.append({"role": "assistant", "content": response})
            return response
