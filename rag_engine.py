import tempfile
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


def create_vector_db_from_pdf(uploaded_file):
    """
    1. Взима качения PDF от Streamlit.
    2. Реже го на парчета (Chunking).
    3. Превръща парчетата във вектори (Embeddings) и ги записва във векторна база (FAISS).
    """
    # Записваме временно качения файл, за да може PyPDFLoader да го прочете
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    try:
        # 1. Зареждане на PDF документа
        loader = PyPDFLoader(tmp_file_path)
        documents = loader.load()

        # 2. Chunking: Разделяме текста на парчета по 1200 символа със застъпване от 150 символа
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1200,
            chunk_overlap=250
        )
        chunks = text_splitter.split_documents(documents)

        # 3. Embeddings: Използваме безплатен локален модел от HuggingFace за превръщане на текст в числа
        embeddings = HuggingFaceEmbeddings(
            model_name = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )

        # 4. Vector Database: Създаваме FAISS векторна база в паметта
        vector_db = FAISS.from_documents(chunks, embeddings)
        return vector_db

    finally:
        # Изтриваме временния файл след като сме готови
        if os.path.exists(tmp_file_path):
            os.remove(tmp_file_path)


def get_relevant_context(vector_db, user_query, k=6):
    """
    Прави Semantic Search (търсене по смисъл) във векторната база
    и връща най-подходящите k (6) пасажа от документа.
    """
    if vector_db is None:
        return ""

    # Търсим 6-те най-близки по смисъл парчета текст до въпроса на потребителя
    relevant_docs = vector_db.similarity_search(user_query, k=k)

    # Събираме намерените парчета в един общ текст
    context = "\n\n---\n\n".join(
        [f"[Страница {doc.metadata.get('page', 0) + 1}]:\n{doc.page_content}" for doc in relevant_docs])
    return context