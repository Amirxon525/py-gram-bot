import requests


class User:

    def __init__(
            self, 
            id: int, 
            first_name: str, 
            username: str | None
        ):
        self.id = id
        self.first_name = first_name
        self.username = username


class Message:

    def __init__(
            self,
            message_id: int,
            from_user: User,
            text: str | None = None,
            contact: None = None,
            photo: None = None,
            sickter: None = None,
        ):
        self.message_id = message_id
        self.from_user = from_user
        self.text = text
        self.contact = contact
        self.photo = photo
        self.sickter = sickter

    def reply_text(self, token: str, text: str):
        params = {
            'chat_id': self.from_user.id,
            'text': text
        }
        requests.get(f"https://api.telegram.org/bot{token}/sendMessage", params=params)


class Update:

    def __init__(
            self,
            update_id: int, 
            message: Message | None = None,
            edited_message: Message | None = None,
        ) -> None:
        self.update_id = update_id
        self.message = message
        self.edited_message = edited_message
