from telebot import types


from database.core import *


def vegans_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_list = []
    for vegans in Vegans.select():
        button_list.append(vegans.product_name)
    for name in button_list:
        button = types.KeyboardButton(text=name)
        keyboard.add(button)

    return keyboard
