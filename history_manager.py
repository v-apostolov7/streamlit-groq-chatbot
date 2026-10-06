import json
import os
from datetime import datetime


def generate_chat_name_from_path(file_path):
    file_path_list = file_path.split('.')[0].split('_')
    return f'{file_path_list[2]} || {file_path_list[1]}'


def get_timestamp_filename_path():
    time_now = datetime.now()
    string_time_now = time_now.strftime('%Y-%m-%d_%H-%M-%S')
    timestamp_file_name = os.path.join(f'chats', f'chat_{string_time_now}.json')
    return timestamp_file_name


def save_chat(chat_history, filename):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(chat_history, json_file, ensure_ascii=False, indent=4)


def load_chat(filename):
    if filename:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as json_file:
                file_content = json.load(json_file)  # Подаваш обекта json_file
                return file_content
    return []


def delete_chat(filename):
    if os.path.exists(filename):
        try:
            file_path = os.path.abspath(filename)
            os.remove(file_path)
            return 'File deleted successfully!'
        except Exception as e:
            return f'Deleting failed because of {e.__class__.__name__}:\n{e}'
    return 'File not found'


def list_available_chats():
    if os.path.exists('chats'):
        list_with_chats = [f for f in os.listdir('chats') if f.endswith('.json')]
        if list_with_chats:
            result = '\n'.join(list_with_chats)
            return result
    else:
        os.mkdir("chats")
    return 'No chats'
