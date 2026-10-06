import streamlit as st
import os
import history_manager


def load_sidebar_with_chats(file_session_state):
    folder_path = 'chats'

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    chat_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

    with st.sidebar:
        st.markdown('<p style="font-size: 30px; font-weight: bold;">Your chats:</p>', unsafe_allow_html=True)

        st.divider()

        if st.button("Start new chat"):
            file_session_state.active_file = history_manager.get_timestamp_filename_path()
            file_session_state.current_chat_content = history_manager.load_chat(os.path.join('chats', file_session_state.active_file))

        st.divider()

        for file_name in chat_files:
            only_date_name = history_manager.generate_chat_name_from_path(file_name)
            if st.button(f"{only_date_name}", key=file_name):
                file_session_state.active_file = os.path.join(folder_path, file_name)
                file_session_state.current_chat_content = history_manager.load_chat(os.path.join('chats', file_name))

