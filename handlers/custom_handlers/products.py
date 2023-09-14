from telebot.types import Message

from loader import bot
from states.product_states import ProductState
from keyboards.reply.product_groups import product_group_keyboard
from keyboards.reply.product_groups import group_names
from keyboards.reply.souses_keyboard import souses_keyboard
from keyboards.reply.cheese_keyboard import chesee_keyboard
from keyboards.reply.fish_keyboards import fish_keyboard
from keyboards.reply.meat_keyboard import meat_keyboard
from keyboards.reply.significant_other import significant_other_keyboard
from keyboards.reply.vegans_keyboard import vegans_keyboard
from handlers.working_func.product_resole_result import product_resolve_result
from database.core import *


@bot.message_handler(commands=["product"])
def product_group_select(message: Message):
    bot.set_state(message.from_user.id, ProductState.get_product, message.chat.id)
    bot.send_message(message.from_user.id, "Виберіть потрібну категорію продуктів",
                     reply_markup=product_group_keyboard())


@bot.message_handler(state=ProductState.get_product)
def product_select(message: Message):
    group = message.text
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["group_ukr"] = [ukr for ukr, _ in group_names]
        if group in data["group_ukr"]:
            for _, selected_group in group_names:
                if _ == group:
                    data["selected_group"] = selected_group
            bot.set_state(message.from_user.id, ProductState.resolve_results, message.chat.id)
            if data["selected_group"] == "Souses":
                bot.send_message(message.from_user.id, "Теперь виберіть потрібний продукт: ",
                                 reply_markup=souses_keyboard())
            elif data["selected_group"] == "Cheese":
                bot.send_message(message.from_user.id, "Теперь виберіть потрібний продукт: ",
                                 reply_markup=chesee_keyboard())
            elif data["selected_group"] == "Fish":
                bot.send_message(message.from_user.id, "Теперь виберіть потрібний продукт: ",
                                 reply_markup=fish_keyboard())
            elif data["selected_group"] == "Meat":
                bot.send_message(message.from_user.id, "Теперь виберіть потрібний продукт: ",
                                 reply_markup=meat_keyboard())
            elif data["selected_group"] == "Significant_other":
                bot.send_message(message.from_user.id, "Теперь виберіть потрібний продукт: ",
                                 reply_markup=significant_other_keyboard())
            elif data["selected_group"] == "Vegans":
                bot.send_message(message.from_user.id, "Теперь виберіть потрібний продукт: ",
                                 reply_markup=vegans_keyboard())
        else:
            bot.send_message(message.from_user.id, "Виберіть продукти із списку!")


@bot.message_handler(state=ProductState.resolve_results)
def result(message: Message):
    bot.send_message(message.from_user.id, "ok")
    answer = message.text
    bot.set_state(message.from_user.id, None, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["answer"] = answer
        if data["selected_group"] == "Souses":
            final_result = product_resolve_result(Souses, data["answer"])
            bot.send_message(message.from_user.id, final_result)
        elif data["selected_group"] == "Cheese":
            final_result = product_resolve_result(Cheese, data["answer"])
            bot.send_message(message.from_user.id, final_result)
        elif data["selected_group"] == "Fish":
            final_result = product_resolve_result(Fish, data["answer"])
            bot.send_message(message.from_user.id, final_result)
        elif data["selected_group"] == "Meat":
            final_result = product_resolve_result(Meat, data["answer"])
            bot.send_message(message.from_user.id, final_result)
        elif data["selected_group"] == "Significant_other":
            final_result = product_resolve_result(Significant_other, data["answer"])
            bot.send_message(message.from_user.id, final_result)
        elif data["selected_group"] == "Vegans":
            final_result = product_resolve_result(Vegans, data["answer"])
            bot.send_message(message.from_user.id, final_result)
