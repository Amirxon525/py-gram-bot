from .types import Update


class Dispatcher:

    def __init__(self):
        pass

    def process_update(self, update: Update):
        print(update.update_id)
