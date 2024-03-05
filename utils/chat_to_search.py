"""
This module is implementing the Gemini chatbot feature into the main interface.
"""
import streamlit as st

# Gemini API
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun
from langchain_community.callbacks import StreamlitCallbackHandler

# api_key = os.getenv("GEMINI_API_KEY")
APIKEY = "AIzaSyAIDOlnc6NVX9LCwvNNuF6zXqBWplJsVpM"

genai.configure(api_key=APIKEY)
genai_model = genai.GenerativeModel('gemini-pro')

# Extract information from text based on prompt instructions
def get_search_result(context, user_prompt):
    """
    This function returns the ressult of user query using Gemini.
    """
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    st.chat_message("user").write(user_prompt)

    if not APIKEY:
        st.info("Please add your GEMINI API key to continue.")
        st.stop()

    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=APIKEY)

    with st.spinner('Asking to GEMINI...'):
        context_prompt = "Answer the question based on the context below. Context:" + context
        prompt =  context_prompt + "Question:" + user_prompt

        result = llm.invoke(prompt)
        search = DuckDuckGoSearchRun(name="Search")
        search_agent = initialize_agent(
            [search], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True
        )

        with st.chat_message("assistant"):
            st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
            response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
            st.session_state.messages.append({"role": "assistant", "content": response})
            return response
