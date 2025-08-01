from .types import Update

class MessageHandler:

    def __init__(self, callback: callable):
        self.callback = callback

    def check_update(self, update: Update):
        return update.message is not None
