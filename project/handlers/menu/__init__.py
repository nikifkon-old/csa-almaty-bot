from aiogram import Dispatcher

from project.handlers.search import entry as search_entry
from project.utils import BACK_TO_MENU_TEXT, OPEN_SEARCH

from .menu import Menu, back_to_menu, entry, handle_category, handle_question  # noqa


def setup(dp: Dispatcher):
    dp.register_message_handler(search_entry, lambda message: message.text == OPEN_SEARCH, state=Menu.wait_for_category)
    dp.register_message_handler(back_to_menu, lambda message: message.text == BACK_TO_MENU_TEXT, state="*")
    dp.register_message_handler(handle_category, state=Menu.wait_for_category)
    dp.register_message_handler(handle_question, state=Menu.wait_for_question)
