import requests
from rag_engine import get_relevant_context


def get_ai_response(user_input, chat_history, api_key, model, api_url, vector_db=None):

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }


    system_prompt = (
        "You are a helpful and precise AI assistant. "
        "Provide clear, structured, and accurate answers."
    )

    if vector_db is not None:
        context = get_relevant_context(vector_db, user_input, k=3)
        if context:
            system_prompt += (
                "\n\nUse the following retrieved document context to answer the user's question. "
                "If the answer is not in the context, state clearly that the document does not contain this information.\n\n"
                f"--- DOCUMENT CONTEXT ---\n{context}\n------------------------"
            )
    messages_payload = [{"role": "system", "content": system_prompt}] + chat_history

    data = {
        "model": model,
        "messages": messages_payload

    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()

        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"