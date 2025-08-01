import time
import requests

from .types import Update
from .dispatcher import Dispatcher


class Updater:

    def __init__(self, token):
        self.token = token
        self.dispatcher = Dispatcher()
        self.offset = 0

    def get_udpates(self):
        payload = {
            'offset': self.offset
        }
        url = f'https://api.telegram.org/bot{self.token}/getUpdates'
        r = requests.get(url=url, params=payload)

        updates: list[Update] = []
        for row_update in r.json()['result']:
            updates.append(Update(
                update_id=row_update['update_id'],
                message=row_update.get('message'),
            ))

        return updates

    def start_polling(self):
        
        while True:
            for update in self.get_udpates():
                self.offset = update.update_id + 1
                self.dispatcher.process_update(update)

            time.sleep(1)
