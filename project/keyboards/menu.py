from aiogram import types

from project.services import get_questions_in_category, list_categories
from project.utils import BACK_TO_MENU_TEXT, OPEN_SEARCH


def get_main_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for category in list_categories():
        button = types.KeyboardButton(category.name)
        keyboard.add(button)

    open_search_button = types.KeyboardButton(OPEN_SEARCH)
    keyboard.add(open_search_button)
    return keyboard


def get_keyboard_by_category_text_or_404(category_name: str):
    if category_name not in [category.name for category in list_categories()]:  # TODO
        return
    return get_keyboard_by_category_text(category_name)


def get_keyboard_by_category_text(category_name: str):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back_to_menu_button = types.KeyboardButton(BACK_TO_MENU_TEXT)
    keyboard.add(back_to_menu_button)
    categories = get_questions_in_category(category_name)
    if len(categories) == 0:
        pass  # TODO
    for question in get_questions_in_category(category_name):
        button = types.KeyboardButton(question.text)
        keyboard.add(button)

    return keyboard
