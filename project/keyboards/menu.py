from aiogram import types
from project.services import list_categories, get_questions_in_category
from project.utils import BACK_TO_MENU_TEXT


def get_main_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for category in list_categories():
        button = types.KeyboardButton(category.name)
        keyboard.add(button)

    return keyboard


def get_keyboard_by_category_text_or_404(category_name: str):
    if category_name not in [category.name for category in list_categories()]:  # TODO
        return
    return get_keyboard_by_category_text(category_name)


def get_keyboard_by_category_text(category_name: str):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    categories = get_questions_in_category(category_name)
    if len(categories) == 0:
        pass  # TODO
    for question in get_questions_in_category(category_name):
        button = types.KeyboardButton(question.text)
        keyboard.row(button)

    back_to_menu_button = types.KeyboardButton(BACK_TO_MENU_TEXT)
    keyboard.add(back_to_menu_button)
    return keyboard
