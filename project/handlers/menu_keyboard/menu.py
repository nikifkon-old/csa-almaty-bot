from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from project.bot import dp
from project.keyboards import get_main_menu_keyboard, get_keyboard_by_category_text_or_404
from project.services import get_question_or_404
from project.utils import BACK_TO_MENU_TEXT


class Menu(StatesGroup):
    wait_for_category = State()
    wait_for_question = State()


@dp.message_handler(lambda message: message.text == BACK_TO_MENU_TEXT, state="*")
async def bot_cancel(message: types.Message):
    """
    BACK_TO_MENU_TEXT handler
    """
    await Menu.first()
    keyboard = get_main_menu_keyboard()
    await message.reply("Возврашаю в главное меню", reply_markup=keyboard)


async def entry(message: types.Message):
    await ask_category(message)


# wait_for_category
async def handle_category(message: types.Message, state: FSMContext):
    keyboard = get_keyboard_by_category_text_or_404(message.text)
    if keyboard is None:
        return await invalid_category(message)
    await state.update_data(category=message.text)

    return await ask_question(message, keyboard=keyboard)


async def ask_category(message: types.Message):
    keyboard = get_main_menu_keyboard()
    await message.answer("Пожалуйста, выберите категорию, используя клавиатуру ниже.", reply_markup=keyboard)
    await Menu.wait_for_category.set()


async def invalid_category(message: types.Message):
    await message.reply("Такой категории не существует", reply_markup=None)
    return await ask_category(message)


# wait_for_question
async def handle_question(message: types.Message, state: FSMContext):
    question = get_question_or_404(message.text)
    if question is None:
        return await invalid_question(message, state=state)
    await message.reply(question.answer)

    return await ask_category(message)


async def ask_question(message: types.Message, keyboard):
    await message.answer("Пожалуйста, выберите вопрос, используя клавиатуру ниже.", reply_markup=keyboard)
    await Menu.wait_for_question.set()


async def invalid_question(message: types.Message, state: FSMContext):
    data = await state.get_data()
    try:
        category = data["category"]
    except KeyError:
        await Menu.wait_for_category.set()

    keyboard = get_keyboard_by_category_text_or_404(category)
    await message.reply("Такого вопроса не существует", reply_markup=None)

    return await ask_question(message, keyboard=keyboard)
