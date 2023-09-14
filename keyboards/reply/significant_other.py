from telebot import types


from database.core import *


def significant_other_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_list = []
    for significant_other in Significant_other.select():
        button_list.append(significant_other.product_name)
    for name in button_list:
        button = types.KeyboardButton(text=name)
        keyboard.add(button)

    return keyboard
