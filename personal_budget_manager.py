import json
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime

# Bot tokeningizni shu joyga qo'ying
TOKEN = "7871756285:AAGbnZbCH0mYz1eFS9EX99Ii6I9-LEXNkAc"
bot = telebot.TeleBot(TOKEN)

class BudgetManager:
    """Budjet boshqaruvchi klass"""
    def __init__(self, balance, data):
        self.balance = balance
        self.data = data if data else {}

    def incomef(self, amount):
        """Daromad qo'shish"""
        if isinstance(amount, int):
            self.balance += amount
            date = datetime.now().strftime("%d.%m.%y")
            if date not in self.data:
                self.data[date] = []
            self.data[date].append({"type": "+", "amount": amount})
            self.write_base()
            return f"{amount}$ daromad qo'shildi!"
        return "Xatolik: Miqdor butun son bo‘lishi kerak!"

    def expenses(self, amount):
        """Xarajat qo'shish"""
        if isinstance(amount, int):
            if amount <= self.balance:
                self.balance -= amount
                date = datetime.now().strftime("%d.%m.%y")
                if date not in self.data:
                    self.data[date] = []
                self.data[date].append({"type": "-", "amount": amount})
                self.write_base()
                return f"{amount}$ xarajat qilindi!"
            return "Xatolik: Balans yetarli emas!"
        return "Xatolik: Miqdor butun son bo‘lishi kerak!"

    def balances(self):
        """Balansni ko‘rsatish"""
        return f"Hozirgi balansingiz: {self.balance}$"

    def write_base(self):
        """JSON faylga yozish"""
        with open("Data_finance.json", "w") as file:
            json.dump(self.data, file, indent=4)

    def read_base(self):
        """JSON fayldan o'qish"""
        try:
            with open("Data_finance.json", "r") as file:
                data = json.load(file)
            return json.dumps(data, indent=4)
        except FileNotFoundError:
            return "Ma’lumotlar topilmadi!"

    def __clear_base(self, secret_code):
        """Maxsus kod orqali bazani tozalash (inkapsulyatsiya)"""
        if secret_code == "dvv112":
            self.data = {}
            self.balance = 0
            self.write_base()
            return "Baza muvaffaqiyatli tozalandi!"
        return "Noto‘g‘ri kod!"

# Budjet obyektini yaratish
budget = BudgetManager(balance=0, data={})

# 🔘 Menyu tugmalari
def main_menu():
    markup = InlineKeyboardMarkup()
    markup.row(
        InlineKeyboardButton("💰 Daromad qo‘shish", callback_data="add_income"),
        InlineKeyboardButton("💸 Xarajat qo‘shish", callback_data="add_expense")
    )
    markup.row(
        InlineKeyboardButton("📊 Balansni ko‘rish", callback_data="show_balance"),
        InlineKeyboardButton("📜 Tarix", callback_data="show_history")
    )
    markup.row(
        InlineKeyboardButton("🗑 Bazani tozalash", callback_data="clear_database")
    )
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "📌 Budjet menejeri botiga xush kelibsiz!\n\nTanlang:", reply_markup=main_menu())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "add_income":
        bot.send_message(call.message.chat.id, "💰 Daromad miqdorini kiriting:")
        bot.register_next_step_handler(call.message, process_income)
    elif call.data == "add_expense":
        bot.send_message(call.message.chat.id, "💸 Xarajat miqdorini kiriting:")
        bot.register_next_step_handler(call.message, process_expense)
    elif call.data == "show_balance":
        bot.send_message(call.message.chat.id, budget.balances())
    elif call.data == "show_history":
        bot.send_message(call.message.chat.id, budget.read_base())
    elif call.data == "clear_database":
        bot.send_message(call.message.chat.id, "🗑 Bazani tozalash uchun maxsus kodni kiriting:")
        bot.register_next_step_handler(call.message, check_clear_code)

def process_income(message):
    try:
        amount = int(message.text)
        response = budget.incomef(amount)
    except ValueError:
        response = "Xatolik: Raqam kiriting!"
    bot.send_message(message.chat.id, response, reply_markup=main_menu())

def process_expense(message):
    try:
        amount = int(message.text)
        response = budget.expenses(amount)
    except ValueError:
        response = "Xatolik: Raqam kiriting!"
    bot.send_message(message.chat.id, response, reply_markup=main_menu())

def check_clear_code(message):
    result = budget._BudgetManager__clear_base(message.text)  # Inkapsulyatsiya qilingan metodni chaqirish
    bot.send_message(message.chat.id, result, reply_markup=main_menu())

bot.polling()
