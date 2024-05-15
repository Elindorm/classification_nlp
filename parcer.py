import time
from pyrogram import Client

def get_api_credentials():
    api_id = 0000
    api_hash = " "
    return api_id, api_hash

def parse_messages(channel_name, limit, app):
    """
    Функция для парсинга сообщений из указанного канала Telegram.
    """
    try:
        channel = app.get_chat(channel_name)
        messages = app.get_chat_history(channel.id, limit=limit)
        return messages
    except Exception as e:
        print(f"Ошибка при получении сообщений: {e}")
        return None

def save_messages_to_file(messages, output_file_name):
    if messages:
        try:
            with open(output_file_name, 'w', encoding='utf-8') as file:
                for i, message in enumerate(messages):
                    try:
                        file.write(f"{i}_\n")
                        if message.caption:
                            file.write(f"{message.caption}\n")
                        elif message.text:
                            file.write(f"{message.text}\n")
                    except Exception as e:
                        print(f"Ошибка при сохранении сообщения: {e}")
        except Exception as e:
            print(f"Ошибка при открытии файла для записи: {e}")
    else:
        print("Нет сообщений для сохранения.")

def main():
    try:
        api_id, api_hash = get_api_credentials()
        app = Client('session', api_id, api_hash)  
        app.start() 
        
        channel_name = input("Введите название канала Telegram: ")
        limit = int(input("Сколько сообщений вы хотите загрузить? "))
        output_file_name = input("Введите название файла для сохранения: ") + '.txt'

        messages = parse_messages(channel_name, limit, app)
        if messages:
            save_messages_to_file(messages, output_file_name)
            print("Сообщения успешно сохранены.")
        
        app.stop()  
    except KeyboardInterrupt:
        print("Процесс прерван пользователем.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == '__main__':
    main()
