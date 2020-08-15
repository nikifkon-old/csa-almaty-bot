from aiogram import types

from project.services import find_questions
from project.utils import BACK_TO_MENU_TEXT, BACK_TO_SEARCH_RESULT, TRY_SEARCH_AGAIN


def get_search_result_keyboard(query):
    questions = find_questions(query)
    if len(questions) == 0:
        return

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_to_menu_button = types.KeyboardButton(BACK_TO_MENU_TEXT)
    keyboard.add(back_to_menu_button)

    for question in questions:
        button = types.KeyboardButton(question.text)
        keyboard.add(button)

    return keyboard


def get_back_to_searh_result_or_categories_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_to_menu_button = types.KeyboardButton(BACK_TO_MENU_TEXT)
    keyboard.add(back_to_menu_button)
    back_to_search_result_button = types.KeyboardButton(BACK_TO_SEARCH_RESULT)
    keyboard.add(back_to_search_result_button)
    return keyboard


def get_question_not_found_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_to_menu_button = types.KeyboardButton(BACK_TO_MENU_TEXT)
    keyboard.add(back_to_menu_button)
    try_search_again_button = types.KeyboardButton(TRY_SEARCH_AGAIN)
    keyboard.add(try_search_again_button)
    return keyboard
