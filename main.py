import os
import asyncio
import requests
from telegram import Bot

async def main():
    print("STARTING BOT...")

    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
    CHAT_ID = os.environ.get("CHAT_ID")
    OURA_TOKEN = os.environ.get("OURA_TOKEN")

    # Проверка переменных
    if not TELEGRAM_TOKEN or not CHAT_ID or not OURA_TOKEN:
        print("❌ Missing env variables")
        return

    bot = Bot(token=TELEGRAM_TOKEN)

    try:
        url = "https://api.ouraring.com/v2/usercollection/sleep"

        headers = {
            "Authorization": f"Bearer {OURA_TOKEN}"
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        print("OURA RESPONSE:", data)

        # Если нет данных
        if "data" not in data or len(data["data"]) == 0:
            await bot.send_message(
                chat_id=CHAT_ID,
                text="😴 Нет данных сна за сегодня"
            )
            return

        sleep = data["data"][0]

        # Безопасно достаём данные
        score = sleep.get("score", "N/A")
        duration = sleep.get("total_sleep_duration", 0)

        # Переводим секунды в часы
        hours = round(duration / 3600, 1) if duration else "N/A"

        message = f"""
💤 Sleep Report

Score: {score}
Duration: {hours}h
"""

        await bot.send_message(chat_id=CHAT_ID, text=message)

        print("✅ MESSAGE SENT")

    except Exception as e:
        print("❌ ERROR:", str(e))

        await bot.send_message(
            chat_id=CHAT_ID,
            text=f"Ошибка: {str(e)}"
        )

asyncio.run(main())
