from aiogram import Dispatcher

from project.handlers.menu_keyboard import Menu
from project.utils import BACK_TO_SEARCH_RESULT, OPEN_SEARCH, TRY_SEARCH_AGAIN

from .keyboard import (Search, entry, handle_after_get_question, handle_back_to_search_again,
                       handle_invalid_after_get_question, handle_invalid_not_found_option, handle_query,
                       handle_question)


def setup(dp: Dispatcher):
    dp.register_message_handler(entry, lambda message: message.text == OPEN_SEARCH, state=Menu.wait_for_category)
    dp.register_message_handler(handle_query, state=Search.wait_for_query)
    dp.register_message_handler(handle_question, state=Search.wait_for_question)
    dp.register_message_handler(handle_back_to_search_again, lambda message: message.text == TRY_SEARCH_AGAIN, state=Search.after_not_found)
    dp.register_message_handler(handle_invalid_not_found_option, state=Search.after_not_found)
    dp.register_message_handler(handle_after_get_question, lambda message: message.text == BACK_TO_SEARCH_RESULT, state=Search.after_get_question)
    dp.register_message_handler(handle_invalid_after_get_question, state=Search.after_get_question)
