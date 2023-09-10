from telebot.types import Message

from loader import bot


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    bot.send_message(message.from_user.id, f"""
    Привіт, {message.from_user.full_name}!\n
    Я - телеграм бот, який допоможе тобі вивчити терміни зберігання продукції.
    \nЩоб вивести список усіх моїх команд, введи /help """)
