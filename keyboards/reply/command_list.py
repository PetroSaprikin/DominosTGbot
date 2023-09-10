from telebot import types

from config_data.config import DEFAULT_COMMANDS


def commands_markup():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for command, description in DEFAULT_COMMANDS:
        button = types.KeyboardButton(text=description)
        keyboard.add(button)
    return keyboard
