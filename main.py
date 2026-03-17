import os
import asyncio
from telegram import Bot

async def main():
    print("STARTING BOT...")

    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
    CHAT_ID = os.environ.get("CHAT_ID")

    print("TOKEN:", TELEGRAM_TOKEN)
    print("CHAT_ID:", CHAT_ID)

    bot = Bot(token=TELEGRAM_TOKEN)

    await bot.send_message(chat_id=CHAT_ID, text="Бот работает 🚀")

    print("MESSAGE SENT")

asyncio.run(main())
