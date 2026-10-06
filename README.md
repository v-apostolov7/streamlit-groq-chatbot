# Streamlit AI Chatbot (Groq API)

A modular, lightweight AI Chatbot web application built with **Python** and **Streamlit**, powered by high-speed LLM inference via the **Groq Cloud API**.

The application features full chat persistence, session-based dialog tracking, and a clean, responsive two-column messaging interface.

---

## Key Features

- **Blazing Fast LLM Inference**: Integrated with Groq API endpoints (`openai/gpt-oss-20b`) for near-instant responses.
- **Interactive UI**: Responsive chat layout built with Streamlit, organizing user and assistant dialogs cleanly across viewport columns.
- **Chat History & Session Management**:
  - Chat History & Session Isolation: Automatically serializes conversations into JSON format (chats/<session_id>/), ensuring each browser session remains private and distinct.
  - Sidebar navigation allows switching between previous conversations or initializing a new session at any time.
- **Dual Configuration Support**: Fully configured to load environment secrets from `.env` locally or via Streamlit Community Cloud (`st.secrets`).
- **Clean Modular Architecture**: Separation of concerns between API communication, history management, and interface components.

---

## Project Structure

```text
├── chats/                  # Stored chat histories in JSON format
├── display_chat.py         # Main chat display and messaging layout logic
├── display_sidebar.py      # Sidebar controller for loading and switching chats
├── get_ai_response.py      # Groq API client handling HTTP completions
├── history_manager.py      # Utilities for saving, loading, and naming sessions
├── streamlit_main.py       # Application entry point
├── requirements.txt        # Production dependencies
├── .env.example            # Environment variables template
└── README.md
```

---

## Tech Stack

- **Language**: Python 3.10+
- **Frontend Framework**: Streamlit
- **API Communication**: Requests
- **Data Persistence**: JSON
- **LLM Provider**: Groq API

---

## Getting Started

### 1. Clone the Repository

git clone https://github.com/<your-username>/<your-repo-name>.git

cd <your-repo-name>

### 2. Create and Activate a Virtual Environment

On Windows:
python -m venv venv
venv\Scripts\activate

On Linux / macOS:
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Configure Environment Variables

Create a `.env` file in the root directory based on the `.env.example` file:

GROQ_API_KEY=your_groq_api_key_here

Get your API key directly from the Groq Console (https://console.groq.com/).

### 5. Run the Application

streamlit run streamlit_main.py

The application will launch locally at `http://localhost:8501`.

---

## Live Demo
Check out the live web app here: [Launch App on Streamlit Cloud](https://app-groq-chatbot-3ytyecsi3r722dq7mya3x5.streamlit.app/)