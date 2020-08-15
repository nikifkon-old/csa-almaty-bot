from aiogram import Dispatcher
from .menu import Menu, entry, handle_category, handle_question  # noqa


def setup(dp: Dispatcher):
    dp.register_message_handler(handle_category, state=Menu.wait_for_category)
    dp.register_message_handler(handle_question, state=Menu.wait_for_question)
