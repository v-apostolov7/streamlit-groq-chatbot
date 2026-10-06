import streamlit as st
import os
from display_sidebar import load_sidebar_with_chats
import display_chat
from dotenv import load_dotenv

load_dotenv()
API_KEY = st.secrets.get("GROQ_API_KEY") or os.getenv('GROQ_API_KEY')
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "openai/gpt-oss-20b"

st.set_page_config(layout="wide")

if "current_chat_content" not in st.session_state:
    st.session_state.current_chat_content = []
if "active_file" not in st.session_state:
    st.session_state.active_file = None


load_sidebar_with_chats(st.session_state)

display_chat.display_chat(st.session_state, st.session_state.current_chat_content, API_KEY, MODEL, API_URL)
