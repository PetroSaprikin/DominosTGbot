from telebot import types


from database.core import *


def meat_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_list = []
    for meat in Meat.select():
        button_list.append(meat.product_name)
    for name in button_list:
        button = types.KeyboardButton(text=name)
        keyboard.add(button)

    return keyboard
