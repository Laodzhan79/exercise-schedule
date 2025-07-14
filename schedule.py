import datetime
import json
import requests

# === Telegram настройки ===
TOKEN = "7836254185:AAE-qjm_NYrsq6lNyIRH1laKdyWZEcnFZ8g"  # Замени на свой токен!
CHAT_ID = "1782079404"  # Замени на свой chat_id!
TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# === Ссылка на JSON с расписанием ===
SCHEDULE_URL = "https://raw.githubusercontent.com/Laodzhan79/exercise-schedule/refs/heads/main/schedule.json?token=GHSAT0AAAAAADCH4VWA64DB34SOGPSYOKAO2DUU4OA"  # Убедись, что путь верный!

# === Загружаем расписание ===
try:
    response = requests.get(SCHEDULE_URL)
    response.raise_for_status()  # Проверка HTTP-ошибок
    schedule = response.json()
except Exception as e:
    message = f"❌ Ошибка загрузки расписания:\n{e}\n\nПроверь:\n1. Ссылку: {SCHEDULE_URL}\n2. Формат JSON"
    requests.post(TELEGRAM_API, data={"chat_id": CHAT_ID, "text": message})
    raise SystemExit()

# === Определяем текущий день недели ===
today = datetime.datetime.today().strftime("%A")
day_data = schedule.get(today)

# === Формируем и отправляем сообщение ===
if day_data:
    message = f"🏋️ Упражнения на {today} ({day_data['time']}):\n\n{day_data['text']}"
else:
    message = f"Сегодня ({today}) упражнений не запланировано. Отдыхай ✨"

requests.post(TELEGRAM_API, data={"chat_id": CHAT_ID, "text": message})
