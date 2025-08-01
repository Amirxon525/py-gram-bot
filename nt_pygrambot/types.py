import requests
from config import TOKEN


class Update:

    def __init__(self, update_id: int, message: dict | None = None):
        self.update_id = update_id
        self.message = Message(
            message_id=message['message_id'],
            from_user=message['from'],
            text=message.get('text'),
        )


class Message:

    def __init__(self, message_id: int, from_user: dict, text: str | None = None):
        self.message_id = message_id
        self.from_user = User(from_user['id'])
        self.text = text

    def reply_text(self, text):
        payload = {
            'chat_id': self.from_user.chat_id,
            'text': text
        }
        url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
        requests.get(url=url, params=payload)


class User:

    def __init__(self, chat_id: int):
        self.chat_id = chat_id
    