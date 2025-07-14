from fpdf import FPDF
import json

# Загружаем данные (можно заменить на URL, как в schedule.py)
with open("schedule.json", "r", encoding="utf-8") as f:
    schedule = json.load(f)

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Гимнастика для позвоночника", 0, 1, "C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "", 8)
        self.cell(0, 10, f"Страница {self.page_no()}", 0, 0, "C")

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Добавляем дни
for day, data in schedule.items():
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, day, ln=True, align="C")
    
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 10, f"🕐 Время: {data['time']}", ln=True)
    pdf.multi_cell(0, 10, data['text'])
    pdf.ln(10)

pdf.output("Гимнастика_по_дням.pdf")
print("✅ PDF создан: Гимнастика_по_дням.pdf")
