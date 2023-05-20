# myapp/telegram.py
from telegram import Bot
from django.conf import settings



def send_telegram_message(text):
    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
    bot.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text=text)


async def some_function():
    # ...

    await send_telegram_message("Привет, мир!")