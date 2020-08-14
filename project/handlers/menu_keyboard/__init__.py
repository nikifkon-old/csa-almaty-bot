from aiogram import Dispatcher
from .menu import Menu, entry, choose_category, choose_question  # noqa


def setup(dp: Dispatcher):
    dp.register_message_handler(choose_category, state=Menu.wait_for_category)
    dp.register_message_handler(choose_question, state=Menu.wait_for_question)
