# nt-telegram-bot

Oddiy va minimal telegram bot uchun Python + requests asosidagi kutubxona.

```python
from telegram.updater import Updater
from telegram.handlers import MessageHandler
from telegram.types import Update
from config import TOKEN
```

`nt-telegram-bot` sizga hech qanday qo‘shimcha murakkabliksiz, tozalangan interfeys orqali Telegram bot yaratish imkonini beradi.

## ⚙️ O‘rnatish

```bash
pip install nt-telegram-bot
```

## 🚀 Boshlang‘ich foydalanish

Quyidagi kod namunasi orqali botni ishga tushiring:

```python
from telegram.updater import Updater
from telegram.handlers import MessageHandler
from telegram.types import Update
from config import TOKEN


def handle_message(update: Update):
    message = update.message

    if message.text:
        if message.text == '/start':
            message.reply_text(
                TOKEN,
                "assalomu alaykum. ECHO BOT"
            )
        else:
            message.reply_text(TOKEN, message.text)
    elif message.contact:
        pass
    elif message.photo:
        pass
    elif message.sickter:
        pass


updater = Updater(TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(handle_message))
updater.start_polling()
```

## 📌 Xususiyatlar

* `Updater` yordamida soddalashtirilgan polling
* `MessageHandler` orqali barcha turdagi xabarlarni tutib olish
* `Update` obyektiga qulay kirish

## 📣 Hissa qo‘shish

Pull request’lar mamnuniyat bilan qabul qilinadi.
Agar xatolik topsangiz — Issue qoldiring.

## 📄 Litsenziya

MIT
