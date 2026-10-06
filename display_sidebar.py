import os
import streamlit as st
import history_manager


def load_sidebar_with_chats(file_session_state):
    user_folder = history_manager.get_user_folder(file_session_state.session_id)
    chat_files = [f for f in os.listdir(user_folder) if f.endswith(".json")]

    with st.sidebar:
        st.markdown('<p style="font-size: 30px; font-weight: bold;">Your chats:</p>', unsafe_allow_html=True)
        st.divider()

        if st.button("Start new chat"):
            file_session_state.active_file = history_manager.get_timestamp_filename_path(file_session_state.session_id)
            file_session_state.current_chat_content = []

        st.divider()

        for file_name in chat_files:
            only_date_name = history_manager.generate_chat_name_from_path(file_name)
            if st.button(f"{only_date_name}", key=file_name):
                full_path = os.path.join(user_folder, file_name)
                file_session_state.active_file = full_path
                file_session_state.current_chat_content = history_manager.load_chat(full_path)