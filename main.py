import os
import asyncio
import requests
from telegram import Bot

async def main():
    print("STARTING BOT...")

    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
    CHAT_ID = os.environ.get("CHAT_ID")
    OURA_TOKEN = os.environ.get("OURA_TOKEN")

    bot = Bot(token=TELEGRAM_TOKEN)

    url = "https://api.ouraring.com/v2/usercollection/sleep"

    headers = {
        "Authorization": f"Bearer {OURA_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    sleep = data["data"][0]

    score = sleep["score"]

    message = f"""
Sleep report 💤

Score: {score}
"""

    await bot.send_message(chat_id=CHAT_ID, text=message)

asyncio.run(main())
