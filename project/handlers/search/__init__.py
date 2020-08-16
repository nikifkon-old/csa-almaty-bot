from aiogram import Dispatcher

from project.utils import BACK_TO_SEARCH_RESULT, TRY_SEARCH_AGAIN

from .keyboard import (Search, back_to_search, back_to_search_again, entry,  # noqa
                       handle_invalid_after_get_question_option, handle_invalid_not_found_option, handle_query,
                       handle_question)


def setup(dp: Dispatcher):
    dp.register_message_handler(handle_query, state=Search.wait_for_query)

    dp.register_message_handler(back_to_search_again, lambda message: message.text == TRY_SEARCH_AGAIN, state=Search.wait_for_question)
    dp.register_message_handler(handle_question, state=Search.wait_for_question)

    dp.register_message_handler(back_to_search_again, lambda message: message.text == TRY_SEARCH_AGAIN, state=Search.after_not_found)
    # dp.register_message_handler(handle_invalid_not_found_option, state=Search.after_not_found)

    dp.register_message_handler(back_to_search, lambda message: message.text == BACK_TO_SEARCH_RESULT, state=Search.after_get_question)
    # dp.register_message_handler(handle_invalid_after_get_question_option, state=Search.after_get_question)
    dp.register_message_handler(handle_query, state=Search.all())
