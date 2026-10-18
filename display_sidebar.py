import os
import streamlit as st
import history_manager
from rag_engine import create_vector_db_from_pdf


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

        st.markdown("### 📄 RAG Document Context")
        uploaded_file = st.file_uploader("Upload PDF for RAG", type=["pdf"])


        if uploaded_file is not None:
            if file_session_state.uploaded_pdf_name != uploaded_file.name:
                with st.spinner("Indexing PDF into Vector DB..."):
                    file_session_state.vector_db = create_vector_db_from_pdf(uploaded_file)
                    file_session_state.uploaded_pdf_name = uploaded_file.name
                st.success(f"Indexed: {uploaded_file.name}")
        else:
            file_session_state.vector_db = None
            file_session_state.uploaded_pdf_name = None

        st.divider()

        for file_name in chat_files:
            only_date_name = history_manager.generate_chat_name_from_path(file_name)
            if st.button(f"{only_date_name}", key=file_name):
                full_path = os.path.join(user_folder, file_name)
                file_session_state.active_file = full_path
                file_session_state.current_chat_content = history_manager.load_chat(full_path)