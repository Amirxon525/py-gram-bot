from .types import Update


class MessageHandler:

    def __init__(self, callback):
        self.callback = callback

    def check_update(self, update: Update) -> bool:
        return update.message is not None
