import streamlit as st
import os
import history_manager
from get_ai_response import get_ai_response


def display_chat(file_session_state, chat_history, api_key, model, api_url):
    if file_session_state.active_file:
        real_chat_name = history_manager.generate_chat_name_from_path(file_session_state.active_file)
        st.markdown(f"<h3 style='text-align: center;'>Chat from {real_chat_name}</h3>", unsafe_allow_html=True)
        chat_container = st.container()

        with chat_container:
            for msg in file_session_state.current_chat_content:
                col1, col2 = st.columns([1, 1])
                # Създаваме две колони с различно съотношение
                # [1, 4] означава, че дясната е 4 пъти по-широка (за съобщението)

                if msg["role"] == "assistant":
                    with col1:  # Асистентът е ВЛЯВО
                        with st.chat_message("assistant"):
                            st.write(msg["content"])
                    with col2:  # Дясната колона остава празна
                        st.empty()
                elif msg["role"] == "user":  # Потребителят е ВДЯСНО
                    with col1:  # Лявата колона остава празна
                        st.empty()
                    with col2:
                        # Използваме CSS, за да подравним аватара вдясно (ако е възможно)
                        with st.chat_message("user"):
                            st.write(msg["content"])

        if prompt := st.chat_input("Напиши съобщение..."):
            user_col1, user_col2 = st.columns([1, 1])
            with user_col1:
                st.empty()
            with user_col2:
                with st.chat_message("user"):
                    st.write(prompt)
            chat_history.append({'role': 'user', 'content': prompt})

            assistant_col1, assistant_col2 = st.columns([1, 1])
            with assistant_col1:
                with st.chat_message("assistant"):
                    response_placeholder = st.empty()
                    with st.spinner("Мисли..."):
                        reply = get_ai_response(prompt, chat_history, api_key, model, api_url)
                response_placeholder.write(reply)
            with assistant_col2:
                st.empty()
            chat_history.append({'role': 'assistant', 'content': reply})
            history_manager.save_chat(chat_history, file_session_state.active_file)
