from telebot.types import Message

from loader import bot
from keyboards.reply.command_list import commands_markup


@bot.message_handler(commands=['help'])
def bot_start(message: Message):
    bot.send_message(message.chat.id, "Виберіть потрібну команду:", reply_markup=commands_markup())
