# nt_pygrambot

A lightweight and easy-to-use Python Telegram Bot wrapper library.

## Features

- Simple polling-based Telegram bot
- Easy message handling
- Structured and modular code
- Clean API to extend your bot's functionality

## Installation

You can install the library via pip:

```bash
pip install nt_pygrambot
````

## Quick Start

Here's a basic example of how to use `nt_pygrambot`:

```python
# Echo Bot Example With nt_pygrambot

from nt_pygrambot.updater import Updater
from nt_pygrambot.handlers import MessageHandler
from nt_pygrambot.types import Update


def handle_message(update: Update):
    if update.message.text:
        update.message.reply_text(update.message.text)


updater = Updater("TOKEN")
updater.dispatcher.add_handler(MessageHandler(handle_message))

updater.start_polling()
```

## Requirements

* Python >= 3.9

## Documentation

More documentation and usage examples will be available soon.

For now, you can explore the source code and basic examples in the [GitHub repository](https://github.com/ziyocamp/py-gram-bot/pygrambot).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.

```
