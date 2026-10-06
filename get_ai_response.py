import requests


def get_ai_response(user_input, chat_history, api_key, model, api_url):

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": chat_history
    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()

        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"