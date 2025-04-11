import datetime
import json
import requests
import os
# === Telegram настройки ===
TOKEN = "7836254185:AAE-qjm_NYrsq6lNyIRH1laKdyWZEcnFZ8g"
CHAT_ID = "1782079404"
TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# === Ссылка на JSON с расписанием ===
SCHEDULE_URL = "https://raw.githubusercontent.com/Laodzhan79/exercise-schedule/refs/heads/main/schedule.json?token=GHSAT0AAAAAADCCZEFSMVAKNRXRJGHPQIMIZ7ZPCZA"

# === Загружаем расписание ===
try:
    response = requests.get(SCHEDULE_URL)
    schedule = response.json()
except Exception as e:
    message = f"Ошибка загрузки расписания: {e}"
    requests.post(TELEGRAM_API, data={"chat_id": CHAT_ID, "text": message})
    raise SystemExit()

# === Определяем текущий день недели ===
today = datetime.datetime.today().strftime("%A")
day_data = schedule.get(today)

# === Отправляем сообщение в Telegram ===
if day_data:
    message = f"🏋️ Упражнения на {today} ({day_data['time']}):\n\n{day_data['text']}"
else:
    message = f"Сегодня ({today}) упражнений не запланировано. Отдыхай ✨"

requests.post(TELEGRAM_API, data={"chat_id": CHAT_ID, "text": message})