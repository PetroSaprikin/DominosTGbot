from telebot.types import Message

from loader import bot
from config_data.config import DEFAULT_COMMANDS


@bot.message_handler(commands=['help'])
def bot_start(message: Message):
    text = ""
    for command, description in DEFAULT_COMMANDS:
        text += f"{description}: /{command}\n"
    bot.send_message(message.chat.id, f"Виберіть потрібну команду:\n{text}")
