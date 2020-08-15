from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from project.keyboards import get_keyboard_by_category_text_or_404, get_main_menu_keyboard
from project.services import get_question_or_404


class Menu(StatesGroup):  # TODO: Move to another folder
    wait_for_category = State()  # When user in main menu
    wait_for_question = State()  # Whne user choose questions


async def back_to_menu(message: types.Message):
    """
    When user click to the button with text: ~project.utils.BACK_TO_MENU_TEXT
    """
    await Menu.first()
    keyboard = get_main_menu_keyboard()
    await message.reply("Возврашаю в главное меню", reply_markup=keyboard)


async def entry(message: types.Message):
    """
    Entry point for menu module. Now this is entry for whole app
    """
    await ask_category(message)


# wait_for_category
async def handle_category(message: types.Message, state: FSMContext):
    """
    When user choose category from main menu
    """
    keyboard = get_keyboard_by_category_text_or_404(message.text)
    if keyboard is None:
        return await invalid_category(message)
    await state.update_data(category=message.text)

    return await ask_question(message, keyboard=keyboard)


async def ask_category(message: types.Message):
    """
    Ask user to click button on main menu keyboard
    """
    keyboard = get_main_menu_keyboard()
    await message.answer("Выберите категорию, используя клавиатуру ниже.", reply_markup=keyboard)
    await Menu.wait_for_category.set()


async def invalid_category(message: types.Message):
    """
    When user typed category that does not exist
    """
    await message.reply("Такой категории не существует", reply_markup=None)
    return await ask_category(message)


# wait_for_question
async def handle_question(message: types.Message, state: FSMContext):
    """
    When user choose question in keyboard: ~project.keyboard.get_keyboard_by_category_text
    """
    question = get_question_or_404(message.text)
    if question is None:
        return await invalid_question(message, state=state)
    await message.reply(question.answer)

    return await ask_category(message)


async def ask_question(message: types.Message, keyboard):
    """
    Ask user to click button on keyboard: ~project.keyboard.get_keyboard_by_category_text
    """
    await message.answer("Выберите вопрос, используя клавиатуру ниже.", reply_markup=keyboard)
    await Menu.wait_for_question.set()


async def invalid_question(message: types.Message, state: FSMContext):
    """
    When user typed invalid question
    """
    data = await state.get_data()
    try:
        category = data["category"]
    except KeyError:
        await Menu.wait_for_category.set()

    keyboard = get_keyboard_by_category_text_or_404(category)
    await message.reply("Такого вопроса не существует", reply_markup=None)

    return await ask_question(message, keyboard=keyboard)
