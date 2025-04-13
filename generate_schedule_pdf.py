from fpdf import FPDF
import json

# Загружаем файл schedule.json (можно заменить на ссылку)
with open("schedule.json", "r", encoding="utf-8") as f:
    schedule = json.load(f)

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.set_text_color(0)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "", 8)
        self.cell(0, 10, f"Страница {self.page_no()}", 0, 0, "C")

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)
pdf.set_fill_color(255, 255, 255)
pdf.set_text_color(0, 0, 0)

# Добавляем по 1 дню на страницу
for day, data in schedule.items():
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, day, ln=True, align="C")
    
    pdf.set_font("Arial", "", 12)
    pdf.ln(5)
    pdf.cell(0, 10, f"🕐 Время: {data['time']}", ln=True)

    pdf.ln(5)
    for exercise in data['exercises']:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, exercise['name'], ln=True)
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 10, exercise['description'])
        pdf.ln(2)

    pdf.ln(5)
    pdf.cell(0, 10, "[  ] Выполнено ✅", ln=True)

# Добавим памятку
pdf.add_page()
pdf.set_font("Arial", "B", 14)
pdf.cell(0, 10, "📌 Как пользоваться PDF", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 10,
    "• Распечатай или открой на телефоне.\n"
    "• Смотри упражнения на каждый день.\n"
    "• Выполняй их в назначенное время.\n"
    "• Отмечай галочкой выполнение.\n"
    "• Напоминания можно получать в Telegram автоматически."
)

# Сохраняем
pdf.output("Гимнастика_по_дням.pdf")
print("✅ PDF создан: Гимнастика_по_дням.pdf")
