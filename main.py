if "data" not in data or len(data["data"]) == 0:
    await bot.send_message(chat_id=CHAT_ID, text="Нет данных сна 😴")
    return

sleep = data["data"][0]

score = sleep.get("score", "N/A")
hr = sleep.get("average_heart_rate", "N/A")

message = f"""
Sleep report 💤

Score: {score}
Avg HR: {hr}
"""

await bot.send_message(chat_id=CHAT_ID, text=message)
