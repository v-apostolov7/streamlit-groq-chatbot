import json
import os
from datetime import datetime


def get_user_folder(session_id):
    folder_path = os.path.join("chats", session_id)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)
    return folder_path


def generate_chat_name_from_path(file_path):
    base_name = os.path.basename(file_path)
    file_path_list = base_name.split(".")[0].split("_")
    if len(file_path_list) >= 3:
        return f"{file_path_list[2]} || {file_path_list[1]}"
    return base_name


def get_timestamp_filename_path(session_id):
    user_folder = get_user_folder(session_id)
    time_now = datetime.now()
    string_time_now = time_now.strftime("%Y-%m-%d_%H-%M-%S")
    return os.path.join(user_folder, f"chat_{string_time_now}.json")


def save_chat(chat_history, filename):
    if filename:
        folder = os.path.dirname(filename)
        if folder and not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(chat_history, json_file, ensure_ascii=False, indent=4)


def load_chat(filename):
    if filename and os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as json_file:
            return json.load(json_file)
    return []


def delete_chat(filename):
    if filename and os.path.exists(filename):
        try:
            os.remove(os.path.abspath(filename))
            return "File deleted successfully!"
        except Exception as e:
            return f"Deleting failed because of {e.__class__.__name__}:\n{e}"
    return "File not found"