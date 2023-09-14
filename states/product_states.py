from telebot.handler_backends import State, StatesGroup


class ProductState(StatesGroup):

    get_product = State()
    resolve_results = State()
