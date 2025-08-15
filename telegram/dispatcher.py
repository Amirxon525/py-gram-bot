from .types import Update


class Dispatcher:

    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        if handler not in self.handlers:
            self.handlers.append(handler)

    def process_update(self, update: Update):
        for handler in self.handlers:
            if handler.check_update(update):
                handler.callback(update)
                break
