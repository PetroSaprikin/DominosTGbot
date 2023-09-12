from telebot.types import Message

from loader import bot


group_names = [
    {"Сири": "cheese"},
    {"Риба": "fish"},
    {"М'ясо": "meat"},
    {"Інше": "significant_other"},
    {"Соуси": "souses"},
    {"Овочі": "vegans"}
]


@bot.message_handler(commands=["product"])
def product(message: Message):
    pass

# todo сделать ф-цию для поиска продуктов
