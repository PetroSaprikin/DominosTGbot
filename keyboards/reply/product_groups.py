from telebot import types

group_names = (
    ("Сири🧀", "Cheese"),
    ("Риба🐟", "Fish"),
    ("М'ясо🥩", "Meat"),
    ("Інше🥔", "Significant_other"),
    ("Соуси🍅", "Souses"),
    ("Овочі🌽", "Vegans")
)


def product_group_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    buttons = [types.KeyboardButton(text=ukr_name) for ukr_name, _ in group_names]

    row_length = 3  # Количество кнопок в каждом ряду
    for i in range(0, len(buttons), row_length):
        keyboard.row(*buttons[i:i + row_length])

    return keyboard

