import requests


# === Chat Function ===
def get_ai_response(user_input, chat_history, api_key, model, api_url):
    # chat_history.append({"role": "user", "content": user_input})

    headers = {
        "Authorization": f"Bearer {api_key}",  # TODO: Use your API key
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": chat_history
    }

    try:
        # Send the POST request to the Groq API
        response = requests.post(api_url, headers=headers, json=data)  # TODO: Complete this line
        response.raise_for_status()  # Ensure no HTTP errors
        result = response.json()  # TODO: Extract JSON content

        return result["choices"][0]["message"]["content"]  # TODO: Get AI's message
    except Exception as e:
        return f"Error: {e}"