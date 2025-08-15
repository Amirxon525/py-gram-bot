from telegram.updater import Updater
from telegram.handlers import MessageHandler
from telegram.types import Update
from config import TOKEN


def handle_message(update: Update):
    message = update.message

    if message.text:
        if message.text == '/start':
            message.reply_text("assalomu alaykum. ECHO BOT")
        else:
            message.reply_text(message.text)
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
