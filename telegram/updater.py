import time
import requests


class Updater:

    def __init__(self, token: str):
        self.token = token
        self.offset = None

    def get_updates(self):
        params = {
            'offset': self.offset
        }
        response = requests.get(f"https://api.telegram.org/bot{self.token}/getUpdates", params=params)

        return response.json()['result']

    def start_polling(self):

        while True:
            
            updates = self.get_updates()
            for update in updates:

                if 'message' in update and 'text' in update['message']:
                    print(update['message']['from']['first_name'], update['message']['text'])

                self.offset = update['update_id'] + 1

            time.sleep(1)
