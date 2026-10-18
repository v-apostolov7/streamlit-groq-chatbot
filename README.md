# Streamlit AI Chatbot & RAG System (Groq API + LangChain + FAISS)

A modular Generative AI and **Retrieval-Augmented Generation (RAG)** web application built with **Python**, **Streamlit**, and **LangChain**, powered by high-speed LLM inference via the **Groq Cloud API**.

The application combines real-time conversational AI with custom PDF document indexing, utilizing local multilingual vector embeddings and a **FAISS Vector Database** for semantic search, alongside session-isolated JSON chat persistence.

---

## Key Features

- **End-to-End RAG Pipeline**:
  - **Automated PDF Parsing & Chunking**: Uses LangChain's `PyPDFLoader` and `RecursiveCharacterTextSplitter` (`chunk_size=1200`, `chunk_overlap=250`) to process uploaded documents on the fly.
  - **Multilingual Embeddings & Vector Store**: Converts text chunks into dense vector representations using HuggingFace's `paraphrase-multilingual-MiniLM-L12-v2` model and indexes them in an in-memory **FAISS** vector database.
  - **Semantic Search**: Retrieves the top-6 (`k=6`) most contextually relevant document passages with page-level metadata to ground LLM responses and minimize hallucinations.
- **Advanced Prompt Engineering**: Implements dynamic system role conditioning, context injection, and strict multilingual output constraints.
- **Blazing Fast LLM Inference**: Integrated with Groq API REST endpoints (`openai/gpt-oss-20b`) for near-instant responses.
- **Chat History & Session Management**:
  - Automatically serializes conversations into JSON format (`chats/<session_id>/`), ensuring each browser session remains private and isolated.
  - Sidebar navigation allows switching between previous conversations, uploading new PDF context, or initializing a new session at any time.
- **Dual Configuration Support**: Configured to load environment secrets seamlessly from `.env` locally or via Streamlit Community Cloud (`st.secrets`).

---

## Project Structure

~~~text
├── chats/                  # Stored chat histories in JSON format (per session)
├── display_chat.py         # Main chat display and two-column messaging layout logic
├── display_sidebar.py      # Sidebar controller for chat history and PDF RAG uploads
├── get_ai_response.py      # Groq API client with dynamic System Prompt & RAG injection
├── rag_engine.py           # LangChain PDF loader, chunking, HuggingFace embeddings & FAISS search
├── history_manager.py      # Utilities for saving, loading, and naming chat sessions
├── streamlit_main.py       # Application entry point and session state initialization
├── requirements.txt        # Production dependencies
├── .env.example            # Environment variables template
└── README.md               # Project documentation
~~~

---

## Tech Stack

- **Language**: Python 3.10+
- **Frontend Framework**: Streamlit
- **LLM Provider & API**: Groq Cloud API (REST HTTP requests)
- **RAG & Orchestration**: LangChain (`langchain-community`, `langchain-text-splitters`, `langchain-huggingface`), `pypdf`
- **Vector Database & Embeddings**: FAISS (`faiss-cpu`), HuggingFace `sentence-transformers` (`paraphrase-multilingual-MiniLM-L12-v2`)
- **Data Persistence**: JSON

---

## Getting Started

### 1. Clone the Repository

~~~bash
git clone https://github.com/v-apostolov7/streamlit-groq-chatbot.git
cd streamlit-groq-chatbot
~~~

### 2. Create and Activate a Virtual Environment

On Windows:

~~~bash
python -m venv venv
venv\Scripts\activate
~~~

On Linux / macOS:

~~~bash
python3 -m venv venv
source venv/bin/activate
~~~

### 3. Install Dependencies

~~~bash
pip install -r requirements.txt
~~~

### 4. Configure Environment Variables

Create a `.env` file in the root directory based on the `.env.example` file:

~~~env
GROQ_API_KEY=your_groq_api_key_here
~~~

Get your API key directly from the [Groq Console](https://console.groq.com/).

### 5. Run the Application

~~~bash
streamlit run streamlit_main.py
~~~

The application will launch locally at `http://localhost:8501`.

---

## Live Demo

Check out the live web app here: [Launch App on Streamlit Cloud](https://app-groq-chatbot-3ytyecsi3r722dq7mya3x5.streamlit.app/)