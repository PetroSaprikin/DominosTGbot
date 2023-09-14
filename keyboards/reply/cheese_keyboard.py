from telebot import types


from database.core import *


def chesee_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_list = []
    for chesse in Cheese.select():
        button_list.append(chesse.product_name)
    for name in button_list:
        button = types.KeyboardButton(text=name)
        keyboard.add(button)

    return keyboard
