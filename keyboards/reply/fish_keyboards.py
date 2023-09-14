from telebot import types


from database.core import *


def fish_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_list = []
    for fish in Fish.select():
        button_list.append(fish.product_name)
    for name in button_list:
        button = types.KeyboardButton(text=name)
        keyboard.add(button)

    return keyboard
