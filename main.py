import os
from telegram import Bot

print("STARTING BOT...")

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

print("TOKEN:", TELEGRAM_TOKEN)
print("CHAT_ID:", CHAT_ID)

bot = Bot(token=TELEGRAM_TOKEN)

bot.send_message(chat_id=CHAT_ID, text="Бот работает 🚀")

print("MESSAGE SENT")
